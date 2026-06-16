"""
Seed a full-length 'GED Science' practice exam that mirrors the real test:

  - 34 questions, the real GED Science test length, in 90 minutes.
  - Built around the three content areas: Life Science (~40%), Physical Science
    (~40%), and Earth & Space Science (~20%), with scientific-reasoning items
    (data, graphs, and experimental design) woven throughout.
  - Scored 100-200 (145 to pass); a calculator and formula sheet are available.
  - A foundational (Level 1) difficulty spread (easy / medium / hard).

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip. Several questions reuse the diagram library.

Run:
    python manage.py seed_ged_science_exam
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Full-Length Practice Exam (Level 1 - Foundational)",
    "slug": "ged-science-exam",
    "program": "GED",
    "subject": "science",
    "description": (
        "A full-length, test-day-style GED Science practice exam: 34 questions modeled on the real "
        "blueprint, spanning Life Science, Physical Science, and Earth & Space Science, with scientific-"
        "reasoning items (reading graphs and tables, and judging experiments) woven throughout. It "
        "covers the core tested ideas -- cells and the human body, genetics and ecosystems, atoms and "
        "matter, energy and forces, and Earth's cycles and the solar system -- at a foundational, easy-"
        "to-hard difficulty spread. Every question includes a worked explanation and a pro tip, and many "
        "reuse the diagram library. Use the lessons to learn the test format (90 minutes, scored 100-"
        "200, 145 to pass) before taking the 34 questions as one timed rehearsal."
    ),
    "lessons": [
        (
            "1. How the GED Science Test Works",
            r"""
This exam is built to feel like the **real GED Science test**. Here is what you are walking into:

- **About 34 questions** in **90 minutes** -- roughly 2.5 minutes each.
- It is one timed section (no separate parts), built around **passages, graphs, tables, and diagrams**. Most questions hand you the information you need -- the answer is often right there in the source.
- The content comes from **three areas**:
  - **Life Science** (about 40%) -- cells, genetics, evolution, ecosystems, and the human body.
  - **Physical Science** (about 40%) -- matter, atoms, chemical reactions, energy, forces, and motion.
  - **Earth & Space Science** (about 20%) -- Earth's structure and cycles, weather, and the solar system.
- A **calculator** and a **formula sheet** are available for the few questions that need them.

**Scoring:** the test is scored from **100 to 200**, and you need **145 to pass**. There is **no penalty for a wrong answer**, so never leave a question blank.

[[check:How many questions are on the GED Science test?|34|It is about 34 questions in 90 minutes.]]
            """,
        ),
        (
            "2. Reading the Source & Scientific Reasoning",
            r"""
GED Science is less about memorizing facts and more about **reasoning from evidence**. The most useful habits:

- **Use the source.** A graph, table, or diagram usually contains the answer -- read the title, the labels, and the units first.
- **Correlation is not causation.** Two things rising together doesn't prove one caused the other.
- **A fair test changes one thing.** In an experiment, the **independent variable** is what you change; the **controlled variables** are kept the same so the test is fair.
- **Energy and matter are conserved.** They are not created or destroyed, only transformed or transferred.

[[figure:controlled_experiment|In a fair test, only the variable being studied changes; everything else stays the same.]]

[[check:In an experiment, what do we call the variables that are deliberately kept the same?|controlled variables;;controlled;;control variables|Controlled variables are held constant to keep the test fair.]]
            """,
        ),
        (
            "3. Test-Day Game Plan",
            r"""
You have the science skills; this is about using them well across 34 questions.

- **Pacing.** About 2.5 minutes per question. If one stalls you, lock in a best guess, flag it, and move on.
- **Read the last line.** Know exactly what the question asks -- a cause, an effect, a prediction, or a value from a graph.
- **Estimate and sanity-check.** A quick estimate catches a misread graph or a decimal error.
- **Never leave a blank.** No penalty for wrong answers -- eliminate what you can, then choose.
- **Use what the test gives you:** the passages, graphs, and diagrams, plus the calculator and formula sheet when a question needs them.

