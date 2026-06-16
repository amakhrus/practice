"""
Seed data: 'GED Math: Algebra In Depth' -- a comprehensive, GED-focused algebra
course that builds from the meaning of a variable all the way to quadratics and
functions. Each lesson is deliberately detailed: intuition first, then rules,
multiple fully worked examples, a common-mistake warning, and a quick tip.
Inline charts illustrate inequalities, graphing, and parabolas.

Run:
    python manage.py seed_ged_algebra
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Math: Algebra In Depth",
    "slug": "ged-algebra-in-depth",
    "program": "GED",
    "subject": "math",
    "description": (
        "A complete, step-by-step algebra course for the GED. We start from the very "
        "meaning of a variable and build carefully through expressions, equations, "
        "inequalities, graphing, systems, exponents, polynomials, factoring, quadratics, "
        "and functions. Every idea is explained in plain language with multiple worked "
        "examples, common-mistake warnings, and visual graphs."
    ),
    "lessons": [
        (
            "1. The Language of Algebra",
            r"Algebra is just arithmetic with a placeholder. A **variable** (usually a letter like \(x\)) is a box that holds a number we don't know yet." "\n\n"
            r"Key vocabulary, using the expression \(3x + 5\):" "\n"
            r"- **Term** — a piece separated by + or −. Here the terms are \(3x\) and \(5\)." "\n"
            r"- **Coefficient** — the number multiplying a variable. The coefficient of \(x\) is \(3\)." "\n"
            r"- **Constant** — a plain number with no variable, like \(5\)." "\n"
            r"- **Expression** — a combination of terms with no equals sign, like \(3x + 5\)." "\n"
            r"- **Equation** — two expressions set equal, like \(3x + 5 = 11\)." "\n\n"
            r"**Translating words into algebra** is half the battle on the GED. Watch the keywords:" "\n"
            r"- 'sum / more than / increased by' → add. 'Five more than a number' is \(x + 5\)." "\n"
            r"- 'difference / less than / decreased by' → subtract. '3 less than a number' is \(x - 3\)." "\n"
            r"- 'product / times / twice' → multiply. 'Twice a number' is \(2x\)." "\n"
            r"- 'quotient / per / divided by' → divide. 'A number divided by 4' is \(\frac{x}{4}\)." "\n\n"
            r"**Evaluating** means plugging in a value. If \(x = 4\), then \(3x + 5 = 3(4) + 5 = 12 + 5 = 17\)." "\n\n"
            r"⚠️ Common mistake: '3 less than a number' is \(x - 3\), NOT \(3 - x\). The order matters with subtraction." "\n\n"
            r"💡 Tip: \(3x\) always means \(3 \times x\). A number written next to a variable is multiplication.",
        ),
        (
            "2. Simplifying: Like Terms & the Distributive Property",
            r"Before solving anything, you often need to tidy an expression. Two tools do almost all the work." "\n\n"
            r"**Combining like terms.** 'Like terms' have the exact same variable part, so you can add or subtract their coefficients. Think of \(3x\) as '3 apples' and \(5x\) as '5 apples' — together that's '8 apples', \(8x\)." "\n"
            r"\[ 3x + 5x = 8x, \qquad 7y - 2y = 5y. \]" "\n"
            r"But \(3x + 5\) cannot be combined — apples and plain numbers are different things." "\n\n"
            r"**The distributive property.** A number outside parentheses multiplies *everything* inside:" "\n"
            r"\[ a(b + c) = ab + ac, \qquad 2(x + 4) = 2x + 8. \]" "\n\n"
            r"**Worked example.** Simplify \(3(x + 2) + 4x\):" "\n"
            r"- Distribute the 3: \(3x + 6 + 4x\)." "\n"
            r"- Combine like terms \(3x\) and \(4x\): \(7x + 6\)." "\n\n"
            r"**Watch negatives.** A minus sign in front of parentheses flips every sign inside:" "\n"
            r"\[ -(x - 3) = -x + 3. \]" "\n\n"
            r"⚠️ Common mistake: distributing to only the first term. \(2(x + 4)\) is \(2x + 8\), not \(2x + 4\)." "\n\n"
            r"💡 Tip: after distributing, hunt for like terms to combine — that's almost always the next step.",
        ),
        (
            "3. Solving Linear Equations",
            r"Solving an equation means finding the value of the variable that makes it true. The golden rule: **keep the equation balanced** — whatever you do to one side, do to the other. To undo an operation, do its **inverse**." "\n\n"
            r"**One-step:** \(x + 7 = 12 \Rightarrow x = 12 - 7 = 5\)." "\n\n"
            r"**Two-step:** solve \(2x + 5 = 13\)." "\n"
            r"- Subtract 5: \(2x = 8\)." "\n"
            r"- Divide by 2: \(x = 4\)." "\n\n"
            r"**Variables on both sides:** solve \(5x - 3 = 2x + 9\)." "\n"
            r"- Get variables together — subtract \(2x\) from both sides: \(3x - 3 = 9\)." "\n"
            r"- Add 3: \(3x = 12\)." "\n"
            r"- Divide by 3: \(x = 4\)." "\n\n"
            r"**Always check.** Put \(x = 4\) back in: \(5(4) - 3 = 17\) and \(2(4) + 9 = 17\). Both sides match, so it's correct." "\n\n"
            r"⚠️ Common mistake: moving a term across the equals sign without changing its sign. Moving \(+5\) to the other side makes it \(-5\)." "\n\n"
            r"💡 Tip: the usual order is (1) distribute, (2) combine like terms on each side, (3) collect variables on one side, (4) isolate the variable.",
        ),
        (
            "4. Inequalities",
            r"An inequality compares two sides that are *not* necessarily equal, using \(<\) (less than), \(>\) (greater than), \(\le\) (at most), or \(\ge\) (at least). Instead of a single answer, the solution is a whole **range** of numbers." "\n\n"
            r"Great news: you solve inequalities almost exactly like equations — with **one special rule**." "\n\n"
            r"**Worked example.** Solve \(2x + 1 > 5\):" "\n"
            r"- Subtract 1: \(2x > 4\)." "\n"
            r"- Divide by 2: \(x > 2\)." "\n\n"
            r"We graph this on a number line with an **open circle** at 2 (because 2 itself is not included) and an arrow pointing right toward all larger numbers." "\n\n"
            r"[[figure:number_line_ineq|The open circle means 2 is NOT part of the solution; the blue ray covers every number greater than 2.]]" "\n\n"
            r"For \(\le\) or \(\ge\), use a **closed (filled) circle** because the endpoint IS included." "\n\n"
            r"**The special rule:** when you multiply or divide both sides by a **negative** number, flip the inequality sign. Solve \(-3x > 12\): divide by \(-3\) and flip: \(x < -4\)." "\n\n"
            r"⚠️ Common mistake: forgetting to flip the sign. \(-3x > 12\) gives \(x < -4\), not \(x > -4\)." "\n\n"
            r"💡 Tip: test your answer with one number from the range. For \(x > 2\), try \(x = 3\): \(2(3)+1 = 7 > 5\). True — so the direction is right.",
        ),
        (
            "5. The Coordinate Plane & Graphing Lines",
            r"The coordinate plane is two number lines crossing at the **origin** \((0,0)\): a horizontal **x-axis** and a vertical **y-axis**. Every point has an address \((x, y)\): go across \(x\), then up/down \(y\)." "\n\n"
            r"Most GED line questions use **slope-intercept form**:" "\n"
            r"\[ y = mx + b, \]" "\n"
            r"where \(m\) is the **slope** (steepness) and \(b\) is the **y-intercept** (where the line crosses the y-axis)." "\n\n"
            r"**Slope = rise over run** — how far the line goes up for each step to the right:" "\n"
            r"\[ m = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1}. \]" "\n\n"
            r"**Worked example.** Graph \(y = 2x + 1\)." "\n"
            r"- The y-intercept is \(b = 1\), so plot the point \((0, 1)\)." "\n"
            r"- The slope is \(m = 2 = \frac{2}{1}\): from \((0,1)\), go up 2 and right 1 to reach \((1, 3)\)." "\n"
            r"- Connect the points." "\n\n"
            r"[[figure:coord_line|Start at the y-intercept (0, 1), then use the slope (up 2, right 1) to find the next point and draw the line.]]" "\n\n"
            r"**Slope from two points.** Through \((1, 2)\) and \((4, 8)\): \(m = \frac{8-2}{4-1} = \frac{6}{3} = 2\)." "\n\n"
            r"⚠️ Common mistake: a positive slope rises left-to-right; a negative slope falls. A horizontal line has slope \(0\)." "\n\n"
            r"💡 Tip: to find the x-intercept, set \(y = 0\) and solve; to find the y-intercept, set \(x = 0\).",
        ),
        (
            "6. Systems of Linear Equations",
            r"A **system** is two equations with the same two unknowns. The solution is the single \((x, y)\) pair that satisfies **both** — graphically, the point where the two lines cross." "\n\n"
            r"**Method 1 — Substitution.** Solve one equation for a variable, then substitute into the other. Solve:" "\n"
            r"\[ \begin{cases} y = x + 1 \\ 2x + y = 7 \end{cases} \]" "\n"
            r"- Substitute \(y = x + 1\) into the second: \(2x + (x + 1) = 7\)." "\n"
            r"- Simplify: \(3x + 1 = 7 \Rightarrow 3x = 6 \Rightarrow x = 2\)." "\n"
            r"- Back-substitute: \(y = 2 + 1 = 3\). Solution \((2, 3)\)." "\n\n"
            r"**Method 2 — Elimination.** Add or subtract the equations so one variable cancels. Solve:" "\n"
            r"\[ \begin{cases} x + y = 10 \\ x - y = 4 \end{cases} \]" "\n"
            r"- Add them: \(2x = 14 \Rightarrow x = 7\)." "\n"
            r"- Substitute: \(7 + y = 10 \Rightarrow y = 3\). Solution \((7, 3)\)." "\n\n"
            r"⚠️ Common mistake: solving for only one variable. A complete answer gives **both** \(x\) and \(y\)." "\n\n"
            r"💡 Tip: use elimination when a variable already lines up to cancel; use substitution when one equation is already solved for a variable.",
        ),
        (
            "7. Exponents & Polynomials",
            r"An **exponent** is repeated multiplication: \(2^4 = 2 \times 2 \times 2 \times 2 = 16\). The **laws of exponents** let you simplify quickly:" "\n"
            r"\[ a^m \cdot a^n = a^{m+n}, \qquad \frac{a^m}{a^n} = a^{m-n}, \qquad (a^m)^n = a^{mn}, \]" "\n"
            r"\[ a^0 = 1, \qquad a^{-n} = \frac{1}{a^n}. \]" "\n"
            r"Example: \(x^3 \cdot x^2 = x^5\) and \(\frac{x^6}{x^2} = x^4\)." "\n\n"
            r"A **polynomial** is a sum of terms like \(2x^2 + 3x - 5\). **Add or subtract** polynomials by combining like terms:" "\n"
            r"\[ (2x^2 + 3x) + (x^2 - 5x) = 3x^2 - 2x. \]" "\n\n"
            r"**Multiply two binomials** with **FOIL** (First, Outer, Inner, Last):" "\n"
            r"\[ (x + 3)(x + 2) = \underbrace{x^2}_{F} + \underbrace{2x}_{O} + \underbrace{3x}_{I} + \underbrace{6}_{L} = x^2 + 5x + 6. \]" "\n\n"
            r"⚠️ Common mistake: \(a^m \cdot a^n\) is \(a^{m+n}\) — you ADD exponents when multiplying, not multiply them." "\n\n"
            r"💡 Tip: only **like terms** combine. \(x^2\) and \(x\) are different and cannot be added together.",
        ),
        (
            "8. Factoring & Quadratic Equations",
            r"**Factoring** is multiplication in reverse: rewriting a polynomial as a product. It's the key to solving quadratic equations of the form \(ax^2 + bx + c = 0\)." "\n\n"
            r"**Step 1 — Pull out a common factor (GCF)** when every term shares one:" "\n"
            r"\[ 6x^2 + 9x = 3x(2x + 3). \]" "\n\n"
            r"**Step 2 — Factor a trinomial** \(x^2 + bx + c\): find two numbers that **multiply to \(c\)** and **add to \(b\)**. For \(x^2 + 5x + 6\), the numbers \(2\) and \(3\) work:" "\n"
            r"\[ x^2 + 5x + 6 = (x + 2)(x + 3). \]" "\n\n"
            r"**Step 3 — Zero-product property.** If a product is zero, one factor must be zero. From \((x+2)(x+3) = 0\): \(x = -2\) or \(x = -3\). These solutions are the **roots** — exactly where the parabola crosses the x-axis." "\n\n"
            r"[[figure:parabola|The graph of a quadratic is a parabola. Its roots are the x-values where it crosses the x-axis.]]" "\n\n"
            r"**When factoring is hard, use the quadratic formula** (it always works):" "\n"
            r"\[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}. \]" "\n"
            r"For \(x^2 - 5x + 6 = 0\) with \(a=1, b=-5, c=6\): \(x = \frac{5 \pm \sqrt{25 - 24}}{2} = \frac{5 \pm 1}{2}\), giving \(x = 3\) or \(x = 2\)." "\n\n"
            r"⚠️ Common mistake: forgetting one solution. A quadratic usually has **two** answers — keep both the \(+\) and \(-\) from the \(\pm\)." "\n\n"
            r"💡 Tip: always factor out a GCF first; it makes the remaining trinomial smaller and easier.",
        ),
        (
            "9. Introduction to Functions",
            r"A **function** is a rule that takes an input and gives exactly one output — like a machine: put a number in, get a number out." "\n\n"
            r"**Function notation** \(f(x)\) is read 'f of x'. It does **not** mean multiplication; \(x\) is the input. The rule \(f(x) = 2x + 1\) says 'double the input and add 1'." "\n\n"
            r"**Evaluating** means substituting a value for \(x\):" "\n"
            r"- \(f(3) = 2(3) + 1 = 7\)." "\n"
            r"- \(f(0) = 2(0) + 1 = 1\)." "\n"
            r"- \(f(-2) = 2(-2) + 1 = -3\)." "\n\n"
            r"You can think of \(y\) and \(f(x)\) as the same thing: \(y = 2x + 1\) and \(f(x) = 2x + 1\) graph the identical line. The input \(x\) is the horizontal value; the output \(f(x)\) is the height." "\n\n"
            r"**Real-world meaning.** If \(C(m) = 30 + 0.10m\) gives a phone bill for \(m\) minutes, then \(C(100) = 30 + 0.10(100) = \$40\) is the cost of 100 minutes." "\n\n"
            r"⚠️ Common mistake: reading \(f(3)\) as \(f \times 3\). It means 'evaluate the function when the input is 3'." "\n\n"
            r"💡 Tip: whatever is inside the parentheses replaces every \(x\) in the rule.",
        ),
    ],
    "mcqs": [
        {
            "text": r"Write an algebraic expression for '7 less than twice a number \(x\)'.",
            "difficulty": 1,
            "choices": [(r"\(2x - 7\)", True), (r"\(7 - 2x\)", False), (r"\(2(x - 7)\)", False), (r"\(7 - x^2\)", False)],
            "explanation": r"'Twice a number' is \(2x\); '7 less than' that subtracts 7 from it, giving \(2x - 7\). Order matters: it is not \(7 - 2x\).",
        },
        {
            "text": r"Evaluate \(4x - 5\) when \(x = 3\).",
            "difficulty": 1,
            "choices": [(r"\(7\)", True), (r"\(2\)", False), (r"\(17\)", False), (r"\(12\)", False)],
            "explanation": r"Substitute \(x = 3\): \(4(3) - 5 = 12 - 5 = 7\).",
        },
        {
            "text": r"Simplify \(3(x + 2) + 4x\).",
            "difficulty": 1,
            "choices": [(r"\(7x + 6\)", True), (r"\(7x + 2\)", False), (r"\(3x + 6\)", False), (r"\(12x\)", False)],
            "explanation": r"Distribute: \(3x + 6 + 4x\). Combine like terms \(3x + 4x = 7x\): the result is \(7x + 6\).",
        },
        {
            "text": r"Simplify \(-(x - 4) + 2x\).",
            "difficulty": 2,
            "choices": [(r"\(x + 4\)", True), (r"\(3x - 4\)", False), (r"\(-x + 4\)", False), (r"\(x - 4\)", False)],
            "explanation": r"The leading minus flips both signs: \(-(x-4) = -x + 4\). Then \(-x + 4 + 2x = x + 4\).",
        },
        {
            "text": r"Solve for \(x\): \(2x + 5 = 13\).",
            "difficulty": 1,
            "choices": [(r"\(x = 4\)", True), (r"\(x = 9\)", False), (r"\(x = 3\)", False), (r"\(x = 6\)", False)],
            "explanation": r"Subtract 5: \(2x = 8\). Divide by 2: \(x = 4\).",
        },
        {
            "text": r"Solve for \(x\): \(5x - 3 = 2x + 9\).",
            "difficulty": 2,
            "choices": [(r"\(x = 4\)", True), (r"\(x = 2\)", False), (r"\(x = 6\)", False), (r"\(x = 3\)", False)],
            "explanation": r"Subtract \(2x\): \(3x - 3 = 9\). Add 3: \(3x = 12\). Divide by 3: \(x = 4\).",
        },
        {
            "text": r"Solve the inequality \(2x + 1 > 5\).",
            "difficulty": 2,
            "choices": [(r"\(x > 2\)", True), (r"\(x < 2\)", False), (r"\(x > 3\)", False), (r"\(x > -2\)", False)],
            "explanation": r"Subtract 1: \(2x > 4\). Divide by 2 (positive, no flip): \(x > 2\).",
        },
        {
            "text": r"Solve the inequality \(-3x > 12\).",
            "difficulty": 2,
            "choices": [(r"\(x < -4\)", True), (r"\(x > -4\)", False), (r"\(x < 4\)", False), (r"\(x > 4\)", False)],
            "explanation": r"Divide both sides by \(-3\) and FLIP the sign because of the negative: \(x < -4\).",
        },
        {
            "text": r"What is the slope of the line \(y = 2x + 1\)?",
            "difficulty": 1,
            "choices": [(r"\(2\)", True), (r"\(1\)", False), (r"\(\tfrac{1}{2}\)", False), (r"\(-2\)", False)],
            "explanation": r"In slope-intercept form \(y = mx + b\), the slope is \(m\). Here \(m = 2\) (and the y-intercept is \(b = 1\)).",
        },
        {
            "text": r"What is the slope of the line through \((1, 2)\) and \((4, 8)\)?",
            "difficulty": 2,
            "choices": [(r"\(2\)", True), (r"\(3\)", False), (r"\(\tfrac{1}{2}\)", False), (r"\(6\)", False)],
            "explanation": r"Slope \(= \frac{y_2 - y_1}{x_2 - x_1} = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2\).",
        },
        {
            "text": r"Solve the system \(\begin{cases} y = x + 1 \\ 2x + y = 7 \end{cases}\). What is \(x\)?",
            "difficulty": 3,
            "choices": [(r"\(x = 2\)", True), (r"\(x = 3\)", False), (r"\(x = 1\)", False), (r"\(x = 7\)", False)],
            "explanation": r"Substitute \(y = x+1\) into \(2x + y = 7\): \(2x + x + 1 = 7\), so \(3x = 6\) and \(x = 2\) (then \(y = 3\)).",
        },
        {
            "text": r"Simplify \(x^3 \cdot x^4\).",
            "difficulty": 1,
            "choices": [(r"\(x^7\)", True), (r"\(x^{12}\)", False), (r"\(x^1\)", False), (r"\(2x^7\)", False)],
            "explanation": r"When multiplying powers with the same base, add the exponents: \(x^{3+4} = x^7\).",
        },
        {
            "text": r"Expand \((x + 3)(x + 2)\).",
            "difficulty": 2,
            "choices": [(r"\(x^2 + 5x + 6\)", True), (r"\(x^2 + 6x + 5\)", False),
                        (r"\(x^2 + 6\)", False), (r"\(2x + 5\)", False)],
            "explanation": r"FOIL: \(x^2 + 2x + 3x + 6 = x^2 + 5x + 6\).",
        },
        {
            "text": r"Factor \(x^2 + 5x + 6\).",
            "difficulty": 2,
            "choices": [(r"\((x + 2)(x + 3)\)", True), (r"\((x + 1)(x + 6)\)", False),
                        (r"\((x - 2)(x - 3)\)", False), (r"\((x + 5)(x + 1)\)", False)],
            "explanation": r"Find two numbers that multiply to \(6\) and add to \(5\): \(2\) and \(3\). So \(x^2 + 5x + 6 = (x+2)(x+3)\).",
        },
        {
            "text": r"Solve \(x^2 - 5x + 6 = 0\).",
            "difficulty": 3,
            "choices": [(r"\(x = 2\) or \(x = 3\)", True), (r"\(x = -2\) or \(x = -3\)", False),
                        (r"\(x = 1\) or \(x = 6\)", False), (r"\(x = 5\) or \(x = 6\)", False)],
            "explanation": r"Factor to \((x-2)(x-3) = 0\). By the zero-product property, \(x = 2\) or \(x = 3\).",
        },
        {
            "text": r"If \(f(x) = 2x + 1\), what is \(f(3)\)?",
            "difficulty": 1,
            "choices": [(r"\(7\)", True), (r"\(6\)", False), (r"\(5\)", False), (r"\(9\)", False)],
            "explanation": r"Substitute the input 3 for \(x\): \(f(3) = 2(3) + 1 = 7\). Note \(f(3)\) means 'evaluate at 3', not multiply.",
        },
    ],
    "essays": [
        {
            "text": (
                r"A taxi charges a flat \(\$3\) fee plus \(\$2\) per mile. "
                r"Write an equation for the total cost \(C\) in terms of miles \(m\), then use it to find the cost of a "
                r"7-mile ride. Finally, if a ride cost \(\$19\), set up and solve an equation to find how many miles it was. "
                r"Show every step."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full marks for: (1) the equation \(C = 2m + 3\); "
                r"(2) cost of 7 miles: \(C = 2(7) + 3 = \$17\); "
                r"(3) setting \(2m + 3 = 19\), solving \(2m = 16\), \(m = 8\) miles, with clear steps. "
                "Deduct for a missing step, an incorrect equation, or arithmetic errors."
            ),
        },
        {
            "text": (
                r"Solve the quadratic equation \(x^2 + 2x - 8 = 0\) two ways: first by factoring, then by the "
                r"quadratic formula. Show that both methods give the same roots, and explain what the roots mean "
                r"on the graph of \(y = x^2 + 2x - 8\)."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full marks for: (1) factoring to \((x + 4)(x - 2) = 0\), giving \(x = -4\) or \(x = 2\); "
                r"(2) quadratic formula with \(a=1, b=2, c=-8\): \(x = \frac{-2 \pm \sqrt{4 + 32}}{2} = \frac{-2 \pm 6}{2}\), "
                r"giving \(x = 2\) or \(x = -4\); (3) explaining the roots are where the parabola crosses the x-axis. "
                "Deduct for an arithmetic error or missing the graphical interpretation."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'GED Math: Algebra In Depth' course."

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

        # Phase 1 is MCQ-only: written-response prompts are not seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
