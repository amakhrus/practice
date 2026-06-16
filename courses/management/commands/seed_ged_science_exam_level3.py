"""
Seed a THIRD full-length 'GED Science' practice exam -- Level 3, the expert tier.

Same test-day structure (34 questions across Life, Physical, and Earth & Space
Science; 90 minutes; scored 100-200, 145 to pass), but the items reach the top of
the GED's range: multi-step reasoning, quantitative data, feedback mechanisms,
and critiquing experiments and conclusions.

Run:
    python manage.py seed_ged_science_exam_level3
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Full-Length Practice Exam (Level 3 - Expert)",
    "slug": "ged-science-exam-level3",
    "program": "GED",
    "subject": "science",
    "description": (
        "The hardest of the early-tier GED Science practice exams, for students who have cleared Levels 1 "
        "and 2. Same test-day format -- 34 questions across Life, Physical, and Earth & Space Science, 90 "
        "minutes, scored 100-200 (145 to pass) -- but the items sit at the top of the range: multi-step "
        "reasoning, quantitative data and calculations, negative-feedback mechanisms, and critiquing "
        "experimental design and conclusions. Every question includes a worked explanation and a pro tip, "
        "and many reuse the diagram library."
    ),
    "lessons": [
        (
            "1. Level 3: The Expert Science Test",
            r"""
This is the **expert** GED Science practice exam. The format is unchanged:

- **34 questions** in **90 minutes**, across **Life**, **Physical**, and **Earth & Space Science**.
- Scored **100-200**, with **145 to pass**.

**What makes Level 3 harder:** the questions demand **multi-step reasoning** and **quantitative work** -- calculating speed, energy, or density; tracing **feedback loops** like blood-sugar control; and **critiquing experiments** for sample size, controls, and valid conclusions. Reading data closely matters more than ever.

[[check:If a study tested only 3 plants, what is the biggest weakness of its conclusion?|small sample size;;the sample size;;too few samples;;small sample|A tiny sample makes the results unreliable.]]
            """,
        ),
        (
            "2. Quantitative Reasoning & Feedback",
            r"""
Expert science blends biology, chemistry, and physics with numbers and systems.

- **Calculate from formulas.** Speed = distance / time; work = force x distance; density = mass / volume; acceleration = change in velocity / time.
- **Energy through trophic levels.** Only about 10% of energy passes up each level of a food chain.
- **Negative feedback.** The body senses a change and acts to reverse it -- as insulin lowers high blood sugar.
- **Evaluate the evidence.** A valid conclusion needs a control group, enough samples, and only one changed variable.

[[figure:blood_glucose_graph|Negative feedback keeps blood glucose within a stable range.]]

[[check:When insulin lowers blood sugar after a meal, returning it toward normal, what kind of control is that?|negative feedback;;feedback;;negative-feedback loop|It is negative feedback -- the body reverses a change to restore balance.]]
            """,
        ),
        (
            "3. Strategy for the Hardest Items",
            r"""
- **Show the calculation.** Write the formula, plug in the numbers, and check the units.
- **Predict the trend.** On a graph, decide what should happen before reading the answer choices.
- **Separate cause from coincidence.** A correlation needs a controlled experiment before you can claim causation.
- **Judge the design.** Ask whether the study had a control group, a large enough sample, and only one variable changed.
- **Estimate to catch errors.** A rough check flags a misplaced decimal.

