"""
Seed a comprehensive GED Geometry course on coordinate geometry and distance.

This course covers the coordinate plane, plotting points, slope calculation,
the distance formula, and application to geometry problems on grids.
Includes detailed worked examples, real-world applications, and extensive practice.

Run:
    python manage.py seed_ged_coordinate_geometry
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Coordinate Geometry & Distance",
    "slug": "ged-coordinate-geometry-distance",
    "program": "GED",
    "subject": "math",
    "description": (
        "A comprehensive course on coordinate geometry for the GED. Students learn the "
        "coordinate plane, how to plot points, calculate slope, apply the distance formula, "
        "find midpoints, determine if lines are parallel or perpendicular, and solve "
        "geometric problems on grids. Includes many worked examples, real-world applications "
        "like navigation and construction, and step-by-step practice questions."
    ),
    "lessons": [
        (
            "1. The Coordinate Plane: Reading and Plotting Points",
            r"""
The **coordinate plane** is formed by two perpendicular number lines: the horizontal **x-axis** and the vertical **y-axis**. They intersect at the **origin** \((0, 0)\).

Every point has an **address**, written as an ordered pair \((x, y)\):
- The first number is the **x-coordinate** (horizontal position, left or right from the origin).
- The second number is the **y-coordinate** (vertical position, up or down from the origin).

[[figure:coordinate_plane|The coordinate plane divided into four quadrants with labeled axes.]]

**The Four Quadrants:**
- Quadrant I: \(x > 0, y > 0\) (top-right; both positive)
- Quadrant II: \(x < 0, y > 0\) (top-left; x negative, y positive)
- Quadrant III: \(x < 0, y < 0\) (bottom-left; both negative)
- Quadrant IV: \(x > 0, y < 0\) (bottom-right; x positive, y negative)

**Plotting a point:** To plot \((3, 4)\):
1. Start at the origin \((0, 0)\).
2. Move right 3 units (positive x-direction).
3. Move up 4 units (positive y-direction).
4. Mark the point.

**Reading a point:** If a point is 2 units left and 5 units up from the origin, its coordinates are \((-2, 5)\).

Common mistake: reversing the order. Always write x-coordinate first, then y-coordinate. The point \((2, 3)\) is NOT the same as \((3, 2)\).

💡 Tip: A helpful way to remember is "x comes before y alphabetically," so plot horizontally first, then vertically.

[[check:What are the coordinates of the point 3 units right and 2 units down from the origin?|3,-2;;(3,-2)|Right is positive x, down is negative y.]]
            """,
        ),
        (
            "2. Distance Formula: How Far Apart Are Two Points?",
            r"""
The **distance** between two points measures the straight-line length connecting them. Use the **distance formula**:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

This formula comes from the Pythagorean theorem: the two points form a right triangle, and the distance is the hypotenuse.

**Worked Example 1:** Find the distance between \((1, 2)\) and \((4, 6)\).

\[
d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
\]

**Worked Example 2:** Find the distance between \((-1, 3)\) and \((2, -1)\).

\[
d = \sqrt{(2-(-1))^2 + (-1-3)^2} = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = \sqrt{25} = 5
\]

Notice: negative numbers become positive when squared, so the signs do not matter.

**Real-world context:** A surveyor marks two property corners at \((10, 20)\) and \((34, 56)\) on a grid (in feet). The distance is:
\[
d = \sqrt{(34-10)^2 + (56-20)^2} = \sqrt{24^2 + 36^2} = \sqrt{576 + 1296} = \sqrt{1872} \approx 43.3 \text{ feet}
\]

Common mistake: forgetting to square root. The value under the radical is not the distance by itself.

💡 Tip: If the two points form a 3-4-5 or 5-12-13 right triangle, the distance is that Pythagorean triple — no calculator needed.

[[check:Find the distance between \((0, 0)\) and \((3, 4)\).|5|Use \(\sqrt{3^2+4^2}=\sqrt{9+16}=\sqrt{25}=5\).]]
            """,
        ),
        (
            "3. Slope: How Steep Is a Line?",
            r"""
