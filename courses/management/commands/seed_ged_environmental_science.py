"""
Seed data: 'GED Science: Environmental Science & Human Impact'.

A standalone course covering the environmental science topics that appear
throughout the GED Science test but have no dedicated course yet:

  1. Ecosystems: Components and Organization
  2. Food Webs and Energy Flow
  3. Biodiversity and Ecological Relationships
  4. Human Impact on Ecosystems
  5. Climate Change and the Greenhouse Effect
  6. Pollution and Natural Resources
  7. Conservation, Sustainability & Reading Environmental Data

Uses existing figures: ecosystem_levels, food_web, energy_pyramid_detailed,
carrying_capacity_graph, carbon_cycle, greenhouse_effect, bar_recycling.

Run:
    python manage.py seed_ged_environmental_science
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Environmental Science & Human Impact",
    "slug": "ged-environmental-science",
    "program": "GED",
    "subject": "science",
    "description": (
        "Explore how living things interact with each other and the planet — and what happens when "
        "humans change those interactions. This course covers ecosystems, food webs, energy flow, "
        "biodiversity, climate change, pollution, natural resources, and conservation. Every lesson "
        "uses real-world examples, labeled diagrams, misconception warnings, and GED-style practice "
        "questions with full explanations. No prior science background required."
    ),
    "lessons": [
        (
            "1. Ecosystems: Components and Organization",
            "An **ecosystem** is all the living and nonliving things in an area, interacting together. "
            "Understanding its parts is the foundation of all environmental science.\n\n"
            "[[figure:ecosystem_levels|Ecosystems are organized from individual organisms up to the entire biosphere.]]\n\n"
            "**Two main components:**\n"
            "- **Biotic factors** — all living things: plants, animals, fungi, bacteria.\n"
            "- **Abiotic factors** — nonliving things: sunlight, temperature, water, soil, air.\n\n"
            "**Levels of ecological organization (small → large):**\n"
            "- **Individual** — one organism (a single oak tree).\n"
            "- **Population** — all individuals of ONE species in an area (all oak trees in a forest).\n"
            "- **Community** — all populations of DIFFERENT species sharing an area (oaks + deer + hawks).\n"
            "- **Ecosystem** — the community PLUS its abiotic environment.\n"
            "- **Biome** — a large region with similar climate and dominant organisms (tropical rainforest, desert).\n"
            "- **Biosphere** — all of Earth's ecosystems combined.\n\n"
            "**Habitat vs. niche:** A habitat is where an organism lives; a niche is its role — what it eats, "
            "when it is active, how it reproduces. Two species cannot share the exact same niche in the same place "
            "for long (**competitive exclusion**).\n\n"
            "**Energy enters ecosystems** through **photosynthesis** in producers (plants, algae). "
            "**Decomposers** (bacteria, fungi) break down dead matter, returning nutrients to the soil.\n\n"
            "⚠️ Common misconception: abiotic factors are just as important as biotic ones. "
            "Remove sunlight or water and the entire ecosystem collapses, no matter how many species are present.\n\n"
            "💡 Tip: On the GED, if a question asks about the 'nonliving parts of an ecosystem,' the answer involves abiotic factors."
        ),
        (
            "2. Food Webs and Energy Flow",
            "Energy captured by producers flows through an ecosystem via **feeding relationships**. "
            "Tracing this flow is a core GED Science skill.\n\n"
            "[[figure:food_web|A food web shows how energy moves through multiple overlapping food chains in an ecosystem.]]\n\n"
            "**Key feeding levels (trophic levels):**\n"
            "- **Producers (autotrophs)** — make their own food via photosynthesis (grass, algae, phytoplankton).\n"
            "- **Primary consumers (herbivores)** — eat producers (rabbits, deer, caterpillars).\n"
            "- **Secondary consumers** — eat primary consumers (foxes, frogs, small fish).\n"
            "- **Tertiary consumers** — eat secondary consumers (eagles, large sharks).\n"
            "- **Decomposers** — break down all levels (bacteria, fungi, earthworms).\n\n"
            "**Food chain vs. food web:** A food chain is a single straight path; a food web shows "
            "ALL the overlapping chains. Real ecosystems are webs, not chains.\n\n"
            "[[figure:energy_pyramid_detailed|Only about 10% of energy transfers to the next trophic level; the rest is lost as heat.]]\n\n"
            "**The 10% Rule:** At each trophic level, only about **10%** of the energy is passed on "
            "to the next level. The other 90% is used for the organism's own life processes or lost as heat. "
            "This is why there are always far more plants than herbivores, and far more herbivores than carnivores.\n\n"
            "⚠️ Common misconception: removing one species from a food web does NOT only affect the species "
            "that ate it — it triggers a **cascade** of changes up and down the web.\n\n"
            "💡 Tip: If a question shows a food web and asks what happens when a species is removed, "
            "trace both the predators (lose food) and the prey (population may explode) of the lost species."
        ),
        (
            "3. Biodiversity and Ecological Relationships",
            "**Biodiversity** is the variety of life in an area — species diversity, genetic diversity, "
            "and ecosystem diversity. More biodiversity generally means a more stable ecosystem.\n\n"
            "[[figure:carrying_capacity_graph|A population grows until it reaches the carrying capacity — the maximum the environment can support.]]\n\n"
            "**Carrying capacity (K):** Every environment has a limit on how many individuals of a species "
            "it can support, set by food, water, shelter, and space. When a population exceeds K, "
            "resources run short, death rates rise, and the population falls back down.\n\n"
            "**Ecological relationships:**\n"
            "- **Predation** — predator benefits, prey is harmed (wolf eats rabbit).\n"
            "- **Competition** — both species are harmed as they fight for the same resource.\n"
            "- **Mutualism** — both species benefit (bees pollinate flowers; flowers feed bees).\n"
            "- **Commensalism** — one benefits, the other is unaffected (barnacles on a whale).\n"
            "- **Parasitism** — parasite benefits, host is harmed (tick on a dog).\n\n"
            "**Keystone species:** A species that has a disproportionately large effect on its ecosystem "
            "relative to its population size (e.g., sea otters control sea urchin populations, which protects kelp forests).\n\n"
            "**Invasive species** arrive in a new ecosystem without natural predators, often outcompeting "
            "native species and reducing biodiversity.\n\n"
            "⚠️ Common misconception: predators are bad for an ecosystem. In fact, predators control "
            "prey populations, preventing overgrazing and maintaining balance.\n\n"
            "💡 Tip: GED questions often give a graph of two interacting populations and ask you to identify "
            "the relationship. Look for whether the populations rise and fall together (mutualism) or "
            "alternate (predation/competition)."
        ),
        (
            "4. Human Impact on Ecosystems",
            "Humans are now the single largest driver of ecosystem change on Earth. "
            "Understanding these impacts is central to the GED Science test.\n\n"
            "[[figure:carbon_cycle|The carbon cycle shows how carbon moves between the atmosphere, living organisms, oceans, and rock. Burning fossil fuels adds extra CO₂.]]\n\n"
            "**Major human impacts:**\n"
            "- **Habitat destruction** — clearing forests, draining wetlands, and paving land reduces the "
            "living space available to species. It is the #1 cause of species extinction today.\n"
            "- **Deforestation** — removes trees that absorb CO₂, store carbon, regulate water cycles, "
            "and prevent soil erosion. Tropical deforestation is especially damaging to biodiversity.\n"
            "- **Overhunting and overfishing** — removing organisms faster than they reproduce depletes populations.\n"
            "- **Introduction of invasive species** — accidentally or intentionally, non-native species "
            "can disrupt food webs (e.g., zebra mussels in the Great Lakes).\n"
            "- **Pollution** — contaminates air, water, and soil (covered in Lesson 6).\n"
            "- **Climate change** — rising temperatures shift habitats, alter seasons, and bleach coral reefs.\n\n"
            "**Biomagnification:** Some pollutants (like DDT and mercury) are not broken down in the body. "
            "They become MORE concentrated at each trophic level because each organism eats many from the level below. "
            "Top predators (including humans eating large fish) receive the highest doses.\n\n"
            "⚠️ Common misconception: habitat fragmentation (breaking habitat into small pieces) is less harmful "
            "than total destruction. In fact, fragmentation isolates populations, preventing breeding and migration, "
            "causing slow extinction even when patches of habitat remain.\n\n"
            "💡 Tip: If a GED question shows a data table of pollutant levels rising through a food chain, "
            "that is biomagnification — choose the top predator as having the highest concentration."
        ),
        (
            "5. Climate Change and the Greenhouse Effect",
            "**Climate** is the long-term pattern of weather in a region. **Climate change** refers to "
            "the shift in global climate patterns, primarily caused by the increase in greenhouse gases "
            "from human activity.\n\n"
            "[[figure:greenhouse_effect|Greenhouse gases trap heat that would otherwise escape to space, warming Earth's surface — the natural greenhouse effect becomes harmful when intensified by human emissions.]]\n\n"
            "**The natural greenhouse effect (necessary for life):**\n"
            "Solar energy reaches Earth. Earth's surface absorbs it and re-emits it as infrared (heat) radiation. "
            "Greenhouse gases in the atmosphere — water vapor (H₂O), carbon dioxide (CO₂), methane (CH₄), "
            "and nitrous oxide (N₂O) — trap some of this heat, keeping Earth warm enough for life.\n\n"
            "**The enhanced greenhouse effect (human-caused):**\n"
            "Burning fossil fuels (coal, oil, natural gas) releases CO₂. Livestock farming and landfills release CH₄. "
            "These added gases trap MORE heat, raising global average temperatures.\n\n"
            "**Evidence for climate change:**\n"
            "- Rising average global temperatures (especially since the 1950s).\n"
            "- Melting glaciers and polar ice caps.\n"
            "- Rising sea levels.\n"
            "- More frequent and intense extreme weather events.\n"
            "- Shifts in species ranges toward the poles and to higher elevations.\n\n"
            "**Key greenhouse gases and their sources:**\n"
            "- CO₂: burning fossil fuels, deforestation.\n"
            "- CH₄ (methane): livestock, natural gas leaks, landfills.\n"
            "- N₂O: fertilizers, agriculture.\n\n"
            "⚠️ Common misconception: the ozone hole and the greenhouse effect are the same thing. "
            "They are NOT. The ozone hole (caused by CFCs) affects UV radiation reaching Earth. "
            "The greenhouse effect is about heat retention.\n\n"
            "💡 Tip: On the GED, 'Which gas contributes most to current climate change?' → CO₂ "
            "from burning fossil fuels is the main answer."
        ),
        (
            "6. Pollution and Natural Resources",
            "**Pollution** is the introduction of harmful substances into the environment. "
            "Understanding types, sources, and effects is a frequent GED topic.\n\n"
            "**Types of pollution:**\n"
            "- **Air pollution** — burning fossil fuels releases CO₂, sulfur dioxide (SO₂), and nitrogen oxides (NOₓ). "
            "SO₂ and NOₓ dissolve in rainwater to form **acid rain**, which damages forests and aquatic ecosystems.\n"
            "- **Water pollution** — industrial waste, agricultural runoff (fertilizers containing nitrogen and "
            "phosphorus), and sewage contaminate lakes, rivers, and groundwater.\n"
            "- **Eutrophication** — excess nutrients (especially from fertilizer runoff) cause algae to "
            "bloom explosively. When the algae die, bacteria decompose them and use up all the oxygen, "
            "creating **dead zones** where fish cannot survive.\n"
            "- **Soil pollution** — pesticides, heavy metals, and plastic waste degrade farmland and groundwater.\n"
            "- **Plastic pollution** — plastics break into **microplastics** that enter food chains.\n\n"
            "**Natural resources:**\n"
            "- **Renewable** — replenish naturally within a human lifetime: solar energy, wind, water (hydro), "
            "wood (if forests are managed), geothermal.\n"
            "- **Nonrenewable** — form over millions of years and are used far faster than they form: "
            "coal, oil, natural gas (fossil fuels), uranium.\n\n"
            "**Fossil fuels** formed from ancient organisms buried under pressure. They are carbon-rich and "
            "release CO₂ when burned — the main driver of climate change.\n\n"
            "⚠️ Common misconception: nuclear power is a renewable resource. Uranium (the fuel) is "
            "**nonrenewable**; nuclear power just produces no direct CO₂ emissions while operating.\n\n"
            "💡 Tip: Eutrophication questions on the GED often show a graph with rising nutrient levels "
            "followed by a drop in dissolved oxygen — trace cause → algae bloom → oxygen depletion → fish die."
        ),
        (
            "7. Conservation, Sustainability & Reading Environmental Data",
            "**Conservation** is the careful management of natural resources to prevent depletion. "
            "**Sustainability** means meeting today's needs without preventing future generations from "
            "meeting theirs — the central goal of modern environmental science.\n\n"
            "**Conservation strategies:**\n"
            "- **Protected areas** — national parks, wildlife reserves, and marine protected areas "
            "preserve habitat and biodiversity.\n"
            "- **Habitat corridors** — strips of natural habitat connecting fragmented patches, allowing "
            "animals to migrate and populations to mix.\n"
            "- **Captive breeding** — breeding endangered species in zoos, then reintroducing them to the wild.\n"
            "- **Reforestation** — planting trees to restore forests, absorb CO₂, and prevent erosion.\n"
            "- **Reduce, Reuse, Recycle** — reducing waste and pollution in production and consumption.\n\n"
            "**Sustainable practices:**\n"
            "- Switching to **renewable energy** (solar, wind) to reduce fossil fuel dependence.\n"
            "- **Sustainable fishing** — setting catch limits below the replenishment rate.\n"
            "- **Organic farming** — reducing synthetic pesticides and fertilizers.\n"
            "- **Carbon capture** — technology that removes CO₂ from the atmosphere.\n\n"
            "**Reading environmental data on the GED:**\n"
            "- Look at the axis labels before reading any data.\n"
            "- Identify trends: is a value rising, falling, or stable?\n"
            "- Correlation ≠ causation: two trends rising together does not prove one causes the other "
            "(though the GED often presents strong, well-established causal links like CO₂ and temperature).\n"
            "- Units matter: ppm (parts per million), °C, kg/ha — make sure you use the right units in calculations.\n\n"
            "⚠️ Common misconception: individual actions do not matter. In fact, large-scale environmental "
            "change is the sum of billions of individual and collective choices.\n\n"
            "💡 Tip: GED graph questions often ask you to 'describe the trend' or 'predict the value at year X'. "
            "Practice reading axes carefully and extrapolating lines."
        ),
    ],
    "mcqs": [
        # Lesson 1 – Ecosystems: Components and Organization
        {
            "text": "Which of the following is an ABIOTIC factor in a forest ecosystem?",
            "difficulty": 1,
            "choices": [("Soil moisture", True), ("Oak trees", False), ("Deer population", False), ("Decomposing fungi", False)],
            "explanation": "Abiotic factors are nonliving components of an ecosystem. Soil moisture is nonliving. Oak trees, deer, and fungi are all living (biotic) factors.",
        },
        {
            "text": "A scientist studies all the deer in a national park. What level of ecological organization is she studying?",
            "difficulty": 1,
            "choices": [("Population", True), ("Community", False), ("Ecosystem", False), ("Biome", False)],
            "explanation": "A population is all individuals of the SAME species in one area. The scientist is studying one species (deer) in one place, so this is a population.",
        },
        {
            "text": "Which statement best describes the difference between a habitat and a niche?",
            "difficulty": 2,
            "choices": [
                ("A habitat is where an organism lives; a niche is its role in the ecosystem.", True),
                ("A habitat is the organism's diet; a niche is its physical location.", False),
                ("Both terms refer to the same concept.", False),
                ("A niche is where an organism lives; a habitat is its role.", False),
            ],
            "explanation": "Habitat = WHERE (the physical place). Niche = WHAT (the organism's role: what it eats, when it is active, how it reproduces). The terms are often confused but describe different things.",
        },
        {
            "text": "Bacteria that break down dead leaves on the forest floor are classified as:",
            "difficulty": 1,
            "choices": [("Decomposers", True), ("Producers", False), ("Primary consumers", False), ("Herbivores", False)],
            "explanation": "Decomposers (bacteria and fungi) break down dead organic matter, recycling nutrients back into the soil. They are essential to every ecosystem.",
        },
        {
            "text": "Which list correctly orders ecological levels from smallest to largest?",
            "difficulty": 2,
            "choices": [
                ("Individual → Population → Community → Ecosystem → Biosphere", True),
                ("Population → Individual → Ecosystem → Community → Biosphere", False),
                ("Community → Population → Ecosystem → Individual → Biosphere", False),
                ("Ecosystem → Community → Biosphere → Population → Individual", False),
            ],
            "explanation": "The correct order from smallest to largest: Individual → Population (same species) → Community (all species) → Ecosystem (community + abiotic) → Biosphere (all ecosystems).",
        },

        # Lesson 2 – Food Webs and Energy Flow
        {
            "text": "In a food chain — Grass → Rabbit → Fox — the rabbit is a:",
            "difficulty": 1,
            "choices": [("Primary consumer", True), ("Producer", False), ("Secondary consumer", False), ("Decomposer", False)],
            "explanation": "The rabbit eats grass (the producer), making it a primary consumer. The fox eats the rabbit, making it a secondary consumer.",
        },
        {
            "text": "According to the 10% rule, if grasses store 10,000 kcal of energy, how much energy is available to secondary consumers?",
            "difficulty": 2,
            "choices": [("100 kcal", True), ("1,000 kcal", False), ("5,000 kcal", False), ("10,000 kcal", False)],
            "explanation": "Each trophic level passes on only 10% of its energy. Grasses (10,000) → Primary consumers (1,000) → Secondary consumers (100 kcal).",
        },
        {
            "text": "A food web is more accurate than a food chain for representing real ecosystems because:",
            "difficulty": 2,
            "choices": [
                ("Most animals eat more than one type of food, creating overlapping feeding relationships.", True),
                ("Food webs include only producers and consumers.", False),
                ("Food chains show energy loss but food webs do not.", False),
                ("Food webs only apply to aquatic ecosystems.", False),
            ],
            "explanation": "In reality, most animals eat multiple food sources and are eaten by multiple predators. A food web captures these overlapping connections; a single chain cannot.",
        },
        {
            "text": "Why are there always far fewer top predators than producers in an ecosystem?",
            "difficulty": 2,
            "choices": [
                ("Energy is lost at each trophic level, leaving little energy available at the top.", True),
                ("Top predators are larger, so they need fewer individuals.", False),
                ("Producers reproduce more slowly than predators.", False),
                ("Predators are outcompeted by producers for resources.", False),
            ],
            "explanation": "The 10% rule means only 10% of energy passes to each higher level. By the time you reach top predators, so little energy remains that only a small population can be supported.",
        },
        {
            "text": "If rabbits are removed from a food web where foxes eat rabbits and rabbits eat grass, which outcome is MOST likely?",
            "difficulty": 2,
            "choices": [
                ("Fox populations decrease; grass populations increase.", True),
                ("Fox populations increase; grass populations decrease.", False),
                ("Both fox and grass populations stay the same.", False),
                ("Grass populations decrease because rabbits no longer fertilize the soil.", False),
            ],
            "explanation": "Removing rabbits starves the foxes (their prey is gone), so fox numbers fall. Without rabbits grazing, grass is no longer kept in check, so it grows more abundantly.",
        },

        # Lesson 3 – Biodiversity and Ecological Relationships
        {
            "text": "Two bird species compete for the same nest sites in the same forest. Over time, one species is likely to:",
            "difficulty": 2,
            "choices": [
                ("Be driven out or forced to use different nest sites (competitive exclusion).", True),
                ("Evolve to become the same species.", False),
                ("Both increase in population because they share resources.", False),
                ("Switch to a predator–prey relationship.", False),
            ],
            "explanation": "Competitive exclusion: two species cannot occupy the exact same niche indefinitely. One will be excluded or will adapt to use a slightly different resource.",
        },
        {
            "text": "Bees pollinate flowers and receive nectar in return. This relationship is best described as:",
            "difficulty": 1,
            "choices": [("Mutualism", True), ("Parasitism", False), ("Commensalism", False), ("Predation", False)],
            "explanation": "Mutualism = both species benefit. The bee gets food (nectar); the flower gets pollinated (reproduction). Both parties gain.",
        },
        {
            "text": "A tick feeds on a dog's blood, harming the dog but benefiting itself. This is an example of:",
            "difficulty": 1,
            "choices": [("Parasitism", True), ("Mutualism", False), ("Commensalism", False), ("Competition", False)],
            "explanation": "Parasitism = parasite benefits while the host is harmed. The tick (parasite) gets nutrition; the dog (host) loses blood and may get disease.",
        },
        {
            "text": "A keystone species is removed from an ecosystem. Based on the definition of a keystone species, the MOST likely result is:",
            "difficulty": 2,
            "choices": [
                ("Major changes in the structure and biodiversity of the ecosystem.", True),
                ("Only the direct prey of the species is affected.", False),
                ("The ecosystem adapts quickly with no lasting change.", False),
                ("Competing species fill the gap within days.", False),
            ],
            "explanation": "Keystone species have an outsized effect on their ecosystem relative to their numbers. Removing one causes cascading changes — often a collapse of structure and sharp drops in biodiversity.",
        },
        {
            "text": "An invasive fish species is introduced to a lake. It has no natural predators there. The MOST likely immediate effect on the lake ecosystem is:",
            "difficulty": 2,
            "choices": [
                ("The invasive species population grows rapidly and outcompetes native species.", True),
                ("The invasive species quickly develops new predators in the lake.", False),
                ("Native species increase because competition decreases.", False),
                ("The invasive species dies out because it is not adapted to the lake.", False),
            ],
            "explanation": "Without natural predators to control it, an invasive species can reproduce unchecked, consuming food that native species depend on and driving native populations down.",
        },

        # Lesson 4 – Human Impact on Ecosystems
        {
            "text": "Which human activity is the LEADING cause of species extinction worldwide?",
            "difficulty": 1,
            "choices": [("Habitat destruction", True), ("Hunting and poaching", False), ("Climate change", False), ("Pollution", False)],
            "explanation": "Habitat destruction — clearing land for agriculture, logging, and urban development — is the number one cause of biodiversity loss and species extinction globally.",
        },
        {
            "text": "A data table shows mercury concentrations in plankton (0.01 ppm), small fish (0.1 ppm), large fish (1 ppm), and eagles (10 ppm). This pattern is an example of:",
            "difficulty": 2,
            "choices": [("Biomagnification", True), ("Eutrophication", False), ("Bioaccumulation in producers only", False), ("The 10% energy rule", False)],
            "explanation": "Biomagnification: a toxic substance becomes MORE concentrated at higher trophic levels because each organism accumulates the pollutant from everything it eats. Mercury at 10 ppm in eagles vs. 0.01 ppm in plankton is a classic example.",
        },
        {
            "text": "Deforestation increases atmospheric CO₂ levels because:",
            "difficulty": 2,
            "choices": [
                ("Trees absorb CO₂ during photosynthesis; removing them reduces CO₂ uptake.", True),
                ("Trees release CO₂ during photosynthesis.", False),
                ("Deforestation produces nitrogen gas that converts to CO₂.", False),
                ("Deforestation has no effect on atmospheric CO₂.", False),
            ],
            "explanation": "Trees are carbon sinks — they absorb CO₂ from the atmosphere during photosynthesis. When forests are cleared, this absorption is lost, and burning or decomposing wood releases stored carbon back as CO₂.",
        },
        {
            "text": "Habitat fragmentation is considered harmful even when total habitat area is preserved because:",
            "difficulty": 3,
            "choices": [
                ("Small, isolated patches prevent animals from migrating or finding mates, leading to gradual extinction.", True),
                ("Smaller patches contain more predators per acre.", False),
                ("Fragmentation increases the amount of food available per animal.", False),
                ("Isolated patches always experience more pollution.", False),
            ],
            "explanation": "Fragmentation cuts off populations from each other. Without migration, genetic diversity shrinks, inbreeding increases, and small isolated populations can be wiped out by disease or weather — even if some habitat remains.",
        },

        # Lesson 5 – Climate Change and the Greenhouse Effect
        {
            "text": "Which gas is currently the GREATEST contributor to human-caused climate change?",
            "difficulty": 1,
            "choices": [("Carbon dioxide (CO₂)", True), ("Oxygen (O₂)", False), ("Ozone (O₃)", False), ("Nitrogen (N₂)", False)],
            "explanation": "CO₂ released from burning fossil fuels and deforestation is the primary driver of enhanced greenhouse warming. Although methane is more potent per molecule, CO₂ is released in far larger quantities.",
        },
        {
            "text": "How does the greenhouse effect NATURALLY benefit Earth?",
            "difficulty": 2,
            "choices": [
                ("It traps heat in the atmosphere, keeping Earth warm enough to support life.", True),
                ("It blocks all solar radiation from reaching Earth's surface.", False),
                ("It converts CO₂ into oxygen.", False),
                ("It prevents the water cycle from occurring.", False),
            ],
            "explanation": "Without the natural greenhouse effect, Earth's average temperature would be about −18°C (0°F) instead of the current +15°C (59°F) — far too cold for most life. The problem is the ENHANCED effect from extra greenhouse gases.",
        },
        {
            "text": "Which of the following is NOT direct evidence of current climate change?",
            "difficulty": 2,
            "choices": [
                ("An increase in the number of rainy days in one city over three years.", True),
                ("Rising global average temperatures since 1950.", False),
                ("Retreating glaciers in mountain ranges worldwide.", False),
                ("Rising sea levels measured by satellite.", False),
            ],
            "explanation": "Climate is a long-term global pattern; weather in one city over three years is local, short-term weather data — not evidence of global climate change. The other three options represent global, long-term measured trends.",
        },
        {
            "text": "The ozone hole and the greenhouse effect are DIFFERENT environmental problems because:",
            "difficulty": 2,
            "choices": [
                ("The ozone hole concerns UV radiation reaching Earth; the greenhouse effect concerns heat retention.", True),
                ("The ozone hole is caused by CO₂; the greenhouse effect is caused by CFCs.", False),
                ("Both are caused by the same gases but affect different altitudes.", False),
                ("The greenhouse effect is not caused by humans, but the ozone hole is.", False),
            ],
            "explanation": "Ozone depletion (caused mainly by CFCs) allows more harmful UV radiation to reach Earth's surface. The greenhouse effect (caused mainly by CO₂ and CH₄) traps infrared heat. Different gases, different mechanisms, different consequences.",
        },

        # Lesson 6 – Pollution and Natural Resources
        {
            "text": "Acid rain is primarily caused by which air pollutants?",
            "difficulty": 2,
            "choices": [
                ("Sulfur dioxide and nitrogen oxides from burning fossil fuels.", True),
                ("Carbon dioxide and methane from livestock.", False),
                ("Chlorofluorocarbons (CFCs) from refrigerants.", False),
                ("Oxygen and water vapor from natural sources.", False),
            ],
            "explanation": "SO₂ and NOₓ emitted by power plants and vehicles react with water in the atmosphere to form sulfuric and nitric acid, which falls as acid rain, damaging forests and lakes.",
        },
        {
            "text": "Eutrophication of a lake begins when:",
            "difficulty": 2,
            "choices": [
                ("Excess nutrients from fertilizer runoff cause an algae bloom.", True),
                ("Too much sunlight evaporates the water.", False),
                ("Predators remove all the fish from the lake.", False),
                ("Cold temperatures prevent plant growth.", False),
            ],
            "explanation": "Nutrient runoff (especially nitrogen and phosphorus from fertilizers) feeds explosive algae growth. When the algae die, decomposers consume the oxygen, creating dead zones where fish cannot survive.",
        },
        {
            "text": "Which energy source is classified as RENEWABLE?",
            "difficulty": 1,
            "choices": [("Solar energy", True), ("Coal", False), ("Natural gas", False), ("Uranium", False)],
            "explanation": "Solar energy is renewed continuously by the sun and will not run out on any human timescale. Coal, natural gas, and uranium are all nonrenewable — they took millions of years to form and are consumed far faster than they can be replaced.",
        },
        {
            "text": "Microplastics in the ocean are most dangerous because:",
            "difficulty": 2,
            "choices": [
                ("They enter food chains when eaten by small organisms and accumulate up the food web.", True),
                ("They absorb all sunlight, causing ocean temperatures to fall.", False),
                ("They break down quickly into harmless gases.", False),
                ("They are too large for fish to eat.", False),
            ],
            "explanation": "Microplastics (tiny plastic fragments) are ingested by zooplankton, small fish, and filter feeders. They pass up the food chain through biomagnification, eventually reaching humans who eat seafood.",
        },

        # Lesson 7 – Conservation, Sustainability & Data
        {
            "text": "A habitat corridor connects two separated forest patches. The PRIMARY benefit of this corridor is:",
            "difficulty": 2,
            "choices": [
                ("It allows animals to migrate between patches, maintaining genetic diversity.", True),
                ("It creates new habitat by converting farmland to forest.", False),
                ("It acts as a barrier to keep invasive species out.", False),
                ("It removes pollution between the two patches.", False),
            ],
            "explanation": "Corridors let animals move between otherwise isolated habitat fragments, enabling migration, gene flow between populations, and recolonization after local extinctions.",
        },
        {
            "text": "A graph shows global average CO₂ levels and global average temperatures both rising over 50 years. A student concludes CO₂ causes warming. This conclusion is:",
            "difficulty": 3,
            "choices": [
                ("Supported by the data, and also supported by the known physical mechanism (greenhouse effect).", True),
                ("Not supported because correlation never implies causation.", False),
                ("Not valid because only 50 years of data is insufficient.", False),
                ("Invalid because temperature causes CO₂ to rise, not the reverse.", False),
            ],
            "explanation": "While correlation alone does not prove causation, the greenhouse effect is a well-established physical mechanism explaining why CO₂ traps heat. The correlation is consistent with the known science, making the conclusion well-supported.",
        },
        {
            "text": "Sustainable fishing limits set catches BELOW the species' reproduction rate. The purpose of this practice is to:",
            "difficulty": 2,
            "choices": [
                ("Ensure the fish population can replenish itself so fishing can continue long-term.", True),
                ("Raise fish prices by creating an artificial shortage.", False),
                ("Reduce the total number of fish species in the ocean.", False),
                ("Prevent decomposers from breaking down dead fish.", False),
            ],
            "explanation": "Sustainability means using resources no faster than they replenish. Setting catch limits below reproduction rates keeps the population stable, protecting both the ecosystem and the fishing industry over the long term.",
        },
        {
            "text": "Which statement about reading environmental data graphs is MOST useful on the GED Science test?",
            "difficulty": 1,
            "choices": [
                ("Always read the axis labels and units before interpreting any trend.", True),
                ("Assume the y-axis starts at zero unless the question says otherwise.", False),
                ("A rising line always indicates a harmful environmental change.", False),
                ("Units are not important as long as the trend is clear.", False),
            ],
            "explanation": "Axis labels and units are the first thing to check — a graph of 'temperature in °C vs. year' and one of 'temperature in °F vs. year' tell very different stories if misread. Always orient yourself before drawing conclusions.",
        },
    ],
}


class Command(BaseCommand):
    help = "Seed GED Science: Environmental Science & Human Impact course"

    def handle(self, *args, **options):
        course, _ = Course.objects.update_or_create(
            slug=COURSE["slug"],
            defaults={
                "title": COURSE["title"],
                "program": COURSE["program"],
                "subject": COURSE["subject"],
                "description": COURSE["description"],
            },
        )
        course.lessons.all().delete()
        for order, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=order)

        course.questions.all().delete()
        for item in COURSE["mcqs"]:
            q = Question.objects.create(
                course=course,
                text=item["text"],
                qtype="mcq",
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=q, text=text, is_correct=is_correct)

        lesson_count = len(COURSE["lessons"])
        question_count = len(COURSE["mcqs"])
        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with {lesson_count} lessons and {question_count} questions."
            )
        )
