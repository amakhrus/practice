"""
Seed a GED Geometry course on the PYTHAGOREAN THEOREM and COORDINATE GEOMETRY.

Designed so that every multiple-choice explanation teaches the underlying idea
(method, why the tempting wrong answer is wrong) and ends with a Pro tip, so a
student who missed a question because of a knowledge gap can learn from it.

12 lessons, ~46 MCQs, labeled diagrams, interactive self-checks. MCQ only.

Run:
    python manage.py seed_ged_pythagorean
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Pythagorean Theorem & Coordinate Geometry",
    "slug": "ged-geometry-pythagorean-coordinate",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep GED Geometry course that connects right triangles to the coordinate plane. "
        "Students master the Pythagorean Theorem -- finding the hypotenuse, finding a missing leg, "
        "and using Pythagorean triples -- then apply the same idea on the grid through the distance "
        "formula, midpoint formula, and slope. Every lesson has a labeled diagram and an interactive "
        "self-check, and every practice question comes with a full teaching explanation and a Pro tip, "
        "so wrong answers turn into learning."
    ),
    "lessons": [
        (
            "1. Right Triangles: Legs and Hypotenuse",
            r"""
Everything in this course depends on the **right triangle** -- a triangle with one \(90^\circ\) angle (a square corner).

[[figure:pythagorean_triangle|The two legs form the right angle; the hypotenuse is opposite it.]]

The three sides have names:
- The two sides that form the right angle are the **legs**, usually called \(a\) and \(b\).
- The side **opposite** the right angle is the **hypotenuse**, called \(c\). It is always the **longest** side.

Spotting the hypotenuse correctly is the single most important first step. Look for the right-angle mark (the small square); the side that does **not** touch that corner is the hypotenuse.

Case study - a ramp leaning against a step forms a right triangle: the ground and the step are the legs, and the ramp itself is the hypotenuse.

Common mistake: calling any long side the hypotenuse. The hypotenuse is specifically the side across from the right angle.

[[check:In a right triangle, which side is the hypotenuse?|the side opposite the right angle;;opposite the right angle;;the longest side|It is the longest side, directly across from the 90 degree angle.]]
            """,
        ),
        (
            "2. The Pythagorean Theorem: a² + b² = c²",
            r"""
The **Pythagorean Theorem** says that in any right triangle, the squares of the two legs add up to the square of the hypotenuse:
\[
a^2 + b^2 = c^2.
\]

[[figure:right_triangle_345|The square on each leg (9 and 16) adds up to the square on the hypotenuse (25).]]

Read it as areas: the square built on leg \(a\) plus the square built on leg \(b\) exactly equals the square built on the hypotenuse \(c\). For the famous 3-4-5 triangle:
\[
3^2 + 4^2 = 9 + 16 = 25 = 5^2. \checkmark
\]

This relationship is **only** true for right triangles. If there is no right angle, the theorem does not apply.

Case study - checking a square corner: builders measure 3 ft and 4 ft along two walls; if the diagonal is exactly 5 ft, the corner is a perfect right angle.

Common mistake: adding the legs before squaring. \(3 + 4 = 7\) is wrong; you must square **first** (\(9 + 16\)), then take the square root.

[[check:For a right triangle, fill in: a² + b² = ?|c^2;;c squared;;c2|The squares of the legs add to the square of the hypotenuse.]]
            """,
        ),
        (
            "3. Finding the Hypotenuse",
            r"""
When you know both legs and want the hypotenuse, solve \(a^2 + b^2 = c^2\) for \(c\) by taking a square root:
\[
c = \sqrt{a^2 + b^2}.
\]

The three steps:
- **Square** each leg.
- **Add** the two results.
- Take the **square root** of the total.

Worked example: legs 6 and 8.
\[
c = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10.
\]

Sometimes the answer is not a whole number. Legs 2 and 3 give \(c = \sqrt{4 + 9} = \sqrt{13} \approx 3.6\). That is a perfectly good answer -- leave it as \(\sqrt{13}\) or round if the question asks.

Case study - a TV's size is the diagonal of the screen. A screen 36 in wide and 27 in tall has a diagonal of \(\sqrt{36^2 + 27^2} = \sqrt{1296 + 729} = \sqrt{2025} = 45\) inches.

Common mistake: stopping at \(a^2 + b^2\) and forgetting the square root. That gives \(c^2\), not \(c\).

[[check:A right triangle has legs 6 and 8. What is the hypotenuse?|10;;10 units|Compute √(6² + 8²) = √(36+64) = √100.]]
            """,
        ),
        (
            "4. Finding a Missing Leg",
            r"""
When you know the **hypotenuse** and **one leg**, you find the other leg by **subtracting** before the square root. Rearrange \(a^2 + b^2 = c^2\):
\[
a = \sqrt{c^2 - b^2}.
\]

The key difference: finding the hypotenuse **adds**, finding a leg **subtracts**. Always identify the hypotenuse first -- it is the one across from the right angle (and the largest number given).

Worked example: hypotenuse 13, one leg 5.
\[
a = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12.
\]

Worked example: a 10 ft ladder leans against a wall, with its base 6 ft from the wall. How high up the wall does it reach?
\[
\sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8 \text{ ft}.
\]

Case study - the ladder problem above is one of the most common GED setups: the ladder is the hypotenuse, the ground distance and the wall height are the legs.

Common mistake: adding when you should subtract. If a side given is the hypotenuse, you must subtract the leg's square, not add.