[[check:Is there any penalty for a wrong answer on the GED Science test? Answer yes or no.|no|So always guess rather than leave a blank.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============================ LIFE SCIENCE ===========================
        # =====================================================================
        {
            "text": r"**Life Science.** Which part of the cell is the control center, holding its DNA?",
            "difficulty": 1,
            "choices": [("The nucleus", True), ("The mitochondrion", False),
                        ("The cell membrane", False), ("The ribosome", False)],
            "explanation": r"The nucleus stores the cell's DNA and directs its activities. The trap, the mitochondrion, is the energy 'powerhouse.' Pro tip: nucleus = control center; mitochondria = energy.",
        },
        {
            "text": r"**Life Science.** Which organelle releases energy for the cell and is called its 'powerhouse'?",
            "difficulty": 1,
            "choices": [("The mitochondrion", True), ("The nucleus", False),
                        ("The cell wall", False), ("The vacuole", False)],
            "explanation": r"Mitochondria release energy from food in a process called cellular respiration. The trap, the nucleus, directs the cell but doesn't make its energy. Pro tip: think 'mighty mitochondria' -- the cell's power source.",
        },
        {
            "text": ("**Life Science.** Use the diagram.\n\n"
                     "[[figure:photosynthesis_overview|Inputs and outputs of photosynthesis]]\n\n"
                     "Which gas do plants take IN from the air during photosynthesis?"),
            "difficulty": 1,
            "choices": [("Carbon dioxide", True), ("Oxygen", False), ("Nitrogen", False), ("Helium", False)],
            "explanation": r"Plants take in carbon dioxide and release oxygen during photosynthesis. The trap, oxygen, is what they give off. Pro tip: photosynthesis takes in CO2 and water and makes sugar and oxygen.",
        },
        {
            "text": r"**Life Science.** What is the main job of the cell membrane?",
            "difficulty": 2,
            "choices": [("To control what enters and leaves the cell", True),
                        ("To store the cell's DNA", False),
                        ("To release energy from food", False),
                        ("To make the cell's proteins", False)],
            "explanation": r"The cell membrane is a gatekeeper, controlling what passes in and out. The trap, storing DNA, is the nucleus's job. Pro tip: the membrane is the cell's 'border control.'",
        },
        {
            "text": ("**Life Science.** Use the food chain.\n\n"
                     "[[figure:food_chain|A simple food chain with arrows]]\n\n"
                     "In a food chain, organisms that make their own food, such as plants, are called:"),
            "difficulty": 1,
            "choices": [("Producers", True), ("Consumers", False),
                        ("Decomposers", False), ("Predators", False)],
            "explanation": r"Producers (like plants) make their own food through photosynthesis. The trap, consumers, must eat other organisms. Pro tip: producers PRODUCE their own food; consumers CONSUME it.",
        },
        {
            "text": ("**Life Science.** Use the diagram.\n\n"
                     "[[figure:dna_double_helix|The double-helix structure of DNA]]\n\n"
                     "What does the DNA inside a cell mainly carry?"),
            "difficulty": 2,
            "choices": [("The genetic instructions for the organism", True),
                        ("Energy for the cell to use", False),
                        ("Oxygen to the body's tissues", False),
                        ("Waste products to be removed", False)],
            "explanation": r"DNA carries the genetic instructions passed from parents to offspring. The trap, energy, is handled by mitochondria. Pro tip: DNA is the cell's instruction manual.",
        },
        {
            "text": ("**Life Science.** Use the Punnett square.\n\n"
                     "[[figure:punnett_square|A Punnett square for two Bb parents]]\n\n"
                     "Two parents are each Bb, where B (brown) is dominant over b (blue). What fraction of "
                     "their offspring is expected to show the blue (recessive) trait?"),
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{3}{4}\)", False),
                        (r"\(\frac{1}{2}\)", False), (r"0", False)],
            "explanation": r"A Bb x Bb cross gives BB, Bb, Bb, bb. Only bb (1 of 4) shows the recessive trait. The trap 3/4 is the dominant share. Pro tip: a recessive trait needs two recessive alleles.",
        },
        {
            "text": r"**Life Science.** A rabbit that eats only plants is best described as a:",
            "difficulty": 1,
            "choices": [("Herbivore", True), ("Carnivore", False),
                        ("Producer", False), ("Decomposer", False)],
            "explanation": r"An herbivore eats only plants. The trap, carnivore, eats meat. Pro tip: 'herb' hints at plants -- herbivores are plant-eaters.",
        },
        {
            "text": ("**Life Science.** Use the energy pyramid.\n\n"
                     "[[figure:energy_pyramid|An energy pyramid showing trophic levels]]\n\n"
                     "As you move UP an energy pyramid from one level to the next, the amount of available "
                     "energy generally:"),
            "difficulty": 2,
            "choices": [("Decreases", True), ("Increases", False),
                        ("Stays exactly the same", False), ("Doubles", False)],
            "explanation": r"Only about 10% of energy passes to the next level, so energy decreases going up. The trap 'increases' reverses this. Pro tip: most energy is lost as heat at each step, so higher levels have less.",
        },
        {
            "text": r"**Life Science.** Which body system is mainly responsible for pumping blood through the body?",
            "difficulty": 1,
            "choices": [("The circulatory system", True), ("The digestive system", False),
                        ("The respiratory system", False), ("The skeletal system", False)],
            "explanation": r"The circulatory system, with the heart, pumps blood. The trap, the respiratory system, handles breathing. Pro tip: 'circulatory' shares a root with 'circulate' -- it moves blood around.",
        },
        {
            "text": r"**Life Science.** In an ecosystem, organisms that break down dead material and recycle nutrients are called:",
            "difficulty": 2,
            "choices": [("Decomposers", True), ("Producers", False),
                        ("Herbivores", False), ("Predators", False)],
            "explanation": r"Decomposers (like bacteria and fungi) break down dead matter and return nutrients to the soil. The trap, producers, make food from sunlight. Pro tip: decomposers DECOMPOSE -- they recycle the dead.",
        },
        {
            "text": ("**Life Science.** A scientist wants to test whether fertilizer makes tomato plants "
                     "grow taller. To keep the test FAIR, what should be the same for both groups of plants?"),
            "difficulty": 2,
            "choices": [("The water, sunlight, and soil they receive", True),
                        ("Whether or not fertilizer is added", False),
                        ("The final height of the plants", False),
                        ("Nothing needs to be kept the same", False)],
            "explanation": r"Controlled variables (water, sunlight, soil) must be identical so the only difference is the fertilizer. The trap, whether fertilizer is added, is the variable being tested. Pro tip: a fair test changes only one thing.",
        },
        {
            "text": r"**Life Science.** A trait that helps an organism survive and reproduce in its environment is called a(n):",
            "difficulty": 2,
            "choices": [("Adaptation", True), ("Disease", False),
                        ("Predator", False), ("Habitat", False)],
            "explanation": r"An adaptation is a helpful inherited trait, like a thick coat for cold climates. The trap, habitat, is where an organism lives. Pro tip: adaptations help an organism 'fit' its environment.",
        },
        # =====================================================================
        # ========================== PHYSICAL SCIENCE =========================
        # =====================================================================
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:atom_structure|The structure of an atom]]\n\n"
                     "Which subatomic particle carries a NEGATIVE charge?"),
            "difficulty": 1,
            "choices": [("The electron", True), ("The proton", False),
                        ("The neutron", False), ("The nucleus", False)],
            "explanation": r"Electrons are negative and orbit the nucleus. The trap, the proton, is positive; neutrons are neutral. Pro tip: electron = negative, proton = positive, neutron = neutral.",
        },
        {
            "text": r"**Physical Science.** When a solid is heated until it melts into a liquid, its particles:",
            "difficulty": 1,
            "choices": [("Gain energy and move faster, spreading apart", True),
                        ("Lose energy and pack closer together", False),
                        ("Disappear completely", False),
                        ("Turn into a different element", False)],
            "explanation": r"Heat adds energy, so particles move faster and spread out as a solid melts. The trap reverses this. Pro tip: more heat means more particle motion.",
        },
        {
            "text": r"**Physical Science.** Which of the following is a CHEMICAL change?",
            "difficulty": 2,
            "choices": [("Wood burning into ash", True), ("Ice melting into water", False),
                        ("Water boiling into steam", False), ("A glass shattering", False)],
            "explanation": r"Burning forms new substances (ash, smoke), so it is a chemical change. The traps are physical changes -- the same substance in a new form. Pro tip: new substance = chemical; same substance = physical.",
        },
        {
            "text": r"**Physical Science.** Which of the following is a PHYSICAL change?",
            "difficulty": 1,
            "choices": [("Ice melting into water", True), ("Iron rusting", False),
                        ("A cake baking", False), ("Paper burning", False)],
            "explanation": r"Melting changes form but not substance -- it is still water -- so it is physical. The traps (rusting, baking, burning) form new substances. Pro tip: if you can reverse it without making something new, it's physical.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:conservation_mass|Mass before and after a chemical reaction]]\n\n"
                     "In a sealed chemical reaction, the total mass of the products compared with the "
                     "total mass of the reactants is:"),
            "difficulty": 2,
            "choices": [("Exactly the same", True), ("Always greater", False),
                        ("Always less", False), ("Zero", False)],
            "explanation": r"By the law of conservation of mass, matter is not created or destroyed, so the mass stays the same. The trap 'always greater' would create matter from nothing. Pro tip: atoms are only rearranged in a reaction, so mass is conserved.",
        },
        {
            "text": r"**Physical Science.** An object will change its speed or direction only when acted on by a(n):",
            "difficulty": 2,
            "choices": [("Unbalanced force", True), ("Balanced force", False),
                        ("Color change", False), ("Magnetic label", False)],
            "explanation": r"An unbalanced (net) force changes an object's motion. The trap, a balanced force, leaves motion unchanged. Pro tip: balanced forces cancel out; only an unbalanced force causes acceleration.",
        },
        {
            "text": r"**Physical Science.** A car travels 300 kilometers in 5 hours. What is its average speed?",
            "difficulty": 2,
            "choices": [("60 km/h", True), ("1,500 km/h", False),
                        ("295 km/h", False), ("305 km/h", False)],
            "explanation": r"Speed = distance / time = 300 / 5 = 60 km/h. The trap 1,500 multiplies instead of dividing. Pro tip: 'per hour' means divide the distance by the number of hours.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:energy_forms|Different forms of energy]]\n\n"
                     "A moving soccer ball has which type of energy?"),
            "difficulty": 1,
            "choices": [("Kinetic energy", True), ("Chemical energy", False),
                        ("Nuclear energy", False), ("Sound energy", False)],
            "explanation": r"Kinetic energy is the energy of motion, so a moving ball has it. The trap, chemical energy, is stored in bonds, like in food or fuel. Pro tip: kinetic = motion; potential = stored.",
        },
        {
            "text": r"**Physical Science.** When you drop a ball, it falls toward the ground because of:",
            "difficulty": 1,
            "choices": [("Gravity", True), ("Friction", False),
                        ("Magnetism", False), ("Electricity", False)],
            "explanation": r"Gravity pulls objects toward Earth's center. The trap, friction, opposes motion between surfaces. Pro tip: gravity is the force that gives objects weight and pulls them down.",
        },
        {
            "text": r"**Physical Science.** On the modern periodic table, the elements are arranged in order of increasing:",
            "difficulty": 2,
            "choices": [("Atomic number (number of protons)", True),
                        ("Color", False),
                        ("Melting temperature", False),
                        ("Date of discovery", False)],
            "explanation": r"Elements are ordered by atomic number, the number of protons. The trap, date of discovery, is not how the table is organized. Pro tip: each step across the table adds one proton.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:wave_anatomy|The parts of a wave]]\n\n"
                     "On a wave, the height from the rest position to a crest is called the:"),
            "difficulty": 2,
            "choices": [("Amplitude", True), ("Wavelength", False),
                        ("Frequency", False), ("Speed", False)],
            "explanation": r"Amplitude is the wave's height and is related to its energy. The trap, wavelength, is the distance between two crests. Pro tip: taller amplitude means more energy (a louder or brighter wave).",
        },
        {
            "text": r"**Physical Science.** Which material is the BEST conductor of electricity?",
            "difficulty": 2,
            "choices": [("Copper metal", True), ("Rubber", False),
                        ("Dry wood", False), ("Plastic", False)],
            "explanation": r"Metals like copper conduct electricity well. The traps (rubber, wood, plastic) are insulators that resist current. Pro tip: metals conduct; nonmetals like rubber and plastic insulate.",
        },
        {
            "text": r"**Physical Science.** A force that opposes motion between two surfaces that are touching is called:",
            "difficulty": 1,
            "choices": [("Friction", True), ("Gravity", False),
                        ("Magnetism", False), ("Buoyancy", False)],
            "explanation": r"Friction acts against motion where surfaces meet. The trap, gravity, pulls objects down rather than opposing sliding. Pro tip: friction is why a sliding object eventually slows and stops.",
        },
        # =====================================================================
        # ======================= EARTH & SPACE SCIENCE =======================
        # =====================================================================
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:water_cycle|The stages of the water cycle]]\n\n"
                     "Which process in the water cycle turns liquid water into water vapor?"),
            "difficulty": 1,
            "choices": [("Evaporation", True), ("Condensation", False),
                        ("Precipitation", False), ("Collection", False)],
            "explanation": r"Evaporation uses the Sun's heat to turn liquid water into vapor. The trap, condensation, is the reverse (vapor to liquid). Pro tip: evaporation goes up as vapor; condensation comes back as droplets.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:rock_cycle|The rock cycle]]\n\n"
                     "Igneous rock forms when:"),
            "difficulty": 2,
            "choices": [("Melted rock (magma or lava) cools and hardens", True),
                        ("Layers of sediment are pressed together", False),
                        ("Plants and animals decay", False),
                        ("Water freezes into ice", False)],
            "explanation": r"Igneous rock forms from cooled, hardened magma or lava. The trap, pressed sediment, forms sedimentary rock. Pro tip: 'igneous' relates to fire -- it comes from molten rock.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:earth_layers|The layers of Earth]]\n\n"
                     "Which layer is at the very center of Earth and is the hottest?"),
            "difficulty": 1,
            "choices": [("The core", True), ("The crust", False),
                        ("The atmosphere", False), ("The ocean", False)],
            "explanation": r"The core is Earth's hot, dense center. The trap, the crust, is the thin, cool outer layer we live on. Pro tip: think of Earth like a peach -- the core is the pit at the center.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:seasons|How Earth's tilt causes the seasons]]\n\n"
                     "What causes the seasons on Earth?"),
            "difficulty": 2,
            "choices": [("The tilt of Earth's axis", True),
                        ("Earth's changing distance from the Sun", False),
                        ("The phases of the Moon", False),
                        ("Solar flares from the Sun", False)],
            "explanation": r"Earth's tilt means each hemisphere leans toward or away from the Sun across the year. The trap (distance) is a common misconception. Pro tip: seasons come from tilt, not distance.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:moon_phases|The phases of the Moon]]\n\n"
                     "The changing phases of the Moon are caused by:"),
            "difficulty": 2,
            "choices": [("The Moon's position relative to the Sun and Earth", True),
                        ("Earth's shadow falling on the Moon each night", False),
                        ("Clouds covering parts of the Moon", False),
                        ("The Moon changing its actual shape", False)],
            "explanation": r"As the Moon orbits Earth, we see different amounts of its sunlit half, creating phases. The trap, Earth's shadow, causes a lunar eclipse, not the regular phases. Pro tip: phases come from the changing angle of sunlight we see.",
        },
        {
            "text": r"**Earth & Space.** Clouds form when water vapor in the air cools and:",
            "difficulty": 2,
            "choices": [("Condenses into tiny droplets", True),
                        ("Evaporates into gas", False),
                        ("Freezes the entire sky", False),
                        ("Turns into oxygen", False)],
            "explanation": r"Cooling vapor condenses into droplets, forming clouds. The trap, evaporates, is the opposite process. Pro tip: condensation is vapor becoming liquid -- the same reason dew forms.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:solar_system|The Sun and planets of the solar system]]\n\n"
                     "At the center of our solar system is:"),
            "difficulty": 1,
            "choices": [("The Sun, which is a star", True),
                        ("Earth", False),
                        ("The Moon", False),
                        ("A black hole", False)],
            "explanation": r"The Sun, a star, sits at the center, and the planets orbit it. The trap, Earth, was the old (incorrect) belief. Pro tip: the planets, including Earth, revolve around the Sun.",
        },
        {
            "text": r"**Earth & Space.** Earthquakes most often occur when:",
            "difficulty": 2,
            "choices": [("Earth's tectonic plates move against one another", True),
                        ("It rains heavily for several days", False),
                        ("The Moon is full", False),
                        ("The Sun sets in the evening", False)],
            "explanation": r"Earthquakes happen as tectonic plates grind, push, or slip past each other. The traps (rain, Moon, sunset) are unrelated to plate motion. Pro tip: earthquakes and volcanoes cluster along the edges of moving plates.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the foundational (Level 1) full-length GED Science practice exam (34 questions; MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent re-seed
        course = Course.objects.create(
            title=COURSE["title"], slug=COURSE["slug"], program=COURSE["program"],
            subject=COURSE["subject"], description=COURSE["description"],
        )
        for i, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content.strip(), order=i)
        for q in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course, qtype="mcq", text=q["text"],
                difficulty=q["difficulty"], explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)
        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- {course.lessons.count()} lessons, "
            f"{course.questions.count()} questions (Life, Physical, Earth & Space)."
        ))
