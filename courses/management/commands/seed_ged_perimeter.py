"""
Seed a dedicated GED Geometry course focused entirely on PERIMETER and
CIRCUMFERENCE -- a companion to the Area Mastery course.

12 lessons, ~46 multiple-choice questions, labeled shape diagrams, interactive
self-checks, case studies, and common-mistake callouts. Every answer explanation
teaches the method, names the tempting wrong answer, and ends with a Pro tip.
Multiple choice only.

Run:
    python manage.py seed_ged_perimeter
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Perimeter & Circumference Mastery",
    "slug": "ged-geometry-perimeter-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep GED Geometry course built around the distance AROUND a shape. Students master "
        "perimeter for rectangles, squares, triangles, regular polygons, and composite figures, "
        "then move to circles -- radius, diameter, pi, and circumference. The course also covers "
        "working backward from a known perimeter, telling perimeter apart from area, and real-world "
        "problems like fencing, framing, and trim. Every shape has a labeled diagram, every lesson "
        "has an interactive self-check, and every practice answer explains the method and adds a Pro tip."
    ),
    "lessons": [
        (
            "1. What Perimeter Means: The Distance Around",
            r"""
**Perimeter** is the total distance **around** the outside of a flat shape. Imagine walking along every edge of a shape until you return to where you started -- the length of that walk is the perimeter.

Unlike area, perimeter is a length, so it is measured in **plain units** -- inches, feet, meters, centimeters -- not square units.

The most basic rule works for **any** shape with straight sides: **add up the lengths of all the sides.**

Worked example: a four-sided figure with sides 5, 3, 5, and 3 has perimeter
\[
5 + 3 + 5 + 3 = 16 \text{ units}.
\]

Do not confuse **perimeter** (the distance around) with **area** (the surface inside). A fence around a yard measures perimeter; the grass inside measures area.

Case study - fencing a garden: to put a fence around a garden, you need its perimeter, because the fence runs along the edges.

Common mistake: using square units for perimeter. Perimeter is a length, so write "16 cm," not "16 cm\(^2\)."

[[check:A four-sided figure has sides 7, 4, 7, and 4. What is its perimeter?|22;;22 units|Add all four sides: \(7+4+7+4\).]]
            """,
        ),
        (
            "2. Perimeter of Rectangles and Squares",
            r"""
A **rectangle** has two equal lengths and two equal widths, so its perimeter is
\[
P = 2l + 2w = 2(l + w).
\]

[[figure:perimeter_rectangle|Add a length and a width, then double, because each appears twice.]]

Worked example: a rectangle 8 cm by 5 cm has perimeter
\[
P = 2(8 + 5) = 2(13) = 26 \text{ cm}.
\]

A **square** has four equal sides, so its perimeter is just four times one side:
\[
P = 4s.
\]
A square with side 6 m has perimeter \(4 \times 6 = 24\) m.

Case study - framing a picture: a 10 in by 8 in photo needs frame molding equal to its perimeter, \(2(10 + 8) = 36\) inches.

Common mistake: doubling only one side. Both the length **and** the width appear twice, so add them first, then double.

[[check:A rectangle is 9 cm long and 4 cm wide. What is its perimeter?|26;;26 cm|Use \(2(9 + 4)\).]]
            """,
        ),
        (
            "3. Perimeter of Triangles and Other Polygons",
            r"""
For any **polygon** (a closed shape with straight sides), the perimeter is simply the **sum of all the side lengths**. There is no shortcut to memorize -- just add.

[[figure:perimeter_triangle|Add the three sides of a triangle to get its perimeter.]]

Worked example (triangle): a triangle with sides 13 cm, 13 cm, and 10 cm has perimeter
\[
P = 13 + 13 + 10 = 36 \text{ cm}.
\]

Worked example (five-sided figure): a pentagon with sides 4, 6, 5, 7, and 3 has perimeter
\[
4 + 6 + 5 + 7 + 3 = 25 \text{ units}.
\]

Case study - a triangular sign needs trim along all three edges, so the trim length is the sum of the three sides.

Common mistake: missing a side. Count the sides first, then make sure your sum has that many numbers in it.

[[check:A triangle has sides 6 cm, 8 cm, and 10 cm. What is its perimeter?|24;;24 cm|Add all three sides: \(6+8+10\).]]
            """,
        ),
        (
            "4. Perimeter of Regular Polygons",
            r"""
A **regular polygon** has all sides equal in length. That makes its perimeter easy: multiply the number of sides by the length of one side.
\[
P = n \times s,
\]
where \(n\) is the number of sides and \(s\) is the side length.

[[figure:perimeter_polygon|Because all six sides are equal, multiply one side by 6.]]

Worked example: a regular hexagon (6 sides) with each side 5 cm has perimeter
\[
P = 6 \times 5 = 30 \text{ cm}.
\]

