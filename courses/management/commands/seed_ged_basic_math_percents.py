"""
Seed a dedicated GED Basic Math percents mastery course.

Run:
    python manage.py seed_ged_basic_math_percents
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Basic Math: Percents Mastery",
    "slug": "ged-basic-math-percents-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep Basic Math course focused only on percents. Students learn percent "
        "meaning, percent-decimal-fraction conversion, percent of a number, discounts, "
        "tax, tips, percent increase and decrease, reverse percent, and GED-style case "
        "studies from shopping, paychecks, test scores, budgeting, and data."
    ),
    "lessons": [
        (
            "1. What Percent Means: Per Hundred",
            r"""
Percent means **per hundred**. The symbol \(\%\) is a shortcut for "out of 100."

\[
37\%=\frac{37}{100}=0.37.
\]

[[figure:percent_grid|A 100-grid makes percent literal: 37 shaded squares out of 100 equals 37%.]]

Think of percent as a common language. If one class has 18 out of 20 students present and another has 27 out of 30 present, the counts are different. Percents let us compare fairly:
\[
\frac{18}{20}=90\%,\qquad \frac{27}{30}=90\%.
\]
Both classes have the same attendance rate.

Three interpretations matter:
- **Part of a whole:** 25% of a pizza means 25 out of 100 equal parts.
- **Rate:** 6% sales tax means 6 dollars per 100 dollars.
- **Change:** 30% increase means the change is 30 out of every 100 of the original amount.

Case study - test score: A student answers 36 questions correctly out of 40. The score is
\[
\frac{36}{40}=0.90=90\%.
\]

Common mistake: reading 0.37 as 37%. That is correct. But reading 0.037 as 37% is not; \(0.037=3.7\%\).

[[check:Write \(42\%\) as a fraction over 100.|42/100|Percent means out of 100.]]
            """,
        ),
        (
            "2. Converting Percents, Decimals, and Fractions",
            r"""
Percents, decimals, and fractions are three names for the same amount.

[[figure:percent_conversion|The same value can be written as percent, fraction, simplified fraction, or decimal.]]

**Percent to decimal:** divide by 100, or move the decimal two places left.
\[
25\%=0.25,\qquad 7\%=0.07,\qquad 125\%=1.25.
\]

**Decimal to percent:** multiply by 100, or move the decimal two places right.
\[
0.63=63\%,\qquad 0.08=8\%,\qquad 1.4=140\%.
\]

**Percent to fraction:** write over 100, then simplify.
\[
40\%=\frac{40}{100}=\frac{2}{5}.
\]

**Fraction to percent:** divide numerator by denominator, then multiply by 100.
\[
\frac{3}{4}=0.75=75\%.
\]

Case study - survey: If \(\frac{9}{20}\) of students prefer online practice, then \(9\div20=0.45=45\%\).

Common mistake: moving the decimal the wrong direction. Percent to decimal moves left because a percent is a smaller decimal form.

[[check:Write \(0.08\) as a percent.|8%;;8|Move the decimal two places right.]]
            """,
        ),
        (
            "3. Finding a Percent of a Number",
            r"""
The core percent equation is:
\[
\text{part}=\text{percent as a decimal}\times\text{whole}.
\]

[[figure:percent_equation_triangle|Cover the unknown: part = percent times whole.]]

Example: Find 30% of 150.
\[
30\%=0.30,\qquad 0.30(150)=45.
\]
So 30% of 150 is 45.

Mental shortcuts help:
- 10% means divide by 10.
- 5% is half of 10%.
- 25% is one fourth.
- 50% is one half.
- 75% is three fourths.

Example: 15% of 80. Find 10% and 5%:
\[
10\%\text{ of }80=8,\qquad 5\%\text{ of }80=4.
\]
So 15% of 80 is 12.

Case study - attendance: A GED class has 24 students. If 75% completed the homework, then
\[
0.75(24)=18.
\]
Eighteen students completed it.

