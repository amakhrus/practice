"""
Seed a GED Math Foundations course for integer and rational-number operations.

Run:
    python manage.py seed_ged_integer_rational_operations
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


def item(text, answer, distractors, steps, trap, difficulty=2):
    return {
        "text": text,
        "difficulty": difficulty,
        "choices": [(answer, True)] + [(choice, False) for choice in distractors],
        "explanation": " ".join(
            [f"Step {index}: {step}" for index, step in enumerate(steps, start=1)]
            + [f"Common trap: {trap}"]
        ),
    }


COURSE = {
    "title": "GED Math Foundations: Integer & Rational Number Operations Mastery",
    "slug": "ged-integer-rational-operations",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Mathematical Reasoning foundation course on integers, "
        "opposites, absolute value, signed addition and subtraction, signed "
        "multiplication and division, rational-number operations with fractions "
        "and decimals, real-world positive and negative contexts, and multi-step "
        "reasonableness checks. The course strengthens the sign control students "
        "need before algebra, formulas, graphing, and word problems."
    ),
    "lessons": [
        (
            "1. Integers, Direction, and the Number Line",
            r"""
Integers are whole-number positions on a number line:
\[
\ldots,-3,-2,-1,0,1,2,3,\ldots
\]
They model situations with direction: deposits and withdrawals, gains and losses, temperatures above and below zero, and elevations above and below sea level.

[[figure:integer_number_line|The number line shows negatives, positives, opposites, and distance from zero.]]

On the number line, values increase as you move right. This is why \(-2>-6\). Both numbers are negative, but \(-2\) is farther right.

The opposite of a number is the same distance from zero on the other side. The opposite of \(8\) is \(-8\), and the opposite of \(-8\) is \(8\).

Common misconception: thinking the negative number with the larger digit is greater. Actually, \(-12<-4\) because \(-12\) is farther left.

Academic habit: when a comparison involves negatives, picture the number line before choosing an answer.

[[check:Which is greater, \(-3\) or \(-9\)?|-3|\(-3\) is farther right, so it is greater.]]
            """,
        ),
        (
            "2. Absolute Value as Distance",
            r"""
Absolute value tells distance from zero:
\[
|-7|=7,\qquad |7|=7.
\]
It is never negative because distance is never negative.

[[figure:absolute_value_distance_model|Absolute value can measure distance between two locations on a number line.]]

Absolute value can also measure distance between two numbers:
\[
|a-b|.
\]
For example, the distance from \(-4\) to \(3\) is:
\[
|3-(-4)|=|7|=7.
\]

This idea appears in GED questions about temperature changes, elevation changes, error from a target value, and distance on a coordinate line.

Absolute value equations have two sides. If \(|x|=6\), then \(x=6\) or \(x=-6\), because both numbers are 6 units from zero.

Common misconception: treating \(|-7|\) as \(-7\). The bars remove direction and keep distance.

Academic habit: read absolute value as "distance from" instead of "make positive." That meaning works in more situations.
            """,
        ),
        (
            "3. Adding Signed Numbers",
            r"""
Adding signed numbers combines movements.

If the signs are the same, add the absolute values and keep the sign:
\[
-6+(-9)=-15.
\]
Both movements go left, so the result is farther left.

If the signs are different, subtract the smaller absolute value from the larger absolute value. Keep the sign of the number with the larger absolute value:
\[
-11+4=-7.
\]
The 11-unit movement left is stronger than the 4-unit movement right.

[[figure:signed_operation_rules|Signed addition depends on signs and absolute values.]]

For decimals and fractions, the sign reasoning is the same:
\[
-2.5+1.1=-1.4,
\qquad
-\frac{3}{4}+\frac{1}{2}=-\frac{1}{4}.
\]

Common misconception: always adding the digits and keeping a negative sign. That works only when both numbers are negative.

Academic habit: before calculating, decide whether the numbers move in the same direction or opposite directions.
            """,
        ),
        (
            "4. Subtracting Signed Numbers",
            r"""
Subtraction means adding the opposite:
\[
a-b=a+(-b).
\]
This rule explains why subtracting a negative increases the value:
\[
5-(-8)=5+8=13.
\]

