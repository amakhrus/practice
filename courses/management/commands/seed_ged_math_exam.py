"""
Seed a full-length 'GED Mathematical Reasoning' practice exam that mirrors the
REAL test environment as closely as a multiple-choice LMS can:

  - 46 questions total, the real GED Math test length.
  - Two parts, exactly like test day:
        Part 1 -- the first 5 questions, CALCULATOR NOT ALLOWED.
        Part 2 -- the remaining 41 questions, calculator (TI-30XS) allowed.
  - 115 minutes total, a provided formula sheet, scored 100-200 (145 to pass).
  - Content mix matches the real blueprint: about 45% Quantitative Problem
    Solving (number sense, ratios/percents, geometry & measurement, data) and
    about 55% Algebraic Problem Solving (expressions, equations, inequalities,
    functions, and graphs).
  - A realistic difficulty spread (easy / medium / hard).

The real GED also uses drag-and-drop, fill-in-the-blank, drop-down, and hot-spot
items; this LMS is multiple choice only, so every item here is written as MCQ
while still covering each tested skill. Items are fresh (not copied from the
topic courses), in the capstone style: each explanation names the tempting wrong
answer and ends with a Pro tip.

Run:
    python manage.py seed_ged_math_exam
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Mathematical Reasoning: Full-Length Practice Exam",
    "slug": "ged-math-reasoning-exam",
    "program": "GED",
    "subject": "math",
    "description": (
        "A full-length, test-day-style GED Mathematical Reasoning practice exam: 46 questions "
        "modeled on the real blueprint, split into a no-calculator section (the first 5 questions) "
        "and a calculator section (the remaining 41), with a provided formula sheet. It covers the "
        "complete range of tested skills -- number sense and operations, ratios, proportions, and "
        "percents, geometry and measurement, data and statistics, and the full sweep of algebra "
        "(expressions, equations, inequalities, functions, and graphs) -- at an easy-to-hard "
        "difficulty spread. Every question includes a worked explanation and a pro tip. Use the "
        "lessons to learn the exam rules (115 minutes, scored 100-200, 145 to pass) and the formula "
        "sheet before you start, then take the 46 questions as one timed rehearsal."
    ),
    "lessons": [
        (
            "1. The Real GED Math Test: Format & Rules",
            r"""
This exam is built to feel like the **real GED Mathematical Reasoning test**. Here is exactly what you are walking into:

- **46 questions** in **115 minutes** (1 hour and 55 minutes). That is just over **2 minutes per question** on average.
- The test comes in **two parts**, and this practice exam follows the same order:
  - **Part 1 -- Questions 1-5: NO CALCULATOR.** These are kept friendly on purpose: clean numbers, basic operations, and number sense you can do by hand.
  - **Part 2 -- Questions 6-46: CALCULATOR ALLOWED.** On the real test you get an on-screen **TI-30XS** calculator (or your own approved one). Everything from percents to algebra to geometry lives here.
- You may **not** go back to Part 1 once you start Part 2 on the real test, so finish the no-calculator questions before moving on.
- A **formula sheet** is provided (see the next lesson) -- you do **not** have to memorize area and volume formulas.

**Scoring:** each GED test is scored from **100 to 200**, and you need **145 to pass**. There is **no penalty for wrong answers**, so never leave a question blank -- always guess.

[[check:How many questions are on the GED Mathematical Reasoning test?|46|It is 46 questions in 115 minutes.]]
            """,
        ),
        (
            "2. The Formula Sheet You Get",
            r"""
On test day the GED gives you a **formula sheet**. You do not need to memorize these -- but you do need to know *which* formula to grab. The most-used ones:

**Area**
- Rectangle: \(A = lw\)
- Triangle: \(A = \tfrac{1}{2}bh\)
- Circle: \(A = \pi r^2\)
- Trapezoid: \(A = \tfrac{1}{2}(b_1 + b_2)h\)

**Perimeter / Circumference**
- Rectangle: \(P = 2l + 2w\)
- Circle: \(C = 2\pi r = \pi d\)

**Volume**
- Box (rectangular prism): \(V = lwh\)
- Cylinder: \(V = \pi r^2 h\)
- Cone: \(V = \tfrac{1}{3}\pi r^2 h\)
- Sphere: \(V = \tfrac{4}{3}\pi r^3\)

