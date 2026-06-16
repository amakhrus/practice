"""
Seed a SECOND full-length 'GED Science' practice exam -- Level 2, a harder
companion to ``seed_ged_science_exam``.

Same test-day structure (34 questions across Life, Physical, and Earth & Space
Science; 90 minutes; scored 100-200, 145 to pass), but the items are tougher:
relationships and mechanisms, graph and data interpretation, and experimental
reasoning. No 'easy' items -- everything is medium or hard.

Run:
    python manage.py seed_ged_science_exam_level2
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Full-Length Practice Exam (Level 2 - Advanced)",
    "slug": "ged-science-exam-level2",
    "program": "GED",
    "subject": "science",
    "description": (
        "A tougher, second full-length GED Science practice exam for students who have cleared Level 1. "
        "Same test-day format -- 34 questions across Life, Physical, and Earth & Space Science, 90 "
        "minutes, scored 100-200 (145 to pass) -- but every item is medium or hard. It pushes into the "
        "relationships and mechanisms the GED saves for harder questions: photosynthesis and respiration, "
        "genetics and natural selection, atoms and reactions, forces and energy transformations, and "
        "Earth's cycles, plus reading graphs and judging experiments. Every question includes a worked "
        "explanation and a pro tip, and many reuse the diagram library."
    ),
    "lessons": [
        (
            "1. Level 2: What's Harder",
            r"""
This is the **advanced** GED Science practice exam. The format matches the real test and Level 1:

- **34 questions** in **90 minutes**, across **Life Science**, **Physical Science**, and **Earth & Space Science**.
- Scored **100-200**, with **145 to pass**. No penalty for wrong answers.

**What's harder here than Level 1:** the questions move past single facts to **relationships and mechanisms** -- how photosynthesis and respiration connect, how natural selection works, how forces produce acceleration -- and they lean harder on **reading graphs and data** and on **experimental reasoning**.

[[check:Two variables rise together on a graph. Does that prove one caused the other? Answer yes or no.|no|Correlation is not causation -- a third factor could explain both.]]
            """,
        ),
        (
            "2. Mechanisms, Data, and Fair Tests",
            r"""
Harder science questions reward thinking about **how** and **why**, and reading evidence carefully.

- **Trace the process.** Know the inputs and outputs of photosynthesis and respiration, and how energy and matter move through a system.
- **Read every axis.** On a graph, check the title, the labels, the units, and the trend before you answer.
- **Independent vs. dependent variable.** The independent variable is what you change; the dependent variable is what you measure in response.
- **Conservation.** Atoms are rearranged but not created or destroyed; energy changes form but the total is conserved.

[[figure:photo_resp_link|Photosynthesis and cellular respiration are linked: the products of one are the reactants of the other.]]

[[check:In an experiment, what is the variable you deliberately change called?|independent variable;;the independent variable;;independent|The independent variable is the one you change on purpose.]]
            """,
        ),
        (
            "3. Strategy for Harder Items",
            r"""
- **Use the source first.** Most data questions are answered directly by the graph or table -- don't rely on memory when the evidence is in front of you.
- **Predict before you peek.** Decide what should happen, then find the matching choice.
- **Watch cause and effect.** Distinguish what causes a result from what merely happens alongside it.
- **Estimate.** A rough calculation catches a misread value or a decimal slip.
- **Never leave a blank.** Eliminate what you can, then choose.