For a negative minus a positive, the movement becomes more negative:
\[
-4-7=-4+(-7)=-11.
\]

For a negative minus a negative, rewrite carefully:
\[
-3-(-10)=-3+10=7.
\]

Subtraction can also represent change. If a temperature goes from \(-5^\circ\) to \(8^\circ\), the change is:
\[
8-(-5)=13^\circ.
\]

Common misconception: changing every sign in the problem. Only the subtraction sign and the sign of the number being subtracted change.

Academic habit: rewrite subtraction as addition of the opposite before doing mental arithmetic.
            """,
        ),
        (
            "5. Multiplying and Dividing Signed Numbers",
            r"""
Multiplication and division use a simpler sign pattern than addition.

For multiplication and division:
- same signs give a positive result
- different signs give a negative result

Examples:
\[
(-6)(4)=-24,\qquad (-6)(-4)=24.
\]
\[
42\div(-6)=-7,\qquad (-18)\div(-3)=6.
\]

When several factors are multiplied, count the negative factors. An even number of negative factors gives a positive product. An odd number of negative factors gives a negative product:
\[
(-2)(-3)(-4)=-24.
\]
There are three negatives, so the result is negative.

Common misconception: using addition sign rules for multiplication. Multiplication does not ask which absolute value is larger.

Academic habit: determine the sign first, then calculate the size.
            """,
        ),
        (
            "6. Signed Fractions and Decimals",
            r"""
Fractions and decimals can be positive or negative. The operation rules do not change.

Signed fractions and signed decimals follow the same direction rules as integers; only the number form changes.

For addition and subtraction, use common denominators or decimal alignment after handling the signs:
\[
-\frac{3}{4}+\frac{1}{2}=-\frac{3}{4}+\frac{2}{4}=-\frac{1}{4}.
\]

For multiplication:
\[
-\frac{2}{3}\cdot\frac{9}{4}=-\frac{18}{12}=-\frac{3}{2}.
\]

For division, multiply by the reciprocal and keep the sign rule:
\[
-\frac{5}{6}\div\frac{10}{3}
=-\frac{5}{6}\cdot\frac{3}{10}
=-\frac{15}{60}
=-\frac{1}{4}.
\]

Decimals require place-value alignment:
\[
-1.25-0.50=-1.75.
\]

Common misconception: ignoring the sign when converting between fractions and decimals. \(-0.75\) is \(-\frac{3}{4}\), not \(\frac{3}{4}\).

Academic habit: write the sign on the simplified final answer, not just during the work.
            """,
        ),
        (
            "7. Real-World Positive and Negative Contexts",
            r"""
GED word problems often hide signed-number operations inside ordinary language.

Real-world positive and negative contexts give signs a meaning before you calculate.

Positive quantities can mean:
- deposit
- gain
- increase
- profit
- elevation above sea level
- temperature above zero

Negative quantities can mean:
- withdrawal
- loss
- decrease
- debt
- elevation below sea level
- temperature below zero

Example: A bank account starts at \(-25\) dollars because of an overdraft. A deposit of 60 dollars changes the balance to:
\[
-25+60=35.
\]

Example: A diver is at \(-18\) feet and rises 7 feet:
\[
-18+7=-11.
\]
The diver is still 11 feet below the surface.

Common misconception: assuming every word problem answer must be positive. In signed contexts, a negative answer may be meaningful.

Academic habit: translate words into signed numbers before choosing an operation.
            """,
        ),
        (
            "8. Multi-Step Signed Expressions",
            r"""
Many GED questions combine sign rules with order of operations.

Multi-step signed expressions require both sign control and operation order.

Example:
\[
6-2(-3).
\]
Multiply first:
\[
2(-3)=-6.
\]
Then subtract:
\[
6-(-6)=12.
\]

Parentheses matter:
\[
(-5)^2=25
\]
because the negative is inside the square. But:
\[
-5^2=-25
\]
because the exponent applies to 5 before the negative sign.

Another example:
\[
-4+\frac{-6}{2}=-4+(-3)=-7.
\]

Common misconception: doing operations left to right even when multiplication, division, or exponents should happen first.

Academic habit: circle multiplication/division and exponents before adding or subtracting.
            """,
        ),
        (
            "9. Comparing, Ordering, and Estimating Signed Values",
            r"""