**Slope** measures the steepness and direction of a line. It is the ratio of **rise** (vertical change) to **run** (horizontal change):

\[
m = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1}
\]

**Interpreting slope:**
- Positive slope: line rises left to right (uphill).
- Negative slope: line falls left to right (downhill).
- Zero slope: horizontal line (flat).
- Undefined slope: vertical line (straight up).

**Worked Example 1:** Find the slope through \((1, 2)\) and \((4, 8)\).

\[
m = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2
\]

The line rises 6 units for every 3 units to the right, or 2 units for every 1 unit to the right.

**Worked Example 2:** Find the slope through \((2, 5)\) and \((5, 2)\).

\[
m = \frac{2 - 5}{5 - 2} = \frac{-3}{3} = -1
\]

The line falls 1 unit for every 1 unit to the right (45-degree downward angle).

**Parallel and perpendicular lines:**
- **Parallel lines** have the same slope.
- **Perpendicular lines** have slopes that are negative reciprocals. If one line has slope \(2\), a perpendicular line has slope \(-\frac{1}{2}\).

[[figure:slope_types|Illustration of positive, negative, zero, and undefined slopes.]]

Common mistake: using \(\frac{y_1 - y_2}{x_1 - x_2}\) instead of \(\frac{y_2 - y_1}{x_2 - x_1}\). The order matters; be consistent.

💡 Tip: Always subtract in the same order: "second point minus first point" for both rise and run.

[[check:Find the slope through \((0, 0)\) and \((2, 8)\).|4|Slope is \(\frac{8-0}{2-0}=\frac{8}{2}=4\).]]
            """,
        ),
        (
            "4. Slope-Intercept Form: Writing and Graphing Line Equations",
            r"""
The **slope-intercept form** of a line is:

\[
y = mx + b
\]

where:
- \(m\) is the **slope**.
- \(b\) is the **y-intercept** (the y-value when \(x = 0\)).

**Graphing from slope-intercept form:**

To graph \(y = 2x + 3\):
1. Plot the y-intercept: \(b = 3\), so mark the point \((0, 3)\).
2. Use the slope: \(m = 2 = \frac{2}{1}\), so from \((0, 3)\), go up 2 and right 1 to reach \((1, 5)\).
3. Repeat using the slope to find more points: up 2, right 1 → \((2, 7)\).
4. Draw the line through all points.

[[figure:slope_intercept_graph|A line with y-intercept at (0,3) and slope 2, showing rise-over-run arrows.]]

**Finding the equation from two points:**

If a line passes through \((1, 3)\) and \((3, 7)\):
1. Find the slope: \(m = \frac{7-3}{3-1} = \frac{4}{2} = 2\).
2. Use the point-slope form or substitute into \(y = mx + b\):
   \[
   3 = 2(1) + b \Rightarrow b = 1
   \]
3. The equation is \(y = 2x + 1\).

**Real-world context:** A cell phone plan charges \(\$30\) per month plus \(\$0.05\) per minute. The cost equation is \(C = 0.05m + 30\), where the y-intercept is \(30\) (base cost) and the slope is \(0.05\) (cost per minute).

Common mistake: confusing which point to use when finding \(b\). Any point on the line works; always verify by substituting.

💡 Tip: The y-intercept is easy: set \(x = 0\) in the original equation. The x-intercept (where the line crosses the x-axis) requires setting \(y = 0\).

[[check:What is the y-intercept of the line \(y = -3x + 7\)?|7|The y-intercept is the value of \(b\).]]
            """,
        ),
        (
            "5. Midpoint and Special Points",
            r"""
The **midpoint** between two points is the point exactly halfway between them. Use the **midpoint formula**:

\[
M = \left( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} \right)
\]

Simply average the x-coordinates and average the y-coordinates.

**Worked Example 1:** Find the midpoint between \((2, 4)\) and \((8, 10)\).

\[
M = \left( \frac{2 + 8}{2}, \frac{4 + 10}{2} \right) = \left( \frac{10}{2}, \frac{14}{2} \right) = (5, 7)
\]