Common mistake: using 30 instead of 0.30. \(30(150)=4500\), which is not reasonable for 30% of 150.

[[check:What is \(15\%\) of 80?|12|Use \(0.15\times80\), or 10% plus 5%.]]
            """,
        ),
        (
            "4. Finding the Percent When You Know Part and Whole",
            r"""
Sometimes the question gives the part and whole, and asks for the percent.

Use:
\[
\text{percent}=\frac{\text{part}}{\text{whole}}\times100\%.
\]

Example: 18 is what percent of 72?
\[
\frac{18}{72}=0.25=25\%.
\]

Another example: A student got 42 out of 50 questions correct.
\[
\frac{42}{50}=0.84=84\%.
\]

Case study - budget: A family spends 450 dollars on rent from a 1,800 dollar monthly budget.
\[
\frac{450}{1800}=0.25=25\%.
\]
Rent is 25% of the budget.

Language clues:
- "What percent of" usually means part divided by whole.
- "is" often marks the part.
- "of" often points to the whole.

In "18 is what percent of 72," 18 is the part and 72 is the whole.

Common mistake: dividing whole by part. \(72\div18=4\), which would become 400%, not the correct 25%.

[[check:\(18\) is what percent of \(72\)?|25%;;25|Divide part by whole: \(18/72\).]]
            """,
        ),
        (
            "5. Discounts, Sale Prices, and Coupons",
            r"""
A discount lowers the original price. If an item is 25% off, the store removes 25% and you pay the remaining 75%.

[[figure:percent_discount_bar|A 25% discount means the paid part is 75% of the original price.]]

Method 1 - subtract the discount:
\[
\text{discount}=0.25(80)=20,\qquad \text{sale price}=80-20=60.
\]

Method 2 - pay the remaining percent:
\[
75\%=0.75,\qquad 0.75(80)=60.
\]

Both methods are correct. The second method is faster when you only need the final price.

Case study - stacked coupon warning: A store takes 20% off a 100 dollar item, then another 10% off the sale price. The price is not 70 dollars. First:
\[
100(0.80)=80.
\]
Then:
\[
80(0.90)=72.
\]
Sequential discounts apply to the new price each time.

Common mistake: adding discount percents without checking the base. 20% off then 10% off is not the same as 30% off when the second discount is applied after the first.

[[check:A 120 dollar jacket is 25% off. What is the sale price?|90|Pay 75% of the original price: \(0.75\times120\).]]
            """,
        ),
        (
            "6. Sales Tax, Tips, Fees, and Commission",
            r"""
Tax, tips, fees, and commission usually **increase** an amount.

For sales tax:
\[
\text{total}=\text{price}+\text{tax}.
\]
If tax is 6%, then the total is 106% of the price:
\[
\text{total}=1.06\times\text{price}.
\]

Example: A 50 dollar item with 6% tax.
\[
\text{tax}=0.06(50)=3,\qquad \text{total}=50+3=53.
\]

Tip example: A restaurant bill is 36 dollars and the tip is 20%.
\[
0.20(36)=7.20.
\]
Total with tip:
\[
36+7.20=43.20.
\]

Commission example: A salesperson earns 8% commission on 2,500 dollars in sales.
\[
0.08(2500)=200.
\]

Case study - delivery fee: A food order costs 28 dollars. A 15% tip is added, plus a 3 dollar delivery fee. Tip:
\[
0.15(28)=4.20.
\]
Total:
\[
28+4.20+3=35.20.
\]

Common mistake: calculating tip after adding unrelated fees when the problem says the tip is based on the food bill only. Read what the percent applies to.

[[check:A 50 dollar item has 6% tax. What is the total price?|53;;$53|Tax is \(0.06\times50=3\), then add it to 50.]]
            """,
        ),
        (
            "7. Percent Increase and Percent Decrease",
            r"""
