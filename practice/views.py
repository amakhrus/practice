import re
from collections import OrderedDict

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from courses.models import Course
from .models import Question, Choice, Attempt
from .diagnostic_data import (
    DIAGNOSTICS, get_diagnostic, correct_index, topic_needs_review, iter_questions,
)


@login_required
def question_detail(request, pk):
    """Show a multiple-choice question and handle the student's answer."""
    question = get_object_or_404(Question, pk=pk, qtype="mcq")
    attempt = None

    if request.method == "POST":
        attempt = Attempt(student=request.user, question=question)
        choice_id = request.POST.get("choice")
        choice = get_object_or_404(Choice, pk=choice_id, question=question)
        _grade_mcq(attempt, question, choice)
        attempt.save()

    return render(
        request,
        "practice/question_detail.html",
        {"question": question, "attempt": attempt},
    )


def _grade_mcq(attempt, question, choice):
    """Fill an MCQ attempt with correctness and local explanatory feedback."""
    attempt.selected_choice = choice
    attempt.is_correct = choice.is_correct
    if question.explanation:
        attempt.ai_feedback = question.explanation
    else:
        correct = question.correct_choice
        if correct:
            attempt.ai_feedback = f"The correct answer is: {correct.text}"
        else:
            attempt.ai_feedback = "No explanation is available for this question yet."


@login_required
def practice_set(request, slug):
    """Show every multiple-choice question in a course; grade locally on submit."""
    course = get_object_or_404(Course, slug=slug)
    questions = list(course.questions.filter(qtype="mcq").prefetch_related("choices"))

    submitted = False
    correct = 0
    mcq_total = len(questions)

    if request.method == "POST":
        submitted = True
        for q in questions:
            q.result = None
            attempt = Attempt(student=request.user, question=q)

            choice_id = request.POST.get(f"q{q.id}")
            choice = Choice.objects.filter(pk=choice_id, question=q).first() if choice_id else None
            if choice:
                _grade_mcq(attempt, q, choice)
                if choice.is_correct:
                    correct += 1
                attempt.save()
                q.result = attempt

    return render(
        request,
        "practice/practice_set.html",
        {
            "course": course,
            "questions": questions,
            "submitted": submitted,
            "correct": correct,
            "mcq_total": mcq_total,
        },
    )


@login_required
def practice_interactive(request, slug):
    """Modern single-question interactive practice interface."""
    course = get_object_or_404(Course, slug=slug)
    questions = list(course.questions.filter(qtype="mcq").prefetch_related("choices"))

    if not questions:
        return render(request, "practice/practice_interactive.html", {
            "course": course,
            "error": "No practice questions available.",
            "questions_count": 0,
        })

    # Get current question index from session or request
    current_index = int(request.GET.get('q', request.session.get(f'practice_{slug}_index', 0)))
    if current_index >= len(questions):
        current_index = 0

    current_question = questions[current_index]
    answered = False
    attempt = None
    is_correct = False

    # Handle answer submission
    if request.method == "POST":
        choice_id = request.POST.get("choice")
        choice = Choice.objects.filter(pk=choice_id, question=current_question).first()

        if choice:
            attempt = Attempt(student=request.user, question=current_question)
            _grade_mcq(attempt, current_question, choice)
            attempt.save()
            answered = True
            is_correct = choice.is_correct

    # Store in session
    request.session[f'practice_{slug}_index'] = current_index

    # Calculate progress percentage
    progress_percent = int((current_index / len(questions)) * 100) if len(questions) > 0 else 0

    # Check whether every question in this course has been attempted at least once
    answered_ids = set(
        Attempt.objects.filter(student=request.user, question__in=questions)
        .values_list("question_id", flat=True)
        .distinct()
    )
    all_question_ids = {q.id for q in questions}
    all_completed = all_question_ids <= answered_ids

    return render(request, "practice/practice_interactive.html", {
        "course": course,
        "current_question": current_question,
        "question_number": current_index + 1,
        "total_questions": len(questions),
        "choices": current_question.choices.all(),
        "answered": answered,
        "attempt": attempt,
        "is_correct": is_correct,
        "current_index": current_index,
        "has_next": current_index < len(questions) - 1,
        "has_previous": current_index > 0,
        "progress_percent": progress_percent,
        "all_completed": all_completed,
    })