Comparing signed numbers requires attention to direction.

Among negative numbers, the value closer to zero is greater:
\[
-0.35>-0.4.
\]
This surprises many students because \(0.4\) looks larger than \(0.35\), but the negative sign reverses the comparison.

Ordering from least to greatest means left to right on a number line:
\[
-2.2,\ -2.1,\ -2.01.
\]
\(-2.2\) is farthest left, and \(-2.01\) is closest to zero.

Estimation catches sign and decimal mistakes. For:
\[
-48+52,
\]
the answer should be a small positive number because the positive 52 is only slightly larger than 48. The exact answer is 4.

Common misconception: comparing negative decimals by digit count instead of position on the number line.

Academic habit: ask whether the final answer should be positive, negative, or near zero before calculating exactly.
            """,
        ),
        (
            "10. GED Strategy for Signed-Number Problems",
            r"""
A strong signed-number strategy has four steps:

1. Identify the context: number line, money, temperature, elevation, or pure computation.
2. Translate each quantity with a sign.
3. Choose the operation and follow sign rules.
4. Check whether the sign and size make sense.

Example: A hiker starts 120 feet above sea level, descends 180 feet, then climbs 45 feet:
\[
120-180+45=-15.
\]
The final elevation is 15 feet below sea level.

When answer choices include opposite signs, do not rush. These choices are often designed to catch one lost negative sign.

When answer choices are all positive, the problem may be asking for distance, absolute value, or total amount rather than final position.

Common misconception: treating "change" and "final value" as the same question. A change may be positive while the final value is still negative.

