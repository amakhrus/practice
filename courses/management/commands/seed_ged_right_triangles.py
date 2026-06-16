"""
Seed the Right Triangles Mathematics course.

The course follows the same seed-command template as the existing course posts:
structured lessons, reusable figures, interactive self-checks, and MCQ-only
practice with teaching explanations.

Run:
    python manage.py seed_ged_right_triangles
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Geometry: Right Triangles",
    "slug": "ged-geometry-right-triangles",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Mathematics course on right triangles: recognizing the "
        "90-degree angle, naming legs and the hypotenuse, using the Pythagorean "
        "Theorem, finding missing sides, using right-triangle area and perimeter, "
        "spotting common triples, and solving practical ramp, ladder, diagonal, "
        "and distance problems. Each lesson includes a diagram or self-check, and "
        "the practice set is multiple-choice with full worked explanations."
    ),
    "lessons": [
        (
            "1. What Makes a Triangle Right?",
            (
                "Right triangles are one of the most dependable geometry patterns on the GED Mathematics test."
                "\n\n"
                r"A **right triangle** is a triangle with exactly one \(90^\circ\) angle. "
                r"That square corner is the signal that right-triangle tools may be useful."
                "\n\n"
                r"[[figure:angle_types|A right angle is exactly 90 degrees -- the square-corner angle.]]"
                "\n\n"
                r"Why exactly one? The angles of any triangle add to \(180^\circ\). If one angle is "
                r"\(90^\circ\), the other two must share the remaining \(90^\circ\), so they are both acute."
                "\n\n"
                r"Test habit: before you use a formula, first prove to yourself that the triangle is right. "
                r"Look for a small square in the corner, wording such as **perpendicular**, or a real-world "
                r"situation where a wall meets level ground."
                "\n\n"
                r"Common mistake: using right-triangle formulas on any triangle that looks almost square. "
                r"The theorem needs a true \(90^\circ\) angle."
                "\n\n"
                r"[[check:What angle measure makes a triangle a right triangle?|90;;90 degrees;;90°|A right triangle has one square corner, which is 90 degrees.]]"
            ),
        ),
        (
            "2. Legs and Hypotenuse",
            r"""
Every right triangle has two **legs** and one **hypotenuse**.

[[figure:pythagorean_triangle|The legs form the right angle; the hypotenuse is opposite the right angle.]]

- The **legs** are the two sides that touch and form the \(90^\circ\) angle.
- The **hypotenuse** is the side across from the \(90^\circ\) angle.
- The hypotenuse is always the **longest** side.

This naming matters because formulas treat the hypotenuse differently. In \(a^2 + b^2 = c^2\), the legs are \(a\) and \(b\), while the hypotenuse is \(c\).

Quick visual rule: find the square corner. The side that does **not** touch that corner is the hypotenuse.

Common mistake: calling the slanted side the hypotenuse every time. In many drawings it is slanted, but the real definition is "opposite the right angle."

[[check:Which side is the hypotenuse?|the side opposite the right angle;;opposite the right angle;;longest side|It is across from the square corner and is the longest side.]]
            """,
        ),
        (
            "3. The Pythagorean Theorem",
            r"""
The central formula for right triangles is the **Pythagorean Theorem**:
\[
a^2 + b^2 = c^2
\]
where \(a\) and \(b\) are the legs, and \(c\) is the hypotenuse.

[[figure:right_triangle_345|For a 3-4-5 right triangle, \(3^2 + 4^2 = 5^2\).]]

The theorem says that the squares on the two legs add up to the square on the hypotenuse. For a 3-4-5 triangle:
\[
3^2 + 4^2 = 9 + 16 = 25 = 5^2.
\]

Use this theorem when a question asks for a missing side, a diagonal, a straight-line distance, a ladder height, or a ramp length.

Common mistake: writing \(a + b = c\). Side lengths do not add directly; their **squares** do.

