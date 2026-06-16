"""
Seed a THIRD full-length 'GED Mathematical Reasoning' practice exam -- Level 3,
the expert tier, harder than ``seed_ged_math_exam_level2``.

Same test-day structure (46 questions, 115 minutes, a no-calculator Part 1 of 5
then a calculator Part 2 of 41, formula sheet provided, scored 100-200, 145 to
pass), but the items reach the top of the GED's difficulty range and lean on
multi-concept reasoning:

  - Compound interest, reverse successive percents, mixture/concentration.
  - Harmonic average speed, net work rates, compound unit conversions, area
    scaling on maps.
  - Effect of removing a value on a mean, combined-group means, conditional
    probability without replacement, expected value, 'at least one' complements.
  - Composite and similar-solid volumes, 3-D diagonals, sectors, coordinate
    geometry, shadow proportions.
  - Quadratic formula (non-factorable), projectile and vertex problems, rational
    and absolute-value equations, elimination systems, absolute-value
    inequalities, function composition, and exponential decay.

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip.

Run:
    python manage.py seed_ged_math_exam_level3
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Mathematical Reasoning: Full-Length Practice Exam (Level 3 - Expert)",
    "slug": "ged-math-reasoning-exam-level3",
    "program": "GED",
    "subject": "math",
    "description": (
        "The hardest of the three full-length GED Mathematical Reasoning practice exams, for students "
        "who have cleared Levels 1 and 2 and want to be sure of a high score. Same test-day format -- "
        "46 questions in 115 minutes, a no-calculator Part 1 (the first 5 questions) then a calculator "
        "Part 2, with a provided formula sheet, scored 100-200 (145 to pass) -- but the items sit at the "
        "top of the GED's range and demand multi-concept reasoning: compound interest, reverse and "
        "successive percents, mixtures, harmonic average speed, net work rates, conditional probability "
        "and expected value, composite and similar-solid volumes, 3-D diagonals, the quadratic formula, "
        "projectile and vertex problems, rational and absolute-value equations and inequalities, "
        "function composition, and exponential decay. Every question includes a worked explanation and "
        "a pro tip."
    ),
    "lessons": [
        (
            "1. Level 3: The Expert Test",
            r"""
This is the **expert** GED Mathematical Reasoning practice exam -- the toughest of the three. The format never changes:

- **46 questions** in **115 minutes**.
- **Part 1 (Questions 1-5): NO CALCULATOR.** Hard by-hand work: order-of-operations with negatives and exponents, exponent laws, scientific notation, and simplifying radicals.
- **Part 2 (Questions 6-46): CALCULATOR ALLOWED.**
- A **formula sheet** is provided (next lesson); you cannot return to Part 1 after starting Part 2.
- Scored **100-200**, with **145 to pass**. No penalty for wrong answers.

**What makes Level 3 the hardest:** almost every question is a **hard, multi-step** item, and many **combine two ideas at once** -- a percent inside a finance problem, a rate inside a geometry problem, a probability that changes after each draw. Reading carefully and writing each step is now non-negotiable.

[[check:How many minutes does the GED Math test give you for all 46 questions?|115|115 minutes total, just over two minutes per question.]]
            """,
        ),
        (
            "2. The Formula Sheet & the Ideas Behind It",
            r"""
You get the **formula sheet** -- but Level 3 tests whether you can *choose and combine* the right tools.

**Geometry**
- Volumes: cylinder \(\pi r^2 h\), cone \(\tfrac{1}{3}\pi r^2 h\), sphere \(\tfrac{4}{3}\pi r^3\), prism/box \(lwh\).
- Surface area (cylinder): \(2\pi r^2 + 2\pi r h\).
- Pythagorean theorem \(a^2+b^2=c^2\); in 3-D the space diagonal is \(\sqrt{l^2+w^2+h^2}\).
- Sector: arc \(= \frac{\theta}{360}\,(2\pi r)\); sector area \(= \frac{\theta}{360}\,(\pi r^2)\).

**Coordinate geometry**
- Distance \(\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}\); midpoint \(\big(\tfrac{x_1+x_2}{2},\tfrac{y_1+y_2}{2}\big)\); slope \(\tfrac{y_2-y_1}{x_2-x_1}\).

**Algebra**
- Quadratic formula: \(x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}\); vertex at \(t=-\dfrac{b}{2a}\).

**Combination ideas the sheet won't state**
- **Compound growth/decay:** multiply by \((1+r)^n\) (decay uses \(1-r\)).
- **Similar solids:** areas scale by the factor **squared**, volumes by the factor **cubed**.
- **Average speed** for equal distances is the **harmonic** mean \(\dfrac{2v_1 v_2}{v_1+v_2}\), not the plain average.

