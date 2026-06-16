"""
Seed data: 'GED Science: Scientific Reasoning & Practices' -- the cross-cutting
skills strand of the GED Science test.

The three content courses (Life, Physical, Earth & Space Science) teach *what*
to know. But roughly half of every GED Science item tests *how* to think like a
scientist: designing a fair test, reading tables and graphs, summarizing data,
and drawing conclusions that the evidence actually supports. This course teaches
those reasoning skills directly, so they transfer to every science passage on
test day. Each lesson leads with intuition and a real example, includes a
labeled diagram, a common-misconception warning, and a quick tip. Practice
questions are deliberately content-light so the focus stays on the reasoning.

Run:
    python manage.py seed_ged_science_practices
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Scientific Reasoning & Practices",
    "slug": "ged-science-reasoning-practices",
    "program": "GED",
    "subject": "science",
    "description": (
        "About half of the GED Science test is not about memorizing facts -- it is about "
        "thinking like a scientist. This course builds those test-day skills directly: how "
        "to design a fair experiment, read tables and graphs, tell correlation from "
        "causation, summarize data with averages and probability, handle scientific "
        "notation and units, and draw conclusions an examiner will accept. These reasoning "
        "skills work hand in hand with the Life, Physical, and Earth & Space Science courses "
        "and apply to every passage you will see on the real test."
    ),
    "lessons": [
        (
            "1. How Science Works: The Scientific Method",
            r"Science is not a pile of facts — it is a **method** for figuring out which ideas about the world are true. The GED test rewards you for following that method, so learn its steps." "\n\n"
            r"[[figure:scientific_method|Science is a loop, not a straight line. A surprising result sends you back to ask a better question.]]" "\n\n"
            r"The key word is **hypothesis** — a *testable, falsifiable* prediction, usually phrased 'if … then …'. For example: 'If plants get more sunlight, then they will grow taller.' A good hypothesis can be proven **wrong** by an experiment; that is what makes it scientific." "\n\n"
            r"A few terms the test uses:" "\n"
            r"- **Observation** — something you notice with your senses or instruments (a fact)." "\n"
            r"- **Hypothesis** — a proposed, testable explanation or prediction." "\n"
            r"- **Theory** — an explanation supported by a large body of evidence (evolution, plate tectonics). A theory is *not* a guess." "\n"
            r"- **Law** — a description of *what* happens, often as a formula (the law of gravity), but not necessarily *why*." "\n\n"
            r"⚠️ Common misconception: in everyday speech a 'theory' means a hunch. In science, a theory is one of the strongest things there is — it has survived years of testing." "\n\n"
            r"💡 Tip: if a statement could never be shown false by any experiment, it is not a scientific hypothesis.",
        ),
        (
            "2. Designing a Fair Test: Variables & Controls",
            r"To find out whether one thing causes another, scientists run a **controlled experiment**: they change one thing at a time and watch what happens, holding everything else steady." "\n\n"
            r"[[figure:controlled_experiment|Change one variable, measure one variable, and keep all the others the same.]]" "\n\n"
            r"- The **independent variable** is the one thing *you* deliberately change (the cause)." "\n"
            r"- The **dependent variable** is what you *measure* in response (the result)." "\n"
            r"- The **controlled variables** are everything else you keep the same so the comparison is fair." "\n\n"
            r"The **control group** gets no treatment (or the normal amount) and acts as a baseline to compare against. Example: to test whether a fertilizer helps tomatoes, you give Group A fertilizer and Group B none. Fertilizer is the **independent** variable; plant height is the **dependent** variable; the **control group** is Group B; and sunlight, water, soil, and pot size must be kept identical for both groups." "\n\n"
            r"⚠️ Common misconception: if you change *two* things at once (more fertilizer **and** more water), and the plants grow, you cannot tell which change caused it. A fair test changes only **one** variable." "\n\n"
            r"💡 Tip: spot the independent variable by asking 'what did the researcher choose to change?' The dependent variable is 'what did they measure to see the effect?'",
        ),
        (
            "3. Reading Data: Tables, Bar Graphs & Line Graphs",
            r"Most GED Science questions hand you a table or graph and ask what it shows. Before any calculation, **read the labels**: the title, the axis names, and the **units**." "\n\n"
            r"**Bar graphs** compare separate categories — taller bar, bigger value." "\n\n"
            r"[[figure:bar_toppings|Each bar stands alone; compare their heights to compare the categories.]]" "\n\n"
            r"**Line graphs** show how something changes — usually over time. Follow the line to read the **trend**." "\n\n"
            r"[[figure:line_sales|A rising line means the value is increasing as you move right.]]" "\n\n"
            r"**Tables** give exact numbers in rows and columns; find the row and column the question asks about and read across." "\n\n"
            r"A reliable routine for any figure:" "\n"
            r"- Read the **title** — what is this about?" "\n"
            r"- Read each **axis label and its units** — what is being measured?" "\n"
            r"- Find the **specific value or trend** the question asks for." "\n\n"
            r"⚠️ Common misconception: don't ignore the **scale**. If each gridline is 50 units, a bar two lines tall is 100, not 2. A graph can also look dramatic only because its scale starts at 90 instead of 0." "\n\n"
            r"💡 Tip: the answer to most data questions is *on the figure*. Resist using outside knowledge — point to the exact bar, row, or part of the line.",
        ),
        (
            "4. Finding Patterns: Trends, Correlation & Causation",
            r"Once you can read a graph, the next skill is describing the **relationship** between two variables." "\n\n"
            r"A **scatterplot** plots paired measurements as dots. The overall drift of the dots is the **trend**:" "\n\n"
            r"[[figure:scatter_trend|The dots drift upward to the right — a positive relationship between the two variables.]]" "\n\n"
            r"- A **positive correlation**: as one variable goes up, the other tends to go up." "\n"
            r"- A **negative correlation**: as one goes up, the other tends to go down." "\n"
            r"- **No correlation**: the dots form no pattern." "\n\n"
            r"Here is the single most-tested idea in this whole course: **correlation does not prove causation**. Two things rising together does not mean one *causes* the other. Ice-cream sales and drowning deaths both rise in summer — but ice cream doesn't cause drowning. A hidden third factor (hot weather) drives both." "\n\n"
            r"To claim that A *causes* B, you need a **controlled experiment** (Lesson 2), not just a correlation." "\n\n"
            r"⚠️ Common misconception: a strong, clear pattern still isn't proof of cause. Always ask, 'could a third factor explain both?'" "\n\n"
            r"💡 Tip: when an answer choice says one thing *causes* another but the data is only an observed correlation, it is almost always the trap.",
        ),
        (
            "5. Summarizing Data: Averages, Spread & Probability",
            r"Science often boils a column of numbers down to a few summary values. The GED expects you to compute them." "\n\n"
            r"**Mean** (average): add all values, divide by how many there are." "\n"
            r"\[ \text{mean} = \frac{\text{sum of values}}{\text{number of values}}. \]" "\n"
            r"For the measurements \(4, 8, 6, 2\): \(\frac{4+8+6+2}{4} = \frac{20}{4} = 5\)." "\n\n"
            r"[[figure:mean_bars|The mean is the 'balance point' of the data — the dashed line that evens out the bars.]]" "\n\n"
            r"**Median**: put the values *in order* and take the middle one. **Mode**: the most frequent value. **Range**: largest − smallest, a quick measure of spread." "\n\n"
            r"**Probability** measures how likely an outcome is, from 0 (impossible) to 1 (certain):" "\n"
            r"\[ P(\text{event}) = \frac{\text{favorable outcomes}}{\text{total outcomes}}. \]" "\n\n"
            r"[[figure:prob_scale|Every probability sits between 0 and 1; it can be written as a fraction, decimal, or percent.]]" "\n\n"
            r"In genetics, for instance, a cross that gives 3 dominant to 1 recessive means \(P(\text{recessive}) = \frac{1}{4} = 0.25 = 25\%\)." "\n\n"
            r"⚠️ Common misconception: the **mean** can be pulled far off by one extreme value. When data has an outlier (one huge or tiny number), the **median** describes the 'typical' value better." "\n\n"
            r"💡 Tip: always order the numbers before finding the median — forgetting to sort is the most common error.",
        ),
        (
            "6. The Math of Science: Units, Notation & Percent",
            r"Science questions are full of very large and very small numbers, so a little math fluency pays off." "\n\n"
            r"**Scientific notation** writes a number as a digit between 1 and 10 times a power of ten. A positive exponent means a large number; a negative exponent means a small one:" "\n"
            r"\[ 6{,}000{,}000 = 6 \times 10^{6}, \qquad 0.0004 = 4 \times 10^{-4}. \]" "\n"
            r"The exponent just counts how many places the decimal point moves." "\n\n"
            r"**Units** must always travel with a number — '37' is meaningless, but '37 °C' is body temperature. Watch for **metric prefixes**:" "\n"
            r"- **kilo-** = 1000 (1 km = 1000 m)" "\n"
            r"- **centi-** = 1/100 (1 cm = 0.01 m)" "\n"
            r"- **milli-** = 1/1000 (1 mL = 0.001 L)" "\n\n"
            r"**Percent** means 'per hundred', and shows up as efficiency, concentration, and 'percent change':" "\n"
            r"\[ \text{percent change} = \frac{\text{new} - \text{old}}{\text{old}} \times 100\%. \]" "\n"
            r"A population rising from 200 to 250: \(\frac{250-200}{200} = \frac{50}{200} = 0.25 = 25\%\) increase." "\n\n"
            r"⚠️ Common misconception: \(10^{-4}\) is a small *positive* number (0.0001), not a negative number. The minus sign is on the exponent, not the value." "\n\n"
            r"💡 Tip: when comparing measurements, convert them to the **same unit first** — you can't compare 500 mL to 2 L until both are in liters (0.5 L vs 2 L).",
        ),
        (
            "7. Drawing Conclusions: Evidence, Inference & Error",
            r"The final reasoning skill is judging which conclusions the evidence actually supports — and which go too far." "\n\n"
            r"- An **observation** is what the data directly shows ('the treated plants averaged 5 cm taller')." "\n"
            r"- An **inference** is a reasonable interpretation that goes a step beyond ('the fertilizer probably helped them grow')." "\n"
            r"- A **valid conclusion** stays *within* what the data supports; an **overreach** claims more than the evidence allows ('this fertilizer makes any plant grow taller anywhere')." "\n\n"
            r"Strong science also values **replication** — a result you can repeat is far more trustworthy than a one-time finding — and a **large sample size**, because a few data points can mislead while many reveal the real pattern." "\n\n"
            r"On the test, the best answer is usually the most **cautious** one that the data still backs up. Watch for trap choices that use absolute words like *always*, *never*, *proves*, or *all* — real data rarely supports them." "\n\n"
            r"Example: a study finds students who ate breakfast scored higher on one test at one school. A valid conclusion: 'breakfast was associated with higher scores in this group.' An overreach: 'breakfast guarantees better grades for everyone.'" "\n\n"
            r"⚠️ Common misconception: a single experiment rarely 'proves' anything for all time. Science builds confidence through repeated, consistent results." "\n\n"
            r"💡 Tip: match the conclusion to the data's *scope*. If the study tested tomatoes, the conclusion can only be about tomatoes — not 'all plants'.",
        ),
    ],
    "mcqs": [
        {
            "text": r"Which statement is a scientific hypothesis?",
            "difficulty": 2,
            "choices": [
                ("If a plant is given more sunlight, then it will grow taller", True),
                ("Sunsets are the most beautiful sight in nature", False),
                ("Plants are important to the world", False),
                ("Everyone should water their plants daily", False),
            ],
            "explanation": r"A hypothesis is a testable, falsifiable prediction, usually 'if … then …'. The others are opinions or value statements that no experiment could prove false.",
        },
        {
            "text": r"In science, the word 'theory' (as in the theory of evolution) means:",
            "difficulty": 2,
            "choices": [
                ("An explanation supported by a large body of evidence", True),
                ("A wild guess with no evidence", False),
                ("A fact that can never be questioned", False),
                ("A mathematical formula", False),
            ],
            "explanation": r"A scientific theory is a well-supported explanation tested many times — not a hunch. A formula that only describes what happens is closer to a scientific law.",
        },
        {
            "text": r"A student tests whether fertilizer affects plant growth. She gives Group A fertilizer and Group B none, keeping light, water, and soil the same. What is the independent variable?",
            "difficulty": 2,
            "choices": [
                ("The amount of fertilizer", True),
                ("The height of the plants", False),
                ("The amount of water", False),
                ("The type of soil", False),
            ],
            "explanation": r"The independent variable is the one thing the researcher deliberately changes — here, the fertilizer. Plant height is the dependent variable (what is measured); water and soil are controlled variables.",
        },
        {
            "text": r"In the same fertilizer experiment, what is the purpose of Group B, which gets no fertilizer?",
            "difficulty": 2,
            "choices": [
                ("It is the control group, a baseline for comparison", True),
                ("It is the independent variable", False),
                ("It makes the experiment take longer", False),
                ("It is the hypothesis", False),
            ],
            "explanation": r"The group that receives no treatment is the control group. Comparing it to the treated group shows whether the fertilizer actually made a difference.",
        },
        {
            "text": r"Why should a fair test change only ONE variable at a time?",
            "difficulty": 2,
            "choices": [
                ("So you can tell which change caused the result", True),
                ("To make the experiment finish faster", False),
                ("Because more than one variable is impossible to measure", False),
                ("So the hypothesis is always correct", False),
            ],
            "explanation": r"If two variables change at once, you can't know which one caused the effect. Changing only one keeps the comparison fair.",
        },
        {
            "text": r"A line graph shows a company's sales rising each month from January to June. What does this trend indicate?",
            "difficulty": 1,
            "choices": [
                ("Sales increased over time", True),
                ("Sales stayed the same", False),
                ("Sales decreased over time", False),
                ("There is not enough information to tell", False),
            ],
            "explanation": r"A line that climbs as you move right shows the measured value increasing over time — here, rising sales.",
        },
        {
            "text": r"On a bar graph, each gridline represents 50 units. A bar reaches the third gridline. What value does it show?",
            "difficulty": 2,
            "choices": [
                ("150", True),
                ("3", False),
                ("50", False),
                ("300", False),
            ],
            "explanation": r"Read the scale: 3 gridlines × 50 units each = 150. Ignoring the scale and reading '3' is the classic mistake.",
        },
        {
            "text": r"A scatterplot shows that as study time increases, test scores increase. This is an example of:",
            "difficulty": 2,
            "choices": [
                ("A positive correlation", True),
                ("A negative correlation", False),
                ("No correlation", False),
                ("Proof that studying causes higher scores", False),
            ],
            "explanation": r"When both variables rise together, the correlation is positive. Note that a correlation alone does not prove causation.",
        },
        {
            "text": r"A town finds that as ice-cream sales rise, the number of sunburns also rises. What is the best conclusion?",
            "difficulty": 3,
            "choices": [
                ("A third factor, like hot sunny weather, likely causes both", True),
                ("Eating ice cream causes sunburn", False),
                ("Sunburns cause people to buy ice cream", False),
                ("The data must be incorrect", False),
            ],
            "explanation": r"This is correlation, not causation. Two things rising together doesn't mean one causes the other; hot weather drives both.",
        },
        {
            "text": r"Find the mean (average) of these measurements: \(4,\ 8,\ 6,\ 2\).",
            "difficulty": 1,
            "choices": [
                (r"\(5\)", True),
                (r"\(6\)", False),
                (r"\(20\)", False),
                (r"\(4\)", False),
            ],
            "explanation": r"Mean \(= \frac{4+8+6+2}{4} = \frac{20}{4} = 5\).",
        },
        {
            "text": r"A data set is \(3, 4, 4, 5, 100\). Which measure best describes the 'typical' value, given the outlier?",
            "difficulty": 3,
            "choices": [
                ("The median (4)", True),
                ("The mean (23.2)", False),
                ("The range (97)", False),
                ("The largest value (100)", False),
            ],
            "explanation": r"The single extreme value (100) drags the mean up to 23.2, which represents none of the data well. The median, 4, better describes a typical value.",
        },
        {
            "text": r"Write the number \(0.0004\) in scientific notation.",
            "difficulty": 2,
            "choices": [
                (r"\(4 \times 10^{-4}\)", True),
                (r"\(4 \times 10^{4}\)", False),
                (r"\(4 \times 10^{-3}\)", False),
                (r"\(0.4 \times 10^{-3}\)", False),
            ],
            "explanation": r"Move the decimal point 4 places to the right to get 4, so the exponent is \(-4\): \(0.0004 = 4 \times 10^{-4}\). The negative exponent marks a small number, not a negative one.",
        },
        {
            "text": r"A bacteria population grows from \(200\) to \(250\). What is the percent increase?",
            "difficulty": 2,
            "choices": [
                (r"\(25\%\)", True),
                (r"\(50\%\)", False),
                (r"\(20\%\)", False),
                (r"\(80\%\)", False),
            ],
            "explanation": r"Percent change \(= \frac{\text{new}-\text{old}}{\text{old}} = \frac{250-200}{200} = \frac{50}{200} = 0.25 = 25\%\).",
        },
        {
            "text": r"A study at one school found that students who ate breakfast scored higher on one test. Which conclusion does the data BEST support?",
            "difficulty": 3,
            "choices": [
                ("In this group, eating breakfast was associated with higher scores", True),
                ("Eating breakfast guarantees better grades for everyone", False),
                ("Skipping breakfast always lowers test scores", False),
                ("Breakfast proves intelligence", False),
            ],
            "explanation": r"A valid conclusion stays within the data's scope: one group, one test, an association. The other choices overreach with words like 'guarantees', 'always', and 'everyone'.",
        },
        {
            "text": r"Why do scientists value replication (repeating an experiment) and large sample sizes?",
            "difficulty": 2,
            "choices": [
                ("Repeated, consistent results from more data are more trustworthy", True),
                ("It makes the experiment more expensive", False),
                ("A single trial always proves a hypothesis", False),
                ("Large samples remove the need for a control group", False),
            ],
            "explanation": r"One trial or a tiny sample can mislead. Results that repeat across many data points are far more reliable evidence.",
        },
    ],
    "essays": [
        {
            "text": (
                "A gardener claims that playing music helps her tomato plants grow taller. "
                "Design a controlled experiment to test this claim. In your answer, identify the "
                "independent variable, the dependent variable, at least two controlled variables, "
                "and the control group."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) independent variable = whether music is played (and ideally how "
                "much); (2) dependent variable = plant height/growth; (3) at least two controlled "
                "variables held the same (water, light, soil, temperature, plant type); (4) a control "
                "group of plants with no music. Deduct for changing more than one variable or omitting "
                "the control group."
            ),
        },
        {
            "text": (
                "A news headline reads: 'Study shows people who drink coffee live longer — so drink "
                "more coffee!' Using what you know about correlation, causation, and drawing valid "
                "conclusions, explain what is wrong with this headline and what the study can and "
                "cannot actually claim."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) identifying that the study shows a correlation, not proof of "
                "causation; (2) noting a third factor could explain both (e.g. coffee drinkers may be "
                "wealthier or more social); (3) explaining the headline overreaches by turning an "
                "association into advice ('drink more'); (4) stating a valid conclusion stays within "
                "the data. Deduct for accepting the causal claim or missing the third-factor idea."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the 'GED Science: Scientific Reasoning & Practices' course."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent
        course = Course.objects.create(
            title=COURSE["title"],
            slug=COURSE["slug"],
            program=COURSE["program"],
            subject=COURSE["subject"],
            description=COURSE["description"],
        )
        for i, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=i)

        for q in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course, qtype="mcq", text=q["text"],
                difficulty=q["difficulty"], explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)

        # Phase 1 is MCQ-only: written-response prompts are not seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