Common regular shapes:
- Equilateral triangle: \(P = 3s\)
- Square: \(P = 4s\)
- Regular pentagon: \(P = 5s\)
- Regular hexagon: \(P = 6s\)
- Regular octagon: \(P = 8s\)

Case study - a stop sign is a regular octagon; if each side is 12 in, its perimeter is \(8 \times 12 = 96\) inches.

Common mistake: forgetting how many sides the polygon has. A pentagon has 5 sides, a hexagon 6, an octagon 8 -- count carefully.

[[check:A regular pentagon has sides of 8 cm each. What is its perimeter?|40;;40 cm|A pentagon has 5 sides: \(5 \times 8\).]]
            """,
        ),
        (
            "5. Perimeter of Composite and Irregular Shapes",
            r"""
A **composite** (irregular) shape is made of straight sides that turn corners, like an L-shape or a staircase. The rule never changes: **walk all the way around and add every side.**

[[figure:perimeter_composite|Go around the whole boundary, adding every side length.]]

Worked example: an L-shape with sides 8, 3, 5, 3, 3, and 6 has perimeter
\[
8 + 3 + 5 + 3 + 3 + 6 = 28 \text{ ft}.
\]

Sometimes a side length is not labeled. Use the labeled sides to figure it out: opposite sides of the overall bounding rectangle must match up. In a rectilinear (right-angle) L-shape, the total of the horizontal pieces on top equals the total on the bottom.

Case study - baseboard for a room shaped like an L: the carpenter measures every wall and adds them, because the baseboard follows the whole edge.

Common mistake: only adding the labeled sides and skipping an unlabeled one. Make sure your path closes the full loop with no gaps.

[[check:An L-shape has sides 8, 3, 5, 3, 3, and 6 feet. What is its perimeter?|28;;28 ft|Add every side around the loop.]]
            """,
        ),
        (
            "6. Circles: Radius, Diameter, and Pi",
            r"""
Circles do not have straight sides, so they need their own vocabulary.

- The **radius** \(r\) is the distance from the center to the edge.
- The **diameter** \(d\) is the distance all the way across through the center. It is twice the radius: \(d = 2r\) (and \(r = \tfrac{d}{2}\)).
- **Pi** (\(\pi\)) is a special number, about **3.14**, that connects a circle's distance around to its diameter.

[[figure:circle_circumference|The diameter goes straight across through the center; the radius is half of it.]]

Worked example: if a circle has diameter 10 cm, its radius is
\[
r = \frac{10}{2} = 5 \text{ cm}.
\]
If a circle has radius 7 cm, its diameter is \(d = 2 \times 7 = 14\) cm.

Knowing how to switch between radius and diameter is the key first step before any circle calculation.

Case study - a round table described as "60 inches across" is giving you the diameter; its radius is 30 inches.

Common mistake: mixing up radius and diameter. The diameter is the long way across; the radius is only half that.

[[check:A circle has a diameter of 16 cm. What is its radius?|8;;8 cm|Radius is half the diameter: \(16 \div 2\).]]
            """,
        ),
        (
            "7. Circumference of a Circle",
            r"""
The **circumference** is the distance around a circle -- its "perimeter." Because a circle has no straight sides, you use \(\pi\):
\[
C = \pi d \qquad\text{or}\qquad C = 2 \pi r.
\]
Both formulas give the same answer, since \(d = 2r\). Use \(\pi \approx 3.14\) unless told otherwise.

Worked example (using diameter): a circle with diameter 10 cm has circumference
\[
C = \pi d = 3.14 \times 10 = 31.4 \text{ cm}.
\]

Worked example (using radius): a circle with radius 7 cm has circumference
\[
C = 2 \pi r = 2 \times 3.14 \times 7 = 43.96 \text{ cm}.
\]

Case study - a bicycle wheel with diameter 26 in travels \(\pi d = 3.14 \times 26 \approx 81.6\) inches in one full turn.

Common mistake: using \(\pi r^2\) for circumference. That is the **area** formula. Circumference uses \(\pi d\) or \(2\pi r\) -- no squaring.

[[check:A circle has a diameter of 10 cm. Using 3.14 for pi, what is its circumference?|31.4;;31.40 cm;;31.4 cm|Use \(C = \pi d = 3.14 \times 10\).]]
            """,
        ),
        (
            "8. Circumference from Radius vs. Diameter",
            r"""
The most common circle mistake on the GED is plugging the wrong measurement into the formula. Pick the formula that matches what you are given.

- **Given the diameter?** Use \(C = \pi d\) directly.
- **Given the radius?** Either use \(C = 2 \pi r\), or first double the radius to get the diameter and use \(C = \pi d\).

Worked example (radius given): radius 5 m.
\[
C = 2 \pi r = 2 \times 3.14 \times 5 = 31.4 \text{ m}.
\]

Worked example (diameter given): diameter 20 m.
\[
C = \pi d = 3.14 \times 20 = 62.8 \text{ m}.
\]
Always check which measurement you have before choosing the formula.

