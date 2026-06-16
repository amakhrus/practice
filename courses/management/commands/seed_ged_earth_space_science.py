"""
Seed data: 'GED Science: Earth & Space Science' -- the third content domain of
the GED Science test, built comprehensively and visually.

Covers Earth's structure, plate tectonics, the rock cycle, Earth's water and the
water cycle, weather and the atmosphere, the solar system, and the Earth-Moon-Sun
system (moon phases and seasons) -- plus the science-reasoning skill of reading
data. Each lesson leads with intuition and a real-world hook, includes a labeled
diagram, a common-misconception warning, and a quick tip. Practice questions
mirror the GED style, including diagram- and data-based items.

Run:
    python manage.py seed_ged_earth_space_science
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Earth & Space Science",
    "slug": "ged-earth-space-science",
    "program": "GED",
    "subject": "science",
    "description": (
        "Earth and Space Science rounds out the GED Science test, alongside life science and "
        "physical science. This course takes you from deep inside our planet out to the edge of "
        "the solar system: Earth's layers, plate tectonics, the rock cycle, the water cycle, "
        "weather and the atmosphere, the planets, and the cycles of the Moon and the seasons. "
        "Every topic uses plain language, labeled diagrams, and GED-style practice with full "
        "explanations."
    ),
    "lessons": [
        (
            "1. Earth's Structure & Layers",
            r"If you could slice Earth open, you would see it is built in **layers**, like an onion — each made of different material and getting hotter toward the center." "\n\n"
            r"[[figure:earth_layers|Four main layers, from the thin rocky crust down to the scorching solid inner core.]]" "\n\n"
            r"From the outside in:" "\n"
            r"- **Crust** — the thin, solid outer shell of rock we live on (continents and ocean floor)." "\n"
            r"- **Mantle** — the thick layer of hot rock below the crust. It is mostly solid but flows very slowly over time, and its motion drives the plates above it." "\n"
            r"- **Outer core** — a layer of **liquid** iron and nickel. Its swirling motion creates Earth's **magnetic field**." "\n"
            r"- **Inner core** — a ball of **solid** iron and nickel at the center. It is the hottest part, but stays solid because of the enormous pressure." "\n\n"
            r"The crust and the very top of the mantle together form a rigid shell that is broken into moving pieces called **tectonic plates** (Lesson 2)." "\n\n"
            r"⚠️ Common misconception: the inner core is hotter than the outer core, yet it is **solid** — extreme pressure keeps it from melting." "\n\n"
            r"💡 Tip: remember the order Crust → Mantle → Outer core → Inner core. The outer core is liquid, the inner core is solid, and it gets hotter all the way down.",
        ),
        (
            "2. Plate Tectonics & Earth's Changing Surface",
            r"Earth's rigid outer shell is cracked into giant slabs called **tectonic plates** that slowly slide on the hot, flowing mantle beneath. They move only a few centimeters a year — about as fast as your fingernails grow — but over millions of years they reshape the planet." "\n\n"
            r"What happens depends on how two plates meet at a **boundary**:" "\n\n"
            r"[[figure:tectonic_boundaries|Three ways plates interact: colliding, pulling apart, or sliding past each other.]]" "\n\n"
            r"- **Convergent** (plates **collide**) — crust crumples up into **mountains**, or one plate dives under another, causing volcanoes." "\n"
            r"- **Divergent** (plates pull **apart**) — magma rises into the gap and forms **new crust** (mid-ocean ridges)." "\n"
            r"- **Transform** (plates **slide** past) — they grind and catch, then slip suddenly, causing **earthquakes** (like California's San Andreas Fault)." "\n\n"
            r"This is also evidence for **continental drift**: the continents were once joined in a single supercontinent and have drifted to their current positions. Matching coastlines, fossils, and rock layers on different continents are the clues." "\n\n"
            r"⚠️ Common misconception: earthquakes and volcanoes are not random — most happen along **plate boundaries**, which is why they cluster in the same regions (like the Pacific 'Ring of Fire')." "\n\n"
            r"💡 Tip: collide = mountains/volcanoes; pull apart = new crust; slide = earthquakes.",
        ),
        (
            "3. The Rock Cycle & Minerals",
            r"Rocks are not permanent — over long stretches of time, any rock can be changed into another kind. This never-ending set of changes is the **rock cycle**, and it is driven by heat, pressure, weathering, and time." "\n\n"
            r"There are three families of rock, based on **how they form**:" "\n"
            r"- **Igneous** — formed when molten rock (magma or lava) **cools and hardens** (granite, basalt)." "\n"
            r"- **Sedimentary** — formed when bits of rock and shells are pressed and cemented together in **layers** (sandstone, limestone). These often hold **fossils**." "\n"
            r"- **Metamorphic** — formed when an existing rock is changed by intense **heat and pressure** without melting (marble from limestone, slate from shale)." "\n\n"
            r"[[figure:rock_cycle|Any rock can become any other type — weathering, heat, pressure, melting, and cooling drive the cycle.]]" "\n\n"
            r"Each path has a process: weathering and erosion break rocks into sediment; burial adds heat and pressure; deep melting makes magma, which cools back into igneous rock — and the cycle continues." "\n\n"
            r"⚠️ Common misconception: the rock cycle has no fixed 'start' or one-way order. A metamorphic rock can melt and become igneous, or be worn down into sediment — rocks move around the cycle in many directions." "\n\n"
            r"💡 Tip: tie the name to the process — Igneous = ignite/heat then cool; Sedimentary = sediment/layers; Metamorphic = morph/change by heat & pressure.",
        ),
        (
            "4. Earth's Water & the Water Cycle",
            r"About **71%** of Earth's surface is covered by water, but most of it is salty ocean. Only a small fraction is the **fresh water** that living things need, and much of that is frozen in ice caps and glaciers." "\n\n"
            r"Earth's water is constantly recycled through the **water cycle**, powered by energy from the **Sun**:" "\n\n"
            r"[[figure:water_cycle|The Sun drives water from the ocean to the sky and back to the land in a continuous loop.]]" "\n\n"
            r"- **Evaporation** — the Sun heats surface water (oceans, lakes) and turns it into invisible water **vapor** that rises. (Plants release vapor too, called transpiration.)" "\n"
            r"- **Condensation** — high up, the cooler air turns the vapor back into tiny droplets that form **clouds**." "\n"
            r"- **Precipitation** — droplets join, grow heavy, and fall as **rain, snow, or hail**." "\n"
            r"- **Collection** — water gathers in oceans, lakes, and rivers, or soaks into the ground, and the cycle repeats." "\n\n"
            r"⚠️ Common misconception: the water cycle does not create new water. The **same** water is recycled again and again — the water you drink today is the same water dinosaurs once drank." "\n\n"
            r"💡 Tip: follow the loop with the Sun as the engine: evaporate up, condense into clouds, precipitate down, collect, repeat.",
        ),
        (
            "5. Weather, Climate & the Atmosphere",
            r"Earth is wrapped in a blanket of gases called the **atmosphere** — mostly **nitrogen** (about 78%) and **oxygen** (about 21%). It holds in heat, blocks harmful radiation, and gives us air to breathe." "\n\n"
            r"[[figure:atmosphere_layers|The atmosphere thins with height, from the weather-filled troposphere up to the thermosphere.]]" "\n\n"
            r"The atmosphere has layers. We live in the bottom layer, the **troposphere**, where nearly all **weather** happens. Higher up, the **stratosphere** holds the **ozone layer**, which absorbs the Sun's ultraviolet rays." "\n\n"
            r"Two words people mix up:" "\n"
            r"- **Weather** is the day-to-day state of the atmosphere in one place (today it is rainy and 60°)." "\n"
            r"- **Climate** is the **average** weather of a region over many years (this desert is hot and dry)." "\n\n"
            r"Weather is driven by the uneven heating of Earth, which moves air and water as **wind** and **currents**. Warm air rising and cool air sinking creates the pressure systems that bring sun or storms." "\n\n"
            r"⚠️ Common misconception: a single cold day does not disprove a warming **climate**. Weather is one moment; climate is the long-term average — don't judge climate from one day's weather." "\n\n"
            r"💡 Tip: Weather = what you grab a jacket for today; Climate = what clothes you own for where you live.",
        ),
        (
            "6. The Solar System & Earth in Space",
            r"Our **solar system** is the **Sun** plus everything held by its gravity: eight planets, their moons, and countless asteroids and comets. The Sun is an ordinary **star** — a giant ball of hot gas — and it holds 99% of the system's mass, so its gravity keeps everything in **orbit**." "\n\n"
            r"[[figure:solar_system|The eight planets in order from the Sun. The inner four are small and rocky; the outer four are giant.]]" "\n\n"
            r"The order from the Sun is **Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune**:" "\n"
            r"- The **inner planets** (Mercury–Mars) are small, rocky, and warmer." "\n"
            r"- The **outer planets** (Jupiter–Neptune) are huge **gas giants**, cold and far apart." "\n\n"
            r"Earth sits in a 'just right' spot — close enough to be warm but far enough for **liquid water**, which makes life possible. A **planet** orbits the Sun; a **moon** orbits a planet; a **comet** is an icy body that grows a tail near the Sun." "\n\n"
            r"⚠️ Common misconception: the Sun is a star, not a planet, and it does not 'burn' like a fire — it produces energy by **nuclear fusion**, joining hydrogen atoms together." "\n\n"
            r"💡 Tip: remember the planet order with a sentence like 'My Very Easy Method Just Speeds Up Names' (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune).",
        ),
        (
            "7. The Moon, Seasons & Reading Science Data",
            r"Earth is part of a three-body system with the **Sun** and the **Moon**, and their motions create cycles we see every day." "\n\n"
            r"**Phases of the Moon.** The Moon does not make its own light — it **reflects** sunlight. As it orbits Earth (about every 29.5 days), we see different amounts of its lit half, from **new** (dark) to **full** and back:" "\n\n"
            r"[[figure:moon_phases|We always see the same lit half of the Moon from a changing angle, so its shape appears to grow and shrink.]]" "\n\n"
            r"**Seasons.** Seasons are **not** caused by Earth's distance from the Sun. They happen because Earth's axis is **tilted** about 23.5°. The hemisphere tilted **toward** the Sun gets more direct light and longer days — that is **summer**; the hemisphere tilted **away** has winter:" "\n\n"
            r"[[figure:seasons|The tilt stays pointed the same way all year, so each hemisphere takes turns leaning toward the Sun.]]" "\n\n"
            r"**Eclipses** happen when Sun, Earth, and Moon line up: a **solar** eclipse when the Moon blocks the Sun, a **lunar** eclipse when Earth's shadow falls on the Moon." "\n\n"
            r"The GED Science test rewards **reasoning with data**. For any graph or table, read the **title, axis labels, and units** first, find the **trend**, and use only what the data **shows** — correlation is not causation." "\n\n"
            r"⚠️ Common misconception: seasons are not caused by Earth being closer to the Sun. It is the **tilt**. (In fact, Earth is closest to the Sun during Northern Hemisphere winter.)" "\n\n"
            r"💡 Tip: Moon phases = monthly cycle from reflected light; seasons = yearly cycle from axial tilt.",
        ),
    ],
    "mcqs": [
        # --- Earth's layers ---
        {
            "text": r"Which layer of Earth is the thin, solid outer shell that we live on?",
            "difficulty": 1,
            "choices": [("The crust", True), ("The mantle", False), ("The outer core", False), ("The inner core", False)],
            "explanation": r"The crust is the thin, solid outermost layer of rock. Below it lies the thick mantle, then the liquid outer core and solid inner core.",
        },
        {
            "text": r"Which layer of Earth is made of LIQUID iron and nickel and creates Earth's magnetic field?",
            "difficulty": 2,
            "choices": [("The outer core", True), ("The inner core", False), ("The crust", False), ("The mantle", False)],
            "explanation": r"The outer core is liquid metal, and its motion generates Earth's magnetic field. The inner core is also metal but solid because of the immense pressure.",
        },
        {
            "text": r"The inner core is the hottest part of Earth, yet it is solid. Why?",
            "difficulty": 3,
            "choices": [("The enormous pressure keeps it from melting", True),
                        ("It is actually cooler than the outer core", False),
                        ("It is made of rock, not metal", False),
                        ("It is cooled by the magnetic field", False)],
            "explanation": r"Despite being hottest, the inner core stays solid because the crushing pressure at Earth's center prevents the metal from melting.",
        },
        # --- Plate tectonics ---
        {
            "text": r"What are the large moving slabs that make up Earth's rigid outer shell called?",
            "difficulty": 1,
            "choices": [("Tectonic plates", True), ("Magma chambers", False), ("Fault lines", False), ("Sediment layers", False)],
            "explanation": r"Earth's outer shell is broken into tectonic plates that slowly slide on the flowing mantle below.",
        },
        {
            "text": r"At a boundary where two plates slide past each other, the most common event is:",
            "difficulty": 2,
            "choices": [("Earthquakes", True), ("New ocean crust forming", False),
                        ("Tall fold mountains", False), ("Nothing ever happens", False)],
            "explanation": r"At a transform boundary the plates grind and catch, then slip suddenly, releasing energy as earthquakes (for example, the San Andreas Fault).",
        },
        {
            "text": r"Matching coastlines and identical fossils found on continents now separated by oceans are evidence for:",
            "difficulty": 2,
            "choices": [("Continental drift (plate tectonics)", True),
                        ("The water cycle", False),
                        ("The rock cycle", False),
                        ("Seasons", False)],
            "explanation": r"These matching clues show the continents were once joined and have since drifted apart — evidence for continental drift and plate tectonics.",
        },
        # --- Rock cycle ---
        {
            "text": r"A rock forms when molten lava cools and hardens. What type of rock is it?",
            "difficulty": 1,
            "choices": [("Igneous", True), ("Sedimentary", False), ("Metamorphic", False), ("Mineral", False)],
            "explanation": r"Rock that forms from cooled and hardened magma or lava is igneous (think 'ignite' = heat). Sedimentary forms in layers; metamorphic forms under heat and pressure.",
        },
        {
            "text": r"Which type of rock most often contains fossils, because it forms from layers of sediment?",
            "difficulty": 2,
            "choices": [("Sedimentary", True), ("Igneous", False), ("Metamorphic", False), ("Molten", False)],
            "explanation": r"Sedimentary rock builds up in layers that can bury and preserve remains, so it most often holds fossils. The heat that forms igneous and metamorphic rock usually destroys fossils.",
        },
        {
            "text": r"Marble forms when limestone is exposed to intense heat and pressure deep underground, without melting. Marble is therefore:",
            "difficulty": 2,
            "choices": [("Metamorphic", True), ("Sedimentary", False), ("Igneous", False), ("A liquid", False)],
            "explanation": r"Changing an existing rock with heat and pressure (but no melting) makes metamorphic rock — think 'metamorphosis' = change.",
        },
        # --- Water cycle ---
        {
            "text": r"In the water cycle, what is the process called when the Sun heats water and turns it into vapor that rises into the air?",
            "difficulty": 1,
            "choices": [("Evaporation", True), ("Condensation", False), ("Precipitation", False), ("Collection", False)],
            "explanation": r"Evaporation is liquid water becoming vapor and rising. Condensation is the reverse (vapor to droplets/clouds); precipitation is rain or snow falling.",
        },
        {
            "text": r"Clouds form during which step of the water cycle?",
            "difficulty": 2,
            "choices": [("Condensation", True), ("Evaporation", False), ("Precipitation", False), ("Runoff", False)],
            "explanation": r"High in the cooler air, water vapor condenses into tiny droplets that gather to form clouds — that step is condensation.",
        },
        {
            "text": r"What is the main source of energy that powers the entire water cycle?",
            "difficulty": 2,
            "choices": [("The Sun", True), ("Earth's core", False), ("The Moon", False), ("Wind machines", False)],
            "explanation": r"The Sun's energy heats surface water and drives evaporation, powering the whole cycle. (The same water is recycled — no new water is made.)",
        },
        # --- Weather, climate & atmosphere ---
        {
            "text": r"Which two gases make up almost all of Earth's atmosphere?",
            "difficulty": 2,
            "choices": [("Nitrogen and oxygen", True), ("Oxygen and carbon dioxide", False),
                        ("Hydrogen and helium", False), ("Carbon dioxide and water vapor", False)],
            "explanation": r"Air is about 78% nitrogen and 21% oxygen — together about 99%. Carbon dioxide and water vapor are present only in small amounts.",
        },
        {
            "text": r"What is the difference between weather and climate?",
            "difficulty": 2,
            "choices": [("Weather is the day-to-day conditions; climate is the long-term average", True),
                        ("They mean exactly the same thing", False),
                        ("Weather is measured in years; climate in hours", False),
                        ("Climate only describes deserts", False)],
            "explanation": r"Weather is what is happening in the atmosphere right now in one place; climate is the average pattern of weather over many years.",
        },
        {
            "text": r"In which layer of the atmosphere does nearly all of our weather occur?",
            "difficulty": 2,
            "choices": [("The troposphere", True), ("The stratosphere", False),
                        ("The mesosphere", False), ("The thermosphere", False)],
            "explanation": r"We live in the troposphere, the bottom layer, where clouds and weather form. The ozone layer sits above it in the stratosphere.",
        },
        {
            "text": r"One unusually cold week occurs during a decade of rising average global temperatures. What is the best conclusion?",
            "difficulty": 3,
            "choices": [("A single week of weather does not disprove a long-term climate trend", True),
                        ("The climate must be cooling after all", False),
                        ("The temperature records are clearly wrong", False),
                        ("Weather and climate are the same thing", False)],
            "explanation": r"Climate is a long-term average, so one cold week (weather) does not overturn a multi-year trend. Don't judge climate from a single moment.",
        },
        # --- Solar system ---
        {
            "text": r"What is at the center of our solar system, holding the planets in orbit with its gravity?",
            "difficulty": 1,
            "choices": [("The Sun", True), ("Earth", False), ("The Moon", False), ("Jupiter", False)],
            "explanation": r"The Sun holds about 99% of the solar system's mass, and its gravity keeps all the planets in orbit. The Sun is a star, not a planet.",
        },
        {
            "text": r"Which list gives the four inner, rocky planets in order from the Sun?",
            "difficulty": 2,
            "choices": [("Mercury, Venus, Earth, Mars", True),
                        ("Earth, Mars, Jupiter, Saturn", False),
                        ("Venus, Earth, Jupiter, Neptune", False),
                        ("Mercury, Earth, Saturn, Neptune", False)],
            "explanation": r"The inner, rocky planets in order are Mercury, Venus, Earth, Mars. The outer giants (Jupiter, Saturn, Uranus, Neptune) come after.",
        },
        {
            "text": r"How does the Sun produce its enormous energy?",
            "difficulty": 3,
            "choices": [("Nuclear fusion, joining hydrogen atoms together", True),
                        ("Burning like a wood fire", False),
                        ("Reflecting light from the planets", False),
                        ("Friction from spinning fast", False)],
            "explanation": r"The Sun is a star powered by nuclear fusion — hydrogen atoms fuse into helium, releasing huge amounts of energy. It does not 'burn' chemically like a fire.",
        },
        # --- Moon, seasons, cycles ---
        {
            "text": r"Why does the Moon appear to shine?",
            "difficulty": 1,
            "choices": [("It reflects sunlight", True), ("It produces its own light", False),
                        ("It is on fire", False), ("It glows from Earth's heat", False)],
            "explanation": r"The Moon makes no light of its own; it reflects light from the Sun. As it orbits Earth, we see different amounts of its lit half — the phases.",
        },
        {
            "text": r"What actually causes Earth's seasons?",
            "difficulty": 2,
            "choices": [("The tilt of Earth's axis", True),
                        ("Earth moving closer to and farther from the Sun", False),
                        ("The phases of the Moon", False),
                        ("Changes in the Sun's brightness", False)],
            "explanation": r"Seasons come from Earth's 23.5° axial tilt: the hemisphere tilted toward the Sun gets more direct light (summer). Distance from the Sun is not the cause.",
        },
        {
            "text": r"It is summer in the Northern Hemisphere. What is happening with Earth's tilt?",
            "difficulty": 3,
            "choices": [("The Northern Hemisphere is tilted toward the Sun", True),
                        ("The Northern Hemisphere is tilted away from the Sun", False),
                        ("Earth is closest to the Sun", False),
                        ("Earth has no tilt in summer", False)],
            "explanation": r"In Northern summer, the North Pole leans toward the Sun, so that hemisphere gets more direct sunlight and longer days. (At the same time it is winter in the south.)",
        },
        {
            "text": r"A lunar eclipse happens when:",
            "difficulty": 2,
            "choices": [("Earth's shadow falls on the Moon", True),
                        ("The Moon's shadow falls on Earth", False),
                        ("The Moon stops reflecting light", False),
                        ("The Sun passes behind Earth's core", False)],
            "explanation": r"In a lunar eclipse, the Sun-Earth-Moon line up so Earth's shadow falls on the Moon. (When the Moon's shadow falls on Earth, that is a solar eclipse.)",
        },
        {
            "text": ("Use the water cycle diagram.\n\n"
                     "[[figure:water_cycle|Stages of the water cycle]]\n\n"
                     "Which stage returns water from the clouds to Earth's surface as rain or snow?"),
            "difficulty": 1,
            "choices": [("Precipitation", True), ("Evaporation", False), ("Condensation", False), ("Collection", False)],
            "explanation": r"Precipitation is water falling from clouds as rain or snow. Evaporation rises as vapor and condensation forms the clouds. Pro tip: precipitation comes down; evaporation goes up.",
        },
        {
            "text": ("Use the diagram of Earth orbiting the Sun.\n\n"
                     "[[figure:seasons|Earth's tilt as it orbits the Sun]]\n\n"
                     "Based on the diagram, what causes summer in the Northern Hemisphere?"),
            "difficulty": 2,
            "choices": [("The North Pole is tilted toward the Sun", True),
                        ("Earth is at its closest point to the Sun", False),
                        ("The Sun temporarily gives off more heat", False),
                        ("The Moon blocks less sunlight", False)],
            "explanation": r"The diagram shows summer when the North Pole tilts toward the Sun. It is the tilt, not Earth's distance, that drives the seasons. Pro tip: seasons come from which hemisphere leans toward the Sun.",
        },
        {
            "text": ("Use the diagram of the Moon's phases.\n\n"
                     "[[figure:moon_phases|The phases of the Moon]]\n\n"
                     "Which phase occurs when the entire side of the Moon facing Earth is lit?"),
            "difficulty": 1,
            "choices": [("Full moon", True), ("New moon", False), ("First quarter", False), ("Waxing crescent", False)],
            "explanation": r"At a full moon we see the whole near side lit. A new moon is the opposite, with the near side dark. Pro tip: full = all lit; new = none lit.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain why we experience seasons on Earth. A friend tells you that summer happens because "
                "Earth is closer to the Sun. Use Earth's axial tilt to explain why your friend is mistaken, "
                "and describe what makes one hemisphere experience summer while the other has winter."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) stating seasons are caused by Earth's ~23.5° axial tilt, not distance; "
                "(2) explaining the hemisphere tilted toward the Sun gets more direct sunlight and longer days "
                "(summer) while the other is tilted away (winter); (3) noting the two hemispheres have opposite "
                "seasons at the same time. Deduct for attributing seasons mainly to distance from the Sun."
            ),
        },
        {
            "text": (
                "Trace a single drop of water through the water cycle, starting in the ocean. Name and describe "
                "each major step it goes through and explain what role the Sun plays. Then explain why we say "
                "the water cycle does not create any new water."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) evaporation — the Sun heats ocean water into vapor that rises; "
                "(2) condensation — vapor cools and forms clouds; (3) precipitation — water falls as rain/snow; "
                "(4) collection — water returns to oceans/lakes/ground and the cycle repeats; (5) the Sun is the "
                "energy source and the same water is recycled, never created. Deduct for missing steps or omitting the Sun."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'GED Science: Earth & Space Science' course."

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

        # Phase 1 is MCQ-only: written-response prompts are not seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