[[check:A right triangle has hypotenuse 13 and one leg 5. What is the other leg?|12;;12 units|Subtract: √(13² − 5²) = √(169−25) = √144.]]
            """,
        ),
        (
            "5. Pythagorean Triples: Useful Shortcuts",
            r"""
A **Pythagorean triple** is a set of three whole numbers that fit \(a^2 + b^2 = c^2\). Memorizing a few lets you answer some questions instantly, with no square roots.

The most common triples:
- **3, 4, 5**
- **5, 12, 13**
- **8, 15, 17**
- **7, 24, 25**

Any **multiple** of a triple is also a triple. Doubling 3-4-5 gives **6, 8, 10**; tripling it gives **9, 12, 15**.

Worked example: a right triangle has legs 9 and 12. Recognize \(9, 12, 15\) as \(3\times(3,4,5)\), so the hypotenuse is **15** -- no calculation needed.

Case study - on a timed test, spotting a triple saves precious seconds: legs 5 and 12 instantly give a hypotenuse of 13.

Common mistake: assuming every right triangle is a triple. Many are not (like legs 2 and 3). Triples are a shortcut to recognize, not a rule to force.

[[check:A right triangle has legs 9 and 12. What is the hypotenuse?|15;;15 units|This is 3 times the 3-4-5 triple, so the hypotenuse is 3 times 5.]]
            """,
        ),
        (
            "6. Real-World Pythagorean Problems",
            r"""
Most GED Pythagorean questions are word problems. The skill is drawing (or imagining) the right triangle and labeling the sides.

A reliable routine:
- **Sketch** the situation and mark the right angle.
- Label the two legs and the hypotenuse (the slanted or longest distance).
- Decide: are you finding the hypotenuse (**add**) or a leg (**subtract**)?

Common setups:
- A **ladder** against a wall: ladder = hypotenuse; ground distance and wall height = legs.
- The **diagonal** of a rectangle, room, or screen: the diagonal = hypotenuse; length and width = legs.
- A **ramp**: the slope = hypotenuse; the run and rise = legs.
- **Distance** traveled (go east, then north): the straight-line distance = hypotenuse.

Worked example: a person walks 9 km east, then 12 km north. Straight-line distance from start:
\[
\sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15 \text{ km}.
\]

Common mistake: not identifying which side is the hypotenuse before computing. Always find the right angle first.

[[check:A rectangle is 9 m long and 12 m wide. What is the length of its diagonal?|15;;15 m|The diagonal is the hypotenuse: √(9² + 12²) = √225.]]
            """,
        ),
        (
            "7. The Coordinate Plane: Points and Quadrants",
            r"""
The **coordinate plane** is a grid made by a horizontal **x-axis** and a vertical **y-axis** crossing at the **origin** \((0, 0)\). Every point has an address \((x, y)\): move right/left \(x\) first, then up/down \(y\).

[[figure:coordinate_quadrants|Read across (x) first, then up (y). The axes split the plane into four quadrants.]]

The axes divide the plane into four **quadrants**, numbered counterclockwise starting from the top right:
- **Quadrant I:** \(x\) positive, \(y\) positive (top right).
- **Quadrant II:** \(x\) negative, \(y\) positive (top left).
- **Quadrant III:** \(x\) negative, \(y\) negative (bottom left).
- **Quadrant IV:** \(x\) positive, \(y\) negative (bottom right).

Worked example: the point \((3, 2)\) is right 3 and up 2, landing in Quadrant I. The point \((-3, 2)\) is left 3 and up 2, in Quadrant II.

Common mistake: reversing the order to (y, x). The first number is always the horizontal move (x), the second is vertical (y).

[[check:In which quadrant is the point (3, 2)?|1;;I;;quadrant 1;;quadrant i|Both coordinates are positive, so it is in the top-right quadrant.]]
            """,
        ),
        (
            "8. Distance Along the Grid: Horizontal and Vertical",
            r"""
Before the full distance formula, master the easy case: when two points share an \(x\) or a \(y\), the segment between them is straight, and you just **subtract**.

- **Horizontal segment** (same \(y\)): length \(= |x_2 - x_1|\).
- **Vertical segment** (same \(x\)): length \(= |y_2 - y_1|\).

Worked example (horizontal): from \((1, 2)\) to \((7, 2)\), the \(y\)-values match, so the length is \(7 - 1 = 6\).

Worked example (vertical): from \((3, 2)\) to \((3, 9)\), the \(x\)-values match, so the length is \(9 - 2 = 7\).

The bars \(| \; |\) mean "absolute value" -- just take the positive difference, since a length is never negative.

Case study - city blocks on a map: moving along a single street is a horizontal or vertical distance, found by subtracting the coordinates.

Common mistake: counting grid dots instead of the spaces between them. From \(x = 1\) to \(x = 7\) there are 6 spaces (the length), even though 7 grid lines are touched.

[[check:What is the distance from (1, 2) to (7, 2)?|6;;6 units|Same y-value, so subtract the x-values: 7 − 1.]]
            """,
        ),
        (
            "9. The Distance Formula",
            r"""
To find the distance between **any** two points, draw a right triangle: the horizontal change is one leg, the vertical change is the other, and the straight-line distance is the **hypotenuse**. That is just the Pythagorean Theorem on the grid:
\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.
\]

[[figure:distance_on_grid|The horizontal and vertical changes are the legs; the distance is the hypotenuse.]]

