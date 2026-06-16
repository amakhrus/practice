"""
Export the seeded 'GED Mathematical Reasoning' full-length exam to a single,
self-contained, interactive HTML file that opens in any browser -- no server,
no internet needed except the MathJax CDN for rendering formulas.

The page recreates the real test environment:
  - A 115-minute countdown timer (auto-submits at 0).
  - The two-part structure (Part 1: no calculator; Part 2: calculator).
  - A collapsible 'Before you begin' section with the rules and formula sheet.
  - All 46 multiple-choice questions with inline figures (the same SVGs the LMS
    uses) and MathJax formulas.
  - A Submit button that grades the exam, shows the raw score, an estimated GED
    scaled score (100-200, 145 to pass), and reveals every explanation.

It reuses the app's own ``richtext`` renderer so figures, bold text, and math
look exactly like they do inside the LMS.

Run (after seeding):
    python manage.py seed_ged_math_exam
    python manage.py export_ged_math_exam_html
    # -> writes ged_math_exam.html in the project root (open it in a browser)

Options:
    --slug   course slug to export (default: ged-math-reasoning-exam)
    --output path for the HTML file (default: ged_math_exam.html)
"""
import html
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from courses.models import Course
from courses.templatetags.richtext import richtext


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<script>
  window.MathJax = {{
    tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }},
    options: {{ ignoreHtmlClass: 'no-mathjax', processHtmlClass: 'mathjax' }}
  }};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  :root {{ --blue:#2563eb; --ink:#1a1a1a; --muted:#6b7280; --line:#e5e7eb;
          --green:#16a34a; --red:#dc2626; --amber:#d97706; --bg:#f8fafc; }}
  * {{ box-sizing:border-box; }}
  body {{ font-family:system-ui,-apple-system,'Segoe UI',sans-serif; color:var(--ink);
         margin:0; background:var(--bg); line-height:1.6; }}
  .wrap {{ max-width:820px; margin:0 auto; padding:0 18px 120px; }}
  header.exam {{ position:sticky; top:0; z-index:50; background:#fff; border-bottom:1px solid var(--line);
                box-shadow:0 1px 6px rgba(0,0,0,.05); }}
  .bar {{ max-width:820px; margin:0 auto; padding:10px 18px; display:flex; align-items:center;
         gap:14px; flex-wrap:wrap; }}
  .bar h1 {{ font-size:1rem; margin:0; flex:1 1 220px; }}
  .timer {{ font-variant-numeric:tabular-nums; font-weight:700; font-size:1.25rem;
           padding:4px 12px; border-radius:8px; background:#eff6ff; color:var(--blue); }}
  .timer.warn {{ background:#fef2f2; color:var(--red); }}
  .progress {{ font-size:.85rem; color:var(--muted); }}
  h2.sec {{ margin:32px 0 6px; font-size:1.15rem; }}
  .badge {{ display:inline-block; font-size:.72rem; font-weight:700; padding:2px 9px; border-radius:999px;
           vertical-align:middle; margin-left:8px; }}
  .badge.no-calc {{ background:#fef2f2; color:var(--red); }}
  .badge.calc {{ background:#ecfdf5; color:var(--green); }}
  details.intro {{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:6px 18px;
                  margin:18px 0; }}
  details.intro > summary {{ cursor:pointer; font-weight:700; padding:10px 0; font-size:1.05rem; }}
  .lesson h3 {{ margin:18px 0 4px; }}
  .q {{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:16px 18px;
       margin:14px 0; }}
  .q-head {{ display:flex; gap:10px; align-items:baseline; }}
  .q-num {{ font-weight:700; color:var(--blue); flex:0 0 auto; }}
  .q-diff {{ margin-left:auto; font-size:.7rem; color:var(--muted); text-transform:uppercase;
            letter-spacing:.04em; }}
  .q-body p:first-child {{ margin-top:0; }}
  .choices {{ list-style:none; margin:12px 0 0; padding:0; }}
  .choices li {{ margin:8px 0; }}
  .choices label {{ display:flex; gap:10px; align-items:flex-start; padding:10px 12px; border:1px solid var(--line);
                   border-radius:9px; cursor:pointer; transition:background .12s,border-color .12s; }}
  .choices label:hover {{ background:#f9fafb; }}
  .choices input {{ margin-top:5px; }}
  .choices label.correct {{ border-color:var(--green); background:#f0fdf4; }}
  .choices label.wrong {{ border-color:var(--red); background:#fef2f2; }}
  .explanation {{ margin-top:12px; padding:12px 14px; border-left:4px solid var(--blue);
                 background:#f8fafc; border-radius:0 8px 8px 0; display:none; }}
  .explanation.show {{ display:block; }}
  .explanation .tag {{ font-weight:700; color:var(--blue); display:block; margin-bottom:2px; }}
  figure.chart {{ margin:14px 0; text-align:center; }}
  figure.chart svg {{ max-width:100%; height:auto; }}
  figcaption {{ font-size:.85rem; color:var(--muted); margin-top:6px; }}
  table.data-table {{ border-collapse:collapse; margin:10px 0; }}
  table.data-table th, table.data-table td {{ border:1px solid var(--line); padding:6px 12px; }}
  .actions {{ position:fixed; bottom:0; left:0; right:0; background:#fff; border-top:1px solid var(--line);
             padding:12px 18px; display:flex; justify-content:center; gap:12px; z-index:60; }}
  button {{ font:inherit; font-weight:700; border:0; border-radius:9px; padding:11px 26px; cursor:pointer; }}
  .btn-primary {{ background:var(--blue); color:#fff; }}
  .btn-ghost {{ background:#fff; color:var(--ink); border:1px solid var(--line); }}
  .results {{ display:none; background:#fff; border:2px solid var(--blue); border-radius:14px;
             padding:22px; margin:24px 0; text-align:center; }}
  .results.show {{ display:block; }}
  .results .score {{ font-size:2.6rem; font-weight:800; line-height:1; }}
  .results .scaled {{ font-size:1.1rem; margin-top:8px; }}
  .pill {{ display:inline-block; padding:4px 16px; border-radius:999px; font-weight:700; margin-top:10px; }}
  .pill.pass {{ background:#ecfdf5; color:var(--green); }}
  .pill.fail {{ background:#fef2f2; color:var(--red); }}
  .note {{ font-size:.82rem; color:var(--muted); margin-top:10px; }}
</style>
</head>
<body class="mathjax">
<header class="exam">
  <div class="bar">
    <h1>{title}</h1>
    <span class="progress" id="progress">0 / {n} answered</span>
    <span class="timer" id="timer">115:00</span>
  </div>
</header>

<div class="wrap">
  <p style="color:var(--muted);margin:18px 0 0">{description}</p>

  <details class="intro">
    <summary>Before you begin &mdash; exam rules &amp; formula sheet</summary>
    {lessons}
  </details>

  <div class="results" id="results"></div>

  {parts}
</div>

<div class="actions">
  <button class="btn-primary" id="submit">Submit Exam</button>
  <button class="btn-ghost" id="reset">Reset</button>
</div>

<script>
  var TOTAL = {n};
  var answers = {answers_json};   // qid -> index of correct choice

  // ---- progress counter ----
  function updateProgress() {{
    var done = 0;
    for (var i = 0; i < TOTAL; i++) {{
      if (document.querySelector('input[name="q' + i + '"]:checked')) done++;
    }}
    document.getElementById('progress').textContent = done + ' / ' + TOTAL + ' answered';
  }}
  document.addEventListener('change', function (e) {{
    if (e.target && e.target.name && e.target.name.charAt(0) === 'q') updateProgress();
  }});

  // ---- countdown timer (115 minutes) ----
  var remaining = 115 * 60;
  var timerEl = document.getElementById('timer');
  var ticking = setInterval(function () {{
    remaining--;
    if (remaining <= 0) {{ remaining = 0; clearInterval(ticking); grade(); }}
    var m = Math.floor(remaining / 60), s = remaining % 60;
    timerEl.textContent = m + ':' + (s < 10 ? '0' : '') + s;
    if (remaining <= 600) timerEl.classList.add('warn');
  }}, 1000);

  // ---- estimated GED scaled score: 0%->100, 65%->145 (pass), 100%->200 ----
  function scaledScore(pct) {{
    var s = pct <= 0.65 ? 100 + (pct / 0.65) * 45
                        : 145 + ((pct - 0.65) / 0.35) * 55;
    return Math.max(100, Math.min(200, Math.round(s)));
  }}

  function grade() {{
    clearInterval(ticking);
    var correct = 0;
    for (var i = 0; i < TOTAL; i++) {{
      var picked = document.querySelector('input[name="q' + i + '"]:checked');
      var labels = document.querySelectorAll('#q' + i + ' .choices label');
      labels.forEach(function (l) {{ l.classList.remove('correct', 'wrong'); }});
      var correctIdx = answers[i];
      if (labels[correctIdx]) labels[correctIdx].classList.add('correct');
      if (picked) {{
        var pickedIdx = parseInt(picked.value, 10);
        if (pickedIdx === correctIdx) correct++;
        else if (labels[pickedIdx]) labels[pickedIdx].classList.add('wrong');
      }}
      var exp = document.querySelector('#q' + i + ' .explanation');
      if (exp) exp.classList.add('show');
    }}
    var pct = correct / TOTAL;
    var scaled = scaledScore(pct);
    var pass = scaled >= 145;
    var box = document.getElementById('results');
    box.innerHTML =
      '<div class="score">' + correct + ' / ' + TOTAL + '</div>' +
      '<div class="scaled">Estimated GED scaled score: <strong>' + scaled +
      '</strong> &nbsp;(' + Math.round(pct * 100) + '% correct)</div>' +
      '<span class="pill ' + (pass ? 'pass' : 'fail') + '">' +
      (pass ? 'PASS' : 'NOT YET') + ' &middot; 145 needed</span>' +
      '<p class="note">The scaled score is an estimate for practice only; the official GED ' +
      'conversion is not public. Review the explanations below each question.</p>';
    box.classList.add('show');
    box.scrollIntoView({{ behavior: 'smooth' }});
    if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([box]);
  }}

  document.getElementById('submit').addEventListener('click', grade);
  document.getElementById('reset').addEventListener('click', function () {{
    if (!confirm('Clear all answers and restart?')) return;
    location.reload();
  }});
</script>
</body>
</html>
"""


class Command(BaseCommand):
    help = "Export the seeded GED Math Reasoning exam to a self-contained interactive HTML file."

    def add_arguments(self, parser):
        parser.add_argument("--slug", default="ged-math-reasoning-exam")
        parser.add_argument("--output", default="ged_math_exam.html")

    def handle(self, *args, **options):
        slug = options["slug"]
        try:
            course = Course.objects.get(slug=slug)
        except Course.DoesNotExist:
            raise CommandError(
                f"Course '{slug}' not found. Run 'python manage.py seed_ged_math_exam' first."
            )

        questions = list(course.questions.order_by("id").prefetch_related("choices"))
        if not questions:
            raise CommandError(f"Course '{slug}' has no questions to export.")

        # Lessons -> rules & formula sheet (rendered with the app's own renderer).
        lessons_html = []
        for lesson in course.lessons.all():
            lessons_html.append(
                f'<div class="lesson"><h3>{html.escape(lesson.title)}</h3>{richtext(lesson.content)}</div>'
            )

        # Build the questions, split into Part 1 (no calculator, first 5) and Part 2.
        diff_label = {1: "Easy", 2: "Medium", 3: "Hard"}
        answers = {}
        blocks = {"part1": [], "part2": []}
        for idx, q in enumerate(questions):
            choices = list(q.choices.all())
            correct_idx = next((i for i, c in enumerate(choices) if c.is_correct), 0)
            answers[idx] = correct_idx

            choice_items = []
            for ci, choice in enumerate(choices):
                choice_items.append(
                    f'<li><label><input type="radio" name="q{idx}" value="{ci}">'
                    f'<span>{richtext(choice.text)}</span></label></li>'
                )

            block = (
                f'<div class="q" id="q{idx}">'
                f'<div class="q-head"><span class="q-num">Q{idx + 1}</span>'
                f'<span class="q-diff">{diff_label.get(q.difficulty, "")}</span></div>'
                f'<div class="q-body">{richtext(q.text)}</div>'
                f'<ul class="choices">{"".join(choice_items)}</ul>'
                f'<div class="explanation"><span class="tag">Explanation</span>{richtext(q.explanation)}</div>'
                f"</div>"
            )
            blocks["part1" if idx < 5 else "part2"].append(block)

        parts_html = (
            '<h2 class="sec">Part 1 &mdash; Questions 1&ndash;5'
            '<span class="badge no-calc">No calculator</span></h2>'
            + "".join(blocks["part1"])
            + '<h2 class="sec">Part 2 &mdash; Questions 6&ndash;'
            + str(len(questions))
            + '<span class="badge calc">Calculator allowed</span></h2>'
            + "".join(blocks["part2"])
        )

        # JSON map of qid -> correct choice index (keys are 0..n-1, dense).
        answers_json = "{" + ",".join(f"{k}:{v}" for k, v in answers.items()) + "}"

        page = PAGE_TEMPLATE.format(
            title=html.escape(str(course.title)),
            description=html.escape(str(course.description)),
            n=len(questions),
            lessons="".join(lessons_html),
            parts=parts_html,
            answers_json=answers_json,
        )

        out_path = Path(options["output"])
        if not out_path.is_absolute():
            out_path = Path(settings.BASE_DIR) / out_path
        out_path.write_text(page, encoding="utf-8")

        self.stdout.write(self.style.SUCCESS(
            f"Wrote {out_path}  ({len(questions)} questions). Open it in any web browser."
        ))
