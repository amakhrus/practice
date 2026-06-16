"""
Seed a complete GED Mathematical Reasoning course.

Run:
    python manage.py seed_ged_math_complete
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Math: Complete Course & Test Prep",
    "slug": "ged-math-complete-course",
    "program": "GED",
    "subject": "math",
    "description": (
        "A full GED Mathematical Reasoning course built like a private tutoring path: "
        "basic math, fractions, decimals, percents, ratios, word problems, geometry, "
        "measurement, data, probability, algebra, graphs, functions, and quadratics. "
        "Each lesson includes worked examples, visual diagrams, quick checks, and "
        "exam-style practice with explanations."
    ),
    "lessons": [
        (
            "1. GED Math Roadmap, Test Mindset, and Study System",
            r"""
The GED Mathematical Reasoning test is not trying to discover whether a student was "born good at math." It is testing whether the student can read a situation, choose a math model, use a formula or equation correctly, and check whether the answer makes sense.

The public GED outline groups math into **Basic Math**, **Geometry**, **Basic Algebra**, and **Graphs and Functions**. The formula sheet and calculator are there to reduce memorization pressure, but they do not choose the method for you. That is the student's job.

[[figure:ged_math_roadmap|The complete course follows the four tested areas and keeps returning to word-problem reasoning.]]

**The solution rule:** every solution needs three parts.
- **Name the target.** What is the question asking for: price, area, slope, probability, \(x\), or a percent?
- **Choose the tool.** Is this a proportion, formula, equation, graph, or statistic?
- **Check the meaning.** Does the unit, size, and direction of the answer make sense?

Example: A jacket costs 80 dollars and is 25% off. The target is the final price. The tool is percent of a number. The check is that the final price must be less than 80 dollars. Discount \(= 0.25(80)=20\), so final price \(=80-20=60\).

**Daily study rhythm.** Spend 10 minutes reviewing notes, 25 minutes solving new problems, and 10 minutes correcting mistakes. Corrections matter most: write the mistake type, the correct method, and one clue that should have told you what to do.

[[check:If a price drops from 80 dollars to 60 dollars, what is the percent decrease?|25%;;25;;0.25|The decrease is 20. Divide by the original price: \(20/80\).]]
            """,
        ),
        (
            "2. Number Sense, Integers, Place Value, and Order of Operations",
            r"""
Number sense means knowing what numbers *mean* before calculating. On the GED, it helps you estimate, compare, and catch unreasonable answers.

**Place value** is the base-10 system. Moving one place left multiplies by 10; moving one place right divides by 10. That is why \(4.7\) is ten times larger than \(0.47\), even though the digits look similar.

[[figure:place_value_ladder|Decimals become easier when each position has a job.]]

**Integers** are positive and negative whole numbers. A negative number can represent debt, temperature below zero, or moving left on a number line. Absolute value is distance from zero, so \(|-8|=8\).

**Order of operations** keeps everyone reading expressions the same way: parentheses, exponents, multiplication/division from left to right, then addition/subtraction from left to right.

Worked example:
\[
6 + 3^2 \times 2 = 6 + 9 \times 2 = 6 + 18 = 24.
\]
The exponent happens before multiplication, and multiplication happens before addition.

Common mistake: doing the expression left to right without respecting order. \(6+3^2\) is not \(9^2\); the exponent belongs only to the 3.

[[check:Evaluate \(6 + 3^2 \times 2\).|24|Square the 3 first, then multiply by 2, then add 6.]]
            """,
        ),
        (
            "3. Fractions: Meaning, Operations, and Mixed Numbers",
            r"""
A fraction is a division statement and a part-whole statement at the same time. In \(\frac{3}{4}\), the whole is cut into 4 equal pieces and we have 3 of them. It also means \(3 \div 4\).

Equivalent fractions are the same amount written with different-sized pieces:
\[
\frac{3}{4} = \frac{6}{8} = \frac{9}{12}.
\]
To simplify, divide numerator and denominator by the same common factor.

[[figure:fraction_percent_bar|A shaded fourth can be named as a fraction, decimal, or percent.]]

**Adding and subtracting fractions:** use a common denominator because the pieces must be the same size.
\[
\frac{2}{3}+\frac{1}{6}=\frac{4}{6}+\frac{1}{6}=\frac{5}{6}.
\]

**Multiplying fractions:** multiply straight across.
\[
\frac{2}{3}\times\frac{9}{10}=\frac{18}{30}=\frac{3}{5}.
\]

