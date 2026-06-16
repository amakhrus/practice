"""
Seed a FIFTH and FINAL full-length 'GED Mathematical Reasoning' practice exam --
Level 5, the elite tier, the hardest of the whole set.

Same test-day structure (46 questions, 115 minutes, a no-calculator Part 1 of 5
then a calculator Part 2 of 41, formula sheet provided, scored 100-200, 145 to
pass). Every item is a hard, multi-concept problem at the absolute ceiling of the
GED's range -- the toughest questions a strong test-taker might ever meet:

  - Fractional/negative exponents, rationalizing radicals, exponent equations,
    complex fractions.
  - Quarterly compound interest, reverse markup-plus-tax, percent-of-a-percent,
    profit margin, two-source alligation mixtures.
  - Three-way chained ratios, part-time pump scheduling, an unknown trip leg,
    currency conversion, gear (inverse) ratios.
  - Outlier effects, reverse weighted returns, conditional probability from a
    two-way table, permutations, the addition rule, variance.
  - Drilled-out volumes, sphere surface area, circle-from-diameter, 30-60-90 and
    equilateral geometry, inscribed angles, area-to-volume, similar-figure ratios.
  - Compound rational expressions, quadratic word problems, exponent equations,
    quadratic and absolute-value inequalities, inverse functions, half-life decay,
    geometric sequences, and vertex-form roots.

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip.

Run:
    python manage.py seed_ged_math_exam_level5
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Mathematical Reasoning: Full-Length Practice Exam (Level 5 - Elite)",
    "slug": "ged-math-reasoning-exam-level5",
    "program": "GED",
    "subject": "math",
    "description": (
        "The fifth and hardest full-length GED Mathematical Reasoning practice exam -- the elite tier, "
        "for students who have cleared Levels 1-4 and want the toughest possible rehearsal. Same test-day "
        "format (46 questions in 115 minutes, a no-calculator Part 1 then a calculator Part 2, with a "
        "provided formula sheet, scored 100-200, 145 to pass), but every single item sits at the absolute "
        "ceiling of the GED's range and layers several concepts: rationalizing radicals and exponent "
        "equations, quarterly compound interest, alligation mixtures, profit margins, three-way chained "
        "ratios, gear (inverse) ratios, conditional probability from two-way tables, permutations and the "
        "addition rule, variance, drilled-out and sphere geometry, 30-60-90 and equilateral triangles, "
        "inscribed angles, compound rational expressions, quadratic word problems, quadratic and "
        "absolute-value inequalities, inverse functions, half-life decay, geometric sequences, and "
        "vertex-form roots. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 5: The Elite Test",
            r"""
This is the **elite** GED Mathematical Reasoning practice exam -- the final and hardest of all five. The format never changes:

- **46 questions** in **115 minutes**.
- **Part 1 (Questions 1-5): NO CALCULATOR.** Expect fractional and negative exponents, rationalizing a radical, an exponent equation, and a complex fraction -- all by hand.
- **Part 2 (Questions 6-46): CALCULATOR ALLOWED.**
- A **formula sheet** is provided (next lesson); no returning to Part 1 once Part 2 begins.
- Scored **100-200**, with **145 to pass**. No penalty for wrong answers.

**What makes Level 5 the hardest of all:** there is not a single routine question. **Every** item is a hard problem that **stacks multiple ideas** and often hides the real question one step past the obvious answer. If you can score well here, the real GED Math test will feel comfortable.

[[check:If you can pass Level 5, how should the real GED Math test feel by comparison -- harder or easier?|easier|Level 5 is tougher than the real test, so the real exam should feel easier.]]
            """,
        ),
        (
            "2. The Formula Sheet & Every Tool You Need",
            r"""
You get the **formula sheet**, but the elite items test whether you can reach for the right tool fast and combine tools.

**Exponents & radicals**
- \(a^{m/n} = \left(\sqrt[n]{a}\right)^m\); \(a^{-n} = \dfrac{1}{a^n}\); rationalize by multiplying by \(\dfrac{\sqrt{b}}{\sqrt{b}}\).

**Geometry**
- Sphere: volume \(\tfrac43\pi r^3\), surface area \(4\pi r^2\).
- Equilateral triangle area: \(\dfrac{\sqrt3}{4}s^2\); 30-60-90 sides are \(x : x\sqrt3 : 2x\); 45-45-90 are \(x : x : x\sqrt2\).
- Inscribed angle in a semicircle is \(90^\circ\).

**Algebra & sequences**
- Quadratic formula \(x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}\); vertex form \(y=a(x-h)^2+k\) has vertex \((h,k)\).
- Arithmetic: \(a_n=a_1+(n-1)d\). Geometric: \(a_n=a_1 r^{\,n-1}\).
- Inverse function: swap \(x\) and \(y\), then solve for \(y\).

