"""
Seed a dedicated GED Basic Math fractions mastery course.

Run:
    python manage.py seed_ged_basic_math_fractions
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Basic Math: Fractions Mastery",
    "slug": "ged-basic-math-fractions-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep Basic Math course focused only on fractions. Students learn what "
        "fractions mean, how to simplify, compare, add, subtract, multiply, divide, "
        "use mixed numbers, and solve real GED-style case studies involving recipes, "
        "shopping, measurement, schedules, and data."
    ),
    "lessons": [
        (
            "1. What a Fraction Means: Equal Parts, Numerator, Denominator",
            r"""
A fraction names part of a whole. The most important word is **equal**: the whole must be cut into equal-size pieces.

In \(\frac{3}{8}\):
- The **denominator** \(8\) tells how many equal parts make one whole.
- The **numerator** \(3\) tells how many of those parts we are using.

[[figure:fraction_circle|Three of eight equal parts are shaded, so the amount is \(\frac{3}{8}\).]]

Think in three pictures:
- **Area model:** 3 of 8 equal pizza slices.
- **Set model:** 3 of 8 students wearing blue shirts.
- **Number line model:** a point three steps out of eight from 0 to 1.

Worked example: A pan of cornbread is cut into 12 equal pieces. A family eats 5 pieces. The fraction eaten is \(\frac{5}{12}\). The fraction left is \(\frac{7}{12}\), because \(12-5=7\).

Common mistake: writing the bigger number on bottom automatically. The denominator is not "the bigger number"; it is the number of equal parts in the whole.

Case study - cafeteria tray: A tray has 10 equal brownie squares. If 4 are sold before lunch, the sold amount is \(\frac{4}{10}\). The unsold amount is \(\frac{6}{10}\). Both fractions describe the same tray, just different parts of it.

[[check:A garden is split into 9 equal plots. If 2 plots have tomatoes, what fraction has tomatoes?|2/9|The denominator is all equal plots. The numerator is tomato plots.]]
            """,
        ),
        (
            "2. Equivalent Fractions and Simplifying",
            r"""
Equivalent fractions are different names for the same amount. If a rectangle is half shaded, it can be labeled \(\frac{1}{2}\), \(\frac{2}{4}\), or \(\frac{4}{8}\). The amount did not change; only the number of cuts changed.

[[figure:equivalent_fraction_strips|The shaded amount is the same in all three strips.]]

To make an equivalent fraction, multiply or divide the numerator and denominator by the same number:
\[
\frac{3}{5}=\frac{3\cdot 2}{5\cdot 2}=\frac{6}{10}.
\]

To simplify, divide top and bottom by their greatest common factor. Example:
\[
\frac{18}{24}=\frac{18\div 6}{24\div 6}=\frac{3}{4}.
\]

Why this works: multiplying or dividing by \(\frac{2}{2}\), \(\frac{3}{3}\), or \(\frac{6}{6}\) is the same as multiplying by 1, so the value stays the same.

Case study - sale sign: A store says 6 out of 8 shelves are full. \(\frac{6}{8}\) simplifies to \(\frac{3}{4}\), so the shelves are three-fourths full. That is easier to understand than 6 eighths.

Common mistake: reducing only the numerator. \(\frac{18}{24}\) cannot become \(\frac{3}{24}\). Whatever divides the top must also divide the bottom.

[[check:Simplify \(\frac{18}{24}\).|3/4|The greatest common factor of 18 and 24 is 6. Divide both by 6.]]
            """,
        ),
        (
            "3. Comparing and Ordering Fractions",
            r"""
To compare fractions, ask: are the pieces the same size? If denominators match, compare numerators:
\[
\frac{5}{9}>\frac{2}{9}.
\]
Five ninths is more pieces than two ninths.

If denominators are different, use one of three strategies.

**Strategy 1 - Common denominator.** Compare \(\frac{3}{4}\) and \(\frac{5}{6}\). The common denominator is 12:
\[
\frac{3}{4}=\frac{9}{12},\qquad \frac{5}{6}=\frac{10}{12}.
\]
So \(\frac{5}{6}\) is larger.

**Strategy 2 - Benchmark.** Compare each fraction to \(\frac{1}{2}\). \(\frac{4}{9}\) is less than half because half of 9 is 4.5. \(\frac{5}{9}\) is more than half.

**Strategy 3 - Decimal check.** Divide numerator by denominator when the numbers are friendly. \(\frac{3}{4}=0.75\), and \(\frac{2}{3}\approx0.67\), so \(\frac{3}{4}\) is larger.

Case study - test progress: One student completed \(\frac{5}{8}\) of a GED practice set. Another completed \(\frac{2}{3}\). Since \(\frac{5}{8}=0.625\) and \(\frac{2}{3}\approx0.667\), the second student completed more.

Common mistake: thinking a larger denominator means a larger fraction. If the numerator is 1, then \(\frac{1}{8}\) is smaller than \(\frac{1}{4}\), because eighths are smaller pieces.

[[check:Which is larger, \(\frac{5}{8}\) or \(\frac{2}{3}\)?|2/3|Use decimals or common denominator 24: \(15/24\) vs \(16/24\).]]
            """,
        ),
        (
            "4. Improper Fractions and Mixed Numbers",
            r"""
A **proper fraction** is less than 1, like \(\frac{3}{5}\). An **improper fraction** is 1 or more, like \(\frac{9}{4}\). A **mixed number** combines a whole number and a fraction, like \(2\frac{1}{4}\).

Improper fraction to mixed number:
\[
\frac{17}{5}=17\div 5=3\text{ remainder }2=3\frac{2}{5}.
\]

Mixed number to improper fraction:
\[
3\frac{2}{5}=\frac{3\cdot 5+2}{5}=\frac{17}{5}.
\]

Why the formula works: \(3\frac{2}{5}\) means 3 wholes plus \(\frac{2}{5}\). Three wholes equal \(\frac{15}{5}\). Add \(\frac{2}{5}\) to get \(\frac{17}{5}\).

