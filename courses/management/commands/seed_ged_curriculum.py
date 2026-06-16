"""
Seed data: a richer GED Math curriculum of seven explanation-heavy courses
designed to build real understanding, not just drill answers.

  1. GED Math Foundations: Number Sense & Measurement Mastery
  2. GED Math Foundations: Integer & Rational Number Operations Mastery
  3. GED Math Foundations: Order of Operations, Calculator & Formula Skills Mastery
  4. GED Math Foundations: Ratios, Proportions & Scale Factors Mastery
  5. GED Math: Mastering Fractions, Decimals & Percents
  6. GED Math: Geometry & Measurement
  7. GED Math: Data, Statistics & Probability Mastery

Each lesson uses plain-language intuition, real-world analogies, fully worked
examples, and "common mistake" callouts. Every practice question carries a
step-by-step solution that is shown to the student after they answer.

Run:
    python manage.py seed_ged_curriculum
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice

from .seed_ged_data_stats_probability import COURSE as DATA_STATS_PROBABILITY_COURSE
from .seed_ged_integer_rational_operations import COURSE as INTEGER_RATIONAL_OPERATIONS_COURSE
from .seed_ged_number_sense_measurement import COURSE as NUMBER_SENSE_MEASUREMENT_COURSE
from .seed_ged_order_operations_formula_skills import COURSE as ORDER_OPERATIONS_FORMULA_SKILLS_COURSE
from .seed_ged_ratios_proportions_scale import COURSE as RATIOS_PROPORTIONS_SCALE_COURSE


# ----------------------------------------------------------------------------
# Course data. Each course is a dict: meta + lessons + mcqs + essays.
# Math is written in LaTeX (\( \) inline, \[ \] display) so MathJax renders it.
# ----------------------------------------------------------------------------

FRACTIONS_COURSE = {
    "title": "GED Math: Mastering Fractions, Decimals & Percents",
    "slug": "ged-fractions-decimals-percents",
    "program": "GED",
    "subject": "math",
    "description": (
        "Fractions, decimals, and percents are three ways of saying the same thing: "
        "a part of a whole. This course builds deep intuition for all three, shows how "
        "to switch between them effortlessly, and connects every idea to real life "
        "(money, recipes, discounts). By the end, parts-of-a-whole problems will feel obvious."
    ),
    "lessons": [
        (
            "1. What a Fraction Really Means",
            r"A fraction is just a way to describe **part of a whole**. Think of a pizza cut into equal slices." "\n\n"
            r"In \(\frac{3}{4}\), the bottom number (the **denominator**, 4) tells you how many equal pieces the whole is cut into. "
            r"The top number (the **numerator**, 3) tells you how many of those pieces you have. So \(\frac{3}{4}\) means '3 out of 4 equal slices.'" "\n\n"
            r"**Equivalent fractions** are different-looking fractions that represent the same amount. If you cut each of your 4 slices in half, you now have 8 tiny slices and you hold 6 of them: \(\frac{3}{4} = \frac{6}{8}\). The pizza didn't change — only the number of cuts did." "\n\n"
            r"**Simplifying** runs this backwards: divide the top and bottom by the same number until they share no common factor. \(\frac{6}{8} = \frac{6 \div 2}{8 \div 2} = \frac{3}{4}\)." "\n\n"
            r"⚠️ Common mistake: you may only multiply or divide the top and bottom by the *same* number. Adding the same number to both (e.g. \(\frac{3+1}{4+1}\)) changes the value — don't do it.",
        ),
        (
            "2. Adding & Subtracting Fractions",
            r"You can only add or subtract fractions when the pieces are the **same size** — that is, when the denominators match. You can't add 1 quarter and 1 third directly any more than you can add 1 apple and 1 orange without a common name ('fruit')." "\n\n"
            r"**Same denominator?** Just add the tops and keep the bottom:" "\n"
            r"\[ \frac{2}{5} + \frac{1}{5} = \frac{3}{5}. \]" "\n"
            r"**Different denominators?** First rewrite them with a common denominator (a number both bottoms divide into), then add." "\n\n"
            r"Example: \(\frac{1}{2} + \frac{1}{3}\). The smallest common denominator is 6." "\n"
            r"\[ \frac{1}{2} = \frac{3}{6}, \qquad \frac{1}{3} = \frac{2}{6}, \qquad \frac{3}{6} + \frac{2}{6} = \frac{5}{6}. \]" "\n\n"
            r"⚠️ Common mistake: never add the denominators. \(\frac{1}{2} + \frac{1}{3}\) is **not** \(\frac{2}{5}\). The bottom tells you the *size* of the piece, not a quantity to add.",
        ),
        (
            "3. Multiplying & Dividing Fractions",
            r"Multiplying fractions is the *easiest* operation — no common denominator needed. Multiply straight across:" "\n"
            r"\[ \frac{2}{3} \times \frac{4}{5} = \frac{2 \times 4}{3 \times 5} = \frac{8}{15}. \]" "\n"
            r"Intuition: \(\frac{2}{3} \times \frac{4}{5}\) means 'two-thirds *of* four-fifths.' The word **of** signals multiplication." "\n\n"
            r"**Dividing** fractions uses a trick: 'keep, change, flip.' Keep the first fraction, change \(\div\) to \(\times\), and flip the second fraction upside down (its **reciprocal**)." "\n"
            r"\[ \frac{3}{4} \div \frac{2}{5} = \frac{3}{4} \times \frac{5}{2} = \frac{15}{8}. \]" "\n\n"
            r"Why flip? Dividing by \(\frac{2}{5}\) asks 'how many two-fifths fit into three-quarters?' Multiplying by the reciprocal answers exactly that." "\n\n"
            r"💡 Tip: always simplify your final answer, and convert improper fractions like \(\frac{15}{8}\) to a mixed number (\(1\frac{7}{8}\)) if the question expects it.",
        ),
        (
            "4. Decimals: Fractions in Disguise",
            r"A decimal is simply a fraction whose denominator is 10, 100, 1000, and so on. The place after the dot is tenths, the next is hundredths:" "\n"
            r"\[ 0.7 = \frac{7}{10}, \qquad 0.25 = \frac{25}{100} = \frac{1}{4}. \]" "\n"
            r"**Fraction → decimal:** divide the top by the bottom. \(\frac{3}{4} = 3 \div 4 = 0.75\)." "\n\n"
            r"**Decimal → fraction:** read the place value, then simplify. \(0.6 = \frac{6}{10} = \frac{3}{5}\)." "\n\n"
            r"Lining up the decimal point is the key skill for adding and subtracting decimals — keep the dots stacked vertically so tenths line up with tenths." "\n\n"
            r"⚠️ Common mistake: when multiplying decimals, count the total number of decimal places in both factors. \(0.2 \times 0.3 = 0.06\) (two decimal places), **not** 0.6.",
        ),
        (
            "5. Percents in the Real World",
            r"'Percent' means **per hundred**. \(45\%\) literally means \(\frac{45}{100} = 0.45\). That single idea connects all three forms:" "\n"
            r"\[ 45\% = \frac{45}{100} = 0.45. \]" "\n"
            r"**Finding a percent of a number:** turn the percent into a decimal and multiply. \(30\%\) of \(150 = 0.30 \times 150 = 45\)." "\n\n"
            r"**Discounts:** a \(\$80\) shirt at \(25\%\) off. The discount is \(0.25 \times 80 = \$20\), so you pay \(80 - 20 = \$60\). Shortcut: paying after a \(25\%\) discount means paying \(75\%\), so \(0.75 \times 80 = \$60\) in one step." "\n\n"
            r"**Percent change:** \(\dfrac{\text{new} - \text{old}}{\text{old}} \times 100\%\). A price rising from \(\$50\) to \(\$65\): \(\frac{65-50}{50} = \frac{15}{50} = 0.30 = 30\%\) increase." "\n\n"
            r"💡 Tip: 'of' usually means multiply, and 'is' usually means equals. 'What is 20% of 60?' becomes \(x = 0.20 \times 60\).",
        ),
    ],
    "mcqs": [
        {
            "text": r"Simplify the fraction \(\dfrac{12}{18}\) to lowest terms.",
            "difficulty": 1,
            "choices": [(r"\(\frac{2}{3}\)", True), (r"\(\frac{6}{9}\)", False),
                        (r"\(\frac{3}{4}\)", False), (r"\(\frac{12}{18}\)", False)],
            "explanation": r"The largest number that divides both 12 and 18 is 6. \(\frac{12 \div 6}{18 \div 6} = \frac{2}{3}\).",
        },
        {
            "text": r"What is \(\dfrac{1}{2} + \dfrac{1}{3}\)?",
            "difficulty": 2,
            "choices": [(r"\(\frac{5}{6}\)", True), (r"\(\frac{2}{5}\)", False),
                        (r"\(\frac{1}{6}\)", False), (r"\(\frac{2}{6}\)", False)],
            "explanation": r"Use a common denominator of 6: \(\frac{1}{2} = \frac{3}{6}\) and \(\frac{1}{3} = \frac{2}{6}\). Then \(\frac{3}{6} + \frac{2}{6} = \frac{5}{6}\).",
        },
        {
            "text": r"Compute \(\dfrac{2}{3} \times \dfrac{4}{5}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{8}{15}\)", True), (r"\(\frac{6}{8}\)", False),
                        (r"\(\frac{2}{15}\)", False), (r"\(\frac{8}{8}\)", False)],
            "explanation": r"Multiply straight across: \(\frac{2 \times 4}{3 \times 5} = \frac{8}{15}\). It is already in lowest terms.",
        },
        {
            "text": r"Compute \(\dfrac{3}{4} \div \dfrac{2}{5}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{15}{8}\)", True), (r"\(\frac{6}{20}\)", False),
                        (r"\(\frac{3}{10}\)", False), (r"\(\frac{8}{15}\)", False)],
            "explanation": r"Keep, change, flip: \(\frac{3}{4} \div \frac{2}{5} = \frac{3}{4} \times \frac{5}{2} = \frac{15}{8}\) (or \(1\frac{7}{8}\)).",
        },
        {
            "text": r"Write \(\dfrac{3}{4}\) as a decimal.",
            "difficulty": 1,
            "choices": [(r"\(0.75\)", True), (r"\(0.34\)", False),
                        (r"\(0.43\)", False), (r"\(1.33\)", False)],
            "explanation": r"Divide the numerator by the denominator: \(3 \div 4 = 0.75\).",
        },
        {
            "text": r"What is \(30\%\) of \(150\)?",
            "difficulty": 1,
            "choices": [(r"\(45\)", True), (r"\(50\)", False), (r"\(30\)", False), (r"\(120\)", False)],
            "explanation": r"Turn the percent into a decimal and multiply: \(0.30 \times 150 = 45\).",
        },
        {
            "text": r"A \(\$60\) jacket is marked \(20\%\) off. What is the sale price?",
            "difficulty": 2,
            "choices": [(r"\(\$48\)", True), (r"\(\$40\)", False), (r"\(\$12\)", False), (r"\(\$52\)", False)],
            "explanation": r"The discount is \(0.20 \times 60 = \$12\), so the price is \(60 - 12 = \$48\). Shortcut: paying \(80\%\) means \(0.80 \times 60 = \$48\).",
        },
        {
            "text": r"A town's population grows from \(2{,}000\) to \(2{,}500\). What is the percent increase?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(50\%\)", False), (r"\(500\%\)", False)],
            "explanation": r"Percent change \(= \frac{\text{new}-\text{old}}{\text{old}} = \frac{2500-2000}{2000} = \frac{500}{2000} = 0.25 = 25\%\).",
        },
    ],
    "essays": [
        {
            "text": (
                r"A recipe needs \(\frac{3}{4}\) cup of sugar, but you want to make only half the recipe. "
                r"How much sugar do you need? Show your reasoning, and explain in words why the answer is "
                r"smaller than \(\frac{3}{4}\)."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full marks for: (1) recognizing 'half of' means \(\frac{1}{2} \times \frac{3}{4}\); "
                r"(2) computing \(\frac{1}{2} \times \frac{3}{4} = \frac{3}{8}\) cup; "
                r"(3) explaining that multiplying by a fraction less than 1 makes the amount smaller. "
                "Deduct for arithmetic errors or missing explanation."
            ),
        },
    ],
}


GEOMETRY_COURSE = {
    "title": "GED Math: Geometry & Measurement",
    "slug": "ged-geometry-measurement",
    "program": "GED",
    "subject": "math",
    "description": (
        "Geometry is the math of shapes and space — the area of a floor, the volume of a tank, "
        "the length of a ramp. This course explains why every formula works, not just what "
        "to memorize, so you can recognize which formula a word problem is really asking for."
    ),
    "lessons": [
        (
            "1. Perimeter & Area: Edges vs. Surface",
            r"Two ideas trip students up because they sound similar but measure very different things." "\n\n"
            r"**Perimeter** is the distance *around* a shape — imagine walking along its edge. It is a length, measured in cm, m, ft. For a rectangle, \(P = 2(l + w)\) because there are two lengths and two widths." "\n\n"
            r"**Area** is the amount of *flat surface inside* — imagine the tiles needed to cover a floor. It is measured in **square** units (\(\text{cm}^2\), \(\text{m}^2\)). For a rectangle, \(A = l \times w\)." "\n\n"
            r"Example: a room \(8\,\text{m}\) by \(5\,\text{m}\)." "\n"
            r"\[ P = 2(8+5) = 26\,\text{m}, \qquad A = 8 \times 5 = 40\,\text{m}^2. \]" "\n"
            r"A triangle's area is \(A = \frac{1}{2} b h\) — a triangle is literally half of a rectangle that surrounds it." "\n\n"
            r"⚠️ Common mistake: mixing up the units. If the answer is a length use single units; if it's a surface use square units.",
        ),
        (
            "2. Circles: π Demystified",
            r"Every circle has a center. The **radius** \(r\) is the distance from the center to the edge; the **diameter** \(d\) goes all the way across through the center, so \(d = 2r\)." "\n\n"
            r"The magic number \(\pi \approx 3.14\) is just the ratio of a circle's circumference to its diameter — the same for *every* circle ever drawn." "\n\n"
            r"**Circumference** (distance around): \(C = 2\pi r\) or \(C = \pi d\)." "\n"
            r"**Area** (surface inside): \(A = \pi r^2\)." "\n\n"
            r"Example: a circle with radius \(5\,\text{cm}\)." "\n"
            r"\[ C = 2\pi(5) = 10\pi \approx 31.4\,\text{cm}, \qquad A = \pi(5)^2 = 25\pi \approx 78.5\,\text{cm}^2. \]" "\n\n"
            r"⚠️ Common mistake: using the diameter where the formula wants the radius. If a problem gives the diameter, halve it first.",
        ),
        (
            "3. Volume: Filling 3D Space",
            r"Volume measures how much space a solid takes up — think of how much water fills a tank. It uses **cubic** units (\(\text{cm}^3\), \(\text{m}^3\))." "\n\n"
            r"A powerful pattern: for any solid with the same cross-section all the way up (a box, a cylinder, a prism), **volume = area of the base × height**." "\n"
            r"\[ \text{Box: } V = l \times w \times h, \qquad \text{Cylinder: } V = \pi r^2 h. \]" "\n"
            r"Example: a cylindrical can with radius \(3\,\text{cm}\) and height \(10\,\text{cm}\)." "\n"
            r"\[ V = \pi (3)^2 (10) = 90\pi \approx 282.7\,\text{cm}^3. \]" "\n\n"
            r"For a box \(4 \times 3 \times 2\): \(V = 4 \times 3 \times 2 = 24\,\text{cm}^3\)." "\n\n"
            r"💡 Tip: spot the base shape first (rectangle? circle?), find its area, then multiply by the height.",
        ),
        (
            "4. The Pythagorean Theorem",
            r"In any **right triangle** (one with a \(90^\circ\) corner), the three sides are linked by one of the most useful formulas in all of math:" "\n"
            r"\[ a^2 + b^2 = c^2, \]" "\n"
            r"where \(a\) and \(b\) are the two shorter sides (the **legs**) and \(c\) is the longest side (the **hypotenuse**) opposite the right angle." "\n\n"
            r"Example: legs of \(3\) and \(4\)." "\n"
            r"\[ c = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5. \]" "\n"
            r"This shows up constantly in real life: the length of a ladder against a wall, the diagonal of a TV screen, the straight-line distance between two points." "\n\n"
            r"⚠️ Common mistake: \(c\) is *always* the hypotenuse (the side facing the right angle). Don't plug a leg in where \(c\) belongs.",
        ),
        (
            "5. The Coordinate Plane",
            r"The coordinate plane is a map made of two number lines: a horizontal **x-axis** and a vertical **y-axis** crossing at the **origin** \((0,0)\). Any point is named by an ordered pair \((x, y)\) — go right/left \(x\), then up/down \(y\)." "\n\n"
            r"**Slope** measures steepness: 'rise over run,' how much a line goes up for each step to the right." "\n"
            r"\[ \text{slope} = \frac{y_2 - y_1}{x_2 - x_1}. \]" "\n"
            r"Between \((1, 2)\) and \((4, 8)\): \(\text{slope} = \frac{8-2}{4-1} = \frac{6}{3} = 2\). The line rises 2 for every 1 across." "\n\n"
            r"**Distance** between two points uses the Pythagorean theorem in disguise:" "\n"
            r"\[ d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}. \]" "\n\n"
            r"💡 Tip: a positive slope climbs left-to-right; a negative slope falls; a horizontal line has slope \(0\).",
        ),
    ],
    "mcqs": [
        {
            "text": r"A rectangle is \(9\,\text{cm}\) long and \(4\,\text{cm}\) wide. What is its perimeter?",
            "difficulty": 1,
            "choices": [(r"\(26\,\text{cm}\)", True), (r"\(36\,\text{cm}\)", False),
                        (r"\(13\,\text{cm}\)", False), (r"\(18\,\text{cm}\)", False)],
            "explanation": r"Perimeter \(= 2(l + w) = 2(9 + 4) = 2(13) = 26\,\text{cm}\). (Area would be \(36\,\text{cm}^2\) — don't confuse the two.)",
        },
        {
            "text": r"What is the area of a triangle with base \(12\,\text{cm}\) and height \(5\,\text{cm}\)?",
            "difficulty": 1,
            "choices": [(r"\(30\,\text{cm}^2\)", True), (r"\(60\,\text{cm}^2\)", False),
                        (r"\(17\,\text{cm}^2\)", False), (r"\(34\,\text{cm}^2\)", False)],
            "explanation": r"Triangle area \(= \tfrac{1}{2} b h = \tfrac{1}{2}(12)(5) = 30\,\text{cm}^2\).",
        },
        {
            "text": r"A circle has a radius of \(7\,\text{cm}\). What is its area? (Use \(\pi \approx 3.14\).)",
            "difficulty": 2,
            "choices": [(r"\(\approx 153.9\,\text{cm}^2\)", True), (r"\(\approx 43.96\,\text{cm}^2\)", False),
                        (r"\(\approx 21.98\,\text{cm}^2\)", False), (r"\(\approx 49\,\text{cm}^2\)", False)],
            "explanation": r"Area \(= \pi r^2 = 3.14 \times 7^2 = 3.14 \times 49 \approx 153.9\,\text{cm}^2\).",
        },
        {
            "text": r"A circle has a diameter of \(10\,\text{cm}\). What is its circumference? (Use \(\pi \approx 3.14\).)",
            "difficulty": 2,
            "choices": [(r"\(\approx 31.4\,\text{cm}\)", True), (r"\(\approx 15.7\,\text{cm}\)", False),
                        (r"\(\approx 78.5\,\text{cm}\)", False), (r"\(\approx 62.8\,\text{cm}\)", False)],
            "explanation": r"With the diameter given, \(C = \pi d = 3.14 \times 10 = 31.4\,\text{cm}\).",
        },
        {
            "text": r"What is the volume of a box measuring \(4\,\text{cm} \times 3\,\text{cm} \times 2\,\text{cm}\)?",
            "difficulty": 1,
            "choices": [(r"\(24\,\text{cm}^3\)", True), (r"\(9\,\text{cm}^3\)", False),
                        (r"\(18\,\text{cm}^3\)", False), (r"\(12\,\text{cm}^3\)", False)],
            "explanation": r"Volume of a box \(= l \times w \times h = 4 \times 3 \times 2 = 24\,\text{cm}^3\).",
        },
        {
            "text": r"A right triangle has legs of \(8\) and \(15\). How long is the hypotenuse?",
            "difficulty": 2,
            "choices": [(r"\(17\)", True), (r"\(23\)", False), (r"\(\sqrt{23}\)", False), (r"\(289\)", False)],
            "explanation": r"\(c = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17\).",
        },
        {
            "text": r"What is the slope of the line through \((1, 2)\) and \((4, 8)\)?",
            "difficulty": 2,
            "choices": [(r"\(2\)", True), (r"\(\tfrac{1}{2}\)", False), (r"\(3\)", False), (r"\(-2\)", False)],
            "explanation": r"Slope \(= \frac{y_2 - y_1}{x_2 - x_1} = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2\).",
        },
    ],
    "essays": [
        {
            "text": (
                r"A cylindrical water tank has a radius of \(2\,\text{m}\) and a height of \(5\,\text{m}\). "
                r"Explain step by step how to find its volume, state the formula you use and why, and give "
                r"the answer in terms of \(\pi\) and as a decimal (use \(\pi \approx 3.14\))."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full marks for: (1) identifying the cylinder volume formula \(V = \pi r^2 h\) and explaining "
                r"it as base area times height; (2) substituting \(r = 2, h = 5\); "
                r"(3) computing \(V = \pi (2)^2 (5) = 20\pi \approx 62.8\,\text{m}^3\). "
                "Deduct for using diameter instead of radius or arithmetic errors."
            ),
        },
    ],
}


STATS_COURSE = {
    "title": "GED Math: Data, Statistics & Probability",
    "slug": "ged-data-stats-probability",
    "program": "GED",
    "subject": "math",
    "description": (
        "Data is everywhere — in the news, in sports, in your bank app. This course teaches you to "
        "read graphs critically, summarize a set of numbers with averages, and reason about chance. "
        "Every concept is tied to everyday situations so the numbers actually mean something."
    ),
    "lessons": [
        (
            "1. Reading Graphs & Tables",
            r"Before any calculation, the GED tests whether you can *read* data correctly. The three most common formats:" "\n\n"
            r"**Bar graphs** compare separate categories — the taller the bar, the bigger the value. Each bar stands alone." "\n\n"
            r"[[figure:bar_toppings|A bar graph: each bar's height shows how many students chose that topping.]]" "\n\n"
            r"**Line graphs** show change over time — follow the line up or down to see a trend. **Tables** list exact numbers in rows and columns." "\n\n"
            r"[[figure:line_sales|A line graph: the upward trend shows sales growing month to month.]]" "\n\n"
            r"Your first move with any graph: read the **title**, the **axis labels**, and the **scale**. A chart can look dramatic only because its scale starts at 90 instead of 0." "\n\n"
            r"Example: from the line graph above, sales rise from \(\$200\) in January to \(\$350\) in February, an increase of \(350 - 200 = \$150\)." "\n\n"
            r"⚠️ Common mistake: forgetting the scale. If each grid line equals 50 units, a bar two lines tall represents 100, not 2.",
        ),
        (
            "2. Mean, Median, Mode & Range",
            r"These four 'summary numbers' describe a whole data set with a single value." "\n\n"
            r"**Mean** (the average): add everything up and divide by how many values there are." "\n"
            r"\[ \text{mean} = \frac{\text{sum of values}}{\text{number of values}}. \]" "\n"
            r"For \(4, 8, 6, 2\): \(\frac{4+8+6+2}{4} = \frac{20}{4} = 5\)." "\n\n"
            r"[[figure:mean_bars|The four bars are the data values; the dashed red line is the mean. It sits in the 'balance point' of the data.]]" "\n\n"
            r"**Median** (the middle): put the numbers *in order* and take the middle one. For \(2, 4, 6, 8\) (an even count) average the two middle values: \(\frac{4+6}{2} = 5\)." "\n\n"
            r"**Mode**: the value that appears most often. **Range**: the spread, \(\text{largest} - \text{smallest}\)." "\n\n"
            r"💡 Tip: the median is more trustworthy than the mean when one extreme value (like a billionaire in an income list) would otherwise drag the average up.",
        ),
        (
            "3. The Idea of Probability",
            r"Probability measures how likely something is, on a scale from \(0\) (impossible) to \(1\) (certain). It is a fraction:" "\n"
            r"\[ P(\text{event}) = \frac{\text{number of favorable outcomes}}{\text{total number of outcomes}}. \]" "\n"
            r"Rolling a fair die and getting a 4: there is \(1\) favorable outcome out of \(6\) equally likely outcomes, so \(P = \frac{1}{6}\)." "\n\n"
            r"Getting an even number (2, 4, or 6): \(P = \frac{3}{6} = \frac{1}{2}\)." "\n\n"
            r"[[figure:prob_scale|Every probability lives between 0 (impossible) and 1 (certain). Rolling an even number sits right in the middle at ½.]]" "\n\n"
            r"You can express probability as a fraction, a decimal, or a percent: \(\frac{1}{2} = 0.5 = 50\%\)." "\n\n"
            r"⚠️ Common mistake: assuming outcomes are equally likely when they aren't. The formula above only works when every outcome has the same chance.",
        ),
        (
            "4. Combining Probabilities",
            r"Two quick rules cover most GED questions." "\n\n"
            r"**'AND' (independent events) → multiply.** The chance of two unrelated things both happening is the product of their chances. Flipping two heads in a row: \(\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}\)." "\n\n"
            r"[[figure:coin_tree|The tree shows all four equally likely outcomes of two flips. Only one branch is HH, so its probability is ¼.]]" "\n\n"
            r"**'OR' (mutually exclusive events) → add.** The chance of one *or* another of two outcomes that can't happen together is the sum. Rolling a 1 or a 2 on a die: \(\frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}\)." "\n\n"
            r"**Complement:** the chance an event does *not* happen is \(1 - P(\text{event})\). If rain is \(70\%\) likely, no rain is \(1 - 0.70 = 0.30 = 30\%\)." "\n\n"
            r"💡 Tip: scan the wording. 'Both / and' usually means multiply; 'either / or' usually means add.",
        ),
    ],
    "mcqs": [
        {
            "text": r"Find the mean (average) of \(4,\ 8,\ 6,\ 2\).",
            "difficulty": 1,
            "choices": [(r"\(5\)", True), (r"\(6\)", False), (r"\(20\)", False), (r"\(4\)", False)],
            "explanation": r"Mean \(= \frac{4+8+6+2}{4} = \frac{20}{4} = 5\).",
        },
        {
            "text": r"Find the median of \(3,\ 9,\ 1,\ 7,\ 5\).",
            "difficulty": 2,
            "choices": [(r"\(5\)", True), (r"\(7\)", False), (r"\(1\)", False), (r"\(9\)", False)],
            "explanation": r"Order them: \(1, 3, 5, 7, 9\). The middle value (3rd of 5) is \(5\).",
        },
        {
            "text": r"What is the range of \(12,\ 4,\ 20,\ 8\)?",
            "difficulty": 1,
            "choices": [(r"\(16\)", True), (r"\(20\)", False), (r"\(8\)", False), (r"\(11\)", False)],
            "explanation": r"Range \(= \text{largest} - \text{smallest} = 20 - 4 = 16\).",
        },
        {
            "text": r"A fair six-sided die is rolled. What is the probability of rolling an even number?",
            "difficulty": 1,
            "choices": [(r"\(\frac{1}{2}\)", True), (r"\(\frac{1}{6}\)", False),
                        (r"\(\frac{1}{3}\)", False), (r"\(\frac{2}{3}\)", False)],
            "explanation": r"Even outcomes are 2, 4, 6 — that's 3 out of 6. \(P = \frac{3}{6} = \frac{1}{2}\).",
        },
        {
            "text": r"A bag has 3 red and 2 blue marbles. What is the probability of drawing a red marble?",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{5}\)", True), (r"\(\frac{2}{5}\)", False),
                        (r"\(\frac{3}{2}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"There are \(3 + 2 = 5\) marbles total, 3 of them red. \(P(\text{red}) = \frac{3}{5}\).",
        },
        {
            "text": r"You flip a fair coin twice. What is the probability of getting heads both times?",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{1}{2}\)", False),
                        (r"\(\frac{2}{1}\)", False), (r"\(1\)", False)],
            "explanation": r"'Both' means multiply independent probabilities: \(\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}\).",
        },
        {
            "text": r"The probability of rain tomorrow is \(70\%\). What is the probability it does NOT rain?",
            "difficulty": 1,
            "choices": [(r"\(30\%\)", True), (r"\(70\%\)", False), (r"\(0\%\)", False), (r"\(100\%\)", False)],
            "explanation": r"The complement: \(1 - 0.70 = 0.30 = 30\%\).",
        },
        {
            "text": ("Use the bar graph.\n\n"
                     "[[figure:bar_toppings|Pizza toppings chosen by 20 students]]\n\n"
                     "How many more students chose cheese than chose veggie?"),
            "difficulty": 1,
            "choices": [(r"\(4\)", True), (r"\(8\)", False), (r"\(12\)", False), (r"\(2\)", False)],
            "explanation": r"Cheese was chosen by 8 students and veggie by 4, a difference of \(8 - 4 = 4\). The trap 12 adds the two bars. Pro tip: 'how many more' means subtract the two bar heights.",
        },
        {
            "text": ("Use the scatterplot.\n\n"
                     "[[figure:scatter_trend|A scatterplot with a trend line]]\n\n"
                     "What kind of association between x and y does the graph show?"),
            "difficulty": 2,
            "choices": [("A positive association", True), ("A negative association", False),
                        ("No association", False), ("A causal relationship", False)],
            "explanation": r"The points and the trend line rise from left to right, so as x increases y tends to increase -- a positive association. (A trend is not proof of cause.) Pro tip: trend line up = positive; down = negative.",
        },
        {
            "text": ("Use the box plot.\n\n"
                     "[[figure:box_plot|A box plot]]\n\n"
                     "What does the line inside the box represent?"),
            "difficulty": 2,
            "choices": [("The median", True), ("The mean", False), ("The maximum", False), ("The range", False)],
            "explanation": r"The line dividing the box marks the median, the middle value of the data. The whisker ends show the minimum and maximum. Pro tip: the box's center line is always the median.",
        },
    ],
    "essays": [
        {
            "text": (
                r"A student's five test scores are \(70, 85, 90, 75, 80\). "
                r"Find both the mean and the median, show your work, and explain in a sentence what each "
                r"number tells you about the student's performance."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full marks for: (1) mean \(= \frac{70+85+90+75+80}{5} = \frac{400}{5} = 80\); "
                r"(2) ordering \(70, 75, 80, 85, 90\) and identifying the median as \(80\); "
                r"(3) a sentence explaining the mean as the average and the median as the middle score. "
                "Deduct for arithmetic errors or not ordering before finding the median."
            ),
        },
    ],
}


COURSES = [
    NUMBER_SENSE_MEASUREMENT_COURSE,
    INTEGER_RATIONAL_OPERATIONS_COURSE,
    ORDER_OPERATIONS_FORMULA_SKILLS_COURSE,
    RATIOS_PROPORTIONS_SCALE_COURSE,
    FRACTIONS_COURSE,
    GEOMETRY_COURSE,
    DATA_STATS_PROBABILITY_COURSE,
]


class Command(BaseCommand):
    help = "Create seven explanation-rich GED Math courses with practice questions."

    def handle(self, *args, **options):
        for data in COURSES:
            Course.objects.filter(slug=data["slug"]).delete()  # idempotent
            course = Course.objects.create(
                title=data["title"],
                slug=data["slug"],
                program=data["program"],
                subject=data.get("subject", "math"),
                description=data["description"],
            )
            for i, (title, content) in enumerate(data["lessons"], start=1):
                Lesson.objects.create(course=course, title=title, content=content, order=i)

            for q in data["mcqs"]:
                question = Question.objects.create(
                    course=course, qtype="mcq", text=q["text"],
                    difficulty=q["difficulty"], explanation=q["explanation"],
                )
                for text, correct in q["choices"]:
                    Choice.objects.create(question=question, text=text, is_correct=correct)

            # Phase 1 is MCQ-only: written-response prompts are not seeded.

            self.stdout.write(self.style.SUCCESS(
                f"Created '{course.title}' — "
                f"{course.lessons.count()} lessons, {course.questions.count()} questions."
            ))

        self.stdout.write(self.style.SUCCESS("All GED Math curriculum courses seeded."))
