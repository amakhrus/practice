"""
Seed a FOURTH full-length 'GED Science' practice exam -- Level 4, the mastery
tier. Same test-day structure (34 questions; 90 minutes; scored 100-200, 145 to
pass), but EVERY item is a hard, multi-layered problem: quantitative analysis,
energy conservation and circuits, evolution mechanisms, feedback systems, and
critiquing experiments and data.

Run:
    python manage.py seed_ged_science_exam_level4
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Full-Length Practice Exam (Level 4 - Mastery)",
    "slug": "ged-science-exam-level4",
    "program": "GED",
    "subject": "science",
    "description": (
        "The fourth and second-hardest full-length GED Science practice exam, for students aiming at a "
        "top score after clearing Levels 1-3. Same test-day format -- 34 questions across Life, Physical, "
        "and Earth & Space Science, 90 minutes, scored 100-200 (145 to pass) -- but every item is a hard, "
        "multi-layered problem: quantitative analysis, energy conservation and electric circuits, "
        "protein synthesis and inheritance ratios, evolution mechanisms, feedback systems, and critiquing "
        "experimental design and data. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 4: The Mastery Science Test",
            r"""
This is the **mastery** GED Science practice exam -- harder than Levels 1-3. The format is unchanged:

- **34 questions** in **90 minutes**, across **Life**, **Physical**, and **Earth & Space Science**; scored **100-200**, **145 to pass**.

**What makes Level 4 the hardest yet:** **every** question is a hard, layered item. You will run **calculations**, trace **energy conservation** through a system, predict **inheritance ratios**, follow **evolution mechanisms**, and judge whether an experiment's **data actually supports its conclusion**.

[[check:In a monohybrid cross of two Bb parents, what is the expected ratio of dominant to recessive phenotypes?|3:1;;3 to 1;;three to one|Bb x Bb gives a 3:1 dominant-to-recessive ratio.]]
            """,
        ),
        (
            "2. Synthesis, Calculation, and Evidence",
            r"""
Mastery science combines fields and demands precise reasoning.

- **Conservation laws.** Energy and matter are conserved; trace where they go (potential to kinetic, reactants to products).
- **Inheritance math.** Use Punnett squares and ratios to predict offspring outcomes.
- **Circuits and forces.** Apply V = IR and Newton's laws to predict behavior.
- **Evidence to conclusion.** A claim is only as strong as its control group, sample size, and the match between data and conclusion.

[[figure:photosynthesis_rate_graph|A rate often rises with one factor, then plateaus when a different factor becomes limiting.]]

[[check:If a graph of photosynthesis rate rises with light and then levels off, what is most likely happening at the plateau?|another factor is limiting;;a different factor limits it;;something else is limiting|Another factor (like CO2 or temperature) has become the limiting factor.]]
            """,
        ),
        (
            "3. Strategy for Mastery Items",
            r"""
- **Write the formula and units.** Every calculation should show the setup, not just an answer.
- **Trace the system.** Follow energy or matter step by step; the total is conserved.
- **Predict the ratio or trend, then match.** Decide the outcome before scanning choices.
- **Test the conclusion against the data.** Does the evidence actually support the claim, or just correlate?
- **Estimate to catch slips.** A rough check exposes a misplaced decimal or a wrong unit.

