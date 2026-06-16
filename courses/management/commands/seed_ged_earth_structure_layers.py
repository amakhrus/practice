"""
Seed data: 'GED Science: Earth's Structure & Layers (Deep Dive)'.

This is a focused EXPANSION of Lesson 1 ("Earth's Structure & Layers") from the
broader 'GED Science: Earth & Space Science' course. Where the parent course gives
a one-lesson overview, this course goes deeper: why Earth is layered at all
(density and differentiation), the compositional layers and their named boundaries,
the crucial difference between the *compositional* and *mechanical* ways of dividing
the interior (crust vs. lithosphere), how we actually know what is down there
(seismic waves and the S-wave shadow zone), Earth's internal heat and the
magnetic-field dynamo, and how to read Earth-science depth-profile data.

Every lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, an explicit "common misconception" warning, and a quick tip. Practice
questions mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
short-answer ("Science Short Answer") items were removed in 2017. The two
extended prompts below are kept as study/teaching material only and, like the
parent course, are NOT seeded by this command (Phase 1 is MCQ-only).

Scientific accuracy & sources (used to keep the numbers and claims honest):
  - U.S. Geological Survey (USGS), "Inside the Earth" and
    E. C. Robertson, "The Interior of the Earth" (USGS general-interest pub.).
  - Tarbuck, E. & Lutgens, F., *Earth Science* (Pearson) -- standard GED-level text.
  - Lowrie, W., *Fundamentals of Geophysics* (Cambridge) -- P/S waves, dynamo.
  - Dziewonski, A. & Anderson, D. (1981), "Preliminary Reference Earth Model"
    (PREM), *Phys. Earth Planet. Inter.* -- layer depths used here.
  - Lehmann, I. (1936), "P'" -- discovery of the solid inner core.
  - NASA & NOAA NCEI Geomagnetism -- Earth's magnetic field / magnetosphere.
  - National Geographic Society, Resource Library: "core", "mantle", "crust".
Approximate figures (rounded for learners): mean radius ~6,371 km; crust 5-70 km;
mantle to ~2,890 km (~84% of Earth's volume); outer core 2,890-5,150 km (liquid);
inner core 5,150 km to center (solid); inner-core temperature ~5,200 C.

Run:
    python manage.py seed_ged_earth_structure_layers
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Earth's Structure & Layers (Deep Dive)",
    "slug": "ged-earth-structure-layers",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the inside of our planet, expanding the single 'Earth's Structure & "
        "Layers' lesson from the GED Earth & Space Science course into a full mini-course. You will "
        "learn why Earth is layered at all, what each layer is made of and how hot and deep it is, "
        "the difference between dividing Earth by composition (crust/mantle/core) and by behavior "
        "(lithosphere/asthenosphere), how scientists know all this without ever drilling there "
        "(seismic waves), and how Earth's churning metal core makes the magnetic field that shields "
        "life. Plain language, labeled diagrams, common-misconception warnings, and GED-style "
        "practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. Why Earth Has Layers: Density & Differentiation",
            r"Earth is not a uniform ball of rock. It is sorted into **layers** — dense metal in the center, lighter rock on the outside. But *why*? The answer goes back to how Earth formed about 4.6 billion years ago." "\n\n"
            r"[[figure:earth_layers|The four main layers, from the thin rocky crust down to the scorching solid inner core.]]" "\n\n"
            r"Early Earth was extremely **hot** and partly **molten**, heated by the energy of countless collisions as it grew (accretion) and by the decay of radioactive elements inside it. When much of the planet is molten, gravity does what it does to oil and water: it **sorts material by density**." "\n\n"
            r"- **Dense** materials — mostly **iron and nickel** — sank to the center, forming the **core**." "\n"
            r"- **Lighter** silicate rock floated upward, forming the **mantle** and, at the very top, the thin **crust**." "\n\n"
            r"This sorting of a planet's material by density is called **differentiation**. It is the reason Earth ended up with a metal core wrapped in rocky layers, and the reason it still gets hotter as you go down." "\n\n"
            r"⚠️ Common misconception: the layers did **not** form by being stacked up from the outside, like sediment settling. They **separated from the inside out** by density while Earth was molten — heavy stuff sank, light stuff rose." "\n\n"
            r"💡 Tip: think 'heavy sinks, light floats.' Iron is heavy → core; rock is lighter → mantle and crust.",
        ),
        (
            "2. The Compositional Layers: Crust, Mantle & Core",
            r"The most familiar way to divide Earth is by **what each layer is made of** — its composition. There are three: the **crust**, the **mantle**, and the **core** (and the core has two parts)." "\n\n"
            r"[[figure:earth_interior_scale|Each layer's depth, temperature, and physical state. The crust is razor-thin compared with the mantle and core.]]" "\n\n"
            r"- **Crust** — the thin, solid, outer shell of rock (about **5–70 km** thick). **Oceanic** crust is thin and dense (basalt); **continental** crust is thicker and less dense (granite). It is the coolest layer." "\n"
            r"- **Mantle** — the thick layer of hot **silicate rock** below the crust, reaching to about **2,890 km** deep. It is by far the **biggest** layer (~84% of Earth's volume). It is **mostly solid**, but over long times the hot rock flows slowly, like extremely stiff putty — and that flow drives the plates above." "\n"
            r"- **Outer core** — a layer of **liquid** iron and nickel (about 2,890–5,150 km deep). Its swirling motion creates Earth's **magnetic field**." "\n"
            r"- **Inner core** — a ball of **solid** iron and nickel at the center (about 5,150 km to ~6,371 km, the center). It is the **hottest** part (~5,200°C, close to the Sun's surface) but stays solid because of the crushing pressure." "\n\n"
            r"The boundaries between layers have names you may see on a test: the **Moho** (Mohorovičić discontinuity) separates crust from mantle; the **Gutenberg discontinuity** separates mantle from outer core." "\n\n"
            r"⚠️ Common misconception: the mantle is **not** a sea of molten lava. It is **mostly solid rock** that merely *flows* very slowly. Only small pockets melt, in special places, to make the magma that feeds volcanoes." "\n\n"
            r"💡 Tip: it gets hotter and denser all the way down — rock (crust, mantle) on the outside, metal (outer core, inner core) inside; outer core liquid, inner core solid.",
        ),
        (
            "3. A Different Slice: Lithosphere & Asthenosphere",
            r"Here is the idea that trips up the most students. There are **two different ways** to divide Earth's interior, and they do **not** line up." "\n\n"
            r"Lesson 2 divided Earth by **composition** (crust / mantle / core). But you can also divide the outer Earth by **how the rock behaves** — whether it is rigid or whether it can flow. That gives different layers:" "\n\n"
            r"[[figure:lithosphere_asthenosphere|Two ways to slice the outer Earth. The lithosphere (rigid plates) includes the crust PLUS the cool, rigid top of the mantle.]]" "\n\n"
            r"- **Lithosphere** — the rigid outer shell, about **100 km** thick. Crucially, it is the **crust plus the cool, rigid uppermost part of the mantle**. The lithosphere is cracked into the moving **tectonic plates**." "\n"
            r"- **Asthenosphere** — the hotter, weaker layer of mantle just below (~100–350 km). It behaves plastically and **flows slowly**, and the rigid plates slide on top of it." "\n"
            r"- Below that, the rest of the mantle is **rigid again** (high pressure), then the **liquid** outer core and **solid** inner core." "\n\n"
            r"So the **crust is not the same thing as a plate**. A tectonic plate is a slab of **lithosphere** — crust *and* the rigid top of the mantle welded together. This is exactly what makes plate tectonics possible: rigid plates riding on the soft, flowing asthenosphere." "\n\n"
            r"⚠️ Common misconception: 'the plates are just the continents' or 'the plates are just the crust.' Plates are **lithosphere** (crust + upper mantle), and they carry both continents and ocean floor." "\n\n"
            r"💡 Tip: composition asks *what is it made of?* (crust/mantle/core). Mechanics asks *can it flow?* (rigid lithosphere vs. soft asthenosphere). Lithosphere = crust + rigid mantle top.",
        ),
        (
            "4. How We Know: Seismic Waves & Evidence",
            r"No one has ever been to Earth's core — not even close. The deepest hole humans have ever drilled, the **Kola Superdeep Borehole** in Russia, reached only about **12 km**. Compared with the 6,371 km to the center, that barely scratches the crust. So how can scientists describe layers thousands of kilometers down?" "\n\n"
            r"The trick: we let **earthquakes** do the digging. Every large earthquake sends **seismic waves** racing through the whole planet, and thousands of instruments (**seismometers**) record exactly when and how they arrive. The waves change speed and direction as they pass through different materials, so their patterns reveal the layers — like an ultrasound or CT scan of the Earth." "\n\n"
            r"[[figure:seismic_waves|P-waves pass through both solid and liquid; S-waves stop at the liquid outer core, leaving a 'shadow zone' on the far side.]]" "\n\n"
            r"Two kinds of waves matter most:" "\n"
            r"- **P-waves** (primary) — fast, push-and-pull (compression) waves that travel through **solids and liquids**." "\n"
            r"- **S-waves** (secondary) — slower, side-to-side (shear) waves that travel through **solids only**. A liquid cannot carry an S-wave." "\n\n"
            r"The key clue is the **S-wave shadow zone**: after an earthquake, S-waves never arrive on the far side of the planet. The only way to explain this is a **liquid** layer deep inside that blocks them — that is the direct evidence the **outer core is liquid**. P-waves bend (refract) and slow at the boundaries, which lets scientists map the **depths** of each layer; reflections off the inner core (Inge Lehmann, 1936) showed the **inner core is solid**." "\n\n"
            r"⚠️ Common misconception: scientists have **not** drilled to or sampled the mantle or core. Everything about the deep interior is **inferred** from seismic waves, from Earth's gravity and total mass, from iron meteorites (pieces of shattered cores), and from lab experiments — not from direct samples." "\n\n"
            r"💡 Tip: **P** = passes through everything (liquid too); **S** = stops at the liquid (solids only). The S-wave shadow zone = proof the outer core is liquid.",
        ),
        (
            "5. Earth's Internal Heat & the Magnetic Field",
            r"Earth's interior is astonishingly hot — hot enough at the center to rival the Sun's surface. Two sources keep it that way over billions of years:" "\n\n"
            r"1. **Primordial heat** — leftover heat from Earth's violent formation and differentiation." "\n"
            r"2. **Radiogenic heat** — heat constantly released by the **radioactive decay** of elements like uranium, thorium, and potassium-40 in the rock." "\n\n"
            r"That heat slowly escapes toward the surface (you can measure it: temperature rises with depth — the **geothermal gradient**). The escaping heat drives **convection**: hot material rises, cooler material sinks, in slow loops in the mantle and in the liquid outer core." "\n\n"
            r"[[figure:geomagnetic_field|Convection of liquid iron in the outer core, plus Earth's spin, works like a dynamo to generate the magnetic field.]]" "\n\n"
            r"That convection of **liquid iron** in the outer core, combined with Earth's **rotation**, acts like a giant electric generator — the **geodynamo**. It produces Earth's **magnetic field**, which is shaped roughly like a bar magnet's (a dipole). The magnetic poles sit near, but not exactly at, the geographic poles, and they slowly wander; over geologic time the field has even **reversed** direction many times." "\n\n"
            r"Why care? The magnetic field forms a protective bubble (the **magnetosphere**) that **deflects much of the solar wind** and cosmic radiation, helping shield the atmosphere and life — and it is why a compass needle points north." "\n\n"
            r"⚠️ Common misconception: Earth's magnetism is **not** from a giant permanent magnet inside. At these temperatures iron is far too hot to stay permanently magnetized (it is above the **Curie point**). The field is **generated by moving liquid metal** — a dynamo — and would fade if the core stopped churning." "\n\n"
            r"💡 Tip: heat (from formation + radioactivity) → convection of liquid iron → spinning dynamo → magnetic field → shields the planet.",
        ),
        (
            "6. Boundaries, Two Layer Schemes & Reading the Data",
            r"Let's pull it together. Earth can be divided **two ways at once**, and a good test-taker keeps them straight:" "\n\n"
            r"- **By composition** (what it's made of): **crust → mantle → outer core → inner core**." "\n"
            r"- **By mechanical behavior** (how it acts): **lithosphere → asthenosphere → lower (rigid) mantle → liquid outer core → solid inner core**." "\n\n"
            r"The boundaries between layers are real, sharp surfaces called **discontinuities**, each found from seismic data and named for its discoverer:" "\n"
            r"- **Moho** — crust ↔ mantle (Andrija Mohorovičić, 1909)." "\n"
            r"- **Gutenberg discontinuity** — mantle ↔ outer core (~2,890 km)." "\n"
            r"- **Lehmann discontinuity** — outer core ↔ inner core (Inge Lehmann, 1936)." "\n\n"
            r"[[figure:earth_interior_scale|Use a depth profile to find boundaries: look for places where a measured value changes sharply.]]" "\n\n"
            r"**Reading Earth-science data (a GED skill).** Many GED Science items give a graph or table — for example, **seismic wave speed vs. depth** or **temperature vs. depth**. Read the **title, axis labels, and units** first; then hunt for **sudden changes**, because a sharp jump or drop marks a **boundary** between layers. Use only what the data **shows**." "\n\n"
            r"Worked example: on a graph of **S-wave speed vs. depth**, the S-wave speed **drops to zero at about 2,890 km**. Conclusion: a **liquid** layer (the outer core) begins there, because S-waves cannot travel through liquid. That single feature locates the mantle–core boundary." "\n\n"
            r"⚠️ Common misconception: rising temperature with depth does **not** mean the mantle is molten. Pressure rises with depth too, which keeps the rock solid; and S-waves *do* pass through the mantle — proof it is solid." "\n\n"
            r"💡 Tip: to find a layer boundary in any depth profile, look for the **sudden change**." "\n\n"
            r"📚 Sources: USGS, *Inside the Earth*; Tarbuck & Lutgens, *Earth Science*; Lowrie, *Fundamentals of Geophysics*; Dziewonski & Anderson (1981), PREM; Lehmann (1936); NASA & NOAA NCEI Geomagnetism.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: differentiation ---
        {
            "text": r"Why did Earth separate into layers, with dense metal at the center and lighter rock on the outside?",
            "difficulty": 1,
            "choices": [("While early Earth was hot and partly molten, dense material sank and lighter material rose", True),
                        ("Layers piled up from the outside over time, like sediment settling", False),
                        ("The Sun's gravity pulled all the metal toward Earth's center", False),
                        ("Meteorites delivered a ready-made iron core to the planet", False)],
            "explanation": r"When much of early Earth was molten, gravity sorted the material by density: heavy iron and nickel sank to form the core, while lighter rock rose to form the mantle and crust. This sorting is called differentiation.",
        },
        {
            "text": r"The process in which a planet's material sorts itself by density, sending heavy iron to the center, is called:",
            "difficulty": 2,
            "choices": [("Differentiation", True), ("Condensation", False), ("Erosion", False), ("Convection", False)],
            "explanation": r"Differentiation is the separation of a body's material by density. It is why Earth has a metal core wrapped in rocky layers.",
        },
        {
            "text": r"Earth's core is mostly iron and nickel, while the crust and mantle are rock. This difference is best explained by:",
            "difficulty": 2,
            "choices": [("Density sorting while Earth was molten — heavy metal sank, lighter rock rose", True),
                        ("The core being a captured asteroid", False),
                        ("Rock slowly turning into metal under pressure", False),
                        ("The magnetic field pulling iron to the center", False)],
            "explanation": r"During Earth's molten early stage, the densest materials (iron, nickel) sank to the center while less-dense silicate rock floated up — differentiation by density.",
        },
        # --- Lesson 2: compositional layers ---
        {
            "text": r"Which is the thickest layer of Earth, making up most of its volume?",
            "difficulty": 1,
            "choices": [("The mantle", True), ("The crust", False), ("The outer core", False), ("The inner core", False)],
            "explanation": r"The mantle reaches to about 2,890 km deep and makes up roughly 84% of Earth's volume — by far the largest layer. The crust is only a thin skin on top.",
        },
        {
            "text": r"How is the mantle BEST described?",
            "difficulty": 2,
            "choices": [("Mostly solid rock that flows very slowly over long periods of time", True),
                        ("A deep ocean of molten lava", False),
                        ("A layer of liquid metal", False),
                        ("Loose sand and sediment", False)],
            "explanation": r"The mantle is mostly solid silicate rock. Over millions of years it can flow slowly like stiff putty, but it is not a sea of lava — only small pockets melt to feed volcanoes.",
        },
        {
            "text": r"Oceanic crust differs from continental crust in that oceanic crust is generally:",
            "difficulty": 2,
            "choices": [("Thinner and denser (basalt)", True),
                        ("Thicker and less dense (granite)", False),
                        ("Made of liquid metal", False),
                        ("Part of the inner core", False)],
            "explanation": r"Oceanic crust is thin (about 5–10 km) and dense, made mostly of basalt. Continental crust is thicker (about 30–70 km) and less dense, made mostly of granite.",
        },
        {
            "text": r"The outer core and inner core are made mostly of which materials?",
            "difficulty": 1,
            "choices": [("Iron and nickel", True), ("Silicate rock", False),
                        ("Water and ice", False), ("Granite and basalt", False)],
            "explanation": r"Both parts of the core are mostly iron and nickel (metal). The outer core is liquid; the inner core is solid.",
        },
        {
            "text": r"The inner core is the hottest part of Earth (about 5,200°C), yet it is SOLID. Why?",
            "difficulty": 3,
            "choices": [("The crushing pressure at Earth's center raises iron's melting point above the local temperature", True),
                        ("It is actually cooler than the outer core", False),
                        ("It is made of rock, not metal", False),
                        ("The magnetic field freezes it", False)],
            "explanation": r"Despite being hottest, the inner core stays solid because the immense pressure at the center raises the melting point of iron above the (very high) temperature there. The outer core, at lower pressure, stays liquid.",
        },
        {
            "text": r"Roughly how far is it from Earth's surface down to its center?",
            "difficulty": 2,
            "choices": [("About 6,400 km", True), ("About 640 km", False),
                        ("About 64 km", False), ("About 64,000 km", False)],
            "explanation": r"Earth's mean radius is about 6,371 km — roughly 6,400 km from the surface to the center.",
        },
        {
            "text": r"The boundary between the crust and the mantle, marked by a sudden jump in seismic wave speed, is the:",
            "difficulty": 3,
            "choices": [("Mohorovičić discontinuity (the 'Moho')", True),
                        ("Gutenberg discontinuity", False),
                        ("Lehmann discontinuity", False),
                        ("Equator", False)],
            "explanation": r"The Moho separates the crust from the mantle. (The Gutenberg discontinuity is the mantle–core boundary; the Lehmann discontinuity divides the outer and inner core.)",
        },
        {
            "text": ("Use the diagram of Earth's interior.\n\n"
                     "[[figure:earth_interior_scale|Depth, temperature, and state of Earth's layers]]\n\n"
                     "According to the diagram, which layer is LIQUID?"),
            "difficulty": 1,
            "choices": [("The outer core", True), ("The crust", False),
                        ("The mantle", False), ("The inner core", False)],
            "explanation": r"The diagram labels the outer core as liquid iron and nickel. The crust, mantle, and inner core are all solid. Pro tip: outer core = liquid; inner core = solid.",
        },
        # --- Lesson 3: lithosphere vs. asthenosphere ---
        {
            "text": r"The lithosphere — the rigid shell that is broken into tectonic plates — is made of:",
            "difficulty": 2,
            "choices": [("The crust plus the rigid uppermost part of the mantle", True),
                        ("Only the crust", False),
                        ("The entire mantle", False),
                        ("The outer core", False)],
            "explanation": r"The lithosphere is the crust welded to the cool, rigid top of the mantle (about 100 km thick total). This is why a tectonic plate is not the same thing as the crust.",
        },
        {
            "text": r"Tectonic plates slide on top of which weak, slowly flowing layer?",
            "difficulty": 2,
            "choices": [("The asthenosphere", True), ("The inner core", False),
                        ("The crust", False), ("The stratosphere", False)],
            "explanation": r"The asthenosphere is the hot, plastic part of the upper mantle (~100–350 km). The rigid lithospheric plates ride and slide on it.",
        },
        {
            "text": r"Which statement correctly contrasts the TWO ways of dividing Earth's interior?",
            "difficulty": 3,
            "choices": [("Crust/mantle/core divides Earth by composition; lithosphere/asthenosphere divides it by how the rock behaves", True),
                        ("They are just two names for the exact same layers", False),
                        ("Composition layers are mechanical; behavior layers are chemical", False),
                        ("Only the lithosphere/asthenosphere scheme is real", False)],
            "explanation": r"One scheme groups layers by what they are made of (composition: crust, mantle, core). The other groups them by mechanical behavior — rigid vs. flowing (lithosphere, asthenosphere, etc.). They overlap but do not line up.",
        },
        {
            "text": ("Use the diagram comparing the two layer schemes.\n\n"
                     "[[figure:lithosphere_asthenosphere|Composition vs. mechanical layering of the outer Earth]]\n\n"
                     "Based on the diagram, how do the crust and the lithosphere compare?"),
            "difficulty": 2,
            "choices": [("They are not the same; the lithosphere includes the crust PLUS part of the mantle", True),
                        ("They are exactly the same layer", False),
                        ("The crust is larger than the lithosphere", False),
                        ("The lithosphere is part of the core", False)],
            "explanation": r"The diagram shows the lithosphere bracket covering the crust and the rigid top of the mantle. So the lithosphere is thicker than the crust alone. Pro tip: a plate = lithosphere, not just crust.",
        },
        # --- Lesson 4: seismic waves & evidence ---
        {
            "text": r"Since we cannot drill to Earth's core, how do scientists learn about the deep interior?",
            "difficulty": 1,
            "choices": [("By studying seismic waves from earthquakes", True),
                        ("By drilling out core samples", False),
                        ("By taking satellite photos of the surface", False),
                        ("By melting through the crust with lasers", False)],
            "explanation": r"Seismic waves from earthquakes travel through the whole planet and change with the material they pass through, so their patterns reveal the layers — an indirect 'scan' of Earth's interior.",
        },
        {
            "text": r"Which seismic wave travels through BOTH solids and liquids and arrives first?",
            "difficulty": 2,
            "choices": [("The P-wave", True), ("The S-wave", False),
                        ("The ocean wave", False), ("The radio wave", False)],
            "explanation": r"P-waves (primary) are fast compression waves that pass through solids and liquids and arrive first. S-waves (secondary) are slower and travel through solids only.",
        },
        {
            "text": r"S-waves cannot travel through liquid, and they vanish on the far side of Earth (the 'S-wave shadow zone'). This is the main evidence that:",
            "difficulty": 2,
            "choices": [("The outer core is liquid", True),
                        ("The mantle is made of metal", False),
                        ("The crust is very thick", False),
                        ("The inner core is liquid", False)],
            "explanation": r"Because S-waves need a solid and disappear on the opposite side of the planet, a liquid layer must be blocking them. That layer is the liquid outer core.",
        },
        {
            "text": r"The deepest hole ever drilled (the Kola borehole) reached only about 12 km, while Earth's center is about 6,371 km down. This shows that:",
            "difficulty": 2,
            "choices": [("Humans have directly sampled only a tiny fraction of the crust", True),
                        ("We have drilled all the way to the mantle", False),
                        ("The crust is only 12 km from the core", False),
                        ("Drilling is how we discovered the core", False)],
            "explanation": r"12 km is a tiny sliver of the 6,371 km to the center — barely into the crust. Knowledge of the mantle and core comes from seismic waves and other indirect evidence, not drilling.",
        },
        {
            "text": ("Use the seismic-wave diagram.\n\n"
                     "[[figure:seismic_waves|P-waves and S-waves traveling through Earth]]\n\n"
                     "In the diagram, why do the S-waves fail to reach the bottom of the globe?"),
            "difficulty": 3,
            "choices": [("They are stopped by the liquid outer core, which cannot carry a shear wave", True),
                        ("They are too fast to be recorded there", False),
                        ("The inner core absorbs all of them", False),
                        ("The crust reflects them back upward", False)],
            "explanation": r"The diagram shows S-waves halting at the liquid outer core, creating a shadow zone on the far side. Liquids cannot transmit S-waves. Pro tip: the S-wave shadow zone is the classic proof the outer core is liquid.",
        },
        # --- Lesson 5: heat & magnetic field ---
        {
            "text": r"What are the two main sources of Earth's internal heat?",
            "difficulty": 2,
            "choices": [("Leftover heat from Earth's formation and heat from radioactive decay", True),
                        ("Sunlight and friction from the wind", False),
                        ("The Moon's gravity and ocean tides", False),
                        ("Lightning strikes and volcanoes", False)],
            "explanation": r"Earth stays hot inside from primordial heat (left over from its formation and differentiation) plus radiogenic heat (the ongoing decay of radioactive elements like uranium, thorium, and potassium-40).",
        },
        {
            "text": r"Earth's magnetic field is generated mainly by:",
            "difficulty": 2,
            "choices": [("The motion of liquid iron in the outer core (a dynamo)", True),
                        ("A giant permanent bar magnet at the center", False),
                        ("The Sun's magnetic field reaching Earth", False),
                        ("The spinning of the solid crust", False)],
            "explanation": r"Churning, electrically conducting liquid iron in the outer core, together with Earth's rotation, acts like a generator — the geodynamo — producing the magnetic field.",
        },
        {
            "text": r"Why can't Earth's magnetic field come from a permanent magnet at its center?",
            "difficulty": 3,
            "choices": [("The interior is far too hot; above a certain temperature iron loses permanent magnetism", True),
                        ("There is no iron at Earth's center", False),
                        ("Magnets only work in space", False),
                        ("The inner core spins too slowly", False)],
            "explanation": r"Above the Curie point, iron cannot stay permanently magnetized — and Earth's interior is far hotter than that. The field must be actively generated by moving liquid metal (a dynamo), not stored in a permanent magnet.",
        },
        {
            "text": r"One important benefit of Earth's magnetic field is that it:",
            "difficulty": 2,
            "choices": [("Deflects much of the solar wind, helping protect the atmosphere and life", True),
                        ("Provides the oxygen we breathe", False),
                        ("Causes the seasons", False),
                        ("Holds the continents together", False)],
            "explanation": r"The magnetic field forms the magnetosphere, which deflects much of the charged-particle solar wind and cosmic radiation — shielding the atmosphere and life (and making compasses work).",
        },
        {
            "text": r"As you go deeper into Earth, the temperature generally:",
            "difficulty": 1,
            "choices": [("Increases (the geothermal gradient)", True),
                        ("Decreases steadily", False),
                        ("Stays exactly the same", False),
                        ("Drops to freezing in the core", False)],
            "explanation": r"Temperature rises with depth — this is the geothermal gradient — reaching thousands of degrees in the core. The escaping heat drives convection in the mantle and outer core.",
        },
        {
            "text": ("Use the geodynamo diagram.\n\n"
                     "[[figure:geomagnetic_field|Earth's magnetic field generated by the outer core]]\n\n"
                     "According to the diagram, the magnetic field is produced by:"),
            "difficulty": 2,
            "choices": [("Churning liquid iron in the outer core plus Earth's spin", True),
                        ("The Sun heating the crust", False),
                        ("Ice melting at the poles", False),
                        ("The Moon orbiting Earth", False)],
            "explanation": r"The diagram shows liquid iron convecting in the outer core while Earth spins — together acting as a dynamo that generates the field and deflects the solar wind.",
        },
        # --- Lesson 6: boundaries & data reasoning ---
        {
            "text": r"The named boundaries Moho, Gutenberg, and Lehmann are all:",
            "difficulty": 1,
            "choices": [("Boundaries (discontinuities) between Earth's internal layers", True),
                        ("Types of earthquakes", False),
                        ("Mountain ranges on the surface", False),
                        ("Names of tectonic plates", False)],
            "explanation": r"Each is a 'discontinuity' where seismic waves change sharply: Moho (crust–mantle), Gutenberg (mantle–core), Lehmann (outer–inner core).",
        },
        {
            "text": r"On a graph of S-wave speed versus depth, the S-wave speed drops to ZERO at about 2,890 km. The best conclusion is that:",
            "difficulty": 2,
            "choices": [("A liquid layer (the outer core) begins at that depth", True),
                        ("The earthquake stopped at that depth", False),
                        ("The mantle ends and the crust begins", False),
                        ("The graph must be a mistake", False)],
            "explanation": r"S-waves cannot travel through liquid, so an S-wave speed of zero marks the top of the liquid outer core — the mantle–core boundary, at about 2,890 km.",
        },
        {
            "text": r"A student says a temperature-vs-depth graph 'proves the mantle is molten' because temperature rises with depth. What is the BEST critique?",
            "difficulty": 3,
            "choices": [("Rising temperature alone doesn't prove melting; pressure also rises and keeps the rock solid, and S-waves pass through the mantle (showing it is solid)", True),
                        ("The student is correct; the whole mantle is molten lava", False),
                        ("Temperature has nothing to do with the state of rock", False),
                        ("The mantle is actually liquid metal", False)],
            "explanation": r"High temperature is only half the story — pressure rises with depth too, keeping mantle rock solid. The clincher is that S-waves travel through the mantle, which only solids allow. Pro tip: use ALL the evidence, not one variable.",
        },
    ],
    "essays": [
        {
            "text": (
                "No one has ever drilled to Earth's core, yet scientists are confident that the outer core is "
                "liquid and the inner core is solid. Explain how they know. In your answer, describe how seismic "
                "P-waves and S-waves behave, and explain what the 'S-wave shadow zone' tells us."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) we cannot drill there (the deepest hole reaches only ~12 km of ~6,371 km), so "
                "evidence is indirect; (2) earthquakes send seismic waves through Earth, recorded by seismometers; "
                "(3) P-waves travel through both solids and liquids, S-waves through solids only; (4) S-waves vanish "
                "on the far side — the S-wave shadow zone — which shows a liquid layer (the outer core) blocks them; "
                "(5) bonus: P-wave refraction and reflections (Lehmann) reveal the depths and the solid inner core. "
                "Deduct for claiming the interior was sampled directly by drilling."
            ),
        },
        {
            "text": (
                "Geologists divide Earth's interior two different ways: by composition (crust, mantle, core) and by "
                "mechanical behavior (lithosphere, asthenosphere, and so on). Compare the two schemes. Explain why the "
                "lithosphere is NOT the same as the crust, and why that distinction matters for plate tectonics."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the compositional scheme groups layers by what they are made of (crust/mantle/core); "
                "(2) the mechanical scheme groups them by whether they are rigid or can flow (lithosphere/asthenosphere/…); "
                "(3) the lithosphere is the crust PLUS the rigid uppermost mantle (~100 km), so it is thicker than the crust "
                "alone; (4) the asthenosphere is soft, hot mantle that flows, and the rigid lithospheric plates slide on it; "
                "(5) this is what makes plate tectonics work — rigid plates riding on the flowing asthenosphere. Deduct for "
                "equating 'plate' with 'crust' or 'continent.'"
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Earth's Structure & Layers (Deep Dive)' course."

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
