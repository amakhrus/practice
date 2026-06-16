"""
Seed written-response (essay) prompts for the local self-assessment feature.

These are open-ended questions students answer in their own words, then compare
against a model "rubric" to grade themselves -- no AI or API key required.

This command is NON-DESTRUCTIVE: for each course it removes only existing
written-response questions and recreates them. Multiple-choice questions (and
their student attempt history) are left untouched.

Run:
    python manage.py seed_essays
"""
from django.core.management.base import BaseCommand
from courses.models import Course
from practice.models import Question


# slug -> list of {text, rubric, difficulty}
ESSAYS = {
    "ged-language-arts": [
        {
            "difficulty": 3,
            "text": (
                "Extended Response. Read the two short arguments, then write an essay explaining which "
                "argument is better supported. Use specific evidence from the passages. (Your own opinion "
                "on the topic is not what is being judged.)\n\n"
                "ARGUMENT A: \"Our school should switch to year-round classes. A district study found that "
                "students lose up to two months of math skills over the long summer break, and that schools "
                "on year-round calendars scored 8% higher on state tests. Shorter, more frequent breaks "
                "help students remember what they learn.\"\n\n"
                "ARGUMENT B: \"Year-round school is a bad idea. Summer is special, and kids deserve a long "
                "break. Everyone I know loved summer vacation, and it would be sad to take that away. School "
                "is stressful enough already.\"\n\n"
                "Which argument is better supported, and why?"
            ),
            "rubric": (
                "A strong response argues that ARGUMENT A is better supported, because it uses specific, "
                "checkable evidence (the district study, the two-month skill loss, the 8% higher scores), "
                "while ARGUMENT B relies on feelings and personal anecdote ('everyone I know', 'it would be "
                "sad'). Give yourself credit for: (1) a clear thesis naming which argument is stronger; "
                "(2) at least two specific pieces of evidence quoted or paraphrased from Argument A; "
                "(3) explaining WHY evidence beats opinion; (4) organized paragraphs and a conclusion. "
                "Deduct if you argued your personal view on year-round school instead of analyzing the two "
                "arguments."
            ),
        },
        {
            "difficulty": 3,
            "text": (
                "Some people believe smartphones should be banned in classrooms because they distract "
                "students. Others believe smartphones are useful learning tools when used responsibly. Write "
                "a well-organized essay that states a clear position and supports it with specific reasons "
                "and examples. Use an introduction, body paragraphs, and a conclusion."
            ),
            "rubric": (
                "Give yourself credit for: (1) a clear thesis that takes ONE side; (2) at least two specific, "
                "relevant reasons or examples (not just opinions); (3) an introduction, focused body "
                "paragraphs each making one point, and a conclusion that restates your position; (4) correct "
                "grammar, punctuation, and varied sentences. Deduct for a missing thesis, disorganized "
                "paragraphs, vague support, or frequent grammar errors."
            ),
        },
    ],
    "ged-life-science": [
        {
            "difficulty": 3,
            "text": (
                "Explain how photosynthesis and cellular respiration are connected. In your answer, name "
                "where each process happens, list the main inputs and outputs of each, and describe how the "
                "two processes form a cycle that keeps carbon and oxygen moving through living things."
            ),
            "rubric": (
                "Full credit for: (1) photosynthesis occurs in chloroplasts, using CO2 + water + light to "
                "make glucose + oxygen; (2) respiration occurs in mitochondria, using glucose + oxygen to "
                "release CO2 + water + energy (ATP); (3) explaining that the outputs of one are the inputs of "
                "the other, forming a cycle. Deduct for missing locations, reversed inputs/outputs, or no "
                "cycle explanation."
            ),
        },
        {
            "difficulty": 3,
            "text": (
                "A moth species comes in light and dark colors. After a forest's tree bark becomes darker "
                "from pollution, the dark moths become far more common over several generations. Use the "
                "four steps of natural selection (variation, inheritance, selection, time) to explain why "
                "this happened."
            ),
            "rubric": (
                "Full credit for applying all four steps: (1) variation -- both light and dark moths exist; "
                "(2) inheritance -- color is passed to offspring; (3) selection -- on dark bark, dark moths "
                "are better camouflaged from predators and survive/reproduce more; (4) time -- over "
                "generations the dark trait becomes more common. Deduct for any missing step or for implying "
                "individual moths changed their own color."
            ),
        },
    ],
    "ged-fractions-decimals-percents": [
        {
            "difficulty": 2,
            "text": (
                "A recipe needs 3/4 cup of sugar, but you want to make only half the recipe. How much sugar "
                "do you need? Show your reasoning, and explain in words why the answer is smaller than 3/4."
            ),
            "rubric": (
                "Full credit for: (1) recognizing 'half of' means 1/2 x 3/4; (2) computing 1/2 x 3/4 = 3/8 "
                "cup; (3) explaining that multiplying by a fraction less than 1 makes the amount smaller. "
                "Deduct for arithmetic errors or a missing explanation."
            ),
        },
    ],
    "ged-geometry-measurement": [
        {
            "difficulty": 3,
            "text": (
                "A cylindrical water tank has a radius of 2 m and a height of 5 m. Explain step by step how "
                "to find its volume, state the formula you use and why, and give the answer in terms of pi "
                "and as a decimal (use pi about 3.14)."
            ),
            "rubric": (
                "Full credit for: (1) identifying the cylinder volume formula V = pi*r^2*h and explaining it "
                "as base area times height; (2) substituting r = 2, h = 5; (3) computing V = pi*(2^2)*5 = "
                "20*pi, about 62.8 cubic meters. Deduct for using diameter instead of radius or for "
                "arithmetic errors."
            ),
        },
    ],
    "ged-data-stats-probability": [
        {
            "difficulty": 2,
            "text": (
                "A student's five test scores are 70, 85, 90, 75, and 80. Find both the mean and the median, "
                "show your work, and explain in a sentence what each number tells you about the student's "
                "performance."
            ),
            "rubric": (
                "Full credit for: (1) mean = (70+85+90+75+80)/5 = 400/5 = 80; (2) ordering 70, 75, 80, 85, 90 "
                "and identifying the median as 80; (3) a sentence explaining the mean as the average and the "
                "median as the middle score. Deduct for arithmetic errors or for not ordering the values "
                "before finding the median."
            ),
        },
    ],
    "ged-social-studies": [
        {
            "difficulty": 3,
            "text": (
                "The U.S. Constitution divides the government into three branches and gives each one ways to "
                "limit the others. Explain what 'checks and balances' means and give two specific examples of "
                "one branch checking another."
            ),
            "rubric": (
                "Full credit for: (1) defining checks and balances as each branch having powers that limit "
                "the others so no branch becomes too powerful; (2) TWO correct examples, such as the "
                "President vetoing a bill from Congress, Congress overriding a veto or impeaching officials, "
                "or the courts ruling a law unconstitutional. Deduct for only one example or for confusing "
                "the branches' roles."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed written-response prompts (non-destructive: leaves MCQs and attempts intact)."

    def handle(self, *args, **options):
        created = 0
        for slug, prompts in ESSAYS.items():
            course = Course.objects.filter(slug=slug).first()
            if not course:
                self.stdout.write(self.style.WARNING(f"skipped (no course): {slug}"))
                continue
            # Remove only existing written prompts; MCQs and their attempts are untouched.
            course.questions.filter(qtype="written").delete()
            for p in prompts:
                Question.objects.create(
                    course=course, qtype="written", text=p["text"],
                    difficulty=p["difficulty"], rubric=p["rubric"], explanation="",
                )
                created += 1
            self.stdout.write(self.style.SUCCESS(
                f"{course.title}: {len(prompts)} written prompt(s)."
            ))
        self.stdout.write(self.style.SUCCESS(f"Done. {created} written-response questions seeded."))
