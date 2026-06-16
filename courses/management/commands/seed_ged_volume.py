"""
Seed a dedicated GED Geometry course on VOLUME and SURFACE AREA -- the third
course in the geometry track, after Area and Perimeter & Circumference.

12 lessons, ~42 multiple-choice questions, labeled 3D-solid diagrams,
interactive self-checks, case studies, and common-mistake callouts. Every answer
explanation teaches the method, names the tempting wrong answer, and ends with a
Pro tip. Multiple choice only.

Run:
    python manage.py seed_ged_volume
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Volume & Surface Area Mastery",
    "slug": "ged-geometry-volume-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep GED Geometry course on three-dimensional solids. Students learn what volume and "
        "surface area mean, then master the formulas for boxes, cubes, cylinders, cones, and "
        "spheres, plus surface area from nets. The course stresses the big idea that prism volume "
        "is base area times height, tells volume apart from surface area, and applies both to "
        "real-world filling, capacity, and wrapping problems. Every solid has a labeled diagram, "
        "every lesson has an interactive self-check, and every practice answer explains the method "
        "and adds a Pro tip. The GED provides a formula sheet, so the focus is on choosing and "
        "using the right formula."
    ),
    "lessons": [
        (
            "1. What Volume Means: Cubic Units",
            r"""
**Volume** is the amount of space a three-dimensional (3D) solid takes up -- how much it can hold or how much material fills it. Because space has three directions (length, width, height), volume is measured in **cubic units**, written with a small \(^3\), like \(\text{cm}^3\) or \(\text{ft}^3\).

The simplest way to picture volume is to count **unit cubes** -- cubes that are 1 unit on every edge.

Worked example: a box that is 4 units long, 3 units wide, and 2 units tall holds
\[
4 \times 3 \times 2 = 24 \text{ unit cubes},
\]
so its volume is 24 cubic units. You can think of it as 2 layers, each holding \(4 \times 3 = 12\) cubes.

Volume is different from **area** (a flat surface, square units) and **perimeter** (a distance around, plain units). Volume fills a solid, so it always uses cubic units.

Case study - a shipping carton: knowing how many 1-foot cubes fit inside a carton tells you its volume in cubic feet, which decides how much it can pack.

Common mistake: using square units for volume. A solid is filled in 3 directions, so the unit is cubed: \(\text{cm}^3\), not \(\text{cm}^2\).

[[check:A box is 4 units long, 3 wide, and 2 tall. How many unit cubes fill it?|24;;24 cubic units|Multiply the three dimensions: \(4 \times 3 \times 2\).]]
            """,
        ),
        (
            "2. Volume of Rectangular Prisms (Boxes)",
            r"""
A **rectangular prism** (a box) has a volume of length times width times height:
\[
V = l \times w \times h.
\]

[[figure:volume_box|Multiply the three dimensions to fill the box with unit cubes.]]

Worked example: a box 5 cm by 4 cm by 3 cm has volume
\[
V = 5 \times 4 \times 3 = 60 \text{ cm}^3.
\]

The order does not matter -- multiplication can be done in any order -- so \(5 \times 4 \times 3\) and \(3 \times 4 \times 5\) both give 60.

Case study - an aquarium 24 in long, 12 in wide, and 16 in tall holds
\[
24 \times 12 \times 16 = 4608 \text{ in}^3 \text{ of water}.
\]

Common mistake: adding the dimensions instead of multiplying. \(5 + 4 + 3 = 12\) is not the volume; multiply all three.

[[check:A box is 6 cm by 5 cm by 4 cm. What is its volume in cubic cm?|120;;120 cm3|Multiply length, width, and height: \(6 \times 5 \times 4\).]]
            """,
        ),
        (
            "3. Volume of a Cube",
            r"""
A **cube** is a box whose length, width, and height are all the same. Since all three edges equal \(s\), its volume is
\[
V = s \times s \times s = s^3.
\]

[[figure:volume_cube|All three edges are equal, so cube the side length.]]

Worked example: a cube with edge 4 cm has volume
\[
V = 4^3 = 4 \times 4 \times 4 = 64 \text{ cm}^3.
\]

Remember that \(s^3\) means multiply \(s\) by itself **three** times, not multiply by 3. For \(s = 4\), that is \(64\), not \(12\).

Case study - a storage cube 3 ft on each side holds \(3^3 = 27 \text{ ft}^3\).

Common mistake: computing \(s \times 3\) instead of \(s \times s \times s\). The exponent 3 means three factors, not "times three."

[[check:A cube has an edge of 5 cm. What is its volume in cubic cm?|125;;125 cm3|Cube the edge: \(5 \times 5 \times 5\).]]
            """,
        ),
        (
            "4. The Big Idea: Base Area times Height",
            r"""
There is one idea behind almost every volume formula: for any solid with the **same cross-section all the way up** (a prism or cylinder), the volume is the **area of the base** times the **height**:
\[
V = B \times h,
\]
where \(B\) is the area of the base and \(h\) is the height.

This is why a box is \(V = lwh\): the base is a rectangle of area \(l \times w\), and you stack it up \(h\) high.

Worked example (triangular prism): a prism whose base is a triangle of area \(6 \text{ cm}^2\) and whose length is 10 cm has volume
\[
V = B \times h = 6 \times 10 = 60 \text{ cm}^3.
\]

