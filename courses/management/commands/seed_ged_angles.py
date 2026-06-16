"""
Seed a GED Geometry course on ANGLES, LINES, and TRIANGLES.

Built in the rich style: 12 lessons, ~46 multiple-choice questions, labeled
diagrams, interactive self-checks, case studies, and common-mistake callouts.
Every answer explanation teaches the method, names the tempting wrong answer,
and ends with a Pro tip. Multiple choice only.

Run:
    python manage.py seed_ged_angles
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Angles, Lines & Triangles",
    "slug": "ged-geometry-angles-triangles",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep GED Geometry course on angles, lines, and triangles. Students learn to measure and "
        "classify angles, use complementary, supplementary, vertical, and parallel-line angle "
        "relationships to find missing angles, classify triangles by their sides and angles, and "
        "apply the triangle angle sum, exterior-angle, and isosceles rules. Every relationship has a "
        "labeled diagram, every lesson has an interactive self-check, and every practice answer "
        "explains the method and adds a Pro tip."
    ),
    "lessons": [
        (
            "1. Points, Lines, Rays, and Angles",
            r"""
Geometry starts with a few simple building blocks.

- A **point** marks a single location (no size).
- A **line** is perfectly straight and goes on forever in both directions.
- A **line segment** is part of a line with two endpoints.
- A **ray** starts at one point and goes forever in one direction.
- An **angle** is formed by two rays meeting at a common endpoint called the **vertex**.

Angles are measured in **degrees** (°). A full turn around a point is \(360^\circ\); a straight line is \(180^\circ\); a square corner is \(90^\circ\).

Two lines that cross at a \(90^\circ\) angle are **perpendicular**. Two lines that never cross and stay the same distance apart are **parallel**.

Case study - a clock: at 3:00 the hands form a \(90^\circ\) angle; at 6:00 they form a \(180^\circ\) straight angle.

Common mistake: measuring an angle by the length of its rays. The rays can be drawn long or short -- the angle is the *amount of turn* between them, not their length.

[[check:What do we call two lines that cross at a 90 degree angle?|perpendicular|They meet at a square corner, a right angle.]]
            """,
        ),
        (
            "2. Types of Angles",
            r"""
Angles are named by their size.

[[figure:angle_types|Acute is small, right is a square corner, obtuse is wide, straight is a flat line.]]

- **Acute angle:** less than \(90^\circ\).
- **Right angle:** exactly \(90^\circ\) (marked with a small square).
- **Obtuse angle:** between \(90^\circ\) and \(180^\circ\).
- **Straight angle:** exactly \(180^\circ\) (a straight line).
- **Reflex angle:** more than \(180^\circ\).

Worked example: an angle of \(45^\circ\) is acute; \(120^\circ\) is obtuse; \(90^\circ\) is right.

Case study - a ramp that rises gently makes an acute angle with the ground; a steep wall makes a right angle.

Common mistake: calling any "big" angle obtuse. Obtuse means strictly between \(90^\circ\) and \(180^\circ\); exactly \(90^\circ\) is right, and \(180^\circ\) is straight.

[[check:An angle measures 120 degrees. What type of angle is it?|obtuse|It is between 90 and 180 degrees.]]
            """,
        ),
        (
            "3. Complementary and Supplementary Angles",
            r"""
Two special pairs come up constantly because they let you find a missing angle by subtraction.

[[figure:comp_supp|Complementary angles fill a right angle (90°); supplementary angles fill a straight line (180°).]]

- **Complementary** angles add up to \(90^\circ\).
- **Supplementary** angles add up to \(180^\circ\).

To find the missing angle, subtract from 90 or 180.

Worked example (complementary): if one angle is \(35^\circ\), its complement is \(90 - 35 = 55^\circ\).

Worked example (supplementary): if one angle is \(110^\circ\), its supplement is \(180 - 110 = 70^\circ\).

Case study - a board cut to lean against a wall: the cut angle and the angle it makes with the floor are often complementary, adding to \(90^\circ\).

Common mistake: mixing up the two. Complementary "C" goes with the **corner** (\(90^\circ\)); Supplementary "S" goes with the **straight** line (\(180^\circ\)).

[[check:Two angles are complementary. One is 35 degrees. What is the other?|55;;55 degrees|Complementary angles add to 90, so 90 − 35.]]
            """,
        ),
        (
            "4. Vertical and Adjacent Angles",
            r"""
When two straight lines cross, they create four angles with a useful pattern.

