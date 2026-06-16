"""
Seed data: 'GED Science: Ecosystems & Energy Flow (Deep Dive)'.

A focused EXPANSION of Lesson 5 ("Ecosystems & Energy Flow") from the broader
'GED Science: Life Science' course, brought up to the full deep-dive standard
(6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. Ecosystems -- living and nonliving parts; levels of organization.
  2. Energy flow -- food chains and food webs.
  3. The energy pyramid and the 10% rule.
  4. Cycling of matter (the carbon cycle).
  5. Populations -- growth, limits, and carrying capacity.
  6. Relationships, disruptions & reading ecology data.

This course uses ALL-NEW diagrams (levels of organization, a food web, a detailed
energy pyramid, the carbon cycle, a carrying-capacity graph, symbiosis types, and
a predator-prey graph) rather than reusing the parent course's 'food_chain' and
'energy_pyramid' figures.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Biology* and *Concepts of Biology* (ecology, energy flow).
  - Campbell & Reece, *Biology*; NOAA and US EPA ecosystem resources.
  - University of California Museum of Paleontology, "Understanding Evolution"
    (for selection/relationship context).
Note: roughly 10% of the energy at one trophic level is passed to the next; the
rest is used in life processes or lost as heat. Matter (carbon, water, nitrogen)
cycles and is reused, while energy flows one way and leaves as heat.

Run:
    python manage.py seed_ged_ecosystems_energy_flow
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Ecosystems & Energy Flow (Deep Dive)",
    "slug": "ged-ecosystems-energy-flow",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into how living things interact and how energy moves through nature, expanding the "
        "single 'Ecosystems & Energy Flow' lesson from the GED Life Science course into a full "
        "mini-course. You'll learn the living and nonliving parts of ecosystems, trace energy through "
        "food chains and webs, see why energy shrinks at each step (the 10% rule), follow how matter "
        "cycles through the carbon cycle, explore population limits and carrying capacity, and study the "
        "relationships and disruptions that shape ecosystems. Plain language, all-new labeled diagrams, "
        "common-misconception warnings, and GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. What Makes an Ecosystem?",
            r"An **ecosystem** is all the **living** things in an area together with the **nonliving** things they interact with. The living parts are **biotic factors** — plants, animals, fungi, bacteria. The nonliving parts are **abiotic factors** — sunlight, temperature, water, air, soil, and rocks." "\n\n"
            r"[[figure:ecosystem_levels|Life is organized in levels: one organism, a population of its kind, a community of many kinds, then the whole ecosystem and biosphere.]]" "\n\n"
            r"Scientists describe nature in **levels of organization**, from small to large:" "\n"
            r"- **Organism** — a single individual." "\n"
            r"- **Population** — all the individuals of **one species** in an area." "\n"
            r"- **Community** — all the **different species** living and interacting there." "\n"
            r"- **Ecosystem** — the community **plus** its nonliving surroundings." "\n"
            r"- **Biosphere** — all of Earth's ecosystems together." "\n\n"
            r"The key idea is **interaction**: organisms depend on resources, compete for what's limited, and change their surroundings. A change in one part can **ripple** through the rest — if rainfall drops, plants grow less, then plant-eaters have less food, and so on." "\n\n"
            r"⚠️ Common misconception: an ecosystem is **not** only the living organisms. The **nonliving** environment (sun, water, soil, air) is part of the system too." "\n\n"
            r"💡 Tip: **biotic = living; abiotic = nonliving.** Order of levels: organism → population → community → ecosystem.",
        ),
        (
            "2. Energy Flow: Food Chains & Webs",
            r"Almost all of an ecosystem's energy starts as **sunlight**. From there it flows from one organism to the next, and every organism has a role based on **how it gets energy**." "\n\n"
            r"[[figure:food_web|In a food web, arrows point from food to the eater because they show the direction energy flows.]]" "\n\n"
            r"- **Producers** (plants, algae) make their own food by **photosynthesis** — they capture energy first." "\n"
            r"- **Consumers** get energy by eating other organisms: **herbivores** eat plants, **carnivores** eat animals, **omnivores** eat both." "\n"
            r"- **Decomposers** (fungi, bacteria) break down dead material and **recycle nutrients** back into the ecosystem." "\n\n"
            r"A **food chain** shows a single path of energy (grass → grasshopper → frog → snake). A **food web** links many chains together and is more realistic, because most organisms eat — and are eaten by — more than one kind of thing." "\n\n"
            r"The **arrows** always point from the **food to the eater**, showing the direction **energy** moves. Grass → grasshopper means the energy stored in grass passes to the grasshopper when it's eaten." "\n\n"
            r"⚠️ Common misconception: the arrows do **not** mean 'chases' or point from predator to prey. They show **energy flowing** from the food to the consumer." "\n\n"
            r"💡 Tip: **producers start every chain** (right after the Sun), and arrows follow the **energy**.",
        ),
        (
            "3. The Energy Pyramid & the 10% Rule",
            r"Energy doesn't pass perfectly from one level to the next — most of it is **lost** along the way. An **energy pyramid** shows how the energy available **shrinks** at each higher feeding (trophic) level." "\n\n"
            r"[[figure:energy_pyramid_detailed|Each level up keeps only about 10% of the energy below it; the rest is used for life processes or lost as heat.]]" "\n\n"
            r"A useful rule of thumb is the **10% rule**: only about **10%** of the energy at one level is passed to the next. The other ~90% is used to live (movement, growth, body heat) and lost as **heat**. So if producers capture **10,000** kcal, primary consumers get about **1,000**, secondary consumers about **100**, and the top level only about **10**." "\n\n"
            r"This is why ecosystems have **many producers but few top predators**, and why food chains rarely have more than four or five links — there simply isn't enough energy left to support more." "\n\n"
            r"⚠️ Common misconception: energy is **not** recycled the way matter is. Energy **flows through** an ecosystem and is eventually lost as heat — it does not return to the producers to be used again." "\n\n"
            r"💡 Tip: remember **'matter cycles; energy flows.'** Energy drops by about 90% at each step up the pyramid.",
        ),
        (
            "4. Cycling of Matter: The Carbon Cycle",
            r"While **energy** flows one way and is lost as heat, **matter** is **recycled** — the same atoms of carbon, oxygen, nitrogen, and water are used again and again. A great example is the **carbon cycle**." "\n\n"
            r"[[figure:carbon_cycle|Photosynthesis pulls carbon dioxide out of the air; respiration, decomposition, and burning fuels release it back.]]" "\n\n"
            r"Follow the carbon:" "\n"
            r"- **Photosynthesis** removes **CO₂** from the air and locks the carbon into sugars in plants." "\n"
            r"- **Eating** passes that carbon from plants to animals." "\n"
            r"- **Cellular respiration** (in plants and animals), **decomposition** of dead matter, and **burning fuels** all **release CO₂** back to the atmosphere." "\n\n"
            r"**Decomposers** are essential to every cycle: by breaking down dead organisms and waste, they return nutrients to the soil and water for producers to use again. Human activities, especially **burning fossil fuels**, add extra CO₂ to the air." "\n\n"
            r"⚠️ Common misconception: decomposers are not unimportant 'rot.' Without them, dead matter and its nutrients would pile up and the cycle would stall." "\n\n"
            r"💡 Tip: **matter cycles** (carbon, water, nitrogen) and is reused; **energy flows** and is lost. Decomposers keep the matter moving.",
        ),
        (
            "5. Populations: Growth & Carrying Capacity",
            r"Populations don't grow forever. When resources are plentiful, a population can grow quickly — but it eventually runs into limits and **levels off**." "\n\n"
            r"[[figure:carrying_capacity_graph|A population grows fast, then levels off at the carrying capacity — the most the environment can support.]]" "\n\n"
            r"The **carrying capacity** is the **largest population an environment can support over time**. It is set by **limiting factors** — resources in short supply, such as **food, water, space, and shelter**. As a population nears its carrying capacity, growth slows and the line flattens out (an S-shaped curve)." "\n\n"
            r"If a population grows **beyond** its carrying capacity, individuals may **die, leave, or reproduce less**, and the population drops back toward the limit. If a new resource becomes available, carrying capacity may **rise**; if drought or habitat loss reduces resources, it may **fall**." "\n\n"
            r"⚠️ Common misconception: population growth **cannot** continue forever in a limited environment. Sooner or later, limited resources cap the population." "\n\n"
            r"💡 Tip: **carrying capacity = the stable limit set by available resources.** A leveling-off graph usually marks it.",
        ),
        (
            "6. Relationships, Disruptions & Reading Ecology Data",
            r"Species interact in close, long-term relationships called **symbiosis**, and these come in three types." "\n\n"
            r"[[figure:symbiosis_types|Mutualism helps both species; commensalism helps one and doesn't affect the other; parasitism helps one and harms the other.]]" "\n\n"
            r"- **Mutualism** (+/+) — **both** benefit (a bee gets nectar while pollinating a flower)." "\n"
            r"- **Commensalism** (+/0) — **one** benefits, the other is **unaffected**." "\n"
            r"- **Parasitism** (+/−) — one benefits and the other is **harmed** (a tick feeding on a dog)." "\n\n"
            r"Populations also affect each other. In **predator-prey** cycles, the populations rise and fall in an offset pattern:" "\n\n"
            r"[[figure:predator_prey_graph|When prey become plentiful, predators increase soon after; then prey decline, and predators follow.]]" "\n\n"
            r"Ecosystems can be **disrupted** by **invasive species**, habitat destruction, pollution, drought, disease, and overharvesting. An invasive species can spread quickly where it has **no natural predators**, outcompeting native species." "\n\n"
            r"**Reading ecology data (a GED skill).** Items often show population graphs or food webs. Read the **title, axes, and key**, find the **trend**, and trace **food-web connections** to predict effects. Remember: **correlation is not causation**." "\n\n"
            r"⚠️ Common misconception: not every nonnative species is 'invasive.' It is invasive only when it **spreads and causes harm** to the ecosystem or economy." "\n\n"
            r"💡 Tip: read the signs — **+ benefits, 0 unaffected, − harmed.** To predict a change, trace the **food-web connections**." "\n\n"
            r"📚 Sources: OpenStax *Biology* / *Concepts of Biology*; Campbell & Reece, *Biology*; NOAA and US EPA ecosystem resources.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: ecosystems ---
        {
            "text": r"Which of the following is an ABIOTIC (nonliving) factor in an ecosystem?",
            "difficulty": 1,
            "choices": [("Sunlight", True), ("Grass", False),
                        ("A fungus", False), ("A rabbit", False)],
            "explanation": r"Abiotic means nonliving. Sunlight, water, temperature, air, and soil are abiotic. Grass, fungi, and rabbits are living (biotic).",
        },
        {
            "text": r"An ecosystem is best described as:",
            "difficulty": 1,
            "choices": [("All the living things in an area plus their nonliving surroundings", True),
                        ("Only the animals in an area", False),
                        ("Only the nonliving parts of an area", False),
                        ("A single organism", False)],
            "explanation": r"An ecosystem includes both the community of living things and the abiotic environment they interact with.",
        },
        {
            "text": r"All the rabbits living and breeding in one meadow are an example of a:",
            "difficulty": 2,
            "choices": [("Population", True), ("Community", False),
                        ("Ecosystem", False), ("Biosphere", False)],
            "explanation": r"A population is all the members of one species in an area. A community is all the different species together.",
        },
        {
            "text": r"All the different species living and interacting in one area form a:",
            "difficulty": 2,
            "choices": [("Community", True), ("Population", False),
                        ("Single organism", False), ("Biome of the whole Earth", False)],
            "explanation": r"A community is the set of all populations (different species) interacting in an area.",
        },
        {
            "text": ("Use the diagram.\n\n"
                     "[[figure:ecosystem_levels|Levels of organization]]\n\n"
                     "Which lists the levels in the correct order from SMALLEST to LARGEST?"),
            "difficulty": 2,
            "choices": [("Organism, population, community, ecosystem", True),
                        ("Ecosystem, community, population, organism", False),
                        ("Population, organism, ecosystem, community", False),
                        ("Community, ecosystem, organism, population", False)],
            "explanation": r"From smallest to largest: organism, then population (one species), community (all species), then ecosystem (community + nonliving). Pro tip: each level contains the one before it.",
        },
        # --- Lesson 2: food chains & webs ---
        {
            "text": r"Organisms that make their own food using sunlight are called:",
            "difficulty": 1,
            "choices": [("Producers", True), ("Consumers", False),
                        ("Decomposers", False), ("Predators", False)],
            "explanation": r"Producers (like plants) capture light energy through photosynthesis and form the base of food chains.",
        },
        {
            "text": r"In a food chain or food web, the arrows point:",
            "difficulty": 1,
            "choices": [("From the food to the organism that eats it (energy flow)", True),
                        ("From the eater to its food", False),
                        ("Toward whichever organism is largest", False),
                        ("In the direction predators run", False)],
            "explanation": r"Arrows show the direction energy flows, which is from the food toward the consumer.",
        },
        {
            "text": r"Decomposers such as fungi and bacteria are important because they:",
            "difficulty": 2,
            "choices": [("Break down dead matter and recycle nutrients", True),
                        ("Capture sunlight to make food", False),
                        ("Are always the top predators", False),
                        ("Stop matter from cycling", False)],
            "explanation": r"Decomposers return nutrients from dead organisms and waste to the soil and water, keeping the ecosystem's matter cycling.",
        },
        {
            "text": r"A food web is considered more realistic than a single food chain because:",
            "difficulty": 2,
            "choices": [("Most organisms eat, and are eaten by, more than one kind of organism", True),
                        ("Food webs have no producers", False),
                        ("Energy never flows in a web", False),
                        ("A web shows only one path of energy", False)],
            "explanation": r"In nature, feeding relationships overlap, so many food chains link together into a web.",
        },
        {
            "text": ("Use the food web.\n\n"
                     "[[figure:food_web|A food web of grassland organisms]]\n\n"
                     "In this web, which organism is the producer?"),
            "difficulty": 1,
            "choices": [("Grass", True), ("Grasshopper", False),
                        ("Snake", False), ("Hawk", False)],
            "explanation": r"Grass makes its own food by photosynthesis, so it is the producer at the base of the web. Pro tip: the producer is where the energy enters, right after the Sun.",
        },
        {
            "text": r"An animal that eats only plants is called a(n):",
            "difficulty": 1,
            "choices": [("Herbivore", True), ("Carnivore", False),
                        ("Producer", False), ("Decomposer", False)],
            "explanation": r"Herbivores eat only plants. Carnivores eat animals, and omnivores eat both.",
        },
        # --- Lesson 3: energy pyramid ---
        {
            "text": r"About how much of the energy at one level of an energy pyramid passes to the next level up?",
            "difficulty": 1,
            "choices": [("About 10%", True), ("About 50%", False),
                        ("About 90%", False), ("100%", False)],
            "explanation": r"Roughly 10% of the energy transfers to the next level; the rest is used in life processes or lost as heat.",
        },
        {
            "text": r"Why are there usually many producers but only a few top predators?",
            "difficulty": 2,
            "choices": [("Available energy decreases at each higher level, so less supports the top", True),
                        ("Top predators do not need any energy", False),
                        ("Producers eat the predators", False),
                        ("Energy increases going up the pyramid", False)],
            "explanation": r"Because only ~10% of energy passes upward, higher levels have far less energy and can support far fewer organisms.",
        },
        {
            "text": ("Use the energy pyramid.\n\n"
                     "[[figure:energy_pyramid_detailed|Energy available at each feeding level]]\n\n"
                     "If the producers have about 10,000 kcal, the SECONDARY consumers have about:"),
            "difficulty": 2,
            "choices": [("100 kcal", True), ("1,000 kcal", False),
                        ("10,000 kcal", False), ("10 kcal", False)],
            "explanation": r"Each level keeps about 10%: 10,000 (producers) -> 1,000 (primary) -> 100 kcal (secondary consumers). Pro tip: drop by about 90% per step.",
        },
        {
            "text": r"Most of the energy that does NOT pass to the next trophic level is:",
            "difficulty": 2,
            "choices": [("Used for life processes and lost as heat", True),
                        ("Stored forever in the producers", False),
                        ("Turned into new matter", False),
                        ("Sent back to the Sun", False)],
            "explanation": r"Organisms use most of their energy to live and move, releasing it as heat, so only a small fraction is available to the next level.",
        },
        {
            "text": r"Energy pyramids are usually widest at the bottom because:",
            "difficulty": 3,
            "choices": [("Energy is greatest at the producer level and decreases upward", True),
                        ("There are more predators than producers", False),
                        ("Energy increases at each higher level", False),
                        ("Producers are the largest organisms", False)],
            "explanation": r"The producer level has the most available energy; since only ~10% passes up at each step, each level above is smaller, giving the upright pyramid shape.",
        },
        # --- Lesson 4: cycling of matter ---
        {
            "text": r"Which moves in CYCLES through an ecosystem, being used again and again?",
            "difficulty": 1,
            "choices": [("Matter (such as carbon and water)", True),
                        ("Energy", False),
                        ("Sunlight", False),
                        ("Heat", False)],
            "explanation": r"Matter cycles and is reused, while energy flows one way through the ecosystem and is lost as heat.",
        },
        {
            "text": r"In the carbon cycle, photosynthesis mainly:",
            "difficulty": 2,
            "choices": [("Removes carbon dioxide from the air and stores carbon in sugars", True),
                        ("Releases carbon dioxide into the air", False),
                        ("Destroys all carbon", False),
                        ("Has nothing to do with carbon", False)],
            "explanation": r"Photosynthesis takes CO2 out of the atmosphere and builds it into glucose, locking carbon into living matter.",
        },
        {
            "text": r"Cellular respiration, decomposition, and burning fuels all:",
            "difficulty": 2,
            "choices": [("Release carbon dioxide into the atmosphere", True),
                        ("Remove carbon dioxide from the air", False),
                        ("Create brand-new carbon atoms", False),
                        ("Stop the carbon cycle", False)],
            "explanation": r"These processes return CO2 to the air, balancing the carbon that photosynthesis removes.",
        },
        {
            "text": ("Use the carbon cycle diagram.\n\n"
                     "[[figure:carbon_cycle|How carbon moves through an ecosystem]]\n\n"
                     "According to the diagram, which process RETURNS carbon to the atmosphere?"),
            "difficulty": 2,
            "choices": [("Respiration (and burning fuels)", True),
                        ("Photosynthesis", False),
                        ("A plant growing taller", False),
                        ("Sunlight striking a leaf", False)],
            "explanation": r"The diagram shows respiration, decomposition, and burning fuels releasing CO2 back to the air, while photosynthesis removes it. Pro tip: photosynthesis takes carbon in; respiration puts it back.",
        },
        {
            "text": r"The phrase 'matter cycles; energy flows' means that:",
            "difficulty": 3,
            "choices": [("Atoms are reused, but energy moves one way and is eventually lost as heat", True),
                        ("Energy is reused, but matter disappears", False),
                        ("Both matter and energy are destroyed", False),
                        ("Neither matter nor energy ever moves", False)],
            "explanation": r"Matter (carbon, water, nitrogen) is recycled through the ecosystem, while energy enters as sunlight, passes through, and exits as heat.",
        },
        # --- Lesson 5: populations & carrying capacity ---
        {
            "text": r"Carrying capacity is:",
            "difficulty": 1,
            "choices": [("The largest population an environment can support over time", True),
                        ("The speed an animal can run", False),
                        ("The number of species on Earth", False),
                        ("A type of mutation", False)],
            "explanation": r"Carrying capacity is the maximum population size an environment can sustain, set by its limiting resources.",
        },
        {
            "text": r"A limiting factor is:",
            "difficulty": 2,
            "choices": [("A resource in short supply that limits population growth", True),
                        ("A gene that codes for a protein", False),
                        ("A type of food-chain arrow", False),
                        ("An organism that never dies", False)],
            "explanation": r"Limiting factors such as food, water, space, and shelter cap how large a population can grow.",
        },
        {
            "text": ("Use the population graph.\n\n"
                     "[[figure:carrying_capacity_graph|A population over time]]\n\n"
                     "The point where the graph rises and then levels off represents the:"),
            "difficulty": 2,
            "choices": [("Carrying capacity", True), ("Starting population", False),
                        ("Extinction point", False), ("Biosphere", False)],
            "explanation": r"The leveling-off region marks the carrying capacity, where the population stops growing because resources are fully used. Pro tip: an S-curve flattens at carrying capacity.",
        },
        {
            "text": r"If a population grows beyond its carrying capacity, what is most likely to happen?",
            "difficulty": 2,
            "choices": [("Some individuals die, leave, or reproduce less, and the population drops back", True),
                        ("The population keeps growing forever", False),
                        ("Carrying capacity disappears", False),
                        ("Every individual instantly becomes a new species", False)],
            "explanation": r"When a population overshoots its limit, shortages of resources cause it to decline back toward the carrying capacity.",
        },
        {
            "text": r"A long drought reduces the food and water in a habitat. The carrying capacity for the animals there will most likely:",
            "difficulty": 2,
            "choices": [("Decrease", True), ("Increase", False),
                        ("Stay exactly the same", False), ("Become unlimited", False)],
            "explanation": r"Fewer resources mean the environment can support fewer individuals, so carrying capacity drops.",
        },
        # --- Lesson 6: relationships, disruptions, data ---
        {
            "text": r"In mutualism, the two species involved:",
            "difficulty": 1,
            "choices": [("Both benefit", True), ("Both are harmed", False),
                        ("One benefits and one is harmed", False), ("Neither is affected", False)],
            "explanation": r"In mutualism (+/+), both species benefit, like a bee getting nectar while pollinating a flower.",
        },
        {
            "text": r"A tick feeds on a dog: the tick benefits and the dog is harmed. This relationship is:",
            "difficulty": 2,
            "choices": [("Parasitism", True), ("Mutualism", False),
                        ("Commensalism", False), ("Competition only", False)],
            "explanation": r"Parasitism (+/-) benefits one organism (the parasite) while harming the other (the host).",
        },
        {
            "text": ("Use the predator-prey graph.\n\n"
                     "[[figure:predator_prey_graph|Predator and prey populations over time]]\n\n"
                     "According to the graph, soon AFTER the prey population rises, the predator population:"),
            "difficulty": 2,
            "choices": [("Rises as well (then the prey fall)", True),
                        ("Immediately drops to zero", False),
                        ("Never changes", False),
                        ("Rises before the prey do", False)],
            "explanation": r"More prey means more food for predators, so the predator population rises soon after; then heavy predation makes the prey fall, and predators follow. Pro tip: the predator curve lags the prey.",
        },
        {
            "text": r"An invasive species can disrupt an ecosystem because it may:",
            "difficulty": 2,
            "choices": [("Spread quickly and outcompete native species (with no natural predators)", True),
                        ("Always improve the ecosystem", False),
                        ("Have no effect on the food web", False),
                        ("Turn into a producer automatically", False)],
            "explanation": r"Without natural predators to control it, an invasive species can take over resources and crowd out native species.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain the difference between how ENERGY moves through an ecosystem and how MATTER moves through "
                "it. In your answer, describe energy flow using the energy pyramid and the 10% rule, and describe "
                "matter cycling using the carbon cycle. End by explaining the phrase 'matter cycles; energy flows.'"
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) energy enters as sunlight, is captured by producers, and passes up trophic "
                "levels with only about 10% transferred each step (the rest used or lost as heat); (2) the energy "
                "pyramid shows energy decreasing upward, so fewer organisms are supported at higher levels; (3) matter "
                "(carbon) cycles -- photosynthesis removes CO2, respiration/decomposition/burning return it; "
                "(4) 'matter cycles; energy flows' means atoms are reused but energy moves one way and exits as heat. "
                "Deduct for saying energy is recycled or matter is lost as heat."
            ),
        },
        {
            "text": (
                "Compare the three types of symbiosis (mutualism, commensalism, and parasitism), giving an example "
                "of each. Then explain how removing one species from a food web -- for example, a predator -- could "
                "affect the other organisms in the ecosystem."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) mutualism -- both benefit (e.g., bee and flower); (2) commensalism -- one "
                "benefits, the other is unaffected; (3) parasitism -- one benefits, the other is harmed (e.g., tick "
                "and dog); (4) explaining a food-web ripple effect, such as removing a predator letting its prey "
                "increase, which then reduces the prey's food source, affecting still other species. Deduct for "
                "mixing up the symbiosis types or treating food-web members as unconnected."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Ecosystems & Energy Flow (Deep Dive)' course."

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