Check: The distance from \((2, 4)\) to \((5, 7)\) is \(\sqrt{3^2 + 3^2} = \sqrt{18} \approx 4.24\), and the distance from \((5, 7)\) to \((8, 10)\) is also \(\sqrt{3^2 + 3^2} \approx 4.24\). ✓

**Worked Example 2:** Find the midpoint between \((-3, 5)\) and \((1, -3)\).

\[
M = \left( \frac{-3 + 1}{2}, \frac{5 + (-3)}{2} \right) = \left( \frac{-2}{2}, \frac{2}{2} \right) = (-1, 1)
\]

**Real-world context:** Two cities are located at \((10, 20)\) and \((50, 80)\) on a coordinate map. A supply depot should be built at the midpoint:
\[
M = \left( \frac{10 + 50}{2}, \frac{20 + 80}{2} \right) = (30, 50)
\]

Common mistake: forgetting to divide by 2. The midpoint is not \((x_1 + x_2, y_1 + y_2)\).

💡 Tip: The midpoint is useful for finding centers of circles, balanced points in designs, and equal-distance locations.

[[check:Find the midpoint between \((0, 0)\) and \((6, 8)\).|3,4;;(3,4)|Average each coordinate.]]
            """,
        ),
        (
            "6. Identifying Geometric Figures on a Coordinate Grid",
            r"""
The coordinate plane is perfect for analyzing shapes: triangles, rectangles, circles, and more. Use distance and slope formulas to verify properties.

**Determining if a triangle is a right triangle:**

Check if any two sides are perpendicular by verifying that their slopes multiply to \(-1\) (negative reciprocals).

Example: Triangle with vertices \(A(0, 0)\), \(B(3, 0)\), \(C(0, 4)\).
- Slope of AB: \(\frac{0-0}{3-0} = 0\) (horizontal).
- Slope of AC: \(\frac{4-0}{0-0}\) is undefined (vertical).
- A horizontal and vertical line are perpendicular, so angle A is a right angle. ✓

**Verifying a rectangle:**

A rectangle has four right angles and opposite sides equal. Check slopes (all perpendicular) and distances (opposite sides equal).

**Finding if points are collinear:**

Three points are **collinear** (on the same line) if the slope between point 1 and point 2 equals the slope between point 2 and point 3.

Example: Are \((1, 2)\), \((2, 4)\), and \((3, 6)\) collinear?
- Slope from \((1, 2)\) to \((2, 4)\): \(\frac{4-2}{2-1} = 2\).
- Slope from \((2, 4)\) to \((3, 6)\): \(\frac{6-4}{3-2} = 2\). ✓
They are collinear (on the line \(y = 2x\)).

**Real-world context:** An architect must verify that four corner points of a proposed building form a rectangle. Using the coordinate grid, they calculate distances and slopes to confirm.

Common mistake: using only distance to verify a rectangle. Two shapes can have equal opposite sides but not be rectangles; you must also check angles.

💡 Tip: Always use multiple properties (distance, slope, angle) to verify geometric shapes.

[[check:If two lines have slopes \(2\) and \(-\frac{1}{2}\), are they perpendicular?|yes;;true|Slopes are negative reciprocals: \(2 \times (-1/2) = -1\).]]
            """,
        ),
        (
            "7. Transformations: Translations, Reflections, and Rotations",
            r"""
**Transformations** move or flip figures on the coordinate plane without changing their size or shape.

**Translation (Slide):**

A translation shifts every point the same distance in the same direction. If a point \((x, y)\) is translated by vector \((a, b)\), it moves to \((x+a, y+b)\).

Example: Translate triangle with vertices \((1, 1)\), \((3, 1)\), \((2, 3)\) by \((2, 3)\).
- \((1, 1) \to (1+2, 1+3) = (3, 4)\)
- \((3, 1) \to (3+2, 1+3) = (5, 4)\)
- \((2, 3) \to (2+2, 3+3) = (4, 6)\)

The triangle is congruent (same size and shape) after translation.