[[check:In \(a^2 + b^2 = c^2\), which letter is the hypotenuse?|c|The hypotenuse is the side across from the right angle. It is usually labeled \(c\).]]
            """,
        ),
        (
            "4. Finding the Hypotenuse",
            r"""
When both legs are known and the hypotenuse is missing, **add** the squares and then take the square root:
\[
c = \sqrt{a^2 + b^2}.
\]

Worked example: a right triangle has legs \(6\) and \(8\).
\[
c = \sqrt{6^2 + 8^2}
  = \sqrt{36 + 64}
  = \sqrt{100}
  = 10.
\]

The answer is a length, not a squared value. If you stop at 100, you found \(c^2\), not \(c\).

GED-style setup: a ramp rises 6 feet over a horizontal run of 8 feet. The ramp is the hypotenuse, so its length is 10 feet.

Common mistake: forgetting the square root at the end.

[[check:A right triangle has legs 5 and 12. What is the hypotenuse?|13;;13 units|Use \(\sqrt{5^2+12^2}=\sqrt{25+144}=\sqrt{169}=13\).]]
            """,
        ),
        (
            "5. Finding a Missing Leg",
            r"""
When the hypotenuse and one leg are known, the missing side is the **other leg**. This time you subtract:
\[
\text{missing leg} = \sqrt{c^2 - \text{known leg}^2}.
\]

Worked example: a right triangle has hypotenuse \(13\) and one leg \(5\).
\[
\sqrt{13^2 - 5^2}
= \sqrt{169 - 25}
= \sqrt{144}
= 12.
\]

Why subtract? The hypotenuse square is the total. One leg's square is already part of that total, so you remove it to find the other leg's square.

GED-style setup: a 13-foot ladder leans against a wall, and the base is 5 feet from the wall. The ladder is the hypotenuse, so the wall height is 12 feet.

Common mistake: adding when a hypotenuse is already given. If the longest side is known, you usually subtract.

[[check:A right triangle has hypotenuse 10 and one leg 6. What is the other leg?|8;;8 units|Use \(\sqrt{10^2-6^2}=\sqrt{100-36}=\sqrt{64}=8\).]]
            """,
        ),
        (
            "6. Area and Perimeter of Right Triangles",
            r"""
A right triangle's two legs are perpendicular, so they can act as the **base** and **height** for area:
\[
A = \frac{1}{2}(\text{leg})(\text{leg}).
\]

[[figure:area_triangle|Triangle area is half of base times height. In a right triangle, the legs are already perpendicular.]]

Worked example: legs \(6\) and \(8\).
\[
A = \frac{1}{2}(6)(8) = 24.
\]

Perimeter is different: add all three sides. If you only know the legs, find the hypotenuse first, then add.

Worked example: legs \(5\) and \(12\) have hypotenuse \(13\), so the perimeter is:
\[
5 + 12 + 13 = 30.
\]

Common mistake: using the hypotenuse as the height for area. Height must be perpendicular to the base; in a right triangle, the two legs are the easy perpendicular pair.

[[check:What is the area of a right triangle with legs 6 and 8?|24;;24 square units|Use \(\frac12(6)(8)\).]]
            """,
        ),
        (
            "7. Triples and Special Right Triangles",
            r"""
Some right triangles have whole-number side lengths called **Pythagorean triples**. Knowing the common ones saves time:

- \(3, 4, 5\)
- \(5, 12, 13\)
- \(8, 15, 17\)
- \(7, 24, 25\)

Multiples also work: \(6, 8, 10\) is just \(2 \times (3,4,5)\), and \(9, 12, 15\) is \(3 \times (3,4,5)\).

Two special patterns also appear in geometry:
- A **45-45-90** right triangle has two equal legs.
- A **30-60-90** right triangle has a short leg that is half the hypotenuse.

Use these as shortcuts only when the pattern is clearly present. If you are unsure, the Pythagorean Theorem always works.

