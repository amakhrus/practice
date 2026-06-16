"""
Seed an advanced GED Algebra course on inequalities.

This course follows GED Algebra: Inequalities Mastery and raises the difficulty:
interval notation, compound and absolute-value inequalities, quadratic and
rational inequalities, systems of inequalities, and harder applications.

Run:
    python manage.py seed_ged_algebra_advanced_inequalities
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
    "title": "GED Algebra: Advanced Inequalities & Applications",
    "slug": "ged-algebra-advanced-inequalities",
    "program": "GED",
    "subject": "math",
    "description": (
        "A harder follow-up to GED Algebra: Inequalities Mastery. Students solve "
        "advanced linear inequalities, compound inequalities, absolute-value "
        "inequalities, quadratic and rational inequalities, systems of inequalities, "
        "and difficult GED-style applications. The course emphasizes interval "
        "notation, endpoint logic, sign charts, testing regions, and step-by-step "
        "reasoning."
    ),
    "lessons": [
        (
            "1. Advanced Inequality Mindset",
            r"""
Advanced inequalities are not about memorizing more symbols. They are about tracking **regions** of possible answers.

An equation usually asks, "Which value makes this exactly true?"

An inequality asks, "Which values make this comparison true?"

That means the final answer is often an interval, a union of intervals, or a shaded region.

Core habits:
- Keep the inequality balanced.
- Flip the sign only when multiplying or dividing by a negative.
- Watch whether endpoints are included.
- Test values when signs can change.
- Check the answer against the original inequality.

Example:
\[
(x-2)(x+3)>0.
\]
The expression is zero at \(x=2\) and \(x=-3\). These values split the number line into regions:
- \(x<-3\)
- \(-3<x<2\)
- \(x>2\)

Test one value in each region. The product is positive on the outside regions, so:
\[
x<-3 \quad \text{or} \quad x>2.
\]

[[figure:number_line_ineq|Advanced inequality answers are still number-line regions; the challenge is finding which regions work.]]

Common mistake: solving only the zero points and forgetting to decide where the inequality is true.

[[check:What do \(x=-3\) and \(x=2\) do for \((x-2)(x+3)>0\)?|split the number line;;make zero;;critical points|They are critical points where the expression can change sign.]]
            """,
        ),
        (
            "2. Interval Notation and Endpoint Logic",
            r"""
Interval notation is a compact way to write solution sets.

Symbols:
- Parentheses \(( \ )\): endpoint is **not** included.
- Brackets \([ \ ]\): endpoint **is** included.
- Infinity always uses parentheses: \((-\infty, 4)\), not \([-\infty, 4]\).

Examples:
\[
x>5 \quad \Longleftrightarrow \quad (5,\infty).
\]
\[
x\le -2 \quad \Longleftrightarrow \quad (-\infty,-2].
\]
\[
-3<x\le7 \quad \Longleftrightarrow \quad (-3,7].
\]
\[
x<1 \ \text{or}\ x\ge5 \quad \Longleftrightarrow \quad (-\infty,1)\cup[5,\infty).
\]

Read the endpoint before choosing a bracket:
- \(<\) or \(>\): parenthesis.
- \(\le\) or \(\ge\): bracket.

Common mistake: using brackets with infinity. Infinity is not a number you can include.

[[check:Write \(x \le 4\) in interval notation.|(-infinity,4];;(-∞,4]|Use a bracket at 4 because 4 is included.]]
            """,
        ),
        (
            "3. Tough Linear Inequalities",
            r"""
Harder linear inequalities often include parentheses on both sides, negative coefficients, or variables on both sides.

Example 1:
\[
4(2x-3)+5\ge37.
\]
Distribute and combine:
\[
8x-12+5\ge37,\qquad 8x-7\ge37.
\]
Add 7 and divide:
\[
8x\ge44,\qquad x\ge\frac{11}{2}.
\]

Example 2:
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
which means \(x\ge7\).

Example 3:
\[
5-(2x-7)>18.
\]
Distribute the negative:
\[
5-2x+7>18.
\]
Combine:
\[
12-2x>18.
\]
Subtract 12:
\[
-2x>6.
\]
Divide by \(-2\), so flip:
\[
x<-3.
\]

Common mistake: rewriting \(7\le x\) as \(x\le7\). If 7 is less than or equal to \(x\), then \(x\) is greater than or equal to 7.

[[check:Rewrite \(7\le x\) with \(x\) first.|x>=7;;x ≥ 7;;x\ge7|The x-values are 7 or greater.]]
            """,
        ),
        (
            "4. Compound Inequalities: AND and OR",
            r"""
Compound inequalities combine two conditions.

**AND** means overlap:
\[
-2\le x<5.
\]
The value must satisfy both sides.

**OR** means union:
\[
x<-2 \quad \text{or} \quad x\ge5.
\]
Either region works.

Example 1:
\[
-4\le2x+6<12.
\]
Subtract 6 from all three parts:
\[
-10\le2x<6.
\]
Divide by 2:
\[
-5\le x<3.
\]

Example 2:
\[
3x-1<5 \quad \text{or} \quad 2x+7\ge17.
\]
Solve the first:
\[
3x<6,\qquad x<2.
\]
Solve the second:
\[
2x\ge10,\qquad x\ge5.
\]
Final:
\[
x<2 \quad \text{or} \quad x\ge5.
\]

Example 3:
\[
x>1 \quad \text{and} \quad x<6
\]
becomes:
\[
1<x<6.
\]

Common mistake: changing OR into AND. OR usually gives two separated rays; AND usually gives the overlap.

[[check:Is \(x<2\) or \(x>5\) one middle interval or two outside intervals?|two outside intervals;;outside|OR keeps both separate regions.]]
            """,
        ),
        (
            "5. Absolute Value Inequalities: Inside and Outside",
            r"""
Absolute value means distance. This gives two major patterns.

Less than means **inside**:
\[
|x-a|<b \quad \Longleftrightarrow \quad a-b<x<a+b.
\]

Greater than means **outside**:
\[
|x-a|>b \quad \Longleftrightarrow \quad x<a-b \quad \text{or} \quad x>a+b.
\]