[[figure:vertical_angles|Angles directly across from each other are equal; neighbors add to 180°.]]

- **Vertical angles** are the pair directly **across** from each other at the crossing. They are always **equal**.
- **Adjacent angles** on a straight line (a "linear pair") are **supplementary** -- they add to \(180^\circ\).

Worked example: two lines cross, and one angle is \(70^\circ\). The angle across from it (vertical) is also \(70^\circ\). The two neighbors are each \(180 - 70 = 110^\circ\).

Case study - an X-shaped railroad crossing: opposite angles match, which is why the pattern looks symmetric.

Common mistake: assuming all four angles are equal. Only the **vertical** (opposite) pairs are equal; the neighbors are supplementary, not equal (unless every angle is \(90^\circ\)).

[[check:Two lines cross. One angle is 70 degrees. What is the angle directly across from it?|70;;70 degrees|Vertical (opposite) angles are equal.]]
            """,
        ),
        (
            "5. Parallel Lines and a Transversal",
            r"""
A **transversal** is a line that cuts across two **parallel** lines. This creates eight angles with special equal-and-supplementary relationships.

[[figure:parallel_transversal|Matching-position angles are equal; same-side interior angles add to 180°.]]

The key facts:
- **Corresponding angles** (same position at each crossing) are **equal**.
- **Alternate interior angles** (between the lines, opposite sides of the transversal) are **equal**.
- **Co-interior (same-side interior) angles** are **supplementary** -- they add to \(180^\circ\).

Worked example: if one angle is \(110^\circ\), its corresponding angle at the other line is also \(110^\circ\), and the co-interior angle on the same side is \(180 - 110 = 70^\circ\).

Case study - a road crossing two parallel train tracks: the angle it makes with the first track equals the angle it makes with the second (corresponding angles).

Common mistake: assuming every pair is equal. Some pairs are equal (corresponding, alternate); the same-side interior pair is supplementary. Decide which relationship you have.

[[check:A transversal crosses two parallel lines. One angle is 110°. What is its corresponding angle?|110;;110 degrees|Corresponding angles are equal.]]
            """,
        ),
        (
            "6. Triangles: Classifying by Sides",
            r"""
A **triangle** is a closed shape with three sides and three angles. One way to classify triangles is by their **side lengths**.

[[figure:triangle_types_sides|Equilateral: all three equal. Isosceles: two equal. Scalene: none equal.]]

- **Equilateral:** all three sides equal (and all three angles \(60^\circ\)).
- **Isosceles:** exactly two sides equal (and the two **base angles** equal).
- **Scalene:** no sides equal (and no angles equal).

Tick marks on a diagram show which sides are equal: matching marks mean matching lengths.

Worked example: a triangle with sides 5, 5, and 8 is isosceles (two equal sides); a triangle with sides 4, 6, and 7 is scalene.

Case study - a roof truss is often an isosceles triangle, with two equal slanted sides meeting at the peak.

Common mistake: thinking equilateral and isosceles are unrelated. An equilateral triangle has all three sides equal, so it is also a special isosceles -- but on the GED, pick the most specific name (equilateral).

[[check:A triangle has sides 5, 5, and 8. What type is it (by sides)?|isosceles|Two of its sides are equal.]]
            """,
        ),
        (
            "7. Triangles: Classifying by Angles",
            r"""
Triangles can also be classified by their **largest angle**.

- **Acute triangle:** all three angles are less than \(90^\circ\).
- **Right triangle:** one angle is exactly \(90^\circ\).
- **Obtuse triangle:** one angle is greater than \(90^\circ\).

A triangle can have at most **one** right or obtuse angle, because all three angles must add to \(180^\circ\) (the next lesson). Two right angles alone would already use up \(180^\circ\), leaving nothing for the third.

Worked example: a triangle with angles \(90^\circ\), \(60^\circ\), and \(30^\circ\) is a right triangle. A triangle with angles \(100^\circ\), \(50^\circ\), and \(30^\circ\) is obtuse.

Case study - the corner of a set square (drafting tool) is a right triangle, used to draw perpendicular lines.

Common mistake: thinking a triangle could have two right angles. It cannot -- the angle sum is fixed at \(180^\circ\), so only one angle can be \(90^\circ\) or more.

[[check:A triangle has a 90 degree angle. What type is it (by angles)?|right|One angle is exactly 90 degrees.]]
            """,
        ),
        (
            "8. The Triangle Angle Sum: 180°",
            r"""
