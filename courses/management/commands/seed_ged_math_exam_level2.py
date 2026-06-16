"""
Seed a SECOND full-length 'GED Mathematical Reasoning' practice exam -- Level 2,
a harder companion to ``seed_ged_math_exam``.

Same test-day structure as Level 1 (46 questions, 115 minutes, a no-calculator
Part 1 of 5 items then a calculator Part 2 of 41, formula sheet provided, scored
100-200 with 145 to pass), but the items are noticeably tougher:

  - No 'easy' questions -- every item is medium or hard.
  - More multi-step work: successive percents, reverse percents, combined ratios,
    work/rate problems, unit conversions, weighted means, probability without
    replacement, cones/spheres/surface area, area ratios of similar figures,
    quadratics, rational equations, compound inequalities, and exponential models.

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip.

Run:
    python manage.py seed_ged_math_exam_level2
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Mathematical Reasoning: Full-Length Practice Exam (Level 2 - Advanced)",
    "slug": "ged-math-reasoning-exam-level2",
    "program": "GED",
    "subject": "math",
    "description": (
        "A tougher, second full-length GED Mathematical Reasoning practice exam for students who have "
        "cleared the Level 1 test. Same test-day format -- 46 questions in 115 minutes, a no-calculator "
        "Part 1 (the first 5 questions) then a calculator Part 2, with a provided formula sheet, scored "
        "100-200 (145 to pass) -- but every item is medium or hard. It pushes into the multi-step skills "
        "the GED saves for its toughest questions: successive and reverse percents, combined ratios and "
        "work-rate problems, unit conversions, weighted means and probability without replacement, "
        "cones, spheres and surface area, area ratios of similar figures, quadratics and rational "
        "equations, compound inequalities, and exponential growth models. Every question includes a "
        "worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 2: What's Different",
            r"""
This is the **advanced** GED Mathematical Reasoning practice exam. The format is identical to the real test and to Level 1:

- **46 questions** in **115 minutes** -- just over 2 minutes each.
- **Part 1 (Questions 1-5): NO CALCULATOR.** Still by-hand work, but with negative exponents, scientific notation, and order-of-operations traps.
- **Part 2 (Questions 6-46): CALCULATOR ALLOWED** (on-screen TI-30XS).
- A **formula sheet** is provided (next lesson), and you cannot return to Part 1 after starting Part 2.
- Scored **100-200**, and you need **145 to pass**. No penalty for wrong answers -- never leave a blank.

**What's harder here than Level 1:** these items are all **medium or hard**, and most take **several steps**. Expect to combine ideas -- a percent *and* a ratio, a formula *and* an equation. The single most useful habit on hard items is to **write down each step** instead of doing it all in your head.

[[check:On this exam, which part does NOT allow a calculator? Answer with the part number.|1;;part 1;;one|Part 1, the first five questions, is the no-calculator section.]]
            """,
        ),
        (
            "2. The Formula Sheet (incl. the harder formulas)",
            r"""
You get a **formula sheet** on test day -- the hard questions on this exam lean on the geometry and algebra formulas, so know which to grab.

**Area**
- Triangle: \(A = \tfrac{1}{2}bh\) | Trapezoid: \(A = \tfrac{1}{2}(b_1 + b_2)h\) | Circle: \(A = \pi r^2\)

**Volume**
- Cylinder: \(V = \pi r^2 h\)
- Cone: \(V = \tfrac{1}{3}\pi r^2 h\)
- Sphere: \(V = \tfrac{4}{3}\pi r^3\)

**Surface area**
- Cylinder: \(SA = 2\pi r^2 + 2\pi r h\)

**Algebra & coordinate geometry**
- Pythagorean theorem: \(a^2 + b^2 = c^2\)
- Distance: \(d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\)
- Midpoint: \(\left(\dfrac{x_1+x_2}{2},\ \dfrac{y_1+y_2}{2}\right)\)
- Slope: \(m = \dfrac{y_2-y_1}{x_2-x_1}\) | Perpendicular slopes multiply to \(-1\)
- Quadratic formula: \(x = \dfrac{-b \pm \sqrt{b^2-4ac}}{2a}\)

**Two facts the sheet won't state but you'll need:**
- For **similar figures**, areas scale by the **square** of the scale factor (and volumes by the **cube**).
- A repeated percent change of \(r\) over \(n\) periods multiplies by \((1+r)^n\).

[[figure:formula_substitution_flow|Pick the right formula, then substitute carefully -- most lost points on hard items are setup errors, not arithmetic.]]

