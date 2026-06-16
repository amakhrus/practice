"""
Seed a dedicated GED Geometry course focused entirely on AREA.

Designed to go deeper than the Rates & Unit Rates course: 12 lessons, ~46
multiple-choice questions, labeled shape diagrams, interactive self-checks,
case studies, and common-mistake callouts. Every answer explanation teaches the
method, names the tempting wrong answer, and ends with a Pro tip. MCQ only.

Run:
    python manage.py seed_ged_geometry_area
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Area Mastery",
    "slug": "ged-geometry-area-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep GED Geometry course built around a single high-value skill: finding AREA. "
        "Students learn what area really means, master the formulas for rectangles, squares, "
        "triangles, parallelograms, trapezoids, and circles, then combine them to handle "
        "composite figures, coordinate grids, missing sides, unit conversions, and real-world "
        "problems from flooring, painting, gardening, and tiling. Every shape has a labeled "
        "diagram, every lesson has an interactive self-check, and every practice answer explains "
        "the method and adds a Pro tip."
    ),
    "lessons": [
        (
            "1. What Area Really Means: Square Units",
            r"""
**Area** is the amount of flat surface inside a two-dimensional shape. It answers the question, "how much space does this cover?" Area is always measured in **square units** -- square inches, square feet, square centimeters, written with a small \(^2\), like \(\text{cm}^2\).

The simplest way to see area is to count **unit squares** -- squares that are 1 unit on each side.

[[figure:area_unit_grid|Count the unit squares: 5 across and 3 down make 15 squares.]]

Worked example: a rectangle that is 5 units wide and 3 units tall holds
\[
5 \times 3 = 15 \text{ square units}.
\]
You could count all 15 squares one by one, but multiplying the rows by the columns is faster.

Do not confuse **area** with **perimeter**. Perimeter is the distance *around* a shape (measured in plain units); area is the surface *inside* it (measured in square units).

Case study - tiling a floor: if a floor is covered by square tiles arranged 8 tiles across and 6 tiles deep, the number of tiles is \(8 \times 6 = 48\). That is area in action.

Common mistake: writing area without the squared unit. "15" is incomplete; "15 square units" or "15 \(\text{cm}^2\)" is the full answer.

[[check:A rectangle is 4 units wide and 3 units tall. How many unit squares cover it?|12;;12 square units|Multiply rows by columns: \(4 \times 3\).]]
            """,
        ),
        (
            "2. Area of Rectangles and Squares",
            r"""
A **rectangle's** area is its length times its width:
\[
A = l \times w.
\]

[[figure:area_rectangle|Multiply the two side lengths: 8 cm by 5 cm gives 40 square cm.]]

Worked example: a rectangle 8 cm by 5 cm has area
\[
A = 8 \times 5 = 40 \text{ cm}^2.
\]

A **square** is a rectangle whose sides are all equal, so its area is a side times itself:
\[
A = s \times s = s^2.
\]
A square with side 6 m has area \(6^2 = 36 \text{ m}^2\).

Case study - a bedroom: a room measuring 12 ft by 10 ft has floor area
\[
12 \times 10 = 120 \text{ ft}^2,
\]
which is exactly how much carpet you would need to cover it.

Common mistake: adding the sides instead of multiplying. \(8 + 5 = 13\) is the start of the *perimeter*, not the area. Area multiplies.

[[check:A rectangle is 9 cm long and 4 cm wide. What is its area in square cm?|36;;36 cm2;;36 square cm|Multiply length by width: \(9 \times 4\).]]
            """,
        ),
        (
            "3. Area of Triangles",
            r"""
A **triangle** is exactly half of a rectangle (or parallelogram) that surrounds it, so its area is
\[
A = \tfrac{1}{2} \times b \times h,
\]
where \(b\) is the **base** and \(h\) is the **height**. The height is the straight-up distance from the base to the opposite point -- it must be **perpendicular** (at a right angle) to the base.

[[figure:area_triangle|The dashed line is the height: straight up from the base to the top point.]]

Worked example: a triangle with base 10 cm and height 6 cm has area
\[
A = \tfrac{1}{2} \times 10 \times 6 = \tfrac{1}{2} \times 60 = 30 \text{ cm}^2.
\]

Case study - a triangular sail: a sail with a 4 m base and 9 m height has area
\[
\tfrac{1}{2} \times 4 \times 9 = 18 \text{ m}^2.
\]

Common mistake: forgetting the \(\tfrac{1}{2}\). Multiplying base times height alone gives the area of the whole rectangle, which is **twice** the triangle.

[[check:A triangle has base 12 cm and height 5 cm. What is its area in square cm?|30;;30 cm2|Use \(\tfrac{1}{2} \times 12 \times 5\).]]
            """,
        ),
        (
            "4. Area of Parallelograms",
            r"""
A **parallelogram** is a slanted rectangle -- if you slice a triangle off one end and slide it to the other, you get a rectangle of the same area. So its area is just base times height:
\[
A = b \times h.
\]

[[figure:area_parallelogram|Use the perpendicular height (the dashed line), not the slanted side.]]

The key is that \(h\) is the **perpendicular height** (straight up and down), not the length of the tilted side.

Worked example: a parallelogram with base 9 cm and height 4 cm has area
\[
A = 9 \times 4 = 36 \text{ cm}^2.
\]

Case study - a parking space painted at a slant: even tilted, a space with a 3 m base and a 5 m perpendicular height covers \(3 \times 5 = 15 \text{ m}^2\) of pavement.

Common mistake: using the slanted side length as the height. Always use the perpendicular distance between the two parallel bases.

[[check:A parallelogram has base 7 cm and perpendicular height 6 cm. What is its area in square cm?|42;;42 cm2|Multiply base by height: \(7 \times 6\).]]
            """,
        ),
        (
            "5. Area of Trapezoids",
            r"""
A **trapezoid** has two parallel sides of different lengths, called \(b_1\) and \(b_2\). Because the two bases differ, you use their **average** times the height:
\[
A = \tfrac{1}{2}(b_1 + b_2) \times h.
\]