**Reflection (Flip):**

A reflection flips a figure across a line (usually the x-axis, y-axis, or the line \(y = x\)).

Reflecting across the x-axis: \((x, y) \to (x, -y)\).
Reflecting across the y-axis: \((x, y) \to (-x, y)\).
Reflecting across the line \(y = x\): \((x, y) \to (y, x)\).

Example: Reflect the point \((3, 4)\) across the x-axis: \((3, 4) \to (3, -4)\).

**Rotation (Turn):**

A rotation turns a figure around a center point (usually the origin) by an angle. Common rotations are 90°, 180°, and 270°.

Rotating 90° counterclockwise around the origin: \((x, y) \to (-y, x)\).
Rotating 180° around the origin: \((x, y) \to (-x, -y)\).
Rotating 270° counterclockwise (or 90° clockwise) around the origin: \((x, y) \to (y, -x)\).

Example: Rotate \((3, 0)\) by 90° counterclockwise: \((3, 0) \to (0, 3)\).

[[figure:transformations|Grid showing translation (arrow pointing right), reflection (mirror image), and rotation (point swinging around center).]]

**Real-world context:** A landscape architect designs a garden. They translate a flower bed, reflect a path design across a centerline, and rotate a patio for sun exposure.

Common mistake: forgetting the order of operations in transformations. Apply the rule exactly: for rotation, \((x, y) \to (-y, x)\) is different from \((x, y) \to (y, -x)\).

💡 Tip: Use graph paper to visualize transformations. Draw the original figure, apply the rule step-by-step, and mark the new position.

[[check:Reflect the point \((2, 5)\) across the y-axis.|-2,5;;(-2,5)|Reflecting across the y-axis: \((x, y) \to (-x, y)\).]]
            """,
        ),
        (
            "8. Test-Taking Strategies for Coordinate Geometry",
            r"""
Coordinate geometry questions often feature grids and require calculation. Master these strategies:

**Strategy 1 - Always label clearly.** Mark given points, identify what you're solving for, and show intermediate steps. One misread coordinate ruins the entire answer.

**Strategy 2 - Use the distance formula systematically.** Write it out: \(d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\). Substitute carefully, squaring each term.

**Strategy 3 - Check for Pythagorean triples.** Common triples save time:
- \(3^2 + 4^2 = 5^2\) (3-4-5 triangle)
- \(5^2 + 12^2 = 13^2\) (5-12-13 triangle)
- \(8^2 + 15^2 = 17^2\) (8-15-17 triangle)

If you see these numbers in coordinates, you can skip the square root.

**Strategy 4 - Draw or visualize the coordinate plane.** Even a rough sketch prevents careless sign errors. Mark the quadrant where your point should be.

**Strategy 5 - Estimate before calculating.** If two points are roughly 5 units apart horizontally and 3 units apart vertically, the distance is about \(\sqrt{25+9}=\sqrt{34} \approx 6\). Does your calculated answer make sense?

**Strategy 6 - Verify parallel and perpendicular lines.** Two slopes multiply to \(-1\) if perpendicular:
\[
m_1 \times m_2 = -1 \Rightarrow \text{perpendicular}
\]
If slopes are equal, lines are parallel.

**Strategy 7 - Use properties of special points.** The midpoint halves the distance. If you know the distance between two points and the location of one endpoint, you can find the other.

**Common pitfalls to avoid:**
- Forgetting the order \((x, y)\) in ordered pairs.
- Using \((y_1 - y_2)\) instead of \((y_2 - y_1)\) — consistent order matters for slope sign.
- Miscalculating \(\sqrt{25}\) as 5 but forgetting that \((-5)^2 = 25\) too (consider context).
- Confusing the y-intercept with the slope.