**Dividing fractions:** keep, change, flip.
\[
\frac{3}{4}\div\frac{2}{5}=\frac{3}{4}\times\frac{5}{2}=\frac{15}{8}=1\frac{7}{8}.
\]

Common mistake: adding denominators. \(\frac{1}{2}+\frac{1}{3}\neq\frac{2}{5}\). Denominators describe piece size; they are not counted like numerators.

[[check:Compute \(\frac{2}{3}+\frac{1}{6}\).|5/6|Rewrite \(\frac{2}{3}\) as \(\frac{4}{6}\), then add the numerators.]]
            """,
        ),
        (
            "4. Decimals, Percents, Ratios, Proportions, and Unit Rates",
            r"""
Decimals, percents, and fractions are three languages for the same idea.
\[
0.25=\frac{25}{100}=\frac{1}{4}=25\%.
\]

To change a decimal to a percent, multiply by 100 or move the decimal two places right: \(0.37=37\%\). To change a percent to a decimal, divide by 100: \(18\%=0.18\).

**Percent of a number:** turn the percent into a decimal, then multiply. \(15\%\) of 240 is \(0.15(240)=36\).

**Percent change:**
\[
\text{percent change}=\frac{\text{new}-\text{old}}{\text{old}}\times 100\%.
\]
If a value rises from 50 to 65, the change is 15 and the original is 50, so \(15/50=0.30=30\%\) increase.

Ratios compare quantities. A ratio of 3 blue tiles to 2 green tiles means 5 total parts. If there are 40 tiles, each part is \(40\div5=8\), so blue tiles \(=3(8)=24\).

[[figure:ratio_tape|Tape diagrams make ratios visible: total parts first, value per part second.]]

A **unit rate** is a rate per 1 unit. If a car travels 180 miles in 3 hours, its rate is \(180\div3=60\) miles per hour.

[[check:What is \(15\%\) of 240?|36|Change \(15\%\) to \(0.15\), then multiply by 240.]]
            """,
        ),
        (
            "5. Word Problems: Translate, Model, Solve, Check",
            r"""
GED math is full of word problems because real life does not say, "Please solve \(3x+8=35\)." Real life says, "A membership costs 8 dollars plus 3 dollars per visit."

Use this four-step structure:
- **Translate.** Underline the numbers and the target.
- **Model.** Choose an equation, proportion, formula, table, or graph.
- **Solve.** Do the arithmetic carefully.
- **Check.** Ask whether the answer's size and unit fit the story.

Keyword shortcuts help, but do not let them replace thinking. "More than" often means addition, "per" often means division or multiplication by a rate, and "of" often means multiplication. Still, always connect the expression to the story.

Worked example: A gym charges a 20 dollar signup fee and 15 dollars per month. After \(m\) months, the total cost is
\[
C=15m+20.
\]
After 6 months, \(C=15(6)+20=110\) dollars. If the total is 200 dollars, solve \(15m+20=200\), so \(15m=180\) and \(m=12\).

**Formula-sheet formulas** are still word problems. Simple interest uses \(I=Prt\). Distance uses \(d=rt\). Total cost uses units times price per unit.

[[check:Find the simple interest on 400 dollars at \(5\%\) for 2 years.|40|Use \(I=Prt\), with \(P=400\), \(r=0.05\), and \(t=2\).]]
            """,
        ),
        (
            "6. Geometry I: Perimeter, Area, and Composite Shapes",
            r"""
Geometry questions are easier when you separate **edge**, **surface**, and **space**.

**Perimeter** is distance around an edge, measured in linear units. **Area** is flat surface, measured in square units. **Volume** is 3D space, measured in cubic units.

Common area formulas:
\[
\text{rectangle } A=lw,\qquad \text{triangle } A=\frac{1}{2}bh,\qquad
\text{circle } A=\pi r^2.
\]

For composite shapes, do not panic. Split the shape into familiar pieces, find each area, then add or subtract.

[[figure:composite_area|This L-shape can be solved as two rectangles.]]

Worked example: Rectangle A is \(10\) ft by \(3\) ft, so \(A=30\). Rectangle B is \(6\) ft by \(6\) ft, so \(A=36\). Total area \(=30+36=66\text{ ft}^2\).

Common mistake: using perimeter when the question asks for area. If the unit should be square feet, you need a surface calculation.

[[check:Using the diagram, what is the total area in square feet?|66|Find the top rectangle \(10\cdot3\), then the lower rectangle \(6\cdot6\), then add.]]
            """,
        ),
        (
            "7. Geometry II: Circles, 3D Measurement, Pythagorean Theorem, and Coordinate Distance",
            r"""
