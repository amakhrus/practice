"""
Seed data: one 'GED Math Basics' course + lessons + practice questions.

Run:
    python manage.py seed_ged_math
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


class Command(BaseCommand):
    help = "Create the sample GED Math course with lessons & questions."

    def handle(self, *args, **options):
        # Delete first if it already exists, so this stays idempotent
        Course.objects.filter(slug="ged-math-dasar").delete()

        course = Course.objects.create(
            title="GED Math Basics",
            slug="ged-math-dasar",
            program="GED",
            subject="math",
            description=(
                "A short basic-math course to prepare for the GED exam. "
                "Covers number operations, percentages, linear equations, and basic geometry. "
                "Includes practice questions with AI explanations & grading."
            ),
        )

        # ---------- Lessons ----------
        lessons = [
            (
                "1. Number Operations & Order of Operations (PEMDAS)",
                "Order of operations: Parentheses, Exponents, Multiplication/Division, "
                "Addition/Subtraction.\n\n"
                r"Example: \(3 + 4 \times 2 = 3 + 8 = 11\) (multiply first, then add)." "\n"
                r"Example: \((3 + 4) \times 2 = 7 \times 2 = 14\) (parentheses come first).",
            ),
            (
                "2. Percentages",
                "Percent means 'per hundred'. To find x% of a number, "
                r"multiply that number by \(\frac{x}{100}\)." "\n\n"
                r"Example: 20% of 150 \(= 150 \times 0.20 = 30\)." "\n"
                r"Increase/discount: final price \(=\) original price \(\times (1 \pm \text{percent})\).",
            ),
            (
                "3. Linear Equations in One Variable",
                r"General form: \(ax + b = c\). The goal is to isolate \(x\)." "\n\n"
                r"Example: \(2x + 5 = 13 \;\Rightarrow\; 2x = 8 \;\Rightarrow\; x = 4\)." "\n"
                "Rule: whatever you do to one side, do to the other side too.",
            ),
            (
                "4. Basic Geometry: Perimeter & Area",
                r"Rectangle: Area \(= l \times w\); Perimeter \(= 2(l + w)\)." "\n"
                r"Triangle: Area \(= \tfrac{1}{2} \times \text{base} \times \text{height}\)." "\n"
                r"Circle: Area \(= \pi r^2\); Circumference \(= 2 \pi r\) (\(\pi \approx 3.14\)).",
            ),
        ]
        for i, (title, content) in enumerate(lessons, start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=i)

        # ---------- Multiple-Choice Questions ----------
        mcqs = [
            {
                "text": r"What is the result of \(3 + 4 \times 2\)?",
                "difficulty": 1,
                "choices": [("11", True), ("14", False), ("10", False), ("24", False)],
                "explanation": r"By PEMDAS, multiplication comes first: \(4 \times 2 = 8\), then \(3 + 8 = 11\).",
            },
            {
                "text": "A shirt costs $80 and is discounted by 25%. What is the price after the discount?",
                "difficulty": 2,
                "choices": [("$60", True), ("$55", False), ("$75", False), ("$20", False)],
                "explanation": r"Discount \(= 80 \times 0.25 = \$20\). Final price \(= 80 - 20 = \$60\).",
            },
            {
                "text": r"If \(2x + 5 = 13\), then the value of \(x\) is ...",
                "difficulty": 2,
                "choices": [("4", True), ("9", False), ("3", False), ("6", False)],
                "explanation": r"\(2x + 5 = 13 \;\Rightarrow\; 2x = 8 \;\Rightarrow\; x = 4\).",
            },
            {
                "text": r"The area of a rectangle with length \(8\,\text{cm}\) and width \(5\,\text{cm}\) is ...",
                "difficulty": 1,
                "choices": [(r"\(40\,\text{cm}^2\)", True), (r"\(26\,\text{cm}^2\)", False),
                            (r"\(13\,\text{cm}^2\)", False), (r"\(45\,\text{cm}^2\)", False)],
                "explanation": r"Area \(= l \times w = 8 \times 5 = 40\,\text{cm}^2\).",
            },
            {
                "text": r"A triangle has a base of \(10\,\text{cm}\) and a height of \(6\,\text{cm}\). What is its area?",
                "difficulty": 2,
                "choices": [(r"\(30\,\text{cm}^2\)", True), (r"\(60\,\text{cm}^2\)", False),
                            (r"\(16\,\text{cm}^2\)", False), (r"\(32\,\text{cm}^2\)", False)],
                "explanation": r"Triangle area \(= \tfrac{1}{2} \times \text{base} \times \text{height} = \tfrac{1}{2} \times 10 \times 6 = 30\,\text{cm}^2\).",
            },
            {
                "text": r"Find the roots of the quadratic equation \(x^2 - 5x + 6 = 0\).",
                "difficulty": 2,
                "choices": [(r"\(x = 2\) or \(x = 3\)", True), (r"\(x = 1\) or \(x = 6\)", False),
                            (r"\(x = -2\) or \(x = -3\)", False), (r"\(x = 2\) or \(x = -3\)", False)],
                "explanation": r"Factor: \(x^2 - 5x + 6 = (x-2)(x-3) = 0\), so \(x = 2\) or \(x = 3\).",
            },
            {
                "text": r"Calculate the value of \(7^2 + 3^2\).",
                "difficulty": 1,
                "choices": [(r"\(58\)", True), (r"\(40\)", False), (r"\(100\)", False), (r"\(21\)", False)],
                "explanation": r"\(7^2 = 49\) and \(3^2 = 9\), so \(49 + 9 = 58\).",
            },
            {
                "text": r"What is the value of \(\sqrt{144}\)?",
                "difficulty": 1,
                "choices": [(r"\(12\)", True), (r"\(14\)", False), (r"\(72\)", False), (r"\(24\)", False)],
                "explanation": r"\(\sqrt{144} = 12\) because \(12^2 = 144\).",
            },
            {
                "text": r"A right triangle has legs of \(6\,\text{cm}\) and \(8\,\text{cm}\). "
                        r"Its hypotenuse is \(\sqrt{6^2 + 8^2}\), which equals ...",
                "difficulty": 2,
                "choices": [(r"\(10\,\text{cm}\)", True), (r"\(14\,\text{cm}\)", False),
                            (r"\(48\,\text{cm}\)", False), (r"\(\sqrt{14}\,\text{cm}\)", False)],
                "explanation": r"Pythagorean theorem: \(\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10\,\text{cm}\).",
            },
        ]
        for q in mcqs:
            question = Question.objects.create(
                course=course,
                qtype="mcq",
                text=q["text"],
                difficulty=q["difficulty"],
                explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)

        # Phase 1 is MCQ-only: written-response prompts are not seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Successfully created course '{course.title}' "
            f"with {course.lessons.count()} lessons & {course.questions.count()} questions."
        ))
