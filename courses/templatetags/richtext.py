r"""
A lightweight rich-text filter for lesson/explanation content.

It renders a small, predictable subset of Markdown WITHOUT pulling in an
external dependency, and -- crucially -- it leaves LaTeX math untouched so
MathJax can still render formulas like \(x^2\) and \[ ... \].

Supported syntax:
  - **bold**             -> <strong>bold</strong>
  - *italic*             -> <em>italic</em>
  - `code`               -> <code>code</code>
  - lines beginning "- " -> bullet list (<ul><li>...)
  - blank line           -> new paragraph (<p>)
  - single newline       -> line break (<br>)
  - [[check:question|answer1;;answer2|hint]] -> interactive self-check

Everything is HTML-escaped first, so raw HTML in the content is shown as
text (safe by default). Math spans are protected before escaping and
restored verbatim afterward.
"""
import re

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from courses.figures import FIGURES

register = template.Library()
_REGISTERED_SIGN = "\N{REGISTERED SIGN}"
_TRADE_MARK_SIGN = "\N{TRADE MARK SIGN}"

# Matches display math \[ ... \] and inline math \( ... \), across newlines.
_MATH_RE = re.compile(r"\\\[.*?\\\]|\\\(.*?\\\)", re.DOTALL)

# Matches a figure token on its own line: [[figure:name]] or [[figure:name|caption]]
_FIGURE_RE = re.compile(r"^\[\[figure:([a-zA-Z0-9_]+)(?:\|(.*))?\]\]$")

# Matches a self-check token on its own line:
# [[check:question|answer1;;answer2|hint]]
_CHECK_RE = re.compile(r"^\[\[check:(.*?)\|(.*?)\|(.*?)\]\]$")

# Placeholder that marks where a math span was removed. The unusual delimiters
# never occur in lesson text, survive html.escape() unchanged, and are not
# touched by the inline-markdown rules below.
_TOKEN = "\x01MATHSPAN{}\x01"
_TOKEN_RE = re.compile(r"\x01MATHSPAN(\d+)\x01")


def _with_exam_marks(value):
    """Add registered marks to public GED/SAT references without changing stored data."""
    if value is None:
        return ""

    text = str(value)
    text = text.replace("GED&reg;", f"GED{_REGISTERED_SIGN}")
    text = text.replace("GED&trade;", f"GED{_REGISTERED_SIGN}")
    text = text.replace(f"GED{_TRADE_MARK_SIGN}", f"GED{_REGISTERED_SIGN}")
    text = text.replace("SAT&reg;", f"SAT{_REGISTERED_SIGN}")
    text = text.replace("SAT&trade;", f"SAT{_REGISTERED_SIGN}")
    text = text.replace(f"SAT{_TRADE_MARK_SIGN}", f"SAT{_REGISTERED_SIGN}")
    text = re.sub(rf"\bGED\b(?!{_REGISTERED_SIGN})", f"GED{_REGISTERED_SIGN}", text)
    text = re.sub(rf"\bSAT\b(?!{_REGISTERED_SIGN})", f"SAT{_REGISTERED_SIGN}", text)
    return text


@register.filter
def exam_marks(value):
    return _with_exam_marks(value)


def _render_inline(text):
    """Apply inline formatting to already-escaped text."""
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


@register.filter
def richtext(value):
    if not value:
        return ""

    value = _with_exam_marks(value)

    # 1. Stash math spans so Markdown/escaping can't corrupt them.
    math = []

    def _stash(match):
        math.append(match.group(0))
        return _TOKEN.format(len(math) - 1)

    work = _MATH_RE.sub(_stash, str(value))

    # 2. Escape HTML (treat raw content as text, not markup).
    work = escape(work)

    # 3. Build block-level HTML: paragraphs and bullet lists.
    blocks = re.split(r"\n\s*\n", work.strip())
    html_parts = []
    for block in blocks:
        stripped = block.strip()

        # Self-checks become tiny interactive drills inside a lesson.
        check = _CHECK_RE.match(stripped)
        if check:
            prompt, answer, hint = check.groups()
            html_parts.append(
                '<div class="self-check" data-answer="{}">'
                "<strong>Quick Check</strong>"
                "<p>{}</p>"
                '<div class="self-check-row">'
                '<input type="text" aria-label="Quick check answer" placeholder="Type your answer">'
                '<button type="button" data-self-check-button>Check</button>'
                '<button type="button" class="hint-btn" data-self-check-hint>Hint</button>'
                "</div>"
                '<p class="self-check-feedback" aria-live="polite"></p>'
                '<p class="self-check-hint" hidden>{}</p>'
                "</div>".format(answer, _render_inline(prompt), _render_inline(hint))
            )
            continue

        # Markdown table: every non-empty line starts with "|"
        table_lines = [l for l in stripped.split("\n") if l.strip()]
        if len(table_lines) >= 2 and all(l.strip().startswith("|") for l in table_lines):
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in table_lines]
            # Second row is separator if all cells match /^[-: ]+$/
            has_header = len(rows) >= 2 and all(re.match(r"^[-: ]+$", c) for c in rows[1] if c.strip())
            header_row = rows[0] if has_header else None
            data_rows = rows[2:] if has_header else rows
            tbl = ['<table class="data-table">']
            if header_row:
                tbl.append("<thead><tr>")
                tbl.extend(f"<th>{_render_inline(c)}</th>" for c in header_row)
                tbl.append("</tr></thead>")
            tbl.append("<tbody>")
            for row in data_rows:
                tbl.append("<tr>")
                tbl.extend(f"<td>{_render_inline(c)}</td>" for c in row)
                tbl.append("</tr>")
            tbl.append("</tbody></table>")
            html_parts.append("".join(tbl))
            continue

        # A figure token on its own line becomes an embedded chart.
        figure = _FIGURE_RE.match(stripped)
        if figure:
            name, caption = figure.group(1), figure.group(2)
            svg = FIGURES.get(name)
            if svg:
                cap = f"<figcaption>{caption}</figcaption>" if caption else ""
                html_parts.append(f'<figure class="chart">{svg}{cap}</figure>')
            else:
                html_parts.append(f"<p><em>[missing figure: {name}]</em></p>")
            continue

        # Within a block, group consecutive "- " lines into a bullet list and
        # everything else into paragraphs (so an intro line can precede a list).
        para, items = [], []

        def flush_para():
            if para:
                html_parts.append(f"<p>{_render_inline('<br>'.join(para))}</p>")
                para.clear()

        def flush_list():
            if items:
                lis = "".join(f"<li>{_render_inline(x)}</li>" for x in items)
                html_parts.append(f"<ul>{lis}</ul>")
                items.clear()

        for line in block.split("\n"):
            if line.strip().startswith("- "):
                flush_para()
                items.append(line.strip()[2:])
            elif line.strip():
                flush_list()
                para.append(line)
        flush_list()
        flush_para()
    work = "\n".join(html_parts)

    # 4. Restore the original math spans verbatim for MathJax.
    work = _TOKEN_RE.sub(lambda m: math[int(m.group(1))], work)

    return mark_safe(work)