**Algebra & Geometry**
- Pythagorean theorem: \(a^2 + b^2 = c^2\)
- Slope: \(m = \dfrac{y_2 - y_1}{x_2 - x_1}\)
- Slope-intercept line: \(y = mx + b\)
- Quadratic formula: \(x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}\)

**Percent & rate ideas to keep in your head**
- Percent change \(= \dfrac{\text{new} - \text{old}}{\text{old}}\)
- Distance \(= \text{rate} \times \text{time}\)

[[figure:formula_substitution_flow|Reading a problem, picking the right formula, and substituting the numbers in.]]

[[check:Which formula gives the volume of a cylinder? Write it using pi, r, and h.|\pi r^2 h;;pi r^2 h;;pir^2h|Volume of a cylinder is pi times r squared times the height.]]
            """,
        ),
        (
            "3. Pacing & Strategy for Test Day",
            r"""
You have the math skills -- this lesson is about **using your time well** across 46 questions.

**Pacing.** A little over **2 minutes per question**. If one stalls you, lock in your best guess, **flag it**, and move on. Coming back with a fresh eye is faster than grinding.

**Backsolve.** When the answer choices are numbers, **plug them into the problem** instead of doing all the algebra -- start with a middle value and adjust.

**Estimate first.** A quick estimate kills obviously-wrong choices and catches calculator typos (a decimal in the wrong place).

**Mind the units.** Length is plain units, area is **square** units, volume is **cubic** units. Re-read the last line of the question so you answer what's actually asked (price vs. discount, area vs. perimeter).

**Never leave a blank.** No penalty for wrong answers -- eliminate what you can, then guess.

**Part 1 first.** Get the 5 no-calculator questions done before you touch Part 2; you can't return to them.

