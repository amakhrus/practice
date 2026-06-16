"""
Seed an advanced GED Algebra course on equations.

This is the next course after GED Algebra: Equations Mastery. It uses tougher
setups, more worked examples, and a larger question bank with detailed
step-by-step explanations.

Run:
    python manage.py seed_ged_algebra_advanced_equations
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


def explain(*steps, trap):
    parts = [f"Step {index}: {step}" for index, step in enumerate(steps, start=1)]
    parts.append(f"Common trap: {trap}")
    return " ".join(parts)


def item(text, correct, wrong, steps, trap, difficulty=3):
    return {
        "text": text,
        "difficulty": difficulty,
        "choices": [(correct, True), *[(choice, False) for choice in wrong]],
        "explanation": explain(*steps, trap=trap),
    }


COURSE = {
    "title": "GED Algebra: Advanced Equations & Applications",
    "slug": "ged-algebra-advanced-equations",
    "program": "GED",
    "subject": "math",
    "description": (
        "A harder follow-up to GED Algebra: Equations Mastery. This course gives "
        "students advanced equation practice with more examples: nested parentheses, "
        "fractions and decimals, variables on both sides, literal equations, percent "
        "and rate applications, absolute value, proportions, quadratics, systems, "
        "radicals, and exponential equations. Every practice answer explains the "
        "solution step by step and names the likely trap."
    ),
    "lessons": [
        (
            "1. Advanced Equation Routine",
            r"""
Hard equations are usually built from easy moves in a longer chain. The secret is not speed; it is order.

Use this routine:
- Clear grouping symbols: parentheses, brackets, and leading minus signs.
- Clear fractions or decimals if they make the equation messy.
- Combine like terms on each side.
- Move variables to one side and constants to the other.
- Divide by the final coefficient.
- Check in the original equation.

[[figure:equation_balance|The balance idea still controls every advanced equation.]]

Example 1:
\[
4(2x-3)+5=37.
\]
Distribute:
\[
8x-12+5=37.
\]
Combine constants:
\[
8x-7=37.
\]
Add 7:
\[
8x=44.
\]
Divide by 8:
\[
x=\frac{44}{8}=\frac{11}{2}=5.5.
\]

Example 2:
\[
5-(2x-7)=18.
\]
The minus sign before the parentheses changes both signs:
\[
5-2x+7=18.
\]
Combine:
\[
12-2x=18.
\]
Subtract 12:
\[
-2x=6.
\]
Divide by \(-2\):
\[
x=-3.
\]

Common mistake: trying to "move" terms in your head before cleaning the equation. Clean first, then isolate.

[[check:What is the first move in \(3(x+4)-2=19\)?|distribute;;distribute 3|Clear the parentheses before combining or isolating.]]
            """,
        ),
        (
            "2. Parentheses Inside Parentheses",
            r"""
Some equations have more than one layer of grouping. Work from the inside outward, or distribute carefully one layer at a time.

Example 1:
\[
2[3x-(x+4)]=16.
\]
Inside the brackets:
\[
3x-(x+4)=3x-x-4=2x-4.
\]
Now multiply by 2:
\[
2(2x-4)=16.
\]
Distribute:
\[
4x-8=16.
\]
Add 8 and divide by 4:
\[
4x=24,\qquad x=6.
\]

Example 2:
\[
6-(x+2)=1.
\]
The subtraction applies to the whole group:
\[
6-x-2=1.
\]
Combine:
\[
4-x=1.
\]
Subtract 4:
\[
-x=-3.
\]
Multiply by \(-1\):
\[
x=3.
\]

Example 3:
\[
5(x+1)-2x=20.
\]
Distribute first:
\[
5x+5-2x=20.
\]
Combine:
\[
3x+5=20.
\]
Then solve:
\[
3x=15,\qquad x=5.
\]

Common mistake: treating \(6-(x+2)\) as \(6-x+2\). The minus changes both signs.

[[check:Solve \(2[3x-(x+4)]=16\).|6|Inside first: \(3x-x-4=2x-4\).]]
            """,
        ),
        (
            "3. Fractions: Clear the Denominators",
            r"""
Fractions are not a different kind of algebra. They only make the arithmetic heavier. To simplify, multiply every term by the least common denominator (LCD).

Example 1:
\[
\frac{x}{2}+\frac{x}{3}=10.
\]
The LCD of 2 and 3 is 6. Multiply every term by 6:
\[
6\cdot\frac{x}{2}+6\cdot\frac{x}{3}=6\cdot10.
\]
Simplify:
\[
3x+2x=60.
\]
So:
\[
5x=60,\qquad x=12.
\]

Example 2:
\[
\frac{x+1}{3}+\frac{x-2}{2}=7.
\]
LCD is 6:
\[
2(x+1)+3(x-2)=42.
\]
Distribute:
\[
2x+2+3x-6=42.
\]
Combine:
\[
5x-4=42.
\]
Solve:
\[
5x=46,\qquad x=\frac{46}{5}.
\]

Example 3:
\[
\frac{2x-1}{5}=\frac{x+4}{3}.
\]
Cross-multiply:
\[
3(2x-1)=5(x+4).
\]
Distribute:
\[
6x-3=5x+20.
\]
So:
\[
x=23.
\]

Common mistake: multiplying only the fraction terms and forgetting constants. Every term on both sides must be multiplied by the LCD.

[[check:What is the LCD of 2 and 3?|6|Use the smallest number both denominators divide into.]]
            """,
        ),
        (
            "4. Decimals and Percent Equations",
            r"""
Decimal equations often appear in money, tax, discount, interest, and percent problems. You can solve with decimals directly or rewrite them as fractions.

Example 1:
\[
0.25(8x-4)=9.
\]
Distribute:
\[
2x-1=9.
\]
Add 1:
\[
2x=10.
\]
Divide by 2:
\[
x=5.
\]