[[figure:area_trapezoid|Add the two parallel sides, take half, then multiply by the height.]]

Worked example: a trapezoid with parallel sides 6 cm and 10 cm and height 4 cm has area
\[
A = \tfrac{1}{2}(6 + 10) \times 4 = \tfrac{1}{2}(16)(4) = 32 \text{ cm}^2.
\]

Reading the formula in words: add the two parallel sides, cut the result in half, then multiply by the height.

Case study - a garden plot shaped like a trapezoid with parallel edges of 8 m and 12 m and a depth of 5 m covers
\[
\tfrac{1}{2}(8 + 12)(5) = \tfrac{1}{2}(20)(5) = 50 \text{ m}^2.
\]

Common mistake: forgetting to add the bases before halving. Do the parentheses first: add \(b_1 + b_2\), then take half.

[[check:A trapezoid has parallel sides 4 cm and 8 cm and height 5 cm. What is its area in square cm?|30;;30 cm2|Compute \(\tfrac{1}{2}(4 + 8)(5)\).]]
            """,
        ),
        (
            "6. Area of Circles",
            r"""
A **circle's** area depends on its **radius** \(r\) -- the distance from the center to the edge:
\[
A = \pi r^2.
\]
The number \(\pi\) (pi) is about **3.14**. The radius is **squared first**, then multiplied by \(\pi\).

[[figure:area_circle|Square the radius, then multiply by about 3.14.]]

Worked example: a circle with radius 7 cm has area
\[
A = \pi (7)^2 = \pi (49) \approx 3.14 \times 49 \approx 153.9 \text{ cm}^2.
\]

If a problem gives the **diameter** (the full distance across), first cut it in half to get the radius. A circle with diameter 10 cm has radius 5 cm and area \(\pi(5)^2 = 3.14 \times 25 = 78.5 \text{ cm}^2\).

Case study - a circular tabletop with radius 3 ft has area \(3.14 \times 9 \approx 28.3 \text{ ft}^2\) of surface to varnish.

Common mistake: doubling the radius instead of squaring it. \(r^2\) means \(r \times r\), not \(r \times 2\). For \(r = 7\), that is \(49\), not \(14\).

[[check:A circle has radius 5 cm. Using 3.14 for pi, what is its area in square cm?|78.5;;78.50|Compute \(3.14 \times 5^2 = 3.14 \times 25\).]]
            """,
        ),
        (
            "7. Composite Figures: Add and Subtract",
            r"""
A **composite** (compound) figure is built from simpler shapes. The trick is to **break it into pieces**, find each piece's area, and then **add** -- or, if a piece is cut out, **subtract**.

[[figure:composite_area|Split the L-shape into two rectangles, find each area, then add them.]]

Worked example (adding): split an L-shaped room into Rectangle A (10 ft by 3 ft) and Rectangle B (6 ft by 6 ft).
\[
A = 10 \times 3 = 30, \qquad B = 6 \times 6 = 36, \qquad \text{total} = 30 + 36 = 66 \text{ ft}^2.
\]

Worked example (subtracting): a 10 m by 8 m yard with a 4 m by 3 m shed removed has usable area
\[
(10 \times 8) - (4 \times 3) = 80 - 12 = 68 \text{ m}^2.
\]

Case study - a running track around a field, a window in a wall, a path through a garden: all are "big shape minus the hole," solved by subtraction.

Common mistake: forgetting a piece, or adding when you should subtract. Decide first whether each region is *added on* or *cut out*.

[[check:A 10 m by 8 m yard has a 4 m by 3 m shed removed. What usable area remains in square meters?|68;;68 m2|Subtract: \(80 - 12\).]]
            """,
        ),
        (
            "8. Area on the Coordinate Grid",
            r"""
Shapes are often drawn on a **coordinate grid**, where each point has an \((x, y)\) address. To find a side length, count the grid squares or subtract coordinates.

For a horizontal side, subtract the x-values; for a vertical side, subtract the y-values.

Worked example: a rectangle has corners at \((1, 1)\), \((6, 1)\), \((6, 4)\), and \((1, 4)\).
- Width \(= 6 - 1 = 5\).
- Height \(= 4 - 1 = 3\).
- Area \(= 5 \times 3 = 15\) square units.

Worked example: a triangle has a base from \((2, 1)\) to \((10, 1)\), so the base is \(10 - 2 = 8\). If its top point is at height \(y = 6\), the height is \(6 - 1 = 5\), and
\[
A = \tfrac{1}{2}(8)(5) = 20 \text{ square units}.
\]

Case study - a plot of land mapped on a grid: surveyors read coordinates and subtract them to get exact side lengths before computing area.

Common mistake: counting the dots instead of the spaces between them. From \(x = 1\) to \(x = 6\) there are 5 *spaces* (the length), even though 6 grid lines are touched.

[[check:A rectangle has corners at (2,2), (9,2), (9,6), and (2,6). What is its area in square units?|28;;28 square units|Width \(= 9-2 = 7\), height \(= 6-2 = 4\), then multiply.]]
            """,
        ),
        (
            "9. Working Backward: Find a Missing Side",
            r"""
Sometimes the GED gives you the **area** and asks for a missing side. Use the same formula, but solve for the unknown by **dividing**.

For a rectangle, since \(A = l \times w\):
\[
l = \frac{A}{w}, \qquad w = \frac{A}{l}.
\]

Worked example: a rectangle has area \(48 \text{ cm}^2\) and width 6 cm. The length is
\[
l = \frac{48}{6} = 8 \text{ cm}.
\]

For a square, since \(A = s^2\), the side is the **square root** of the area:
\[
s = \sqrt{A}.
\]
A square of area \(49 \text{ cm}^2\) has side \(\sqrt{49} = 7\) cm.

For a triangle, since \(A = \tfrac{1}{2} b h\), undo the half first. If \(A = 24\) and \(b = 8\):
\[
24 = \tfrac{1}{2}(8)h = 4h, \qquad h = \frac{24}{4} = 6.
\]

