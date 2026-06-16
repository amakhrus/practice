"""
Seed a FOURTH full-length 'GED Mathematical Reasoning' practice exam -- Level 4,
the mastery tier, harder than ``seed_ged_math_exam_level3``.

Same test-day structure (46 questions, 115 minutes, a no-calculator Part 1 of 5
then a calculator Part 2 of 41, formula sheet provided, scored 100-200, 145 to
pass), but EVERY item is a hard, multi-concept problem at the very top of the
GED's range:

  - Fractional and negative exponents, nested radicals, absolute value in
    order-of-operations.
  - Semi-annual compound interest, reverse multi-step pricing, markup-then-
    discount, dilution to a target concentration, marginal tax brackets.
  - Inverse variation, three-worker rates, multi-leg average speed, density.
  - Effect of shifting a data set, reverse weighted averages, conditional
    probability, combinations, expected value.
  - Hemisphere-on-cylinder volume, annulus area, volume scaling, co-interior
    angles, reverse trapezoid height.
  - Quadratic formula, line-parabola systems, factoring by grouping, combining
    rational expressions, quadratic and absolute-value inequalities, function
    composition, exponential thresholds, and arithmetic sequences.

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip.

Run:
    python manage.py seed_ged_math_exam_level4
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Mathematical Reasoning: Full-Length Practice Exam (Level 4 - Mastery)",
    "slug": "ged-math-reasoning-exam-level4",
    "program": "GED",
    "subject": "math",
    "description": (
        "The final and hardest of the four full-length GED Mathematical Reasoning practice exams, for "
        "students aiming at a top score after clearing Levels 1-3. Same test-day format -- 46 questions "
        "in 115 minutes, a no-calculator Part 1 (the first 5 questions) then a calculator Part 2, with a "
        "provided formula sheet, scored 100-200 (145 to pass) -- but every single item is a hard, "
        "multi-concept problem at the ceiling of the GED's range: fractional and negative exponents and "
        "nested radicals, semi-annual compound interest, reverse pricing, dilution to a target, marginal "
        "tax brackets, inverse variation, multi-leg average speed, conditional probability, combinations "
        "and expected value, hemisphere-on-cylinder volumes, annulus area and volume scaling, the "
        "quadratic formula, line-parabola systems, factoring by grouping, rational expressions, quadratic "
        "and absolute-value inequalities, function composition, exponential thresholds, and arithmetic "
        "sequences. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 4: The Mastery Test",
            r"""
This is the **mastery** GED Mathematical Reasoning practice exam -- the hardest of all four. The format is unchanged from the real test:

- **46 questions** in **115 minutes**.
- **Part 1 (Questions 1-5): NO CALCULATOR.** Expect fractional and negative exponents, nested radicals, and absolute value buried in order-of-operations.
- **Part 2 (Questions 6-46): CALCULATOR ALLOWED.**
- A **formula sheet** is provided (next lesson); no returning to Part 1 once Part 2 begins.
- Scored **100-200**, with **145 to pass**. No penalty for wrong answers.

**What makes Level 4 the hardest:** **every** question is a hard, multi-step item, and most **layer two or three concepts** -- a tax bracket on top of a percent, a probability that depends on a count, a geometry answer that feeds an algebra step. There are no easy points to bank, so accuracy and careful reading decide your score.

[[check:On Level 4, how many of the questions are easy?|0;;none;;zero|Every item is a hard, multi-concept problem -- there are no easy questions.]]
            """,
        ),
        (
            "2. The Formula Sheet & Mastery Ideas",
            r"""
You get the **formula sheet**, but at this level success is about *combining* tools and recalling a few facts the sheet leaves out.

**Geometry**
- Volumes: cylinder \(\pi r^2 h\), cone \(\tfrac13\pi r^2 h\), sphere \(\tfrac43\pi r^3\) (a hemisphere is half of that).
- Annulus (ring) area: \(\pi R^2 - \pi r^2\).
- Sector: arc \(=\frac{\theta}{360}(2\pi r)\), area \(=\frac{\theta}{360}(\pi r^2)\).

**Algebra**
- Quadratic formula: \(x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}\).
- Fractional exponent: \(a^{m/n}=\left(\sqrt[n]{a}\right)^m\); negative exponent: \(a^{-n}=\dfrac{1}{a^n}\).
- Arithmetic sequence: \(a_n=a_1+(n-1)d\).