Case study - measuring boards: A board is \(2\frac{3}{4}\) feet long. For multiplication, convert it to an improper fraction:
\[
2\frac{3}{4}=\frac{11}{4}.
\]
Now it is easier to calculate if you need several boards.

Common mistake: multiplying the whole number by the numerator instead of the denominator. In \(2\frac{3}{4}\), use \(2\cdot4+3=11\), not \(2\cdot3+4\).

[[check:Convert \(3\frac{2}{5}\) to an improper fraction.|17/5|Multiply the whole number by the denominator, then add the numerator.]]
            """,
        ),
        (
            "5. Adding and Subtracting Fractions",
            r"""
Addition and subtraction require same-size pieces. This is the one rule that explains almost everything.

Same denominator:
\[
\frac{2}{7}+\frac{3}{7}=\frac{5}{7}.
\]
The denominator stays 7 because the piece size did not change.

Different denominators:
\[
\frac{1}{2}+\frac{1}{3}.
\]
Halves and thirds are different sizes, so rewrite both as sixths:
\[
\frac{1}{2}=\frac{3}{6},\qquad \frac{1}{3}=\frac{2}{6},\qquad \frac{3}{6}+\frac{2}{6}=\frac{5}{6}.
\]

[[figure:common_denominator_bars|Before adding, rewrite the fractions with a common denominator.]]

Subtraction example:
\[
\frac{5}{6}-\frac{1}{4}=\frac{10}{12}-\frac{3}{12}=\frac{7}{12}.
\]

Case study - recipe: A recipe uses \(\frac{1}{2}\) cup of oats and \(\frac{1}{3}\) cup of nuts. Total dry mix is \(\frac{5}{6}\) cup. If the bowl holds 1 cup, there is \(\frac{1}{6}\) cup of space left.

Common mistake: adding denominators. \(\frac{1}{2}+\frac{1}{3}\) is not \(\frac{2}{5}\). You do not add piece sizes; you rename the pieces first.

[[check:Compute \(\frac{1}{2}+\frac{1}{3}\).|5/6|Use sixths: \(1/2=3/6\), and \(1/3=2/6\).]]
            """,
        ),
        (
            "6. Borrowing With Mixed Numbers",
            r"""
Mixed-number subtraction can require borrowing, just like whole-number subtraction.

Example:
\[
4\frac{1}{3}-1\frac{5}{6}.
\]
First use a common denominator:
\[
4\frac{2}{6}-1\frac{5}{6}.
\]
You cannot subtract \(5/6\) from \(2/6\), so borrow 1 whole from 4. One whole is \(6/6\):
\[
4\frac{2}{6}=3\frac{8}{6}.
\]
Now subtract:
\[
3\frac{8}{6}-1\frac{5}{6}=2\frac{3}{6}=2\frac{1}{2}.
\]

Alternative method: convert both mixed numbers to improper fractions.
\[
4\frac{1}{3}=\frac{13}{3}=\frac{26}{6},\qquad 1\frac{5}{6}=\frac{11}{6}.
\]
Then
\[
\frac{26}{6}-\frac{11}{6}=\frac{15}{6}=2\frac{1}{2}.
\]

Case study - construction: A worker has \(4\frac{1}{3}\) feet of trim and uses \(1\frac{5}{6}\) feet. The remaining trim is \(2\frac{1}{2}\) feet.

Common mistake: borrowing 1 as \(1/6\). When the denominator is 6, one whole is \(6/6\), not \(1/6\).

[[check:Compute \(4\frac{1}{3}-1\frac{5}{6}\).|2 1/2;;2.5;;5/2|Use sixths and borrow: \(4\frac{2}{6}=3\frac{8}{6}\).]]
            """,
        ),
        (
            "7. Multiplying Fractions and Scaling",
            r"""
Multiplication answers "of" questions. One half of one third means:
\[
\frac{1}{2}\times\frac{1}{3}=\frac{1}{6}.
\]

Multiply straight across:
\[
\frac{3}{4}\times\frac{2}{5}=\frac{6}{20}=\frac{3}{10}.
\]

You can simplify before multiplying:
\[
\frac{3}{8}\times\frac{4}{9}.
\]
Cancel 4 with 8 to get 1 and 2; cancel 3 with 9 to get 1 and 3. The product is
\[
\frac{1}{2}\times\frac{1}{3}=\frac{1}{6}.
\]

Mixed number multiplication:
\[
2\frac{1}{2}\times\frac{3}{4}=\frac{5}{2}\times\frac{3}{4}=\frac{15}{8}=1\frac{7}{8}.
\]

Case study - recipe scaling: A full recipe needs \(\frac{3}{4}\) cup of sugar. Half a recipe needs \(\frac{1}{2}\) of that:
\[
\frac{1}{2}\times\frac{3}{4}=\frac{3}{8}.
\]

Common mistake: thinking multiplication always makes numbers bigger. Multiplying by a fraction less than 1 makes the amount smaller.

[[check:What is half of \(\frac{3}{4}\)?|3/8|Half of means multiply by \(1/2\).]]
            """,
        ),
        (
            "8. Dividing Fractions: How Many Groups?",
            r"""
Division asks how many groups fit. If you have \(\frac{3}{4}\) cup of rice and each serving uses \(\frac{1}{8}\) cup, then:
\[
\frac{3}{4}\div\frac{1}{8}.
\]
Rewrite \(\frac{3}{4}\) as \(\frac{6}{8}\). Six eighth-cup servings fit, so the answer is 6.

The shortcut is **keep, change, flip**:
\[
\frac{3}{4}\div\frac{1}{8}=\frac{3}{4}\times\frac{8}{1}=6.
\]

Another example:
\[
\frac{2}{3}\div\frac{4}{5}=\frac{2}{3}\times\frac{5}{4}=\frac{10}{12}=\frac{5}{6}.
\]

