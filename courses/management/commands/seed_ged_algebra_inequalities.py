"""
Seed a GED Algebra course on inequalities.

This course follows the same pattern as the recent advanced equations course:
many worked examples, a larger MCQ bank, and detailed step-by-step answer
explanations with common traps.

Run:
    python manage.py seed_ged_algebra_inequalities
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


def explain(*steps, trap):
    parts = [f"Step {index}: {step}" for index, step in enumerate(steps, start=1)]
    parts.append(f"Common trap: {trap}")
    return " ".join(parts)


def item(text, correct, wrong, steps, trap, difficulty=2):
    return {
        "text": text,
        "difficulty": difficulty,
        "choices": [(correct, True), *[(choice, False) for choice in wrong]],
        "explanation": explain(*steps, trap=trap),
    }


COURSE = {
    "title": "GED Algebra: Inequalities Mastery",
    "slug": "ged-algebra-inequalities-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Algebra course on inequalities. Students learn inequality "
        "symbols, number-line graphs, one-step and two-step inequalities, the sign "
        "flip rule, variables on both sides, fraction and decimal inequalities, "
        "compound and absolute value inequalities, word-problem modeling, and "
        "linear inequalities in two variables. Lessons include many examples, and "
        "every practice answer gives detailed step-by-step reasoning."
    ),
    "lessons": [
        (
            "1. What an Inequality Means",
            r"""
An **inequality** compares two expressions that are not necessarily equal. Instead of one answer, an inequality often has many possible answers.

The symbols:
- \(<\): less than
- \(>\): greater than
- \(\le\): less than or equal to, also called **at most**
- \(\ge\): greater than or equal to, also called **at least**

Example 1:
\[
x > 5
\]
means \(x\) can be any number greater than 5, such as 6, 10, or 5.1. It cannot be exactly 5.

Example 2:
\[
x \le 5
\]
means \(x\) can be 5 or any number less than 5.

Words matter:
- **At least 12** means \(x \ge 12\).
- **More than 12** means \(x > 12\).
- **At most 12** means \(x \le 12\).
- **Less than 12** means \(x < 12\).

Common mistake: treating \(<\) and \(\le\) as the same. The equal bar tells whether the endpoint is included.

[[check:Translate "at least 10" as an inequality.|x>=10;;x ≥ 10;;x\ge10|At least means 10 or more.]]
            """,
        ),
        (
            "2. Graphing Inequalities on a Number Line",
            r"""
A number-line graph shows all possible answers.

[[figure:number_line_ineq|An open circle means the endpoint is not included; the ray points toward the solution values.]]

Use the endpoint and the direction:
- \(x > 2\): open circle at 2, shade right.
- \(x \ge 2\): closed circle at 2, shade right.
- \(x < 2\): open circle at 2, shade left.
- \(x \le 2\): closed circle at 2, shade left.

Why open or closed?
- Open circle: \(<\) or \(>\). Endpoint is not part of the solution.
- Closed circle: \(\le\) or \(\ge\). Endpoint is part of the solution.

Example:
\[
x \le -3
\]
has a closed circle at \(-3\) and shading left.

Test a point if you are unsure. For \(x<2\), try 0. Since \(0<2\), 0 should be in the shaded region.

Common mistake: shading the wrong direction. Greater than goes right; less than goes left.

[[check:For \(x \le 4\), should the circle at 4 be open or closed?|closed|The equal bar means 4 is included.]]
            """,
        ),
        (
            "3. One-Step Inequalities",
            r"""
One-step inequalities solve almost like one-step equations.

Example 1:
\[
x+7>12.
\]
Subtract 7 from both sides:
\[
x>5.
\]

Example 2:
\[
x-4\le 9.
\]
Add 4 to both sides:
\[
x\le 13.
\]

Example 3:
\[
4x\le 28.
\]
Divide by positive 4:
\[
x\le 7.
\]

Example 4:
\[
\frac{x}{5}<3.
\]
Multiply by positive 5:
\[
x<15.
\]

When you add, subtract, multiply by a positive, or divide by a positive, the inequality sign keeps the same direction.

Common mistake: flipping the sign when adding or subtracting. You only flip for multiplying or dividing by a negative.

[[check:Solve \(x+3>-2\).|x>-5;;-5|Subtract 3 from both sides.]]
            """,
        ),
        (
            "4. The Sign-Flip Rule",
            r"""
Here is the special rule that makes inequalities different from equations:

**When you multiply or divide both sides by a negative number, flip the inequality sign.**

Example 1:
\[
-3x < 12.
\]
Divide by \(-3\). Because the divisor is negative, flip \(<\) to \(>\):
\[
x > -4.
\]

Example 2:
\[
-2x+7\le 15.
\]
Subtract 7:
\[
-2x\le 8.
\]
Divide by \(-2\) and flip:
\[
x\ge -4.
\]

Why does the sign flip? Try true numbers:
\[
2<5.
\]
Multiply both sides by \(-1\):
\[
-2>-5.
\]
The direction must reverse to stay true.

Common mistake: flipping when subtracting a negative. The flip happens only when multiplying or dividing by a negative, not simply because a negative number appears.

[[check:When do you flip the inequality sign?|when multiplying or dividing by a negative;;divide by negative;;multiply by negative|The sign flips only for multiplying or dividing both sides by a negative number.]]
            """,
        ),
        (
            "5. Two-Step Inequalities",
            r"""
