"""
Seed a focused GED Algebra course on equations.

This course is intentionally narrower and more detailed than the broad Algebra
In Depth course. It gives students many worked examples, then uses step-by-step
MCQ explanations so missed questions become mini-lessons.

Run:
    python manage.py seed_ged_algebra_equations
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Algebra: Equations Mastery",
    "slug": "ged-algebra-equations-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Algebra course for mastering equations. Students learn how an "
        "equation works like a balance, solve one-step, two-step, multi-step, "
        "fraction, decimal, and variable-on-both-sides equations, rearrange formulas, "
        "translate word problems into equations, and recognize no-solution and "
        "infinitely-many-solution cases. Lessons include many worked examples, and "
        "practice questions use detailed step-by-step explanations."
    ),
    "lessons": [
        (
            "1. Equations as a Balance",
            r"""
An **equation** says two expressions are equal. The equals sign is not an instruction to "get an answer"; it is a balance point. Whatever is on the left must have the same value as whatever is on the right.

[[figure:equation_balance|Solving equations means keeping both sides balanced while isolating the unknown.]]

The golden rule:
- Whatever you do to one side, you must do to the other side.
- Use **inverse operations** to undo what is happening to the variable.

Inverse pairs:
- Addition and subtraction undo each other.
- Multiplication and division undo each other.
- Squaring and square roots undo each other.

Example 1:
\[
x + 6 = 14.
\]
The variable has 6 added to it, so subtract 6 from both sides:
\[
x + 6 - 6 = 14 - 6,\qquad x = 8.
\]

Example 2:
\[
3x = 21.
\]
The variable is multiplied by 3, so divide both sides by 3:
\[
\frac{3x}{3} = \frac{21}{3},\qquad x = 7.
\]

Always check by substituting the answer back into the original equation. If the two sides match, the solution works.

Common mistake: doing a different operation on each side. That breaks the balance and changes the equation.

[[check:What must you do to both sides of an equation to keep it balanced?|the same thing;;same operation;;same|Both sides must receive the same operation.]]
            """,
        ),
        (
            "2. One-Step Equations",
            r"""
A **one-step equation** needs one inverse operation to isolate the variable.

Example 1 - addition:
\[
x + 9 = 22.
\]
Undo \(+9\) by subtracting 9:
\[
x = 22 - 9 = 13.
\]

Example 2 - subtraction:
\[
x - 5 = 18.
\]
Undo \(-5\) by adding 5:
\[
x = 18 + 5 = 23.
\]

Example 3 - multiplication:
\[
4x = 36.
\]
Undo multiplication by 4 by dividing by 4:
\[
x = 9.
\]

Example 4 - division:
\[
\frac{x}{6} = 7.
\]
Undo division by 6 by multiplying by 6:
\[
x = 42.
\]

If the coefficient is negative, keep the sign with the number:
\[
-3x = 24 \Rightarrow x = -8.
\]

Common mistake: changing the sign of the answer without a reason. A negative coefficient divided into a positive number gives a negative answer.

[[check:Solve \(x - 8 = 15\).|23|Add 8 to both sides.]]
            """,
        ),
        (
            "3. Two-Step Equations",
            r"""
A **two-step equation** usually has a variable term plus or minus a constant:
\[
ax + b = c.
\]

Solve by undoing operations in reverse order:
- First undo addition or subtraction.
- Then undo multiplication or division.

Example 1:
\[
2x + 5 = 17.
\]
Step 1: subtract 5 from both sides:
\[
2x = 12.
\]
Step 2: divide both sides by 2:
\[
x = 6.
\]
Check:
\[
2(6)+5=12+5=17.
\]

Example 2:
\[
3x - 4 = 20.
\]
Add 4, then divide by 3:
\[
3x = 24,\qquad x = 8.
\]

Example 3:
\[
-2x + 7 = 15.
\]
Subtract 7:
\[
-2x = 8.
\]
Divide by \(-2\):
\[
x = -4.
\]

Common mistake: dividing before removing the constant. In \(2x+5=17\), you cannot divide only the \(2x\) by 2 and leave the \(+5\) alone unless you divide the entire side.

[[check:Solve \(3x + 2 = 20\).|6|Subtract 2, then divide by 3.]]
            """,
        ),
        (
            "4. Multi-Step Equations: Combine and Distribute",
            r"""
Multi-step equations are not harder because of new rules. They are harder because the equation needs cleaning first.

Use this order:
- Distribute if there are parentheses.
- Combine like terms on each side.
- Move constants and variables using inverse operations.
- Divide by the coefficient.
- Check.

Example 1:
\[
3(x+2)=21.
\]
Distribute:
\[
3x+6=21.
\]
Subtract 6:
\[
3x=15.
\]
Divide by 3:
\[
x=5.
\]

Example 2:
\[
2(x-4)+5=15.
\]
Distribute:
\[
2x-8+5=15.
\]
Combine constants:
\[
2x-3=15.
\]
Add 3:
\[
2x=18.
\]
Divide by 2:
\[
x=9.
\]

Example 3:
\[
4x+3x-5=30.
\]
Combine like terms:
\[
7x-5=30.
\]
Add 5:
\[
7x=35.
\]
Divide by 7:
\[
x=5.
\]

Common mistake: distributing to only the first term. \(3(x+2)\) is \(3x+6\), not \(3x+2\).

[[check:Solve \(4(x+1)=20\).|4|Distribute or divide first: \(x+1=5\), so \(x=4\).]]
            """,
        ),
        (
            "5. Variables on Both Sides",
            r"""
Some equations have \(x\) on both sides. The goal is to collect all variable terms on one side and all constants on the other.

Example 1:
\[
5x - 3 = 2x + 12.
\]
Subtract \(2x\) from both sides:
\[
3x - 3 = 12.
\]
Add 3:
\[
3x = 15.
\]
Divide by 3:
\[
x = 5.
\]