@login_required
def practice_results(request, slug):
    """Course-specific results page. Only accessible once every MCQ has been attempted."""
    from django.shortcuts import redirect
    course = get_object_or_404(Course, slug=slug)
    questions = list(course.questions.filter(qtype="mcq").prefetch_related("choices"))

    if not questions:
        return redirect("courses:course_detail", slug=slug)

    # Latest attempt per question (chronological order → later rows overwrite earlier)
    attempts_qs = (
        Attempt.objects
        .filter(student=request.user, question__in=questions)
        .select_related("question", "selected_choice")
        .order_by("created_at")
    )
    latest = {}
    for a in attempts_qs:
        latest[a.question_id] = a

    all_question_ids = {q.id for q in questions}
    if not all_question_ids <= set(latest.keys()):
        return redirect("practice:practice_interactive", slug=slug)

    correct_count = sum(1 for a in latest.values() if a.is_correct)
    score_percent = round(100 * correct_count / len(questions))

    question_results = [
        {"question": q, "attempt": latest.get(q.id)}
        for q in questions
    ]

    return render(request, "practice/practice_results.html", {
        "course": course,
        "question_results": question_results,
        "correct": correct_count,
        "total": len(questions),
        "score_percent": score_percent,
    })


@login_required
def written_set(request, slug):
    """Written-response practice: the student types answers, then self-assesses
    against a model rubric. There is no AI grading -- answers are saved (ungraded)
    so they appear in the student's history, and the rubric is revealed on submit.
    """
    course = get_object_or_404(Course, slug=slug)
    questions = list(course.questions.filter(qtype="written"))
    submitted = False

    for q in questions:
        q.answer = ""

    if request.method == "POST":
        submitted = True
        for q in questions:
            q.answer = (request.POST.get(f"q{q.id}") or "").strip()
            if q.answer:
                # is_correct stays None: this is self-assessed, not auto-graded.
                Attempt.objects.create(
                    student=request.user, question=q, answer_text=q.answer, is_correct=None,
                )

    return render(request, "practice/written_set.html", {
        "course": course, "questions": questions, "submitted": submitted,
    })


# ---------------------------------------------------------------------------
# Progress dashboard: surface a student's own Attempt history.
# ---------------------------------------------------------------------------

def _question_snippet(text, length=90):
    """A clean one-line preview of a question (no figure tokens or math delimiters)."""
    text = re.sub(r"\[\[figure:[^\]]*\]\]", "", text)          # drop figure tokens
    text = text.replace(r"\(", "").replace(r"\)", "")          # drop inline-math delimiters
    text = text.replace(r"\[", "").replace(r"\]", "")          # drop display-math delimiters
    text = re.sub(r"\s+", " ", text).strip()
    return (text[:length].rstrip() + "…") if len(text) > length else text


@login_required
def dashboard(request):
    """Show the signed-in student their practice history and per-course progress."""
    attempts = list(
        Attempt.objects
        .filter(student=request.user)
        .select_related("question", "question__course")
        .order_by("created_at")
    )

    # Aggregate per course. For accuracy we keep each question's MOST RECENT
    # result (attempts are chronological, so later entries overwrite earlier
    # ones), which reflects the student's current standing rather than old tries.
    courses = OrderedDict()  # course_id -> {course, latest: {qid: bool}, submitted, written}
    for a in attempts:
        q = a.question
        if q is None:
            continue
        bucket = courses.setdefault(
            q.course_id, {"course": q.course, "latest": {}, "submitted": 0, "written": 0}
        )
        bucket["submitted"] += 1
        if a.is_correct is None:
            # Written responses are self-assessed, not auto-graded: count, don't score.
            bucket["written"] += 1
        else:
            bucket["latest"][q.id] = bool(a.is_correct)

    course_rows = []
    overall_answered = 0
    overall_correct = 0
    overall_written = 0
    for bucket in courses.values():
        course = bucket["course"]
        answered = len(bucket["latest"])
        correct = sum(1 for ok in bucket["latest"].values() if ok)
        total_q = course.mcq_count
        overall_answered += answered
        overall_correct += correct
        overall_written += bucket["written"]
        course_rows.append({
            "course": course,
            "answered": answered,
            "total": total_q,
            "correct": correct,
            "accuracy": round(100 * correct / answered) if answered else 0,
            "coverage": round(100 * answered / total_q) if total_q else 0,
            "submitted": bucket["submitted"],
            "written": bucket["written"],
        })
    course_rows.sort(key=lambda r: r["course"].title)

    recent = [
        {
            "snippet": _question_snippet(a.question.text),
            "course": a.question.course,
            "is_correct": a.is_correct,
            "created_at": a.created_at,
        }
        for a in reversed(attempts[-15:]) if a.question is not None
    ]

    return render(request, "practice/dashboard.html", {
        "has_data": bool(attempts),
        "course_rows": course_rows,
        "overall_answered": overall_answered,
        "overall_correct": overall_correct,
        "overall_accuracy": round(100 * overall_correct / overall_answered) if overall_answered else 0,
        "overall_written": overall_written,
        "total_submitted": len(attempts),
        "recent": recent,
    })