The most useful fact about triangles: the three interior angles **always add up to \(180^\circ\)**, no matter the triangle's shape or size.
\[
\angle A + \angle B + \angle C = 180^\circ.
\]

[[figure:triangle_angle_sum|Whatever the triangle, its three angles total 180 degrees.]]

To find a missing angle, subtract the two known angles from \(180\).

Worked example: a triangle has angles \(50^\circ\) and \(60^\circ\). The third is
\[
180 - 50 - 60 = 70^\circ.
\]

Worked example (right triangle): if one angle is \(90^\circ\) and another is \(30^\circ\), the third is \(180 - 90 - 30 = 60^\circ\).

Case study - a surveyor who measures two angles of a triangular plot can find the third instantly by subtracting from \(180^\circ\).

Common mistake: forgetting the total is \(180^\circ\), not \(360^\circ\). A full circle is \(360^\circ\), but a triangle's interior angles sum to \(180^\circ\).

[[check:A triangle has angles 50° and 60°. What is the third angle?|70;;70 degrees|Subtract from 180: 180 − 50 − 60.]]
            """,
        ),
        (
            "9. Exterior Angles of a Triangle",
            r"""
If you extend one side of a triangle, the angle formed outside is an **exterior angle**. It has a handy shortcut:
\[
\text{exterior angle} = \text{sum of the two remote (far) interior angles}.
\]

[[figure:exterior_angle|The exterior angle equals the two interior angles that are not next to it.]]

The "remote" interior angles are the two that are **not** next to the exterior angle.

Worked example: a triangle has interior angles \(70^\circ\) and \(60^\circ\) at the two far corners. The exterior angle at the third corner is
\[
70 + 60 = 130^\circ.
\]

You could also get this the long way: the third interior angle is \(180 - 70 - 60 = 50^\circ\), and the exterior angle is its supplement, \(180 - 50 = 130^\circ\). Same answer, more steps.

Case study - reading a road sign angle or a roof overhang: the exterior angle shortcut saves a step.

Common mistake: adding all three interior angles, or using the adjacent interior angle. Use only the **two remote** (far) angles.

[[check:A triangle has remote interior angles 70° and 60°. What is the exterior angle?|130;;130 degrees|Add the two remote interior angles: 70 + 60.]]
            """,
        ),
        (
            "10. Isosceles and Equilateral Triangle Rules",
            r"""
Equal sides come with equal angles, which often unlocks a missing-angle problem.

- **Isosceles triangle:** the two angles opposite the equal sides (the **base angles**) are **equal**.
- **Equilateral triangle:** all sides equal, so all three angles are equal -- each is \(\frac{180}{3} = 60^\circ\).

Worked example (isosceles): an isosceles triangle has a vertex (top) angle of \(40^\circ\). The two equal base angles share the rest:
\[
\frac{180 - 40}{2} = \frac{140}{2} = 70^\circ \text{ each}.
\]

Worked example: if an isosceles triangle has a base angle of \(50^\circ\), the other base angle is also \(50^\circ\), and the vertex angle is \(180 - 50 - 50 = 80^\circ\).

Case study - the equal sides of an A-frame house create equal base angles where the frame meets the ground.

Common mistake: splitting the wrong angle, or forgetting the base angles are equal. In an isosceles triangle, subtract the vertex angle from 180, then split the rest **in half** for the two equal base angles.

[[check:An isosceles triangle has a vertex angle of 40°. What is each base angle?|70;;70 degrees|Base angles are equal: (180 − 40) ÷ 2.]]
            """,
        ),
        (
            "11. Real-World Angle and Triangle Problems",
            r"""
GED angle questions usually hide a simple relationship inside a real situation. Find the relationship, then add or subtract.

A reliable routine:
- **What is being formed?** A straight line (\(180^\circ\)), a right angle (\(90^\circ\)), a crossing (vertical angles), parallel lines, or a triangle (\(180^\circ\)).
- **Which rule fits?** Complementary, supplementary, vertical, corresponding, or the triangle angle sum.
- **Add or subtract** to find the missing angle.

Worked example - a ramp: a ramp meets the ground, and the angle on one side is \(25^\circ\). The angle on the other side of that straight line is \(180 - 25 = 155^\circ\) (supplementary).

Worked example - a triangular garden: two corners measure \(80^\circ\) and \(55^\circ\); the third corner is \(180 - 80 - 55 = 45^\circ\).

Worked example - a clock: at 3:00 the hands are \(90^\circ\) apart (a right angle).

