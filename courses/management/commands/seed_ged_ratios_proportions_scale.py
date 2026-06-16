"""
Seed a GED Math Foundations course for ratios, proportions, and scale factors.

Run:
    python manage.py seed_ged_ratios_proportions_scale
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
    "title": "GED Math Foundations: Ratios, Proportions & Scale Factors Mastery",
    "slug": "ged-ratios-proportions-scale",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Mathematical Reasoning course on ratios, equivalent ratios, "
        "proportions, ratio tables, part-to-part and part-to-whole reasoning, scale "
        "drawings, map scales, similar figures, direct variation, percent proportions, "
        "and multi-step proportional word problems. The course strengthens one of the "
        "most common GED quantitative reasoning patterns."
    ),
    "lessons": [
        (
            "1. Ratio Language: Part-to-Part and Part-to-Whole",
            r"""
A **ratio** compares quantities. The comparison can be part-to-part or part-to-whole, and the difference matters.

If a class has 12 students studying math and 8 students studying science, the part-to-part ratio of math students to science students is:
\[
12:8=3:2.
\]
This compares one part of the class to another part.

The total class has \(12+8=20\) students. The part-to-whole ratio of math students to all students is:
\[
12:20=3:5.
\]
This compares one part to the whole group.

[[figure:ratio_tape|A tape diagram keeps part-to-part and part-to-whole relationships visible.]]

Ratios can be written three ways:
\[
3:2,\qquad 3\text{ to }2,\qquad \frac{3}{2}.
\]
The fraction form is useful for computation, but the meaning still comes from the context.

Order matters. A ratio of boys to girls is not the same as girls to boys unless the two numbers are equal.

Common misconception: using the total when the question asks for part-to-part, or using a part when the question asks for part-to-whole.

Academic habit: write labels on both sides of the ratio, such as math:science or blue:total. Labels prevent reversed ratios.

[[check:A group has 6 red tiles and 4 blue tiles. What is the ratio of red tiles to all tiles?|6:10;;3:5|The whole is \(6+4=10\), so red:total is \(6:10=3:5\).]]
            """,
        ),
        (
            "2. Equivalent Ratios and Ratio Tables",
            r"""
Equivalent ratios name the same comparison. You create an equivalent ratio by multiplying or dividing both parts by the same nonzero number:
\[
3:2=6:4=9:6.
\]

Ratio tables organize equivalent ratios. If a recipe uses 3 cups of flour for 2 cups of sugar, then doubling the recipe gives 6 cups of flour and 4 cups of sugar.

\[
\begin{array}{c|cccc}
\text{flour} & 3 & 6 & 9 & 12\\
\text{sugar} & 2 & 4 & 6 & 8
\end{array}
\]

A ratio table can be scaled up, scaled down, or built by finding a unit value. If 5 notebooks cost 15 dollars, divide both quantities by 5 to get 1 notebook for 3 dollars.

Equivalent ratios are also useful for comparing. The ratios \(8:12\) and \(10:15\) are equivalent because both simplify to \(2:3\).

Common misconception: adding the same number to both parts. \(3:2\) is not equivalent to \(5:4\), because adding 2 changes the comparison.

Academic habit: when checking equivalent ratios, simplify both ratios or cross-multiply.
            """,
        ),
        (
            "3. Proportions and Cross Products",
            r"""
A **proportion** is an equation that says two ratios are equivalent:
\[
\frac{3}{4}=\frac{x}{20}.
\]
This can model recipes, maps, similar shapes, scale drawings, and percent problems.

[[figure:proportion_cross_products|Cross products solve a proportion by multiplying opposite corners.]]

To solve:
\[
\frac{3}{4}=\frac{x}{20}
\]
cross-multiply:
\[
3\cdot20=4x.
\]
Then solve:
\[
60=4x,\qquad x=15.
\]

Cross products work because multiplying both sides by both denominators clears the fractions. It is a shortcut, not magic.

Set up proportions with consistent labels. If one ratio is cups:cookies, the other ratio must also be cups:cookies. If the units switch positions, the equation may still look mathematical but represent the wrong relationship.

Common misconception: cross-multiplying the two numerators and the two denominators. Cross products use opposite corners, not same-level pairs.

Academic habit: write a label above each ratio column before solving. For example, \(\frac{\text{cups}}{\text{cookies}}=\frac{\text{cups}}{\text{cookies}}\).
            """,
        ),
        (
            "4. Unit Rates as a Proportional Reasoning Tool",
            r"""
