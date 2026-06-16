"""
Seed a GED Math Foundations course for order of operations, calculator entry,
and formula skills.

Run:
    python manage.py seed_ged_order_operations_formula_skills
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
    "title": "GED Math Foundations: Order of Operations, Calculator & Formula Skills Mastery",
    "slug": "ged-order-operations-formula-skills",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Mathematical Reasoning foundation course on expression "
        "structure, order of operations, exponents and roots, scientific calculator "
        "entry, parentheses, formula-sheet use, substitution, simple formula "
        "rearrangement, units, rounding, estimation, and multi-step quantitative "
        "reasoning. The course helps students avoid calculator and formula traps "
        "that appear across algebra, geometry, data, and science-style GED problems."
    ),
    "lessons": [
        (
            "1. Expressions, Terms, and Grouping Symbols",
            r"""
An expression is a mathematical phrase. It may contain numbers, variables, operations, and grouping symbols:
\[
2(5+3)^2-7.
\]

Grouping symbols include parentheses, brackets, fraction bars, and radicals. They tell you what must be treated as one unit.

[[figure:expression_anatomy|An expression has terms, coefficients, variables, constants, and operations.]]

In \(2(5+3)^2-7\), the \(5+3\) must be simplified before the exponent. The parentheses create a single base.

Fraction bars also group. The expression
\[
\frac{12+8}{5-1}
\]
means the entire top is divided by the entire bottom:
\[
\frac{20}{4}=5.
\]

Common misconception: reading only visible parentheses as grouping. Fraction bars and radicals group too.

Academic habit: before calculating, identify every group in the expression.
            """,
        ),
        (
            "2. Order of Operations from Structure",
            r"""
Order of operations is not a memorized chant only. It is a way to respect the structure of an expression.

[[figure:order_operations_stack|Use grouping first, then exponents, then multiplication/division, then addition/subtraction.]]

The general order is:
1. grouping symbols
2. exponents and roots
3. multiplication and division from left to right
4. addition and subtraction from left to right

Example:
\[
6+2(5)^2.
\]
Square first:
\[
5^2=25.
\]
Multiply:
\[
2(25)=50.
\]
Add:
\[
6+50=56.
\]

Multiplication and division have equal priority. Work them left to right. Addition and subtraction also have equal priority.

Common misconception: always doing multiplication before division, even when division appears first from left to right.

Academic habit: rewrite one clean line after each operation step.
            """,
        ),
        (
            "3. Exponents, Roots, and Negative Bases",
            r"""
An exponent tells how many times a base is used as a factor:
\[
5^2=5\cdot5=25.
\]

A square root asks what number squares to the given value:
\[
\sqrt{81}=9
\]
because \(9^2=81\).

Negative bases require parentheses:
\[
(-3)^2=9,
\qquad
-3^2=-9.
\]
In \((-3)^2\), the whole negative number is squared. In \(-3^2\), the exponent applies to \(3\) first, and the negative sign stays outside.

Exponents also appear in area, volume, scientific notation, and growth problems.

Common misconception: treating \(-3^2\) as \(9\). Without parentheses, the exponent does not include the negative sign.

Academic habit: when a negative number is squared, check whether the negative is inside parentheses.
            """,
        ),
        (
            "4. Scientific Calculator Entry and Parentheses",
            r"""
A scientific calculator follows the symbols you enter. It does not know what you meant.

For:
\[
3+4\div2,
\]
the calculator gives 5 because division happens before addition:
\[
3+2=5.
\]

If you mean \((3+4)\div2\), you must enter parentheses:
\[
(3+4)\div2=3.5.
\]

Parentheses are especially important with fractions:
\[
\frac{12+8}{5-1}
\]
should be entered as:
\[
(12+8)\div(5-1).
\]

When substituting negative numbers, use parentheses:
\[
x^2 \text{ when } x=-4
\]
should be entered as:
\[
(-4)^2=16.
\]

Common misconception: trusting a calculator display without checking whether the entry matched the written expression.