Common mistake: forcing a triple when the numbers do not fit. Legs \(2\) and \(3\) give \(\sqrt{13}\), not a whole number.

[[check:A right triangle has legs 8 and 15. What is the hypotenuse?|17;;17 units|This is the 8-15-17 triple.]]
            """,
        ),
        (
            "8. Word Problems: Draw the Hidden Triangle",
            r"""
Many right-triangle questions hide the triangle inside a real situation. Your job is to draw it.

[[figure:distance_on_grid|A straight-line distance can be the hypotenuse of a hidden right triangle.]]

Common right-triangle setups:
- A **ladder** against a wall: ladder = hypotenuse.
- A **ramp**: ramp surface = hypotenuse; rise and run = legs.
- A **rectangle diagonal**: diagonal = hypotenuse; length and width = legs.
- A **map or grid distance**: east/west and north/south moves are legs; straight-line distance is the hypotenuse.

Routine:
- Sketch the right angle.
- Label the legs and hypotenuse.
- Decide whether you are finding the hypotenuse (add) or a leg (subtract).
- Check units and reasonableness. The hypotenuse should be the longest side.

Worked example: a person walks 12 blocks east and 5 blocks north. Straight-line distance:
\[
\sqrt{12^2 + 5^2} = \sqrt{144+25} = \sqrt{169} = 13.
\]

Common mistake: adding the walking distances \(12+5=17\). That is the path walked, not the straight-line distance.