A unit rate is a ratio with 1 in the denominator. It tells how much for one unit:
\[
\frac{180\text{ miles}}{3\text{ hours}}=60\text{ miles per hour}.
\]

[[figure:rate_double_number_line|A double number line shows two quantities growing at the same constant rate.]]

Proportional relationships have a constant unit rate. If a worker earns 18 dollars per hour, then the pay is proportional to hours:
\[
\frac{18}{1}=\frac{36}{2}=\frac{90}{5}.
\]

The unit rate can solve missing-value problems. If 4 pounds of apples cost 10 dollars, the cost per pound is:
\[
10/4=2.50.
\]
Then 7 pounds cost:
\[
7(2.50)=17.50.
\]

Some comparisons are easier with a unit rate than with cross products. To compare prices, compute dollars per ounce or dollars per item and choose the lower unit price.

Common misconception: dividing in the wrong order. Dollars per pound is dollars divided by pounds, not pounds divided by dollars.

Academic habit: include units in the unit rate. The phrase "2.50 per pound" is much clearer than "2.50."
            """,
        ),
        (
            "5. Part-Whole Ratio Problems",
            r"""
In part-whole ratio problems, the ratio parts add to the total number of equal parts.

Example: Blue and green tiles are in the ratio \(3:2\). There are 40 tiles total. How many are blue?

The total parts are:
\[
3+2=5.
\]
Each part represents:
\[
40/5=8\text{ tiles}.
\]
Blue uses 3 parts:
\[
3(8)=24\text{ blue tiles}.
\]

This is why a tape diagram is powerful: it shows how many equal parts make the whole.

If the problem asks for one part, multiply the part value by the number of parts requested. If it asks for the difference between parts, subtract the part counts first. In a \(7:4\) ratio with each part equal to 6, the difference is \((7-4)(6)=18\).

Common misconception: using \(3/2\) of the total when the ratio is \(3:2\). The blue share is \(3/5\), not \(3/2\), because the whole has 5 parts.

Academic habit: always add ratio parts before using a total. The sum of ratio parts represents the whole.
            """,
        ),
        (
            "6. Scale Drawings and Map Scales",
            r"""
A scale drawing represents a real object at a smaller or larger size. A map is a scale drawing of distance.

[[figure:map_scale_distance|A map scale converts a measured map distance into a real distance.]]

If a map scale says 1 inch represents 8 miles, then 3 inches on the map represents:
\[
3(8)=24\text{ miles}.
\]

You can also work backward. If the real distance is 40 miles and 1 inch represents 8 miles, then the map distance is:
\[
40/8=5\text{ inches}.
\]

Scale problems are proportional because the same multiplier applies throughout the drawing. The ratio:
\[
\frac{\text{map distance}}{\text{real distance}}
\]
should stay constant.

Units must match before comparing. If one distance is in inches and another in feet, convert first or use the given scale carefully.

Common misconception: adding the scale number instead of multiplying. If 1 inch represents 8 miles, then 4 inches represents \(4\cdot8=32\) miles, not 12 miles.

Academic habit: write "drawing -> real" or "map -> real" above the proportion. That keeps the scale direction consistent.
            """,
        ),
        (
            "7. Similar Figures and Scale Factor",
            r"""
Similar figures have the same shape but not necessarily the same size. Corresponding angles are equal, and corresponding side lengths are proportional.

[[figure:similar_rectangles_scale|Every corresponding length is multiplied by the same scale factor.]]

The **scale factor** from a smaller figure to a larger figure is:
\[
\frac{\text{new length}}{\text{original length}}.
\]
If a 4 cm side becomes 12 cm, the scale factor is:
\[
12/4=3.
\]

Every corresponding length uses the same multiplier. If a similar rectangle has width 3 cm and scale factor 3, the new width is:
\[
3(3)=9\text{ cm}.
\]

To find a missing side, set up a proportion:
\[
\frac{4}{12}=\frac{3}{x}.
\]
Cross products give \(4x=36\), so \(x=9\).

Common misconception: matching sides by position without checking correspondence. Long side must match long side, width must match width, and height must match height.

Academic habit: mark corresponding sides with the same symbol before writing the proportion.
            """,
        ),
        (
            "8. Scale Factor for Area and Volume",
            r"""