[[check:Two similar triangles have a scale factor of 3. Their areas differ by a factor of what number?|9|Areas scale by the square of the scale factor, so 3 squared = 9.]]
            """,
        ),
        (
            "3. Strategy for Hard Items",
            r"""
Hard GED questions reward a calm, written process more than speed.

- **Show each step.** Multi-step items (percent-then-percent, ratio-then-total) are where careless mistakes live. One line per step.
- **Backsolve when you can.** If the choices are numbers, plug them into the original problem -- often faster than solving a quadratic or rational equation.
- **Estimate to catch calculator slips.** A quick estimate flags a decimal in the wrong place.
- **Watch the sign flip.** Multiplying or dividing an inequality by a negative reverses the direction.
- **Re-read the last line.** Hard problems often ask for the *original* price, the *largest* angle, or the *other* leg -- not the value you just computed.
- **Flag and move on.** Don't let one brutal question eat five minutes; guess, flag it, return later. No penalty for a wrong guess.

[[check:When you divide both sides of an inequality by a negative number, what must you do to the inequality sign?|flip;;reverse;;flip it;;switch it|Dividing by a negative reverses the direction of the inequality.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  QUESTIONS 1-5  --  NO CALCULATOR ============
        # =====================================================================
        {
            "text": (r"**No-calculator section.** Evaluate: \(-3^2 + (-2)^3\)."),
            "difficulty": 3,
            "choices": [(r"\(-17\)", True), (r"\(1\)", False), (r"\(17\)", False), (r"\(-1\)", False)],
            "explanation": r"By order of operations, \(-3^2\) means \(-(3^2) = -9\), and \((-2)^3 = -8\). So \(-9 + (-8) = -17\). The trap \(1\) reads \(-3^2\) as \((-3)^2 = 9\). Pro tip: without parentheses, the exponent attaches to the 3 only, so the negative stays outside.",
        },
        {
            "text": (r"**No-calculator section.** What is \(\dfrac{2}{3} \div \dfrac{4}{9}\)?"),
            "difficulty": 2,
            "choices": [(r"\(\frac{3}{2}\)", True), (r"\(\frac{8}{27}\)", False), (r"\(\frac{2}{3}\)", False), (r"\(\frac{6}{12}\)", False)],
            "explanation": r"Dividing flips the second fraction: \(\frac{2}{3} \times \frac{9}{4} = \frac{18}{12} = \frac{3}{2}\). The trap \(\frac{8}{27}\) multiplies the fractions instead of inverting. Pro tip: 'keep, change, flip' -- keep the first, change \(\div\) to \(\times\), flip the second.",
        },
        {
            "text": (r"**No-calculator section.** What is the value of \(2^{-3}\)?"),
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{8}\)", True), (r"\(-8\)", False), (r"\(-6\)", False), (r"\(8\)", False)],
            "explanation": r"A negative exponent means the reciprocal: \(2^{-3} = \frac{1}{2^3} = \frac{1}{8}\). The trap \(-8\) treats the exponent as making the result negative. Pro tip: a negative exponent flips the base to the denominator; it does not make the number negative.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \((3 \times 10^4)(2 \times 10^3)\)."),
            "difficulty": 2,
            "choices": [(r"\(6 \times 10^7\)", True), (r"\(6 \times 10^{12}\)", False), (r"\(5 \times 10^7\)", False), (r"\(6 \times 10^1\)", False)],
            "explanation": r"Multiply the numbers \((3 \times 2 = 6)\) and add the exponents \((4 + 3 = 7)\): \(6 \times 10^7\). The trap \(6 \times 10^{12}\) multiplies the exponents. Pro tip: with the same base 10, multiplying means add the exponents.",
        },
        {
            "text": (r"**No-calculator section.** Which expression has the greatest value: \(-9,\ \ |-7|,\ \ 2^3,\ \ -(2)^4\)?"),
            "difficulty": 2,
            "choices": [(r"\(2^3\)", True), (r"\(|-7|\)", False), (r"\(-9\)", False), (r"\(-(2)^4\)", False)],
            "explanation": r"Their values are \(-9,\ 7,\ 8,\ -16\). The largest is \(2^3 = 8\). The trap \(|-7| = 7\) is close but smaller. Pro tip: evaluate each expression to a single number first, then compare.",
        },
        # =====================================================================
        # ============ PART 2  --  QUESTIONS 6-46  --  CALCULATOR =============
        # =====================================================================
        # ----- Percents (multi-step) -----
        {
            "text": (r"A \$200 jacket is marked \(20\%\) off, and then an additional \(10\%\) is taken off the reduced price. What is the final price?"),
            "difficulty": 3,
            "choices": [(r"\$144", True), (r"\$140", False), (r"\$150", False), (r"\$160", False)],
            "explanation": r"First discount: \(200 \times 0.80 = \$160\). Second discount on that: \(160 \times 0.90 = \$144\). The trap \$140 adds the discounts to 30% off (\(200 \times 0.70\)). Pro tip: successive percents multiply step by step -- they do not simply add.",
        },
        {
            "text": (r"After a \(25\%\) increase, the price of an item is \$75. What was the original price?"),
            "difficulty": 3,
            "choices": [(r"\$60", True), (r"\$56.25", False), (r"\$100", False), (r"\$93.75", False)],
            "explanation": r"A 25% increase multiplies by 1.25, so the original is \(75 \div 1.25 = \$60\). The trap \$56.25 subtracts 25% of 75. Pro tip: to undo a percent increase, divide by \((1 + \text{rate})\), don't subtract the percent of the new price.",
        },
        {
            "text": (r"A restaurant meal costs \$50. An \(8\%\) tax and an \(18\%\) tip are each added to the original price. What is the total?"),
            "difficulty": 3,
            "choices": [(r"\$63.00", True), (r"\$59.00", False), (r"\$76.00", False), (r"\$68.00", False)],
            "explanation": r"Tax \(= 0.08 \times 50 = \$4\) and tip \(= 0.18 \times 50 = \$9\), so total \(= 50 + 4 + 9 = \$63\). Equivalently \(50 \times 1.26\). The trap \$59 adds only the tax. Pro tip: when both are on the original price, add the percents (8% + 18% = 26%) and apply once.",
        },
        {
            "text": (r"A town's population of \(12{,}500\) decreases by \(12\%\) in a year. What is the new population?"),
            "difficulty": 2,
            "choices": [(r"\(11{,}000\)", True), (r"\(11{,}500\)", False), (r"\(14{,}000\)", False), (r"\(1{,}500\)", False)],
            "explanation": r"A 12% decrease leaves 88%: \(12{,}500 \times 0.88 = 11{,}000\). The trap 1,500 is only the size of the decrease \((0.12 \times 12{,}500)\). Pro tip: a 12% decrease means you keep 88% -- multiply by 0.88 in one step.",
        },
        # ----- Ratios, proportions, rates -----
        {
            "text": (r"If \(A:B = 2:3\) and \(B:C = 4:5\), what is \(A:C\)?"),
            "difficulty": 3,
            "choices": [(r"\(8:15\)", True), (r"\(2:5\)", False), (r"\(8:5\)", False), (r"\(10:8\)", False)],
            "explanation": r"Make B match: \(A:B = 8:12\) and \(B:C = 12:15\). Now \(A:C = 8:15\). The trap \(2:5\) just pairs the outer numbers without scaling B. Pro tip: to chain ratios, rewrite both so the shared term (B) is the same number.",
        },
        {
            "text": (r"One pump can fill a tank in \(6\) hours; a second pump can fill it in \(3\) hours. Working together, how long do they take?"),
            "difficulty": 3,
            "choices": [(r"\(2\) hours", True), (r"\(4.5\) hours", False), (r"\(9\) hours", False), (r"\(4\) hours", False)],
            "explanation": r"Add the rates: \(\frac{1}{6} + \frac{1}{3} = \frac{1}{6} + \frac{2}{6} = \frac{3}{6} = \frac{1}{2}\) tank per hour, so the time is 2 hours. The trap 4.5 averages the two times. Pro tip: for combined-work problems, add the rates (jobs per hour), not the times.",
        },
        {
            "text": (r"A car travels at \(90\) kilometers per hour. What is this speed in meters per second?"),
            "difficulty": 3,
            "choices": [(r"\(25\) m/s", True), (r"\(324\) m/s", False), (r"\(1.5\) m/s", False), (r"\(250\) m/s", False)],
            "explanation": r"\(90 \text{ km/h} = \frac{90 \times 1000 \text{ m}}{3600 \text{ s}} = \frac{90000}{3600} = 25\) m/s. The trap 324 multiplies by 3.6 instead of dividing. Pro tip: to go from km/h to m/s, divide by 3.6.",
        },
        {
            "text": (r"\(3\) machines produce \(360\) parts in \(4\) hours. At the same rate, how many parts do \(5\) machines produce in \(6\) hours?"),
            "difficulty": 3,
            "choices": [(r"\(900\)", True), (r"\(750\)", False), (r"\(600\)", False), (r"\(1{,}080\)", False)],
            "explanation": r"One machine makes \(360 \div (3 \times 4) = 30\) parts per hour. Then \(5 \times 6 \times 30 = 900\). The trap 600 scales only the machines, not the hours. Pro tip: find the rate per machine per hour first, then multiply by both the machines and the hours.",
        },
        {
            "text": (r"A model car is built at a \(1:18\) scale. If the real car is \(4.5\) meters long, how long is the model?"),
            "difficulty": 2,
            "choices": [(r"\(25\) cm", True), (r"\(81\) cm", False), (r"\(8.1\) m", False), (r"\(2.5\) cm", False)],
            "explanation": r"The model is \(\frac{1}{18}\) of the real length: \(4.5 \div 18 = 0.25\) m \(= 25\) cm. The trap 81 cm multiplies by 18 instead of dividing. Pro tip: a 1:18 scale model is smaller, so divide the real measurement by 18.",
        },
        # ----- Data, statistics, probability -----
        {
            "text": (r"A course grade is \(70\%\) exams and \(30\%\) homework. A student averages \(80\) on exams and \(90\) on homework. What is the course grade?"),
            "difficulty": 3,
            "choices": [(r"\(83\)", True), (r"\(85\)", False), (r"\(82\)", False), (r"\(170\)", False)],
            "explanation": r"Weighted mean: \(0.70 \times 80 + 0.30 \times 90 = 56 + 27 = 83\). The trap 85 is the plain average of 80 and 90, ignoring the weights. Pro tip: a weighted mean multiplies each value by its weight before adding.",
        },
        {
            "text": (r"Four numbers have a mean of \(25\). Three of them are \(20,\ 28,\) and \(30\). What is the fourth number?"),
            "difficulty": 2,
            "choices": [(r"\(22\)", True), (r"\(25\)", False), (r"\(18\)", False), (r"\(27\)", False)],
            "explanation": r"The total must be \(4 \times 25 = 100\). The three known values sum to \(78\), so the fourth is \(100 - 78 = 22\). The trap 25 just repeats the mean. Pro tip: mean times count gives the total; subtract the known values to find the missing one.",
        },
        {
            "text": (r"A bag holds \(4\) red and \(6\) blue marbles. You draw \(2\) without replacing the first. What is the probability both are red?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{2}{15}\)", True), (r"\(\frac{4}{25}\)", False), (r"\(\frac{2}{9}\)", False), (r"\(\frac{1}{15}\)", False)],
            "explanation": r"First red: \(\frac{4}{10}\). After removing one red, second red: \(\frac{3}{9}\). Multiply: \(\frac{4}{10} \times \frac{3}{9} = \frac{12}{90} = \frac{2}{15}\). The trap \(\frac{4}{25}\) uses \(\frac{4}{10} \times \frac{4}{10}\) as if the marble were replaced. Pro tip: 'without replacement' means the totals drop by one for the second draw.",
        },
        {
            "text": (r"A fair six-sided die is rolled twice. What is the probability of getting at least one \(6\)?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{11}{36}\)", True), (r"\(\frac{1}{3}\)", False), (r"\(\frac{1}{36}\)", False), (r"\(\frac{25}{36}\)", False)],
            "explanation": r"Find the opposite first: P(no 6 either roll) \(= \frac{5}{6} \times \frac{5}{6} = \frac{25}{36}\). So P(at least one 6) \(= 1 - \frac{25}{36} = \frac{11}{36}\). The trap \(\frac{1}{3}\) adds \(\frac{1}{6} + \frac{1}{6}\), double-counting. Pro tip: for 'at least one,' compute 1 minus the probability of none.",
        },
        {
            "text": (r"Set A is \(10,\ 10,\ 10,\ 10\). Set B is \(4,\ 8,\ 12,\ 16\). Both have a mean of \(10\). Which has the larger standard deviation, and why?"),
            "difficulty": 2,
            "choices": [("Set B, because its values are more spread out from the mean", True),
                        ("Set A, because all its values are the same", False),
                        ("They are equal, because the means are equal", False),
                        ("Set A, because it has a larger total", False)],
            "explanation": r"Standard deviation measures spread. Set A's values never move from 10 (deviation 0); Set B's values range from 4 to 16, far from the mean, so Set B's deviation is larger. The trap 'equal means' confuses center with spread. Pro tip: equal means tell you nothing about spread -- look at how far values sit from the mean.",
        },
        {
            "text": ("Use the box plot below.\n\n"
                     "[[figure:box_plot|A box-and-whisker plot with a lower quartile, median, and upper quartile]]\n\n"
                     r"A box plot shows a lower quartile \(Q_1 = 15\) and an upper quartile \(Q_3 = 35\). What is the interquartile range (IQR)?"),
            "difficulty": 2,
            "choices": [(r"\(20\)", True), (r"\(50\)", False), (r"\(25\)", False), (r"\(15\)", False)],
            "explanation": r"IQR \(= Q_3 - Q_1 = 35 - 15 = 20\). The trap 50 adds the quartiles. Pro tip: the IQR is the width of the box -- subtract the lower quartile from the upper quartile.",
        },
        # ----- Geometry & measurement (advanced) -----
        {
            "text": ("Use the composite figure below.\n\n"
                     "[[figure:composite_area|A rectangle with a circular hole cut out of it]]\n\n"
                     r"A \(12 \times 8\) rectangle has a circular hole of radius \(2\) cut out of it. What is the remaining area? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 83.4\)", True), (r"\(\approx 108.6\)", False), (r"\(\approx 71.4\)", False), (r"\(\approx 90.9\)", False)],
            "explanation": r"Rectangle area \(= 12 \times 8 = 96\). Circle area \(= \pi r^2 = 3.14 \times 4 = 12.56\). Remaining \(= 96 - 12.56 \approx 83.4\). The trap 108.6 adds the circle instead of subtracting. Pro tip: for a 'hole,' subtract the cut-out area from the whole.",
        },
        {
            "text": ("Use the cone below.\n\n"
                     "[[figure:volume_cone|A cone with its radius and height labeled]]\n\n"
                     r"What is the volume of a cone with radius \(6\) and height \(10\)? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 376.8\)", True), (r"\(\approx 1130.4\)", False), (r"\(\approx 188.4\)", False), (r"\(\approx 753.6\)", False)],
            "explanation": r"\(V = \frac{1}{3}\pi r^2 h = \frac{1}{3}(3.14)(36)(10) = \frac{1}{3}(1130.4) = 376.8\). The trap 1130.4 forgets the \(\frac{1}{3}\) (that's a cylinder). Pro tip: a cone is exactly one-third of the cylinder with the same base and height.",
        },
        {
            "text": ("Use the sphere below.\n\n"
                     "[[figure:volume_sphere|A sphere with its radius labeled]]\n\n"
                     r"What is the volume of a sphere with radius \(3\)? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 113.0\)", True), (r"\(\approx 339.1\)", False), (r"\(\approx 84.8\)", False), (r"\(\approx 28.3\)", False)],
            "explanation": r"\(V = \frac{4}{3}\pi r^3 = \frac{4}{3}(3.14)(27) = \frac{4}{3}(84.78) = 113.0\). The trap 339.1 forgets the \(\frac{1}{3}\); 84.8 forgets the \(\frac{4}{3}\) entirely. Pro tip: cube the radius first, then apply \(\frac{4}{3}\pi\).",
        },
        {
            "text": ("Use the cylinder below.\n\n"
                     "[[figure:surface_cylinder|A cylinder with its radius and height labeled]]\n\n"
                     r"What is the total surface area of a cylinder with radius \(4\) and height \(10\)? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 351.7\)", True), (r"\(\approx 251.2\)", False), (r"\(\approx 1004.8\)", False), (r"\(\approx 100.5\)", False)],
            "explanation": r"\(SA = 2\pi r^2 + 2\pi r h = 2(3.14)(16) + 2(3.14)(4)(10) = 100.48 + 251.2 = 351.7\). The trap 251.2 is only the side; 100.5 is only the two ends. Pro tip: total surface area is the two circular ends PLUS the wrapped-around side.",
        },
        {
            "text": (r"What is the distance between the points \((1,\ 2)\) and \((7,\ 10)\)?"),
            "difficulty": 2,
            "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(\sqrt{28}\)", False), (r"\(100\)", False)],
            "explanation": r"\(d = \sqrt{(7-1)^2 + (10-2)^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). The trap 14 adds the differences \((6 + 8)\); 100 forgets the square root. Pro tip: the distance formula is the Pythagorean theorem on the coordinate grid.",
        },
        {
            "text": (r"Two triangles are similar with a scale factor of \(3\). The smaller triangle has an area of \(12\). What is the area of the larger triangle?"),
            "difficulty": 3,
            "choices": [(r"\(108\)", True), (r"\(36\)", False), (r"\(324\)", False), (r"\(4\)", False)],
            "explanation": r"Areas scale by the square of the scale factor: \(3^2 = 9\), so \(12 \times 9 = 108\). The trap 36 multiplies the area by 3 (the length factor, not the area factor). Pro tip: lengths scale by the factor, but areas scale by its square.",
        },
        {
            "text": ("Use the trapezoid below.\n\n"
                     "[[figure:area_trapezoid|A trapezoid with two parallel bases and a height]]\n\n"
                     r"What is the area of a trapezoid with parallel sides \(8\) and \(14\) and a height of \(6\)?"),
            "difficulty": 2,
            "choices": [(r"\(66\)", True), (r"\(132\)", False), (r"\(72\)", False), (r"\(60\)", False)],
            "explanation": r"\(A = \frac{1}{2}(b_1 + b_2)h = \frac{1}{2}(8 + 14)(6) = \frac{1}{2}(22)(6) = 66\). The trap 132 forgets the \(\frac{1}{2}\). Pro tip: add the two parallel sides, then take half times the height.",
        },
        {
            "text": ("Use the triangle below.\n\n"
                     "[[figure:triangle_angle_sum|A triangle with its three interior angles marked]]\n\n"
                     r"The three angles of a triangle are in the ratio \(2:3:4\). What is the largest angle?"),
            "difficulty": 3,
            "choices": [(r"\(80^\circ\)", True), (r"\(90^\circ\)", False), (r"\(60^\circ\)", False), (r"\(40^\circ\)", False)],
            "explanation": r"The ratio has \(2 + 3 + 4 = 9\) parts, and the angles sum to \(180^\circ\), so each part is \(180 \div 9 = 20^\circ\). The largest is \(4 \times 20 = 80^\circ\). The trap 90 assumes a right angle. Pro tip: split 180 into the total number of ratio parts first.",
        },
        {
            "text": (r"A wheel has a radius of \(14\) inches. How far does it travel in one full revolution? Use \(\pi \approx \frac{22}{7}\)."),
            "difficulty": 2,
            "choices": [(r"\(88\) inches", True), (r"\(44\) inches", False), (r"\(176\) inches", False), (r"\(616\) inches", False)],
            "explanation": r"One revolution covers the circumference: \(C = 2\pi r = 2 \times \frac{22}{7} \times 14 = 88\) inches. The trap 616 is the area \((\pi r^2)\). Pro tip: distance per revolution is the circumference, not the area.",
        },
        # ----- Coordinate geometry -----
        {
            "text": (r"What is the midpoint of the segment joining \((-2,\ 5)\) and \((6,\ -1)\)?"),
            "difficulty": 2,
            "choices": [(r"\((2,\ 2)\)", True), (r"\((4,\ 4)\)", False), (r"\((2,\ 3)\)", False), (r"\((8,\ -6)\)", False)],
            "explanation": r"Average the coordinates: \(\left(\frac{-2+6}{2},\ \frac{5+(-1)}{2}\right) = (2,\ 2)\). The trap \((8,-6)\) subtracts instead of averaging. Pro tip: the midpoint is the average of the x's and the average of the y's.",
        },
        {
            "text": (r"A line has a slope of \(\frac{2}{3}\). What is the slope of a line perpendicular to it?"),
            "difficulty": 3,
            "choices": [(r"\(-\frac{3}{2}\)", True), (r"\(\frac{3}{2}\)", False), (r"\(\frac{2}{3}\)", False), (r"\(-\frac{2}{3}\)", False)],
            "explanation": r"Perpendicular slopes are negative reciprocals: flip \(\frac{2}{3}\) to \(\frac{3}{2}\) and change the sign to \(-\frac{3}{2}\). The trap \(\frac{3}{2}\) flips but forgets the sign. Pro tip: perpendicular slopes multiply to \(-1\), so flip and negate.",
        },
        # ----- Algebra: expressions -----
        {
            "text": (r"Simplify: \(\dfrac{x^2 - 9}{x - 3}\) (for \(x \ne 3\))."),
            "difficulty": 3,
            "choices": [(r"\(x + 3\)", True), (r"\(x - 3\)", False), (r"\(x^2 - 3\)", False), (r"\(x + 9\)", False)],
            "explanation": r"Factor the top as a difference of squares: \(x^2 - 9 = (x-3)(x+3)\). Cancel the \((x-3)\): the result is \(x + 3\). The trap \(x - 3\) cancels the wrong factor. Pro tip: \(a^2 - b^2 = (a-b)(a+b)\) -- factor before you cancel.",
        },
        {
            "text": (r"Expand: \((2x - 3)(x + 4)\)."),
            "difficulty": 2,
            "choices": [(r"\(2x^2 + 5x - 12\)", True), (r"\(2x^2 - 12\)", False), (r"\(2x^2 + 8x - 12\)", False), (r"\(2x^2 + 11x - 12\)", False)],
            "explanation": r"FOIL: \(2x \cdot x = 2x^2\), \(2x \cdot 4 = 8x\), \(-3 \cdot x = -3x\), \(-3 \cdot 4 = -12\). Combine: \(2x^2 + 5x - 12\). The trap \(2x^2 - 12\) forgets the two middle terms. Pro tip: FOIL gives four products -- don't skip the inner and outer ones.",
        },
        {
            "text": (r"Simplify: \((3x^2 y)^3\)."),
            "difficulty": 3,
            "choices": [(r"\(27x^6 y^3\)", True), (r"\(9x^6 y^3\)", False), (r"\(3x^6 y^3\)", False), (r"\(27x^5 y^3\)", False)],
            "explanation": r"Raise each factor to the 3rd power: \(3^3 = 27\), \((x^2)^3 = x^6\), \(y^3\). So \(27x^6 y^3\). The trap \(9x^6 y^3\) uses \(3^2\) instead of \(3^3\). Pro tip: a power outside the parentheses applies to the coefficient AND every variable inside.",
        },
        # ----- Algebra: equations -----
        {
            "text": (r"Solve: \(x^2 - 4x - 5 = 0\)."),
            "difficulty": 2,
            "choices": [(r"\(x = 5\) or \(x = -1\)", True), (r"\(x = -5\) or \(x = 1\)", False), (r"\(x = 5\) or \(x = 1\)", False), (r"\(x = -5\) or \(x = -1\)", False)],
            "explanation": r"Factor: \((x - 5)(x + 1) = 0\), giving \(x = 5\) or \(x = -1\). The trap \(-5, 1\) flips both signs. Pro tip: find two numbers that multiply to \(-5\) and add to \(-4\) (that's \(-5\) and \(+1\)), then flip their signs for the solutions.",
        },
        {
            "text": (r"Solve: \(2x^2 + 3x - 2 = 0\)."),
            "difficulty": 3,
            "choices": [(r"\(x = \frac{1}{2}\) or \(x = -2\)", True), (r"\(x = -\frac{1}{2}\) or \(x = 2\)", False), (r"\(x = 2\) or \(x = -1\)", False), (r"\(x = 1\) or \(x = -2\)", False)],
            "explanation": r"Factor: \((2x - 1)(x + 2) = 0\). Set each to zero: \(2x - 1 = 0 \Rightarrow x = \frac{1}{2}\), and \(x + 2 = 0 \Rightarrow x = -2\). The trap flips both signs. Pro tip: with a leading coefficient, check by expanding your factors back out.",
        },
        {
            "text": (r"Solve for \(x\): \(\dfrac{3}{x+1} = \dfrac{2}{x-1}\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 5\)", True), (r"\(x = 1\)", False), (r"\(x = -5\)", False), (r"\(x = 0.2\)", False)],
            "explanation": r"Cross-multiply: \(3(x-1) = 2(x+1)\), so \(3x - 3 = 2x + 2\). Then \(x = 5\). The trap \(x = 1\) would make the right side undefined. Pro tip: cross-multiply to clear the fractions, then solve the linear equation.",
        },
        {
            "text": (r"The area of a triangle is \(A = \frac{1}{2}bh\). Solve this formula for \(h\)."),
            "difficulty": 2,
            "choices": [(r"\(h = \dfrac{2A}{b}\)", True), (r"\(h = \dfrac{A}{2b}\)", False), (r"\(h = 2A - b\)", False), (r"\(h = \dfrac{Ab}{2}\)", False)],
            "explanation": r"Multiply both sides by 2: \(2A = bh\). Divide by \(b\): \(h = \frac{2A}{b}\). The trap \(\frac{A}{2b}\) divides by 2 instead of multiplying. Pro tip: to isolate \(h\), undo the \(\frac{1}{2}\) by multiplying by 2, then undo the \(b\) by dividing.",
        },
        {
            "text": (r"Three consecutive even integers add up to \(78\). What is the smallest of the three?"),
            "difficulty": 3,
            "choices": [(r"\(24\)", True), (r"\(26\)", False), (r"\(22\)", False), (r"\(12\)", False)],
            "explanation": r"Let them be \(n, n+2, n+4\). Then \(3n + 6 = 78\), so \(3n = 72\) and \(n = 24\) (giving 24, 26, 28). The trap 26 is the middle integer. Pro tip: name the smallest as \(n\) and write the others in terms of it, then re-read which one is asked.",
        },
        # ----- Algebra: inequalities -----
        {
            "text": (r"Solve the compound inequality: \(-3 \le 2x - 1 < 5\)."),
            "difficulty": 3,
            "choices": [(r"\(-1 \le x < 3\)", True), (r"\(-2 \le x < 6\)", False), (r"\(-1 < x \le 3\)", False), (r"\(1 \le x < 3\)", False)],
            "explanation": r"Add 1 to all three parts: \(-2 \le 2x < 6\). Divide all by 2: \(-1 \le x < 3\). The trap \(-2 \le x < 6\) forgets to divide by 2. Pro tip: whatever you do to the middle, do to BOTH outer parts, and keep each inequality symbol.",
        },
        {
            "text": (r"Solve: \(-4x + 10 \ge 2\)."),
            "difficulty": 2,
            "choices": [(r"\(x \le 2\)", True), (r"\(x \ge 2\)", False), (r"\(x \le -2\)", False), (r"\(x \ge -2\)", False)],
            "explanation": r"Subtract 10: \(-4x \ge -8\). Divide by \(-4\) and FLIP the sign: \(x \le 2\). The trap \(x \ge 2\) forgets to flip. Pro tip: dividing an inequality by a negative number reverses the direction of the sign.",
        },
        # ----- Algebra: systems -----
        {
            "text": (r"Solve the system: \(y = 2x - 1\) and \(3x + y = 14\)."),
            "difficulty": 2,
            "choices": [(r"\((3,\ 5)\)", True), (r"\((5,\ 3)\)", False), (r"\((2,\ 3)\)", False), (r"\((3,\ 2)\)", False)],
            "explanation": r"Substitute \(y = 2x - 1\) into the second equation: \(3x + (2x - 1) = 14\), so \(5x = 15\) and \(x = 3\). Then \(y = 2(3) - 1 = 5\). The trap \((5,3)\) swaps the values. Pro tip: since \(y\) is already isolated, substitution is the fastest route.",
        },
        # ----- Algebra: functions, graphs, exponential -----
        {
            "text": (r"If \(f(x) = x^2 - 3x + 2\), what is \(f(-2)\)?"),
            "difficulty": 2,
            "choices": [(r"\(12\)", True), (r"\(0\)", False), (r"\(-8\)", False), (r"\(4\)", False)],
            "explanation": r"Substitute \(x = -2\): \((-2)^2 - 3(-2) + 2 = 4 + 6 + 2 = 12\). The trap 0 mishandles the sign on \(-3(-2)\), making it \(-6\). Pro tip: keep parentheses around \(-2\) so the squaring and the double-negative come out right.",
        },
        {
            "text": (r"A population of \(2{,}000\) grows by \(5\%\) each year. To the nearest whole number, what is the population after \(3\) years?"),
            "difficulty": 3,
            "choices": [(r"\(\approx 2{,}315\)", True), (r"\(2{,}300\)", False), (r"\(2{,}310\)", False), (r"\(2{,}205\)", False)],
            "explanation": r"Multiply by \(1.05\) three times: \(2000 \times 1.05^3 = 2000 \times 1.157625 \approx 2315\). The trap 2,300 adds a flat 5% per year (15% total). Pro tip: repeated percent growth uses \((1 + r)^n\), not \(n\) times the percent.",
        },
        {
            "text": (r"A burning candle shrinks at a constant rate. After \(2\) hours it is \(18\) cm tall; after \(5\) hours it is \(9\) cm tall. What is its rate of change in height?"),
            "difficulty": 3,
            "choices": [(r"\(-3\) cm per hour", True), (r"\(-9\) cm per hour", False), (r"\(3\) cm per hour", False), (r"\(-4.5\) cm per hour", False)],
            "explanation": r"Rate \(= \frac{9 - 18}{5 - 2} = \frac{-9}{3} = -3\) cm per hour. The trap \(-9\) is the change in height without dividing by the 3 hours. Pro tip: a rate of change is slope -- the change in height over the change in time, and it's negative because the candle shrinks.",
        },
        {
            "text": ("Use the table-and-line below.\n\n"
                     "[[figure:function_table_line|A straight line shown with its table of values]]\n\n"
                     r"A linear function gives \(y = 4\) at \(x = 1\), \(y = 7\) at \(x = 2\), and \(y = 10\) at \(x = 3\). What is \(y\) when \(x = 10\)?"),
            "difficulty": 3,
            "choices": [(r"\(31\)", True), (r"\(30\)", False), (r"\(34\)", False), (r"\(13\)", False)],
            "explanation": r"Each step of 1 in \(x\) adds 3 to \(y\), so the slope is 3 and \(y = 3x + 1\) (since at \(x=1\), \(y=4\)). Then \(y = 3(10) + 1 = 31\). The trap 30 forgets the \(+1\) intercept. Pro tip: find the constant change (slope), build \(y = mx + b\), then plug in the new \(x\).",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the advanced (Level 2) full-length GED Mathematical Reasoning practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 5 no-calculator, Part 2: 41 calculator; all medium/hard)."
        ))