Example 2:
\[
0.2x+4=10.
\]
Subtract 4:
\[
0.2x=6.
\]
Since \(0.2=\frac{1}{5}\), divide by \(0.2\), or multiply by 5:
\[
x=30.
\]

Example 3 - percent:
"The sale price is 85 percent of the original price. The sale price is 170 dollars."
\[
0.85p=170.
\]
Divide:
\[
p=200.
\]

[[figure:percent_equation_triangle|Percent equations still use part = percent times whole.]]

Common mistake: taking the percent of the known value when the known value is already the result. In \(0.85p=170\), 170 is the part, not the original whole.

[[check:Write 85 percent as a decimal.|0.85|Move the decimal point two places left.]]
            """,
        ),
        (
            "5. Variables on Both Sides: Harder Cases",
            r"""
When variables appear on both sides, first simplify each side. Then collect variables.

Example 1:
\[
4(2x-3)=5x+15.
\]
Distribute:
\[
8x-12=5x+15.
\]
Subtract \(5x\):
\[
3x-12=15.
\]
Add 12:
\[
3x=27.
\]
Divide:
\[
x=9.
\]

Example 2:
\[
8-2x=x-13.
\]
Add \(2x\) to both sides:
\[
8=3x-13.
\]
Add 13:
\[
21=3x.
\]
Divide:
\[
x=7.
\]

Example 3:
\[
3(x+2)=2x+11.
\]
Distribute:
\[
3x+6=2x+11.
\]
Subtract \(2x\):
\[
x+6=11.
\]
Subtract 6:
\[
x=5.
\]

Strategy tip: move the smaller variable term when possible. It keeps the coefficient positive and reduces sign errors.

Common mistake: subtracting a variable term from only one side. Equations must stay balanced.

[[check:Solve \(3(x+2)=2x+11\).|5|Distribute, subtract \(2x\), then subtract 6.]]
            """,
        ),
        (
            "6. Literal Equations and Rearranging Formulas",
            r"""
A literal equation asks you to solve for a variable while other letters remain in the answer. Treat the other letters like numbers.

Example 1:
\[
A=lw.
\]
Solve for \(w\):
\[
w=\frac{A}{l}.
\]

Example 2:
\[
P=2l+2w.
\]
Solve for \(l\). Subtract \(2w\):
\[
P-2w=2l.
\]
Divide by 2:
\[
l=\frac{P-2w}{2}.
\]

Example 3:
\[
C=\frac{5}{9}(F-32).
\]
Solve for \(F\). Multiply by \(\frac{9}{5}\):
\[
\frac{9}{5}C=F-32.
\]
Add 32:
\[
F=\frac{9}{5}C+32.
\]

Example 4:
\[
y=mx+b.
\]
Solve for \(m\). Subtract \(b\):
\[
y-b=mx.
\]
Divide by \(x\):
\[
m=\frac{y-b}{x}.
\]

Common mistake: dividing only one term. In \(l=\frac{P-2w}{2}\), the entire numerator \(P-2w\) is divided by 2.

[[check:Solve \(A=lw\) for \(w\).|A/l;;\frac{A}{l}|Divide both sides by \(l\).]]
            """,
        ),
        (
            "7. Word Problems with Two Expressions",
            r"""
Advanced word problems often compare two expressions.

Example 1 - two plans:
Plan A costs 20 dollars plus 5 dollars per month. Plan B costs 50 dollars plus 2 dollars per month. When are they equal?
\[
20+5m=50+2m.
\]
Subtract \(2m\):
\[
20+3m=50.
\]
Subtract 20:
\[
3m=30.
\]
Divide:
\[
m=10.
\]

Example 2 - consecutive integers:
Three consecutive integers have sum 75. Let the first be \(n\):
\[
n+(n+1)+(n+2)=75.
\]
Combine:
\[
3n+3=75.
\]
Subtract 3:
\[
3n=72.
\]
Divide:
\[
n=24.
\]
The integers are 24, 25, and 26.

Example 3 - geometry:
A rectangle has width \(x\), length \(x+5\), and perimeter 74:
\[
2x+2(x+5)=74.
\]
Distribute:
\[
2x+2x+10=74.
\]
Solve:
\[
4x=64,\qquad x=16.
\]

Common mistake: defining the variable but not translating every part of the story.

[[check:Three consecutive integers start with \(n\). What are the next two?|n+1 and n+2;;n+1,n+2|Consecutive integers increase by 1 each time.]]
            """,
        ),
        (
            "8. Absolute Value Equations",
            r"""
Absolute value means distance from zero, so it cannot be negative. Most absolute value equations split into two cases.

Example 1:
\[
|x-5|=12.
\]
Two cases:
\[
x-5=12 \quad \text{or} \quad x-5=-12.
\]
Solve:
\[
x=17 \quad \text{or} \quad x=-7.
\]

Example 2:
\[
|2x+1|=9.
\]
Two cases:
\[
2x+1=9 \quad \text{or} \quad 2x+1=-9.
\]
Solve:
\[
2x=8 \Rightarrow x=4,
\]
or
\[
2x=-10 \Rightarrow x=-5.
\]

Example 3:
\[
|x-4|=-3.
\]
No solution, because absolute value cannot equal a negative number.

Check absolute value answers in the original equation. It is easy to drop one of the two cases.

Common mistake: giving only the positive case. Distance 12 can mean 12 units to the right or 12 units to the left.

[[check:Can an absolute value equal \(-3\)?|no;;no solution|Absolute value is a distance, so it cannot be negative.]]
            """,
        ),
        (
            "9. Proportions and Rational Equations",
            r"""
A **proportion** says two ratios are equal. You can often cross-multiply.

Example 1:
\[
\frac{x}{12}=\frac{5}{8}.
\]
Cross-multiply:
\[
8x=60.
\]
Divide:
\[
x=\frac{60}{8}=\frac{15}{2}=7.5.
\]