Case study - a circular pond with radius 10 ft needs an edging that is \(2 \times 3.14 \times 10 = 62.8\) ft long.

Common mistake: using the radius in \(C = \pi d\) (which expects the diameter). If you only have the radius, either double it first or use \(2\pi r\).

[[check:A circle has a radius of 5 m. Using 3.14 for pi, what is its circumference?|31.4;;31.4 m|Use \(2 \times 3.14 \times 5\).]]
            """,
        ),
        (
            "9. Working Backward: Find a Side or Radius",
            r"""
Sometimes the GED gives you the **perimeter** and asks for a missing measurement. Reverse the formula by dividing.

**Square:** since \(P = 4s\), the side is
\[
s = \frac{P}{4}.
\]
A square with perimeter 36 cm has side \(36 / 4 = 9\) cm.

**Rectangle:** since \(P = 2(l + w)\), divide the perimeter by 2 to get \(l + w\), then subtract the known side. If \(P = 26\) and \(w = 5\):
\[
l + w = \frac{26}{2} = 13, \qquad l = 13 - 5 = 8.
\]

**Circle:** since \(C = \pi d\), the diameter is
\[
d = \frac{C}{\pi}.
\]
A circle with circumference 31.4 cm has diameter \(31.4 / 3.14 = 10\) cm, so radius 5 cm.

Case study - you have 40 ft of fencing for a square pen; each side can be \(40 / 4 = 10\) ft.

Common mistake: forgetting to divide the rectangle's perimeter by 2 first. \(P = 2(l + w)\), so \(l + w\) is **half** the perimeter, not the whole perimeter.

[[check:A square has a perimeter of 36 cm. How long is each side?|9;;9 cm|Divide the perimeter by 4: \(36 \div 4\).]]
            """,
        ),
        (
            "10. Perimeter vs. Area: Don't Mix Them Up",
            r"""
Perimeter and area answer different questions, and the GED loves to test whether you can tell them apart.

- **Perimeter** = the distance **around** the edge. Units: plain (cm, ft, m).
- **Area** = the surface **inside**. Units: square (cm\(^2\), ft\(^2\), m\(^2\)).

Quick comparison for a 6 by 4 rectangle:
\[
\text{Perimeter} = 2(6 + 4) = 20 \text{ units}, \qquad \text{Area} = 6 \times 4 = 24 \text{ square units}.
\]

How to decide which one a word problem wants:
- **Perimeter** words: fence, border, trim, frame, edging, "around," "distance around."
- **Area** words: carpet, paint, tile, cover, "surface," "how much to fill."

Case study - "How much fencing for a yard?" is perimeter. "How much sod to cover the yard?" is area. Same yard, different question.

Common mistake: giving the area when the question asked for the distance around (or vice versa). Read for the keyword and check the units of your answer.

[[check:For a 6 by 4 rectangle, what is the perimeter?|20;;20 units|Perimeter is \(2(6+4)\), not the area.]]
            """,
        ),
        (
            "11. Real-World Perimeter Problems",
            r"""
Most GED perimeter questions are everyday situations. Spot the shape, add the sides (or use the circle formula), and watch for a final "cost" or "how many" step.

Common perimeter situations:
- **Fencing** a yard or pen.
- **Framing** a picture or window (molding length).
- **Trim, baseboard, or edging** around a room or garden.
- **Ribbon or border** around an object.

Worked example - fencing: a rectangular yard 30 ft by 20 ft needs
\[
P = 2(30 + 20) = 100 \text{ ft of fence}.
\]

Worked example - cost: if fencing costs 6 dollars per foot and the yard above needs 100 ft, the cost is \(100 \times 6 = 600\) dollars.

Worked example - circular edging: a round garden with radius 4 ft needs edging of length \(2 \times 3.14 \times 4 = 25.12\) ft.

Case study - a banner border: trim sewn around a 5 ft by 3 ft banner is \(2(5 + 3) = 16\) ft of trim.

Common mistake: stopping at the perimeter when the question asks for total **cost**. Multiply the perimeter by the price per unit length.

[[check:A rectangular yard is 30 ft by 20 ft. How many feet of fence go around it?|100;;100 ft|Use \(2(30 + 20)\).]]
            """,
        ),
        (
            "12. GED Strategy: Around the Shape, Right Units",
            r"""
Use a steady routine for every perimeter or circumference question:

- **Is it a circle or a straight-sided shape?** Circles use \(\pi\); polygons add sides.
- **For a circle, do I have the radius or the diameter?** Match the formula (\(2\pi r\) or \(\pi d\)).
- **Did I include every side?** Walk the full boundary; don't skip a side.
- **Perimeter or area?** Perimeter is the distance around (plain units); area is the inside (square units).
- **Is there a cost or "how many" step left?**

Formula quick-reference:
- Rectangle: \(P = 2(l + w)\)
- Square: \(P = 4s\)
- Any polygon: \(P = \) sum of all sides
- Regular polygon: \(P = n \times s\)
- Circle: \(C = \pi d = 2 \pi r\)