[[check:Two points are 12 units apart horizontally and 9 units apart vertically. Is the straight-line distance closer to 15, 20, or 25?|15|Distance is \(\sqrt{12^2+9^2}=\sqrt{144+81}=\sqrt{225}=15\) (a 9-12-15 Pythagorean triple, scaled from 3-4-5).]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"What are the coordinates of a point that is 4 units right and 3 units up from the origin?",
            "difficulty": 1,
            "choices": [(r"\((4, 3)\)", True), (r"\((3, 4)\)", False), (r"\((-4, 3)\)", False), (r"\((4, -3)\)", False)],
            "explanation": r"Right is positive x, up is positive y. The point is \((4, 3)\).",
        },
        {
            "text": r"In which quadrant is the point \((-2, 5)\) located?",
            "difficulty": 1,
            "choices": [("Quadrant II", True), ("Quadrant I", False), ("Quadrant III", False), ("Quadrant IV", False)],
            "explanation": r"Quadrant II has \(x < 0\) and \(y > 0\). The point \((-2, 5)\) has negative x and positive y.",
        },
        {
            "text": r"Find the distance between \((0, 0)\) and \((3, 4)\).",
            "difficulty": 1,
            "choices": [("5", True), ("7", False), ("3.5", False), ("4.5", False)],
            "explanation": r"\(d = \sqrt{(3-0)^2 + (4-0)^2} = \sqrt{9 + 16} = \sqrt{25} = 5\). This is a 3-4-5 Pythagorean triple.",
        },
        {
            "text": r"Find the distance between \((1, 2)\) and \((4, 6)\).",
            "difficulty": 2,
            "choices": [("5", True), ("6", False), ("7", False), ("4", False)],
            "explanation": r"\(d = \sqrt{(4-1)^2 + (6-2)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\).",
        },
        {
            "text": r"What is the slope of the line through \((0, 0)\) and \((2, 8)\)?",
            "difficulty": 1,
            "choices": [("4", True), ("2", False), ("8", False), ("0.25", False)],
            "explanation": r"\(m = \frac{8-0}{2-0} = \frac{8}{2} = 4\).",
        },
        {
            "text": r"Find the slope through \((1, 3)\) and \((4, 9)\).",
            "difficulty": 1,
            "choices": [("2", True), ("3", False), ("1.5", False), ("4", False)],
            "explanation": r"\(m = \frac{9-3}{4-1} = \frac{6}{3} = 2\).",
        },
        {
            "text": r"What is the slope of a line perpendicular to a line with slope \(3\)?",
            "difficulty": 2,
            "choices": [(r"\(-\frac{1}{3}\)", True), (r"\(\frac{1}{3}\)", False), ("3", False), ("-3", False)],
            "explanation": r"Perpendicular slopes are negative reciprocals: \(3 \times (-1/3) = -1\).",
        },
        {
            "text": r"What is the y-intercept of the line \(y = 2x + 5\)?",
            "difficulty": 1,
            "choices": [("5", True), ("2", False), ("0", False), ("-5", False)],
            "explanation": r"In \(y = mx + b\), the y-intercept is \(b = 5\).",
        },
        {
            "text": r"Find the midpoint between \((0, 0)\) and \((6, 8)\).",
            "difficulty": 1,
            "choices": [(r"\((3, 4)\)", True), (r"\((2, 4)\)", False), (r"\((3, 3)\)", False), (r"\((4, 4)\)", False)],
            "explanation": r"\(M = \left(\frac{0+6}{2}, \frac{0+8}{2}\right) = (3, 4)\).",
        },
        {
            "text": r"Find the midpoint between \((2, 5)\) and \((8, 11)\).",
            "difficulty": 1,
            "choices": [(r"\((5, 8)\)", True), (r"\((4, 8)\)", False), (r"\((6, 8)\)", False), (r"\((5, 7)\)", False)],
            "explanation": r"\(M = \left(\frac{2+8}{2}, \frac{5+11}{2}\right) = (5, 8)\).",
        },
        {
            "text": r"A line passes through \((1, 2)\) and \((3, 6)\). What is the slope?",
            "difficulty": 2,
            "choices": [("2", True), ("1", False), ("3", False), ("0.5", False)],
            "explanation": r"\(m = \frac{6-2}{3-1} = \frac{4}{2} = 2\).",
        },
        {
            "text": r"Find the distance between \((-1, 1)\) and \((2, 5)\).",
            "difficulty": 2,
            "choices": [("5", True), ("4", False), ("6", False), ("3", False)],
            "explanation": r"\(d = \sqrt{(2-(-1))^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5\).",
        },
        {
            "text": r"If a line has slope \(-2\) and y-intercept \(3\), what is the equation?",
            "difficulty": 1,
            "choices": [(r"\(y = -2x + 3\)", True), (r"\(y = 2x + 3\)", False), (r"\(y = -2x - 3\)", False), (r"\(y = x + 3\)", False)],
            "explanation": r"Slope-intercept form: \(y = mx + b\) where \(m = -2\) and \(b = 3\).",
        },
        {
            "text": r"Are the lines \(y = 3x + 1\) and \(y = 3x - 4\) parallel?",
            "difficulty": 1,
            "choices": [("Yes", True), ("No", False), ("Cannot be determined", False), ("They are the same line", False)],
            "explanation": r"Parallel lines have the same slope. Both lines have slope \(3\), so they are parallel.",
        },
        {
            "text": r"Are the lines with slopes \(2\) and \(-\frac{1}{2}\) perpendicular?",
            "difficulty": 2,
            "choices": [("Yes", True), ("No", False), ("Only if they intersect", False), ("Cannot be determined", False)],
            "explanation": r"Perpendicular slopes multiply to \(-1\): \(2 \times (-1/2) = -1\). ✓",
        },
        {
            "text": r"Reflect the point \((3, 4)\) across the x-axis.",
            "difficulty": 1,
            "choices": [(r"\((3, -4)\)", True), (r"\((-3, 4)\)", False), (r"\((4, 3)\)", False), (r"\((-3, -4)\)", False)],
            "explanation": r"Reflecting across the x-axis: \((x, y) \to (x, -y)\), so \((3, 4) \to (3, -4)\).",
        },
        {
            "text": r"Reflect the point \((2, 5)\) across the y-axis.",
            "difficulty": 1,
            "choices": [(r"\((-2, 5)\)", True), (r"\((2, -5)\)", False), (r"\((5, 2)\)", False), (r"\((-2, -5)\)", False)],
            "explanation": r"Reflecting across the y-axis: \((x, y) \to (-x, y)\), so \((2, 5) \to (-2, 5)\).",
        },
        {
            "text": r"Rotate the point \((4, 0)\) by 90° counterclockwise around the origin.",
            "difficulty": 2,
            "choices": [(r"\((0, 4)\)", True), (r"\((4, 4)\)", False), (r"\((-4, 0)\)", False), (r"\((0, -4)\)", False)],
            "explanation": r"90° counterclockwise rotation: \((x, y) \to (-y, x)\), so \((4, 0) \to (0, 4)\).",
        },
        {
            "text": r"Find the distance between \((0, 5)\) and \((12, 0)\).",
            "difficulty": 2,
            "choices": [("13", True), ("12", False), ("17", False), ("10", False)],
            "explanation": r"\(d = \sqrt{(12-0)^2 + (0-5)^2} = \sqrt{144 + 25} = \sqrt{169} = 13\). This is a 5-12-13 triple.",
        },
        {
            "text": r"What is the slope of the line \(y = -\frac{1}{2}x + 7\)?",
            "difficulty": 1,
            "choices": [(r"\(-\frac{1}{2}\)", True), (r"\(\frac{1}{2}\)", False), ("7", False), ("-7", False)],
            "explanation": r"In \(y = mx + b\), the slope is \(m = -\frac{1}{2}\).",
        },
        {
            "text": r"Are the points \((0, 0)\), \((1, 2)\), and \((2, 4)\) collinear?",
            "difficulty": 2,
            "choices": [("Yes", True), ("No", False), ("Only if ordered differently", False), ("Cannot be determined", False)],
            "explanation": r"Slope from \((0,0)\) to \((1,2)\) is \(\frac{2}{1}=2\). Slope from \((1,2)\) to \((2,4)\) is \(\frac{2}{1}=2\). Equal slopes mean collinear.",
        },
        {
            "text": r"Translate the point \((2, 3)\) by the vector \((5, -2)\).",
            "difficulty": 2,
            "choices": [(r"\((7, 1)\)", True), (r"\((3, 5)\)", False), (r"\((7, 5)\)", False), (r"\((3, 1)\)", False)],
            "explanation": r"Translation: \((x, y) + (a, b) = (x+a, y+b)\). So \((2, 3) + (5, -2) = (7, 1)\).",
        },
        {
            "text": r"Find the distance between \((2, 1)\) and \((5, 5)\).",
            "difficulty": 2,
            "choices": [("5", True), ("4", False), ("6", False), ("7", False)],
            "explanation": r"\(d = \sqrt{(5-2)^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = \sqrt{9+16} = 5\).",
        },
        {
            "text": r"What is the slope of a line parallel to the line \(y = -3x + 2\)?",
            "difficulty": 1,
            "choices": [("-3", True), ("3", False), ("2", False), (r"\(-\frac{1}{3}\)", False)],
            "explanation": r"Parallel lines have equal slopes. The slope is \(-3\).",
        },
        {
            "text": r"A line has slope \(4\) and passes through \((1, 2)\). What is the y-intercept?",
            "difficulty": 2,
            "choices": [("-2", True), ("4", False), ("6", False), ("-4", False)],
            "explanation": r"Using \(y = mx + b\): \(2 = 4(1) + b \Rightarrow b = 2 - 4 = -2\).",
        },
        {
            "text": r"Find the midpoint between \((-2, 3)\) and \((4, -1)\).",
            "difficulty": 2,
            "choices": [(r"\((1, 1)\)", True), (r"\((2, 1)\)", False), (r"\((1, 2)\)", False), (r"\((0, 1)\)", False)],
            "explanation": r"\(M = \left(\frac{-2+4}{2}, \frac{3+(-1)}{2}\right) = (1, 1)\).",
        },
        {
            "text": r"What is the y-intercept of a line passing through \((0, -5)\)?",
            "difficulty": 1,
            "choices": [("-5", True), ("0", False), ("5", False), ("Cannot be determined", False)],
            "explanation": r"The y-intercept is the y-value when \(x = 0\). The point \((0, -5)\) lies on the y-axis, so \(b = -5\).",
        },
        {
            "text": r"Rotate the point \((1, 0)\) by 180° around the origin.",
            "difficulty": 2,
            "choices": [(r"\((-1, 0)\)", True), (r"\((1, 0)\)", False), (r"\((0, 1)\)", False), (r"\((0, -1)\)", False)],
            "explanation": r"180° rotation: \((x, y) \to (-x, -y)\), so \((1, 0) \to (-1, 0)\).",
        },
        {
            "text": r"Which points form a right angle with the origin: \(A(3, 0)\), \(B(0, 4)\), \(C(3, 4)\)?",
            "difficulty": 2,
            "choices": [("A, B, and O form a right angle", True), ("B, C, and O", False), ("A, C, and O", False), ("No right angle exists", False)],
            "explanation": r"The line from O to A is horizontal (slope 0). The line from O to B is vertical (undefined slope). Horizontal and vertical are perpendicular.",
        },
        {
            "text": r"Find the distance between \((-3, 0)\) and \((0, 4)\).",
            "difficulty": 2,
            "choices": [("5", True), ("7", False), ("4", False), ("6", False)],
            "explanation": r"\(d = \sqrt{(0-(-3))^2 + (4-0)^2} = \sqrt{3^2 + 4^2} = 5\). (3-4-5 triple)",
        },
        {
            "text": r"A line has undefined slope. What can you conclude?",
            "difficulty": 1,
            "choices": [("The line is vertical", True), ("The line is horizontal", False), ("The line is diagonal", False), ("The line passes through the origin", False)],
            "explanation": r"Undefined slope occurs when the denominator (change in x) is zero, meaning the line is vertical.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Coordinate Geometry & Distance course."

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