Example 2:
\[
4x + 9 = 6x - 5.
\]
Subtract \(4x\) from both sides:
\[
9 = 2x - 5.
\]
Add 5:
\[
14 = 2x.
\]
Divide by 2:
\[
x = 7.
\]

Tip: move the smaller variable term to the other side when possible. It often keeps the coefficient positive.

Check Example 2:
\[
4(7)+9=37,\qquad 6(7)-5=37.
\]
Both sides match.

Common mistake: changing signs randomly when "moving" a term. Think of it as doing the inverse operation to both sides.

[[check:Solve \(7x+4=3x+28\).|6|Subtract \(3x\), subtract 4, then divide by 4.]]
            """,
        ),
        (
            "6. Fraction and Decimal Equations",
            r"""
Fractions and decimals are still solved with the same balance rule. The cleanest strategy is often to clear the fraction or decimal early.

Example 1:
\[
\frac{x}{3}+4=10.
\]
Subtract 4:
\[
\frac{x}{3}=6.
\]
Multiply by 3:
\[
x=18.
\]

Example 2:
\[
\frac{2}{5}x = 8.
\]
Divide by \(\frac{2}{5}\), which is the same as multiplying by \(\frac{5}{2}\):
\[
x = 8\cdot \frac{5}{2}=20.
\]

Example 3:
\[
\frac{3x+1}{2}=11.
\]
Multiply both sides by 2:
\[
3x+1=22.
\]
Subtract 1:
\[
3x=21.
\]
Divide by 3:
\[
x=7.
\]

Example 4:
\[
0.2x+4=10.
\]
Subtract 4:
\[
0.2x=6.
\]
Divide by \(0.2\):
\[
x=30.
\]

Common mistake: multiplying only part of a side when clearing fractions. If you multiply by 2, every term on both sides must be multiplied by 2.

[[check:Solve \(\frac{x-2}{4}=5\).|22|Multiply by 4 to get \(x-2=20\), then add 2.]]
            """,
        ),
        (
            "7. Formulas and Literal Equations",
            r"""
A **formula** is an equation with more than one variable. A **literal equation** asks you to solve for one variable in terms of the others.

The same rules apply: isolate the target variable.

Example 1 - rectangle area:
\[
A = lw.
\]
Solve for \(w\). Since \(w\) is multiplied by \(l\), divide both sides by \(l\):
\[
w = \frac{A}{l}.
\]

Example 2 - distance:
\[
d = rt.
\]
Solve for \(t\):
\[
t = \frac{d}{r}.
\]

Example 3 - perimeter of a rectangle:
\[
P = 2l + 2w.
\]
Solve for \(l\). Subtract \(2w\):
\[
P - 2w = 2l.
\]
Divide by 2:
\[
l = \frac{P - 2w}{2}.
\]

Example 4 - line equation:
\[
y = 3x + 2.
\]
If \(y=20\), solve \(20=3x+2\):
\[
18=3x,\qquad x=6.
\]

Common mistake: dividing only one term by 2 in \(P-2w=2l\). The whole expression \(P-2w\) is divided by 2.

[[check:Solve \(d=rt\) for \(t\).|d/r;;\frac{d}{r}|Divide both sides by \(r\).]]
            """,
        ),
        (
            "8. Word Problems: Build the Equation",
            r"""
GED algebra often hides the equation in a real situation. Translate slowly.

Routine:
- Define the variable.
- Write what each part means.
- Build the equation.
- Solve.
- Check whether the answer makes sense in the story.

Example 1:
"A gym charges a 25 dollar sign-up fee plus 8 dollars per class. The total is 89 dollars. How many classes?"

Let \(c\) be the number of classes:
\[
25 + 8c = 89.
\]
Subtract 25:
\[
8c=64.
\]
Divide by 8:
\[
c=8.
\]

Example 2:
"A taxi costs 4 dollars plus 2.50 dollars per mile. The total is 24 dollars. How many miles?"
\[
4 + 2.50m = 24.
\]
Subtract 4:
\[
2.50m=20.
\]
Divide by 2.50:
\[
m=8.
\]

Example 3:
"Three times a number plus 5 is 41."
\[
3x+5=41.
\]
Subtract 5:
\[
3x=36.
\]
Divide by 3:
\[
x=12.
\]

Common mistake: forgetting the fixed starting amount. In the gym example, 25 dollars is charged once, not once per class.

[[check:A plan costs 30 dollars plus 5 dollars per month. Total is 80. What equation finds \(m\)?|30+5m=80;;5m+30=80|Fixed fee plus monthly fee times months equals total.]]
            """,
        ),
        (
            "9. No Solution and Infinitely Many Solutions",
            r"""
Most linear equations have one solution, but sometimes the variable disappears.

Case 1 - no solution:
\[
3x+4=3x+10.
\]
Subtract \(3x\) from both sides:
\[
4=10.
\]
That is false, so there is **no solution**. No value of \(x\) can make the equation true.

Case 2 - infinitely many solutions:
\[
2(x+3)=2x+6.
\]
Distribute:
\[
2x+6=2x+6.
\]
Subtract \(2x\):
\[
6=6.
\]
That is always true, so **every value of \(x\)** works.

How to tell the difference:
- False statement like \(4=10\): no solution.
- True statement like \(6=6\): infinitely many solutions.

Example check:
For \(2(x+3)=2x+6\), try \(x=0\): left \(=6\), right \(=6\). Try \(x=5\): left \(=16\), right \(=16\). Many values work because the two sides are the same expression.

Common mistake: saying \(x=0\) when the variable disappears. If the final statement is true, all values work; if false, none work.

[[check:What does \(5=5\) mean after solving an equation?|infinitely many solutions;;all real numbers;;all values work|A true statement means the two sides were equivalent.]]
            """,
        ),
        (
            "10. Checking and GED Test Strategy",
            r"""
Checking is not extra work; it is how you catch arithmetic mistakes.

For any equation:
- Solve carefully.
- Substitute the answer into the original equation, not a later line.
- Simplify both sides.
- Confirm that left side equals right side.

