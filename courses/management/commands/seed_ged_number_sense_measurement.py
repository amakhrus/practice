"""
Seed a GED Math Foundations mastery course for number sense and measurement.

Run:
    python manage.py seed_ged_number_sense_measurement
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
    "title": "GED Math Foundations: Number Sense & Measurement Mastery",
    "slug": "ged-number-sense-measurement",
    "program": "GED",
    "subject": "math",
    "description": (
        "A complete GED Mathematical Reasoning foundation course for number sense, "
        "signed numbers, rational-number operations, order of operations, factors, "
        "multiples, exponents, roots, scientific notation, measurement units, unit "
        "conversions, and reasonableness checks. The course prepares students for higher GED math "
        "topics by strengthening the quantitative skills that appear across word "
        "problems, formula use, calculator-free work, and data interpretation."
    ),
    "lessons": [
        (
            "1. Place Value, Magnitude, and Estimation",
            r"""
Place value is the structure that tells what a digit is worth. In \(7.049\), the digit 7 is in the ones place, 0 is in the tenths place, 4 is in the hundredths place, and 9 is in the thousandths place. The number is:
\[
7+0.04+0.009.
\]

[[figure:place_value_ladder|The place-value ladder shows how each step left multiplies by 10 and each step right divides by 10.]]

Magnitude means the size of a number. A student with strong magnitude sense can tell that \(0.8\) is close to 1, \(0.08\) is close to 0, and \(80\) is much larger than both. This matters on the GED because answer choices often include decimal-place traps.

Rounding keeps a number close while making it easier to use. To round \(6.847\) to the nearest hundredth, look at the thousandths digit. The hundredths digit is 4, the next digit is 7, so round up to \(6.85\).

Estimation is not guessing. It is a controlled way to predict a reasonable size before using exact calculation. For \(48.7 \times 19.6\), round to \(50 \times 20=1000\). An exact answer near 1000 is reasonable; an answer near 100 or 10,000 is not.

Common misconception: more digits after the decimal do not automatically mean a larger number. \(0.9\) is greater than \(0.125\), even though 0.125 has more decimal digits.

Academic habit: before calculating, ask "about how large should the answer be?" This habit catches many calculator entry errors.

[[check:Round \(6.847\) to the nearest hundredth.|6.85|The hundredths digit is 4. The next digit is 7, so round the 4 up to 5.]]
            """,
        ),
        (
            "2. Integers, Opposites, and Absolute Value",
            r"""
Integers are whole-number positions on both sides of zero:
\[
\ldots,-3,-2,-1,0,1,2,3,\ldots
\]
They are used for debts, temperatures below zero, elevations below sea level, and gains or losses.

[[figure:integer_number_line|A number line organizes negative numbers, zero, and positive numbers by position.]]

Two numbers are **opposites** if they are the same distance from 0 on opposite sides. The opposite of 5 is \(-5\), and the opposite of \(-12\) is 12.

Absolute value measures distance from 0:
\[
|-8|=8,\qquad |8|=8.
\]
Absolute value is never negative because distance is never negative.

Comparison on a number line follows position: numbers farther right are greater. This is why \(-2>-7\). Both are negative, but \(-2\) is closer to zero and lies farther right.

Distance between two numbers can be found by subtracting the smaller location from the larger location. From \(-3\) to 5 is 8 units because \(5-(-3)=8\).

Common misconception: thinking the negative number with the larger digit is greater. Actually, \(-9<-4\) because \(-9\) is farther left.

Academic habit: for signed numbers, sketch a quick number line when the comparison or distance feels uncertain.

[[check:Which is greater, \(-2\) or \(-7\)?|-2|\(-2\) is farther right on the number line.]]
            """,
        ),
        (
            "3. Adding and Subtracting Signed Rational Numbers",
            r"""
Signed arithmetic combines direction with size. A positive number can represent a gain, deposit, or movement right. A negative number can represent a loss, withdrawal, or movement left.

[[figure:signed_operation_rules|Adding and subtracting signed numbers depends on signs, sizes, and opposites.]]

When adding numbers with the same sign, add the absolute values and keep the sign:
\[
-6+(-9)=-15.
\]
Both terms move left, so the result is farther left.

When adding numbers with different signs, subtract the smaller absolute value from the larger absolute value. Keep the sign of the number with the larger absolute value:
\[
-11+4=-7.
\]
The 11-unit movement left is stronger than the 4-unit movement right.

Subtraction means adding the opposite:
\[
5-(-8)=5+8=13.
\]
This rule is especially important because subtracting a negative increases the value.

Fractions and decimals follow the same sign rules. For example:
\[
-\frac{3}{4}+\frac{1}{2}=-\frac{3}{4}+\frac{2}{4}=-\frac{1}{4}.
\]

Common misconception: changing only one sign randomly. In subtraction, rewrite the problem as addition of the opposite; then use the addition rules.

Academic habit: state the operation in words: "subtract negative 8" means "move 8 units in the positive direction."
            """,
        ),
        (
            "4. Multiplying and Dividing Signed Numbers",
            r"""