[[check:To claim that one thing CAUSES another, an experiment must change how many variables at a time?|one;;1;;only one|Change only one variable so you can attribute the effect to it.]]
            """,
        ),
    ],
    "mcqs": [
        # ============================ LIFE SCIENCE ===========================
        {
            "text": r"**Life Science.** The genetic instructions in DNA are used to build the body's:",
            "difficulty": 3,
            "choices": [("Proteins", True), ("Minerals", False),
                        ("Water molecules", False), ("Sunlight", False)],
            "explanation": r"DNA's code is read to assemble proteins, which build and run the body. The trap, minerals, are not coded by DNA. Pro tip: DNA -> RNA -> protein is the flow of genetic information.",
        },
        {
            "text": r"**Life Science.** Unlike mitosis, the cell division called meiosis produces sex cells (gametes) that have:",
            "difficulty": 3,
            "choices": [("Half the number of chromosomes", True),
                        ("Twice the number of chromosomes", False),
                        ("The exact same DNA as body cells", False),
                        ("No DNA at all", False)],
            "explanation": r"Meiosis halves the chromosome number so that fertilization restores the full set. The trap 'twice' would double chromosomes each generation. Pro tip: meiosis makes gametes with half the DNA; fertilization recombines them.",
        },
        {
            "text": ("**Life Science.** Use the diagram.\n\n"
                     "[[figure:antibiotic_resistance|How antibiotic resistance spreads]]\n\n"
                     "Bacteria become resistant to an antibiotic over time mainly because:"),
            "difficulty": 3,
            "choices": [("Resistant bacteria survive and reproduce, passing on the trait", True),
                        ("Each bacterium chooses to become resistant", False),
                        ("Antibiotics create brand-new species", False),
                        ("Resistance has nothing to do with survival", False)],
            "explanation": r"The antibiotic kills non-resistant bacteria, leaving resistant ones to multiply -- natural selection. The trap 'chooses to become resistant' misunderstands how selection works. Pro tip: the environment selects existing variation; organisms don't choose to mutate.",
        },
        {
            "text": r"**Life Science.** A food chain starts with 10,000 units of energy in the plants. About how much energy is available to the second-level consumers (the animals that eat the herbivores)?",
            "difficulty": 3,
            "choices": [("About 100 units", True), ("About 9,000 units", False),
                        ("About 10,000 units", False), ("About 1 million units", False)],
            "explanation": r"Only ~10% passes up each level: 10,000 -> 1,000 (herbivores) -> 100 (second-level consumers). The trap 9,000 forgets the loss at each step. Pro tip: multiply by 0.1 for each step up the chain.",
        },
        {
            "text": ("**Life Science.** Use the graph.\n\n"
                     "[[figure:blood_glucose_graph|Blood glucose rising after a meal, then returning to normal]]\n\n"
                     "After a meal raises blood sugar, the hormone insulin lowers it back toward normal. "
                     "This is an example of:"),
            "difficulty": 3,
            "choices": [("Negative feedback maintaining homeostasis", True),
                        ("Photosynthesis", False),
                        ("Natural selection", False),
                        ("A chemical reaction creating new elements", False)],
            "explanation": r"The body senses high sugar and reverses it with insulin -- negative feedback keeping conditions stable. The trap, photosynthesis, is a plant process. Pro tip: negative feedback pushes a value back toward its set point.",
        },
        {
            "text": r"**Life Science.** Water moves across a cell membrane from a region of higher water concentration to lower water concentration. This specific type of diffusion is called:",
            "difficulty": 3,
            "choices": [("Osmosis", True), ("Combustion", False),
                        ("Respiration", False), ("Mitosis", False)],
            "explanation": r"Osmosis is the diffusion of water across a membrane. The trap, respiration, releases energy from glucose. Pro tip: osmosis is specifically the movement of WATER.",
        },
        {
            "text": r"**Life Science.** Most of a cell's energy (ATP) is produced in the:",
            "difficulty": 2,
            "choices": [("Mitochondria", True), ("Nucleus", False),
                        ("Cell wall", False), ("Ribosome", False)],
            "explanation": r"Mitochondria carry out cellular respiration, producing most of the cell's ATP. The trap, the nucleus, stores DNA. Pro tip: mitochondria are the cell's energy factories.",
        },
        {
            "text": r"**Life Science.** An invasive species introduced to a new ecosystem with no natural predators is MOST likely to:",
            "difficulty": 3,
            "choices": [("Grow rapidly and outcompete native species", True),
                        ("Quickly die out from loneliness", False),
                        ("Have no effect on the ecosystem", False),
                        ("Turn into a native species within a week", False)],
            "explanation": r"Without predators or competition, an invasive species often booms and crowds out natives. The trap 'no effect' ignores the disruption invasives cause. Pro tip: missing predators remove the natural check on a population.",
        },
        {
            "text": r"**Life Science.** A change in the DNA sequence of a gene is called a:",
            "difficulty": 2,
            "choices": [("Mutation", True), ("Digestion", False),
                        ("Condensation", False), ("Reflex", False)],
            "explanation": r"A mutation is a change in the DNA code, which can be harmful, helpful, or neutral. The trap, digestion, breaks down food. Pro tip: mutations are the raw source of new genetic variation.",
        },
        {
            "text": ("**Life Science.** A student concludes that a new plant food works because the ONE plant given it "
                     "grew taller than the ONE plant without it. The biggest flaw in this experiment is:"),
            "difficulty": 3,
            "choices": [("The sample size is far too small to be reliable", True),
                        ("The plants were watered at all", False),
                        ("Plants should never be measured", False),
                        ("Sunlight has no effect on plants", False)],
            "explanation": r"With only one plant per group, the result could be chance, not the plant food. The trap 'watered at all' isn't a flaw. Pro tip: reliable experiments need many samples, not just one in each group.",
        },
        {
            "text": ("**Life Science.** Use the diagram.\n\n"
                     "[[figure:disease_transmission|How an infectious disease spreads]]\n\n"
                     "Washing hands and covering coughs slow the spread of many illnesses because they:"),
            "difficulty": 3,
            "choices": [("Reduce the transfer of germs from person to person", True),
                        ("Cure the disease instantly in everyone", False),
                        ("Make the germs reproduce faster", False),
                        ("Change a person's DNA", False)],
            "explanation": r"These habits cut down how germs pass between people, lowering transmission. The trap 'cure instantly' overstates it -- prevention is not a cure. Pro tip: blocking transmission protects others even before anyone is treated.",
        },
        {
            "text": r"**Life Science.** Which factor would most directly LIMIT the growth of a deer population in a forest?",
            "difficulty": 3,
            "choices": [("A shortage of available food", True),
                        ("An increase in available food", False),
                        ("Fewer predators in the area", False),
                        ("A milder, easier winter", False)],
            "explanation": r"Limited food caps how many deer the forest can support. The traps (more food, fewer predators, mild winter) would let the population GROW, not shrink. Pro tip: limiting factors are scarcities -- food, water, space -- that hold a population down.",
        },
        {
            "text": r"**Life Science.** In photosynthesis, plants capture energy from sunlight using a green pigment called:",
            "difficulty": 2,
            "choices": [("Chlorophyll", True), ("Hemoglobin", False),
                        ("Keratin", False), ("Insulin", False)],
            "explanation": r"Chlorophyll absorbs sunlight to power photosynthesis and gives plants their green color. The trap, hemoglobin, carries oxygen in blood. Pro tip: chlorophyll = the green light-catcher in leaves.",
        },
        # ========================== PHYSICAL SCIENCE =========================
        {
            "text": r"**Physical Science.** A car speeds up from 0 to 20 m/s in 4 seconds. What is its acceleration?",
            "difficulty": 3,
            "choices": [("5 m/s²", True), ("80 m/s²", False),
                        ("24 m/s²", False), ("16 m/s²", False)],
            "explanation": r"Acceleration = change in velocity / time = (20 - 0) / 4 = 5 m/s². The trap 80 multiplies instead of dividing. Pro tip: acceleration is how much the speed changes each second.",
        },
        {
            "text": r"**Physical Science.** How much work is done when a force of 10 newtons pushes a box 3 meters in the direction of the force?",
            "difficulty": 3,
            "choices": [("30 joules", True), ("13 joules", False),
                        ("3.3 joules", False), ("0 joules", False)],
            "explanation": r"Work = force x distance = 10 x 3 = 30 joules. The trap 13 adds instead of multiplying. Pro tip: work multiplies the force by the distance moved in that direction.",
        },
        {
            "text": r"**Physical Science.** A block has a mass of 60 grams and a volume of 20 cm³. What is its density?",
            "difficulty": 3,
            "choices": [("3 g/cm³", True), ("1,200 g/cm³", False),
                        ("0.33 g/cm³", False), ("40 g/cm³", False)],
            "explanation": r"Density = mass / volume = 60 / 20 = 3 g/cm³. The trap 1,200 multiplies instead of dividing. Pro tip: density tells you how much mass is packed into each unit of volume.",
        },
        {
            "text": r"**Physical Science.** According to Newton's third law, when you push on a wall, the wall:",
            "difficulty": 3,
            "choices": [("Pushes back on you with equal force", True),
                        ("Does not push back at all", False),
                        ("Pushes back with a much greater force", False),
                        ("Pulls you toward it", False)],
            "explanation": r"For every action there is an equal and opposite reaction, so the wall pushes back equally. The trap 'does not push back' violates the law. Pro tip: forces always come in equal, opposite pairs.",
        },
        {
            "text": r"**Physical Science.** The kinetic energy of a moving object increases when the object's:",
            "difficulty": 3,
            "choices": [("Speed increases", True), ("Color changes", False),
                        ("Temperature is recorded", False), ("Name is changed", False)],
            "explanation": r"Kinetic energy grows with mass and especially with speed. The trap, color, has no effect on kinetic energy. Pro tip: a faster object carries more kinetic energy -- speed matters most.",
        },
        {
            "text": ("**Physical Science.** Use the diagram.\n\n"
                     "[[figure:bohr_models|Bohr models showing electrons in shells]]\n\n"
                     "In a Bohr model of an atom, the electrons are found:"),
            "difficulty": 2,
            "choices": [("Orbiting the nucleus in shells", True),
                        ("Packed inside the nucleus", False),
                        ("Spread evenly through empty space only", False),
                        ("Attached to neutrons in the center", False)],
            "explanation": r"In the Bohr model, electrons orbit the nucleus in energy levels (shells). The trap 'inside the nucleus' describes protons and neutrons. Pro tip: the nucleus is the center; electrons circle it in shells.",
        },
        {
            "text": r"**Physical Science.** Powdered sugar dissolves faster than a sugar cube because the powder has:",
            "difficulty": 3,
            "choices": [("More surface area exposed to the water", True),
                        ("A different chemical formula", False),
                        ("Less total mass always", False),
                        ("A higher pH", False)],
            "explanation": r"Breaking the sugar into powder exposes far more surface area, so it reacts and dissolves faster. The trap 'different formula' is false -- it's the same sugar. Pro tip: more surface area means more contact and a faster reaction.",
        },
        {
            "text": r"**Physical Science.** When a metal spoon left in hot soup becomes warm at the handle, heat has traveled through the spoon by:",
            "difficulty": 3,
            "choices": [("Conduction", True), ("Radiation through empty space", False),
                        ("Evaporation", False), ("Magnetism", False)],
            "explanation": r"Conduction transfers heat through direct contact within a solid, like a metal spoon. The trap, radiation, travels through space (like the Sun's heat). Pro tip: conduction = touch; convection = moving fluids; radiation = waves through space.",
        },
        {
            "text": r"**Physical Science.** A sound wave has a frequency of 200 Hz and a wavelength of 1.7 m. Roughly, its speed equals frequency times wavelength, which is about:",
            "difficulty": 3,
            "choices": [("340 m/s", True), ("201.7 m/s", False),
                        ("118 m/s", False), ("3.4 m/s", False)],
            "explanation": r"Wave speed = frequency x wavelength = 200 x 1.7 = 340 m/s (the speed of sound in air). The trap 201.7 adds instead of multiplying. Pro tip: speed = frequency x wavelength.",
        },
        {
            "text": r"**Physical Science.** Mixing an acid with a base produces water and a salt in a reaction called:",
            "difficulty": 3,
            "choices": [("Neutralization", True), ("Combustion", False),
                        ("Photosynthesis", False), ("Condensation", False)],
            "explanation": r"An acid and a base neutralize each other, forming water and a salt and moving toward pH 7. The trap, combustion, is burning. Pro tip: neutralization brings an acid and base toward neutral.",
        },
        {
            "text": r"**Physical Science.** In the reaction CH₄ + 2O₂ → CO₂ + 2H₂O, how many oxygen ATOMS are on the left side?",
            "difficulty": 3,
            "choices": [("4", True), ("2", False), ("1", False), ("6", False)],
            "explanation": r"2O₂ means 2 x 2 = 4 oxygen atoms. The trap '2' counts molecules, not atoms. Pro tip: multiply the coefficient by the subscript to count atoms.",
        },
        {
            "text": r"**Physical Science.** A roller coaster car has the MOST gravitational potential energy:",
            "difficulty": 3,
            "choices": [("At the highest point of the track", True),
                        ("At the lowest point of the track", False),
                        ("When it is moving fastest", False),
                        ("When it is painted a bright color", False)],
            "explanation": r"Potential energy is greatest at the highest point; it converts to kinetic energy as the car drops. The trap 'moving fastest' is where KINETIC energy peaks, at the bottom. Pro tip: high and slow = potential; low and fast = kinetic.",
        },
        {
            "text": r"**Physical Science.** Two atoms of the SAME element always have the same number of:",
            "difficulty": 3,
            "choices": [("Protons", True), ("Neutrons", False),
                        ("Bonds", False), ("Molecules", False)],
            "explanation": r"The number of protons (the atomic number) defines the element, so it is always the same. The trap, neutrons, can vary -- those are isotopes. Pro tip: change the protons and you change the element itself.",
        },
        # ======================= EARTH & SPACE SCIENCE =======================
        {
            "text": r"**Earth & Space.** In undisturbed layers of sedimentary rock, the OLDEST layer is usually:",
            "difficulty": 3,
            "choices": [("At the bottom", True), ("At the very top", False),
                        ("In the exact middle", False), ("Impossible to estimate", False)],
            "explanation": r"By the law of superposition, lower layers were deposited first, so they are oldest. The trap 'at the top' reverses this. Pro tip: deeper usually means older in undisturbed rock layers.",
        },
        {
            "text": r"**Earth & Space.** At a divergent plate boundary, such as the mid-ocean ridge, plates move apart and:",
            "difficulty": 3,
            "choices": [("New crust forms as magma rises and cools", True),
                        ("Tall mountains are pushed up by collision", False),
                        ("Crust is destroyed and pulled under", False),
                        ("Nothing happens to the crust", False)],
            "explanation": r"As plates spread apart, magma rises to fill the gap and forms new crust (seafloor spreading). The trap 'mountains by collision' describes a convergent boundary. Pro tip: divergent = spreading apart = new crust.",
        },
        {
            "text": r"**Earth & Space.** Which statement best describes the difference between weather and climate?",
            "difficulty": 3,
            "choices": [("Weather is day-to-day; climate is the long-term average", True),
                        ("Weather lasts for decades; climate changes hourly", False),
                        ("They mean exactly the same thing", False),
                        ("Climate only exists at the equator", False)],
            "explanation": r"Weather is the short-term state of the atmosphere; climate is the long-term pattern. The trap reverses the time scales. Pro tip: weather is what you get today; climate is what you expect over years.",
        },
        {
            "text": ("**Earth & Space.** Use the diagram.\n\n"
                     "[[figure:sun_anatomy|The structure of the Sun]]\n\n"
                     "The Sun produces its enormous energy through the process of:"),
            "difficulty": 3,
            "choices": [("Nuclear fusion of hydrogen into helium", True),
                        ("Burning wood and coal", False),
                        ("Friction between clouds", False),
                        ("Reflecting light from Earth", False)],
            "explanation": r"In the Sun's core, hydrogen nuclei fuse into helium, releasing immense energy. The trap 'burning wood and coal' is ordinary combustion, far too weak. Pro tip: stars shine by nuclear fusion, not chemical burning.",
        },
        {
            "text": r"**Earth & Space.** Warm ocean water near the equator tends to flow toward the poles. This large-scale movement of heat by moving water is an example of:",
            "difficulty": 3,
            "choices": [("Convection", True), ("Conduction", False),
                        ("Reflection", False), ("Sedimentation", False)],
            "explanation": r"Convection moves heat through a flowing fluid -- here, ocean currents carrying warmth toward the poles. The trap, conduction, needs direct solid contact. Pro tip: convection currents move heat in both oceans and air.",
        },
        {
            "text": r"**Earth & Space.** Scientists can pinpoint the location of an earthquake's origin by comparing the arrival times of seismic waves at:",
            "difficulty": 3,
            "choices": [("Several stations in different places", True),
                        ("A single station only", False),
                        ("Weather satellites that track clouds", False),
                        ("The phases of the Moon", False)],
            "explanation": r"Comparing when waves reach multiple stations lets scientists triangulate the source. The trap, a single station, can't fix a location alone. Pro tip: it takes at least three stations to triangulate an epicenter.",
        },
        {
            "text": r"**Earth & Space.** Rising levels of carbon dioxide in the atmosphere are linked to a long-term rise in global temperatures because CO₂:",
            "difficulty": 3,
            "choices": [("Traps additional heat near Earth's surface", True),
                        ("Blocks sunlight from reaching Earth", False),
                        ("Cools the planet by reflecting heat", False),
                        ("Has no effect on temperature at all", False)],
            "explanation": r"CO₂ is a greenhouse gas that traps heat, so more of it warms the planet. The trap 'cools the planet' is the opposite. Pro tip: more greenhouse gas = more trapped heat = warming.",
        },
        {
            "text": r"**Earth & Space.** The Moon takes about the same time to rotate once as it does to orbit Earth, which is why we always see:",
            "difficulty": 3,
            "choices": [("The same side of the Moon", True),
                        ("Every side of the Moon each night", False),
                        ("No Moon at all", False),
                        ("Two Moons in the sky", False)],
            "explanation": r"Because its rotation and orbit are synchronized, the Moon always shows Earth the same face. The trap 'every side each night' ignores this lock. Pro tip: this synchronized spin is why there is a permanent 'far side' of the Moon.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the expert (Level 3) full-length GED Science practice exam (34 questions; MCQ only)."

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
            f"{course.questions.count()} questions (expert level)."
        ))
