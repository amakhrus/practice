"""
Seed the capstone 'GED Science: Full-Length Practice Test' course -- one mixed
review that pulls from every science strand the test covers:

  - Life Science       (~40% of the real test)
  - Physical Science   (~40%)
  - Earth & Space      (~20%)
  - Scientific Reasoning & Practices (woven throughout)

Concise recap lessons (reusing existing diagrams, each with a Quick Check) plus
a large mixed question bank in roughly test proportions. Every answer
explanation teaches the method, names the tempting wrong answer, and ends with a
Pro tip. Multiple choice only.

Run:
    python manage.py seed_ged_science_complete
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Science: Full-Length Practice Test (Life, Physical, Earth & Space)",
    "slug": "ged-science-complete-practice",
    "program": "GED",
    "subject": "science",
    "description": (
        "A capstone GED Science practice test that mixes every strand into one comprehensive "
        "review: Life Science (cells, energy, genetics, evolution, ecosystems, the human body), "
        "Physical Science (matter, atoms, reactions, energy, forces, waves), Earth & Space "
        "Science (the rock and water cycles, plate tectonics, weather, the solar system), and "
        "the scientific-reasoning skills woven through the whole exam. Free multiple-choice "
        "questions with full explanations and pro tips, plus quick recaps of each strand, so you "
        "can review all of GED Science in one place before test day."
    ),
    "lessons": [
        (
            "1. Recap: Life Science Essentials",
            r"""
Life Science is the **largest** part of the GED Science test. Make sure these core ideas are automatic.