**Mastery facts the sheet won't give you**
- **Scaling:** lengths by \(k\), areas by \(k^2\), **volumes by \(k^3\)**.
- **Inverse variation:** if more workers means fewer days, the *product* (worker-days) is constant.
- **Average speed** over a whole trip is *total distance \(\div\) total time* -- never the plain average of the speeds.
- **Conditional probability:** \(P(B\mid A)=\dfrac{P(A\text{ and }B)}{P(A)}\).
- **Combinations:** choosing \(r\) from \(n\) (order doesn't matter) is \({}_nC_r=\dfrac{n!}{r!\,(n-r)!}\).

[[figure:formula_substitution_flow|At mastery level, almost every miss is a setup slip -- name the concept, choose the formula, then substitute one careful line at a time.]]

[[check:A cube's edges are tripled. Its volume grows by a factor of what?|27|Volume scales by the cube of the linear factor, so 3 cubed = 27.]]
            """,
        ),
        (
            "3. Strategy for Mastery-Level Items",
            r"""
With no easy questions, your process has to be airtight.

- **Unpack the layers.** Write down each concept a problem stacks: "bracket, then percent," "area, then cost," "doubling, then count the doublings."
- **Backsolve the algebra.** For quadratics, rational, and absolute-value equations, plugging the numeric choices back in is often the safest route -- and it catches extraneous solutions.
- **Use complements and ratios.** 'At least one' is \(1-P(\text{none})\); a conditional is the joint over the given.
- **Re-read the exact target.** Mastery traps love to ask for the *original* value, the *other* root, the *leftover* area, the *time* (not the height).
- **Flip and split on inequalities.** Dividing by a negative flips the sign; \(|x|>c\) splits into two pieces; a quadratic inequality needs the sign between or outside its roots.
- **Estimate to sanity-check.** A quick estimate flags a calculator slip before it costs the point.

[[check:To solve the quadratic inequality (x-2)(x-3) < 0, are the solutions between the roots or outside them?|between;;between the roots;;in between|A product is negative between its two roots, so 2 < x < 3.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  QUESTIONS 1-5  --  NO CALCULATOR ============
        # =====================================================================
        {
            "text": (r"**No-calculator section.** Evaluate: \(\dfrac{(-3)^2 - 2 \cdot 5}{(-1)^3 + 4}\)."),
            "difficulty": 3,
            "choices": [(r"\(-\frac{1}{3}\)", True), (r"\(\frac{1}{3}\)", False), (r"\(-1\)", False), (r"\(\frac{19}{3}\)", False)],
            "explanation": r"Top: \((-3)^2 - 2\cdot 5 = 9 - 10 = -1\). Bottom: \((-1)^3 + 4 = -1 + 4 = 3\). So \(\frac{-1}{3} = -\frac{1}{3}\). The trap \(\frac{1}{3}\) drops the numerator's sign. Pro tip: finish the numerator and denominator separately, keeping every sign, before dividing.",
        },
        {
            "text": (r"**No-calculator section.** What is the value of \(16^{3/4}\)?"),
            "difficulty": 3,
            "choices": [(r"\(8\)", True), (r"\(12\)", False), (r"\(64\)", False), (r"\(6\)", False)],
            "explanation": r"A fractional exponent is a root then a power: \(16^{3/4} = \left(\sqrt[4]{16}\right)^3 = 2^3 = 8\). The trap 12 multiplies \(16 \times \frac{3}{4}\). Pro tip: the denominator is the root and the numerator is the power -- take the 4th root first, then cube it.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(\left(\dfrac{2}{3}\right)^{-2}\)."),
            "difficulty": 3,
            "choices": [(r"\(\frac{9}{4}\)", True), (r"\(\frac{4}{9}\)", False), (r"\(-\frac{9}{4}\)", False), (r"\(\frac{3}{2}\)", False)],
            "explanation": r"A negative exponent flips the fraction: \(\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^2 = \frac{9}{4}\). The trap \(\frac{4}{9}\) squares without flipping. Pro tip: invert the fraction to make the exponent positive, then apply the power.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(\sqrt{50} - \sqrt{18}\)."),
            "difficulty": 3,
            "choices": [(r"\(2\sqrt{2}\)", True), (r"\(\sqrt{32}\)", False), (r"\(8\sqrt{2}\)", False), (r"\(2\sqrt{34}\)", False)],
            "explanation": r"\(\sqrt{50} = 5\sqrt2\) and \(\sqrt{18} = 3\sqrt2\), so \(5\sqrt2 - 3\sqrt2 = 2\sqrt2\). The trap \(\sqrt{32}\) subtracts under one root \((50-18)\). Pro tip: simplify each radical to its \(\sqrt2\) form first, then subtract like terms.",
        },
        {
            "text": (r"**No-calculator section.** Evaluate: \(-2\,|3 - 7| + (-2)^2\)."),
            "difficulty": 3,
            "choices": [(r"\(-4\)", True), (r"\(12\)", False), (r"\(-12\)", False), (r"\(4\)", False)],
            "explanation": r"\(|3-7| = 4\), so \(-2(4) = -8\); and \((-2)^2 = 4\). Then \(-8 + 4 = -4\). The trap 12 mishandles the signs. Pro tip: evaluate the absolute value and the power first, then combine -- the \(-2\) outside stays negative.",
        },
        # =====================================================================
        # ============ PART 2  --  QUESTIONS 6-46  --  CALCULATOR =============
        # =====================================================================
        # ----- Percents & finance (layered) -----
        {
            "text": (r"\$2{,}000 is invested at \(8\%\) annual interest, compounded semi-annually. What is it worth after \(1\) year?"),
            "difficulty": 3,
            "choices": [(r"\$2{,}163.20", True), (r"\$2{,}160.00", False), (r"\$2{,}166.40", False), (r"\$2{,}080.00", False)],
            "explanation": r"Semi-annual means two periods of \(4\%\): \(2000 \times 1.04^2 = 2000 \times 1.0816 = \$2{,}163.20\). The trap \$2,160 applies a single 8%. Pro tip: divide the annual rate by the number of periods and raise \((1+r)\) to that many periods.",
        },
        {
            "text": (r"After a \(10\%\) discount and then a \$5 coupon, a shirt costs \$40. What was the original price?"),
            "difficulty": 3,
            "choices": [(r"\$50", True), (r"\$45", False), (r"\$48.33", False), (r"\$55", False)],
            "explanation": r"Let the price be \(x\): \(0.9x - 5 = 40\), so \(0.9x = 45\) and \(x = 50\). The trap \$45 stops at \(0.9x\). Pro tip: undo the steps in reverse -- add back the \$5 coupon first, then divide by 0.9 to undo the 10% off.",
        },
        {
            "text": (r"A store buys an item for \$80, marks it up \(50\%\), then puts it on sale at \(20\%\) off. What is the sale price?"),
            "difficulty": 3,
            "choices": [(r"\$96", True), (r"\$104", False), (r"\$120", False), (r"\$88", False)],
            "explanation": r"Marked price \(= 80 \times 1.50 = \$120\); sale price \(= 120 \times 0.80 = \$96\). The trap \$104 adds 50% then subtracts 20% of the cost, not the marked price. Pro tip: apply each percent to the price that exists at that step -- markup on cost, discount on the marked price.",
        },
        {
            "text": (r"How many liters of pure water must be added to \(10\) L of a \(40\%\) acid solution to dilute it to \(25\%\) acid?"),
            "difficulty": 3,
            "choices": [(r"\(6\) L", True), (r"\(4\) L", False), (r"\(16\) L", False), (r"\(1.5\) L", False)],
            "explanation": r"The acid stays at \(0.40 \times 10 = 4\) L. Adding \(x\) L of water: \(\frac{4}{10+x} = 0.25\), so \(10 + x = 16\) and \(x = 6\). The trap 16 is the new total volume, not the water added. Pro tip: in a dilution the solute amount is constant -- set it over the new total equal to the target percent.",
        },
        {
            "text": (r"A tax charges \(10\%\) on the first \$1{,}000 of income and \(20\%\) on every dollar above \$1{,}000. What is the tax on \$3{,}000?"),
            "difficulty": 3,
            "choices": [(r"\$500", True), (r"\$600", False), (r"\$400", False), (r"\$300", False)],
            "explanation": r"First \$1,000: \(0.10 \times 1000 = \$100\). The remaining \$2,000: \(0.20 \times 2000 = \$400\). Total \(= \$500\). The trap \$600 applies 20% to all \$3,000. Pro tip: a bracketed tax applies each rate only to the income inside that bracket, then adds the pieces.",
        },
        # ----- Ratios, rates, variation -----
        {
            "text": (r"A bag's red-to-blue marble ratio is \(5:3\). After \(8\) more blue marbles are added, the ratio becomes \(1:1\). How many red marbles are there?"),
            "difficulty": 3,
            "choices": [(r"\(20\)", True), (r"\(12\)", False), (r"\(5\)", False), (r"\(32\)", False)],
            "explanation": r"Let reds \(=5k\) and blues \(=3k\). After adding 8 blue, reds equal blues: \(5k = 3k + 8\), so \(2k = 8\), \(k = 4\), and reds \(= 5(4) = 20\). The trap 12 gives the original blue count. Pro tip: write both quantities with the same multiplier \(k\), then translate the new condition into an equation.",
        },
        {
            "text": (r"Pump A fills a tank in \(6\) hours, pump B in \(8\) hours, and pump C in \(12\) hours. Working together, about how long do they take?"),
            "difficulty": 3,
            "choices": [(r"\(\approx 2.67\) hours", True), (r"\(\approx 8.67\) hours", False), (r"\(3\) hours", False), (r"\(2\) hours", False)],
            "explanation": r"Add the rates: \(\frac{1}{6}+\frac{1}{8}+\frac{1}{12} = \frac{4+3+2}{24} = \frac{9}{24} = \frac{3}{8}\) tank/hour, so the time is \(\frac{8}{3} \approx 2.67\) hours. The trap 8.67 adds the times. Pro tip: combined work adds rates (tanks per hour); invert the total rate to get the time.",
        },
        {
            "text": (r"A trip covers \(90\) miles at \(30\) mph, then \(120\) miles at \(60\) mph. What is the average speed for the whole trip?"),
            "difficulty": 3,
            "choices": [(r"\(42\) mph", True), (r"\(45\) mph", False), (r"\(90\) mph", False), (r"\(50\) mph", False)],
            "explanation": r"Time \(= \frac{90}{30} + \frac{120}{60} = 3 + 2 = 5\) hours for \(90 + 120 = 210\) miles, so average \(= \frac{210}{5} = 42\) mph. The trap 45 averages the two speeds. Pro tip: average speed is always total distance divided by total time, never the mean of the speeds.",
        },
        {
            "text": (r"A metal bar measuring \(5 \times 4 \times 2\) cm has a mass of \(772\) grams. What is its density?"),
            "difficulty": 3,
            "choices": [(r"\(19.3\ \text{g/cm}^3\)", True), (r"\(30.9\ \text{g/cm}^3\)", False), (r"\(0.052\ \text{g/cm}^3\)", False), (r"\(193\ \text{g/cm}^3\)", False)],
            "explanation": r"Volume \(= 5 \times 4 \times 2 = 40\ \text{cm}^3\). Density \(= \frac{772}{40} = 19.3\ \text{g/cm}^3\). The trap 0.052 divides volume by mass. Pro tip: density is mass over volume -- find the volume first, then divide.",
        },
        {
            "text": (r"\(8\) workers build a wall in \(15\) days. Working at the same rate, how long would \(12\) workers take?"),
            "difficulty": 3,
            "choices": [(r"\(10\) days", True), (r"\(22.5\) days", False), (r"\(7.5\) days", False), (r"\(20\) days", False)],
            "explanation": r"The job is \(8 \times 15 = 120\) worker-days. With 12 workers: \(120 \div 12 = 10\) days. The trap 22.5 scales the wrong way (more workers should mean fewer days). Pro tip: this is inverse variation -- the product (workers times days) stays constant.",
        },
        # ----- Data, statistics, probability -----
        {
            "text": (r"If \(5\) is added to every value in a data set, what happens to the mean and the standard deviation?"),
            "difficulty": 3,
            "choices": [("The mean increases by 5; the standard deviation is unchanged", True),
                        ("Both increase by 5", False),
                        ("The mean is unchanged; the standard deviation increases by 5", False),
                        ("Both are unchanged", False)],
            "explanation": r"Shifting every value by the same amount slides the center up by 5 but doesn't change how spread out the values are, so the mean rises by 5 and the standard deviation stays the same. The trap 'both increase' forgets that spread is unaffected by a shift. Pro tip: adding a constant moves the mean; only stretching or squeezing the data changes the standard deviation.",
        },
        {
            "text": (r"A student wants an average of \(85\) over four tests. The first three scores are \(80,\ 88,\) and \(84\). What is needed on the fourth test?"),
            "difficulty": 3,
            "choices": [(r"\(88\)", True), (r"\(85\)", False), (r"\(90\)", False), (r"\(86\)", False)],
            "explanation": r"The four tests must total \(4 \times 85 = 340\). The first three sum to \(252\), so the fourth must be \(340 - 252 = 88\). The trap 85 just repeats the target average. Pro tip: multiply the goal average by the number of items to get the required total, then subtract what you already have.",
        },
        {
            "text": (r"In a group, \(60\%\) like tea and \(30\%\) like both tea and coffee. Among the people who like tea, what fraction also like coffee?"),
            "difficulty": 3,
            "choices": [(r"\(50\%\)", True), (r"\(30\%\)", False), (r"\(18\%\)", False), (r"\(90\%\)", False)],
            "explanation": r"Conditional probability: \(\frac{P(\text{tea and coffee})}{P(\text{tea})} = \frac{0.30}{0.60} = 0.50 = 50\%\). The trap 30% reports the joint percent without conditioning on tea. Pro tip: 'among those who like tea' means divide by the tea group, not the whole group.",
        },
        {
            "text": (r"In how many ways can a committee of \(2\) be chosen from \(6\) people (order does not matter)?"),
            "difficulty": 3,
            "choices": [(r"\(15\)", True), (r"\(30\)", False), (r"\(12\)", False), (r"\(36\)", False)],
            "explanation": r"Combinations: \({}_6C_2 = \frac{6 \times 5}{2 \times 1} = 15\). The trap 30 is the ordered count \((6 \times 5)\), which double-counts each pair. Pro tip: when order doesn't matter, divide the ordered count by the number of arrangements of the chosen group.",
        },
        {
            "text": (r"A fair six-sided die is rolled once, and you win a number of dollars equal to the face shown. What is the expected value of the game?"),
            "difficulty": 3,
            "choices": [(r"\$3.50", True), (r"\$3.00", False), (r"\$21.00", False), (r"\$6.00", False)],
            "explanation": r"Each face has probability \(\frac{1}{6}\): \(\frac{1+2+3+4+5+6}{6} = \frac{21}{6} = \$3.50\). The trap \$21 forgets to divide by the 6 outcomes. Pro tip: expected value is the average outcome -- here the mean of the equally likely faces 1 through 6.",
        },
        {
            "text": (r"Three true/false questions are answered by random guessing. What is the probability of getting at least one wrong?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{7}{8}\)", True), (r"\(\frac{1}{8}\)", False), (r"\(\frac{3}{8}\)", False), (r"\(\frac{1}{2}\)", False)],
            "explanation": r"P(all three right) \(= \left(\frac{1}{2}\right)^3 = \frac{1}{8}\), so P(at least one wrong) \(= 1 - \frac{1}{8} = \frac{7}{8}\). The trap \(\frac{1}{8}\) is the chance of getting them all right. Pro tip: 'at least one wrong' is the complement of 'all correct.'",
        },
        # ----- Geometry & measurement (mastery) -----
        {
            "text": ("Use the cylinder below.\n\n"
                     "[[figure:cylinder_volume|A cylinder with its radius and height labeled]]\n\n"
                     r"A solid is a cylinder of radius \(3\) and height \(10\) with a hemisphere of radius \(3\) on top. What is the total volume? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 339.1\)", True), (r"\(\approx 395.6\)", False), (r"\(\approx 282.6\)", False), (r"\(\approx 452.2\)", False)],
            "explanation": r"Cylinder \(= \pi r^2 h = \pi(9)(10) = 90\pi\). Hemisphere \(= \frac{1}{2}\cdot\frac{4}{3}\pi r^3 = \frac{2}{3}\pi(27) = 18\pi\). Total \(= 108\pi \approx 339.1\). The trap 282.6 leaves off the hemisphere. Pro tip: a hemisphere is half a sphere -- \(\frac{2}{3}\pi r^3\) -- so find each piece and add.",
        },
        {
            "text": (r"Two triangles are similar. Sides of \(6\) and \(9\) in the small triangle correspond to \(x\) and \(15\) in the large triangle. What is \(x\)?"),
            "difficulty": 3,
            "choices": [(r"\(10\)", True), (r"\(9\)", False), (r"\(22.5\)", False), (r"\(4\)", False)],
            "explanation": r"Corresponding sides are proportional: \(\frac{6}{x} = \frac{9}{15}\), so \(9x = 90\) and \(x = 10\). The trap 22.5 sets up \(\frac{6}{9} = \frac{15}{x}\) with the pairs crossed. Pro tip: match corresponding sides carefully -- the 9 pairs with the 15, so 6 pairs with \(x\).",
        },
        {
            "text": ("Use the coordinate grid below.\n\n"
                     "[[figure:coordinate_quadrants|The coordinate plane with its four quadrants]]\n\n"
                     r"A triangle has vertices at \((1,1)\), \((5,1)\), and \((3,6)\). What is its area?"),
            "difficulty": 3,
            "choices": [(r"\(10\)", True), (r"\(20\)", False), (r"\(12\)", False), (r"\(7.5\)", False)],
            "explanation": r"The base from \((1,1)\) to \((5,1)\) is 4 units long, and the height up to \(y = 6\) is \(6 - 1 = 5\). Area \(= \frac{1}{2}(4)(5) = 10\). The trap 20 forgets the \(\frac{1}{2}\). Pro tip: pick the horizontal side as the base, measure the vertical distance to the third point as the height.",
        },
        {
            "text": (r"An isosceles right triangle has two legs of length \(5\). What is the length of its hypotenuse?"),
            "difficulty": 3,
            "choices": [(r"\(5\sqrt{2}\)", True), (r"\(10\)", False), (r"\(25\)", False), (r"\(7.5\)", False)],
            "explanation": r"\(c = \sqrt{5^2 + 5^2} = \sqrt{50} = 5\sqrt2\). The trap 10 just adds the legs. Pro tip: in a 45-45-90 triangle the hypotenuse is always a leg times \(\sqrt2\).",
        },
        {
            "text": (r"A ring (annulus) has an outer radius of \(7\) and an inner radius of \(4\). What is its area? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 103.6\)", True), (r"\(\approx 9.4\)", False), (r"\(\approx 153.9\)", False), (r"\(\approx 28.3\)", False)],
            "explanation": r"Area \(= \pi R^2 - \pi r^2 = \pi(49 - 16) = 33\pi \approx 103.6\). The trap 153.9 uses only the outer circle. Pro tip: a ring's area is the big circle minus the hole -- subtract the radii squared, then multiply by \(\pi\).",
        },
        {
            "text": (r"A cone has a volume of \(96\pi\). If its radius and height are both doubled, what is the new volume?"),
            "difficulty": 3,
            "choices": [(r"\(768\pi\)", True), (r"\(192\pi\)", False), (r"\(384\pi\)", False), (r"\(96\pi\)", False)],
            "explanation": r"Volume scales by the cube of the linear factor: doubling both gives \(2^3 = 8\) times, so \(96\pi \times 8 = 768\pi\). The trap 192 just doubles. Pro tip: when every linear dimension is multiplied by \(k\), the volume is multiplied by \(k^3\).",
        },
        {
            "text": (r"A rectangular floor is \(12\) ft by \(10\) ft. Carpet costs \$3.50 per square foot. What is the total cost to carpet the floor?"),
            "difficulty": 3,
            "choices": [(r"\$420", True), (r"\$385", False), (r"\$77", False), (r"\$840", False)],
            "explanation": r"Area \(= 12 \times 10 = 120\ \text{ft}^2\); cost \(= 120 \times 3.50 = \$420\). The trap \$77 multiplies the perimeter by the rate. Pro tip: carpet covers area, so find square feet first, then multiply by the price per square foot.",
        },
        {
            "text": (r"Two parallel lines are cut by a transversal. One interior angle measures \(110^\circ\). What is the measure of the co-interior (same-side interior) angle?"),
            "difficulty": 3,
            "choices": [(r"\(70^\circ\)", True), (r"\(110^\circ\)", False), (r"\(90^\circ\)", False), (r"\(35^\circ\)", False)],
            "explanation": r"Co-interior angles on the same side of the transversal are supplementary: \(180 - 110 = 70^\circ\). The trap 110 assumes they're equal (that's alternate interior angles). Pro tip: same-side interior angles add to 180; alternate interior angles are equal.",
        },
        {
            "text": (r"A trapezoid has parallel sides of \(10\) and \(6\) and an area of \(48\). What is its height?"),
            "difficulty": 3,
            "choices": [(r"\(6\)", True), (r"\(3\)", False), (r"\(12\)", False), (r"\(8\)", False)],
            "explanation": r"\(A = \frac{1}{2}(b_1+b_2)h\): \(48 = \frac{1}{2}(16)h = 8h\), so \(h = 6\). The trap 3 forgets to use the full base sum. Pro tip: plug the knowns into the area formula and solve for the missing height like any equation.",
        },
        # ----- Coordinate geometry / lines -----
        {
            "text": (r"What is the equation of the line through \((2,\ 5)\) that is perpendicular to \(y = 2x + 1\)?"),
            "difficulty": 3,
            "choices": [(r"\(y = -\tfrac{1}{2}x + 6\)", True), (r"\(y = 2x + 1\)", False), (r"\(y = -\tfrac{1}{2}x + 5\)", False), (r"\(y = \tfrac{1}{2}x + 6\)", False)],
            "explanation": r"Perpendicular slope is the negative reciprocal of 2, which is \(-\frac{1}{2}\). Through \((2,5)\): \(5 = -\frac{1}{2}(2) + b = -1 + b\), so \(b = 6\), giving \(y = -\frac{1}{2}x + 6\). The trap with \(+5\) skips solving for \(b\). Pro tip: flip and negate the slope, then plug in the point to find the intercept.",
        },
        {
            "text": (r"Where does the line \(3x - 4y = 24\) cross the x-axis?"),
            "difficulty": 3,
            "choices": [(r"\((8,\ 0)\)", True), (r"\((0,\ -6)\)", False), (r"\((0,\ 8)\)", False), (r"\((24,\ 0)\)", False)],
            "explanation": r"The x-intercept has \(y = 0\): \(3x = 24\), so \(x = 8\), giving \((8, 0)\). The trap \((0,-6)\) is the y-intercept. Pro tip: set \(y = 0\) for an x-intercept (and \(x = 0\) for a y-intercept).",
        },
        # ----- Algebra: expressions -----
        {
            "text": (r"Simplify: \((x + 3)^2 - (x - 2)^2\)."),
            "difficulty": 3,
            "choices": [(r"\(10x + 5\)", True), (r"\(5\)", False), (r"\(2x + 5\)", False), (r"\(10x + 13\)", False)],
            "explanation": r"Expand: \((x^2 + 6x + 9) - (x^2 - 4x + 4) = 10x + 5\). The trap \(10x + 13\) adds the constants instead of subtracting. Pro tip: distribute the minus sign to every term of the second square before combining.",
        },
        {
            "text": (r"Factor by grouping: \(x^3 + 2x^2 + 3x + 6\)."),
            "difficulty": 3,
            "choices": [(r"\((x + 2)(x^2 + 3)\)", True), (r"\((x + 3)(x^2 + 2)\)", False), (r"\((x + 2)(x^2 - 3)\)", False), (r"\((x^2 + 2)(x + 3)\)", False)],
            "explanation": r"Group: \(x^2(x + 2) + 3(x + 2) = (x + 2)(x^2 + 3)\). The trap \((x+3)(x^2+2)\) pairs the terms incorrectly. Pro tip: factor each pair, and if the leftover parentheses match, pull that common binomial out front.",
        },
        {
            "text": (r"Simplify: \(\dfrac{1}{x} - \dfrac{1}{x + 1}\)."),
            "difficulty": 3,
            "choices": [(r"\(\dfrac{1}{x^2 + x}\)", True), (r"\(0\)", False), (r"\(\dfrac{1}{2x + 1}\)", False), (r"\(-\dfrac{1}{x^2 + x}\)", False)],
            "explanation": r"Common denominator \(x(x+1)\): \(\frac{(x+1) - x}{x(x+1)} = \frac{1}{x(x+1)} = \frac{1}{x^2 + x}\). The trap \(\frac{1}{2x+1}\) just adds the denominators. Pro tip: get a common denominator first, then subtract the numerators.",
        },
        # ----- Algebra: equations -----
        {
            "text": (r"Solve using the quadratic formula: \(2x^2 - 4x - 3 = 0\)."),
            "difficulty": 3,
            "choices": [(r"\(x = \dfrac{2 \pm \sqrt{10}}{2}\)", True), (r"\(x = \dfrac{4 \pm \sqrt{10}}{2}\)", False), (r"\(x = \dfrac{2 \pm \sqrt{10}}{4}\)", False), (r"\(x = 1 \pm \sqrt{10}\)", False)],
            "explanation": r"With \(a=2, b=-4, c=-3\): \(x = \frac{4 \pm \sqrt{16 + 24}}{4} = \frac{4 \pm \sqrt{40}}{4} = \frac{4 \pm 2\sqrt{10}}{4} = \frac{2 \pm \sqrt{10}}{2}\). The trap keeps \(\frac{4 \pm \sqrt{10}}{2}\) without simplifying. Pro tip: the discriminant is \(16 - 4(2)(-3) = 40\); simplify \(\sqrt{40} = 2\sqrt{10}\) and reduce.",
        },
        {
            "text": (r"Solve the system: \(y = x^2\) and \(y = x + 6\). What is the point with the positive \(x\)-value?"),
            "difficulty": 3,
            "choices": [(r"\((3,\ 9)\)", True), (r"\((-2,\ 4)\)", False), (r"\((3,\ 6)\)", False), (r"\((2,\ 4)\)", False)],
            "explanation": r"Set equal: \(x^2 = x + 6\), so \(x^2 - x - 6 = 0 = (x-3)(x+2)\). The positive solution is \(x = 3\), giving \(y = 3^2 = 9\). The trap \((-2,4)\) is the other intersection. Pro tip: substitute one equation into the other, solve the quadratic, then read the requested point.",
        },
        {
            "text": (r"Solve for \(x\): \(\dfrac{x + 3}{x - 1} = 2\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 5\)", True), (r"\(x = 1\)", False), (r"\(x = -5\)", False), (r"\(x = 2.5\)", False)],
            "explanation": r"Cross-multiply: \(x + 3 = 2(x - 1) = 2x - 2\), so \(5 = x\). The trap \(x = 1\) would make the denominator zero (undefined). Pro tip: clear the fraction by cross-multiplying, then check your answer doesn't make any denominator zero.",
        },
        {
            "text": (r"Simple interest is \(I = Prt\). Solve this formula for \(t\)."),
            "difficulty": 3,
            "choices": [(r"\(t = \dfrac{I}{Pr}\)", True), (r"\(t = IPr\)", False), (r"\(t = \dfrac{I}{P} + r\)", False), (r"\(t = \dfrac{Pr}{I}\)", False)],
            "explanation": r"Divide both sides by \(Pr\): \(t = \frac{I}{Pr}\). The trap \(\frac{Pr}{I}\) flips the fraction. Pro tip: \(P\), \(r\), and \(t\) are all multiplied, so divide by the two you're not solving for.",
        },
        {
            "text": (r"A theater sells \$12 adult tickets and \$8 child tickets. It sells \(200\) tickets for a total of \$2{,}160. How many adult tickets were sold?"),
            "difficulty": 3,
            "choices": [(r"\(140\)", True), (r"\(60\)", False), (r"\(110\)", False), (r"\(90\)", False)],
            "explanation": r"Let \(a\) be adults and \(200 - a\) children: \(12a + 8(200 - a) = 2160\). Then \(12a + 1600 - 8a = 2160\), so \(4a = 560\) and \(a = 140\). The trap 60 is the number of child tickets. Pro tip: write one variable in terms of the total, substitute, and re-read which group is asked.",
        },
        # ----- Algebra: inequalities -----
        {
            "text": (r"Solve the quadratic inequality: \(x^2 - 5x + 6 < 0\)."),
            "difficulty": 3,
            "choices": [(r"\(2 < x < 3\)", True), (r"\(x < 2\) or \(x > 3\)", False), (r"\(-3 < x < -2\)", False), (r"\(x > 3\)", False)],
            "explanation": r"Factor: \((x - 2)(x - 3) < 0\). A product is negative only between its roots, so \(2 < x < 3\). The trap '\(x<2\) or \(x>3\)' is the solution to the '\(>0\)' version. Pro tip: for '\(<0\),' the answer is between the roots; for '\(>0\),' it's outside them.",
        },
        {
            "text": (r"Solve: \(|2x + 1| \ge 5\)."),
            "difficulty": 3,
            "choices": [(r"\(x \le -3\) or \(x \ge 2\)", True), (r"\(-3 \le x \le 2\)", False), (r"\(x \ge 2\)", False), (r"\(x \le -3\)", False)],
            "explanation": r"Split: \(2x + 1 \ge 5 \Rightarrow x \ge 2\), or \(2x + 1 \le -5 \Rightarrow 2x \le -6 \Rightarrow x \le -3\). The trap \(-3 \le x \le 2\) is the solution to a '\(\le\)' (between) inequality. Pro tip: '\(\ge\)' absolute values split into two outward pieces joined by 'or.'",
        },
        # ----- Functions, exponential, sequences -----
        {
            "text": (r"If \(f(x) = 2x - 3\), for what value of \(x\) does \(f(f(x)) = 5\)?"),
            "difficulty": 3,
            "choices": [(r"\(x = 3.5\)", True), (r"\(x = 2\)", False), (r"\(x = 5\)", False), (r"\(x = 1\)", False)],
            "explanation": r"\(f(f(x)) = 2(2x - 3) - 3 = 4x - 9\). Set equal to 5: \(4x = 14\), so \(x = 3.5\). The trap \(x = 2\) solves only \(f(x) = 5\) once. Pro tip: apply the function twice to build the expression, then solve the resulting equation.",
        },
        {
            "text": (r"A bacterial culture doubles every \(3\) hours, starting at \(100\) cells. After how many hours does it reach \(800\) cells?"),
            "difficulty": 3,
            "choices": [(r"\(9\) hours", True), (r"\(24\) hours", False), (r"\(8\) hours", False), (r"\(6\) hours", False)],
            "explanation": r"\(800 \div 100 = 8 = 2^3\), so it takes 3 doublings. At 3 hours each, that's \(3 \times 3 = 9\) hours. The trap 24 multiplies \(8 \times 3\). Pro tip: figure out how many doublings reach the target (here 3), then multiply by the doubling time.",
        },
        {
            "text": (r"A \$20{,}000 machine loses \(10\%\) of its value each year. After how many whole years is it first worth less than \$15{,}000?"),
            "difficulty": 3,
            "choices": [(r"\(3\) years", True), (r"\(2\) years", False), (r"\(4\) years", False), (r"\(5\) years", False)],
            "explanation": r"Each year multiply by 0.9: after 1 yr \$18,000; after 2 yr \$16,200; after 3 yr \$14,580, which is first below \$15,000. The trap 2 years (\$16,200) is still above. Pro tip: step through the multiplications by 0.9 until you cross the threshold -- exponential decay isn't a flat subtraction.",
        },
        {
            "text": (r"In the arithmetic sequence \(5,\ 8,\ 11,\ 14,\ \dots\), what is the \(20^{\text{th}}\) term?"),
            "difficulty": 3,
            "choices": [(r"\(62\)", True), (r"\(65\)", False), (r"\(60\)", False), (r"\(59\)", False)],
            "explanation": r"The common difference is 3, so \(a_{20} = a_1 + (n-1)d = 5 + 19(3) = 5 + 57 = 62\). The trap 65 uses 20 steps instead of 19. Pro tip: the \(n\)th term adds the difference \((n-1)\) times, because the first term takes no step.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the mastery (Level 4) full-length GED Mathematical Reasoning practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 5 no-calculator, Part 2: 41 calculator; mastery level)."
        ))