For circles, the radius is the distance from center to edge. The diameter goes all the way across, so \(d=2r\).
\[
C=2\pi r=\pi d,\qquad A=\pi r^2.
\]

For prisms and cylinders, the core idea is **base area times height**. A cylinder has circular base area \(\pi r^2\), so
\[
V=\pi r^2h.
\]

[[figure:cylinder_volume|A cylinder's volume is the area of its circular base repeated through the height.]]

The Pythagorean theorem applies only to right triangles:
\[
a^2+b^2=c^2,
\]
where \(c\) is the hypotenuse, the side across from the right angle. Legs 5 and 12 give \(c=\sqrt{25+144}=\sqrt{169}=13\).

The distance formula is the Pythagorean theorem on the coordinate plane:
\[
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
\]
From \((1,2)\) to \((7,10)\), the horizontal change is 6 and the vertical change is 8, so the distance is \(\sqrt{6^2+8^2}=10\).

[[check:A cylinder has radius 3 and height 5. What is its volume in terms of \(\pi\)?|45pi;;45*pi|Use \(V=\pi r^2h\). Compute \(3^2\cdot5\).]]
            """,
        ),
        (
            "8. Data, Graphs, Tables, and Statistics",
            r"""
Data questions test careful reading. Before calculating, read the title, axis labels, scale, and units. A graph that starts at 90 can make a small change look huge.

**Mean** is the balance point: add the values and divide by the number of values. **Median** is the middle after ordering. **Mode** is most frequent. **Range** is maximum minus minimum.

Example: \(12,8,10,14\). The mean is \((12+8+10+14)/4=44/4=11\). Ordered values are \(8,10,12,14\), so the median is \((10+12)/2=11\).

[[figure:box_plot|A box plot shows spread: minimum, first quartile, median, third quartile, maximum.]]

**Weighted average** appears when scores or categories count differently. If quizzes are 40% of a grade and the final test is 60%, a quiz average of 80 and final score of 90 gives
\[
0.40(80)+0.60(90)=32+54=86.
\]

Scatter plots show association. If points generally rise from left to right, the association is positive. If they fall, it is negative.

[[figure:scatter_trend|A trend line summarizes the direction of a scatter plot.]]

[[check:Find the mean of \(12,8,10,14\).|11|Add all four numbers, then divide by 4.]]
            """,
        ),
        (
            "9. Probability and Counting",
            r"""
Probability is a fraction:
\[
P(\text{event})=\frac{\text{favorable outcomes}}{\text{total outcomes}}.
\]
It can be written as a fraction, decimal, or percent.

Example: A bag has 5 red marbles and 3 blue marbles. There are 8 total marbles, so \(P(\text{red})=5/8\).

**AND** usually means multiply for independent events. The chance of flipping heads and then rolling a 6 is
\[
\frac{1}{2}\times\frac{1}{6}=\frac{1}{12}.
\]

**OR** usually means add when the outcomes cannot both happen at the same time. Rolling a 1 or 2 on one die has probability \(\frac{1}{6}+\frac{1}{6}=\frac{1}{3}\).

**Complement** means "not." If rain has probability \(70\%\), no rain has probability \(30\%\).

Counting questions often use multiplication. If there are 4 shirts and 3 pants, there are \(4\times3=12\) outfits.

[[figure:coin_tree|A tree diagram shows all outcomes for two coin flips.]]

[[check:What is the probability of flipping two heads in a row?|1/4;;0.25;;25%|Heads on the first flip is \(1/2\). Heads on the second flip is \(1/2\). Multiply.]]
            """,
        ),
        (
            "10. Algebra I: Expressions, Equations, and Inequalities",
            r"""
Algebra is a language for unknown numbers. A variable is a placeholder. A coefficient is the number multiplying the variable. In \(3x+5\), the coefficient is 3 and the constant is 5.

To simplify, combine like terms and distribute carefully:
\[
2(x+5)+3x = 2x+10+3x = 5x+10.
\]

An equation is a balance. Whatever you do to one side, do to the other side.

[[figure:equation_balance|Solving equations is keeping the scale balanced while isolating the unknown.]]

Worked example:
\[
4x+7=31.
\]
Subtract 7: \(4x=24\). Divide by 4: \(x=6\).

Inequalities solve almost the same way, except for one major rule: **when multiplying or dividing by a negative number, flip the inequality sign.**
\[
-2x\le 8 \quad\Rightarrow\quad x\ge -4.
\]

Common mistake: losing the direction of the inequality after dividing by a negative.

[[check:Solve \(3x-4=14\). What is \(x\)?|6;;x=6|Add 4 to both sides, then divide by 3.]]
            """,
        ),
        (
            "11. Algebra II: Coordinate Plane, Slope, Lines, and Systems",
            r"""
The coordinate plane turns algebra into pictures. A point \((x,y)\) tells you how far to move horizontally and vertically from the origin.

Slope is steepness:
\[
m=\frac{y_2-y_1}{x_2-x_1}.
\]
From \((2,3)\) to \((6,11)\), slope is \((11-3)/(6-2)=8/4=2\).

The most common line form is
\[
y=mx+b,
\]
where \(m\) is slope and \(b\) is the y-intercept. In \(y=-3x+4\), the slope is \(-3\) and the y-intercept is 4.

[[figure:coord_line|Slope is rise over run, starting from the y-intercept.]]

A system of equations asks for a point that makes both equations true. Solve:
\[
\begin{cases}
y=x+2\\
x+y=10
\end{cases}
\]
Substitute \(y=x+2\): \(x+x+2=10\), so \(2x=8\), \(x=4\), and \(y=6\). The solution is \((4,6)\).

Common mistake: giving only \(x\) for a system. A complete system answer usually gives both coordinates.

[[check:What is the slope through \((2,3)\) and \((6,11)\)?|2|Use change in y over change in x: \((11-3)/(6-2)\).]]
            """,
        ),
        (
            "12. Functions, Exponents, Polynomials, Quadratics, and Final Review",
            r"""
A function is a rule where each input has exactly one output. Function notation \(f(x)\) means "the output when the input is \(x\)." It does not mean multiplication.

[[figure:function_machine|A function is a rule machine: input goes in, one output comes out.]]

If \(f(x)=2x+3\), then \(f(5)=2(5)+3=13\).

Exponents mean repeated multiplication. Key rules:
\[
x^a\cdot x^b=x^{a+b},\qquad \frac{x^a}{x^b}=x^{a-b},\qquad (x^a)^b=x^{ab}.
\]
So \(x^2\cdot x^5=x^7\).

Polynomials are expressions like \(x^2+7x+12\). Factoring reverses multiplication:
\[
x^2+7x+12=(x+3)(x+4).
\]

Quadratic equations may be solved by factoring or by the quadratic formula. For \(x^2-9=0\), factor:
\[
(x-3)(x+3)=0,
\]
so \(x=3\) or \(x=-3\).

[[figure:parabola|Quadratic roots are the x-values where the graph crosses the x-axis.]]

Final review method: after every missed problem, label the miss as one of these: reading, setup, formula, algebra move, arithmetic, calculator entry, or unit check. That turns mistakes into a study map.

[[check:If \(f(x)=2x+3\), what is \(f(5)\)?|13|Replace \(x\) with 5, then simplify.]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"Evaluate \(6 + 3^2 \times 2\).",
            "difficulty": 1,
            "choices": [(r"\(24\)", True), (r"\(18\)", False), (r"\(81\)", False), (r"\(30\)", False)],
            "explanation": r"Use order of operations: \(3^2=9\), then \(9\times2=18\), then \(6+18=24\).",
        },
        {
            "text": r"Simplify \(\dfrac{18}{24}\).",
            "difficulty": 1,
            "choices": [(r"\(\frac{3}{4}\)", True), (r"\(\frac{6}{8}\)", False), (r"\(\frac{9}{12}\)", False), (r"\(\frac{2}{3}\)", False)],
            "explanation": r"The greatest common factor of 18 and 24 is 6. Divide top and bottom by 6: \(\frac{18}{24}=\frac{3}{4}\).",
        },
        {
            "text": r"Compute \(\dfrac{5}{6}-\dfrac{1}{4}\).",
            "difficulty": 2,
            "choices": [(r"\(\frac{7}{12}\)", True), (r"\(\frac{4}{2}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(\frac{5}{24}\)", False)],
            "explanation": r"Use common denominator 12: \(\frac{5}{6}=\frac{10}{12}\) and \(\frac{1}{4}=\frac{3}{12}\). Difference \(=\frac{7}{12}\).",
        },
        {
            "text": r"What is \(\dfrac{2}{3}\) of \(45\)?",
            "difficulty": 1,
            "choices": [(r"\(30\)", True), (r"\(15\)", False), (r"\(20\)", False), (r"\(67.5\)", False)],
            "explanation": r"'Of' means multiply: \(\frac{2}{3}\times45=30\).",
        },
        {
            "text": r"Write \(0.45\) as a percent.",
            "difficulty": 1,
            "choices": [(r"\(45\%\)", True), (r"\(4.5\%\)", False), (r"\(0.45\%\)", False), (r"\(450\%\)", False)],
            "explanation": r"Move the decimal two places right: \(0.45=45\%\).",
        },
        {
            "text": r"\(18\) is what percent of \(72\)?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(40\%\)", False), (r"\(54\%\)", False)],
            "explanation": r"Divide part by whole: \(18/72=0.25=25\%\).",
        },
        {
            "text": r"A mix has blue and green tiles in the ratio \(3:2\). If there are \(40\) tiles total, how many are blue?",
            "difficulty": 2,
            "choices": [(r"\(24\)", True), (r"\(16\)", False), (r"\(20\)", False), (r"\(30\)", False)],
            "explanation": r"There are \(3+2=5\) parts. Each part is \(40/5=8\). Blue tiles \(=3\times8=24\).",
        },
        {
            "text": r"A car travels \(180\) miles in \(3\) hours. What is its average speed?",
            "difficulty": 1,
            "choices": [(r"\(60\) miles per hour", True), (r"\(54\) miles per hour", False), (r"\(90\) miles per hour", False), (r"\(183\) miles per hour", False)],
            "explanation": r"Average speed is distance divided by time: \(180/3=60\) miles per hour.",
        },
        {
            "text": r"A price increases from \(80\) dollars to \(100\) dollars. What is the percent increase?",
            "difficulty": 2,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(80\%\)", False), (r"\(125\%\)", False)],
            "explanation": r"The increase is \(20\). Divide by the original price: \(20/80=0.25=25\%\).",
        },
        {
            "text": r"Find the simple interest on \(500\) dollars at \(6\%\) for \(2\) years.",
            "difficulty": 2,
            "choices": [(r"\(60\) dollars", True), (r"\(30\) dollars", False), (r"\(56\) dollars", False), (r"\(600\) dollars", False)],
            "explanation": r"Use \(I=Prt\). \(I=500(0.06)(2)=60\).",
        },
        {
            "text": r"A rectangle is \(7\) ft long and \(4\) ft wide. What is its perimeter?",
            "difficulty": 1,
            "choices": [(r"\(22\) ft", True), (r"\(28\) ft", False), (r"\(11\) ft", False), (r"\(44\) ft", False)],
            "explanation": r"Perimeter of a rectangle is \(2l+2w=2(7)+2(4)=14+8=22\) ft.",
        },
        {
            "text": r"A triangle has base \(14\) cm and height \(9\) cm. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(63\text{ cm}^2\)", True), (r"\(126\text{ cm}^2\)", False), (r"\(23\text{ cm}^2\)", False), (r"\(46\text{ cm}^2\)", False)],
            "explanation": r"Triangle area \(=\frac{1}{2}bh=\frac{1}{2}(14)(9)=63\text{ cm}^2\).",
        },
        {
            "text": r"A circle has diameter \(12\) in. What is its circumference? Use \(\pi\approx3.14\).",
            "difficulty": 2,
            "choices": [(r"\(37.68\) in", True), (r"\(18.84\) in", False), (r"\(113.04\) in", False), (r"\(75.36\) in", False)],
            "explanation": r"Use \(C=\pi d\). \(C=3.14(12)=37.68\) inches.",
        },
        {
            "text": r"A cylinder has radius \(4\) cm and height \(6\) cm. What is its volume?",
            "difficulty": 2,
            "choices": [(r"\(96\pi\text{ cm}^3\)", True), (r"\(24\pi\text{ cm}^3\)", False), (r"\(48\pi\text{ cm}^3\)", False), (r"\(192\pi\text{ cm}^3\)", False)],
            "explanation": r"Volume \(=\pi r^2h=\pi(4^2)(6)=96\pi\text{ cm}^3\).",
        },
        {
            "text": r"A right triangle has legs \(5\) and \(12\). What is the hypotenuse?",
            "difficulty": 2,
            "choices": [(r"\(13\)", True), (r"\(17\)", False), (r"\(\sqrt{119}\)", False), (r"\(60\)", False)],
            "explanation": r"Use \(a^2+b^2=c^2\): \(5^2+12^2=25+144=169\), so \(c=13\).",
        },
        {
            "text": r"What is the distance between \((1,2)\) and \((7,10)\)?",
            "difficulty": 3,
            "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(\sqrt{52}\)", False), (r"\(8\)", False)],
            "explanation": r"The changes are \(6\) and \(8\). Distance \(=\sqrt{6^2+8^2}=\sqrt{100}=10\).",
        },
        {
            "text": r"An L-shaped floor can be seen as a \(10\) by \(6\) rectangle with a \(4\) by \(3\) rectangle removed. What is the area?",
            "difficulty": 2,
            "choices": [(r"\(48\) square units", True), (r"\(60\) square units", False), (r"\(12\) square units", False), (r"\(72\) square units", False)],
            "explanation": r"Large rectangle area \(=10(6)=60\). Removed rectangle area \(=4(3)=12\). Remaining area \(=60-12=48\).",
        },
        {
            "text": r"A sphere has radius \(3\). What is its volume?",
            "difficulty": 3,
            "choices": [(r"\(36\pi\)", True), (r"\(9\pi\)", False), (r"\(12\pi\)", False), (r"\(108\pi\)", False)],
            "explanation": r"Use \(V=\frac{4}{3}\pi r^3\). With \(r=3\), \(V=\frac{4}{3}\pi(27)=36\pi\).",
        },
        {
            "text": r"Find the mean of \(4,8,10,14\).",
            "difficulty": 1,
            "choices": [(r"\(9\)", True), (r"\(10\)", False), (r"\(36\)", False), (r"\(8\)", False)],
            "explanation": r"Mean \(=(4+8+10+14)/4=36/4=9\).",
        },
        {
            "text": r"Find the median of \(12,3,18,7,9\).",
            "difficulty": 1,
            "choices": [(r"\(9\)", True), (r"\(7\)", False), (r"\(12\)", False), (r"\(18\)", False)],
            "explanation": r"Order the data: \(3,7,9,12,18\). The middle value is \(9\).",
        },
        {
            "text": r"What is the mode of \(2,4,4,5,7\)?",
            "difficulty": 1,
            "choices": [(r"\(4\)", True), (r"\(2\)", False), (r"\(5\)", False), (r"\(7\)", False)],
            "explanation": r"The mode is the value that appears most often. \(4\) appears twice.",
        },
        {
            "text": r"What is the range of \(12,31,18,25\)?",
            "difficulty": 1,
            "choices": [(r"\(19\)", True), (r"\(43\)", False), (r"\(21.5\)", False), (r"\(13\)", False)],
            "explanation": r"Range \(=\text{maximum}-\text{minimum}=31-12=19\).",
        },
        {
            "text": r"A quiz average counts \(40\%\) and a final exam counts \(60\%\). If the quiz average is \(80\) and the final exam is \(90\), what is the weighted average?",
            "difficulty": 2,
            "choices": [(r"\(86\)", True), (r"\(85\)", False), (r"\(170\)", False), (r"\(88\)", False)],
            "explanation": r"Weighted average \(=0.40(80)+0.60(90)=32+54=86\).",
        },
        {
            "text": r"A box plot has \(Q1=22\) and \(Q3=38\). What is the interquartile range?",
            "difficulty": 2,
            "choices": [(r"\(16\)", True), (r"\(60\)", False), (r"\(30\)", False), (r"\(8\)", False)],
            "explanation": r"Interquartile range \(=Q3-Q1=38-22=16\).",
        },
        {
            "text": r"A bag has \(5\) red marbles and \(3\) blue marbles. What is the probability of drawing a red marble?",
            "difficulty": 1,
            "choices": [(r"\(\frac{5}{8}\)", True), (r"\(\frac{3}{8}\)", False), (r"\(\frac{5}{3}\)", False), (r"\(\frac{1}{5}\)", False)],
            "explanation": r"There are \(8\) marbles total and \(5\) red, so \(P(\text{red})=\frac{5}{8}\).",
        },
        {
            "text": r"What is the probability of flipping heads and then rolling a \(6\) on a fair die?",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{12}\)", True), (r"\(\frac{1}{8}\)", False), (r"\(\frac{1}{6}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"The events are independent, so multiply: \(\frac{1}{2}\times\frac{1}{6}=\frac{1}{12}\).",
        },
        {
            "text": r"A student has \(4\) shirts and \(3\) pairs of pants. How many different outfits are possible?",
            "difficulty": 1,
            "choices": [(r"\(12\)", True), (r"\(7\)", False), (r"\(9\)", False), (r"\(24\)", False)],
            "explanation": r"Use the counting principle: \(4\times3=12\) outfits.",
        },
        {
            "text": r"Evaluate \(3x-2\) when \(x=5\).",
            "difficulty": 1,
            "choices": [(r"\(13\)", True), (r"\(15\)", False), (r"\(10\)", False), (r"\(17\)", False)],
            "explanation": r"Substitute \(x=5\): \(3(5)-2=15-2=13\).",
        },
        {
            "text": r"Simplify \(2(x+5)+3x\).",
            "difficulty": 1,
            "choices": [(r"\(5x+10\)", True), (r"\(5x+5\)", False), (r"\(2x+15\)", False), (r"\(10x+3\)", False)],
            "explanation": r"Distribute first: \(2x+10+3x\). Combine like terms: \(5x+10\).",
        },
        {
            "text": r"Solve \(4x+7=31\).",
            "difficulty": 1,
            "choices": [(r"\(x=6\)", True), (r"\(x=8\)", False), (r"\(x=9.5\)", False), (r"\(x=5\)", False)],
            "explanation": r"Subtract 7: \(4x=24\). Divide by 4: \(x=6\).",
        },
        {
            "text": r"Solve \(5x-2=3x+10\).",
            "difficulty": 2,
            "choices": [(r"\(x=6\)", True), (r"\(x=4\)", False), (r"\(x=8\)", False), (r"\(x=12\)", False)],
            "explanation": r"Subtract \(3x\): \(2x-2=10\). Add 2: \(2x=12\). Divide by 2: \(x=6\).",
        },
        {
            "text": r"Solve \(-2x\le 8\).",
            "difficulty": 2,
            "choices": [(r"\(x\ge -4\)", True), (r"\(x\le -4\)", False), (r"\(x\ge 4\)", False), (r"\(x\le 4\)", False)],
            "explanation": r"Divide by \(-2\) and flip the inequality sign: \(x\ge -4\).",
        },
        {
            "text": r"What is the slope of \(y=-3x+4\)?",
            "difficulty": 1,
            "choices": [(r"\(-3\)", True), (r"\(4\)", False), (r"\(3\)", False), (r"\(-4\)", False)],
            "explanation": r"In \(y=mx+b\), the slope is \(m\). Here \(m=-3\).",
        },
        {
            "text": r"What is the y-intercept of \(y=2x-7\)?",
            "difficulty": 1,
            "choices": [(r"\(-7\)", True), (r"\(2\)", False), (r"\(7\)", False), (r"\(-2\)", False)],
            "explanation": r"In \(y=mx+b\), the y-intercept is \(b\). Here \(b=-7\).",
        },
        {
            "text": r"Which equation has slope \(3\) and y-intercept \(2\)?",
            "difficulty": 2,
            "choices": [(r"\(y=3x+2\)", True), (r"\(y=2x+3\)", False), (r"\(y=-3x+2\)", False), (r"\(y=3x-2\)", False)],
            "explanation": r"Slope-intercept form is \(y=mx+b\). With \(m=3\) and \(b=2\), the equation is \(y=3x+2\).",
        },
        {
            "text": r"Solve the system: \(y=x+2\) and \(x+y=10\).",
            "difficulty": 3,
            "choices": [(r"\((4,6)\)", True), (r"\((6,4)\)", False), (r"\((5,5)\)", False), (r"\((8,2)\)", False)],
            "explanation": r"Substitute \(y=x+2\) into \(x+y=10\): \(x+x+2=10\), so \(2x=8\), \(x=4\), and \(y=6\).",
        },
        {
            "text": r"Simplify \(x^2\cdot x^5\).",
            "difficulty": 1,
            "choices": [(r"\(x^7\)", True), (r"\(x^{10}\)", False), (r"\(2x^7\)", False), (r"\(x^3\)", False)],
            "explanation": r"When multiplying powers with the same base, add exponents: \(x^{2+5}=x^7\).",
        },
        {
            "text": r"Factor \(x^2+7x+12\).",
            "difficulty": 2,
            "choices": [(r"\((x+3)(x+4)\)", True), (r"\((x+2)(x+6)\)", False), (r"\((x-3)(x-4)\)", False), (r"\((x+1)(x+12)\)", False)],
            "explanation": r"Find numbers that multiply to 12 and add to 7: 3 and 4. So \(x^2+7x+12=(x+3)(x+4)\).",
        },
        {
            "text": r"Solve \(x^2-9=0\).",
            "difficulty": 2,
            "choices": [(r"\(x=-3\) or \(x=3\)", True), (r"\(x=9\)", False), (r"\(x=-9\) or \(x=9\)", False), (r"\(x=0\) or \(x=9\)", False)],
            "explanation": r"\(x^2-9=(x-3)(x+3)\). Set each factor to zero: \(x=3\) or \(x=-3\).",
        },
        {
            "text": r"If \(f(x)=x^2-1\), what is \(f(4)\)?",
            "difficulty": 1,
            "choices": [(r"\(15\)", True), (r"\(7\)", False), (r"\(16\)", False), (r"\(17\)", False)],
            "explanation": r"Substitute \(x=4\): \(f(4)=4^2-1=16-1=15\).",
        },
    ],
    "essays": [
        {
            "text": (
                r"A tablet costs \(240\) dollars. It is discounted by \(15\%\), then a \(6\%\) sales tax is applied "
                r"to the discounted price. Find the final price. Show every step and explain why the tax should "
                r"be calculated after the discount."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: computes discount \(0.15(240)=36\), discounted price \(240-36=204\), tax "
                r"\(0.06(204)=12.24\), final price \(216.24\), and explains that tax is applied to the actual sale "
                r"price after the discount. Deduct for applying tax to the original price or missing units."
            ),
        },
        {
            "text": (
                r"A recipe uses \(\frac{2}{3}\) cup of milk for one batch. You need \(2\frac{1}{2}\) batches. "
                r"How much milk is needed? Show the multiplication and simplify the answer."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: converts \(2\frac{1}{2}\) to \(\frac{5}{2}\), multiplies "
                r"\(\frac{2}{3}\cdot\frac{5}{2}=\frac{10}{6}=\frac{5}{3}=1\frac{2}{3}\), "
                "and includes cups as the unit."
            ),
        },
        {
            "text": (
                r"A tutoring service charges a \(25\) dollar registration fee plus \(18\) dollars per session. "
                r"Write an equation for total cost \(C\) after \(s\) sessions. Then find the cost for 7 sessions "
                r"and solve for the number of sessions if the total cost is \(169\) dollars."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: writes \(C=18s+25\), computes \(C=18(7)+25=151\), then solves "
                r"\(18s+25=169\), \(18s=144\), \(s=8\). Deduct for reversing the fee and rate or omitting a step."
            ),
        },
        {
            "text": (
                r"A cylindrical tank has radius \(2.5\) meters and height \(8\) meters. Find the volume in terms "
                r"of \(\pi\), then approximate using \(\pi\approx3.14\). Explain what the cubic units mean."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: uses \(V=\pi r^2h\), substitutes \(r=2.5\), \(h=8\), computes "
                r"\(V=\pi(6.25)(8)=50\pi\approx157\text{ m}^3\), and explains cubic meters measure 3D space."
            ),
        },
        {
            "text": (
                r"The data set is \(68, 72, 75, 85, 100\). Find the mean and median. Then explain which measure "
                r"better represents the typical score and why."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: mean \(=(68+72+75+85+100)/5=400/5=80\), median \(=75\), and explains that "
                r"the median may better represent the typical score because 100 pulls the mean upward."
            ),
        },
        {
            "text": (
                r"A bag contains 4 red, 3 blue, and 5 yellow marbles. A marble is drawn, replaced, then another "
                r"marble is drawn. Find the probability of drawing red first and yellow second. Explain why "
                r"replacement matters."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: total marbles \(=12\), \(P(\text{red})=4/12=1/3\), "
                r"\(P(\text{yellow})=5/12\), multiply to get \(5/36\), and explains that replacement keeps "
                r"the second draw probabilities the same."
            ),
        },
        {
            "text": (
                r"A line passes through \((2,5)\) and \((6,17)\). Find its slope, write the equation in "
                r"slope-intercept form, and interpret the slope in words."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: slope \(m=(17-5)/(6-2)=12/4=3\), uses \(y=3x+b\) and point \((2,5)\) "
                r"to find \(5=6+b\), \(b=-1\), equation \(y=3x-1\), and says y increases by 3 for each "
                r"1-unit increase in x."
            ),
        },
        {
            "text": (
                r"Solve \(x^2+5x+6=0\) by factoring. Then explain what the solutions mean on the graph of "
                r"\(y=x^2+5x+6\)."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: factors \(x^2+5x+6=(x+2)(x+3)\), sets each factor to zero, gets "
                r"\(x=-2\) and \(x=-3\), and explains that these are the x-intercepts where the graph crosses "
                r"the x-axis."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the complete GED Mathematical Reasoning course."

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
