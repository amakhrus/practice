"""
Seed data: 'GED Science: Weather, Climate & the Atmosphere (Deep Dive)'.

A focused EXPANSION of Lesson 5 ("Weather, Climate & the Atmosphere") from the
broader 'GED Science: Earth & Space Science' course. The parent course gives a
one-lesson overview; this course goes deeper:

  1. The atmosphere -- what air is made of and what it does for us.
  2. The layers of the atmosphere and how temperature changes with altitude.
  3. The Sun, uneven heating, and how heat moves (radiation, conduction, convection).
  4. Air pressure, wind, and circulation (highs/lows, the sea breeze, Coriolis).
  5. Water in the air -- humidity, air masses, fronts, and storms.
  6. Weather vs. climate, what shapes climate, the greenhouse effect, and reading
     weather data.

This course uses ALL-NEW diagrams (atmospheric composition, a layered atmosphere
with a temperature profile, the three modes of heat transfer, a sea-breeze
pressure/wind diagram, cold vs. warm fronts, and the greenhouse effect) rather
than reusing the parent course's 'atmosphere_layers' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - NOAA National Weather Service / JetStream (online weather school) -- layers,
    fronts, pressure and wind, storms.
  - NASA Global Climate Change / Earth Observatory -- greenhouse effect, CO2.
  - Tarbuck, E. & Lutgens, F., *Earth Science* (Pearson); Ahrens, *Meteorology Today*.
  - UCAR Center for Science Education -- atmosphere and climate basics.
Composition figures (dry air, rounded): nitrogen ~78%, oxygen ~21%, argon ~0.93%,
carbon dioxide ~0.04%; water vapor varies (0-4%) and is excluded from "dry air."

Run:
    python manage.py seed_ged_weather_atmosphere
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Weather, Climate & the Atmosphere (Deep Dive)",
    "slug": "ged-weather-atmosphere",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the air around us, expanding the single 'Weather, Climate & the Atmosphere' "
        "lesson from the GED Earth & Space Science course into a full mini-course. You'll learn what air "
        "is made of and how the atmosphere is layered, how the Sun's uneven heating sets the air in "
        "motion, and how pressure, wind, humidity, and fronts combine to make our weather. You'll also "
        "tell weather apart from climate, see how the greenhouse effect keeps Earth warm, and practice "
        "reading weather data. Plain language, all-new labeled diagrams, common-misconception warnings, "
        "and GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. The Atmosphere: Earth's Blanket of Air",
            r"Earth is wrapped in a thin blanket of gases we call the **atmosphere**. It is invisible, but it does an enormous amount of work: it gives us air to breathe, holds in warmth, shields us from harmful radiation and most incoming meteors, and creates the pressure that lets liquid water exist." "\n\n"
            r"[[figure:atmosphere_composition|Dry air is about 78% nitrogen and 21% oxygen, with roughly 1% other gases — including the small but important carbon dioxide.]]" "\n\n"
            r"What is air made of? For **dry air**:" "\n"
            r"- **Nitrogen (N₂)** — about **78%**. The most common gas; fairly unreactive." "\n"
            r"- **Oxygen (O₂)** — about **21%**. The gas animals need to breathe." "\n"
            r"- **Other gases** — about **1%**, mostly **argon** (~0.93%), plus a trace of **carbon dioxide** (~0.04%) and others." "\n\n"
            r"Two gases that are small in amount but big in effect are **carbon dioxide** and **water vapor**: both are **greenhouse gases** that help keep Earth warm (Lesson 6). Water vapor is so variable (0–4%) that it's usually left out when we list the percentages of 'dry air.'" "\n\n"
            r"⚠️ Common misconception: air is **mostly oxygen**. In fact it is mostly **nitrogen** (~78%); oxygen is only about a fifth of the air." "\n\n"
            r"💡 Tip: remember **'78 nitrogen, 21 oxygen, 1 everything else.'** The big two add up to about 99%.",
        ),
        (
            "2. The Layers of the Atmosphere",
            r"The atmosphere isn't the same all the way up — it is built in **layers**, and the temperature rises and falls as you climb through them. From the ground up:" "\n\n"
            r"[[figure:atmosphere_layers_detailed|The four main layers and how temperature changes with altitude — falling, then rising, then falling, then rising.]]" "\n\n"
            r"- **Troposphere** (0 to ~12 km) — where we live and where nearly all **weather and clouds** happen. Temperature **drops** as you go up." "\n"
            r"- **Stratosphere** (~12–50 km) — holds the **ozone layer**, which absorbs the Sun's harmful **ultraviolet (UV)** rays. Because the ozone warms it, temperature **rises** with height. It's calm and stable, so jets like to cruise here." "\n"
            r"- **Mesosphere** (~50–85 km) — the coldest layer, where most **meteors burn up**, making 'shooting stars.' Temperature **drops** again." "\n"
            r"- **Thermosphere** (~85–600 km) — very thin air that the Sun heats to high temperatures; home to the **auroras** and the orbiting space station. Temperature **rises** sharply." "\n\n"
            r"⚠️ Common misconception: the temperature does **not** simply keep dropping the higher you go. It falls in the troposphere, but **rises** in the stratosphere (thanks to ozone) before falling again — the profile zig-zags." "\n\n"
            r"💡 Tip: bottom to top — **Tropo (weather), Strato (ozone), Meso (meteors), Thermo (auroras).** Temperature falls, rises, falls, rises.",
        ),
        (
            "3. The Sun, Uneven Heating & How Heat Moves",
            r"Almost all weather is, at heart, the atmosphere moving heat around — and the heat comes from the **Sun**. The key is that the Sun heats Earth **unevenly**." "\n\n"
            r"- The **equator** gets more direct sunlight than the **poles**, so it is warmer." "\n"
            r"- **Land** heats and cools faster than **water**." "\n"
            r"- The **day** side warms while the **night** side cools." "\n\n"
            r"This uneven heating creates temperature differences, and nature always tries to even them out by **moving heat** — which sets the air and oceans in motion. Heat moves in three ways:" "\n\n"
            r"[[figure:heat_transfer|Radiation carries heat through empty space; conduction moves it through direct contact; convection carries it in a moving fluid.]]" "\n\n"
            r"- **Radiation** — heat travels as rays through empty space (how the Sun's energy reaches Earth)." "\n"
            r"- **Conduction** — heat passes by **direct contact**, atom to atom (a metal spoon heating up in hot soup)." "\n"
            r"- **Convection** — heat is carried by a **moving fluid**: warm air or water rises, cool air or water sinks, forming a circulating loop. Convection is the main engine of winds and weather." "\n\n"
            r"⚠️ Common misconception: the seasons and weather are **not** caused by Earth getting closer to or farther from the Sun. What matters is how **directly** sunlight strikes a place and how that uneven heating moves the air." "\n\n"
            r"💡 Tip: **Radiation = through space; Conduction = through contact; Convection = through a moving fluid.** Convection drives the winds.",
        ),
        (
            "4. Air Pressure, Wind & Circulation",
            r"Air has weight, and the air pressing down creates **air pressure**. Differences in pressure are what make the **wind** blow." "\n\n"
            r"When air is heated it expands, becomes less dense, and **rises**, leaving **low pressure (L)** below — air rising and cooling often makes clouds and stormy weather. Where air cools, it grows denser and **sinks**, creating **high pressure (H)** — usually clear, fair weather. Air then flows along the surface **from high pressure to low pressure**, and that moving air is **wind**." "\n\n"
            r"[[figure:pressure_wind|By day the land warms faster than the sea: warm air rises over land (low), cool air sinks over the sea (high), and the surface wind blows from sea to land.]]" "\n\n"
            r"A **sea breeze** is a perfect everyday example. On a sunny day the **land heats faster than the water**, so air rises over the land (low pressure) while cooler, denser air sits over the sea (high pressure). The result is a refreshing surface wind blowing **from the sea toward the land**." "\n\n"
            r"On the scale of the whole planet, this rising-and-sinking sets up giant **convection cells** and global wind belts (like the trade winds). Because the Earth **rotates**, moving air is deflected and curves — the **Coriolis effect** — which is why large weather systems spin." "\n\n"
            r"⚠️ Common misconception: wind does **not** blow from low to high pressure. Air always moves **from high pressure to low pressure** (think of air rushing out of a popped balloon — from high inside to low outside)." "\n\n"
            r"💡 Tip: **rising air → low pressure → clouds/storms; sinking air → high pressure → fair weather; wind blows High → Low.**",
        ),
        (
            "5. Water in the Air: Humidity, Fronts & Storms",
            r"Add **water** to moving air and you get most of our dramatic weather. The amount of water vapor in the air is its **humidity**; when the air can hold no more, it is saturated and water condenses into clouds, fog, or rain." "\n\n"
            r"Large bodies of air with similar temperature and humidity are called **air masses** (for example, a cold, dry mass from the north or a warm, moist mass from the south). Where two different air masses meet, the boundary is a **front**, and fronts are where the weather changes." "\n\n"
            r"[[figure:weather_fronts|At a cold front, cold air shoves warm air up fast (tall storm clouds); at a warm front, warm air glides up slowly (wide layered clouds).]]" "\n\n"
            r"- **Cold front** — a cold air mass pushes **under** a warm one, forcing the warm air up **quickly**. This builds tall clouds and often brief, **heavy thunderstorms**, followed by cooler, clearer air." "\n"
            r"- **Warm front** — a warm air mass slides **up and over** a retreating cold mass **gradually**. This makes **wide, layered clouds** and longer periods of **steady, light rain**." "\n\n"
            r"When conditions are extreme, storms form: **thunderstorms** (from strong convection), **hurricanes** (huge spiral storms powered by **warm ocean water**), and **tornadoes** (violently rotating columns of air)." "\n\n"
            r"⚠️ Common misconception: humidity isn't 'the heat' — it is the **water vapor** in the air. High humidity feels hotter because it slows the evaporation of your sweat, so your body cools less easily." "\n\n"
            r"💡 Tip: **cold front = fast lift = short, intense storms; warm front = slow lift = long, gentle rain.** Hurricanes feed on warm ocean water.",
        ),
        (
            "6. Weather vs. Climate, the Greenhouse Effect & Reading Data",
            r"Two words people mix up:" "\n"
            r"- **Weather** is the **day-to-day** state of the atmosphere in one place (today it's rainy and 60°)." "\n"
            r"- **Climate** is the **long-term average** of weather in a region over many years (this desert is hot and dry)." "\n\n"
            r"A region's climate is shaped mostly by its **latitude** (distance from the equator, which sets how direct the sunlight is), and also by **altitude**, **nearness to oceans**, and **ocean currents**." "\n\n"
            r"[[figure:greenhouse_effect|Sunlight warms Earth's surface, which radiates heat; greenhouse gases absorb some of that heat and send part of it back down, keeping the planet warm.]]" "\n\n"
            r"**The greenhouse effect.** Sunlight passes through the atmosphere and warms the surface. Earth then radiates that energy back as **infrared heat**. **Greenhouse gases** (carbon dioxide, water vapor, methane) absorb some of this heat and re-radiate part of it back down, keeping Earth about 33°C warmer than it would otherwise be — without it, the planet would be frozen. Burning fossil fuels **adds** greenhouse gases, which traps **more** heat and is warming Earth's climate." "\n\n"
            r"**Reading weather data (a GED skill).** GED items may give a temperature graph, a weather map with **high/low pressure** centers and **fronts**, or a climate table. Read the **title, axis labels, units, and map key** first, find the **trend**, and conclude only what the data shows." "\n\n"
            r"⚠️ Common misconception: a single cold day (or week) does **not** disprove a warming **climate**. Weather is one moment; climate is the long-term average — don't judge climate from one day's weather." "\n\n"
            r"💡 Tip: **Weather = what you grab a jacket for today; Climate = what clothes you own for where you live.** Greenhouse gases trap heat; more of them = more warming." "\n\n"
            r"📚 Sources: NOAA National Weather Service / JetStream; NASA Global Climate Change; Tarbuck & Lutgens, *Earth Science*; Ahrens, *Meteorology Today*; UCAR Center for Science Education.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: composition ---
        {
            "text": r"Which two gases make up almost all (about 99%) of Earth's atmosphere?",
            "difficulty": 1,
            "choices": [("Nitrogen and oxygen", True), ("Oxygen and carbon dioxide", False),
                        ("Hydrogen and helium", False), ("Carbon dioxide and water vapor", False)],
            "explanation": r"Dry air is about 78% nitrogen and 21% oxygen — together about 99%. Carbon dioxide and water vapor are present only in small amounts.",
        },
        {
            "text": r"Approximately what percentage of dry air is nitrogen?",
            "difficulty": 2,
            "choices": [("About 78%", True), ("About 21%", False),
                        ("About 50%", False), ("About 1%", False)],
            "explanation": r"Nitrogen is the most abundant gas in the atmosphere at about 78%. Oxygen is about 21%.",
        },
        {
            "text": r"Besides giving us oxygen to breathe, the atmosphere also:",
            "difficulty": 2,
            "choices": [("Holds in heat and blocks much harmful radiation", True),
                        ("Provides the soil that plants grow in", False),
                        ("Generates Earth's magnetic field", False),
                        ("Supplies all of Earth's fresh water at once", False)],
            "explanation": r"The atmosphere keeps Earth warm, shields the surface from harmful radiation and most meteors, and supplies the air we breathe.",
        },
        {
            "text": ("Use the air composition diagram.\n\n"
                     "[[figure:atmosphere_composition|The make-up of dry air]]\n\n"
                     "According to the diagram, oxygen makes up about:"),
            "difficulty": 1,
            "choices": [("21%", True), ("78%", False), ("1%", False), ("50%", False)],
            "explanation": r"The diagram shows oxygen as about 21% of dry air, with nitrogen the large majority at about 78%. Pro tip: nitrogen is the big one, not oxygen.",
        },
        {
            "text": r"Carbon dioxide is only about 0.04% of the atmosphere, yet scientists watch it closely because it:",
            "difficulty": 3,
            "choices": [("Is a greenhouse gas that helps trap heat and affects climate", True),
                        ("Is the gas animals breathe in to survive", False),
                        ("Makes up most of the air", False),
                        ("Destroys the ozone layer", False)],
            "explanation": r"Despite its small amount, carbon dioxide is an important greenhouse gas; increasing it traps more heat and warms the climate.",
        },
        # --- Lesson 2: layers ---
        {
            "text": r"In which layer of the atmosphere do nearly all weather events occur?",
            "difficulty": 1,
            "choices": [("The troposphere", True), ("The stratosphere", False),
                        ("The mesosphere", False), ("The thermosphere", False)],
            "explanation": r"We live in the troposphere, the bottom layer, where clouds and weather form.",
        },
        {
            "text": r"The ozone layer, which absorbs much of the Sun's harmful ultraviolet (UV) radiation, is found in the:",
            "difficulty": 2,
            "choices": [("Stratosphere", True), ("Troposphere", False),
                        ("Mesosphere", False), ("Thermosphere", False)],
            "explanation": r"The ozone layer sits in the stratosphere, where it absorbs UV rays — which is also why that layer warms with height.",
        },
        {
            "text": r"In which layer do most meteors burn up, creating 'shooting stars'?",
            "difficulty": 2,
            "choices": [("The mesosphere", True), ("The troposphere", False),
                        ("The stratosphere", False), ("The thermosphere", False)],
            "explanation": r"Most meteors burn up in the mesosphere, the cold middle layer above the stratosphere.",
        },
        {
            "text": ("Use the atmosphere layers diagram.\n\n"
                     "[[figure:atmosphere_layers_detailed|Atmospheric layers with a temperature profile]]\n\n"
                     "According to the temperature profile, as you go UP through the troposphere, the temperature:"),
            "difficulty": 2,
            "choices": [("Decreases", True), ("Increases", False),
                        ("Stays exactly the same", False), ("Doubles", False)],
            "explanation": r"In the troposphere, temperature falls with altitude (that's why mountaintops are cold). The profile then rises in the stratosphere. Pro tip: the temperature profile zig-zags.",
        },
        {
            "text": r"Why do many jet airliners prefer to cruise in the lower stratosphere rather than the troposphere?",
            "difficulty": 3,
            "choices": [("The stratosphere is calm and stable, with little weather", True),
                        ("The stratosphere has the most oxygen", False),
                        ("It is the layer closest to the ground", False),
                        ("Most weather and storms occur there", False)],
            "explanation": r"Almost all weather happens in the troposphere, so the stable, weather-free lower stratosphere gives a smoother ride.",
        },
        # --- Lesson 3: sun & heat transfer ---
        {
            "text": r"What is the ultimate source of energy for nearly all of Earth's weather?",
            "difficulty": 1,
            "choices": [("The Sun", True), ("Earth's core", False),
                        ("The Moon", False), ("Ocean tides", False)],
            "explanation": r"The Sun heats Earth unevenly, and the atmosphere moving that heat around is what drives the weather.",
        },
        {
            "text": r"Heat that travels as rays through the empty space between the Sun and Earth moves by:",
            "difficulty": 2,
            "choices": [("Radiation", True), ("Conduction", False),
                        ("Convection", False), ("Precipitation", False)],
            "explanation": r"Radiation carries energy as waves/rays and needs no material to travel through, which is how the Sun's heat crosses space to Earth.",
        },
        {
            "text": r"A metal spoon left in a pot of hot soup slowly becomes hot at the handle. This is heat transfer by:",
            "difficulty": 2,
            "choices": [("Conduction", True), ("Radiation", False),
                        ("Convection", False), ("Evaporation", False)],
            "explanation": r"Conduction moves heat through direct contact, atom to atom, along the solid spoon.",
        },
        {
            "text": r"Warm air rising while cooler air sinks, forming a circulating loop that carries heat, is called:",
            "difficulty": 2,
            "choices": [("Convection", True), ("Conduction", False),
                        ("Radiation", False), ("Condensation", False)],
            "explanation": r"Convection transfers heat through the motion of a fluid (air or water): warm fluid rises, cool fluid sinks. It is the main driver of winds.",
        },
        {
            "text": r"The equator receives more direct sunlight than the poles. This uneven heating mainly:",
            "difficulty": 2,
            "choices": [("Drives the movement of air and water that creates winds and weather", True),
                        ("Has no effect on weather", False),
                        ("Makes the poles warmer than the equator", False),
                        ("Stops the atmosphere from moving", False)],
            "explanation": r"Because some places are warmer than others, the atmosphere and oceans move heat around to balance it out — producing winds, currents, and weather.",
        },
        {
            "text": ("Use the heat transfer diagram.\n\n"
                     "[[figure:heat_transfer|Three ways heat moves]]\n\n"
                     "In the diagram, the circulating loop of heated fluid illustrates:"),
            "difficulty": 2,
            "choices": [("Convection", True), ("Conduction", False),
                        ("Radiation", False), ("Insulation", False)],
            "explanation": r"The looping arrows in the heated fluid show convection — rising warm fluid and sinking cool fluid. Pro tip: a moving-fluid loop = convection.",
        },
        # --- Lesson 4: pressure & wind ---
        {
            "text": r"Wind is air moving from areas of ______ pressure toward areas of ______ pressure.",
            "difficulty": 1,
            "choices": [("high; low", True), ("low; high", False),
                        ("hot; cold only", False), ("wet; dry only", False)],
            "explanation": r"Air flows from high pressure to low pressure, and that moving air is wind (like air rushing out of a balloon).",
        },
        {
            "text": r"At a low-pressure area, air tends to:",
            "difficulty": 2,
            "choices": [("Rise, often forming clouds and stormy weather", True),
                        ("Sink, bringing clear skies", False),
                        ("Stay completely still", False),
                        ("Turn into solid ice", False)],
            "explanation": r"In a low, warm air rises and cools, so water vapor condenses into clouds — often bringing unsettled, stormy weather.",
        },
        {
            "text": r"A high-pressure area usually brings:",
            "difficulty": 2,
            "choices": [("Sinking air and clear, fair weather", True),
                        ("Rising air and heavy storms", False),
                        ("No air at all", False),
                        ("Constant snowfall everywhere", False)],
            "explanation": r"In a high, air sinks and warms, discouraging cloud formation — so highs are linked with clear, calm, fair weather.",
        },
        {
            "text": ("Use the sea breeze diagram.\n\n"
                     "[[figure:pressure_wind|A daytime sea breeze]]\n\n"
                     "During the day the land heats faster than the sea. According to the diagram, the surface wind (the sea breeze) blows:"),
            "difficulty": 2,
            "choices": [("From the sea toward the land", True),
                        ("From the land toward the sea", False),
                        ("Straight up into space", False),
                        ("In no particular direction", False)],
            "explanation": r"Warm air rises over the hot land (low pressure) and cooler air sinks over the sea (high pressure), so the surface wind blows from sea (high) to land (low). Pro tip: wind goes High to Low.",
        },
        {
            "text": r"The apparent curving of winds and large weather systems caused by Earth's rotation is called the:",
            "difficulty": 3,
            "choices": [("Coriolis effect", True), ("Greenhouse effect", False),
                        ("Doppler effect", False), ("Water cycle", False)],
            "explanation": r"The Coriolis effect, caused by Earth's rotation, deflects moving air, which is why large storms and wind belts spin rather than moving in straight lines.",
        },
        # --- Lesson 5: humidity, fronts, storms ---
        {
            "text": r"The amount of water vapor in the air is called:",
            "difficulty": 1,
            "choices": [("Humidity", True), ("Pressure", False),
                        ("Precipitation", False), ("Altitude", False)],
            "explanation": r"Humidity is the amount of water vapor in the air. When the air is saturated, that vapor condenses into clouds or rain.",
        },
        {
            "text": r"A cold front forms when:",
            "difficulty": 2,
            "choices": [("A cold air mass pushes under a warm air mass, forcing the warm air up quickly", True),
                        ("Warm air slowly slides over a cold air mass", False),
                        ("Two warm air masses merge", False),
                        ("The ground heats the air evenly", False)],
            "explanation": r"At a cold front, dense cold air wedges beneath warm air and shoves it up rapidly, building tall clouds and often brief, heavy storms.",
        },
        {
            "text": r"Compared with a warm front, a cold front more often brings:",
            "difficulty": 2,
            "choices": [("Brief but heavy thunderstorms", True),
                        ("Long periods of steady, light rain", False),
                        ("Weeks of clear skies", False),
                        ("No change in the weather at all", False)],
            "explanation": r"The fast, steep lifting at a cold front builds towering clouds and short, intense storms. Warm fronts lift air gently, giving widespread, steady, light rain.",
        },
        {
            "text": ("Use the weather fronts diagram.\n\n"
                     "[[figure:weather_fronts|Cold front vs. warm front]]\n\n"
                     "Based on the diagram, the warm front (warm air gliding gently up over cold air) tends to produce:"),
            "difficulty": 2,
            "choices": [("Wide, layered clouds and steady, light rain", True),
                        ("A single tall storm cloud with hail", False),
                        ("Clear skies and strong winds", False),
                        ("A tornado every time", False)],
            "explanation": r"The diagram shows warm air sliding up a gentle slope, spreading out into broad layered clouds and long-lasting light rain. Pro tip: gentle lift = gentle, steady weather.",
        },
        {
            "text": r"A hurricane gets most of its energy from:",
            "difficulty": 3,
            "choices": [("Warm ocean water (evaporation, and heat released when the vapor condenses)", True),
                        ("Cold air from the poles", False),
                        ("Earth's magnetic field", False),
                        ("Friction with the land", False)],
            "explanation": r"Hurricanes form over warm oceans: water evaporates, rises, and condenses, releasing huge amounts of heat that powers the storm. That's why hurricanes weaken over land.",
        },
        # --- Lesson 6: weather vs climate, greenhouse, data ---
        {
            "text": r"What is the difference between weather and climate?",
            "difficulty": 1,
            "choices": [("Weather is the day-to-day conditions; climate is the long-term average", True),
                        ("They mean exactly the same thing", False),
                        ("Weather lasts for centuries; climate changes hourly", False),
                        ("Climate only describes the ocean", False)],
            "explanation": r"Weather is what's happening in the atmosphere right now in one place; climate is the average pattern of weather over many years.",
        },
        {
            "text": r"Which factor has the BIGGEST effect on whether a region's climate is generally hot or cold?",
            "difficulty": 2,
            "choices": [("Its latitude (distance from the equator)", True),
                        ("The day of the week", False),
                        ("The color of its soil", False),
                        ("How many people live there", False)],
            "explanation": r"Latitude sets how directly sunlight strikes a region, which is the main control on its temperature. Altitude, nearness to water, and ocean currents also matter.",
        },
        {
            "text": r"One unusually cold week occurs during a decade of rising average global temperatures. What is the best conclusion?",
            "difficulty": 2,
            "choices": [("A single week of weather does not disprove a long-term climate trend", True),
                        ("The climate must actually be cooling", False),
                        ("The temperature records must be fake", False),
                        ("Weather and climate are the same thing", False)],
            "explanation": r"Climate is a long-term average, so one cold week (weather) does not overturn a multi-year warming trend. Don't judge climate from a single moment.",
        },
        {
            "text": ("Use the greenhouse effect diagram.\n\n"
                     "[[figure:greenhouse_effect|How greenhouse gases trap heat]]\n\n"
                     "According to the diagram, greenhouse gases warm Earth because they:"),
            "difficulty": 3,
            "choices": [("Absorb heat radiating from Earth's surface and send some of it back down", True),
                        ("Block all sunlight from reaching the surface", False),
                        ("Cool the surface by reflecting heat into space", False),
                        ("Create brand-new energy out of nothing", False)],
            "explanation": r"Sunlight warms the surface, which radiates infrared heat; greenhouse gases absorb some of it and re-radiate part back down, keeping Earth warm. Adding more gases traps more heat. Pro tip: in goes sunlight, out goes heat, some is trapped.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain how the Sun's uneven heating of Earth leads to wind. In your answer, describe how "
                "air pressure relates to rising and sinking air, which way wind blows between high and low "
                "pressure, and use the daytime sea breeze as an example."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the Sun heats Earth unevenly (e.g., land heats faster than water); "
                "(2) warm air expands, rises, and leaves low pressure, while cool air sinks and forms high pressure; "
                "(3) wind blows from high pressure to low pressure; (4) the sea-breeze example -- by day the land "
                "heats faster, air rises over land (low) and sinks over the sea (high), so the surface wind blows from "
                "sea to land; (5) optional mention of convection cells / Coriolis. Deduct for saying wind blows from "
                "low to high pressure."
            ),
        },
        {
            "text": (
                "A friend says, 'It snowed last week, so global warming must be fake.' Using the difference between "
                "weather and climate, and the greenhouse effect, explain why this reasoning is flawed."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) defining weather as short-term, day-to-day conditions and climate as the "
                "long-term average over many years; (2) explaining that one snowy week is weather and cannot disprove "
                "a long-term climate trend; (3) describing the greenhouse effect -- sunlight warms the surface, Earth "
                "radiates heat, and greenhouse gases (CO2, water vapor, methane) trap some of it; (4) noting that "
                "adding greenhouse gases (e.g., from burning fossil fuels) traps more heat and warms the climate over "
                "time. Deduct for treating a single weather event as proof about climate."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Weather, Climate & the Atmosphere (Deep Dive)' course."

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
