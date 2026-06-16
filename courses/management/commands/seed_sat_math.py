"""
Seed data: 'SAT Math: Complete Course & Test Prep' -- the first course in the SAT
program, covering the full Digital SAT Math content in one place.

Covers the four SAT Math domains: Algebra (linear equations, systems,
inequalities), Problem-Solving & Data Analysis (ratios, percentages, statistics),
Advanced Math (functions, quadratics, exponents, exponential models), and
Geometry & Trigonometry -- plus a test-taking strategy lesson (backsolving and
plugging in numbers). Each lesson leads with intuition, reuses the math diagram
library, includes a common-trap warning, and a quick tip. Practice questions are
multiple choice with full worked solutions and pro tips.

Run:
    python manage.py seed_sat_math
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "SAT Math: Complete Course & Test Prep",
    "slug": "sat-math-complete-course",
    "program": "SAT",
    "subject": "math",
    "description": (
        "A complete review of Digital SAT Math in one course. It covers all four SAT Math "
        "domains: Algebra (linear equations, systems, and inequalities), Problem-Solving and Data "
        "Analysis (ratios, percentages, and statistics), Advanced Math (functions, quadratics, "
        "exponents, and exponential models), and Geometry and Trigonometry. You also get an SAT "
        "strategy lesson on backsolving and plugging in numbers. Every topic uses plain language, "
        "graphs and diagrams, and SAT-style multiple-choice practice with full worked solutions "
        "and pro tips."
    ),
    "lessons": [
        (
            "1. Linear Equations & Slope",
            r"Linear equations are the backbone of SAT Algebra, the largest math domain on the test. A **linear equation** graphs as a straight line and is usually written in **slope-intercept form**:" "\n"
            r"\[ y = mx + b, \]" "\n"
            r"where \(m\) is the **slope** (steepness) and \(b\) is the **y-intercept** (where the line crosses the y-axis)." "\n\n"
            r"[[figure:coord_line|Slope is rise over run; the y-intercept b is where the line meets the y-axis.]]" "\n\n"
            r"To **solve** a linear equation, undo the operations to isolate the variable. For \(3x + 7 = 22\): subtract 7 to get \(3x = 15\), then divide by 3 to get \(x = 5\)." "\n\n"
            r"Key facts the SAT tests:" "\n"
            r"- **Slope** between two points: \(m = \dfrac{y_2 - y_1}{x_2 - x_1}\) (rise over run)." "\n"
            r"- **Parallel** lines have the **same** slope; **perpendicular** lines have slopes that are **negative reciprocals** (like \(2\) and \(-\tfrac{1}{2}\))." "\n"
            r"- A positive slope rises left to right; a negative slope falls." "\n\n"
            r"⚠️ Common trap: in \(y = mx + b\), the slope is the number multiplied by \(x\), not the constant. In \(y = -2x + 5\), the slope is \(-2\) and the y-intercept is \(5\)." "\n\n"
            r"💡 Tip: whatever you do to one side of an equation, do to the other — that keeps it balanced.",
        ),
        (
            "2. Systems of Linear Equations",
            r"A **system** is two equations with two variables. The **solution** is the pair \((x, y)\) that makes **both** equations true — graphically, the point where the two lines **cross**." "\n\n"
            r"[[figure:system_graph|The solution of a system is the single point that lies on both lines.]]" "\n\n"
            r"Two algebra methods solve systems without graphing:" "\n"
            r"- **Substitution** — solve one equation for a variable, then plug it into the other. For \(y = x + 2\) and \(2x + y = 11\): replace \(y\) to get \(2x + (x+2) = 11\), so \(3x = 9\), \(x = 3\), and \(y = 5\)." "\n"
            r"- **Elimination** — add or subtract the equations to cancel a variable. For \(x + y = 10\) and \(x - y = 4\): adding gives \(2x = 14\), so \(x = 7\) and \(y = 3\)." "\n\n"
            r"**How many solutions?** Compare the lines:" "\n"
            r"- Lines cross once → **one** solution." "\n"
            r"- **Parallel** lines (same slope, different intercept) → **no** solution." "\n"
            r"- The **same** line (identical equations) → **infinitely many** solutions." "\n\n"
            r"⚠️ Common trap: two equations with the **same slope but different y-intercepts** never meet, so the system has **no** solution — even though both are valid lines." "\n\n"
            r"💡 Tip: if a variable already has a matching \(+\) and \(-\) coefficient (like \(+y\) and \(-y\)), elimination by adding is fastest.",
        ),
        (
            "3. Linear Inequalities & Absolute Value",
            r"An **inequality** uses \(<\), \(>\), \(\le\), or \(\ge\) instead of \(=\), and its solution is a **range** of values rather than a single number." "\n\n"
            r"[[figure:number_line_ineq|An inequality's solution is a whole region on the number line, not one point.]]" "\n\n"
            r"Solve inequalities just like equations, with **one crucial rule**:" "\n"
            r"- When you **multiply or divide both sides by a negative number, flip the inequality sign.**" "\n\n"
            r"For \(3x - 5 > 7\): add 5 to get \(3x > 12\), divide by 3 to get \(x > 4\). For \(-2x \le 6\): divide by \(-2\) **and flip** to get \(x \ge -3\)." "\n\n"
            r"**Absolute value** \(|x|\) is the distance from zero, so it is never negative. An equation like \(|x - 2| = 5\) has **two** answers: \(x - 2 = 5\) gives \(x = 7\), and \(x - 2 = -5\) gives \(x = -3\)." "\n\n"
            r"⚠️ Common trap: forgetting to flip the sign when dividing by a negative. \(-2x \le 6\) becomes \(x \ge -3\), not \(x \le -3\)." "\n\n"
            r"💡 Tip: absolute-value equations usually have two solutions — set the inside equal to both the positive and the negative value.",
        ),
        (
            "4. Ratios, Proportions & Percentages",
            r"This is the heart of SAT **Problem-Solving and Data Analysis**. A **ratio** compares quantities; a **proportion** sets two ratios equal. Solve proportions by **cross-multiplying**: \(\dfrac{3}{4} = \dfrac{x}{20}\) gives \(4x = 60\), so \(x = 15\)." "\n\n"
            r"[[figure:percent_equation_triangle|Cover the quantity you want to find to see whether to multiply or divide.]]" "\n\n"
            r"**Percent** means 'out of 100'. The core relationship is:" "\n"
            r"\[ \text{part} = \text{percent} \times \text{whole}. \]" "\n"
            r"- 'What percent of 120 is 30?' → \(30 \div 120 = 0.25 = 25\%\)." "\n"
            r"- 'Find 15% of 80' → \(0.15 \times 80 = 12\)." "\n"
            r"- **Percent increase/decrease:** a 25%-off \$40 shirt costs \(40 - 0.25(40) = \$30\); raising 80 by 15% gives \(80 \times 1.15 = 92\)." "\n\n"
            r"A **unit rate** is the amount per one unit: 150 miles in 3 hours is \(150 \div 3 = 50\) miles per hour." "\n\n"
            r"⚠️ Common trap: for a percent **change**, divide by the **original** amount, not the new one. And a 20% raise followed by a 20% cut does **not** return to the start." "\n\n"
            r"💡 Tip: turn a percent into a decimal (move the point two places left) and multiply — fast and calculator-friendly.",
        ),
        (
            "5. Data Analysis & Statistics",
            r"The SAT asks you to read graphs and tables and to summarize data with a few key statistics." "\n\n"
            r"[[figure:scatter_trend|A line of best fit summarizes the trend; an upward line means a positive association.]]" "\n\n"
            r"The center of a data set:" "\n"
            r"- **Mean** (average) — add all values, divide by how many. For 4, 8, 10, 10, 8: \(40 \div 5 = 8\)." "\n"
            r"- **Median** — the middle value when the data is in order. For 3, 7, 9, 12, 20, the median is 9." "\n"
            r"- **Mode** — the value that appears most often (10 above)." "\n"
            r"- **Range** — the highest value minus the lowest." "\n\n"
            r"On a **scatterplot**, the **line of best fit** shows the overall trend. An upward line is a **positive** association; a downward line is **negative**. You can use the line to **predict** values." "\n\n"
            r"⚠️ Common trap: an **outlier** (one extreme value) pulls the **mean** far more than the **median**. When data is skewed, the median better represents a 'typical' value." "\n\n"
            r"💡 Tip: always put the numbers in order before finding the median, and remember correlation is not causation.",
        ),
        (
            "6. Functions & Quadratics",
            r"A **function** is a rule that gives exactly one output for each input. **Function notation** \(f(x)\) just means 'the output for input \(x\)'. To **evaluate**, substitute: if \(f(x) = 2x + 3\), then \(f(4) = 2(4) + 3 = 11\)." "\n\n"
            r"A **quadratic** has an \(x^2\) term and graphs as a **parabola** (a U-shaped curve)." "\n\n"
            r"[[figure:parabola|A parabola's x-intercepts are the solutions (roots); the vertex is its highest or lowest point.]]" "\n\n"
            r"Key quadratic skills:" "\n"
            r"- **Solve by factoring:** \(x^2 - 5x + 6 = 0\) factors to \((x-2)(x-3) = 0\), so \(x = 2\) or \(x = 3\)." "\n"
            r"- The **roots** (x-intercepts) are where \(y = 0\); the **vertex** is the turning point (minimum if the parabola opens up, maximum if it opens down)." "\n"
            r"- The **quadratic formula** \(x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}\) solves any \(ax^2 + bx + c = 0\)." "\n\n"
            r"⚠️ Common trap: \(f(x)\) is not 'f times x' — it is the value of the function at \(x\). To find \(f(-3)\) for \(f(x)=x^2+1\), square \(-3\) first: \(9 + 1 = 10\)." "\n\n"
            r"💡 Tip: a quadratic can have 2, 1, or 0 real solutions — that is how many times its parabola crosses the x-axis.",
        ),
        (
            "7. Exponents, Radicals & Exponential Models",
            r"**Exponents** are repeated multiplication. The rules the SAT uses most:" "\n"
            r"- **Multiply** like bases: add exponents — \(2^3 \cdot 2^4 = 2^{7} = 128\)." "\n"
            r"- **Divide** like bases: subtract exponents — \(\dfrac{x^5}{x^2} = x^{3}\)." "\n"
            r"- **Power of a power:** multiply — \((x^3)^2 = x^{6}\)." "\n"
            r"- **Zero power:** anything (nonzero) to the 0 is \(1\)." "\n"
            r"- **Negative exponent:** \(x^{-2} = \dfrac{1}{x^2}\)." "\n\n"
            r"A **radical** (root) undoes a power: \(\sqrt{64} = 8\) because \(8^2 = 64\). A square root is the same as a \(\tfrac{1}{2}\) power." "\n\n"
            r"[[figure:exponential_growth|In exponential growth the quantity multiplies by a fixed factor each step, so it climbs faster and faster.]]" "\n\n"
            r"**Exponential models** grow or shrink by a constant **factor**: \(y = a \cdot b^{x}\). If \(b > 1\) it is **growth** (a population that doubles: \(100 \cdot 2^{x}\)); if \(0 < b < 1\) it is **decay**. At \(x = 3\), \(100 \cdot 2^3 = 100 \cdot 8 = 800\)." "\n\n"
            r"⚠️ Common trap: exponential growth (multiplying each step) far outpaces linear growth (adding each step). Don't treat \(2^x\) like \(2x\)." "\n\n"
            r"💡 Tip: in \(y = a \cdot b^x\), \(a\) is the starting amount and \(b\) is the growth factor (\(1 + r\) for a rate \(r\)).",
        ),
        (
            "8. Geometry & Trigonometry",
            r"Geometry and Trigonometry is a smaller SAT domain, but a few formulas cover most of it." "\n\n"
            r"[[figure:pythagorean_triangle|In a right triangle, the squares of the two legs add up to the square of the hypotenuse.]]" "\n\n"
            r"Essential facts:" "\n"
            r"- **Pythagorean theorem:** \(a^2 + b^2 = c^2\). Legs 6 and 8 give a hypotenuse \(\sqrt{36+64} = \sqrt{100} = 10\). Memorize the 3-4-5 and 5-12-13 triples." "\n"
            r"- **Area of a circle** \(= \pi r^2\); **circumference** \(= 2\pi r\). A circle with \(r = 5\) has area \(\pi(25) \approx 78.5\)." "\n"
            r"- **Triangle angles** sum to \(180^\circ\); a full circle is \(360^\circ\)." "\n"
            r"- **Special right triangles:** 45-45-90 has sides \(x, x, x\sqrt2\); 30-60-90 has sides \(x, x\sqrt3, 2x\)." "\n\n"
            r"**Basic trig** uses **SOH-CAH-TOA** for right triangles: \(\sin = \tfrac{\text{opp}}{\text{hyp}}\), \(\cos = \tfrac{\text{adj}}{\text{hyp}}\), \(\tan = \tfrac{\text{opp}}{\text{adj}}\). If the side opposite an angle is 3 and the hypotenuse is 5, then \(\sin = \tfrac{3}{5}\)." "\n\n"
            r"⚠️ Common trap: the Pythagorean theorem works **only** for right triangles, and \(c\) must be the hypotenuse (the side opposite the right angle)." "\n\n"
            r"💡 Tip: label the triangle's sides relative to the angle (opposite, adjacent, hypotenuse) before choosing sin, cos, or tan.",
        ),
        (
            "9. SAT Math Strategy: Backsolve & Plug In",
            r"On the SAT, the fastest route to a right answer is not always algebra. Because the math is **multiple choice**, two strategies turn hard problems into easy arithmetic." "\n\n"
            r"**Backsolving (plug in the answers).** When a question asks for a specific value (\"what is \(x\)?\") and the choices are numbers, just **test the choices** in the original problem — start with the middle value. The one that works is the answer, and you never have to set up the algebra." "\n\n"
            r"**Plugging in numbers.** When the question and answers contain **variables** (\"which expression is equivalent...\"), pick an easy number for the variable (like \(x = 2\)), compute the target, then see which answer choice matches. Avoid 0 and 1, which can make several choices look equal." "\n\n"
            r"Other test-day habits:" "\n"
            r"- **Use the calculator wisely** — it is allowed on the whole Digital SAT, but setting up the problem still matters more than button-pushing." "\n"
            r"- **Read the last line** of the question: it may ask for \(x + 1\), not \(x\)." "\n"
            r"- **Estimate** to eliminate answers that are obviously too big or too small." "\n\n"
            r"⚠️ Common trap: solving for \(x\) correctly but forgetting the question asked for something else (like \(2x\) or \(x - 3\)). Always re-read what is wanted." "\n\n"
            r"💡 Tip: if you are stuck for more than a few seconds and the choices are numbers, backsolve instead of staring at the algebra.",
        ),
    ],
    "mcqs": [
        # --- Linear equations & slope ---
        {
            "text": r"Solve for \(x\): \(3x + 7 = 22\).",
            "difficulty": 1,
            "choices": [(r"\(x = 5\)", True), (r"\(x = 9\)", False), (r"\(x = \tfrac{29}{3}\)", False), (r"\(x = 15\)", False)],
            "explanation": r"Subtract 7: \(3x = 15\). Divide by 3: \(x = 5\). The trap 15 stops after subtracting and forgets to divide. Pro tip: undo \(+7\) first, then undo the \(\times 3\).",
        },
        {
            "text": r"What is the slope of the line through \((1, 2)\) and \((3, 8)\)?",
            "difficulty": 2,
            "choices": [(r"\(3\)", True), (r"\(\tfrac{1}{3}\)", False), (r"\(2\)", False), (r"\(6\)", False)],
            "explanation": r"Slope is rise over run: \(\dfrac{8-2}{3-1} = \dfrac{6}{2} = 3\). The trap \(\tfrac{1}{3}\) flips the formula; 6 forgets to divide by the run. Pro tip: keep the same point first on top and bottom.",
        },
        {
            "text": r"A line is written \(y = -2x + 5\). What is its y-intercept?",
            "difficulty": 1,
            "choices": [(r"\(5\)", True), (r"\(-2\)", False), (r"\(2\)", False), (r"\(-5\)", False)],
            "explanation": r"In \(y = mx + b\), the y-intercept is \(b = 5\); the slope is \(m = -2\). The trap \(-2\) gives the slope instead. Pro tip: the y-intercept is the constant with no \(x\) attached.",
        },
        {
            "text": r"A line is perpendicular to a line with slope \(2\). What is its slope?",
            "difficulty": 3,
            "choices": [(r"\(-\tfrac{1}{2}\)", True), (r"\(2\)", False), (r"\(\tfrac{1}{2}\)", False), (r"\(-2\)", False)],
            "explanation": r"Perpendicular slopes are negative reciprocals: flip \(2\) to \(\tfrac{1}{2}\) and negate to \(-\tfrac{1}{2}\). The trap \(2\) is a parallel slope; \(-2\) only negates. Pro tip: negative reciprocal = flip AND change the sign.",
        },
        # --- Systems ---
        {
            "text": r"Solve the system \(x + y = 10\) and \(x - y = 4\). What is \(x\)?",
            "difficulty": 2,
            "choices": [(r"\(7\)", True), (r"\(3\)", False), (r"\(6\)", False), (r"\(14\)", False)],
            "explanation": r"Add the equations to eliminate \(y\): \(2x = 14\), so \(x = 7\) (and \(y = 3\)). The trap 3 is the value of \(y\); 14 forgets to divide by 2. Pro tip: matching \(+y\) and \(-y\) means adding cancels \(y\) instantly.",
        },
        {
            "text": r"Using substitution with \(y = x + 2\) and \(2x + y = 11\), what is \(y\)?",
            "difficulty": 2,
            "choices": [(r"\(5\)", True), (r"\(3\)", False), (r"\(11\)", False), (r"\(9\)", False)],
            "explanation": r"Substitute: \(2x + (x+2) = 11 \Rightarrow 3x = 9 \Rightarrow x = 3\), so \(y = 3 + 2 = 5\). The trap 3 stops at \(x\). Pro tip: after finding one variable, plug back in to get the other.",
        },
        {
            "text": r"How many solutions does the system \(y = 2x + 1\) and \(y = 2x - 3\) have?",
            "difficulty": 3,
            "choices": [("No solution", True), ("Exactly one", False), ("Infinitely many", False), ("Exactly two", False)],
            "explanation": r"Both lines have slope 2 but different y-intercepts, so they are parallel and never cross — no solution. The trap 'one' assumes lines always meet. Pro tip: same slope + different intercept = parallel = no solution.",
        },
        # --- Inequalities & absolute value ---
        {
            "text": r"Solve the inequality \(3x - 5 > 7\).",
            "difficulty": 1,
            "choices": [(r"\(x > 4\)", True), (r"\(x < 4\)", False), (r"\(x > \tfrac{2}{3}\)", False), (r"\(x > 12\)", False)],
            "explanation": r"Add 5: \(3x > 12\). Divide by 3: \(x > 4\). The sign does not flip because 3 is positive. The trap 12 forgets to divide. Pro tip: only flip the sign when dividing by a NEGATIVE.",
        },
        {
            "text": r"Solve \(-2x \le 6\).",
            "difficulty": 2,
            "choices": [(r"\(x \ge -3\)", True), (r"\(x \le -3\)", False), (r"\(x \ge 3\)", False), (r"\(x \le 3\)", False)],
            "explanation": r"Divide both sides by \(-2\) and FLIP the sign: \(x \ge -3\). The trap \(x \le -3\) forgets to flip. Pro tip: dividing or multiplying by a negative reverses the inequality.",
        },
        {
            "text": r"Which values satisfy \(|x - 2| = 5\)?",
            "difficulty": 2,
            "choices": [(r"\(x = 7\) or \(x = -3\)", True), (r"\(x = 7\) only", False), (r"\(x = 3\) or \(x = -7\)", False), (r"\(x = 5\) or \(x = -5\)", False)],
            "explanation": r"Set the inside to \(+5\) and \(-5\): \(x - 2 = 5 \Rightarrow x = 7\); \(x - 2 = -5 \Rightarrow x = -3\). The trap '7 only' misses the negative case. Pro tip: absolute-value equations usually give two answers.",
        },
        # --- Ratios, proportions & percentages ---
        {
            "text": r"\(30\) is what percent of \(120\)?",
            "difficulty": 1,
            "choices": [(r"\(25\%\)", True), (r"\(40\%\)", False), (r"\(4\%\)", False), (r"\(90\%\)", False)],
            "explanation": r"Divide the part by the whole: \(30 \div 120 = 0.25 = 25\%\). The trap 40% divides the wrong way (\(120/30 = 4\)). Pro tip: 'what percent of the whole' means part ÷ whole.",
        },
        {
            "text": r"Solve the proportion \(\dfrac{3}{4} = \dfrac{x}{20}\).",
            "difficulty": 1,
            "choices": [(r"\(x = 15\)", True), (r"\(x = 12\)", False), (r"\(x = 60\)", False), (r"\(x = 5\)", False)],
            "explanation": r"Cross-multiply: \(4x = 3 \times 20 = 60\), so \(x = 15\). The trap 60 stops before dividing by 4. Pro tip: cross-multiply, then divide by the leftover number.",
        },
        {
            "text": r"A \$40 shirt is marked 25% off. What is the sale price?",
            "difficulty": 2,
            "choices": [(r"\$30", True), (r"\$15", False), (r"\$10", False), (r"\$35", False)],
            "explanation": r"The discount is \(0.25 \times 40 = \$10\), so the price is \(40 - 10 = \$30\). The trap \$10 gives only the discount; \$15 over-subtracts. Pro tip: 25% off means you pay 75%: \(0.75 \times 40 = 30\).",
        },
        {
            "text": r"A car travels \(150\) miles in \(3\) hours. What is its average speed?",
            "difficulty": 1,
            "choices": [("50 miles per hour", True), ("450 miles per hour", False),
                        ("47 miles per hour", False), ("153 miles per hour", False)],
            "explanation": r"Rate is distance ÷ time: \(150 \div 3 = 50\) mph. The trap 450 multiplies instead of divides. Pro tip: 'per hour' tells you to divide the miles by the hours.",
        },
        # --- Data analysis & statistics ---
        {
            "text": r"What is the mean (average) of \(4, 8, 10, 10, 8\)?",
            "difficulty": 1,
            "choices": [(r"\(8\)", True), (r"\(10\)", False), (r"\(40\)", False), (r"\(9\)", False)],
            "explanation": r"Add them: \(4+8+10+10+8 = 40\); divide by 5: \(40 \div 5 = 8\). The trap 40 forgets to divide; 10 is the mode. Pro tip: mean = total ÷ how many values.",
        },
        {
            "text": r"What is the median of \(3, 7, 9, 12, 20\)?",
            "difficulty": 2,
            "choices": [(r"\(9\)", True), (r"\(12\)", False), (r"\(10.2\)", False), (r"\(17\)", False)],
            "explanation": r"The data is already in order, so the median is the middle value: 9. The trap 10.2 is the mean; 17 is the range. Pro tip: median = the middle number once the list is sorted.",
        },
        {
            "text": r"A scatterplot's line of best fit slopes upward from left to right. This shows:",
            "difficulty": 2,
            "choices": [("A positive association", True), ("A negative association", False),
                        ("No association", False), ("That one variable causes the other", False)],
            "explanation": r"An upward line means that as one variable increases, so does the other — a positive association. The trap 'causes' confuses correlation with causation. Pro tip: up = positive, down = negative; a trend is not proof of cause.",
        },
        {
            "text": r"Adding one very large outlier to a data set affects which measure the most?",
            "difficulty": 3,
            "choices": [("The mean", True), ("The median", False), ("The mode", False), ("None of them change", False)],
            "explanation": r"The mean uses every value, so an extreme value pulls it strongly; the median (middle position) barely moves. Pro tip: with outliers or skew, the median is the more 'typical' center.",
        },
        # --- Functions & quadratics ---
        {
            "text": r"If \(f(x) = 2x + 3\), what is \(f(4)\)?",
            "difficulty": 1,
            "choices": [(r"\(11\)", True), (r"\(9\)", False), (r"\(24\)", False), (r"\(14\)", False)],
            "explanation": r"Substitute 4 for \(x\): \(2(4) + 3 = 8 + 3 = 11\). The trap 24 multiplies \(f\) by \(x\); 9 forgets the \(+3\) on \(2\cdot 4\). Pro tip: \(f(4)\) means 'plug in 4', not 'f times 4'.",
        },
        {
            "text": r"Solve \(x^2 - 5x + 6 = 0\).",
            "difficulty": 2,
            "choices": [(r"\(x = 2\) or \(x = 3\)", True), (r"\(x = -2\) or \(x = -3\)", False),
                        (r"\(x = 1\) or \(x = 6\)", False), (r"\(x = 5\) or \(x = 6\)", False)],
            "explanation": r"Factor into \((x-2)(x-3) = 0\), so \(x = 2\) or \(x = 3\) (they multiply to \(+6\) and add to \(-5\)). The trap with negatives flips the signs. Pro tip: find two numbers that multiply to \(c\) and add to \(b\).",
        },
        {
            "text": r"If \(f(x) = x^2 + 1\), what is \(f(-3)\)?",
            "difficulty": 2,
            "choices": [(r"\(10\)", True), (r"\(-8\)", False), (r"\(7\)", False), (r"\(-5\)", False)],
            "explanation": r"Square first: \((-3)^2 = 9\), then \(9 + 1 = 10\). The trap \(-8\) wrongly computes \(-(3^2)+1\); a negative squared is positive. Pro tip: square the entire value, including its sign.",
        },
        {
            "text": r"The graph of \(y = x^2 - 4\) crosses the x-axis at which points?",
            "difficulty": 2,
            "choices": [(r"\(x = -2\) and \(x = 2\)", True), (r"\(x = -4\) and \(x = 4\)", False),
                        (r"\(x = 0\) only", False), (r"\(x = 4\) only", False)],
            "explanation": r"Set \(y = 0\): \(x^2 - 4 = 0 \Rightarrow x^2 = 4 \Rightarrow x = \pm 2\). The trap \(\pm 4\) forgets the square root. Pro tip: x-intercepts are where \(y = 0\); take the square root and keep both signs.",
        },
        # --- Exponents, radicals & exponential ---
        {
            "text": r"Simplify \(2^3 \cdot 2^4\).",
            "difficulty": 1,
            "choices": [(r"\(128\)", True), (r"\(64\)", False), (r"\(2^{12}\)", False), (r"\(16\)", False)],
            "explanation": r"Same base, so add exponents: \(2^{3+4} = 2^7 = 128\). The trap \(2^{12}\) multiplies the exponents; 64 is \(2^6\). Pro tip: multiplying like bases means ADD the exponents.",
        },
        {
            "text": r"Simplify \((x^3)^2\).",
            "difficulty": 2,
            "choices": [(r"\(x^6\)", True), (r"\(x^5\)", False), (r"\(x^9\)", False), (r"\(x^8\)", False)],
            "explanation": r"A power of a power multiplies exponents: \(x^{3 \times 2} = x^6\). The trap \(x^5\) adds them. Pro tip: power-of-a-power = multiply; multiplying like bases = add.",
        },
        {
            "text": r"What is \(\sqrt{64}\)?",
            "difficulty": 1,
            "choices": [(r"\(8\)", True), (r"\(32\)", False), (r"\(16\)", False), (r"\(6.4\)", False)],
            "explanation": r"\(\sqrt{64} = 8\) because \(8^2 = 64\). The trap 32 halves 64; a square root is not half. Pro tip: ask 'what number times itself gives 64?'",
        },
        {
            "text": r"A population is modeled by \(P = 100 \cdot 2^{t}\), where \(t\) is in years. What is the population at \(t = 3\)?",
            "difficulty": 3,
            "choices": [(r"\(800\)", True), (r"\(600\)", False), (r"\(106\)", False), (r"\(200\)", False)],
            "explanation": r"\(P = 100 \cdot 2^3 = 100 \cdot 8 = 800\). The trap 600 treats \(2^3\) as \(2 \times 3 = 6\). Pro tip: exponential growth multiplies — \(2^3\) is \(2\times2\times2 = 8\), not \(2 \times 3\).",
        },
        # --- Geometry & trigonometry ---
        {
            "text": r"A right triangle has legs \(6\) and \(8\). What is the length of the hypotenuse?",
            "difficulty": 1,
            "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(48\)", False), (r"\(100\)", False)],
            "explanation": r"\(c = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). The trap 14 adds the legs; 100 forgets the square root. Pro tip: 6-8-10 is the 3-4-5 triple doubled.",
        },
        {
            "text": r"What is the area of a circle with radius \(5\)? (Use \(\pi \approx 3.14\).)",
            "difficulty": 2,
            "choices": [(r"\(78.5\)", True), (r"\(31.4\)", False), (r"\(25\)", False), (r"\(15.7\)", False)],
            "explanation": r"\(A = \pi r^2 = 3.14 \times 5^2 = 3.14 \times 25 = 78.5\). The trap 31.4 is the circumference (\(2\pi r\)); 25 forgets \(\pi\). Pro tip: area squares the radius first, then multiplies by \(\pi\).",
        },
        {
            "text": r"In a right triangle, the side opposite angle \(A\) is \(3\) and the hypotenuse is \(5\). What is \(\sin A\)?",
            "difficulty": 2,
            "choices": [(r"\(\tfrac{3}{5}\)", True), (r"\(\tfrac{5}{3}\)", False), (r"\(\tfrac{4}{5}\)", False), (r"\(\tfrac{3}{4}\)", False)],
            "explanation": r"SOH: \(\sin = \dfrac{\text{opposite}}{\text{hypotenuse}} = \dfrac{3}{5}\). The trap \(\tfrac{4}{5}\) is \(\cos A\) (adjacent/hyp); \(\tfrac{5}{3}\) flips the ratio. Pro tip: SOH-CAH-TOA — sine is opposite over hypotenuse.",
        },
        {
            "text": r"Two angles of a triangle measure \(50^\circ\) and \(60^\circ\). What is the third angle?",
            "difficulty": 1,
            "choices": [(r"\(70^\circ\)", True), (r"\(110^\circ\)", False), (r"\(80^\circ\)", False), (r"\(250^\circ\)", False)],
            "explanation": r"The angles total \(180^\circ\): \(180 - 50 - 60 = 70^\circ\). The trap 110 just adds the two given angles. Pro tip: subtract the two known angles from 180.",
        },
        # --- Strategy ---
        {
            "text": r"A question asks for the value of \(x\) and the four answer choices are numbers. The fastest reliable strategy is often to:",
            "difficulty": 2,
            "choices": [("Backsolve — test the answer choices in the original equation", True),
                        ("Always set up and solve the full algebra", False),
                        ("Pick the largest choice", False),
                        ("Skip the question", False)],
            "explanation": r"With numerical choices, plugging them in (starting from the middle value) finds the answer without setting up algebra. Pro tip: backsolving turns 'solve for x' into quick checking.",
        },
        {
            "text": r"A problem and all its answer choices contain the variable \(x\) (\"which expression is equivalent?\"). A good strategy is to:",
            "difficulty": 2,
            "choices": [("Pick a simple number for \(x\), then compare results", True),
                        ("Use \(x = 0\) or \(x = 1\) for guaranteed accuracy", False),
                        ("Add all the answer choices together", False),
                        ("Choose the longest expression", False)],
            "explanation": r"Plugging in an easy value (avoiding 0 and 1, which can make several choices match) lets you test each expression with arithmetic. Pro tip: 0 and 1 are 'tricky' numbers — choose something like 2.",
        },
        {
            "text": r"You correctly solve and find \(x = 4\), but the question asks for \(x + 3\). The answer is:",
            "difficulty": 1,
            "choices": [(r"\(7\)", True), (r"\(4\)", False), (r"\(12\)", False), (r"\(1\)", False)],
            "explanation": r"The question wants \(x + 3 = 4 + 3 = 7\), not \(x\). The trap 4 answers the wrong question. Pro tip: re-read the final line — the SAT often asks for an expression of \(x\), not \(x\) itself.",
        },
        # --- Data analysis from a graph (charts now render inside questions) ---
        {
            "text": ("Use the scatterplot.\n\n"
                     "[[figure:scatter_trend|A scatterplot with a line of best fit]]\n\n"
                     "The line of best fit indicates that x and y have:"),
            "difficulty": 2,
            "choices": [("A positive association", True), ("A negative association", False),
                        ("No association", False), ("A guaranteed causal link", False)],
            "explanation": r"The line of best fit rises from left to right, so larger x goes with larger y — a positive association. Note that an association is not proof of causation. Pro tip: line up = positive, line down = negative.",
        },
        {
            "text": ("Use the function machine.\n\n"
                     "[[figure:function_machine|A machine whose rule is: multiply by 2, then add 3]]\n\n"
                     "Based on the rule shown, what is the output when the input is \\(x = 5\\)?"),
            "difficulty": 2,
            "choices": [(r"\(13\)", True), (r"\(10\)", False), (r"\(16\)", False), (r"\(25\)", False)],
            "explanation": r"Apply the rule in order: multiply by 2 (\(5 \times 2 = 10\)), then add 3 (\(10 + 3 = 13\)). The trap 10 stops before adding 3. Pro tip: follow the steps in the order the machine lists them.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'SAT Math: Complete Course & Test Prep' course (MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent
        course = Course.objects.create(
            title=COURSE["title"],
            slug=COURSE["slug"],
            program=COURSE["program"],
            subject=COURSE["subject"],
            description=COURSE["description"],
        )
        for i, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=i)

        for q in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course, qtype="mcq", text=q["text"],
                difficulty=q["difficulty"], explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