[[figure:formula_substitution_flow|On hard items the lost points are almost always setup -- pick the formula, then substitute one careful step at a time.]]

[[check:Two similar cylinders have a linear scale factor of 2. Their volumes differ by a factor of what number?|8|Volumes scale by the cube of the scale factor, so 2 cubed = 8.]]
            """,
        ),
        (
            "3. Strategy for the Hardest Items",
            r"""
At this level, process beats speed every time.

- **Name both concepts.** If a question hides a percent inside a finance problem, label them: "this is compound interest" and "this is a percent." Solve in that order.
- **Backsolve the brutal ones.** For quadratics, rational equations, or absolute-value equations, plugging the numeric choices back in is often faster and surer than solving.
- **Watch 'at least one.'** Compute \(1 - P(\text{none})\) instead of adding cases.
- **Re-read the target.** Hard items ask for the *original* price, the *time it lands*, the *maximum* height, the *other* solution -- not the first number you find.
- **Flip on negatives.** Multiplying or dividing an inequality by a negative reverses the sign; absolute-value inequalities split into two cases.
- **Estimate as a check.** A rough estimate catches a calculator slip or a misplaced decimal before it costs you the point.

[[check:To find the probability of 'at least one' success, what should you subtract from 1?|the probability of none;;P(none);;probability of none;;none|Compute 1 minus the probability that none of them happen.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  QUESTIONS 1-5  --  NO CALCULATOR ============
        # =====================================================================
        {
            "text": (r"**No-calculator section.** Evaluate: \(\dfrac{(-2)^3 + 4^2}{2^3 - 6}\)."),
            "difficulty": 3,
            "choices": [(r"\(4\)", True), (r"\(-4\)", False), (r"\(12\)", False), (r"\(8\)", False)],
            "explanation": r"Top: \((-2)^3 + 4^2 = -8 + 16 = 8\). Bottom: \(2^3 - 6 = 8 - 6 = 2\). So \(\frac{8}{2} = 4\). The trap \(-4\) mishandles the sign of \((-2)^3\). Pro tip: simplify the numerator and denominator completely before dividing.",
        },
        {
            "text": (r"**No-calculator section.** What is \(\dfrac{3}{4} - \dfrac{2}{3} \times \dfrac{1}{2}\)?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{5}{12}\)", True), (r"\(\frac{1}{12}\)", False), (r"\(\frac{5}{24}\)", False), (r"\(\frac{1}{8}\)", False)],
            "explanation": r"Multiply first: \(\frac{2}{3} \times \frac{1}{2} = \frac{1}{3}\). Then \(\frac{3}{4} - \frac{1}{3} = \frac{9}{12} - \frac{4}{12} = \frac{5}{12}\). The trap \(\frac{1}{12}\) subtracts before multiplying. Pro tip: order of operations applies to fractions too -- multiply before you subtract.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(\dfrac{2^{-2} \cdot 2^{5}}{2^{4}}\)."),
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{2}\)", True), (r"\(2\)", False), (r"\(8\)", False), (r"\(\frac{1}{8}\)", False)],
            "explanation": r"Add the top exponents and subtract the bottom: \(2^{-2+5-4} = 2^{-1} = \frac{1}{2}\). The trap 2 drops the negative exponent. Pro tip: combine all the exponents on base 2 first, then read a negative result as a reciprocal.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(\dfrac{8 \times 10^{6}}{4 \times 10^{2}}\)."),
            "difficulty": 2,
            "choices": [(r"\(2 \times 10^{4}\)", True), (r"\(2 \times 10^{3}\)", False), (r"\(2 \times 10^{8}\)", False), (r"\(4 \times 10^{4}\)", False)],
            "explanation": r"Divide the numbers \((8 \div 4 = 2)\) and subtract the exponents \((6 - 2 = 4)\): \(2 \times 10^4\). The trap \(2 \times 10^8\) adds the exponents instead of subtracting. Pro tip: dividing powers of 10 means subtract the exponents.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(\sqrt{12} + \sqrt{27}\)."),
            "difficulty": 3,
            "choices": [(r"\(5\sqrt{3}\)", True), (r"\(\sqrt{39}\)", False), (r"\(6\sqrt{6}\)", False), (r"\(5\sqrt{6}\)", False)],
            "explanation": r"\(\sqrt{12} = 2\sqrt{3}\) and \(\sqrt{27} = 3\sqrt{3}\), so \(2\sqrt{3} + 3\sqrt{3} = 5\sqrt{3}\). The trap \(\sqrt{39}\) adds under one root \((12+27)\). Pro tip: pull out perfect squares first, then add like radical terms the way you'd add like variables.",
        },
        # =====================================================================
        # ============ PART 2  --  QUESTIONS 6-46  --  CALCULATOR =============
        # =====================================================================
        # ----- Percents & finance (multi-step) -----
        {
            "text": (r"\$1{,}000 is invested at \(4\%\) annual interest, compounded yearly. What is it worth after \(2\) years?"),
            "difficulty": 3,
            "choices": [(r"\$1{,}081.60", True), (r"\$1{,}080.00", False), (r"\$1{,}160.00", False), (r"\$1{,}082.43", False)],
            "explanation": r"Compound yearly: \(1000 \times 1.04^2 = 1000 \times 1.0816 = \$1{,}081.60\). The trap \$1,080 adds simple interest (\(2 \times 4\%\) of 1000). Pro tip: compound interest multiplies by \((1+r)\) once per year, so the second year earns interest on the first year's interest.",
        },
        {
            "text": (r"A price is increased by \(20\%\) and then the new price is decreased by \(20\%\), ending at \$96. What was the original price?"),
            "difficulty": 3,
            "choices": [(r"\$100", True), (r"\$96", False), (r"\$120", False), (r"\$80", False)],
            "explanation": r"The net factor is \(1.20 \times 0.80 = 0.96\), so original \(= 96 \div 0.96 = \$100\). The trap \$96 assumes a 20% up then 20% down cancels out. Pro tip: successive percents multiply -- a 20% rise then 20% fall leaves 96%, not 100%.",
        },
        {
            "text": (r"\(A\) is \(25\%\) more than \(B\). If \(A = 150\), what is \(B\)?"),
            "difficulty": 3,
            "choices": [(r"\(120\)", True), (r"\(112.5\)", False), (r"\(187.5\)", False), (r"\(125\)", False)],
            "explanation": r"\(A = 1.25B\), so \(B = 150 \div 1.25 = 120\). The trap 112.5 takes 25% off of 150. Pro tip: '25% more than B' means \(1.25B\); to recover B, divide by 1.25, don't subtract 25% of A.",
        },
        {
            "text": (r"\(200\) mL of a \(30\%\) salt solution is mixed with \(300\) mL of an \(80\%\) salt solution. What is the concentration of the mixture?"),
            "difficulty": 3,
            "choices": [(r"\(60\%\)", True), (r"\(55\%\)", False), (r"\(50\%\)", False), (r"\(110\%\)", False)],
            "explanation": r"Salt amount \(= 0.30(200) + 0.80(300) = 60 + 240 = 300\) mL of salt in \(500\) mL total, so \(\frac{300}{500} = 60\%\). The trap 55% averages 30% and 80% as if the volumes were equal. Pro tip: in a mixture, total the actual amounts, then divide by the total volume.",
        },
        {
            "text": (r"An item's price increases by \(10\%\), and then that new price increases by another \(30\%\). What is the total percent increase from the original?"),
            "difficulty": 3,
            "choices": [(r"\(43\%\)", True), (r"\(40\%\)", False), (r"\(13\%\)", False), (r"\(33\%\)", False)],
            "explanation": r"Multiply the factors: \(1.10 \times 1.30 = 1.43\), a 43% increase. The trap 40% just adds the two percents. Pro tip: chained percent increases multiply, and the extra 3% is the percent-on-a-percent.",
        },
        # ----- Ratios, rates, proportions -----
        {
            "text": (r"\$4{,}000 is shared in the ratio \(2:3:5\). How much is the middle share?"),
            "difficulty": 2,
            "choices": [(r"\$1{,}200", True), (r"\$800", False), (r"\$2{,}000", False), (r"\$1{,}333", False)],
            "explanation": r"There are \(2+3+5 = 10\) parts, so one part is \(4000 \div 10 = \$400\). The middle (3 parts) is \(3 \times 400 = \$1{,}200\). The trap \$800 is the smallest share (2 parts). Pro tip: divide the total by the number of ratio parts first, then multiply by the share you want.",
        },
        {
            "text": (r"A pipe fills a tank in \(4\) hours, while an open drain empties it in \(6\) hours. With both open, how long does it take to fill?"),
            "difficulty": 3,
            "choices": [(r"\(12\) hours", True), (r"\(2.4\) hours", False), (r"\(5\) hours", False), (r"\(10\) hours", False)],
            "explanation": r"Net rate \(= \frac{1}{4} - \frac{1}{6} = \frac{3}{12} - \frac{2}{12} = \frac{1}{12}\) tank per hour, so it takes 12 hours. The trap 2.4 adds the rates instead of subtracting the drain. Pro tip: a drain works against the fill, so subtract its rate.",
        },
        {
            "text": (r"A driver goes to a city at \(60\) mph and returns along the same road at \(40\) mph. What is the average speed for the whole round trip?"),
            "difficulty": 3,
            "choices": [(r"\(48\) mph", True), (r"\(50\) mph", False), (r"\(52\) mph", False), (r"\(45\) mph", False)],
            "explanation": r"For equal distances, average speed is the harmonic mean: \(\frac{2(60)(40)}{60+40} = \frac{4800}{100} = 48\) mph. The trap 50 just averages 60 and 40. Pro tip: more time is spent at the slower speed, so the true average is below the simple midpoint.",
        },
        {
            "text": (r"A faucet drips \(2\) mL every \(5\) seconds. How many liters leak in one hour?"),
            "difficulty": 3,
            "choices": [(r"\(1.44\) L", True), (r"\(2.4\) L", False), (r"\(0.72\) L", False), (r"\(14.4\) L", False)],
            "explanation": r"Rate \(= \frac{2}{5} = 0.4\) mL/s. In an hour: \(0.4 \times 3600 = 1440\) mL \(= 1.44\) L. The trap 14.4 misplaces the mL-to-L decimal. Pro tip: convert to a per-second rate, multiply by 3600, then divide by 1000 to reach liters.",
        },
        {
            "text": (r"On a map, \(1\) cm represents \(4\) km. Two cities and a landmark form a triangle with an area of \(6\ \text{cm}^2\) on the map. What is the actual area?"),
            "difficulty": 3,
            "choices": [(r"\(96\ \text{km}^2\)", True), (r"\(24\ \text{km}^2\)", False), (r"\(384\ \text{km}^2\)", False), (r"\(48\ \text{km}^2\)", False)],
            "explanation": r"Areas scale by the square of the length scale: \((4\ \text{km/cm})^2 = 16\ \text{km}^2/\text{cm}^2\), so \(6 \times 16 = 96\ \text{km}^2\). The trap 24 scales by 4 (a length factor, not an area factor). Pro tip: when a scale converts lengths, areas convert by the square of that scale.",
        },
        # ----- Data, statistics, probability -----
        {
            "text": (r"A class of \(20\) students has a mean score of \(75\). One student who scored \(94\) drops the class. What is the mean of the remaining \(19\) students?"),
            "difficulty": 3,
            "choices": [(r"\(74\)", True), (r"\(75\)", False), (r"\(74.2\)", False), (r"\(73\)", False)],
            "explanation": r"Total was \(20 \times 75 = 1500\). Remove 94: \(1500 - 94 = 1406\). New mean \(= 1406 \div 19 = 74\). The trap 75 assumes the mean is unchanged. Pro tip: rebuild the total, subtract the value, and divide by the new count.",
        },
        {
            "text": (r"Class A has \(10\) students averaging \(80\); Class B has \(15\) students averaging \(90\). What is the combined average of all \(25\) students?"),
            "difficulty": 3,
            "choices": [(r"\(86\)", True), (r"\(85\)", False), (r"\(84\)", False), (r"\(87\)", False)],
            "explanation": r"Combined total \(= 10(80) + 15(90) = 800 + 1350 = 2150\); divide by 25: \(2150 \div 25 = 86\). The trap 85 averages 80 and 90 directly, ignoring the larger Class B. Pro tip: weight each group's average by its size before combining.",
        },
        {
            "text": (r"A box has \(12\) items, \(3\) of them defective. You pick \(2\) at random without replacement. What is the probability both are defective?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{22}\)", True), (r"\(\frac{1}{16}\)", False), (r"\(\frac{1}{4}\)", False), (r"\(\frac{1}{11}\)", False)],
            "explanation": r"\(\frac{3}{12} \times \frac{2}{11} = \frac{6}{132} = \frac{1}{22}\). The trap \(\frac{1}{16}\) uses \(\frac{3}{12} \times \frac{3}{12}\) as if the item were replaced. Pro tip: without replacement, both the favorable count and the total drop by one on the second draw.",
        },
        {
            "text": (r"In a game you win \$5 with probability \(0.2\) and lose \$1 with probability \(0.8\). What is the expected value of one play?"),
            "difficulty": 3,
            "choices": [(r"\$0.20", True), (r"\$4.00", False), (r"-\$0.20", False), (r"\$1.00", False)],
            "explanation": r"Expected value \(= 0.2(5) + 0.8(-1) = 1 - 0.8 = \$0.20\). The trap \$4 ignores the loss. Pro tip: expected value multiplies each outcome by its probability and adds -- include the losing outcome as a negative.",
        },
        {
            "text": (r"A spinner lands on red with probability \(\frac{1}{4}\). If you spin it \(3\) times, what is the probability of getting at least one red?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{37}{64}\)", True), (r"\(\frac{27}{64}\)", False), (r"\(\frac{3}{4}\)", False), (r"\(\frac{1}{64}\)", False)],
            "explanation": r"P(no red) \(= \left(\frac{3}{4}\right)^3 = \frac{27}{64}\), so P(at least one) \(= 1 - \frac{27}{64} = \frac{37}{64}\). The trap \(\frac{3}{4}\) just adds \(\frac{1}{4}\) three times. Pro tip: for 'at least one,' it's almost always easiest to do 1 minus the probability of none.",
        },
        {
            "text": (r"Find the median of \(12,\ 15,\ 15,\ 18,\ 20,\ 22,\ 25,\ 30\)."),
            "difficulty": 2,
            "choices": [(r"\(19\)", True), (r"\(18\)", False), (r"\(20\)", False), (r"\(18.5\)", False)],
            "explanation": r"There are 8 values (already sorted), so average the 4th and 5th: \(\frac{18 + 20}{2} = 19\). The trap 18 picks only the 4th value. Pro tip: with an even count, the median is the mean of the two middle numbers.",
        },
        # ----- Geometry & measurement (advanced) -----
        {
            "text": (r"A solid is a cylinder of radius \(3\) and height \(8\) with a cone of the same radius and height \(6\) sitting on top. What is the total volume? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 282.6\)", True), (r"\(\approx 254.3\)", False), (r"\(\approx 565.2\)", False), (r"\(\approx 226.1\)", False)],
            "explanation": r"Cylinder \(= \pi r^2 h = \pi(9)(8) = 72\pi\). Cone \(= \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(9)(6) = 18\pi\). Total \(= 90\pi \approx 282.6\). The trap 226.1 forgets the cone's \(\frac{1}{3}\). Pro tip: find each solid's volume separately, then add.",
        },
        {
            "text": (r"Two cylinders are similar with a linear scale factor of \(2\). The smaller one has a volume of \(50\). What is the volume of the larger one?"),
            "difficulty": 3,
            "choices": [(r"\(400\)", True), (r"\(100\)", False), (r"\(200\)", False), (r"\(800\)", False)],
            "explanation": r"Volumes scale by the cube of the scale factor: \(2^3 = 8\), so \(50 \times 8 = 400\). The trap 100 multiplies by 2 (a length factor); 200 uses the square (an area factor). Pro tip: lengths scale by the factor, areas by its square, volumes by its cube.",
        },
        {
            "text": (r"A triangle has vertices at \((0,0)\), \((9,0)\), and \((0,12)\). What is its perimeter?"),
            "difficulty": 3,
            "choices": [(r"\(36\)", True), (r"\(54\)", False), (r"\(21\)", False), (r"\(18\)", False)],
            "explanation": r"The legs are 9 and 12; the hypotenuse is \(\sqrt{9^2+12^2} = \sqrt{225} = 15\). Perimeter \(= 9 + 12 + 15 = 36\). The trap 54 is the area \((\frac{1}{2}\cdot 9\cdot 12)\), not the perimeter. Pro tip: find the missing side with the Pythagorean theorem, then add all three sides.",
        },
        {
            "text": (r"A rectangular box measures \(3 \times 4 \times 12\). What is the length of its longest interior (space) diagonal?"),
            "difficulty": 3,
            "choices": [(r"\(13\)", True), (r"\(19\)", False), (r"\(\sqrt{160}\)", False), (r"\(12\)", False)],
            "explanation": r"The space diagonal is \(\sqrt{l^2+w^2+h^2} = \sqrt{9+16+144} = \sqrt{169} = 13\). The trap 19 adds the dimensions. Pro tip: the 3-D diagonal extends the Pythagorean theorem to all three edge lengths under one square root.",
        },
        {
            "text": (r"A circle is inscribed in a square with a side of \(10\). What is the area inside the square but outside the circle? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 21.5\)", True), (r"\(\approx 78.5\)", False), (r"\(\approx 68.6\)", False), (r"\(\approx 7.16\)", False)],
            "explanation": r"The inscribed circle has radius 5, so its area is \(\pi(25) = 78.5\). Square area is \(100\), so the leftover is \(100 - 78.5 = 21.5\). The trap 78.5 reports the circle, not the leftover. Pro tip: an inscribed circle's diameter equals the square's side, so the radius is half the side.",
        },
        {
            "text": (r"A circle has a radius of \(12\). What is the arc length of a sector with a central angle of \(90^\circ\)? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 18.84\)", True), (r"\(\approx 9.42\)", False), (r"\(\approx 37.68\)", False), (r"\(\approx 113.04\)", False)],
            "explanation": r"Arc \(= \frac{90}{360}(2\pi r) = \frac{1}{4}(2 \cdot 3.14 \cdot 12) = \frac{1}{4}(75.36) = 18.84\). The trap 113.04 is the full circumference. Pro tip: a sector is a fraction \(\frac{\theta}{360}\) of the whole circle.",
        },
        {
            "text": (r"A cube has a volume of \(64\ \text{cm}^3\). What is its total surface area?"),
            "difficulty": 2,
            "choices": [(r"\(96\ \text{cm}^2\)", True), (r"\(64\ \text{cm}^2\)", False), (r"\(24\ \text{cm}^2\)", False), (r"\(384\ \text{cm}^2\)", False)],
            "explanation": r"The side is \(\sqrt[3]{64} = 4\) cm. Surface area \(= 6 \times 4^2 = 6 \times 16 = 96\ \text{cm}^2\). The trap 64 repeats the volume. Pro tip: take the cube root of the volume to get the side, then use 6 faces of \(s^2\).",
        },
        {
            "text": (r"A \(6\)-foot-tall person casts a \(4\)-foot shadow. At the same time, a nearby tree casts a \(30\)-foot shadow. How tall is the tree?"),
            "difficulty": 2,
            "choices": [(r"\(45\) feet", True), (r"\(20\) feet", False), (r"\(40\) feet", False), (r"\(33\) feet", False)],
            "explanation": r"Set up similar triangles: \(\frac{6}{4} = \frac{h}{30}\), so \(h = \frac{6 \times 30}{4} = 45\) feet. The trap 20 inverts the proportion. Pro tip: height-to-shadow is the same ratio for both objects at the same time of day.",
        },
        {
            "text": (r"A garden is a \(20\) ft by \(15\) ft rectangle with a triangular extension of base \(15\) ft and height \(8\) ft attached to one end. What is the total area?"),
            "difficulty": 3,
            "choices": [(r"\(360\ \text{ft}^2\)", True), (r"\(420\ \text{ft}^2\)", False), (r"\(320\ \text{ft}^2\)", False), (r"\(300\ \text{ft}^2\)", False)],
            "explanation": r"Rectangle \(= 20 \times 15 = 300\). Triangle \(= \frac{1}{2}(15)(8) = 60\). Total \(= 300 + 60 = 360\ \text{ft}^2\). The trap 420 doubles the triangle by forgetting the \(\frac{1}{2}\). Pro tip: break a composite shape into simple pieces, find each area, then add.",
        },
        # ----- Coordinate geometry / lines -----
        {
            "text": (r"What is the equation of the line through the points \((2,\ 3)\) and \((4,\ 7)\)?"),
            "difficulty": 2,
            "choices": [(r"\(y = 2x - 1\)", True), (r"\(y = 2x + 3\)", False), (r"\(y = \tfrac{1}{2}x - 1\)", False), (r"\(y = 2x + 1\)", False)],
            "explanation": r"Slope \(= \frac{7-3}{4-2} = 2\). Using \(y = 2x + b\) with \((2,3)\): \(3 = 4 + b\), so \(b = -1\), giving \(y = 2x - 1\). The trap \(y = 2x + 3\) reads the intercept off the y-value of a point. Pro tip: find the slope first, then solve for \(b\) by plugging in one point.",
        },
        {
            "text": (r"Which line is parallel to \(y = 3x + 2\) and passes through \((0,\ -4)\)?"),
            "difficulty": 2,
            "choices": [(r"\(y = 3x - 4\)", True), (r"\(y = -\tfrac{1}{3}x - 4\)", False), (r"\(y = 3x + 2\)", False), (r"\(y = -3x - 4\)", False)],
            "explanation": r"Parallel lines share the slope 3, and the point \((0,-4)\) is the y-intercept, so \(y = 3x - 4\). The trap \(-\frac{1}{3}\) is the perpendicular slope, not the parallel one. Pro tip: parallel means same slope; perpendicular means negative reciprocal.",
        },
        # ----- Algebra: expressions -----
        {
            "text": (r"Factor completely: \(3x^2 - 12\)."),
            "difficulty": 3,
            "choices": [(r"\(3(x-2)(x+2)\)", True), (r"\(3(x^2 - 4)\)", False), (r"\((3x-4)(x+3)\)", False), (r"\((x-2)(x+6)\)", False)],
            "explanation": r"Factor out 3: \(3(x^2 - 4)\). Then \(x^2 - 4\) is a difference of squares: \(3(x-2)(x+2)\). The trap \(3(x^2-4)\) stops too early -- it isn't fully factored. Pro tip: always pull out the common factor first, then check whether what's left factors again.",
        },
        {
            "text": (r"Simplify: \(\dfrac{x^2 + 5x + 6}{x^2 - 9}\)."),
            "difficulty": 3,
            "choices": [(r"\(\dfrac{x+2}{x-3}\)", True), (r"\(\dfrac{x+3}{x-3}\)", False), (r"\(\dfrac{x+2}{x+3}\)", False), (r"\(\dfrac{x-2}{x-3}\)", False)],
            "explanation": r"Factor both: \(\frac{(x+2)(x+3)}{(x-3)(x+3)}\). Cancel the \((x+3)\): \(\frac{x+2}{x-3}\). The trap \(\frac{x+3}{x-3}\) cancels the wrong factor. Pro tip: factor the top and bottom fully before canceling the common factor.",
        },
        {
            "text": (r"Simplify: \(\dfrac{12x^5 y^3}{4x^2 y^7}\)."),
            "difficulty": 3,
            "choices": [(r"\(\dfrac{3x^3}{y^4}\)", True), (r"\(3x^3 y^4\)", False), (r"\(8x^3 y^4\)", False), (r"\(\dfrac{x^3}{3y^4}\)", False)],
            "explanation": r"Numbers: \(12 \div 4 = 3\). Variables: \(x^{5-2} = x^3\) and \(y^{3-7} = y^{-4} = \frac{1}{y^4}\). Result: \(\frac{3x^3}{y^4}\). The trap \(3x^3 y^4\) ignores the negative exponent. Pro tip: subtract exponents when dividing, and move negative powers to the denominator.",
        },
        # ----- Algebra: equations -----
        {
            "text": (r"Solve using the quadratic formula: \(x^2 - 4x - 1 = 0\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 2 \pm \sqrt{5}\)", True), (r"\(x = 2 \pm \sqrt{3}\)", False), (r"\(x = -2 \pm \sqrt{5}\)", False), (r"\(x = 4 \pm \sqrt{5}\)", False)],
            "explanation": r"With \(a=1, b=-4, c=-1\): \(x = \frac{4 \pm \sqrt{16+4}}{2} = \frac{4 \pm \sqrt{20}}{2} = \frac{4 \pm 2\sqrt5}{2} = 2 \pm \sqrt5\). The trap \(2 \pm \sqrt3\) miscomputes the discriminant. Pro tip: \(b^2 - 4ac = 16 - 4(1)(-1) = 20\); don't drop the double negative.",
        },
        {
            "text": (r"A ball's height is \(h = -16t^2 + 32t + 48\) feet after \(t\) seconds. At what time does it hit the ground?"),
            "difficulty": 3,
            "choices": [(r"\(t = 3\) seconds", True), (r"\(t = 1\) second", False), (r"\(t = 4\) seconds", False), (r"\(t = 48\) seconds", False)],
            "explanation": r"Set \(h = 0\): \(-16t^2 + 32t + 48 = 0\). Divide by \(-16\): \(t^2 - 2t - 3 = 0\), which factors as \((t-3)(t+1)=0\). The positive solution is \(t = 3\). The trap \(t=1\) is not a root at all. Pro tip: 'hits the ground' means height 0; reject the negative time.",
        },
        {
            "text": (r"Solve for \(x\): \(\dfrac{1}{x} + \dfrac{1}{2x} = 3\)."),
            "difficulty": 3,
            "choices": [(r"\(x = \tfrac{1}{2}\)", True), (r"\(x = 3\)", False), (r"\(x = \tfrac{1}{6}\)", False), (r"\(x = 2\)", False)],
            "explanation": r"Combine over \(2x\): \(\frac{2}{2x} + \frac{1}{2x} = \frac{3}{2x} = 3\). So \(2x = 1\) and \(x = \frac{1}{2}\). The trap \(x = \frac{1}{6}\) sets \(3x = ...\) incorrectly. Pro tip: get a common denominator, then cross-multiply to clear the fractions.",
        },
        {
            "text": (r"Solve: \(|2x - 3| = 7\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 5\) or \(x = -2\)", True), (r"\(x = 5\) or \(x = 2\)", False), (r"\(x = -5\) or \(x = 2\)", False), (r"\(x = 5\) only", False)],
            "explanation": r"Split into two cases: \(2x - 3 = 7 \Rightarrow x = 5\), and \(2x - 3 = -7 \Rightarrow 2x = -4 \Rightarrow x = -2\). The trap '\(x=5\) only' forgets the negative case. Pro tip: an absolute-value equation gives two equations -- the inside equals the positive AND the negative value.",
        },
        {
            "text": (r"Solve the system by elimination: \(3x + 2y = 16\) and \(5x - 2y = 8\)."),
            "difficulty": 3,
            "choices": [(r"\((3,\ 3.5)\)", True), (r"\((3,\ 2)\)", False), (r"\((2,\ 5)\)", False), (r"\((3.5,\ 3)\)", False)],
            "explanation": r"Add the equations to cancel \(y\): \(8x = 24\), so \(x = 3\). Then \(3(3) + 2y = 16 \Rightarrow 2y = 7 \Rightarrow y = 3.5\). The trap \((3,2)\) mis-solves for \(y\). Pro tip: the \(+2y\) and \(-2y\) cancel when you add, isolating \(x\) immediately.",
        },
        # ----- Algebra: inequalities -----
        {
            "text": (r"Solve: \(|x - 2| < 5\)."),
            "difficulty": 3,
            "choices": [(r"\(-3 < x < 7\)", True), (r"\(x < 7\)", False), (r"\(-7 < x < 3\)", False), (r"\(x > 7\) or \(x < -3\)", False)],
            "explanation": r"\(|x-2| < 5\) means \(-5 < x - 2 < 5\). Add 2 throughout: \(-3 < x < 7\). The trap 'x > 7 or x < -3' is the solution to a 'greater than' absolute value. Pro tip: '\(<\)' absolute values become a single 'between' inequality; '\(>\)' becomes two separate pieces.",
        },
        {
            "text": (r"A taxi charges a \$3 flat fee plus \$2 per mile. With \$20, what is the greatest whole number of miles you can travel?"),
            "difficulty": 3,
            "choices": [(r"\(8\) miles", True), (r"\(8.5\) miles", False), (r"\(10\) miles", False), (r"\(11\) miles", False)],
            "explanation": r"Solve \(3 + 2m \le 20\): \(2m \le 17\), so \(m \le 8.5\). Since miles billed must be whole, the most you can afford is 8. The trap 8.5 ignores that you need a whole number. Pro tip: set up the inequality, then round DOWN to the nearest whole number for a 'greatest you can afford' question.",
        },
        # ----- Functions, composition, exponential -----
        {
            "text": (r"If \(f(x) = 2x + 1\) and \(g(x) = x^2\), what is \(f(g(3))\)?"),
            "difficulty": 3,
            "choices": [(r"\(19\)", True), (r"\(49\)", False), (r"\(13\)", False), (r"\(37\)", False)],
            "explanation": r"Work inside out: \(g(3) = 3^2 = 9\), then \(f(9) = 2(9) + 1 = 19\). The trap 49 computes \(g(f(3)) = g(7)\) in the wrong order. Pro tip: \(f(g(3))\) means do \(g\) first, then feed its result into \(f\).",
        },
        {
            "text": (r"A \$24{,}000 car loses \(15\%\) of its value each year. What is it worth after \(2\) years?"),
            "difficulty": 3,
            "choices": [(r"\$17{,}340", True), (r"\$16{,}800", False), (r"\$17{,}000", False), (r"\$20{,}400", False)],
            "explanation": r"Each year it keeps 85%: \(24000 \times 0.85^2 = 24000 \times 0.7225 = \$17{,}340\). The trap \$16,800 subtracts a flat 30% (\(2 \times 15\%\)). Pro tip: exponential decay multiplies by \((1 - r)\) once per year, so the second year's loss is smaller in dollars.",
        },
        {
            "text": (r"A projectile's height is \(h = -16t^2 + 64t\) feet. What is its maximum height?"),
            "difficulty": 3,
            "choices": [(r"\(64\) feet", True), (r"\(2\) feet", False), (r"\(128\) feet", False), (r"\(48\) feet", False)],
            "explanation": r"The vertex is at \(t = -\frac{b}{2a} = -\frac{64}{2(-16)} = 2\) s. Then \(h = -16(2)^2 + 64(2) = -64 + 128 = 64\) feet. The trap 2 reports the time, not the height. Pro tip: find the vertex time with \(-\frac{b}{2a}\), then substitute it back to get the maximum height.",
        },
        {
            "text": (r"Plan A costs \$50 to join plus \$30 per month. Plan B costs \$20 to join plus \$35 per month. After how many months do the two plans cost the same?"),
            "difficulty": 3,
            "choices": [(r"\(6\) months", True), (r"\(5\) months", False), (r"\(7\) months", False), (r"\(10\) months", False)],
            "explanation": r"Set them equal: \(50 + 30m = 20 + 35m\). Then \(30 = 5m\), so \(m = 6\). The trap 5 comes from a sign slip. Pro tip: write a cost expression for each plan, set them equal, and solve for the month they break even.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the expert (Level 3) full-length GED Mathematical Reasoning practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 5 no-calculator, Part 2: 41 calculator; expert level)."
        ))