Two-step inequalities usually look like:
\[
ax+b<c.
\]
Remove the constant first, then divide by the coefficient.

Example 1:
\[
2x+5<17.
\]
Subtract 5:
\[
2x<12.
\]
Divide by 2:
\[
x<6.
\]

Example 2:
\[
3x-4\ge20.
\]
Add 4:
\[
3x\ge24.
\]
Divide by 3:
\[
x\ge8.
\]

Example 3:
\[
5-x>2.
\]
Subtract 5:
\[
-x>-3.
\]
Divide by \(-1\) and flip:
\[
x<3.
\]

Check by testing one value. For \(x<3\), try \(x=0\):
\[
5-0>2
\]
is true, so the direction is reasonable.

Common mistake: solving \(5-x>2\) as \(x>3\). The coefficient of \(x\) is \(-1\), so the sign flips at the end.

[[check:Solve \(3x-4\ge20\).|x>=8;;x ≥ 8;;8|Add 4, then divide by 3.]]
            """,
        ),
        (
            "6. Multi-Step Inequalities",
            r"""
Multi-step inequalities need the same cleanup routine as equations.

Use this order:
- Distribute.
- Combine like terms.
- Move variables and constants.
- Divide by the coefficient.
- Flip only if you divide by a negative.

Example 1:
\[
3(x+2)>21.
\]
Distribute:
\[
3x+6>21.
\]
Subtract 6:
\[
3x>15.
\]
Divide by 3:
\[
x>5.
\]

Example 2:
\[
2(x-4)+5\le15.
\]
Distribute:
\[
2x-8+5\le15.
\]
Combine:
\[
2x-3\le15.
\]
Add 3:
\[
2x\le18.
\]
Divide:
\[
x\le9.
\]

Example 3:
\[
6-(x+2)<1.
\]
Distribute the minus sign:
\[
6-x-2<1.
\]
Combine:
\[
4-x<1.
\]
Subtract 4:
\[
-x<-3.
\]
Divide by \(-1\) and flip:
\[
x>3.
\]

Common mistake: forgetting that a minus before parentheses changes every sign inside.

[[check:Solve \(3(x+2)>21\).|x>5;;5|Distribute, subtract 6, divide by 3.]]
            """,
        ),
        (
            "7. Variables on Both Sides",
            r"""
When variables appear on both sides, simplify first. Then collect variable terms on one side.

Example 1:
\[
5x-3<2x+12.
\]
Subtract \(2x\):
\[
3x-3<12.
\]
Add 3:
\[
3x<15.
\]
Divide:
\[
x<5.
\]

Example 2:
\[
4x+9>6x-5.
\]
Subtract \(4x\):
\[
9>2x-5.
\]
Add 5:
\[
14>2x.
\]
Divide:
\[
7>x.
\]
That means:
\[
x<7.
\]

Example 3:
\[
8-2x\le x-13.
\]
Add \(2x\):
\[
8\le3x-13.
\]
Add 13:
\[
21\le3x.
\]
Divide:
\[
7\le x,
\]
or \(x\ge7\).

Common mistake: reversing the meaning when rewriting. \(7>x\) is the same as \(x<7\), not \(x>7\).

[[check:Rewrite \(7>x\) with \(x\) first.|x<7|If 7 is greater than x, then x is less than 7.]]
            """,
        ),
        (
            "8. Fraction and Decimal Inequalities",
            r"""
Fractions and decimals do not change the inequality rules. They only make the arithmetic heavier.

Example 1:
\[
\frac{x}{2}+\frac{x}{3}>10.
\]
Multiply every term by the LCD, 6:
\[
3x+2x>60.
\]
Combine:
\[
5x>60.
\]
Divide:
\[
x>12.
\]

Example 2:
\[
\frac{x+1}{3}+\frac{x-2}{2}\le7.
\]
Multiply every term by 6:
\[
2(x+1)+3(x-2)\le42.
\]
Distribute:
\[
2x+2+3x-6\le42.
\]
Combine:
\[
5x-4\le42.
\]
Solve:
\[
5x\le46,\qquad x\le\frac{46}{5}.
\]

Example 3:
\[
0.2x+4\ge10.
\]
Subtract 4:
\[
0.2x\ge6.
\]
Divide by \(0.2\):
\[
x\ge30.
\]

Common mistake: multiplying only the fraction terms by the LCD and forgetting the whole-number term on the other side.

[[check:What is the LCD of 2 and 3?|6|The LCD is the smallest number divisible by both 2 and 3.]]
            """,
        ),
        (
            "9. Compound Inequalities",
            r"""
A **compound inequality** joins two inequalities.

AND means the number must satisfy both conditions:
\[
2<x\le8.
\]
This means \(x\) is greater than 2 and at most 8.

OR means either condition can work:
\[
x<2 \quad \text{or} \quad x>5.
\]
This means numbers below 2 and numbers above 5 are included, with a gap between.

Example 1:
\[
2<x+1<8.
\]
Subtract 1 from all three parts:
\[
1<x<7.
\]

Example 2:
\[
-3\le2x+1<9.
\]
Subtract 1 from all three parts:
\[
-4\le2x<8.
\]
Divide all three parts by 2:
\[
-2\le x<4.
\]

Example 3:
\[
-1<\frac{x-2}{3}\le4.
\]
Multiply all parts by 3:
\[
-3<x-2\le12.
\]
Add 2:
\[
-1<x\le14.
\]

