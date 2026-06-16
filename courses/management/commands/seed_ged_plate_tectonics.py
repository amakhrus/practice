"""
Seed data: 'GED Science: Plate Tectonics & Earth's Changing Surface (Deep Dive)'.

A focused EXPANSION of Lesson 2 ("Plate Tectonics & Earth's Changing Surface")
from the broader 'GED Science: Earth & Space Science' course. The parent course
gives a one-lesson overview of plate boundaries; this course goes deeper and tells
the story the way it actually unfolded in science:

  1. Continental drift -- Wegener's evidence, and why it was rejected.
  2. The engine -- mantle convection, ridge push, and slab pull (the mechanism
     Wegener was missing).
  3. Seafloor spreading -- Hess's idea and the magnetic-stripe proof.
  4. The three plate boundaries in depth (divergent, convergent, transform),
     including the three kinds of convergence.
  5. Mountains, volcanoes, earthquakes, and the Pacific Ring of Fire.
  6. Hotspots, the pace of change, and reading tectonic data.

This course uses ALL-NEW diagrams (continental drift, mantle convection, seafloor
spreading, a subduction cross-section, a transform boundary, the Ring of Fire, and
a hotspot island chain). It deliberately does NOT reuse the parent course's
'tectonic_boundaries' figure, per the course brief.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - U.S. Geological Survey (USGS), Kious & Tilling, *This Dynamic Earth: The Story
    of Plate Tectonics*, and "Understanding Plate Motions."
  - Tarbuck, E. & Lutgens, F., *Earth Science* (Pearson) -- standard GED-level text.
  - Wegener, A. (1915), *The Origin of Continents and Oceans* (Pangaea, drift).
  - Hess, H. (1962), "History of Ocean Basins" (seafloor spreading).
  - Vine, F. & Matthews, D. (1963), Nature -- symmetric magnetic stripes.
  - National Geographic Society, Resource Library: "plate tectonics," "Ring of Fire."
Approximate figures (rounded for learners): plate speeds ~2-10 cm/yr; oldest ocean
floor < ~200 million years; the Ring of Fire holds ~75% of the world's volcanoes.

Run:
    python manage.py seed_ged_plate_tectonics
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Plate Tectonics & Earth's Changing Surface (Deep Dive)",
    "slug": "ged-plate-tectonics",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the theory that reshaped Earth science, expanding the single 'Plate "
        "Tectonics & Earth's Changing Surface' lesson from the GED Earth & Space Science course into a "
        "full mini-course. You'll follow the real detective story: Wegener's idea that the continents "
        "once fit together, why scientists rejected it, and how the discovery of seafloor spreading and "
        "magnetic stripes finally revealed the engine driving the plates. From there you'll master the "
        "three kinds of plate boundaries and the mountains, volcanoes, earthquakes, and island chains "
        "they build. Plain language, all-new labeled diagrams, common-misconception warnings, and "
        "GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. Continental Drift: Wegener's Big Idea",
            r"Look at a world map. Doesn't the bulge of **South America** seem to fit into the curve of **West Africa**, like two puzzle pieces? In 1912, a German scientist named **Alfred Wegener** noticed the same thing and made a bold claim: the continents were once joined in a single supercontinent he called **Pangaea**, and they have slowly **drifted** apart ever since." "\n\n"
            r"[[figure:continental_drift|Pangaea split apart; matching fossils, rock layers, and mountain belts line up across continents now separated by oceans.]]" "\n\n"
            r"Wegener gathered four kinds of evidence:" "\n"
            r"- **The fit** — the coastlines of continents like South America and Africa match like puzzle pieces." "\n"
            r"- **Matching fossils** — identical fossils of *Mesosaurus*, a small freshwater reptile that could not swim across an ocean, are found on **both** South America and Africa. The fern *Glossopteris* is found across several now-separated southern continents." "\n"
            r"- **Matching rocks & mountains** — rock layers and mountain belts line up across the ocean (the Appalachians in North America match mountains in Britain and Scandinavia)." "\n"
            r"- **Ancient climate clues** — coal (from tropical swamps) lies under Antarctic ice, and scratches from ancient glaciers appear in places that are now warm." "\n\n"
            r"Yet most scientists **rejected** his idea for almost 50 years. The problem: Wegener could not explain **how** something as huge as a continent could move. Without a mechanism, the evidence wasn't enough. The answer would come from the bottom of the ocean (Lessons 2–3)." "\n\n"
            r"⚠️ Common misconception: Wegener thought continents **plowed through** the solid ocean floor like ships — and that's physically impossible, which is partly why he was dismissed. We now know continents don't push through the seafloor; they **ride on plates** that include the seafloor." "\n\n"
            r"💡 Tip: remember Wegener's evidence as **fit, fossils, rocks, climate** — but note he lacked a *mechanism*.",
        ),
        (
            "2. The Engine: Mantle Convection",
            r"Wegener's missing piece was a **force** big enough to move continents. The answer is **heat** — the same internal heat (from Earth's formation and from radioactive decay) that keeps the core molten." "\n\n"
            r"That heat sets the **mantle** in motion. The mantle is solid rock, but it is so hot that over millions of years it **flows** very slowly, like incredibly stiff putty. Hot rock near the bottom **rises**, spreads out near the top, cools, and **sinks** again — a slow loop called a **convection cell**." "\n\n"
            r"[[figure:mantle_convection|Slow convection loops in the solid mantle: hot rock rises at a ridge and sinking slabs pull plates down at a trench.]]" "\n\n"
            r"The rigid plates sit on top of these flowing currents and get carried along. Scientists now think two forces matter most:" "\n"
            r"- **Ridge push** — new, elevated crust at a mid-ocean ridge slides downhill, pushing the plate away." "\n"
            r"- **Slab pull** — where a cold, dense plate edge sinks into the mantle, it **pulls** the rest of the plate along behind it. Slab pull is thought to be the **strongest** driver." "\n\n"
            r"How fast? Only a few **centimeters per year** — about as fast as your fingernails grow. Tiny, but over millions of years it moves continents across the globe." "\n\n"
            r"⚠️ Common misconception: the mantle is **not** boiling liquid lava. It is **solid rock** that flows in extreme slow motion. One convection loop can take tens of millions of years." "\n\n"
            r"💡 Tip: heat → convection in the solid mantle → **ridge push + slab pull** → plates creep along at a few cm/year.",
        ),
        (
            "3. Seafloor Spreading: The Proof",
            r"In the 1960s, geologist **Harry Hess** studied the ocean floor and proposed **seafloor spreading**. At long undersea mountain ranges called **mid-ocean ridges**, magma rises from the mantle, hardens into **new oceanic crust**, and pushes the older crust outward on both sides — like a conveyor belt slowly carrying the seafloor away from the ridge." "\n\n"
            r"[[figure:seafloor_spreading|New crust forms at the ridge and spreads outward. Symmetric magnetic stripes record Earth's field reversals — a mirror image on each side.]]" "\n\n"
            r"The proof came from **magnetism**. Earth's magnetic field flips direction every so often (Lesson on the core). As new crust hardens at the ridge, it **records** the field's direction at that moment. The result: the seafloor carries a pattern of magnetic **stripes** — and they are a perfect **mirror image** on both sides of the ridge. The only way to make that pattern is if new crust forms at the ridge and spreads symmetrically outward." "\n\n"
            r"Two more clues clinched it:" "\n"
            r"- The seafloor is **youngest at the ridge** and gets **older** with distance from it." "\n"
            r"- The oldest ocean floor is **less than about 200 million years** old — far younger than the continents (billions of years) — because old seafloor is constantly recycled back into the mantle." "\n\n"
            r"Seafloor spreading was the **mechanism Wegener lacked**. Combined with continental drift, it became the modern theory of **plate tectonics**." "\n\n"
            r"⚠️ Common misconception: Earth is **not** expanding. New crust made at ridges is balanced by old crust destroyed at **subduction zones** (Lesson 4) — the planet stays the same size." "\n\n"
            r"💡 Tip: the **symmetric magnetic stripes** are the 'barcode' that proves the seafloor spreads.",
        ),
        (
            "4. The Three Plate Boundaries",
            r"Earth's surface is broken into about a dozen major **plates**, each a slab of rigid **lithosphere** (crust + the rigid top of the mantle). Almost all the action happens where plates **meet** — at **boundaries**. What happens depends on how the plates move relative to each other." "\n\n"
            r"**1. Divergent — plates pull APART.** Magma rises into the gap and makes new crust. This is seafloor spreading at mid-ocean ridges; on land it forms **rift valleys** (the East African Rift)." "\n\n"
            r"**2. Convergent — plates COLLIDE.** There are three cases:" "\n"
            r"[[figure:convergent_boundary|Ocean-continent convergence: the dense oceanic plate subducts, carving a deep trench and feeding a chain of volcanoes.]]" "\n"
            r"- **Ocean meets continent** — the denser ocean plate **subducts** (dives under), making a deep **trench** and volcanic mountains (the Andes)." "\n"
            r"- **Ocean meets ocean** — one subducts, building a curved chain of **volcanic islands** (Japan)." "\n"
            r"- **Continent meets continent** — neither is dense enough to sink, so the crust **crumples** into towering **fold mountains** (the Himalayas, where India collides with Asia)." "\n\n"
            r"**3. Transform — plates SLIDE past each other.** No crust is made or destroyed. The plates lock, stress builds, then they slip suddenly — causing **earthquakes**." "\n\n"
            r"[[figure:transform_boundary|At a transform boundary the plates grind past horizontally, offsetting features and triggering earthquakes (the San Andreas Fault).]]" "\n\n"
            r"⚠️ Common misconception: earthquakes and volcanoes are **not** scattered randomly. The vast majority happen **along plate boundaries**, which is why they cluster in the same belts year after year." "\n\n"
            r"💡 Tip: **divergent = build** (ridges); **convergent = collide** (trenches, mountains, volcanoes); **transform = slide** (earthquakes).",
        ),
        (
            "5. Mountains, Volcanoes, Earthquakes & the Ring of Fire",
            r"Plate boundaries don't just move the continents around — they **build the landscape** and drive Earth's biggest hazards. Once you know the boundary, you can predict the feature." "\n\n"
            r"- **Mountains** — *fold* mountains rise where continents collide (the Himalayas); *volcanic* mountains rise above subduction zones (the Andes, the Cascades)." "\n"
            r"- **Volcanoes** — form mostly where a subducting plate melts and magma rises to the surface (and at divergent ridges)." "\n"
            r"- **Earthquakes** — happen when stress released at a locked boundary suddenly slips. The point underground where it starts is the **focus**; the spot directly above on the surface is the **epicenter**." "\n\n"
            r"[[figure:ring_of_fire|The Pacific Ring of Fire: a horseshoe of subduction-zone volcanoes and earthquakes around the rim of the Pacific Ocean.]]" "\n\n"
            r"Because these features trace plate edges, they **cluster** in predictable belts. The most famous is the **Pacific Ring of Fire**, a horseshoe of subduction zones circling the Pacific Ocean. It contains about **75% of the world's active volcanoes** and produces a large share of its biggest earthquakes — including the undersea quakes that can launch **tsunamis**." "\n\n"
            r"⚠️ Common misconception: volcanoes and earthquakes don't strike 'anywhere, equally.' They follow plate boundaries — which is exactly why some regions (Japan, Chile, Indonesia) are far more active than others." "\n\n"
            r"💡 Tip: name the boundary, predict the hazard. The Pacific rim is busy because it is ringed by **subduction zones**.",
        ),
        (
            "6. Hotspots, the Pace of Change & Reading Tectonic Data",
            r"There's one famous exception to 'everything happens at boundaries': **hotspots**. A hotspot is a plume of unusually hot mantle rising in the **middle** of a plate, far from any edge — and it stays roughly **fixed** in place. As the plate slides over it, the plume punches through to make a volcano. Over time this leaves a **chain** of volcanoes that get **older** with distance from the active one." "\n\n"
            r"[[figure:hotspot|A fixed mantle plume builds a volcano; as the plate moves, it carries each volcano away, leaving a trail of older, extinct islands (the Hawaiian chain).]]" "\n\n"
            r"The Hawaiian Islands are the classic example: the Big Island sits over the hotspot now and is still erupting, while the islands to the northwest are older and extinct. The **age-versus-distance** pattern even lets scientists measure how fast and in which direction the plate is moving." "\n\n"
            r"**How fast does the map change?** Plates move about **2–10 cm per year**. That's slow, but it adds up: the Atlantic Ocean widens a few centimeters a year, and India's slow-motion crash into Asia is still pushing the Himalayas higher. Today **GPS** instruments measure this motion directly." "\n\n"
            r"**Reading tectonic data (a GED skill).** Many GED items give a table or graph — island **age vs. distance** from a hotspot, or GPS **plate-velocity** data. Read the **title, axis labels, and units** first; a steady rise of age with distance supports a moving plate; and you can find **rate = distance ÷ time**." "\n\n"
            r"Worked example: an island **500 km** from a hotspot is about **10 million years** old. Speed ≈ 500 km ÷ 10 million yr = 50 km per million years = **5 cm per year**." "\n\n"
            r"⚠️ Common misconception: in a hotspot chain it is the **plate that moves**, not the hotspot. The plume stays put; the conveyor-belt plate carries the old volcanoes away." "\n\n"
            r"💡 Tip: to get a plate's speed from a hotspot chain, **divide the distance by the age** (watch your units — aim for cm/year)." "\n\n"
            r"📚 Sources: USGS, *This Dynamic Earth* (Kious & Tilling) and *Understanding Plate Motions*; Tarbuck & Lutgens, *Earth Science*; Wegener (1915); Hess (1962); Vine & Matthews (1963).",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: continental drift ---
        {
            "text": r"Who proposed the idea that the continents were once joined together and have slowly drifted apart?",
            "difficulty": 1,
            "choices": [("Alfred Wegener", True), ("Isaac Newton", False),
                        ("Charles Darwin", False), ("Galileo Galilei", False)],
            "explanation": r"Alfred Wegener proposed continental drift in 1912, arguing the continents were once joined in the supercontinent Pangaea.",
        },
        {
            "text": r"What was the name of the single supercontinent in Wegener's hypothesis?",
            "difficulty": 1,
            "choices": [("Pangaea", True), ("Gondwana City", False),
                        ("Atlantis", False), ("Laurasia Prime", False)],
            "explanation": r"Wegener named the ancient supercontinent Pangaea, meaning 'all lands.' It later broke apart into today's continents.",
        },
        {
            "text": r"Identical fossils of Mesosaurus, a freshwater reptile that could not cross an ocean, are found on both South America and Africa. This is best explained by:",
            "difficulty": 2,
            "choices": [("The two continents were once joined together", True),
                        ("The reptile swam across the Atlantic Ocean", False),
                        ("Birds carried the fossils across the ocean", False),
                        ("The fossils formed in the ocean and drifted ashore", False)],
            "explanation": r"A freshwater reptile couldn't swim across an ocean, so finding the same species on both continents shows they were once connected — evidence for continental drift.",
        },
        {
            "text": r"Wegener's continental drift idea was rejected by most scientists for decades mainly because he could not:",
            "difficulty": 2,
            "choices": [("Explain HOW the continents could move", True),
                        ("Find any fossils to support it", False),
                        ("Show that the coastlines fit together", False),
                        ("Measure the size of the continents", False)],
            "explanation": r"Wegener had strong evidence but no mechanism — no force that could move continents. That missing explanation is why the idea was dismissed until seafloor spreading was discovered.",
        },
        {
            "text": ("Use the continental drift diagram.\n\n"
                     "[[figure:continental_drift|Pangaea splitting, with matching evidence across continents]]\n\n"
                     "In the diagram, matching mountain belts and rock layers that line up across a now-wide ocean are evidence that the continents:"),
            "difficulty": 2,
            "choices": [("Were once connected as one landmass", True),
                        ("Are about to collide again", False),
                        ("Have always been in their current positions", False),
                        ("Are made of completely different rock", False)],
            "explanation": r"When mountain belts and rock layers match up across separated continents, the simplest explanation is that they formed as one and were later split apart. Pro tip: lined-up rocks = once joined.",
        },
        {
            "text": r"Which of the following was NOT a piece of evidence Wegener used for continental drift?",
            "difficulty": 3,
            "choices": [("GPS satellite measurements of moving continents", True),
                        ("Matching coastlines that fit like puzzle pieces", False),
                        ("Identical fossils on separated continents", False),
                        ("Matching rock layers and mountain belts", False)],
            "explanation": r"GPS is a modern tool that now measures plate motion directly, but it did not exist in Wegener's time. He relied on the fit of coastlines, fossils, rock matches, and ancient climate clues.",
        },
        # --- Lesson 2: mantle convection ---
        {
            "text": r"What is the main source of energy that drives the movement of Earth's plates?",
            "difficulty": 1,
            "choices": [("Heat inside the Earth", True), ("Light from the Sun", False),
                        ("The gravity of the Moon", False), ("Ocean tides", False)],
            "explanation": r"Earth's internal heat (from its formation and from radioactive decay) drives mantle convection, which moves the plates.",
        },
        {
            "text": r"In a mantle convection cell, hot rock ______ and cooler rock ______.",
            "difficulty": 2,
            "choices": [("rises; sinks", True), ("sinks; rises", False),
                        ("disappears; appears", False), ("freezes; melts", False)],
            "explanation": r"Hot, less-dense rock rises; after spreading and cooling near the top it becomes denser and sinks — a convection loop that drags the plates along.",
        },
        {
            "text": r"The force in which a cold, dense plate edge sinking into the mantle drags the rest of the plate along is called:",
            "difficulty": 2,
            "choices": [("Slab pull", True), ("Ridge push", False),
                        ("Tidal force", False), ("Friction lock", False)],
            "explanation": r"Slab pull is the pulling force of a sinking (subducting) slab. It is thought to be the strongest force driving plate motion. (Ridge push is the related shove from an elevated ridge.)",
        },
        {
            "text": r"About how fast do tectonic plates typically move?",
            "difficulty": 2,
            "choices": [("A few centimeters per year", True), ("A few meters per day", False),
                        ("Hundreds of kilometers per year", False), ("They do not move at all", False)],
            "explanation": r"Plates move only a few centimeters a year — roughly the rate your fingernails grow — but over millions of years that adds up to continents crossing the globe.",
        },
        {
            "text": r"The mantle is made of solid rock, yet it still drives the plates. How is that possible?",
            "difficulty": 3,
            "choices": [("Over millions of years the hot solid rock flows very slowly, like stiff putty", True),
                        ("The mantle is actually a deep ocean of liquid lava", False),
                        ("The solid rock cracks and the pieces fly apart", False),
                        ("The mantle is made of loose sand that pours downhill", False)],
            "explanation": r"Mantle rock is solid but hot enough to deform and flow extremely slowly (plastic flow). That slow convective flow is what carries the plates.",
        },
        # --- Lesson 3: seafloor spreading ---
        {
            "text": r"At a mid-ocean ridge, what happens to the seafloor?",
            "difficulty": 1,
            "choices": [("Magma rises and forms new crust that spreads outward", True),
                        ("Old crust piles up and the ocean gets shallower", False),
                        ("Crust is destroyed and pulled into the mantle", False),
                        ("Nothing changes; the seafloor is fixed", False)],
            "explanation": r"At mid-ocean ridges, magma rises, hardens into new oceanic crust, and pushes the older crust outward on both sides — this is seafloor spreading.",
        },
        {
            "text": r"Symmetric magnetic stripes that form a mirror image on both sides of a mid-ocean ridge are strong evidence for:",
            "difficulty": 2,
            "choices": [("Seafloor spreading", True), ("Continental collision", False),
                        ("A shrinking Earth", False), ("The water cycle", False)],
            "explanation": r"As new crust forms at the ridge, it records Earth's magnetic field. The matching, mirror-image stripes on each side show that new seafloor forms at the ridge and spreads symmetrically outward.",
        },
        {
            "text": r"Where is the YOUNGEST oceanic crust found?",
            "difficulty": 2,
            "choices": [("At the mid-ocean ridge", True), ("Next to the continents", False),
                        ("In the deepest trenches", False), ("At the center of the ocean floor only", False)],
            "explanation": r"Crust is newest at the ridge, where it forms, and gets older with distance from the ridge as it spreads away.",
        },
        {
            "text": r"New crust is constantly created at mid-ocean ridges, yet Earth is not getting bigger. Why not?",
            "difficulty": 3,
            "choices": [("Old crust is destroyed at subduction zones at about the same rate", True),
                        ("The new crust is invisible and weighs nothing", False),
                        ("The oceans slowly evaporate to make room", False),
                        ("Earth actually is expanding rapidly", False)],
            "explanation": r"Plate tectonics balances out: the new crust made at ridges is matched by old crust subducted (destroyed) at trenches, so Earth stays the same size.",
        },
        {
            "text": ("Use the seafloor spreading diagram.\n\n"
                     "[[figure:seafloor_spreading|New crust forming and spreading from a mid-ocean ridge]]\n\n"
                     "According to the diagram, as you move AWAY from the ridge, the seafloor becomes:"),
            "difficulty": 2,
            "choices": [("Older", True), ("Younger", False),
                        ("Made of water", False), ("Hotter", False)],
            "explanation": r"The diagram shows the youngest crust at the ridge, with age increasing outward. Pro tip: youngest at the ridge, oldest far from it.",
        },
        # --- Lesson 4: plate boundaries ---
        {
            "text": r"At a divergent plate boundary, the plates:",
            "difficulty": 1,
            "choices": [("Move apart, and new crust forms in the gap", True),
                        ("Collide and form mountains", False),
                        ("Slide past each other", False),
                        ("Stop moving completely", False)],
            "explanation": r"Divergent boundaries are where plates pull apart; magma rises to fill the gap and makes new crust (as at mid-ocean ridges and rift valleys).",
        },
        {
            "text": r"When a dense oceanic plate meets a continental plate, what usually happens?",
            "difficulty": 2,
            "choices": [("The oceanic plate sinks beneath the continent (subduction), forming a trench and volcanoes", True),
                        ("The continental plate sinks beneath the ocean plate", False),
                        ("Both plates slide past each other with no change", False),
                        ("The two plates merge into a single new plate", False)],
            "explanation": r"The denser oceanic plate subducts under the less-dense continental plate, creating a deep trench and a chain of volcanic mountains (like the Andes).",
        },
        {
            "text": r"The Himalayas formed where the Indian plate collided with the Asian plate, with neither sinking. This is a:",
            "difficulty": 2,
            "choices": [("Convergent (continent-continent) boundary", True),
                        ("Divergent boundary", False),
                        ("Transform boundary", False),
                        ("Hotspot", False)],
            "explanation": r"When two continental plates collide, neither is dense enough to subduct, so the crust crumples upward into tall fold mountains — the Himalayas.",
        },
        {
            "text": r"At a transform boundary, where two plates slide past each other, the main hazard is:",
            "difficulty": 2,
            "choices": [("Earthquakes", True), ("New ocean crust forming", False),
                        ("Tall volcanic islands", False), ("Glaciers", False)],
            "explanation": r"At a transform boundary the plates grind, lock, and then slip suddenly, releasing energy as earthquakes — for example, along the San Andreas Fault.",
        },
        {
            "text": ("Use the subduction diagram.\n\n"
                     "[[figure:convergent_boundary|An ocean-continent convergent boundary]]\n\n"
                     "In the diagram, the deep trench forms because:"),
            "difficulty": 2,
            "choices": [("The dense oceanic plate bends and dives down beneath the other plate", True),
                        ("The two plates are pulling apart", False),
                        ("New crust is bubbling up from the ridge", False),
                        ("The continent is sinking into the ocean", False)],
            "explanation": r"The trench marks the line where the dense oceanic plate bends downward and subducts beneath the continent. Pro tip: subduction makes both the trench and the volcanoes.",
        },
        {
            "text": r"At which type of plate boundary is crust NEITHER created nor destroyed?",
            "difficulty": 3,
            "choices": [("Transform", True), ("Divergent", False),
                        ("Convergent", False), ("Subduction", False)],
            "explanation": r"At a transform boundary the plates only slide past each other horizontally — no new crust forms and none is destroyed. Divergent makes crust; convergent destroys it.",
        },
        # --- Lesson 5: mountains, volcanoes, earthquakes, Ring of Fire ---
        {
            "text": r"Most of Earth's earthquakes and volcanoes occur:",
            "difficulty": 1,
            "choices": [("Along plate boundaries", True),
                        ("Randomly all over the planet", False),
                        ("Only in the middle of continents", False),
                        ("Only at the North and South Poles", False)],
            "explanation": r"Earthquakes and volcanoes cluster along plate boundaries, where plates interact. That is why the same belts are active over and over.",
        },
        {
            "text": r"The 'Ring of Fire' is best described as:",
            "difficulty": 2,
            "choices": [("A zone of volcanoes and earthquakes around the rim of the Pacific Ocean", True),
                        ("A ring of fire around the Sun", False),
                        ("A chain of deserts across Africa", False),
                        ("The ring of ice at the South Pole", False)],
            "explanation": r"The Ring of Fire is a horseshoe of subduction zones circling the Pacific Ocean, home to about 75% of the world's active volcanoes and many large earthquakes.",
        },
        {
            "text": r"On a fault, the point on Earth's surface directly above where an earthquake begins is called the:",
            "difficulty": 2,
            "choices": [("Epicenter", True), ("Focus", False),
                        ("Trench", False), ("Hotspot", False)],
            "explanation": r"The earthquake starts underground at the focus; the point on the surface directly above it is the epicenter.",
        },
        # --- Lesson 6: hotspots & data ---
        {
            "text": r"The Hawaiian Islands sit in the middle of the Pacific plate, far from any boundary. They formed from:",
            "difficulty": 2,
            "choices": [("A hotspot — a plume of hot mantle beneath the moving plate", True),
                        ("Two plates colliding", False),
                        ("A transform fault", False),
                        ("Falling meteorites", False)],
            "explanation": r"A hotspot is a fixed mantle plume that builds volcanoes in the middle of a plate. As the Pacific plate moves over it, it leaves a chain of islands like Hawaii.",
        },
        {
            "text": r"In a hotspot island chain, the islands get older with distance from the active volcano because:",
            "difficulty": 3,
            "choices": [("The hotspot stays roughly fixed while the plate moves over it", True),
                        ("The hotspot races across the plate", False),
                        ("Older islands were built first on purpose", False),
                        ("The ocean ages the islands evenly everywhere", False)],
            "explanation": r"The plume stays put while the plate slides over it like a conveyor belt. Each volcano is carried away and goes extinct, so islands age with distance from the hotspot.",
        },
        {
            "text": ("A volcanic island is about 500 km from its hotspot, and rock there is about 10 million years old.\n\n"
                     "Using rate = distance ÷ time, the plate's average speed is closest to:"),
            "difficulty": 3,
            "choices": [("About 5 cm per year", True), ("About 50 cm per year", False),
                        ("About 0.5 cm per year", False), ("About 5 meters per year", False)],
            "explanation": r"500 km ÷ 10 million yr = 50 km per million yr. Converting: 50 km = 5,000,000 cm over 1,000,000 yr = 5 cm/yr. Pro tip: divide distance by age, then watch your units.",
        },
        {
            "text": r"Today, scientists can measure the slow motion of tectonic plates directly using:",
            "difficulty": 2,
            "choices": [("GPS instruments", True), ("Thermometers", False),
                        ("Telescopes", False), ("Rain gauges", False)],
            "explanation": r"Highly precise GPS receivers can detect plate movements of a few centimeters per year, confirming the directions and speeds predicted by plate tectonics.",
        },
    ],
    "essays": [
        {
            "text": (
                "Alfred Wegener proposed continental drift in 1912, but most scientists rejected it for almost "
                "50 years. Explain what evidence Wegener had, why his idea was rejected, and how the discovery of "
                "seafloor spreading later provided the missing piece that turned drift into the theory of plate "
                "tectonics."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) Wegener's evidence — the puzzle-piece fit of coastlines, matching fossils "
                "(e.g., Mesosaurus) on separated continents, matching rock layers/mountain belts, and ancient "
                "climate clues; (2) the reason for rejection — he had no mechanism to explain HOW continents move; "
                "(3) seafloor spreading (Hess) supplied the mechanism — new crust forms at mid-ocean ridges and "
                "spreads outward; (4) the proof — symmetric magnetic stripes and seafloor that ages away from the "
                "ridge. Deduct for claiming continents plow through the seafloor or that Earth is expanding."
            ),
        },
        {
            "text": (
                "Compare the three types of plate boundaries — divergent, convergent, and transform. For each, "
                "describe how the plates move and name one landform or hazard it produces. Then explain why "
                "earthquakes and volcanoes are not scattered randomly across the Earth."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) divergent — plates move apart, new crust forms (mid-ocean ridges / rift "
                "valleys); (2) convergent — plates collide; subduction makes trenches and volcanoes, or collisions "
                "build fold mountains (Himalayas); (3) transform — plates slide past, causing earthquakes (San "
                "Andreas); (4) explanation that quakes and volcanoes cluster along plate boundaries (e.g., the "
                "Pacific Ring of Fire), not at random. Deduct for mixing up the boundary types or their features."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Plate Tectonics & Earth's Changing Surface (Deep Dive)' course."

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
