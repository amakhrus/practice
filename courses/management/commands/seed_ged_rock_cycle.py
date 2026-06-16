"""
Seed data: 'GED Science: The Rock Cycle & Minerals (Deep Dive)'.

A focused EXPANSION of Lesson 3 ("The Rock Cycle & Minerals") from the broader
'GED Science: Earth & Space Science' course. The parent course gives a one-lesson
overview of the three rock families; this course goes deeper:

  1. Minerals as the building blocks of rocks (and how we identify them: Mohs
     hardness, luster, streak, cleavage).
  2. Igneous rocks -- magma vs. lava, and how cooling rate sets crystal size
     (intrusive vs. extrusive).
  3. Sedimentary rocks -- weathering, erosion, deposition, lithification; clastic,
     chemical, and organic types; strata, superposition, and fossils.
  4. Metamorphic rocks -- solid-state change by heat & pressure; foliated vs.
     non-foliated; parent-rock pairs.
  5. The rock cycle -- the full set of pathways connecting all three families and
     magma, with no fixed start or order.
  6. Reading the rocks -- using texture and layering to identify a rock, everyday
     uses of rocks & minerals, and data/key reasoning.

This course uses ALL-NEW diagrams (Mohs scale, igneous textures, sedimentary
layering, metamorphic foliation, a detailed rock-cycle wheel, and a three-family
comparison chart) rather than reusing the parent course's 'rock_cycle' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - U.S. Geological Survey (USGS), "Rocks and Minerals" and the National Park
    Service Geology education resources.
  - Tarbuck, E. & Lutgens, F., *Earth Science*; Marshak, S., *Essentials of
    Geology* (W. W. Norton) -- standard texts for rock classification.
  - Mohs, F. (1812) -- the relative hardness scale (talc 1 ... diamond 10).
  - National Geographic Society, Resource Library: "rock cycle," "mineral."
Note on hardness: Mohs is a RELATIVE (ordinal) scale -- a 10 is not "ten times"
harder than a 1; the gaps are uneven (diamond, 10, is far harder than the step
from 9 would suggest).

Run:
    python manage.py seed_ged_rock_cycle
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: The Rock Cycle & Minerals (Deep Dive)",
    "slug": "ged-rock-cycle",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the rocks beneath your feet, expanding the single 'Rock Cycle & Minerals' "
        "lesson from the GED Earth & Space Science course into a full mini-course. You'll start with "
        "minerals -- the building blocks of rocks -- and how to identify them, then explore how each of "
        "the three rock families forms: igneous from cooling magma, sedimentary from layers of "
        "sediment, and metamorphic from heat and pressure. Finally you'll see how the rock cycle ties "
        "them all together, with any rock able to become any other over time. Plain language, all-new "
        "labeled diagrams, common-misconception warnings, and GED-style practice with full explanations."
    ),
    "lessons": [
        (
            "1. Minerals: The Building Blocks of Rocks",
            r"Before we can understand rocks, we need to meet their ingredients: **minerals**. People often use 'rock' and 'mineral' to mean the same thing, but to a geologist they are different." "\n\n"
            r"A **mineral** is a **naturally occurring**, **inorganic** (non-living) **solid** with a **definite chemical makeup** and an orderly **crystal structure** — for example, quartz, calcite, or feldspar. A **rock** is a solid made of **one or more minerals** packed together. So a rock is like a fruitcake, and the minerals are the nuts and fruit inside it." "\n\n"
            r"[[figure:mohs_hardness|The Mohs scale ranks minerals by hardness — each mineral can scratch any mineral softer than itself.]]" "\n\n"
            r"Because each mineral has its own properties, geologists **identify** minerals by testing them:" "\n"
            r"- **Hardness** — resistance to scratching, ranked 1–10 on the **Mohs scale** (talc = 1, diamond = 10). A mineral scratches anything softer than itself." "\n"
            r"- **Luster** — how the surface reflects light (metallic vs. glassy/dull)." "\n"
            r"- **Streak** — the color of the mineral's powder when rubbed on a tile (often more reliable than the mineral's color)." "\n"
            r"- **Cleavage** — whether it breaks along smooth, flat planes or into uneven chunks." "\n\n"
            r"⚠️ Common misconception: color is **not** a reliable way to identify a mineral. The same mineral (like quartz) comes in many colors, and different minerals can share a color — that's why streak and hardness are more trustworthy." "\n\n"
            r"💡 Tip: a **mineral** is one pure ingredient with a fixed recipe; a **rock** is a mixture of mineral grains. Mohs scale: the higher the number, the harder.",
        ),
        (
            "2. Igneous Rocks: Born from Fire",
            r"**Igneous** rock is the starting point of most rock — it forms when hot, molten rock **cools and hardens** (the word comes from the Latin for 'fire'). The clue to *how* an igneous rock formed is hidden in its **crystal size**." "\n\n"
            r"First, two words people mix up:" "\n"
            r"- **Magma** — molten rock **below** the surface." "\n"
            r"- **Lava** — molten rock that has **erupted onto** the surface." "\n\n"
            r"[[figure:igneous_textures|Slow cooling underground grows large crystals (intrusive); fast cooling at the surface freezes tiny ones (extrusive).]]" "\n\n"
            r"How fast the melt cools controls the crystals:" "\n"
            r"- **Intrusive** (plutonic) rock cools **slowly deep underground**. Atoms have lots of time to arrange themselves, so the crystals grow **large** enough to see — like **granite**." "\n"
            r"- **Extrusive** (volcanic) rock cools **quickly at the surface**. There's little time, so crystals stay **tiny** — like **basalt**. If cooling is almost instant, no crystals form at all and you get volcanic glass like **obsidian**; trapped gas bubbles make frothy **pumice**." "\n\n"
            r"⚠️ Common misconception: big crystals do **not** mean a rock is old or 'better' — they mean it cooled **slowly**. Tiny crystals mean **fast** cooling, not youth." "\n\n"
            r"💡 Tip: **slow & deep → large crystals; fast & surface → small crystals (or glass).**",
        ),
        (
            "3. Sedimentary Rocks: Layers of Time",
            r"**Sedimentary** rock is the great record-keeper of Earth's history. It forms at or near the surface, building up in **layers** over long stretches of time — and those layers can trap **fossils**." "\n\n"
            r"[[figure:sedimentary_layers|Weathering and erosion make sediment that is deposited in layers, then compacted and cemented into rock.]]" "\n\n"
            r"The process (sometimes called **lithification**) goes step by step:" "\n"
            r"1. **Weathering** breaks existing rock into small pieces (sediment)." "\n"
            r"2. **Erosion** carries the sediment away, usually by water, wind, or ice." "\n"
            r"3. **Deposition** drops the sediment in flat layers, often in lakes or the sea." "\n"
            r"4. **Compaction & cementation** press and glue the layers into solid rock." "\n\n"
            r"There are three main kinds, by what the sediment is:" "\n"
            r"- **Clastic** — bits of other rock cemented together (**sandstone**, **shale**, conglomerate)." "\n"
            r"- **Chemical** — minerals left behind when water evaporates (**rock salt**, some **limestone**)." "\n"
            r"- **Organic** — built from the remains of living things (**coal** from plants; much **limestone** from shells)." "\n\n"
            r"Because layers stack up over time, in undisturbed rock the **oldest layer is on the bottom** and the youngest on top — the **law of superposition**, a key tool for reading Earth's past." "\n\n"
            r"⚠️ Common misconception: **fossils** are found almost only in **sedimentary** rock. The intense heat that forms igneous and metamorphic rock usually destroys any remains." "\n\n"
            r"💡 Tip: think **'sediment → settles in layers.'** Flat layers + fossils = sedimentary; bottom layer = oldest.",
        ),
        (
            "4. Metamorphic Rocks: Changed by Heat & Pressure",
            r"**Metamorphic** rock is a 'made-over' rock. Take any existing rock — igneous, sedimentary, or even another metamorphic rock — bury it deep where it is squeezed by **pressure** and baked by **heat**, and its minerals rearrange into something new. The key: this happens in the **solid state**, *without melting* (if it melted, it would become magma and then igneous)." "\n\n"
            r"[[figure:metamorphic_change|Heat and pressure realign the minerals of a parent rock into bands (foliation) — no melting required.]]" "\n\n"
            r"The original rock is called the **parent rock**, and there are two textures:" "\n"
            r"- **Foliated** — minerals line up into visible **bands** or layers, because pressure squeezes them flat. Examples (in order of increasing heat/pressure): **shale → slate → schist → gneiss**." "\n"
            r"- **Non-foliated** — no banding, just a denser, often crystalline rock. Examples: **limestone → marble**, and **sandstone → quartzite**." "\n\n"
            r"⚠️ Common misconception: metamorphism does **not** melt the rock. If it melted, you'd be making igneous rock instead. Metamorphic change happens while the rock stays **solid**." "\n\n"
            r"💡 Tip: **'metamorphosis = change.'** Heat + pressure (no melting) → bands (foliated) like gneiss, or solid recrystallized rock (non-foliated) like marble.",
        ),
        (
            "5. The Rock Cycle: Everything Is Connected",
            r"Now put the pieces together. Rocks are not permanent — given enough time, **any rock can become any other kind**. This endless set of changes is the **rock cycle**, and it is powered by Earth's internal heat and by surface processes like weathering." "\n\n"
            r"[[figure:rock_cycle_detailed|Magma, igneous, sedimentary, and metamorphic rock are linked by melting, cooling, weathering, deposition, and heat & pressure.]]" "\n\n"
            r"Follow the main processes that move a rock around the cycle:" "\n"
            r"- **Melting** turns any rock into **magma**." "\n"
            r"- **Cooling & crystallizing** turns magma into **igneous** rock." "\n"
            r"- **Weathering, erosion, deposition, then compaction & cementation** turn any rock into **sedimentary** rock." "\n"
            r"- **Heat & pressure** turn any rock into **metamorphic** rock." "\n\n"
            r"The cycle has **no fixed starting point and no set order**. A metamorphic rock might melt and become igneous; an igneous rock might be weathered into sediment; a sedimentary rock might be cooked into metamorphic — and round and round, over millions of years." "\n\n"
            r"⚠️ Common misconception: the rock cycle is **not** a one-way street that always goes igneous → sedimentary → metamorphic. Rocks can take many different paths, skipping steps or repeating them." "\n\n"
            r"💡 Tip: tie each arrow to a process — **melt** → magma; **cool** → igneous; **weather + compact** → sedimentary; **heat + pressure** → metamorphic.",
        ),
        (
            "6. Reading the Rocks: Identifying & Using Them",
            r"Geologists are detectives: a rock's **texture** tells the story of how it formed, and that lets you **identify** it and even put a number on Earth's past." "\n\n"
            r"[[figure:rock_classes|How each rock family forms, the clue that gives it away, and common examples.]]" "\n\n"
            r"A simple identification key:" "\n"
            r"- **Interlocking crystals, no layers or bands** → **igneous** (big crystals = slow/intrusive; tiny = fast/extrusive)." "\n"
            r"- **Flat layers or visible grains, maybe fossils** → **sedimentary**." "\n"
            r"- **Bands of aligned minerals, or a shiny, recrystallized look** → **metamorphic**." "\n\n"
            r"Rocks and minerals are also everywhere in daily life: **granite** countertops, **marble** statues, **limestone** in cement, **coal** and oil for energy, **salt** for food, and metals refined from **ore** minerals. Reading rock layers also lets geologists date events: by **superposition**, lower layers are older, so a fossil in a deep layer is older than one above it." "\n\n"
            r"**Reading rock data (a GED skill).** GED items may give a **property table** (hardness, luster, streak) or an **identification key** and ask you to classify a sample. Match the clues to the key, and use only what the data shows — for instance, a sample with clear mineral **bands** is metamorphic." "\n\n"
            r"⚠️ Common misconception: you can't reliably name a rock by **color** alone. Use **texture** — crystals, layers, or bands — which records how it actually formed." "\n\n"
            r"💡 Tip: identify by texture: **crystals = igneous, layers = sedimentary, bands = metamorphic.**" "\n\n"
            r"📚 Sources: USGS *Rocks and Minerals*; National Park Service Geology; Tarbuck & Lutgens, *Earth Science*; Marshak, *Essentials of Geology*; Mohs (1812).",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: minerals ---
        {
            "text": r"Which statement best describes a mineral?",
            "difficulty": 1,
            "choices": [("A naturally occurring, inorganic solid with a definite chemical makeup and crystal structure", True),
                        ("Any hard object found in the ground", False),
                        ("A man-made crystal grown in a lab", False),
                        ("A mixture of several different rocks", False)],
            "explanation": r"A mineral is naturally occurring, inorganic, solid, with a fixed chemical composition and an orderly crystal structure (like quartz or calcite). A rock, by contrast, is a mixture of minerals.",
        },
        {
            "text": r"What is the relationship between rocks and minerals?",
            "difficulty": 1,
            "choices": [("A rock is made of one or more minerals", True),
                        ("A mineral is made of many rocks", False),
                        ("Rocks and minerals are exactly the same thing", False),
                        ("Minerals are only found inside living things", False)],
            "explanation": r"Minerals are the building blocks; a rock is a solid made of one or more minerals packed together.",
        },
        {
            "text": r"The Mohs scale is used to measure a mineral's:",
            "difficulty": 2,
            "choices": [("Hardness (resistance to scratching)", True),
                        ("Weight", False), ("Temperature", False), ("Age", False)],
            "explanation": r"The Mohs scale ranks hardness from 1 (talc) to 10 (diamond). A mineral can scratch any mineral with a lower number.",
        },
        {
            "text": r"Quartz has a Mohs hardness of 7 and a steel knife is about 5.5. What happens when quartz is rubbed hard against the knife?",
            "difficulty": 2,
            "choices": [("Quartz scratches the steel knife", True),
                        ("The knife scratches the quartz", False),
                        ("Nothing can happen between them", False),
                        ("Both instantly shatter", False)],
            "explanation": r"A harder mineral scratches a softer material. Quartz (7) is harder than steel (~5.5), so quartz scratches the knife.",
        },
        {
            "text": r"Why do geologists consider a mineral's COLOR an unreliable way to identify it?",
            "difficulty": 2,
            "choices": [("The same mineral can come in many colors, and different minerals can share a color", True),
                        ("Color is impossible to see on minerals", False),
                        ("All minerals are exactly the same color", False),
                        ("Color changes the mineral's chemical formula", False)],
            "explanation": r"Color varies within a mineral (quartz alone has many colors) and overlaps between minerals, so tests like streak and hardness are more reliable.",
        },
        {
            "text": ("Use the Mohs hardness scale.\n\n"
                     "[[figure:mohs_hardness|The Mohs scale from talc (1) to diamond (10)]]\n\n"
                     "Which mineral can scratch apatite (5) but is itself scratched by quartz (7)?"),
            "difficulty": 3,
            "choices": [("Feldspar (6)", True), ("Gypsum (2)", False),
                        ("Calcite (3)", False), ("Topaz (8)", False)],
            "explanation": r"A mineral scratches anything softer and is scratched by anything harder. Feldspar (6) is harder than apatite (5) but softer than quartz (7). Topaz (8) would scratch quartz, not the reverse.",
        },
        # --- Lesson 2: igneous ---
        {
            "text": r"Igneous rock forms when:",
            "difficulty": 1,
            "choices": [("Molten rock (magma or lava) cools and hardens", True),
                        ("Layers of sediment are pressed together", False),
                        ("Heat and pressure change a solid rock", False),
                        ("Water evaporates from a lake", False)],
            "explanation": r"Igneous rock forms by the cooling and hardening of molten rock. ('Igneous' comes from the Latin for fire.)",
        },
        {
            "text": r"What is the difference between magma and lava?",
            "difficulty": 2,
            "choices": [("Magma is molten rock below the surface; lava is molten rock on the surface", True),
                        ("Magma is solid; lava is liquid", False),
                        ("They are two words for the same thing", False),
                        ("Magma is cold; lava is hot", False)],
            "explanation": r"Both are molten rock. The difference is location: magma is underground; once it erupts onto the surface, it is called lava.",
        },
        {
            "text": r"An igneous rock has large crystals you can see with the naked eye. This tells you it most likely:",
            "difficulty": 2,
            "choices": [("Cooled slowly, deep underground (intrusive)", True),
                        ("Cooled very quickly at the surface", False),
                        ("Was made of layers of sediment", False),
                        ("Formed without any cooling at all", False)],
            "explanation": r"Slow cooling underground gives crystals time to grow large (intrusive rock, like granite). Fast surface cooling makes tiny crystals.",
        },
        {
            "text": r"Obsidian is a smooth volcanic glass with no crystals at all. The best explanation is that the lava:",
            "difficulty": 3,
            "choices": [("Cooled so fast that crystals had no time to form", True),
                        ("Cooled extremely slowly over millions of years", False),
                        ("Was actually made of compacted sediment", False),
                        ("Was changed by heat and pressure without melting", False)],
            "explanation": r"Crystals need time to grow. When lava cools almost instantly, no crystals form and the result is volcanic glass like obsidian.",
        },
        {
            "text": ("Use the igneous textures diagram.\n\n"
                     "[[figure:igneous_textures|Intrusive vs. extrusive igneous rock]]\n\n"
                     "According to the diagram, why does the intrusive rock have larger crystals than the extrusive rock?"),
            "difficulty": 2,
            "choices": [("It cooled more slowly, giving crystals time to grow", True),
                        ("It is much older than the extrusive rock", False),
                        ("It contains fossils that grew into crystals", False),
                        ("It was squeezed by pressure into bands", False)],
            "explanation": r"The diagram links slow, deep cooling to large crystals and fast, surface cooling to tiny ones. Pro tip: crystal size is about cooling speed, not age.",
        },
        # --- Lesson 3: sedimentary ---
        {
            "text": r"Sedimentary rock forms when:",
            "difficulty": 1,
            "choices": [("Layers of sediment are compacted and cemented together", True),
                        ("Magma cools deep underground", False),
                        ("A rock melts completely and re-forms", False),
                        ("Heat and pressure bend a solid rock", False)],
            "explanation": r"Sediment settles in layers, then is pressed (compacted) and glued (cemented) into solid sedimentary rock.",
        },
        {
            "text": r"Which is the correct ORDER of steps that form sedimentary rock?",
            "difficulty": 2,
            "choices": [("Weathering, erosion, deposition, compaction & cementation", True),
                        ("Compaction, deposition, erosion, weathering", False),
                        ("Melting, cooling, weathering, deposition", False),
                        ("Deposition, weathering, melting, cementation", False)],
            "explanation": r"Rock is first broken into sediment (weathering), carried away (erosion), dropped in layers (deposition), then pressed and glued (compaction & cementation).",
        },
        {
            "text": r"Which type of rock is most likely to contain fossils, and why?",
            "difficulty": 2,
            "choices": [("Sedimentary, because remains get buried gently in layers", True),
                        ("Igneous, because magma preserves bones", False),
                        ("Metamorphic, because pressure protects fossils", False),
                        ("All rock types preserve fossils equally well", False)],
            "explanation": r"Sediment can bury remains gently and harden around them, preserving fossils. The intense heat that forms igneous and metamorphic rock usually destroys them.",
        },
        {
            "text": r"In a stack of undisturbed sedimentary layers, the oldest layer is found at the bottom. This principle is the law of:",
            "difficulty": 2,
            "choices": [("Superposition", True), ("Gravity", False),
                        ("Conservation", False), ("Reflection", False)],
            "explanation": r"By the law of superposition, in undisturbed layers each layer is younger than the one beneath it, so the bottom layer is oldest.",
        },
        {
            "text": ("Use the sedimentary layers diagram.\n\n"
                     "[[figure:sedimentary_layers|Layers of sedimentary rock]]\n\n"
                     "Based on the diagram, which layer is the OLDEST?"),
            "difficulty": 1,
            "choices": [("The bottom layer", True), ("The top layer", False),
                        ("The middle layer", False), ("They are all the same age", False)],
            "explanation": r"Layers build up over time, so the bottom layer was deposited first and is oldest (superposition). Pro tip: bottom = oldest, top = youngest.",
        },
        {
            "text": r"Coal forms from the buried, compressed remains of ancient plants. This makes coal an example of a(n) ______ sedimentary rock.",
            "difficulty": 3,
            "choices": [("Organic", True), ("Igneous", False),
                        ("Metamorphic", False), ("Chemical (evaporite)", False)],
            "explanation": r"Organic sedimentary rocks form from the remains of living things — coal from plants, and much limestone from shells. (Chemical/evaporite rocks form when water evaporates.)",
        },
        # --- Lesson 4: metamorphic ---
        {
            "text": r"Metamorphic rock forms when an existing rock is changed by:",
            "difficulty": 1,
            "choices": [("Heat and pressure, without melting", True),
                        ("Cooling from magma", False),
                        ("Settling into layers of sediment", False),
                        ("Evaporation of seawater", False)],
            "explanation": r"Metamorphic rock forms in the solid state when heat and pressure rearrange a rock's minerals. If it melted, it would become magma instead.",
        },
        {
            "text": r"Marble forms from limestone under heat and pressure. In this change, limestone is the:",
            "difficulty": 2,
            "choices": [("Parent rock", True), ("Magma", False),
                        ("Sediment", False), ("Fossil", False)],
            "explanation": r"The original rock that gets metamorphosed is called the parent rock. Limestone is the parent rock of marble.",
        },
        {
            "text": r"The banded, layered look in metamorphic rocks like gneiss, caused by minerals lining up under pressure, is called:",
            "difficulty": 2,
            "choices": [("Foliation", True), ("Cementation", False),
                        ("Erosion", False), ("Crystallization", False)],
            "explanation": r"Foliation is the alignment of minerals into bands under directed pressure. Foliated rocks include slate, schist, and gneiss; marble and quartzite are non-foliated.",
        },
        {
            "text": r"Which is a correct parent-rock to metamorphic-rock pairing?",
            "difficulty": 2,
            "choices": [("Shale changes into slate", True),
                        ("Limestone changes into granite", False),
                        ("Sandstone changes into magma", False),
                        ("Marble changes into shale", False)],
            "explanation": r"Shale (a sedimentary rock) metamorphoses into slate, then schist, then gneiss with increasing heat and pressure. (Limestone changes into marble; sandstone into quartzite.)",
        },
        {
            "text": r"If a metamorphic rock were heated until it MELTED, what would it become next in the rock cycle?",
            "difficulty": 3,
            "choices": [("Magma, which can then cool into igneous rock", True),
                        ("Sedimentary rock immediately", False),
                        ("A mineral with no rock type", False),
                        ("Another metamorphic rock", False)],
            "explanation": r"Melting any rock makes magma; when that magma cools and hardens, it becomes igneous rock. (Metamorphism itself stops short of melting.)",
        },
        {
            "text": ("Use the metamorphism diagram.\n\n"
                     "[[figure:metamorphic_change|A parent rock changed into a foliated metamorphic rock]]\n\n"
                     "In the diagram, what causes the parent rock's minerals to line up into bands?"),
            "difficulty": 2,
            "choices": [("Heat and pressure, while the rock stays solid", True),
                        ("Complete melting of the rock", False),
                        ("Settling into layers underwater", False),
                        ("Rapid cooling at the surface", False)],
            "explanation": r"The diagram shows heat and pressure realigning the minerals into bands (foliation) without melting. Pro tip: metamorphism changes rock in the solid state.",
        },
        # --- Lesson 5: the rock cycle ---
        {
            "text": r"The rock cycle describes how:",
            "difficulty": 1,
            "choices": [("Any rock type can change into another over time", True),
                        ("Rocks stay exactly the same forever", False),
                        ("Only sedimentary rock can change", False),
                        ("Rocks turn into living things", False)],
            "explanation": r"The rock cycle is the ongoing set of processes by which any rock can be transformed into any other type over long periods of time.",
        },
        {
            "text": r"In the rock cycle, which process turns ANY rock into magma?",
            "difficulty": 2,
            "choices": [("Melting", True), ("Weathering", False),
                        ("Cementation", False), ("Deposition", False)],
            "explanation": r"Melting (from intense heat deep in the Earth) turns any rock into magma, which can later cool into igneous rock.",
        },
        {
            "text": r"Weathering and erosion break a rock into small pieces of sediment. Those pieces can eventually form which rock type?",
            "difficulty": 2,
            "choices": [("Sedimentary", True), ("Igneous", False),
                        ("Magma", False), ("A mineral only", False)],
            "explanation": r"Sediment that is deposited, compacted, and cemented becomes sedimentary rock.",
        },
        {
            "text": r"Which statement about the rock cycle is TRUE?",
            "difficulty": 3,
            "choices": [("It has no fixed starting point, and rocks can follow many different paths", True),
                        ("It always goes igneous, then sedimentary, then metamorphic, in that order", False),
                        ("A rock can only change type once", False),
                        ("Once a rock is metamorphic, it can never change again", False)],
            "explanation": r"The rock cycle is not a one-way sequence. Rocks can melt, weather, or be heated and squeezed in many orders, looping endlessly over geologic time.",
        },
        {
            "text": ("Use the rock cycle diagram.\n\n"
                     "[[figure:rock_cycle_detailed|The rock cycle linking magma and the three rock families]]\n\n"
                     "According to the diagram, magma becomes igneous rock by:"),
            "difficulty": 2,
            "choices": [("Cooling and crystallizing", True),
                        ("Weathering and erosion", False),
                        ("Heat and pressure", False),
                        ("Compaction and cementation", False)],
            "explanation": r"The diagram labels the magma-to-igneous arrow as cooling and crystallizing. Pro tip: each arrow in the cycle is a specific process.",
        },
        # --- Lesson 6: identifying & reading rocks ---
        {
            "text": r"A geologist finds a rock made of large interlocking crystals, with no layers or bands. It is most likely:",
            "difficulty": 2,
            "choices": [("Igneous (intrusive)", True), ("Sedimentary", False),
                        ("Metamorphic", False), ("A single mineral, not a rock", False)],
            "explanation": r"Interlocking crystals and no layering point to igneous rock; large crystals mean it cooled slowly underground (intrusive).",
        },
        {
            "text": ("A field guide gives this key:\n"
                     "- interlocking crystals -> igneous\n"
                     "- flat layers or grains -> sedimentary\n"
                     "- bands of aligned minerals -> metamorphic\n\n"
                     "A sample shows clear bands of aligned minerals. Using the key, it is:"),
            "difficulty": 3,
            "choices": [("Metamorphic", True), ("Igneous", False),
                        ("Sedimentary", False), ("Impossible to classify", False)],
            "explanation": r"The key matches bands of aligned minerals (foliation) to metamorphic rock. Use only the clue the data gives. Pro tip: crystals = igneous, layers = sedimentary, bands = metamorphic.",
        },
    ],
    "essays": [
        {
            "text": (
                "A single piece of rock can, over millions of years, exist as an igneous rock, later as a "
                "sedimentary rock, and later still as a metamorphic rock. Using the rock cycle, describe one "
                "path the material could take through all three types. Name the process that drives each change, "
                "and explain why we say the rock cycle has no fixed starting point."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) a valid path, e.g., magma cools and crystallizes into igneous rock; "
                "(2) weathering, erosion, deposition, and compaction/cementation turn it into sedimentary rock; "
                "(3) heat and pressure turn it into metamorphic rock (and optionally melting returns it to magma); "
                "(4) correctly naming the driving process for each step; (5) explaining that any rock can melt, "
                "weather, or be heated/squeezed in any order, so there is no fixed start. Deduct for treating the "
                "cycle as a one-way sequence."
            ),
        },
        {
            "text": (
                "Compare the three rock families -- igneous, sedimentary, and metamorphic. For each, explain how it "
                "forms and give one feature you could use to identify it. Then explain why fossils are found almost "
                "entirely in sedimentary rock."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) igneous -- forms when molten rock cools and hardens; identify by interlocking "
                "crystals (large = slow/intrusive, small = fast/extrusive); (2) sedimentary -- forms when sediment is "
                "compacted and cemented in layers; identify by flat layers/grains (and fossils); (3) metamorphic -- "
                "forms when heat and pressure change a rock in the solid state; identify by bands/foliation or a "
                "recrystallized look; (4) fossils survive in sedimentary rock because sediment buries remains gently, "
                "while the heat that makes igneous and metamorphic rock destroys them. Deduct for mixing up how the "
                "types form."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: The Rock Cycle & Minerals (Deep Dive)' course."

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