Case study - planning a 60 ft\(^2\) rug for a room that is 10 ft long: the rug's width must be \(60 / 10 = 6\) ft.

Common mistake: forgetting to undo the \(\tfrac{1}{2}\) in a triangle. Multiply the area by 2 (or divide by \(\tfrac{1}{2}\)) before dividing by the base.

[[check:A rectangle has area 48 square cm and a width of 6 cm. What is its length in cm?|8;;8 cm|Divide area by width: \(48 \div 6\).]]
            """,
        ),
        (
            "10. Units, Squared Units, and Conversions",
            r"""
Area units are always **squared**, and squared units convert differently from regular ones.

Because 1 foot = 12 inches, a 1 ft by 1 ft square is 12 in by 12 in, so
\[
1 \text{ ft}^2 = 12 \times 12 = 144 \text{ in}^2.
\]
Likewise, since 1 yard = 3 feet,
\[
1 \text{ yd}^2 = 3 \times 3 = 9 \text{ ft}^2.
\]

Worked example: a 2 ft by 3 ft poster has area \(6 \text{ ft}^2\). In square inches that is
\[
6 \times 144 = 864 \text{ in}^2.
\]

Always keep the **same unit** on both sides before multiplying. If one side is in feet and the other in inches, convert first.

Case study - carpet is often priced per square yard. A 12 ft by 9 ft room is \(108 \text{ ft}^2\), which is \(108 / 9 = 12\) square yards.

Common mistake: converting square units like regular units. \(1 \text{ ft}^2\) is **144** in\(^2\), not 12. The conversion factor itself gets squared.

[[check:How many square inches are in 1 square foot?|144;;144 in2|A foot is 12 inches, so \(12 \times 12\).]]
            """,
        ),
        (
            "11. Real-World Area Problems",
            r"""
Most GED area questions are dressed up as everyday situations. The wording changes, but the math is the same: pick the shape, use its formula.

- **Flooring / carpet / tile:** area of the floor (length times width).
- **Painting:** area of the wall or surface.
- **Gardening / lawn / fertilizer:** area of the plot.
- **Material to buy:** total area, sometimes minus openings like doors and windows.

Worked example - carpet: a room 15 ft by 12 ft needs
\[
15 \times 12 = 180 \text{ ft}^2 \text{ of carpet}.
\]

Worked example - paint with an opening: a wall 10 ft by 8 ft \(= 80 \text{ ft}^2\) has a 3 ft by 7 ft door (\(21 \text{ ft}^2\)) that is not painted, so the painted area is
\[
80 - 21 = 59 \text{ ft}^2.
\]

Worked example - cost: if tile costs 4 dollars per square foot and a floor is \(50 \text{ ft}^2\), the cost is \(50 \times 4 = 200\) dollars.

Case study - a garden bed: a rectangular bed 20 ft by 4 ft is \(80 \text{ ft}^2\); one bag of soil covers \(16 \text{ ft}^2\), so you need \(80 / 16 = 5\) bags.

Common mistake: ignoring the "per square foot" step. Finding the area is only half the problem when the question asks for total **cost** or number of **bags / cans / boxes**.

[[check:A room is 15 ft by 12 ft. How many square feet of carpet are needed?|180;;180 ft2|Multiply length by width: \(15 \times 12\).]]
            """,
        ),
        (
            "12. GED Area Strategy: Pick the Formula, Check the Units",
            r"""
Area problems get easier with a steady routine. Use this checklist:

- **What shape is it?** Rectangle, square, triangle, parallelogram, trapezoid, circle, or a composite of these.
- **Which formula fits?** Match the shape to its formula.
- **Do I have the right measurements?** A triangle and parallelogram need the *perpendicular* height; a circle needs the *radius* (halve the diameter if needed).
- **Did I keep one unit?** Convert so all lengths share a unit before multiplying.
- **Does the answer use square units?**

Formula quick-reference:
- Rectangle: \(A = l \times w\)
- Square: \(A = s^2\)
- Triangle: \(A = \tfrac{1}{2} b h\)
- Parallelogram: \(A = b h\)
- Trapezoid: \(A = \tfrac{1}{2}(b_1 + b_2) h\)
- Circle: \(A = \pi r^2\)

Error analysis: a student finds a triangle's area as \(b \times h = 10 \times 6 = 60 \text{ cm}^2\). The mistake is skipping the \(\tfrac{1}{2}\); the real area is \(\tfrac{1}{2}(10)(6) = 30 \text{ cm}^2\).

Case study - mixed figure: an arena floor is a rectangle (\(30 \times 20 = 600\)) with a semicircle on one end (radius 10, half of \(\pi r^2\): \(\tfrac{1}{2}(3.14)(100) = 157\)). Total \(\approx 757 \text{ ft}^2\). Break it up, then add.

Final habit: before you compute, say the shape and the formula out loud. The right formula is most of the battle.