Multiplication and division use a different sign pattern from addition. For multiplication or division:
- same signs give a positive result
- different signs give a negative result

Examples:
\[
(-6)(-4)=24,\qquad 18\div(-3)=-6.
\]

The size of the result comes from ordinary multiplication or division. The sign comes from the sign rule. A good two-step process is:
1. Ignore signs and compute the size.
2. Decide whether the final sign is positive or negative.

Decimals and fractions use the same rule:
\[
(-2.5)(4)=-10,\qquad -\frac{3}{5}\div\frac{1}{2}=-\frac{6}{5}.
\]

Zero has special rules. Zero times any number is zero. Zero divided by a nonzero number is zero. Division by zero is undefined because no number can be multiplied by 0 to make a nonzero result.

Common misconception: using addition rules for multiplication. For example, \((-6)(-4)\) is positive, even though both numbers are negative.

Academic habit: before multiplying or dividing, count the negative factors. An even number of negative factors gives a positive product; an odd number gives a negative product.

[[check:What is \((-6)(-4)\)?|24|Same signs give a positive product, and \(6\cdot4=24\).]]
            """,
        ),
        (
            "5. Order of Operations and Expression Evaluation",
            r"""
Order of operations is an agreement that makes expressions have one clear value. The standard order is:
1. Parentheses or grouping symbols
2. Exponents and roots
3. Multiplication and division from left to right
4. Addition and subtraction from left to right

For example:
\[
18-3(4)+10\div2=18-12+5=11.
\]
Multiplication and division happen before addition and subtraction.

Parentheses can change the result:
\[
2^3+4(5-2)=8+4(3)=20.
\]

Negative numbers need parentheses when they are squared. The expression \((-3)^2\) means \((-3)(-3)=9\). The expression \(-3^2\) means the opposite of \(3^2\), so it equals \(-9\).

Variables are evaluated by substitution. If \(a=-2\) and \(b=5\), then:
\[
3a-2b=3(-2)-2(5)=-6-10=-16.
\]

Common misconception: working strictly left to right. Left-to-right order applies only within multiplication/division or within addition/subtraction after higher-priority operations are finished.

Academic habit: rewrite one clean line after each operation. Do not try to do all steps mentally when signs or exponents are involved.

[[check:Evaluate \(18-3(4)+10\div2\).|11|Multiply and divide first: \(18-12+5=11\).]]
            """,
        ),
        (
            "6. Factors, Multiples, Prime Factorization, GCF, and LCM",
            r"""
A factor divides a number evenly. A multiple is the result of multiplying by a whole number. For 24, examples of factors are 1, 2, 3, 4, 6, 8, 12, and 24. Examples of multiples are 24, 48, 72, and 96.

A prime number has exactly two positive factors: 1 and itself. A composite number has more than two positive factors. Prime factorization writes a number as a product of primes:
\[
60=2^2\cdot3\cdot5.
\]

[[figure:gcf_lcm_factor_map|Prime factors show both what two numbers share and what both numbers need.]]

The **greatest common factor** (GCF) is the largest factor shared by two or more numbers. For 18 and 30:
\[
18=2\cdot3^2,\qquad 30=2\cdot3\cdot5.
\]
The shared prime factors are 2 and 3, so the GCF is \(2\cdot3=6\).

The **least common multiple** (LCM) is the smallest positive number that is a multiple of both numbers. It uses every prime factor needed by either number:
\[
LCM(18,30)=2\cdot3^2\cdot5=90.
\]

GCF often helps with simplifying or factoring. LCM often helps with common denominators, schedules, and repeated cycles.

Common misconception: confusing GCF and LCM. GCF is usually smaller than or equal to the numbers; LCM is usually larger than or equal to the numbers.

Academic habit: label the task before solving: "largest shared factor" means GCF, while "first shared multiple" means LCM.
            """,
        ),
        (
            "7. Decimal Operations and Precision",
            r"""
Decimals use the same place-value structure as whole numbers, so alignment matters. For adding and subtracting decimals, line up the decimal points:
\[
4.8+0.37=4.80+0.37=5.17.
\]

Subtraction also requires place-value alignment:
\[
12.60-8.95=3.65.
\]
Writing 12.60 instead of 12.6 makes the hundredths place visible.

For multiplication, multiply as if the numbers were whole numbers, then place the decimal by counting total decimal places. For example:
\[
0.06\cdot0.7=0.042.
\]
The factors have three decimal places total, so the product has three decimal places.

For division by a decimal, move the decimal in the divisor until the divisor is a whole number, and move the decimal in the dividend the same number of places:
\[
5.4\div0.9=54\div9=6.
\]

Precision means how exact a measurement or answer is. A result rounded to the nearest tenth is less precise than a result rounded to the nearest hundredth. On the GED, use the rounding direction requested by the problem.

Common misconception: lining up the right edge instead of the decimal point. Decimal operations are place-value operations, so the decimal points must control alignment.

