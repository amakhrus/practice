---
name: richtext-renders-question-text
description: Practice question text renders through the richtext filter, so figures/markdown work in questions
metadata:
  type: project
---

The practice templates (`templates/practice/question_detail.html` and `practice_set.html`) render question text with `{{ ...|richtext }}` (not `|exam_marks|linebreaks`). `richtext` already applies the GED/SAT registered-mark substitution internally, so don't also pipe through `exam_marks`.

**Why:** This means a question's `text` supports everything lessons do — `[[figure:NAME|caption]]` SVG charts, `**bold**`, `- ` bullet lists, and `\(LaTeX\)` (MathJax). Choices still render with `|exam_marks` only. This is what makes chart-based / read-the-source practice items possible.

**How to apply:** When authoring questions in `seed_*` commands, put a `[[figure:...]]` token on its own line with blank lines around it so it renders as its own block. Verify the figure key exists in `courses/figures.py` `FIGURES`. Avoid stray leading `- ` or `*` in question text unless you intend a list/italics. Related: [[seeders-wipe-attempt-history]].