**Counting & probability**
- Permutations \({}_nP_r=\dfrac{n!}{(n-r)!}\); combinations \({}_nC_r=\dfrac{n!}{r!(n-r)!}\).
- Addition rule: \(P(A\text{ or }B)=P(A)+P(B)-P(A\text{ and }B)\). Conditional: \(P(B\mid A)=\dfrac{P(A\text{ and }B)}{P(A)}\).

**Growth & decay**
- Compound: multiply by \((1+\tfrac{r}{n})\) per period; half-life: multiply by \(\tfrac12\) each half-life.

[[figure:formula_substitution_flow|At the elite level, the answer is usually one step past the obvious -- name the concept, pick the tool, and read the exact question being asked.]]

[[check:A quantity halves every 5 years. After 15 years, what fraction of the original remains?|1/8;;one eighth;;0.125|Three half-lives means one-half cubed, which is one eighth.]]
            """,
        ),
        (
            "3. Strategy for Elite Items",
            r"""
At this level, every point is earned by disciplined process.

- **Decode the layers out loud.** "Markup, then tax." "Two solutions mixed to a target." "Doubling, then count terms." Name each before touching the calculator.
- **Backsolve relentlessly.** For quadratics, rational, exponent, and absolute-value equations, testing the numeric choices is often the fastest and safest path -- and it exposes extraneous roots.
- **Answer the exact target.** Elite traps hand you a correct intermediate value -- the cost, the time, the first root, the y-intercept -- when the question wants the next thing.
- **Use complements, conditionals, and ratios.** 'At least one' is \(1 - P(\text{none})\); 'among those who…' divides by that group; area ratios are the square, volume ratios the cube, of the length ratio.
- **Handle inequalities with care.** Flip on a negative; split \(|x|>c\) into two outward pieces; a quadratic inequality is between or outside its roots.
- **Estimate to defend the point.** A quick estimate catches a misplaced decimal or a wrong sign before it costs you.