Percent change compares the **change** to the **original** amount.

\[
\text{percent change}=\frac{\text{new}-\text{old}}{\text{old}}\times100\%.
\]

[[figure:percent_change_arrow|The change is compared to the old value, not the new value.]]

Increase example: A price rises from 50 dollars to 65 dollars.
\[
\text{change}=65-50=15.
\]
\[
\frac{15}{50}=0.30=30\%.
\]
This is a 30% increase.

Decrease example: A price drops from 80 dollars to 60 dollars.
\[
\text{change}=60-80=-20.
\]
The amount of decrease is 20:
\[
\frac{20}{80}=0.25=25\%.
\]
This is a 25% decrease.

Case study - population: A town grows from 2,000 people to 2,500 people. Change \(=500\). Percent increase:
\[
\frac{500}{2000}=0.25=25\%.
\]

Common mistake: dividing by the new value. Percent change is measured from the original value unless the problem clearly says otherwise.

[[check:A value grows from 200 to 250. What is the percent increase?|25%;;25|The change is 50. Divide by the original value, 200.]]
            """,
        ),
        (
            "8. Reverse Percent: Finding the Original",
            r"""
Reverse percent problems give the final amount and ask for the original. These feel harder because the original is hidden.

Use this idea:
\[
\text{final}=\text{multiplier}\times\text{original}.
\]

If a price after 20% off is 64 dollars, then the customer paid 80% of the original:
\[
64=0.80x.
\]
Solve:
\[
x=\frac{64}{0.80}=80.
\]
The original price was 80 dollars.

Tax reverse example: A total after 5% tax is 84 dollars. The total is 105% of the original:
\[
84=1.05x,\qquad x=80.
\]

Case study - paycheck raise: After a 10% raise, a worker earns 22 dollars per hour. The new wage is 110% of the old wage:
\[
22=1.10x,\qquad x=20.
\]
The old wage was 20 dollars per hour.

Common mistake: subtracting 20% from 64 to undo a 20% discount. That gives 51.20, but 64 is already the discounted value. You must divide by the paid percent.

[[check:After 20% off, the sale price is 64 dollars. What was the original price?|80;;$80|After 20% off, 64 is 80% of the original. Solve \(64=0.80x\).]]
            """,
        ),
        (
            "9. Percent Case Studies: Shopping, Grades, Budgeting, and Data",
            r"""
Percent questions become easier when you identify the base: what is the percent being taken **of**?

**Case study 1 - shopping with discount and tax.** A tablet costs 240 dollars. It is 15% off, then 6% sales tax is applied to the sale price.
\[
\text{sale price}=0.85(240)=204.
\]
\[
\text{tax}=0.06(204)=12.24.
\]
\[
\text{final price}=204+12.24=216.24.
\]

**Case study 2 - grades.** A student earns 45 points out of 60:
\[
\frac{45}{60}=0.75=75\%.
\]

**Case study 3 - budgeting.** A 2,400 dollar monthly income has 30% reserved for rent:
\[
0.30(2400)=720.
\]

**Case study 4 - data comparison.** Store A sells 45 of 60 items. Store B sells 72 of 90 items.
\[
\frac{45}{60}=75\%,\qquad \frac{72}{90}=80\%.
\]
Store B has the higher sell-through rate, even though both sold different counts.

Case-study habit: write the base next to every percent. "15% off 240" and "6% tax on 204" use different bases.

[[check:A tablet is 240 dollars and 15% off. What is the sale price before tax?|204|Pay 85% of the original: \(0.85\times240\).]]
            """,
        ),
        (
            "10. GED Percent Strategy: Estimate, Model, Solve, Check",
            r"""
Percent mastery is not just knowing formulas. It is knowing which formula fits the story.