Common mistake: solving only one side of an AND inequality. You must apply the operation to all three parts.

[[check:Solve \(2<x+1<8\).|1<x<7;;x>1 and x<7|Subtract 1 from all three parts.]]
            """,
        ),
        (
            "10. Absolute Value Inequalities",
            r"""
Absolute value means distance from zero. Absolute value inequalities are about distance from a center.

Less than means **inside** the distance:
\[
|x-3|<5
\]
means \(x\) is within 5 units of 3:
\[
-5<x-3<5.
\]
Add 3:
\[
-2<x<8.
\]

Greater than means **outside** the distance:
\[
|x+4|>6.
\]
Split into two cases:
\[
x+4<-6 \quad \text{or} \quad x+4>6.
\]
Solve:
\[
x<-10 \quad \text{or} \quad x>2.
\]

Special cases:
- \(|x-2|\ge0\) is true for all real numbers.
- \(|x-2|<-1\) has no solution because distance cannot be negative.

Common mistake: treating \(|x-3|<5\) as \(x-3<5\) only. Less-than absolute value needs a middle compound inequality.

[[check:Solve \(|x-3|<5\).|-2<x<8;;x>-2 and x<8|Write \(-5<x-3<5\), then add 3.]]
            """,
        ),
        (
            "11. Word Problems with Inequalities",
            r"""
Use inequalities when a story says at least, at most, no more than, fewer than, under, over, minimum, or maximum.

Example 1 - budget:
A gym costs 25 dollars plus 8 dollars per class. You can spend at most 89 dollars.
\[
25+8c\le89.
\]
Subtract 25:
\[
8c\le64.
\]
Divide:
\[
c\le8.
\]

Example 2 - test average:
Three tests must average at least 80. The first two scores are 78 and 84.
\[
\frac{78+84+x}{3}\ge80.
\]
Multiply by 3:
\[
162+x\ge240.
\]
Subtract 162:
\[
x\ge78.
\]

Example 3 - percent increase:
After an 8 percent tax, the total must be no more than 54 dollars:
\[
1.08p\le54.
\]
Divide:
\[
p\le50.
\]

Common mistake: translating "at most" as \(>\). At most means less than or equal to.

[[check:Translate "no more than 89" as an inequality.|x<=89;;x ≤ 89;;x\le89|No more than means 89 or less.]]
            """,
        ),
        (
            "12. Linear Inequalities in Two Variables",
            r"""
Some inequalities use both \(x\) and \(y\). Their solutions are points, not just numbers.

Example:
\[
y>2x+1.
\]
To test whether \((1,4)\) is a solution, substitute \(x=1\) and \(y=4\):
\[
4>2(1)+1.
\]
Simplify:
\[
4>3.
\]
True, so \((1,4)\) is a solution.

Graphing rules:
- Use the boundary line \(y=mx+b\).
- Dashed line for \(<\) or \(>\).
- Solid line for \(\le\) or \(\ge\).
- Shade above for \(y>\) or \(y\ge\).
- Shade below for \(y<\) or \(y\le\).

[[figure:coord_line|A boundary line separates the coordinate plane into two half-planes. Test one point to decide which side is shaded.]]

Example:
\[
y\le -x+3.
\]
The boundary line is \(y=-x+3\). Since the symbol is \(\le\), use a solid line and shade below it.

Common mistake: using a solid line for \(>\) or \(<\). Without the equal bar, the boundary line is not included.