Academic habit: estimate first. Since \(5.4\div0.9\) is close to \(5.4\div1\), an answer near 6 is reasonable.
            """,
        ),
        (
            "8. Comparing Fractions, Decimals, and Percents",
            r"""
Fractions, decimals, and percents are three forms of rational numbers. The GED may ask you to compare them in mixed form, so you need a common language.

To compare, convert to the form that makes the decision easiest. Decimals are often efficient:
\[
\frac{3}{5}=0.6,\qquad 12.5\%=0.125,\qquad \frac{1}{8}=0.125.
\]

Benchmarks help you estimate quickly:
- \(0.25=\frac{1}{4}=25\%\)
- \(0.5=\frac{1}{2}=50\%\)
- \(0.75=\frac{3}{4}=75\%\)
- \(1=100\%\)

When comparing \(\frac{5}{8}\) and \(0.7\), convert \(\frac{5}{8}\) to \(0.625\). Since \(0.7>0.625\), the decimal \(0.7\) is greater.

Ordering mixed rational numbers requires careful conversion. For example:
\[
0.07 < \frac{1}{8}=0.125 < \frac{1}{2}=0.5 < 0.6 < \frac{4}{5}=0.8.
\]

Common misconception: comparing only numerators, denominators, or the number of decimal digits. The real question is value, not appearance.

Academic habit: write every value in one form before ordering. Circle the smallest and largest first, then place the middle values.

[[check:Which is greater, \(\frac{5}{8}\) or \(0.7\)?|0.7|\(\frac{5}{8}=0.625\), and \(0.7\) is greater.]]
            """,
        ),
        (
            "9. Exponents, Squares, Cubes, and Roots",
            r"""
An exponent tells how many times to use a base as a factor:
\[
4^3=4\cdot4\cdot4=64.
\]
The base is 4, and the exponent is 3.

Squares and square roots undo each other:
\[
9^2=81,\qquad \sqrt{81}=9.
\]
On the GED, square roots often appear in geometry, especially with the Pythagorean theorem.

Cubes and cube roots also undo each other:
\[
3^3=27,\qquad \sqrt[3]{27}=3.
\]

Exponent patterns make powers easier to handle:
\[
2^3\cdot2^2=2^{3+2}=2^5=32.
\]
This works because the same base is being multiplied.

Negative bases require parentheses. \((-2)^4=16\) because there are four negative factors. But \(-2^4=-16\) because the exponent applies to 2 before the outside negative sign.

Common misconception: multiplying the base by the exponent. \(4^3\) is not \(4\cdot3\); it is \(4\cdot4\cdot4\).

Academic habit: expand a power when the sign is confusing. Writing the repeated factors prevents sign errors.
            """,
        ),
        (
            "10. Scientific Notation and Powers of Ten",
            r"""
Scientific notation writes very large or very small numbers compactly:
\[
a\times10^n
\]
where \(1\le a<10\) and \(n\) is an integer.

[[figure:scientific_notation_ladder|Powers of 10 show how the decimal point moves when numbers grow or shrink by factors of 10.]]

Positive exponents make numbers larger:
\[
5.2\times10^4=52,000.
\]
The decimal moves 4 places right.

Negative exponents make numbers smaller:
\[
7.3\times10^{-4}=0.00073.
\]
The decimal moves 4 places left.

To convert a standard number into scientific notation, place the decimal after the first nonzero digit and count how many places it moved. For \(0.00073\), the decimal moves 4 places right to make 7.3, so the exponent is \(-4\):
\[
0.00073=7.3\times10^{-4}.
\]

Numbers in scientific notation can be compared by exponent first. \(1.2\times10^6\) is greater than \(8.5\times10^5\) because \(10^6\) is ten times the size of \(10^5\).

Common misconception: making the first factor greater than or equal to 10. \(52\times10^3\) is related, but standard scientific notation is \(5.2\times10^4\).

Academic habit: after converting, check the direction. Large standard numbers should have positive exponents; small decimals should have negative exponents.
            """,
        ),
        (
            "11. Measurement Units and Dimensional Analysis",
            r"""
Measurement connects number sense to real objects. Units tell what is being measured: length, area, volume, weight, time, or rate. A number without a unit is incomplete in a word problem.

Unit conversion changes the unit name while preserving the same measured amount. For example, 3 feet and 36 inches describe the same length.

Dimensional analysis uses conversion factors equal to 1. For example, because \(1\text{ ft}=12\text{ in}\), the fraction \(\frac{12\text{ in}}{1\text{ ft}}\) has the same value as 1.

[[figure:unit_conversion_bridge|A conversion factor is placed so the old unit cancels and the desired unit remains.]]

Convert 3.5 feet to inches:
\[
3.5\text{ ft}\times\frac{12\text{ in}}{1\text{ ft}}=42\text{ in}.
\]
The feet cancel, leaving inches.

Metric conversions use powers of 10:
\[
2.4\text{ kg}=2400\text{ g},\qquad 150\text{ cm}=1.5\text{ m}.
\]