Example 1:
\[
|x-4|\le9.
\]
Inside pattern:
\[
-9\le x-4\le9.
\]
Add 4:
\[
-5\le x\le13.
\]

Example 2:
\[
|2x+1|>7.
\]
Outside pattern:
\[
2x+1<-7 \quad \text{or} \quad 2x+1>7.
\]
Solve:
\[
x<-4 \quad \text{or} \quad x>3.
\]

Example 3:
\[
3|x+2|-5<10.
\]
Add 5:
\[
3|x+2|<15.
\]
Divide:
\[
|x+2|<5.
\]
Inside pattern:
\[
-5<x+2<5.
\]
Subtract 2:
\[
-7<x<3.
\]

Common mistake: applying the inside pattern before isolating the absolute value expression.

[[check:For \(|x-4|\le9\), is the solution inside or outside?|inside|Less than or equal means within the distance.]]
            """,
        ),
        (
            "6. Quadratic Inequalities",
            r"""
A quadratic inequality has an \(x^2\) term. The solution is found by looking where the parabola is above or below the x-axis.

[[figure:parabola|A quadratic changes sign at its roots; the inequality asks which side of the x-axis works.]]

Example 1:
\[
x^2-9>0.
\]
Factor:
\[
(x-3)(x+3)>0.
\]
Critical points: \(-3\) and \(3\). Test regions:
- \(x<-3\): choose \(-4\), product positive.
- \(-3<x<3\): choose \(0\), product negative.
- \(x>3\): choose \(4\), product positive.

So:
\[
x<-3 \quad \text{or} \quad x>3.
\]

Example 2:
\[
x^2-5x+6\le0.
\]
Factor:
\[
(x-2)(x-3)\le0.
\]
The product is zero at 2 and 3 and negative between them, so:
\[
2\le x\le3.
\]

Rule of thumb for an upward-opening quadratic:
- \(>0\): outside the roots.
- \(<0\): between the roots.
Adjust endpoints for \(\le\) or \(\ge\).

Common mistake: giving only the roots. The roots are boundaries, not the whole solution.

[[check:For \(x^2-9>0\), are the solutions between or outside \(-3\) and \(3\)?|outside|The product is positive outside the roots.]]
            """,
        ),
        (
            "7. Sign Charts for Products",
            r"""
A sign chart tracks whether each factor is positive or negative in each interval.

Example:
\[
(x-1)(x+2)(x-4)\ge0.
\]
Critical points:
\[
x=-2,\quad x=1,\quad x=4.
\]
They split the number line:
- \((-\infty,-2)\)
- \((-2,1)\)
- \((1,4)\)
- \((4,\infty)\)

Test one value in each interval:
- \(x=-3\): \((-)(-)(-)\) = negative.
- \(x=0\): \((-)(+)(-)\) = positive.
- \(x=2\): \((+)(+)(-)\) = negative.
- \(x=5\): \((+)(+)(+)\) = positive.

Because the inequality is \(\ge0\), include positive intervals and zero points:
\[
[-2,1]\cup[4,\infty).
\]

Repeated factors matter. For \((x-2)^2\), the sign does not change when crossing \(x=2\), because a square is never negative.

Common mistake: assuming signs alternate every time. They alternate at simple roots, but not at even powers.

[[check:Does \((x-2)^2\) change sign at \(x=2\)?|no|An even-powered factor touches zero but stays nonnegative.]]
            """,
        ),
        (
            "8. Rational Inequalities",
            r"""
A rational inequality has a variable in a denominator. Denominators create **excluded values**.

Example 1:
\[
\frac{x-3}{x+2}>0.
\]
Critical values:
- Numerator zero: \(x=3\).
- Denominator zero: \(x=-2\), excluded.

Test intervals:
- \(x<-2\): choose \(-3\), fraction positive.
- \(-2<x<3\): choose \(0\), fraction negative.
- \(x>3\): choose \(4\), fraction positive.

Since the inequality is \(>0\), do not include \(x=3\). Never include \(x=-2\). Final:
\[
(-\infty,-2)\cup(3,\infty).
\]

Example 2:
\[
\frac{x+1}{x-4}\le0.
\]
Critical values: \(-1\) and \(4\). The fraction is negative between them. Include \(-1\) because it makes the numerator zero, but exclude \(4\) because it makes the denominator zero:
\[
[-1,4).
\]

Common mistake: multiplying both sides by a variable denominator without knowing whether it is positive or negative. Use a sign chart instead.

[[check:Can a denominator zero ever be included in a solution?|no|Division by zero is undefined.]]
            """,
        ),
        (
            "9. Systems of Inequalities",
            r"""
A system of inequalities asks for points that satisfy all inequalities at the same time. The solution is the overlapping shaded region.

Example 1:
\[
y>2x+1,\qquad y\le -x+7.
\]
Test a point by substituting into both inequalities. Try \((1,4)\):
\[
4>2(1)+1 \Rightarrow 4>3,
\]
true.
\[
4\le -1+7 \Rightarrow 4\le6,
\]
true.
So \((1,4)\) is a solution.

Graphing rules:
- Dashed line for \(<\) or \(>\).
- Solid line for \(\le\) or \(\ge\).
- Shade above for \(y>\) or \(y\ge\).
- Shade below for \(y<\) or \(y\le\).
- The answer is where the shading overlaps.

[[figure:coord_line|A boundary line helps divide the plane; a system uses overlapping shaded regions.]]

Example 2:
\[
x\ge0,\qquad y\ge0,\qquad x+y\le10.
\]
This describes a triangular region in the first quadrant under the line \(x+y=10\).

Common mistake: checking only one inequality in a system. A point must satisfy every inequality.

[[check:For a system of inequalities, must a point satisfy one inequality or all of them?|all;;all of them|The solution is the overlap of all conditions.]]
            """,
        ),
        (
            "10. Inequality Word Problems with Constraints",
            r"""
Advanced word problems often include a practical restriction: whole numbers, nonnegative values, capacity, budget, or minimum requirements.