Common mistake: not identifying the relationship first. Always name what the angles form (line, corner, crossing, triangle) before computing.

[[check:A straight line is split into two angles. One is 25°. What is the other?|155;;155 degrees|A straight line is 180°, so 180 − 25.]]
            """,
        ),
        (
            "12. Strategy: The Angle-Relationship Toolkit",
            r"""
Most angle questions are solved with one of a handful of rules. Match the picture to the rule.

Your toolkit:
- **Angles in a right angle** add to \(90^\circ\) (complementary).
- **Angles on a straight line** add to \(180^\circ\) (supplementary).
- **Angles around a point** add to \(360^\circ\).
- **Vertical angles** (across a crossing) are **equal**.
- **Parallel lines:** corresponding and alternate angles are **equal**; co-interior angles add to \(180^\circ\).
- **Triangle angles** add to \(180^\circ\); an **exterior angle** equals the two remote interior angles.
- **Isosceles:** base angles equal. **Equilateral:** all angles \(60^\circ\).

Error analysis: a student says a triangle's three angles add to \(360^\circ\) and gets a missing angle of \(250^\circ\). The total is \(180^\circ\), not \(360^\circ\); \(360^\circ\) is the angles around a full point.

Case study - a complex figure: break it into the pieces you recognize -- a straight line here, a triangle there -- and apply one rule at a time.

Final habit: name the relationship (line, corner, crossing, parallel, triangle) before you compute. The right rule turns the problem into a quick addition or subtraction.