Worked example (any prism): if the base area is \(15 \text{ in}^2\) and the height is 4 in, then \(V = 15 \times 4 = 60 \text{ in}^3\).

Case study - a swimming pool with a flat bottom: find the area of the bottom, then multiply by the depth to get the water volume.

Common mistake: using a side length instead of the base **area**. First find the area of the base shape, then multiply by the height.

[[check:A prism has a base area of 15 square inches and a height of 4 inches. What is its volume in cubic inches?|60;;60 in3|Volume of a prism is base area times height: \(15 \times 4\).]]
            """,
        ),
        (
            "5. Volume of a Cylinder",
            r"""
A **cylinder** is like a circular prism: its base is a circle, so its volume is the circle's area (\(\pi r^2\)) times the height:
\[
V = \pi r^2 h.
\]

[[figure:cylinder_volume|Find the circular base area, then multiply by the height.]]

Use \(\pi \approx 3.14\) unless told otherwise. Square the radius **first**, multiply by \(\pi\), then by the height.

Worked example: a cylinder with radius 3 cm and height 10 cm has volume
\[
V = \pi r^2 h = 3.14 \times 3^2 \times 10 = 3.14 \times 9 \times 10 = 282.6 \text{ cm}^3.
\]

If a problem gives the **diameter**, halve it first to get the radius.

Case study - a soup can with radius 4 cm and height 11 cm holds \(3.14 \times 16 \times 11 \approx 552.6 \text{ cm}^3\).

Common mistake: forgetting to square the radius, or doubling it instead. \(r^2\) means \(r \times r\). For \(r = 3\), that is 9, not 6.

[[check:A cylinder has radius 2 cm and height 5 cm. Using 3.14 for pi, what is its volume in cubic cm?|62.8;;62.80 cm3|Compute \(3.14 \times 2^2 \times 5 = 3.14 \times 4 \times 5\).]]
            """,
        ),
        (
            "6. Volume of a Cone",
            r"""
A **cone** has a circular base and narrows to a point. It holds exactly **one-third** as much as a cylinder with the same base and height:
\[
V = \tfrac{1}{3} \pi r^2 h.
\]

[[figure:volume_cone|A cone is one-third of the matching cylinder.]]

Worked example: a cone with radius 3 cm and height 4 cm has volume
\[
V = \tfrac{1}{3} \times 3.14 \times 3^2 \times 4 = \tfrac{1}{3} \times 3.14 \times 9 \times 4 = \tfrac{1}{3}(113.04) = 37.68 \text{ cm}^3.
\]

A good shortcut: compute the cylinder volume first (\(\pi r^2 h\)), then divide by 3.

Case study - an ice cream cone or a paper cup: its capacity uses the cone formula, which is why a cone holds less than a can of the same size.

Common mistake: forgetting the \(\tfrac{1}{3}\). Without it you get the cylinder's volume, which is three times too big.

[[check:A cone has radius 3 cm and height 4 cm. Using 3.14 for pi, what is its volume in cubic cm?|37.68;;37.68 cm3|Find \(\pi r^2 h\), then divide by 3.]]
            """,
        ),
        (
            "7. Volume of a Sphere",
            r"""
A **sphere** is a perfectly round ball. Its volume depends only on the radius:
\[
V = \tfrac{4}{3} \pi r^3.
\]

[[figure:volume_sphere|Cube the radius, multiply by pi, then by four-thirds.]]

Note that the radius is **cubed** here (\(r^3\)), because a sphere fills space in all three directions.

Worked example: a sphere with radius 3 cm has volume
\[
V = \tfrac{4}{3} \times 3.14 \times 3^3 = \tfrac{4}{3} \times 3.14 \times 27 = \tfrac{4}{3}(84.78) = 113.04 \text{ cm}^3.
\]

A clear order of steps: cube the radius, multiply by \(\pi\), then multiply by \(\tfrac{4}{3}\) (or by 4 and divide by 3).

Case study - a basketball or a globe: its volume uses the sphere formula with the radius (half the diameter).

Common mistake: squaring the radius instead of cubing it. A sphere uses \(r^3\) (three factors), not \(r^2\).

[[check:A sphere has radius 3 cm. Using 3.14 for pi, what is its volume in cubic cm?|113.04;;113.04 cm3|Use \(\tfrac{4}{3} \times 3.14 \times 3^3\).]]
            """,
        ),
        (
            "8. What Surface Area Means: Nets",
            r"""
**Surface area** is the total area of the **outside** of a solid -- every face added together. Because each face is a flat surface, surface area is measured in **square units** (like area), not cubic units.

A great way to see surface area is a **net**: the solid unfolded flat so you can see all its faces at once.

[[figure:surface_net|Unfold the box and add the area of all six faces.]]

A box has 6 faces in 3 matching pairs: top and bottom, front and back, and the two sides. To find the surface area, find the area of each face and add them all.

Worked example: a box 5 by 4 by 3 has three different face sizes:
\[
5 \times 4 = 20, \qquad 5 \times 3 = 15, \qquad 4 \times 3 = 12.
\]
Each appears twice, so
\[
SA = 2(20 + 15 + 12) = 2(47) = 94 \text{ square units}.
\]

Case study - gift wrapping: the paper needed to cover a box (with no overlap) is its surface area.

Common mistake: confusing surface area with volume. Surface area covers the outside (square units); volume fills the inside (cubic units).