Academic habit: write the calculator entry on paper for expressions with fractions, negatives, or grouped quantities.
            """,
        ),
        (
            "5. Formula Sheet Mindset: Variables and Units",
            r"""
GED formula questions usually test whether you can choose, substitute, and interpret a formula. You do not need to memorize every formula, but you do need to understand how formulas work.

A formula sheet is most helpful when you know how to match each variable to the quantities in the problem.

[[figure:formula_substitution_flow|Formula work follows a repeatable process: choose, label, substitute, simplify, attach units.]]

A formula uses variables to represent quantities. For rectangle area:
\[
A=lw.
\]
\(A\) is area, \(l\) is length, and \(w\) is width.

If \(l=8\) and \(w=5\), substitute:
\[
A=(8)(5)=40.
\]
Because area measures surface, the units are square units.

Units help choose formulas. Length uses units like feet or meters. Area uses square units. Volume uses cubic units. Rate uses compound units such as miles per hour or dollars per pound.

Common misconception: copying a formula but not identifying what each variable represents.

Academic habit: make a mini-list of given values before substituting.
            """,
        ),
        (
            "6. Substitution into Formulas",
            r"""
Substitution means replacing variables with known values.

Example: distance formula for constant speed:
\[
d=rt.
\]
If \(r=55\) miles per hour and \(t=3\) hours, then:
\[
d=(55)(3)=165\text{ miles}.
\]

Example: force formula:
\[
F=ma.
\]
If \(m=12\) kg and \(a=3\text{ m/s}^2\), then:
\[
F=(12)(3)=36.
\]

Use parentheses when substituting negative values or multi-part values:
\[
A=\frac{1}{2}bh,\quad b=10,\quad h=7
\]
becomes:
\[
A=\frac{1}{2}(10)(7)=35.
\]

Common misconception: replacing only one variable and then guessing the rest.

Academic habit: after substituting, the expression should contain numbers only.
            """,
        ),
        (
            "7. Rearranging Simple Formulas",
            r"""
Sometimes a formula is not solved for the value you need. Rearranging means isolating the requested variable.

From:
\[
d=rt,
\]
solve for \(t\) by dividing both sides by \(r\):
\[
t=\frac{d}{r}.
\]

From:
\[
A=lw,
\]
solve for \(w\) by dividing by \(l\):
\[
w=\frac{A}{l}.
\]

For rectangle perimeter:
\[
P=2l+2w.
\]
To solve for \(l\), subtract \(2w\):
\[
P-2w=2l.
\]
Then divide by 2:
\[
l=\frac{P-2w}{2}.
\]

Common misconception: dividing only one term when the whole expression must be divided.

Academic habit: undo operations in reverse order and keep the equation balanced.
            """,
        ),
        (
            "8. Units, Conversions, and Formula Results",
            r"""
Units are part of the answer. A correct number with the wrong unit can be wrong.

Common GED conversions may be provided in the problem:
\[
1\text{ ft}=12\text{ in},\qquad 1\text{ kg}=1000\text{ g}.
\]

If a length is 48 inches, then:
\[
48\div12=4\text{ ft}.
\]

If a mass is 3.5 kg, then:
\[
3.5(1000)=3500\text{ g}.
\]

Formula units should match the measurement type:
- perimeter or circumference: linear units
- area: square units
- volume: cubic units
- speed: distance per time

[[figure:unit_conversion_bridge|A conversion factor is a bridge between equivalent units.]]

Common misconception: multiplying when converting to a larger unit or dividing when converting to a smaller unit without checking reasonableness.

Academic habit: ask whether the converted number should be larger or smaller.
            """,
        ),
        (
            "9. Rounding, Precision, and Money Answers",
            r"""
GED problems often specify how to round. Follow the requested place.

To round \(8.47\) to the nearest tenth, look at the hundredths digit. Since 7 is 5 or more, round \(8.4\) up to \(8.5\).

To round \(4.236\) to the nearest hundredth, look at the thousandths digit. Since 6 is 5 or more, \(4.23\) becomes \(4.24\).