[[check:What is the sum of the interior angles of any triangle?|180;;180 degrees|Every triangle's three angles total 180°.]]
            """,
        ),
    ],
    "mcqs": [
        # --- Angle vocabulary / types ---
        {
            "text": r"What do we call two lines that cross at a \(90^\circ\) angle?",
            "difficulty": 1,
            "choices": [("Perpendicular", True), ("Parallel", False), ("Acute", False), ("Vertical", False)],
            "explanation": r"Lines that meet at a \(90^\circ\) (square corner) are perpendicular. 'Parallel' lines never meet at all. Pro tip: perpendicular = a right-angle crossing (think of the corner of a book); parallel = same distance apart forever, like railroad tracks.",
        },
        {
            "text": r"An angle that measures \(45^\circ\) is called:",
            "difficulty": 1,
            "choices": [("Acute", True), ("Right", False), ("Obtuse", False), ("Straight", False)],
            "explanation": r"Less than \(90^\circ\) is acute. A right angle is exactly \(90^\circ\), obtuse is between \(90^\circ\) and \(180^\circ\). Pro tip: 'acute' sounds like 'a cute little angle' -- small, under \(90^\circ\).",
        },
        {
            "text": r"An angle that measures \(120^\circ\) is called:",
            "difficulty": 1,
            "choices": [("Obtuse", True), ("Acute", False), ("Right", False), ("Reflex", False)],
            "explanation": r"Between \(90^\circ\) and \(180^\circ\) is obtuse. Reflex would be over \(180^\circ\); acute is under \(90^\circ\). Pro tip: obtuse angles look 'open' or 'leaning back' -- wider than a square corner but not yet a straight line.",
        },
        {
            "text": r"An angle of exactly \(180^\circ\) is a:",
            "difficulty": 1,
            "choices": [("Straight angle", True), ("Right angle", False), ("Full turn", False), ("Reflex angle", False)],
            "explanation": r"\(180^\circ\) forms a straight line, so it is a straight angle. A right angle is \(90^\circ\); a full turn is \(360^\circ\). Pro tip: a straight angle literally looks like a straight line -- half of a full \(360^\circ\) turn.",
        },
        # --- Complementary ---
        {
            "text": r"Two angles are complementary. One is \(35^\circ\). What is the other?",
            "difficulty": 1,
            "choices": [("55°", True), ("145°", False), ("35°", False), ("65°", False)],
            "explanation": r"Complementary angles add to \(90^\circ\), so the other is \(90 - 35 = 55^\circ\). The trap 145 uses \(180\) (that is supplementary). Pro tip: Complementary = Corner = \(90^\circ\); subtract from 90.",
        },
        {
            "text": r"What is the complement of a \(60^\circ\) angle?",
            "difficulty": 1,
            "choices": [("30°", True), ("120°", False), ("60°", False), ("40°", False)],
            "explanation": r"\(90 - 60 = 30^\circ\). The trap 120 subtracts from 180 (supplementary, not complementary). Pro tip: if the question says 'complement', the total is \(90^\circ\) -- subtract from 90.",
        },
        {
            "text": r"Two complementary angles are equal. What is each one?",
            "difficulty": 2,
            "choices": [("45°", True), ("90°", False), ("30°", False), ("60°", False)],
            "explanation": r"They add to \(90^\circ\) and are equal, so each is \(90 \div 2 = 45^\circ\). The trap 90 forgets to split. Pro tip: 'two equal angles that add to 90' means split 90 in half -- \(45^\circ\) each.",
        },
        # --- Supplementary ---
        {
            "text": r"Two angles are supplementary. One is \(110^\circ\). What is the other?",
            "difficulty": 1,
            "choices": [("70°", True), ("20°", False), ("110°", False), ("250°", False)],
            "explanation": r"Supplementary angles add to \(180^\circ\), so the other is \(180 - 110 = 70^\circ\). The trap 20 subtracts from 90 (complementary). Pro tip: Supplementary = Straight line = \(180^\circ\); subtract from 180.",
        },
        {
            "text": r"What is the supplement of a \(45^\circ\) angle?",
            "difficulty": 1,
            "choices": [("135°", True), ("45°", False), ("315°", False), ("55°", False)],
            "explanation": r"\(180 - 45 = 135^\circ\). The trap 55 subtracts from 90 (that is the complement). Pro tip: 'supplement' means the total is \(180^\circ\) (a straight line) -- subtract from 180.",
        },
        {
            "text": r"A straight line is divided into two angles. One is \(130^\circ\). What is the other?",
            "difficulty": 1,
            "choices": [("50°", True), ("230°", False), ("130°", False), ("40°", False)],
            "explanation": r"Angles on a straight line add to \(180^\circ\), so the other is \(180 - 130 = 50^\circ\). The trap 40 uses 90 by mistake. Pro tip: a straight line is always \(180^\circ\) -- two angles on it are supplementary.",
        },
        # --- Vertical / adjacent ---
        {
            "text": r"Two lines cross. One angle is \(70^\circ\). What is the angle directly across from it?",
            "difficulty": 1,
            "choices": [("70°", True), ("110°", False), ("20°", False), ("90°", False)],
            "explanation": r"Vertical (opposite) angles are equal, so the angle across is also \(70^\circ\). The trap 110 is the neighbor (supplementary), not the opposite angle. Pro tip: directly ACROSS a crossing = equal; right NEXT to it = adds to 180.",
        },
        {
            "text": r"Two lines cross. One angle is \(70^\circ\). What is the angle right next to it (on the straight line)?",
            "difficulty": 2,
            "choices": [("110°", True), ("70°", False), ("20°", False), ("90°", False)],
            "explanation": r"Neighboring angles on a straight line are supplementary: \(180 - 70 = 110^\circ\). The trap 70 is the vertical (opposite) angle, not the neighbor. Pro tip: the angle ACROSS is equal (70); the angle NEXT TO it is the supplement (110).",
        },
        {
            "text": r"When two straight lines cross, the pair of angles directly opposite each other are:",
            "difficulty": 1,
            "choices": [("Equal (vertical angles)", True), ("Supplementary", False), ("Complementary", False), ("Always 90°", False)],
            "explanation": r"Opposite angles at a crossing are vertical angles, and vertical angles are always equal. They are only \(90^\circ\) if the lines are perpendicular. Pro tip: 'vertical' here means 'across the vertex', not 'up and down' -- and across means equal.",
        },
        # --- Parallel lines & transversal ---
        {
            "text": r"A transversal crosses two parallel lines. One angle is \(110^\circ\). Its corresponding angle is:",
            "difficulty": 2,
            "choices": [("110°", True), ("70°", False), ("180°", False), ("55°", False)],
            "explanation": r"Corresponding angles (same position at each crossing) are equal when the lines are parallel, so it is \(110^\circ\). The trap 70 is the co-interior (same-side) angle, which is supplementary. Pro tip: corresponding angles sit in the 'same corner' at each intersection -- they match.",
        },
        {
            "text": r"A transversal crosses two parallel lines. One interior angle is \(110^\circ\). The same-side (co-interior) angle is:",
            "difficulty": 3,
            "choices": [("70°", True), ("110°", False), ("90°", False), ("180°", False)],
            "explanation": r"Co-interior (same-side interior) angles are supplementary: \(180 - 110 = 70^\circ\). The trap 110 treats them as equal, but only corresponding and alternate angles are equal. Pro tip: same-side interior angles form a 'C' shape and add to 180; alternate (Z-shape) angles are equal.",
        },
        {
            "text": r"Alternate interior angles formed by a transversal cutting parallel lines are:",
            "difficulty": 2,
            "choices": [("Equal", True), ("Supplementary", False), ("Complementary", False), ("Always right angles", False)],
            "explanation": r"Alternate interior angles (between the lines, on opposite sides of the transversal) are equal. The 'Z' or 'N' shape they make is the visual cue. Pro tip: alternate angles = equal (Z-shape); co-interior = supplementary (C-shape).",
        },
        {
            "text": r"Which relationship requires the two lines to be PARALLEL to guarantee equal angles?",
            "difficulty": 2,
            "choices": [("Corresponding angles", True), ("Vertical angles", False), ("Angles on a straight line", False), ("Angles around a point", False)],
            "explanation": r"Corresponding (and alternate) angles are only guaranteed equal when the lines are parallel. Vertical angles are equal at ANY crossing, parallel or not. Pro tip: vertical angles never need parallel lines; corresponding/alternate angles do.",
        },
        # --- Classify by sides ---
        {
            "text": r"A triangle has sides \(5\), \(5\), and \(8\). By its sides, it is:",
            "difficulty": 1,
            "choices": [("Isosceles", True), ("Equilateral", False), ("Scalene", False), ("Right", False)],
            "explanation": r"Two sides are equal (the two 5s), so it is isosceles. Equilateral needs all three equal; scalene needs all different. Pro tip: count the equal sides -- exactly two equal = isosceles, all three = equilateral, none = scalene.",
        },
        {
            "text": r"A triangle has sides \(4\), \(6\), and \(7\). By its sides, it is:",
            "difficulty": 1,
            "choices": [("Scalene", True), ("Isosceles", False), ("Equilateral", False), ("Obtuse", False)],
            "explanation": r"No two sides are equal, so it is scalene. (Obtuse is a classification by angle, not side.) Pro tip: all three sides different = scalene; check the side lengths before naming.",
        },
        {
            "text": r"Every angle of an equilateral triangle measures:",
            "difficulty": 1,
            "choices": [("60°", True), ("90°", False), ("45°", False), ("180°", False)],
            "explanation": r"All three sides equal means all three angles equal, and they must total \(180^\circ\), so each is \(180 \div 3 = 60^\circ\). Pro tip: equilateral always means three \(60^\circ\) angles -- a fact worth memorizing.",
        },
        {
            "text": r"A triangle with no equal sides and no equal angles is:",
            "difficulty": 1,
            "choices": [("Scalene", True), ("Isosceles", False), ("Equilateral", False), ("Right", False)],
            "explanation": r"No equal sides or angles is the definition of scalene. Pro tip: 'scalene' = 'scattered/uneven' -- everything different.",
        },
        # --- Classify by angles ---
        {
            "text": r"A triangle has angles \(90^\circ\), \(60^\circ\), and \(30^\circ\). By its angles, it is:",
            "difficulty": 1,
            "choices": [("Right", True), ("Acute", False), ("Obtuse", False), ("Equilateral", False)],
            "explanation": r"It has a \(90^\circ\) angle, so it is a right triangle. Acute needs all angles under \(90^\circ\); obtuse needs one over \(90^\circ\). Pro tip: look at the LARGEST angle -- exactly \(90^\circ\) = right, over \(90^\circ\) = obtuse, all under = acute.",
        },
        {
            "text": r"A triangle has angles \(100^\circ\), \(50^\circ\), and \(30^\circ\). By its angles, it is:",
            "difficulty": 2,
            "choices": [("Obtuse", True), ("Right", False), ("Acute", False), ("Scalene", False)],
            "explanation": r"One angle (\(100^\circ\)) is greater than \(90^\circ\), so it is obtuse. (Scalene classifies by sides, not angles.) Pro tip: a single angle over \(90^\circ\) makes the whole triangle obtuse.",
        },
        {
            "text": r"Can a triangle have two right angles?",
            "difficulty": 2,
            "choices": [("No -- the angles would exceed 180°", True), ("Yes, always", False), ("Yes, if it is large", False), ("Only if it is equilateral", False)],
            "explanation": r"Two right angles already total \(90 + 90 = 180^\circ\), leaving \(0^\circ\) for the third -- impossible. A triangle can have at most one right or obtuse angle. Pro tip: since all three angles must total exactly \(180^\circ\), only one of them can be \(90^\circ\) or more.",
        },
        # --- Angle sum ---
        {
            "text": r"A triangle has angles \(50^\circ\) and \(60^\circ\). What is the third angle?",
            "difficulty": 1,
            "choices": [("70°", True), ("110°", False), ("80°", False), ("250°", False)],
            "explanation": r"The three angles total \(180^\circ\), so the third is \(180 - 50 - 60 = 70^\circ\). The trap 110 only adds the two given angles. Pro tip: to find a missing triangle angle, subtract the two known ones from 180.",
        },
        {
            "text": r"A right triangle has one angle of \(30^\circ\) (besides the right angle). What is the third angle?",
            "difficulty": 2,
            "choices": [("60°", True), ("90°", False), ("150°", False), ("30°", False)],
            "explanation": r"A right triangle already has a \(90^\circ\) angle: \(180 - 90 - 30 = 60^\circ\). The trap 150 forgets to subtract the right angle. Pro tip: in a right triangle the two non-right angles always add to \(90^\circ\) (here \(30 + 60 = 90\)).",
        },
        {
            "text": r"Two angles of a triangle are \(40^\circ\) and \(40^\circ\). What is the third angle?",
            "difficulty": 2,
            "choices": [("100°", True), ("80°", False), ("40°", False), ("140°", False)],
            "explanation": r"\(180 - 40 - 40 = 100^\circ\). The trap 80 stops after adding the two 40s. Pro tip: even when two angles match, still subtract BOTH from 180 to get the third.",
        },
        {
            "text": r"The three interior angles of any triangle add up to:",
            "difficulty": 1,
            "choices": [("180°", True), ("360°", False), ("90°", False), ("270°", False)],
            "explanation": r"Every triangle's interior angles total \(180^\circ\). The trap 360 is the angles around a full point (or a quadrilateral's angle sum), not a triangle's. Pro tip: triangle = \(180^\circ\); a four-sided shape = \(360^\circ\).",
        },
        {
            "text": r"A student says a triangle's angles add to \(360^\circ\). What is the correct total?",
            "difficulty": 1,
            "choices": [("180°", True), ("360°", False), ("90°", False), ("540°", False)],
            "explanation": r"A triangle's interior angles total \(180^\circ\), not \(360^\circ\). The \(360^\circ\) value is the angles all the way around a point. Pro tip: cut any triangle's corners off and lay them together -- they form a straight line, \(180^\circ\).",
        },
        # --- Exterior angle ---
        {
            "text": r"A triangle has remote interior angles of \(70^\circ\) and \(60^\circ\). What is the exterior angle at the third vertex?",
            "difficulty": 2,
            "choices": [("130°", True), ("50°", False), ("180°", False), ("110°", False)],
            "explanation": r"An exterior angle equals the sum of the two remote (far) interior angles: \(70 + 60 = 130^\circ\). The trap 50 is the third interior angle (\(180-70-60\)); 130 is its supplement. Pro tip: the exterior-angle shortcut -- just add the two far interior angles -- skips a step.",
        },
        {
            "text": r"An exterior angle of a triangle is \(120^\circ\). One remote interior angle is \(70^\circ\). What is the other remote interior angle?",
            "difficulty": 3,
            "choices": [("50°", True), ("190°", False), ("60°", False), ("110°", False)],
            "explanation": r"The exterior angle equals the sum of the two remote interiors: \(120 = 70 + x\), so \(x = 120 - 70 = 50^\circ\). The trap 190 adds instead of subtracting. Pro tip: rearrange the rule -- if you know the exterior and one remote angle, subtract to get the other.",
        },
        {
            "text": r"The exterior angle of a triangle is equal to:",
            "difficulty": 2,
            "choices": [("The sum of the two remote interior angles", True), ("The sum of all three interior angles", False), ("The adjacent interior angle", False), ("90° always", False)],
            "explanation": r"An exterior angle equals the two interior angles NOT next to it (the remote ones). It is the supplement of the adjacent interior angle, not equal to it. Pro tip: 'remote' means far -- use the two angles across the triangle, not the neighbor.",
        },
        # --- Isosceles / equilateral ---
        {
            "text": r"An isosceles triangle has a vertex (top) angle of \(40^\circ\). What is each base angle?",
            "difficulty": 2,
            "choices": [("70°", True), ("140°", False), ("40°", False), ("100°", False)],
            "explanation": r"The base angles are equal and share what is left after the vertex: \((180 - 40) \div 2 = 140 \div 2 = 70^\circ\) each. The trap 140 forgets to split in half. Pro tip: subtract the vertex angle from 180, then divide by 2 for the two equal base angles.",
        },
        {
            "text": r"An isosceles triangle has a base angle of \(50^\circ\). What is the vertex angle?",
            "difficulty": 3,
            "choices": [("80°", True), ("50°", False), ("100°", False), ("130°", False)],
            "explanation": r"Both base angles are \(50^\circ\) (they are equal), so the vertex is \(180 - 50 - 50 = 80^\circ\). The trap 100 only subtracts one \(50^\circ\). Pro tip: in an isosceles triangle the two base angles match -- subtract BOTH from 180 to get the vertex.",
        },
        {
            "text": r"In an isosceles triangle, which two angles are equal?",
            "difficulty": 1,
            "choices": [("The two base angles (opposite the equal sides)", True), ("All three angles", False), ("The two largest sides' angles only if right", False), ("None of them", False)],
            "explanation": r"The two base angles -- the ones opposite the two equal sides -- are equal. (All three equal would make it equilateral.) Pro tip: equal sides face equal angles, so find the two equal sides and the angles across from them match.",
        },
        # --- Real-world / mixed / strategy ---
        {
            "text": r"A triangular garden has corners of \(80^\circ\) and \(55^\circ\). What is the third corner?",
            "difficulty": 2,
            "choices": [("45°", True), ("135°", False), ("35°", False), ("90°", False)],
            "explanation": r"\(180 - 80 - 55 = 45^\circ\). The trap 135 only adds the two known angles. Pro tip: any triangle problem -- garden, sign, roof -- uses the same \(180^\circ\) angle sum. Subtract the known angles from 180.",
        },
        {
            "text": r"At 3:00, the two hands of a clock form what kind of angle?",
            "difficulty": 1,
            "choices": [("A right angle (90°)", True), ("A straight angle", False), ("An acute angle", False), ("A reflex angle", False)],
            "explanation": r"At 3:00 the hands point straight up and straight right, forming a \(90^\circ\) right angle. Pro tip: each hour mark is \(30^\circ\) apart (\(360 \div 12\)), so 3 hours apart is \(3 \times 30 = 90^\circ\).",
        },
        {
            "text": r"Angles around a single point add up to:",
            "difficulty": 2,
            "choices": [("360°", True), ("180°", False), ("90°", False), ("270°", False)],
            "explanation": r"A complete turn around a point is a full circle, \(360^\circ\). The trap 180 is a straight line (half turn). Pro tip: full turn = \(360^\circ\); half turn (straight line) = \(180^\circ\); quarter turn (corner) = \(90^\circ\).",
        },
        {
            "text": r"Which fact is true at ANY crossing of two lines, even if they are not parallel?",
            "difficulty": 2,
            "choices": [("Vertical (opposite) angles are equal", True), ("Corresponding angles are equal", False), ("Co-interior angles are supplementary", False), ("Alternate angles are equal", False)],
            "explanation": r"Vertical angles are equal at any crossing. Corresponding, alternate, and co-interior relationships require the lines to be parallel. Pro tip: only vertical angles are 'free' -- the parallel-line rules need parallel lines to hold.",
        },
        {
            "text": r"A triangle has two angles that are both \(60^\circ\). The third angle is \(60^\circ\). What kind of triangle is it?",
            "difficulty": 2,
            "choices": [("Equilateral", True), ("Right", False), ("Obtuse", False), ("Scalene", False)],
            "explanation": r"All three angles are \(60^\circ\), so all three sides are equal too -- it is equilateral. Pro tip: three equal angles (each \(60^\circ\)) and three equal sides go together -- that is the equilateral triangle.",
        },
        {
            "text": r"To find a missing angle, you first decide what the angles form. Which clue means the angles add to \(180^\circ\)?",
            "difficulty": 2,
            "choices": [("They lie on a straight line or are a triangle's interior angles", True), ("They form a square corner", False), ("They go all the way around a point", False), ("They are vertical angles", False)],
            "explanation": r"A straight line and a triangle's interior angles each total \(180^\circ\). A square corner is \(90^\circ\), a full point is \(360^\circ\), and vertical angles are equal (not a sum). Pro tip: name the picture first -- line or triangle means \(180^\circ\); corner means \(90^\circ\); full turn means \(360^\circ\).",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Angles, Lines & Triangles course (MCQ only)."

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