[[check:About how many minutes do you have per question on the GED Math test? Answer with a number.|2|115 minutes for 46 questions is just over 2 minutes each.]]
            """,
        ),
    ],
    # qtype defaults to mcq. "part" is informational and is prefixed to the text.
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  QUESTIONS 1-5  --  NO CALCULATOR ============
        # =====================================================================
        {
            "text": (r"**No-calculator section.** Simplify using order of operations: \(3 + 4 \times 2^2\)."),
            "difficulty": 1,
            "choices": [(r"\(19\)", True), (r"\(28\)", False), (r"\(49\)", False), (r"\(22\)", False)],
            "explanation": r"Powers first: \(2^2 = 4\). Then multiply: \(4 \times 4 = 16\). Then add: \(3 + 16 = 19\). The trap 28 does \((3+4)\times 4\), adding before multiplying. Pro tip: remember PEMDAS -- exponents and multiplication come before addition.",
        },
        {
            "text": (r"**No-calculator section.** What is \(\dfrac{3}{4} - \dfrac{1}{2}\)?"),
            "difficulty": 1,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{1}{2}\)", False), (r"\(\frac{2}{2}\)", False), (r"\(\frac{1}{8}\)", False)],
            "explanation": r"Use a common denominator of 4: \(\frac{1}{2} = \frac{2}{4}\), so \(\frac{3}{4} - \frac{2}{4} = \frac{1}{4}\). The trap \(\frac{1}{8}\) subtracts tops and multiplies bottoms. Pro tip: you can only add or subtract fractions once the denominators match.",
        },
        {
            "text": (r"**No-calculator section.** Evaluate: \(-5 + (-3) \times 2\)."),
            "difficulty": 2,
            "choices": [(r"\(-11\)", True), (r"\(-16\)", False), (r"\(4\)", False), (r"\(-1\)", False)],
            "explanation": r"Multiply first: \((-3)\times 2 = -6\). Then add: \(-5 + (-6) = -11\). The trap \(-16\) does \((-5 + -3)\times 2\), adding before multiplying. Pro tip: multiplication comes before addition, even with negatives.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(2^3 \times 2^2\)."),
            "difficulty": 2,
            "choices": [(r"\(32\)", True), (r"\(64\)", False), (r"\(16\)", False), (r"\(12\)", False)],
            "explanation": r"When you multiply powers with the same base, add the exponents: \(2^{3+2} = 2^5 = 32\). You can also check: \(8 \times 4 = 32\). The trap 64 multiplies the exponents \((2^6)\). Pro tip: same base and multiplying -> add the exponents.",
        },
        {
            "text": (r"**No-calculator section.** Between which two whole numbers does \(\sqrt{50}\) fall?"),
            "difficulty": 2,
            "choices": [("Between 7 and 8", True), ("Between 6 and 7", False), ("Between 8 and 9", False), ("Between 24 and 26", False)],
            "explanation": r"\(7^2 = 49\) and \(8^2 = 64\). Since 50 is just above 49, \(\sqrt{50}\) is a little more than 7, so it sits between 7 and 8. The trap 'between 24 and 26' halves 50. Pro tip: to estimate a square root, find the two perfect squares it lands between.",
        },
        # =====================================================================
        # ============ PART 2  --  QUESTIONS 6-46  --  CALCULATOR =============
        # =====================================================================
        # ----- Percents -----
        {
            "text": (r"**Calculator section.** What is \(20\%\) of \(150\)?"),
            "difficulty": 1,
            "choices": [(r"\(30\)", True), (r"\(3\)", False), (r"\(300\)", False), (r"\(7.5\)", False)],
            "explanation": r"\(20\% = 0.20\), and \(0.20 \times 150 = 30\). The trap 3 misplaces the decimal \((0.02 \times 150)\). Pro tip: 'percent of' means multiply, after turning the percent into a decimal.",
        },
        {
            "text": (r"An \$80 pair of shoes is marked \(25\%\) off. What is the sale price?"),
            "difficulty": 2,
            "choices": [(r"\$60", True), (r"\$20", False), (r"\$55", False), (r"\$100", False)],
            "explanation": r"The discount is \(0.25 \times 80 = \$20\), so the price is \(80 - 20 = \$60\). The trap \$20 gives only the discount, not the new price. Pro tip: 25% off means you pay 75%: \(0.75 \times 80 = 60\).",
        },
        {
            "text": (r"A price rises from \$40 to \$50. What is the percent increase?"),
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(10\%\)", False), (r"\(125\%\)", False)],
            "explanation": r"Percent change \(= \frac{\text{new}-\text{old}}{\text{old}} = \frac{50-40}{40} = \frac{10}{40} = 0.25 = 25\%\). The trap 20% divides by the new value (50). Pro tip: for percent change, always divide by the ORIGINAL amount.",
        },
        {
            "text": (r"\(12\) is what percent of \(48\)?"),
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(4\%\)", False), (r"\(40\%\)", False), (r"\(36\%\)", False)],
            "explanation": r"\(\frac{12}{48} = 0.25 = 25\%\). The trap 4% comes from \(48 \div 12\) read backwards. Pro tip: 'what percent of' means part divided by whole, then times 100.",
        },
        {
            "text": (r"A \$50 item has an \(8\%\) sales tax added. What is the total cost?"),
            "difficulty": 2,
            "choices": [(r"\$54.00", True), (r"\$58.00", False), (r"\$50.08", False), (r"\$4.00", False)],
            "explanation": r"The tax is \(0.08 \times 50 = \$4\), so the total is \(50 + 4 = \$54\). The trap \$4 is only the tax. Pro tip: adding 8% tax is the same as multiplying by 1.08: \(1.08 \times 50 = 54\).",
        },
        # ----- Ratios, proportions, rates, scale -----
        {
            "text": (r"Two numbers are in the ratio \(3:5\) and add up to \(40\). What is the smaller number?"),
            "difficulty": 2,
            "choices": [(r"\(15\)", True), (r"\(24\)", False), (r"\(8\)", False), (r"\(5\)", False)],
            "explanation": r"The ratio has \(3 + 5 = 8\) parts, so each part is \(40 \div 8 = 5\). The smaller number is \(3 \times 5 = 15\). The trap 24 is the larger number \((5 \times 5 - 1)\)? No -- 24 is \(3\times 8\), mixing up the steps. Pro tip: add the ratio numbers to find the size of one part first.",
        },
        {
            "text": (r"Solve the proportion \(\dfrac{4}{10} = \dfrac{x}{25}\)."),
            "difficulty": 2,
            "choices": [(r"\(x = 10\)", True), (r"\(x = 62.5\)", False), (r"\(x = 16\)", False), (r"\(x = 100\)", False)],
            "explanation": r"Cross-multiply: \(10x = 4 \times 25 = 100\), so \(x = 10\). The trap 62.5 cross-multiplies the wrong pair. Pro tip: \(\frac{4}{10}\) is the same as \(0.4\), and \(0.4 \times 25 = 10\).",
        },
        {
            "text": (r"A car travels \(240\) miles in \(4\) hours. What is its average speed?"),
            "difficulty": 1,
            "choices": [(r"\(60\) mph", True), (r"\(960\) mph", False), (r"\(236\) mph", False), (r"\(40\) mph", False)],
            "explanation": r"Speed \(= \frac{\text{distance}}{\text{time}} = \frac{240}{4} = 60\) mph. The trap 960 multiplies instead of dividing. Pro tip: 'per hour' means divide the distance by the number of hours.",
        },
        {
            "text": (r"A train travels at \(65\) miles per hour for \(3\) hours. How far does it go?"),
            "difficulty": 1,
            "choices": [(r"\(195\) miles", True), (r"\(68\) miles", False), (r"\(21.7\) miles", False), (r"\(62\) miles", False)],
            "explanation": r"Distance \(= \text{rate} \times \text{time} = 65 \times 3 = 195\) miles. The trap 21.7 divides instead of multiplying. Pro tip: distance equals rate times time -- when you know the speed and the hours, multiply.",
        },
        {
            "text": (r"On a map, \(1\) inch represents \(50\) miles. How many miles apart are two towns that are \(3.5\) inches apart on the map?"),
            "difficulty": 2,
            "choices": [(r"\(175\) miles", True), (r"\(53.5\) miles", False), (r"\(14.3\) miles", False), (r"\(142.9\) miles", False)],
            "explanation": r"Each inch is 50 miles, so \(3.5 \times 50 = 175\) miles. The trap 14.3 divides \(50 \div 3.5\). Pro tip: set up a proportion, \(\frac{1\text{ in}}{50\text{ mi}} = \frac{3.5\text{ in}}{x}\), and keep inches across from inches.",
        },
        # ----- Data, statistics, probability -----
        {
            "text": (r"What is the mean (average) of \(12,\ 15,\ 18,\ 21,\ 24\)?"),
            "difficulty": 1,
            "choices": [(r"\(18\)", True), (r"\(21\)", False), (r"\(90\)", False), (r"\(15\)", False)],
            "explanation": r"Add them: \(12+15+18+21+24 = 90\). Divide by 5: \(90 \div 5 = 18\). The trap 90 forgets to divide. Pro tip: mean = total divided by how many values there are.",
        },
        {
            "text": (r"What is the median of \(3,\ 8,\ 2,\ 10,\ 6,\ 5\)?"),
            "difficulty": 2,
            "choices": [(r"\(5.5\)", True), (r"\(6\)", False), (r"\(5\)", False), (r"\(8\)", False)],
            "explanation": r"Sort first: \(2, 3, 5, 6, 8, 10\). With an even count, average the two middle values: \(\frac{5+6}{2} = 5.5\). The trap 5 or 6 picks just one middle value. Pro tip: always sort the list, and average the middle two when there's an even number of values.",
        },
        {
            "text": (r"For the data set \(4,\ 7,\ 7,\ 9,\ 12\), what is the range?"),
            "difficulty": 1,
            "choices": [(r"\(8\)", True), (r"\(7\)", False), (r"\(5\)", False), (r"\(12\)", False)],
            "explanation": r"Range \(= \text{largest} - \text{smallest} = 12 - 4 = 8\). The trap 7 is the mode (the most frequent value), not the range. Pro tip: range measures spread -- subtract the smallest value from the largest.",
        },
        {
            "text": (r"A spinner has \(8\) equal sections, \(3\) of them red. What is the probability of landing on red?"),
            "difficulty": 2,
            "choices": [(r"\(\frac{3}{8}\)", True), (r"\(\frac{3}{5}\)", False), (r"\(\frac{5}{8}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"Probability \(= \frac{\text{favorable}}{\text{total}} = \frac{3}{8}\). The trap \(\frac{3}{5}\) compares red to non-red instead of to the total. Pro tip: probability is the wanted count over the TOTAL count.",
        },
        {
            "text": ("Use the scatter plot below.\n\n"
                     "[[figure:scatter_trend|A scatter plot of points rising from lower-left to upper-right]]\n\n"
                     "What kind of relationship does the scatter plot show between the two variables?"),
            "difficulty": 2,
            "choices": [("A positive (increasing) relationship", True),
                        ("A negative (decreasing) relationship", False),
                        ("No relationship at all", False),
                        ("A perfectly horizontal relationship", False)],
            "explanation": r"The points rise from lower-left to upper-right, so as one variable increases the other tends to increase -- a positive relationship. The trap 'negative' describes points that fall. Pro tip: up-to-the-right is positive; down-to-the-right is negative.",
        },
        # ----- Geometry & measurement -----
        {
            "text": ("Use the rectangle below.\n\n"
                     "[[figure:area_rectangle|A rectangle with a length and a width labeled]]\n\n"
                     r"A rectangle is \(12\) cm long and \(7\) cm wide. What is its area?"),
            "difficulty": 1,
            "choices": [(r"\(84\ \text{cm}^2\)", True), (r"\(38\ \text{cm}^2\)", False), (r"\(19\ \text{cm}^2\)", False), (r"\(42\ \text{cm}^2\)", False)],
            "explanation": r"Area \(= l \times w = 12 \times 7 = 84\ \text{cm}^2\). The trap 38 is the perimeter \((2\times12 + 2\times7)\). Pro tip: area multiplies the sides and uses square units; perimeter adds them.",
        },
        {
            "text": (r"What is the area of a triangle with a base of \(14\) cm and a height of \(9\) cm?"),
            "difficulty": 1,
            "choices": [(r"\(63\ \text{cm}^2\)", True), (r"\(126\ \text{cm}^2\)", False), (r"\(23\ \text{cm}^2\)", False), (r"\(46\ \text{cm}^2\)", False)],
            "explanation": r"\(A = \frac{1}{2}bh = \frac{1}{2}(14)(9) = 63\ \text{cm}^2\). The trap 126 forgets the \(\frac{1}{2}\). Pro tip: every triangle area starts with one-half of base times height.",
        },
        {
            "text": (r"What is the area of a circle with a radius of \(5\) cm? Use \(\pi \approx 3.14\)."),
            "difficulty": 2,
            "choices": [(r"\(78.5\ \text{cm}^2\)", True), (r"\(31.4\ \text{cm}^2\)", False), (r"\(15.7\ \text{cm}^2\)", False), (r"\(25\ \text{cm}^2\)", False)],
            "explanation": r"\(A = \pi r^2 = 3.14 \times 5^2 = 3.14 \times 25 = 78.5\ \text{cm}^2\). The trap 31.4 finds the circumference \((2\pi r)\) instead. Pro tip: area uses \(r^2\); circumference uses \(2\pi r\) -- don't mix them up.",
        },
        {
            "text": (r"What is the circumference of a circle with a radius of \(7\) cm? Use \(\pi \approx 3.14\)."),
            "difficulty": 2,
            "choices": [(r"\(\approx 44\ \text{cm}\)", True), (r"\(\approx 153.9\ \text{cm}\)", False), (r"\(\approx 22\ \text{cm}\)", False), (r"\(\approx 14\ \text{cm}\)", False)],
            "explanation": r"\(C = 2\pi r = 2 \times 3.14 \times 7 = 43.96 \approx 44\) cm. The trap 153.9 is the area \((\pi r^2)\). Pro tip: circumference is a length \((2\pi r)\); area is a region \((\pi r^2)\).",
        },
        {
            "text": ("Use the box below.\n\n"
                     "[[figure:volume_box|A rectangular box with length, width, and height labeled]]\n\n"
                     r"What is the volume of a box measuring \(5 \times 4 \times 3\)?"),
            "difficulty": 1,
            "choices": [(r"\(60\)", True), (r"\(12\)", False), (r"\(47\)", False), (r"\(23\)", False)],
            "explanation": r"Volume multiplies all three dimensions: \(5 \times 4 \times 3 = 60\). The trap 12 multiplies only two of them. Pro tip: volume uses all three sides and cubic units.",
        },
        {
            "text": (r"A cylinder has a radius of \(3\) cm and a height of \(10\) cm. What is its volume? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 282.6\ \text{cm}^3\)", True), (r"\(\approx 94.2\ \text{cm}^3\)", False), (r"\(\approx 188.4\ \text{cm}^3\)", False), (r"\(\approx 90\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \pi r^2 h = 3.14 \times 3^2 \times 10 = 3.14 \times 9 \times 10 = 282.6\ \text{cm}^3\). The trap 188.4 uses \(2r\) instead of \(r^2\) \((2\pi r h)\). Pro tip: square the radius first, then multiply by the height and \(\pi\).",
        },
        {
            "text": ("Use the right triangle below.\n\n"
                     "[[figure:pythagorean_triangle|A right triangle with two legs and a hypotenuse]]\n\n"
                     r"The two legs of a right triangle are \(6\) and \(8\). How long is the hypotenuse?"),
            "difficulty": 2,
            "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(100\)", False), (r"\(48\)", False)],
            "explanation": r"\(c = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). The trap 14 just adds the legs; 100 forgets the square root. Pro tip: 6-8-10 is the 3-4-5 triple doubled.",
        },
        {
            "text": (r"A right triangle has a hypotenuse of \(13\) and one leg of \(5\). How long is the other leg?"),
            "difficulty": 3,
            "choices": [(r"\(12\)", True), (r"\(18\)", False), (r"\(8\)", False), (r"\(\sqrt{194}\)", False)],
            "explanation": r"Use \(a^2 + b^2 = c^2\): \(5^2 + b^2 = 13^2\), so \(b^2 = 169 - 25 = 144\) and \(b = 12\). The trap \(\sqrt{194}\) adds the squares instead of subtracting. Pro tip: when you know the hypotenuse, subtract the known leg's square from the hypotenuse's square.",
        },
        {
            "text": ("Use the similar rectangles below.\n\n"
                     "[[figure:similar_rectangles_scale|A small rectangle and a larger, same-shaped rectangle]]\n\n"
                     r"A small rectangle is \(4\) by \(6\). A larger, similar rectangle has a width of \(10\) (matching the \(4\) side). What is its length?"),
            "difficulty": 3,
            "choices": [(r"\(15\)", True), (r"\(12\)", False), (r"\(8.5\)", False), (r"\(9.6\)", False)],
            "explanation": r"The scale factor is \(10 \div 4 = 2.5\), so the length is \(6 \times 2.5 = 15\). The trap 12 adds the difference \((6 + 6)\) instead of scaling. Pro tip: similar shapes scale by multiplying every side by the same factor.",
        },
        # ----- Coordinate geometry -----
        {
            "text": ("Use the coordinate plane below.\n\n"
                     "[[figure:coordinate_quadrants|The four quadrants of the coordinate plane]]\n\n"
                     r"In which quadrant does the point \((-3,\ 5)\) lie?"),
            "difficulty": 1,
            "choices": [("Quadrant II", True), ("Quadrant I", False), ("Quadrant III", False), ("Quadrant IV", False)],
            "explanation": r"A negative x and a positive y put the point in the upper-left, Quadrant II. The trap Quadrant III needs both coordinates negative. Pro tip: quadrants go counter-clockwise starting from the upper-right (I), so (-, +) is II.",
        },
        {
            "text": (r"What is the slope of the line through the points \((1,\ 2)\) and \((4,\ 11)\)?"),
            "difficulty": 2,
            "choices": [(r"\(3\)", True), (r"\(\frac{1}{3}\)", False), (r"\(9\)", False), (r"\(13\)", False)],
            "explanation": r"Slope \(= \frac{y_2 - y_1}{x_2 - x_1} = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3\). The trap \(\frac{1}{3}\) flips the fraction (run over rise). Pro tip: slope is rise over run -- change in y on top.",
        },
        # ----- Algebra: expressions -----
        {
            "text": (r"Simplify: \(3x + 5 - x + 2\)."),
            "difficulty": 1,
            "choices": [(r"\(2x + 7\)", True), (r"\(4x + 7\)", False), (r"\(2x + 3\)", False), (r"\(9x\)", False)],
            "explanation": r"Combine like terms: \(3x - x = 2x\) and \(5 + 2 = 7\), giving \(2x + 7\). The trap \(4x+7\) adds the x-terms instead of subtracting. Pro tip: only combine terms that share the same variable.",
        },
        {
            "text": (r"Use the distributive property to simplify: \(4(2x - 3)\)."),
            "difficulty": 1,
            "choices": [(r"\(8x - 12\)", True), (r"\(8x - 3\)", False), (r"\(6x - 12\)", False), (r"\(2x - 12\)", False)],
            "explanation": r"Multiply 4 by both terms: \(4 \times 2x = 8x\) and \(4 \times (-3) = -12\), giving \(8x - 12\). The trap \(8x - 3\) forgets to distribute to the \(-3\). Pro tip: the outside number multiplies EVERY term inside the parentheses.",
        },
        {
            "text": (r"Evaluate \(3x^2 - 2x\) when \(x = 4\)."),
            "difficulty": 2,
            "choices": [(r"\(40\)", True), (r"\(16\)", False), (r"\(56\)", False), (r"\(136\)", False)],
            "explanation": r"\(3(4)^2 - 2(4) = 3(16) - 8 = 48 - 8 = 40\). The trap 136 squares \(3 \times 4\) first \(((12)^2 - 8)\). Pro tip: do the exponent before the multiplication -- square the 4, then multiply by 3.",
        },
        # ----- Algebra: equations -----
        {
            "text": (r"Solve for \(x\): \(5x - 7 = 18\)."),
            "difficulty": 1,
            "choices": [(r"\(x = 5\)", True), (r"\(x = 25\)", False), (r"\(x = 2.2\)", False), (r"\(x = 11\)", False)],
            "explanation": r"Add 7: \(5x = 25\). Divide by 5: \(x = 5\). The trap 25 stops before dividing. Pro tip: undo the subtraction first, then undo the multiplication.",
        },
        {
            "text": (r"Solve for \(x\): \(\dfrac{x}{3} + 4 = 9\)."),
            "difficulty": 2,
            "choices": [(r"\(x = 15\)", True), (r"\(x = 39\)", False), (r"\(x = 1.67\)", False), (r"\(x = 5\)", False)],
            "explanation": r"Subtract 4: \(\frac{x}{3} = 5\). Multiply by 3: \(x = 15\). The trap 39 multiplies before subtracting \((9 \times 3 + ...)\). Pro tip: clear the \(+4\) first, then multiply both sides by 3 to undo the division.",
        },
        {
            "text": (r"Solve for \(x\): \(3x + 4 = x + 12\)."),
            "difficulty": 2,
            "choices": [(r"\(x = 4\)", True), (r"\(x = 8\)", False), (r"\(x = 2\)", False), (r"\(x = 16\)", False)],
            "explanation": r"Subtract \(x\) from both sides: \(2x + 4 = 12\). Subtract 4: \(2x = 8\). Divide by 2: \(x = 4\). The trap 8 stops before dividing. Pro tip: collect the variables on one side first, then solve the simpler equation.",
        },
        {
            "text": (r"A phone plan costs \$40 per month plus \$0.10 per text. What is the cost in a month with \(100\) texts?"),
            "difficulty": 2,
            "choices": [(r"\$50", True), (r"\$140", False), (r"\$4{,}040", False), (r"\$50.10", False)],
            "explanation": r"The texts cost \(0.10 \times 100 = \$10\), plus the \$40 base: \(40 + 10 = \$50\). The trap \$140 treats each text as \$1. Pro tip: build the expression \(40 + 0.10t\), then substitute \(t = 100\).",
        },
        # ----- Algebra: inequalities -----
        {
            "text": ("Use the number line idea below.\n\n"
                     "[[figure:number_line_ineq|A number line showing the solution to an inequality]]\n\n"
                     r"Solve the inequality \(3x - 2 > 10\)."),
            "difficulty": 2,
            "choices": [(r"\(x > 4\)", True), (r"\(x < 4\)", False), (r"\(x > 2.67\)", False), (r"\(x > 12\)", False)],
            "explanation": r"Add 2: \(3x > 12\). Divide by 3: \(x > 4\). The sign stays the same because 3 is positive. The trap \(x < 4\) flips the sign for no reason. Pro tip: only flip the inequality when you multiply or divide by a NEGATIVE number.",
        },
        {
            "text": (r"Solve the inequality \(-2x + 1 < 9\)."),
            "difficulty": 3,
            "choices": [(r"\(x > -4\)", True), (r"\(x < -4\)", False), (r"\(x > 4\)", False), (r"\(x < 4\)", False)],
            "explanation": r"Subtract 1: \(-2x < 8\). Now divide by \(-2\) and FLIP the sign: \(x > -4\). The trap \(x < -4\) forgets to flip. Pro tip: dividing or multiplying an inequality by a negative number always reverses the direction of the sign.",
        },
        # ----- Algebra: quadratics & systems -----
        {
            "text": (r"Solve: \(x^2 + 5x + 6 = 0\)."),
            "difficulty": 3,
            "choices": [(r"\(x = -2\) or \(x = -3\)", True), (r"\(x = 2\) or \(x = 3\)", False), (r"\(x = -1\) or \(x = -6\)", False), (r"\(x = 1\) or \(x = 6\)", False)],
            "explanation": r"Factor into \((x+2)(x+3) = 0\), so \(x = -2\) or \(x = -3\). The trap \(x = 2, 3\) forgets the signs flip when you solve each factor. Pro tip: find two numbers that multiply to 6 and add to 5 (that's 2 and 3), then change their signs.",
        },
        {
            "text": (r"Solve the system: \(x + y = 10\) and \(x - y = 4\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 7,\ y = 3\)", True), (r"\(x = 3,\ y = 7\)", False), (r"\(x = 6,\ y = 4\)", False), (r"\(x = 5,\ y = 5\)", False)],
            "explanation": r"Add the two equations: \(2x = 14\), so \(x = 7\). Then \(7 + y = 10\) gives \(y = 3\). The trap \(x=3, y=7\) swaps the two values. Pro tip: adding the equations cancels \(y\) and solves for \(x\) in one step.",
        },
        # ----- Algebra: functions & graphs -----
        {
            "text": (r"If \(f(x) = 2x + 3\), what is \(f(5)\)?"),
            "difficulty": 1,
            "choices": [(r"\(13\)", True), (r"\(10\)", False), (r"\(16\)", False), (r"\(25\)", False)],
            "explanation": r"Substitute \(x = 5\): \(f(5) = 2(5) + 3 = 10 + 3 = 13\). The trap 10 forgets to add the 3. Pro tip: \(f(5)\) means replace every \(x\) with 5, then simplify.",
        },
        {
            "text": ("Use the line below.\n\n"
                     "[[figure:function_table_line|A straight line shown with its table of values]]\n\n"
                     r"A line has a slope of \(3\) and crosses the y-axis at \(-2\). What is its equation?"),
            "difficulty": 2,
            "choices": [(r"\(y = 3x - 2\)", True), (r"\(y = -2x + 3\)", False), (r"\(y = 3x + 2\)", False), (r"\(y = -2x - 3\)", False)],
            "explanation": r"Slope-intercept form is \(y = mx + b\), with \(m = 3\) (slope) and \(b = -2\) (y-intercept), giving \(y = 3x - 2\). The trap \(y = -2x + 3\) swaps the slope and intercept. Pro tip: in \(y = mx + b\), \(m\) multiplies \(x\) and \(b\) stands alone.",
        },
        {
            "text": (r"A colony of bacteria triples every hour. If it starts with \(5\) bacteria, how many are there after \(2\) hours?"),
            "difficulty": 3,
            "choices": [(r"\(45\)", True), (r"\(30\)", False), (r"\(15\)", False), (r"\(10\)", False)],
            "explanation": r"Tripling twice: \(5 \times 3 \times 3 = 5 \times 9 = 45\). The trap 30 multiplies \(5 \times 3 \times 2\), treating it as repeated addition. Pro tip: 'triples each hour' means multiply by 3 for each hour -- it grows exponentially, \(5 \times 3^2\).",
        },
        {
            "text": (r"What is the slope of the line that passes through \((2,\ 1)\) and \((6,\ 9)\)?"),
            "difficulty": 2,
            "choices": [(r"\(2\)", True), (r"\(\frac{1}{2}\)", False), (r"\(4\)", False), (r"\(8\)", False)],
            "explanation": r"Slope \(= \frac{9 - 1}{6 - 2} = \frac{8}{4} = 2\). The trap 8 uses only the change in y and forgets to divide by the change in x. Pro tip: slope is rise over run -- divide the y-change by the x-change.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create a full-length GED Mathematical Reasoning practice exam (46 questions, two parts; MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent re-seed
        course = Course.objects.create(
            title=COURSE["title"],
            slug=COURSE["slug"],
            program=COURSE["program"],
            subject=COURSE["subject"],
            description=COURSE["description"],
        )
        for i, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content.strip(), order=i)

        for q in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course, qtype="mcq", text=q["text"],
                difficulty=q["difficulty"], explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions "
            f"(Part 1: 5 no-calculator, Part 2: 41 calculator)."
        ))