[[check:A box is 5 by 4 by 3. What is its surface area in square units?|94;;94 square units|Add the three face areas (20, 15, 12) and double: \(2(20+15+12)\).]]
            """,
        ),
        (
            "9. Surface Area of Boxes and Cubes",
            r"""
For a **rectangular prism** (box), surface area adds the three pairs of faces:
\[
SA = 2(lw + lh + wh).
\]

Worked example: a box 6 by 4 by 2 has
\[
SA = 2(6\cdot4 + 6\cdot2 + 4\cdot2) = 2(24 + 12 + 8) = 2(44) = 88 \text{ square units}.
\]

For a **cube**, all 6 faces are identical squares of area \(s^2\), so
\[
SA = 6 s^2.
\]
A cube with edge 5 cm has \(SA = 6 \times 5^2 = 6 \times 25 = 150 \text{ cm}^2\).

Case study - painting a crate: the amount of paint depends on the surface area of all the faces you cover.

Common mistake: forgetting that each face has a partner. A box has 6 faces, so multiply the three distinct face areas by 2 (or, for a cube, by 6).

[[check:A cube has an edge of 5 cm. What is its surface area in square cm?|150;;150 cm2|Use \(6 s^2 = 6 \times 5^2\).]]
            """,
        ),
        (
            "10. Surface Area of a Cylinder",
            r"""
A cylinder's surface has three parts: the **top** circle, the **bottom** circle, and the **side** that wraps around. Unrolling the side gives a rectangle whose width is the circumference (\(2\pi r\)) and whose height is \(h\).

[[figure:surface_cylinder|Two circles for the ends plus a rectangle for the wrap-around.]]

Putting the pieces together:
\[
SA = \underbrace{2\pi r^2}_{\text{two circles}} + \underbrace{2\pi r h}_{\text{the wrap}}.
\]

Worked example: a cylinder with radius 3 cm and height 10 cm has
\[
SA = 2(3.14)(3^2) + 2(3.14)(3)(10) = 56.52 + 188.4 = 244.92 \text{ cm}^2.
\]

A label on a can (with no top or bottom) is just the wrap-around part, \(2\pi r h\).

Case study - making a closed tin can: the metal needed is the full surface area, both circles plus the side.

Common mistake: including only the side or only the circles. A closed cylinder needs both: two circles **and** the wrap-around rectangle.

[[check:A cylinder has radius 2 cm and height 5 cm. Using 3.14 for pi, what is its surface area in square cm?|87.92;;87.92 cm2|Use \(2\pi r^2 + 2\pi r h = 2(3.14)(4) + 2(3.14)(2)(5)\).]]
            """,
        ),
        (
            "11. Volume vs. Surface Area; Real-World",
            r"""
Volume and surface area answer different questions, and the GED tests whether you can tell them apart.

- **Volume** = how much a solid **holds or fills**. Units: cubic (cm\(^3\), ft\(^3\)).
- **Surface area** = how much covers the **outside**. Units: square (cm\(^2\), ft\(^2\)).

How to decide which a word problem wants:
- **Volume** words: fill, hold, capacity, how much water/sand/air, contents.
- **Surface area** words: cover, wrap, paint, label, material to build the outside.

Worked example - capacity: a tank 2 m by 3 m by 1.5 m holds
\[
2 \times 3 \times 1.5 = 9 \text{ m}^3 \text{ of water}.
\]

Worked example - wrapping: covering that same tank's outside would use its surface area, not its volume.

Quick comparison for a 3 by 3 by 3 cube:
\[
V = 27 \text{ cm}^3, \qquad SA = 6(3^2) = 54 \text{ cm}^2.
\]

Common mistake: giving volume when the question asks how much material covers the outside (or vice versa). Read for the keyword and check the units.

[[check:A tank is 2 m by 3 m by 1.5 m. How many cubic meters of water can it hold?|9;;9 m3|Volume is \(2 \times 3 \times 1.5\).]]
            """,
        ),
        (
            "12. GED Strategy: Pick the Solid, Pick the Formula",
            r"""
The GED gives you a **formula sheet**, so your job is to choose the right formula and put the numbers in correctly. Use this routine:

- **What solid is it?** Box, cube, cylinder, cone, or sphere.
- **Volume or surface area?** Fill/hold = volume (cubic units); cover/wrap = surface area (square units).
- **Radius or diameter?** Circles need the radius; halve the diameter if needed.
- **Square or cube the radius?** Cylinder and cone area use \(r^2\); a sphere's volume uses \(r^3\).
- **Any fraction out front?** Cone has \(\tfrac{1}{3}\); sphere has \(\tfrac{4}{3}\).

Volume quick-reference:
- Box: \(V = lwh\)
- Cube: \(V = s^3\)
- Prism / cylinder: \(V = Bh\) (base area times height); cylinder \(= \pi r^2 h\)
- Cone: \(V = \tfrac{1}{3}\pi r^2 h\)
- Sphere: \(V = \tfrac{4}{3}\pi r^3\)

Error analysis: a student finds a cone's volume as \(\pi r^2 h = 3.14 \times 9 \times 4 = 113.04\). They forgot the \(\tfrac{1}{3}\); the real volume is \(\tfrac{1}{3}(113.04) = 37.68 \text{ cm}^3\).

Case study - a silo shaped like a cylinder with a cone on top: find each volume separately, then add. Break a complex solid into simple ones.