# ---------------------------------------------------------------------------
# Diagnostic pre-test: a short, login-free, stateless quiz that recommends
# which courses to start with based on the topics a student misses.
# ---------------------------------------------------------------------------

def diagnostic_home(request):
    """Landing page: choose which program's diagnostic to take."""
    programs = [
        {
            "code": code,
            "label": d["label"],
            "blurb": d["blurb"],
            "count": sum(len(t["questions"]) for t in d["topics"]),
        }
        for code, d in DIAGNOSTICS.items()
    ]
    return render(request, "practice/diagnostic_home.html", {"programs": programs})


def diagnostic_quiz(request, program):
    """Show the diagnostic (GET) and grade it by topic proficiency (POST).

    Each topic has several questions. A topic is flagged for review only when the
    student falls below the proficiency threshold (see ``topic_needs_review``), so
    a single careless slip won't trigger a recommendation. A course is recommended
    when any of its topics is flagged.
    """
    data = get_diagnostic(program)
    if not data:
        raise Http404("Unknown diagnostic program")
    code = program.upper()

    if request.method == "POST":
        total_correct = 0
        total_questions = 0
        topic_results = []
        missed_by_slug = OrderedDict()  # slug -> list of weak topic labels

        gidx = 0
        for topic in data["topics"]:
            t_correct = 0
            t_total = 0
            for q in topic["questions"]:
                sel = request.POST.get(f"q{gidx}")
                sel_idx = int(sel) if (sel is not None and sel.isdigit()) else None
                if sel_idx == correct_index(q):
                    t_correct += 1
                t_total += 1
                gidx += 1

            needs_review = topic_needs_review(t_correct, t_total)
            topic_results.append({
                "topic": topic["topic"],
                "correct": t_correct,
                "total": t_total,
                "needs_review": needs_review,
            })
            total_correct += t_correct
            total_questions += t_total
            if needs_review:
                missed_by_slug.setdefault(topic["recommend"], [])
                if topic["topic"] not in missed_by_slug[topic["recommend"]]:
                    missed_by_slug[topic["recommend"]].append(topic["topic"])

        recommended = []
        for slug, topics in missed_by_slug.items():
            course = Course.objects.filter(slug=slug).first()
            if course:
                recommended.append({"course": course, "topics": topics})

        ready = []
        if not missed_by_slug:  # proficient across every topic
            for slug in data.get("ready_recommend", []):
                course = Course.objects.filter(slug=slug).first()
                if course:
                    ready.append(course)

        return render(request, "practice/diagnostic_result.html", {
            "program": code,
            "label": data["label"],
            "total": total_questions,
            "correct": total_correct,
            "recommended": recommended,
            "ready": ready,
            "topic_results": topic_results,
        })

    # GET: render the quiz. Topics are hidden so they don't hint at the answer.
    quiz = [
        {"index": gidx, "text": q["text"],
         "choices": list(enumerate(text for text, _ in q["choices"]))}
        for gidx, _topic, _slug, q in iter_questions(data)
    ]
    return render(request, "practice/diagnostic_quiz.html", {
        "program": code, "label": data["label"], "questions": quiz,
    })