Area and volume units require extra care. If 1 yard equals 3 feet, then \(1\text{ yd}^2=9\text{ ft}^2\), not 3 square feet, because both length dimensions are converted.

Rates include compound units, such as miles per hour or dollars per pound. A car traveling 45 miles per hour for 2.5 hours travels:
\[
45\cdot2.5=112.5\text{ miles}.
\]

Common misconception: multiplying every conversion without checking whether units cancel. The setup is correct only when the unwanted unit appears once on top and once on bottom.

Academic habit: write units in every step. Units are not decoration; they are part of the reasoning.
            """,
        ),
        (
            "12. Reasonableness, Calculator Strategy, and GED Problem Control",
            r"""
The GED math test rewards controlled problem solving. A correct procedure is important, but so is judging whether the answer fits the situation.

A strong problem-control routine is:
1. Identify what the question asks.
2. Label known values and units.
3. Estimate the answer size.
4. Choose an operation or formula.
5. Calculate carefully.
6. Check the answer against the estimate and the context.

For \(19.8\times50.6\), estimate \(20\times50=1000\). If a calculator display shows 10018.8, the decimal point was probably entered incorrectly.

In word problems, operation choice comes from meaning:
- total groups of equal size often means multiplication
- sharing or rate per one unit often means division
- increase, decrease, deposit, or withdrawal often means signed addition/subtraction
- repeated scale by powers of 10 often means decimal movement or scientific notation

Reasonableness also includes context. A wall cannot require \(-8\) gallons of paint. A probability cannot be greater than 1. A trip distance should not be in square feet.

Common misconception: trusting a calculator answer without checking the size or unit. Calculators follow entries; they do not know whether the entry matched the problem.

Academic habit: write one sentence at the end: "The answer is reasonable because..." This is a fast way to catch impossible units, signs, or magnitudes.