Final habit: name the solid and say "fill or cover" before you compute. The right formula does most of the work.

[[check:Which formula gives the volume of a cylinder?|pi r^2 h;;πr²h;;pir2h|A cylinder is base area (pi r squared) times height.]]
            """,
        ),
    ],
    "mcqs": [
        # --- Boxes ---
        {
            "text": r"A box is \(5\) cm by \(4\) cm by \(3\) cm. What is its volume?",
            "difficulty": 1,
            "choices": [(r"\(60\ \text{cm}^3\)", True), (r"\(12\ \text{cm}^3\)", False), (r"\(47\ \text{cm}^3\)", False), (r"\(120\ \text{cm}^3\)", False)],
            "explanation": r"Volume of a box is length times width times height: \(5 \times 4 \times 3 = 60\ \text{cm}^3\). The trap 12 ADDS the dimensions (\(5+4+3\)); 47 is the surface-area face sum. Pro tip: volume multiplies all three dimensions and uses CUBIC units (\(\text{cm}^3\)).",
        },
        {
            "text": r"A box is \(6\) cm by \(5\) cm by \(4\) cm. What is its volume?",
            "difficulty": 1,
            "choices": [(r"\(120\ \text{cm}^3\)", True), (r"\(15\ \text{cm}^3\)", False), (r"\(74\ \text{cm}^3\)", False), (r"\(60\ \text{cm}^3\)", False)],
            "explanation": r"\(6 \times 5 \times 4 = 120\ \text{cm}^3\). The trap 15 adds the dimensions; 74 is half the surface area. Pro tip: multiply in any order -- \(6 \times 5 = 30\), then \(\times 4 = 120\).",
        },
        {
            "text": r"A box is \(4\) units long, \(3\) wide, and \(2\) tall. How many unit cubes fill it?",
            "difficulty": 1,
            "choices": [("24", True), ("9", False), ("12", False), ("18", False)],
            "explanation": r"\(4 \times 3 \times 2 = 24\) unit cubes. The trap 9 adds the dimensions; 12 multiplies only two of the three. Pro tip: think in layers -- one \(4 \times 3 = 12\) layer, stacked 2 high, gives 24.",
        },
        {
            "text": r"A crate is \(10\) ft by \(2\) ft by \(3\) ft. What is its volume?",
            "difficulty": 1,
            "choices": [(r"\(60\ \text{ft}^3\)", True), (r"\(15\ \text{ft}^3\)", False), (r"\(30\ \text{ft}^3\)", False), (r"\(50\ \text{ft}^3\)", False)],
            "explanation": r"\(10 \times 2 \times 3 = 60\ \text{ft}^3\). The trap 15 adds; 30 multiplies only two of the dimensions. Pro tip: every box volume needs all THREE measurements multiplied together.",
        },
        {
            "text": r"A student adds \(5 + 4 + 3 = 12\) to find the volume of a \(5 \times 4 \times 3\) box. What is the error?",
            "difficulty": 2,
            "choices": [("They added the dimensions instead of multiplying them", True), ("They used the wrong units", False), ("They forgot to divide by 3", False), ("Nothing is wrong", False)],
            "explanation": r"Volume multiplies the dimensions: \(5 \times 4 \times 3 = 60\), not \(5 + 4 + 3 = 12\). Adding is the most common volume slip. Pro tip: 'how much it holds' = volume = multiply all three dimensions, in cubic units.",
        },
        # --- Cubes ---
        {
            "text": r"A cube has an edge of \(3\) cm. What is its volume?",
            "difficulty": 1,
            "choices": [(r"\(27\ \text{cm}^3\)", True), (r"\(9\ \text{cm}^3\)", False), (r"\(6\ \text{cm}^3\)", False), (r"\(18\ \text{cm}^3\)", False)],
            "explanation": r"A cube's volume is \(s^3 = 3^3 = 3 \times 3 \times 3 = 27\ \text{cm}^3\). The trap 9 squares the edge (\(3^2\), an area); 6 doubles it. Pro tip: \(s^3\) means three factors -- a cube fills space in 3 directions.",
        },
        {
            "text": r"A cube has an edge of \(5\) cm. What is its volume?",
            "difficulty": 1,
            "choices": [(r"\(125\ \text{cm}^3\)", True), (r"\(25\ \text{cm}^3\)", False), (r"\(15\ \text{cm}^3\)", False), (r"\(75\ \text{cm}^3\)", False)],
            "explanation": r"\(5^3 = 5 \times 5 \times 5 = 125\ \text{cm}^3\). The trap 25 squares the edge; 15 multiplies by 3. Pro tip: knowing \(5^3 = 125\) and \(4^3 = 64\) by heart speeds up cube questions.",
        },
        {
            "text": r"A storage cube is \(3\) ft on each side. What is its volume?",
            "difficulty": 1,
            "choices": [(r"\(27\ \text{ft}^3\)", True), (r"\(9\ \text{ft}^3\)", False), (r"\(12\ \text{ft}^3\)", False), (r"\(81\ \text{ft}^3\)", False)],
            "explanation": r"\(3^3 = 27\ \text{ft}^3\). The trap 9 is \(3^2\) (a single face area); 12 is \(3 \times 4\). Pro tip: a cube has equal edges, so its volume is one edge CUBED, never squared.",
        },
        {
            "text": r"What does \(s^3\) mean for a cube of side \(4\)?",
            "difficulty": 2,
            "choices": [(r"\(4 \times 4 \times 4 = 64\)", True), (r"\(4 \times 3 = 12\)", False), (r"\(4 + 4 + 4 = 12\)", False), (r"\(4 \times 4 = 16\)", False)],
            "explanation": r"The exponent 3 means three factors: \(4 \times 4 \times 4 = 64\). It is not 'times 3' (12) and not 'squared' (16). Pro tip: the exponent counts how many times you multiply the base by itself -- \(^3\) means three of them.",
        },
        # --- Base area times height ---
        {
            "text": r"A prism has a base area of \(15\ \text{in}^2\) and a height of \(4\) in. What is its volume?",
            "difficulty": 2,
            "choices": [(r"\(60\ \text{in}^3\)", True), (r"\(19\ \text{in}^3\)", False), (r"\(30\ \text{in}^3\)", False), (r"\(11\ \text{in}^3\)", False)],
            "explanation": r"Volume of a prism is base area times height: \(V = B \times h = 15 \times 4 = 60\ \text{in}^3\). The trap 19 adds; 30 halves. Pro tip: ANY prism (box, cylinder, triangular) is base area times height.",
        },
        {
            "text": r"A triangular prism has a base (triangle) of area \(6\ \text{cm}^2\) and length \(10\) cm. What is its volume?",
            "difficulty": 2,
            "choices": [(r"\(60\ \text{cm}^3\)", True), (r"\(16\ \text{cm}^3\)", False), (r"\(30\ \text{cm}^3\)", False), (r"\(600\ \text{cm}^3\)", False)],
            "explanation": r"\(V = B \times h = 6 \times 10 = 60\ \text{cm}^3\). The trap 16 adds; 30 halves. Pro tip: the 'base' here is the triangle's AREA (already given as 6) -- just multiply it by the length, no extra halving.",
        },
        {
            "text": r"For a prism, the volume equals:",
            "difficulty": 1,
            "choices": [("The base area times the height", True), ("The sum of all edges", False), ("The base perimeter times height", False), ("Length plus width plus height", False)],
            "explanation": r"Any prism's volume is \(V = B \times h\), the area of the base times the height. 'Base perimeter times height' gives the side surface area, not the volume. Pro tip: find the base shape's AREA first, then multiply by how tall the prism is.",
        },
        # --- Cylinders ---
        {
            "text": r"A cylinder has radius \(3\) cm and height \(10\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 2,
            "choices": [(r"\(282.6\ \text{cm}^3\)", True), (r"\(94.2\ \text{cm}^3\)", False), (r"\(188.4\ \text{cm}^3\)", False), (r"\(28.26\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \pi r^2 h = 3.14 \times 3^2 \times 10 = 3.14 \times 9 \times 10 = 282.6\ \text{cm}^3\). The trap 94.2 forgets to square the radius (uses 3, not 9); 188.4 is the side surface area. Pro tip: square the radius FIRST, then times \(\pi\), then times the height.",
        },
        {
            "text": r"A cylinder has radius \(2\) cm and height \(5\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 2,
            "choices": [(r"\(62.8\ \text{cm}^3\)", True), (r"\(31.4\ \text{cm}^3\)", False), (r"\(20\ \text{cm}^3\)", False), (r"\(125.6\ \text{cm}^3\)", False)],
            "explanation": r"\(3.14 \times 2^2 \times 5 = 3.14 \times 4 \times 5 = 62.8\ \text{cm}^3\). The trap 31.4 forgets to square the radius; 20 drops \(\pi\). Pro tip: do \(r^2\) before anything else -- \(2^2 = 4\); using the radius without squaring is the usual slip.",
        },
        {
            "text": r"A cylinder has radius \(5\) m and height \(4\) m. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 2,
            "choices": [(r"\(314\ \text{m}^3\)", True), (r"\(62.8\ \text{m}^3\)", False), (r"\(125.6\ \text{m}^3\)", False), (r"\(78.5\ \text{m}^3\)", False)],
            "explanation": r"\(3.14 \times 5^2 \times 4 = 3.14 \times 25 \times 4 = 314\ \text{m}^3\). The trap 62.8 forgets to square the radius; 125.6 is the side surface area. Pro tip: \(5^2 = 25\) -- squaring the radius is the step most often skipped in cylinder volume.",
        },
        {
            "text": r"A cylinder has a diameter of \(6\) cm and a height of \(10\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 3,
            "choices": [(r"\(282.6\ \text{cm}^3\)", True), (r"\(1130.4\ \text{cm}^3\)", False), (r"\(188.4\ \text{cm}^3\)", False), (r"\(94.2\ \text{cm}^3\)", False)],
            "explanation": r"Halve the diameter first: \(r = 3\). Then \(3.14 \times 3^2 \times 10 = 3.14 \times 9 \times 10 = 282.6\ \text{cm}^3\). The trap 1130.4 uses \(r = 6\) (forgot to halve the diameter); 94.2 forgets to square. Pro tip: given a diameter, ALWAYS halve it to the radius before using \(\pi r^2 h\).",
        },
        # --- Cones ---
        {
            "text": r"A cone has radius \(3\) cm and height \(4\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 2,
            "choices": [(r"\(37.68\ \text{cm}^3\)", True), (r"\(113.04\ \text{cm}^3\)", False), (r"\(12.56\ \text{cm}^3\)", False), (r"\(28.26\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \tfrac{1}{3}\pi r^2 h = \tfrac{1}{3}(3.14)(9)(4) = \tfrac{1}{3}(113.04) = 37.68\ \text{cm}^3\). The trap 113.04 forgets the \(\tfrac{1}{3}\) (that is the cylinder volume). Pro tip: a cone is one-third of the matching cylinder -- compute the cylinder, then divide by 3.",
        },
        {
            "text": r"A cone and a cylinder have the same base and height. The cone holds:",
            "difficulty": 2,
            "choices": [("One-third as much as the cylinder", True), ("The same as the cylinder", False), ("Three times the cylinder", False), ("Twice the cylinder", False)],
            "explanation": r"A cone's volume is \(\tfrac{1}{3}\) of the matching cylinder's, because of the \(\tfrac{1}{3}\) in \(V = \tfrac{1}{3}\pi r^2 h\). Pro tip: three cones of ice cream fill one cylinder of the same base and height -- cone = \(\tfrac{1}{3}\) cylinder.",
        },
        {
            "text": r"A student finds a cone's volume (radius 3, height 4) as \(3.14 \times 9 \times 4 = 113.04\). What did they forget?",
            "difficulty": 3,
            "choices": [(r"To multiply by \(\tfrac{1}{3}\)", True), ("To square the radius", False), ("To use pi", False), ("Nothing; it is correct", False)],
            "explanation": r"That \(113.04\) is the CYLINDER volume. A cone needs the \(\tfrac{1}{3}\): \(\tfrac{1}{3}(113.04) = 37.68\). Pro tip: if your cone answer equals the full \(\pi r^2 h\), you forgot to divide by 3.",
        },
        {
            "text": r"A cone has radius \(6\) cm and height \(10\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 3,
            "choices": [(r"\(376.8\ \text{cm}^3\)", True), (r"\(1130.4\ \text{cm}^3\)", False), (r"\(188.4\ \text{cm}^3\)", False), (r"\(120\ \text{cm}^3\)", False)],
            "explanation": r"\(\tfrac{1}{3}(3.14)(6^2)(10) = \tfrac{1}{3}(3.14)(36)(10) = \tfrac{1}{3}(1130.4) = 376.8\ \text{cm}^3\). The trap 1130.4 forgets the \(\tfrac{1}{3}\) (the cylinder). Pro tip: compute \(\pi r^2 h\) first (1130.4), then divide by 3 -- splitting the steps avoids errors.",
        },
        # --- Spheres ---
        {
            "text": r"A sphere has radius \(3\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 3,
            "choices": [(r"\(113.04\ \text{cm}^3\)", True), (r"\(28.26\ \text{cm}^3\)", False), (r"\(84.78\ \text{cm}^3\)", False), (r"\(339.12\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \tfrac{4}{3}\pi r^3 = \tfrac{4}{3}(3.14)(3^3) = \tfrac{4}{3}(3.14)(27) = \tfrac{4}{3}(84.78) = 113.04\ \text{cm}^3\). The trap 28.26 squares instead of cubing (uses 9); 84.78 forgets the \(\tfrac{4}{3}\). Pro tip: a sphere CUBES the radius (\(r^3\)) and has \(\tfrac{4}{3}\) out front.",
        },
        {
            "text": r"In the sphere volume formula, the radius is:",
            "difficulty": 2,
            "choices": [("Cubed (raised to the third power)", True), ("Squared", False), ("Doubled", False), ("Used as is", False)],
            "explanation": r"A sphere's volume uses \(r^3\): \(V = \tfrac{4}{3}\pi r^3\). Squaring would be wrong -- a sphere fills space in three directions. Pro tip: cylinder and cone use \(r^2\) for the circular base, but a sphere's volume uses \(r^3\).",
        },
        {
            "text": r"A sphere has radius \(6\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 3,
            "choices": [(r"\(904.32\ \text{cm}^3\)", True), (r"\(452.16\ \text{cm}^3\)", False), (r"\(226.08\ \text{cm}^3\)", False), (r"\(113.04\ \text{cm}^3\)", False)],
            "explanation": r"\(\tfrac{4}{3}(3.14)(6^3) = \tfrac{4}{3}(3.14)(216) = \tfrac{4}{3}(678.24) = 904.32\ \text{cm}^3\). The trap 452.16 uses \(\tfrac{2}{3}\) instead of \(\tfrac{4}{3}\); 113.04 uses \(r = 3\). Pro tip: \(6^3 = 216\) -- cube the radius first, then multiply by \(\pi\) and \(\tfrac{4}{3}\).",
        },
        # --- Surface area: box & cube ---
        {
            "text": r"A box is \(5\) by \(4\) by \(3\). What is its surface area?",
            "difficulty": 2,
            "choices": [("94 square units", True), ("60 square units", False), ("47 square units", False), ("12 square units", False)],
            "explanation": r"Surface area adds all 6 faces: the distinct areas are \(5\times4=20\), \(5\times3=15\), \(4\times3=12\), each appearing twice: \(SA = 2(20+15+12) = 94\). The trap 60 is the VOLUME; 47 forgets to double. Pro tip: a box has 3 pairs of faces -- add the three distinct areas, then double.",
        },
        {
            "text": r"A box is \(6\) by \(4\) by \(2\). What is its surface area?",
            "difficulty": 2,
            "choices": [("88 square units", True), ("48 square units", False), ("44 square units", False), ("24 square units", False)],
            "explanation": r"\(SA = 2(24 + 12 + 8) = 88\) square units. The trap 48 is the VOLUME (\(6 \times 4 \times 2\)); 44 forgets to double. Pro tip: surface area uses square units and volume uses cubic -- the units tell you which one you found.",
        },
        {
            "text": r"A cube has an edge of \(5\) cm. What is its surface area?",
            "difficulty": 2,
            "choices": [(r"\(150\ \text{cm}^2\)", True), (r"\(125\ \text{cm}^2\)", False), (r"\(25\ \text{cm}^2\)", False), (r"\(30\ \text{cm}^2\)", False)],
            "explanation": r"All 6 faces are \(5^2 = 25\): \(SA = 6 \times 25 = 150\ \text{cm}^2\). The trap 125 is the VOLUME (\(5^3\)); 25 is just one face. Pro tip: a cube's surface area is \(6s^2\) (six square faces); its volume is \(s^3\).",
        },
        {
            "text": r"A cube has an edge of \(3\) cm. What is its surface area?",
            "difficulty": 2,
            "choices": [(r"\(54\ \text{cm}^2\)", True), (r"\(27\ \text{cm}^2\)", False), (r"\(9\ \text{cm}^2\)", False), (r"\(18\ \text{cm}^2\)", False)],
            "explanation": r"\(6 \times 3^2 = 6 \times 9 = 54\ \text{cm}^2\). The trap 27 is the VOLUME (\(3^3\)); 9 is one face. Pro tip: \(6s^2\) for a cube's surface -- six faces, each \(s^2\).",
        },
        {
            "text": r"How many faces does a rectangular box have?",
            "difficulty": 1,
            "choices": [("6", True), ("4", False), ("8", False), ("12", False)],
            "explanation": r"A box has 6 faces, in 3 matching pairs (top/bottom, front/back, two sides). Pro tip: that is exactly why surface area DOUBLES the three distinct face areas -- each face has a partner.",
        },
        # --- Surface area: cylinder ---
        {
            "text": r"A cylinder has radius \(3\) cm and height \(10\) cm. Using \(\pi \approx 3.14\), what is its surface area?",
            "difficulty": 3,
            "choices": [(r"\(244.92\ \text{cm}^2\)", True), (r"\(188.4\ \text{cm}^2\)", False), (r"\(56.52\ \text{cm}^2\)", False), (r"\(282.6\ \text{cm}^2\)", False)],
            "explanation": r"\(SA = 2\pi r^2 + 2\pi r h = 56.52 + 188.4 = 244.92\ \text{cm}^2\). The trap 188.4 is only the side; 56.52 is only the two circles; 282.6 is the VOLUME. Pro tip: a closed cylinder needs BOTH the two circles (\(2\pi r^2\)) and the wrap (\(2\pi r h\)).",
        },
        {
            "text": r"A cylinder has radius \(2\) cm and height \(5\) cm. Using \(\pi \approx 3.14\), what is its surface area?",
            "difficulty": 3,
            "choices": [(r"\(87.92\ \text{cm}^2\)", True), (r"\(62.8\ \text{cm}^2\)", False), (r"\(25.12\ \text{cm}^2\)", False), (r"\(125.6\ \text{cm}^2\)", False)],
            "explanation": r"\(SA = 2(3.14)(4) + 2(3.14)(2)(5) = 25.12 + 62.8 = 87.92\ \text{cm}^2\). The trap 62.8 is only the side; 25.12 only the circles. Pro tip: add the caps and the wrap -- missing one is the usual cylinder surface-area error.",
        },
        {
            "text": r"The surface area of a closed cylinder includes which parts?",
            "difficulty": 2,
            "choices": [("Two circles plus the wrap-around side", True), ("Only the wrap-around side", False), ("Only the two circles", False), ("Just one circle", False)],
            "explanation": r"A closed cylinder has a top circle, a bottom circle, and the curved side: \(2\pi r^2 + 2\pi r h\). A label with no top or bottom would be only the side. Pro tip: 'closed' or 'tin can' means include both circles AND the side.",
        },
        # --- Volume vs surface area / units ---
        {
            "text": r"Volume is measured in which kind of units?",
            "difficulty": 1,
            "choices": [("Cubic units", True), ("Square units", False), ("Plain (linear) units", False), ("No units", False)],
            "explanation": r"Volume fills space in three directions, so it uses cubic units like \(\text{cm}^3\). Square units are for surface area; plain units for length. Pro tip: the little \(^3\) on the unit signals volume -- three dimensions multiplied.",
        },
        {
            "text": r"Which question is asking about VOLUME?",
            "difficulty": 1,
            "choices": [("How much water can the tank hold?", True), ("How much paper covers the box?", False), ("How much trim goes around the lid?", False), ("How long is the edge?", False)],
            "explanation": r"'How much it can hold' is capacity, which is volume. Covering with paper is surface area, and trim around is perimeter. Pro tip: 'hold / fill / capacity / contents' all signal volume.",
        },
        {
            "text": r"A tank is \(2\) m by \(3\) m by \(1.5\) m. How much water can it hold?",
            "difficulty": 2,
            "choices": [(r"\(9\ \text{m}^3\)", True), (r"\(6.5\ \text{m}^3\)", False), (r"\(13\ \text{m}^3\)", False), (r"\(4.5\ \text{m}^3\)", False)],
            "explanation": r"Capacity is volume: \(V = 2 \times 3 \times 1.5 = 9\ \text{m}^3\). The trap 6.5 adds the dimensions; 13 mis-multiplies. Pro tip: 'how much water it holds' is volume -- multiply all three dimensions, even the decimal one.",
        },
        {
            "text": r"You want to gift-wrap a box. Which measurement tells you how much paper you need?",
            "difficulty": 1,
            "choices": [("Surface area", True), ("Volume", False), ("Perimeter", False), ("Height", False)],
            "explanation": r"Wrapping covers the outside, so you need the surface area (square units). Volume is what fills the inside. Pro tip: 'wrap / cover / paint / label' = surface area; 'fill / hold' = volume.",
        },
        {
            "text": r"For a \(3\) by \(3\) by \(3\) cube, which statement is correct?",
            "difficulty": 3,
            "choices": [(r"Volume is \(27\ \text{cm}^3\) and surface area is \(54\ \text{cm}^2\)", True), (r"Volume is \(54\) and surface area is \(27\)", False), (r"Both equal \(9\)", False), (r"Both equal \(27\)", False)],
            "explanation": r"\(V = 3^3 = 27\ \text{cm}^3\) (cubic) and \(SA = 6(3^2) = 54\ \text{cm}^2\) (square). They are different numbers AND different units. Pro tip: keep them straight by their units -- volume is cubic, surface area is square.",
        },
        # --- Real world / mixed ---
        {
            "text": r"An aquarium is \(24\) in by \(12\) in by \(16\) in. What is its volume?",
            "difficulty": 2,
            "choices": [(r"\(4608\ \text{in}^3\)", True), (r"\(52\ \text{in}^3\)", False), (r"\(288\ \text{in}^3\)", False), (r"\(2304\ \text{in}^3\)", False)],
            "explanation": r"\(24 \times 12 \times 16 = 4608\ \text{in}^3\). The trap 52 adds the dimensions; 288 multiplies only two of them. Pro tip: an aquarium's water capacity is volume -- multiply all three measurements.",
        },
        {
            "text": r"A can has radius \(4\) cm and height \(11\) cm. Using \(\pi \approx 3.14\), about how much does it hold?",
            "difficulty": 3,
            "choices": [(r"\(\approx 552.6\ \text{cm}^3\)", True), (r"\(\approx 138.2\ \text{cm}^3\)", False), (r"\(\approx 276.3\ \text{cm}^3\)", False), (r"\(\approx 44\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \pi r^2 h = 3.14 \times 4^2 \times 11 = 3.14 \times 16 \times 11 \approx 552.6\ \text{cm}^3\). The trap 138.2 forgets to square the radius; 276.3 halves. Pro tip: square the radius (\(4^2 = 16\)) before multiplying by \(\pi\) and the height.",
        },
        {
            "text": r"Which formula gives the volume of a sphere?",
            "difficulty": 2,
            "choices": [(r"\(\tfrac{4}{3}\pi r^3\)", True), (r"\(\pi r^2 h\)", False), (r"\(\tfrac{1}{3}\pi r^2 h\)", False), (r"\(6 s^2\)", False)],
            "explanation": r"A sphere's volume is \(\tfrac{4}{3}\pi r^3\). \(\pi r^2 h\) is a cylinder; \(\tfrac{1}{3}\pi r^2 h\) a cone; \(6s^2\) a cube's surface area. Pro tip: the sphere is the one with \(r^3\) and \(\tfrac{4}{3}\) -- no height \(h\) appears.",
        },
        {
            "text": r"Which formula gives the volume of a cylinder?",
            "difficulty": 1,
            "choices": [(r"\(\pi r^2 h\)", True), (r"\(2\pi r h\)", False), (r"\(\tfrac{4}{3}\pi r^3\)", False), (r"\(l \times w \times h\)", False)],
            "explanation": r"A cylinder's volume is base area times height: \(\pi r^2 h\). \(2\pi r h\) is the side surface; \(\tfrac{4}{3}\pi r^3\) a sphere. Pro tip: cylinder volume = circle area (\(\pi r^2\)) stacked \(h\) high.",
        },
        {
            "text": r"A silo is a cylinder with a cone on top. To find its total volume, you should:",
            "difficulty": 2,
            "choices": [("Find each volume separately and add them", True), ("Multiply the two volumes", False), ("Use only the cylinder", False), ("Subtract the cone from the cylinder", False)],
            "explanation": r"Break a composite solid into simple solids, find each volume, then ADD them. Multiplying or subtracting does not apply when one sits on top of the other. Pro tip: for any combined solid, compute each piece's volume and sum.",
        },
        {
            "text": r"A rectangular pool has a flat bottom of area \(40\ \text{m}^2\) and a depth of \(2\) m. What is the water volume?",
            "difficulty": 2,
            "choices": [(r"\(80\ \text{m}^3\)", True), (r"\(42\ \text{m}^3\)", False), (r"\(20\ \text{m}^3\)", False), (r"\(160\ \text{m}^3\)", False)],
            "explanation": r"Volume of a prism is base area times height (depth): \(V = B \times h = 40 \times 2 = 80\ \text{m}^3\). The trap 42 adds; 20 halves. Pro tip: a flat-bottomed pool's water volume is the bottom AREA times the depth.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Volume & Surface Area Mastery course (MCQ only)."

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