Lengths, areas, and volumes scale differently.

If the length scale factor is \(k\), then:
- corresponding lengths multiply by \(k\)
- areas multiply by \(k^2\)
- volumes multiply by \(k^3\)

Example: A rectangle is enlarged by scale factor 3. A side of 5 becomes 15. But the area becomes \(3^2=9\) times as large, not 3 times as large.

If a small rectangle has area \(20\text{ cm}^2\) and the scale factor is 3, the new area is:
\[
20(3^2)=20(9)=180\text{ cm}^2.
\]

For volume, if a cube is enlarged by scale factor 2, the volume becomes:
\[
2^3=8
\]
times as large.

Common misconception: using the length scale factor for area or volume. Area has two dimensions; volume has three dimensions.

Academic habit: identify the measurement type before using the scale factor: length, area, or volume.
            """,
        ),
        (
            "9. Direct Variation and Constant of Proportionality",
            r"""
A direct variation relationship has the form:
\[
y=kx.
\]
The number \(k\) is the **constant of proportionality**. It is also the unit rate:
\[
k=\frac{y}{x}.
\]

Example: A car travels 60 miles each hour. Distance \(d\) varies directly with time \(t\):
\[
d=60t.
\]
Here, \(k=60\) miles per hour.

[[figure:rate_graph|A proportional graph is a straight line through the origin.]]

A table is proportional if \(y/x\) is the same for every row. For:
\[
(2,10),\ (4,20),\ (6,30),
\]
the value \(y/x\) is 5 each time, so \(y=5x\).

If a graph or table does not pass through the origin or does not keep the same \(y/x\), it is not a direct variation.

Common misconception: thinking any straight line is proportional. A proportional line must go through \((0,0)\).

Academic habit: compute \(y/x\) for at least two rows before deciding a table is proportional.
            """,
        ),
        (
            "10. Percent Proportions and Percent Models",
            r"""
Percent means "per hundred," so many percent problems are proportions:
\[
\frac{\text{part}}{\text{whole}}=\frac{\text{percent}}{100}.
\]

Example: What is 30% of 80?
\[
\frac{x}{80}=\frac{30}{100}.
\]
Cross-multiply:
\[
100x=2400,\qquad x=24.
\]

Percent increase and decrease also use part-whole thinking. If a price goes from 50 dollars to 65 dollars, the increase is 15 dollars. The percent increase is:
\[
\frac{15}{50}=\frac{x}{100}.
\]
So \(x=30\%\).

Percent proportions connect to ratio language. A class with 18 out of 24 students passing has:
\[
\frac{18}{24}=\frac{75}{100}=75\%.
\]

Common misconception: using the new amount as the denominator for percent change. Percent change uses the original amount as the denominator.

Academic habit: label part, whole, and percent before writing the proportion.
            """,
        ),
        (
            "11. Multi-Step Proportional Word Problems",
            r"""
GED proportional reasoning often appears in multi-step word problems. The challenge is deciding which relationship is proportional and which extra step is needed.

Example: A recipe uses 3 cups of rice for 12 servings. How much rice is needed for 20 servings?
\[
\frac{3}{12}=\frac{x}{20}.
\]
Cross-multiply:
\[
12x=60,\qquad x=5.
\]
The recipe needs 5 cups of rice.

Example: A scale model car is 7 inches long. The real car is 14 feet long. Since 14 feet equals 168 inches, the scale is:
\[
7:168=1:24.
\]
The unit conversion is part of the setup.

Example: If 6 workers complete a job in 4 hours, doubling workers does not always mean the same situation unless the workers are equally productive and independent. GED problems usually state enough information; do not assume proportionality if the context does not support it.

Common misconception: cross-multiplying before checking units. A proportion with mismatched units can produce a neat but wrong answer.

Academic habit: write a one-line plan before calculating: "This is servings to cups," "This is map inches to miles," or "This is similar sides."
            """,
        ),
        (
            "12. Choosing a Strategy and Checking Reasonableness",
            r"""
Ratios and proportions can be solved in several valid ways. Choose the strategy that makes the structure clearest.

Useful strategies:
- **Simplify ratios** when comparing.
- **Use a ratio table** when quantities scale by friendly numbers.
- **Find a unit rate** when the question asks "per 1."
- **Use cross products** when one value is missing in a proportion.
- **Use a tape diagram** when a total is split into ratio parts.
- **Use scale factor** when figures are similar.