Example 2:
\[
\frac{x+2}{5}=\frac{6}{10}.
\]
Cross-multiply:
\[
10(x+2)=30.
\]
Divide by 10:
\[
x+2=3.
\]
So:
\[
x=1.
\]

Example 3:
\[
\frac{x-1}{x+2}=2.
\]
Multiply both sides by \(x+2\):
\[
x-1=2(x+2).
\]
Distribute:
\[
x-1=2x+4.
\]
Solve:
\[
x=-5.
\]
Check that the denominator is not zero. Here \(x+2=-3\), so it is allowed.

Common mistake: forgetting to check denominator restrictions. A value that makes a denominator zero cannot be a solution.

[[check:In \(\frac{x-1}{x+2}\), what value is not allowed?| -2;;-2|The denominator \(x+2\) cannot equal zero.]]
            """,
        ),
        (
            "10. Quadratic Equations",
            r"""
A **quadratic equation** has an \(x^2\) term. Many GED-level quadratics can be solved by factoring or square roots.

Example 1:
\[
x^2=49.
\]
Take the square root of both sides:
\[
x=7 \quad \text{or} \quad x=-7.
\]

Example 2:
\[
x^2-9=0.
\]
Add 9:
\[
x^2=9.
\]
So:
\[
x=3 \quad \text{or} \quad x=-3.
\]

Example 3:
\[
x^2+5x+6=0.
\]
Factor:
\[
(x+2)(x+3)=0.
\]
Set each factor equal to zero:
\[
x=-2 \quad \text{or} \quad x=-3.
\]

Example 4:
\[
x^2=5x.
\]
Move all terms to one side:
\[
x^2-5x=0.
\]
Factor:
\[
x(x-5)=0.
\]
So:
\[
x=0 \quad \text{or} \quad x=5.
\]

Common mistake: dividing both sides by \(x\) in \(x^2=5x\). That loses the solution \(x=0\). Move all terms to one side and factor.

[[figure:parabola|Quadratic solutions are the x-values where the parabola crosses the x-axis.]]

[[check:Solve \(x^2=16\).|4 and -4;;-4 and 4;;x=4 or x=-4|Both positive and negative 4 square to 16.]]
            """,
        ),
        (
            "11. Systems as Advanced Equations",
            r"""
A **system of equations** asks for values that make two equations true at the same time.

Example 1 - substitution:
\[
y=2x+1,\qquad y=x+6.
\]
Set the two expressions for \(y\) equal:
\[
2x+1=x+6.
\]
Subtract \(x\):
\[
x+1=6.
\]
Subtract 1:
\[
x=5.
\]
Then:
\[
y=2(5)+1=11.
\]
Solution: \((5,11)\).

Example 2 - elimination:
\[
x+y=18,\qquad x-y=4.
\]
Add the equations:
\[
2x=22.
\]
So:
\[
x=11.
\]
Substitute:
\[
11+y=18,\qquad y=7.
\]

Example 3:
\[
3x+2y=16,\qquad x-y=2.
\]
From the second equation, \(x=y+2\). Substitute:
\[
3(y+2)+2y=16.
\]
Simplify:
\[
5y+6=16.
\]
So:
\[
y=2,\qquad x=4.
\]

Common mistake: stopping after finding one variable. A system solution is usually an ordered pair.

[[check:If \(x=5\) and \(y=2x+1\), what is \(y\)?|11|Substitute: \(2(5)+1=11\).]]
            """,
        ),
        (
            "12. Radical and Exponential Equations",
            r"""
Some advanced equations use square roots, cubes, or exponents. The same inverse-operation idea still works.

Example 1:
\[
\sqrt{x+5}=4.
\]
Square both sides:
\[
x+5=16.
\]
Subtract 5:
\[
x=11.
\]
Check:
\[
\sqrt{11+5}=\sqrt{16}=4.
\]

Example 2:
\[
\sqrt{2x-1}=5.
\]
Square both sides:
\[
2x-1=25.
\]
Add 1:
\[
2x=26.
\]
Divide:
\[
x=13.
\]

Example 3:
\[
2^x=16.
\]
Rewrite 16 as a power of 2:
\[
16=2^4.
\]
So:
\[
x=4.
\]

Example 4:
\[
x^3=27.
\]
Take the cube root:
\[
x=3.
\]

Check radical equations because squaring can sometimes create an answer that does not work in the original.

Common mistake: squaring only part of a side. If \(\sqrt{x+5}=4\), the whole left side is squared, giving \(x+5\), not \(x^2+5\).