Example:
\[
4(x-2)=2x+10.
\]
Distribute:
\[
4x-8=2x+10.
\]
Subtract \(2x\):
\[
2x-8=10.
\]
Add 8:
\[
2x=18.
\]
Divide by 2:
\[
x=9.
\]
Check in the original:
\[
4(9-2)=4(7)=28,\qquad 2(9)+10=28.
\]
Correct.

Multiple-choice strategy:
- If answer choices are numbers, you can plug them into the original equation.
- Start with the middle-sized choice when the choices are ordered.
- Eliminate answers that make one side too large or too small.

GED reminder: many questions ask for something after solving. If the problem says "find \(x+3\)" and you found \(x=9\), the answer is \(12\), not \(9\).

Common mistake: checking in a simplified line that already contains your mistake. Always check in the original equation.

[[check:After solving \(x=9\), a question asks for \(x+3\). What is the final answer?|12|Answer the question asked, not just the value of \(x\).]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"Solve for \(x\): \(x+7=19\).",
            "difficulty": 1,
            "choices": [(r"\(x=12\)", True), (r"\(x=26\)", False), (r"\(x=7\)", False), (r"\(x=19\)", False)],
            "explanation": r"Step 1: Identify what is happening to \(x\). The equation is \(x+7=19\), so 7 is being added to \(x\). Step 2: Use the inverse operation, subtract 7 from both sides: \(x+7-7=19-7\). Step 3: Simplify to get \(x=12\). Check: \(12+7=19\), so the answer works. The trap \(26\) adds 7 instead of subtracting it.",
        },
        {
            "text": r"Solve for \(x\): \(x-9=14\).",
            "difficulty": 1,
            "choices": [(r"\(x=23\)", True), (r"\(x=5\)", False), (r"\(x=14\)", False), (r"\(x=-23\)", False)],
            "explanation": r"Step 1: \(x\) has 9 subtracted from it. Step 2: Undo subtraction by adding 9 to both sides: \(x-9+9=14+9\). Step 3: Simplify: \(x=23\). Check: \(23-9=14\). The trap \(5\) subtracts 9 again instead of undoing it.",
        },
        {
            "text": r"Solve for \(x\): \(4x=36\).",
            "difficulty": 1,
            "choices": [(r"\(x=9\)", True), (r"\(x=32\)", False), (r"\(x=40\)", False), (r"\(x=144\)", False)],
            "explanation": r"Step 1: \(4x\) means \(4\) times \(x\). Step 2: Undo multiplication by 4 by dividing both sides by 4: \(\frac{4x}{4}=\frac{36}{4}\). Step 3: Simplify: \(x=9\). Check: \(4(9)=36\). The trap \(144\) multiplies by 4 instead of dividing.",
        },
        {
            "text": r"Solve for \(x\): \(\frac{x}{5}=8\).",
            "difficulty": 1,
            "choices": [(r"\(x=40\)", True), (r"\(x=13\)", False), (r"\(x=\frac{8}{5}\)", False), (r"\(x=3\)", False)],
            "explanation": r"Step 1: \(x\) is divided by 5. Step 2: Undo division by multiplying both sides by 5: \(5\cdot \frac{x}{5}=8\cdot5\). Step 3: Simplify: \(x=40\). Check: \(40/5=8\). The trap \(\frac{8}{5}\) divides again instead of multiplying.",
        },
        {
            "text": r"Solve for \(x\): \(-3x=21\).",
            "difficulty": 1,
            "choices": [(r"\(x=-7\)", True), (r"\(x=7\)", False), (r"\(x=-63\)", False), (r"\(x=18\)", False)],
            "explanation": r"Step 1: The coefficient of \(x\) is \(-3\), so \(x\) is multiplied by \(-3\). Step 2: Divide both sides by \(-3\): \(\frac{-3x}{-3}=\frac{21}{-3}\). Step 3: Simplify: \(x=-7\). Check: \(-3(-7)=21\). The trap \(x=7\) forgets that a positive divided by a negative is negative.",
        },
        {
            "text": r"Solve for \(x\): \(x+2.5=9\).",
            "difficulty": 1,
            "choices": [(r"\(x=6.5\)", True), (r"\(x=11.5\)", False), (r"\(x=7.5\)", False), (r"\(x=22.5\)", False)],
            "explanation": r"Step 1: \(2.5\) is added to \(x\). Step 2: Subtract \(2.5\) from both sides: \(x=9-2.5\). Step 3: Compute \(9.0-2.5=6.5\). Check: \(6.5+2.5=9\). The trap \(11.5\) adds instead of subtracting.",
        },
        {
            "text": r"Solve for \(x\): \(2x+5=17\).",
            "difficulty": 1,
            "choices": [(r"\(x=6\)", True), (r"\(x=11\)", False), (r"\(x=8.5\)", False), (r"\(x=12\)", False)],
            "explanation": r"Step 1: Undo the addition first: subtract 5 from both sides, so \(2x=12\). Step 2: Undo multiplication by 2: divide both sides by 2, so \(x=6\). Step 3: Check in the original equation: \(2(6)+5=12+5=17\). The trap \(x=11\) subtracts 5 but forgets to divide by 2.",
        },
        {
            "text": r"Solve for \(x\): \(3x-4=20\).",
            "difficulty": 1,
            "choices": [(r"\(x=8\)", True), (r"\(x=\frac{16}{3}\)", False), (r"\(x=6\)", False), (r"\(x=24\)", False)],
            "explanation": r"Step 1: The equation is \(3x-4=20\). Undo \(-4\) by adding 4 to both sides: \(3x=24\). Step 2: Divide both sides by 3: \(x=8\). Step 3: Check: \(3(8)-4=24-4=20\). The trap \(\frac{16}{3}\) comes from subtracting 4 again instead of adding 4.",
        },
        {
            "text": r"Solve for \(x\): \(18=5x+3\).",
            "difficulty": 1,
            "choices": [(r"\(x=3\)", True), (r"\(x=15\)", False), (r"\(x=\frac{21}{5}\)", False), (r"\(x=5\)", False)],
            "explanation": r"Step 1: It is okay that the variable is on the right. Subtract 3 from both sides: \(18-3=5x\), so \(15=5x\). Step 2: Divide both sides by 5: \(3=x\). Step 3: Write the answer as \(x=3\). Check: \(5(3)+3=18\). The trap \(15\) stops one step too early.",
        },
        {
            "text": r"Solve for \(x\): \(\frac{x}{4}+6=10\).",
            "difficulty": 2,
            "choices": [(r"\(x=16\)", True), (r"\(x=1\)", False), (r"\(x=64\)", False), (r"\(x=4\)", False)],
            "explanation": r"Step 1: Remove the constant first: subtract 6 from both sides to get \(\frac{x}{4}=4\). Step 2: Undo division by 4 by multiplying both sides by 4: \(x=16\). Step 3: Check: \(16/4+6=4+6=10\). The trap \(x=4\) stops after subtracting 6 and forgets to multiply by 4.",
        },
        {
            "text": r"Solve for \(x\): \(-2x+7=15\).",
            "difficulty": 2,
            "choices": [(r"\(x=-4\)", True), (r"\(x=4\)", False), (r"\(x=-11\)", False), (r"\(x=1\)", False)],
            "explanation": r"Step 1: Subtract 7 from both sides: \(-2x=8\). Step 2: Divide both sides by \(-2\): \(x=-4\). Step 3: Check: \(-2(-4)+7=8+7=15\). The trap \(x=4\) loses the negative sign when dividing by \(-2\).",
        },
        {
            "text": r"Solve for \(x\): \(0.5x+3=9\).",
            "difficulty": 2,
            "choices": [(r"\(x=12\)", True), (r"\(x=3\)", False), (r"\(x=6\)", False), (r"\(x=18\)", False)],
            "explanation": r"Step 1: Subtract 3 from both sides: \(0.5x=6\). Step 2: Divide by \(0.5\). Dividing by \(0.5\) is the same as multiplying by 2, so \(x=12\). Step 3: Check: \(0.5(12)+3=6+3=9\). The trap \(x=6\) stops before dividing by \(0.5\).",
        },
        {
            "text": r"Solve for \(x\): \(3(x+2)=21\).",
            "difficulty": 1,
            "choices": [(r"\(x=5\)", True), (r"\(x=7\)", False), (r"\(x=9\)", False), (r"\(x=3\)", False)],
            "explanation": r"Step 1: Distribute 3: \(3x+6=21\). Step 2: Subtract 6 from both sides: \(3x=15\). Step 3: Divide by 3: \(x=5\). Check: \(3(5+2)=3(7)=21\). The trap \(x=7\) stops after dividing \(21\) by \(3\) but forgets the \(+2\) inside the parentheses.",
        },
        {
            "text": r"Solve for \(x\): \(2(x-4)+5=15\).",
            "difficulty": 2,
            "choices": [(r"\(x=9\)", True), (r"\(x=7\)", False), (r"\(x=4\)", False), (r"\(x=13\)", False)],
            "explanation": r"Step 1: Distribute: \(2x-8+5=15\). Step 2: Combine constants: \(2x-3=15\). Step 3: Add 3 to both sides: \(2x=18\). Step 4: Divide by 2: \(x=9\). Check: \(2(9-4)+5=10+5=15\). The trap \(x=7\) often comes from treating \(-8+5\) as \(-13\).",
        },
        {
            "text": r"Solve for \(x\): \(4x+3x-5=30\).",
            "difficulty": 1,
            "choices": [(r"\(x=5\)", True), (r"\(x=7\)", False), (r"\(x=35\)", False), (r"\(x=25\)", False)],
            "explanation": r"Step 1: Combine like terms: \(4x+3x=7x\), so \(7x-5=30\). Step 2: Add 5 to both sides: \(7x=35\). Step 3: Divide by 7: \(x=5\). Check: \(4(5)+3(5)-5=20+15-5=30\). The trap \(x=35\) stops before dividing by 7.",
        },
        {
            "text": r"Solve for \(x\): \(5(x+1)-2x=20\).",
            "difficulty": 2,
            "choices": [(r"\(x=5\)", True), (r"\(x=3\)", False), (r"\(x=\frac{15}{7}\)", False), (r"\(x=4\)", False)],
            "explanation": r"Step 1: Distribute 5: \(5x+5-2x=20\). Step 2: Combine like terms: \(3x+5=20\). Step 3: Subtract 5: \(3x=15\). Step 4: Divide by 3: \(x=5\). Check: \(5(5+1)-2(5)=30-10=20\). The trap \(\frac{15}{7}\) comes from adding \(5x\) and \(2x\) instead of subtracting.",
        },
        {
            "text": r"Solve for \(x\): \(-2(x-3)=14\).",
            "difficulty": 2,
            "choices": [(r"\(x=-4\)", True), (r"\(x=10\)", False), (r"\(x=4\)", False), (r"\(x=-10\)", False)],
            "explanation": r"Step 1: Distribute \(-2\): \(-2x+6=14\). Step 2: Subtract 6: \(-2x=8\). Step 3: Divide by \(-2\): \(x=-4\). Check: \(-2(-4-3)=-2(-7)=14\). The trap \(x=4\) loses the negative sign.",
        },
        {
            "text": r"Solve for \(x\): \(6-(x+2)=1\).",
            "difficulty": 2,
            "choices": [(r"\(x=3\)", True), (r"\(x=7\)", False), (r"\(x=-3\)", False), (r"\(x=5\)", False)],
            "explanation": r"Step 1: Distribute the minus sign: \(6-x-2=1\). Step 2: Combine constants: \(4-x=1\). Step 3: Subtract 4 from both sides: \(-x=-3\). Step 4: Multiply or divide by \(-1\): \(x=3\). Check: \(6-(3+2)=6-5=1\). The trap \(x=7\) treats \(6-(x+2)\) as \(6-x+2\).",
        },
        {
            "text": r"Solve for \(x\): \(5x-3=2x+12\).",
            "difficulty": 2,
            "choices": [(r"\(x=5\)", True), (r"\(x=3\)", False), (r"\(x=15\)", False), (r"\(x=-5\)", False)],
            "explanation": r"Step 1: Move variable terms together. Subtract \(2x\) from both sides: \(3x-3=12\). Step 2: Add 3 to both sides: \(3x=15\). Step 3: Divide by 3: \(x=5\). Check: \(5(5)-3=22\), and \(2(5)+12=22\). The trap \(x=3\) stops after forming \(3x\) and does not finish isolating \(x\).",
        },
        {
            "text": r"Solve for \(x\): \(7x+4=3x+28\).",
            "difficulty": 2,
            "choices": [(r"\(x=6\)", True), (r"\(x=8\)", False), (r"\(x=4\)", False), (r"\(x=24\)", False)],
            "explanation": r"Step 1: Subtract \(3x\) from both sides: \(4x+4=28\). Step 2: Subtract 4 from both sides: \(4x=24\). Step 3: Divide by 4: \(x=6\). Check: \(7(6)+4=46\), and \(3(6)+28=46\). The trap \(x=8\) comes from dividing 28 by 4 before removing the constant.",
        },
        {
            "text": r"Solve for \(x\): \(4x+9=6x-5\).",
            "difficulty": 2,
            "choices": [(r"\(x=7\)", True), (r"\(x=2\)", False), (r"\(x=-7\)", False), (r"\(x=14\)", False)],
            "explanation": r"Step 1: Move the smaller variable term. Subtract \(4x\) from both sides: \(9=2x-5\). Step 2: Add 5 to both sides: \(14=2x\). Step 3: Divide by 2: \(x=7\). Check: \(4(7)+9=37\), and \(6(7)-5=37\). The trap \(x=2\) stops at \(2x\).",
        },
        {
            "text": r"Solve for \(x\): \(3(x+2)=2x+11\).",
            "difficulty": 2,
            "choices": [(r"\(x=5\)", True), (r"\(x=3\)", False), (r"\(x=17\)", False), (r"\(x=-5\)", False)],
            "explanation": r"Step 1: Distribute the left side: \(3x+6=2x+11\). Step 2: Subtract \(2x\) from both sides: \(x+6=11\). Step 3: Subtract 6: \(x=5\). Check: \(3(5+2)=21\), and \(2(5)+11=21\). The trap \(x=3\) comes from not distributing correctly.",
        },
        {
            "text": r"Solve for \(x\): \(8-2x=x-13\).",
            "difficulty": 3,
            "choices": [(r"\(x=7\)", True), (r"\(x=-7\)", False), (r"\(x=5\)", False), (r"\(x=21\)", False)],
            "explanation": r"Step 1: Add \(2x\) to both sides to collect variables on the right: \(8=3x-13\). Step 2: Add 13 to both sides: \(21=3x\). Step 3: Divide by 3: \(x=7\). Check: \(8-2(7)=-6\), and \(7-13=-6\). The trap \(-7\) usually comes from subtracting \(2x\) instead of adding it.",
        },
        {
            "text": r"Solve for \(x\): \(\frac{x}{3}+4=10\).",
            "difficulty": 2,
            "choices": [(r"\(x=18\)", True), (r"\(x=2\)", False), (r"\(x=6\)", False), (r"\(x=42\)", False)],
            "explanation": r"Step 1: Subtract 4 from both sides: \(\frac{x}{3}=6\). Step 2: Multiply both sides by 3 to undo division by 3: \(x=18\). Step 3: Check: \(18/3+4=6+4=10\). The trap \(x=6\) stops before multiplying by 3.",
        },
        {
            "text": r"Solve for \(x\): \(\frac{2}{5}x=8\).",
            "difficulty": 2,
            "choices": [(r"\(x=20\)", True), (r"\(x=\frac{16}{5}\)", False), (r"\(x=10\)", False), (r"\(x=40\)", False)],
            "explanation": r"Step 1: \(x\) is multiplied by \(\frac{2}{5}\). Step 2: Divide by \(\frac{2}{5}\), or multiply by its reciprocal \(\frac{5}{2}\): \(x=8\cdot\frac{5}{2}\). Step 3: Simplify: \(8/2=4\), and \(4\cdot5=20\). Check: \(\frac{2}{5}(20)=8\). The trap \(\frac{16}{5}\) multiplies by \(\frac{2}{5}\) again.",
        },
        {
            "text": r"Solve for \(x\): \(\frac{x-2}{4}=5\).",
            "difficulty": 2,
            "choices": [(r"\(x=22\)", True), (r"\(x=18\)", False), (r"\(x=3\)", False), (r"\(x=20\)", False)],
            "explanation": r"Step 1: The entire numerator \(x-2\) is divided by 4. Multiply both sides by 4: \(x-2=20\). Step 2: Add 2 to both sides: \(x=22\). Step 3: Check: \((22-2)/4=20/4=5\). The trap \(20\) stops before adding 2.",
        },
        {
            "text": r"Solve for \(x\): \(\frac{3x+1}{2}=11\).",
            "difficulty": 2,
            "choices": [(r"\(x=7\)", True), (r"\(x=21\)", False), (r"\(x=\frac{11}{2}\)", False), (r"\(x=5\)", False)],
            "explanation": r"Step 1: Multiply both sides by 2 to clear the denominator: \(3x+1=22\). Step 2: Subtract 1: \(3x=21\). Step 3: Divide by 3: \(x=7\). Check: \((3(7)+1)/2=22/2=11\). The trap \(21\) stops before dividing by 3.",
        },
        {
            "text": r"Solve for \(x\): \(0.2x+4=10\).",
            "difficulty": 2,
            "choices": [(r"\(x=30\)", True), (r"\(x=6\)", False), (r"\(x=3\)", False), (r"\(x=50\)", False)],
            "explanation": r"Step 1: Subtract 4 from both sides: \(0.2x=6\). Step 2: Divide by \(0.2\). Since \(0.2=\frac{1}{5}\), dividing by \(0.2\) is multiplying by 5: \(x=30\). Step 3: Check: \(0.2(30)+4=6+4=10\). The trap \(6\) stops too early.",
        },
        {
            "text": r"Solve for \(x\): \(1.5x-6=9\).",
            "difficulty": 2,
            "choices": [(r"\(x=10\)", True), (r"\(x=2\)", False), (r"\(x=15\)", False), (r"\(x=1.5\)", False)],
            "explanation": r"Step 1: Add 6 to both sides: \(1.5x=15\). Step 2: Divide by \(1.5\): \(x=10\). Step 3: Check: \(1.5(10)-6=15-6=9\). The trap \(15\) stops before dividing by \(1.5\).",
        },
        {
            "text": r"The formula \(A=lw\) gives the area of a rectangle. Solve for \(w\).",
            "difficulty": 2,
            "choices": [(r"\(w=\frac{A}{l}\)", True), (r"\(w=A-l\)", False), (r"\(w=Al\)", False), (r"\(w=\frac{l}{A}\)", False)],
            "explanation": r"Step 1: Identify the target variable: \(w\). Step 2: In \(A=lw\), \(w\) is multiplied by \(l\). Step 3: Undo multiplication by \(l\) by dividing both sides by \(l\): \(\frac{A}{l}=w\). Write \(w=\frac{A}{l}\). The trap \(Al\) multiplies instead of dividing.",
        },
        {
            "text": r"The formula \(P=2l+2w\) gives rectangle perimeter. Solve for \(l\).",
            "difficulty": 3,
            "choices": [(r"\(l=\frac{P-2w}{2}\)", True), (r"\(l=P-2w\)", False), (r"\(l=\frac{P}{2}-2w\)", False), (r"\(l=2P-2w\)", False)],
            "explanation": r"Step 1: Isolate the term with \(l\): subtract \(2w\) from both sides to get \(P-2w=2l\). Step 2: Divide both sides by 2: \(\frac{P-2w}{2}=l\). Step 3: Write \(l=\frac{P-2w}{2}\). The trap \(\frac{P}{2}-2w\) divides only \(P\) by 2, but the entire quantity \(P-2w\) must be divided by 2.",
        },
        {
            "text": r"Use \(C=\frac{5}{9}(F-32)\). What is \(C\) when \(F=68\)?",
            "difficulty": 2,
            "choices": [(r"\(20\)", True), (r"\(36\)", False), (r"\(180\)", False), (r"\(\frac{5}{9}\)", False)],
            "explanation": r"Step 1: Substitute \(F=68\): \(C=\frac{5}{9}(68-32)\). Step 2: Simplify inside the parentheses first: \(68-32=36\). Step 3: Multiply: \(C=\frac{5}{9}\cdot36=5\cdot4=20\). Check: 68 degrees Fahrenheit is 20 degrees Celsius. The trap \(36\) stops before multiplying by \(\frac{5}{9}\).",
        },
        {
            "text": r"The formula \(d=rt\) gives distance. Solve for \(t\).",
            "difficulty": 2,
            "choices": [(r"\(t=\frac{d}{r}\)", True), (r"\(t=dr\)", False), (r"\(t=d-r\)", False), (r"\(t=\frac{r}{d}\)", False)],
            "explanation": r"Step 1: Target \(t\). Step 2: In \(d=rt\), \(t\) is multiplied by \(r\). Step 3: Divide both sides by \(r\): \(\frac{d}{r}=t\). Write \(t=\frac{d}{r}\). The trap \(\frac{r}{d}\) reverses the fraction.",
        },
        {
            "text": r"Simple interest is \(I=prt\). Find \(I\) when \(p=500\), \(r=0.04\), and \(t=3\).",
            "difficulty": 2,
            "choices": [(r"\(60\)", True), (r"\(20\)", False), (r"\(600\)", False), (r"\(503.04\)", False)],
            "explanation": r"Step 1: Substitute the values: \(I=500(0.04)(3)\). Step 2: Multiply \(500\cdot0.04=20\). Step 3: Multiply by 3: \(20\cdot3=60\). So \(I=60\). The trap 20 stops after one multiplication and forgets the 3 years.",
        },
        {
            "text": r"If \(y=3x+2\) and \(y=20\), what is \(x\)?",
            "difficulty": 2,
            "choices": [(r"\(x=6\)", True), (r"\(x=18\)", False), (r"\(x=\frac{20}{3}\)", False), (r"\(x=22\)", False)],
            "explanation": r"Step 1: Substitute \(y=20\): \(20=3x+2\). Step 2: Subtract 2 from both sides: \(18=3x\). Step 3: Divide by 3: \(x=6\). Check: \(3(6)+2=20\). The trap \(\frac{20}{3}\) divides before removing the +2.",
        },
        {
            "text": r"'A number plus 7 is 19.' What is the number?",
            "difficulty": 1,
            "choices": [(r"\(12\)", True), (r"\(26\)", False), (r"\(7\)", False), (r"\(19\)", False)],
            "explanation": r"Step 1: Let \(x\) be the number. Step 2: Translate the sentence: \(x+7=19\). Step 3: Subtract 7 from both sides: \(x=12\). Step 4: Check in words: 12 plus 7 is 19. The trap 26 comes from adding 7 to 19 instead of undoing the plus 7.",
        },
        {
            "text": r"A gym charges a \(\$25\) sign-up fee plus \(\$8\) per class. If the total is \(\$89\), how many classes were taken?",
            "difficulty": 2,
            "choices": [(r"\(8\)", True), (r"\(11\)", False), (r"\(14\)", False), (r"\(7\)", False)],
            "explanation": r"Step 1: Let \(c\) be the number of classes. Step 2: Build the equation: fixed fee plus class cost equals total, so \(25+8c=89\). Step 3: Subtract 25: \(8c=64\). Step 4: Divide by 8: \(c=8\). Check: \(25+8(8)=25+64=89\). The trap 11 comes from \(89/8\), forgetting the fixed fee.",
        },
        {
            "text": r"A taxi ride costs \(\$4\) plus \(\$2.50\) per mile. The total is \(\$24\). How many miles was the ride?",
            "difficulty": 2,
            "choices": [(r"\(8\)", True), (r"\(9.6\)", False), (r"\(11.2\)", False), (r"\(20\)", False)],
            "explanation": r"Step 1: Let \(m\) be miles. Step 2: Write the equation: \(4+2.50m=24\). Step 3: Subtract the starting fee: \(2.50m=20\). Step 4: Divide by 2.50: \(m=8\). Check: \(4+2.50(8)=4+20=24\). The trap 9.6 divides the total by 2.50 and ignores the 4 dollar fee.",
        },
        {
            "text": r"A rectangle has length \(12\) and perimeter \(40\). What is its width?",
            "difficulty": 2,
            "choices": [(r"\(8\)", True), (r"\(16\)", False), (r"\(28\)", False), (r"\(10\)", False)],
            "explanation": r"Step 1: Use the perimeter formula \(P=2l+2w\). Step 2: Substitute \(P=40\) and \(l=12\): \(40=2(12)+2w\). Step 3: Simplify: \(40=24+2w\). Step 4: Subtract 24: \(16=2w\). Step 5: Divide by 2: \(w=8\). Check: \(2(12)+2(8)=24+16=40\).",
        },
        {
            "text": r"Three times a number plus \(5\) is \(41\). What is the number?",
            "difficulty": 1,
            "choices": [(r"\(12\)", True), (r"\(15\)", False), (r"\(36\)", False), (r"\(14\)", False)],
            "explanation": r"Step 1: Let \(x\) be the number. Step 2: Translate: \(3x+5=41\). Step 3: Subtract 5: \(3x=36\). Step 4: Divide by 3: \(x=12\). Check: three times 12 plus 5 is \(36+5=41\). The trap 36 stops before dividing by 3.",
        },
        {
            "text": r"A sale price is \(75\%\) of the original price. If the sale price is \(\$60\), what was the original price?",
            "difficulty": 3,
            "choices": [(r"\(\$80\)", True), (r"\(\$45\)", False), (r"\(\$75\)", False), (r"\(\$135\)", False)],
            "explanation": r"Step 1: Let \(p\) be the original price. Step 2: \(75\%\) means \(0.75\), so write \(0.75p=60\). Step 3: Divide both sides by \(0.75\): \(p=60/0.75=80\). Step 4: Check: \(75\%\) of 80 is \(0.75(80)=60\). The trap 45 finds 75 percent of 60, but 60 is already the sale price.",
        },
        {
            "text": r"Solve: \(3x+4=3x+10\).",
            "difficulty": 2,
            "choices": [("No solution", True), (r"\(x=2\)", False), (r"\(x=6\)", False), ("Infinitely many solutions", False)],
            "explanation": r"Step 1: Subtract \(3x\) from both sides. The variable terms cancel, leaving \(4=10\). Step 2: Decide what the final statement means. \(4=10\) is false. Step 3: A false statement means no value of \(x\) can make the equation true, so there is no solution. The trap 'infinitely many' would require a true statement like \(4=4\).",
        },
        {
            "text": r"Solve: \(2(x+3)=2x+6\).",
            "difficulty": 2,
            "choices": [("Infinitely many solutions", True), ("No solution", False), (r"\(x=0\)", False), (r"\(x=3\)", False)],
            "explanation": r"Step 1: Distribute the left side: \(2x+6=2x+6\). Step 2: Subtract \(2x\) from both sides: \(6=6\). Step 3: The final statement is always true, so every value of \(x\) works. That means infinitely many solutions. The trap \(x=0\) is only one value that works, not the entire solution set.",
        },
        {
            "text": r"Solve for \(x\): \(4(x-2)=2x+10\).",
            "difficulty": 2,
            "choices": [(r"\(x=9\)", True), (r"\(x=1\)", False), (r"\(x=6\)", False), (r"\(x=18\)", False)],
            "explanation": r"Step 1: Distribute: \(4x-8=2x+10\). Step 2: Subtract \(2x\) from both sides: \(2x-8=10\). Step 3: Add 8 to both sides: \(2x=18\). Step 4: Divide by 2: \(x=9\). Step 5: Check: \(4(9-2)=28\), and \(2(9)+10=28\). The trap \(x=1\) comes from subtracting 10 and 8 incorrectly.",
        },
        {
            "text": r"Which value checks correctly in \(2x-1=9\)?",
            "difficulty": 1,
            "choices": [(r"\(x=5\)", True), (r"\(x=4\)", False), (r"\(x=9\)", False), (r"\(x=10\)", False)],
            "explanation": r"Step 1: Test the correct-looking value in the original equation. For \(x=5\), the left side is \(2(5)-1=10-1=9\). Step 2: The right side is 9, so both sides match. Therefore \(x=5\). Why the trap \(x=4\) fails: \(2(4)-1=7\), not 9.",
        },
        {
            "text": r"Solve: \(\frac{x}{4}+3=10\).",
            "difficulty": 2,
            "choices": [(r"\(x=28\)", True), (r"\(x=13\)", False), (r"\(x=52\)", False), (r"\(x=7\)", False)],
            "explanation": r"Subtract 3: \(\frac{x}{4}=7\). Multiply by 4: \(x=28\).",
        },
        {
            "text": r"Solve: \(2(x-3)=14\).",
            "difficulty": 2,
            "choices": [(r"\(x=10\)", True), (r"\(x=17\)", False), (r"\(x=8\)", False), (r"\(x=11\)", False)],
            "explanation": r"Divide by 2: \(x-3=7\). Add 3: \(x=10\).",
        },
        {
            "text": r"Solve: \(5x-2x=18\).",
            "difficulty": 1,
            "choices": [(r"\(x=6\)", True), (r"\(x=9\)", False), (r"\(x=3\)", False), (r"\(x=12\)", False)],
            "explanation": r"Combine like terms: \(3x=18\). Divide by 3: \(x=6\).",
        },
        {
            "text": r"Solve: \(4x=2x+8\).",
            "difficulty": 2,
            "choices": [(r"\(x=4\)", True), (r"\(x=8\)", False), (r"\(x=2\)", False), (r"\(x=6\)", False)],
            "explanation": r"Move \(2x\) to the left: \(4x-2x=8\). Combine: \(2x=8\). Divide: \(x=4\).",
        },
        {
            "text": r"Solve: \(3(x+4)=24\).",
            "difficulty": 2,
            "choices": [(r"\(x=4\)", True), (r"\(x=8\)", False), (r"\(x=12\)", False), (r"\(x=0\)", False)],
            "explanation": r"Divide both sides by 3: \(x+4=8\). Subtract 4: \(x=4\).",
        },
        {
            "text": r"Solve: \(6x+5=2x+21\).",
            "difficulty": 2,
            "choices": [(r"\(x=4\)", True), (r"\(x=2\)", False), (r"\(x=6\)", False), (r"\(x=16\)", False)],
            "explanation": r"Move \(2x\) left and 5 right: \(6x-2x=21-5\). Simplify: \(4x=16\). Divide: \(x=4\).",
        },
        {
            "text": r"Solve: \(\frac{x-3}{2}=5\).",
            "difficulty": 2,
            "choices": [(r"\(x=13\)", True), (r"\(x=8\)", False), (r"\(x=10\)", False), (r"\(x=7\)", False)],
            "explanation": r"Multiply both sides by 2: \(x-3=10\). Add 3: \(x=13\).",
        },
        {
            "text": r"Solve: \(2(3x-1)=4x+10\).",
            "difficulty": 3,
            "choices": [(r"\(x=6\)", True), (r"\(x=4\)", False), (r"\(x=5\)", False), (r"\(x=3\)", False)],
            "explanation": r"Distribute: \(6x-2=4x+10\). Move \(4x\) left and 2 right: \(2x=12\). Divide: \(x=6\).",
        },
        {
            "text": r"Solve: \(\frac{2x}{3}=10\).",
            "difficulty": 1,
            "choices": [(r"\(x=15\)", True), (r"\(x=20\)", False), (r"\(x=6.67\)", False), (r"\(x=5\)", False)],
            "explanation": r"Multiply both sides by 3: \(2x=30\). Divide by 2: \(x=15\).",
        },
        {
            "text": r"Solve: \(x+x+x=15\).",
            "difficulty": 1,
            "choices": [(r"\(x=5\)", True), (r"\(x=15\)", False), (r"\(x=3\)", False), (r"\(x=10\)", False)],
            "explanation": r"Combine like terms: \(3x=15\). Divide by 3: \(x=5\).",
        },
        {
            "text": r"Solve for \(y\): \(3y-7=2y+5\).",
            "difficulty": 2,
            "choices": [(r"\(y=12\)", True), (r"\(y=5\)", False), (r"\(y=2\)", False), (r"\(y=-2\)", False)],
            "explanation": r"Subtract \(2y\) from both sides: \(y-7=5\). Add 7: \(y=12\).",
        },
        {
            "text": r"Solve: \(-4x+9=-7\).",
            "difficulty": 2,
            "choices": [(r"\(x=4\)", True), (r"\(x=-4\)", False), (r"\(x=2\)", False), (r"\(x=16\)", False)],
            "explanation": r"Subtract 9: \(-4x=-16\). Divide by -4: \(x=4\).",
        },
        {
            "text": r"Solve: \(2(x+5)-3=13\).",
            "difficulty": 2,
            "choices": [(r"\(x=3\)", True), (r"\(x=4\)", False), (r"\(x=2\)", False), (r"\(x=6\)", False)],
            "explanation": r"Distribute and combine: \(2x+10-3=13\), so \(2x+7=13\). Subtract 7: \(2x=6\). Divide: \(x=3\).",
        },
        {
            "text": r"Solve: \(5(2x-4)=30\).",
            "difficulty": 2,
            "choices": [(r"\(x=5\)", True), (r"\(x=6\)", False), (r"\(x=4\)", False), (r"\(x=3\)", False)],
            "explanation": r"Distribute or divide by 5: \(2x-4=6\). Add 4: \(2x=10\). Divide by 2: \(x=5\).",
        },
        {
            "text": r"Solve: \(\frac{x}{2}-4=3\).",
            "difficulty": 1,
            "choices": [(r"\(x=14\)", True), (r"\(x=7\)", False), (r"\(x=12\)", False), (r"\(x=10\)", False)],
            "explanation": r"Add 4: \(\frac{x}{2}=7\). Multiply by 2: \(x=14\).",
        },
        {
            "text": r"Solve: \(3x+2x-5=30\).",
            "difficulty": 1,
            "choices": [(r"\(x=7\)", True), (r"\(x=5\)", False), (r"\(x=6\)", False), (r"\(x=35\)", False)],
            "explanation": r"Combine \(3x+2x=5x\): \(5x-5=30\). Add 5: \(5x=35\). Divide: \(x=7\).",
        },
        {
            "text": r"Solve: \(4(x-2)=2(x+6)\).",
            "difficulty": 3,
            "choices": [(r"\(x=10\)", True), (r"\(x=8\)", False), (r"\(x=6\)", False), (r"\(x=12\)", False)],
            "explanation": r"Distribute both sides: \(4x-8=2x+12\). Move variables and constants: \(2x=20\). Divide: \(x=10\).",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Equations Mastery course (MCQ only)."

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

        for item in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course,
                qtype="mcq",
                text=item["text"],
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=is_correct)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