Reasonableness checks:
- A part cannot be larger than the whole unless the question asks for a ratio greater than 1.
- A scale drawing with more inches should represent more real distance.
- A larger similar figure should have longer corresponding sides.
- A percent greater than 100% is possible for increase but not for "part of a whole" unless the context allows more than one whole.

Example check: If 1 inch represents 8 miles, then 0.5 inch should represent less than 8 miles, not more. The answer should be 4 miles.

Common misconception: using one favorite method for every problem. Proportional reasoning is flexible, and the best method depends on the structure.

Academic habit: after solving, read the answer with units and ask whether the size makes sense.
            """,
        ),
    ],
    "mcqs": [
        item(r"A group has 12 math students and 8 science students. What is the ratio of math students to science students in simplest form?", r"\(3:2\)", [r"\(2:3\)", r"\(3:5\)", r"\(12:20\)"], ["Write the requested order: math:science is \(12:8\).", "Divide both parts by 4.", "The simplified ratio is \(3:2\)."], "using the total or reversing the order.", 1),
        item(r"A group has 12 math students and 8 science students. What is the ratio of math students to all students?", r"\(3:5\)", [r"\(3:2\)", r"\(2:5\)", r"\(5:3\)"], ["Find the whole: \(12+8=20\).", "Write math:total as \(12:20\).", "Simplify by 4 to get \(3:5\)."], "answering the part-to-part ratio instead of part-to-whole.", 1),
        item(r"Which ratio is equivalent to \(4:6\)?", r"\(2:3\)", [r"\(8:10\)", r"\(5:7\)", r"\(4:10\)"], ["Simplify \(4:6\) by dividing both parts by 2.", "The simplified ratio is \(2:3\).", "Therefore \(2:3\) is equivalent."], "adding or subtracting instead of multiplying/dividing both parts.", 1),
        item(r"A ratio is written as \(5\) to \(9\). Which fraction form matches the ratio?", r"\(\frac{5}{9}\)", [r"\(\frac{9}{5}\)", r"\(\frac{5}{14}\)", r"\(\frac{9}{14}\)"], ["The first quantity becomes the numerator.", "The second quantity becomes the denominator.", "So \(5\) to \(9\) is \(\frac{5}{9}\)."], "using the total as the denominator when only a two-part ratio was requested.", 1),

        item(r"Complete the equivalent ratio: \(3:5=12:?\)", r"\(20\)", [r"\(14\)", r"\(15\)", r"\(9\)"], ["The first part \(3\) was multiplied by 4 to get 12.", "Multiply the second part \(5\) by 4.", "The missing number is 20."], "adding 9 to both parts instead of multiplying by the same factor.", 1),
        item(r"A recipe uses 2 cups of sugar for 5 cups of flour. How many cups of sugar are needed for 15 cups of flour?", r"\(6\)", [r"\(3\)", r"\(10\)", r"\(12\)"], ["The flour amount is multiplied by 3 from 5 to 15.", "Multiply sugar by the same factor: \(2\cdot3=6\).", "The recipe needs 6 cups of sugar."], "scaling only one quantity or using addition.", 2),
        item(r"Are the ratios \(8:12\) and \(10:15\) equivalent?", "Yes, both simplify to \(2:3\).", ["No, because the numbers are different.", "No, because \(8+12\ne10+15\).", "Only if the total is 20."], ["Simplify \(8:12\) to \(2:3\).", "Simplify \(10:15\) to \(2:3\).", "Since they simplify to the same ratio, they are equivalent."], "judging by appearance instead of simplifying.", 1),
        item(r"A ratio table has \(x\): 4, 8, 12 and \(y\): 7, 14, ?. What is the missing \(y\)-value?", r"\(21\)", [r"\(18\)", r"\(19\)", r"\(28\)"], ["From \(x=4\) to \(x=12\), the factor is 3.", "Apply the same factor to \(y=7\).", "\(7\cdot3=21\)."], "using the difference in x-values instead of the scale factor.", 2),

        item(r"Solve the proportion \(\frac{3}{4}=\frac{x}{20}\).", r"\(15\)", [r"\(12\)", r"\(16\)", r"\(60\)"], ["Cross-multiply: \(3\cdot20=4x\).", "Compute \(60=4x\).", "Divide by 4 to get \(x=15\)."], "multiplying across the top or forgetting to divide by 4.", 2),
        item(r"Solve \(\frac{5}{8}=\frac{15}{x}\).", r"\(24\)", [r"\(18\)", r"\(20\)", r"\(30\)"], ["Cross-multiply: \(5x=8\cdot15\).", "Compute \(5x=120\).", "Divide by 5 to get \(x=24\)."], "matching 5 with 15 and scaling the wrong denominator.", 2),
        item(r"Which proportion is set up correctly for '3 cups make 12 servings; x cups make 20 servings'?", r"\(\frac{3}{12}=\frac{x}{20}\)", [r"\(\frac{3}{x}=\frac{12}{20}\)", r"\(\frac{3}{20}=\frac{12}{x}\)", r"\(\frac{12}{3}=\frac{x}{20}\)"], ["Keep the same labels in the same positions.", "Use cups over servings on both sides.", "The correct setup is \(\frac{3}{12}=\frac{x}{20}\)."], "switching labels between the two ratios.", 2),
        item(r"If \(\frac{a}{b}=\frac{c}{d}\), which equation shows the cross products?", r"\(ad=bc\)", [r"\(ab=cd\)", r"\(ac=bd\)", r"\(a+b=c+d\)"], ["Cross products multiply opposite corners.", "The opposite products are \(a\cdot d\) and \(b\cdot c\).", "So \(ad=bc\)."], "multiplying numbers that are on the same level.", 2),

        item(r"A car travels 180 miles in 3 hours. What is the unit rate?", r"\(60\) miles per hour", ["\(3\) hours per mile", "\(540\) miles per hour", "\(177\) miles per hour"], ["Unit rate means per 1 hour.", "Divide miles by hours: \(180/3=60\).", "The rate is 60 miles per hour."], "dividing in the wrong order or multiplying.", 1),
        item(r"Four pounds of apples cost \(\$10\). What is the cost per pound?", r"\(\$2.50\)", [r"\(\$4.00\)", r"\(\$0.40\)", r"\(\$14.00\)"], ["Cost per pound is dollars divided by pounds.", "Compute \(10/4=2.50\).", "The unit price is \(\$2.50\) per pound."], "dividing pounds by dollars.", 1),
        item(r"If apples cost \(\$2.50\) per pound, how much do 7 pounds cost?", r"\(\$17.50\)", [r"\(\$9.50\)", r"\(\$14.00\)", r"\(\$28.00\)"], ["Multiply the unit price by pounds.", "\(2.50\cdot7=17.50\).", "The cost is \(\$17.50\)."], "adding the unit price to the number of pounds.", 1),
        item(r"Which is the better buy: 12 oz for \(\$3.60\) or 20 oz for \(\$5.00\)?", "20 oz for \(\$5.00\)", ["12 oz for \(\$3.60\)", "They cost the same per ounce.", "Cannot be determined"], ["Find unit prices: \(3.60/12=0.30\) per oz.", "Find \(5.00/20=0.25\) per oz.", "The lower unit price is 20 oz for \(\$5.00\)."], "choosing the smaller total price without comparing per ounce.", 2),

        item(r"Blue and green tiles are in the ratio \(3:2\). There are 40 tiles total. How many are blue?", r"\(24\)", [r"\(16\)", r"\(20\)", r"\(60\)"], ["Add ratio parts: \(3+2=5\).", "Each part is \(40/5=8\).", "Blue is 3 parts, so \(3\cdot8=24\)."], "using \(3/2\) of the total instead of \(3/5\).", 2),
        item(r"A mix has red and white beads in the ratio \(7:5\). If there are 72 beads total, how many are white?", r"\(30\)", [r"\(42\)", r"\(35\)", r"\(12\)"], ["Total parts are \(7+5=12\).", "Each part is \(72/12=6\).", "White is 5 parts, so \(5\cdot6=30\)."], "using the red part or forgetting to add ratio parts.", 2),
        item(r"The ratio of adults to children is \(4:3\). If there are 28 people total, how many adults are there?", r"\(16\)", [r"\(12\)", r"\(7\)", r"\(21\)"], ["Total parts are \(4+3=7\).", "Each part is \(28/7=4\).", "Adults are 4 parts, so \(4\cdot4=16\)."], "using the number of ratio parts as the answer.", 2),
        item(r"In a \(9:4\) ratio, the larger group has 45 people. How many people are in the smaller group?", r"\(20\)", [r"\(36\)", r"\(25\)", r"\(49\)"], ["The larger group is 9 parts.", "Each part is \(45/9=5\).", "The smaller group is 4 parts, so \(4\cdot5=20\)."], "using the total-parts method when the given amount is only one part group.", 2),

        item(r"A map scale is 1 inch = 8 miles. How many miles are represented by 3 inches?", r"\(24\) miles", ["\(11\) miles", "\(5\) miles", "\(32\) miles"], ["Each inch represents 8 miles.", "Multiply \(3\cdot8\).", "The real distance is 24 miles."], "adding 3 and 8 instead of multiplying.", 1),
        item(r"A map scale is 1 inch = 8 miles. A real distance is 40 miles. What is the map distance?", r"\(5\) inches", ["\(32\) inches", "\(48\) inches", "\(4\) inches"], ["Use 8 miles per map inch.", "Divide real miles by 8: \(40/8=5\).", "The map distance is 5 inches."], "multiplying when working backward from real distance to map distance.", 2),
        item(r"A blueprint scale is 1 cm = 4 ft. A wall is 6 cm on the blueprint. How long is the real wall?", r"\(24\) ft", ["\(10\) ft", "\(1.5\) ft", "\(18\) ft"], ["Each blueprint centimeter represents 4 feet.", "Multiply \(6\cdot4=24\).", "The real wall is 24 feet."], "adding the scale numbers instead of using multiplication.", 1),
        item(r"A model is built with scale 1 inch = 5 feet. The model height is 9 inches. What is the real height?", r"\(45\) feet", ["\(14\) feet", "\(1.8\) feet", "\(54\) feet"], ["Each inch represents 5 feet.", "Multiply \(9\cdot5=45\).", "The real height is 45 feet."], "dividing by the scale when converting model to real size.", 1),

        item(r"A 4 cm side in a small rectangle corresponds to a 12 cm side in a larger similar rectangle. What is the scale factor from small to large?", r"\(3\)", [r"\(8\)", r"\(\frac{1}{3}\)", r"\(16\)"], ["Scale factor from small to large is new length divided by original length.", "Compute \(12/4=3\).", "The scale factor is 3."], "subtracting side lengths instead of dividing.", 1),
        item(r"Two similar rectangles have corresponding sides 3 cm and 9 cm. If another side in the small rectangle is 5 cm, what is the corresponding larger side?", r"\(15\) cm", ["\(11\) cm", "\(45\) cm", "\(8\) cm"], ["The scale factor is \(9/3=3\).", "Multiply the small side by 3.", "\(5\cdot3=15\) cm."], "adding the scale difference instead of multiplying by scale factor.", 2),
        item(r"In similar triangles, a 6-inch side corresponds to a 15-inch side. A second side is 8 inches. What is the corresponding larger side?", r"\(20\) inches", ["\(17\) inches", "\(30\) inches", "\(23\) inches"], ["The scale factor is \(15/6=2.5\).", "Multiply the second small side by 2.5.", "\(8\cdot2.5=20\) inches."], "using the difference \(15-6\) instead of the ratio \(15/6\).", 3),
        item(r"Which statement must be true for similar figures?", "Corresponding side lengths are proportional.", ["All side lengths are equal.", "Areas are always equal.", "Corresponding sides differ by the same addition."], ["Similar figures have the same shape.", "Their corresponding angles match and corresponding side lengths form equal ratios.", "Therefore corresponding side lengths are proportional."], "thinking similar means congruent, or equal in size.", 1),

        item(r"A figure is enlarged by scale factor 3. If an original side is 7 cm, what is the new side?", r"\(21\) cm", ["\(10\) cm", "\(49\) cm", "\(14\) cm"], ["Lengths multiply by the scale factor.", "Compute \(7\cdot3=21\).", "The new side is 21 cm."], "adding 3 to the side length.", 1),
        item(r"A rectangle has area \(20\text{ cm}^2\). It is enlarged by scale factor 3. What is the new area?", r"\(180\text{ cm}^2\)", [r"\(60\text{ cm}^2\)", r"\(23\text{ cm}^2\)", r"\(540\text{ cm}^2\)"], ["Area scales by the square of the length scale factor.", "\(3^2=9\).", "New area is \(20\cdot9=180\text{ cm}^2\)."], "multiplying area by 3 instead of \(3^2\).", 3),
        item(r"A cube is enlarged by scale factor 2. How many times as large is the volume?", r"\(8\) times", ["2 times", "4 times", "6 times"], ["Volume scales by the cube of the length scale factor.", "\(2^3=8\).", "The volume is 8 times as large."], "using the length or area scale factor for volume.", 2),
        item(r"A similar figure has scale factor \(\frac{1}{2}\). If the original area is 48 square units, what is the new area?", r"\(12\) square units", ["24 square units", "96 square units", "36 square units"], ["Area scales by \(k^2\).", "\((\frac{1}{2})^2=\frac{1}{4}\).", "New area is \(48\cdot\frac{1}{4}=12\)."], "halving the area instead of multiplying by the square of the scale factor.", 3),

        item(r"If \(y=5x\), what is the constant of proportionality?", r"\(5\)", [r"\(x\)", r"\(y\)", r"\(\frac{1}{5}\)"], ["A direct variation has form \(y=kx\).", "Compare \(y=5x\) to \(y=kx\).", "The constant \(k\) is 5."], "choosing a variable instead of the multiplier.", 1),
        item(r"The table has points \((2,10),(4,20),(6,30)\). What is \(y/x\) for each row?", r"\(5\)", [r"\(2\)", r"\(10\)", r"\(20\)"], ["Compute \(10/2=5\).", "Check another row: \(20/4=5\).", "The constant ratio is 5."], "subtracting instead of dividing.", 1),
        item(r"Which equation represents a proportional relationship with constant \(7\)?", r"\(y=7x\)", [r"\(y=x+7\)", r"\(y=7\)", r"\(x=7y\)"], ["A proportional relationship has form \(y=kx\).", "With \(k=7\), the equation is \(y=7x\).", "It passes through the origin."], "confusing a starting value with a proportional constant.", 1),
        item(r"Which table is proportional?", r"\((1,4),(2,8),(3,12)\)", [r"\((1,4),(2,7),(3,10)\)", r"\((0,4),(1,8),(2,12)\)", r"\((2,4),(4,6),(6,8)\)"], ["For \((1,4),(2,8),(3,12)\), \(y/x=4\) in every row.", "The ratio is constant.", "So the table is proportional."], "choosing a table with a constant difference instead of a constant ratio.", 2),
        item(r"Why is \(y=3x+2\) not a direct variation?", "It does not pass through the origin.", ["Its graph is a line.", "It has a coefficient of 3.", "It uses two variables."], ["Direct variation has form \(y=kx\).", "The \(+2\) means the graph crosses the y-axis at 2.", "It does not pass through \((0,0)\), so it is not direct variation."], "thinking any linear equation is proportional.", 2),

        item(r"What is \(30\%\) of 80?", r"\(24\)", [r"\(30\)", r"\(26.7\)", r"\(50\)"], ["Use \(\frac{x}{80}=\frac{30}{100}\).", "Cross-multiply: \(100x=2400\).", "Solve to get \(x=24\)."], "using 30 as the answer because it is the percent number.", 1),
        item(r"18 out of 24 students passed. What percent passed?", r"\(75\%\)", [r"\(24\%\)", r"\(18\%\)", r"\(133\%\)"], ["Write the part-whole ratio: \(18/24\).", "Simplify or divide: \(18/24=0.75\).", "Convert to percent: \(75\%\)."], "using the part or whole directly as the percent.", 1),
        item(r"A price rises from \(\$50\) to \(\$65\). What is the percent increase?", r"\(30\%\)", [r"\(15\%\)", r"\(23\%\)", r"\(65\%\)"], ["Find the increase: \(65-50=15\).", "Divide by the original amount: \(15/50=0.30\).", "Convert to percent: \(30\%\)."], "dividing by the new price instead of the original price.", 2),
        item(r"A shirt is discounted from \(\$80\) to \(\$60\). What percent decrease is this?", r"\(25\%\)", [r"\(20\%\)", r"\(33.3\%\)", r"\(60\%\)"], ["Find the decrease: \(80-60=20\).", "Divide by the original price: \(20/80=0.25\).", "The percent decrease is \(25\%\)."], "using the sale price as the denominator.", 2),
        item(r"Which proportion can find 18% of 250?", r"\(\frac{x}{250}=\frac{18}{100}\)", [r"\(\frac{250}{x}=\frac{18}{100}\)", r"\(\frac{x}{18}=\frac{250}{100}\)", r"\(\frac{18}{250}=\frac{x}{100}\)"], ["The unknown part is \(x\).", "The whole is 250.", "Use part over whole equals percent over 100."], "putting the percent in the whole position.", 2),

        item(r"A recipe uses 3 cups of rice for 12 servings. How much rice is needed for 20 servings?", r"\(5\) cups", ["4 cups", "6 cups", "8 cups"], ["Set up \(\frac{3}{12}=\frac{x}{20}\).", "Cross-multiply: \(12x=60\).", "Solve \(x=5\)."], "scaling 12 to 20 by adding 8 and adding 8 to the cups.", 2),
        item(r"A model car is 7 inches long. The real car is 14 feet long. What is the scale in inches to inches?", r"\(1:24\)", [r"\(1:2\)", r"\(7:14\)", r"\(24:1\)"], ["Convert 14 feet to inches: \(14\cdot12=168\) inches.", "Write model:real as \(7:168\).", "Simplify by 7 to get \(1:24\)."], "comparing inches to feet without converting units.", 3),
        item(r"A printer prints 45 pages in 3 minutes. At the same rate, how many pages in 8 minutes?", r"\(120\) pages", ["56 pages", "90 pages", "15 pages"], ["Find the unit rate: \(45/3=15\) pages per minute.", "Multiply by 8 minutes.", "\(15\cdot8=120\) pages."], "multiplying 45 by 8 without accounting for the original 3 minutes.", 2),
        item(r"If 5 markers cost \(\$7.50\), how much do 12 markers cost at the same price per marker?", r"\(\$18.00\)", [r"\(\$14.50\)", r"\(\$20.00\)", r"\(\$15.00\)"], ["Find price per marker: \(7.50/5=1.50\).", "Multiply by 12 markers.", "\(1.50\cdot12=18.00\)."], "adding the extra markers to the price instead of finding unit price.", 2),
        item(r"A scale drawing is 2.5 inches wide. The scale is 1 inch = 6 feet. What is the real width?", r"\(15\) feet", ["8.5 feet", "3.5 feet", "18 feet"], ["Each inch represents 6 feet.", "Multiply \(2.5\cdot6\).", "The real width is 15 feet."], "adding the scale number to the drawing length.", 1),

        item(r"Which method is usually best when a total is split in the ratio \(5:3\)?", "Use total parts or a tape diagram.", ["Use the quadratic formula.", "Use area scale factor.", "Use slope-intercept form."], ["A ratio split uses equal parts.", "The total parts are \(5+3\).", "A tape diagram or total-parts method matches the structure."], "choosing an unrelated algebra or geometry method.", 1),
        item(r"If 1 inch represents 8 miles, what should 0.5 inch represent?", r"\(4\) miles", ["8.5 miles", "16 miles", "0.5 miles"], ["Half an inch is half of 1 inch.", "Half of 8 miles is 4 miles.", "So 0.5 inch represents 4 miles."], "adding 0.5 and 8 or forgetting proportional scaling.", 1),
        item(r"Which answer is most reasonable if a map distance increases from 2 inches to 6 inches using the same scale?", "The real distance triples.", ["The real distance increases by exactly 4 miles.", "The real distance stays the same.", "The real distance is divided by 3."], ["The map distance changes from 2 to 6 inches.", "That is a factor of 3.", "With the same scale, real distance also triples."], "using the difference without knowing the scale or ignoring the multiplicative relationship.", 2),
        item(r"A ratio \(2:5\) describes part A to part B. Which statement is correct?", "For every 2 units of A, there are 5 units of B.", ["A is always 2 total units.", "The whole has 5 total parts.", "A is larger than B."], ["A ratio compares quantities by parts.", "\(2:5\) means A has 2 parts for every 5 parts of B.", "It does not give a fixed total unless a total is provided."], "treating ratio parts as exact counts without context.", 1),
        item(r"Which situation may not be proportional without more information?", "6 workers finish a job in 4 hours, so 12 workers finish in 2 hours.", ["1 inch on a map is 8 miles.", "A recipe doubles every ingredient.", "A unit price stays the same per ounce."], ["Worker problems depend on whether workers are equally productive and can work independently.", "The other situations state a fixed scale or rate.", "So the worker claim needs more information."], "assuming every real-world situation scales perfectly.", 3),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Math Foundations: Ratios, Proportions & Scale Factors Mastery course."

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