The steps:
- Find the horizontal change \((x_2 - x_1)\) and the vertical change \((y_2 - y_1)\).
- Square each, add them, take the square root.

Worked example: from \((1, 1)\) to \((5, 4)\).
\[
d = \sqrt{(5-1)^2 + (4-1)^2} = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5.
\]

Case study - the straight-line ("as the crow flies") distance between two points on a map is exactly this formula.

Common mistake: subtracting then forgetting to square, or squaring a negative wrong. Note \((-4)^2 = 16\), not \(-16\) -- squaring always gives a positive.

[[check:What is the distance from (1, 1) to (5, 4)?|5;;5 units|Legs are 4 and 3, so d = √(16 + 9) = √25.]]
            """,
        ),
        (
            "10. The Midpoint Formula",
            r"""
The **midpoint** is the exact middle of a segment. To find it, simply **average** the \(x\)-coordinates and average the \(y\)-coordinates:
\[
M = \left( \frac{x_1 + x_2}{2}, \; \frac{y_1 + y_2}{2} \right).
\]

[[figure:midpoint_grid|Average the two x-values and the two y-values to land in the middle.]]

Worked example: the midpoint of \((2, 1)\) and \((8, 5)\) is
\[
\left( \frac{2 + 8}{2}, \; \frac{1 + 5}{2} \right) = \left( \frac{10}{2}, \frac{6}{2} \right) = (5, 3).
\]

Notice the difference from distance: midpoint **adds and divides by 2** (an average), while distance **subtracts and squares**. They answer different questions.

Case study - finding the center of a rectangle, or the halfway rest stop between two towns on a straight road, both use the midpoint.

Common mistake: subtracting the coordinates (that is distance) instead of adding them. Midpoint averages, so you add first.

[[check:What is the midpoint of (2, 4) and (6, 8)?|(4,6);;4,6;;(4, 6)|Average each coordinate: ((2+6)/2, (4+8)/2).]]
            """,
        ),
        (
            "11. Slope on the Coordinate Plane",
            r"""
**Slope** measures how steep a line is -- how much it rises for each step to the right. It is "rise over run":
\[
\text{slope} = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1}.
\]

[[figure:coord_line|From the y-intercept, the slope tells you how far up and over to reach the next point.]]

Like distance, slope uses the **differences** of the coordinates -- but it **divides** them instead of squaring and adding.

Worked example: the slope through \((1, 2)\) and \((4, 8)\) is
\[
\frac{8 - 2}{4 - 1} = \frac{6}{3} = 2.
\]
The line rises 2 for every 1 it moves right.

Reading slope:
- **Positive** slope rises left to right; **negative** slope falls.
- A **horizontal** line has slope \(0\); a **vertical** line has an undefined slope.

Common mistake: flipping the formula to "run over rise," or subtracting the x's and y's in a different order. Keep the same point first in both the top and bottom.

[[check:What is the slope of the line through (1, 2) and (4, 8)?|2|Rise over run: (8−2)/(4−1) = 6/3.]]
            """,
        ),
        (
            "12. Strategy: Which Tool, and When",
            r"""
This course gives you several tools that all use coordinate differences. The trick is choosing the right one. Ask what the question wants:

- **"How far apart?" / length / distance** → **Distance formula** (subtract, square, add, square root). On a right triangle off the grid, use **Pythagoras** directly.
- **"Middle / center / halfway"** → **Midpoint** (add the coordinates, divide by 2).
- **"How steep / rate of change"** → **Slope** (rise over run).
- **"Missing side of a right triangle"** → **Pythagorean Theorem** (add for the hypotenuse, subtract for a leg).

A memory hook for the differences:
- Distance **subtracts and squares**.
- Midpoint **adds and halves**.
- Slope **subtracts and divides**.

Error analysis: a student finds the "distance" from \((2, 4)\) to \((6, 8)\) by averaging to get \((4, 6)\). That is the **midpoint**, not the distance. The distance is \(\sqrt{(6-2)^2 + (8-4)^2} = \sqrt{16 + 16} = \sqrt{32} \approx 5.7\).

Case study - one set of two points can be used three ways: their distance apart, their midpoint, and the slope of the line through them. Read the question to know which is wanted.

Final habit: underline the key word -- distance, midpoint, slope, or missing side -- before you pick a formula.

