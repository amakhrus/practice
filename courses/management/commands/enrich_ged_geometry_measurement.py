from django.core.management.base import BaseCommand
from courses.models import Lesson

LESSONS = [
    (1, """Perimeter & Area: Edges vs. Surface

Understanding the difference between perimeter and area is one of the most fundamental skills in geometry. These two measurements describe very different things about a shape, and confusing them is one of the most common mistakes on the GED Math test.

PERIMETER is the total distance around the outside of a shape. Think of it as the length of a fence you would need to enclose a yard. Perimeter is always measured in linear units: feet, meters, inches, and so on.

AREA is the amount of surface space inside a shape. Think of it as the amount of carpet needed to cover a floor. Area is always measured in square units: square feet (ft^2), square meters (m^2), and so on.

Key Formulas:

Rectangle:
  Perimeter = 2 x length + 2 x width   (or 2(l + w))
  Area = length x width

Square (a rectangle where all sides are equal):
  Perimeter = 4 x side
  Area = side x side  (or side^2)

Triangle:
  Perimeter = side a + side b + side c  (add all three sides)
  Area = (1/2) x base x height

Parallelogram:
  Area = base x height  (note: height is the perpendicular distance, not the slant side)

Worked Example:

A rectangular garden is 12 feet long and 7 feet wide. A homeowner wants to put a fence around the entire garden and also lay sod inside it. How many feet of fencing are needed, and how many square feet of sod?

Step 1 - Fencing (perimeter):
  P = 2(l + w) = 2(12 + 7) = 2(19) = 38 feet of fencing

Step 2 - Sod (area):
  A = l x w = 12 x 7 = 84 square feet of sod

The answer: 38 ft of fence and 84 ft^2 of sod.

Second Worked Example:

A triangle has a base of 10 cm and a height of 6 cm. Find its area.

  Area = (1/2) x base x height
       = (1/2) x 10 x 6
       = (1/2) x 60
       = 30 cm^2

Common Trap:

Students often use the slant height of a triangle or parallelogram instead of the perpendicular height when calculating area. The height in any area formula must be measured at a right angle (90 degrees) to the base. If a triangle leans to one side, the height is the vertical line dropped straight down from the top vertex to the base line, not the length of the slanting side.

Another trap: forgetting to use square units for area and linear units for perimeter. If the GED question asks for area, your answer needs "square" in the unit label.

Practical GED Tip:

On the GED, formulas for area and perimeter are provided on a formula sheet. You do not need to memorize every formula, but you must know which formula applies to which situation. Read each word problem carefully for keywords: "around," "border," "fence," or "trim" signal perimeter; "cover," "fill," "surface," or "floor" signal area. Always label your answer with the correct units -- examiners notice missing or wrong units, and the answer choices will often include a version with incorrect units as a distractor.
"""),

    (2, """Circles: pi Demystified

Circles are unique shapes because they have no straight sides or corners. All measurements of a circle trace back to one special number: pi (approximately 3.14 or 22/7). Understanding what pi actually means, and knowing the two key circle formulas, will let you handle any GED circle problem with confidence.

KEY TERMS:

Radius (r): the distance from the center of the circle to any point on its edge.
Diameter (d): the distance straight across the circle through the center. Diameter = 2 x radius.
Circumference (C): the distance all the way around the circle (the perimeter of a circle).
Area (A): the surface space inside the circle.

WHAT IS pi?

pi is the ratio of a circle's circumference to its diameter. No matter how big or small a circle is, if you divide its circumference by its diameter, you always get the same number: approximately 3.14159... The GED typically uses pi = 3.14.

Key Formulas:

  Circumference: C = 2 x pi x r   (or C = pi x d)
  Area:          A = pi x r^2

Notice: circumference uses the radius to the first power (linear measurement), while area uses the radius squared (square measurement). This mirrors the perimeter-vs-area distinction from the previous lesson.

Worked Example 1 - Circumference:

A circular fountain has a radius of 5 meters. What is its circumference? Use pi = 3.14.

  C = 2 x pi x r
    = 2 x 3.14 x 5
    = 6.28 x 5
    = 31.4 meters

Worked Example 2 - Area:

A circular pizza has a diameter of 14 inches. What is its area? Use pi = 3.14.

Step 1: Find the radius.
  r = d / 2 = 14 / 2 = 7 inches

Step 2: Apply the area formula.
  A = pi x r^2
    = 3.14 x 7^2
    = 3.14 x 49
    = 153.86 square inches

Worked Example 3 - Working Backwards:

The circumference of a circle is 62.8 cm. What is its radius?

  C = 2 x pi x r
  62.8 = 2 x 3.14 x r
  62.8 = 6.28 x r
  r = 62.8 / 6.28
  r = 10 cm

Common Trap:

The single most common circle mistake is using the diameter when the formula calls for the radius (or vice versa). When a problem gives you a diameter, always divide by 2 to get the radius before plugging into the area formula. If you forget this step, you will get an answer that is four times too large (because r^2 would be replaced by d^2 = (2r)^2 = 4r^2). All four wrong answer choices on the GED are carefully designed to catch this exact error.

A second trap: squaring pi along with the radius. Only the radius gets squared in A = pi x r^2. Pi stays at 3.14.

Practical GED Tip:

The GED formula sheet includes both circle formulas. When you see a circle problem, your first two actions should be: (1) identify whether the problem gives you radius or diameter, and (2) decide whether the question asks for circumference or area. Write down the correct formula, substitute the radius (not diameter), and work step by step. Rounding: the GED usually specifies pi = 3.14, so use that value unless told otherwise.
"""),

    (3, """Volume: Filling 3D Space

While area measures the flat surface inside a 2D shape, volume measures the total three-dimensional space inside a solid figure. You can think of volume as how much water a container can hold, or how many unit cubes it takes to fill a box.

Volume is always measured in cubic units: cubic inches (in^3), cubic feet (ft^3), cubic centimeters (cm^3), and so on.

KEY 3D SHAPES AND THEIR VOLUME FORMULAS:

Rectangular Prism (box):
  V = length x width x height   (or V = l x w x h)

Cube (all sides equal):
  V = side^3   (or V = s x s x s)

Cylinder (like a soup can):
  V = pi x r^2 x height   (or V = pi x r^2 x h)
  Note: the base of a cylinder is a circle, so pi x r^2 is the area of the circular base.

Cone:
  V = (1/3) x pi x r^2 x height

Pyramid (rectangular base):
  V = (1/3) x length x width x height

Sphere:
  V = (4/3) x pi x r^3

The GED provides all of these formulas on its formula sheet. Your job is to recognize which shape is described, extract the right measurements, and apply the formula correctly.

Worked Example 1 - Rectangular Prism:

A storage box is 4 feet long, 3 feet wide, and 2 feet tall. What is its volume?

  V = l x w x h
    = 4 x 3 x 2
    = 24 cubic feet

Worked Example 2 - Cylinder:

A cylindrical water tank has a radius of 3 meters and a height of 10 meters. What is its volume? Use pi = 3.14.

  V = pi x r^2 x h
    = 3.14 x 3^2 x 10
    = 3.14 x 9 x 10
    = 3.14 x 90
    = 282.6 cubic meters

Worked Example 3 - Cone vs. Cylinder Comparison:

An ice cream cone has a radius of 2 inches and a height of 6 inches. A cylindrical cup has the same radius and height. How do their volumes compare?

Cylinder: V = pi x r^2 x h = 3.14 x 4 x 6 = 75.36 in^3
Cone:     V = (1/3) x pi x r^2 x h = (1/3) x 75.36 = 25.12 in^3

The cone holds exactly one-third the volume of the cylinder with the same base and height. This relationship is worth memorizing.

Common Trap:

Students frequently forget the (1/3) factor in the cone and pyramid formulas. If you see either of those shapes, write "(1/3) x" at the start of your work as a reminder before filling in the other values.

A second trap with cylinders: using the diameter instead of the radius. The formula needs r^2, so if the problem gives the diameter, divide by 2 first.

A third trap: mixing units. If a problem gives length in feet but asks for volume in cubic inches, you must convert before calculating. There are 12 inches in a foot, so 1 cubic foot = 12 x 12 x 12 = 1,728 cubic inches.

Practical GED Tip:

GED volume problems often describe a real-world container (fish tank, silo, pool) and ask how much liquid it holds. These are straightforward if you match the shape to the right formula. Look for keywords: "box" or "room" suggests rectangular prism; "can" or "pipe" suggests cylinder; "cone" or "funnel" suggests cone formula. Write the formula, plug in numbers carefully, and pay attention to whether they give radius or diameter.
"""),

    (4, """The Pythagorean Theorem

The Pythagorean Theorem is one of the most famous equations in all of mathematics, and it appears regularly on the GED. It describes a special relationship that exists in every right triangle -- a triangle that contains one 90-degree angle.

THE THEOREM:

In a right triangle, if the two shorter sides (called legs) are labeled a and b, and the longest side (called the hypotenuse) is labeled c, then:

  a^2 + b^2 = c^2

The hypotenuse is always the side directly across from the right angle. It is always the longest side of the triangle.

USING THE THEOREM:

You can use this formula in three ways:
1. Find the hypotenuse (c) when you know both legs (a and b).
2. Find a missing leg when you know the hypotenuse and the other leg.
3. Determine whether a triangle is a right triangle by checking if a^2 + b^2 = c^2.

Worked Example 1 - Finding the Hypotenuse:

A ramp rises 6 feet vertically and extends 8 feet horizontally. How long is the ramp (the slanted surface)?

The ramp is the hypotenuse. The vertical rise and horizontal run are the two legs.

  a^2 + b^2 = c^2
  6^2 + 8^2 = c^2
  36 + 64 = c^2
  100 = c^2
  c = square root of 100
  c = 10 feet

The ramp is 10 feet long.

Worked Example 2 - Finding a Missing Leg:

A ladder 13 feet long leans against a wall. The base of the ladder is 5 feet from the wall. How high up the wall does the ladder reach?

Here c = 13 (hypotenuse), a = 5 (one leg), and b = ? (the height up the wall).

  a^2 + b^2 = c^2
  5^2 + b^2 = 13^2
  25 + b^2 = 169
  b^2 = 169 - 25
  b^2 = 144
  b = square root of 144
  b = 12 feet

The ladder reaches 12 feet up the wall.

COMMON PYTHAGOREAN TRIPLES:

Some combinations of whole numbers satisfy the theorem perfectly. Recognizing these saves calculation time:
  3, 4, 5
  5, 12, 13
  8, 15, 17
  Multiples also work: 6, 8, 10 (double of 3-4-5); 9, 12, 15 (triple of 3-4-5)

Common Trap:

The most frequent mistake is adding the squares incorrectly or adding the sides before squaring. Remember: you MUST square each leg first, THEN add. Never add the legs first and then square the sum. That is, (a + b)^2 does NOT equal a^2 + b^2.

Also, always identify the hypotenuse correctly. It is the side across from the right angle (the corner with the little square symbol in diagrams), and it is always c in the formula -- never a or b.

Practical GED Tip:

On the GED, Pythagorean Theorem problems often appear in context: a diagonal path across a rectangular field, the diagonal of a screen or room, a ladder against a wall, or a wire anchoring a pole. Draw a right triangle and label the three sides with the numbers from the problem before writing the formula. This simple sketch prevents the most common errors. The GED formula sheet includes a^2 + b^2 = c^2, so you do not need to memorize it, but you do need to know when to apply it.
"""),

    (5, """The Coordinate Plane

The coordinate plane (also called the Cartesian plane) is a grid formed by two perpendicular number lines. It gives every point in space a unique address using a pair of numbers, and it is the foundation for graphing, finding distances, and understanding slope -- all of which appear on the GED.

THE BASICS:

The horizontal number line is called the x-axis.
The vertical number line is called the y-axis.
The point where they intersect is called the origin, which has coordinates (0, 0).

Every point on the plane is written as an ordered pair: (x, y).
  x tells you how far to move left or right from the origin (negative = left, positive = right).
  y tells you how far to move up or down (negative = down, positive = up).

The plane is divided into four quadrants:
  Quadrant I:   x positive, y positive (upper right)
  Quadrant II:  x negative, y positive (upper left)
  Quadrant III: x negative, y negative (lower left)
  Quadrant IV:  x positive, y negative (lower right)

FINDING THE DISTANCE BETWEEN TWO POINTS:

The distance formula is derived from the Pythagorean Theorem:

  Distance = square root of [ (x2 - x1)^2 + (y2 - y1)^2 ]

Think of drawing a right triangle between the two points: the horizontal leg is (x2 - x1) and the vertical leg is (y2 - y1). The distance between the points is the hypotenuse.

Worked Example 1 - Plotting and Distance:

Find the distance between points A(1, 2) and B(4, 6).

  Horizontal difference: x2 - x1 = 4 - 1 = 3
  Vertical difference:   y2 - y1 = 6 - 2 = 4

  Distance = square root of (3^2 + 4^2)
           = square root of (9 + 16)
           = square root of 25
           = 5 units

Notice that 3, 4, 5 is a Pythagorean triple -- a useful shortcut to recognize.

FINDING THE MIDPOINT BETWEEN TWO POINTS:

The midpoint formula finds the exact center between two points:

  Midpoint = ( (x1 + x2) / 2,  (y1 + y2) / 2 )

Simply average the x-coordinates and average the y-coordinates.

Worked Example 2 - Midpoint:

Find the midpoint between P(2, 8) and Q(6, 4).

  Midpoint x = (2 + 6) / 2 = 8 / 2 = 4
  Midpoint y = (8 + 4) / 2 = 12 / 2 = 6

  Midpoint = (4, 6)

UNDERSTANDING SLOPE:

Slope measures the steepness of a line. It is calculated as:

  Slope (m) = rise / run = (y2 - y1) / (x2 - x1)

A positive slope goes uphill from left to right. A negative slope goes downhill. A slope of zero is a flat horizontal line. An undefined slope is a vertical line.

Worked Example 3 - Slope:

Find the slope of the line through (1, 3) and (5, 11).

  m = (11 - 3) / (5 - 1) = 8 / 4 = 2

The line rises 2 units for every 1 unit it moves to the right.

Common Trap:

Students often mix up the order of subtraction in the distance or slope formulas, subtracting x2 - x1 in the numerator but y1 - y2 (reversed) in the denominator. Always subtract in the same order: second point minus first point for both coordinates. The distance formula squares the differences so order does not matter there, but the slope formula does not -- a reversed subtraction flips the sign of the slope.

Another trap: confusing the x-coordinate with the y-coordinate when reading an ordered pair. Remember: x always comes first, y always comes second: (x, y). To plot a point, move horizontally first, then vertically.

Practical GED Tip:

GED coordinate plane problems sometimes show a graph and ask for slope, distance, or a missing endpoint. If the graph is provided, count grid squares to find rise and run for slope rather than calculating -- this is faster and avoids arithmetic errors. When no graph is given, write out the formula, label which values are x1, y1, x2, and y2 before substituting, and work one step at a time.
"""),
]

class Command(BaseCommand):
    help = "Enrich lesson content for GED Geometry & Measurement"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(course__slug="ged-geometry-measurement", order=order).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(self.style.SUCCESS("Done."))