[[check:On the GED Science test, where is the answer to most graph questions found?|in the graph;;the graph;;the source;;in the source|Read it directly from the graph or data source.]]
            """,
        ),
    ],
    "mcqs": [
        # ============================ LIFE SCIENCE ===========================
        {
            "text": r"**Life Science.** Besides oxygen, what is the main product that photosynthesis produces for the plant to use as food?",
            "difficulty": 2,
            "choices": [("Glucose (sugar)", True), ("Carbon dioxide", False),
                        ("Nitrogen", False), ("Salt", False)],
            "explanation": r"Photosynthesis combines carbon dioxide and water into glucose and oxygen. The trap, carbon dioxide, is a reactant the plant takes IN, not a product. Pro tip: plants build sugar (glucose) for energy and release oxygen.",
        },
        {
            "text": r"**Life Science.** During cellular respiration, cells release energy by breaking down glucose using which gas?",
            "difficulty": 3,
            "choices": [("Oxygen", True), ("Carbon dioxide", False),
                        ("Nitrogen", False), ("Hydrogen", False)],
            "explanation": r"Respiration uses oxygen to break down glucose, releasing energy and giving off carbon dioxide. The trap, carbon dioxide, is a product, not a reactant. Pro tip: respiration is roughly the reverse of photosynthesis.",
        },
        {
            "text": r"**Life Science.** When a body cell divides by mitosis, the two new cells are:",
            "difficulty": 2,
            "choices": [("Genetically identical to the original cell", True),
                        ("Each missing half of the DNA", False),
                        ("Always different species", False),
                        ("Unable to divide again", False)],
            "explanation": r"Mitosis copies the DNA first, so each new cell is an identical copy. The trap, missing half the DNA, describes meiosis (sex cells). Pro tip: mitosis = identical copies for growth and repair.",
        },
        {
            "text": r"**Life Science.** A pea plant with the genotype Bb (B is dominant) will show which trait?",
            "difficulty": 3,
            "choices": [("The dominant trait (B)", True),
                        ("The recessive trait (b)", False),
                        ("A blend of both traits", False),
                        ("No trait at all", False)],
            "explanation": r"With at least one dominant allele (B), the dominant trait appears. The trap, a blend, is not how simple dominance works. Pro tip: a single dominant allele is enough to mask the recessive one.",
        },
        {
            "text": ("**Life Science.** Use the diagram.\n\n"
                     "[[figure:natural_selection_cycle|The steps of natural selection]]\n\n"
                     "In natural selection, which individuals are MOST likely to pass on their traits?"),
            "difficulty": 3,
            "choices": [("Those best adapted to survive and reproduce in their environment", True),
                        ("The largest individuals, regardless of fitness", False),
                        ("Individuals chosen at random", False),
                        ("The oldest individuals in the group", False)],
            "explanation": r"Better-adapted individuals survive and reproduce more, passing on their helpful traits. The trap 'largest' isn't always the most fit. Pro tip: 'survival of the fittest' means best-suited to the environment, not strongest.",
        },
        {
            "text": ("**Life Science.** Use the food web.\n\n"
                     "[[figure:food_web|A food web with several connected species]]\n\n"
                     "If a disease wiped out most of the rabbits in a food web, the population of foxes "
                     "that eat them would most likely:"),
            "difficulty": 3,
            "choices": [("Decrease, because they lose a food source", True),
                        ("Increase rapidly", False),
                        ("Stay exactly the same", False),
                        ("Turn into producers", False)],
            "explanation": r"Fewer rabbits means less food for foxes, so the fox population would fall. The trap 'increase' ignores that predators depend on prey. Pro tip: in a food web, losing a prey species harms the predators above it.",
        },
        {
            "text": r"**Life Science.** When you get hot, you sweat to cool down; when you get cold, you shiver to warm up. These responses are examples of:",
            "difficulty": 3,
            "choices": [("Homeostasis -- keeping internal conditions stable", True),
                        ("Photosynthesis", False),
                        ("Natural selection", False),
                        ("Digestion", False)],
            "explanation": r"Homeostasis is the body's effort to keep a stable internal state, like a steady temperature. The trap, photosynthesis, occurs in plants, not human temperature control. Pro tip: homeostasis = staying balanced despite outside changes.",
        },
        {
            "text": ("**Life Science.** Use the graph.\n\n"
                     "[[figure:carrying_capacity_graph|A population leveling off at carrying capacity]]\n\n"
                     "When a population stops growing and levels off, it has most likely reached the "
                     "environment's:"),
            "difficulty": 3,
            "choices": [("Carrying capacity", True), ("Boiling point", False),
                        ("Atomic number", False), ("Half-life", False)],
            "explanation": r"Carrying capacity is the largest population the resources can support, where growth levels off. The traps are unrelated terms. Pro tip: limited food, space, and water cap how large a population can grow.",
        },
        {
            "text": r"**Life Science.** Molecules naturally move from an area of HIGH concentration to an area of LOW concentration in a process called:",
            "difficulty": 3,
            "choices": [("Diffusion", True), ("Combustion", False),
                        ("Condensation", False), ("Erosion", False)],
            "explanation": r"Diffusion spreads molecules from high to low concentration until they are even. The trap, combustion, is burning. Pro tip: diffusion is why a smell spreads across a room on its own.",
        },
        {
            "text": r"**Life Science.** Enzymes are special proteins in the body that mainly:",
            "difficulty": 3,
            "choices": [("Speed up chemical reactions", True),
                        ("Carry oxygen in the blood", False),
                        ("Store genetic information", False),
                        ("Build the cell wall", False)],
            "explanation": r"Enzymes are catalysts that speed up reactions, such as digestion. The trap, carrying oxygen, is the job of hemoglobin. Pro tip: enzymes lower the energy needed for a reaction, making it go faster.",
        },
        {
            "text": ("**Life Science.** Use the graph.\n\n"
                     "[[figure:predator_prey_graph|Predator and prey populations over time]]\n\n"
                     "In a predator-prey graph, a rise in the prey population is usually followed by:"),
            "difficulty": 3,
            "choices": [("A rise in the predator population", True),
                        ("The immediate extinction of both", False),
                        ("No change in predators ever", False),
                        ("Plants disappearing", False)],
            "explanation": r"More prey means more food for predators, so the predator population rises after the prey does. The trap 'extinction of both' ignores the cycle. Pro tip: predator and prey populations rise and fall in a lagging cycle.",
        },
        {
            "text": r"**Life Science.** A decomposer such as a fungus is important to an ecosystem mainly because it:",
            "difficulty": 2,
            "choices": [("Returns nutrients from dead organisms to the soil", True),
                        ("Produces all the oxygen in the air", False),
                        ("Hunts and eats large animals", False),
                        ("Blocks sunlight from plants", False)],
            "explanation": r"Decomposers recycle nutrients from dead matter back into the soil for plants. The trap, producing oxygen, is the role of plants. Pro tip: decomposers are nature's recyclers.",
        },
        {
            "text": r"**Life Science.** Which of these is an example of an INHERITED trait rather than a learned behavior?",
            "difficulty": 3,
            "choices": [("Eye color in humans", True),
                        ("Speaking a particular language", False),
                        ("Riding a bicycle", False),
                        ("A favorite food", False)],
            "explanation": r"Eye color is coded in DNA and inherited from parents. The traps (language, biking, food) are learned through experience. Pro tip: inherited traits are passed in the genes; learned behaviors come from the environment.",
        },
        # ========================== PHYSICAL SCIENCE =========================
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:atomic_number_mass|Atomic number and mass number of an atom]]\n\n"
                     "An atom's ATOMIC NUMBER is equal to its number of:"),
            "difficulty": 3,
            "choices": [("Protons", True), ("Protons plus neutrons", False),
                        ("Electrons plus neutrons", False), ("Neutrons only", False)],
            "explanation": r"The atomic number is the number of protons, which defines the element. The trap, protons plus neutrons, is the MASS number. Pro tip: atomic number = protons; mass number = protons + neutrons.",
        },
        {
            "text": r"**Physical Science.** Water (H₂O) is best classified as a:",
            "difficulty": 2,
            "choices": [("Compound", True), ("Pure element", False),
                        ("Mixture that can be filtered apart", False), ("Single atom", False)],
            "explanation": r"Water is a compound -- two elements (hydrogen and oxygen) chemically bonded. The trap, element, would be a single kind of atom. Pro tip: a compound has different elements bonded in fixed ratios.",
        },
        {
            "text": r"**Physical Science.** In the reaction 2H₂ + O₂ → 2H₂O, the number of hydrogen atoms on the left compared with the right is:",
            "difficulty": 3,
            "choices": [("Equal -- 4 on each side", True),
                        ("Greater on the left", False),
                        ("Greater on the right", False),
                        ("Zero on the right", False)],
            "explanation": r"2H₂ has 4 hydrogen atoms, and 2H₂O also has 4 -- they balance, as conservation of mass requires. The trap 'greater on the left' would mean atoms vanished. Pro tip: a balanced equation has equal atoms of each element on both sides.",
        },
        {
            "text": r"**Physical Science.** According to Newton's second law, if the same force is applied to a lighter object and a heavier object, the lighter object will have:",
            "difficulty": 3,
            "choices": [("Greater acceleration", True),
                        ("Less acceleration", False),
                        ("The same acceleration", False),
                        ("No acceleration", False)],
            "explanation": r"Since F = ma, for the same force a smaller mass gives a larger acceleration. The trap 'less acceleration' reverses the relationship. Pro tip: lighter objects accelerate more easily under the same push.",
        },
        {
            "text": r"**Physical Science.** Acceleration is best defined as the rate of change of an object's:",
            "difficulty": 3,
            "choices": [("Velocity (speed or direction)", True),
                        ("Mass", False),
                        ("Color", False),
                        ("Temperature", False)],
            "explanation": r"Acceleration is how quickly velocity changes -- speeding up, slowing down, or turning. The trap, mass, doesn't change during normal motion. Pro tip: any change in speed OR direction is acceleration.",
        },
        {
            "text": r"**Physical Science.** As you lift a book higher above the floor, its gravitational POTENTIAL energy:",
            "difficulty": 2,
            "choices": [("Increases", True), ("Decreases", False),
                        ("Stays the same", False), ("Becomes negative heat", False)],
            "explanation": r"The higher an object, the more gravitational potential energy it stores. The trap 'decreases' is the opposite. Pro tip: lifting an object stores energy that gravity can release if it falls.",
        },
        {
            "text": r"**Physical Science.** When a flashlight is turned on, the battery's stored CHEMICAL energy is converted mainly into:",
            "difficulty": 2,
            "choices": [("Electrical energy and then light", True),
                        ("Nuclear energy", False),
                        ("Sound energy only", False),
                        ("Gravitational energy", False)],
            "explanation": r"The battery's chemical energy becomes electrical energy, which the bulb turns into light. The trap, nuclear energy, isn't involved. Pro tip: trace energy step by step -- chemical to electrical to light.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:density_compare|Objects of different densities in water]]\n\n"
                     "An object placed in water will FLOAT if the object is:"),
            "difficulty": 3,
            "choices": [("Less dense than the water", True),
                        ("More dense than the water", False),
                        ("Heavier than one kilogram", False),
                        ("A different color than the water", False)],
            "explanation": r"An object floats when it is less dense than the fluid around it. The trap 'more dense' would sink. Pro tip: density, not weight alone, decides floating -- a huge ship floats because it is less dense overall.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:reaction_rate_factors|Factors that affect reaction rate]]\n\n"
                     "Raising the temperature usually makes a chemical reaction go:"),
            "difficulty": 3,
            "choices": [("Faster, because particles collide more often", True),
                        ("Slower, because particles freeze", False),
                        ("At exactly the same rate", False),
                        ("Backward every time", False)],
            "explanation": r"Higher temperature gives particles more energy, so they collide more often and react faster. The trap 'slower' reverses this. Pro tip: heat speeds reactions; cold (like a refrigerator) slows them, which is why it preserves food.",
        },
        {
            "text": r"**Physical Science.** In a simple circuit, why is the wire usually made of metal rather than plastic?",
            "difficulty": 2,
            "choices": [("Metal conducts electricity; plastic does not", True),
                        ("Plastic is a better conductor than metal", False),
                        ("Metal blocks all electricity", False),
                        ("The color of metal carries the current", False)],
            "explanation": r"Metals conduct electricity, letting current flow; plastic is an insulator. The trap reverses their roles. Pro tip: wires use metal to carry current and plastic coating to insulate it safely.",
        },
        {
            "text": r"**Physical Science.** Compared with a low-pitched sound, a high-pitched sound has a:",
            "difficulty": 3,
            "choices": [("Higher frequency", True), ("Lower frequency", False),
                        ("Larger mass", False), ("Slower speed in the same air", False)],
            "explanation": r"Pitch depends on frequency -- higher pitch means higher frequency. The trap 'lower frequency' is backwards. Pro tip: more waves per second = higher frequency = higher pitch.",
        },
        {
            "text": r"**Physical Science.** A solution with a pH of 3 is best described as:",
            "difficulty": 3,
            "choices": [("Acidic", True), ("Basic (alkaline)", False),
                        ("Neutral", False), ("A pure metal", False)],
            "explanation": r"A pH below 7 is acidic; a pH of 3 (like vinegar or lemon juice) is clearly acidic. The trap, basic, would be above 7. Pro tip: pH 7 is neutral, below 7 is acidic, above 7 is basic.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:reaction_types|Types of chemical reactions]]\n\n"
                     "A reaction that RELEASES heat to its surroundings is called:"),
            "difficulty": 3,
            "choices": [("Exothermic", True), ("Endothermic", False),
                        ("Photosynthetic", False), ("Magnetic", False)],
            "explanation": r"Exothermic reactions release heat (like burning). The trap, endothermic, absorbs heat instead. Pro tip: 'exo' = exit -- heat exits in an exothermic reaction.",
        },
        # ======================= EARTH & SPACE SCIENCE =======================
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:carbon_cycle|The carbon cycle]]\n\n"
                     "Burning fossil fuels (combustion) adds which gas to the atmosphere?"),
            "difficulty": 3,
            "choices": [("Carbon dioxide", True), ("Pure oxygen", False),
                        ("Helium", False), ("Nitrogen only", False)],
            "explanation": r"Combustion releases carbon dioxide into the air. The trap, pure oxygen, is consumed by burning, not released. Pro tip: burning carbon-based fuels puts CO2 back into the atmosphere.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:greenhouse_effect|How the greenhouse effect traps heat]]\n\n"
                     "Greenhouse gases such as carbon dioxide warm the planet because they:"),
            "difficulty": 3,
            "choices": [("Trap heat that would otherwise escape to space", True),
                        ("Block all sunlight from reaching Earth", False),
                        ("Cool the surface by reflecting heat away", False),
                        ("Produce oxygen for breathing", False)],
            "explanation": r"Greenhouse gases let sunlight in but trap the heat radiating back, warming Earth. The trap 'cool the surface' is the opposite. Pro tip: the greenhouse effect works like a blanket holding in warmth.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:weather_fronts|Warm and cold weather fronts]]\n\n"
                     "A fast-moving COLD front pushing under warm air often brings:"),
            "difficulty": 3,
            "choices": [("Storms and a quick drop in temperature", True),
                        ("Weeks of clear, dry skies", False),
                        ("A permanent rise in temperature", False),
                        ("No change in the weather", False)],
            "explanation": r"A cold front shoves warm air up quickly, often causing storms and cooler air behind it. The trap 'weeks of clear skies' ignores the storms. Pro tip: cold fronts bring sharp, short bursts of stormy weather.",
        },
        {
            "text": r"**Earth & Space.** When two continental tectonic plates push together (a convergent boundary), they often form:",
            "difficulty": 3,
            "choices": [("Mountain ranges", True), ("Deep ocean trenches with no land", False),
                        ("Flat deserts", False), ("New oceans that split apart", False)],
            "explanation": r"Continental plates colliding crumple the crust upward into mountains, like the Himalayas. The trap 'new oceans that split apart' describes a divergent boundary. Pro tip: convergent = coming together (mountains); divergent = moving apart.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:rock_cycle_detailed|The rock cycle in detail]]\n\n"
                     "Metamorphic rock forms when existing rock is changed by:"),
            "difficulty": 3,
            "choices": [("Intense heat and pressure", True),
                        ("Cooling from lava only", False),
                        ("Gentle rainfall", False),
                        ("Exposure to moonlight", False)],
            "explanation": r"Heat and pressure deep underground change rock into metamorphic rock (like marble from limestone). The trap, cooling lava, forms igneous rock. Pro tip: 'metamorphic' shares a root with 'metamorphosis' -- changed by heat and pressure.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:eclipses|Solar and lunar eclipses]]\n\n"
                     "A solar eclipse happens when:"),
            "difficulty": 3,
            "choices": [("The Moon passes between the Sun and Earth", True),
                        ("Earth passes between the Sun and the Moon", False),
                        ("The Sun passes between Earth and the Moon", False),
                        ("Clouds cover the Sun", False)],
            "explanation": r"In a solar eclipse, the Moon moves between the Sun and Earth, casting a shadow on Earth. The trap (Earth between Sun and Moon) is a LUNAR eclipse. Pro tip: SOLAR eclipse hides the Sun; the Moon is in the middle.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:atmosphere_layers|The layers of the atmosphere]]\n\n"
                     "Most of Earth's weather occurs in the lowest layer of the atmosphere, called the:"),
            "difficulty": 2,
            "choices": [("Troposphere", True), ("Stratosphere", False),
                        ("Mesosphere", False), ("Thermosphere", False)],
            "explanation": r"The troposphere is the lowest layer, where clouds and weather form. The trap, the stratosphere, holds the ozone layer above it. Pro tip: we live in the troposphere -- that's where weather happens.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:seismic_waves|Seismic waves traveling through Earth]]\n\n"
                     "Scientists learn about the layers deep inside Earth mainly by studying:"),
            "difficulty": 3,
            "choices": [("How seismic (earthquake) waves travel through the planet", True),
                        ("The color of surface rocks only", False),
                        ("Photographs of the core", False),
                        ("The phases of the Moon", False)],
            "explanation": r"Seismic waves change speed and direction as they pass through different layers, revealing Earth's interior. The trap, photographs of the core, is impossible -- no one can see it directly. Pro tip: earthquake waves act like an X-ray of Earth's inside.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the advanced (Level 2) full-length GED Science practice exam (34 questions; MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()
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
            f"{course.questions.count()} questions (all medium/hard)."
        ))
