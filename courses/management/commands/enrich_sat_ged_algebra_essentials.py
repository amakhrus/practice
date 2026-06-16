from django.core.management.base import BaseCommand
from courses.models import Lesson

LESSONS = [
    (0, """Solving Linear Equations

A linear equation is any equation where the variable appears to the first power — no exponents, no square roots on the variable itself. The goal is always the same: isolate the variable on one side of the equals sign by performing the same operation on both sides.

Key Algebraic Procedure
The golden rule of algebra is balance: whatever you do to one side of the equation, you must do to the other. Work through these steps in order:
1. Simplify each side separately — distribute and combine like terms.
2. Move all variable terms to one side using addition or subtraction.
3. Move all constant (number) terms to the other side.
4. Divide both sides by the coefficient of the variable.

Worked Example
Solve for x: 3(2x - 4) = 2x + 8

Step 1 — Distribute on the left:
  6x - 12 = 2x + 8

Step 2 — Subtract 2x from both sides to gather variable terms on the left:
  6x - 2x - 12 = 8
  4x - 12 = 8

Step 3 — Add 12 to both sides to isolate the variable term:
  4x = 20

Step 4 — Divide both sides by 4:
  x = 5

Check your answer by substituting back: 3(2·5 - 4) = 3(6) = 18, and 2·5 + 8 = 18. Both sides match, so x = 5 is correct.

A Second Example with Fractions
Solve for x: x/3 + 2 = 5

Subtract 2 from both sides: x/3 = 3
Multiply both sides by 3: x = 9

Fractions in linear equations are easiest to handle by multiplying through by the denominator early. If your equation has multiple fractions with different denominators, multiply every term by the least common denominator (LCD) to clear all fractions at once.

Common Mistake to Avoid
Forgetting to distribute the negative sign. When you see something like -(3x - 5), many students write -3x - 5. The correct distribution is -3x + 5 because the negative applies to every term inside the parentheses. A missed sign flip will give you a completely wrong answer even if all your other steps are perfect.

Another frequent error is dividing only one term instead of the entire side. If you have 4x = 20 and mistakenly write x = 20 - 4, that is incorrect. Division by 4 applies to the whole right side: x = 20/4 = 5.

Practical GED/SAT Test Strategy
On the GED and SAT, many linear equation problems are disguised as word problems. Train yourself to translate words into equations quickly. Phrases like "five more than twice a number" become 2x + 5. "Three times a number decreased by seven equals fourteen" becomes 3x - 7 = 14.

When you are short on time, use back-substitution: plug each answer choice into the original equation and see which one makes both sides equal. This approach is slower but virtually foolproof, and on multiple-choice sections it guarantees the correct answer without requiring you to solve from scratch.

Also, after solving, always do a 10-second mental check — substitute your answer back into the original equation. This single habit catches arithmetic errors before they cost you points.

Linear equations appear on virtually every GED math section and account for a large share of SAT Math questions. Mastering this foundational skill pays dividends across the entire test.
"""),
    (1, """Systems of Two Equations

A system of two equations is a pair of linear equations that share the same two variables, typically x and y. The solution is the ordered pair (x, y) that satisfies both equations simultaneously — graphically, it is the point where two lines intersect.

There are three possible outcomes for any system:
- One solution: the lines intersect at exactly one point (most common on tests).
- No solution: the lines are parallel and never meet.
- Infinitely many solutions: the lines are identical (one equation is a multiple of the other).

Key Algebraic Procedures: Two Methods

Method 1 — Substitution
Best when one equation already has a variable isolated (or nearly so).
1. Solve one equation for one variable.
2. Substitute that expression into the second equation.
3. Solve the resulting single-variable equation.
4. Substitute back to find the other variable.

Method 2 — Elimination (Addition/Subtraction)
Best when coefficients can be made equal easily.
1. Multiply one or both equations by constants so that the coefficient of one variable is the same (or opposite) in both equations.
2. Add or subtract the equations to eliminate that variable.
3. Solve for the remaining variable.
4. Substitute back to find the eliminated variable.

Worked Example — Substitution
Solve the system:
  y = 2x - 1   ...(Equation 1)
  3x + y = 14  ...(Equation 2)

Since Equation 1 already isolates y, substitute (2x - 1) for y in Equation 2:
  3x + (2x - 1) = 14
  5x - 1 = 14
  5x = 15
  x = 3

Now substitute x = 3 back into Equation 1:
  y = 2(3) - 1 = 5

Solution: (3, 5). Check in Equation 2: 3(3) + 5 = 9 + 5 = 14. Correct.

Worked Example — Elimination
Solve the system:
  2x + 3y = 12  ...(Equation 1)
  4x - 3y = 6   ...(Equation 2)

The y-coefficients are already opposites (+3 and -3), so add the equations directly:
  (2x + 4x) + (3y - 3y) = 12 + 6
  6x = 18
  x = 3

Substitute x = 3 into Equation 1:
  2(3) + 3y = 12
  6 + 3y = 12
  3y = 6
  y = 2

Solution: (3, 2).

Identifying No-Solution and Infinite-Solution Systems
If, after elimination or substitution, every variable cancels and you get a false statement like 0 = 5, the system has no solution. If you get a true statement like 0 = 0, the system has infinitely many solutions.

Common Mistake to Avoid
Substituting back into the equation you derived rather than one of the originals. After finding x = 3 through substitution, always plug back into one of the original equations — not into the rearranged form you created mid-solution. The original equations are guaranteed to be correct; the intermediate steps might contain errors.

Also watch for sign errors when using elimination. If you multiply an equation by -1 to set up subtraction, rewrite every term with its new sign before proceeding.

Practical GED/SAT Test Strategy
The SAT often presents systems disguised in context: "A store sells apples for $1.50 and oranges for $0.75. A customer buys 10 pieces of fruit for $12. How many of each?" Set up two equations (one for quantity, one for cost) and solve.

Elimination is generally faster than substitution for GED and SAT problems because the numbers are designed to cancel cleanly. If you see coefficients that are multiples of each other, reach for elimination first. Save substitution for when one equation already gives you y = ... or x = ... without extra work.

For grid-in SAT questions where you must produce a numeric answer, systems of equations are among the most predictable problem types — the answer is almost always a small integer or a simple fraction. If your answer is a large or messy number, re-examine your setup.
"""),
    (2, """Quadratic Equations

A quadratic equation is any equation that can be written in the standard form ax² + bx + c = 0, where a ≠ 0. The variable is raised to the second power, which means quadratics can have up to two solutions (called roots or zeros). These solutions represent the x-values where a parabola crosses the x-axis.

Key Algebraic Procedures: Three Methods

Method 1 — Factoring
When the quadratic factors neatly into two binomials, this is the fastest approach.
1. Write the equation in standard form (= 0).
2. Find two numbers that multiply to ac and add to b.
3. Factor and set each factor equal to zero.
4. Solve each mini-equation.

Method 2 — Quadratic Formula
Works for any quadratic, even when factoring is difficult or impossible.
  x = (-b ± √(b² - 4ac)) / (2a)
The expression under the radical, b² - 4ac, is called the discriminant. If it is positive, there are two real solutions. If it equals zero, there is exactly one (repeated) solution. If it is negative, there are no real solutions.

Method 3 — Completing the Square
Useful for deriving formulas and for certain SAT problems, but less common as a direct test strategy.

Worked Example — Factoring
Solve: x² + 5x + 6 = 0

Find two numbers that multiply to 6 and add to 5: those are 2 and 3.
Factor: (x + 2)(x + 3) = 0

Set each factor to zero:
  x + 2 = 0  →  x = -2
  x + 3 = 0  →  x = -3

Solutions: x = -2 and x = -3.

Check: (-2)² + 5(-2) + 6 = 4 - 10 + 6 = 0. Correct.

Worked Example — Quadratic Formula
Solve: 2x² - 3x - 2 = 0

Identify: a = 2, b = -3, c = -2.

Discriminant: b² - 4ac = (-3)² - 4(2)(-2) = 9 + 16 = 25.

Since the discriminant is positive and a perfect square, we get two rational solutions:
  x = (3 ± √25) / (2·2) = (3 ± 5) / 4

  x = (3 + 5)/4 = 8/4 = 2
  x = (3 - 5)/4 = -2/4 = -1/2

Solutions: x = 2 and x = -1/2.

Special Cases
Difference of squares: x² - 9 = 0 factors as (x + 3)(x - 3) = 0, giving x = ±3.
Perfect square trinomials: x² - 6x + 9 = 0 factors as (x - 3)² = 0, giving x = 3 (one repeated root).

Common Mistake to Avoid
Forgetting to set the equation equal to zero before factoring. If the equation reads x² + 5x = -6 and you try to factor the left side directly, you will get a wrong answer. You must first move all terms to one side: x² + 5x + 6 = 0. Factoring only works when one side is exactly zero.

A second common error is misapplying the quadratic formula by dropping the ± sign and computing only one solution. Quadratics typically have two roots — show both.

Also be careful with the formula when b is negative. Students often substitute b² as a negative number. Remember: (-3)² = +9, never -9.

Practical GED/SAT Test Strategy
The SAT includes both standard quadratic problems and contextual ones (such as finding the time when a projectile reaches the ground using h(t) = -16t² + vt + h₀). In these applied problems, one of the two solutions often produces a negative value for time or distance and is therefore rejected in context. Always check which solution makes physical sense.

For GED exams, factoring is sufficient for most quadratic questions because the test tends to use coefficients that factor cleanly. However, memorizing the quadratic formula is an insurance policy — it works every time, regardless of how unfriendly the numbers look. Spend a few minutes committing x = (-b ± √(b² - 4ac)) / (2a) to memory.

When pressed for time on a multiple-choice problem, you can verify a proposed root by substituting it into the original equation. If both sides equal zero, the answer is confirmed.
"""),
    (3, """Exponents and Radicals

Exponents and radicals (roots) are two sides of the same coin. An exponent tells you how many times to multiply a base by itself; a radical undoes that operation. Understanding how they interact is essential for simplifying expressions and solving equations that appear throughout GED and SAT algebra sections.

Key Rules for Exponents
Let a and b be nonzero bases, and let m and n be any real-number exponents.

Product Rule:   a^m · a^n = a^(m+n)      — add exponents when multiplying same base
Quotient Rule:  a^m / a^n = a^(m-n)      — subtract exponents when dividing same base
Power Rule:     (a^m)^n  = a^(m·n)       — multiply exponents for a power of a power
Product of Powers: (ab)^n = a^n · b^n    — distribute exponent over a product
Zero Exponent:  a^0 = 1                  — any nonzero base to the zero power is 1
Negative Exponent: a^(-n) = 1/a^n        — a negative exponent means reciprocal
Fractional Exponent: a^(m/n) = (n-th root of a)^m — connects radicals and exponents

Key Rules for Radicals
√(a · b) = √a · √b     — product property of radicals
√(a / b) = √a / √b     — quotient property of radicals
(√a)² = a               — squaring a square root returns the original value

Simplifying a radical means factoring out all perfect squares (or perfect cubes for cube roots). For example, √72 = √(36 · 2) = 6√2.

Adding and subtracting radicals works like combining like terms: 3√5 + 7√5 = 10√5. You can only add radicals if their radicands (the expressions under the radical sign) are identical.

Worked Example — Simplifying Exponential Expressions
Simplify: (2x³y)² · x⁻¹

Step 1 — Apply the power rule to the parentheses:
  2² · x^(3·2) · y² = 4x⁶y²

Step 2 — Multiply by x⁻¹ using the product rule:
  4x^(6 + (-1)) · y² = 4x⁵y²

Final answer: 4x⁵y²

Worked Example — Solving an Equation with a Radical
Solve: √(3x + 4) = 5

Step 1 — Square both sides to eliminate the radical:
  3x + 4 = 25

Step 2 — Subtract 4 from both sides:
  3x = 21

Step 3 — Divide by 3:
  x = 7

Always check radical equation solutions by substituting back: √(3·7 + 4) = √25 = 5. Correct.

Worked Example — Fractional Exponents
Evaluate: 27^(2/3)

The denominator of the fractional exponent is the root index, and the numerator is the power:
  27^(2/3) = (cube root of 27)² = 3² = 9

Common Mistake to Avoid
Misapplying the power rule by adding instead of multiplying. Students often confuse (x³)² = x⁶ (correct: multiply 3 × 2) with x³ · x² = x⁵ (correct: add 3 + 2). The key distinction: parentheses with an outer exponent means multiply; multiplication of same-base terms means add.

Another widespread error is forgetting to check for extraneous solutions when solving radical equations. Squaring both sides can introduce solutions that do not satisfy the original equation. For example, if you obtain x = -1 after squaring, you must verify it in the original equation — a square root cannot equal a negative number.

Also remember that negative exponents do not make a number negative. The expression 2⁻³ equals 1/8, not -8.

Practical GED/SAT Test Strategy
The SAT frequently tests fractional exponents alongside radical notation in the same problem to check whether you recognize they are equivalent. If you see 8^(1/3), rewrite it as the cube root of 8 immediately — that equals 2, and the problem likely continues from there.

For the GED, exponent questions often appear in scientific notation context (for example, 3.2 × 10⁴). Practice converting between standard and scientific notation using exponent rules, since these problems are quick points if you have the rules memorized.

A powerful test-taking shortcut: when an expression with exponents looks complex, try assigning a simple number (like x = 2) to the variable and evaluating both the expression and each answer choice numerically. The answer choice that matches your evaluation is correct. This "plug-in" strategy is especially useful when simplifying algebraic expressions with multiple exponent rules.
"""),
]

class Command(BaseCommand):
    help = "Enrich lesson content for SAT/GED Algebra Essentials"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(course__slug="sat-ged-algebra-essentials", order=order).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(self.style.SUCCESS("Done."))