[[check:For \(y<3x-2\), is the boundary line solid or dashed?|dashed|There is no equal bar, so the boundary is not included.]]
            """,
        ),
    ],
    "mcqs": [
        item(r"Which value is a solution of \(x>5\)?", r"\(8\)", [r"\(5\)", r"\(4\)", r"\(-8\)"], [r"Read \(x>5\) as x is greater than 5.", r"Test the choices. \(8>5\) is true.", r"\(5>5\) is false because 5 is not greater than itself.", r"So \(8\) is a solution."], r"including the endpoint 5 even though the symbol is \(>\), not \(\ge\).", 1),
        item(r"Which value is included in \(x\le -2\)?", r"\(-2\)", [r"\(-1\)", r"\(0\)", r"\(3\)"], [r"The symbol \(\le\) means less than or equal to.", r"The endpoint \(-2\) is included because of the equal bar.", r"\(-1\), 0, and 3 are all greater than \(-2\).", r"Therefore \(-2\) is included."], r"forgetting that the equal bar includes the endpoint.", 1),
        item(r"How should \(x<4\) be graphed on a number line?", "Open circle at 4, shade left", ["Closed circle at 4, shade left", "Open circle at 4, shade right", "Closed circle at 4, shade right"], [r"The symbol \(<\) does not include 4, so use an open circle.", r"Less than means values smaller than 4.", r"Smaller values are to the left on a number line.", r"So use an open circle at 4 and shade left."], r"using a closed circle even though the endpoint is not included.", 1),
        item(r"Translate 'at least 12' into an inequality.", r"\(x\ge12\)", [r"\(x>12\)", r"\(x\le12\)", r"\(x<12\)"], [r"'At least 12' means 12 is allowed.", r"It also means any number greater than 12 is allowed.", r"That is \(x\ge12\).", r"The equal bar matters because 12 itself is included."], r"using \(>\), which excludes 12.", 1),
        item(r"Translate 'no more than 30' into an inequality.", r"\(x\le30\)", [r"\(x<30\)", r"\(x\ge30\)", r"\(x>30\)"], [r"'No more than 30' means 30 is the maximum.", r"The value can be 30 or less.", r"That is \(x\le30\).", r"The phrase 'no more than' points to at most."], r"treating 'no more than' as greater than.", 1),
        item(r"Is \(x=3\) a solution of \(2x+1>5\)?", "Yes", ["No", "Only if \(x=5\)", "Cannot tell"], [r"Substitute \(x=3\) into the left side.", r"\(2(3)+1=7\).", r"Compare: \(7>5\) is true.", r"So \(x=3\) is a solution."], r"solving for \(x\) before simply testing the given value.", 1),
        item(r"Solve: \(x+7>12\).", r"\(x>5\)", [r"\(x<5\)", r"\(x>19\)", r"\(x<19\)"], [r"Subtract 7 from both sides.", r"\(x+7-7>12-7\).", r"Simplify: \(x>5\).", r"No sign flip happens because you subtracted, not divided by a negative."], r"flipping the sign during subtraction.", 1),
        item(r"Solve: \(x-4\le9\).", r"\(x\le13\)", [r"\(x\ge13\)", r"\(x\le5\)", r"\(x\ge5\)"], [r"Undo \(-4\) by adding 4 to both sides.", r"\(x-4+4\le9+4\).", r"Simplify: \(x\le13\).", r"Check with \(x=13\): \(13-4=9\), so the endpoint works."], r"subtracting 4 again instead of adding it.", 1),
        item(r"Solve: \(x+3\ge -2\).", r"\(x\ge -5\)", [r"\(x\le -5\)", r"\(x\ge1\)", r"\(x\le1\)"], [r"Subtract 3 from both sides.", r"\(x\ge -2-3\).", r"Simplify: \(x\ge -5\).", r"Adding or subtracting does not flip the sign."], r"flipping the sign just because negative numbers appear.", 1),
        item(r"Solve: \(\frac{x}{5}<3\).", r"\(x<15\)", [r"\(x>15\)", r"\(x<\frac{3}{5}\)", r"\(x>8\)"], [r"\(x\) is divided by 5.", r"Multiply both sides by positive 5.", r"The sign stays the same: \(x<15\).", r"Check with \(x=10\): \(10/5=2<3\)."], r"flipping the sign when multiplying by a positive number.", 1),
        item(r"Solve: \(4x\le28\).", r"\(x\le7\)", [r"\(x\ge7\)", r"\(x\le24\)", r"\(x\ge24\)"], [r"Divide both sides by positive 4.", r"\(4x/4\le28/4\).", r"Simplify: \(x\le7\).", r"The sign does not flip because 4 is positive."], r"flipping the inequality when dividing by a positive coefficient.", 1),
        item(r"Solve: \(-3x<12\).", r"\(x>-4\)", [r"\(x<-4\)", r"\(x>4\)", r"\(x<4\)"], [r"Divide both sides by \(-3\).", r"Because you divide by a negative, flip \(<\) to \(>\).", r"\(x>12/(-3)\), so \(x>-4\).", r"Check with \(x=0\): \(-3(0)<12\) is true, and \(0>-4\)." ], r"forgetting to flip the sign when dividing by a negative.", 2),
        item(r"Solve: \(2x+5<17\).", r"\(x<6\)", [r"\(x>6\)", r"\(x<11\)", r"\(x>11\)"], [r"Subtract 5 from both sides: \(2x<12\).", r"Divide both sides by positive 2.", r"The sign stays the same: \(x<6\).", r"Check with \(x=5\): \(2(5)+5=15<17\)."], r"stopping at \(2x<12\) or flipping the sign for no reason.", 2),
        item(r"Solve: \(3x-4\ge20\).", r"\(x\ge8\)", [r"\(x\le8\)", r"\(x\ge\frac{16}{3}\)", r"\(x\le\frac{16}{3}\)"], [r"Add 4 to both sides: \(3x\ge24\).", r"Divide by positive 3.", r"The sign stays the same: \(x\ge8\).", r"Check \(x=8\): \(24-4=20\), so the endpoint is included."], r"subtracting 4 instead of adding 4.", 2),
        item(r"Solve: \(-2x+7\le15\).", r"\(x\ge -4\)", [r"\(x\le -4\)", r"\(x\ge4\)", r"\(x\le4\)"], [r"Subtract 7 from both sides: \(-2x\le8\).", r"Divide by \(-2\).", r"Flip \(\le\) to \(\ge\): \(x\ge -4\).", r"Check with \(x=0\): \(7\le15\) is true, and \(0\ge-4\)." ], r"forgetting the sign flip at the final division.", 2),
        item(r"Solve: \(0.5x+3>9\).", r"\(x>12\)", [r"\(x>6\)", r"\(x<12\)", r"\(x>3\)"], [r"Subtract 3 from both sides: \(0.5x>6\).", r"Divide by positive \(0.5\).", r"Dividing by \(0.5\) doubles the value: \(x>12\).", r"Check with \(x=14\): \(7+3>9\)." ], r"stopping at \(x>6\) before dividing by \(0.5\).", 2),
        item(r"Solve: \(\frac{x}{4}+6\le10\).", r"\(x\le16\)", [r"\(x\ge16\)", r"\(x\le4\)", r"\(x\ge4\)"], [r"Subtract 6 from both sides: \(\frac{x}{4}\le4\).", r"Multiply both sides by positive 4.", r"The sign stays the same: \(x\le16\).", r"Check \(x=16\): \(4+6=10\), so it works."], r"stopping at \(x/4\le4\).", 2),
        item(r"Solve: \(5-x>2\).", r"\(x<3\)", [r"\(x>3\)", r"\(x<-3\)", r"\(x>7\)"], [r"Subtract 5 from both sides: \(-x>-3\).", r"Divide by \(-1\).", r"Flip the sign: \(x<3\).", r"Check with \(x=0\): \(5-0>2\) is true."], r"forgetting that the coefficient of \(x\) is \(-1\).", 2),
        item(r"Solve: \(3(x+2)>21\).", r"\(x>5\)", [r"\(x<5\)", r"\(x>7\)", r"\(x>3\)"], [r"Distribute: \(3x+6>21\).", r"Subtract 6: \(3x>15\).", r"Divide by positive 3: \(x>5\).", r"Check with \(x=6\): \(3(8)=24>21\)." ], r"dividing 21 by 3 and stopping at \(x+2>7\).", 2),
        item(r"Solve: \(2(x-4)+5\le15\).", r"\(x\le9\)", [r"\(x\ge9\)", r"\(x\le7\)", r"\(x\le4\)"], [r"Distribute: \(2x-8+5\le15\).", r"Combine constants: \(2x-3\le15\).", r"Add 3: \(2x\le18\).", r"Divide by 2: \(x\le9\)." ], r"combining \(-8+5\) as \(-13\) instead of \(-3\).", 2),
        item(r"Solve: \(5(x+1)-2x>20\).", r"\(x>5\)", [r"\(x<5\)", r"\(x>3\)", r"\(x>15\)"], [r"Distribute: \(5x+5-2x>20\).", r"Combine like terms: \(3x+5>20\).", r"Subtract 5: \(3x>15\).", r"Divide by 3: \(x>5\)." ], r"adding \(5x\) and \(2x\) instead of subtracting \(2x\).", 2),
        item(r"Solve: \(-2(x-3)\le14\).", r"\(x\ge -4\)", [r"\(x\le -4\)", r"\(x\ge4\)", r"\(x\le10\)"], [r"Distribute: \(-2x+6\le14\).", r"Subtract 6: \(-2x\le8\).", r"Divide by \(-2\) and flip: \(x\ge -4\).", r"Check with \(x=0\): \(6\le14\) is true."], r"forgetting to flip when dividing by \(-2\).", 2),
        item(r"Solve: \(6-(x+2)<1\).", r"\(x>3\)", [r"\(x<3\)", r"\(x>7\)", r"\(x<-3\)"], [r"Distribute the minus sign: \(6-x-2<1\).", r"Combine constants: \(4-x<1\).", r"Subtract 4: \(-x<-3\).", r"Divide by \(-1\) and flip: \(x>3\)." ], r"writing \(6-(x+2)\) as \(6-x+2\).", 2),
        item(r"Solve: \(4(2x-3)+5\ge37\).", r"\(x\ge\frac{11}{2}\)", [r"\(x\le\frac{11}{2}\)", r"\(x\ge4\)", r"\(x\ge5\)"], [r"Distribute: \(8x-12+5\ge37\).", r"Combine: \(8x-7\ge37\).", r"Add 7: \(8x\ge44\).", r"Divide by 8: \(x\ge\frac{11}{2}\)." ], r"rounding \(\frac{11}{2}\) down to 5.", 3),
        item(r"Solve: \(5x-3<2x+12\).", r"\(x<5\)", [r"\(x>5\)", r"\(x<3\)", r"\(x>15\)"], [r"Subtract \(2x\) from both sides: \(3x-3<12\).", r"Add 3: \(3x<15\).", r"Divide by 3: \(x<5\).", r"Check with \(x=4\): \(17<20\) is true."], r"moving \(2x\) without doing the same operation to both sides.", 2),
        item(r"Solve: \(7x+4\ge3x+28\).", r"\(x\ge6\)", [r"\(x\le6\)", r"\(x\ge8\)", r"\(x\le8\)"], [r"Subtract \(3x\): \(4x+4\ge28\).", r"Subtract 4: \(4x\ge24\).", r"Divide by 4: \(x\ge6\).", r"Check \(x=6\): \(46\ge46\)." ], r"dividing 28 by 4 before subtracting 4.", 2),
        item(r"Solve: \(4x+9>6x-5\).", r"\(x<7\)", [r"\(x>7\)", r"\(x<2\)", r"\(x>14\)"], [r"Subtract \(4x\): \(9>2x-5\).", r"Add 5: \(14>2x\).", r"Divide by 2: \(7>x\).", r"Rewrite with \(x\) first: \(x<7\)." ], r"rewriting \(7>x\) as \(x>7\).", 3),
        item(r"Solve: \(8-2x\le x-13\).", r"\(x\ge7\)", [r"\(x\le7\)", r"\(x\ge-7\)", r"\(x\le-7\)"], [r"Add \(2x\) to both sides: \(8\le3x-13\).", r"Add 13: \(21\le3x\).", r"Divide by 3: \(7\le x\).", r"Rewrite as \(x\ge7\)." ], r"losing the inequality direction when rewriting the final statement.", 3),
        item(r"Solve: \(3(x+2)>2x+11\).", r"\(x>5\)", [r"\(x<5\)", r"\(x>3\)", r"\(x>17\)"], [r"Distribute: \(3x+6>2x+11\).", r"Subtract \(2x\): \(x+6>11\).", r"Subtract 6: \(x>5\).", r"Check with \(x=6\): \(24>23\)." ], r"forgetting to distribute before moving terms.", 2),
        item(r"Solve: \(4(2x-3)<5x+15\).", r"\(x<9\)", [r"\(x>9\)", r"\(x<3\)", r"\(x>27\)"], [r"Distribute: \(8x-12<5x+15\).", r"Subtract \(5x\): \(3x-12<15\).", r"Add 12: \(3x<27\).", r"Divide by 3: \(x<9\)." ], r"adding 12 to only one side.", 3),
        item(r"Solve: \(\frac{x}{2}+\frac{x}{3}>10\).", r"\(x>12\)", [r"\(x<12\)", r"\(x>5\)", r"\(x>60\)"], [r"Use LCD 6 and multiply every term by 6.", r"You get \(3x+2x>60\).", r"Combine: \(5x>60\).", r"Divide by 5: \(x>12\)." ], r"adding denominators and treating the left side as \(\frac{2x}{5}\).", 3),
        item(r"Solve: \(\frac{x+1}{3}+\frac{x-2}{2}\le7\).", r"\(x\le\frac{46}{5}\)", [r"\(x\ge\frac{46}{5}\)", r"\(x\le9\)", r"\(x\le10\)"], [r"Multiply every term by LCD 6.", r"The equation becomes \(2(x+1)+3(x-2)\le42\).", r"Distribute and combine: \(5x-4\le42\).", r"Add 4 and divide by 5: \(x\le\frac{46}{5}\)." ], r"forgetting to multiply the right side by 6.", 3),
        item(r"Solve: \(\frac{2x-1}{5}\ge\frac{x+4}{3}\).", r"\(x\ge23\)", [r"\(x\le23\)", r"\(x\ge20\)", r"\(x\le20\)"], [r"Cross-multiply by positive denominators: \(3(2x-1)\ge5(x+4)\).", r"Distribute: \(6x-3\ge5x+20\).", r"Subtract \(5x\): \(x-3\ge20\).", r"Add 3: \(x\ge23\)." ], r"cross-multiplying only part of a numerator.", 3),
        item(r"Solve: \(0.25(8x-4)<9\).", r"\(x<5\)", [r"\(x>5\)", r"\(x<4\)", r"\(x<40\)"], [r"Distribute \(0.25\): \(2x-1<9\).", r"Add 1: \(2x<10\).", r"Divide by 2: \(x<5\).", r"Check with \(x=4\): \(0.25(28)=7<9\)." ], r"forgetting that \(0.25\cdot(-4)=-1\).", 2),
        item(r"Solve: \(0.2x+4\ge10\).", r"\(x\ge30\)", [r"\(x\le30\)", r"\(x\ge6\)", r"\(x\ge50\)"], [r"Subtract 4: \(0.2x\ge6\).", r"Divide by positive \(0.2\).", r"\(6/0.2=30\), so \(x\ge30\).", r"No flip happens because \(0.2\) is positive."], r"stopping at \(x\ge6\).", 2),
        item(r"Solve: \(1.5x-6<9\).", r"\(x<10\)", [r"\(x>10\)", r"\(x<2\)", r"\(x<15\)"], [r"Add 6: \(1.5x<15\).", r"Divide by positive \(1.5\).", r"\(x<10\).", r"Check with \(x=8\): \(12-6=6<9\)." ], r"stopping at \(1.5x<15\).", 2),
        item(r"Solve: \(2<x+1<8\).", r"\(1<x<7\)", [r"\(3<x<9\)", r"\(x<1\) or \(x>7\)", r"\(1\le x\le7\)"], [r"Subtract 1 from all three parts.", r"\(2-1<x+1-1<8-1\).", r"Simplify: \(1<x<7\).", r"The endpoints are not included because the original symbols were strict."], r"subtracting 1 from only the middle expression.", 2),
        item(r"Solve: \(-3\le2x+1<9\).", r"\(-2\le x<4\)", [r"\(-1\le x<5\)", r"\(x\le-2\) or \(x>4\)", r"\(-2<x\le4\)"], [r"Subtract 1 from all three parts: \(-4\le2x<8\).", r"Divide all three parts by positive 2.", r"The sign directions stay the same.", r"The result is \(-2\le x<4\)." ], r"forgetting which endpoint has the equal bar.", 3),
        item(r"Solve: \(x-3<-1\) or \(x+2>7\).", r"\(x<2\) or \(x>5\)", [r"\(2<x<5\)", r"\(x<5\) or \(x>2\)", r"\(x>2\) and \(x<5\)"], [r"Solve the first inequality: \(x-3<-1\), so \(x<2\).", r"Solve the second inequality: \(x+2>7\), so \(x>5\).", r"Keep the word OR between the solutions.", r"The final answer is \(x<2\) or \(x>5\)." ], r"turning OR into AND and shading only between 2 and 5.", 3),
        item(r"Which graph matches \(3<x\le10\)?", "Open circle at 3, closed circle at 10, shade between", ["Closed circle at 3, open circle at 10, shade between", "Open circles at both endpoints", "Closed circles at both endpoints"], [r"The symbol \(3<x\) means \(x\) is greater than 3, so 3 is not included.", r"Use an open circle at 3.", r"The symbol \(x\le10\) includes 10.", r"Use a closed circle at 10 and shade between the endpoints."], r"making both endpoints the same type.", 2),
        item(r"Solve: \(-1<\frac{x-2}{3}\le4\).", r"\(-1<x\le14\)", [r"\(-5<x\le10\)", r"\(1<x\le14\)", r"\(-1\le x<14\)"], [r"Multiply all three parts by positive 3: \(-3<x-2\le12\).", r"Add 2 to all three parts.", r"The result is \(-1<x\le14\).", r"The left endpoint stays open and the right endpoint stays closed."], r"adding 2 to only the middle part.", 3),
        item(r"Translate 'between 5 and 12 inclusive' into an inequality.", r"\(5\le x\le12\)", [r"\(5<x<12\)", r"\(x<5\) or \(x>12\)", r"\(5\ge x\ge12\)"], [r"'Between 5 and 12' means the values lie in the interval from 5 to 12.", r"'Inclusive' means the endpoints are included.", r"Use \(\le\) on both sides.", r"The answer is \(5\le x\le12\)." ], r"using strict inequalities even though inclusive means the endpoints count.", 1),
        item(r"Solve: \(|x-3|<5\).", r"\(-2<x<8\)", [r"\(x<-2\) or \(x>8\)", r"\(x<8\)", r"\(-8<x<2\)"], [r"Less-than absolute value means inside a distance.", r"Write \(-5<x-3<5\).", r"Add 3 to all three parts.", r"The solution is \(-2<x<8\)." ], r"using OR instead of the inside interval.", 3),
        item(r"Solve: \(|2x+1|\le9\).", r"\(-5\le x\le4\)", [r"\(x\le-5\) or \(x\ge4\)", r"\(-4\le x\le5\)", r"\(-5<x<4\)"], [r"Write the compound inequality: \(-9\le2x+1\le9\).", r"Subtract 1 from all three parts: \(-10\le2x\le8\).", r"Divide by positive 2: \(-5\le x\le4\).", r"The endpoints are included because the original used \(\le\)." ], r"forgetting the equal bar in the final answer.", 3),
        item(r"Solve: \(|x+4|>6\).", r"\(x<-10\) or \(x>2\)", [r"\(-10<x<2\)", r"\(x<2\) or \(x>-10\)", r"\(x>10\) or \(x<-2\)"], [r"Greater-than absolute value means outside the distance.", r"Split into \(x+4<-6\) or \(x+4>6\).", r"Solve each: \(x<-10\) or \(x>2\).", r"These are two outside rays, not the middle interval."], r"using AND/between for a greater-than absolute value inequality.", 3),
        item(r"Solve: \(|x-2|\ge0\).", "All real numbers", ["No solution", r"\(x\ge2\)", r"\(x=2\) only"], [r"Absolute value is always a distance.", r"A distance is always greater than or equal to 0.", r"Therefore every real value of \(x\) works.", r"For example, \(x=2\) gives 0 and \(x=10\) gives 8; both satisfy \(\ge0\)." ], r"thinking only \(x=2\) works because it makes the absolute value exactly 0.", 3),
        item(r"Solve: \(|x-2|<-1\).", "No solution", ["All real numbers", r"\(x<1\)", r"\(x>3\)"], [r"Absolute value is a distance.", r"A distance cannot be negative.", r"The inequality asks for a distance less than \(-1\).", r"That is impossible, so there is no solution."], r"splitting into cases even though the right side is negative.", 3),
        item(r"Solve: \(|3x|<12\).", r"\(-4<x<4\)", [r"\(x<-4\) or \(x>4\)", r"\(-12<x<12\)", r"\(x<4\)"], [r"Write the inside compound inequality: \(-12<3x<12\).", r"Divide all three parts by positive 3.", r"The signs stay the same.", r"The result is \(-4<x<4\)." ], r"forgetting to divide both bounds by 3.", 3),
        item(r"A gym charges \(\$25\) plus \(\$8\) per class. You can spend at most \(\$89\). Which inequality finds the number of classes \(c\)?", r"\(25+8c\le89\)", [r"\(25+8c\ge89\)", r"\(8+25c\le89\)", r"\(25c+8\le89\)"], [r"Identify the fixed fee: 25 dollars.", r"Identify the variable cost: 8 dollars per class, so \(8c\).", r"'At most 89' means \(\le89\).", r"The inequality is \(25+8c\le89\)." ], r"reversing the fixed fee and the per-class fee.", 2),
        item(r"For \(25+8c\le89\), what is the greatest whole number of classes?", r"\(8\)", [r"\(9\)", r"\(7\)", r"\(64\)"], [r"Subtract 25: \(8c\le64\).", r"Divide by 8: \(c\le8\).", r"Classes must be a whole number.", r"The greatest allowed whole number is 8."], r"choosing 9 because it is close; 9 classes costs \(25+72=97\), too much.", 2),
        item(r"Three tests must average at least \(80\). Scores are \(78\), \(84\), and \(x\). What inequality models this?", r"\(\frac{78+84+x}{3}\ge80\)", [r"\(\frac{78+84+x}{3}\le80\)", r"\(78+84+x\ge80\)", r"\(\frac{78+84}{3}\ge x\)"], [r"Average means total divided by number of scores.", r"The total is \(78+84+x\).", r"There are 3 tests, so divide by 3.", r"'At least 80' means \(\ge80\)." ], r"forgetting to divide the total by 3.", 2),
        item(r"In the test average problem \(\frac{78+84+x}{3}\ge80\), what score is needed on the third test?", r"\(x\ge78\)", [r"\(x\ge80\)", r"\(x\le78\)", r"\(x\ge162\)"], [r"Multiply both sides by 3: \(78+84+x\ge240\).", r"Combine known scores: \(162+x\ge240\).", r"Subtract 162: \(x\ge78\).", r"Check: \(78,84,78\) average to \(80\)." ], r"thinking the third score must be at least 80 even though the 84 helps the average.", 3),
        item(r"A taxi costs \(\$4\) plus \(\$2.50\) per mile. The total must be under \(\$24\). What is the solution for miles \(m\)?", r"\(m<8\)", [r"\(m>8\)", r"\(m<9.6\)", r"\(m\le8\)"], [r"Write the inequality: \(4+2.50m<24\).", r"Subtract 4: \(2.50m<20\).", r"Divide by 2.50: \(m<8\).", r"'Under 24' is strict, so 8 miles is not included."], r"using \(\le\) even though 'under' means strictly less than.", 2),
        item(r"A rectangle has width \(x\), length \(x+5\), and perimeter at most \(74\). What is the solution for \(x\)?", r"\(x\le16\)", [r"\(x\ge16\)", r"\(x\le21\)", r"\(x\le32\)"], [r"Perimeter is \(2x+2(x+5)\).", r"Write \(2x+2(x+5)\le74\).", r"Distribute and combine: \(4x+10\le74\).", r"Subtract 10 and divide by 4: \(x\le16\)." ], r"forgetting to double both the width and the length.", 3),
        item(r"A student has \(\$40\) saved and adds \(\$15\) each week. How many weeks \(w\) until the savings are at least \(\$160\)?", r"\(w\ge8\)", [r"\(w\le8\)", r"\(w\ge13\)", r"\(w\ge120\)"], [r"Write the inequality: \(40+15w\ge160\).", r"Subtract 40: \(15w\ge120\).", r"Divide by 15: \(w\ge8\).", r"'At least' includes 8 weeks."], r"dividing 160 by 15 and forgetting the 40 already saved.", 2),
        item(r"Use \(F=1.8C+32\). If \(F<68\), what is the solution for \(C\)?", r"\(C<20\)", [r"\(C>20\)", r"\(C<36\)", r"\(C>36\)"], [r"Substitute the inequality: \(1.8C+32<68\).", r"Subtract 32: \(1.8C<36\).", r"Divide by positive 1.8.", r"\(C<20\)." ], r"forgetting to subtract 32 before dividing by 1.8.", 3),
        item(r"Is \((1,4)\) a solution of \(y>2x+1\)?", "Yes", ["No", "Only on the boundary", "Cannot tell"], [r"Substitute \(x=1\) and \(y=4\).", r"The inequality becomes \(4>2(1)+1\).", r"Simplify the right side: \(4>3\).", r"This is true, so \((1,4)\) is a solution."], r"checking only the \(x\)-value and ignoring \(y\).", 2),
        item(r"Is \((4,-1)\) a solution of \(y\le -x+3\)?", "Yes", ["No", "Only if the line is dashed", "Cannot tell"], [r"Substitute \(x=4\) and \(y=-1\).", r"The right side is \(-4+3=-1\).", r"The inequality becomes \(-1\le-1\).", r"This is true because the equal bar includes boundary points."], r"forgetting that \(\le\) includes equality.", 2),
        item(r"For \(y<3x-2\), should the boundary line be solid or dashed?", "Dashed", ["Solid", "Neither", "Closed circle"], [r"Look at the inequality symbol.", r"The symbol \(<\) has no equal bar.", r"That means points on the boundary line are not included.", r"Use a dashed boundary line."], r"using a solid line for every linear inequality.", 2),
        item(r"For \(y\ge -2x+5\), should the boundary line be solid or dashed?", "Solid", ["Dashed", "Open circle", "No line"], [r"Look at the symbol \(\ge\).", r"The equal bar means boundary points are included.", r"In two-variable inequalities, included boundary lines are solid.", r"So the boundary line is solid."], r"missing the equal bar.", 2),
        item(r"Which point is a solution of \(y<x+2\)?", r"\((0,1)\)", [r"\((0,3)\)", r"\((4,7)\)", r"\((-1,2)\)"], [r"Test \((0,1)\): \(1<0+2\).", r"This simplifies to \(1<2\), true.", r"The other choices fail: \(3<2\) false, \(7<6\) false, and \(2<1\) false.", r"So \((0,1)\) is the solution point."], r"assuming a point is a solution because it is close to the boundary.", 3),
        item(r"How do you graph \(x\ge4\) in the coordinate plane?", "Solid vertical line \(x=4\), shade right", ["Dashed vertical line \(x=4\), shade right", "Solid horizontal line \(y=4\), shade above", "Dashed horizontal line \(y=4\), shade below"], [r"The inequality \(x\ge4\) has a vertical boundary line \(x=4\).", r"The equal bar means the boundary is solid.", r"Values greater than 4 are to the right of the line.", r"So draw a solid vertical line and shade right."], r"graphing it as a horizontal line because the number 4 appears alone.", 3),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Inequalities Mastery course (MCQ only)."

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