[[check:Which formula finds the point exactly halfway between two points?|midpoint;;the midpoint formula;;midpoint formula|Average the x-coordinates and the y-coordinates.]]
            """,
        ),
    ],
    "mcqs": [
        # --- Parts / concept ---
        {
            "text": r"In a right triangle, which side is called the hypotenuse?",
            "difficulty": 1,
            "choices": [("The side opposite the right angle", True), ("The shortest side", False), ("Either side touching the right angle", False), ("The bottom side", False)],
            "explanation": r"The hypotenuse is the side directly across from the \(90^\circ\) angle, and it is always the longest side of a right triangle. The two sides that form the right angle are the legs. Identifying the hypotenuse first is essential, because it plays a special role (\(c\)) in \(a^2 + b^2 = c^2\). Pro tip: find the little right-angle square in the figure; the side that does NOT touch that corner is the hypotenuse.",
        },
        {
            "text": r"The Pythagorean Theorem applies to which kind of triangle?",
            "difficulty": 1,
            "choices": [("A right triangle (one 90° angle)", True), ("Any triangle", False), ("Only equilateral triangles", False), ("Only very large triangles", False)],
            "explanation": r"\(a^2 + b^2 = c^2\) is true ONLY when the triangle has a right angle. If there is no \(90^\circ\) corner, the relationship does not hold, and using it would give a wrong answer. Many GED questions test whether you notice the right-angle mark. Pro tip: before applying the theorem, confirm there is a right angle (a small square in the corner, or wording like 'perpendicular' or 'vertical wall meets level ground').",
        },
        {
            "text": r"Which equation states the Pythagorean Theorem?",
            "difficulty": 1,
            "choices": [(r"\(a^2 + b^2 = c^2\)", True), (r"\(a + b = c\)", False), (r"\(a^2 - b^2 = c^2\)", False), (r"\(2a + 2b = c\)", False)],
            "explanation": r"The theorem squares each leg, then adds: \(a^2 + b^2 = c^2\), where \(c\) is the hypotenuse. The wrong choice \(a + b = c\) is the most common trap -- you cannot just add the legs, because the sides relate through their squares (areas), not their lengths. Pro tip: picture the 3-4-5 triangle to check a formula: \(3 + 4 = 7\) is not 5, but \(3^2 + 4^2 = 25 = 5^2\) works.",
        },
        # --- Hypotenuse ---
        {
            "text": r"A right triangle has legs \(3\) and \(4\). What is the hypotenuse?",
            "difficulty": 1,
            "choices": [("5", True), ("7", False), ("12", False), ("25", False)],
            "explanation": r"Use \(c = \sqrt{a^2 + b^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\). The tempting wrong answer 7 comes from adding the legs (\(3 + 4\)) without squaring -- a method that does not work. The answer 25 forgets the final square root (that is \(c^2\), not \(c\)). Pro tip: memorize 3-4-5; it appears constantly, so you can write 5 on sight.",
        },
        {
            "text": r"A right triangle has legs \(6\) and \(8\). What is the hypotenuse?",
            "difficulty": 1,
            "choices": [("10", True), ("14", False), ("48", False), ("100", False)],
            "explanation": r"\(c = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). Choice 14 adds the legs; choice 100 stops at \(c^2\) and forgets the square root. Notice 6-8-10 is just the 3-4-5 triple doubled. Pro tip: if both legs share a common factor, factor it out -- 6 and 8 are \(2\times(3,4)\), so the hypotenuse is \(2 \times 5 = 10\).",
        },
        {
            "text": r"A right triangle has legs \(5\) and \(12\). What is the hypotenuse?",
            "difficulty": 2,
            "choices": [("13", True), ("17", False), ("60", False), ("169", False)],
            "explanation": r"\(c = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13\). Choice 17 adds the legs; 169 is \(c^2\) (forgot the root). This is the 5-12-13 triple, worth memorizing. Pro tip: keep a short list of triples (3-4-5, 5-12-13, 8-15-17, 7-24-25); spotting one turns a 30-second problem into a 3-second one.",
        },
        {
            "text": r"A right triangle has legs \(8\) and \(15\). What is the hypotenuse?",
            "difficulty": 2,
            "choices": [("17", True), ("23", False), ("120", False), ("289", False)],
            "explanation": r"\(c = \sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17\). Choice 23 adds the legs; 289 is \(c^2\). This is the 8-15-17 triple. Pro tip: \(\sqrt{289} = 17\) is easier to see if you remember that \(17^2 = 289\); knowing perfect squares up to \(20^2 = 400\) speeds up these problems a lot.",
        },
        {
            "text": r"A right triangle has legs \(9\) and \(12\). What is the hypotenuse?",
            "difficulty": 2,
            "choices": [("15", True), ("21", False), ("108", False), ("225", False)],
            "explanation": r"\(c = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15\). Choice 21 adds the legs. Recognize \(9, 12, 15\) as \(3\times(3,4,5)\). Pro tip: when you see 9 and 12 together, suspect the tripled 3-4-5 and check -- the hypotenuse is \(3 \times 5 = 15\).",
        },
        {
            "text": r"A right triangle has both legs equal to \(1\). What is the hypotenuse?",
            "difficulty": 3,
            "choices": [(r"\(\sqrt{2}\)", True), ("2", False), ("1", False), (r"\(\sqrt{1}\)", False)],
            "explanation": r"\(c = \sqrt{1^2 + 1^2} = \sqrt{1 + 1} = \sqrt{2} \approx 1.41\). Not every answer is a whole number; \(\sqrt{2}\) cannot be simplified, so it stays as is. Choice 2 wrongly adds the legs. Pro tip: when \(a^2 + b^2\) is not a perfect square, the exact answer is a square root -- leave it as \(\sqrt{\,}\) unless the question asks you to round.",
        },
        {
            "text": r"A screen is \(36\) in wide and \(27\) in tall. What is its diagonal?",
            "difficulty": 3,
            "choices": [("45 in", True), ("63 in", False), ("9 in", False), ("2025 in", False)],
            "explanation": r"The diagonal is the hypotenuse: \(\sqrt{36^2 + 27^2} = \sqrt{1296 + 729} = \sqrt{2025} = 45\) in. Choice 63 adds the sides; 2025 forgets the square root. (This is the 3-4-5 triple times 9.) Pro tip: 'screen size' and 'diagonal' both signal the hypotenuse -- the width and height are the legs.",
        },
        # --- Missing leg ---
        {
            "text": r"A right triangle has hypotenuse \(13\) and one leg \(5\). What is the other leg?",
            "difficulty": 2,
            "choices": [("12", True), ("18", False), (r"\(\sqrt{194}\)", False), ("8", False)],
            "explanation": r"Because you know the hypotenuse, SUBTRACT: \(b = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12\). The wrong choice \(\sqrt{194}\) comes from adding (\(13^2 + 5^2\)) -- a mistake that treats the hypotenuse like a leg. Pro tip: finding the hypotenuse adds; finding a leg subtracts. Identify the hypotenuse (largest side, opposite the right angle) before you decide.",
        },
        {
            "text": r"A right triangle has hypotenuse \(10\) and one leg \(6\). What is the other leg?",
            "difficulty": 2,
            "choices": [("8", True), ("16", False), (r"\(\sqrt{136}\)", False), ("4", False)],
            "explanation": r"Subtract, since 10 is the hypotenuse: \(\sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8\). The trap \(\sqrt{136}\) comes from adding instead of subtracting. This is the 6-8-10 triple. Pro tip: if the largest number in the problem is one of your givens, it is the hypotenuse -- so subtract.",
        },
        {
            "text": r"A \(10\)-ft ladder rests with its base \(6\) ft from a wall. How high up the wall does it reach?",
            "difficulty": 2,
            "choices": [("8 ft", True), ("16 ft", False), ("4 ft", False), (r"\(\sqrt{136}\) ft", False)],
            "explanation": r"The ladder is the hypotenuse (10), the ground distance is a leg (6), and the wall height is the missing leg. Subtract: \(\sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8\) ft. Adding would give the wrong \(\sqrt{136}\). Pro tip: in every ladder problem the ladder itself is the hypotenuse -- so you will subtract to find the wall height or the ground distance.",
        },
        {
            "text": r"A right triangle has hypotenuse \(25\) and one leg \(7\). What is the other leg?",
            "difficulty": 3,
            "choices": [("24", True), ("18", False), ("32", False), (r"\(\sqrt{674}\)", False)],
            "explanation": r"Subtract: \(\sqrt{25^2 - 7^2} = \sqrt{625 - 49} = \sqrt{576} = 24\). The trap \(\sqrt{674}\) adds the squares. This is the 7-24-25 triple. Pro tip: \(\sqrt{576} = 24\) because \(24^2 = 576\); recognizing perfect squares (here \(25^2=625\) and \(24^2=576\)) makes the arithmetic quick and safe.",
        },
        {
            "text": r"To find a missing LEG of a right triangle, you should:",
            "difficulty": 2,
            "choices": [("Subtract the known leg's square from the hypotenuse's square, then take the root", True), ("Add the two known squares, then take the root", False), ("Add the two sides directly", False), ("Divide the hypotenuse by 2", False)],
            "explanation": r"A leg is found by \(\text{leg} = \sqrt{c^2 - (\text{other leg})^2}\) -- you subtract because the hypotenuse is the largest and you are 'undoing' the addition. Adding the squares is how you find the hypotenuse, not a leg. Pro tip: hypotenuse = add; leg = subtract. Decide which side is missing before choosing the operation.",
        },
        # --- Triples ---
        {
            "text": r"Which set of three numbers is a Pythagorean triple?",
            "difficulty": 2,
            "choices": [("5, 12, 13", True), ("4, 5, 6", False), ("2, 3, 4", False), ("6, 7, 8", False)],
            "explanation": r"A triple satisfies \(a^2 + b^2 = c^2\): \(5^2 + 12^2 = 25 + 144 = 169 = 13^2\). The others fail; e.g. \(4^2 + 5^2 = 41\), which is not \(6^2 = 36\). Pro tip: to test any trio, square the two smaller numbers, add, and check whether it equals the square of the largest.",
        },
        {
            "text": r"A right triangle has legs \(6\) and \(8\). Recognizing the triple, the hypotenuse is:",
            "difficulty": 1,
            "choices": [("10", True), ("14", False), ("48", False), ("7", False)],
            "explanation": r"\(6, 8, 10\) is the 3-4-5 triple doubled (\(2 \times 3, 2 \times 4, 2 \times 5\)), so the hypotenuse is \(2 \times 5 = 10\). You could also compute \(\sqrt{36 + 64} = \sqrt{100} = 10\). Pro tip: any whole-number multiple of a triple is also a triple, so scaling 3-4-5 gives 6-8-10, 9-12-15, 12-16-20, and so on.",
        },
        {
            "text": r"A right triangle has legs \(15\) and \(20\). What is the hypotenuse?",
            "difficulty": 3,
            "choices": [("25", True), ("35", False), ("300", False), ("625", False)],
            "explanation": r"\(15, 20, 25\) is the 3-4-5 triple times 5. Check: \(\sqrt{15^2 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25\). Choice 35 adds the legs. Pro tip: when both legs are multiples of 5 (15 and 20), factor out the 5 to see the 3-4-5 pattern: \(5 \times (3, 4, 5)\) gives 25.",
        },
        {
            "text": r"Is every right triangle a Pythagorean triple?",
            "difficulty": 2,
            "choices": [("No -- many have square-root answers like √13", True), ("Yes, always", False), ("Only if it is large", False), ("Only if it is small", False)],
            "explanation": r"Triples are special cases where all three sides are whole numbers. Plenty of right triangles are not triples -- legs 2 and 3 give \(\sqrt{13}\), which is not a whole number. Pro tip: try the triple shortcut first; if the legs do not match a known triple, fall back to \(\sqrt{a^2+b^2}\) and accept a square-root answer.",
        },
        # --- Real-world Pythagorean ---
        {
            "text": r"A person walks \(9\) km east, then \(12\) km north. How far are they from the start (straight line)?",
            "difficulty": 2,
            "choices": [("15 km", True), ("21 km", False), ("3 km", False), ("108 km", False)],
            "explanation": r"East and north are perpendicular, so they form the legs of a right triangle, and the straight-line distance is the hypotenuse: \(\sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15\) km. Choice 21 adds the legs (that is the walking distance, not the straight-line distance). Pro tip: 'straight-line' or 'as the crow flies' always means the hypotenuse.",
        },
        {
            "text": r"A rectangular field is \(40\) m by \(30\) m. What is the length of the diagonal path across it?",
            "difficulty": 2,
            "choices": [("50 m", True), ("70 m", False), ("35 m", False), ("1200 m", False)],
            "explanation": r"The diagonal of a rectangle splits it into two right triangles, with the length and width as legs: \(\sqrt{40^2 + 30^2} = \sqrt{1600 + 900} = \sqrt{2500} = 50\) m. Choice 70 adds the sides. (It is the 3-4-5 triple times 10.) Pro tip: a rectangle's diagonal is always the hypotenuse of a right triangle made by two of its sides.",
        },
        {
            "text": r"A ramp rises \(5\) ft over a horizontal run of \(12\) ft. How long is the ramp surface?",
            "difficulty": 2,
            "choices": [("13 ft", True), ("17 ft", False), ("7 ft", False), ("60 ft", False)],
            "explanation": r"The rise (5) and run (12) are the legs; the ramp surface is the hypotenuse: \(\sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13\) ft. Choice 17 adds the legs. This is the 5-12-13 triple. Pro tip: for ramps, the sloped surface you walk on is the hypotenuse; the rise and run are the legs.",
        },
        {
            "text": r"A \(17\)-ft wire runs from the top of a pole to a point \(8\) ft from its base. How tall is the pole?",
            "difficulty": 3,
            "choices": [("15 ft", True), ("25 ft", False), ("9 ft", False), (r"\(\sqrt{353}\) ft", False)],
            "explanation": r"The wire is the hypotenuse (17), the ground distance is a leg (8), and the pole height is the missing leg, so subtract: \(\sqrt{17^2 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15\) ft. Adding would give the wrong \(\sqrt{353}\). This uses the 8-15-17 triple. Pro tip: a guy-wire or cable to the top of a pole is the hypotenuse -- subtract to find the height.",
        },
        {
            "text": r"Two boats leave a dock: one goes \(8\) miles south, the other \(15\) miles east. How far apart are they?",
            "difficulty": 3,
            "choices": [("17 miles", True), ("23 miles", False), ("7 miles", False), ("120 miles", False)],
            "explanation": r"South and east are perpendicular, forming legs of 8 and 15; the distance between the boats is the hypotenuse: \(\sqrt{8^2 + 15^2} = \sqrt{64 + 225} = \sqrt{289} = 17\) miles. Choice 23 adds the legs. (8-15-17 triple.) Pro tip: whenever two paths go in perpendicular directions, the gap between the endpoints is a hypotenuse.",
        },
        {
            "text": r"In a real-world right-triangle problem, the hypotenuse is always:",
            "difficulty": 1,
            "choices": [("The slanted or straight-line distance (longest side)", True), ("The side along the ground", False), ("The vertical side", False), ("The shortest side", False)],
            "explanation": r"The hypotenuse is opposite the right angle and is the longest side -- in word problems it is usually the slanted distance (ramp, ladder, wire) or the straight-line 'as the crow flies' distance. The two perpendicular directions (up/down and along the ground) are the legs. Pro tip: sketch the situation, mark the right angle where the two perpendicular directions meet, and the remaining slanted side is your hypotenuse.",
        },
        # --- Coordinate plane / quadrants ---
        {
            "text": r"In which quadrant is the point \((-3, 2)\)?",
            "difficulty": 2,
            "choices": [("Quadrant II", True), ("Quadrant I", False), ("Quadrant III", False), ("Quadrant IV", False)],
            "explanation": r"The \(x\)-value is negative (left) and the \(y\)-value is positive (up), which is the top-left region, Quadrant II. Quadrants are numbered counterclockwise from the top right (I), so II is top-left. Pro tip: read the SIGNS -- (\(-\), \(+\)) is II, (\(+\), \(+\)) is I, (\(-\), \(-\)) is III, (\(+\), \(-\)) is IV.",
        },
        {
            "text": r"What are the coordinates of a point that is \(4\) right and \(3\) up from the origin?",
            "difficulty": 1,
            "choices": [("(4, 3)", True), ("(3, 4)", False), ("(-4, 3)", False), ("(4, -3)", False)],
            "explanation": r"A point is written \((x, y)\): the horizontal move first, then the vertical. Four right and three up is \((4, 3)\). The trap \((3, 4)\) reverses the order. Pro tip: say 'over, then up' -- the x-coordinate (across) always comes before the y-coordinate (up/down).",
        },
        {
            "text": r"The point \((0, -5)\) lies where?",
            "difficulty": 2,
            "choices": [("On the y-axis, below the origin", True), ("In Quadrant IV", False), ("On the x-axis", False), ("In Quadrant III", False)],
            "explanation": r"Because the \(x\)-coordinate is 0, the point sits exactly on the \(y\)-axis (no left or right movement); the \(-5\) puts it 5 units down. Points on an axis are not in any quadrant. Pro tip: a 0 in a coordinate means the point is on an axis -- \( (0, y)\) is on the y-axis, and \((x, 0)\) is on the x-axis.",
        },
        # --- Horizontal / vertical distance ---
        {
            "text": r"What is the distance from \((1, 2)\) to \((7, 2)\)?",
            "difficulty": 1,
            "choices": [("6", True), ("8", False), ("5", False), ("9", False)],
            "explanation": r"The \(y\)-values are equal (both 2), so this is a horizontal segment -- just subtract the \(x\)-values: \(7 - 1 = 6\). No square root is needed when the points share an \(x\) or \(y\). Pro tip: if two points share one coordinate, the distance is a simple subtraction; save the distance formula for slanted segments.",
        },
        {
            "text": r"What is the distance from \((3, 2)\) to \((3, 9)\)?",
            "difficulty": 1,
            "choices": [("7", True), ("6", False), ("11", False), ("12", False)],
            "explanation": r"The \(x\)-values match (both 3), so this is a vertical segment -- subtract the \(y\)-values: \(9 - 2 = 7\). Pro tip: same x means a vertical line (subtract the y's); same y means a horizontal line (subtract the x's).",
        },
        {
            "text": r"How long is the horizontal segment from \((-2, 4)\) to \((5, 4)\)?",
            "difficulty": 2,
            "choices": [("7", True), ("3", False), ("9", False), ("-7", False)],
            "explanation": r"Same \(y\)-value, so subtract the \(x\)-values, using the positive difference: \(5 - (-2) = 5 + 2 = 7\). A length is never negative, so \(-7\) is impossible. Pro tip: subtracting a negative adds -- \(5 - (-2) = 7\). Distances are always positive, so take the absolute value if you get a negative.",
        },
        # --- Distance formula ---
        {
            "text": r"What is the distance between \((1, 1)\) and \((5, 4)\)?",
            "difficulty": 2,
            "choices": [("5", True), ("7", False), ("25", False), (r"\(\sqrt{7}\)", False)],
            "explanation": r"Use \(d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2} = \sqrt{(5-1)^2 + (4-1)^2} = \sqrt{16 + 9} = \sqrt{25} = 5\). The legs of the hidden right triangle are 4 and 3. Choice 25 forgets the square root. Pro tip: the distance formula is just Pythagoras -- the horizontal change and vertical change are the two legs.",
        },
        {
            "text": r"What is the distance between \((0, 0)\) and \((6, 8)\)?",
            "difficulty": 2,
            "choices": [("10", True), ("14", False), ("48", False), ("100", False)],
            "explanation": r"\(d = \sqrt{(6-0)^2 + (8-0)^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). From the origin, the coordinates themselves are the legs (6 and 8 -- the 6-8-10 triple). Choice 14 adds them; 100 is \(d^2\). Pro tip: when one point is the origin \((0,0)\), the other point's coordinates are exactly the two legs.",
        },
        {
            "text": r"What is the distance between \((-2, -1)\) and \((1, 3)\)?",
            "difficulty": 3,
            "choices": [("5", True), ("7", False), (r"\(\sqrt{5}\)", False), ("25", False)],
            "explanation": r"\(d = \sqrt{(1-(-2))^2 + (3-(-1))^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\). Be careful with the negatives: \(1 - (-2) = 3\) and \(3 - (-1) = 4\). Pro tip: subtracting a negative adds -- mishandling the signs is the most common error here, so write out \(1 - (-2)\) fully before simplifying.",
        },
        {
            "text": r"The distance formula \(d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\) is really an application of:",
            "difficulty": 2,
            "choices": [("The Pythagorean Theorem", True), ("The midpoint formula", False), ("The slope formula", False), ("The area formula", False)],
            "explanation": r"The horizontal change \((x_2 - x_1)\) and vertical change \((y_2 - y_1)\) are the legs of a right triangle, and the distance is its hypotenuse -- so the formula is \(a^2 + b^2 = c^2\) in disguise. Pro tip: if you forget the distance formula, just sketch the right triangle between the two points and use Pythagoras directly.",
        },
        {
            "text": r"What is the distance between \((2, 3)\) and \((2, 8)\)?",
            "difficulty": 1,
            "choices": [("5", True), (r"\(\sqrt{29}\)", False), ("10", False), ("11", False)],
            "explanation": r"The \(x\)-values are the same, so this is vertical: \(8 - 3 = 5\). You do not need the full formula when a coordinate is shared. (Using the formula still works: \(\sqrt{0^2 + 5^2} = 5\).) Pro tip: always glance at whether the two points share an x or a y first -- it can turn a formula problem into one quick subtraction.",
        },
        # --- Midpoint ---
        {
            "text": r"What is the midpoint of \((2, 4)\) and \((6, 8)\)?",
            "difficulty": 2,
            "choices": [("(4, 6)", True), ("(8, 12)", False), ("(2, 2)", False), ("(4, 4)", False)],
            "explanation": r"Average each coordinate: \(\left(\frac{2+6}{2}, \frac{4+8}{2}\right) = \left(\frac{8}{2}, \frac{12}{2}\right) = (4, 6)\). Choice \((8, 12)\) forgot to divide by 2 (that is just the sum). Pro tip: the midpoint always lands between the two points, so each coordinate of your answer should be between the matching coordinates of the originals -- 4 is between 2 and 6, and 6 is between 4 and 8.",
        },
        {
            "text": r"What is the midpoint of \((1, 3)\) and \((5, 9)\)?",
            "difficulty": 2,
            "choices": [("(3, 6)", True), ("(6, 12)", False), ("(4, 6)", False), ("(2, 3)", False)],
            "explanation": r"\(\left(\frac{1+5}{2}, \frac{3+9}{2}\right) = (3, 6)\). The trap \((4, 6)\) comes from subtracting the x-values instead of averaging. Pro tip: midpoint ADDS and halves; if you find yourself subtracting, you are doing distance or slope, not midpoint.",
        },
        {
            "text": r"What is the midpoint of \((-2, 4)\) and \((4, -2)\)?",
            "difficulty": 3,
            "choices": [("(1, 1)", True), ("(2, 2)", False), ("(-1, -1)", False), ("(3, 3)", False)],
            "explanation": r"\(\left(\frac{-2+4}{2}, \frac{4+(-2)}{2}\right) = \left(\frac{2}{2}, \frac{2}{2}\right) = (1, 1)\). Handle the signs carefully: \(-2 + 4 = 2\) and \(4 + (-2) = 2\). Pro tip: add the coordinates exactly as written (including their signs) before dividing by 2; rushing the signs is the usual slip.",
        },
        {
            "text": r"The midpoint formula tells you to do what to the coordinates?",
            "difficulty": 1,
            "choices": [("Add them and divide by 2 (average)", True), ("Subtract them and square", False), ("Multiply them", False), ("Take the square root", False)],
            "explanation": r"The midpoint is the average of the endpoints: \(\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)\). Subtracting and squaring is the distance formula -- a different question. Pro tip: 'middle' = 'average' = add and halve. Keep the three coordinate tools straight: midpoint adds/halves, distance subtracts/squares, slope subtracts/divides.",
        },
        # --- Slope ---
        {
            "text": r"What is the slope of the line through \((1, 2)\) and \((4, 8)\)?",
            "difficulty": 2,
            "choices": [("2", True), (r"\(\tfrac{1}{2}\)", False), ("3", False), ("6", False)],
            "explanation": r"Slope is rise over run: \(\frac{y_2 - y_1}{x_2 - x_1} = \frac{8 - 2}{4 - 1} = \frac{6}{3} = 2\). The trap \(\tfrac{1}{2}\) flips the formula (run over rise). Pro tip: keep the SAME point first on top and bottom -- subtract the y's in the same order as the x's, or your sign will flip.",
        },
        {
            "text": r"A line through \((0, 1)\) and \((2, 5)\) has what slope?",
            "difficulty": 2,
            "choices": [("2", True), ("4", False), (r"\(\tfrac{1}{2}\)", False), ("3", False)],
            "explanation": r"\(\frac{5 - 1}{2 - 0} = \frac{4}{2} = 2\). Choice 4 forgot to divide by the run (it is only the rise). Pro tip: slope is a RATIO -- always divide the vertical change by the horizontal change, never report the rise alone.",
        },
        {
            "text": r"A horizontal line has what slope?",
            "difficulty": 2,
            "choices": [("0", True), ("1", False), ("Undefined", False), ("Infinity", False)],
            "explanation": r"A horizontal line has no rise (the y-values never change), so the slope is \(\frac{0}{\text{run}} = 0\). (A vertical line is the opposite case: the run is 0, making the slope undefined.) Pro tip: flat line = slope 0; standing-straight-up line = undefined slope. Don't mix the two.",
        },
        # --- Strategy / mixed ---
        {
            "text": r"A student averages \((2, 4)\) and \((6, 8)\) to get \((4, 6)\) and calls it the 'distance.' What did they actually find?",
            "difficulty": 3,
            "choices": [("The midpoint, not the distance", True), ("The slope", False), ("The correct distance", False), ("The hypotenuse", False)],
            "explanation": r"Averaging the coordinates gives the MIDPOINT \((4, 6)\), the middle of the segment -- not the distance. The distance would be \(\sqrt{(6-2)^2 + (8-4)^2} = \sqrt{16 + 16} = \sqrt{32} \approx 5.7\). Pro tip: match the operation to the question -- average for midpoint, subtract-square-root for distance, subtract-divide for slope.",
        },
        {
            "text": r"Which question is answered by the distance formula?",
            "difficulty": 1,
            "choices": [("How far apart are two points?", True), ("Where is the middle of a segment?", False), ("How steep is a line?", False), ("What is the area of a triangle?", False)],
            "explanation": r"The distance formula gives the straight-line length between two points (how far apart they are). The middle is the midpoint, and steepness is slope. Pro tip: underline the key word in the problem -- 'how far' / 'length' / 'distance' points you to the distance formula every time.",
        },
        {
            "text": r"Which tool would you use to find the missing side of a right triangle that is NOT drawn on a grid?",
            "difficulty": 2,
            "choices": [("The Pythagorean Theorem", True), ("The midpoint formula", False), ("The slope formula", False), ("The distance formula", False)],
            "explanation": r"With a bare right triangle (no coordinates), use \(a^2 + b^2 = c^2\) directly. The distance formula is for two points on a grid (and is the same idea underneath). Midpoint and slope answer different questions entirely. Pro tip: coordinates given → distance/midpoint/slope; a triangle with side lengths → Pythagorean Theorem.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Pythagorean Theorem & Coordinate Geometry course (MCQ only)."

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