Academic habit: read the last sentence again before selecting the answer. It tells whether the problem asks for value, change, distance, or comparison.
            """,
        ),
    ],
    "mcqs": [
        item(r"Which number is greater: \(-4\) or \(-9\)?", r"\(-4\)", [r"\(-9\)", "They are equal.", "Neither is greater."], ["On a number line, greater numbers are farther right.", r"\(-4\) is farther right than \(-9\).", r"So \(-4\) is greater."], "choosing the negative number with the larger digit.", 1),
        item(r"What is the opposite of \(-8\)?", r"\(8\)", [r"\(-8\)", r"\(0\)", r"\(-\frac{1}{8}\)"], ["Opposites are the same distance from zero on different sides.", r"\(-8\) is 8 units left of zero.", r"Its opposite is \(8\)."], "thinking the opposite keeps the same sign.", 1),
        item(r"What is \(|-13|\)?", r"\(13\)", [r"\(-13\)", r"\(0\)", r"\(26\)"], ["Absolute value means distance from zero.", r"\(-13\) is 13 units from zero.", "The absolute value is 13."], "keeping the negative sign inside the absolute value bars.", 1),
        item(r"What is the distance from \(-5\) to \(2\) on a number line?", r"\(7\)", [r"\(3\)", r"\(-7\)", r"\(5\)"], [r"Use distance \(|a-b|\).", r"\(|2-(-5)|=|7|\).", "The distance is 7 units."], "subtracting as if both numbers were positive.", 2),

        item(r"Compute \(-7+(-6)\).", r"\(-13\)", [r"\(13\)", r"\(-1\)", r"\(1\)"], ["Both signs are negative.", "Add the absolute values: \(7+6=13\).", "Keep the negative sign."], "subtracting because the numbers have minus signs.", 1),
        item(r"Compute \(-9+14\).", r"\(5\)", [r"\(-23\)", r"\(-5\)", r"\(23\)"], ["The signs are different.", "Subtract absolute values: \(14-9=5\).", "The larger absolute value is positive, so the answer is 5."], "adding the absolute values and keeping a negative sign.", 1),
        item(r"Compute \(12+(-18)\).", r"\(-6\)", [r"\(6\)", r"\(30\)", r"\(-30\)"], ["The signs are different.", "Subtract absolute values: \(18-12=6\).", "The larger absolute value is negative, so the answer is \(-6\)."], "keeping the sign of the first number instead of the larger absolute value.", 1),
        item(r"Compute \(-3.5+1.2\).", r"\(-2.3\)", [r"\(-4.7\)", r"\(2.3\)", r"\(4.7\)"], ["The signs are different.", "Subtract \(3.5-1.2=2.3\).", "The larger absolute value is negative, so the answer is \(-2.3\)."], "adding the decimals or losing the negative sign.", 2),

        item(r"Compute \(8-13\).", r"\(-5\)", [r"\(5\)", r"\(21\)", r"\(-21\)"], ["Rewrite as \(8+(-13)\).", "The signs are different, so subtract \(13-8=5\).", "The larger absolute value is negative, so the answer is \(-5\)."], "making every subtraction answer positive.", 1),
        item(r"Compute \(5-(-9)\).", r"\(14\)", [r"\(-4\)", r"\(4\)", r"\(-14\)"], ["Subtracting a negative means add the opposite.", r"\(5-(-9)=5+9\).", "The result is 14."], "forgetting that subtracting a negative increases the value.", 1),
        item(r"Compute \(-4-7\).", r"\(-11\)", [r"\(3\)", r"\(-3\)", r"\(11\)"], ["Rewrite as \(-4+(-7)\).", "Both movements are negative.", "Add the absolute values and keep the negative sign: \(-11\)."], "changing the problem into \(-4+7\).", 1),
        item(r"Compute \(-2.5-(-6.1)\).", r"\(3.6\)", [r"\(-8.6\)", r"\(-3.6\)", r"\(8.6\)"], ["Subtracting a negative means adding.", r"\(-2.5-(-6.1)=-2.5+6.1\).", "The result is \(3.6\)."], "changing both signs or adding the absolute values.", 2),

        item(r"Compute \((-6)(4)\).", r"\(-24\)", [r"\(24\)", r"\(-10\)", r"\(10\)"], ["The factors have different signs.", "Different signs give a negative product.", "The size is \(6\cdot4=24\), so the answer is \(-24\)."], "using the addition rule instead of the multiplication sign rule.", 1),
        item(r"Compute \((-7)(-5)\).", r"\(35\)", [r"\(-35\)", r"\(-12\)", r"\(12\)"], ["The factors have the same sign.", "Same signs give a positive product.", "The size is \(7\cdot5=35\)."], "thinking a negative times a negative stays negative.", 1),
        item(r"Compute \(42\div(-6)\).", r"\(-7\)", [r"\(7\)", r"\(-6\)", r"\(48\)"], ["The numbers have different signs.", "Different signs give a negative quotient.", "\(42\div6=7\), so the answer is \(-7\)."], "making division positive because 42 is positive.", 1),
        item(r"Compute \((-18)\div(-3)\).", r"\(6\)", [r"\(-6\)", r"\(15\)", r"\(-15\)"], ["The numbers have the same sign.", "Same signs give a positive quotient.", "\(18\div3=6\)."], "forgetting that two negatives divide to a positive.", 1),
        item(r"What is the sign of \((-2)(-3)(-4)\)?", "Negative", ["Positive", "Zero", "Cannot be determined"], ["There are three negative factors.", "An odd number of negative factors gives a negative product.", "So the product is negative."], "stopping after the first two negatives make a positive.", 2),

        item(r"Compute \(-\frac{3}{4}+\frac{1}{2}\).", r"\(-\frac{1}{4}\)", [r"\(\frac{1}{4}\)", r"\(-\frac{5}{4}\)", r"\(\frac{5}{4}\)"], [r"Use a common denominator: \(\frac{1}{2}=\frac{2}{4}\).", r"\(-\frac{3}{4}+\frac{2}{4}=-\frac{1}{4}\).", "The result is negative because the negative fraction has greater size."], "adding numerators without sign control.", 2),
        item(r"Compute \(-1.25-0.50\).", r"\(-1.75\)", [r"\(-0.75\)", r"\(1.75\)", r"\(0.75\)"], ["Rewrite as \(-1.25+(-0.50)\).", "Both numbers are negative.", "Add the sizes to get \(1.75\) and keep the negative sign."], "treating subtraction as distance instead of final value.", 1),
        item(r"Compute \(-\frac{2}{3}\cdot\frac{9}{4}\).", r"\(-\frac{3}{2}\)", [r"\(\frac{3}{2}\)", r"\(-\frac{11}{12}\)", r"\(\frac{11}{12}\)"], ["The factors have different signs, so the answer is negative.", r"Multiply: \(\frac{2}{3}\cdot\frac{9}{4}=\frac{18}{12}\).", r"Simplify \(\frac{18}{12}\) to \(\frac{3}{2}\), then keep the negative sign."], "multiplying correctly but dropping the negative sign.", 2),
        item(r"Compute \(-\frac{5}{6}\div\frac{10}{3}\).", r"\(-\frac{1}{4}\)", [r"\(\frac{1}{4}\)", r"\(-\frac{25}{9}\)", r"\(\frac{25}{9}\)"], ["Keep, change, flip.", r"\(-\frac{5}{6}\div\frac{10}{3}=-\frac{5}{6}\cdot\frac{3}{10}\).", r"The product is \(-\frac{15}{60}=-\frac{1}{4}\)."], "flipping the wrong fraction or losing the sign.", 3),

        item(r"If \(|x|=5\), which values can \(x\) have?", r"\(5\) or \(-5\)", [r"\(5\) only", r"\(-5\) only", r"\(0\) or \(5\)"], ["Absolute value means distance from zero.", "Both 5 and \(-5\) are 5 units from zero.", r"So \(x=5\) or \(x=-5\)."], "giving only the positive value.", 2),
        item(r"A temperature changes from \(-4^\circ\) to \(9^\circ\). How many degrees did it increase?", r"\(13^\circ\)", [r"\(5^\circ\)", r"\(-13^\circ\)", r"\(9^\circ\)"], ["Change is final minus initial.", r"\(9-(-4)=13\).", "The temperature increased by 13 degrees."], "subtracting the absolute values only.", 2),
        item(r"A bank balance is \(-\$25\). A deposit of \(\$60\) is made. What is the new balance?", r"\(\$35\)", [r"\(-\$85\)", r"\(-\$35\)", r"\(\$85\)"], ["Translate the overdraft as \(-25\) and deposit as \(+60\).", r"\(-25+60=35\).", "The new balance is 35 dollars."], "adding the amounts but keeping the account negative.", 1),
        item(r"A diver is at \(-18\) feet and rises 7 feet. What is the diver's new elevation?", r"\(-11\) feet", [r"\(-25\) feet", r"\(11\) feet", r"\(25\) feet"], ["Start at \(-18\).", "Rising means add 7.", r"\(-18+7=-11\), so the diver is still below the surface."], "answering distance from the surface instead of signed elevation.", 2),
        item(r"A team loses 6 yards, gains 14 yards, then loses 3 yards. What is the net change?", r"\(+5\) yards", [r"\(-23\) yards", r"\(+23\) yards", r"\(-5\) yards"], ["Translate losses as negative and gains as positive.", r"\(-6+14-3=5\).", "The net change is a gain of 5 yards."], "adding all yard amounts without signs.", 2),

        item(r"Evaluate \(6-2(-3)\).", r"\(12\)", [r"\(0\)", r"\(-12\)", r"\(6\)"], ["Multiply first: \(2(-3)=-6\).", r"Then \(6-(-6)=6+6\).", "The result is 12."], "subtracting 6 after seeing \(2\cdot3\).", 2),
        item(r"Which expression equals \(25\)?", r"\((-5)^2\)", [r"\(-5^2\)", r"\(-25\)", r"\(-(-5)^2\)"], [r"\((-5)^2\) squares the entire negative number.", "A negative times a negative is positive.", "So \((-5)^2=25\)."], "thinking \(-5^2\) and \((-5)^2\) are the same.", 2),
        item(r"Evaluate \(-4+\frac{-6}{2}\).", r"\(-7\)", [r"\(-1\)", r"\(7\)", r"\(1\)"], ["Divide first: \(-6\div2=-3\).", r"Then \(-4+(-3)\).", "The result is \(-7\)."], "adding before dividing.", 2),
        item(r"Evaluate \((-5)^2-3^2\).", r"\(16\)", [r"\(-34\)", r"\(34\)", r"\(-16\)"], [r"\((-5)^2=25\).", r"\(3^2=9\).", r"\(25-9=16\)."], "forgetting the parentheses around \(-5\).", 2),
        item(r"Evaluate \(-12\div(2-5)\).", r"\(4\)", [r"\(-4\)", r"\(-36\)", r"\(36\)"], ["Evaluate parentheses first: \(2-5=-3\).", r"Then \(-12\div(-3)\).", "Same signs give a positive quotient: 4."], "dividing before simplifying the grouping symbols.", 2),

        item(r"Which is greater: \(-0.35\) or \(-0.4\)?", r"\(-0.35\)", [r"\(-0.4\)", "They are equal.", "Cannot be determined."], ["For negative decimals, the value closer to zero is greater.", r"\(-0.35\) is closer to zero than \(-0.4\).", r"So \(-0.35\) is greater."], "choosing \(-0.4\) because \(0.4\) is larger than \(0.35\).", 2),
        item(r"Order from least to greatest: \(-2.1,\ -2.01,\ -2.2\).", r"\(-2.2,\ -2.1,\ -2.01\)", [r"\(-2.01,\ -2.1,\ -2.2\)", r"\(-2.1,\ -2.01,\ -2.2\)", r"\(-2.2,\ -2.01,\ -2.1\)"], ["Least means farthest left on the number line.", r"\(-2.2\) is farthest left.", r"\(-2.01\) is closest to zero, so it is greatest."], "ordering negative decimals as if they were positive.", 3),
        item(r"Estimate the sign and size of \(-48+52\). Which is most reasonable?", "A small positive number", ["A large negative number", "A large positive number", "Exactly zero"], ["The positive number 52 is slightly larger than 48.", "The answer should be positive.", "Because the numbers are close, the answer should be small."], "adding 48 and 52 instead of comparing their sizes.", 1),
        item(r"Compute \(|-8|+|3|\).", r"\(11\)", [r"\(-5\)", r"\(5\)", r"\(-11\)"], [r"\(|-8|=8\).", r"\(|3|=3\).", r"Add distances: \(8+3=11\)."], "keeping a negative absolute value.", 1),

        item(r"A business loses \(\$120\), then earns \(\$85\), then earns \(\$60\). What is the net result?", r"\(\$25\) profit", [r"\(\$265\) profit", r"\(\$25\) loss", r"\(\$145\) loss"], ["Translate loss as \(-120\), earnings as \(+85\) and \(+60\).", r"\(-120+85+60=25\).", "The net result is positive, so it is a 25 dollar profit."], "adding all amounts or keeping the first negative sign.", 2),
        item(r"A hiker starts 120 feet above sea level, descends 180 feet, then climbs 45 feet. What is the final elevation?", r"\(-15\) feet", [r"\(15\) feet", r"\(-105\) feet", r"\(345\) feet"], ["Write the signed expression \(120-180+45\).", "Compute \(120-180=-60\).", "Then \(-60+45=-15\), so the hiker is 15 feet below sea level."], "finding total distance traveled instead of final signed elevation.", 2),
        item(r"Which question is asking for distance rather than final position?", "How far is \(-6\) from \(4\)?", ["What is \(-6+4\)?", "What is the new balance after losing 6 and gaining 4?", "Which number is greater, \(-6\) or \(4\)?"], ["Distance asks how far apart two positions are.", r"How far \(-6\) is from \(4\) uses absolute value.", "Final position and comparison are different questions."], "using absolute value for every signed-number problem.", 1),
        item(r"A student says \(7-(-2)=5\). What is the error?", "Subtracting a negative should add 2.", ["The 7 should be negative.", "The answer should be zero.", "The problem cannot be solved."], ["Rewrite subtraction as adding the opposite.", r"\(7-(-2)=7+2\).", "The correct result is 9."], "treating the two minus signs as one subtraction sign.", 1),
        item(r"A freezer is at \(-6^\circ\). The temperature drops \(9^\circ\). What is the new temperature?", r"\(-15^\circ\)", [r"\(3^\circ\)", r"\(-3^\circ\)", r"\(15^\circ\)"], ["A drop means subtract 9 or add \(-9\).", r"\(-6-9=-15\).", "The new temperature is \(-15^\circ\)."], "treating a drop as movement toward zero.", 1),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Math Foundations: Integer & Rational Number Operations Mastery course."

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