Example 1:
A truck can carry at most 1200 lb. Each box weighs 45 lb. There is already 300 lb loaded. How many more boxes \(b\) can be loaded?
\[
300+45b\le1200.
\]
Subtract:
\[
45b\le900.
\]
Divide:
\[
b\le20.
\]
Because boxes are whole items, the maximum is 20 boxes.

Example 2:
A student needs an average of at least 85 on four tests. The first three scores are 82, 87, and 90.
\[
\frac{82+87+90+x}{4}\ge85.
\]
Multiply:
\[
259+x\ge340.
\]
Subtract:
\[
x\ge81.
\]

Example 3:
A plan charges 12 dollars plus 0.08 dollars per minute. The bill must be under 30 dollars:
\[
12+0.08m<30.
\]
Solve:
\[
0.08m<18,\qquad m<225.
\]

Common mistake: ignoring whole-number restrictions. If the answer is \(b\le20.7\) boxes, the maximum whole number is 20, not 21.

[[check:If boxes must be whole and \(b\le20.7\), what is the greatest number of boxes?|20|You cannot load 0.7 of a box.]]
            """,
        ),
        (
            "11. Advanced Percent and Rate Inequalities",
            r"""
Percent and rate inequalities require careful setup.

Example 1 - tax:
After 8 percent tax, the total must be at most 54 dollars.
\[
1.08p\le54.
\]
Divide:
\[
p\le50.
\]

Example 2 - discount:
A sale price is 75 percent of the original price. The sale price must be under 60 dollars.
\[
0.75p<60.
\]
Divide:
\[
p<80.
\]

Example 3 - hourly rate:
A worker charges 50 dollars plus 18 dollars per hour. The total must be at least 194 dollars:
\[
50+18h\ge194.
\]
Solve:
\[
18h\ge144,\qquad h\ge8.
\]

Example 4 - speed:
A trip must be more than 180 miles in 3 hours. If speed is \(r\):
\[
3r>180.
\]
Divide:
\[
r>60.
\]

Common mistake: using \(0.08p\le54\) for tax total. Tax total after an 8 percent increase is \(1.08p\), not \(0.08p\).

[[check:After an 8 percent increase, what multiplier do you use?|1.08|Original plus 8 percent is 108 percent, or 1.08.]]
            """,
        ),
        (
            "12. Final Strategy: Test Regions and Check",
            r"""
For advanced inequalities, the final answer is only trustworthy if it passes a test.

Checklist:
- Did you flip the sign only when multiplying or dividing by a negative?
- Did you include endpoints only for \(\le\) or \(\ge\)?
- Did you exclude denominator zeros?
- Did you split absolute value correctly?
- Did you test each region for quadratic or rational inequalities?
- Did you apply word-problem restrictions like whole numbers or nonnegative values?

Example:
\[
\frac{x-1}{x+3}\ge0.
\]
Critical values:
\[
x=1,\quad x=-3.
\]
The value \(x=-3\) is excluded because it makes the denominator zero.

Test regions:
- \(x<-3\): choose \(-4\), fraction positive.
- \(-3<x<1\): choose \(0\), fraction negative.
- \(x>1\): choose \(2\), fraction positive.

Because \(\ge0\), include \(x=1\) but not \(x=-3\):
\[
(-\infty,-3)\cup[1,\infty).
\]

Final habit: if your answer is an interval, pick one number inside it and one number outside it. The inside number should work; the outside number should fail.

Common mistake: including every critical point. Numerator zeros may be included for \(\le\) or \(\ge\), but denominator zeros are never included.