Why flipping works: division by \(\frac{4}{5}\) asks how many \(\frac{4}{5}\)-size groups fit. Multiplying by \(\frac{5}{4}\), the reciprocal, scales the first amount into that group size.

Case study - fabric: A ribbon is \(5\frac{1}{2}\) yards long. Each bow needs \(\frac{3}{4}\) yard. Number of bows:
\[
5\frac{1}{2}\div\frac{3}{4}=\frac{11}{2}\times\frac{4}{3}=\frac{44}{6}=7\frac{1}{3}.
\]
You can make 7 full bows, with ribbon left over.

Common mistake: flipping the first fraction. Keep the first fraction, change divide to multiply, flip the second fraction only.

[[check:Compute \(\frac{3}{4}\div\frac{1}{8}\).|6|Ask how many eighths are in three fourths, or keep-change-flip.]]
            """,
        ),
        (
            "9. Fraction Case Studies: Recipes, Shopping, Schedules, and Measurement",
            r"""
Fractions become real when they measure things.

**Case study 1 - recipe scaling.** A recipe uses \(\frac{2}{3}\) cup of milk for one batch. You need \(2\frac{1}{2}\) batches:
\[
\frac{2}{3}\times 2\frac{1}{2}=\frac{2}{3}\times\frac{5}{2}=\frac{10}{6}=\frac{5}{3}=1\frac{2}{3}.
\]
You need \(1\frac{2}{3}\) cups of milk.

**Case study 2 - shopping discount.** A jacket is \(\frac{1}{4}\) off. That means you pay \(\frac{3}{4}\) of the price. If the original price is 80 dollars:
\[
\frac{3}{4}\times 80=60.
\]

**Case study 3 - schedule.** A student studies \(\frac{3}{5}\) hour on Monday and \(\frac{7}{10}\) hour on Tuesday:
\[
\frac{3}{5}+\frac{7}{10}=\frac{6}{10}+\frac{7}{10}=\frac{13}{10}=1\frac{3}{10}.
\]
Total study time is \(1\frac{3}{10}\) hours.

**Case study 4 - measurement.** A shelf is \(6\frac{1}{4}\) feet long. Each section is \(1\frac{1}{4}\) feet:
\[
6\frac{1}{4}\div1\frac{1}{4}=\frac{25}{4}\div\frac{5}{4}=\frac{25}{4}\times\frac{4}{5}=5.
\]
The shelf has 5 sections.

[[figure:fraction_operation_map|Choose the operation from the story before doing arithmetic.]]

[[check:A recipe uses \(\frac{2}{3}\) cup for one batch. How much is needed for \(2\frac{1}{2}\) batches?|1 2/3;;5/3|Multiply \(\frac{2}{3}\) by \(\frac{5}{2}\).]]
            """,
        ),
        (
            "10. GED Fraction Strategy: Diagnose, Solve, Check",
            r"""
A student fully understands fractions when they can explain **why** the method works, not only get the answer.

Use this diagnostic checklist:
- Is this a part of one whole, several wholes, or a comparison?
- Are the pieces equal size?
- Do I need a common denominator?
- Does the phrase "of" mean multiplication?
- Does division mean "how many groups fit?"
- Should the final answer be less than 1, equal to 1, or more than 1?

Before solving, estimate. Example:
\[
\frac{7}{8}+\frac{1}{5}
\]
is a little more than 1 because \(\frac{7}{8}\) is close to 1 and \(\frac{1}{5}\) adds a small amount. Exact work:
\[
\frac{7}{8}+\frac{1}{5}=\frac{35}{40}+\frac{8}{40}=\frac{43}{40}=1\frac{3}{40}.
\]
The exact answer matches the estimate.

Error analysis example: A student says
\[
\frac{1}{2}+\frac{1}{3}=\frac{2}{5}.
\]
The mistake is adding denominators. Correct solution:
\[
\frac{1}{2}=\frac{3}{6},\quad \frac{1}{3}=\frac{2}{6},\quad \frac{3}{6}+\frac{2}{6}=\frac{5}{6}.
\]

Final mastery habit: after every missed fraction problem, write one sentence: "The clue was ___, so the operation should have been ___." That builds transfer to GED word problems.

[[check:Estimate first: is \(\frac{7}{8}+\frac{1}{5}\) less than 1 or greater than 1?|greater than 1;;greater;;more than 1|Seven eighths is close to 1, and one fifth adds more.]]
            """,
        ),
        (
            "11. Fraction Shortcuts & Test-Taking Tips",
            r"""
**Benchmark fractions.** Know these key reference points by heart:
- \(\frac{1}{2}=0.5\)
- \(\frac{1}{3}\approx0.33\)
- \(\frac{2}{3}\approx0.67\)
- \(\frac{1}{4}=0.25\)
- \(\frac{3}{4}=0.75\)
- \(\frac{1}{5}=0.2\)
- \(\frac{2}{5}=0.4\)
- \(\frac{4}{5}=0.8\)

Use these to estimate answers instantly: \(\frac{7}{8}+\frac{2}{3}\) is roughly \(0.875+0.67\approx1.5\), so eliminate any answer less than 1 or greater than 2.

**Quick GCD finder.** For small numbers, factorize mentally:
- Does it divide by 2? (both even)
- Does it divide by 3? (sum of digits divisible by 3)
- Does it divide by 5? (ends in 0 or 5)

Example: \(\frac{15}{35}\). Both are odd, so not 2. \(1+5=6\) and \(3+5=8\); only 15 divides by 3. Both divide by 5: \(\frac{15}{35}=\frac{3}{7}\).

**Multiplication shortcut — cancel before multiplying.** In \(\frac{8}{15}\times\frac{9}{16}\), spot that 8 and 16 share a factor of 8, and 9 and 15 share a factor of 3:
\[
\frac{8}{15}\times\frac{9}{16}=\frac{\cancel{8}^{1}}{{\cancel{15}^{5}}}\times\frac{\cancel{9}^{3}}{\cancel{16}^{2}}=\frac{3}{10}.
\]
Canceling first avoids huge products and reduces errors.