[[check:For the addition rule P(A or B), what do you subtract to avoid double-counting?|P(A and B);;the overlap;;the intersection;;P(A and B), the overlap|Subtract the overlap, P(A and B), since it was counted in both P(A) and P(B).]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  QUESTIONS 1-5  --  NO CALCULATOR ============
        # =====================================================================
        {
            "text": (r"**No-calculator section.** Evaluate: \(27^{2/3} + 4^{-1/2}\)."),
            "difficulty": 3,
            "choices": [(r"\(\frac{19}{2}\)", True), (r"\(18\)", False), (r"\(9\)", False), (r"\(\frac{37}{4}\)", False)],
            "explanation": r"\(27^{2/3} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9\), and \(4^{-1/2} = \frac{1}{\sqrt4} = \frac{1}{2}\). Sum \(= 9 + \frac{1}{2} = \frac{19}{2}\). The trap 18 doubles 9 instead of adding a half. Pro tip: the denominator of a fractional exponent is the root; a negative one means take the reciprocal.",
        },
        {
            "text": (r"**No-calculator section.** Rationalize and simplify: \(\dfrac{6}{\sqrt{3}}\)."),
            "difficulty": 3,
            "choices": [(r"\(2\sqrt{3}\)", True), (r"\(6\sqrt{3}\)", False), (r"\(\sqrt{2}\)", False), (r"\(2\)", False)],
            "explanation": r"Multiply by \(\frac{\sqrt3}{\sqrt3}\): \(\frac{6\sqrt3}{3} = 2\sqrt3\). The trap \(6\sqrt3\) forgets to divide by 3. Pro tip: to clear a radical from the denominator, multiply top and bottom by that radical.",
        },
        {
            "text": (r"**No-calculator section.** Solve for \(x\): \(3^{x+1} = 81\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 3\)", True), (r"\(x = 4\)", False), (r"\(x = 26\)", False), (r"\(x = 2\)", False)],
            "explanation": r"Write 81 as \(3^4\): \(3^{x+1} = 3^4\), so \(x + 1 = 4\) and \(x = 3\). The trap 4 forgets to subtract the 1. Pro tip: rewrite both sides as the same base, then set the exponents equal.",
        },
        {
            "text": (r"**No-calculator section.** Simplify the complex fraction: \(\dfrac{\frac{1}{2} + \frac{1}{3}}{\frac{1}{6}}\)."),
            "difficulty": 3,
            "choices": [(r"\(5\)", True), (r"\(\frac{1}{5}\)", False), (r"\(\frac{5}{6}\)", False), (r"\(30\)", False)],
            "explanation": r"Top: \(\frac{1}{2} + \frac{1}{3} = \frac{5}{6}\). Dividing by \(\frac{1}{6}\) means multiplying by 6: \(\frac{5}{6} \times 6 = 5\). The trap \(\frac{5}{6}\) stops before dividing. Pro tip: simplify the numerator first, then dividing by \(\frac{1}{6}\) is the same as multiplying by 6.",
        },
        {
            "text": (r"**No-calculator section.** Simplify: \(\dfrac{x^{-2} \cdot x^{5}}{x^{-1}}\)."),
            "difficulty": 3,
            "choices": [(r"\(x^4\)", True), (r"\(x^2\)", False), (r"\(x^6\)", False), (r"\(x^{-8}\)", False)],
            "explanation": r"Top: \(x^{-2+5} = x^3\). Dividing by \(x^{-1}\) adds 1 to the exponent: \(x^{3-(-1)} = x^4\). The trap \(x^2\) subtracts the \(-1\) the wrong way. Pro tip: dividing by a negative exponent flips it to a positive, so it gets added.",
        },
        # =====================================================================
        # ============ PART 2  --  QUESTIONS 6-46  --  CALCULATOR =============
        # =====================================================================
        # ----- Percents & finance -----
        {
            "text": (r"\$5{,}000 is invested at \(12\%\) annual interest, compounded quarterly. What is it worth after \(1\) year?"),
            "difficulty": 3,
            "choices": [(r"\$5{,}627.54", True), (r"\$5{,}600.00", False), (r"\$5{,}640.00", False), (r"\$5{,}609.00", False)],
            "explanation": r"Quarterly means four periods of \(3\%\): \(5000 \times 1.03^4 = 5000 \times 1.1255 \approx \$5{,}627.54\). The trap \$5,600 applies a single 12%. Pro tip: divide the annual rate by the number of periods (here 4) and raise \((1+r)\) to that many periods.",
        },
        {
            "text": (r"A final price includes a \(25\%\) markup and then an \(8\%\) tax, ending at \$135. What was the original cost?"),
            "difficulty": 3,
            "choices": [(r"\$100", True), (r"\$96.30", False), (r"\$108", False), (r"\$125", False)],
            "explanation": r"The factors multiply: \(1.25 \times 1.08 = 1.35\), so cost \(= 135 \div 1.35 = \$100\). The trap \$125 undoes only the markup. Pro tip: combine the multipliers first, then divide the final price by the single combined factor.",
        },
        {
            "text": (r"An interest rate rises from \(4\%\) to \(5\%\). By what percent did the rate increase?"),
            "difficulty": 3,
            "choices": [(r"\(25\%\)", True), (r"\(1\%\)", False), (r"\(20\%\)", False), (r"\(100\%\)", False)],
            "explanation": r"Percent change \(= \frac{5 - 4}{4} = \frac{1}{4} = 25\%\). The trap 1% reports the 1 percentage-point rise, not the percent increase. Pro tip: a rise from 4 to 5 is one percentage point but a 25% increase -- divide the change by the original.",
        },
        {
            "text": (r"A product sells for \$150 at a \(25\%\) profit margin (profit measured as a percent of the selling price). What was the cost?"),
            "difficulty": 3,
            "choices": [(r"\$112.50", True), (r"\$120", False), (r"\$187.50", False), (r"\$37.50", False)],
            "explanation": r"Profit \(= 0.25 \times 150 = \$37.50\), so cost \(= 150 - 37.50 = \$112.50\). The trap \$120 divides by 1.25 (margin on cost, not on price). Pro tip: 'margin on selling price' means the profit is a percent of the \$150, so subtract it from the price.",
        },
        {
            "text": (r"How many liters of a \(50\%\) solution are needed, mixed with a \(20\%\) solution, to make \(30\) liters of a \(40\%\) solution?"),
            "difficulty": 3,
            "choices": [(r"\(20\) L", True), (r"\(10\) L", False), (r"\(15\) L", False), (r"\(24\) L", False)],
            "explanation": r"Let \(x\) be liters of the 50% solution: \(0.50x + 0.20(30 - x) = 0.40(30) = 12\). Then \(0.30x + 6 = 12\), so \(x = 20\) L. The trap 10 L is the amount of the 20% solution. Pro tip: track the actual solute from each source, set the total equal to the target, and re-read which solution is asked.",
        },
        # ----- Ratios, rates, variation -----
        {
            "text": (r"Three quantities satisfy \(A:B = 3:4\) and \(B:C = 6:7\). If \(A + B + C = 70\), what is \(C\)?"),
            "difficulty": 3,
            "choices": [(r"\(28\)", True), (r"\(24\)", False), (r"\(18\)", False), (r"\(20\)", False)],
            "explanation": r"Make B match: \(A:B = 9:12\) and \(B:C = 12:14\), so \(A:B:C = 9:12:14\) (35 parts). Each part is \(70 \div 35 = 2\), so \(C = 14 \times 2 = 28\). The trap 24 uses B's share. Pro tip: scale both ratios so the shared term B is equal, then split the total by the number of parts.",
        },
        {
            "text": (r"Pipe A fills a tank in \(10\) hours and pipe B in \(15\) hours. A runs alone for \(2\) hours, then both run together until full. What is the total time to fill the tank?"),
            "difficulty": 3,
            "choices": [(r"\(6.8\) hours", True), (r"\(4.8\) hours", False), (r"\(5\) hours", False), (r"\(6\) hours", False)],
            "explanation": r"In 2 hours A fills \(\frac{2}{10} = \frac{1}{5}\), leaving \(\frac{4}{5}\). Together the rate is \(\frac{1}{10} + \frac{1}{15} = \frac{1}{6}\) tank/hour, so the rest takes \(\frac{4/5}{1/6} = 4.8\) hours. Total \(= 2 + 4.8 = 6.8\) hours. The trap 4.8 forgets the first 2 hours. Pro tip: subtract the work done alone, then divide the remaining work by the combined rate.",
        },
        {
            "text": (r"A car averages \(48\) mph over a \(5\)-hour trip. It drove the first \(2\) hours at \(60\) mph. What was its average speed for the remaining \(3\) hours?"),
            "difficulty": 3,
            "choices": [(r"\(40\) mph", True), (r"\(36\) mph", False), (r"\(45\) mph", False), (r"\(42\) mph", False)],
            "explanation": r"Total distance \(= 48 \times 5 = 240\) miles. First leg \(= 60 \times 2 = 120\) miles, leaving \(120\) miles over 3 hours: \(120 \div 3 = 40\) mph. The trap 36 averages the wrong way. Pro tip: use total distance to back out the missing leg, then divide by its time.",
        },
        {
            "text": (r"An exchange rate is \(\$5 = 4\) euros. How many dollars does an item costing \(90\) euros cost?"),
            "difficulty": 3,
            "choices": [(r"\$112.50", True), (r"\$72.00", False), (r"\$450.00", False), (r"\$96.00", False)],
            "explanation": r"Each euro is \(\frac{5}{4} = \$1.25\), so \(90 \times 1.25 = \$112.50\). The trap \$72 multiplies by \(\frac{4}{5}\) (the wrong direction). Pro tip: set up the proportion so the units cancel -- dollars per euro times euros leaves dollars.",
        },
        {
            "text": (r"A gear with \(30\) teeth meshes with a gear of \(18\) teeth. If the \(30\)-tooth gear turns at \(60\) rpm, how fast does the \(18\)-tooth gear turn?"),
            "difficulty": 3,
            "choices": [(r"\(100\) rpm", True), (r"\(36\) rpm", False), (r"\(50\) rpm", False), (r"\(108\) rpm", False)],
            "explanation": r"Meshed gears satisfy \(\text{teeth} \times \text{rpm}\) constant: \(30 \times 60 = 18 \times n\), so \(n = \frac{1800}{18} = 100\) rpm. The trap 36 scales the wrong way. Pro tip: the smaller gear spins faster -- this is inverse variation, so the products of teeth and speed are equal.",
        },
        # ----- Data, statistics, probability -----
        {
            "text": (r"A data set is \(4,\ 5,\ 6,\ 7,\ 8\). The value \(50\) is then added to the set. Which is affected more, the mean or the median?"),
            "difficulty": 3,
            "choices": [("The mean, because it is pulled upward by the outlier", True),
                        ("The median, because the list grew longer", False),
                        ("Both change by the same amount", False),
                        ("Neither one changes", False)],
            "explanation": r"The mean jumps from 6 to \(\frac{80}{6} \approx 13.3\), while the median only moves from 6 to 6.5. The far-off value of 50 drags the mean up but barely shifts the median. The trap 'the median' has it backwards. Pro tip: the mean is sensitive to outliers; the median is resistant to them.",
        },
        {
            "text": (r"A portfolio holds \(60\%\) stocks returning \(10\%\) and \(40\%\) bonds. The overall return is \(7\%\). What was the bond return?"),
            "difficulty": 3,
            "choices": [(r"\(2.5\%\)", True), (r"\(4\%\)", False), (r"\(3\%\)", False), (r"\(1\%\)", False)],
            "explanation": r"Weighted: \(0.60(10) + 0.40b = 7\), so \(6 + 0.40b = 7\), giving \(0.40b = 1\) and \(b = 2.5\%\). The trap 4% forgets the stock contribution. Pro tip: set the weighted average equal to the overall return and solve for the unknown piece.",
        },
        {
            "text": (r"Of \(100\) people, \(70\) own a car and, of those, \(40\) own a house. Another \(20\) of the non-car-owners own a house. If a randomly chosen person owns a house, what is the probability they own a car?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{2}{3}\)", True), (r"\(\frac{4}{7}\)", False), (r"\(\frac{2}{5}\)", False), (r"\(\frac{1}{2}\)", False)],
            "explanation": r"Total house owners \(= 40 + 20 = 60\); those who also own a car \(= 40\). So \(P(\text{car} \mid \text{house}) = \frac{40}{60} = \frac{2}{3}\). The trap \(\frac{4}{7}\) divides by car owners instead of house owners. Pro tip: 'given they own a house' means the denominator is the 60 house owners.",
        },
        {
            "text": (r"In how many ways can \(4\) books be arranged on a shelf, chosen from \(6\) distinct books (order matters)?"),
            "difficulty": 3,
            "choices": [(r"\(360\)", True), (r"\(15\)", False), (r"\(24\)", False), (r"\(1296\)", False)],
            "explanation": r"Permutations: \(6 \times 5 \times 4 \times 3 = 360\). The trap 15 is the combination \({}_6C_2\); 1296 is \(6^4\) (with repetition). Pro tip: when order matters and there's no repeating, multiply the shrinking counts \(6\cdot 5\cdot 4\cdot 3\).",
        },
        {
            "text": (r"For two events, \(P(A) = 0.5\), \(P(B) = 0.4\), and \(P(A \text{ and } B) = 0.2\). What is \(P(A \text{ or } B)\)?"),
            "difficulty": 3,
            "choices": [(r"\(0.7\)", True), (r"\(0.9\)", False), (r"\(0.2\)", False), (r"\(0.5\)", False)],
            "explanation": r"Addition rule: \(P(A \text{ or } B) = 0.5 + 0.4 - 0.2 = 0.7\). The trap 0.9 forgets to subtract the overlap. Pro tip: subtract \(P(A \text{ and } B)\) once, because it was counted in both \(P(A)\) and \(P(B)\).",
        },
        {
            "text": (r"What is the variance of the data set \(2,\ 4,\ 6\)?"),
            "difficulty": 3,
            "choices": [(r"\(\frac{8}{3}\)", True), (r"\(4\)", False), (r"\(2\)", False), (r"\(\frac{16}{3}\)", False)],
            "explanation": r"Mean \(= 4\). Squared deviations: \((2-4)^2 + (4-4)^2 + (6-4)^2 = 4 + 0 + 4 = 8\). Variance \(= \frac{8}{3} \approx 2.67\). The trap 4 forgets to divide by the 3 values. Pro tip: variance is the average of the squared distances from the mean.",
        },
        # ----- Geometry & measurement (elite) -----
        {
            "text": (r"A cylinder of radius \(4\) and height \(9\) has a cone of the same radius and height drilled out of it. What is the remaining volume? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 301.4\)", True), (r"\(\approx 150.7\)", False), (r"\(\approx 452.2\)", False), (r"\(\approx 201.0\)", False)],
            "explanation": r"Cylinder \(= \pi(16)(9) = 144\pi\); cone \(= \frac{1}{3}\pi(16)(9) = 48\pi\). Remaining \(= 144\pi - 48\pi = 96\pi \approx 301.4\). The trap 452.2 is the full cylinder. Pro tip: a cone is one-third of its cylinder, so drilling it out leaves two-thirds: \(\frac{2}{3}(144\pi) = 96\pi\).",
        },
        {
            "text": (r"What is the surface area of a sphere with radius \(6\)? Use \(\pi \approx 3.14\)."),
            "difficulty": 3,
            "choices": [(r"\(\approx 452.2\)", True), (r"\(\approx 904.3\)", False), (r"\(\approx 113.0\)", False), (r"\(\approx 150.7\)", False)],
            "explanation": r"Surface area \(= 4\pi r^2 = 4(3.14)(36) = 452.2\). The trap 904.3 doubles it; 113.0 uses \(\pi r^2\) (a flat circle). Pro tip: a sphere's surface area is \(4\pi r^2\) -- four times the area of its great circle.",
        },
        {
            "text": (r"A circle has a diameter with endpoints \((1,\ 2)\) and \((7,\ 10)\). What is the radius of the circle?"),
            "difficulty": 3,
            "choices": [(r"\(5\)", True), (r"\(10\)", False), (r"\(25\)", False), (r"\(2.5\)", False)],
            "explanation": r"The diameter length is \(\sqrt{(7-1)^2 + (10-2)^2} = \sqrt{36 + 64} = \sqrt{100} = 10\), so the radius is half: 5. The trap 10 reports the diameter. Pro tip: find the diameter with the distance formula, then halve it for the radius.",
        },
        {
            "text": (r"In a 30-60-90 right triangle, the hypotenuse is \(12\). What is the length of the shorter leg?"),
            "difficulty": 3,
            "choices": [(r"\(6\)", True), (r"\(6\sqrt{3}\)", False), (r"\(12\)", False), (r"\(4\sqrt{3}\)", False)],
            "explanation": r"In a 30-60-90 triangle the sides are \(x : x\sqrt3 : 2x\), and the hypotenuse is the \(2x\). So \(2x = 12\) gives \(x = 6\) for the shorter leg. The trap \(6\sqrt3\) is the longer leg. Pro tip: the shorter leg (opposite the 30 degree angle) is always half the hypotenuse.",
        },
        {
            "text": (r"What is the area of an equilateral triangle with a side length of \(6\)?"),
            "difficulty": 3,
            "choices": [(r"\(9\sqrt{3}\)", True), (r"\(18\)", False), (r"\(36\)", False), (r"\(15\)", False)],
            "explanation": r"Area \(= \frac{\sqrt3}{4}s^2 = \frac{\sqrt3}{4}(36) = 9\sqrt3 \approx 15.6\). The trap 18 uses \(\frac{1}{2}(6)(6)\) as if it were a right triangle. Pro tip: an equilateral triangle's area is \(\frac{\sqrt3}{4}\) times the side squared.",
        },
        {
            "text": (r"A swimming pool is \(10\) m by \(5\) m by \(2\) m deep. Water costs \$1.50 per cubic meter to fill it. What is the total cost?"),
            "difficulty": 3,
            "choices": [(r"\$150", True), (r"\$100", False), (r"\$25.50", False), (r"\$300", False)],
            "explanation": r"Volume \(= 10 \times 5 \times 2 = 100\ \text{m}^3\); cost \(= 100 \times 1.50 = \$150\). The trap \$300 doubles the volume. Pro tip: filling uses volume (cubic meters), so multiply all three dimensions, then by the price per cubic meter.",
        },
        {
            "text": (r"A triangle is inscribed in a circle so that one of its sides is a diameter. What is the measure of the angle opposite that diameter?"),
            "difficulty": 3,
            "choices": [(r"\(90^\circ\)", True), (r"\(180^\circ\)", False), (r"\(45^\circ\)", False), (r"\(60^\circ\)", False)],
            "explanation": r"By Thales' theorem, an inscribed angle that subtends a diameter is a right angle, \(90^\circ\). The trap 180 confuses the angle with the straight diameter. Pro tip: any triangle drawn with the diameter as one side and the third point on the circle is a right triangle.",
        },
        {
            "text": (r"Two similar pentagons have areas of \(50\) and \(200\). What is the ratio of their perimeters?"),
            "difficulty": 3,
            "choices": [(r"\(1:2\)", True), (r"\(1:4\)", False), (r"\(1:16\)", False), (r"\(2:1\)", False)],
            "explanation": r"The area ratio is \(50:200 = 1:4\). Perimeters scale by the square root of the area ratio: \(\sqrt{1:4} = 1:2\). The trap \(1:4\) uses the area ratio directly. Pro tip: areas scale by the square of the length ratio, so take the square root of an area ratio to compare lengths.",
        },
        {
            "text": (r"A cube has a total surface area of \(96\ \text{cm}^2\). What is its volume?"),
            "difficulty": 3,
            "choices": [(r"\(64\ \text{cm}^3\)", True), (r"\(96\ \text{cm}^3\)", False), (r"\(16\ \text{cm}^3\)", False), (r"\(512\ \text{cm}^3\)", False)],
            "explanation": r"Surface area \(= 6s^2 = 96\), so \(s^2 = 16\) and \(s = 4\). Volume \(= 4^3 = 64\ \text{cm}^3\). The trap 16 reports \(s^2\). Pro tip: work back from the surface area to the side length, then cube it for the volume.",
        },
        # ----- Coordinate geometry -----
        {
            "text": (r"The point \((a,\ 3)\) is \(5\) units from the point \((1,\ -1)\). What is the positive value of \(a\)?"),
            "difficulty": 3,
            "choices": [(r"\(4\)", True), (r"\(2\)", False), (r"\(6\)", False), (r"\(3\)", False)],
            "explanation": r"Distance: \(\sqrt{(a-1)^2 + (3-(-1))^2} = 5\), so \((a-1)^2 + 16 = 25\), giving \((a-1)^2 = 9\) and \(a - 1 = \pm 3\). The positive value is \(a = 4\). The trap 6 adds without taking the square root step. Pro tip: square the distance, isolate the squared term, then take both roots and pick the one asked.",
        },
        {
            "text": (r"Where do the lines \(y = 2x - 1\) and \(y = -x + 8\) intersect?"),
            "difficulty": 3,
            "choices": [(r"\((3,\ 5)\)", True), (r"\((5,\ 3)\)", False), (r"\((2,\ 3)\)", False), (r"\((3,\ 2)\)", False)],
            "explanation": r"Set them equal: \(2x - 1 = -x + 8\), so \(3x = 9\), \(x = 3\), and \(y = 2(3) - 1 = 5\). The trap \((5,3)\) swaps the coordinates. Pro tip: intersection means equal \(y\)-values -- set the two expressions equal and solve for \(x\) first.",
        },
        # ----- Algebra: expressions -----
        {
            "text": (r"Simplify: \(\dfrac{x^2 - x - 6}{x^2 - 4} \cdot \dfrac{x + 2}{x - 3}\)."),
            "difficulty": 3,
            "choices": [(r"\(\dfrac{x + 2}{x - 2}\)", True), (r"\(\dfrac{x - 3}{x - 2}\)", False), (r"\(1\)", False), (r"\(\dfrac{x + 2}{x - 3}\)", False)],
            "explanation": r"Factor: \(\frac{(x-3)(x+2)}{(x-2)(x+2)} \cdot \frac{x+2}{x-3}\). Cancel \((x-3)\) and one \((x+2)\), leaving \(\frac{x+2}{x-2}\). The trap 1 cancels too much. Pro tip: factor every part fully, then cancel matching factors across the multiplication.",
        },
        {
            "text": (r"Simplify: \((2x - 1)(x + 3) - (x - 2)^2\)."),
            "difficulty": 3,
            "choices": [(r"\(x^2 + 9x - 7\)", True), (r"\(x^2 + x - 7\)", False), (r"\(3x^2 + x + 1\)", False), (r"\(x^2 + 9x + 1\)", False)],
            "explanation": r"Expand: \((2x^2 + 5x - 3) - (x^2 - 4x + 4) = x^2 + 9x - 7\). The trap \(x^2 + 9x + 1\) mishandles the constant \(-3 - 4\). Pro tip: distribute the minus sign across all three terms of \((x-2)^2\) before combining.",
        },
        {
            "text": (r"Simplify: \(\dfrac{x^{1/2} \cdot x^{3/2}}{x}\)."),
            "difficulty": 3,
            "choices": [(r"\(x\)", True), (r"\(x^2\)", False), (r"\(x^{1/2}\)", False), (r"\(x^3\)", False)],
            "explanation": r"Top: \(x^{1/2 + 3/2} = x^2\). Divide by \(x\): \(x^{2-1} = x\). The trap \(x^2\) forgets to divide by the \(x\). Pro tip: add the fractional exponents first \(\left(\frac12 + \frac32 = 2\right)\), then subtract for the division.",
        },
        # ----- Algebra: equations -----
        {
            "text": (r"A rectangle's length is \(3\) more than its width, and its area is \(40\). What is the width?"),
            "difficulty": 3,
            "choices": [(r"\(5\)", True), (r"\(8\)", False), (r"\(4\)", False), (r"\(10\)", False)],
            "explanation": r"Let width \(= w\): \(w(w + 3) = 40\), so \(w^2 + 3w - 40 = 0 = (w + 8)(w - 5)\). The positive solution is \(w = 5\). The trap 8 is the rejected negative root's size. Pro tip: set up the area as a quadratic, factor, and keep only the positive dimension.",
        },
        {
            "text": (r"Solve: \(3x^2 + 5x - 2 = 0\)."),
            "difficulty": 3,
            "choices": [(r"\(x = \tfrac{1}{3}\) or \(x = -2\)", True), (r"\(x = -\tfrac{1}{3}\) or \(x = 2\)", False), (r"\(x = \tfrac{1}{3}\) or \(x = 2\)", False), (r"\(x = 3\) or \(x = -2\)", False)],
            "explanation": r"Factor: \((3x - 1)(x + 2) = 0\). So \(3x - 1 = 0 \Rightarrow x = \frac{1}{3}\), and \(x + 2 = 0 \Rightarrow x = -2\). The trap flips both signs. Pro tip: check by expanding \((3x-1)(x+2) = 3x^2 + 5x - 2\).",
        },
        {
            "text": (r"Solve for \(x\): \(x + \dfrac{6}{x} = 5\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 2\) or \(x = 3\)", True), (r"\(x = -2\) or \(x = -3\)", False), (r"\(x = 1\) or \(x = 6\)", False), (r"\(x = 5\) or \(x = 1\)", False)],
            "explanation": r"Multiply through by \(x\): \(x^2 + 6 = 5x\), so \(x^2 - 5x + 6 = 0 = (x-2)(x-3)\), giving \(x = 2\) or \(x = 3\). The trap 1 or 6 multiplies to 6 but adds to 7. Pro tip: clear the fraction by multiplying by \(x\), then solve the resulting quadratic.",
        },
        {
            "text": (r"Solve for \(x\): \(2^{x+1} = 8^{x-1}\)."),
            "difficulty": 3,
            "choices": [(r"\(x = 2\)", True), (r"\(x = 1\)", False), (r"\(x = 4\)", False), (r"\(x = 0.5\)", False)],
            "explanation": r"Write 8 as \(2^3\): \(2^{x+1} = 2^{3(x-1)}\). Set exponents equal: \(x + 1 = 3x - 3\), so \(4 = 2x\) and \(x = 2\). The trap 1 mis-solves the linear step. Pro tip: rewrite both sides with the same base, then equate the exponents.",
        },
        {
            "text": (r"The sum of two numbers is \(24\) and their difference is \(6\). What is their product?"),
            "difficulty": 3,
            "choices": [(r"\(135\)", True), (r"\(144\)", False), (r"\(90\)", False), (r"\(18\)", False)],
            "explanation": r"Adding the equations: \(2x = 30\), so \(x = 15\); then the other number is 9. Product \(= 15 \times 9 = 135\). The trap 144 squares the average (12). Pro tip: solve the system for the two numbers first, then do exactly what's asked -- multiply them.",
        },
        # ----- Algebra: inequalities -----
        {
            "text": (r"Solve: \(x^2 - 4 \ge 0\)."),
            "difficulty": 3,
            "choices": [(r"\(x \le -2\) or \(x \ge 2\)", True), (r"\(-2 \le x \le 2\)", False), (r"\(x \ge 2\)", False), (r"\(x \le 2\)", False)],
            "explanation": r"Factor: \((x - 2)(x + 2) \ge 0\). A product is non-negative outside its roots, so \(x \le -2\) or \(x \ge 2\). The trap \(-2 \le x \le 2\) is the '\(\le 0\)' (between) case. Pro tip: for '\(\ge 0\),' the solution is outside the roots; for '\(\le 0\),' it's between them.",
        },
        {
            "text": (r"A part is acceptable if its weight \(w\) (in grams) satisfies \(|w - 50| \le 3\). What is the acceptable range of weights?"),
            "difficulty": 3,
            "choices": [(r"\(47 \le w \le 53\)", True), (r"\(53 \le w \le 56\)", False), (r"\(-3 \le w \le 3\)", False), (r"\(47 \le w \le 50\)", False)],
            "explanation": r"\(|w - 50| \le 3\) means \(-3 \le w - 50 \le 3\). Add 50 throughout: \(47 \le w \le 53\). The trap \(-3 \le w \le 3\) forgets to add 50 back. Pro tip: '\(\le\)' absolute value becomes a single 'between' inequality centered on the target value.",
        },
        # ----- Functions, decay, sequences -----
        {
            "text": (r"If \(f(x) = \dfrac{x - 4}{3}\), what is the inverse function \(f^{-1}(x)\)?"),
            "difficulty": 3,
            "choices": [(r"\(f^{-1}(x) = 3x + 4\)", True), (r"\(f^{-1}(x) = 3x - 4\)", False), (r"\(f^{-1}(x) = \dfrac{x + 4}{3}\)", False), (r"\(f^{-1}(x) = \dfrac{x - 4}{3}\)", False)],
            "explanation": r"Swap \(x\) and \(y\): \(x = \frac{y - 4}{3}\). Solve: \(3x = y - 4\), so \(y = 3x + 4\). The trap \(3x - 4\) forgets to move the \(-4\) correctly. Pro tip: to invert, swap \(x\) and \(y\), then undo each operation in reverse order.",
        },
        {
            "text": (r"A radioactive substance has a half-life of \(5\) years. Starting from \(80\) grams, how much remains after \(15\) years?"),
            "difficulty": 3,
            "choices": [(r"\(10\) grams", True), (r"\(20\) grams", False), (r"\(40\) grams", False), (r"\(5\) grams", False)],
            "explanation": r"\(15 \div 5 = 3\) half-lives, so multiply by \(\left(\frac{1}{2}\right)^3 = \frac{1}{8}\): \(80 \times \frac{1}{8} = 10\) grams. The trap 20 uses only 2 half-lives. Pro tip: count how many half-lives fit in the time, then halve that many times.",
        },
        {
            "text": (r"In the geometric sequence \(3,\ 6,\ 12,\ 24,\ \dots\), what is the \(8^{\text{th}}\) term?"),
            "difficulty": 3,
            "choices": [(r"\(384\)", True), (r"\(192\)", False), (r"\(768\)", False), (r"\(256\)", False)],
            "explanation": r"The common ratio is 2, so \(a_8 = a_1 r^{\,n-1} = 3 \cdot 2^{7} = 3 \cdot 128 = 384\). The trap 192 uses \(2^6\) (only 6 steps). Pro tip: a geometric term multiplies the first term by the ratio \((n-1)\) times -- here \(2^7\), not \(2^8\).",
        },
        {
            "text": (r"A parabola is given by \(y = (x - 2)^2 - 9\). What are its x-intercepts?"),
            "difficulty": 3,
            "choices": [(r"\(x = 5\) and \(x = -1\)", True), (r"\(x = 2\) and \(x = -9\)", False), (r"\(x = -5\) and \(x = 1\)", False), (r"\(x = 3\) and \(x = -3\)", False)],
            "explanation": r"Set \(y = 0\): \((x - 2)^2 = 9\), so \(x - 2 = \pm 3\), giving \(x = 5\) or \(x = -1\). The trap \((2, -9)\) reads off the vertex instead. Pro tip: for vertex form, isolate the squared term, take both square roots, and solve each case.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the elite (Level 5) full-length GED Mathematical Reasoning practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 5 no-calculator, Part 2: 41 calculator; elite level, all hardest)."
        ))
