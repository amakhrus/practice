"""
Seed data: 'GED Science: Earth's Water & the Water Cycle (Deep Dive)'.

A focused EXPANSION of Lesson 4 ("Earth's Water & the Water Cycle") from the
broader 'GED Science: Earth & Space Science' course. The parent course gives a
one-lesson overview of evaporation/condensation/precipitation/collection; this
course goes deeper:

  1. Where Earth's water actually is (salt vs. fresh; most fresh water is frozen).
  2. The full water cycle loop, including transpiration, runoff, and infiltration.
  3. The physics: changes of state and the energy (latent heat) that powers it.
  4. Clouds and precipitation -- how rising, cooling air makes clouds and rain.
  5. Water on land -- watersheds, infiltration, the water table, and aquifers.
  6. Humans and the water cycle -- fresh water as a limited resource, watersheds,
     conservation, and reading water data.

This course uses ALL-NEW diagrams (water distribution, a detailed water-cycle
loop, water's changes of state, cloud formation, and a groundwater/aquifer
cross-section) rather than reusing the parent course's 'water_cycle' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - U.S. Geological Survey (USGS) Water Science School, "The Water Cycle" and
    "How Much Water Is There on Earth?" (distribution figures used here).
  - NOAA National Weather Service / JetStream -- cloud formation, precipitation.
  - Tarbuck, E. & Lutgens, F., *Earth Science* (Pearson).
  - National Geographic Society, Resource Library: "water cycle," "aquifer."
Distribution figures (rounded for learners): ~71% of Earth's surface is water;
about 97% of all water is salt water; of the ~3% fresh, roughly 69% is ice/glaciers
and 30% is groundwater, leaving ~1% in lakes, rivers, and the atmosphere.

Run:
    python manage.py seed_ged_water_cycle
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Earth's Water & the Water Cycle (Deep Dive)",
    "slug": "ged-water-cycle",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into Earth's water, expanding the single 'Earth's Water & the Water Cycle' lesson "
        "from the GED Earth & Space Science course into a full mini-course. You'll see where Earth's "
        "water really is (and why so little is usable), follow the full water cycle from the ocean to "
        "the clouds and back into the ground, and learn the physics of how water changes state and "
        "stores energy. You'll also explore clouds and precipitation, groundwater and aquifers, and why "
        "fresh water is a limited resource worth protecting. Plain language, all-new labeled diagrams, "
        "common-misconception warnings, and GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. Earth's Water: Where It All Is",
            r"Earth is the 'blue planet': about **71%** of its surface is covered by water. With that much water, it's tempting to think we'll never run short. But look closer at *where* the water is, and the picture changes." "\n\n"
            r"[[figure:water_distribution|Almost all of Earth's water is salty ocean; the small fresh-water slice is mostly frozen, leaving only a sliver in lakes and rivers.]]" "\n\n"
            r"Scientists describe the water cycle in terms of **reservoirs** — places where water is stored:" "\n"
            r"- **Oceans** hold about **97%** of all of Earth's water — but it is **salt water**, which we cannot drink or use on crops without treatment." "\n"
            r"- That leaves only about **3%** as **fresh water**. And most of *that* is **frozen** in ice caps and glaciers (~69%) or buried as **groundwater** (~30%)." "\n"
            r"- Only about **1% of the fresh water** — a tiny sliver of all water — sits in the **lakes, rivers, and atmosphere** we most easily use." "\n\n"
            r"So the 'blue planet' actually has very little easy-to-reach fresh water, which is why it must be used carefully (Lesson 6)." "\n\n"
            r"⚠️ Common misconception: 'Earth has plenty of water, so fresh water can't run out.' Most water is **salty**, and most fresh water is **frozen** — the usable part is small and unevenly spread around the world." "\n\n"
            r"💡 Tip: remember the chain **salty ocean (most) → fresh (little) → and most fresh water is frozen.**",
        ),
        (
            "2. The Water Cycle: The Big Loop",
            r"Earth's water is always on the move, recycled endlessly through the **water cycle**. Two things power the loop: the **Sun** (which supplies the energy) and **gravity** (which pulls water back down)." "\n\n"
            r"[[figure:water_cycle_detailed|Water rises by evaporation and transpiration, condenses into clouds, falls as precipitation, then runs off or soaks into the ground.]]" "\n\n"
            r"Trace the journey:" "\n"
            r"- **Evaporation** — the Sun heats surface water (oceans, lakes) and turns it into invisible **water vapor** that rises." "\n"
            r"- **Transpiration** — plants release water vapor from their leaves too. (Evaporation + transpiration together are called **evapotranspiration**.)" "\n"
            r"- **Condensation** — high up, cooler air turns the vapor back into tiny droplets that form **clouds**." "\n"
            r"- **Precipitation** — droplets join, grow heavy, and fall as **rain, snow, sleet, or hail**." "\n"
            r"- **Collection** — fallen water gathers. Some flows over the surface as **runoff** into streams and oceans; some soaks into the ground as **infiltration**, becoming groundwater. Then the cycle repeats." "\n\n"
            r"⚠️ Common misconception: the water cycle does **not** create new water. The **same** water is recycled again and again — the water you drink today is the same water dinosaurs once drank." "\n\n"
            r"💡 Tip: follow the loop with the Sun as the engine — **evaporate up, condense into clouds, precipitate down, then run off or soak in, repeat.**",
        ),
        (
            "3. Changes of State & the Energy Behind Them",
            r"The water cycle works because water easily changes between **three states** — solid (ice), liquid (water), and gas (water vapor) — at the everyday temperatures found on Earth. Each change involves **energy**." "\n\n"
            r"[[figure:water_phase_changes|Adding energy moves water toward gas (melting, evaporation); releasing energy moves it toward solid (condensation, freezing).]]" "\n\n"
            r"- **Evaporation** (liquid → gas) **absorbs** energy. That's why evaporating sweat **cools** your skin — it carries heat away." "\n"
            r"- **Condensation** (gas → liquid) **releases** that stored energy back into the air. This released heat is a major fuel for clouds and storms." "\n"
            r"- **Melting** (solid → liquid) absorbs energy; **freezing** (liquid → solid) releases it." "\n\n"
            r"The **Sun** is the energy source that lifts water into the air; gravity later brings it back. And note: **water vapor is an invisible gas**. The white 'steam' you see above a kettle or as clouds is not vapor — it is vapor that has already **condensed** into tiny visible droplets." "\n\n"
            r"⚠️ Common misconception: clouds and 'steam' are **not** water vapor. Water vapor is invisible; what you see are tiny **liquid droplets** (or ice crystals) that formed when vapor condensed." "\n\n"
            r"💡 Tip: **add energy → toward gas; remove energy → toward solid.** Evaporation cools (absorbs heat); condensation warms the air (releases heat).",
        ),
        (
            "4. Clouds, Precipitation & the Sky",
            r"Where do clouds actually come from? The key is **rising air**. When air near the warm ground rises, it expands and **cools** as it goes up. Cooler air can hold less water vapor, so at a certain height — the **dew point** — the vapor **condenses** onto tiny floating particles (dust, salt, smoke) to make **cloud droplets**." "\n\n"
            r"[[figure:cloud_formation|Warm, moist air rises and cools; at the dew point its vapor condenses on tiny particles, forming a cloud.]]" "\n\n"
            r"Clouds come in families you can learn to read:" "\n"
            r"- **Cumulus** — puffy, cotton-like fair-weather clouds (but they can grow into storm clouds)." "\n"
            r"- **Stratus** — flat, gray layers that often bring drizzle." "\n"
            r"- **Cirrus** — thin, wispy, high clouds made of ice crystals." "\n\n"
            r"When droplets grow big and heavy enough, gravity wins and they fall as **precipitation**: **rain** (liquid), **snow** (ice crystals), **sleet** (frozen rain), or **hail** (layered ice from strong storm updrafts). This is the step that returns the cycle's water to the surface." "\n\n"
            r"⚠️ Common misconception: **dew and fog are not precipitation.** Precipitation must **fall** from clouds. Dew is condensation on cool surfaces, and fog is a cloud sitting at ground level — neither falls from the sky." "\n\n"
            r"💡 Tip: clouds form when **rising air cools to its dew point** and vapor condenses; precipitation is condensed water heavy enough to **fall**.",
        ),
        (
            "5. Water on Land: Watersheds, Groundwater & Aquifers",
            r"Once precipitation reaches the ground, it goes two main ways: it **runs off** the surface, or it **soaks in**." "\n\n"
            r"Water that runs off flows downhill into streams and rivers. All the land that drains into a particular river or lake is its **watershed** (or drainage basin). Everything that happens on that land — including pollution — can end up in the shared water downstream." "\n\n"
            r"[[figure:groundwater_aquifer|Rain infiltrates and fills the spaces between underground grains; the top of the saturated zone is the water table, and a usable saturated layer is an aquifer.]]" "\n\n"
            r"Water that soaks in becomes **groundwater**. Underground it fills the tiny spaces between soil and rock:" "\n"
            r"- Near the surface is the **unsaturated zone**, where the gaps hold both air and water." "\n"
            r"- Deeper down, the gaps are completely full of water — the **saturated zone**." "\n"
            r"- The boundary between them is the **water table** (it rises in wet seasons and falls in droughts)." "\n"
            r"- A layer of saturated rock or sediment that can store and supply usable water is an **aquifer**. We reach it by drilling a **well** below the water table; where it meets the surface naturally, a **spring** flows." "\n\n"
            r"⚠️ Common misconception: groundwater is **not** a hidden underground 'lake' or river (except in rare caves). It mostly fills the **pore spaces** between grains of rock and soil, like water in a sponge." "\n\n"
            r"💡 Tip: runoff fills **rivers** (and defines a **watershed**); infiltration fills the spaces underground, and the top of the fully wet zone is the **water table**.",
        ),
        (
            "6. Humans & the Water Cycle: Resources & Data",
            r"The water cycle isn't just nature's plumbing — it's where our drinking water, farms, and cities get their supply. And because usable fresh water is scarce (Lesson 1), how we treat the cycle matters." "\n\n"
            r"[[figure:water_distribution|A reminder of why fresh water is limited: most water is salty, and most fresh water is frozen.]]" "\n\n"
            r"- **Fresh water is a limited resource.** Even on the 'blue planet,' only about 1% of all water is easily usable, and it is spread unevenly, so some regions face shortages and droughts." "\n"
            r"- **Watersheds connect us.** Because water flows through a connected watershed, pollution dumped upstream can harm drinking water, farms, and wildlife far downstream." "\n"
            r"- **Conservation works.** Fixing leaks, using efficient appliances, and protecting watersheds keep fresh water available." "\n\n"
            r"**Reading water data (a GED skill).** GED items often show a graph or table — water use over time, a river's flow after a storm (a hydrograph), or evaporation versus temperature. Read the **title, axis labels, and units** first, find the **trend**, and conclude only what the data shows. For example, if a graph shows **evaporation rising as temperature rises**, the supported conclusion is that **warmer temperatures speed up evaporation**." "\n\n"
            r"⚠️ Common misconception: 'one country's water use can't affect anyone else.' Within a shared **watershed** (and through the global cycle), water — and pollution — is connected across farms, cities, and borders." "\n\n"
            r"💡 Tip: for any water graph, read the **axes and units**, name the **trend**, and don't claim more than the data shows." "\n\n"
            r"📚 Sources: USGS Water Science School (*The Water Cycle*; *How Much Water Is There on Earth?*); NOAA National Weather Service / JetStream; Tarbuck & Lutgens, *Earth Science*.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: distribution ---
        {
            "text": r"About what fraction of Earth's surface is covered by water?",
            "difficulty": 1,
            "choices": [("About 71%", True), ("About 10%", False),
                        ("About 30%", False), ("About 95%", False)],
            "explanation": r"Water covers roughly 71% of Earth's surface, which is why Earth is called the 'blue planet.'",
        },
        {
            "text": r"Most of Earth's water is found in:",
            "difficulty": 1,
            "choices": [("The salty oceans", True), ("Rivers and lakes", False),
                        ("Clouds in the sky", False), ("Underground caves", False)],
            "explanation": r"About 97% of Earth's water is salt water in the oceans. Only about 3% is fresh water.",
        },
        {
            "text": r"Only about 3% of Earth's water is fresh water. Where is most of that fresh water located?",
            "difficulty": 2,
            "choices": [("Frozen in ice caps and glaciers", True),
                        ("Flowing in rivers", False),
                        ("Floating in clouds", False),
                        ("Inside living things", False)],
            "explanation": r"Most fresh water (about 69%) is locked up frozen in ice caps and glaciers; most of the rest is groundwater. Only a tiny share is in lakes and rivers.",
        },
        {
            "text": ("Use the water distribution diagram.\n\n"
                     "[[figure:water_distribution|How Earth's water is divided]]\n\n"
                     "Based on the diagram, the water humans most easily use (lakes and rivers) makes up:"),
            "difficulty": 2,
            "choices": [("A very small fraction of all of Earth's water", True),
                        ("About half of all of Earth's water", False),
                        ("Most of Earth's water", False),
                        ("None of Earth's water", False)],
            "explanation": r"The diagram shows lakes and rivers as roughly 1% of the 3% that is fresh — a tiny sliver of all water. Pro tip: most water is salty, and most fresh water is frozen.",
        },
        {
            "text": r"In the water cycle, the term 'reservoir' means:",
            "difficulty": 2,
            "choices": [("A place where water is stored, such as the ocean, ice, or groundwater", True),
                        ("A machine that makes new water", False),
                        ("A type of cloud", False),
                        ("The energy that drives the cycle", False)],
            "explanation": r"A reservoir is any place water is stored — oceans, glaciers, groundwater, lakes, or the atmosphere. Water moves between these reservoirs as it cycles.",
        },
        # --- Lesson 2: the loop ---
        {
            "text": r"What is the main source of ENERGY that powers the water cycle?",
            "difficulty": 1,
            "choices": [("The Sun", True), ("Earth's core", False),
                        ("The Moon", False), ("Ocean waves", False)],
            "explanation": r"The Sun's energy heats surface water and drives evaporation, powering the whole cycle. Gravity then pulls water back down.",
        },
        {
            "text": r"Evaporation is the process in which:",
            "difficulty": 1,
            "choices": [("Liquid water turns into water vapor and rises", True),
                        ("Water vapor turns into liquid droplets", False),
                        ("Water falls from clouds as rain", False),
                        ("Water soaks into the ground", False)],
            "explanation": r"Evaporation is liquid water becoming vapor and rising. Condensation is the reverse; precipitation is water falling; infiltration is water soaking in.",
        },
        {
            "text": r"The release of water vapor from plants, mainly through their leaves, is called:",
            "difficulty": 2,
            "choices": [("Transpiration", True), ("Condensation", False),
                        ("Precipitation", False), ("Infiltration", False)],
            "explanation": r"Transpiration is water vapor released by plants. Together with evaporation it is sometimes called evapotranspiration.",
        },
        {
            "text": r"Water soaking down from the surface into the ground is called:",
            "difficulty": 2,
            "choices": [("Infiltration", True), ("Runoff", False),
                        ("Evaporation", False), ("Condensation", False)],
            "explanation": r"Infiltration is water soaking into the ground (where it becomes groundwater). Runoff is water flowing over the surface instead.",
        },
        {
            "text": ("Use the water cycle diagram.\n\n"
                     "[[figure:water_cycle_detailed|The full water cycle loop]]\n\n"
                     "In the diagram, water flowing over the land surface back toward the ocean in rivers is called:"),
            "difficulty": 2,
            "choices": [("Runoff", True), ("Evaporation", False),
                        ("Transpiration", False), ("Condensation", False)],
            "explanation": r"Water that flows over the surface into streams and rivers is runoff. Pro tip: runoff travels over the surface; infiltration soaks in.",
        },
        {
            "text": r"Why do scientists say the water cycle does not create any new water?",
            "difficulty": 2,
            "choices": [("The same water is recycled over and over between reservoirs", True),
                        ("New water is made by the Sun each day", False),
                        ("Rain is always brand-new water", False),
                        ("Water is destroyed when it evaporates", False)],
            "explanation": r"The water cycle just moves the same water around — evaporating, condensing, falling, and collecting. No new water is made; the water on Earth today is billions of years old.",
        },
        # --- Lesson 3: states & energy ---
        {
            "text": r"When water vapor cools and turns back into tiny liquid droplets, the process is:",
            "difficulty": 1,
            "choices": [("Condensation", True), ("Evaporation", False),
                        ("Melting", False), ("Infiltration", False)],
            "explanation": r"Condensation is gas turning into liquid (vapor to droplets), which is how clouds form. Evaporation is the reverse.",
        },
        {
            "text": r"Clouds are made of:",
            "difficulty": 2,
            "choices": [("Tiny liquid water droplets (and ice crystals)", True),
                        ("Invisible water vapor", False),
                        ("Pure oxygen gas", False),
                        ("Dry dust only", False)],
            "explanation": r"Clouds are visible because they are made of tiny condensed water droplets and ice crystals — not water vapor, which is an invisible gas.",
        },
        {
            "text": r"When water evaporates from your skin, it makes you feel cooler. This is because evaporation:",
            "difficulty": 2,
            "choices": [("Absorbs heat energy, carrying it away from your skin", True),
                        ("Releases heat energy onto your skin", False),
                        ("Adds new water to your skin", False),
                        ("Freezes the water instantly", False)],
            "explanation": r"Evaporation absorbs energy (it takes heat to turn liquid into vapor). That heat is carried away with the vapor, cooling your skin.",
        },
        {
            "text": r"The white 'steam' you see above a boiling kettle is actually:",
            "difficulty": 3,
            "choices": [("Water vapor that has condensed into tiny visible droplets", True),
                        ("Pure invisible water vapor", False),
                        ("Smoke from the kettle", False),
                        ("Oxygen released from the water", False)],
            "explanation": r"Water vapor itself is invisible. The visible white cloud is vapor that has already cooled and condensed into tiny liquid droplets.",
        },
        {
            "text": r"When water vapor condenses into clouds, energy is:",
            "difficulty": 3,
            "choices": [("Released into the air, which can help power storms", True),
                        ("Absorbed from the air, cooling it", False),
                        ("Created from nothing", False),
                        ("Turned into new water", False)],
            "explanation": r"Condensation releases the energy that evaporation absorbed earlier. That released heat is an important energy source for clouds and storms.",
        },
        # --- Lesson 4: clouds & precipitation ---
        {
            "text": r"Precipitation is best defined as:",
            "difficulty": 1,
            "choices": [("Water that falls from clouds as rain, snow, sleet, or hail", True),
                        ("Water vapor rising into the air", False),
                        ("Water soaking into the soil", False),
                        ("Dew forming on grass", False)],
            "explanation": r"Precipitation is condensed water that becomes heavy enough to fall from clouds — rain, snow, sleet, or hail.",
        },
        {
            "text": r"Clouds form when:",
            "difficulty": 2,
            "choices": [("Rising air cools and its water vapor condenses around tiny particles", True),
                        ("Sinking air warms and dries out", False),
                        ("Groundwater rises to the surface", False),
                        ("Rivers flow into the ocean", False)],
            "explanation": r"As air rises it cools to its dew point; the vapor then condenses onto tiny floating particles, forming cloud droplets.",
        },
        {
            "text": r"Why does air that rises tend to form clouds?",
            "difficulty": 2,
            "choices": [("As it rises it cools, and cooler air forces its vapor to condense", True),
                        ("Rising air gets hotter and wetter", False),
                        ("Rising air gains brand-new water", False),
                        ("Rising air sinks back down immediately", False)],
            "explanation": r"Rising air expands and cools. Cool air holds less vapor, so at the dew point the vapor condenses into cloud droplets.",
        },
        {
            "text": r"Which of the following is NOT a form of precipitation?",
            "difficulty": 3,
            "choices": [("Dew", True), ("Snow", False),
                        ("Sleet", False), ("Hail", False)],
            "explanation": r"Precipitation must fall from clouds (snow, sleet, hail, rain). Dew is condensation that forms directly on cool surfaces — it doesn't fall, so it isn't precipitation.",
        },
        {
            "text": ("Use the cloud formation diagram.\n\n"
                     "[[figure:cloud_formation|Warm, moist air rising and cooling to form a cloud]]\n\n"
                     "According to the diagram, the cloud forms at the height where:"),
            "difficulty": 2,
            "choices": [("The rising air cools to its dew point and vapor condenses", True),
                        ("The air sinks and warms up", False),
                        ("Groundwater reaches the surface", False),
                        ("The Sun's rays are blocked", False)],
            "explanation": r"The diagram marks the condensation level (dew point), where rising, cooling air can no longer hold its vapor, so droplets form. Pro tip: clouds form where rising air hits the dew point.",
        },
        # --- Lesson 5: water on land ---
        {
            "text": r"Water that soaks into the ground and fills the spaces between soil and rock is called:",
            "difficulty": 1,
            "choices": [("Groundwater", True), ("Runoff", False),
                        ("Precipitation", False), ("Vapor", False)],
            "explanation": r"Groundwater is water stored underground in the pore spaces of soil and rock. Runoff, by contrast, flows over the surface.",
        },
        {
            "text": r"The boundary marking the top of the zone where the ground is completely saturated with water is the:",
            "difficulty": 2,
            "choices": [("Water table", True), ("Watershed", False),
                        ("Dew point", False), ("Aquifer cap", False)],
            "explanation": r"The water table is the top of the saturated zone. It rises in wet periods and drops during droughts.",
        },
        {
            "text": r"An underground layer of rock or sediment that stores and supplies usable groundwater is a(n):",
            "difficulty": 2,
            "choices": [("Aquifer", True), ("Glacier", False),
                        ("Estuary", False), ("Reservoir cloud", False)],
            "explanation": r"An aquifer is a saturated layer that can store and yield water to wells and springs.",
        },
        {
            "text": ("Use the groundwater diagram.\n\n"
                     "[[figure:groundwater_aquifer|A cross-section of the ground showing the water table and an aquifer]]\n\n"
                     "Based on the diagram, a well must be drilled below the ______ to reach water."),
            "difficulty": 2,
            "choices": [("Water table", True), ("Cloud base", False),
                        ("Mountain peak", False), ("Ocean surface", False)],
            "explanation": r"Below the water table the ground is fully saturated, so a well must reach below it to pump water. Pro tip: above the water table = unsaturated; below it = saturated.",
        },
        {
            "text": r"All of the land area that drains into a particular river or lake is called its:",
            "difficulty": 2,
            "choices": [("Watershed (drainage basin)", True), ("Aquifer", False),
                        ("Water table", False), ("Estuary", False)],
            "explanation": r"A watershed (drainage basin) is all the land whose runoff drains to a common river or lake. What happens on that land affects the shared water.",
        },
        # --- Lesson 6: humans, resources & data ---
        {
            "text": r"Even though about 71% of Earth is covered in water, fresh water is considered a limited resource because:",
            "difficulty": 2,
            "choices": [("Most water is salty or frozen, leaving little that is easily usable", True),
                        ("Water is constantly destroyed and lost forever", False),
                        ("Plants drink almost all of it", False),
                        ("The Sun evaporates all fresh water each day", False)],
            "explanation": r"About 97% of water is salty, and most fresh water is frozen in ice. Only roughly 1% of all water is the easily usable fresh water in lakes, rivers, and the atmosphere.",
        },
        {
            "text": r"Pollution dumped in one part of a watershed can affect water far downstream because:",
            "difficulty": 2,
            "choices": [("Water flows through the connected watershed, carrying pollutants along", True),
                        ("Pollution evaporates and never moves", False),
                        ("Each part of a river is completely separate", False),
                        ("Downstream water flows back uphill", False)],
            "explanation": r"A watershed is connected by flowing water, so contaminants introduced upstream are carried downstream to other users and ecosystems.",
        },
        {
            "text": r"Which action would best help conserve fresh water?",
            "difficulty": 2,
            "choices": [("Fixing leaks and using water-efficient appliances", True),
                        ("Leaving taps running while not in use", False),
                        ("Pouring chemicals into a storm drain", False),
                        ("Watering lawns at midday in the heat", False)],
            "explanation": r"Reducing waste — fixing leaks and using efficient appliances — conserves limited fresh water. The other options waste or pollute it.",
        },
        {
            "text": ("A graph shows that as air temperature rises, the rate of evaporation from a lake also rises.\n\n"
                     "What conclusion does the data best support?"),
            "difficulty": 3,
            "choices": [("Warmer temperatures tend to speed up evaporation", True),
                        ("Evaporation has nothing to do with temperature", False),
                        ("Colder temperatures speed up evaporation", False),
                        ("Evaporation makes the air colder forever", False)],
            "explanation": r"The graph shows evaporation increasing along with temperature, so it supports the conclusion that higher temperatures speed up evaporation. Use only what the data shows.",
        },
    ],
    "essays": [
        {
            "text": (
                "Trace a single drop of water through the water cycle, starting in the ocean. Name and describe "
                "each major step it goes through, explain the role the Sun plays, and explain why we say the water "
                "cycle does not create any new water."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) evaporation -- the Sun heats ocean water into vapor that rises; "
                "(2) condensation -- the vapor cools and forms clouds; (3) precipitation -- water falls as rain or "
                "snow; (4) collection -- water returns via runoff to rivers/oceans or infiltrates as groundwater, then "
                "the cycle repeats; (5) the Sun is the energy source and the same water is recycled, never created. "
                "Deduct for missing steps or omitting the Sun's role."
            ),
        },
        {
            "text": (
                "Although about 71% of Earth's surface is covered by water, fresh water is a limited resource. "
                "Explain where Earth's water is stored (salt vs. fresh, and where the fresh water is), why so little "
                "is easily usable, and why protecting watersheds and conserving water matter."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) about 97% of water is salt water in oceans; (2) only ~3% is fresh, and most of "
                "that is frozen in ice/glaciers or stored as groundwater; (3) only ~1% of fresh water (a tiny sliver "
                "of all water) is easily usable in lakes, rivers, and the atmosphere; (4) because the supply is small "
                "and unevenly distributed, and watersheds connect users, pollution and overuse upstream affect others "
                "-- so conservation and watershed protection matter. Deduct for implying fresh water is unlimited."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Earth's Water & the Water Cycle (Deep Dive)' course."

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