**On timed tests:** if you cannot get an exact answer, estimate and pick the closest option. A reasonable approximation scores better than a wrong calculation.

**Sanity-check your answer.** After any operation, ask: is the result reasonable?
- Adding two proper fractions (both less than 1) should give less than 2.
- Multiplying two proper fractions should give less than either one.
- Dividing by a fraction less than 1 should give a bigger answer.

[[check:What is a good estimate for \(\frac{8}{9}\times\frac{5}{11}\)?|between 0 and 1;;less than 1;;around 0.4|Both fractions are less than 1, so the product is less than either one.]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"A cake is cut into \(8\) equal slices. A student eats \(3\) slices. What fraction of the cake was eaten?",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{8}\)", True), (r"\(\frac{8}{3}\)", False), (r"\(\frac{5}{8}\)", False), (r"\(\frac{3}{5}\)", False)],
            "explanation": r"The denominator is the total equal slices, 8. The numerator is the eaten slices, 3. The fraction is \(\frac{3}{8}\).",
        },
        {
            "text": r"A pan has \(12\) equal pieces. If \(5\) pieces are gone, what fraction is left?",
            "difficulty": 1,
            "choices": [(r"\(\frac{7}{12}\)", True), (r"\(\frac{5}{12}\)", False), (r"\(\frac{12}{7}\)", False), (r"\(\frac{7}{5}\)", False)],
            "explanation": r"There are \(12-5=7\) pieces left, out of 12 total equal pieces. The fraction left is \(\frac{7}{12}\).",
        },
        {
            "text": r"Which fraction is equivalent to \(\frac{2}{3}\)?",
            "difficulty": 1,
            "choices": [(r"\(\frac{8}{12}\)", True), (r"\(\frac{4}{9}\)", False), (r"\(\frac{6}{8}\)", False), (r"\(\frac{3}{2}\)", False)],
            "explanation": r"Multiply numerator and denominator by 4: \(\frac{2}{3}=\frac{8}{12}\).",
        },
        {
            "text": r"Simplify \(\frac{16}{20}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{4}{5}\)", True), (r"\(\frac{8}{10}\)", False), (r"\(\frac{5}{4}\)", False), (r"\(\frac{3}{5}\)", False)],
            "explanation": r"The greatest common factor of 16 and 20 is 4. Divide both by 4: \(\frac{16}{20}=\frac{4}{5}\).",
        },
        {
            "text": r"Simplify \(\frac{21}{28}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{4}\)", True), (r"\(\frac{7}{9}\)", False), (r"\(\frac{4}{3}\)", False), (r"\(\frac{1}{7}\)", False)],
            "explanation": r"Divide top and bottom by 7: \(\frac{21}{28}=\frac{3}{4}\).",
        },
        {
            "text": r"Which is larger: \(\frac{3}{5}\) or \(\frac{5}{8}\)?",
            "difficulty": 2,
            "choices": [(r"\(\frac{5}{8}\)", True), (r"\(\frac{3}{5}\)", False), ("They are equal", False), ("Cannot be determined", False)],
            "explanation": r"Use denominator 40: \(\frac{3}{5}=\frac{24}{40}\) and \(\frac{5}{8}=\frac{25}{40}\). So \(\frac{5}{8}\) is larger.",
        },
        {
            "text": r"Order from least to greatest: \(\frac{1}{2},\frac{3}{4},\frac{2}{3}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{2},\frac{2}{3},\frac{3}{4}\)", True), (r"\(\frac{3}{4},\frac{2}{3},\frac{1}{2}\)", False), (r"\(\frac{2}{3},\frac{1}{2},\frac{3}{4}\)", False), (r"\(\frac{1}{2},\frac{3}{4},\frac{2}{3}\)", False)],
            "explanation": r"Compare decimals or use twelfths: \(\frac{1}{2}=\frac{6}{12}\), \(\frac{2}{3}=\frac{8}{12}\), \(\frac{3}{4}=\frac{9}{12}\).",
        },
        {
            "text": r"Convert \(\frac{17}{5}\) to a mixed number.",
            "difficulty": 1,
            "choices": [(r"\(3\frac{2}{5}\)", True), (r"\(2\frac{3}{5}\)", False), (r"\(3\frac{1}{5}\)", False), (r"\(4\frac{2}{5}\)", False)],
            "explanation": r"\(17\div5=3\) remainder 2, so \(\frac{17}{5}=3\frac{2}{5}\).",
        },
        {
            "text": r"Convert \(4\frac{1}{3}\) to an improper fraction.",
            "difficulty": 1,
            "choices": [(r"\(\frac{13}{3}\)", True), (r"\(\frac{5}{3}\)", False), (r"\(\frac{12}{3}\)", False), (r"\(\frac{4}{3}\)", False)],
            "explanation": r"Multiply \(4\cdot3=12\), then add 1. The result is \(\frac{13}{3}\).",
        },
        {
            "text": r"Compute \(\frac{2}{9}+\frac{4}{9}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{2}{3}\)", True), (r"\(\frac{6}{18}\)", False), (r"\(\frac{6}{9}\)", False), (r"\(\frac{4}{9}\)", False)],
            "explanation": r"Same denominator: add numerators to get \(\frac{6}{9}\), then simplify to \(\frac{2}{3}\).",
        },
        {
            "text": r"Compute \(\frac{1}{4}+\frac{1}{6}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{5}{12}\)", True), (r"\(\frac{2}{10}\)", False), (r"\(\frac{1}{24}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"Use denominator 12: \(\frac{1}{4}=\frac{3}{12}\), \(\frac{1}{6}=\frac{2}{12}\), total \(\frac{5}{12}\).",
        },
        {
            "text": r"Compute \(\frac{5}{6}-\frac{1}{4}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{7}{12}\)", True), (r"\(\frac{4}{2}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(\frac{4}{6}\)", False)],
            "explanation": r"Use denominator 12: \(\frac{5}{6}=\frac{10}{12}\), \(\frac{1}{4}=\frac{3}{12}\). Difference is \(\frac{7}{12}\).",
        },
        {
            "text": r"A recipe uses \(\frac{2}{3}\) cup oats and \(\frac{1}{2}\) cup nuts. How much is that total?",
            "difficulty": 2,
            "choices": [(r"\(1\frac{1}{6}\) cups", True), (r"\(\frac{3}{5}\) cup", False), (r"\(\frac{2}{6}\) cup", False), (r"\(1\frac{2}{3}\) cups", False)],
            "explanation": r"\(\frac{2}{3}+\frac{1}{2}=\frac{4}{6}+\frac{3}{6}=\frac{7}{6}=1\frac{1}{6}\).",
        },
        {
            "text": r"Compute \(3\frac{1}{2}+2\frac{2}{3}\).",
            "difficulty": 2,
            "choices": [(r"\(6\frac{1}{6}\)", True), (r"\(5\frac{3}{5}\)", False), (r"\(6\frac{3}{5}\)", False), (r"\(5\frac{1}{6}\)", False)],
            "explanation": r"Add wholes \(3+2=5\). Add fractions \(\frac{1}{2}+\frac{2}{3}=\frac{3}{6}+\frac{4}{6}=\frac{7}{6}=1\frac{1}{6}\). Total \(6\frac{1}{6}\).",
        },
        {
            "text": r"Compute \(4\frac{1}{3}-1\frac{5}{6}\).",
            "difficulty": 3,
            "choices": [(r"\(2\frac{1}{2}\)", True), (r"\(3\frac{1}{2}\)", False), (r"\(2\frac{2}{3}\)", False), (r"\(1\frac{1}{2}\)", False)],
            "explanation": r"Convert to sixths and borrow: \(4\frac{2}{6}=3\frac{8}{6}\). Then \(3\frac{8}{6}-1\frac{5}{6}=2\frac{3}{6}=2\frac{1}{2}\).",
        },
        {
            "text": r"Compute \(\frac{3}{4}\times\frac{2}{5}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{10}\)", True), (r"\(\frac{5}{9}\)", False), (r"\(\frac{6}{9}\)", False), (r"\(\frac{1}{5}\)", False)],
            "explanation": r"Multiply straight across: \(\frac{3\cdot2}{4\cdot5}=\frac{6}{20}=\frac{3}{10}\).",
        },
        {
            "text": r"What is \(\frac{1}{2}\) of \(\frac{3}{4}\)?",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{8}\)", True), (r"\(\frac{4}{6}\)", False), (r"\(\frac{1}{4}\)", False), (r"\(\frac{3}{2}\)", False)],
            "explanation": r"'Of' means multiply: \(\frac{1}{2}\times\frac{3}{4}=\frac{3}{8}\).",
        },
        {
            "text": r"Compute \(2\frac{1}{2}\times\frac{3}{4}\).",
            "difficulty": 2,
            "choices": [(r"\(1\frac{7}{8}\)", True), (r"\(2\frac{3}{8}\)", False), (r"\(\frac{5}{8}\)", False), (r"\(3\frac{1}{4}\)", False)],
            "explanation": r"Convert \(2\frac{1}{2}\) to \(\frac{5}{2}\). Then \(\frac{5}{2}\times\frac{3}{4}=\frac{15}{8}=1\frac{7}{8}\).",
        },
        {
            "text": r"A full recipe needs \(\frac{3}{4}\) cup sugar. How much sugar is needed for half the recipe?",
            "difficulty": 2,
            "choices": [(r"\(\frac{3}{8}\) cup", True), (r"\(\frac{1}{4}\) cup", False), (r"\(\frac{3}{2}\) cups", False), (r"\(\frac{4}{3}\) cup", False)],
            "explanation": r"Half of \(\frac{3}{4}\) is \(\frac{1}{2}\times\frac{3}{4}=\frac{3}{8}\).",
        },
        {
            "text": r"Compute \(\frac{3}{4}\div\frac{1}{8}\).",
            "difficulty": 2,
            "choices": [(r"\(6\)", True), (r"\(\frac{3}{32}\)", False), (r"\(\frac{1}{6}\)", False), (r"\(8\)", False)],
            "explanation": r"Keep, change, flip: \(\frac{3}{4}\times\frac{8}{1}=6\).",
        },
        {
            "text": r"Compute \(\frac{2}{3}\div\frac{4}{5}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{5}{6}\)", True), (r"\(\frac{8}{15}\)", False), (r"\(\frac{6}{5}\)", False), (r"\(\frac{3}{10}\)", False)],
            "explanation": r"\(\frac{2}{3}\div\frac{4}{5}=\frac{2}{3}\times\frac{5}{4}=\frac{10}{12}=\frac{5}{6}\).",
        },
        {
            "text": r"A ribbon is \(5\frac{1}{2}\) yards long. Each bow uses \(\frac{3}{4}\) yard. How many full bows can be made?",
            "difficulty": 3,
            "choices": [("7 full bows", True), ("8 full bows", False), ("6 full bows", False), ("5 full bows", False)],
            "explanation": r"\(5\frac{1}{2}\div\frac{3}{4}=\frac{11}{2}\times\frac{4}{3}=\frac{44}{6}=7\frac{1}{3}\). Only 7 full bows can be made.",
        },
        {
            "text": r"A jacket is \(\frac{1}{4}\) off. What fraction of the price do you pay?",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{4}\)", True), (r"\(\frac{1}{4}\)", False), (r"\(\frac{4}{3}\)", False), (r"\(\frac{2}{4}\)", False)],
            "explanation": r"If \(\frac{1}{4}\) is taken off, the remaining part is \(1-\frac{1}{4}=\frac{3}{4}\).",
        },
        {
            "text": r"A student studies \(\frac{3}{5}\) hour Monday and \(\frac{7}{10}\) hour Tuesday. What is the total?",
            "difficulty": 2,
            "choices": [(r"\(1\frac{3}{10}\) hours", True), (r"\(\frac{10}{15}\) hour", False), (r"\(1\frac{1}{5}\) hours", False), (r"\(\frac{4}{10}\) hour", False)],
            "explanation": r"\(\frac{3}{5}=\frac{6}{10}\). Then \(\frac{6}{10}+\frac{7}{10}=\frac{13}{10}=1\frac{3}{10}\).",
        },
        {
            "text": r"A shelf is \(6\frac{1}{4}\) feet long. Each section is \(1\frac{1}{4}\) feet. How many sections fit?",
            "difficulty": 3,
            "choices": [(r"\(5\)", True), (r"\(4\)", False), (r"\(6\)", False), (r"\(7\)", False)],
            "explanation": r"\(6\frac{1}{4}\div1\frac{1}{4}=\frac{25}{4}\div\frac{5}{4}=\frac{25}{4}\times\frac{4}{5}=5\).",
        },
        {
            "text": r"Which operation is suggested by the phrase '\(\frac{2}{3}\) of a batch'?",
            "difficulty": 1,
            "choices": [("Multiplication", True), ("Subtraction", False), ("Division only", False), ("Addition only", False)],
            "explanation": r"In fraction word problems, 'of' usually means multiplication.",
        },
        {
            "text": r"Which answer is reasonable for \(\frac{7}{8}+\frac{1}{5}\)?",
            "difficulty": 2,
            "choices": [("A little more than 1", True), ("Less than 1/2", False), ("Exactly 2", False), ("Less than 0", False)],
            "explanation": r"\(\frac{7}{8}\) is close to 1, and adding \(\frac{1}{5}\) makes it greater than 1 but far less than 2.",
        },
        {
            "text": r"Compute \(\frac{7}{8}+\frac{1}{5}\).",
            "difficulty": 3,
            "choices": [(r"\(1\frac{3}{40}\)", True), (r"\(\frac{8}{13}\)", False), (r"\(\frac{12}{40}\)", False), (r"\(1\frac{1}{13}\)", False)],
            "explanation": r"Use denominator 40: \(\frac{7}{8}=\frac{35}{40}\), \(\frac{1}{5}=\frac{8}{40}\), total \(\frac{43}{40}=1\frac{3}{40}\).",
        },
        {
            "text": r"A student solves \(\frac{1}{2}+\frac{1}{3}\) as \(\frac{2}{5}\). What mistake did they make?",
            "difficulty": 2,
            "choices": [("They added the denominators instead of using a common denominator.", True), ("They multiplied straight across.", False), ("They simplified too early.", False), ("They converted to a mixed number.", False)],
            "explanation": r"For addition, denominators must match. The correct work is \(\frac{3}{6}+\frac{2}{6}=\frac{5}{6}\).",
        },
        {
            "text": r"What is the reciprocal of \(\frac{5}{7}\)?",
            "difficulty": 1,
            "choices": [(r"\(\frac{7}{5}\)", True), (r"\(\frac{5}{7}\)", False), (r"\(\frac{1}{7}\)", False), (r"\(\frac{1}{5}\)", False)],
            "explanation": r"The reciprocal flips numerator and denominator: \(\frac{5}{7}\) becomes \(\frac{7}{5}\).",
        },
        {
            "text": r"Compute \(\frac{4}{9}\times\frac{3}{8}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{6}\)", True), (r"\(\frac{12}{72}\)", False), (r"\(\frac{7}{17}\)", False), (r"\(\frac{3}{2}\)", False)],
            "explanation": r"\(\frac{4}{9}\times\frac{3}{8}=\frac{12}{72}=\frac{1}{6}\).",
        },
        {
            "text": r"A class completed \(\frac{5}{6}\) of a project. What fraction remains?",
            "difficulty": 1,
            "choices": [(r"\(\frac{1}{6}\)", True), (r"\(\frac{5}{6}\)", False), (r"\(\frac{6}{5}\)", False), (r"\(\frac{4}{6}\)", False)],
            "explanation": r"One whole is \(\frac{6}{6}\). Remaining \(=\frac{6}{6}-\frac{5}{6}=\frac{1}{6}\).",
        },
        {
            "text": r"Compute \(\frac{5}{8}+\frac{1}{2}-\frac{1}{4}\).",
            "difficulty": 3,
            "choices": [(r"\(\frac{7}{8}\)", True), (r"\(\frac{5}{8}\)", False), (r"\(\frac{3}{4}\)", False), (r"\(\frac{1}{2}\)", False)],
            "explanation": r"Convert to eighths: \(\frac{5}{8}+\frac{4}{8}-\frac{2}{8}=\frac{7}{8}\).",
        },
        {
            "text": r"A tank is \(\frac{3}{4}\) full. If \(\frac{1}{3}\) of the contents are drained, what fraction is left?",
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{2}\)", True), (r"\(\frac{1}{4}\)", False), (r"\(\frac{3}{7}\)", False), (r"\(\frac{7}{12}\)", False)],
            "explanation": r"Drained amount is \(\frac{1}{3}\times\frac{3}{4}=\frac{1}{4}\). Remaining \(=\frac{3}{4}-\frac{1}{4}=\frac{1}{2}\).",
        },
        {
            "text": r"Compute \(\left(\frac{1}{2}+\frac{1}{3}\right)\times\frac{3}{5}\).",
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{2}\)", True), (r"\(\frac{5}{18}\)", False), (r"\(\frac{3}{10}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"\(\frac{1}{2}+\frac{1}{3}=\frac{5}{6}\). Then \(\frac{5}{6}\times\frac{3}{5}=\frac{1}{2}\).",
        },
        {
            "text": r"A pizza is cut into \(8\) slices. If \(3\) people share \(5\) slices equally, what fraction of the whole pizza does each person get?",
            "difficulty": 3,
            "choices": [(r"\(\frac{5}{24}\)", True), (r"\(\frac{5}{8}\)", False), (r"\(\frac{3}{8}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"Each person gets \(\frac{5}{3}\) slices. As a fraction of the whole: \(\frac{5}{3}\div8=\frac{5}{3}\times\frac{1}{8}=\frac{5}{24}\).",
        },
        {
            "text": r"What fraction of \(\frac{4}{5}\) is equal to \(\frac{2}{3}\)?",
            "difficulty": 3,
            "choices": [(r"\(\frac{5}{6}\)", True), (r"\(\frac{2}{3}\)", False), (r"\(\frac{4}{5}\)", False), (r"\(\frac{8}{15}\)", False)],
            "explanation": r"We need \(x \times \frac{4}{5}=\frac{2}{3}\). So \(x=\frac{2}{3}\div\frac{4}{5}=\frac{2}{3}\times\frac{5}{4}=\frac{5}{6}\).",
        },
        {
            "text": r"Simplify \(\frac{36}{48}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{4}\)", True), (r"\(\frac{9}{12}\)", False), (r"\(\frac{6}{8}\)", False), (r"\(\frac{2}{3}\)", False)],
            "explanation": r"The GCD of 36 and 48 is 12. \(\frac{36}{48}=\frac{3}{4}\).",
        },
        {
            "text": r"How many \(\frac{1}{12}\)-cup servings are in \(\frac{2}{3}\) cup?",
            "difficulty": 2,
            "choices": [("8 servings", True), ("6 servings", False), ("4 servings", False), ("10 servings", False)],
            "explanation": r"\(\frac{2}{3}\div\frac{1}{12}=\frac{2}{3}\times12=8\).",
        },
        {
            "text": r"A painter uses \(\frac{3}{8}\) gallon of paint per room. How many complete rooms can be painted with \(4\frac{1}{2}\) gallons?",
            "difficulty": 3,
            "choices": [("12 rooms", True), ("10 rooms", False), ("11 rooms", False), ("9 rooms", False)],
            "explanation": r"\(4\frac{1}{2}=\frac{9}{2}\). Rooms painted: \(\frac{9}{2}\div\frac{3}{8}=\frac{9}{2}\times\frac{8}{3}=12\).",
        },
        {
            "text": r"At the start of the day, a bin is \(\frac{5}{6}\) full. During the day, \(\frac{2}{3}\) of the contents are used. What fraction of the bin is left?",
            "difficulty": 3,
            "choices": [(r"\(\frac{5}{18}\)", True), (r"\(\frac{1}{3}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(\frac{3}{8}\)", False)],
            "explanation": r"Amount used: \(\frac{2}{3}\times\frac{5}{6}=\frac{10}{18}=\frac{5}{9}\). Remaining: \(\frac{5}{6}-\frac{5}{9}=\frac{15}{18}-\frac{10}{18}=\frac{5}{18}\).",
        },
        {
            "text": r"Compute \(2\frac{3}{4}+3\frac{1}{6}\).",
            "difficulty": 2,
            "choices": [(r"\(5\frac{11}{12}\)", True), (r"\(5\frac{5}{6}\)", False), (r"\(6\frac{1}{4}\)", False), (r"\(5\frac{7}{12}\)", False)],
            "explanation": r"Add wholes: \(2+3=5\). Add fractions with LCD 12: \(\frac{3}{4}=\frac{9}{12}\), \(\frac{1}{6}=\frac{2}{12}\). Total: \(5+\frac{11}{12}=5\frac{11}{12}\).",
        },
        {
            "text": r"Which is NOT equivalent to \(\frac{3}{4}\)?",
            "difficulty": 1,
            "choices": [(r"\(\frac{9}{16}\)", True), (r"\(\frac{6}{8}\)", False), (r"\(\frac{9}{12}\)", False), (r"\(\frac{15}{20}\)", False)],
            "explanation": r"\(\frac{9}{16}\) cannot be simplified to \(\frac{3}{4}\). The others all equal \(\frac{3}{4}\).",
        },
        {
            "text": r"A road crew works \(\frac{1}{4}\) hour in the morning, \(\frac{3}{5}\) hour at midday, and \(\frac{1}{3}\) hour in the evening. Total hours worked?",
            "difficulty": 3,
            "choices": [(r"\(1\frac{11}{60}\) hours", True), (r"\(1\frac{1}{12}\) hours", False), (r"\(\frac{19}{60}\) hours", False), (r"\(1\frac{1}{4}\) hours", False)],
            "explanation": r"LCD of 4, 5, 3 is 60. \(\frac{15}{60}+\frac{36}{60}+\frac{20}{60}=\frac{71}{60}=1\frac{11}{60}\).",
        },
        {
            "text": r"Compute \(\frac{7}{10}-\frac{2}{5}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{10}\)", True), (r"\(\frac{5}{5}\)", False), (r"\(\frac{5}{10}\)", False), (r"\(\frac{1}{5}\)", False)],
            "explanation": r"Convert: \(\frac{2}{5}=\frac{4}{10}\). Then \(\frac{7}{10}-\frac{4}{10}=\frac{3}{10}\).",
        },
        {
            "text": r"A student answered \(\frac{3}{4}\) of the questions correctly and \(\frac{1}{6}\) incorrectly. Assuming no blanks, what fraction is unaccounted for?",
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{12}\)", True), (r"\(\frac{5}{24}\)", False), (r"\(\frac{1}{8}\)", False), (r"\(\frac{1}{10}\)", False)],
            "explanation": r"Total accounted for: \(\frac{3}{4}+\frac{1}{6}=\frac{9}{12}+\frac{2}{12}=\frac{11}{12}\). Unaccounted: \(1-\frac{11}{12}=\frac{1}{12}\).",
        },
    ],
    "essays": [
        {
            "text": (
                r"A recipe uses \(\frac{3}{4}\) cup of sugar for one batch. You need to make "
                r"\(2\frac{1}{2}\) batches. How much sugar is needed? Show the conversion, multiplication, "
                r"and final mixed-number answer."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: converts \(2\frac{1}{2}\) to \(\frac{5}{2}\), computes "
                r"\(\frac{3}{4}\times\frac{5}{2}=\frac{15}{8}=1\frac{7}{8}\), and includes cups. "
                "Deduct for adding instead of multiplying or leaving an unsimplified answer without explanation."
            ),
        },
        {
            "text": (
                r"A student studies \(\frac{2}{3}\) hour before dinner and \(\frac{5}{6}\) hour after dinner. "
                r"Find the total study time. Explain why a common denominator is needed."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: rewrites \(\frac{2}{3}=\frac{4}{6}\), adds \(\frac{4}{6}+\frac{5}{6}=\frac{9}{6}\), "
                r"simplifies to \(1\frac{1}{2}\) hours, and explains that thirds and sixths are different-size pieces."
            ),
        },
        {
            "text": (
                r"A board is \(7\frac{1}{2}\) feet long. A carpenter cuts pieces that are \(\frac{3}{4}\) foot long. "
                r"How many full pieces can be cut? Show the division and explain what any remainder means."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: converts \(7\frac{1}{2}=\frac{15}{2}\), divides by \(\frac{3}{4}\) using "
                r"\(\frac{15}{2}\times\frac{4}{3}=10\), and states that 10 full pieces can be cut with no remainder."
            ),
        },
        {
            "text": (
                r"A store shelf is \(\frac{7}{8}\) full in the morning and \(\frac{1}{4}\) of the shelf is sold by noon. "
                r"What fraction of the shelf is full at noon? Show the subtraction."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: rewrites \(\frac{1}{4}=\frac{2}{8}\), subtracts "
                r"\(\frac{7}{8}-\frac{2}{8}=\frac{5}{8}\), and explains the denominator stayed eighths."
            ),
        },
        {
            "text": (
                r"Compare \(\frac{5}{8}\), \(\frac{3}{5}\), and \(\frac{2}{3}\). Order them from least to greatest "
                r"and explain your method."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: uses a valid method such as denominator 120 or decimals: "
                r"\(\frac{3}{5}=0.6\), \(\frac{5}{8}=0.625\), \(\frac{2}{3}\approx0.667\), so "
                r"\(\frac{3}{5}<\frac{5}{8}<\frac{2}{3}\)."
            ),
        },
        {
            "text": (
                r"Correct this mistake: \(\frac{1}{2}+\frac{1}{3}=\frac{2}{5}\). Explain what went wrong and solve it correctly."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: identifies the error as adding denominators, rewrites with sixths, "
                r"\(\frac{1}{2}=\frac{3}{6}\), \(\frac{1}{3}=\frac{2}{6}\), and gives \(\frac{5}{6}\). "
                "The explanation should mention same-size pieces."
            ),
        },
        {
            "text": (
                r"A recipe calls for \(\frac{2}{3}\) cup of flour, \(\frac{1}{4}\) cup of sugar, and \(\frac{1}{6}\) cup of "
                r"butter. How much total dry ingredient is needed? Show all steps."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: finds LCD of 12, converts \(\frac{2}{3}=\frac{8}{12}\), \(\frac{1}{4}=\frac{3}{12}\), "
                r"\(\frac{1}{6}=\frac{2}{12}\), adds to get \(\frac{13}{12}=1\frac{1}{12}\) cups, and shows all work."
            ),
        },
        {
            "text": (
                r"A store has \(\frac{7}{8}\) of a shelf filled with books. A clerk removes \(\frac{1}{3}\) of the books "
                r"for restocking. What fraction of the shelf is now empty? Show the calculation."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: calculates the amount removed as \(\frac{1}{3}\times\frac{7}{8}=\frac{7}{24}\), "
                r"then finds the new filled amount \(\frac{7}{8}-\frac{7}{24}=\frac{21}{24}-\frac{7}{24}=\frac{14}{24}=\frac{7}{12}\), "
                r"and finally states empty fraction as \(1-\frac{7}{12}=\frac{5}{12}\)."
            ),
        },
        {
            "text": (
                r"A student completes \(\frac{5}{12}\) of a homework assignment in the morning and \(\frac{1}{3}\) in the afternoon. "
                r"How much is left to do? Explain your reasoning."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: converts \(\frac{1}{3}=\frac{4}{12}\), adds \(\frac{5}{12}+\frac{4}{12}=\frac{9}{12}=\frac{3}{4}\), "
                r"then subtracts from 1 to get \(\frac{1}{4}\) remaining. Explanation should clarify the steps."
            ),
        },
        {
            "text": (
                r"Three friends split a pizza. Alex eats \(\frac{1}{4}\) of it, Bella eats \(\frac{1}{3}\) of it, and "
                r"Carlos eats \(\frac{1}{6}\) of it. What fraction of the pizza is left over? Show all work."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: finds LCD of 12, converts each fraction, adds \(\frac{3}{12}+\frac{4}{12}+\frac{2}{12}=\frac{9}{12}=\frac{3}{4}\), "
                r"and calculates leftover as \(\frac{1}{4}\). Must show conversions."
            ),
        },
        {
            "text": (
                r"Explain why \(\frac{1}{2}\times\frac{1}{3}\) is less than either \(\frac{1}{2}\) or \(\frac{1}{3}\). "
                r"Use a real-world example to support your answer."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: states that multiplying by a fraction less than 1 makes the result smaller, "
                r"computes \(\frac{1}{6}\), and provides a sensible example such as 'half of one-third of a pizza.' "
                "The reasoning must be clear."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the dedicated GED Basic Math fractions mastery course."

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
