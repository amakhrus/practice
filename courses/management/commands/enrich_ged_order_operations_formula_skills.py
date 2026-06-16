from django.core.management.base import BaseCommand
from courses.models import Lesson

LESSONS = [
    (1, """Expressions, Terms, and Grouping Symbols

In mathematics, an expression is a combination of numbers, variables, and operations that represents a value. Unlike an equation, an expression does not have an equals sign — it simply describes a quantity. Understanding how expressions are built is the foundation for all arithmetic and algebra you will encounter on the GED Math test.

A term is a single number, a variable, or a product of numbers and variables. For example, in the expression 3x + 5y - 7, there are three terms: 3x, 5y, and -7. Each term is separated by an addition or subtraction sign. When you count terms, always include the sign that belongs to each one.

Grouping symbols tell you which part of an expression to treat as a single unit. The most common grouping symbols are:
- Parentheses: ( )
- Brackets: [ ]
- Braces: { }
- Fraction bars (the line between the numerator and denominator acts as a grouping symbol)

Whatever is inside a grouping symbol must be evaluated first before combining it with anything outside.

WORKED EXAMPLE
Identify the terms and simplify: 4(3 + 2) - 8

Step 1: Recognize the grouping symbol. The parentheses group (3 + 2) together.
Step 2: Evaluate inside the parentheses first. 3 + 2 = 5
Step 3: The expression becomes 4(5) - 8
Step 4: Multiply. 4 x 5 = 20
Step 5: Subtract. 20 - 8 = 12

Answer: 12

The original expression had two main operations: multiplication and subtraction. The parentheses made it clear that addition had to happen first. Without the parentheses, 4 x 3 + 2 - 8 would equal 6, a completely different answer.

COMMON MISTAKE TO AVOID
Many students forget that a number written directly next to parentheses means multiplication. If you see 4(3 + 2), the 4 is multiplied by the entire result inside the parentheses, not just the 3. Similarly, -3(x + 4) means you multiply -3 by both x and 4, giving -3x - 12. Missing this distribution is one of the most frequent errors on algebra problems.

GED TEST TIP
On the GED, expressions with nested grouping symbols (parentheses inside brackets) are common. Always work from the innermost group outward. Write out each step rather than trying to do it mentally. The test awards credit only for correct answers, and a single arithmetic slip can cost you the entire problem. Taking 30 extra seconds to write clearly is always worth it.
"""),

    (2, """Order of Operations from Structure

The order of operations is the agreement mathematicians follow so that every person who evaluates the same expression gets the same answer. Without a standard order, 2 + 3 x 4 could equal 20 (if you add first) or 14 (if you multiply first). The correct answer is 14 because multiplication is always done before addition.

The standard order is summarized by the acronym PEMDAS:
P - Parentheses (and all grouping symbols)
E - Exponents (powers and roots)
M - Multiplication
D - Division
A - Addition
S - Subtraction

Important note: Multiplication and Division are at the same level of priority. You do them left to right as they appear. The same rule applies to Addition and Subtraction — they share the same level and are worked left to right.

WORKED EXAMPLE
Evaluate: 3 + 6 x (4 - 1)^2 / 9 - 2

Step 1: Parentheses first. (4 - 1) = 3
Expression becomes: 3 + 6 x 3^2 / 9 - 2

Step 2: Exponents next. 3^2 = 9
Expression becomes: 3 + 6 x 9 / 9 - 2

Step 3: Multiplication and Division left to right.
6 x 9 = 54, then 54 / 9 = 6
Expression becomes: 3 + 6 - 2

Step 4: Addition and Subtraction left to right.
3 + 6 = 9, then 9 - 2 = 7

Answer: 7

COMMON MISTAKE TO AVOID
The most common error is treating PEMDAS as a strict left-to-right list where multiplication always comes before division. It does not. Multiplication and division have equal priority, and the same is true for addition and subtraction. Always scan the expression from left to right when you reach the M/D level or the A/S level.

For example: 12 / 4 x 3
Wrong: 12 / (4 x 3) = 12 / 12 = 1
Right: (12 / 4) x 3 = 3 x 3 = 9

GED TEST TIP
When the GED gives you a long multi-operation expression, rewrite it after completing each step. This keeps you from losing track of where you are. Even experienced test-takers make errors when trying to hold too many steps in memory at once. Each rewrite only takes a few seconds and dramatically reduces mistakes.
"""),

    (3, """Exponents, Roots, and Negative Bases

An exponent tells you how many times a base number is multiplied by itself. In the expression 5^3, the base is 5 and the exponent is 3, meaning 5 x 5 x 5 = 125. Exponents appear frequently on the GED in area formulas, the Pythagorean theorem, and scientific notation.

A square root is the inverse of squaring. The square root of 25 is 5 because 5^2 = 25. The GED formula sheet provides the Pythagorean theorem (a^2 + b^2 = c^2), and you will often need to take a square root to find a side length. You do not need to memorize perfect squares, but knowing the squares from 1 to 15 will save significant time.

Negative bases require special care. When a negative number is raised to an even power, the result is positive. When raised to an odd power, the result is negative.

(-3)^2 = (-3) x (-3) = 9 (positive)
(-3)^3 = (-3) x (-3) x (-3) = -27 (negative)

The placement of the negative sign matters enormously. Note the difference:
(-3)^2 = 9 (the negative is inside the exponent)
-3^2 = -9 (only 3 is squared, then the negative is applied)

WORKED EXAMPLE
Evaluate: -2^4 + (-2)^4

Step 1: Evaluate -2^4. The exponent applies only to 2, not to the negative sign.
2^4 = 16, so -2^4 = -16

Step 2: Evaluate (-2)^4. The negative is part of the base.
(-2)^4 = (-2) x (-2) x (-2) x (-2) = 16

Step 3: Add the results. -16 + 16 = 0

Answer: 0

COMMON MISTAKE TO AVOID
Confusing -3^2 with (-3)^2 is extremely common. If you see a negative number without parentheses before an exponent, the exponent does NOT apply to the negative sign. Write out the parentheses yourself to clarify before you calculate. On the GED, this distinction frequently appears in answer choices designed to catch students who rush.

GED TEST TIP
The GED calculator (TI-30XS MultiView) handles negative bases correctly when you use the negative key (the (-) key, not the minus key). Always use parentheses when entering negative bases: enter (-3)^2 as ( (-) 3 ) ^ 2. If you omit the parentheses, the calculator computes -(3^2) = -9 instead of 9. Practice this on the calculator before test day.
"""),

    (4, """Scientific Calculator Entry and Parentheses

The GED Math test allows you to use the TI-30XS MultiView calculator for Part 1 (the non-formula-sheet section does not have a calculator). Knowing how to enter expressions correctly is just as important as knowing the math itself. An entry error can turn a correct setup into a wrong answer in seconds.

Key calculator skills for the GED:

1. The negative key vs. the minus key. The (-) key (bottom left area) makes a number negative. The - key performs subtraction. Never use the subtraction key when you mean to enter a negative number.

2. Using parentheses for grouped expressions. Whenever you have a numerator or denominator with multiple terms, wrap it in parentheses. The calculator does not automatically treat the fraction bar as a grouping symbol when you type on one line.

3. Entering exponents. Use the ^ key for powers. For square roots, use the 2nd function above the x^2 key.

4. Order of entry follows PEMDAS. The calculator applies order of operations automatically, but only if you enter the expression the same way it is written. Misplaced parentheses are the number one source of calculator errors.

WORKED EXAMPLE
Use the calculator to evaluate: (8 + 4) / (3 - 1)

Incorrect entry: 8 + 4 / 3 - 1
This computes 8 + (4/3) - 1 = 8 + 1.333... - 1 = 8.333...

Correct entry: ( 8 + 4 ) / ( 3 - 1 )
This computes 12 / 2 = 6

Step-by-step keystrokes: ( 8 + 4 ) / ( 3 - 1 ) ENTER

Answer: 6

The incorrect entry produces 8.33, which would be a wrong answer choice designed to trap students who skip the parentheses.

COMMON MISTAKE TO AVOID
When dividing expressions that each contain multiple terms, students often enter the numerator, press the division key, and then enter the denominator without parentheses. The calculator reads this as only dividing by the first term of the denominator. Always add parentheses around any multi-term numerator or denominator, even when the original problem uses a fraction bar.

GED TEST TIP
After entering a complex expression, verify your entry by pressing the up arrow to scroll back through what you typed. The TI-30XS displays the entire expression in its history. Catch errors before you press ENTER. Also, estimate the answer mentally before calculating — if your estimate is 6 and the calculator shows 8.33, you know something was entered wrong.
"""),

    (5, """Formula Sheet Mindset: Variables and Units

The GED Math test provides a formula sheet. You do not need to memorize formulas — but you do need to know how to read them, identify the variables, and substitute values correctly. Many test-takers waste the formula sheet because they do not know what each letter means or which formula applies to a given situation.

A variable is a letter that represents an unknown or changeable quantity. In the area formula A = l x w, A stands for area, l stands for length, and w stands for width. The formula tells you the relationship between those three quantities. If you know any two, you can find the third.

Units are labels that tell you what kind of quantity you are measuring: inches, feet, square meters, gallons, etc. When you substitute values into a formula, the units must be consistent. If length is in feet, width must also be in feet — not a mix of feet and inches.

The GED formula sheet includes formulas for:
- Area and perimeter of rectangles, triangles, circles, and other shapes
- Volume of rectangular prisms, cylinders, pyramids, and cones
- The Pythagorean theorem
- The distance, rate, and time formula (d = rt)
- The slope formula
- The quadratic formula

WORKED EXAMPLE
A rectangular garden is 12 feet long and 7 feet wide. What is its area?

Step 1: Identify the correct formula. For a rectangle, A = l x w (from the formula sheet).
Step 2: Identify the variables. l = 12 feet, w = 7 feet.
Step 3: Substitute. A = 12 x 7
Step 4: Calculate. A = 84
Step 5: Include the unit. Because we multiplied feet x feet, the unit is square feet.

Answer: 84 square feet

COMMON MISTAKE TO AVOID
Students often copy a formula correctly but forget to include or convert units. On area problems, the unit is always squared (ft^2, m^2, etc.) because you are multiplying two lengths together. On volume problems, the unit is cubed. Leaving off the unit or writing the wrong unit is an error even when your numerical answer is correct.

GED TEST TIP
Before solving any geometry or applied math problem, write down the formula you plan to use and label each variable. This two-step habit forces you to slow down, match the right formula to the problem, and avoid substituting a value into the wrong slot. The extra 20 seconds this takes pays off in accuracy.
"""),

    (6, """Substitution into Formulas

Substitution is the process of replacing a variable in a formula with a specific number. It is one of the most frequently tested skills on the GED because it appears in geometry (area, volume), science-related word problems (distance = rate x time), and finance problems (simple interest = principal x rate x time).

The steps are always the same:
1. Write the formula.
2. Identify what each variable represents.
3. Replace each variable with the given number.
4. Follow the order of operations to simplify.

When substituting, be especially careful with formulas that include exponents or fractions. Write out every multiplication step so you do not drop a factor.

WORKED EXAMPLE
The formula for simple interest is I = P x r x t, where I is interest, P is principal (starting amount), r is the annual interest rate as a decimal, and t is time in years.

Find the interest earned on $2,500 at 4% annual interest for 3 years.

Step 1: Write the formula. I = P x r x t
Step 2: Identify values. P = 2500, r = 0.04 (4% converted to decimal), t = 3
Step 3: Substitute. I = 2500 x 0.04 x 3
Step 4: Calculate left to right. 2500 x 0.04 = 100, then 100 x 3 = 300

Answer: $300 in interest

WORKED EXAMPLE 2
Use the area formula for a circle: A = pi x r^2 (pi is approximately 3.14)
Find the area of a circle with radius 5 cm.

Step 1: A = pi x r^2
Step 2: r = 5
Step 3: Substitute. A = 3.14 x 5^2
Step 4: Exponent first (order of operations). 5^2 = 25
Step 5: Multiply. A = 3.14 x 25 = 78.5

Answer: 78.5 square centimeters

COMMON MISTAKE TO AVOID
In the circle area formula A = pi x r^2, the exponent applies only to r, not to pi x r. A frequent error is computing (pi x r)^2 instead of pi x (r^2). Always square the radius first, then multiply by pi.

GED TEST TIP
When a problem gives a percentage rate, always convert it to a decimal before substituting. Move the decimal point two places to the left: 4% becomes 0.04, 12.5% becomes 0.125. Substituting the whole number 4 instead of 0.04 will produce an answer 100 times too large, and that incorrect value will not match any answer choice — which alerts you to recheck.
"""),

    (7, """Rearranging Simple Formulas

Rearranging a formula (also called solving for a variable) means rewriting the formula so that a different variable is isolated on one side. This skill is essential when you know the output of a formula but need to find one of the inputs.

The key principle: whatever you do to one side of an equation, you must do to the other side. This keeps the equation balanced.

Common operations used to rearrange:
- If a variable is added to something, subtract that something from both sides.
- If a variable is multiplied by something, divide both sides by that something.
- If a variable is squared, take the square root of both sides.

The goal is to get the target variable alone on one side of the equals sign.

WORKED EXAMPLE 1
The distance formula is d = r x t. Rearrange to solve for t (time).

Step 1: Start with d = r x t
Step 2: To isolate t, divide both sides by r.
d / r = (r x t) / r
Step 3: Simplify. The r's on the right cancel.
t = d / r

If a car travels 240 miles at 60 mph, how long did it take?
t = 240 / 60 = 4 hours

WORKED EXAMPLE 2
The perimeter of a rectangle is P = 2l + 2w. Solve for l.

Step 1: Start with P = 2l + 2w
Step 2: Subtract 2w from both sides.
P - 2w = 2l
Step 3: Divide both sides by 2.
(P - 2w) / 2 = l

If P = 36 and w = 8: l = (36 - 16) / 2 = 20 / 2 = 10

COMMON MISTAKE TO AVOID
When dividing both sides of an equation to isolate a variable, students sometimes only divide part of the other side. In the perimeter example, after reaching P - 2w = 2l, you must divide the entire left side by 2, not just one term. The correct result is (P - 2w) / 2 = l, not P - w = l.

GED TEST TIP
The GED sometimes gives you a formula and a scenario where you need a specific variable. Before reaching for the calculator, write the rearranged formula with the target variable isolated. Substituting into the rearranged form is faster and less error-prone than substituting first and then solving algebraically.
"""),

    (8, """Units, Conversions, and Formula Results

Many real-world GED problems require you to convert between units before or after applying a formula. If the formula expects feet but the problem gives inches, you must convert first. Skipping this step gives you a numerically calculated but contextually wrong answer.

Key unit relationships to know for the GED:
Length: 12 inches = 1 foot, 3 feet = 1 yard, 5,280 feet = 1 mile
Weight: 16 ounces = 1 pound, 2,000 pounds = 1 ton
Volume: 8 fluid ounces = 1 cup, 2 cups = 1 pint, 2 pints = 1 quart, 4 quarts = 1 gallon
Time: 60 seconds = 1 minute, 60 minutes = 1 hour, 24 hours = 1 day

Metric conversions involve powers of 10. The prefixes kilo- (1,000), centi- (1/100), and milli- (1/1,000) are the most common. So 1 kilometer = 1,000 meters, 1 centimeter = 0.01 meters, 1 millimeter = 0.001 meters.

WORKED EXAMPLE
A rectangular room is 15 feet long and 10 feet wide. You want to install carpet and the carpet cost is listed in square yards. What is the area in square yards?

Step 1: Find the area in square feet first.
A = l x w = 15 x 10 = 150 square feet

Step 2: Convert square feet to square yards.
There are 3 feet in 1 yard, so there are 3 x 3 = 9 square feet in 1 square yard.
150 sq ft / 9 = 16.67 square yards (rounded to two decimal places)

Answer: approximately 16.67 square yards

Note: Do not just divide 150 by 3. Because you are converting square units, you divide by 3^2 = 9, not by 3.

COMMON MISTAKE TO AVOID
Converting linear units and area units use different conversion factors. To convert from square feet to square yards, you divide by 9 (not 3). To convert from cubic feet to cubic yards, you divide by 27 (not 3). Always square or cube the linear conversion factor to match the dimension you are working in.

GED TEST TIP
Read every GED word problem twice — once to understand the scenario and once specifically to check the units. Circle or underline the units in the problem and the units required in the answer. This habit catches conversion errors before you do any math. If the question asks for an answer in square inches and your formula produced square feet, you know you need to convert.
"""),

    (9, """Rounding, Precision, and Money Answers

Rounding is a practical skill used whenever an exact answer is not necessary or not possible. On the GED, you will frequently need to round to a specific decimal place, and many real-world problems — especially those involving money — require rounding to the nearest cent (hundredths place).

Place value review:
- Ones: the digit to the left of the decimal point
- Tenths: first digit after the decimal
- Hundredths: second digit after the decimal (the cents place in money)
- Thousandths: third digit after the decimal

Rounding rule: Look at the digit immediately to the right of the place you are rounding to. If it is 5 or greater, round up. If it is 4 or less, round down (keep the digit the same).

For money: always round to the hundredths place unless the problem specifies otherwise. A calculated cost of $14.2875 rounds to $14.29.

WORKED EXAMPLE 1
Round 47.386 to the nearest tenth.

Step 1: Identify the tenths digit. It is 3 (the digit right after the decimal).
Step 2: Look at the digit to its right. It is 8.
Step 3: Since 8 >= 5, round the tenths digit up: 3 becomes 4.
Step 4: Drop all digits after the tenths place.

Answer: 47.4

WORKED EXAMPLE 2
A cell phone plan costs $28.99 per month. What is the total cost for 8 months?

Step 1: Multiply. 28.99 x 8 = 231.92
Step 2: The answer is already at the hundredths place and is exact.

Answer: $231.92

If the result had been $231.926, you would round down to $231.93 — wait, the third decimal is 6, which is >= 5, so you round the hundredths digit up: $231.93.

COMMON MISTAKE TO AVOID
Students sometimes round at an intermediate step instead of at the final answer. This is called intermediate rounding error. If you round $14.2875 to $14.29 before multiplying by 12, your final answer will differ slightly from the exact answer. Always complete all calculations with full precision and round only at the very end.

GED TEST TIP
When the GED asks for a money amount and the answer choices are all in dollar-and-cent format, compute your answer to at least three decimal places before rounding. This ensures your rounding decision is correct. Also watch for the word "nearest" in the question — "nearest dollar" means rounding to the ones place, not the hundredths.
"""),

    (10, """Multi-Step Formula and Calculator Strategy

The most challenging problems on the GED Math test require you to combine multiple skills: reading a scenario, selecting the right formula, converting units, substituting values, using the calculator correctly, and rounding the final answer. These multi-step problems are worth the most points and are where strategic test-takers separate themselves.

A reliable strategy for multi-step problems:

1. Read the problem completely before writing anything.
2. Identify the final question being asked and the unit of the answer.
3. Write down the formula you will use.
4. List all given values and check that units are consistent.
5. Substitute values into the formula.
6. Calculate using the order of operations, writing each step.
7. Round to the precision the problem requires.
8. Check that your answer is reasonable.

WORKED EXAMPLE
A cylindrical water tank has a radius of 3 feet and a height of 8 feet. Water costs $0.003 per gallon. One cubic foot of water equals 7.48 gallons. What is the cost to fill the tank? Round to the nearest cent.

Step 1: Formula for volume of a cylinder: V = pi x r^2 x h

Step 2: Identify values. r = 3, h = 8, pi ≈ 3.14

Step 3: Substitute. V = 3.14 x 3^2 x 8

Step 4: Exponent first. 3^2 = 9
V = 3.14 x 9 x 8

Step 5: Multiply left to right. 3.14 x 9 = 28.26, then 28.26 x 8 = 226.08 cubic feet

Step 6: Convert to gallons. 226.08 x 7.48 = 1691.0784 gallons

Step 7: Calculate cost. 1691.0784 x 0.003 = 5.0732352

Step 8: Round to nearest cent. $5.07

Answer: $5.07

COMMON MISTAKE TO AVOID
On multi-step problems, students often stop at an intermediate result and choose that as their answer. In the example above, 226.08 and 1691.08 both look like plausible answers. The GED frequently includes intermediate results as wrong answer choices to trap students who stop too soon. Always re-read the final question to confirm you have answered what was actually asked.

GED TEST TIP
Budget your time on multi-step problems. If a problem has four or five steps, expect to spend 2-3 minutes on it. Do not rush through the setup to save time — setup errors cost you the entire problem. Write clearly, perform one operation per line, and check your calculator entries against what is written on your paper. A calm, organized approach on hard problems is what turns a passing score into a strong one.
"""),
]


class Command(BaseCommand):
    help = "Enrich lesson content for GED Order of Operations & Formula Skills"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(course__slug="ged-order-operations-formula-skills", order=order).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(self.style.SUCCESS("Done."))
