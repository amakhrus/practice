"""
Seed data: 'GED Science: Homeostasis & Life Science Data (Deep Dive)'.

A focused EXPANSION of Lesson 7 ("Homeostasis & Reading Science Data") from the
broader 'GED Science: Life Science' course, brought up to the full deep-dive
standard (6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. Homeostasis & feedback loops.
  2. Regulating temperature, water & blood sugar.
  3. Responding to the environment (animals and plants).
  4. Reading graphs and tables.
  5. Claims, evidence & designing experiments.
  6. Correlation vs. causation.

This course uses ALL-NEW diagrams (a negative-feedback loop, thermoregulation,
plant stomata, a blood-glucose graph, the parts of an experiment, and a
correlation-vs-causation illustration).

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Biology* and *Anatomy & Physiology* (homeostasis, feedback).
  - University of California Museum of Paleontology / "Understanding Science"
    (claims, evidence, experiments).
  - NIH / MedlinePlus (blood glucose, temperature regulation).
Note: most homeostasis uses NEGATIVE feedback (the response reverses the change).
Correlation (two variables changing together) does not prove causation; a
controlled experiment changes one variable while holding others constant.

Run:
    python manage.py seed_ged_homeostasis_data
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Homeostasis & Life Science Data (Deep Dive)",
    "slug": "ged-homeostasis-data",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into how living things stay in balance and how to reason with science data, "
        "expanding the single 'Homeostasis & Reading Science Data' lesson from the GED Life Science "
        "course into a full mini-course. You'll learn how feedback loops keep conditions like "
        "temperature, water, and blood sugar stable, how organisms respond to their environment, and "
        "the core science-reasoning skills the GED rewards: reading graphs and tables, telling claims "
        "from evidence, designing fair experiments, and knowing why correlation is not causation. Plain "
        "language, all-new labeled diagrams, common-misconception warnings, and GED-style practice."
    ),
    "lessons": [
        (
            "1. Homeostasis & Feedback Loops",
            r"**Homeostasis** is the process of keeping the body's internal conditions within a healthy **range**, even when the outside world changes. Body temperature, blood sugar, water balance, oxygen level, and pH all need to be regulated. These conditions don't stay perfectly fixed — they **fluctuate** around a normal **set point**." "\n\n"
            r"[[figure:feedback_loop|A feedback loop: a change is detected by a sensor, a control center responds through an effector, and the change is reversed back toward normal.]]" "\n\n"
            r"Homeostasis works through **feedback loops** with three parts:" "\n"
            r"- A **sensor (receptor)** detects a change." "\n"
            r"- A **control center** compares the change to the set point." "\n"
            r"- An **effector** carries out a response." "\n\n"
            r"Most homeostasis uses **negative feedback**, meaning the response **reverses** the original change. If you get too hot, you sweat to cool down; if you get too cold, you shiver to warm up. Both responses push the body **back toward normal**." "\n\n"
            r"⚠️ Common misconception: 'negative feedback' is **not** 'bad' feedback. It is called negative because the response works **against** the change, returning the body toward its set point." "\n\n"
            r"💡 Tip: homeostasis is the body **fighting change to stay near normal** — detect, respond, reverse.",
        ),
        (
            "2. Regulating Temperature, Water & Blood Sugar",
            r"Let's see homeostasis in action with three conditions the body works hard to control." "\n\n"
            r"[[figure:thermoregulation|If you get too hot, the body sweats and widens skin blood vessels; if too cold, it shivers and narrows them — both returning you to normal.]]" "\n\n"
            r"- **Body temperature.** When you're **too hot**, you **sweat** (evaporation removes heat) and blood vessels in the skin **widen** to release heat. When you're **too cold**, you **shiver** (muscle activity makes heat) and skin vessels **narrow** to hold heat in." "\n"
            r"- **Water balance.** The **kidneys** and hormones manage water. If you're **dehydrated**, the kidneys conserve water and urine becomes **concentrated**. If you drink a **lot** of water, the kidneys release more, making urine **dilute**." "\n"
            r"- **Blood sugar.** After a meal, blood glucose rises; the hormone **insulin** helps cells take in glucose and brings the level back down. If glucose drops too low, other responses release stored glucose." "\n\n"
            r"⚠️ Common misconception: homeostasis does **not** mean nothing changes. It means the body **responds to changes** to stay within a workable range." "\n\n"
            r"💡 Tip: for any example, find the **variable**, the **change**, and the **response that reverses it**.",
        ),
        (
            "3. Responding to the Environment",
            r"The outside world constantly challenges homeostasis — heat, cold, dehydration, high altitude, injury, disease, and food shortages can all push an organism away from its normal range. Living things survive by **responding**: behaviorally, physically, or chemically." "\n\n"
            r"[[figure:stomata|A plant opens its stomata for gas exchange and closes them during a drought to conserve water — its own kind of homeostasis.]]" "\n\n"
            r"Examples are everywhere:" "\n"
            r"- In **heat**, humans sweat and seek **shade** (a behavior). In **cold**, they shiver and reduce blood flow to the skin." "\n"
            r"- At **high altitude**, where there is less oxygen, the body **breathes faster** and, over time, makes more **red blood cells**." "\n"
            r"- **Plants** respond too: they **close their stomata** (tiny leaf pores) to reduce water loss in a drought, grow roots toward water, or drop leaves in a dry season." "\n\n"
            r"⚠️ Common misconception: **only humans** maintain homeostasis. In fact, **all living things** regulate their internal conditions in some way — including plants and single-celled organisms." "\n\n"
            r"💡 Tip: the pattern is always **environmental change → response → return toward balance.**",
        ),
        (
            "4. Reading Graphs & Tables",
            r"Half of GED Science is **reasoning with data**, not just recalling facts. The skill is reading a graph or table carefully before you answer." "\n\n"
            r"[[figure:blood_glucose_graph|Blood glucose rises after a meal and then returns to the normal range — a graph that shows homeostasis at work.]]" "\n\n"
            r"A reliable routine:" "\n"
            r"- Read the **title, axis labels, units, and legend** first." "\n"
            r"- Identify the **trend** — is the line rising, falling, or steady?" "\n"
            r"- Notice **sudden changes**, which may mark a stimulus, treatment, or event." "\n\n"
            r"**Worked example.** A graph shows **blood glucose rising after a meal and then returning** near the starting level. That pattern is evidence of **homeostasis**: the body responded to bring glucose back toward normal. A strong answer points to the **specific pattern**, not just general memory." "\n\n"
            r"And always watch the **units**: a change from 37.0 to 37.5 °C is small, but a change from 37 to 75 °C would be biologically extreme." "\n\n"
            r"⚠️ Common misconception: don't **ignore the units or the scale**. The same number can mean very different things depending on the units." "\n\n"
            r"💡 Tip: a good data answer **points to a specific row, bar, point, or trend** in the figure.",
        ),
        (
            "5. Claims, Evidence & Designing Experiments",
            r"Science questions often ask which **evidence** supports a **claim**. Keeping these terms straight is the key." "\n\n"
            r"[[figure:experiment_variables|A fair experiment changes one thing (the independent variable), measures the result (the dependent variable), and keeps everything else the same (controlled variables).]]" "\n\n"
            r"- A **claim** is a conclusion." "\n"
            r"- **Evidence** is the data or observations that support it." "\n"
            r"- **Reasoning** explains *why* the evidence supports the claim." "\n\n"
            r"Strong answers stay **close to the data provided**. And to test a cause-and-effect idea, scientists run a **controlled experiment**:" "\n"
            r"- The **independent variable** is the one thing the experimenter **changes**." "\n"
            r"- The **dependent variable** is the result they **measure**." "\n"
            r"- The **controlled variables** are kept the **same** so the test is fair." "\n\n"
            r"**Repeated trials** and **larger sample sizes** make results more **reliable**." "\n\n"
            r"⚠️ Common misconception: a single result or a pattern by itself does **not** prove a cause. A fair, repeated, controlled test is what builds confidence." "\n\n"
            r"💡 Tip: **independent = what you change; dependent = what you measure; controlled = kept the same.**",
        ),
        (
            "6. Correlation vs. Causation",
            r"The most important data-reasoning trap on the GED is confusing **correlation** with **causation**." "\n\n"
            r"[[figure:correlation_causation|Ice cream sales and sunburns rise together, but neither causes the other — hot, sunny weather causes both.]]" "\n\n"
            r"- **Correlation** means two variables **change together** (as one goes up, so does the other)." "\n"
            r"- **Causation** means one variable **directly causes** a change in the other." "\n\n"
            r"Two things can be correlated without one causing the other — often a **third factor** is responsible. For example, **ice cream sales** and **sunburns** both rise in summer, but eating ice cream doesn't cause sunburns. The real cause of **both** is **hot, sunny weather**." "\n\n"
            r"To support a claim that one thing **causes** another, you need a **controlled experiment** (Lesson 5), not just a graph showing the two rising together. When a GED question shows a correlation, the safest answer usually notes that **more testing is needed** or that a **third factor** may be involved." "\n\n"
            r"⚠️ Common misconception: a pattern **alone** does not prove cause. **Correlation is not causation** — a hidden third factor can make two variables move together." "\n\n"
            r"💡 Tip: before claiming a cause, look for a **controlled experiment** and ask whether a **third factor** could explain the pattern." "\n\n"
            r"📚 Sources: OpenStax *Biology* / *Anatomy & Physiology*; UC Museum of Paleontology, *Understanding Science*; NIH / MedlinePlus.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: homeostasis & feedback ---
        {
            "text": r"Homeostasis means:",
            "difficulty": 1,
            "choices": [("Maintaining stable internal conditions within a healthy range", True),
                        ("Never changing anything at all", False),
                        ("Only digesting food", False),
                        ("Producing offspring", False)],
            "explanation": r"Homeostasis keeps internal conditions (like temperature and blood sugar) within a workable range, even as the environment changes.",
        },
        {
            "text": r"In a feedback loop, the part that DETECTS a change is the:",
            "difficulty": 2,
            "choices": [("Sensor (receptor)", True), ("Effector", False),
                        ("Bone", False), ("Hormone storage", False)],
            "explanation": r"A sensor detects the change, the control center compares it to the set point, and the effector carries out the response.",
        },
        {
            "text": r"Sweating when your body temperature rises is an example of:",
            "difficulty": 1,
            "choices": [("Negative feedback", True), ("Meiosis", False),
                        ("Photosynthesis", False), ("Mutation", False)],
            "explanation": r"Sweating reverses the temperature increase, returning the body toward normal — that is negative feedback.",
        },
        {
            "text": ("Use the feedback diagram.\n\n"
                     "[[figure:feedback_loop|A negative-feedback loop]]\n\n"
                     "In the diagram, the response works to:"),
            "difficulty": 2,
            "choices": [("Reverse the change and return the condition to normal", True),
                        ("Make the change even larger", False),
                        ("Stop the body from sensing anything", False),
                        ("Permanently change the set point", False)],
            "explanation": r"The loop shows the response pushing the condition back toward the set point. Pro tip: negative feedback opposes the change.",
        },
        {
            "text": r"Why is it called 'negative' feedback?",
            "difficulty": 3,
            "choices": [("The response opposes (reverses) the original change", True),
                        ("It always harms the body", False),
                        ("It only happens at night", False),
                        ("It removes all feedback", False)],
            "explanation": r"'Negative' refers to the direction of the response — it counteracts the change, not that it is bad.",
        },
        # --- Lesson 2: temperature, water, blood sugar ---
        {
            "text": r"When you get cold and start to shiver, the shivering helps to:",
            "difficulty": 1,
            "choices": [("Raise body temperature", True), ("Lower body temperature", False),
                        ("Stop the heart", False), ("Make glucose by photosynthesis", False)],
            "explanation": r"Shivering is rapid muscle activity that generates heat, helping warm the body back toward normal.",
        },
        {
            "text": r"After a person drinks a large amount of water, the kidneys most likely produce:",
            "difficulty": 2,
            "choices": [("More dilute urine", True), ("More concentrated urine", False),
                        ("No urine at all", False), ("Oxygen gas", False)],
            "explanation": r"When water is plentiful, the kidneys release more of it, so urine becomes more dilute. When dehydrated, they conserve water and urine is concentrated.",
        },
        {
            "text": r"Which hormone helps LOWER blood sugar after a meal?",
            "difficulty": 2,
            "choices": [("Insulin", True), ("Chlorophyll", False),
                        ("Hemoglobin", False), ("Adrenaline only", False)],
            "explanation": r"Insulin helps cells take in glucose and helps store the excess, bringing blood sugar back down toward normal.",
        },
        {
            "text": ("Use the temperature diagram.\n\n"
                     "[[figure:thermoregulation|How the body responds to heat and cold]]\n\n"
                     "When body temperature rises above normal, the body responds by:"),
            "difficulty": 2,
            "choices": [("Sweating and widening skin blood vessels to release heat", True),
                        ("Shivering to make more heat", False),
                        ("Narrowing skin blood vessels to keep heat", False),
                        ("Doing nothing", False)],
            "explanation": r"The diagram shows the 'too hot' response: sweating and dilated skin vessels release heat to cool the body. Pro tip: hot -> lose heat; cold -> keep heat.",
        },
        {
            "text": r"Sweating helps cool the body because:",
            "difficulty": 2,
            "choices": [("Evaporation of sweat removes heat from the skin", True),
                        ("Sweat adds heat to the skin", False),
                        ("Sweat is colder than ice", False),
                        ("Sweat blocks the Sun", False)],
            "explanation": r"As sweat evaporates, it carries heat away from the skin, lowering body temperature.",
        },
        # --- Lesson 3: responding to the environment ---
        {
            "text": r"Do plants maintain homeostasis?",
            "difficulty": 1,
            "choices": [("Yes — for example, they close stomata to conserve water", True),
                        ("No — only animals do", False),
                        ("No — plants never respond to anything", False),
                        ("Only when they are flowering", False)],
            "explanation": r"All living things regulate their internal conditions. Plants, for instance, close their stomata to reduce water loss.",
        },
        {
            "text": ("Use the stomata diagram.\n\n"
                     "[[figure:stomata|Open and closed stomata on a leaf]]\n\n"
                     "A plant closes its stomata during a drought mainly to:"),
            "difficulty": 2,
            "choices": [("Reduce water loss", True), ("Take in more sunlight", False),
                        ("Release more oxygen", False), ("Grow taller faster", False)],
            "explanation": r"Closing the stomata limits the escape of water vapor, helping the plant conserve water. Pro tip: stomata close to save water.",
        },
        {
            "text": r"At high altitude, where there is less oxygen, the human body responds by:",
            "difficulty": 2,
            "choices": [("Breathing faster (and making more red blood cells over time)", True),
                        ("Stopping all breathing", False),
                        ("Making oxygen by photosynthesis", False),
                        ("Lowering its heart rate to zero", False)],
            "explanation": r"With less oxygen available, breathing rate increases, and over time the body produces more red blood cells to carry oxygen.",
        },
        {
            "text": r"Which is a BEHAVIORAL response to being too hot?",
            "difficulty": 2,
            "choices": [("Moving into the shade", True), ("Sweating", False),
                        ("Widening skin blood vessels", False), ("Shivering", False)],
            "explanation": r"Seeking shade is a behavior (an action the organism chooses). Sweating and changing blood vessel width are physical/automatic responses.",
        },
        # --- Lesson 4: reading graphs & tables ---
        {
            "text": r"When you first look at a graph, what should you check FIRST?",
            "difficulty": 1,
            "choices": [("The title, axis labels, and units", True),
                        ("The color of the page", False),
                        ("How long the graph took to draw", False),
                        ("Nothing — just guess the answer", False)],
            "explanation": r"Reading the title, axes, and units tells you what is being measured before you interpret the trend.",
        },
        {
            "text": ("Use the blood-glucose graph.\n\n"
                     "[[figure:blood_glucose_graph|Blood glucose after a meal]]\n\n"
                     "The graph shows blood glucose rising after a meal and then returning to normal. This pattern is evidence of:"),
            "difficulty": 2,
            "choices": [("Homeostasis", True), ("Photosynthesis", False),
                        ("Natural selection", False), ("A broken instrument", False)],
            "explanation": r"Returning toward the normal range after a change is exactly what homeostasis does. Pro tip: a value that rises then returns to normal shows regulation.",
        },
        {
            "text": r"On a graph, a line that stays flat (horizontal) means the measured value is:",
            "difficulty": 2,
            "choices": [("Staying about the same (stable)", True),
                        ("Rising quickly", False),
                        ("Falling to zero", False),
                        ("Doubling each second", False)],
            "explanation": r"A flat line indicates the value is steady over that period.",
        },
        {
            "text": r"Why do the UNITS on a graph matter so much?",
            "difficulty": 2,
            "choices": [("A change from 37 to 75 degrees is extreme, but 37.0 to 37.5 is small", True),
                        ("Units never change the meaning of the data", False),
                        ("Larger numbers are always more important", False),
                        ("Units only matter in math, not science", False)],
            "explanation": r"The size and units of a change determine whether it is biologically minor or extreme, so you must read them carefully.",
        },
        # --- Lesson 5: claims, evidence, experiments ---
        {
            "text": r"In an experiment, the INDEPENDENT variable is:",
            "difficulty": 1,
            "choices": [("The one thing the experimenter changes", True),
                        ("The result that is measured", False),
                        ("A variable kept the same", False),
                        ("The title of the graph", False)],
            "explanation": r"The independent variable is deliberately changed to test its effect on the dependent variable.",
        },
        {
            "text": r"The DEPENDENT variable is:",
            "difficulty": 1,
            "choices": [("The result that is measured", True),
                        ("The factor kept the same", False),
                        ("The hypothesis", False),
                        ("The number of trials only", False)],
            "explanation": r"The dependent variable is the outcome you measure; it 'depends on' the independent variable.",
        },
        {
            "text": r"Why are controlled variables important in an experiment?",
            "difficulty": 2,
            "choices": [("They keep other factors the same, making the test fair", True),
                        ("They guarantee the hypothesis is correct", False),
                        ("They replace the need for data", False),
                        ("They stop all measurement", False)],
            "explanation": r"Holding other factors constant lets you be sure the independent variable, not something else, caused any change.",
        },
        {
            "text": ("Use the experiment diagram.\n\n"
                     "[[figure:experiment_variables|Parts of a fair experiment]]\n\n"
                     "If you test how the AMOUNT OF FERTILIZER affects plant height, the independent variable is:"),
            "difficulty": 2,
            "choices": [("The amount of fertilizer", True), ("The plant's height", False),
                        ("The type of pot", False), ("The amount of water", False)],
            "explanation": r"The amount of fertilizer is what you change (independent). Plant height is what you measure (dependent). Pro tip: independent = changed; dependent = measured.",
        },
        {
            "text": r"Which would make an experiment's results MORE reliable?",
            "difficulty": 2,
            "choices": [("Repeating the trials and getting consistent results", True),
                        ("Changing every variable at once", False),
                        ("Using no measurements", False),
                        ("Choosing the answer before collecting data", False)],
            "explanation": r"Repeated trials with consistent results (and larger samples) increase confidence that the result is real, not chance.",
        },
        # --- Lesson 6: correlation vs causation ---
        {
            "text": r"Correlation means that two variables:",
            "difficulty": 1,
            "choices": [("Change together", True), ("Are completely unrelated", False),
                        ("Can never be graphed", False), ("Are always opposite", False)],
            "explanation": r"Correlation is when two variables change together. It does not, by itself, prove that one causes the other.",
        },
        {
            "text": r"Ice cream sales and sunburns both rise in summer. What is the best conclusion?",
            "difficulty": 2,
            "choices": [("A third factor, hot sunny weather, likely affects both", True),
                        ("Eating ice cream causes sunburn", False),
                        ("Sunburns make people buy ice cream", False),
                        ("The data must be wrong", False)],
            "explanation": r"This is correlation, not causation. A third factor (hot, sunny weather) drives both, so neither causes the other.",
        },
        {
            "text": ("Use the diagram.\n\n"
                     "[[figure:correlation_causation|Two correlated variables and a hidden cause]]\n\n"
                     "The diagram, with a hidden factor causing two correlated variables, best illustrates that:"),
            "difficulty": 3,
            "choices": [("Correlation is not causation", True),
                        ("Ice cream causes sunburns", False),
                        ("Two variables can never be related", False),
                        ("Graphs are always misleading", False)],
            "explanation": r"The diagram shows a third factor (hot weather) causing both variables, demonstrating that correlation does not prove causation. Pro tip: look for a hidden cause.",
        },
        {
            "text": r"To show that one thing actually CAUSES another, you usually need:",
            "difficulty": 2,
            "choices": [("A controlled experiment", True),
                        ("Only a single graph", False),
                        ("A larger correlation", False),
                        ("To assume it is true", False)],
            "explanation": r"A controlled experiment changes one variable while holding others constant, which is what supports a cause-and-effect claim.",
        },
        {
            "text": r"A graph shows two variables rising together. The SAFEST conclusion is that they:",
            "difficulty": 3,
            "choices": [("Are correlated, and more testing is needed to claim causation", True),
                        ("Definitely cause each other", False),
                        ("Have nothing to do with each other", False),
                        ("Prove the hypothesis is true", False)],
            "explanation": r"Rising together is a correlation. Without a controlled experiment, you cannot conclude one causes the other.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain how the body keeps its temperature stable using negative feedback. Describe the parts of a "
                "feedback loop (sensor, control center, effector), and explain what the body does when it gets too "
                "hot and when it gets too cold. End by explaining what 'negative feedback' means."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) naming the feedback parts -- a sensor detects the change, a control center "
                "compares it to the set point, and an effector responds; (2) too hot -> sweating and widening skin "
                "blood vessels to release heat; (3) too cold -> shivering and narrowing skin blood vessels to keep "
                "heat; (4) negative feedback means the response reverses the change, returning the body toward normal. "
                "Deduct for saying homeostasis means nothing changes, or reversing the hot/cold responses."
            ),
        },
        {
            "text": (
                "A student notices that on days when more cold drinks are sold, more people also go swimming, and "
                "concludes that buying cold drinks causes people to swim. Explain why this reasoning is flawed using "
                "the idea of correlation versus causation, and describe how a controlled experiment (independent, "
                "dependent, and controlled variables) could properly test a cause-and-effect claim."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the two variables are correlated (they rise together) but that does not prove "
                "causation; (2) a third factor (hot weather) likely causes both; (3) defining a controlled experiment "
                "-- change one independent variable, measure the dependent variable, keep other (controlled) variables "
                "the same; (4) noting repeated trials improve reliability. Deduct for accepting the student's "
                "conclusion or confusing the variable types."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Homeostasis & Life Science Data (Deep Dive)' course."

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

        # Phase 1 is MCQ-only: the written-response prompts above are not seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
