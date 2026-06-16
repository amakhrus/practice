"""
Claude (Anthropic) integration for the GED & SAT LMS.

Two main functions:
  - explain_question(): produces a step-by-step explanation of a question.
  - grade_essay(): grades a student's essay against a rubric (score 0-100 + feedback).

The API key is read from settings.ANTHROPIC_API_KEY (loaded from a .env file).
"""
import json
from django.conf import settings

# Claude model. Sonnet = a good balance of quality & cost for explanations
# and grading. Switch to 'claude-opus-4-8' if you need the highest quality.
MODEL = "claude-sonnet-4-6"


def _client():
    if not settings.ANTHROPIC_API_KEY:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Add it to your .env file "
            "(ANTHROPIC_API_KEY=sk-ant-...)."
        )
    from anthropic import Anthropic

    return Anthropic(api_key=settings.ANTHROPIC_API_KEY)


def explain_question(question_text, correct_answer="", program="GED", student_answer=""):
    """Generate a clear, step-by-step explanation of a question (in English)."""
    client = _client()

    context = f"This is a {program} exam question.\n\nQUESTION:\n{question_text}\n"
    if correct_answer:
        context += f"\nCORRECT ANSWER: {correct_answer}\n"
    if student_answer:
        context += f"\nSTUDENT ANSWER: {student_answer}\n"

    system = (
        "You are a patient, expert GED & SAT tutor. "
        "Give a clear, step-by-step explanation in English that a student can easily "
        "follow. Explain the CONCEPT behind it, not just the answer. "
        "If the student's answer is wrong, kindly point out where they went wrong. "
        "When writing math, use LaTeX with \\( \\) for inline and \\[ \\] for display."
    )

    msg = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        system=system,
        messages=[{"role": "user", "content": context}],
    )
    return msg.content[0].text


def grade_essay(question_text, rubric, student_answer, program="GED"):
    """Grade an essay answer. Returns a dict: {score: 0-100, feedback: str}."""
    client = _client()

    system = (
        "You are an objective, fair GED & SAT exam grader. "
        "Grade the student's answer based on the given rubric. "
        "Reply ONLY with valid JSON in the format: "
        '{"score": <number 0-100>, "feedback": "<constructive feedback in English>"}'
    )

    user = (
        f"Program: {program}\n\n"
        f"QUESTION:\n{question_text}\n\n"
        f"GRADING RUBRIC:\n{rubric or 'Use reasonable general grading standards.'}\n\n"
        f"STUDENT ANSWER:\n{student_answer}\n\n"
        "Provide a score and feedback in JSON format."
    )

    msg = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    raw = msg.content[0].text.strip()

    # Clean up if wrapped in a code fence ```json ... ```
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        data = json.loads(raw)
        return {"score": float(data.get("score", 0)), "feedback": data.get("feedback", "")}
    except (json.JSONDecodeError, ValueError):
        # Fallback if the model doesn't return pure JSON
        return {"score": None, "feedback": raw}
