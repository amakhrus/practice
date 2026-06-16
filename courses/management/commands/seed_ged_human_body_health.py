"""
Seed data: 'GED Science: Human Body Systems & Health (Deep Dive)'.

A focused EXPANSION of Lesson 6 ("The Human Body Systems") from the broader
'GED Science: Life Science' course, brought up to the full deep-dive standard
(6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. From cells to body systems (levels of organization).
  2. The major organ systems and their jobs.
  3. Oxygen, nutrients & energy (systems working together).
  4. Control & movement (nervous, endocrine, skeletal, muscular).
  5. Nutrition: calories, vitamins & minerals.
  6. Disease, pathogens, immunity & reading health data.

This course uses ALL-NEW diagrams (body organization, an organ-systems overview,
oxygen/nutrient delivery, a reflex arc, a nutrition chart, and disease
transmission/prevention).

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Anatomy & Physiology* and *Biology*.
  - National Institutes of Health (NIH) / MedlinePlus; CDC (disease prevention).
  - USDA nutrition (MyPlate) basics.
Note: levels of organization are cells -> tissues -> organs -> organ systems ->
organism. The respiratory system handles oxygen/carbon dioxide; the kidneys
(excretory system) filter other wastes. Antibiotics treat bacteria, not viruses.

Run:
    python manage.py seed_ged_human_body_health
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Human Body Systems & Health (Deep Dive)",
    "slug": "ged-human-body-health",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into how the human body is built and kept alive, expanding the single 'Human Body "
        "Systems' lesson from the GED Life Science course into a full mini-course. You'll see how cells "
        "build up into organ systems, meet the major systems and their jobs, follow oxygen and nutrients "
        "to your cells, learn how the body senses and moves, understand nutrition, and explore how "
        "disease spreads and how the body and public health defend against it. Plain language, all-new "
        "labeled diagrams, common-misconception warnings, and GED-style practice with full explanations."
    ),
    "lessons": [
        (
            "1. From Cells to Body Systems",
            r"Your body is built in **levels**, each made of the level before it. Understanding this ladder makes the rest of the body make sense." "\n\n"
            r"[[figure:body_organization|Similar cells form tissues, tissues form organs, organs form organ systems, and systems make up the whole organism.]]" "\n\n"
            r"From smallest to largest:" "\n"
            r"- **Cells** — the smallest living units (a muscle cell)." "\n"
            r"- **Tissues** — groups of **similar cells** working together (muscle tissue). The body has four main tissue types: epithelial, connective, muscle, and nervous." "\n"
            r"- **Organs** — different tissues forming a structure with a job (the **heart**)." "\n"
            r"- **Organ systems** — organs that team up for a larger job (the **circulatory system**)." "\n"
            r"- **Organism** — all the systems working together (**you**)." "\n\n"
            r"Because every level builds on the last, the body's systems are deeply **connected**. A problem in one organ or system often affects others — a weak heart, for example, means cells everywhere get less oxygen." "\n\n"
            r"⚠️ Common misconception: organs do **not** work in isolation. The systems constantly cooperate, so trouble in one place can have effects far away." "\n\n"
            r"💡 Tip: memorize the ladder — **cells → tissues → organs → organ systems → organism.**",
        ),
        (
            "2. The Major Organ Systems",
            r"The body is a **team of organ systems**, each handling a job. The GED test focuses on what each system does and how to match a system to its function." "\n\n"
            r"[[figure:organ_systems|Each major system has a specific job, and together they keep the body alive.]]" "\n\n"
            r"- **Circulatory** — the **heart** pumps **blood** to carry oxygen, nutrients, and wastes." "\n"
            r"- **Respiratory** — the **lungs** take in **oxygen** and release **carbon dioxide** (gas exchange)." "\n"
            r"- **Digestive** — breaks **food** into nutrients the body can absorb." "\n"
            r"- **Nervous** — the **brain** and nerves sense the environment and send **fast** signals." "\n"
            r"- **Skeletal & Muscular** — provide support, protection, and **movement**." "\n"
            r"- **Immune** — defends against **germs**." "\n"
            r"- Other systems include the **endocrine** (hormones), the **excretory/urinary** (the **kidneys** filter wastes), and the **integumentary** (skin)." "\n\n"
            r"⚠️ Common misconception: the **lungs** do not filter all of the blood's wastes — they handle **carbon dioxide**. The **kidneys** filter most other wastes from the blood." "\n\n"
            r"💡 Tip: match the system to its job — when a question links two systems, look for **what they exchange** (usually oxygen, nutrients, or a signal).",
        ),
        (
            "3. Oxygen, Nutrients & Energy",
            r"Why do you need to **eat** and **breathe**? Because your cells need raw materials to make energy, and three systems work together to deliver them." "\n\n"
            r"[[figure:oxygen_delivery|The lungs supply oxygen, the digestive system supplies glucose, the blood delivers both, and cells make ATP.]]" "\n\n"
            r"- The **respiratory** system brings **oxygen** into the lungs and removes carbon dioxide." "\n"
            r"- The **digestive** system breaks food into nutrients, including **glucose**." "\n"
            r"- The **circulatory** system carries **oxygen and glucose** in the blood to every cell." "\n\n"
            r"Inside the cell, the **mitochondria** combine oxygen and glucose in **cellular respiration** to make **ATP**, the energy that powers everything the cell does. The waste **carbon dioxide** travels back through the blood to the lungs and is exhaled." "\n\n"
            r"This is a favorite GED reasoning chain: **food supplies glucose, breathing supplies oxygen, blood transports both, and cells release energy.** If any part fails, cells get less energy." "\n\n"
            r"⚠️ Common misconception: **breathing** itself does not make ATP. Breathing only **supplies oxygen**; the ATP is made inside cells during **cellular respiration**." "\n\n"
            r"💡 Tip: **digestive = nutrients, respiratory = oxygen, circulatory = delivery, mitochondria = energy.**",
        ),
        (
            "4. Control & Movement",
            r"Your body senses its surroundings and responds — quickly through the **nervous** system and more slowly through the **endocrine** system — while the **skeletal** and **muscular** systems carry out movement." "\n\n"
            r"[[figure:neuron_reflex|In a reflex, a sensory neuron signals the spinal cord, which sends a motor neuron signal to the muscle — no waiting for the brain.]]" "\n\n"
            r"- **Nervous system** — sends **fast electrical signals** through the brain, spinal cord, and nerves. A **reflex** (like jerking your hand off a hot stove) is so fast because the **spinal cord** triggers the response before the brain is even involved." "\n"
            r"- **Endocrine system** — sends **chemical messengers called hormones** through the blood. Hormones are slower but longer-lasting; **insulin**, for example, helps regulate blood sugar." "\n"
            r"- **Skeletal system** — bones **support and protect** the body. **Muscular system** — muscles create movement by **pulling** on bones, often working in **opposing pairs** (one pulls, the other pulls back)." "\n\n"
            r"⚠️ Common misconception: the brain does **not** move bones directly. The nervous system signals a **muscle**, the muscle **contracts**, and the muscle **pulls** the bone at a joint." "\n\n"
            r"💡 Tip: **nervous = fast signals; endocrine = hormone messages; skeletal + muscular = support and movement.**",
        ),
        (
            "5. Nutrition: Calories, Vitamins & Minerals",
            r"Food gives the body both **energy** and the **building materials** it needs. Nutrition is where biology meets daily health." "\n\n"
            r"[[figure:nutrition_chart|Carbohydrates and fats supply energy, proteins build and repair, and vitamins and minerals help body processes.]]" "\n\n"
            r"- **Calories** measure the **energy** in food." "\n"
            r"- **Carbohydrates** are often a **quick energy** source; **fats** store **concentrated energy**." "\n"
            r"- **Proteins** mainly **build and repair** tissues and form enzymes." "\n"
            r"- **Vitamins** and **minerals** usually provide no calories but help body processes work. **Calcium** supports **bones**; **iron** helps red blood cells **carry oxygen**." "\n"
            r"- **Water** is needed for transport and reactions." "\n\n"
            r"A **balanced diet** supplies both energy and materials. Too little energy can limit growth and repair; too little of a key vitamin or mineral can disrupt a specific body process. GED questions usually give a nutrition table — use the **data provided**." "\n\n"
            r"⚠️ Common misconception: calories are not 'bad.' A **calorie is a unit of energy**. Health depends on the **amount and balance** of what you eat, and on getting the nutrients your body needs." "\n\n"
            r"💡 Tip: **carbs & fats = energy; protein = build & repair; vitamins & minerals = help processes.**",
        ),
        (
            "6. Disease, Pathogens, Immunity & Health Data",
            r"A **pathogen** is an organism or agent that can cause disease — certain **bacteria, viruses, fungi, or parasites**. Diseases spread in different ways, and matching the **prevention** to the **route** is key." "\n\n"
            r"[[figure:disease_transmission|Diseases spread through the air, water/food, contact, or insect vectors; each route has matching prevention.]]" "\n\n"
            r"Common transmission routes:" "\n"
            r"- **Airborne** (coughs, sneezes) — prevent with covering coughs and good ventilation." "\n"
            r"- **Water/food-borne** (contaminated water or food) — prevent with clean water and **sanitation**." "\n"
            r"- **Contact / bloodborne** (touch, body fluids) — prevent with **handwashing** and avoiding contact with fluids." "\n"
            r"- **Vector-borne** (insects like mosquitoes) — prevent with **nets and insect control**." "\n\n"
            r"The body's own defense is the **immune system**, which recognizes and attacks pathogens. **Vaccination** trains the immune system to recognize a pathogen **before** a serious infection. Note that **antibiotics** treat **bacterial** infections — they do **not** work on viruses." "\n\n"
            r"**Reading health data (a GED skill).** Items may show cases over time or a nutrition table. Read the **title, axes, and units**, find the **trend**, match prevention to the transmission route, and remember **correlation is not causation**." "\n\n"
            r"⚠️ Common misconception: **antibiotics do not treat viral infections** (like the common cold or flu). Antibiotics target bacteria; viruses need different prevention and treatment." "\n\n"
            r"💡 Tip: **match prevention to transmission** — airborne, waterborne, contact, or vector-borne." "\n\n"
            r"📚 Sources: OpenStax *Anatomy & Physiology* / *Biology*; NIH / MedlinePlus; CDC; USDA nutrition.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: levels of organization ---
        {
            "text": r"Which lists the levels of body organization in the correct order, from smallest to largest?",
            "difficulty": 1,
            "choices": [("Cells, tissues, organs, organ systems", True),
                        ("Organs, cells, systems, tissues", False),
                        ("Tissues, organs, cells, systems", False),
                        ("Systems, organs, tissues, cells", False)],
            "explanation": r"Cells form tissues, tissues form organs, and organs work together in organ systems (which make up the organism).",
        },
        {
            "text": r"A group of similar cells working together to do a job is called a(n):",
            "difficulty": 2,
            "choices": [("Tissue", True), ("Organ", False),
                        ("Organ system", False), ("Organism", False)],
            "explanation": r"A tissue is a group of similar cells. Different tissues combine to form an organ.",
        },
        {
            "text": r"The heart is an example of a(n):",
            "difficulty": 1,
            "choices": [("Organ", True), ("Cell", False),
                        ("Tissue", False), ("Organ system", False)],
            "explanation": r"The heart is an organ made of several tissues; it is part of the circulatory (organ) system.",
        },
        {
            "text": ("Use the diagram.\n\n"
                     "[[figure:body_organization|Levels of body organization]]\n\n"
                     "According to the diagram, the level BETWEEN an organ and the whole organism is the:"),
            "difficulty": 2,
            "choices": [("Organ system", True), ("Cell", False),
                        ("Tissue", False), ("Atom", False)],
            "explanation": r"The order is cell, tissue, organ, organ system, organism, so the organ system sits between organ and organism. Pro tip: organs team up into systems.",
        },
        {
            "text": r"Why does a problem in one organ system often affect other systems?",
            "difficulty": 2,
            "choices": [("The systems are connected and work together", True),
                        ("Each system is completely independent", False),
                        ("Organs can move between systems", False),
                        ("The body has only one system", False)],
            "explanation": r"The body's systems cooperate constantly, so trouble in one (like the heart) can reduce oxygen or nutrients reaching others.",
        },
        # --- Lesson 2: organ systems ---
        {
            "text": r"Which body system transports oxygen, nutrients, and wastes in the blood?",
            "difficulty": 1,
            "choices": [("Circulatory system", True), ("Skeletal system", False),
                        ("Nervous system", False), ("Integumentary system", False)],
            "explanation": r"The circulatory system, centered on the heart, moves blood that carries oxygen, nutrients, wastes, and hormones.",
        },
        {
            "text": r"Which system takes in oxygen and releases carbon dioxide?",
            "difficulty": 1,
            "choices": [("Respiratory system", True), ("Digestive system", False),
                        ("Muscular system", False), ("Endocrine system", False)],
            "explanation": r"The respiratory system (the lungs) performs gas exchange: oxygen in, carbon dioxide out.",
        },
        {
            "text": r"Which system breaks food down into nutrients the body can absorb?",
            "difficulty": 2,
            "choices": [("Digestive system", True), ("Circulatory system", False),
                        ("Nervous system", False), ("Skeletal system", False)],
            "explanation": r"The digestive system breaks food into small molecules (like glucose) that can be absorbed and used by cells.",
        },
        {
            "text": r"Which system mainly provides support and protects the body's organs?",
            "difficulty": 2,
            "choices": [("Skeletal system", True), ("Respiratory system", False),
                        ("Immune system", False), ("Digestive system", False)],
            "explanation": r"The skeletal system (bones) supports the body and protects organs such as the brain and heart.",
        },
        {
            "text": ("Use the organ-systems diagram.\n\n"
                     "[[figure:organ_systems|Major organ systems and their jobs]]\n\n"
                     "Which system is mainly responsible for FAST signals and control?"),
            "difficulty": 2,
            "choices": [("Nervous system", True), ("Circulatory system", False),
                        ("Skeletal system", False), ("Digestive system", False)],
            "explanation": r"The nervous system sends rapid electrical signals to sense the environment and control responses. Pro tip: nervous = fast; endocrine = slower hormones.",
        },
        {
            "text": r"The kidneys (the excretory/urinary system) mainly:",
            "difficulty": 2,
            "choices": [("Filter wastes from the blood", True),
                        ("Pump blood to the body", False),
                        ("Take in oxygen", False),
                        ("Digest food", False)],
            "explanation": r"The kidneys filter wastes from the blood and make urine. The lungs, by contrast, handle carbon dioxide.",
        },
        # --- Lesson 3: oxygen, nutrients, energy ---
        {
            "text": r"The respiratory and circulatory systems work together most directly to:",
            "difficulty": 1,
            "choices": [("Bring in oxygen and deliver it to the body's cells", True),
                        ("Digest food into nutrients", False),
                        ("Send fast nerve signals", False),
                        ("Support and move the body", False)],
            "explanation": r"The respiratory system brings oxygen into the lungs, and the circulatory system carries it in the blood to all cells.",
        },
        {
            "text": r"Body cells use oxygen and glucose to make energy (ATP) in the:",
            "difficulty": 2,
            "choices": [("Mitochondria (cellular respiration)", True),
                        ("Lungs", False),
                        ("Stomach", False),
                        ("Nerves", False)],
            "explanation": r"Cellular respiration in the mitochondria combines oxygen and glucose to release energy as ATP.",
        },
        {
            "text": ("Use the delivery diagram.\n\n"
                     "[[figure:oxygen_delivery|How oxygen and glucose reach a cell]]\n\n"
                     "According to the diagram, oxygen travels from the lungs to the cells through the:"),
            "difficulty": 2,
            "choices": [("Blood (circulatory system)", True),
                        ("Nerves", False),
                        ("Bones", False),
                        ("Skin only", False)],
            "explanation": r"The diagram shows oxygen passing from the lungs into the blood, which carries it to the cells. Pro tip: lungs take it in, blood delivers it.",
        },
        {
            "text": r"Where do body cells get the glucose they use to make energy?",
            "difficulty": 2,
            "choices": [("From food broken down by the digestive system", True),
                        ("From the air in the lungs", False),
                        ("From the bones", False),
                        ("They make it from nothing", False)],
            "explanation": r"The digestive system breaks food into glucose and other nutrients, which the blood then delivers to cells.",
        },
        {
            "text": r"Breathing supplies oxygen, but breathing itself does not make ATP. Why?",
            "difficulty": 3,
            "choices": [("ATP is made inside cells during cellular respiration, not in the lungs", True),
                        ("Breathing destroys ATP", False),
                        ("The lungs make all the body's ATP", False),
                        ("ATP is made only in bones", False)],
            "explanation": r"Breathing moves air and delivers oxygen, but the actual energy (ATP) is produced inside cells (in the mitochondria) when oxygen and glucose react.",
        },
        # --- Lesson 4: control & movement ---
        {
            "text": r"The nervous system sends signals that are:",
            "difficulty": 1,
            "choices": [("Fast and electrical, through nerves and the brain", True),
                        ("Slow chemical hormones only", False),
                        ("Carried by red blood cells", False),
                        ("Made of bone", False)],
            "explanation": r"The nervous system uses fast electrical signals to sense and respond quickly.",
        },
        {
            "text": r"Hormones such as insulin are chemical messengers of the:",
            "difficulty": 2,
            "choices": [("Endocrine system", True), ("Skeletal system", False),
                        ("Respiratory system", False), ("Digestive system", False)],
            "explanation": r"The endocrine system releases hormones into the blood. They act more slowly than nerve signals but last longer.",
        },
        {
            "text": r"Pulling your hand off a hot stove before you even think about it is an example of a:",
            "difficulty": 2,
            "choices": [("Reflex (a fast, automatic nervous response)", True),
                        ("Hormone response", False),
                        ("Digestive process", False),
                        ("Bone growth", False)],
            "explanation": r"A reflex is an automatic response handled by the spinal cord, which is why it happens so quickly.",
        },
        {
            "text": ("Use the reflex-arc diagram.\n\n"
                     "[[figure:neuron_reflex|The path of a reflex]]\n\n"
                     "In the reflex arc, the signal travels: sensory neuron, then spinal cord, then ______, then muscle."),
            "difficulty": 2,
            "choices": [("Motor neuron", True), ("Bone", False),
                        ("Red blood cell", False), ("Hormone", False)],
            "explanation": r"After the spinal cord receives the signal, a motor neuron carries the command out to the muscle. Pro tip: sensory in, motor out.",
        },
        {
            "text": r"Muscles create movement by:",
            "difficulty": 2,
            "choices": [("Pulling on bones, often in opposing pairs", True),
                        ("Pushing bones apart", False),
                        ("Sending hormones to bones", False),
                        ("Dissolving the bones", False)],
            "explanation": r"Muscles can only pull (contract), not push, so they work in opposing pairs to move bones back and forth at joints.",
        },
        {
            "text": r"How does the brain make a bone move?",
            "difficulty": 3,
            "choices": [("It sends a signal through nerves to a muscle, which contracts and pulls the bone", True),
                        ("It pulls the bone directly", False),
                        ("It sends blood to push the bone", False),
                        ("It grows new bone instantly", False)],
            "explanation": r"The brain signals a muscle through the nervous system; the muscle then contracts and pulls the bone at a joint.",
        },
        # --- Lesson 5: nutrition ---
        {
            "text": r"Calories are a measure of:",
            "difficulty": 1,
            "choices": [("The energy in food", True), ("The number of vitamins in food", False),
                        ("How many germs are in food", False), ("The weight of food only", False)],
            "explanation": r"A calorie is a unit of energy. Carbohydrates, fats, and proteins can all provide calories.",
        },
        {
            "text": r"Which nutrient group is used mainly to BUILD and REPAIR body tissues?",
            "difficulty": 2,
            "choices": [("Proteins", True), ("Carbohydrates", False),
                        ("Vitamins", False), ("Water", False)],
            "explanation": r"Proteins build and repair tissues and form enzymes. Carbohydrates and fats are mainly energy sources.",
        },
        {
            "text": r"Iron is an important mineral because it helps red blood cells:",
            "difficulty": 2,
            "choices": [("Carry oxygen", True), ("Build bones", False),
                        ("Digest food", False), ("Send nerve signals", False)],
            "explanation": r"Iron is part of hemoglobin, the molecule in red blood cells that carries oxygen.",
        },
        {
            "text": r"Calcium is a mineral that mainly supports:",
            "difficulty": 2,
            "choices": [("Bones (and teeth)", True), ("Vision in dim light", False),
                        ("Oxygen transport", False), ("Hair color", False)],
            "explanation": r"Calcium is important for strong bones and teeth, and it also helps muscles and nerves work.",
        },
        {
            "text": ("Use the nutrition chart.\n\n"
                     "[[figure:nutrition_chart|Nutrient groups and their jobs]]\n\n"
                     "According to the chart, carbohydrates mainly provide:"),
            "difficulty": 1,
            "choices": [("Energy", True), ("New bones", False),
                        ("Antibodies", False), ("Oxygen", False)],
            "explanation": r"The chart lists carbohydrates as a quick energy source. Pro tip: carbs and fats are for energy; proteins build and repair.",
        },
        # --- Lesson 6: disease, immunity, data ---
        {
            "text": r"A pathogen is:",
            "difficulty": 1,
            "choices": [("An agent (such as a bacterium or virus) that can cause disease", True),
                        ("A type of vitamin", False),
                        ("A unit of energy", False),
                        ("A kind of muscle", False)],
            "explanation": r"Pathogens are disease-causing agents, including certain bacteria, viruses, fungi, and parasites.",
        },
        {
            "text": r"Vaccination helps prevent disease by:",
            "difficulty": 2,
            "choices": [("Training the immune system to recognize a pathogen in advance", True),
                        ("Adding calories to the body", False),
                        ("Replacing the need for clean water", False),
                        ("Killing every bacterium in the body", False)],
            "explanation": r"A vaccine prepares the immune system to recognize and fight a specific pathogen before a serious infection occurs.",
        },
        {
            "text": r"Which prevention method best reduces a disease spread through CONTAMINATED WATER?",
            "difficulty": 2,
            "choices": [("Water treatment and sanitation", True),
                        ("Wearing a wristband", False),
                        ("Getting more sunlight", False),
                        ("Eating more protein", False)],
            "explanation": r"Clean water and good sanitation stop waterborne pathogens from reaching people. Match the prevention to the route of spread.",
        },
        {
            "text": r"Antibiotics are effective against:",
            "difficulty": 2,
            "choices": [("Bacteria, but not viruses", True),
                        ("Viruses, but not bacteria", False),
                        ("All pathogens equally", False),
                        ("Vitamins and minerals", False)],
            "explanation": r"Antibiotics target bacteria. Viral infections (like colds and flu) are not treated by antibiotics and need different approaches.",
        },
        {
            "text": ("Use the disease-spread diagram.\n\n"
                     "[[figure:disease_transmission|Routes of disease spread and prevention]]\n\n"
                     "A disease spreads mainly through mosquito bites. The best matching prevention is:"),
            "difficulty": 3,
            "choices": [("Insect control and nets (controlling the vector)", True),
                        ("Treating drinking water", False),
                        ("Covering coughs", False),
                        ("Taking more vitamins", False)],
            "explanation": r"A mosquito is a vector, so the prevention should target the insects (nets, insect control). Pro tip: match each prevention to how the disease actually spreads.",
        },
    ],
    "essays": [
        {
            "text": (
                "Trace how oxygen and glucose reach a body cell and how the cell uses them to make energy. In your "
                "answer, name the organ systems involved (respiratory, digestive, and circulatory), explain what each "
                "one contributes, and connect the process to cellular respiration in the mitochondria."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the respiratory system brings oxygen into the lungs; (2) the digestive system "
                "breaks food into glucose; (3) the circulatory system carries oxygen and glucose in the blood to the "
                "cells; (4) inside the cell, mitochondria use oxygen and glucose in cellular respiration to make ATP, "
                "releasing carbon dioxide that the blood carries back to the lungs to be exhaled. Deduct for saying "
                "breathing itself makes ATP, or for omitting a system."
            ),
        },
        {
            "text": (
                "Explain how diseases spread and how the body and public-health measures defend against them. "
                "Describe at least two ways a disease can be transmitted with a matching prevention method, explain "
                "the role of the immune system and vaccination, and explain why antibiotics do not cure viral "
                "infections."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) at least two transmission routes with matched prevention (e.g., waterborne -> "
                "clean water/sanitation; airborne -> cover coughs/ventilation; vector-borne -> insect control); "
                "(2) the immune system recognizes and attacks pathogens; (3) vaccination trains the immune system in "
                "advance; (4) antibiotics treat bacteria, not viruses, so they don't cure viral infections. Deduct "
                "for mismatching a prevention to a route or claiming antibiotics cure viruses."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Human Body Systems & Health (Deep Dive)' course."

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
