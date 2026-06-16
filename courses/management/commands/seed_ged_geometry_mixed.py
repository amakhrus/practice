"""
Seed the capstone GED Geometry Mixed Review course -- a full mixed practice test
pulling from every geometry strand (area, perimeter & circumference, volume &
surface area, the Pythagorean theorem & coordinate geometry, and angles &
triangles).

Concise formula-recap lessons (reusing existing diagrams) plus a large mixed
question bank. Every answer explanation teaches the method, names the tempting
wrong answer, and ends with a Pro tip. Multiple choice only.

Run:
    python manage.py seed_ged_geometry_mixed
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry Mixed Review: Practice Test (Area, Perimeter, Volume, Angles & More)",
    "slug": "ged-geometry-mixed-review",
    "program": "GED",
    "subject": "math",
    "description": (
        "A capstone GED geometry practice test that mixes every key skill into one comprehensive "
        "review: area, perimeter, circumference, volume, surface area, the Pythagorean theorem, "
        "coordinate geometry (distance, midpoint, slope), and angles and triangles. Free "
        "multiple-choice questions with full worked solutions and pro tips, plus quick formula "
        "recaps for each topic, so you can review all of GED geometry in one place before test day."
    ),
    "lessons": [
        (
            "1. Quick Recap: Area Formulas",
            r"""
**Area** is the surface inside a flat shape, measured in **square units** (\(\text{cm}^2\), \(\text{ft}^2\)).

[[figure:area_rectangle|Area multiplies two lengths and is always in square units.]]

The formulas to know:
- Rectangle: \(A = l \times w\)
- Square: \(A = s^2\)
- Triangle: \(A = \tfrac{1}{2} b h\)
- Parallelogram: \(A = b h\)
- Trapezoid: \(A = \tfrac{1}{2}(b_1 + b_2) h\)
- Circle: \(A = \pi r^2\) (use \(\pi \approx 3.14\))

Common mix-up: forgetting the \(\tfrac{1}{2}\) for a triangle, or using \(2\pi r\) (circumference) instead of \(\pi r^2\) for a circle's area.

[[check:What is the area of a triangle with base 10 and height 8?|40;;40 square units|Use \(\tfrac{1}{2}(10)(8)\).]]
            """,
        ),
        (
            "2. Quick Recap: Perimeter & Circumference",
            r"""
**Perimeter** is the distance **around** a shape, in **plain units** (cm, ft). For a circle, that distance is the **circumference**.

[[figure:circle_circumference|Circumference uses pi times the diameter -- no squaring.]]

The formulas to know:
- Rectangle: \(P = 2(l + w)\)
- Square: \(P = 4s\)
- Any polygon: add all the sides
- Regular polygon: \(P = n \times s\)
- Circle: \(C = \pi d = 2\pi r\)

Common mix-up: using a square unit for perimeter (it is a length), or using \(\pi r^2\) (area) when you needed \(\pi d\) (circumference).

[[check:What is the perimeter of a rectangle 9 by 5?|28;;28 units|Use \(2(9 + 5)\).]]
            """,
        ),
        (
            "3. Quick Recap: Volume & Surface Area",
            r"""
**Volume** is how much a solid holds, in **cubic units** (\(\text{cm}^3\)). **Surface area** is the outside, in **square units**.

[[figure:volume_box|Volume multiplies three dimensions and uses cubic units.]]

The volume formulas to know:
- Box: \(V = l w h\)
- Cube: \(V = s^3\)
- Cylinder: \(V = \pi r^2 h\)
- Cone: \(V = \tfrac{1}{3}\pi r^2 h\)
- Sphere: \(V = \tfrac{4}{3}\pi r^3\)
- Any prism: \(V = B h\) (base area times height)

Surface area: a box is \(2(lw + lh + wh)\); a cube is \(6s^2\).

Common mix-up: giving volume (cubic) when the question asks how much covers the outside (surface area, square), or forgetting the \(\tfrac{1}{3}\) for a cone.

[[check:What is the volume of a box 5 by 3 by 2?|30;;30 cubic units|Multiply all three: \(5 \times 3 \times 2\).]]
            """,
        ),
        (
            "4. Quick Recap: Pythagorean Theorem, Distance & Midpoint",
            r"""