[[figure:cell_animal|The cell is life's basic unit; each organelle has a job.]]

The must-knows:
- **Cells:** the nucleus is the control center (holds DNA); mitochondria are the powerhouse (release energy). Plant cells add a cell wall and chloroplasts.
- **Energy:** photosynthesis (in chloroplasts) **stores** energy in sugar; cellular respiration (in mitochondria) **releases** it. They form a cycle.
- **Genetics:** a dominant allele needs only one copy to show; a recessive trait needs two (bb). A Bb × Bb cross gives a 3 : 1 ratio.
- **Evolution:** natural selection acts on **populations over generations**, favoring inherited traits that aid survival.
- **Ecosystems:** energy flows from producers up; only about **10%** passes to each next level.

Common mix-up: thinking plants only do photosynthesis. They also respire around the clock.

[[check:Which organelle releases energy from food and is called the 'powerhouse'?|mitochondria;;mitochondrion|It carries out cellular respiration.]]
            """,
        ),
        (
            "2. Recap: Physical Science Essentials",
            r"""
Physical Science is about matter and energy -- the rules everything else obeys.

[[figure:atom_structure|Protons and neutrons sit in the nucleus; electrons orbit around it.]]

The must-knows:
- **Atoms:** protons are positive, electrons negative, neutrons neutral. The **atomic number** = the number of protons, which identifies the element.
- **States of matter:** solid → liquid → gas as particles gain energy and move faster. These are **physical** changes (no new substance).
- **Chemical change:** a new substance forms (burning, rusting). **Conservation of mass:** matter is not created or destroyed, so mass is the same before and after.
- **Energy:** potential energy is stored (position/height); kinetic energy is motion. Energy transforms but is conserved.
- **Forces & motion:** Newton's second law, \(F = ma\); speed \(= \dfrac{\text{distance}}{\text{time}}\).
- **Waves:** higher frequency means shorter wavelength.

Common mix-up: a physical change (ice melting) is reversible and makes no new substance; a chemical change (burning) does.

[[check:What particle has a positive charge and sits in the nucleus?|proton;;protons|Its count is the atomic number.]]
            """,
        ),
        (
            "3. Recap: Earth & Space Science Essentials",
            r"""
Earth & Space Science is the smallest strand, but its cycles and patterns are very testable.

[[figure:rock_cycle|Rocks change type through heat, pressure, weathering, melting, and cooling.]]

The must-knows:
- **Rock cycle:** igneous (cooled magma), sedimentary (compacted layers, often with fossils), and metamorphic (changed by heat and pressure) rocks transform into one another.
- **Water cycle:** evaporation → condensation → precipitation → collection, driven by the **Sun**.
- **Plate tectonics:** Earth's plates move, building mountains and causing earthquakes and volcanoes at their boundaries.
- **Earth's layers:** crust, mantle, outer core (liquid), inner core (solid).
- **Day, seasons, Moon:** day/night come from Earth's **rotation**; seasons come from Earth's **tilt**, not its distance from the Sun; Moon phases come from its orbit.

Common mix-up: seasons are caused by the Earth's **tilt** (which hemisphere leans toward the Sun), not by how close Earth is to the Sun.

[[check:What drives the water cycle, powering evaporation?|sun;;the sun;;sunlight|Heat energy from it evaporates water.]]
            """,
        ),
        (
            "4. Recap: Scientific Reasoning on Test Day",
            r"""
Roughly **half** of GED Science questions test how you *think*, not what you memorized. These skills earn points on every passage.

[[figure:scientific_method|A testable hypothesis and a fair experiment are the heart of science.]]

The must-knows:
- **Hypothesis:** a testable, falsifiable 'if … then' prediction.
- **Variables:** the **independent** variable is what you change; the **dependent** variable is what you measure; **controlled** variables are kept the same. A fair test changes only **one** thing.
- **Correlation vs. causation:** two things rising together does **not** prove one causes the other -- a third factor may explain both.
- **Reading data:** check the title, axis labels, units, and scale before answering.
- **Valid conclusions:** stay within what the data shows; distrust answers using *always*, *never*, or *proves*.

Common mix-up: a strong correlation is not proof of cause. Only a controlled experiment can show causation.

[[check:Two things rise together. Does that prove one causes the other? (yes/no)|no|A third factor could cause both.]]
            """,
        ),
        (
            "5. Test-Taking Strategy for GED Science",
            r"""
The GED Science test gives you about **90 minutes** for roughly **34 questions**, mixing all the strands above with short passages, tables, and graphs. Work the question, not your memory.

A reliable routine for every item:
- **Read the question's last line first**, then the passage or figure. Know what is actually being asked.
- **Use the passage and data.** Most answers are supported right there -- resist relying only on outside facts.
- **For a graph or table,** read the title, the axis labels, the units, and the scale before you read the answer choices.
- **Eliminate overreach.** Choices with *always, never, all, proves* are usually traps; the cautious answer the data supports is usually right.
- **Don't leave blanks.** There is no penalty for guessing -- eliminate what you can, then choose.

Error analysis: a passage shows coffee drinkers live longer, and a choice says 'coffee causes long life.' That overreaches -- the data is a correlation, so the safe choice is 'coffee is associated with longer life.'

Pace check: about 90 minutes for 34 questions is roughly **2.5 minutes each**. If one stalls you, mark your best guess and move on.

[[check:If a study shows only a correlation, which word in an answer choice is a red flag?|proves;;causes;;always;;never|These claim more than a correlation can show.]]
            """,
        ),
    ],
    "mcqs": [
        # ===================== LIFE SCIENCE (~40%) =====================
        {
            "text": r"Which organelle is known as the 'powerhouse of the cell'?",
            "difficulty": 1,
            "choices": [("Mitochondrion", True), ("Nucleus", False), ("Ribosome", False), ("Cell wall", False)],
            "explanation": r"Mitochondria release energy (ATP) from food through cellular respiration. The trap, the nucleus, is the control center that holds DNA. Pro tip: powerhouse = mitochondria; control center = nucleus.",
        },
        {
            "text": r"What is the defining difference between a prokaryotic and a eukaryotic cell?",
            "difficulty": 2,
            "choices": [("Eukaryotes have a nucleus; prokaryotes do not", True), ("Only eukaryotes contain DNA", False), ("Prokaryotes are always larger", False), ("Only prokaryotes have a cell membrane", False)],
            "explanation": r"The nucleus is the key: eukaryotes enclose their DNA in one, prokaryotes (bacteria) do not. The trap claims only eukaryotes have DNA -- both do. Pro tip: 'pro' = no nucleus; 'eu' = true nucleus.",
        },
        {
            "text": r"Which two structures are found in plant cells but NOT in animal cells?",
            "difficulty": 2,
            "choices": [("Cell wall and chloroplasts", True), ("Nucleus and ribosomes", False), ("Mitochondria and cytoplasm", False), ("Cell membrane and nucleus", False)],
            "explanation": r"Plant cells add a rigid cell wall (support) and chloroplasts (photosynthesis). The traps list parts both cells share. Pro tip: plants are stuck in place and make their own food -- wall + chloroplasts.",
        },
        {
            "text": r"In photosynthesis, which two ingredients does a plant combine using light energy?",
            "difficulty": 2,
            "choices": [("Carbon dioxide and water", True), ("Oxygen and glucose", False), ("Glucose and water", False), ("Oxygen and carbon dioxide", False)],
            "explanation": r"Photosynthesis uses carbon dioxide + water + light to make glucose + oxygen. The trap (oxygen and glucose) lists the products, not the ingredients. Pro tip: ingredients go in (CO2, water); products come out (sugar, O2).",
        },
        {
            "text": r"Cellular respiration takes place mainly in which organelle?",
            "difficulty": 1,
            "choices": [("Mitochondria", True), ("Chloroplasts", False), ("Nucleus", False), ("Cell wall", False)],
            "explanation": r"Respiration releases energy from glucose in the mitochondria. The trap, chloroplasts, is where photosynthesis happens. Pro tip: respiration = mitochondria; photosynthesis = chloroplasts.",
        },
        {
            "text": r"Two parents are each Bb, where B (brown) is dominant over b (blue). What fraction of offspring is expected to show the blue trait?",
            "difficulty": 2,
            "choices": [(r"\(\tfrac{1}{4}\)", True), (r"\(\tfrac{3}{4}\)", False), (r"\(\tfrac{1}{2}\)", False), (r"\(0\)", False)],
            "explanation": r"A Bb × Bb cross gives BB, Bb, Bb, bb. Only bb (1 of 4) shows the recessive trait, so \(\tfrac{1}{4}\). The trap \(\tfrac{3}{4}\) is the dominant share. Pro tip: a recessive trait needs two recessive alleles.",
        },
        {
            "text": r"An organism shows a recessive trait. What must its genotype be?",
            "difficulty": 2,
            "choices": [("bb (two recessive alleles)", True), ("BB", False), ("Bb", False), ("Either BB or Bb", False)],
            "explanation": r"A recessive trait appears only with two recessive alleles, so bb. The trap Bb would show the dominant trait. Pro tip: visible recessive = both copies recessive, no exceptions.",
        },
        {
            "text": r"A few bacteria survive an antibiotic and multiply until most of the population is resistant. This is an example of:",
            "difficulty": 2,
            "choices": [("Natural selection", True), ("Photosynthesis", False), ("Homeostasis", False), ("A bacterium choosing to adapt", False)],
            "explanation": r"Resistant individuals survive and reproduce while others die, so resistance spreads -- natural selection. The trap says an individual 'chooses' to adapt; no individual chooses. Pro tip: selection acts on populations across generations.",
        },
        {
            "text": r"In a food chain, what do the arrows represent?",
            "difficulty": 1,
            "choices": [("The flow of energy from food to consumer", True), ("The direction predators run", False), ("Which organism is largest", False), ("Energy flowing from consumer to food", False)],
            "explanation": r"Arrows point from the organism eaten toward the eater, showing energy's direction. The trap reverses it. Pro tip: follow the arrow to see where the energy goes -- into the consumer.",
        },
        {
            "text": r"About how much of the energy at one level of an energy pyramid passes to the next level up?",
            "difficulty": 2,
            "choices": [("About 10%", True), ("About 50%", False), ("About 90%", False), ("100%", False)],
            "explanation": r"Only ~10% transfers; the rest is lost mostly as heat. The trap 90% reverses this. Pro tip: because so little passes up, higher levels support far fewer organisms.",
        },
        {
            "text": r"Which pair of body systems works together to take in oxygen and deliver it to the body's cells?",
            "difficulty": 2,
            "choices": [("Respiratory and circulatory", True), ("Digestive and nervous", False), ("Skeletal and muscular", False), ("Immune and digestive", False)],
            "explanation": r"The respiratory system brings oxygen into the lungs; the circulatory system carries it in the blood to cells. Pro tip: look for what two systems exchange -- here, oxygen.",
        },
        {
            "text": r"Sweating to cool down on a hot day is an example of:",
            "difficulty": 1,
            "choices": [("Homeostasis", True), ("Natural selection", False), ("Photosynthesis", False), ("Inheritance", False)],
            "explanation": r"Returning body temperature toward normal is homeostasis -- a stable internal environment kept by feedback. Pro tip: homeostasis = the body fighting a change to stay balanced.",
        },
        {
            "text": r"A segment of DNA that codes for a particular trait is called a:",
            "difficulty": 1,
            "choices": [("Gene", True), ("Cell", False), ("Protein", False), ("Chromosome", False)],
            "explanation": r"A gene is the DNA segment coding for a trait. The trap, chromosome, is a whole bundle of DNA holding many genes. Pro tip: gene = one instruction; chromosome = the whole instruction book.",
        },
        {
            "text": r"Which group of organisms makes its own food and forms the base of most food chains?",
            "difficulty": 1,
            "choices": [("Producers", True), ("Consumers", False), ("Decomposers", False), ("Predators", False)],
            "explanation": r"Producers (plants) make food by photosynthesis, so they sit at the base. The trap, decomposers, recycle dead matter rather than starting the chain. Pro tip: producers capture the Sun's energy first.",
        },
        # ===================== PHYSICAL SCIENCE (~40%) =====================
        {
            "text": r"Which subatomic particle carries a negative charge?",
            "difficulty": 1,
            "choices": [("Electron", True), ("Proton", False), ("Neutron", False), ("Nucleus", False)],
            "explanation": r"Electrons are negative and orbit the nucleus. The trap, proton, is positive; neutrons are neutral. Pro tip: electron = negative; proton = positive; neutron = neutral (no charge).",
        },
        {
            "text": r"The atomic number of an element tells you the number of:",
            "difficulty": 2,
            "choices": [("Protons", True), ("Neutrons", False), ("Electrons plus neutrons", False), ("Total particles", False)],
            "explanation": r"The atomic number equals the proton count, which identifies the element. The trap counts neutrons (that changes the mass number, not the element). Pro tip: change the protons and you change the element itself.",
        },
        {
            "text": r"As a solid is heated and becomes a liquid, then a gas, its particles:",
            "difficulty": 2,
            "choices": [("Gain energy and move faster and farther apart", True), ("Lose energy and slow down", False), ("Disappear", False), ("Turn into a different element", False)],
            "explanation": r"Heat adds energy, so particles move faster and spread out: solid → liquid → gas. The trap reverses it. Pro tip: more heat = more particle motion = more spread-out states.",
        },
        {
            "text": r"Which of the following is a CHEMICAL change?",
            "difficulty": 2,
            "choices": [("Iron rusting", True), ("Ice melting", False), ("Water boiling", False), ("Tearing paper", False)],
            "explanation": r"Rusting forms a new substance (iron oxide), so it is chemical. The traps are physical changes -- no new substance, often reversible. Pro tip: new substance formed = chemical; same substance, new form = physical.",
        },
        {
            "text": r"In a sealed container, 10 g of reactants combine in a chemical reaction. What is the total mass of the products?",
            "difficulty": 2,
            "choices": [("10 g", True), ("Less than 10 g", False), ("More than 10 g", False), ("0 g", False)],
            "explanation": r"By the law of conservation of mass, matter is neither created nor destroyed, so the products also total 10 g. The traps assume mass changes. Pro tip: in a closed system, mass in = mass out.",
        },
        {
            "text": r"A ball held at the top of a hill, not yet moving, has mostly which kind of energy?",
            "difficulty": 1,
            "choices": [("Potential energy", True), ("Kinetic energy", False), ("Chemical energy", False), ("No energy", False)],
            "explanation": r"Stored energy due to height is potential energy. The trap, kinetic, is energy of motion -- it appears once the ball rolls. Pro tip: position/height = potential; motion = kinetic.",
        },
        {
            "text": r"Newton's second law is \(F = ma\). If the same force is applied to a lighter and a heavier object, the lighter object will have:",
            "difficulty": 3,
            "choices": [("A greater acceleration", True), ("A smaller acceleration", False), ("The same acceleration", False), ("No acceleration", False)],
            "explanation": r"Rearranged, \(a = F/m\): with force fixed, smaller mass gives larger acceleration. The trap reverses the relationship. Pro tip: lighter objects are easier to speed up for the same push.",
        },
        {
            "text": r"A car travels 150 km in 3 hours. What is its average speed?",
            "difficulty": 2,
            "choices": [("50 km/h", True), ("450 km/h", False), ("153 km/h", False), ("3 km/h", False)],
            "explanation": r"Speed \(= \dfrac{\text{distance}}{\text{time}} = \dfrac{150}{3} = 50\) km/h. The trap 450 multiplies instead of divides. Pro tip: speed divides distance by time -- the units (km/h) tell you so.",
        },
        {
            "text": r"For waves, as the frequency increases, the wavelength:",
            "difficulty": 2,
            "choices": [("Decreases", True), ("Increases", False), ("Stays the same", False), ("Becomes zero", False)],
            "explanation": r"Frequency and wavelength are inversely related: more waves per second means each is shorter. The trap says they rise together. Pro tip: squeeze in more waves and each one must get shorter.",
        },
        {
            "text": r"On the pH scale, a solution with a pH of 2 is:",
            "difficulty": 2,
            "choices": [("A strong acid", True), ("A strong base", False), ("Neutral", False), ("Pure water", False)],
            "explanation": r"pH below 7 is acidic, and 2 is strongly acidic. The trap calls low pH a base; bases are above 7. Pro tip: low pH = acid, high pH = base, 7 = neutral (pure water).",
        },
        {
            "text": r"Energy cannot be created or destroyed, only changed in form. A toaster mainly converts electrical energy into:",
            "difficulty": 1,
            "choices": [("Heat (thermal) energy", True), ("Chemical energy", False), ("Nuclear energy", False), ("Sound energy", False)],
            "explanation": r"A toaster turns electrical energy into heat (and some light). The traps name forms not central to toasting. Pro tip: energy transforms but the total is conserved -- track 'electrical in, heat out.'",
        },
        {
            "text": r"In the periodic table, elements in the same vertical column (group) tend to have:",
            "difficulty": 3,
            "choices": [("Similar chemical properties", True), ("Exactly the same mass", False), ("The same number of neutrons", False), ("No relationship at all", False)],
            "explanation": r"Elements in a group share similar chemical behavior because of their outer-electron arrangement. The traps confuse this with mass or neutrons. Pro tip: columns = chemical 'families' that act alike.",
        },
        # ===================== EARTH & SPACE SCIENCE (~20%) =====================
        {
            "text": r"What is the main source of energy that drives the water cycle?",
            "difficulty": 1,
            "choices": [("The Sun", True), ("The Moon", False), ("Earth's core", False), ("Wind", False)],
            "explanation": r"The Sun's heat evaporates water, powering the cycle. The trap, the Moon, drives tides, not the water cycle. Pro tip: evaporation needs heat, and that heat comes from the Sun.",
        },
        {
            "text": r"Sedimentary rock, which often contains fossils, forms when:",
            "difficulty": 2,
            "choices": [("Layers of sediment are compacted and cemented", True), ("Magma cools and hardens", False), ("Rock is changed by intense heat and pressure", False), ("Water evaporates from the ocean", False)],
            "explanation": r"Compacted layers of sediment make sedimentary rock -- and trap fossils. The traps describe igneous (cooled magma) and metamorphic (heat/pressure) rock. Pro tip: 'sediment' → sedimentary; layers and fossils are the clue.",
        },
        {
            "text": r"Earthquakes and volcanoes occur most often:",
            "difficulty": 2,
            "choices": [("At the boundaries between tectonic plates", True), ("Only at the equator", False), ("In the center of large plates", False), ("Only where it is cold", False)],
            "explanation": r"Plate boundaries are where plates grind, pull apart, or collide, releasing energy. The trap places them mid-plate, where activity is rare. Pro tip: 'boundary' = where the action (quakes, volcanoes) happens.",
        },
        {
            "text": r"What causes the seasons on Earth?",
            "difficulty": 2,
            "choices": [("The tilt of Earth's axis", True), ("Earth's changing distance from the Sun", False), ("The Moon blocking sunlight", False), ("Changes in the Sun's output", False)],
            "explanation": r"Earth's tilt means each hemisphere leans toward or away from the Sun, creating seasons. The trap (distance) is the famous misconception -- Earth is actually closest to the Sun in northern winter. Pro tip: seasons = tilt, not distance.",
        },
        {
            "text": r"The different phases of the Moon (new, crescent, full) are caused by:",
            "difficulty": 2,
            "choices": [("The Moon's orbit changing how much of its lit side we see", True), ("Earth's shadow falling on the Moon each night", False), ("The Moon producing its own light", False), ("Clouds covering part of the Moon", False)],
            "explanation": r"As the Moon orbits, we see different amounts of its sunlit half -- that is the phases. The trap (Earth's shadow) describes an eclipse, which is rare. Pro tip: phases come from viewing angle, not Earth's shadow.",
        },
        {
            "text": r"Which layer of the Earth is the thin, solid, outermost layer we live on?",
            "difficulty": 1,
            "choices": [("The crust", True), ("The mantle", False), ("The outer core", False), ("The inner core", False)],
            "explanation": r"The crust is the thin outer shell. Below it the mantle is hot rock that flows slowly, the outer core is liquid, and the inner core is solid. Pro tip: order from the outside in -- crust, mantle, outer core, inner core.",
        },
        {
            "text": r"Day and night are caused by:",
            "difficulty": 1,
            "choices": [("Earth rotating on its axis", True), ("Earth orbiting the Sun once a year", False), ("The Moon's phases", False), ("The Sun turning on and off", False)],
            "explanation": r"Earth's daily rotation turns each spot toward and away from the Sun. The trap (the yearly orbit) causes the year and, with the tilt, the seasons. Pro tip: rotation = day/night; revolution (orbit) = the year.",
        },
        {
            "text": r"In our solar system, the planets:",
            "difficulty": 1,
            "choices": [("Orbit the Sun", True), ("Orbit the Earth", False), ("Stay in fixed positions", False), ("Orbit the Moon", False)],
            "explanation": r"The planets orbit the Sun, which holds them with gravity. The trap (Earth-centered) is the old, incorrect model. Pro tip: the Sun is the center of the solar system; planets revolve around it.",
        },
        # ===================== SCIENTIFIC REASONING (woven throughout) =====================
        {
            "text": r"Which statement is a testable scientific hypothesis?",
            "difficulty": 2,
            "choices": [("If a plant gets more sunlight, then it will grow taller", True), ("Sunsets are beautiful", False), ("Plants are important", False), ("Everyone should garden", False)],
            "explanation": r"A hypothesis is a testable 'if … then' prediction. The traps are opinions no experiment could prove false. Pro tip: if no test could ever disprove it, it is not a scientific hypothesis.",
        },
        {
            "text": r"A student tests a fertilizer by giving Group A fertilizer and Group B none, keeping light and water the same. What is the dependent variable?",
            "difficulty": 2,
            "choices": [("The height the plants grow", True), ("The amount of fertilizer", False), ("The amount of water", False), ("The type of plant", False)],
            "explanation": r"The dependent variable is what you measure in response -- plant height. The trap (fertilizer) is the independent variable you change. Pro tip: independent = what you change; dependent = what you measure.",
        },
        {
            "text": r"A town notices that as ice-cream sales rise, drownings also rise. What is the best conclusion?",
            "difficulty": 3,
            "choices": [("A third factor, like hot weather, likely causes both", True), ("Eating ice cream causes drowning", False), ("Drowning makes people buy ice cream", False), ("The data must be wrong", False)],
            "explanation": r"This is correlation, not causation -- hot summer weather raises both. The traps invent a cause-and-effect the data can't support. Pro tip: when two things rise together, ask whether a third factor drives both.",
        },
        {
            "text": r"Find the mean (average) of the measurements \(4, 8, 6, 2\).",
            "difficulty": 1,
            "choices": [(r"\(5\)", True), (r"\(6\)", False), (r"\(20\)", False), (r"\(4\)", False)],
            "explanation": r"Mean \(= \dfrac{4+8+6+2}{4} = \dfrac{20}{4} = 5\). The trap 20 is the sum without dividing. Pro tip: mean = add up, then divide by how many values there are.",
        },
        {
            "text": r"Write the number \(0.0004\) in scientific notation.",
            "difficulty": 2,
            "choices": [(r"\(4 \times 10^{-4}\)", True), (r"\(4 \times 10^{4}\)", False), (r"\(4 \times 10^{-3}\)", False), (r"\(0.4 \times 10^{-3}\)", False)],
            "explanation": r"Move the decimal 4 places to reach 4, so the exponent is \(-4\). The trap \(4 \times 10^{4}\) would be a huge number. Pro tip: a negative exponent marks a small number, not a negative one.",
        },
        {
            "text": r"A study at one school finds students who ate breakfast scored higher on one test. Which conclusion does the data BEST support?",
            "difficulty": 3,
            "choices": [("In this group, breakfast was associated with higher scores", True), ("Breakfast guarantees better grades for everyone", False), ("Skipping breakfast always lowers scores", False), ("Breakfast proves intelligence", False)],
            "explanation": r"A valid conclusion stays within the data's scope -- one group, an association. The traps overreach with 'guarantees,' 'always,' and 'everyone.' Pro tip: on the GED, the cautious answer the data supports is usually right.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the capstone full-length GED Science practice-test course (MCQ only)."

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