Use this decision map:
- **Find part:** "What is 30% of 150?" Use percent decimal times whole.
- **Find percent:** "18 is what percent of 72?" Use part divided by whole.
- **Find final after increase/decrease:** Use a multiplier like 1.08, 0.75, or 1.20.
- **Find original:** Divide final by the multiplier.
- **Find percent change:** change divided by original.

Estimate first:
- 49% of 202 is about half of 200, so about 100.
- 12% tax on 48 dollars is a little less than 6 dollars.
- A 90 dollar item at 30% off should cost less than 90 but more than 45.

Error analysis example: A student says 20% of 60 is 300 because \(20\times60=1200\) and moved the decimal. The mistake is using 20 instead of 0.20. Correct:
\[
0.20(60)=12.
\]

Final GED check:
- Is the answer a dollar amount, percent, count, or original value?
- Did I use the correct base?
- Does increase make the final bigger and discount make it smaller?
- Did I convert the percent to a decimal before multiplying?

[[check:Estimate: is 49% of 202 closer to 10, 100, or 200?|100|49% is close to 50%, and half of 202 is about 101.]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"Write \(37\%\) as a decimal.",
            "difficulty": 1,
            "choices": [(r"\(0.37\)", True), (r"\(3.7\)", False), (r"\(37.0\)", False), (r"\(0.037\)", False)],
            "explanation": r"Percent to decimal means divide by 100: \(37\%=0.37\).",
        },
        {
            "text": r"Write \(0.08\) as a percent.",
            "difficulty": 1,
            "choices": [(r"\(8\%\)", True), (r"\(0.8\%\)", False), (r"\(80\%\)", False), (r"\(0.08\%\)", False)],
            "explanation": r"Decimal to percent means multiply by 100: \(0.08=8\%\).",
        },
        {
            "text": r"Write \(40\%\) as a simplified fraction.",
            "difficulty": 1,
            "choices": [(r"\(\frac{2}{5}\)", True), (r"\(\frac{4}{100}\)", False), (r"\(\frac{5}{2}\)", False), (r"\(\frac{1}{4}\)", False)],
            "explanation": r"\(40\%=\frac{40}{100}=\frac{2}{5}\).",
        },
        {
            "text": r"Write \(\frac{3}{4}\) as a percent.",
            "difficulty": 1,
            "choices": [(r"\(75\%\)", True), (r"\(34\%\)", False), (r"\(43\%\)", False), (r"\(0.75\%\)", False)],
            "explanation": r"\(\frac{3}{4}=0.75=75\%\).",
        },
        {
            "text": r"What is \(30\%\) of \(150\)?",
            "difficulty": 1,
            "choices": [(r"\(45\)", True), (r"\(30\)", False), (r"\(50\)", False), (r"\(450\)", False)],
            "explanation": r"Convert \(30\%\) to \(0.30\), then multiply: \(0.30(150)=45\).",
        },
        {
            "text": r"What is \(15\%\) of \(80\)?",
            "difficulty": 1,
            "choices": [(r"\(12\)", True), (r"\(15\)", False), (r"\(8\)", False), (r"\(120\)", False)],
            "explanation": r"\(0.15(80)=12\). You can also use 10% of 80 plus 5% of 80: \(8+4=12\).",
        },
        {
            "text": r"What is \(125\%\) of \(40\)?",
            "difficulty": 2,
            "choices": [(r"\(50\)", True), (r"\(45\)", False), (r"\(32\)", False), (r"\(125\)", False)],
            "explanation": r"\(125\%=1.25\). Then \(1.25(40)=50\).",
        },
        {
            "text": r"\(18\) is what percent of \(72\)?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(40\%\)", False), (r"\(54\%\)", False)],
            "explanation": r"Part divided by whole: \(18/72=0.25=25\%\).",
        },
        {
            "text": r"A student answers \(42\) out of \(50\) questions correctly. What percent is correct?",
            "difficulty": 1,
            "choices": [(r"\(84\%\)", True), (r"\(42\%\)", False), (r"\(50\%\)", False), (r"\(92\%\)", False)],
            "explanation": r"\(\frac{42}{50}=0.84=84\%\).",
        },
        {
            "text": r"A family spends \(450\) dollars on rent from an \(1{,}800\) dollar budget. What percent is rent?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(40\%\)", False), (r"\(4\%\)", False)],
            "explanation": r"\(\frac{450}{1800}=0.25=25\%\).",
        },
        {
            "text": r"A \(120\) dollar jacket is \(25\%\) off. What is the sale price?",
            "difficulty": 2,
            "choices": [(r"\(90\) dollars", True), (r"\(95\) dollars", False), (r"\(30\) dollars", False), (r"\(100\) dollars", False)],
            "explanation": r"A 25% discount means you pay 75%. \(0.75(120)=90\).",
        },
        {
            "text": r"An \(80\) dollar item is \(20\%\) off. What is the discount amount?",
            "difficulty": 1,
            "choices": [(r"\(16\) dollars", True), (r"\(64\) dollars", False), (r"\(20\) dollars", False), (r"\(8\) dollars", False)],
            "explanation": r"Discount \(=0.20(80)=16\) dollars.",
        },
        {
            "text": r"An \(80\) dollar item is \(20\%\) off. What is the sale price?",
            "difficulty": 1,
            "choices": [(r"\(64\) dollars", True), (r"\(16\) dollars", False), (r"\(60\) dollars", False), (r"\(100\) dollars", False)],
            "explanation": r"Pay 80% after a 20% discount: \(0.80(80)=64\).",
        },
        {
            "text": r"A \(50\) dollar item has \(6\%\) sales tax. What is the total price?",
            "difficulty": 1,
            "choices": [(r"\(53\) dollars", True), (r"\(56\) dollars", False), (r"\(3\) dollars", False), (r"\(50.60\) dollars", False)],
            "explanation": r"Tax \(=0.06(50)=3\). Total \(=50+3=53\).",
        },
        {
            "text": r"A restaurant bill is \(36\) dollars. A \(20\%\) tip is added. What is the tip?",
            "difficulty": 1,
            "choices": [(r"\(7.20\) dollars", True), (r"\(20\) dollars", False), (r"\(3.60\) dollars", False), (r"\(43.20\) dollars", False)],
            "explanation": r"Tip \(=0.20(36)=7.20\) dollars.",
        },
        {
            "text": r"A salesperson earns \(8\%\) commission on \(2{,}500\) dollars in sales. What is the commission?",
            "difficulty": 2,
            "choices": [(r"\(200\) dollars", True), (r"\(20\) dollars", False), (r"\(250\) dollars", False), (r"\(2{,}000\) dollars", False)],
            "explanation": r"\(0.08(2500)=200\).",
        },
        {
            "text": r"A price rises from \(50\) dollars to \(65\) dollars. What is the percent increase?",
            "difficulty": 2,
            "choices": [(r"\(30\%\)", True), (r"\(15\%\)", False), (r"\(23\%\)", False), (r"\(130\%\)", False)],
            "explanation": r"The change is \(15\). Divide by the original \(50\): \(15/50=0.30=30\%\).",
        },
        {
            "text": r"A price drops from \(80\) dollars to \(60\) dollars. What is the percent decrease?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(33.3\%\)", False), (r"\(75\%\)", False)],
            "explanation": r"The decrease is \(20\). Divide by the original \(80\): \(20/80=0.25=25\%\).",
        },
        {
            "text": r"A town grows from \(2{,}000\) to \(2{,}500\) people. What is the percent increase?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(50\%\)", False), (r"\(500\%\)", False)],
            "explanation": r"Change \(=500\). Original \(=2000\). \(500/2000=0.25=25\%\).",
        },
        {
            "text": r"After \(20\%\) off, the sale price is \(64\) dollars. What was the original price?",
            "difficulty": 3,
            "choices": [(r"\(80\) dollars", True), (r"\(76.80\) dollars", False), (r"\(51.20\) dollars", False), (r"\(84\) dollars", False)],
            "explanation": r"After 20% off, the sale price is 80% of the original. \(64=0.80x\), so \(x=80\).",
        },
        {
            "text": r"After a \(10\%\) raise, a worker earns \(22\) dollars per hour. What was the old wage?",
            "difficulty": 3,
            "choices": [(r"\(20\) dollars per hour", True), (r"\(19.80\) dollars per hour", False), (r"\(24.20\) dollars per hour", False), (r"\(21\) dollars per hour", False)],
            "explanation": r"The new wage is 110% of the old wage. \(22=1.10x\), so \(x=20\).",
        },
        {
            "text": r"A total after \(5\%\) tax is \(84\) dollars. What was the price before tax?",
            "difficulty": 3,
            "choices": [(r"\(80\) dollars", True), (r"\(79.80\) dollars", False), (r"\(88.20\) dollars", False), (r"\(76\) dollars", False)],
            "explanation": r"The total is 105% of the original. \(84=1.05x\), so \(x=80\).",
        },
        {
            "text": r"A tablet costs \(240\) dollars and is \(15\%\) off. What is the sale price before tax?",
            "difficulty": 2,
            "choices": [(r"\(204\) dollars", True), (r"\(225\) dollars", False), (r"\(36\) dollars", False), (r"\(216.24\) dollars", False)],
            "explanation": r"A 15% discount means pay 85%: \(0.85(240)=204\).",
        },
        {
            "text": r"A tablet sale price is \(204\) dollars. Sales tax is \(6\%\). What is the tax amount?",
            "difficulty": 2,
            "choices": [(r"\(12.24\) dollars", True), (r"\(14.40\) dollars", False), (r"\(216.24\) dollars", False), (r"\(10.20\) dollars", False)],
            "explanation": r"Tax \(=0.06(204)=12.24\) dollars.",
        },
        {
            "text": r"Store A sells \(45\) of \(60\) items. Store B sells \(72\) of \(90\) items. Which store has the higher sell-through rate?",
            "difficulty": 3,
            "choices": [("Store B", True), ("Store A", False), ("They are equal", False), ("Cannot be determined", False)],
            "explanation": r"Store A: \(45/60=75\%\). Store B: \(72/90=80\%\). Store B is higher.",
        },
        {
            "text": r"Which multiplier represents a \(12\%\) increase?",
            "difficulty": 2,
            "choices": [(r"\(1.12\)", True), (r"\(0.12\)", False), (r"\(0.88\)", False), (r"\(12\)", False)],
            "explanation": r"A 12% increase means 100% + 12% = 112% = 1.12.",
        },
        {
            "text": r"Which multiplier represents a \(35\%\) decrease?",
            "difficulty": 2,
            "choices": [(r"\(0.65\)", True), (r"\(1.35\)", False), (r"\(0.35\)", False), (r"\(35\)", False)],
            "explanation": r"A 35% decrease means pay or keep 65%, and \(65\%=0.65\).",
        },
        {
            "text": r"Estimate \(49\%\) of \(202\). Which is closest?",
            "difficulty": 1,
            "choices": [(r"\(100\)", True), (r"\(10\)", False), (r"\(200\)", False), (r"\(300\)", False)],
            "explanation": r"49% is close to 50%, and half of 202 is about 101, so 100 is closest.",
        },
        {
            "text": r"A student says \(20\%\) of \(60\) is \(300\). What is the likely mistake?",
            "difficulty": 2,
            "choices": [("They used 20 instead of 0.20.", True), ("They divided by 100 twice.", False), ("They used the wrong original value.", False), ("They found percent change.", False)],
            "explanation": r"To find 20% of 60, use \(0.20(60)=12\), not \(20(60)\).",
        },
        {
            "text": r"What is \(2.5\%\) as a decimal?",
            "difficulty": 2,
            "choices": [(r"\(0.025\)", True), (r"\(0.25\)", False), (r"\(2.5\)", False), (r"\(25\)", False)],
            "explanation": r"Divide by 100: \(2.5\%=0.025\).",
        },
        {
            "text": r"What is \(0.125\) as a percent?",
            "difficulty": 2,
            "choices": [(r"\(12.5\%\)", True), (r"\(1.25\%\)", False), (r"\(125\%\)", False), (r"\(0.125\%\)", False)],
            "explanation": r"Multiply by 100: \(0.125=12.5\%\).",
        },
        {
            "text": r"A 90 dollar item is 30% off. What is the sale price?",
            "difficulty": 1,
            "choices": [(r"\(63\) dollars", True), (r"\(27\) dollars", False), (r"\(60\) dollars", False), (r"\(120\) dollars", False)],
            "explanation": r"Pay 70% after a 30% discount: \(0.70(90)=63\).",
        },
        {
            "text": r"A worker earns 15% more than a 400 dollar weekly base bonus. What is the increased amount?",
            "difficulty": 2,
            "choices": [(r"\(460\) dollars", True), (r"\(415\) dollars", False), (r"\(60\) dollars", False), (r"\(340\) dollars", False)],
            "explanation": r"A 15% increase means multiply by 1.15: \(1.15(400)=460\).",
        },
    ],
    "essays": [
        {
            "text": (
                r"A tablet costs \(240\) dollars. It is discounted by \(15\%\), then \(6\%\) sales tax is applied "
                r"to the discounted price. Find the final price and explain why the tax is based on the discounted price."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: computes sale price \(0.85(240)=204\), tax \(0.06(204)=12.24\), final price "
                r"\(216.24\), and explains that tax is applied after the discount because the discounted price is the actual price paid."
            ),
        },
        {
            "text": (
                r"A student got \(42\) out of \(50\) questions correct on one practice test and \(36\) out of \(40\) "
                r"on another. Find both percentages and explain which score is higher."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: \(42/50=0.84=84\%\), \(36/40=0.90=90\%\), and states the second score is higher. "
                "Deduct for comparing only the raw correct counts."
            ),
        },
        {
            "text": (
                r"A jacket's price drops from \(120\) dollars to \(90\) dollars. Find the percent decrease. "
                r"Show the change, the original value, and the final percent."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: change \(=120-90=30\), original \(=120\), \(30/120=0.25=25\%\) decrease. "
                "Deduct for dividing by the new price instead of the original."
            ),
        },
        {
            "text": (
                r"After a \(20\%\) discount, a bike costs \(160\) dollars. Find the original price. "
                r"Explain why subtracting \(20\%\) from \(160\) does not correctly undo the discount."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: recognizes \(160\) is \(80\%\) of the original, solves \(160=0.80x\), gets "
                r"\(x=200\), and explains that the discount was based on the original price, not on 160."
            ),
        },
        {
            "text": (
                r"A monthly income is \(2{,}400\) dollars. Rent should be \(30\%\), food \(15\%\), and savings \(10\%\). "
                r"Find each dollar amount and the total assigned to these three categories."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: rent \(0.30(2400)=720\), food \(0.15(2400)=360\), savings \(0.10(2400)=240\), "
                r"total \(1320\). Deduct for using different bases."
            ),
        },
        {
            "text": (
                r"Correct this mistake: A student says \(18\) is \(400\%\) of \(72\) because \(72\div18=4\). "
                r"Explain the error and solve correctly."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: identifies that the student divided whole by part, uses \(18/72=0.25=25\%\), "
                r"and explains that '18 is what percent of 72' means part divided by whole."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the dedicated GED Basic Math percents mastery course."

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

        # Phase 1 is MCQ-only: written-response prompts are not seeded.

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