In a **right triangle**, \(a^2 + b^2 = c^2\), where \(c\) is the hypotenuse (opposite the right angle).

[[figure:distance_on_grid|On a grid, distance is the hypotenuse of a right triangle.]]

The tools to know:
- **Hypotenuse:** \(c = \sqrt{a^2 + b^2}\) (add the squares).
- **Missing leg:** \(a = \sqrt{c^2 - b^2}\) (subtract).
- **Distance** between two points: \(d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\) (Pythagoras on the grid).
- **Midpoint:** average the coordinates, \(\left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)\).
- **Slope:** \(\frac{y_2-y_1}{x_2-x_1}\) (rise over run).

Common mix-up: adding when finding a leg (you subtract), or confusing midpoint (average) with distance (subtract and square).

[[check:Find the hypotenuse of a right triangle with legs 6 and 8.|10;;10 units|√(6² + 8²) = √100.]]
            """,
        ),
        (
            "5. Quick Recap: Angles, Lines & Triangles",
            r"""
Most angle problems use one of a handful of rules.

[[figure:triangle_angle_sum|A triangle's three angles always total 180 degrees.]]

The rules to know:
- **Complementary** angles add to \(90^\circ\); **supplementary** add to \(180^\circ\).
- **Vertical angles** (across a crossing) are **equal**.
- **Parallel lines:** corresponding and alternate angles are **equal**; co-interior add to \(180^\circ\).
- **Triangle angles** add to \(180^\circ\).
- **Exterior angle** = sum of the two remote interior angles.
- **Isosceles:** base angles equal. **Equilateral:** all angles \(60^\circ\).

Common mix-up: thinking a triangle's angles total \(360^\circ\) (it is \(180^\circ\)), or that all four angles at a crossing are equal (only the opposite pairs are).

[[check:Two angles of a triangle are 45° and 55°. What is the third?|80;;80 degrees|180 − 45 − 55.]]
            """,
        ),
        (
            "6. Mixed-Review Strategy: Shape, Formula, Units",
            r"""
On a mixed test, the hardest part is choosing the right tool. Use this three-step routine for every question:

- **Name the shape or situation.** Rectangle, circle, box, right triangle, crossing lines, a triangle's angles?
- **Decide what is being asked.** Distance around (perimeter), surface inside (area), space filled (volume), a missing length (Pythagoras), or a missing angle (angle rules)?
- **Check the units of your answer.** Plain units = length/perimeter; square units = area/surface area; cubic units = volume; degrees = angle.

The units are a powerful self-check:
- If you computed an "area" but your answer is in plain feet, you actually found a perimeter.
- If a "volume" answer is in square units, you found surface area instead.

Error analysis: a student is asked for the carpet to cover a \(10 \times 8\) room and answers \(36\) (that is the perimeter \(2(10+8)\)). Carpet covers a surface, so the answer is the area \(10 \times 8 = 80\ \text{ft}^2\).

Final habit: read the question's last line carefully -- "how much fence" (perimeter), "how much carpet" (area), "how much water" (volume), "how long is the diagonal" (Pythagoras).

[[check:Which measurement tells you how much water a tank holds?|volume|Capacity of a solid is volume, in cubic units.]]
            """,
        ),
    ],
    "mcqs": [
        # --- Area ---
        {
            "text": r"What is the area of a rectangle \(7\) cm by \(4\) cm?",
            "difficulty": 1,
            "choices": [(r"\(28\ \text{cm}^2\)", True), (r"\(22\ \text{cm}^2\)", False), (r"\(11\ \text{cm}^2\)", False), (r"\(14\ \text{cm}^2\)", False)],
            "explanation": r"Area multiplies the sides: \(7 \times 4 = 28\ \text{cm}^2\). The trap 22 is the perimeter \(2(7+4)\); 11 is just \(7+4\). Pro tip: area = multiply (square units); perimeter = add then double (plain units).",
        },
        {
            "text": r"What is the area of a triangle with base \(10\) and height \(8\)?",
            "difficulty": 1,
            "choices": [(r"\(40\)", True), (r"\(80\)", False), (r"\(18\)", False), (r"\(36\)", False)],
            "explanation": r"\(A = \tfrac{1}{2} b h = \tfrac{1}{2}(10)(8) = 40\). The trap 80 forgets the \(\tfrac{1}{2}\). Pro tip: every triangle area starts with \(\tfrac{1}{2}\) -- multiply base by height, then halve.",
        },
        {
            "text": r"A circle has radius \(6\) cm. Using \(\pi \approx 3.14\), what is its area?",
            "difficulty": 2,
            "choices": [(r"\(113.04\ \text{cm}^2\)", True), (r"\(37.68\ \text{cm}^2\)", False), (r"\(18.84\ \text{cm}^2\)", False), (r"\(36\ \text{cm}^2\)", False)],
            "explanation": r"\(A = \pi r^2 = 3.14 \times 6^2 = 3.14 \times 36 = 113.04\ \text{cm}^2\). The trap 37.68 is the circumference (\(2\pi r\)); 36 forgets \(\pi\). Pro tip: area squares the radius first (\(6^2 = 36\)), then multiplies by \(\pi\).",
        },
        {
            "text": r"A trapezoid has parallel sides \(5\) and \(9\) and height \(4\). What is its area?",
            "difficulty": 2,
            "choices": [(r"\(28\)", True), (r"\(56\)", False), (r"\(18\)", False), (r"\(20\)", False)],
            "explanation": r"\(A = \tfrac{1}{2}(5+9)(4) = \tfrac{1}{2}(14)(4) = 28\). The trap 56 forgets the \(\tfrac{1}{2}\); 20 multiplies only one base by the height. Pro tip: average the two parallel sides (\(14/2 = 7\)), then times the height (\(7 \times 4 = 28\)).",
        },
        {
            "text": r"An \(8 \times 5\) rectangle has a \(2 \times 2\) square cut out. What is the remaining area?",
            "difficulty": 2,
            "choices": [(r"\(36\)", True), (r"\(44\)", False), (r"\(40\)", False), (r"\(13\)", False)],
            "explanation": r"\((8 \times 5) - (2 \times 2) = 40 - 4 = 36\). The trap 44 adds the cut-out; 40 forgets to remove it. Pro tip: a piece that is 'cut out' or 'removed' is subtracted from the whole.",
        },
        # --- Perimeter & circumference ---
        {
            "text": r"What is the perimeter of a rectangle \(9\) by \(5\)?",
            "difficulty": 1,
            "choices": [(r"\(28\)", True), (r"\(45\)", False), (r"\(14\)", False), (r"\(40\)", False)],
            "explanation": r"\(P = 2(9 + 5) = 2(14) = 28\). The trap 45 is the area (\(9 \times 5\)); 14 forgets to double. Pro tip: add length and width first, then double, because each side appears twice.",
        },
        {
            "text": r"What is the perimeter of a square with side \(7\)?",
            "difficulty": 1,
            "choices": [(r"\(28\)", True), (r"\(49\)", False), (r"\(14\)", False), (r"\(21\)", False)],
            "explanation": r"\(P = 4s = 4 \times 7 = 28\). The trap 49 is the area (\(7^2\)); 14 doubles instead of using all four sides. Pro tip: a square's perimeter is four equal sides -- multiply one side by 4.",
        },
        {
            "text": r"A circle has diameter \(8\) cm. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [(r"\(25.12\ \text{cm}\)", True), (r"\(50.24\ \text{cm}\)", False), (r"\(12.56\ \text{cm}\)", False), (r"\(64\ \text{cm}\)", False)],
            "explanation": r"\(C = \pi d = 3.14 \times 8 = 25.12\) cm. The trap 50.24 is the area for \(r = 4\); 12.56 uses the radius in \(\pi d\). Pro tip: with the diameter given, just use \(\pi d\) -- no squaring, no halving.",
        },
        {
            "text": r"A circle has radius \(5\) m. Using \(\pi \approx 3.14\), what is its circumference?",
            "difficulty": 2,
            "choices": [(r"\(31.4\ \text{m}\)", True), (r"\(78.5\ \text{m}\)", False), (r"\(15.7\ \text{m}\)", False), (r"\(10\ \text{m}\)", False)],
            "explanation": r"\(C = 2\pi r = 2 \times 3.14 \times 5 = 31.4\) m. The trap 78.5 is the area (\(\pi r^2\)); 10 is just the diameter. Pro tip: circumference from a radius uses \(2\pi r\) -- don't drop the 2.",
        },
        {
            "text": r"A triangle has sides \(7\), \(9\), and \(11\). What is its perimeter?",
            "difficulty": 1,
            "choices": [(r"\(27\)", True), (r"\(693\)", False), (r"\(18\)", False), (r"\(20\)", False)],
            "explanation": r"Add all three sides: \(7 + 9 + 11 = 27\). The trap 693 multiplies them; 18 and 20 miss a side. Pro tip: any polygon's perimeter is simply the sum of every side.",
        },
        # --- Volume & surface area ---
        {
            "text": r"What is the volume of a box \(5\) by \(3\) by \(2\)?",
            "difficulty": 1,
            "choices": [(r"\(30\)", True), (r"\(10\)", False), (r"\(31\)", False), (r"\(60\)", False)],
            "explanation": r"\(V = l w h = 5 \times 3 \times 2 = 30\). The trap 10 adds the dimensions; 31 is the surface-area face sum. Pro tip: volume multiplies all three dimensions and uses cubic units.",
        },
        {
            "text": r"What is the volume of a cube with edge \(4\) cm?",
            "difficulty": 1,
            "choices": [(r"\(64\ \text{cm}^3\)", True), (r"\(16\ \text{cm}^3\)", False), (r"\(12\ \text{cm}^3\)", False), (r"\(48\ \text{cm}^3\)", False)],
            "explanation": r"\(V = s^3 = 4^3 = 64\ \text{cm}^3\). The trap 16 squares the edge (\(4^2\)); 12 multiplies by 3. Pro tip: \(s^3\) means three factors -- \(4 \times 4 \times 4\), not \(4 \times 2\) or \(4 \times 3\).",
        },
        {
            "text": r"A cylinder has radius \(3\) cm and height \(5\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 2,
            "choices": [(r"\(141.3\ \text{cm}^3\)", True), (r"\(47.1\ \text{cm}^3\)", False), (r"\(94.2\ \text{cm}^3\)", False), (r"\(45\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \pi r^2 h = 3.14 \times 3^2 \times 5 = 3.14 \times 9 \times 5 = 141.3\ \text{cm}^3\). The trap 47.1 forgets to square the radius; 45 drops \(\pi\). Pro tip: square the radius first (\(3^2 = 9\)), then times \(\pi\), then times the height.",
        },
        {
            "text": r"A cone has radius \(3\) cm and height \(4\) cm. Using \(\pi \approx 3.14\), what is its volume?",
            "difficulty": 3,
            "choices": [(r"\(37.68\ \text{cm}^3\)", True), (r"\(113.04\ \text{cm}^3\)", False), (r"\(12.56\ \text{cm}^3\)", False), (r"\(28.26\ \text{cm}^3\)", False)],
            "explanation": r"\(V = \tfrac{1}{3}\pi r^2 h = \tfrac{1}{3}(3.14)(9)(4) = \tfrac{1}{3}(113.04) = 37.68\ \text{cm}^3\). The trap 113.04 forgets the \(\tfrac{1}{3}\) (that is the cylinder). Pro tip: a cone is one-third of the matching cylinder -- compute the cylinder, then divide by 3.",
        },
        {
            "text": r"What is the surface area of a cube with edge \(3\) cm?",
            "difficulty": 2,
            "choices": [(r"\(54\ \text{cm}^2\)", True), (r"\(27\ \text{cm}^2\)", False), (r"\(9\ \text{cm}^2\)", False), (r"\(18\ \text{cm}^2\)", False)],
            "explanation": r"\(SA = 6s^2 = 6 \times 3^2 = 6 \times 9 = 54\ \text{cm}^2\). The trap 27 is the VOLUME (\(3^3\)); 9 is one face. Pro tip: a cube has 6 square faces, so surface area is \(6s^2\) (square units); volume is \(s^3\) (cubic).",
        },
        {
            "text": r"How much water can a tank \(2\) m by \(2\) m by \(3\) m hold?",
            "difficulty": 2,
            "choices": [(r"\(12\ \text{m}^3\)", True), (r"\(7\ \text{m}^3\)", False), (r"\(32\ \text{m}^2\)", False), (r"\(14\ \text{m}^3\)", False)],
            "explanation": r"Capacity is volume: \(2 \times 2 \times 3 = 12\ \text{m}^3\). The trap 7 adds the dimensions; the \(32\ \text{m}^2\) option is a surface area (and wrong units for 'how much it holds'). Pro tip: 'how much it holds' = volume, in cubic units -- multiply all three dimensions.",
        },
        # --- Pythagorean / coordinate ---
        {
            "text": r"A right triangle has legs \(9\) and \(12\). What is the hypotenuse?",
            "difficulty": 2,
            "choices": [(r"\(15\)", True), (r"\(21\)", False), (r"\(225\)", False), (r"\(108\)", False)],
            "explanation": r"\(c = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15\). The trap 21 adds the legs; 225 forgets the square root. (This is the 3-4-5 triple times 3.) Pro tip: spot multiples of 3-4-5 (here 9-12-15) to skip the arithmetic.",
        },
        {
            "text": r"A right triangle has hypotenuse \(13\) and one leg \(5\). What is the other leg?",
            "difficulty": 2,
            "choices": [(r"\(12\)", True), (r"\(18\)", False), (r"\(\sqrt{194}\)", False), (r"\(8\)", False)],
            "explanation": r"Subtract, because 13 is the hypotenuse: \(\sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12\). The trap \(\sqrt{194}\) adds instead of subtracting. Pro tip: hypotenuse = add the squares; a missing leg = subtract.",
        },
        {
            "text": r"What is the distance between \((0, 0)\) and \((6, 8)\)?",
            "difficulty": 2,
            "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(48\)", False), (r"\(100\)", False)],
            "explanation": r"\(d = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\). From the origin, the coordinates are the legs. The trap 14 adds them; 100 forgets the square root. Pro tip: the distance formula is just the Pythagorean theorem on the grid.",
        },
        {
            "text": r"What is the distance between \((1, 1)\) and \((4, 5)\)?",
            "difficulty": 2,
            "choices": [(r"\(5\)", True), (r"\(7\)", False), (r"\(\sqrt{7}\)", False), (r"\(25\)", False)],
            "explanation": r"\(d = \sqrt{(4-1)^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\). The hidden legs are 3 and 4. The trap 25 forgets the square root. Pro tip: subtract the coordinates for each leg, then square, add, and take the root.",
        },
        {
            "text": r"What is the midpoint of \((2, 4)\) and \((8, 10)\)?",
            "difficulty": 2,
            "choices": [(r"\((5, 7)\)", True), (r"\((10, 14)\)", False), (r"\((3, 3)\)", False), (r"\((6, 6)\)", False)],
            "explanation": r"Average each coordinate: \(\left(\frac{2+8}{2}, \frac{4+10}{2}\right) = (5, 7)\). The trap \((10, 14)\) forgot to divide by 2 (that is the sum); \((3, 3)\) subtracts. Pro tip: midpoint ADDS the coordinates and halves; subtracting is for distance or slope.",
        },
        {
            "text": r"What is the slope of the line through \((1, 2)\) and \((3, 8)\)?",
            "difficulty": 2,
            "choices": [(r"\(3\)", True), (r"\(\tfrac{1}{3}\)", False), (r"\(6\)", False), (r"\(2\)", False)],
            "explanation": r"Slope is rise over run: \(\frac{8 - 2}{3 - 1} = \frac{6}{2} = 3\). The trap \(\tfrac{1}{3}\) flips the formula; 6 forgets to divide by the run. Pro tip: keep the same point first on top and bottom, and divide the vertical change by the horizontal change.",
        },
        # --- Angles & triangles ---
        {
            "text": r"What is the complement of a \(25^\circ\) angle?",
            "difficulty": 1,
            "choices": [("65°", True), ("155°", False), ("25°", False), ("75°", False)],
            "explanation": r"Complementary angles add to \(90^\circ\): \(90 - 25 = 65^\circ\). The trap 155 subtracts from 180 (supplementary). Pro tip: Complementary = Corner = \(90^\circ\); subtract from 90.",
        },
        {
            "text": r"What is the supplement of a \(70^\circ\) angle?",
            "difficulty": 1,
            "choices": [("110°", True), ("20°", False), ("70°", False), ("290°", False)],
            "explanation": r"Supplementary angles add to \(180^\circ\): \(180 - 70 = 110^\circ\). The trap 20 subtracts from 90 (complementary). Pro tip: Supplementary = Straight line = \(180^\circ\); subtract from 180.",
        },
        {
            "text": r"Two lines cross and one angle is \(65^\circ\). What is the angle directly across from it?",
            "difficulty": 1,
            "choices": [("65°", True), ("115°", False), ("25°", False), ("90°", False)],
            "explanation": r"Vertical (opposite) angles are equal, so it is also \(65^\circ\). The trap 115 is the neighbor (supplementary). Pro tip: directly ACROSS a crossing = equal; right NEXT TO it = adds to 180.",
        },
        {
            "text": r"Two angles of a triangle are \(45^\circ\) and \(55^\circ\). What is the third?",
            "difficulty": 1,
            "choices": [("80°", True), ("100°", False), ("90°", False), ("260°", False)],
            "explanation": r"The angles total \(180^\circ\): \(180 - 45 - 55 = 80^\circ\). The trap 100 just adds the two given angles. Pro tip: subtract the two known angles from 180 to find the third.",
        },
        {
            "text": r"Each angle of an equilateral triangle measures:",
            "difficulty": 1,
            "choices": [("60°", True), ("90°", False), ("45°", False), ("180°", False)],
            "explanation": r"All three angles are equal and total \(180^\circ\), so each is \(180 \div 3 = 60^\circ\). Pro tip: equilateral = three equal sides = three \(60^\circ\) angles.",
        },
        {
            "text": r"An isosceles triangle has a vertex angle of \(50^\circ\). What is each base angle?",
            "difficulty": 2,
            "choices": [("65°", True), ("130°", False), ("50°", False), ("90°", False)],
            "explanation": r"The two equal base angles share what is left: \((180 - 50) \div 2 = 130 \div 2 = 65^\circ\). The trap 130 forgets to split in half. Pro tip: subtract the vertex from 180, then divide by 2 for the two equal base angles.",
        },
        {
            "text": r"A triangle has remote interior angles \(50^\circ\) and \(60^\circ\). What is the exterior angle at the third vertex?",
            "difficulty": 2,
            "choices": [("110°", True), ("70°", False), ("180°", False), ("100°", False)],
            "explanation": r"An exterior angle equals the sum of the two remote interior angles: \(50 + 60 = 110^\circ\). The trap 70 is the third interior angle (\(180-50-60\)). Pro tip: the exterior-angle shortcut just adds the two far interior angles.",
        },
        {
            "text": r"A transversal crosses two parallel lines. One angle is \(75^\circ\). Its corresponding angle is:",
            "difficulty": 2,
            "choices": [("75°", True), ("105°", False), ("15°", False), ("180°", False)],
            "explanation": r"Corresponding angles are equal when the lines are parallel, so it is \(75^\circ\). The trap 105 is the supplement (a co-interior angle). Pro tip: corresponding angles sit in the 'same corner' at each crossing -- they match.",
        },
        # --- Mixed / multi-step / concept ---
        {
            "text": r"A room is \(12\) ft by \(10\) ft. How many square feet of carpet are needed?",
            "difficulty": 1,
            "choices": [(r"\(120\)", True), (r"\(44\)", False), (r"\(22\)", False), (r"\(60\)", False)],
            "explanation": r"Carpet covers the floor, so use area: \(12 \times 10 = 120\ \text{ft}^2\). The trap 44 is the perimeter \(2(12+10)\). Pro tip: 'cover / carpet / paint' = area (multiply); 'fence / trim' = perimeter (add).",
        },
        {
            "text": r"A yard is \(12\) ft by \(10\) ft. How many feet of fence go around it?",
            "difficulty": 1,
            "choices": [(r"\(44\)", True), (r"\(120\)", False), (r"\(22\)", False), (r"\(60\)", False)],
            "explanation": r"Fencing is the perimeter: \(2(12 + 10) = 44\) ft. The trap 120 is the area (\(12 \times 10\)). Pro tip: same room, two answers -- fence is the distance around (44), carpet is the surface inside (120).",
        },
        {
            "text": r"What is the length of the diagonal of a rectangle that is \(3\) by \(4\)?",
            "difficulty": 2,
            "choices": [(r"\(5\)", True), (r"\(7\)", False), (r"\(12\)", False), (r"\(25\)", False)],
            "explanation": r"The diagonal is the hypotenuse of a right triangle with legs 3 and 4: \(\sqrt{3^2 + 4^2} = \sqrt{25} = 5\). The trap 7 adds the sides; 12 is the area. Pro tip: a rectangle's diagonal is always a hypotenuse -- use the Pythagorean theorem.",
        },
        {
            "text": r"Tile costs \(3\) dollars per square foot. How much to tile a \(50\ \text{ft}^2\) floor?",
            "difficulty": 2,
            "choices": [("150 dollars", True), ("53 dollars", False), ("16.67 dollars", False), ("100 dollars", False)],
            "explanation": r"The area is given, so multiply by the price: \(50 \times 3 = 150\) dollars. The trap 53 adds; 16.67 divides. Pro tip: a cost question is two steps -- find the area, then multiply by the price per square unit.",
        },
        {
            "text": r"Which measurement is in CUBIC units?",
            "difficulty": 1,
            "choices": [("Volume", True), ("Area", False), ("Perimeter", False), ("An angle", False)],
            "explanation": r"Volume fills space in three directions, so it uses cubic units (\(\text{cm}^3\)). Area is square units, perimeter is plain units, angles are degrees. Pro tip: the unit tells the quantity -- cubic = volume, square = area, plain = length, degrees = angle.",
        },
        {
            "text": r"Which formula gives the area of a circle?",
            "difficulty": 1,
            "choices": [(r"\(\pi r^2\)", True), (r"\(2\pi r\)", False), (r"\(\pi d\)", False), (r"\(\tfrac{1}{2}bh\)", False)],
            "explanation": r"A circle's area is \(\pi r^2\) (square the radius). \(2\pi r\) and \(\pi d\) are both the circumference; \(\tfrac{1}{2}bh\) is a triangle. Pro tip: area has the square (\(r^2\)); circumference does not.",
        },
        {
            "text": r"The interior angles of any triangle add up to:",
            "difficulty": 1,
            "choices": [("180°", True), ("360°", False), ("90°", False), ("270°", False)],
            "explanation": r"Every triangle's three interior angles total \(180^\circ\). The trap 360 is the angles around a full point (or a four-sided shape). Pro tip: triangle = \(180^\circ\); a quadrilateral = \(360^\circ\).",
        },
        {
            "text": r"A problem asks how much paper is needed to wrap a box. Which measurement is that?",
            "difficulty": 1,
            "choices": [("Surface area", True), ("Volume", False), ("Perimeter", False), ("Diagonal", False)],
            "explanation": r"Wrapping covers the outside, so it is the surface area (square units). Volume is what fills the inside. Pro tip: 'wrap / cover / paint / label' = surface area; 'fill / hold / capacity' = volume.",
        },
        {
            "text": r"A right triangle has legs \(8\) and \(6\). What is the hypotenuse?",
            "difficulty": 1,
            "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(48\)", False), (r"\(100\)", False)],
            "explanation": r"\(c = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10\). The trap 14 adds the legs; 100 forgets the square root. (The 6-8-10 triple.) Pro tip: 6-8-10 is 3-4-5 doubled -- recognizing it saves time.",
        },
        {
            "text": r"A square has area \(64\ \text{cm}^2\). What is the length of each side?",
            "difficulty": 2,
            "choices": [(r"\(8\) cm", True), (r"\(32\) cm", False), (r"\(16\) cm", False), (r"\(4096\) cm", False)],
            "explanation": r"The side is the square root of the area: \(s = \sqrt{64} = 8\) cm. The trap 32 halves the area; 16 divides by 4. Pro tip: area-to-side for a square is a square root, because \(A = s^2\).",
        },
        {
            "text": r"A square has a perimeter of \(40\) cm. What is its area?",
            "difficulty": 3,
            "choices": [(r"\(100\ \text{cm}^2\)", True), (r"\(160\ \text{cm}^2\)", False), (r"\(1600\ \text{cm}^2\)", False), (r"\(10\ \text{cm}^2\)", False)],
            "explanation": r"First the side: \(s = 40 \div 4 = 10\) cm. Then the area: \(s^2 = 10^2 = 100\ \text{cm}^2\). The trap 10 stops at the side. Pro tip: a two-step problem -- use the perimeter to get the side, then square it for the area.",
        },
        {
            "text": r"Angles around a single point add up to:",
            "difficulty": 1,
            "choices": [("360°", True), ("180°", False), ("90°", False), ("270°", False)],
            "explanation": r"A full turn around a point is \(360^\circ\). The trap 180 is a straight line (half turn). Pro tip: full turn = \(360^\circ\); straight line = \(180^\circ\); square corner = \(90^\circ\).",
        },
        {
            "text": r"A cylinder and a cone have the same radius and height. The cone's volume is:",
            "difficulty": 2,
            "choices": [("One-third of the cylinder's", True), ("Equal to the cylinder's", False), ("Three times the cylinder's", False), ("Twice the cylinder's", False)],
            "explanation": r"The cone formula has a \(\tfrac{1}{3}\): \(V = \tfrac{1}{3}\pi r^2 h\), exactly one-third of the cylinder's \(\pi r^2 h\). Pro tip: three identical cones fill one matching cylinder.",
        },
        {
            "text": r"Which calculation finds how far apart two points on a grid are?",
            "difficulty": 1,
            "choices": [("The distance formula", True), ("The midpoint formula", False), ("The slope formula", False), ("The area formula", False)],
            "explanation": r"'How far apart' is the distance formula, \(\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}\). The midpoint gives the middle; slope gives steepness. Pro tip: match the key word -- 'how far / length' = distance; 'middle' = midpoint; 'how steep' = slope.",
        },
        {
            "text": r"A wall is \(10\) ft by \(8\) ft with a \(3\) ft by \(6\) ft window that is not painted. What area is painted?",
            "difficulty": 3,
            "choices": [(r"\(62\ \text{ft}^2\)", True), (r"\(80\ \text{ft}^2\)", False), (r"\(98\ \text{ft}^2\)", False), (r"\(18\ \text{ft}^2\)", False)],
            "explanation": r"Wall minus window: \((10 \times 8) - (3 \times 6) = 80 - 18 = 62\ \text{ft}^2\). The trap 80 forgets the window; 98 adds it. Pro tip: openings like windows and doors are not painted -- subtract their area.",
        },
        {
            "text": r"Two lines cross. One of the four angles is \(90^\circ\). What are the other three?",
            "difficulty": 2,
            "choices": [("All 90°", True), ("All 45°", False), ("90°, 45°, 45°", False), ("Cannot be determined", False)],
            "explanation": r"If one angle is \(90^\circ\), its vertical angle is also \(90^\circ\), and the two neighbors are \(180 - 90 = 90^\circ\) each -- the lines are perpendicular, so all four are \(90^\circ\). Pro tip: perpendicular lines create four equal right angles.",
        },
        {
            "text": r"A box is \(3\) by \(2\) by \(2\). What is its surface area?",
            "difficulty": 3,
            "choices": [("32 square units", True), ("12 square units", False), ("16 square units", False), ("7 square units", False)],
            "explanation": r"\(SA = 2(lw + lh + wh) = 2(3\cdot2 + 3\cdot2 + 2\cdot2) = 2(6 + 6 + 4) = 2(16) = 32\). The trap 12 is the VOLUME (\(3 \times 2 \times 2\)); 16 forgets to double. Pro tip: a box has 3 pairs of faces -- add the three distinct face areas, then double.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the capstone GED Geometry Mixed Review practice-test course (MCQ only)."

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