[[check:Why is 10,018.8 unreasonable for \(19.8\times50.6\)?|It is far from the estimate near 1000.|Rounding gives \(20\times50=1000\), so 10,018.8 is about ten times too large.]]
            """,
        ),
    ],
    "mcqs": [
        item(r"In \(7.049\), what is the value of the digit 4?", r"\(0.04\)", [r"\(0.4\)", r"\(0.004\)", r"\(4\)"], ["The 4 is two places to the right of the decimal point.", "That place is the hundredths place.", "The value is \(4\) hundredths, or \(0.04\)."], "reading the digit as if it were in the tenths or thousandths place.", 1),
        item(r"Round \(6.847\) to the nearest hundredth.", r"\(6.85\)", [r"\(6.84\)", r"\(6.8\)", r"\(6.8470\)"], ["The hundredths digit is 4.", "The next digit, in the thousandths place, is 7.", "Because 7 is at least 5, round the hundredths digit up to get \(6.85\)."], "rounding to the wrong place value.", 1),
        item(r"Which number is greatest?", r"\(0.9\)", [r"\(0.125\)", r"\(0.45\)", r"\(0.09\)"], ["Compare place value or convert to hundredths/thousandths.", "\(0.9=0.900\), which is larger than \(0.125\), \(0.450\), and \(0.090\).", "Therefore \(0.9\) is greatest."], "choosing the number with the most decimal digits.", 1),
        item(r"Estimate \(48.7\times19.6\). Which is most reasonable?", r"\(1{,}000\)", [r"\(100\)", r"\(10{,}000\)", r"\(50\)"], ["Round \(48.7\) to about 50.", "Round \(19.6\) to about 20.", "\(50\times20=1000\), so 1000 is the best estimate."], "moving a decimal place and choosing an answer ten times too small or too large.", 1),
        item(r"Which list is ordered from least to greatest?", r"\(0.07,\ 0.7,\ 7\)", [r"\(7,\ 0.7,\ 0.07\)", r"\(0.7,\ 0.07,\ 7\)", r"\(0.07,\ 7,\ 0.7\)"], ["Compare magnitudes.", "\(0.07\) is seven hundredths, \(0.7\) is seven tenths, and \(7\) is seven ones.", "Thus \(0.07<0.7<7\)."], "treating all numbers with a 7 as the same size.", 1),

        item(r"What is \(|-8|\)?", r"\(8\)", [r"\(-8\)", r"\(0\)", r"\(16\)"], ["Absolute value is distance from zero.", "The number \(-8\) is 8 units from zero.", "Therefore \(|-8|=8\)."], "thinking absolute value keeps the negative sign.", 1),
        item(r"Use the number line idea: how far apart are \(-3\) and \(5\)?", r"\(8\) units", [r"\(2\) units", r"\(-8\) units", r"\(5\) units"], ["Distance is positive.", "Compute \(5-(-3)=8\).", "The points are 8 units apart."], "subtracting the digits only or giving distance as a negative number.", 1),
        item(r"Which comparison is true?", r"\(-2>-7\)", [r"\(-7>-2\)", r"\(-2<-7\)", r"\(-2=-7\)"], ["On a number line, farther right means greater.", "\(-2\) lies to the right of \(-7\).", "So \(-2>-7\)."], "thinking the larger digit always makes the negative number larger.", 1),
        item(r"The temperature changes from \(-6^\circ\) to \(3^\circ\). How many degrees did it rise?", r"\(9^\circ\)", [r"\(3^\circ\)", r"\(6^\circ\)", r"\(-9^\circ\)"], ["A rise is a positive change.", "Compute \(3-(-6)=9\).", "The temperature rose \(9^\circ\)."], "subtracting \(6-3\) or ignoring the negative starting point.", 2),
        item(r"Which number is the opposite of \(-12\)?", r"\(12\)", [r"\(-12\)", r"\(\frac{1}{12}\)", r"\(0\)"], ["Opposites have the same distance from zero and opposite signs.", "\(-12\) is 12 units left of zero.", "Its opposite is 12."], "confusing opposite with reciprocal.", 1),

        item(r"Compute \(-7+12\).", r"\(5\)", [r"\(-19\)", r"\(-5\)", r"\(19\)"], ["The signs are different, so subtract the absolute values.", "\(12-7=5\).", "The larger absolute value is positive, so the result is \(5\)."], "adding the absolute values and keeping a negative sign.", 1),
        item(r"Compute \(5-(-8)\).", r"\(13\)", [r"\(-3\)", r"\(3\)", r"\(-13\)"], ["Subtracting a number means adding its opposite.", "\(5-(-8)=5+8\).", "The result is 13."], "treating subtraction of a negative as ordinary subtraction.", 1),
        item(r"Compute \(-\frac{3}{4}+\frac{1}{2}\).", r"\(-\frac{1}{4}\)", [r"\(\frac{1}{4}\)", r"\(-\frac{5}{4}\)", r"\(\frac{5}{4}\)"], ["Rewrite \(\frac{1}{2}\) as \(\frac{2}{4}\).", "Compute \(-\frac{3}{4}+\frac{2}{4}=-\frac{1}{4}\).", "The negative fraction has the larger absolute value, so the result is negative."], "adding numerators without considering signs.", 2),
        item(r"A bank balance is \(-\$15\). A deposit of \(\$42\) is made. What is the new balance?", r"\(\$27\)", [r"\(-\$57\)", r"\(\$57\)", r"\(-\$27\)"], ["The balance starts at \(-15\).", "A deposit is positive, so compute \(-15+42\).", "The result is 27 dollars."], "adding the amounts but keeping the old negative sign.", 1),

        item(r"Compute \((-6)(-4)\).", r"\(24\)", [r"\(-24\)", r"\(-10\)", r"\(10\)"], ["The signs are the same.", "Same signs in multiplication give a positive product.", "\(6\cdot4=24\), so the answer is 24."], "using addition sign rules instead of multiplication sign rules.", 1),
        item(r"Compute \(18\div(-3)\).", r"\(-6\)", [r"\(6\)", r"\(-15\)", r"\(15\)"], ["The signs are different.", "Different signs in division give a negative result.", "\(18\div3=6\), so the answer is \(-6\)."], "dropping the negative sign after dividing.", 1),
        item(r"Compute \((-2.5)(4)\).", r"\(-10\)", [r"\(10\)", r"\(-6.5\)", r"\(-1.6\)"], ["The signs are different, so the product is negative.", "Compute \(2.5\cdot4=10\).", "The answer is \(-10\)."], "multiplying correctly but losing the negative sign.", 1),
        item(r"Which expression is undefined?", r"\(12\div0\)", [r"\(0\div12\)", r"\(12\cdot0\)", r"\(0+12\)"], ["Division by zero is undefined.", "\(12\div0\) asks what number times 0 gives 12, and no such number exists.", "Therefore \(12\div0\) is undefined."], "confusing zero divided by a number with a number divided by zero.", 2),

        item(r"Evaluate \(18-3(4)+10\div2\).", r"\(11\)", [r"\(35\)", r"\(8\)", r"\(20\)"], ["Multiply and divide first: \(3(4)=12\) and \(10\div2=5\).", "The expression becomes \(18-12+5\).", "Compute left to right: \(6+5=11\)."], "working strictly from left to right.", 2),
        item(r"Evaluate \(2^3+4(5-2)\).", r"\(20\)", [r"\(36\)", r"\(14\)", r"\(32\)"], ["Evaluate parentheses first: \(5-2=3\).", "Evaluate the exponent: \(2^3=8\).", "Compute \(8+4(3)=8+12=20\)."], "multiplying before simplifying the parentheses or treating \(2^3\) as \(2\cdot3\).", 2),
        item(r"What is \((-3)^2\)?", r"\(9\)", [r"\(-9\)", r"\(-6\)", r"\(6\)"], ["The parentheses make the base \(-3\).", "\((-3)^2=(-3)(-3)\).", "The product is 9."], "forgetting that the negative is inside the parentheses.", 1),
        item(r"What is \(-3^2\)?", r"\(-9\)", [r"\(9\)", r"\(-6\)", r"\(6\)"], ["Without parentheses, the exponent applies to 3 only.", "Compute \(3^2=9\).", "Then apply the outside negative to get \(-9\)."], "treating \(-3^2\) as \((-3)^2\).", 2),
        item(r"If \(a=-2\) and \(b=5\), evaluate \(3a-2b\).", r"\(-16\)", [r"\(4\)", r"\(-4\)", r"\(16\)"], ["Substitute carefully: \(3(-2)-2(5)\).", "Compute \(-6-10\).", "The value is \(-16\)."], "dropping one negative sign during substitution.", 2),

        item(r"What is the prime factorization of \(60\)?", r"\(2^2\cdot3\cdot5\)", [r"\(2\cdot30\)", r"\(6\cdot10\)", r"\(3^2\cdot5\)"], ["Break 60 into prime factors.", "\(60=2\cdot30=2\cdot2\cdot15=2^2\cdot3\cdot5\).", "All factors are prime."], "stopping before all factors are prime.", 2),
        item(r"What is the greatest common factor of 18 and 30?", r"\(6\)", [r"\(90\)", r"\(3\)", r"\(12\)"], ["List or factor the numbers.", "\(18=2\cdot3^2\) and \(30=2\cdot3\cdot5\).", "The shared prime factors are \(2\cdot3=6\)."], "finding a common factor but not the greatest one, or finding the LCM.", 2),
        item(r"What is the least common multiple of 8 and 12?", r"\(24\)", [r"\(4\)", r"\(20\)", r"\(96\)"], ["Multiples of 8 include 8, 16, 24.", "Multiples of 12 include 12, 24.", "The first shared positive multiple is 24."], "answering with the GCF instead of the LCM.", 2),
        item(r"Use the GCF to factor \(36+24\).", r"\(12(3+2)\)", [r"\(6(6+4)\)", r"\(24(12+1)\)", r"\(60(1)\)"], ["The greatest common factor of 36 and 24 is 12.", "Divide each term by 12: \(36/12=3\), \(24/12=2\).", "So \(36+24=12(3+2)\)."], "factoring with a smaller common factor when the problem asks for the GCF.", 2),
        item(r"Two bells ring every 8 minutes and every 12 minutes. If they ring together now, when will they next ring together?", "In 24 minutes", ["In 4 minutes", "In 20 minutes", "In 96 minutes"], ["This is a repeated-cycle problem, so use LCM.", "The LCM of 8 and 12 is 24.", "They next ring together in 24 minutes."], "using GCF because the word common appears.", 2),

        item(r"Compute \(4.8+0.37\).", r"\(5.17\)", [r"\(0.85\)", r"\(4.117\)", r"\(8.5\)"], ["Line up decimal points: \(4.80+0.37\).", "Add hundredths, tenths, and ones by place value.", "The sum is \(5.17\)."], "lining up the right edge instead of the decimal point.", 1),
        item(r"Compute \(12.6-8.95\).", r"\(3.65\)", [r"\(4.35\)", r"\(3.75\)", r"\(21.55\)"], ["Write \(12.6\) as \(12.60\).", "Subtract \(8.95\) by place value.", "The result is \(3.65\)."], "forgetting the placeholder zero in the hundredths place.", 2),
        item(r"Compute \(0.06\cdot0.7\).", r"\(0.042\)", [r"\(0.42\)", r"\(0.0042\)", r"\(4.2\)"], ["Multiply the digits: \(6\cdot7=42\).", "The factors have three decimal places total.", "Place three decimal places in the product: \(0.042\)."], "placing the decimal one place too far left or right.", 2),
        item(r"Compute \(5.4\div0.9\).", r"\(6\)", [r"\(0.6\)", r"\(60\)", r"\(4.86\)"], ["Move the decimal in both numbers one place right.", "\(5.4\div0.9=54\div9\).", "The quotient is 6."], "moving the decimal in only one number.", 2),

        item(r"Write \(\frac{3}{5}\) as a decimal.", r"\(0.6\)", [r"\(0.35\)", r"\(1.67\)", r"\(0.06\)"], ["Divide numerator by denominator or use equivalent tenths.", "\(\frac{3}{5}=\frac{6}{10}\).", "So \(\frac{3}{5}=0.6\)."], "writing the numerator and denominator as decimal digits.", 1),
        item(r"Write \(0.125\) as a simplified fraction.", r"\(\frac{1}{8}\)", [r"\(\frac{125}{10}\)", r"\(\frac{5}{8}\)", r"\(\frac{1}{4}\)"], ["Read \(0.125\) as \(125/1000\).", "Simplify by dividing numerator and denominator by 125.", "The simplified fraction is \(\frac{1}{8}\)."], "stopping at an unsimplified or place-value incorrect fraction.", 2),
        item(r"Which is greater: \(\frac{5}{8}\) or \(0.7\)?", r"\(0.7\)", [r"\(\frac{5}{8}\)", "They are equal.", "Cannot be determined"], ["Convert \(\frac{5}{8}\) to a decimal: \(5\div8=0.625\).", "Compare \(0.625\) and \(0.7\).", "\(0.7\) is greater."], "assuming the fraction is larger because 5 and 8 look larger than 0.7.", 2),
        item(r"Order these from least to greatest: \(0.07,\ \frac{1}{8},\ \frac{1}{2},\ 0.6,\ \frac{4}{5}\).", r"\(0.07,\ \frac{1}{8},\ \frac{1}{2},\ 0.6,\ \frac{4}{5}\)", [r"\(\frac{1}{8},\ 0.07,\ \frac{1}{2},\ 0.6,\ \frac{4}{5}\)", r"\(0.6,\ \frac{4}{5},\ \frac{1}{2},\ \frac{1}{8},\ 0.07\)", r"\(0.07,\ \frac{1}{2},\ \frac{1}{8},\ 0.6,\ \frac{4}{5}\)"], ["Convert key fractions: \(\frac{1}{8}=0.125\), \(\frac{1}{2}=0.5\), and \(\frac{4}{5}=0.8\).", "Compare decimals: \(0.07<0.125<0.5<0.6<0.8\).", "Write the original forms in that order."], "ordering by appearance instead of value.", 3),
        item(r"Which is equivalent to \(37.5\%\)?", r"\(0.375\)", [r"\(3.75\)", r"\(37.5\)", r"\(0.0375\)"], ["Percent means per hundred.", "Divide \(37.5\) by 100.", "The decimal is \(0.375\)."], "moving the decimal point the wrong number of places.", 1),

        item(r"Compute \(4^3\).", r"\(64\)", [r"\(12\)", r"\(16\)", r"\(7\)"], ["An exponent tells repeated multiplication.", "\(4^3=4\cdot4\cdot4\).", "The value is 64."], "multiplying the base by the exponent.", 1),
        item(r"What is \(\sqrt{81}\)?", r"\(9\)", [r"\(40.5\)", r"\(8\)", r"\(18\)"], ["A square root asks what number squared gives the radicand.", "\(9^2=81\).", "So \(\sqrt{81}=9\)."], "dividing by 2 instead of finding the square root.", 1),
        item(r"What is \(\sqrt[3]{27}\)?", r"\(3\)", [r"\(9\)", r"\(6\)", r"\(24\)"], ["A cube root asks what number cubed gives 27.", "\(3^3=27\).", "Therefore \(\sqrt[3]{27}=3\)."], "confusing cube root with square root.", 2),
        item(r"Simplify \(2^3\cdot2^2\).", r"\(32\)", [r"\(64\)", r"\(12\)", r"\(16\)"], ["The bases are the same, so add exponents: \(2^{3+2}=2^5\).", "Compute \(2^5=32\).", "The simplified value is 32."], "multiplying the exponents instead of adding them.", 2),
        item(r"What is \((-2)^4\)?", r"\(16\)", [r"\(-16\)", r"\(8\)", r"\(-8\)"], ["The base is \(-2\) because of the parentheses.", "Four negative factors make a positive product.", "\((-2)^4=16\)."], "dropping the parentheses and making the answer negative.", 2),

        item(r"Write \(5.2\times10^4\) in standard form.", r"\(52{,}000\)", [r"\(5{,}200\)", r"\(0.00052\)", r"\(520{,}000\)"], ["A positive exponent moves the decimal right.", "Move the decimal in 5.2 four places right.", "The number is 52,000."], "moving the decimal the wrong number of places.", 1),
        item(r"Write \(0.00073\) in scientific notation.", r"\(7.3\times10^{-4}\)", [r"\(7.3\times10^4\)", r"\(73\times10^{-5}\)", r"\(0.73\times10^{-3}\)"], ["Move the decimal to make a number between 1 and 10: \(7.3\).", "The original is a small decimal, so the exponent is negative.", "The decimal moved 4 places, so \(0.00073=7.3\times10^{-4}\)."], "using a positive exponent for a small decimal or a first factor not in standard form.", 2),
        item(r"Add \((3.1\times10^6)+(2.4\times10^6)\).", r"\(5.5\times10^6\)", [r"\(5.5\times10^{12}\)", r"\(7.44\times10^6\)", r"\(0.7\times10^6\)"], ["The powers of 10 match.", "Add the coefficients: \(3.1+2.4=5.5\).", "Keep the common power: \(5.5\times10^6\)."], "adding the exponents when adding numbers.", 2),
        item(r"Multiply \((6\times10^3)(2\times10^4)\).", r"\(1.2\times10^8\)", [r"\(12\times10^7\)", r"\(8\times10^7\)", r"\(12\times10^{12}\)"], ["Multiply coefficients: \(6\cdot2=12\).", "Multiply powers of 10 by adding exponents: \(10^3\cdot10^4=10^7\).", "Rewrite \(12\times10^7\) as \(1.2\times10^8\)."], "leaving the first factor outside the 1 to 10 scientific-notation range.", 3),
        item(r"Which number is larger?", r"\(1.2\times10^6\)", [r"\(8.5\times10^5\)", "They are equal.", "Cannot be compared"], ["Compare powers of ten first.", "\(10^6\) is ten times \(10^5\).", "\(1.2\times10^6=1,200,000\), which is larger than \(850,000\)."], "comparing only the coefficients and choosing 8.5.", 2),

        item(r"Convert 3.5 feet to inches. Use \(1\text{ ft}=12\text{ in}\).", r"\(42\text{ in}\)", [r"\(15.5\text{ in}\)", r"\(0.292\text{ in}\)", r"\(35\text{ in}\)"], ["Use the conversion factor \(12\text{ in}/1\text{ ft}\).", "Compute \(3.5\cdot12=42\).", "The result is \(42\text{ in}\)."], "dividing by 12 instead of multiplying when converting feet to inches.", 1),
        item(r"Convert \(2.4\text{ kg}\) to grams. Use \(1\text{ kg}=1000\text{ g}\).", r"\(2400\text{ g}\)", [r"\(240\text{ g}\)", r"\(0.0024\text{ g}\)", r"\(24{,}000\text{ g}\)"], ["Kilograms are larger than grams, so the number of grams should be larger.", "Multiply \(2.4\) by 1000.", "The result is \(2400\text{ g}\)."], "moving the decimal in the wrong direction.", 1),
        item(r"Convert \(150\text{ cm}\) to meters. Use \(100\text{ cm}=1\text{ m}\).", r"\(1.5\text{ m}\)", [r"\(15\text{ m}\)", r"\(0.15\text{ m}\)", r"\(1500\text{ m}\)"], ["Centimeters are smaller than meters, so the number of meters should be smaller.", "Divide \(150\) by 100.", "The result is \(1.5\text{ m}\)."], "multiplying when converting from smaller units to larger units.", 1),
        item(r"A car travels \(45\) miles per hour for \(2.5\) hours. How far does it travel?", r"\(112.5\) miles", ["18 miles", "47.5 miles", "180 miles"], ["Distance equals rate times time.", "Compute \(45\cdot2.5=112.5\).", "The car travels \(112.5\) miles."], "dividing by time even though rate and time are given.", 2),
        item(r"Convert 5 yards to feet. Use \(1\text{ yd}=3\text{ ft}\).", r"\(15\text{ ft}\)", [r"\(\frac{5}{3}\text{ ft}\)", r"\(8\text{ ft}\)", r"\(30\text{ ft}\)"], ["One yard contains 3 feet.", "Multiply \(5\) by 3.", "The result is \(15\text{ ft}\)."], "dividing by 3 when converting to the smaller unit.", 1),
        item(r"If \(1\text{ yd}=3\text{ ft}\), then \(1\text{ yd}^2\) equals how many square feet?", r"\(9\text{ ft}^2\)", [r"\(3\text{ ft}^2\)", r"\(6\text{ ft}^2\)", r"\(12\text{ ft}^2\)"], ["A square yard is 1 yard by 1 yard.", "Convert both dimensions: \(3\text{ ft}\) by \(3\text{ ft}\).", "Area is \(3\cdot3=9\text{ ft}^2\)."], "using the linear conversion factor for an area conversion.", 3),

        item(r"Best estimate: \(19.8\times50.6\).", r"About \(1{,}000\)", ["About \(100\)", "About \(10{,}000\)", "About \(70\)"], ["Round \(19.8\) to 20.", "Round \(50.6\) to 50.", "\(20\cdot50=1000\)."], "ignoring the size of the factors before multiplying.", 1),
        item(r"A student enters \(19.8\times50.6\) and gets \(10{,}018.8\). Why should the student be suspicious?", "The estimate is near \(1{,}000\), not \(10{,}000\).", ["The product must be less than 50.", "Any decimal multiplication must be less than 1.", "The answer has a comma."], ["Estimate first: \(20\cdot50=1000\).", "\(10,018.8\) is about ten times the estimate.", "The student should check decimal entry or operation."], "trusting a calculator display without a reasonableness check.", 2),
        item(r"A store sells 4 notebooks at \(\$6.75\) each plus a \(\$2.50\) fee. What is the total cost?", r"\(\$29.50\)", [r"\(\$27.00\)", r"\(\$9.25\)", r"\(\$24.50\)"], ["Multiply the repeated cost: \(4\cdot6.75=27.00\).", "Add the fee: \(27.00+2.50=29.50\).", "The total cost is \(\$29.50\)."], "adding the fee before multiplying or forgetting the fee.", 2),
        item(r"Which answer is impossible for a probability?", r"\(1.25\)", [r"\(0\)", r"\(\frac{1}{2}\)", r"\(0.98\)"], ["A probability must be between 0 and 1 inclusive.", "\(1.25\) is greater than 1.", "Therefore it is impossible as a probability."], "forgetting that probability has a maximum value of 1.", 1),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Math Foundations: Number Sense & Measurement Mastery course (MCQ only)."

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