Money is usually rounded to the nearest cent:
\[
\$12.50(0.07)=\$0.875\approx\$0.88.
\]

Precision means how exact a number is. Rounding too early can change an answer. For multi-step problems, keep extra digits until the final answer unless the problem tells you otherwise.

Common misconception: rounding every intermediate step. This can create avoidable error.

Academic habit: underline the rounding instruction before solving.
            """,
        ),
        (
            "10. Multi-Step Formula and Calculator Strategy",
            r"""
A GED formula problem may combine reading, substitution, unit conversion, and rounding. Use a stable process:

1. Identify what the question asks.
2. Choose the formula or relationship.
3. List the given values with units.
4. Substitute with parentheses.
5. Simplify using order of operations.
6. Round only as requested.
7. Check reasonableness.

Example: A car travels 2.5 hours at 60 miles per hour:
\[
d=rt=(60)(2.5)=150\text{ miles}.
\]

Example: A circle has diameter 9 inches. Circumference is:
\[
C=\pi d\approx3.14(9)=28.26\text{ inches}.
\]

Reasonableness check: \(3.14\) times 9 should be a little more than 27, so 28.26 makes sense.

Common misconception: beginning with arithmetic before deciding what the question asks.

Academic habit: after solving, read the answer as a sentence with units.
            """,
        ),
    ],
    "mcqs": [
        item(r"Evaluate \(6+2\cdot5\).", r"\(16\)", [r"\(40\)", r"\(13\)", r"\(30\)"], ["Multiply before adding.", r"\(2\cdot5=10\).", r"\(6+10=16\)."], "adding \(6+2\) first without parentheses.", 1),
        item(r"Evaluate \((6+2)\cdot5\).", r"\(40\)", [r"\(16\)", r"\(13\)", r"\(30\)"], ["Parentheses come first.", r"\(6+2=8\).", r"\(8\cdot5=40\)."], "ignoring grouping symbols.", 1),
        item(r"Evaluate \(18\div3^2\).", r"\(2\)", [r"\(36\)", r"\(6\)", r"\(9\)"], ["Exponents come before division.", r"\(3^2=9\).", r"\(18\div9=2\)."], "dividing before evaluating the exponent.", 2),
        item(r"Evaluate \(4(3+2)^2\).", r"\(100\)", [r"\(40\)", r"\(28\)", r"\(52\)"], ["Parentheses first: \(3+2=5\).", r"Square: \(5^2=25\).", r"Multiply: \(4\cdot25=100\)."], "multiplying before squaring the grouped value.", 2),
        item(r"Evaluate \(7+12\div3-2\).", r"\(9\)", [r"\(4\)", r"\(17\)", r"\(5\)"], ["Divide first: \(12\div3=4\).", r"Then \(7+4-2\).", "Work left to right to get 9."], "doing addition before division.", 1),
        item(r"Evaluate \(\frac{24-(3+5)}{4}\).", r"\(4\)", [r"\(6\)", r"\(8\)", r"\(2\)"], ["Evaluate parentheses: \(3+5=8\).", "Subtract in the numerator: \(24-8=16\).", "Divide by 4 to get 4."], "dividing only part of the numerator.", 2),

        item(r"What is \(5^2\)?", r"\(25\)", [r"\(10\)", r"\(7\)", r"\(32\)"], ["An exponent of 2 means use 5 as a factor twice.", r"\(5^2=5\cdot5\).", "The value is 25."], "multiplying the base by the exponent.", 1),
        item(r"What is \(\sqrt{81}\)?", r"\(9\)", [r"\(8\)", r"\(40.5\)", r"\(18\)"], ["A square root asks what number squares to 81.", r"\(9^2=81\).", r"So \(\sqrt{81}=9\)."], "dividing by 2 instead of finding the square root.", 1),
        item(r"Evaluate \(2^3\cdot4\).", r"\(32\)", [r"\(24\)", r"\(20\)", r"\(14\)"], ["Evaluate the exponent first: \(2^3=8\).", r"Multiply \(8\cdot4\).", "The result is 32."], "multiplying 3 by 4 before using the exponent.", 2),
        item(r"Which expression equals \(9\)?", r"\((-3)^2\)", [r"\(-3^2\)", r"\(-9\)", r"\(-(-3)^2\)"], [r"\((-3)^2\) squares the entire negative number.", "A negative times a negative is positive.", "The value is 9."], "missing the difference between \(-3^2\) and \((-3)^2\).", 2),
        item(r"What is \(-3^2\)?", r"\(-9\)", [r"\(9\)", r"\(-6\)", r"\(6\)"], ["Without parentheses, the exponent applies to 3 first.", r"\(3^2=9\).", "The negative sign remains outside, so the value is \(-9\)."], "assuming the negative sign is part of the base.", 2),

        item(r"A calculator expression is \(3+4\div2\). What value should it give?", r"\(5\)", [r"\(3.5\)", r"\(7\)", r"\(14\)"], ["Division happens before addition.", r"\(4\div2=2\).", r"\(3+2=5\)."], "reading the expression as \((3+4)\div2\).", 1),
        item(r"Which calculator entry matches \(\frac{12+8}{5-1}\)?", r"\((12+8)\div(5-1)\)", [r"\(12+8\div5-1\)", r"\(12+(8\div5)-1\)", r"\((12+8)\div5-1\)"], ["A fraction bar groups the entire numerator and denominator.", "The top needs parentheses and the bottom needs parentheses.", r"The matching entry is \((12+8)\div(5-1)\)."], "not using parentheses around the numerator and denominator.", 2),
        item(r"If \(x=-4\), how should \(x^2\) be entered?", r"\((-4)^2\)", [r"\(-4^2\)", r"\(-4\cdot2\)", r"\(4^2-\)"], ["The variable value is the entire number \(-4\).", "Use parentheses around the negative value.", r"\((-4)^2\) gives 16."], "entering \(-4^2\), which gives \(-16\).", 2),
        item(r"What is the value of \((12+8)\div(5-1)\)?", r"\(5\)", [r"\(7\)", r"\(4\)", r"\(20\)"], ["Evaluate the numerator group: \(12+8=20\).", "Evaluate the denominator group: \(5-1=4\).", "\(20\div4=5\)."], "dividing before simplifying both groups.", 1),

        item(r"The formula \(A=lw\) gives rectangle area. If \(l=8\) and \(w=5\), what is \(A\)?", r"\(40\)", [r"\(13\)", r"\(26\)", r"\(3\)"], ["Substitute \(l=8\) and \(w=5\).", r"\(A=(8)(5)\).", "The area is 40 square units."], "adding length and width instead of multiplying for area.", 1),
        item(r"The formula \(P=2l+2w\) gives rectangle perimeter. If \(l=8\) and \(w=5\), what is \(P\)?", r"\(26\)", [r"\(40\)", r"\(13\)", r"\(80\)"], ["Substitute \(l=8\) and \(w=5\).", r"\(P=2(8)+2(5)=16+10\).", "The perimeter is 26 units."], "using the area formula instead of perimeter.", 1),
        item(r"The formula \(d=rt\) gives distance. If \(r=55\) mph and \(t=3\) hours, what is \(d\)?", r"\(165\) miles", [r"\(58\) miles", r"\(18.3\) miles", r"\(110\) miles"], ["Substitute \(r=55\) and \(t=3\).", r"\(d=(55)(3)\).", "The distance is 165 miles."], "adding rate and time instead of multiplying.", 1),
        item(r"Simple interest uses \(I=prt\). If \(p=500\), \(r=0.06\), and \(t=2\), what is \(I\)?", r"\(60\)", [r"\(600\)", r"\(6\)", r"\(508\)"], ["Substitute the values.", r"\(I=(500)(0.06)(2)\).", r"\(500\cdot0.06=30\), and \(30\cdot2=60\)."], "using 6 instead of \(0.06\) for 6%.", 2),
        item(r"The formula \(F=ma\). If \(m=12\) and \(a=3\), what is \(F\)?", r"\(36\)", [r"\(15\)", r"\(4\)", r"\(9\)"], ["Substitute \(m=12\) and \(a=3\).", r"\(F=(12)(3)\).", "The value is 36."], "adding the values instead of multiplying.", 1),
        item(r"Use \(C=2\pi r\). If \(r=4\), what is \(C\) using \(\pi\approx3.14\)?", r"\(25.12\)", [r"\(12.56\)", r"\(50.24\)", r"\(16\)"], ["Substitute \(r=4\).", r"\(C=2(3.14)(4)\).", "The circumference is \(25.12\)."], "forgetting the factor of 2 or using area instead.", 2),
        item(r"Use \(A=\frac{1}{2}bh\). If \(b=10\) and \(h=7\), what is \(A\)?", r"\(35\)", [r"\(70\)", r"\(17\)", r"\(140\)"], ["Substitute \(b=10\) and \(h=7\).", r"\(A=\frac{1}{2}(10)(7)\).", "The area is 35 square units."], "forgetting the one-half factor for triangle area.", 1),
        item(r"Use \(V=lwh\). If \(l=3\), \(w=4\), and \(h=5\), what is \(V\)?", r"\(60\)", [r"\(12\)", r"\(27\)", r"\(45\)"], ["Substitute the three dimensions.", r"\(V=(3)(4)(5)\).", "The volume is 60 cubic units."], "adding the dimensions instead of multiplying.", 1),

        item(r"Solve \(d=rt\) for \(t\).", r"\(t=\frac{d}{r}\)", [r"\(t=dr\)", r"\(t=d-r\)", r"\(t=\frac{r}{d}\)"], ["To isolate \(t\), undo multiplication by \(r\).", "Divide both sides by \(r\).", r"The result is \(t=\frac{d}{r}\)."], "reversing the fraction or multiplying.", 2),
        item(r"Solve \(A=lw\) for \(w\).", r"\(w=\frac{A}{l}\)", [r"\(w=Al\)", r"\(w=A-l\)", r"\(w=\frac{l}{A}\)"], ["To isolate \(w\), undo multiplication by \(l\).", "Divide both sides by \(l\).", r"The result is \(w=\frac{A}{l}\)."], "putting the known side over the area.", 2),
        item(r"Solve \(P=2l+2w\) for \(l\).", r"\(l=\frac{P-2w}{2}\)", [r"\(l=P-2w\)", r"\(l=\frac{P}{2}-2w\)", r"\(l=2P-2w\)"], [r"Subtract \(2w\) from both sides: \(P-2w=2l\).", "Divide the entire left side by 2.", r"The result is \(l=\frac{P-2w}{2}\)."], "dividing only one term by 2.", 3),
        item(r"Solve \(C=\pi d\) for \(d\).", r"\(d=\frac{C}{\pi}\)", [r"\(d=C\pi\)", r"\(d=C-\pi\)", r"\(d=\frac{\pi}{C}\)"], ["The diameter is multiplied by \(\pi\).", "Divide both sides by \(\pi\).", r"The result is \(d=\frac{C}{\pi}\)."], "multiplying by \(\pi\) instead of dividing.", 2),

        item(r"Convert \(3.5\) kg to grams. Use \(1\text{ kg}=1000\text{ g}\).", r"\(3500\text{ g}\)", [r"\(350\text{ g}\)", r"\(0.0035\text{ g}\)", r"\(35{,}000\text{ g}\)"], ["Grams are smaller than kilograms, so the number should get larger.", "Multiply by 1000.", r"\(3.5\text{ kg}=3500\text{ g}\)."], "moving the decimal the wrong direction.", 1),
        item(r"Convert \(48\) inches to feet. Use \(1\text{ ft}=12\text{ in}\).", r"\(4\text{ ft}\)", [r"\(36\text{ ft}\)", r"\(576\text{ ft}\)", r"\(12\text{ ft}\)"], ["Feet are larger than inches, so the number should get smaller.", "Divide by 12.", r"\(48\div12=4\text{ ft}\)."], "multiplying when converting to a larger unit.", 1),
        item(r"A car travels \(2.5\) hours at \(60\) mph. How far does it travel?", r"\(150\) miles", [r"\(62.5\) miles", r"\(24\) miles", r"\(120\) miles"], ["Use \(d=rt\).", r"\(d=(60)(2.5)\).", "The distance is 150 miles."], "adding rate and time or dividing in the wrong direction.", 1),
        item(r"Which unit is appropriate for the area of a rectangle?", "Square feet", ["Feet", "Cubic feet", "Feet per second"], ["Area measures flat surface.", "Flat surface uses square units.", "Square feet is the area unit."], "using length or volume units for area.", 1),

        item(r"Round \(8.47\) to the nearest tenth.", r"\(8.5\)", [r"\(8.4\)", r"\(8.47\)", r"\(9.0\)"], ["The tenths digit is 4.", "The hundredths digit is 7, so round up.", "The result is \(8.5\)."], "rounding down even though the next digit is 5 or more.", 1),
        item(r"Round \(4.236\) to the nearest hundredth.", r"\(4.24\)", [r"\(4.23\)", r"\(4.2\)", r"\(4.30\)"], ["The hundredths digit is 3.", "The thousandths digit is 6, so round up.", "The result is \(4.24\)."], "rounding to the wrong place.", 1),
        item(r"A tax is \(\$12.50\cdot0.07=\$0.875\). Rounded to the nearest cent, what is the tax?", r"\(\$0.88\)", [r"\(\$0.87\)", r"\(\$0.90\)", r"\(\$0.08\)"], ["Cents use two decimal places.", "The third decimal place is 5.", "Round \(0.875\) to \(0.88\)."], "truncating instead of rounding money.", 1),
        item(r"Which estimate is most reasonable for \(49\cdot21\)?", r"\(1{,}000\)", [r"\(100\)", r"\(10{,}000\)", r"\(70\)"], ["Round 49 to 50.", "Round 21 to 20.", r"\(50\cdot20=1000\)."], "placing the decimal or magnitude one power of ten away.", 1),

        item(r"In \(2(5+3)^2\), which operation should happen first?", r"\(5+3\)", [r"\(2\cdot5\)", r"\(3^2\)", r"\(2+3\)"], ["Grouping symbols come first.", "The group is \(5+3\).", "After that, square the result and multiply by 2."], "starting with multiplication because 2 is next to the parentheses.", 1),
        item(r"Which result is impossible for an area measurement?", r"\(-12\text{ ft}^2\)", [r"\(0\text{ ft}^2\)", r"\(12\text{ ft}^2\)", r"\(12.5\text{ ft}^2\)"], ["Area measures surface.", "Surface area cannot be negative.", "So a negative area is impossible in ordinary geometry."], "forgetting to check whether the sign makes sense.", 1),
        item(r"What is the best first step when using a formula from a formula sheet?", "Identify what each variable means.", ["Copy every formula into the answer.", "Round all numbers immediately.", "Ignore the units."], ["A formula is useful only when the variables match the problem.", "Identify the requested value and the given values.", "Then substitute into the correct formula."], "substituting numbers before knowing what the variables mean.", 1),
        item(r"A circle has diameter 9 inches. Use \(C=\pi d\) and \(\pi\approx3.14\). What is the circumference?", r"\(28.26\) inches", [r"\(14.13\) inches", r"\(63.59\) inches", r"\(9.14\) inches"], ["Substitute \(d=9\).", r"\(C=3.14(9)\).", "The circumference is \(28.26\) inches."], "using radius or area when the diameter formula was given.", 2),
        item(r"Evaluate \(2(3+4)^2-5\).", r"\(93\)", [r"\(45\)", r"\(23\)", r"\(191\)"], ["Parentheses first: \(3+4=7\).", r"Square: \(7^2=49\), then multiply: \(2(49)=98\).", r"Subtract 5 to get \(93\)."], "multiplying before handling the grouped exponent.", 2),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Math Foundations: Order of Operations, Calculator & Formula Skills Mastery course."

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