[[check:To conclude that a drug works, a study must compare the treated group with what?|a control group;;a control;;an untreated control group|Compare against a control group that did not get the drug.]]
            """,
        ),
    ],
    "mcqs": [
        # ============================ LIFE SCIENCE ===========================
        {
            "text": r"**Life Science.** During protein synthesis, the process of copying a gene's code from DNA into messenger RNA is called:",
            "difficulty": 3,
            "choices": [("Transcription", True), ("Translation", False),
                        ("Digestion", False), ("Respiration", False)],
            "explanation": r"Transcription copies DNA into mRNA; translation then builds the protein from the mRNA. The trap, translation, is the second step. Pro tip: transcribe = rewrite (DNA to RNA); translate = change languages (RNA to protein).",
        },
        {
            "text": r"**Life Science.** Two heterozygous (Bb) parents are crossed. What ratio of dominant to recessive phenotypes is expected in their offspring?",
            "difficulty": 3,
            "choices": [("3 dominant : 1 recessive", True), ("1 : 1", False),
                        ("All dominant", False), ("All recessive", False)],
            "explanation": r"Bb x Bb yields BB, Bb, Bb, bb -- three showing the dominant trait to one recessive. The trap '1:1' is a test cross (Bb x bb). Pro tip: a monohybrid cross of two heterozygotes gives the classic 3:1 ratio.",
        },
        {
            "text": r"**Life Science.** To find out whether a plant showing the dominant trait is BB or Bb, a scientist crosses it with a homozygous recessive (bb) plant. This is called a:",
            "difficulty": 3,
            "choices": [("Test cross", True), ("Mutation", False),
                        ("Mitosis", False), ("Vaccination", False)],
            "explanation": r"A test cross with bb reveals the unknown genotype: any recessive offspring means the parent was Bb. The trap, mutation, is a DNA change. Pro tip: crossing with a recessive 'unmasks' a hidden allele.",
        },
        {
            "text": ("**Life Science.** Use the graph.\n\n"
                     "[[figure:photosynthesis_rate_graph|Photosynthesis rate rising with light, then leveling off]]\n\n"
                     "When the photosynthesis rate stops rising even as light increases, the BEST "
                     "explanation is that:"),
            "difficulty": 3,
            "choices": [("Another factor, such as CO₂ or temperature, has become limiting", True),
                        ("Light has stopped reaching the plant", False),
                        ("The plant has died", False),
                        ("Photosynthesis has reversed direction", False)],
            "explanation": r"Once light is plentiful, a different factor caps the rate, so it plateaus. The trap 'light has stopped' contradicts the rising light. Pro tip: a plateau means some OTHER factor is now the bottleneck.",
        },
        {
            "text": ("**Life Science.** Use the diagram.\n\n"
                     "[[figure:dna_gene_chromosome|The relationship among DNA, genes, and chromosomes]]\n\n"
                     "Which sequence correctly orders these from smallest to largest?"),
            "difficulty": 3,
            "choices": [("Gene → chromosome → cell nucleus", True),
                        ("Chromosome → gene → DNA base", False),
                        ("Nucleus → gene → chromosome", False),
                        ("Cell → gene → chromosome", False)],
            "explanation": r"A gene is a segment of DNA; many genes make up a chromosome, which sits in the nucleus. The trap reverses the order. Pro tip: gene (small) -> chromosome (a long DNA molecule) -> nucleus (holds them all).",
        },
        {
            "text": r"**Life Science.** Aerobic cellular respiration releases far more energy than anaerobic respiration (fermentation) because it:",
            "difficulty": 3,
            "choices": [("Uses oxygen to fully break down glucose", True),
                        ("Does not use any glucose", False),
                        ("Happens only in plants", False),
                        ("Produces no carbon dioxide", False)],
            "explanation": r"With oxygen, glucose is broken down completely, releasing much more energy (ATP). The trap 'does not use glucose' is false -- glucose is the fuel. Pro tip: oxygen lets cells extract far more energy from each glucose molecule.",
        },
        {
            "text": r"**Life Science.** Homologous structures, such as the similar bone patterns in a human arm, a whale flipper, and a bat wing, are strong evidence for:",
            "difficulty": 3,
            "choices": [("Common ancestry through evolution", True),
                        ("The animals being the same species", False),
                        ("These animals never changing over time", False),
                        ("A lack of any relationship", False)],
            "explanation": r"Shared underlying structures point to a common ancestor whose limb was modified over time. The trap 'same species' is false -- they are clearly different. Pro tip: homologous structures show descent with modification from a shared ancestor.",
        },
        {
            "text": r"**Life Science.** After a fire clears a forest, the first organisms to colonize the bare ground, such as lichens and mosses, are called:",
            "difficulty": 3,
            "choices": [("Pioneer species", True), ("Apex predators", False),
                        ("Decomposers only", False), ("Keystone species", False)],
            "explanation": r"Pioneer species are the first to colonize and begin ecological succession. The trap, apex predators, arrive much later. Pro tip: pioneers like lichens prepare the soil for larger plants to follow.",
        },
        {
            "text": ("**Life Science.** A study claims a vitamin boosts memory. Which design would BEST support that "
                     "conclusion?"),
            "difficulty": 3,
            "choices": [("A large group taking the vitamin compared with a similar group taking a placebo", True),
                        ("One person who takes the vitamin and reports feeling smarter", False),
                        ("A survey asking people if they like vitamins", False),
                        ("Measuring memory in only the vitamin group", False)],
            "explanation": r"A large treated group compared with a placebo control isolates the vitamin's effect. The trap, one person reporting, is anecdotal and uncontrolled. Pro tip: strong evidence needs a control group and a large sample.",
        },
        {
            "text": r"**Life Science.** A population of beetles lives on a tree with light and dark bark. Over years, birds eat the beetles that stand out, and the population shifts toward one color. This is an example of:",
            "difficulty": 3,
            "choices": [("Natural selection acting on variation", True),
                        ("Beetles choosing their own color", False),
                        ("A learned behavior passed to offspring", False),
                        ("Photosynthesis in the beetles", False)],
            "explanation": r"Predators remove the more visible beetles, so camouflaged ones survive and reproduce -- natural selection. The trap 'choosing their color' misunderstands selection. Pro tip: selection acts on existing variation; the environment does the 'choosing.'",
        },
        {
            "text": r"**Life Science.** In humans, the pancreas releases insulin when blood sugar is high and glucagon when it is low. Together these keep blood sugar stable, an example of:",
            "difficulty": 3,
            "choices": [("Homeostasis through negative feedback", True),
                        ("Photosynthesis", False),
                        ("Natural selection", False),
                        ("Mitosis", False)],
            "explanation": r"Opposing hormones push blood sugar back toward a set point -- negative feedback maintaining homeostasis. The trap, photosynthesis, is unrelated. Pro tip: two opposing controls (insulin/glucagon) keep a value balanced.",
        },
        {
            "text": r"**Life Science.** Which of the following provides the most direct evidence that two organisms are closely related?",
            "difficulty": 3,
            "choices": [("Very similar DNA sequences", True),
                        ("Living in the same country", False),
                        ("Being roughly the same size", False),
                        ("Having the same color", False)],
            "explanation": r"The more alike two organisms' DNA, the more recently they shared an ancestor. The traps (location, size, color) can be coincidental. Pro tip: DNA similarity is the strongest modern evidence of relatedness.",
        },
        {
            "text": r"**Life Science.** A mutation in a body (skin) cell, rather than a sex cell, will:",
            "difficulty": 3,
            "choices": [("Not be passed to the organism's offspring", True),
                        ("Always be passed to every offspring", False),
                        ("Change the DNA of every cell at once", False),
                        ("Instantly create a new species", False)],
            "explanation": r"Only mutations in sex cells (eggs/sperm) can be inherited; a skin-cell mutation stays with that individual. The trap 'always passed' confuses body cells with sex cells. Pro tip: only gamete mutations reach the next generation.",
        },
        # ========================== PHYSICAL SCIENCE =========================
        {
            "text": r"**Physical Science.** A 2 kg ball moves at 3 m/s. What is its momentum (mass × velocity)?",
            "difficulty": 3,
            "choices": [("6 kg·m/s", True), ("1.5 kg·m/s", False),
                        ("5 kg·m/s", False), ("9 kg·m/s", False)],
            "explanation": r"Momentum = mass x velocity = 2 x 3 = 6 kg·m/s. The trap 1.5 divides instead of multiplying. Pro tip: momentum combines how much mass is moving with how fast.",
        },
        {
            "text": r"**Physical Science.** As a swinging pendulum rises to the top of its swing, its energy is mostly:",
            "difficulty": 3,
            "choices": [("Gravitational potential energy", True),
                        ("Kinetic energy", False),
                        ("Chemical energy", False),
                        ("Nuclear energy", False)],
            "explanation": r"At the top it momentarily stops, so kinetic energy is lowest and potential energy is highest. The trap, kinetic, peaks at the BOTTOM of the swing. Pro tip: energy trades back and forth -- high and slow = potential; low and fast = kinetic.",
        },
        {
            "text": r"**Physical Science.** In a circuit, if the voltage stays the same but the resistance increases, the current will (V = IR):",
            "difficulty": 3,
            "choices": [("Decrease", True), ("Increase", False),
                        ("Stay exactly the same", False), ("Become negative", False)],
            "explanation": r"From V = IR, current I = V/R, so more resistance means less current at constant voltage. The trap 'increase' reverses the relationship. Pro tip: resistance fights current -- more resistance, less flow.",
        },
        {
            "text": r"**Physical Science.** In a SERIES circuit with two bulbs, if one bulb burns out, the other bulb will:",
            "difficulty": 3,
            "choices": [("Also go out, because the circuit is broken", True),
                        ("Stay lit and grow brighter", False),
                        ("Stay lit at the same brightness", False),
                        ("Turn into a parallel circuit", False)],
            "explanation": r"A series circuit is a single loop, so one break stops all current. The trap 'stay lit' describes a parallel circuit. Pro tip: series = one path (one fails, all fail); parallel = separate paths (others keep working).",
        },
        {
            "text": r"**Physical Science.** Water resists changing temperature more than most substances. This property, called high specific heat, helps explain why:",
            "difficulty": 3,
            "choices": [("Coastal areas have milder temperatures than inland deserts", True),
                        ("Metal heats up slowly in the sun", False),
                        ("Ice is denser than liquid water", False),
                        ("Oil and water do not mix", False)],
            "explanation": r"Water's high specific heat lets oceans absorb and release heat slowly, moderating nearby climates. The trap about metal is the opposite (metal heats quickly). Pro tip: high specific heat means a substance stores a lot of heat with little temperature change.",
        },
        {
            "text": r"**Physical Science.** A catalyst speeds up a chemical reaction by:",
            "difficulty": 3,
            "choices": [("Lowering the activation energy needed to react", True),
                        ("Being used up as a reactant", False),
                        ("Adding mass to the products", False),
                        ("Raising the activation energy", False)],
            "explanation": r"A catalyst lowers the energy barrier, so the reaction proceeds faster, and it is not consumed. The trap 'used up as a reactant' is false -- catalysts are reused. Pro tip: enzymes are biological catalysts that lower activation energy.",
        },
        {
            "text": r"**Physical Science.** Two atoms are isotopes of the same element. They have the same number of protons but a different number of:",
            "difficulty": 3,
            "choices": [("Neutrons", True), ("Protons", False),
                        ("Nuclei", False), ("Elements", False)],
            "explanation": r"Isotopes share the proton count (same element) but differ in neutrons, giving different mass numbers. The trap, protons, would make them different elements. Pro tip: same protons, different neutrons = isotopes.",
        },
        {
            "text": r"**Physical Science.** Which type of electromagnetic wave carries the MOST energy?",
            "difficulty": 3,
            "choices": [("Gamma rays", True), ("Radio waves", False),
                        ("Microwaves", False), ("Visible light", False)],
            "explanation": r"Gamma rays have the highest frequency and the most energy in the spectrum. The trap, radio waves, has the lowest energy. Pro tip: energy rises from radio to gamma -- higher frequency, more energy.",
        },
        {
            "text": r"**Physical Science.** A radioactive isotope has a half-life of 10 years. After 20 years, the fraction of the original sample remaining is:",
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{1}{2}\)", False),
                        (r"0", False), (r"\(\frac{1}{20}\)", False)],
            "explanation": r"20 years is two half-lives: 1 -> 1/2 -> 1/4. The trap 1/2 counts only one half-life. Pro tip: each half-life halves the amount, so two half-lives leave one quarter.",
        },
        {
            "text": r"**Physical Science.** An object floats in water because the upward buoyant force on it equals the:",
            "difficulty": 3,
            "choices": [("Weight of the water it displaces", True),
                        ("Color of the object", False),
                        ("Temperature of the air", False),
                        ("Length of the object only", False)],
            "explanation": r"By Archimedes' principle, the buoyant force equals the weight of displaced fluid; if that matches the object's weight, it floats. The trap, color, is irrelevant. Pro tip: displace enough water and the upward push can support the object.",
        },
        {
            "text": r"**Physical Science.** A ball is thrown straight up. As it rises, its kinetic energy converts mostly into:",
            "difficulty": 3,
            "choices": [("Gravitational potential energy", True),
                        ("Chemical energy", False),
                        ("Sound energy", False),
                        ("Nuclear energy", False)],
            "explanation": r"As the ball rises and slows, kinetic energy becomes potential energy, which returns to kinetic on the way down. The trap, chemical energy, isn't involved. Pro tip: energy is conserved -- it changes form but isn't lost.",
        },
        {
            "text": r"**Physical Science.** When iron rusts, it gains mass as it combines with oxygen from the air. This does NOT violate conservation of mass because:",
            "difficulty": 3,
            "choices": [("The oxygen's mass is added from the surroundings", True),
                        ("Mass is created out of nothing", False),
                        ("Rust has no mass", False),
                        ("Iron loses electrons that weigh a lot", False)],
            "explanation": r"The added mass comes from oxygen atoms joining the iron, so total mass (iron + oxygen) is conserved. The trap 'created out of nothing' violates the law. Pro tip: count everything, including gases from the air, and mass always balances.",
        },
        {
            "text": r"**Physical Science.** A 1,000 kg car going 20 m/s must stop. Compared with stopping from 10 m/s, stopping from 20 m/s requires the car to lose:",
            "difficulty": 3,
            "choices": [("Much more kinetic energy", True),
                        ("Less kinetic energy", False),
                        ("Exactly the same kinetic energy", False),
                        ("No energy at all", False)],
            "explanation": r"Kinetic energy depends on the square of speed, so doubling the speed quadruples the energy to remove. The trap 'same energy' ignores the speed difference. Pro tip: faster objects carry disproportionately more kinetic energy -- and need more braking.",
        },
        # ======================= EARTH & SPACE SCIENCE =======================
        {
            "text": r"**Earth & Space.** Scientists determine the absolute age of very old rocks by measuring the decay of radioactive isotopes, a method that relies on each isotope's known:",
            "difficulty": 3,
            "choices": [("Half-life", True), ("Color", False),
                        ("Hardness", False), ("Magnetic north", False)],
            "explanation": r"Radiometric dating compares parent and daughter isotopes using the known half-life. The trap, color, tells nothing about age. Pro tip: a steady half-life acts like a built-in clock inside the rock.",
        },
        {
            "text": r"**Earth & Space.** At a transform plate boundary, such as a strike-slip fault, the plates:",
            "difficulty": 3,
            "choices": [("Slide horizontally past each other, causing earthquakes", True),
                        ("Collide to build tall mountains", False),
                        ("Pull apart to form new crust", False),
                        ("Stack on top of one another permanently", False)],
            "explanation": r"Transform boundaries grind side by side, building stress that releases as earthquakes. The trap 'collide to build mountains' is a convergent boundary. Pro tip: transform = sliding past; convergent = colliding; divergent = spreading apart.",
        },
        {
            "text": r"**Earth & Space.** As Arctic ice melts, darker ocean water is exposed, which absorbs more sunlight and causes further warming. This is an example of:",
            "difficulty": 3,
            "choices": [("A positive feedback loop", True),
                        ("A negative feedback loop", False),
                        ("Conduction", False),
                        ("Conservation of mass", False)],
            "explanation": r"The warming causes more melting, which causes more warming -- a self-amplifying positive feedback. The trap, negative feedback, would dampen the change instead. Pro tip: positive feedback amplifies; negative feedback stabilizes.",
        },
        {
            "text": r"**Earth & Space.** Ocean tides on Earth are caused mainly by the gravitational pull of the:",
            "difficulty": 3,
            "choices": [("Moon", True), ("North Pole", False),
                        ("clouds", False), ("ocean currents", False)],
            "explanation": r"The Moon's gravity (with a smaller pull from the Sun) raises the tides. The trap, the North Pole, exerts no special pull. Pro tip: the Moon's gravity tugs the oceans, creating high and low tides.",
        },
        {
            "text": r"**Earth & Space.** As the oceans absorb more carbon dioxide from the atmosphere, the seawater becomes:",
            "difficulty": 3,
            "choices": [("More acidic (lower pH)", True),
                        ("More basic (higher pH)", False),
                        ("Completely fresh water", False),
                        ("Warmer but unchanged in pH", False)],
            "explanation": r"Dissolved CO₂ forms carbonic acid, lowering the ocean's pH -- ocean acidification. The trap 'more basic' is the opposite. Pro tip: more CO₂ in seawater means more acid and a lower pH, which harms shells and coral.",
        },
        {
            "text": r"**Earth & Space.** Our Sun is expected to eventually run low on hydrogen fuel and expand into a:",
            "difficulty": 3,
            "choices": [("Red giant", True), ("Black hole", False),
                        ("Brand-new planet", False), ("Comet", False)],
            "explanation": r"A medium star like the Sun swells into a red giant late in life, then becomes a white dwarf. The trap, black hole, forms only from much more massive stars. Pro tip: the Sun isn't massive enough to become a black hole.",
        },
        {
            "text": r"**Earth & Space.** Geologists use 'index fossils' -- species that were widespread but existed only briefly -- to:",
            "difficulty": 3,
            "choices": [("Estimate the age of the rock layers that contain them", True),
                        ("Measure the temperature of magma", False),
                        ("Predict tomorrow's weather", False),
                        ("Locate underground water", False)],
            "explanation": r"Because an index fossil marks a narrow span of time, finding it dates the surrounding rock. The trap, predicting weather, is unrelated. Pro tip: a good index fossil is common, widespread, and short-lived.",
        },
        {
            "text": r"**Earth & Space.** Earth's seasons are caused by its tilted axis, which means that during a hemisphere's summer, that hemisphere:",
            "difficulty": 3,
            "choices": [("Is tilted toward the Sun, receiving more direct sunlight", True),
                        ("Is much closer to the Sun than in winter", False),
                        ("Receives no sunlight at all", False),
                        ("Stops rotating for several weeks", False)],
            "explanation": r"In summer a hemisphere leans toward the Sun, so sunlight strikes more directly and days are longer. The trap 'closer to the Sun' is the common distance misconception. Pro tip: it's the angle of sunlight from the tilt, not distance, that makes seasons.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the mastery (Level 4) full-length GED Science practice exam (34 questions; MCQ only)."

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
            f"{course.questions.count()} questions (all hard)."
        ))