[[check:In \(\frac{x-1}{x+3}\ge0\), why is \(-3\) excluded?|denominator zero;;undefined|At \(x=-3\), the denominator is zero, so the expression is undefined.]]
            """,
        ),
    ],
    "mcqs": [
        item(r"Write \(x>5\) in interval notation.", r"\((5,\infty)\)", [r"\([5,\infty)\)", r"\((-\infty,5)\)", r"\((5,\infty]\)"], [r"The inequality \(x>5\) means values greater than 5.", r"Because 5 is not included, use a parenthesis at 5.", r"The interval goes to positive infinity.", r"The answer is \((5,\infty)\)."], r"using a bracket at 5 even though \(>\) does not include the endpoint.", 2),
        item(r"Write \(x\le -2\) in interval notation.", r"\((-\infty,-2]\)", [r"\((-\infty,-2)\)", r"\([-2,\infty)\)", r"\([-\infty,-2]\)"], [r"The inequality includes all numbers less than or equal to \(-2\).", r"The interval starts at negative infinity and ends at \(-2\).", r"Use a bracket at \(-2\) because it is included.", r"Use a parenthesis with infinity."], r"putting a bracket on infinity; infinity is not a number that can be included.", 2),
        item(r"Write \(-3<x\le7\) in interval notation.", r"\((-3,7]\)", [r"\([-3,7]\)", r"\((-3,7)\)", r"\([-3,7)\)"], [r"The left endpoint is \(-3\).", r"Since \(-3<x\), \(-3\) is not included, so use a parenthesis.", r"Since \(x\le7\), 7 is included, so use a bracket.", r"The interval is \((-3,7]\)."], r"making both endpoints open or both endpoints closed.", 2),
        item(r"Write \(x<1\) or \(x\ge5\) in interval notation.", r"\((-\infty,1)\cup[5,\infty)\)", [r"\((1,5]\)", r"\((-\infty,1]\cup(5,\infty)\)", r"\([1,5)\)"], [r"The part \(x<1\) is \((-\infty,1)\).", r"The part \(x\ge5\) is \([5,\infty)\).", r"OR means union, so connect the intervals with \(\cup\).", r"The answer is \((-\infty,1)\cup[5,\infty)\)."], r"turning OR into the middle interval between 1 and 5.", 3),
        item(r"Which interval notation means \(x\) is at least 4?", r"\([4,\infty)\)", [r"\((4,\infty)\)", r"\((-\infty,4]\)", r"\((-\infty,4)\)"], [r"'At least 4' means \(x\ge4\).", r"The endpoint 4 is included, so use a bracket.", r"Values greater than 4 go toward positive infinity.", r"The interval is \([4,\infty)\)."], r"using a parenthesis and excluding 4.", 2),
        item(r"Solve: \(4(2x-3)+5\ge37\).", r"\(x\ge\frac{11}{2}\)", [r"\(x\le\frac{11}{2}\)", r"\(x\ge5\)", r"\(x\ge4\)"], [r"Distribute: \(8x-12+5\ge37\).", r"Combine constants: \(8x-7\ge37\).", r"Add 7: \(8x\ge44\).", r"Divide by positive 8: \(x\ge\frac{11}{2}\)."], r"rounding \(5.5\) to 5 or flipping the sign without a negative division.", 3),
        item(r"Solve: \(8-2x\le x-13\).", r"\(x\ge7\)", [r"\(x\le7\)", r"\(x\ge-7\)", r"\(x\le-7\)"], [r"Add \(2x\) to both sides: \(8\le3x-13\).", r"Add 13 to both sides: \(21\le3x\).", r"Divide by 3: \(7\le x\).", r"Rewrite with \(x\) first: \(x\ge7\)."], r"rewriting \(7\le x\) as \(x\le7\).", 3),
        item(r"Solve: \(5-(2x-7)>18\).", r"\(x<-3\)", [r"\(x>-3\)", r"\(x<3\)", r"\(x>3\)"], [r"Distribute the minus sign: \(5-2x+7>18\).", r"Combine constants: \(12-2x>18\).", r"Subtract 12: \(-2x>6\).", r"Divide by \(-2\) and flip: \(x<-3\)."], r"forgetting the sign flip when dividing by \(-2\).", 3),
        item(r"Solve: \(3(2x+5)-4(x-1)<29\).", r"\(x<5\)", [r"\(x>5\)", r"\(x<7\)", r"\(x>7\)"], [r"Distribute: \(6x+15-4x+4<29\).", r"Combine: \(2x+19<29\).", r"Subtract 19: \(2x<10\).", r"Divide by 2: \(x<5\)."], r"distributing \(-4(x-1)\) as \(-4x-4\).", 3),
        item(r"Solve: \(7x-2(3x+5)\ge12\).", r"\(x\ge22\)", [r"\(x\le22\)", r"\(x\ge2\)", r"\(x\ge12\)"], [r"Distribute: \(7x-6x-10\ge12\).", r"Combine: \(x-10\ge12\).", r"Add 10 to both sides.", r"The result is \(x\ge22\)."], r"turning \(-2(3x+5)\) into \(-6x+10\).", 3),
        item(r"Solve: \(-4(x+2)+3x\le10\).", r"\(x\ge-18\)", [r"\(x\le-18\)", r"\(x\ge18\)", r"\(x\le18\)"], [r"Distribute: \(-4x-8+3x\le10\).", r"Combine: \(-x-8\le10\).", r"Add 8: \(-x\le18\).", r"Divide by \(-1\) and flip: \(x\ge-18\)."], r"forgetting the flip after dividing by \(-1\).", 3),
        item(r"Solve: \(2[3x-(x+4)]>16\).", r"\(x>6\)", [r"\(x<6\)", r"\(x>4\)", r"\(x>8\)"], [r"Simplify inside brackets: \(3x-(x+4)=2x-4\).", r"Multiply by 2: \(4x-8>16\).", r"Add 8: \(4x>24\).", r"Divide by 4: \(x>6\)."], r"forgetting the minus sign before \(x+4\).", 3),
        item(r"Solve: \(6-(x+2)\ge1\).", r"\(x\le3\)", [r"\(x\ge3\)", r"\(x\le7\)", r"\(x\ge7\)"], [r"Distribute the minus: \(6-x-2\ge1\).", r"Combine: \(4-x\ge1\).", r"Subtract 4: \(-x\ge-3\).", r"Divide by \(-1\) and flip: \(x\le3\)."], r"writing \(6-(x+2)\) as \(6-x+2\).", 3),
        item(r"Solve: \(-4\le2x+6<12\).", r"\(-5\le x<3\)", [r"\(-5<x\le3\)", r"\(-2\le x<6\)", r"\(-10\le x<6\)"], [r"Subtract 6 from all three parts: \(-10\le2x<6\).", r"Divide all three parts by positive 2.", r"The inequality signs keep their directions.", r"The result is \(-5\le x<3\)."], r"forgetting which endpoint has the equal bar.", 3),
        item(r"Solve: \(3x-1<5\) or \(2x+7\ge17\).", r"\(x<2\) or \(x\ge5\)", [r"\(2<x<5\)", r"\(x<5\) or \(x\ge2\)", r"\(x\le2\) and \(x>5\)"], [r"Solve the first inequality: \(3x-1<5\), so \(3x<6\), and \(x<2\).", r"Solve the second inequality: \(2x+7\ge17\), so \(2x\ge10\), and \(x\ge5\).", r"Keep the OR connector.", r"The solution is \(x<2\) or \(x\ge5\)."], r"turning OR into the middle interval.", 3),
        item(r"Solve: \(1<\frac{x+3}{2}\le5\).", r"\(-1<x\le7\)", [r"\(-1\le x<7\)", r"\(2<x\le10\)", r"\(-5<x\le3\)"], [r"Multiply all three parts by positive 2: \(2<x+3\le10\).", r"Subtract 3 from all three parts.", r"The result is \(-1<x\le7\).", r"Keep the left endpoint open and the right endpoint closed."], r"changing the endpoint types while solving.", 3),
        item(r"Which interval matches \(x\le -4\) or \(x>3\)?", r"\((-\infty,-4]\cup(3,\infty)\)", [r"\([-4,3)\)", r"\((-\infty,-4)\cup[3,\infty)\)", r"\((-4,3]\)"], [r"The part \(x\le-4\) becomes \((-\infty,-4]\).", r"The part \(x>3\) becomes \((3,\infty)\).", r"OR means union.", r"The correct interval is \((-\infty,-4]\cup(3,\infty)\)."], r"turning two rays into the middle interval.", 3),
        item(r"Solve: \(-6< -2x+4\le10\).", r"\(-3\le x<5\)", [r"\(-5<x\le3\)", r"\(-3<x\le5\)", r"\(x<-3\) or \(x\ge5\)"], [r"Subtract 4 from all three parts: \(-10<-2x\le6\).", r"Divide all three parts by \(-2\), so both inequality directions reverse.", r"The result is \(5>x\ge-3\).", r"Rewrite in increasing order: \(-3\le x<5\)."], r"forgetting to reverse both inequality signs when dividing by \(-2\).", 3),
        item(r"Solve: \(4\le3x-2<13\).", r"\(2\le x<5\)", [r"\(2<x\le5\)", r"\(6\le x<15\)", r"\(x\le2\) or \(x>5\)"], [r"Add 2 to all three parts: \(6\le3x<15\).", r"Divide by positive 3.", r"The result is \(2\le x<5\).", r"The left endpoint is included; the right is not."], r"not preserving the endpoint inclusion.", 2),
        item(r"Solve: \(x>1\) and \(x\le6\).", r"\((1,6]\)", [r"\((-\infty,1)\cup[6,\infty)\)", r"\([1,6)\)", r"\((1,6)\)"], [r"AND means overlap.", r"The values must be greater than 1 and less than or equal to 6.", r"That interval starts open at 1 and closed at 6.", r"The answer is \((1,6]\)."], r"treating AND as OR.", 2),
        item(r"Solve: \(|x-4|\le9\).", r"\(-5\le x\le13\)", [r"\(x\le-5\) or \(x\ge13\)", r"\(-13\le x\le5\)", r"\(-5<x<13\)"], [r"Less-than-or-equal absolute value means inside.", r"Write \(-9\le x-4\le9\).", r"Add 4 to all three parts.", r"The result is \(-5\le x\le13\)."], r"using outside intervals for a less-than absolute value inequality.", 3),
        item(r"Solve: \(|2x+1|>7\).", r"\(x<-4\) or \(x>3\)", [r"\(-4<x<3\)", r"\(x<3\) or \(x>-4\)", r"\(x\le-4\) or \(x\ge3\)"], [r"Greater-than absolute value means outside.", r"Split into \(2x+1<-7\) or \(2x+1>7\).", r"Solve: \(2x<-8\) gives \(x<-4\), and \(2x>6\) gives \(x>3\).", r"The final answer is \(x<-4\) or \(x>3\)."], r"using the inside interval \(-4<x<3\).", 3),
        item(r"Solve: \(3|x+2|-5<10\).", r"\(-7<x<3\)", [r"\(x<-7\) or \(x>3\)", r"\(-3<x<7\)", r"\(-5<x<5\)"], [r"Isolate the absolute value: add 5 to get \(3|x+2|<15\).", r"Divide by 3: \(|x+2|<5\).", r"Write \(-5<x+2<5\).", r"Subtract 2 to get \(-7<x<3\)."], r"splitting the absolute value before isolating it.", 3),
        item(r"Solve: \(|x-6|\ge4\).", r"\(x\le2\) or \(x\ge10\)", [r"\(2\le x\le10\)", r"\(x<2\) or \(x>10\)", r"\(-10\le x\le2\)"], [r"Greater-than-or-equal absolute value means outside.", r"Set \(x-6\le-4\) or \(x-6\ge4\).", r"Solve to get \(x\le2\) or \(x\ge10\).", r"The endpoints are included because the symbol is \(\ge\)."], r"using the inside interval instead of outside rays.", 3),
        item(r"Solve: \(|3x-2|<10\).", r"\(-\frac{8}{3}<x<4\)", [r"\(x<-\frac{8}{3}\) or \(x>4\)", r"\(-4<x<\frac{8}{3}\)", r"\(-8<x<12\)"], [r"Write the inside compound inequality: \(-10<3x-2<10\).", r"Add 2 to all three parts: \(-8<3x<12\).", r"Divide by positive 3.", r"The result is \(-\frac{8}{3}<x<4\)."], r"forgetting to divide both bounds by 3.", 3),
        item(r"Solve: \(2|x-1|+3\le11\).", r"\(-3\le x\le5\)", [r"\(x\le-3\) or \(x\ge5\)", r"\(-5\le x\le3\)", r"\(-4\le x\le4\)"], [r"Subtract 3: \(2|x-1|\le8\).", r"Divide by 2: \(|x-1|\le4\).", r"Write \(-4\le x-1\le4\).", r"Add 1: \(-3\le x\le5\)."], r"forgetting to isolate the absolute value before making the compound inequality.", 3),
        item(r"Solve: \(|x+5|<-2\).", "No solution", ["All real numbers", r"\(-7<x<-3\)", r"\(x<-7\) or \(x>-3\)"], [r"Absolute value is a distance.", r"A distance cannot be less than a negative number.", r"Since the right side is \(-2\), the inequality is impossible.", r"Therefore there is no solution."], r"solving as if the right side were positive 2.", 3),
        item(r"Solve: \(|x-3|>0\).", r"\(x\ne3\)", ["All real numbers", r"\(x=3\)", "No solution"], [r"Absolute value is greater than 0 whenever the inside is not 0.", r"Set the inside equal to 0 to find the excluded value: \(x-3=0\).", r"So \(x=3\) makes the absolute value 0.", r"All real numbers except 3 work."], r"saying all real numbers, even though \(x=3\) gives 0, not greater than 0.", 3),
        item(r"Solve: \(x^2-9>0\).", r"\(x<-3\) or \(x>3\)", [r"\(-3<x<3\)", r"\(x=-3\) or \(x=3\)", r"\(x\le-3\) or \(x\ge3\)"], [r"Factor: \(x^2-9=(x-3)(x+3)\).", r"The critical points are \(-3\) and \(3\).", r"The product is positive outside the roots.", r"Because the symbol is \(>\), do not include the endpoints."], r"giving only the roots or including the roots for a strict inequality.", 3),
        item(r"Solve: \(x^2-5x+6\le0\).", r"\(2\le x\le3\)", [r"\(x\le2\) or \(x\ge3\)", r"\(2<x<3\)", r"\(x=-2\) or \(x=-3\)"], [r"Factor: \(x^2-5x+6=(x-2)(x-3)\).", r"The roots are 2 and 3.", r"For an upward-opening quadratic, the expression is negative between the roots.", r"Because the symbol is \(\le\), include the roots: \(2\le x\le3\)."], r"using outside intervals for a less-than quadratic.", 3),
        item(r"Solve: \(x^2+4x+3\ge0\).", r"\(x\le-3\) or \(x\ge-1\)", [r"\(-3\le x\le-1\)", r"\(x<-3\) or \(x>-1\)", r"\(x\le1\) or \(x\ge3\)"], [r"Factor: \(x^2+4x+3=(x+3)(x+1)\).", r"The roots are \(-3\) and \(-1\).", r"The upward-opening quadratic is nonnegative outside the roots.", r"Include the endpoints because the symbol is \(\ge\)." ], r"forgetting that \(\ge0\) includes zeros.", 3),
        item(r"Solve: \(x^2-4x<0\).", r"\(0<x<4\)", [r"\(x<0\) or \(x>4\)", r"\(0\le x\le4\)", r"\(x=0\) or \(x=4\)"], [r"Factor: \(x^2-4x=x(x-4)\).", r"The roots are 0 and 4.", r"The product is negative between the roots.", r"Because the symbol is strict \(<\), do not include 0 or 4."], r"including endpoints for a strict inequality.", 3),
        item(r"Solve: \((x-1)(x+2)(x-4)\ge0\).", r"\([-2,1]\cup[4,\infty)\)", [r"\((-\infty,-2]\cup[1,4]\)", r"\((-2,1)\cup(4,\infty)\)", r"\([1,4]\)"], [r"The critical points are \(-2\), \(1\), and \(4\).", r"Test the intervals split by those points.", r"The product is positive on \((-2,1)\) and \((4,\infty)\).", r"Include the critical points because the inequality is \(\ge0\)." ], r"assuming the positive intervals are always outside only; with three factors, signs alternate across each simple root.", 3),
        item(r"Solve: \((x-2)^2(x+1)<0\).", r"\(x<-1\)", [r"\(-1<x<2\)", r"\(x<2\)", r"\(x<-1\) or \(x>2\)"], [r"The squared factor \((x-2)^2\) is never negative.", r"The sign is controlled by \(x+1\), except at \(x=2\), where the product is zero.", r"For the product to be negative, \(x+1<0\), so \(x<-1\).", r"The point \(x=2\) is not in \(x<-1\), so no extra exclusion is needed."], r"thinking the sign changes at \(x=2\), even though the factor is squared.", 3),
        item(r"Solve: \(-x^2+4>0\).", r"\(-2<x<2\)", [r"\(x<-2\) or \(x>2\)", r"\(-2\le x\le2\)", r"\(x=2\) or \(x=-2\)"], [r"Rewrite: \(-x^2+4>0\) means \(4>x^2\).", r"So \(x^2<4\).", r"The numbers whose squares are less than 4 are between \(-2\) and \(2\).", r"The endpoints are not included because the inequality is strict."], r"using outside intervals as if the leading coefficient were positive.", 3),
        item(r"Solve: \(x^2+2x-8\le0\).", r"\(-4\le x\le2\)", [r"\(x\le-4\) or \(x\ge2\)", r"\(-4<x<2\)", r"\(-2\le x\le4\)"], [r"Factor: \(x^2+2x-8=(x+4)(x-2)\).", r"The roots are \(-4\) and \(2\).", r"An upward-opening quadratic is below or equal to zero between the roots.", r"Include endpoints because the symbol is \(\le\)." ], r"using the factor numbers 4 and -2 as roots without changing signs.", 3),
        item(r"Solve: \(\frac{x-3}{x+2}>0\).", r"\((-\infty,-2)\cup(3,\infty)\)", [r"\((-2,3)\)", r"\((-\infty,-2]\cup[3,\infty)\)", r"\([-2,3]\)"], [r"Critical values are \(x=3\) from the numerator and \(x=-2\) from the denominator.", r"The denominator value \(-2\) is excluded.", r"Test intervals: the fraction is positive on \((-\infty,-2)\) and \((3,\infty)\).", r"Because the symbol is \(>0\), \(x=3\) is not included either."], r"including the denominator zero or using the middle negative interval.", 3),
        item(r"Solve: \(\frac{x+1}{x-4}\le0\).", r"\([-1,4)\)", [r"\((-1,4]\)", r"\((-\infty,-1]\cup(4,\infty)\)", r"\([-1,4]\)"], [r"Critical values are \(x=-1\) and \(x=4\).", r"The numerator zero \(-1\) can be included because the inequality allows zero.", r"The denominator zero \(4\) must be excluded.", r"The fraction is negative between \(-1\) and \(4\), so the solution is \([-1,4)\)." ], r"including \(4\), which makes the expression undefined.", 3),
        item(r"Solve: \(\frac{2x-6}{x+5}\ge0\).", r"\((-\infty,-5)\cup[3,\infty)\)", [r"\((-5,3]\)", r"\((-\infty,-5]\cup[3,\infty)\)", r"\([ -5,3]\)"], [r"Find critical values: numerator zero at \(x=3\); denominator zero at \(x=-5\).", r"Exclude \(x=-5\).", r"Test intervals: the fraction is positive on \((-\infty,-5)\) and \((3,\infty)\).", r"Include \(x=3\) because the inequality is \(\ge0\)." ], r"including the denominator zero at \(-5\).", 3),
        item(r"Solve: \(\frac{x}{x-2}<1\).", r"\((-\infty,2)\)", [r"\((2,\infty)\)", r"\((-\infty,2]\)", r"\((0,2)\)"], [r"Move 1 to the left: \(\frac{x}{x-2}-1<0\).", r"Use a common denominator: \(\frac{x-(x-2)}{x-2}<0\).", r"Simplify: \(\frac{2}{x-2}<0\).", r"Since the numerator is positive, the fraction is negative when \(x-2<0\), so \(x<2\). Exclude 2."], r"multiplying by \(x-2\) without knowing its sign.", 3),
        item(r"Solve: \(\frac{x-1}{x+3}\ge0\).", r"\((-\infty,-3)\cup[1,\infty)\)", [r"\((-3,1]\)", r"\((-\infty,-3]\cup[1,\infty)\)", r"\([-3,1]\)"], [r"Critical values are \(x=1\) and \(x=-3\).", r"Exclude \(x=-3\) because it makes the denominator zero.", r"Test intervals: the fraction is nonnegative on \((-\infty,-3)\) and \([1,\infty)\).", r"Include \(x=1\), where the numerator is zero."], r"including the denominator zero.", 3),
        item(r"Solve: \(\frac{(x-2)(x+1)}{x-4}>0\).", r"\((-1,2)\cup(4,\infty)\)", [r"\((-\infty,-1)\cup(2,4)\)", r"\([-1,2]\cup(4,\infty)\)", r"\((-1,4)\)"], [r"Critical values are \(-1\), \(2\), and \(4\).", r"The value \(4\) is excluded because it is a denominator zero.", r"Test intervals split by those points.", r"The expression is positive on \((-1,2)\) and \((4,\infty)\); endpoints are not included because the inequality is strict."], r"including numerator zeros for a strict \(>0\) inequality.", 3),
        item(r"Is \((1,4)\) a solution of \(y>2x+1\) and \(y\le -x+7\)?", "Yes", ["No", "Only for the first inequality", "Only for the second inequality"], [r"Test the first inequality: \(4>2(1)+1\), so \(4>3\), true.", r"Test the second inequality: \(4\le-1+7\), so \(4\le6\), true.", r"A system solution must satisfy both inequalities.", r"Since both are true, \((1,4)\) is a solution."], r"checking only one inequality in the system.", 2),
        item(r"Which point satisfies \(x\ge0\), \(y\ge0\), and \(x+y\le10\)?", r"\((3,4)\)", [r"\((-1,4)\)", r"\((6,7)\)", r"\((4,-1)\)"], [r"Check \((3,4)\): both coordinates are nonnegative.", r"Check the sum: \(3+4=7\le10\).", r"The other choices fail either nonnegative constraints or the sum constraint.", r"So \((3,4)\) works."], r"checking only \(x+y\le10\) and ignoring first-quadrant constraints.", 2),
        item(r"For \(y\ge -2x+5\), should the boundary line be solid or dashed?", "Solid", ["Dashed", "No boundary", "Open circle"], [r"The symbol \(\ge\) includes equality.", r"Points on the boundary line \(y=-2x+5\) are included.", r"Included boundary lines are solid.", r"So the line is solid."], r"using dashed lines for every inequality.", 2),
        item(r"For \(y<3x-2\), which side of the boundary line is shaded?", "Below", ["Above", "On the line only", "Neither side"], [r"The inequality is already solved for \(y\).", r"The symbol is \(<\), meaning y-values less than the line.", r"Less y-values are below the boundary line.", r"So shade below."], r"shading above because the slope is positive.", 2),
        item(r"Which point satisfies \(y< x+2\)?", r"\((0,1)\)", [r"\((0,3)\)", r"\((4,7)\)", r"\((-1,2)\)"], [r"Test \((0,1)\): \(1<0+2\), so \(1<2\), true.", r"Test \((0,3)\): \(3<2\), false.", r"Test \((4,7)\): \(7<6\), false.", r"Test \((-1,2)\): \(2<1\), false."], r"assuming a point near the line automatically works.", 2),
        item(r"Graph \(x<4\) in the coordinate plane.", "Dashed vertical line \(x=4\), shade left", ["Solid vertical line \(x=4\), shade left", "Dashed horizontal line \(y=4\), shade below", "Solid horizontal line \(y=4\), shade right"], [r"The boundary is \(x=4\), a vertical line.", r"The symbol \(<\) has no equal bar, so the line is dashed.", r"Values with \(x<4\) are to the left of the line.", r"So use a dashed vertical line and shade left."], r"graphing \(x<4\) as a horizontal line.", 3),
        item(r"A truck can carry at most 1200 lb. It already has 300 lb, and each box is 45 lb. What is the greatest number of boxes?", r"\(20\)", [r"\(21\)", r"\(26\)", r"\(33\)"], [r"Write \(300+45b\le1200\).", r"Subtract 300: \(45b\le900\).", r"Divide by 45: \(b\le20\).", r"Because boxes are whole, the maximum is 20 boxes."], r"rounding up in a capacity problem; 21 boxes would exceed the limit.", 3),
        item(r"A student needs an average of at least 85 on four tests. Scores are 82, 87, 90, and \(x\). What score is needed?", r"\(x\ge81\)", [r"\(x\ge85\)", r"\(x\le81\)", r"\(x\ge259\)"], [r"Write \(\frac{82+87+90+x}{4}\ge85\).", r"Multiply by 4: \(259+x\ge340\).", r"Subtract 259: \(x\ge81\).", r"Check: \(82+87+90+81=340\), and \(340/4=85\)." ], r"thinking the last score must be at least 85 even though earlier scores can help.", 3),
        item(r"A phone plan costs 12 dollars plus 0.08 dollars per minute. The bill must be under 30 dollars. What is \(m\)?", r"\(m<225\)", [r"\(m\le225\)", r"\(m<18\)", r"\(m>225\)"], [r"Write \(12+0.08m<30\).", r"Subtract 12: \(0.08m<18\).", r"Divide by 0.08: \(m<225\).", r"Use strict \(<\) because the bill must be under 30, not at most 30."], r"using \(\le\) when the wording says under.", 3),
        item(r"After 8 percent tax, the total must be at most 54 dollars. What is the greatest pre-tax price \(p\)?", r"\(p\le50\)", [r"\(p\le54\)", r"\(p\le46\)", r"\(p\ge50\)"], [r"After 8 percent tax, total is \(1.08p\).", r"Write \(1.08p\le54\).", r"Divide by 1.08: \(p\le50\).", r"Check: \(50+8\%\text{ of }50=54\)." ], r"using \(0.08p\le54\), which represents only the tax amount, not the total.", 3),
        item(r"A sale price is 75 percent of the original price and must be under 60 dollars. What original prices \(p\) work?", r"\(p<80\)", [r"\(p>80\)", r"\(p<45\)", r"\(p\le80\)"], [r"Sale price is \(0.75p\).", r"Write \(0.75p<60\).", r"Divide by 0.75: \(p<80\).", r"Strict inequality remains strict because the sale price must be under 60."], r"finding 75 percent of 60 instead of solving for the original price.", 3),
        item(r"A worker charges 50 dollars plus 18 dollars per hour. The total must be at least 194 dollars. What is \(h\)?", r"\(h\ge8\)", [r"\(h\le8\)", r"\(h\ge10.8\)", r"\(h\ge144\)"], [r"Write \(50+18h\ge194\).", r"Subtract 50: \(18h\ge144\).", r"Divide by 18: \(h\ge8\).", r"'At least' includes 8."], r"dividing 194 by 18 and ignoring the 50 dollar fixed charge.", 2),
        item(r"A trip must be more than 180 miles in 3 hours. What average speed \(r\) is needed?", r"\(r>60\)", [r"\(r\ge60\)", r"\(r<60\)", r"\(r>180\)"], [r"Distance equals rate times time.", r"Write \(3r>180\).", r"Divide by 3: \(r>60\).", r"Use \(>\), not \(\ge\), because the trip must be more than 180 miles."], r"using \(\ge\) even though 'more than' is strict.", 2),
        item(r"A rectangle width is \(x\), length is \(2x+1\), and perimeter is less than 50. What is the solution?", r"\(x<8\)", [r"\(x>8\)", r"\(x<\frac{49}{6}\)", r"\(x<16\)"], [r"Perimeter is \(2w+2l\), so \(2x+2(2x+1)<50\).", r"Distribute: \(2x+4x+2<50\).", r"Combine: \(6x+2<50\).", r"Subtract 2 and divide by 6: \(x<8\)." ], r"forgetting to double the length and width.", 3),
        item(r"A class needs at least 240 total points from 4 quizzes. The first three scores are 55, 62, and 58. What is needed on quiz 4?", r"\(x\ge65\)", [r"\(x\ge60\)", r"\(x\le65\)", r"\(x\ge175\)"], [r"Write \(55+62+58+x\ge240\).", r"Combine known scores: \(175+x\ge240\).", r"Subtract 175.", r"The result is \(x\ge65\)."], r"dividing by 4 even though the problem asks for total points, not average.", 3),
        item(r"A package must weigh no more than 70 lb. The box weighs 4 lb, and each item weighs 3 lb. What is the greatest number of items?", r"\(22\)", [r"\(23\)", r"\(24\)", r"\(21\)"], [r"Write \(4+3n\le70\).", r"Subtract 4: \(3n\le66\).", r"Divide by 3: \(n\le22\).", r"The greatest whole number is 22."], r"rounding up beyond the weight limit.", 2),
        item(r"A monthly budget is at most 500 dollars. Rent is 320 dollars, and each trip costs 12 dollars. What is \(t\)?", r"\(t\le15\)", [r"\(t\le41\)", r"\(t\ge15\)", r"\(t\le14\)"], [r"Write \(320+12t\le500\).", r"Subtract 320: \(12t\le180\).", r"Divide by 12: \(t\le15\).", r"The endpoint 15 is allowed because the budget is at most 500."], r"using strict \(<\) when 'at most' includes the limit.", 2),
        item(r"A value after a 20 percent decrease is at least 64. What original values \(p\) work?", r"\(p\ge80\)", [r"\(p\le80\)", r"\(p\ge76.8\)", r"\(p\le64\)"], [r"After a 20 percent decrease, the value is \(0.80p\).", r"Write \(0.80p\ge64\).", r"Divide by 0.80: \(p\ge80\).", r"Check: 20 percent off 80 is 64."], r"subtracting 20 from 64 instead of reversing a 20 percent decrease.", 3),
        item(r"Solve: \(\frac{x+2}{x-1}\le1\).", r"\((-\infty,1)\)", [r"\((1,\infty)\)", r"\((-\infty,1]\)", "All real numbers except 1"], [r"Move 1 to the left: \(\frac{x+2}{x-1}-1\le0\).", r"Use a common denominator: \(\frac{x+2-(x-1)}{x-1}\le0\).", r"Simplify the numerator: \(\frac{3}{x-1}\le0\).", r"Since 3 is positive, the fraction is nonpositive only when \(x-1<0\), so \(x<1\)."], r"multiplying by \(x-1\) without knowing whether it is positive or negative.", 3),
        item(r"Solve: \(-x^2+6x-8\ge0\).", r"\(2\le x\le4\)", [r"\(x\le2\) or \(x\ge4\)", r"\(2<x<4\)", r"\(x\le-4\) or \(x\ge-2\)"], [r"Multiply by \(-1\) and flip the inequality: \(x^2-6x+8\le0\).", r"Factor: \(x^2-6x+8=(x-2)(x-4)\).", r"An upward-opening quadratic is less than or equal to zero between its roots.", r"Include the roots because the inequality is \(\le0\), giving \(2\le x\le4\)."], r"multiplying by \(-1\) but forgetting to flip \(\ge\) to \(\le\).", 3),
        item(r"Solve: \(1<|x-2|\le5\).", r"\([-3,1)\cup(3,7]\)", [r"\((-3,7)\)", r"\([1,3]\)", r"\((-\infty,1)\cup(3,\infty)\)"], [r"The inequality says the distance from 2 is more than 1 but no more than 5.", r"First use \(|x-2|\le5\): this gives \(-3\le x\le7\).", r"Then remove the values with distance 1 or less from 2: \([1,3]\).", r"The remaining values are \([-3,1)\cup(3,7]\)."], r"solving only \(|x-2|\le5\) and forgetting the lower bound \(1<|x-2|\).", 3),
        item(r"A van holds at most 14 students. Two seats are already taken by helpers, and each group has 3 students. What is the greatest number of groups \(g\)?", r"\(4\)", [r"\(5\)", r"\(3\)", r"\(6\)"], [r"Write the capacity inequality: \(2+3g\le14\).", r"Subtract 2: \(3g\le12\).", r"Divide by 3: \(g\le4\).", r"Because the question asks for the greatest whole number of groups, the answer is 4."], r"rounding up to 5 groups even though \(2+3(5)=17\), which exceeds the van capacity.", 3),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Advanced Inequalities & Applications course (MCQ only)."

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