[[check:Solve \(\sqrt{x+5}=4\).|11|Square both sides, then subtract 5.]]
            """,
        ),
    ],
    "mcqs": [
        item(r"Solve for \(x\): \(4(2x-3)+5=37\).", r"\(x=\frac{11}{2}\)", [r"\(x=5\)", r"\(x=4\)", r"\(x=\frac{37}{8}\)"], [r"Distribute \(4\) to get \(8x-12+5=37\).", r"Combine constants: \(8x-7=37\).", r"Add 7 to get \(8x=44\), then divide by 8: \(x=\frac{11}{2}\).", r"Check: \(4(11-3)+5=4(8)+5=37\)."], r"stopping at \(8x=44\) or rounding \(5.5\) incorrectly.", 3),
        item(r"Solve for \(x\): \(3(2x+5)-4(x-1)=29\).", r"\(x=5\)", [r"\(x=7\)", r"\(x=10\)", r"\(x=4\)"], [r"Distribute both parts: \(6x+15-4x+4=29\).", r"Combine like terms: \(2x+19=29\).", r"Subtract 19 to get \(2x=10\), then divide by 2: \(x=5\).", r"Check: \(3(15)-4(4)=45-16=29\)."], r"forgetting that \(-4(x-1)\) becomes \(-4x+4\), not \(-4x-4\).", 3),
        item(r"Solve for \(x\): \(5-(2x-7)=18\).", r"\(x=-3\)", [r"\(x=3\)", r"\(x=-5\)", r"\(x=10\)"], [r"Distribute the minus sign: \(5-2x+7=18\).", r"Combine constants: \(12-2x=18\).", r"Subtract 12: \(-2x=6\), then divide by \(-2\): \(x=-3\).", r"Check: \(5-(2(-3)-7)=5-(-13)=18\)."], r"changing only the first sign inside the parentheses.", 3),
        item(r"Solve for \(x\): \(2[3x-(x+4)]=16\).", r"\(x=6\)", [r"\(x=4\)", r"\(x=8\)", r"\(x=10\)"], [r"Simplify inside the brackets: \(3x-(x+4)=3x-x-4=2x-4\).", r"Multiply by 2: \(2(2x-4)=16\), so \(4x-8=16\).", r"Add 8 to get \(4x=24\), then divide by 4: \(x=6\).", r"Check: \(2[18-(10)]=2(8)=16\)."], r"forgetting to distribute the minus sign to the \(+4\).", 3),
        item(r"Solve for \(x\): \(7x-2(3x+5)=12\).", r"\(x=22\)", [r"\(x=2\)", r"\(x=12\)", r"\(x=-22\)"], [r"Distribute \(-2\): \(7x-6x-10=12\).", r"Combine like terms: \(x-10=12\).", r"Add 10 to both sides: \(x=22\).", r"Check: \(7(22)-2(66+5)=154-142=12\)."], r"turning \(-2(3x+5)\) into \(-6x+10\) instead of \(-6x-10\).", 3),
        item(r"Solve for \(x\): \(0.25(8x-4)=9\).", r"\(x=5\)", [r"\(x=4\)", r"\(x=9\)", r"\(x=40\)"], [r"Distribute \(0.25\): \(2x-1=9\).", r"Add 1 to both sides: \(2x=10\).", r"Divide by 2: \(x=5\).", r"Check: \(0.25(40-4)=0.25(36)=9\)."], r"multiplying \(0.25\) by \(8x\) correctly but forgetting \(0.25\cdot(-4)=-1\).", 2),
        item(r"Solve for \(x\): \(\frac{x}{2}+\frac{x}{3}=10\).", r"\(x=12\)", [r"\(x=5\)", r"\(x=60\)", r"\(x=6\)"], [r"Use LCD 6 and multiply every term by 6.", r"The equation becomes \(3x+2x=60\).", r"Combine: \(5x=60\), then divide by 5: \(x=12\).", r"Check: \(12/2+12/3=6+4=10\)."], r"adding denominators and treating the left side as \(\frac{2x}{5}\).", 3),
        item(r"Solve for \(x\): \(\frac{x+1}{3}+\frac{x-2}{2}=7\).", r"\(x=\frac{46}{5}\)", [r"\(x=9\)", r"\(x=\frac{42}{5}\)", r"\(x=10\)"], [r"Use LCD 6 and multiply every term by 6.", r"You get \(2(x+1)+3(x-2)=42\).", r"Distribute and combine: \(2x+2+3x-6=42\), so \(5x-4=42\).", r"Add 4 and divide by 5: \(x=\frac{46}{5}\)."], r"forgetting to multiply the right side \(7\) by 6.", 3),
        item(r"Solve for \(x\): \(\frac{2x-1}{5}=\frac{x+4}{3}\).", r"\(x=23\)", [r"\(x=17\)", r"\(x=-23\)", r"\(x=20\)"], [r"Cross-multiply: \(3(2x-1)=5(x+4)\).", r"Distribute: \(6x-3=5x+20\).", r"Subtract \(5x\): \(x-3=20\).", r"Add 3: \(x=23\)."], r"cross-multiplying as \(3(2x)-1=5x+4\) and not multiplying the whole numerator.", 3),
        item(r"Solve for \(x\): \(\frac{x}{4}-\frac{x}{6}=5\).", r"\(x=60\)", [r"\(x=10\)", r"\(x=30\)", r"\(x=12\)"], [r"Use LCD 12 and multiply every term by 12.", r"The equation becomes \(3x-2x=60\).", r"Combine: \(x=60\).", r"Check: \(60/4-60/6=15-10=5\)."], r"subtracting the denominators and writing \(\frac{x}{2}=5\).", 3),
        item(r"Solve for \(x\): \(\frac{3x+2}{4}-\frac{x-1}{2}=5\).", r"\(x=16\)", [r"\(x=20\)", r"\(x=8\)", r"\(x=4\)"], [r"Use LCD 4 and multiply every term by 4.", r"You get \((3x+2)-2(x-1)=20\).", r"Distribute the \(-2\): \(3x+2-2x+2=20\), so \(x+4=20\).", r"Subtract 4: \(x=16\)."], r"turning \(-2(x-1)\) into \(-2x-2\) instead of \(-2x+2\).", 3),
        item(r"Solve for \(x\): \(5-\frac{x-3}{4}=2\).", r"\(x=15\)", [r"\(x=9\)", r"\(x=5\)", r"\(x=-15\)"], [r"Subtract 5 from both sides: \(-\frac{x-3}{4}=-3\).", r"Multiply both sides by 4: \(-(x-3)=-12\).", r"Multiply by \(-1\): \(x-3=12\).", r"Add 3: \(x=15\)."], r"missing the negative sign in front of the fraction.", 3),
        item(r"Solve for \(x\): \(4(2x-3)=5x+15\).", r"\(x=9\)", [r"\(x=3\)", r"\(x=27\)", r"\(x=6\)"], [r"Distribute: \(8x-12=5x+15\).", r"Subtract \(5x\): \(3x-12=15\).", r"Add 12: \(3x=27\).", r"Divide by 3: \(x=9\)."], r"subtracting 12 from 15 instead of adding 12 to both sides.", 3),
        item(r"Solve: \(6x+7=2(3x+5)-3\).", "Infinitely many solutions", ["No solution", r"\(x=0\)", r"\(x=7\)"], [r"Simplify the right side: \(2(3x+5)-3=6x+10-3=6x+7\).", r"The equation is \(6x+7=6x+7\).", r"Subtract \(6x\) from both sides to get \(7=7\).", r"A true statement means every value of \(x\) works."], r"choosing \(x=0\) just because zero works; all values work.", 3),
        item(r"Solve: \(9x-4=9x+8\).", "No solution", [r"\(x=12\)", "Infinitely many solutions", r"\(x=0\)"], [r"Subtract \(9x\) from both sides.", r"The equation becomes \(-4=8\).", r"This statement is false.", r"Therefore no value of \(x\) can solve the equation."], r"thinking a disappeared variable always means infinitely many solutions; the final statement must be true.", 3),
        item(r"Solve: \(3(x-2)+4=2(x+5)+x-12\).", "Infinitely many solutions", ["No solution", r"\(x=2\)", r"\(x=-2\)"], [r"Simplify the left side: \(3x-6+4=3x-2\).", r"Simplify the right side: \(2x+10+x-12=3x-2\).", r"The equation becomes \(3x-2=3x-2\).", r"This identity is always true, so there are infinitely many solutions."], r"stopping when the variable disappears without checking whether the remaining statement is true.", 3),
        item(r"Solve for \(x\): \(5(x+1)-2=3x+17\).", r"\(x=7\)", [r"\(x=5\)", r"\(x=10\)", r"\(x=-7\)"], [r"Distribute and combine on the left: \(5x+5-2=5x+3\).", r"Set up \(5x+3=3x+17\).", r"Subtract \(3x\): \(2x+3=17\).", r"Subtract 3 and divide by 2: \(x=7\)."], r"forgetting to combine \(+5-2\) before moving terms.", 3),
        item(r"Solve: \(2(4x-1)-3x=5(x+6)-32\).", "Infinitely many solutions", ["No solution", r"\(x=0\)", r"\(x=2\)"], [r"Simplify the left side: \(8x-2-3x=5x-2\).", r"Simplify the right side: \(5x+30-32=5x-2\).", r"The equation becomes \(5x-2=5x-2\).", r"This is always true, so every value of \(x\) works."], r"reporting only one example value instead of recognizing all values work.", 3),
        item(r"Solve \(ax+b=c\) for \(x\).", r"\(x=\frac{c-b}{a}\)", [r"\(x=\frac{c+b}{a}\)", r"\(x=a(c-b)\)", r"\(x=c-ab\)"], [r"Start with \(ax+b=c\).", r"Subtract \(b\) from both sides: \(ax=c-b\).", r"Divide both sides by \(a\): \(x=\frac{c-b}{a}\).", r"This isolates \(x\) completely."], r"adding \(b\) instead of subtracting it.", 3),
        item(r"The formula \(A=\frac{1}{2}bh\) gives triangle area. Solve for \(h\).", r"\(h=\frac{2A}{b}\)", [r"\(h=\frac{A}{2b}\)", r"\(h=2Ab\)", r"\(h=\frac{b}{2A}\)"], [r"Start with \(A=\frac{1}{2}bh\).", r"Multiply both sides by 2: \(2A=bh\).", r"Divide both sides by \(b\): \(h=\frac{2A}{b}\).", r"The target variable \(h\) is now alone."], r"dividing by 2 again instead of undoing the one-half by multiplying by 2.", 3),
        item(r"The formula \(V=\pi r^2h\) gives cylinder volume. Solve for \(h\).", r"\(h=\frac{V}{\pi r^2}\)", [r"\(h=V\pi r^2\)", r"\(h=\frac{\pi r^2}{V}\)", r"\(h=\frac{V}{2\pi r}\)"], [r"Identify the target \(h\).", r"In \(V=\pi r^2h\), \(h\) is multiplied by \(\pi r^2\).", r"Divide both sides by \(\pi r^2\).", r"The result is \(h=\frac{V}{\pi r^2}\)."], r"dividing by circumference \(2\pi r\) instead of the base area \(\pi r^2\).", 3),
        item(r"Solve \(C=\frac{5}{9}(F-32)\) for \(F\).", r"\(F=\frac{9}{5}C+32\)", [r"\(F=\frac{5}{9}C+32\)", r"\(F=\frac{9}{5}(C+32)\)", r"\(F=C-32\)"], [r"Multiply both sides by \(\frac{9}{5}\): \(\frac{9}{5}C=F-32\).", r"Add 32 to both sides.", r"The result is \(F=\frac{9}{5}C+32\).", r"Check the structure: multiply first, then add 32."], r"adding 32 inside the multiplication instead of after isolating \(F-32\).", 3),
        item(r"Solve \(y=mx+b\) for \(m\).", r"\(m=\frac{y-b}{x}\)", [r"\(m=\frac{y+b}{x}\)", r"\(m=\frac{x}{y-b}\)", r"\(m=y-bx\)"], [r"Subtract \(b\) from both sides: \(y-b=mx\).", r"Divide both sides by \(x\).", r"The result is \(m=\frac{y-b}{x}\).", r"This works when \(x\ne0\)."], r"forgetting to subtract \(b\) before dividing by \(x\).", 3),
        item(r"Solve \(P=2l+2w\) for \(w\).", r"\(w=\frac{P-2l}{2}\)", [r"\(w=P-2l\)", r"\(w=\frac{P}{2}-2l\)", r"\(w=2P-2l\)"], [r"Subtract \(2l\) from both sides: \(P-2l=2w\).", r"Divide the entire left side by 2.", r"The result is \(w=\frac{P-2l}{2}\).", r"Keep the numerator grouped because both terms are divided by 2."], r"dividing only \(P\) by 2 and not the whole expression \(P-2l\).", 3),
        item(r"A gym charges 40 dollars plus 12 dollars per month. The total is 160 dollars. How many months?", r"\(10\)", [r"\(13\)", r"\(12\)", r"\(120\)"], [r"Let \(m\) be the number of months.", r"Write \(40+12m=160\).", r"Subtract 40: \(12m=120\).", r"Divide by 12: \(m=10\)."], r"dividing 160 by 12 and forgetting the 40 dollar fixed fee.", 2),
        item(r"Plan A costs \(20+5m\). Plan B costs \(50+2m\). For what \(m\) are the costs equal?", r"\(m=10\)", [r"\(m=6\)", r"\(m=30\)", r"\(m=14\)"], [r"Set the two costs equal: \(20+5m=50+2m\).", r"Subtract \(2m\): \(20+3m=50\).", r"Subtract 20: \(3m=30\).", r"Divide by 3: \(m=10\)."], r"setting only the variable parts equal and ignoring the fixed costs.", 3),
        item(r"Three consecutive integers have sum \(75\). What is the largest integer?", r"\(26\)", [r"\(24\)", r"\(25\)", r"\(27\)"], [r"Let the integers be \(n\), \(n+1\), and \(n+2\).", r"Write \(n+(n+1)+(n+2)=75\).", r"Combine: \(3n+3=75\), so \(3n=72\), and \(n=24\).", r"The integers are 24, 25, and 26, so the largest is 26."], r"answering \(24\), which is the first integer, not the largest.", 3),
        item(r"Two consecutive odd integers have sum \(64\). What is the smaller integer?", r"\(31\)", [r"\(32\)", r"\(33\)", r"\(29\)"], [r"Let the smaller odd integer be \(n\).", r"The next consecutive odd integer is \(n+2\).", r"Write \(n+(n+2)=64\), so \(2n+2=64\).", r"Subtract 2 and divide by 2: \(2n=62\), so \(n=31\)."], r"using \(n+1\) instead of \(n+2\) for consecutive odd integers.", 3),
        item(r"A rectangle has width \(x\), length \(x+5\), and perimeter \(74\). What is the width?", r"\(16\)", [r"\(21\)", r"\(18.5\)", r"\(32\)"], [r"Use perimeter: \(2w+2l=74\).", r"Substitute \(w=x\) and \(l=x+5\): \(2x+2(x+5)=74\).", r"Distribute and combine: \(2x+2x+10=74\), so \(4x+10=74\).", r"Subtract 10 and divide by 4: \(x=16\)."], r"forgetting that both length and width appear twice in perimeter.", 3),
        item(r"A triangle has angles \(x\), \(2x\), and \(x+20\). What is \(x\)?", r"\(40\)", [r"\(80\)", r"\(60\)", r"\(30\)"], [r"Triangle angles sum to 180 degrees.", r"Write \(x+2x+(x+20)=180\).", r"Combine: \(4x+20=180\).", r"Subtract 20 and divide by 4: \(x=40\)."], r"answering \(80\), which is the angle \(2x\), not the value of \(x\).", 3),
        item(r"A worker charges 50 dollars plus 18 dollars per hour. The total is 194 dollars. How many hours?", r"\(8\)", [r"\(10.8\)", r"\(11\)", r"\(144\)"], [r"Let \(h\) be the hours.", r"Write \(50+18h=194\).", r"Subtract 50: \(18h=144\).", r"Divide by 18: \(h=8\)."], r"dividing 194 by 18 and ignoring the starting fee.", 2),
        item(r"A car rental costs 30 dollars plus 0.20 dollars per mile. The total is 90 dollars. How many miles?", r"\(300\)", [r"\(450\)", r"\(60\)", r"\(120\)"], [r"Let \(m\) be miles.", r"Write \(30+0.20m=90\).", r"Subtract 30: \(0.20m=60\).", r"Divide by 0.20: \(m=300\)."], r"stopping at 60, which is the variable cost, not the number of miles.", 3),
        item(r"A sale price is 85 percent of the original price. If the sale price is 170 dollars, what was the original price?", r"\(200\) dollars", [r"\(144.50\) dollars", r"\(255\) dollars", r"\(185\) dollars"], [r"Let \(p\) be the original price.", r"Write \(0.85p=170\).", r"Divide by 0.85: \(p=200\).", r"Check: \(0.85(200)=170\)."], r"finding 85 percent of 170 instead of recognizing 170 is already the sale price.", 3),
        item(r"A price plus 8 percent tax is 54 dollars. What was the price before tax?", r"\(50\) dollars", [r"\(49.68\) dollars", r"\(58.32\) dollars", r"\(46\) dollars"], [r"Let \(p\) be the price before tax.", r"Tax makes the total \(1.08p\), so \(1.08p=54\).", r"Divide by 1.08: \(p=50\).", r"Check: \(50+0.08(50)=50+4=54\)."], r"subtracting 8 dollars instead of 8 percent.", 3),
        item(r"A restaurant total after a 15 percent tip is 92 dollars. What was the bill before tip?", r"\(80\) dollars", [r"\(78.20\) dollars", r"\(106\) dollars", r"\(77\) dollars"], [r"Let \(b\) be the bill before tip.", r"After a 15 percent tip, the total is \(1.15b\).", r"Set \(1.15b=92\).", r"Divide by 1.15 to get \(b=80\)."], r"taking 15 percent of 92 instead of reversing the percent increase.", 3),
        item(r"After a 25 percent increase, a value is 150. What was the original value?", r"\(120\)", [r"\(125\)", r"\(187.5\)", r"\(100\)"], [r"Let \(x\) be the original value.", r"A 25 percent increase means \(1.25x=150\).", r"Divide by 1.25: \(x=120\).", r"Check: \(120+0.25(120)=150\)."], r"subtracting 25 from 150 instead of reversing a 25 percent increase.", 3),
        item(r"Solve: absolute value of \(x-5\) equals \(12\).", r"\(x=17\) or \(x=-7\)", [r"\(x=17\) only", r"\(x=7\) or \(x=-17\)", "No solution"], [r"Set up two cases: \(x-5=12\) or \(x-5=-12\).", r"First case: \(x=17\).", r"Second case: \(x=-7\).", r"Both check because both are 12 units from 5."], r"giving only the positive case.", 3),
        item(r"Solve: absolute value of \(2x+1\) equals \(9\).", r"\(x=4\) or \(x=-5\)", [r"\(x=4\) only", r"\(x=5\) or \(x=-4\)", "No solution"], [r"Set up \(2x+1=9\) or \(2x+1=-9\).", r"First case: \(2x=8\), so \(x=4\).", r"Second case: \(2x=-10\), so \(x=-5\).", r"Check: both make the absolute value equal 9."], r"forgetting the negative case.", 3),
        item(r"Solve: absolute value of \(x+3\), plus 2, equals \(10\).", r"\(x=5\) or \(x=-11\)", [r"\(x=5\) only", r"\(x=7\) or \(x=-13\)", "No solution"], [r"Subtract 2 first: absolute value of \(x+3\) equals 8.", r"Set up \(x+3=8\) or \(x+3=-8\).", r"Solve to get \(x=5\) or \(x=-11\).", r"Check: both make the absolute value 8, then adding 2 gives 10."], r"splitting before isolating the absolute value expression.", 3),
        item(r"Solve: absolute value of \(3x-6\) equals \(0\).", r"\(x=2\)", [r"\(x=2\) or \(x=-2\)", "No solution", r"\(x=0\)"], [r"An absolute value equals 0 only when the inside equals 0.", r"Set \(3x-6=0\).", r"Add 6: \(3x=6\).", r"Divide by 3: \(x=2\)."], r"creating two cases even though positive zero and negative zero are the same case.", 3),
        item(r"Solve: absolute value of \(x-4\) equals \(-3\).", "No solution", [r"\(x=1\) or \(x=7\)", r"\(x=-7\)", r"\(x=4\)"], [r"Notice the right side is negative.", r"Absolute value represents distance, so it cannot be negative.", r"Therefore the equation has no solution.", r"No algebraic split is needed."], r"solving \(x-4=3\) and \(x-4=-3\) even though the original equals \(-3\).", 3),
        item(r"Solve the proportion \(\frac{x}{12}=\frac{5}{8}\).", r"\(x=\frac{15}{2}\)", [r"\(x=\frac{10}{3}\)", r"\(x=20\)", r"\(x=7\)"], [r"Cross-multiply: \(8x=12\cdot5\).", r"Simplify: \(8x=60\).", r"Divide by 8: \(x=\frac{60}{8}=\frac{15}{2}\).", r"As a decimal, this is 7.5."], r"dividing 12 by 8 and then multiplying incorrectly.", 3),
        item(r"Solve the proportion \(\frac{x+2}{5}=\frac{6}{10}\).", r"\(x=1\)", [r"\(x=3\)", r"\(x=4\)", r"\(x=-1\)"], [r"Cross-multiply: \(10(x+2)=5\cdot6\).", r"Simplify: \(10x+20=30\).", r"Subtract 20: \(10x=10\).", r"Divide by 10: \(x=1\)."], r"forgetting to subtract 2 after finding \(x+2=3\).", 3),
        item(r"Solve: \(\frac{6}{x+1}=2\).", r"\(x=2\)", [r"\(x=3\)", r"\(x=-1\)", r"\(x=12\)"], [r"Multiply both sides by \(x+1\): \(6=2(x+1)\).", r"Distribute: \(6=2x+2\).", r"Subtract 2: \(4=2x\).", r"Divide by 2: \(x=2\), and \(x+1\ne0\), so it is valid."], r"choosing \(x=-1\), which would make the denominator zero.", 3),
        item(r"Solve: \(\frac{x-1}{x+2}=2\).", r"\(x=-5\)", [r"\(x=5\)", r"\(x=-2\)", r"\(x=3\)"], [r"Multiply both sides by \(x+2\): \(x-1=2(x+2)\).", r"Distribute: \(x-1=2x+4\).", r"Subtract \(x\): \(-1=x+4\).", r"Subtract 4: \(x=-5\). Check denominator: \(-5+2=-3\), so it is valid."], r"using \(x=-2\), which is not allowed because it makes the denominator zero.", 3),
        item(r"Solve: \(\frac{4}{x-3}=1\).", r"\(x=7\)", [r"\(x=4\)", r"\(x=3\)", r"\(x=1\)"], [r"Multiply both sides by \(x-3\): \(4=x-3\).", r"Add 3 to both sides.", r"The result is \(x=7\).", r"Check: \(4/(7-3)=4/4=1\)."], r"choosing \(x=3\), which makes the denominator zero.", 3),
        item(r"Solve: \(x^2=49\).", r"\(x=7\) or \(x=-7\)", [r"\(x=7\) only", r"\(x=24.5\)", r"\(x=49\)"], [r"Take the square root of both sides.", r"The square root of 49 is 7.", r"Include both signs: \(x=7\) or \(x=-7\).", r"Check: both \(7^2\) and \((-7)^2\) equal 49."], r"forgetting the negative square-root solution.", 3),
        item(r"Solve: \(x^2-9=0\).", r"\(x=3\) or \(x=-3\)", [r"\(x=3\) only", r"\(x=9\)", r"\(x=-9\)"], [r"Add 9 to both sides: \(x^2=9\).", r"Take square roots.", r"\(x=3\) or \(x=-3\).", r"Both values make \(x^2-9=0\)."], r"giving only \(x=3\).", 3),
        item(r"Solve: \(x^2+5x+6=0\).", r"\(x=-2\) or \(x=-3\)", [r"\(x=2\) or \(x=3\)", r"\(x=-6\) or \(x=-1\)", r"\(x=6\)"], [r"Factor the trinomial: \(x^2+5x+6=(x+2)(x+3)\).", r"Set each factor equal to zero.", r"\(x+2=0\) gives \(x=-2\); \(x+3=0\) gives \(x=-3\).", r"Check: both values make the product zero."], r"using the factor numbers 2 and 3 as positive solutions instead of changing their signs.", 3),
        item(r"Solve: \(x^2-7x+10=0\).", r"\(x=2\) or \(x=5\)", [r"\(x=-2\) or \(x=-5\)", r"\(x=1\) or \(x=10\)", r"\(x=7\)"], [r"Find numbers that multiply to 10 and add to \(-7\): \(-2\) and \(-5\).", r"Factor: \((x-2)(x-5)=0\).", r"Set each factor to zero.", r"The solutions are \(x=2\) and \(x=5\)."], r"reporting the factor signs \(-2\) and \(-5\) as the solutions.", 3),
        item(r"Solve: \(x^2=5x\).", r"\(x=0\) or \(x=5\)", [r"\(x=5\) only", r"\(x=0\) only", r"\(x=-5\)"], [r"Move all terms to one side: \(x^2-5x=0\).", r"Factor: \(x(x-5)=0\).", r"Set each factor to zero: \(x=0\) or \(x-5=0\).", r"The solutions are \(x=0\) or \(x=5\)."], r"dividing both sides by \(x\), which loses the solution \(x=0\).", 3),
        item(r"Solve: \(x^2-16=0\).", r"\(x=4\) or \(x=-4\)", [r"\(x=4\) only", r"\(x=16\)", r"\(x=-16\)"], [r"Add 16 to both sides: \(x^2=16\).", r"Take square roots.", r"The solutions are \(x=4\) and \(x=-4\).", r"Check: both square to 16."], r"forgetting that negative 4 also squares to 16.", 3),
        item(r"Solve the system: \(y=2x+1\) and \(y=x+6\). What is \(x\)?", r"\(x=5\)", [r"\(x=11\)", r"\(x=6\)", r"\(x=1\)"], [r"Both expressions equal \(y\), so set them equal: \(2x+1=x+6\).", r"Subtract \(x\): \(x+1=6\).", r"Subtract 1: \(x=5\).", r"Then \(y=11\), but the question asks for \(x\)."], r"answering \(11\), which is \(y\), not \(x\).", 3),
        item(r"Solve the system: \(x+y=18\) and \(x-y=4\). What is \(x\)?", r"\(x=11\)", [r"\(x=7\)", r"\(x=14\)", r"\(x=22\)"], [r"Add the two equations to eliminate \(y\).", r"\((x+y)+(x-y)=18+4\), so \(2x=22\).", r"Divide by 2: \(x=11\).", r"Check with \(y=7\): \(11+7=18\) and \(11-7=4\)."], r"answering \(7\), which is \(y\).", 3),
        item(r"Solve the system: \(2x+3y=21\) and \(x=3\). What is \(y\)?", r"\(y=5\)", [r"\(y=3\)", r"\(y=9\)", r"\(y=7\)"], [r"Substitute \(x=3\) into \(2x+3y=21\).", r"You get \(2(3)+3y=21\), so \(6+3y=21\).", r"Subtract 6: \(3y=15\).", r"Divide by 3: \(y=5\)."], r"forgetting to multiply \(2(3)\) before subtracting.", 2),
        item(r"Solve the system: \(3x+2y=16\) and \(x-y=2\). What is \(x\)?", r"\(x=4\)", [r"\(x=2\)", r"\(x=6\)", r"\(x=8\)"], [r"From \(x-y=2\), solve for \(x\): \(x=y+2\).", r"Substitute into \(3x+2y=16\): \(3(y+2)+2y=16\).", r"Simplify: \(5y+6=16\), so \(5y=10\), and \(y=2\).", r"Then \(x=y+2=4\)."], r"stopping at \(y=2\) when the question asks for \(x\).", 3),
        item(r"Solve: \(\sqrt{x+5}=4\).", r"\(x=11\)", [r"\(x=16\)", r"\(x=21\)", r"\(x=-11\)"], [r"Square both sides to undo the square root.", r"\(x+5=16\).", r"Subtract 5 from both sides: \(x=11\).", r"Check: \(\sqrt{11+5}=\sqrt{16}=4\)."], r"squaring \(x\) separately and writing \(x^2+5=16\).", 3),
        item(r"Solve: \(\sqrt{2x-1}=5\).", r"\(x=13\)", [r"\(x=12\)", r"\(x=26\)", r"\(x=3\)"], [r"Square both sides: \(2x-1=25\).", r"Add 1: \(2x=26\).", r"Divide by 2: \(x=13\).", r"Check: \(\sqrt{2(13)-1}=\sqrt{25}=5\)."], r"forgetting to add 1 before dividing by 2.", 3),
        item(r"Solve: \(2^x=16\).", r"\(x=4\)", [r"\(x=8\)", r"\(x=14\)", r"\(x=2\)"], [r"Rewrite 16 as a power of 2.", r"\(16=2^4\).", r"So \(2^x=2^4\).", r"Therefore \(x=4\)."], r"dividing 16 by 2 instead of matching powers.", 3),
        item(r"Solve: \(x^3=27\).", r"\(x=3\)", [r"\(x=9\)", r"\(x=-3\)", r"\(x=24\)"], [r"Use the inverse of cubing: take the cube root.", r"\(\sqrt[3]{27}=3\).", r"So \(x=3\).", r"Check: \(3^3=27\)."], r"using square roots instead of cube roots.", 3),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Advanced Equations & Applications course (MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()
        course = Course.objects.create(
            title=COURSE["title"],
            slug=COURSE["slug"],
            program=COURSE["program"],
            subject=COURSE["subject"],
            description=COURSE["description"],
        )

        for index, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content.strip(), order=index)

        for question_data in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course,
                qtype="mcq",
                text=question_data["text"],
                difficulty=question_data["difficulty"],
                explanation=question_data["explanation"],
            )
            for text, is_correct in question_data["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=is_correct)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