Error analysis: a student finds a circle's "perimeter" with radius 5 as \(\pi r^2 = 3.14 \times 25 = 78.5\). That is the **area**. The circumference is \(2 \pi r = 2 \times 3.14 \times 5 = 31.4\).

Case study - a running track: a straight-sided infield plus two semicircular ends. Add the straight sides and the two half-circumferences (which together make one full circle) to get the distance around.

Final habit: name the shape, then say "around" out loud. If it's a circle, decide radius-or-diameter before you compute.

[[check:A circle has radius 5. Which value is its circumference, using 3.14 for pi?|31.4;;31.4 cm|Circumference is \(2\pi r\), not \(\pi r^2\).]]
            """,
        ),
    ],
    "mcqs": [
        # --- Rectangles & squares ---
        {
            "text": r"A rectangle is \(8\) cm long and \(5\) cm wide. What is its perimeter?",
            "difficulty": 1,
            "choices": [("26 cm", True), ("40 cm", False), ("13 cm", False), ("80 cm", False)],
            "explanation": r"Perimeter adds all four sides: \(2(l + w) = 2(8 + 5) = 26\) cm. The trap 40 is the AREA (\(8 \times 5\)); 13 is just one length plus one width (you forgot to double). Pro tip: perimeter uses plain units (cm) and adds; area uses square units and multiplies. Decide which the question wants.",
        },
        {
            "text": r"A square has a side length of \(6\) m. What is its perimeter?",
            "difficulty": 1,
            "choices": [("24 m", True), ("36 m", False), ("12 m", False), ("18 m", False)],
            "explanation": r"A square has 4 equal sides: \(P = 4s = 4 \times 6 = 24\) m. The trap 36 is the area (\(6^2\)); 12 only doubles the side. Pro tip: \(4s\) for a square's perimeter, \(s^2\) for its area -- don't swap them.",
        },
        {
            "text": r"A rectangle is \(12\) ft by \(7\) ft. What is its perimeter?",
            "difficulty": 1,
            "choices": [("38 ft", True), ("19 ft", False), ("84 ft", False), ("76 ft", False)],
            "explanation": r"\(2(12 + 7) = 2(19) = 38\) ft. The trap 84 is the area; 19 is just \(12+7\) (you forgot to double). Pro tip: in \(2(l+w)\), add length and width FIRST, then double, because each side appears twice.",
        },
        {
            "text": r"A square photo has sides of \(9\) in. What is its perimeter?",
            "difficulty": 1,
            "choices": [("36 in", True), ("81 in", False), ("18 in", False), ("27 in", False)],
            "explanation": r"\(4s = 4 \times 9 = 36\) in. The trap 81 is the area (\(9^2\)); 18 only doubles the side instead of using all four. Pro tip: a square frame has four equal edges -- multiply one side by 4.",
        },
        {
            "text": r"A picture is \(10\) in by \(8\) in. How much frame molding is needed to go around it?",
            "difficulty": 2,
            "choices": [("36 in", True), ("80 in", False), ("18 in", False), ("26 in", False)],
            "explanation": r"Frame molding runs around the edge, so it is the perimeter: \(2(10 + 8) = 36\) in. The trap 80 is the area (\(10 \times 8\)); 18 forgets to double. Pro tip: 'frame', 'border', and 'trim' all mean perimeter -- the distance around.",
        },
        {
            "text": r"A rectangle is \(15\) m long and \(10\) m wide. What is its perimeter?",
            "difficulty": 1,
            "choices": [("50 m", True), ("150 m", False), ("25 m", False), ("60 m", False)],
            "explanation": r"\(2(15 + 10) = 2(25) = 50\) m. The trap 150 is the area; 25 forgets to double. Pro tip: half the perimeter equals length plus width, so doubling \(25\) gives \(50\) -- a handy check.",
        },
        # --- Triangles & polygons ---
        {
            "text": r"A triangle has sides \(6\) cm, \(8\) cm, and \(10\) cm. What is its perimeter?",
            "difficulty": 1,
            "choices": [("24 cm", True), ("240 cm", False), ("18 cm", False), ("48 cm", False)],
            "explanation": r"Add all three sides: \(6 + 8 + 10 = 24\) cm. The trap 240 multiplies the sides; 48 doubles. There is no special triangle-perimeter formula -- just sum the sides. Pro tip: for ANY polygon, the perimeter is simply the sum of every side.",
        },
        {
            "text": r"A triangle has sides \(13\) cm, \(13\) cm, and \(10\) cm. What is its perimeter?",
            "difficulty": 1,
            "choices": [("36 cm", True), ("33 cm", False), ("169 cm", False), ("26 cm", False)],
            "explanation": r"\(13 + 13 + 10 = 36\) cm. The trap 33 misses one of the 13s; 169 squares a side. Pro tip: count the sides first (three here), then make sure your sum has exactly that many numbers in it.",
        },
        {
            "text": r"A pentagon has sides \(4\), \(6\), \(5\), \(7\), and \(3\). What is its perimeter?",
            "difficulty": 2,
            "choices": [("25 units", True), ("20 units", False), ("30 units", False), ("22 units", False)],
            "explanation": r"A pentagon has five sides; add them all: \(4 + 6 + 5 + 7 + 3 = 25\) units. The trap 20 drops a side; 30 over-adds. Pro tip: list the sides and check each off as you add, so none is skipped or double-counted.",
        },
        {
            "text": r"An equilateral triangle has sides of \(7\) cm each. What is its perimeter?",
            "difficulty": 1,
            "choices": [("21 cm", True), ("14 cm", False), ("49 cm", False), ("7 cm", False)],
            "explanation": r"All three sides equal 7, so \(P = 3 \times 7 = 21\) cm. The trap 14 doubles; 49 squares a side. Pro tip: 'equilateral' means all sides equal -- multiply one side by 3.",
        },
        # --- Regular polygons ---
        {
            "text": r"A regular hexagon has sides of \(5\) cm each. What is its perimeter?",
            "difficulty": 1,
            "choices": [("30 cm", True), ("25 cm", False), ("11 cm", False), ("35 cm", False)],
            "explanation": r"A regular hexagon has 6 equal sides: \(P = 6 \times 5 = 30\) cm. The trap 25 uses 5 sides (a pentagon); 11 just adds \(6+5\). Pro tip: use \(P = n \times s\) -- a hexagon's \(n\) is 6, so multiply by 6.",
        },
        {
            "text": r"A regular pentagon has sides of \(8\) cm each. What is its perimeter?",
            "difficulty": 1,
            "choices": [("40 cm", True), ("13 cm", False), ("32 cm", False), ("48 cm", False)],
            "explanation": r"A pentagon has 5 sides: \(5 \times 8 = 40\) cm. The trap 32 uses 4 sides; 13 adds \(5+8\). Pro tip: match the polygon to its side count -- pentagon 5, hexagon 6, octagon 8.",
        },
        {
            "text": r"A stop sign is a regular octagon with sides of \(12\) in each. What is its perimeter?",
            "difficulty": 2,
            "choices": [("96 in", True), ("84 in", False), ("48 in", False), ("20 in", False)],
            "explanation": r"A stop sign (octagon) has 8 sides: \(8 \times 12 = 96\) in. The trap 48 uses 4 sides; 20 adds \(8+12\). Pro tip: an octagon has 8 sides -- think of an octopus's 8 arms.",
        },
        {
            "text": r"A regular polygon has \(6\) equal sides and a perimeter of \(48\) cm. How long is each side?",
            "difficulty": 2,
            "choices": [("8 cm", True), ("6 cm", False), ("42 cm", False), ("288 cm", False)],
            "explanation": r"Reverse \(P = n \times s\): \(s = P / n = 48 / 6 = 8\) cm. The trap 42 subtracts (\(48-6\)); 288 multiplies. Pro tip: given the perimeter of a regular polygon, divide by the number of sides to get one side.",
        },
        # --- Composite / irregular ---
        {
            "text": r"An L-shape has sides \(8\), \(3\), \(5\), \(3\), \(3\), and \(6\) ft. What is its perimeter?",
            "difficulty": 2,
            "choices": [("28 ft", True), ("25 ft", False), ("32 ft", False), ("22 ft", False)],
            "explanation": r"Add every side around the boundary: \(8 + 3 + 5 + 3 + 3 + 6 = 28\) ft. The trap 25 misses a side; 32 over-counts. Pro tip: trace the outline like a pencil walk and count each side exactly once as you go around.",
        },
        {
            "text": r"To find the perimeter of an irregular straight-sided shape, you should:",
            "difficulty": 1,
            "choices": [("Add the lengths of all the sides", True), ("Multiply length by width", False), ("Use \\(\\pi r^2\\)", False), ("Add only the two longest sides", False)],
            "explanation": r"For any straight-sided shape, the perimeter is the sum of all side lengths -- there is no shortcut formula. 'Multiply length by width' is AREA, and \(\pi r^2\) is a circle's area. Pro tip: walk the whole boundary and add; multiplying is for area, not perimeter.",
        },
        {
            "text": r"A figure has sides \(10\), \(4\), \(6\), \(4\), \(4\), and \(8\) m. What is its perimeter?",
            "difficulty": 2,
            "choices": [("36 m", True), ("32 m", False), ("40 m", False), ("28 m", False)],
            "explanation": r"\(10 + 4 + 6 + 4 + 4 + 8 = 36\) m. The trap 32 drops a side; 40 over-adds. Pro tip: write the sides in order as you go around the shape, then add the list -- this keeps you from missing one.",
        },
        # --- Radius / diameter ---
        {
            "text": r"A circle has a diameter of \(16\) cm. What is its radius?",
            "difficulty": 1,
            "choices": [("8 cm", True), ("32 cm", False), ("16 cm", False), ("4 cm", False)],
            "explanation": r"The radius is half the diameter: \(16 \div 2 = 8\) cm. The trap 32 doubles instead of halving; 16 leaves it unchanged. Pro tip: diameter is the long way across, radius is half -- given a diameter, divide by 2.",
        },
        {
            "text": r"A circle has a radius of \(7\) cm. What is its diameter?",
            "difficulty": 1,
            "choices": [("14 cm", True), ("3.5 cm", False), ("49 cm", False), ("7 cm", False)],
            "explanation": r"The diameter is twice the radius: \(2 \times 7 = 14\) cm. The trap 3.5 halves (the wrong direction); 49 squares it. Pro tip: radius to diameter, multiply by 2; diameter to radius, divide by 2.",
        },
        {
            "text": r"A round table is described as \(60\) inches across. What is its radius?",
            "difficulty": 1,
            "choices": [("30 in", True), ("120 in", False), ("60 in", False), ("15 in", False)],
            "explanation": r"'Across' means the diameter (60), so the radius is half: \(60 \div 2 = 30\) in. The trap 120 doubles; 60 uses the diameter as the radius. Pro tip: 'across' or 'wide' usually describes the diameter -- halve it to get the radius.",
        },
        # --- Circumference ---
        {
            "text": r"A circle has a diameter of \(10\) cm. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [("31.4 cm", True), ("78.5 cm", False), ("15.7 cm", False), ("314 cm", False)],
            "explanation": r"\(C = \pi d = 3.14 \times 10 = 31.4\) cm. The trap 78.5 is the AREA (\(\pi r^2\) with \(r=5\)); 15.7 uses the radius in \(\pi d\). Pro tip: circumference uses \(\pi d\) (or \(2\pi r\)) with no squaring; \(\pi r^2\) is area.",
        },
        {
            "text": r"A circle has a radius of \(7\) cm. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [("43.96 cm", True), ("21.98 cm", False), ("153.86 cm", False), ("14 cm", False)],
            "explanation": r"\(C = 2 \pi r = 2 \times 3.14 \times 7 = 43.96\) cm. The trap 153.86 is the area (\(\pi r^2\)); 14 is just \(2r\) (the diameter); 21.98 forgets the 2. Pro tip: with a radius, use \(2\pi r\) -- don't drop the 2.",
        },
        {
            "text": r"A circle has a radius of \(5\) m. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [("31.4 m", True), ("15.7 m", False), ("78.5 m", False), ("10 m", False)],
            "explanation": r"\(2 \times 3.14 \times 5 = 31.4\) m. The trap 78.5 is the area; 10 is just the diameter. Pro tip: \(2\pi r\) and \(\pi d\) match because \(d = 2r\) -- here \(d = 10\) and \(3.14 \times 10 = 31.4\).",
        },
        {
            "text": r"A circle has a diameter of \(20\) m. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [("62.8 m", True), ("31.4 m", False), ("314 m", False), ("125.6 m", False)],
            "explanation": r"\(C = \pi d = 3.14 \times 20 = 62.8\) m. The trap 314 is the area for \(r = 10\); 31.4 halves the answer. Pro tip: when the diameter is given, \(\pi d\) is the one-step route -- no need to halve first.",
        },
        {
            "text": r"A bicycle wheel has a diameter of \(26\) in. About how far does it travel in one full turn? (Use \(\pi \approx 3.14\).)",
            "difficulty": 3,
            "choices": [("About 81.6 in", True), ("About 163 in", False), ("About 40.8 in", False), ("About 530 in", False)],
            "explanation": r"One full turn covers the circumference: \(3.14 \times 26 \approx 81.6\) in. The trap 163 doubles it; 40.8 halves it; 530 is roughly the area. Pro tip: a wheel's distance per turn IS its circumference -- use \(\pi d\).",
        },
        {
            "text": r"A student finds a circle's circumference (radius 5) by computing \(3.14 \times 5^2 = 78.5\). What is the error?",
            "difficulty": 3,
            "choices": [("They used the area formula instead of circumference", True), ("They used the wrong value of pi", False), ("They forgot to halve the diameter", False), ("Nothing is wrong", False)],
            "explanation": r"\(\pi r^2\) is the AREA formula. Circumference is \(2 \pi r = 2 \times 3.14 \times 5 = 31.4\). Pro tip: if a 'distance around' answer came from squaring the radius, you used the area formula by mistake.",
        },
        {
            "text": r"A circular pond has a radius of \(10\) ft. How long an edging goes around it? (Use \(\pi \approx 3.14\).)",
            "difficulty": 2,
            "choices": [("62.8 ft", True), ("31.4 ft", False), ("314 ft", False), ("20 ft", False)],
            "explanation": r"Edging goes around, so use circumference: \(C = 2 \pi r = 2 \times 3.14 \times 10 = 62.8\) ft. The trap 31.4 forgets the 2; 314 is the area. Pro tip: 'edging' or 'around the pond' means circumference, not area.",
        },
        # --- Working backward ---
        {
            "text": r"A square has a perimeter of \(36\) cm. How long is each side?",
            "difficulty": 2,
            "choices": [("9 cm", True), ("6 cm", False), ("18 cm", False), ("144 cm", False)],
            "explanation": r"Reverse \(P = 4s\): \(s = P / 4 = 36 / 4 = 9\) cm. The trap 6 divides by 6; 18 divides by 2. Pro tip: a square's perimeter divided by 4 gives one side, because all four sides are equal.",
        },
        {
            "text": r"A rectangle has a perimeter of \(26\) cm and a width of \(5\) cm. What is its length?",
            "difficulty": 3,
            "choices": [("8 cm", True), ("21 cm", False), ("13 cm", False), ("16 cm", False)],
            "explanation": r"Half the perimeter is \(l + w = 13\); subtract the width: \(13 - 5 = 8\) cm. The trap 21 subtracts 5 from the full 26 (forgot to halve); 13 stops at \(l+w\). Pro tip: for a rectangle, halve the perimeter FIRST to get \(l+w\), then subtract the known side.",
        },
        {
            "text": r"You have \(40\) ft of fencing for a square pen. How long can each side be?",
            "difficulty": 2,
            "choices": [("10 ft", True), ("4 ft", False), ("160 ft", False), ("20 ft", False)],
            "explanation": r"The fencing is the perimeter, so \(s = 40 / 4 = 10\) ft. The trap 160 multiplies; 20 divides by 2. Pro tip: a square pen's fence is its perimeter -- divide by 4 for each side.",
        },
        {
            "text": r"A circle has a circumference of \(31.4\) cm. Using \(\pi \approx 3.14\), what is its diameter?",
            "difficulty": 3,
            "choices": [("10 cm", True), ("5 cm", False), ("100 cm", False), ("15.7 cm", False)],
            "explanation": r"Reverse \(C = \pi d\): \(d = C / \pi = 31.4 / 3.14 = 10\) cm. The trap 5 gives the radius (\(d/2\)); 100 squares. Pro tip: to undo circumference, divide by \(\pi\) -- that gives the diameter, then halve for the radius.",
        },
        # --- Perimeter vs area ---
        {
            "text": r"For a \(6\) by \(4\) rectangle, what is the perimeter?",
            "difficulty": 1,
            "choices": [("20 units", True), ("24 units", False), ("10 units", False), ("48 units", False)],
            "explanation": r"\(P = 2(6 + 4) = 20\) units. The trap 24 is the AREA (\(6 \times 4\)); 10 forgets to double. Pro tip: the same rectangle has two different answers -- perimeter 20 (around) and area 24 (inside). Read which one is asked.",
        },
        {
            "text": r"Which calculation tells you how much fencing to buy for a yard?",
            "difficulty": 1,
            "choices": [("The perimeter", True), ("The area", False), ("The diagonal", False), ("The volume", False)],
            "explanation": r"Fencing runs along the edges, so you need the perimeter (the distance around). Area would tell you the grass inside, not the length of fence. Pro tip: fence, border, and trim are always perimeter problems.",
        },
        {
            "text": r"Which units are correct for a perimeter?",
            "difficulty": 1,
            "choices": [("Plain units like cm or ft", True), ("Square units like cm² or ft²", False), ("Cubic units like cm³", False), ("No units at all", False)],
            "explanation": r"Perimeter is a length, so it uses plain units (cm, ft). Square units are for area; cubic units are for volume. Pro tip: if your 'distance around' answer has a little \(^2\) on the unit, you actually computed area by mistake.",
        },
        {
            "text": r"A problem asks how much carpet covers a floor. Which measurement is needed?",
            "difficulty": 2,
            "choices": [("Area", True), ("Perimeter", False), ("Circumference", False), ("Diameter", False)],
            "explanation": r"Covering a surface is area (multiply the sides). Perimeter is only the distance around the edge. Pro tip: 'cover / carpet / paint / tile' = area; 'fence / trim / border' = perimeter.",
        },
        # --- Real-world / cost ---
        {
            "text": r"A rectangular yard is \(30\) ft by \(20\) ft. How many feet of fence go around it?",
            "difficulty": 2,
            "choices": [("100 ft", True), ("600 ft", False), ("50 ft", False), ("120 ft", False)],
            "explanation": r"Fencing is the perimeter: \(P = 2(30 + 20) = 100\) ft. The trap 600 is the area (\(30 \times 20\)); 50 forgets to double. Pro tip: fencing equals the perimeter -- add the sides and double for a rectangle.",
        },
        {
            "text": r"Fencing costs \(6\) dollars per foot. How much does it cost to fence a yard that needs \(100\) ft of fence?",
            "difficulty": 2,
            "choices": [("600 dollars", True), ("106 dollars", False), ("60 dollars", False), ("166 dollars", False)],
            "explanation": r"Cost is perimeter times price: \(100 \times 6 = 600\) dollars. The trap 106 adds; 60 divides. Pro tip: a fencing-cost problem has two steps -- find the perimeter, then multiply by the price per foot.",
        },
        {
            "text": r"Trim is sewn around a \(5\) ft by \(3\) ft banner. How much trim is needed?",
            "difficulty": 1,
            "choices": [("16 ft", True), ("15 ft", False), ("8 ft", False), ("30 ft", False)],
            "explanation": r"Trim goes around the edge, so use perimeter: \(2(5 + 3) = 16\) ft. The trap 15 is the area (\(5 \times 3\)); 8 forgets to double. Pro tip: 'trim around' means perimeter; multiply only if it says 'cover'.",
        },
        {
            "text": r"A round garden has a radius of \(4\) ft. How much edging goes around it? (Use \(\pi \approx 3.14\).)",
            "difficulty": 2,
            "choices": [("25.12 ft", True), ("12.56 ft", False), ("50.24 ft", False), ("8 ft", False)],
            "explanation": r"Edging around a circle is the circumference: \(2 \times 3.14 \times 4 = 25.12\) ft. The trap 50.24 doubles; 12.56 forgets the 2 (\(\pi r\)). Pro tip: circular border or edging uses \(2\pi r\).",
        },
        {
            "text": r"Baseboard costs \(3\) dollars per foot. A square room has a perimeter of \(48\) ft. What is the baseboard cost?",
            "difficulty": 3,
            "choices": [("144 dollars", True), ("51 dollars", False), ("16 dollars", False), ("96 dollars", False)],
            "explanation": r"Baseboard follows the perimeter, so cost is \(48 \times 3 = 144\) dollars. The trap 51 adds; 16 divides by 3. Pro tip: like fencing, baseboard cost is the perimeter times the price per foot.",
        },
        # --- Concept / formula ---
        {
            "text": r"Which formula gives the circumference of a circle?",
            "difficulty": 1,
            "choices": [(r"\(C = \pi d\)", True), (r"\(C = \pi r^2\)", False), (r"\(C = l \times w\)", False), (r"\(C = \tfrac{1}{2}bh\)", False)],
            "explanation": r"Circumference is \(C = \pi d\) (or \(2\pi r\)). \(\pi r^2\) is the AREA -- note the square. Pro tip: circumference has no squaring; if you see \(r^2\), that is area, not the distance around.",
        },
        {
            "text": r"Which formula gives the perimeter of a rectangle?",
            "difficulty": 1,
            "choices": [(r"\(P = 2(l + w)\)", True), (r"\(P = l \times w\)", False), (r"\(P = 4s\)", False), (r"\(P = \pi d\)", False)],
            "explanation": r"A rectangle's perimeter is \(2(l + w)\). \(4s\) is for a square (equal sides), and \(l \times w\) is the area. Pro tip: a rectangle has two different side lengths, so add length and width, then double.",
        },
        {
            "text": r"Perimeter measures which of the following?",
            "difficulty": 1,
            "choices": [("The distance around a shape", True), ("The surface inside a shape", False), ("The space a solid fills", False), ("The number of corners", False)],
            "explanation": r"Perimeter is the total distance around the outside edge of a flat shape. The surface inside is area; the space a solid fills is volume. Pro tip: perimeter = a walk all the way around the boundary.",
        },
        {
            "text": r"A regular octagon has a perimeter of \(96\) in. How long is each side?",
            "difficulty": 2,
            "choices": [("12 in", True), ("8 in", False), ("88 in", False), ("16 in", False)],
            "explanation": r"An octagon has 8 sides: \(s = 96 / 8 = 12\) in. The trap 8 divides the wrong way; 88 subtracts. Pro tip: a regular polygon's side = perimeter divided by the number of sides (8 for an octagon).",
        },
        {
            "text": r"A circle has a radius of \(3\) cm. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [("18.84 cm", True), ("9.42 cm", False), ("28.26 cm", False), ("6 cm", False)],
            "explanation": r"\(C = 2 \pi r = 2 \times 3.14 \times 3 = 18.84\) cm. The trap 28.26 is the area (\(\pi r^2\)); 9.42 forgets the 2 (\(\pi r\)). Pro tip: \(2\pi r\) for circumference -- always include the 2 when you start from the radius.",
        },
        {
            "text": r"A rectangle is \(9\) m by \(6\) m. What is the difference between its area and its perimeter (as numbers)?",
            "difficulty": 3,
            "choices": [("24 (area 54, perimeter 30)", True), ("0 (they are equal)", False), ("54 (area only)", False), ("30 (perimeter only)", False)],
            "explanation": r"Area \(= 9 \times 6 = 54\); perimeter \(= 2(9 + 6) = 30\); difference \(= 54 - 30 = 24\). This shows area and perimeter are different quantities (and different units). Pro tip: never assume the two are related -- compute each with its own formula.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Perimeter & Circumference Mastery course (MCQ only)."

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
