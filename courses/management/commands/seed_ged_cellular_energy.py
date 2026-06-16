"""
Seed data: 'GED Science: Cellular Energy (Deep Dive)'.

A focused EXPANSION of Lesson 2 ("Cellular Energy: Photosynthesis & Respiration")
from the broader 'GED Science: Life Science' course, brought up to the full
deep-dive standard (6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. Energy & ATP -- the cell's energy currency and metabolism.
  2. Photosynthesis -- capturing light and storing it in sugar.
  3. Cellular respiration -- releasing usable energy (ATP) from sugar.
  4. How the two processes are linked (the carbon & oxygen cycle).
  5. Fermentation -- making energy without oxygen.
  6. Reading cellular-energy data.

This course uses ALL-NEW diagrams (the ATP-ADP cycle, photosynthesis and
respiration overviews, a photosynthesis/respiration link, fermentation pathways,
and a photosynthesis-rate graph) rather than reusing the parent course's
'energy_cycle' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Biology* and *Concepts of Biology* (photosynthesis, respiration,
    fermentation, ATP).
  - Campbell & Reece, *Biology* (standard reference).
  - National Human Genome Research Institute / NIH; USDA nutrition basics.
Note (rounded for learners): aerobic respiration yields roughly 36 ATP per glucose;
fermentation (via glycolysis) yields a net of about 2 ATP. Photosynthesis:
6 CO2 + 6 H2O + light -> C6H12O6 + 6 O2. Respiration is nearly its reverse.

Run:
    python manage.py seed_ged_cellular_energy
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Cellular Energy (Deep Dive)",
    "slug": "ged-cellular-energy",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into how living things get, store, and use energy, expanding the single 'Cellular "
        "Energy' lesson from the GED Life Science course into a full mini-course. You'll meet ATP (the "
        "cell's energy currency), follow photosynthesis as it captures sunlight into sugar and cellular "
        "respiration as it releases that energy, see how the two processes form a cycle, learn how cells "
        "make energy without oxygen (fermentation), and practice reading energy data. Plain language, "
        "all-new labeled diagrams, common-misconception warnings, and GED-style practice with full "
        "explanations throughout."
    ),
    "lessons": [
        (
            "1. Energy for Life: ATP & Metabolism",
            r"Every living thing needs **energy** — to grow, move materials, build molecules, repair damage, and stay warm. But cells can't plug into a wall outlet. Instead they use a tiny energy-carrying molecule called **ATP** (adenosine triphosphate)." "\n\n"
            r"[[figure:atp_adp_cycle|ATP works like a rechargeable battery: cells store energy by making ATP and release it by breaking ATP back into ADP.]]" "\n\n"
            r"Think of ATP as the cell's **rechargeable battery**. ATP carries three phosphate groups. When the cell needs energy, it breaks off one phosphate, turning **ATP into ADP** and **releasing energy** for work. Later, energy from food is used to reattach the phosphate, **recharging ADP back into ATP**. This cycle runs constantly." "\n\n"
            r"All of a cell's chemical reactions together make up its **metabolism**. Some reactions **build** larger molecules and store energy (for example, linking amino acids into proteins); others **break down** molecules and release energy (like splitting glucose). Food provides the raw stored energy; ATP is the usable form the cell actually spends. And almost all of that energy traces back to the **Sun**." "\n\n"
            r"⚠️ Common misconception: the energy in food doesn't simply 'disappear' when you use it. Cells **transform** it — into ATP, motion, body heat, and stored molecules. Energy is converted, not destroyed." "\n\n"
            r"💡 Tip: **ATP = the cell's usable energy 'cash'; food = the larger stored 'savings.'**",
        ),
        (
            "2. Photosynthesis: Storing Sunlight in Sugar",
            r"**Photosynthesis** is how plants, algae, and some bacteria **capture light energy** and store it as chemical energy in sugar. In plants it happens mainly in the **chloroplasts**, green organelles packed with the light-absorbing pigment **chlorophyll**." "\n\n"
            r"[[figure:photosynthesis_overview|Photosynthesis takes in carbon dioxide, water, and light and produces glucose and oxygen.]]" "\n\n"
            r"The overall reaction is:" "\n"
            r"\[ 6\,CO_2 + 6\,H_2O + \text{light} \;\rightarrow\; C_6H_{12}O_6 + 6\,O_2. \]" "\n"
            r"In words: **carbon dioxide + water + light → glucose (sugar) + oxygen**. The glucose stores the captured energy; the **oxygen** is released into the air — the same oxygen most living things breathe." "\n\n"
            r"Photosynthesis links life to the atmosphere: plants take in **carbon dioxide** and give off **oxygen**. It's also the base of most food chains, because it turns sunlight into the chemical energy that feeds nearly every other organism." "\n\n"
            r"⚠️ Common misconception: a plant does **not** get most of its added mass from the soil. Much of a plant's new material comes from the **carbon dioxide in the air**, rearranged into sugars (the carbon comes from CO₂)." "\n\n"
            r"💡 Tip: photosynthesis = **light in, sugar (and oxygen) out.** It *stores* energy.",
        ),
        (
            "3. Cellular Respiration: Releasing the Energy",
            r"Storing energy in sugar is only half the story. To actually **use** that energy, cells run **cellular respiration**, which breaks glucose back down and captures the released energy as **ATP**. In eukaryotic cells, most of this happens in the **mitochondria**." "\n\n"
            r"[[figure:respiration_overview|Cellular respiration takes in glucose and oxygen and produces carbon dioxide, water, and ATP.]]" "\n\n"
            r"The overall reaction is almost the **reverse** of photosynthesis:" "\n"
            r"\[ C_6H_{12}O_6 + 6\,O_2 \;\rightarrow\; 6\,CO_2 + 6\,H_2O + \text{ATP}. \]" "\n"
            r"In words: **glucose + oxygen → carbon dioxide + water + ATP**. This is why animals need to eat *and* breathe: food supplies glucose, the lungs and blood supply oxygen, and the mitochondria combine them to release energy." "\n\n"
            r"Note an important difference: **breathing** is not the same as **cellular respiration**. Breathing moves air in and out of the lungs; cellular respiration is the **chemical process inside cells** that makes ATP. They're connected, but not identical." "\n\n"
            r"⚠️ Common misconception: only animals do cellular respiration. **Plants do it too** — every living cell needs ATP, so plant cells run respiration around the clock (not just photosynthesis)." "\n\n"
            r"💡 Tip: respiration = **sugar + oxygen in, ATP (and CO₂ + water) out.** It *releases* energy.",
        ),
        (
            "4. Two Processes, One Cycle",
            r"Photosynthesis and cellular respiration aren't separate facts to memorize — they're two halves of a single **energy and matter cycle**. Look closely and you'll see the outputs of one are the inputs of the other." "\n\n"
            r"[[figure:photo_resp_link|The products of photosynthesis (glucose and oxygen) are the reactants of respiration, and vice versa.]]" "\n\n"
            r"- **Photosynthesis** uses CO₂ and water (plus light) to make **glucose and oxygen**." "\n"
            r"- **Cellular respiration** uses **glucose and oxygen** to make CO₂ and water (plus ATP)." "\n\n"
            r"So the **glucose and oxygen** that respiration needs are exactly what photosynthesis produces, and the **carbon dioxide and water** that photosynthesis needs are exactly what respiration gives off. Carbon and oxygen keep cycling between living things and the air. Energy, meanwhile, flows **one way**: it enters as sunlight and eventually leaves as heat." "\n\n"
            r"⚠️ Common misconception: plants only photosynthesize. In reality plants do **both** — they photosynthesize when there's light, and they respire all the time to power their cells." "\n\n"
            r"💡 Tip: **photosynthesis stores energy in sugar; respiration releases it.** One builds up, the other breaks down — and they feed each other.",
        ),
        (
            "5. Fermentation: Energy Without Oxygen",
            r"Aerobic respiration needs **oxygen** and produces a lot of ATP. But what happens when oxygen runs low? Some cells can still make a small amount of ATP without it, through **fermentation**." "\n\n"
            r"[[figure:fermentation_paths|With oxygen, cells run aerobic respiration for lots of ATP; without oxygen, fermentation makes only a little.]]" "\n\n"
            r"Both paths start with **glycolysis**, which splits glucose and yields a little ATP. After that:" "\n"
            r"- **With oxygen** → the process continues into the mitochondria (aerobic respiration), releasing **a lot** of ATP (about 36 per glucose)." "\n"
            r"- **Without oxygen** → **fermentation** keeps glycolysis going but makes only a **little** ATP (about 2 per glucose)." "\n\n"
            r"There are two common types of fermentation:" "\n"
            r"- **Lactic acid fermentation** — in human muscle cells during hard exercise (when oxygen runs short), and in bacteria that make **yogurt** and cheese." "\n"
            r"- **Alcoholic fermentation** — in **yeast**, which produces alcohol and **carbon dioxide**. The CO₂ bubbles are what make bread dough rise." "\n\n"
            r"⚠️ Common misconception: fermentation is **not** the same as photosynthesis. Fermentation **breaks down** food without oxygen; photosynthesis **builds** sugar using light." "\n\n"
            r"💡 Tip: **no oxygen + little ATP = fermentation.** Yeast bubbles (CO₂) and tired-muscle burn (lactic acid) are the classic clues.",
        ),
        (
            "6. Reading Cellular-Energy Data",
            r"The GED test often presents cellular energy as a **graph or table**. The skill is reading it carefully, not just recalling facts." "\n\n"
            r"[[figure:photosynthesis_rate_graph|As light increases, the photosynthesis rate rises — then levels off when some other factor becomes the limit.]]" "\n\n"
            r"Start with the **title, axis labels, and units**, then identify the **input and output** being measured, and find the **trend**:" "\n"
            r"- For **photosynthesis** data, rising **oxygen output** usually means a higher photosynthesis rate." "\n"
            r"- For **respiration** data, rising **carbon dioxide output** usually means a higher respiration rate." "\n"
            r"- A curve that **rises then flattens** means a factor was increasing the rate until something else became the **limiting factor** (for example, light helps until CO₂ or temperature limits the process)." "\n\n"
            r"**Worked example.** A plant produces 2 units of O₂ in dim light, 8 units in medium light, and 12 units in bright light. The trend is clear: more light is associated with more oxygen, so a higher photosynthesis rate — *in this setup*." "\n\n"
            r"⚠️ Common misconception: two variables changing together does **not** prove cause and effect. To claim causation, look for a **controlled experiment** with one variable changed and the others held constant." "\n\n"
            r"💡 Tip: **oxygen output tracks photosynthesis; carbon dioxide output tracks respiration.** Read the axes, name the trend, and don't overclaim causation." "\n\n"
            r"📚 Sources: OpenStax *Biology* / *Concepts of Biology*; Campbell & Reece, *Biology*; NIH; USDA nutrition basics.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: ATP & metabolism ---
        {
            "text": r"What is ATP best described as?",
            "difficulty": 1,
            "choices": [("The cell's usable energy-carrying molecule", True),
                        ("A type of chromosome", False),
                        ("A disease-causing organism", False),
                        ("A structure found only in plants", False)],
            "explanation": r"ATP (adenosine triphosphate) stores and delivers energy in a form cells can spend on work — the cell's energy currency.",
        },
        {
            "text": r"When ATP releases energy for the cell to use, it usually:",
            "difficulty": 2,
            "choices": [("Loses a phosphate group, becoming ADP", True),
                        ("Gains a phosphate group, becoming ADP", False),
                        ("Turns into glucose", False),
                        ("Becomes oxygen gas", False)],
            "explanation": r"Breaking off one phosphate turns ATP into ADP and releases energy. Adding the phosphate back (using energy from food) recharges it.",
        },
        {
            "text": r"Recharging ADP back into ATP requires:",
            "difficulty": 2,
            "choices": [("Energy, ultimately from food", True),
                        ("No energy at all", False),
                        ("Removing all phosphates", False),
                        ("Sunlight striking the ATP directly", False)],
            "explanation": r"It takes energy to reattach a phosphate to ADP. That energy comes from breaking down food in cellular respiration.",
        },
        {
            "text": r"The sum of all the chemical reactions in an organism is called its:",
            "difficulty": 2,
            "choices": [("Metabolism", True), ("Genotype", False),
                        ("Ecosystem", False), ("Mitosis", False)],
            "explanation": r"Metabolism is all of an organism's chemical reactions — both those that build molecules and those that break them down.",
        },
        {
            "text": r"The original source of the energy used by almost all living things is:",
            "difficulty": 1,
            "choices": [("The Sun", True), ("Earth's core", False),
                        ("The Moon", False), ("Ocean tides", False)],
            "explanation": r"Sunlight is captured by photosynthesis and stored in sugar, which then powers most life through cellular respiration.",
        },
        # --- Lesson 2: photosynthesis ---
        {
            "text": r"Photosynthesis takes place mainly in which plant-cell organelle?",
            "difficulty": 1,
            "choices": [("Chloroplast", True), ("Mitochondrion", False),
                        ("Nucleus", False), ("Ribosome", False)],
            "explanation": r"Chloroplasts contain chlorophyll, which captures light energy for photosynthesis.",
        },
        {
            "text": r"Which are the INPUTS (reactants) of photosynthesis?",
            "difficulty": 2,
            "choices": [("Carbon dioxide, water, and light", True),
                        ("Glucose and oxygen", False),
                        ("ATP and lactic acid", False),
                        ("Protein and minerals", False)],
            "explanation": r"Photosynthesis uses carbon dioxide, water, and light energy to make glucose and oxygen. Glucose and oxygen are the products.",
        },
        {
            "text": r"Which are the OUTPUTS (products) of photosynthesis?",
            "difficulty": 2,
            "choices": [("Glucose and oxygen", True),
                        ("Carbon dioxide and water", False),
                        ("ATP and heat only", False),
                        ("Nitrogen and salt", False)],
            "explanation": r"Photosynthesis produces glucose (which stores the energy) and oxygen (released into the air).",
        },
        {
            "text": ("Use the photosynthesis diagram.\n\n"
                     "[[figure:photosynthesis_overview|Inputs and outputs of photosynthesis]]\n\n"
                     "According to the diagram, the oxygen leaves the chloroplast as a:"),
            "difficulty": 1,
            "choices": [("Product (output) of photosynthesis", True),
                        ("Reactant (input) of photosynthesis", False),
                        ("Source of light energy", False),
                        ("Type of sugar", False)],
            "explanation": r"The diagram shows oxygen as an output. Photosynthesis releases oxygen as it builds glucose. Pro tip: inputs go in (CO2, water, light); outputs come out (glucose, oxygen).",
        },
        {
            "text": r"Where does most of the new mass of a growing plant actually come from?",
            "difficulty": 3,
            "choices": [("Carbon dioxide from the air", True),
                        ("Soil eaten through the roots", False),
                        ("Water alone", False),
                        ("Sunlight turning into solid matter", False)],
            "explanation": r"The carbon in a plant's sugars and structures comes mostly from carbon dioxide in the air, not from soil. Water and minerals matter too, but the bulk of added carbon is from CO2.",
        },
        # --- Lesson 3: cellular respiration ---
        {
            "text": r"Cellular respiration takes place mainly in which organelle?",
            "difficulty": 1,
            "choices": [("Mitochondrion", True), ("Chloroplast", False),
                        ("Cell wall", False), ("Vacuole", False)],
            "explanation": r"Mitochondria release usable energy (ATP) from glucose through cellular respiration.",
        },
        {
            "text": r"Which are the INPUTS of cellular respiration?",
            "difficulty": 2,
            "choices": [("Glucose and oxygen", True),
                        ("Carbon dioxide and water", False),
                        ("Light and chlorophyll", False),
                        ("Lactic acid and alcohol", False)],
            "explanation": r"Cellular respiration uses glucose and oxygen and produces carbon dioxide, water, and ATP.",
        },
        {
            "text": r"Which list gives the OUTPUTS of cellular respiration?",
            "difficulty": 2,
            "choices": [("Carbon dioxide, water, and ATP", True),
                        ("Glucose and oxygen", False),
                        ("Light and sugar", False),
                        ("Only oxygen", False)],
            "explanation": r"Respiration breaks glucose down with oxygen, releasing carbon dioxide, water, and usable energy as ATP.",
        },
        {
            "text": r"Why is breathing NOT the same thing as cellular respiration?",
            "difficulty": 2,
            "choices": [("Breathing moves air; cellular respiration is the chemical process in cells that makes ATP", True),
                        ("They are exactly the same thing", False),
                        ("Breathing happens in mitochondria", False),
                        ("Cellular respiration only happens in the lungs", False)],
            "explanation": r"Breathing supplies oxygen and removes carbon dioxide by moving air. Cellular respiration is the chemical reaction inside cells that uses that oxygen to make ATP.",
        },
        {
            "text": r"Aerobic cellular respiration produces much more ATP than fermentation because it:",
            "difficulty": 3,
            "choices": [("Uses oxygen to break glucose down more completely", True),
                        ("Does not need any glucose", False),
                        ("Happens in the nucleus", False),
                        ("Produces light instead of heat", False)],
            "explanation": r"With oxygen, cells fully break down glucose in the mitochondria, capturing far more energy as ATP than the small amount fermentation yields.",
        },
        # --- Lesson 4: the two processes linked ---
        {
            "text": r"How are photosynthesis and cellular respiration related?",
            "difficulty": 1,
            "choices": [("The products of one are the reactants of the other", True),
                        ("They are completely unrelated", False),
                        ("Both only happen in animals", False),
                        ("Both destroy energy permanently", False)],
            "explanation": r"Photosynthesis makes the glucose and oxygen that respiration uses, and respiration makes the carbon dioxide and water that photosynthesis uses.",
        },
        {
            "text": r"Do plants carry out cellular respiration?",
            "difficulty": 2,
            "choices": [("Yes — plant cells need ATP, so they respire all the time", True),
                        ("No — plants only photosynthesize", False),
                        ("Only at night, never during the day", False),
                        ("Only when they are dying", False)],
            "explanation": r"Plants do both: they photosynthesize when there's light, and they run cellular respiration continuously to power their cells.",
        },
        {
            "text": ("Use the energy-cycle diagram.\n\n"
                     "[[figure:photo_resp_link|How photosynthesis and respiration connect]]\n\n"
                     "According to the diagram, the carbon dioxide released by respiration is:"),
            "difficulty": 2,
            "choices": [("Used as a raw material by photosynthesis", True),
                        ("Destroyed and removed forever", False),
                        ("Turned directly into ATP", False),
                        ("Converted into sunlight", False)],
            "explanation": r"The diagram shows respiration's CO2 and water feeding back into photosynthesis. The two processes recycle carbon and oxygen. Pro tip: outputs of one = inputs of the other.",
        },
        {
            "text": r"Photosynthesis ______ energy in glucose, while cellular respiration ______ it.",
            "difficulty": 2,
            "choices": [("stores; releases", True),
                        ("releases; stores", False),
                        ("destroys; creates", False),
                        ("hides; deletes", False)],
            "explanation": r"Photosynthesis stores light energy as chemical energy in sugar; respiration releases that energy as ATP for the cell to use.",
        },
        # --- Lesson 5: fermentation ---
        {
            "text": r"Fermentation allows cells to make ATP:",
            "difficulty": 1,
            "choices": [("Without oxygen", True), ("Only with lots of oxygen", False),
                        ("Using sunlight directly", False), ("Without any glucose", False)],
            "explanation": r"Fermentation is an anaerobic process — it makes a small amount of ATP when oxygen is not available.",
        },
        {
            "text": r"Yeast making carbon dioxide bubbles that cause bread dough to rise is an example of:",
            "difficulty": 2,
            "choices": [("Alcoholic fermentation", True), ("Photosynthesis", False),
                        ("Mitosis", False), ("Osmosis", False)],
            "explanation": r"Yeast carry out alcoholic fermentation, producing alcohol and carbon dioxide. The CO2 bubbles make dough rise.",
        },
        {
            "text": r"During intense exercise when muscle cells run low on oxygen, they may carry out:",
            "difficulty": 2,
            "choices": [("Lactic acid fermentation", True), ("Photosynthesis", False),
                        ("Alcoholic fermentation", False), ("Digestion", False)],
            "explanation": r"When oxygen is in short supply, muscle cells use lactic acid fermentation to keep making a little ATP.",
        },
        {
            "text": r"Compared with aerobic respiration, fermentation produces:",
            "difficulty": 2,
            "choices": [("Much less ATP", True), ("Much more ATP", False),
                        ("More oxygen", False), ("More chromosomes", False)],
            "explanation": r"Fermentation yields only a small amount of ATP (about 2 per glucose) versus the much larger amount (about 36) from aerobic respiration.",
        },
        {
            "text": ("Use the fermentation diagram.\n\n"
                     "[[figure:fermentation_paths|Glucose breakdown with and without oxygen]]\n\n"
                     "According to the diagram, which path does a cell take when oxygen is NOT available?"),
            "difficulty": 2,
            "choices": [("Fermentation (a little ATP)", True),
                        ("Aerobic respiration (lots of ATP)", False),
                        ("Photosynthesis", False),
                        ("No path is possible", False)],
            "explanation": r"The diagram branches: with oxygen, the cell does aerobic respiration; without oxygen, it does fermentation, which makes far less ATP. Pro tip: no oxygen = fermentation.",
        },
        # --- Lesson 6: reading energy data ---
        {
            "text": r"On a graph of a plant's activity, rising OXYGEN output most directly indicates an increasing rate of:",
            "difficulty": 2,
            "choices": [("Photosynthesis", True), ("Fermentation", False),
                        ("Digestion", False), ("Mitosis", False)],
            "explanation": r"Oxygen is a product of photosynthesis, so more oxygen output points to a higher photosynthesis rate.",
        },
        {
            "text": r"Rising CARBON DIOXIDE output from an animal most directly indicates an increasing rate of:",
            "difficulty": 2,
            "choices": [("Cellular respiration", True), ("Photosynthesis", False),
                        ("Osmosis", False), ("Natural selection", False)],
            "explanation": r"Carbon dioxide is a product of cellular respiration, so more CO2 output points to a higher respiration rate.",
        },
        {
            "text": ("Use the photosynthesis-rate graph.\n\n"
                     "[[figure:photosynthesis_rate_graph|Photosynthesis rate vs. light intensity]]\n\n"
                     "The graph rises and then levels off. The leveling off most likely means:"),
            "difficulty": 3,
            "choices": [("Some other factor (like CO2 or temperature) is now limiting the rate", True),
                        ("Light has stopped reaching the plant", False),
                        ("The plant has died", False),
                        ("Photosynthesis has reversed into respiration", False)],
            "explanation": r"More light speeds photosynthesis until another factor becomes the limit; then adding light no longer helps and the curve flattens. Pro tip: a leveling curve points to a limiting factor.",
        },
        {
            "text": r"A graph shows two variables rising together. Before concluding that one CAUSES the other, you should:",
            "difficulty": 3,
            "choices": [("Look for a controlled experiment, because correlation is not causation", True),
                        ("Assume the first variable causes the second", False),
                        ("Assume the data must be wrong", False),
                        ("Ignore the units and labels", False)],
            "explanation": r"Two variables moving together is correlation. Demonstrating cause and effect requires a controlled experiment that changes one variable while holding others constant.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain how photosynthesis and cellular respiration are connected. In your answer, name where "
                "each process happens, list the main inputs and outputs of each, and describe how the two "
                "processes form a cycle that keeps carbon and oxygen moving through living things."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) photosynthesis occurs in chloroplasts, using CO2 + water + light to make "
                "glucose + oxygen; (2) respiration occurs in mitochondria, using glucose + oxygen to release "
                "CO2 + water + ATP; (3) explaining that the outputs of one are the inputs of the other, forming a "
                "cycle of carbon and oxygen; (4) optional: energy flows one way (sunlight in, heat out). Deduct for "
                "missing locations, reversed inputs/outputs, or no cycle explanation."
            ),
        },
        {
            "text": (
                "Compare aerobic cellular respiration with fermentation. Explain when each occurs, roughly how much "
                "ATP each produces, and give one real-world example of fermentation. Then explain why a cell would "
                "ever use fermentation if it makes so little ATP."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) aerobic respiration occurs when oxygen is available and produces a lot of ATP "
                "(about 36 per glucose) in the mitochondria; (2) fermentation occurs when oxygen is absent and "
                "produces only a little ATP (about 2 per glucose); (3) a valid example -- yeast/alcoholic "
                "fermentation (bread, CO2 bubbles) or muscle/lactic acid fermentation; (4) a cell uses fermentation "
                "because a little ATP without oxygen is better than none, letting it keep going until oxygen returns. "
                "Deduct for saying fermentation needs oxygen or produces more ATP than aerobic respiration."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Cellular Energy (Deep Dive)' course."

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