[[check:Which formula gives the area of a triangle with base b and height h?|1/2bh;;0.5bh;;half b h|Area of a triangle is half the base times the height.]]
            """,
        ),
    ],
    "mcqs": [
        # --- Rectangles & squares ---
        {
            "text": r"A rectangle is \(8\) cm long and \(5\) cm wide. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(40\ \text{cm}^2\)", True), (r"\(13\ \text{cm}^2\)", False), (r"\(26\ \text{cm}^2\)", False), (r"\(80\ \text{cm}^2\)", False)],
            "explanation": r"Area of a rectangle is length times width: \(8 \times 5 = 40\ \text{cm}^2\). The trap 13 comes from adding the sides (\(8+5\)) -- that starts a perimeter, not an area -- and 26 is the full perimeter \(2(8+5)\). Area multiplies the two dimensions. Pro tip: area answers use SQUARE units (\(\text{cm}^2\)); if a question asks for the distance around, that is perimeter instead.",
        },
        {
            "text": r"What is the area of a square with side length \(6\) m?",
            "difficulty": 1,
            "choices": [(r"\(36\ \text{m}^2\)", True), (r"\(24\ \text{m}^2\)", False), (r"\(12\ \text{m}^2\)", False), (r"\(18\ \text{m}^2\)", False)],
            "explanation": r"A square's area is a side times itself: \(s^2 = 6^2 = 36\ \text{m}^2\). The trap 24 is the perimeter (\(4 \times 6\)), and 12 doubles the side instead of squaring it. Squaring means \(6 \times 6\), not \(6 \times 2\). Pro tip: \(s^2\) is 'side times side' -- picture a 6-by-6 grid, which holds exactly 36 unit squares.",
        },
        {
            "text": r"A rectangular rug is \(12\) ft by \(7\) ft. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(84\ \text{ft}^2\)", True), (r"\(38\ \text{ft}^2\)", False), (r"\(19\ \text{ft}^2\)", False), (r"\(94\ \text{ft}^2\)", False)],
            "explanation": r"Multiply length by width: \(12 \times 7 = 84\ \text{ft}^2\). The trap 38 is the perimeter \(2(12+7)\), and 19 is just \(12+7\). A rug covers a surface, so you need area (multiply), not perimeter (add). Pro tip: when a problem says 'cover', 'carpet', or 'tile', you want area in square units.",
        },
        {
            "text": r"A square tile measures \(9\) in on each side. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(81\ \text{in}^2\)", True), (r"\(18\ \text{in}^2\)", False), (r"\(36\ \text{in}^2\)", False), (r"\(72\ \text{in}^2\)", False)],
            "explanation": r"A square tile's area is \(s^2 = 9^2 = 81\ \text{in}^2\). The trap 36 is the perimeter (\(4 \times 9\)); 18 doubles the side instead of squaring. Remember \(9^2 = 9 \times 9 = 81\), not \(9 \times 2\). Pro tip: memorizing perfect squares (\(1, 4, 9, 16, 25, 36, 49, 64, 81, 100\)) makes square-area questions instant.",
        },
        {
            "text": r"A bedroom floor is \(12\) ft by \(10\) ft. How much carpet covers it?",
            "difficulty": 1,
            "choices": [(r"\(120\ \text{ft}^2\)", True), (r"\(44\ \text{ft}^2\)", False), (r"\(22\ \text{ft}^2\)", False), (r"\(110\ \text{ft}^2\)", False)],
            "explanation": r"Carpet covers the floor's surface, so find area: \(12 \times 10 = 120\ \text{ft}^2\). The trap 44 is the perimeter \(2(12+10)\); 22 is \(12+10\). 'How much carpet' means area, in square feet. Pro tip: match the keyword to the math -- 'cover/carpet/paint' = area (multiply); 'fence/border/trim' = perimeter (add).",
        },
        # --- Triangles ---
        {
            "text": r"A triangle has base \(10\) cm and height \(6\) cm. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(30\ \text{cm}^2\)", True), (r"\(60\ \text{cm}^2\)", False), (r"\(16\ \text{cm}^2\)", False), (r"\(32\ \text{cm}^2\)", False)],
            "explanation": r"Triangle area is half the base times the height: \(\tfrac{1}{2}(10)(6) = 30\ \text{cm}^2\). The trap 60 forgets the \(\tfrac{1}{2}\) (that is the full surrounding rectangle); 16 just adds base and height. A triangle is exactly half its bounding rectangle. Pro tip: compute \(b \times h\) first, then halve -- the halving is what students most often skip.",
        },
        {
            "text": r"A triangle has base \(12\) cm and height \(5\) cm. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(30\ \text{cm}^2\)", True), (r"\(60\ \text{cm}^2\)", False), (r"\(17\ \text{cm}^2\)", False), (r"\(35\ \text{cm}^2\)", False)],
            "explanation": r"Half base times height: \(\tfrac{1}{2}(12)(5) = 30\ \text{cm}^2\). The trap 60 drops the \(\tfrac{1}{2}\); 17 adds the two numbers. Pro tip: if your triangle answer equals base times height with no halving, you have made the classic triangle error -- always take half.",
        },
        {
            "text": r"A triangular sail has a base of \(4\) m and a height of \(9\) m. What is its area?",
            "difficulty": 2,
            "choices": [(r"\(18\ \text{m}^2\)", True), (r"\(36\ \text{m}^2\)", False), (r"\(13\ \text{m}^2\)", False), (r"\(22\ \text{m}^2\)", False)],
            "explanation": r"\(\tfrac{1}{2}(4)(9) = 18\ \text{m}^2\). The trap 36 forgets the half; 13 just adds \(4+9\). The height must be perpendicular to the base, which it is here. Pro tip: words like 'sail' or 'triangular' signal the \(\tfrac{1}{2} b h\) formula -- spot the shape, then use its formula.",
        },
        {
            "text": r"What is the area of a triangle with base \(14\) cm and height \(10\) cm?",
            "difficulty": 1,
            "choices": [(r"\(70\ \text{cm}^2\)", True), (r"\(140\ \text{cm}^2\)", False), (r"\(24\ \text{cm}^2\)", False), (r"\(35\ \text{cm}^2\)", False)],
            "explanation": r"\(\tfrac{1}{2}(14)(10) = 70\ \text{cm}^2\). The trap 140 is \(b \times h\) without the half; 24 adds the sides. Pro tip: multiply base and height first (140), then halve (70) -- doing the halving last keeps the arithmetic clean.",
        },
        {
            "text": r"A student computes a triangle's area as \(b \times h = 8 \times 6 = 48\). What did they do wrong?",
            "difficulty": 2,
            "choices": [(r"They forgot to multiply by \(\tfrac{1}{2}\)", True), ("They forgot to add the sides", False), ("They used the wrong base", False), ("Nothing; 48 is correct", False)],
            "explanation": r"The student found \(b \times h = 48\) but forgot the \(\tfrac{1}{2}\); the real area is \(\tfrac{1}{2}(8)(6) = 24\ \text{cm}^2\). That missing one-half is the number-one triangle mistake. Pro tip: a triangle is half of a rectangle, so its area is always half of base times height -- never the full product.",
        },
        # --- Parallelograms ---
        {
            "text": r"A parallelogram has base \(9\) cm and perpendicular height \(4\) cm. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(36\ \text{cm}^2\)", True), (r"\(13\ \text{cm}^2\)", False), (r"\(18\ \text{cm}^2\)", False), (r"\(40\ \text{cm}^2\)", False)],
            "explanation": r"A parallelogram's area is base times perpendicular height: \(9 \times 4 = 36\ \text{cm}^2\). The trap 13 adds \(9+4\); 18 wrongly halves the product as if it were a triangle. A parallelogram equals a full rectangle of the same base and height -- no halving. Pro tip: only triangles get the \(\tfrac{1}{2}\); parallelograms use the full \(b \times h\).",
        },
        {
            "text": r"A parallelogram has base \(12\) cm and height \(5\) cm. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(60\ \text{cm}^2\)", True), (r"\(17\ \text{cm}^2\)", False), (r"\(30\ \text{cm}^2\)", False), (r"\(34\ \text{cm}^2\)", False)],
            "explanation": r"\(b \times h = 12 \times 5 = 60\ \text{cm}^2\). The trap 17 adds the numbers; 30 wrongly halves it (that would be a triangle). Pro tip: a parallelogram 'slides' into a rectangle of the same base and height, so no halving is needed.",
        },
        {
            "text": r"A parallelogram has base \(7\) m and perpendicular height \(6\) m. What is its area?",
            "difficulty": 1,
            "choices": [(r"\(42\ \text{m}^2\)", True), (r"\(13\ \text{m}^2\)", False), (r"\(26\ \text{m}^2\)", False), (r"\(21\ \text{m}^2\)", False)],
            "explanation": r"\(7 \times 6 = 42\ \text{m}^2\). The trap 13 adds \(7+6\); 21 halves it. Use the perpendicular height (6), never the slanted side. Pro tip: when a figure gives both a slanted side and a perpendicular height, use the perpendicular height in \(b \times h\).",
        },
        {
            "text": r"For a parallelogram, which length is used as the height in \(A = b h\)?",
            "difficulty": 2,
            "choices": [("The perpendicular distance between the parallel sides", True), ("The length of the slanted side", False), ("The longest side", False), ("The diagonal", False)],
            "explanation": r"The height is the perpendicular (straight up-and-down) distance between the two parallel bases, not the slanted side. Using the tilted side overstates the area. Pro tip: look for the little right-angle mark -- the height is the dashed line that meets the base at \(90^\circ\).",
        },
        # --- Trapezoids ---
        {
            "text": r"A trapezoid has parallel sides \(6\) cm and \(10\) cm and height \(4\) cm. What is its area?",
            "difficulty": 2,
            "choices": [(r"\(32\ \text{cm}^2\)", True), (r"\(64\ \text{cm}^2\)", False), (r"\(40\ \text{cm}^2\)", False), (r"\(20\ \text{cm}^2\)", False)],
            "explanation": r"Average the two parallel sides, then multiply by the height: \(\tfrac{1}{2}(6+10)(4) = \tfrac{1}{2}(16)(4) = 32\ \text{cm}^2\). The trap 64 forgets the \(\tfrac{1}{2}\); 40 multiplies only one base by the height. You must use BOTH parallel sides. Pro tip: think 'average of the bases times height' -- \((6+10)/2 = 8\), then \(8 \times 4 = 32\).",
        },
        {
            "text": r"A trapezoid has parallel sides \(4\) cm and \(8\) cm and height \(5\) cm. What is its area?",
            "difficulty": 2,
            "choices": [(r"\(30\ \text{cm}^2\)", True), (r"\(60\ \text{cm}^2\)", False), (r"\(40\ \text{cm}^2\)", False), (r"\(17\ \text{cm}^2\)", False)],
            "explanation": r"\(\tfrac{1}{2}(4+8)(5) = \tfrac{1}{2}(12)(5) = 30\ \text{cm}^2\). The trap 60 drops the half; 40 uses only one base. Pro tip: a clean order is add the bases (12), halve (6), then times the height (30) -- small steps, fewer slips.",
        },
        {
            "text": r"A garden is a trapezoid with parallel edges \(8\) m and \(12\) m and depth \(5\) m. What is its area?",
            "difficulty": 2,
            "choices": [(r"\(50\ \text{m}^2\)", True), (r"\(100\ \text{m}^2\)", False), (r"\(60\ \text{m}^2\)", False), (r"\(25\ \text{m}^2\)", False)],
            "explanation": r"\(\tfrac{1}{2}(8+12)(5) = \tfrac{1}{2}(20)(5) = 50\ \text{m}^2\). The trap 100 forgets the half; 60 uses one edge only. Pro tip: a trapezoid always has two different parallel sides -- add them before anything else.",
        },
        {
            "text": r"In the trapezoid area formula \(A = \tfrac{1}{2}(b_1 + b_2)h\), what do you do first?",
            "difficulty": 2,
            "choices": [(r"Add the two parallel sides \(b_1 + b_2\)", True), ("Multiply the two sides together", False), ("Square the height", False), ("Subtract the sides", False)],
            "explanation": r"Follow the order of operations: add the two parallel bases first (inside the parentheses), then take half, then multiply by the height. Skipping the addition is the common error. Pro tip: \(\tfrac{1}{2}(b_1+b_2)h\) -- parentheses (add) before the half before the height.",
        },
        # --- Circles ---
        {
            "text": r"A circle has a radius of \(7\) cm. Using \(\pi \approx 3.14\), what is its area?",
            "difficulty": 2,
            "choices": [(r"\(\approx 153.9\ \text{cm}^2\)", True), (r"\(\approx 43.96\ \text{cm}^2\)", False), (r"\(\approx 21.98\ \text{cm}^2\)", False), (r"\(\approx 49\ \text{cm}^2\)", False)],
            "explanation": r"Area \(= \pi r^2 = 3.14 \times 7^2 = 3.14 \times 49 \approx 153.9\ \text{cm}^2\). The trap 43.96 uses the circumference (\(2\pi r\)) instead of area; 21.98 is \(\pi r\). You must SQUARE the radius. Pro tip: area uses \(\pi r^2\) (squared, square units); circumference uses \(2\pi r\). Square first, then times \(\pi\).",
        },
        {
            "text": r"A circle has a radius of \(5\) cm. Using \(\pi \approx 3.14\), what is its area?",
            "difficulty": 2,
            "choices": [(r"\(78.5\ \text{cm}^2\)", True), (r"\(31.4\ \text{cm}^2\)", False), (r"\(15.7\ \text{cm}^2\)", False), (r"\(25\ \text{cm}^2\)", False)],
            "explanation": r"\(3.14 \times 5^2 = 3.14 \times 25 = 78.5\ \text{cm}^2\). The trap 31.4 is the circumference (\(2\pi r\)); 15.7 is \(\pi r\). Pro tip: square the radius before multiplying by \(\pi\) -- \(5^2 = 25\), not \(5 \times 2\).",
        },
        {
            "text": r"A circle has a diameter of \(10\) cm. Using \(\pi \approx 3.14\), what is its area?",
            "difficulty": 3,
            "choices": [(r"\(78.5\ \text{cm}^2\)", True), (r"\(314\ \text{cm}^2\)", False), (r"\(31.4\ \text{cm}^2\)", False), (r"\(157\ \text{cm}^2\)", False)],
            "explanation": r"Halve the diameter first: \(r = 5\). Then \(A = 3.14 \times 25 = 78.5\ \text{cm}^2\). The trap 314 uses \(r = 10\) (forgot to halve the diameter); 31.4 is a circumference. Pro tip: when given a diameter, your FIRST step is always to halve it to get the radius.",
        },
        {
            "text": r"A circle has a radius of \(10\) m. Using \(\pi \approx 3.14\), what is its area?",
            "difficulty": 2,
            "choices": [(r"\(314\ \text{m}^2\)", True), (r"\(62.8\ \text{m}^2\)", False), (r"\(31.4\ \text{m}^2\)", False), (r"\(100\ \text{m}^2\)", False)],
            "explanation": r"\(3.14 \times 10^2 = 3.14 \times 100 = 314\ \text{m}^2\). The trap 62.8 is the circumference; 31.4 is half of it. Pro tip: \(10^2 = 100\) -- squaring 10 gives 100, a quick mental check that you squared (not doubled) the radius.",
        },
        {
            "text": r"A student finds a circle's area for radius \(7\) by computing \(3.14 \times 14\). What is the error?",
            "difficulty": 3,
            "choices": [(r"They doubled the radius instead of squaring it", True), ("They used the wrong value of pi", False), ("They used the diameter", False), ("Nothing is wrong", False)],
            "explanation": r"The student computed \(3.14 \times 14\), doubling the radius instead of squaring it. \(r^2\) means \(7 \times 7 = 49\), so the area is \(3.14 \times 49 \approx 153.9\). Pro tip: the exponent 2 means multiply the radius by ITSELF, never by 2.",
        },
        # --- Composite figures ---
        {
            "text": r"An L-shape splits into a \(10 \times 3\) rectangle and a \(6 \times 6\) rectangle. What is the total area?",
            "difficulty": 2,
            "choices": [(r"\(66\ \text{ft}^2\)", True), (r"\(96\ \text{ft}^2\)", False), (r"\(36\ \text{ft}^2\)", False), (r"\(60\ \text{ft}^2\)", False)],
            "explanation": r"Split into two rectangles: \(10 \times 3 = 30\) and \(6 \times 6 = 36\); add them: \(30 + 36 = 66\ \text{ft}^2\). The trap 36 forgets Rectangle A; 96 multiplies wrong pieces. Pro tip: break a composite into simple shapes, find each area, then add -- label each piece so you do not miss one.",
        },
        {
            "text": r"A \(10\) m by \(8\) m yard has a \(4\) m by \(3\) m shed removed. What area remains?",
            "difficulty": 2,
            "choices": [(r"\(68\ \text{m}^2\)", True), (r"\(92\ \text{m}^2\)", False), (r"\(80\ \text{m}^2\)", False), (r"\(56\ \text{m}^2\)", False)],
            "explanation": r"Find the big area, then subtract the hole: \((10 \times 8) - (4 \times 3) = 80 - 12 = 68\ \text{m}^2\). The trap 92 adds the shed instead of removing it; 80 forgets to remove it at all. Pro tip: a piece that is 'removed' or 'cut out' is subtracted, never added.",
        },
        {
            "text": r"A rectangle \(20\) by \(12\) has a \(5\) by \(4\) rectangle cut out of it. What is the remaining area?",
            "difficulty": 2,
            "choices": [(r"\(220\)", True), (r"\(240\)", False), (r"\(200\)", False), (r"\(260\)", False)],
            "explanation": r"\((20 \times 12) - (5 \times 4) = 240 - 20 = 220\) square units. The trap 240 forgets the cut-out; 260 adds it instead of subtracting. Pro tip: 'cut out', 'hole', or 'removed' all mean subtract that area from the whole.",
        },
        {
            "text": r"A figure is a \(6 \times 6\) square with a triangle (base \(6\), height \(4\)) on top. What is the total area?",
            "difficulty": 3,
            "choices": [(r"\(48\)", True), (r"\(60\)", False), (r"\(42\)", False), (r"\(36\)", False)],
            "explanation": r"Add the parts: square \(= 6^2 = 36\) and triangle \(= \tfrac{1}{2}(6)(4) = 12\); total \(= 36 + 12 = 48\). The trap 60 forgets the triangle's \(\tfrac{1}{2}\) (using 24); 36 forgets the triangle entirely. Pro tip: for a stacked figure, compute each shape with its OWN formula (square \(s^2\), triangle \(\tfrac{1}{2}bh\)), then add.",
        },
        {
            "text": r"To find the area of a shape with a hole cut out, you should:",
            "difficulty": 1,
            "choices": [("Subtract the hole's area from the whole shape's area", True), ("Add the hole's area", False), ("Multiply the two areas", False), ("Ignore the hole", False)],
            "explanation": r"A cut-out region is removed, so subtract its area from the total. Adding it would over-count the surface. Pro tip: decide for each region whether it is 'added on' or 'cut out' before doing any arithmetic.",
        },
        # --- Coordinate grid ---
        {
            "text": r"A rectangle has corners at \((1,1)\), \((6,1)\), \((6,4)\), and \((1,4)\). What is its area?",
            "difficulty": 2,
            "choices": [("15 square units", True), ("12 square units", False), ("20 square units", False), ("9 square units", False)],
            "explanation": r"Find side lengths by subtracting coordinates: width \(= 6-1 = 5\), height \(= 4-1 = 3\); area \(= 5 \times 3 = 15\). The trap 12 multiplies the larger coordinates (6 and 4) instead of the differences; 20 mis-subtracts. Pro tip: a side length is the DIFFERENCE of coordinates, not the larger coordinate.",
        },
        {
            "text": r"A rectangle has corners at \((2,2)\), \((9,2)\), \((9,6)\), and \((2,6)\). What is its area?",
            "difficulty": 2,
            "choices": [("28 square units", True), ("24 square units", False), ("11 square units", False), ("32 square units", False)],
            "explanation": r"Width \(= 9-2 = 7\), height \(= 6-2 = 4\); area \(= 7 \times 4 = 28\). The trap 11 adds \(7+4\) (that is half the perimeter); 24 subtracts wrong. Pro tip: subtract the x's for the width and the y's for the height, then multiply the two results.",
        },
        {
            "text": r"A triangle has a base from \((2,1)\) to \((10,1)\) and a top point at height \(y = 6\). What is its area?",
            "difficulty": 3,
            "choices": [("20 square units", True), ("40 square units", False), ("24 square units", False), ("13 square units", False)],
            "explanation": r"Base \(= 10-2 = 8\); height \(= 6-1 = 5\); \(A = \tfrac{1}{2}(8)(5) = 20\). The trap 40 forgets the \(\tfrac{1}{2}\); 13 just adds \(8+5\). Pro tip: on a grid, find the base and height by subtracting coordinates, then apply the normal \(\tfrac{1}{2}bh\) formula.",
        },
        # --- Missing side ---
        {
            "text": r"A rectangle has area \(48\ \text{cm}^2\) and width \(6\) cm. What is its length?",
            "difficulty": 2,
            "choices": [(r"\(8\) cm", True), (r"\(42\) cm", False), (r"\(288\) cm", False), (r"\(54\) cm", False)],
            "explanation": r"Reverse the area formula by dividing: \(l = A/w = 48/6 = 8\) cm. The trap 42 subtracts (\(48-6\)); 288 multiplies (\(48 \times 6\)). Pro tip: if you know the area and one side, DIVIDE to get the other side -- division undoes the multiplication in \(A = l \times w\).",
        },
        {
            "text": r"A square has area \(49\ \text{cm}^2\). What is the length of each side?",
            "difficulty": 2,
            "choices": [(r"\(7\) cm", True), (r"\(24.5\) cm", False), (r"\(12.25\) cm", False), (r"\(14\) cm", False)],
            "explanation": r"The side is the square root of the area: \(s = \sqrt{49} = 7\) cm. The trap 24.5 halves the area; 12.25 divides by 4 (that is a perimeter idea). Pro tip: square goes area-to-side by a square root -- \(\sqrt{49} = 7\) because \(7^2 = 49\).",
        },
        {
            "text": r"A triangle has area \(24\ \text{cm}^2\) and base \(8\) cm. What is its height?",
            "difficulty": 3,
            "choices": [(r"\(6\) cm", True), (r"\(3\) cm", False), (r"\(12\) cm", False), (r"\(16\) cm", False)],
            "explanation": r"Undo the \(\tfrac{1}{2}\) first: \(24 = \tfrac{1}{2}(8)h = 4h\), so \(h = 24/4 = 6\) cm. The trap 3 divides 24 by 8 without undoing the half; 12 forgets the half entirely. Pro tip: for a triangle, multiply the area by 2 (or note \(\tfrac{1}{2}b = 4\)) before dividing by the base.",
        },
        {
            "text": r"A rectangular rug must cover \(60\ \text{ft}^2\) in a room that is \(10\) ft long. How wide must it be?",
            "difficulty": 2,
            "choices": [(r"\(6\) ft", True), (r"\(50\) ft", False), (r"\(600\) ft", False), (r"\(70\) ft", False)],
            "explanation": r"Width \(= A/l = 60/10 = 6\) ft. The trap 50 subtracts (\(60-10\)); 600 multiplies. Pro tip: area divided by a known side gives the other side -- whenever the area is known and you need a length, divide.",
        },
        # --- Units & conversion ---
        {
            "text": r"How many square inches are in \(1\) square foot?",
            "difficulty": 2,
            "choices": [("144", True), ("12", False), ("24", False), ("100", False)],
            "explanation": r"A foot is 12 inches, so a 1-ft square is 12 in by 12 in: \(1\ \text{ft}^2 = 12 \times 12 = 144\ \text{in}^2\). The trap 12 converts as if it were a length, not an area. Pro tip: to convert SQUARE units, square the conversion factor (\(12 \to 144\)), not just use it once.",
        },
        {
            "text": r"How many square feet are in \(1\) square yard?",
            "difficulty": 2,
            "choices": [("9", True), ("3", False), ("6", False), ("12", False)],
            "explanation": r"A yard is 3 feet, so \(1\ \text{yd}^2 = 3 \times 3 = 9\ \text{ft}^2\). The trap 3 forgets to square the factor. Pro tip: square units convert by the SQUARE of the linear factor (\(3^2 = 9\)), never by the factor itself.",
        },
        {
            "text": r"A poster is \(2\) ft by \(3\) ft. What is its area in square inches?",
            "difficulty": 3,
            "choices": [("864", True), ("72", False), ("6", False), ("288", False)],
            "explanation": r"Area \(= 6\ \text{ft}^2\); convert: \(6 \times 144 = 864\ \text{in}^2\). The trap 72 multiplies by 12 (the linear factor) instead of 144; 6 forgets to convert at all. Pro tip: find the area in the given units first, THEN multiply by 144 to reach square inches.",
        },
        {
            "text": r"A \(12\) ft by \(9\) ft room is how many square yards?",
            "difficulty": 3,
            "choices": [("12", True), ("108", False), ("36", False), ("4", False)],
            "explanation": r"Area \(= 108\ \text{ft}^2\); divide by 9: \(108 / 9 = 12\ \text{yd}^2\). The trap 36 divides by 3 (the linear factor) instead of 9; 108 forgets to convert. Pro tip: carpet is sold by the square yard -- divide square feet by 9, not 3.",
        },
        # --- Real-world / cost ---
        {
            "text": r"A room is \(15\) ft by \(12\) ft. How many square feet of carpet are needed?",
            "difficulty": 1,
            "choices": [(r"\(180\ \text{ft}^2\)", True), (r"\(54\ \text{ft}^2\)", False), (r"\(27\ \text{ft}^2\)", False), (r"\(170\ \text{ft}^2\)", False)],
            "explanation": r"Carpet covers the floor, so use area: \(15 \times 12 = 180\ \text{ft}^2\). The trap 54 is the perimeter \(2(15+12)\); 27 is \(15+12\). Pro tip: 'how many square feet of carpet' is an area question -- multiply length by width.",
        },
        {
            "text": r"A wall is \(10\) ft by \(8\) ft with a \(3\) ft by \(7\) ft door that is not painted. What area gets painted?",
            "difficulty": 3,
            "choices": [(r"\(59\ \text{ft}^2\)", True), (r"\(80\ \text{ft}^2\)", False), (r"\(101\ \text{ft}^2\)", False), (r"\(21\ \text{ft}^2\)", False)],
            "explanation": r"Wall area minus the door: \((10 \times 8) - (3 \times 7) = 80 - 21 = 59\ \text{ft}^2\). The trap 80 forgets to remove the door; 101 adds the door instead of subtracting. Pro tip: openings like doors and windows are not painted -- subtract their area from the wall.",
        },
        {
            "text": r"Tile costs \(4\) dollars per square foot. How much does it cost to tile a \(50\ \text{ft}^2\) floor?",
            "difficulty": 2,
            "choices": [("200 dollars", True), ("54 dollars", False), ("12.50 dollars", False), ("100 dollars", False)],
            "explanation": r"The area (\(50\ \text{ft}^2\)) is given, so multiply by the price: \(50 \times 4 = 200\) dollars. The trap 54 adds (\(50+4\)); 12.50 divides. Pro tip: a cost question has two steps -- find the area, THEN multiply by the price per square unit.",
        },
        {
            "text": r"A garden bed is \(20\) ft by \(4\) ft. If one bag of soil covers \(16\ \text{ft}^2\), how many bags are needed?",
            "difficulty": 3,
            "choices": [("5 bags", True), ("4 bags", False), ("80 bags", False), ("8 bags", False)],
            "explanation": r"Area \(= 20 \times 4 = 80\ \text{ft}^2\); bags \(= 80 / 16 = 5\). The trap 80 stops at the area; 4 forgets a step. Pro tip: 'how many bags / cans / boxes' needs a final division of the total area by the coverage of one bag.",
        },
        # --- Concept / strategy ---
        {
            "text": r"Area is measured in which kind of units?",
            "difficulty": 1,
            "choices": [("Square units", True), ("Plain (linear) units", False), ("Cubic units", False), ("No units", False)],
            "explanation": r"Area covers a surface (two dimensions), so it uses square units like \(\text{cm}^2\) or \(\text{ft}^2\). Plain units are for length/perimeter; cubic units are for volume. Pro tip: the little \(^2\) on the unit is your reminder that area multiplies two lengths.",
        },
        {
            "text": r"Which measures the distance around a shape rather than the surface inside it?",
            "difficulty": 1,
            "choices": [("Perimeter", True), ("Area", False), ("Volume", False), ("Radius", False)],
            "explanation": r"Perimeter is the distance around the outside (plain units); area is the surface inside (square units). They answer different questions. Pro tip: 'fence / border / trim' = perimeter; 'carpet / paint / cover' = area.",
        },
        {
            "text": r"Which formula gives the area of a trapezoid?",
            "difficulty": 2,
            "choices": [(r"\(\tfrac{1}{2}(b_1 + b_2)h\)", True), (r"\(l \times w\)", False), (r"\(\pi r^2\)", False), (r"\(\tfrac{1}{2}bh\)", False)],
            "explanation": r"A trapezoid uses \(A = \tfrac{1}{2}(b_1 + b_2)h\) -- the average of the two parallel sides times the height. \(l \times w\) is a rectangle, \(\pi r^2\) a circle, \(\tfrac{1}{2}bh\) a triangle. Pro tip: a trapezoid is the shape with TWO parallel sides -- that is your cue to average them.",
        },
        {
            "text": r"A circular flower bed has radius \(3\) ft. Using \(\pi \approx 3.14\), about how much area does it cover?",
            "difficulty": 2,
            "choices": [(r"\(\approx 28.3\ \text{ft}^2\)", True), (r"\(\approx 18.8\ \text{ft}^2\)", False), (r"\(\approx 9.4\ \text{ft}^2\)", False), (r"\(\approx 9\ \text{ft}^2\)", False)],
            "explanation": r"Area \(= \pi r^2 = 3.14 \times 3^2 = 3.14 \times 9 \approx 28.3\ \text{ft}^2\). The trap 18.8 uses the circumference (\(2\pi r\)); 9.4 is \(\pi r\). Pro tip: a circular bed's surface is \(\pi r^2\) -- square the radius first, then multiply by 3.14.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Area Mastery course (multiple choice only)."

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

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