[[check:A rectangle is 7 by 24. What is the diagonal?|25;;25 units|The diagonal is the hypotenuse: \(\sqrt{7^2+24^2}=25\).]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"Which angle measure makes a triangle a right triangle?",
            "difficulty": 1,
            "choices": [(r"\(90^\circ\)", True), (r"\(60^\circ\)", False), (r"\(120^\circ\)", False), (r"\(180^\circ\)", False)],
            "explanation": r"A right triangle has exactly one \(90^\circ\) angle. A \(60^\circ\) angle may be part of a right triangle, but it does not make the triangle right by itself. Pro tip: look for the small square corner before using right-triangle formulas.",
        },
        {
            "text": r"In a right triangle, the side opposite the \(90^\circ\) angle is called the:",
            "difficulty": 1,
            "choices": [("Hypotenuse", True), ("Base", False), ("Height", False), ("Vertex", False)],
            "explanation": r"The hypotenuse is opposite the right angle and is always the longest side. Base and height can be the legs when finding area, and a vertex is a corner. Pro tip: find the right-angle mark; the side that does not touch it is the hypotenuse.",
        },
        {
            "text": r"The two sides that form the right angle are called the:",
            "difficulty": 1,
            "choices": [("Legs", True), ("Hypotenuses", False), ("Diagonals", False), ("Radii", False)],
            "explanation": r"The legs are the two perpendicular sides that meet at the \(90^\circ\) corner. There is only one hypotenuse, and it is across from that corner. Pro tip: legs touch the square corner; hypotenuse faces it.",
        },
        {
            "text": r"Which equation is the Pythagorean Theorem for a right triangle?",
            "difficulty": 1,
            "choices": [(r"\(a^2+b^2=c^2\)", True), (r"\(a+b=c\)", False), (r"\(2a+2b=c\)", False), (r"\(ab=c^2\)", False)],
            "explanation": r"The Pythagorean Theorem is \(a^2+b^2=c^2\), where \(c\) is the hypotenuse. The trap \(a+b=c\) adds the side lengths directly, which does not work. Pro tip: square the legs first, then take a square root if you need \(c\).",
        },
        {
            "text": r"A right triangle has legs \(3\) and \(4\). What is the hypotenuse?",
            "difficulty": 1,
            "choices": [("5", True), ("7", False), ("12", False), ("25", False)],
            "explanation": r"\(c=\sqrt{3^2+4^2}=\sqrt{9+16}=\sqrt{25}=5\). Choice 7 just adds the legs; 25 forgets the square root. Pro tip: 3-4-5 is the most common right-triangle triple.",
        },
        {
            "text": r"A right triangle has legs \(6\) and \(8\). What is the hypotenuse?",
            "difficulty": 1,
            "choices": [("10", True), ("14", False), ("48", False), ("100", False)],
            "explanation": r"\(\sqrt{6^2+8^2}=\sqrt{36+64}=\sqrt{100}=10\). Choice 14 adds the legs, and 100 is \(c^2\), not \(c\). Pro tip: when the answer is a length, do not stop before the square root.",
        },
        {
            "text": r"A right triangle has legs \(5\) and \(12\). What is the hypotenuse?",
            "difficulty": 1,
            "choices": [("13", True), ("17", False), ("60", False), ("169", False)],
            "explanation": r"\(\sqrt{5^2+12^2}=\sqrt{25+144}=\sqrt{169}=13\). Choice 17 adds \(5+12\), while 169 is the squared hypotenuse. Pro tip: 5-12-13 is a high-value triple to memorize.",
        },
        {
            "text": r"A right triangle has legs \(8\) and \(15\). What is the hypotenuse?",
            "difficulty": 2,
            "choices": [("17", True), ("23", False), ("120", False), ("289", False)],
            "explanation": r"\(\sqrt{8^2+15^2}=\sqrt{64+225}=\sqrt{289}=17\). Choice 23 adds the legs, and 289 is \(c^2\). Pro tip: 8-15-17 is another common triple.",
        },
        {
            "text": r"A right triangle has legs \(2\) and \(3\). What is the exact hypotenuse?",
            "difficulty": 2,
            "choices": [(r"\(\sqrt{13}\)", True), ("5", False), (r"\(\sqrt{5}\)", False), ("13", False)],
            "explanation": r"\(c=\sqrt{2^2+3^2}=\sqrt{4+9}=\sqrt{13}\). Choice 5 adds the legs, and 13 forgets the square root. Pro tip: not every right triangle has whole-number sides; a square-root answer can be correct.",
        },
        {
            "text": r"A right triangle has hypotenuse \(13\) and one leg \(5\). What is the other leg?",
            "difficulty": 2,
            "choices": [("12", True), ("18", False), ("14", False), (r"\(\sqrt{194}\)", False)],
            "explanation": r"For a missing leg, subtract: \(\sqrt{13^2-5^2}=\sqrt{169-25}=\sqrt{144}=12\). Choice 18 adds the given side lengths. Pro tip: if the hypotenuse is given, you are usually subtracting squares.",
        },
        {
            "text": r"A right triangle has hypotenuse \(10\) and one leg \(6\). What is the other leg?",
            "difficulty": 2,
            "choices": [("8", True), ("4", False), ("16", False), (r"\(\sqrt{136}\)", False)],
            "explanation": r"\(\sqrt{10^2-6^2}=\sqrt{100-36}=\sqrt{64}=8\). Choice 16 adds or subtracts lengths instead of squares. Pro tip: missing leg = square root of hypotenuse squared minus known leg squared.",
        },
        {
            "text": r"A right triangle has hypotenuse \(17\) and one leg \(15\). What is the other leg?",
            "difficulty": 2,
            "choices": [("8", True), ("2", False), ("32", False), (r"\(\sqrt{514}\)", False)],
            "explanation": r"\(\sqrt{17^2-15^2}=\sqrt{289-225}=\sqrt{64}=8\). Choice 2 only subtracts \(17-15\). Pro tip: never subtract side lengths directly when using Pythagoras; subtract their squares.",
        },
        {
            "text": r"To find a missing leg when the hypotenuse \(c\) and one leg \(b\) are known, use:",
            "difficulty": 2,
            "choices": [(r"\(\sqrt{c^2-b^2}\)", True), (r"\(\sqrt{c^2+b^2}\)", False), (r"\(c+b\)", False), (r"\(c^2+b^2\)", False)],
            "explanation": r"The hypotenuse square is the total, so remove the known leg's square: \(\sqrt{c^2-b^2}\). Adding would find a side longer than the hypotenuse, which is impossible. Pro tip: hypotenuse missing = add; leg missing = subtract.",
        },
        {
            "text": r"Do the side lengths \(9\), \(12\), and \(15\) form a right triangle?",
            "difficulty": 2,
            "choices": [("Yes, because \(9^2+12^2=15^2\)", True), ("No, because \(9+12\ne15\)", False), ("Yes, because all triangles are right triangles", False), ("No, because 15 is too long", False)],
            "explanation": r"Check the two smaller sides against the largest: \(9^2+12^2=81+144=225=15^2\). So the triangle is right. Pro tip: to test whether three sides make a right triangle, square the two smaller and compare with the largest squared.",
        },
        {
            "text": r"Do the side lengths \(6\), \(8\), and \(11\) form a right triangle?",
            "difficulty": 2,
            "choices": [("No, because \(6^2+8^2\ne11^2\)", True), ("Yes, because \(6+8>11\)", False), ("Yes, because \(6^2+8^2=11^2\)", False), ("No, because 11 is the longest side", False)],
            "explanation": r"\(6^2+8^2=36+64=100\), but \(11^2=121\). The sides may form a triangle, but not a right triangle. Pro tip: the triangle inequality tells whether a triangle can exist; the Pythagorean check tells whether it is right.",
        },
        {
            "text": r"What is the area of a right triangle with legs \(6\) and \(8\)?",
            "difficulty": 1,
            "choices": [("24 square units", True), ("48 square units", False), ("14 square units", False), ("10 square units", False)],
            "explanation": r"Use the legs as base and height: \(A=\frac12(6)(8)=24\). Choice 48 forgets the half. Pro tip: in a right triangle, the legs are already perpendicular, so they make the easiest base-height pair.",
        },
        {
            "text": r"What is the area of a right triangle with legs \(5\) and \(12\)?",
            "difficulty": 1,
            "choices": [("30 square units", True), ("60 square units", False), ("17 square units", False), ("13 square units", False)],
            "explanation": r"\(A=\frac12(5)(12)=30\). Choice 60 is base times height without dividing by 2. Pro tip: every triangle area formula has the half factor.",
        },
        {
            "text": r"A right triangle has legs \(9\) and \(12\), and hypotenuse \(15\). What is its perimeter?",
            "difficulty": 1,
            "choices": [("36", True), ("108", False), ("27", False), ("21", False)],
            "explanation": r"Perimeter means distance around, so add all sides: \(9+12+15=36\). Choice 108 multiplies, and 21 adds only the legs. Pro tip: perimeter always adds side lengths.",
        },
        {
            "text": r"A right triangle has legs \(5\) and \(12\). What is its perimeter?",
            "difficulty": 2,
            "choices": [("30", True), ("17", False), ("60", False), ("25", False)],
            "explanation": r"First find the hypotenuse: \(5,12,13\). Then add all sides: \(5+12+13=30\). Choice 17 adds only the legs. Pro tip: if perimeter asks for all three sides, find any missing side before adding.",
        },
        {
            "text": r"A 13-foot ladder leans against a wall. Its base is 5 feet from the wall. How high up the wall does it reach?",
            "difficulty": 2,
            "choices": [("12 feet", True), ("18 feet", False), ("8 feet", False), ("13 feet", False)],
            "explanation": r"The ladder is the hypotenuse, and the ground distance is one leg. Height \(=\sqrt{13^2-5^2}=\sqrt{144}=12\) feet. Pro tip: ladder problems almost always make the ladder the hypotenuse.",
        },
        {
            "text": r"A ramp rises 6 feet over a horizontal run of 8 feet. How long is the ramp?",
            "difficulty": 2,
            "choices": [("10 feet", True), ("14 feet", False), ("48 feet", False), ("2 feet", False)],
            "explanation": r"The ramp length is the hypotenuse: \(\sqrt{6^2+8^2}=\sqrt{100}=10\) feet. Choice 14 adds rise and run. Pro tip: ramp surface = hypotenuse; rise and run = legs.",
        },
        {
            "text": r"A rectangle is \(7\) units by \(24\) units. What is the length of its diagonal?",
            "difficulty": 2,
            "choices": [("25 units", True), ("31 units", False), ("168 units", False), ("17 units", False)],
            "explanation": r"The diagonal is the hypotenuse of a right triangle with legs 7 and 24: \(\sqrt{7^2+24^2}=\sqrt{625}=25\). Pro tip: rectangle diagonals are right-triangle questions in disguise.",
        },
        {
            "text": r"A student walks 12 blocks east and then 5 blocks north. What is the straight-line distance back to the start?",
            "difficulty": 2,
            "choices": [("13 blocks", True), ("17 blocks", False), ("60 blocks", False), ("7 blocks", False)],
            "explanation": r"East and north are perpendicular legs, so straight-line distance is \(\sqrt{12^2+5^2}=\sqrt{169}=13\). Choice 17 is the walking path, not the straight-line distance. Pro tip: straight-line distance is the hypotenuse.",
        },
        {
            "text": r"In a 45-45-90 right triangle, one leg is \(7\). What is the other leg?",
            "difficulty": 2,
            "choices": [("7", True), ("14", False), (r"\(7\sqrt{2}\)", False), ("3.5", False)],
            "explanation": r"A 45-45-90 triangle has two equal legs, so the other leg is also 7. The value \(7\sqrt2\) would be the hypotenuse. Pro tip: 45-45-90 means equal acute angles and equal legs.",
        },
        {
            "text": r"In a 30-60-90 right triangle, the hypotenuse is \(10\). What is the shorter leg?",
            "difficulty": 3,
            "choices": [("5", True), ("10", False), ("20", False), (r"\(5\sqrt{3}\)", False)],
            "explanation": r"In a 30-60-90 triangle, the shorter leg is half the hypotenuse, so it is \(10/2=5\). The value \(5\sqrt3\) is the longer leg. Pro tip: if the 30-degree angle is given, the side opposite it is the short leg.",
        },
        {
            "text": r"Which item is usually the hypotenuse in a right-triangle word problem?",
            "difficulty": 1,
            "choices": [("A ladder leaning against a wall", True), ("The right angle itself", False), ("The shorter wall height", False), ("The label on a vertex", False)],
            "explanation": r"A ladder leaning against a wall forms the slanted side across from the right angle, so it is the hypotenuse. The wall height and ground distance are legs. Pro tip: diagonal, ladder, ramp, and straight-line distance often signal hypotenuse.",
        },
        {
            "text": r"A student calculates \(6^2+8^2=100\) and answers \(100\) for the hypotenuse. What mistake did the student make?",
            "difficulty": 2,
            "choices": [("They forgot to take the square root", True), ("They should have added 6 and 8 first", False), ("They used the wrong theorem", False), ("They found the missing leg", False)],
            "explanation": r"\(100\) is \(c^2\), not \(c\). The hypotenuse is \(\sqrt{100}=10\). Pro tip: after adding the squares, ask whether the problem wants \(c^2\) or the actual side length \(c\).",
        },
        {
            "text": r"A right triangle has one leg \(8\). What additional information is enough to find the hypotenuse?",
            "difficulty": 2,
            "choices": [("The length of the other leg", True), ("The color of the triangle", False), ("Only that it is a triangle", False), ("The order of the vertices only", False)],
            "explanation": r"To find the hypotenuse with Pythagoras, you need both legs, or one leg plus another side/angle relationship. The other leg is enough because \(c=\sqrt{8^2+\text{other leg}^2}\). Pro tip: identify which two pieces of information connect to the side you need.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Geometry: Right Triangles course (MCQ only)."

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
