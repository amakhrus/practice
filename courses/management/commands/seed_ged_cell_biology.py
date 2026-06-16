"""
Seed data: 'GED Science: The Cell -- Structure & Function (Deep Dive)'.

A focused EXPANSION of Lesson 1 ("The Cell: Life's Basic Unit") from the broader
'GED Science: Life Science' course. The parent course gives a one-lesson overview;
this course goes deeper:

  1. What a cell is -- the cell theory and how cells were discovered.
  2. Prokaryotic vs. eukaryotic cells (and why cells stay small).
  3. The organelles and what each one does.
  4. Plant cells vs. animal cells.
  5. The cell membrane and how things move in and out (transport, osmosis).
  6. Cell division (the cell cycle and mitosis) and reading cell data.

This course uses ALL-NEW diagrams (a discovery timeline, prokaryote vs. eukaryote,
a detailed organelle map, plant vs. animal cells, membrane transport, and the cell
cycle) rather than reusing the parent course's 'cell_animal' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Biology* and *Concepts of Biology* (cell structure, transport).
  - Campbell & Reece, *Biology* (standard reference for organelles, the cell cycle).
  - National Human Genome Research Institute / NIH (cell biology basics).
  - Cell theory history: Hooke (1665), Leeuwenhoek (1670s), Schleiden & Schwann
    (1838-39), Virchow (1855, "omnis cellula e cellula").
Note: prokaryotes are typically ~1-10 micrometers; eukaryotic cells ~10-100
micrometers. Cells stay small because volume grows faster than surface area
(surface-area-to-volume ratio).

Run:
    python manage.py seed_ged_cell_biology
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: The Cell -- Structure & Function (Deep Dive)",
    "slug": "ged-cell-biology",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the cell, expanding the single 'The Cell' lesson from the GED Life Science "
        "course into a full mini-course. You'll learn the cell theory and how cells were discovered, "
        "the difference between bacteria-style (prokaryotic) and plant/animal-style (eukaryotic) cells, "
        "what each organelle does, how plant and animal cells differ, how the cell membrane controls "
        "what moves in and out, and how cells divide. Plain language, all-new labeled diagrams, "
        "common-misconception warnings, and GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. What Is a Cell? Cell Theory & Discovery",
            r"Every living thing — a single bacterium, a blade of grass, you — is built from **cells**. The cell is the smallest unit that is truly **alive**. This big idea is summed up by the **cell theory**, which has three parts:" "\n\n"
            r"- **All living things are made of one or more cells.**" "\n"
            r"- **The cell is the basic unit of structure and function** in living things." "\n"
            r"- **All cells come from existing cells** (cells don't appear from nothing)." "\n\n"
            r"[[figure:cell_discovery_timeline|Cell theory came together over 200 years as microscopes improved and scientists shared observations.]]" "\n\n"
            r"This understanding depended on the **microscope**. In **1665** Robert **Hooke** looked at a thin slice of cork and named the little boxes he saw '**cells**.' Soon after, Antonie van **Leeuwenhoek** used better lenses to see actual **living** microbes. In **1838–39**, **Schleiden** and **Schwann** concluded that all plants and animals are made of cells, and in **1855** **Virchow** added that every cell comes from another cell." "\n\n"
            r"Cells are usually **tiny** — most can only be seen with a microscope — which is exactly why they went unnoticed for so long." "\n\n"
            r"⚠️ Common misconception: Hooke did **not** see living cells. He saw the empty **walls** of dead cork cells. It took stronger microscopes (Leeuwenhoek) to reveal living cells." "\n\n"
            r"💡 Tip: memorize the three parts of cell theory — **made of cells, basic unit of life, cells from cells.**",
        ),
        (
            "2. Two Kinds of Cell: Prokaryotic vs. Eukaryotic",
            r"All cells fall into two broad designs, and the dividing line is one structure: the **nucleus**." "\n\n"
            r"[[figure:prokaryote_eukaryote|A prokaryotic cell has no nucleus; a eukaryotic cell keeps its DNA in a nucleus and has many organelles.]]" "\n\n"
            r"- **Prokaryotic** cells (**bacteria** and archaea) have **no nucleus**. Their DNA floats freely in the cytoplasm as a loop. They have **no membrane-bound organelles** and are **small** (about 1–10 micrometers)." "\n"
            r"- **Eukaryotic** cells (**plants, animals, fungi, protists**) keep their DNA inside a **nucleus** and contain many specialized, membrane-bound **organelles**. They are **larger** (about 10–100 micrometers)." "\n\n"
            r"**Why do cells stay so small?** It comes down to the **surface-area-to-volume ratio**. As a cell grows, its **volume** (the inside that needs feeding) grows **faster** than its **surface area** (the membrane that brings in food and removes waste). Past a certain size the membrane can't keep up — so cells stay small or divide." "\n\n"
            r"⚠️ Common misconception: prokaryotes are not 'primitive' or 'simple animals.' They are a distinct, hugely successful kind of life — just built without a nucleus." "\n\n"
            r"💡 Tip: **pro**karyote = 'before the nucleus' (none); **eu**karyote = 'true nucleus.' Pro = small & simple-looking; Eu = bigger with organelles.",
        ),
        (
            "3. Organelles: The Cell's Working Parts",
            r"A eukaryotic cell works like a tiny **factory**, with each **organelle** ('little organ') doing a specific job. Here are the ones the GED test cares about most." "\n\n"
            r"[[figure:eukaryotic_cell_detailed|Each organelle has a role — control, energy, manufacturing, packaging, and recycling.]]" "\n\n"
            r"- **Nucleus** — the **control center**; holds the cell's **DNA** (instructions). The **nucleolus** inside it builds ribosomes." "\n"
            r"- **Mitochondria** — the **powerhouse**; carry out cellular respiration to release energy (**ATP**) from food." "\n"
            r"- **Ribosomes** — tiny machines that **build proteins** (found free in the cytoplasm or on the rough ER)." "\n"
            r"- **Rough endoplasmic reticulum (ER)** — studded with ribosomes; makes and transports **proteins**." "\n"
            r"- **Smooth ER** — makes **lipids** (fats) and helps detoxify." "\n"
            r"- **Golgi apparatus** — the **packaging & shipping** center; finishes and sends out proteins." "\n"
            r"- **Lysosomes** — the **recycling/clean-up** crew; break down waste and worn-out parts." "\n"
            r"- **Cytoplasm** — the jelly-like fluid where organelles sit and reactions happen." "\n\n"
            r"⚠️ Common misconception: **ribosomes are not membrane-bound organelles** — they are tiny structures (the smallest), and they make proteins whether floating free or attached to the rough ER." "\n\n"
            r"💡 Tip: tie each part to a factory job — **nucleus = boss, mitochondria = power plant, ribosomes = assembly line, Golgi = shipping, lysosome = recycling.**",
        ),
        (
            "4. Plant Cells vs. Animal Cells",
            r"Plant and animal cells are **both eukaryotic** and share most organelles — nucleus, mitochondria, ribosomes, ER, Golgi, and a cell membrane. But plant cells have a few important **extras**." "\n\n"
            r"[[figure:plant_vs_animal_cell|Plant cells add a rigid cell wall, chloroplasts for photosynthesis, and a large central vacuole.]]" "\n\n"
            r"Plant cells have three structures animal cells lack:" "\n"
            r"- **Cell wall** — a rigid outer layer (made of cellulose) **outside** the cell membrane that gives the cell its shape and support. It's why plant cells look boxy." "\n"
            r"- **Chloroplasts** — green organelles that capture sunlight to make food by **photosynthesis**." "\n"
            r"- **A large central vacuole** — a big sac that stores water and keeps the cell firm (turgor pressure)." "\n\n"
            r"Animal cells, by contrast, are usually **rounder**, have only a **membrane** (no wall), and rely on getting their food rather than making it." "\n\n"
            r"⚠️ Common misconception: a plant cell does **not** replace its membrane with a wall. It has **both** — the cell wall sits **outside** the cell membrane, not instead of it." "\n\n"
            r"💡 Tip: plant-only extras spell **'W-C-V': Wall, Chloroplasts, big Vacuole.**",
        ),
        (
            "5. The Cell Membrane & Transport",
            r"Every cell is wrapped in a **cell membrane** — a double layer of fat molecules (a **phospholipid bilayer**) dotted with proteins. Its key property is **selective permeability**: it controls what gets in and out, letting some things pass while blocking others." "\n\n"
            r"[[figure:membrane_transport|Passive transport moves materials down their gradient for free; active transport pumps them against the gradient using ATP.]]" "\n\n"
            r"There are two main ways materials cross:" "\n"
            r"- **Passive transport** — needs **no energy**; molecules move from **high to low** concentration (down the gradient)." "\n"
            r"  - **Diffusion** — molecules spread out from where they're crowded to where they're not." "\n"
            r"  - **Osmosis** — the diffusion of **water** across the membrane." "\n"
            r"  - **Facilitated diffusion** — passage through a helper **protein**, still down the gradient." "\n"
            r"- **Active transport** — needs **energy (ATP)** to move materials from **low to high** concentration (against the gradient), using protein pumps." "\n\n"
            r"Water balance matters: a cell in a **hypotonic** solution (more water outside) **swells** as water moves in; in a **hypertonic** solution (more solute outside) it **shrinks**; in an **isotonic** solution it stays balanced." "\n\n"
            r"⚠️ Common misconception: in **osmosis**, water moves toward the side with **more dissolved solute** (less water) — not the other way around. It's trying to even out the concentrations." "\n\n"
            r"💡 Tip: **passive = downhill, no ATP; active = uphill, needs ATP.** Osmosis is just diffusion of water.",
        ),
        (
            "6. Cell Division & Reading Cell Data",
            r"Cells don't last forever, and organisms need to grow — so cells **divide**. They divide to **grow**, to **repair** damage (like healing a cut), and, in single-celled organisms, to **reproduce**." "\n\n"
            r"[[figure:cell_cycle|A cell spends most of its life in interphase, then divides by mitosis into two identical cells.]]" "\n\n"
            r"The **cell cycle** has two main parts:" "\n"
            r"- **Interphase** — the longest part. The cell **grows**, does its normal jobs, and **copies its DNA** so each new cell will get a full set." "\n"
            r"- **Mitosis** (then **cytokinesis**) — the nucleus divides and the cell splits into **two daughter cells** that are **genetically identical** to the original." "\n\n"
            r"Mitosis is for growth and repair. (A different process, **meiosis**, makes sex cells — eggs and sperm — that are **not** identical; don't confuse the two.)" "\n\n"
            r"**Reading cell data (a GED skill).** Biology questions often show a graph or table — cell counts over time, sizes under a microscope, or rates of a process. Read the **title, axes, and units** first, find the **trend**, and use only what the data shows. Remember **correlation is not causation** — two things changing together doesn't prove one causes the other." "\n\n"
            r"⚠️ Common misconception: mitosis does **not** make cells that are different from the parent. Its two daughter cells are **identical copies**; it's meiosis (for reproduction) that shuffles the genes." "\n\n"
            r"💡 Tip: **interphase = grow + copy DNA; mitosis = split into two identical cells** for growth and repair." "\n\n"
            r"📚 Sources: OpenStax *Biology* / *Concepts of Biology*; Campbell & Reece, *Biology*; NIH / National Human Genome Research Institute.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: cell theory & discovery ---
        {
            "text": r"According to the cell theory, where do all new cells come from?",
            "difficulty": 1,
            "choices": [("From other, already-existing cells", True),
                        ("They appear from non-living matter", False),
                        ("They are made in the nucleus from scratch", False),
                        ("They form only inside the brain", False)],
            "explanation": r"One part of the cell theory (from Virchow) is that all cells come from pre-existing cells — cells don't arise from nothing.",
        },
        {
            "text": r"What is the basic unit of structure and function in all living things?",
            "difficulty": 1,
            "choices": [("The cell", True), ("The atom", False),
                        ("The organ", False), ("The molecule", False)],
            "explanation": r"The cell is the smallest unit that is alive and the basic building block of every living thing — a central idea of the cell theory.",
        },
        {
            "text": r"In 1665 Robert Hooke looked at cork and named the boxes he saw 'cells.' What was he actually looking at?",
            "difficulty": 2,
            "choices": [("The empty walls of dead cork cells", True),
                        ("Living, swimming microbes", False),
                        ("The nucleus of a plant cell", False),
                        ("Tiny animals inside the cork", False)],
            "explanation": r"Hooke saw the box-like walls left behind by dead cork cells. Living cells weren't observed until Leeuwenhoek used stronger lenses.",
        },
        {
            "text": r"Which invention made the discovery of cells possible?",
            "difficulty": 1,
            "choices": [("The microscope", True), ("The telescope", False),
                        ("The thermometer", False), ("The X-ray machine", False)],
            "explanation": r"Cells are too small to see with the naked eye, so the microscope was essential to discovering and studying them.",
        },
        {
            "text": ("Use the discovery timeline.\n\n"
                     "[[figure:cell_discovery_timeline|Key discoveries leading to the cell theory]]\n\n"
                     "According to the timeline, who concluded that all cells come from existing cells?"),
            "difficulty": 2,
            "choices": [("Virchow (1855)", True), ("Hooke (1665)", False),
                        ("Leeuwenhoek (1670s)", False), ("Schleiden (1838)", False)],
            "explanation": r"The timeline places Virchow in 1855 with the idea that cells come from pre-existing cells. Pro tip: Hooke named cells; Virchow explained where they come from.",
        },
        # --- Lesson 2: prokaryote vs eukaryote ---
        {
            "text": r"What is the main difference between a prokaryotic cell and a eukaryotic cell?",
            "difficulty": 1,
            "choices": [("Eukaryotic cells have a nucleus; prokaryotic cells do not", True),
                        ("Prokaryotic cells are always larger", False),
                        ("Only eukaryotic cells contain DNA", False),
                        ("Prokaryotic cells have more organelles", False)],
            "explanation": r"The defining difference is the nucleus: eukaryotes keep their DNA inside a nucleus, while prokaryotes (like bacteria) have none. Both contain DNA.",
        },
        {
            "text": r"Bacteria are an example of which kind of cell?",
            "difficulty": 1,
            "choices": [("Prokaryotic", True), ("Eukaryotic", False),
                        ("Plant", False), ("Animal", False)],
            "explanation": r"Bacteria are prokaryotes — small cells with no nucleus and no membrane-bound organelles.",
        },
        {
            "text": r"Where is the DNA located in a prokaryotic cell?",
            "difficulty": 2,
            "choices": [("Floating freely in the cytoplasm (no nucleus)", True),
                        ("Inside a nucleus", False),
                        ("Inside the mitochondria", False),
                        ("On the outside of the cell wall", False)],
            "explanation": r"Prokaryotes have no nucleus, so their DNA sits as a loop in the cytoplasm. Eukaryotes enclose their DNA in a nucleus.",
        },
        {
            "text": r"As a cell grows larger, why does it eventually have to divide or stay small?",
            "difficulty": 3,
            "choices": [("Its volume grows faster than its surface area, so the membrane can't supply it fast enough", True),
                        ("Large cells run out of DNA", False),
                        ("The nucleus gets too heavy", False),
                        ("Big cells cannot contain water", False)],
            "explanation": r"This is the surface-area-to-volume problem: a bigger cell has much more inside to feed but proportionally less membrane to bring in food and remove waste, so cells stay small or divide.",
        },
        {
            "text": ("Use the cell comparison diagram.\n\n"
                     "[[figure:prokaryote_eukaryote|A prokaryotic cell next to a eukaryotic cell]]\n\n"
                     "Which structure is shown in the eukaryotic cell but NOT in the prokaryotic cell?"),
            "difficulty": 2,
            "choices": [("A nucleus", True), ("DNA", False),
                        ("A cell membrane", False), ("Cytoplasm", False)],
            "explanation": r"The diagram shows the eukaryote with a nucleus around its DNA, while the prokaryote's DNA floats free. Both have DNA, a membrane, and cytoplasm. Pro tip: nucleus = eukaryote.",
        },
        # --- Lesson 3: organelles ---
        {
            "text": r"Which organelle is the control center of the cell and holds its DNA?",
            "difficulty": 1,
            "choices": [("The nucleus", True), ("The mitochondrion", False),
                        ("The ribosome", False), ("The Golgi apparatus", False)],
            "explanation": r"The nucleus stores the cell's DNA and directs its activities — the control center.",
        },
        {
            "text": r"Which organelle is known as the 'powerhouse' because it releases energy (ATP) from food?",
            "difficulty": 1,
            "choices": [("The mitochondrion", True), ("The nucleus", False),
                        ("The lysosome", False), ("The cell wall", False)],
            "explanation": r"Mitochondria carry out cellular respiration, releasing usable energy (ATP) from glucose.",
        },
        {
            "text": r"Which structures build proteins for the cell?",
            "difficulty": 2,
            "choices": [("Ribosomes", True), ("Lysosomes", False),
                        ("Vacuoles", False), ("Chloroplasts", False)],
            "explanation": r"Ribosomes assemble proteins, either floating free in the cytoplasm or attached to the rough ER.",
        },
        {
            "text": r"Which organelle packages and ships proteins, much like a post office?",
            "difficulty": 2,
            "choices": [("The Golgi apparatus", True), ("The nucleus", False),
                        ("The mitochondrion", False), ("The ribosome", False)],
            "explanation": r"The Golgi apparatus finishes, packages, and ships proteins to where they are needed.",
        },
        {
            "text": r"Which organelle breaks down waste and worn-out cell parts (the cell's clean-up crew)?",
            "difficulty": 2,
            "choices": [("The lysosome", True), ("The nucleus", False),
                        ("The chloroplast", False), ("The ribosome", False)],
            "explanation": r"Lysosomes contain enzymes that digest waste, debris, and worn-out organelles — recycling materials for the cell.",
        },
        {
            "text": ("Use the cell diagram.\n\n"
                     "[[figure:eukaryotic_cell_detailed|A detailed animal cell]]\n\n"
                     "In the diagram, the rough endoplasmic reticulum (ER) is covered with which structures?"),
            "difficulty": 2,
            "choices": [("Ribosomes", True), ("Mitochondria", False),
                        ("Chloroplasts", False), ("Vacuoles", False)],
            "explanation": r"The rough ER is 'rough' because it is studded with ribosomes, which is why it specializes in making proteins. Pro tip: rough ER = ribosomes + protein-making.",
        },
        # --- Lesson 4: plant vs animal ---
        {
            "text": r"Which structures are found in plant cells but NOT in animal cells?",
            "difficulty": 1,
            "choices": [("Cell wall and chloroplasts", True),
                        ("Nucleus and ribosomes", False),
                        ("Mitochondria and cytoplasm", False),
                        ("Cell membrane and nucleus", False)],
            "explanation": r"Plant cells add a cell wall (support), chloroplasts (photosynthesis), and a large central vacuole. Both cell types share the nucleus, ribosomes, mitochondria, cytoplasm, and membrane.",
        },
        {
            "text": r"The rigid outer layer that gives a plant cell its shape and support is the:",
            "difficulty": 2,
            "choices": [("Cell wall", True), ("Cell membrane", False),
                        ("Nucleus", False), ("Vacuole", False)],
            "explanation": r"The cell wall, made of cellulose, is a stiff layer outside the membrane that supports and shapes the plant cell.",
        },
        {
            "text": r"Chloroplasts give plant cells the ability to:",
            "difficulty": 2,
            "choices": [("Make their own food by photosynthesis", True),
                        ("Break down waste", False),
                        ("Store DNA", False),
                        ("Pump out water", False)],
            "explanation": r"Chloroplasts capture sunlight and use it to make sugar (photosynthesis), so plants can produce their own food.",
        },
        {
            "text": r"Does a plant cell have a cell membrane?",
            "difficulty": 2,
            "choices": [("Yes — it has a membrane inside its cell wall", True),
                        ("No — the cell wall replaces the membrane", False),
                        ("No — only animal cells have membranes", False),
                        ("Only when it is dividing", False)],
            "explanation": r"Plant cells have both: the cell membrane lies just inside the rigid cell wall. The wall is an extra layer, not a replacement.",
        },
        {
            "text": ("Use the cell comparison diagram.\n\n"
                     "[[figure:plant_vs_animal_cell|An animal cell next to a plant cell]]\n\n"
                     "According to the diagram, the large central vacuole is a feature of the:"),
            "difficulty": 1,
            "choices": [("Plant cell", True), ("Animal cell", False),
                        ("Both equally", False), ("Neither", False)],
            "explanation": r"The diagram shows the large central vacuole in the plant cell, where it stores water and keeps the cell firm. Pro tip: plant extras = wall, chloroplasts, big vacuole.",
        },
        # --- Lesson 5: membrane & transport ---
        {
            "text": r"The cell membrane controls what enters and leaves the cell. This property is called:",
            "difficulty": 2,
            "choices": [("Selective permeability", True), ("Photosynthesis", False),
                        ("Mitosis", False), ("Respiration", False)],
            "explanation": r"Selective permeability means the membrane lets some substances through while blocking others, regulating the cell's contents.",
        },
        {
            "text": r"Movement of molecules from an area of high concentration to low concentration, without using energy, is called:",
            "difficulty": 2,
            "choices": [("Diffusion (passive transport)", True),
                        ("Active transport", False),
                        ("Mitosis", False),
                        ("Photosynthesis", False)],
            "explanation": r"Diffusion is passive transport: molecules spread from where they are crowded to where they are not, requiring no energy.",
        },
        {
            "text": r"Osmosis is the diffusion of which molecule across a membrane?",
            "difficulty": 2,
            "choices": [("Water", True), ("Oxygen", False),
                        ("Glucose", False), ("Protein", False)],
            "explanation": r"Osmosis is specifically the movement of water across a selectively permeable membrane, from where water is more concentrated to where it is less.",
        },
        {
            "text": r"Moving a substance against its concentration gradient (from low to high) requires:",
            "difficulty": 2,
            "choices": [("Energy (ATP) — active transport", True),
                        ("No energy at all", False),
                        ("Only sunlight", False),
                        ("A cell wall", False)],
            "explanation": r"Pushing materials 'uphill' against the gradient needs energy. Cells use ATP-powered pumps for this active transport.",
        },
        {
            "text": r"A cell is placed in pure water (a hypotonic solution). What happens?",
            "difficulty": 3,
            "choices": [("Water moves into the cell and it swells (it may burst)", True),
                        ("Water leaves and the cell shrinks", False),
                        ("Nothing — water never moves", False),
                        ("The cell instantly freezes", False)],
            "explanation": r"In a hypotonic solution there is more water outside, so water moves in by osmosis and the cell swells. (In a hypertonic solution it would shrink.)",
        },
        {
            "text": ("Use the membrane transport diagram.\n\n"
                     "[[figure:membrane_transport|Ways materials cross the cell membrane]]\n\n"
                     "According to the diagram, which process requires ATP (energy)?"),
            "difficulty": 2,
            "choices": [("Active transport (the pump moving low to high)", True),
                        ("Diffusion", False),
                        ("Facilitated diffusion", False),
                        ("Osmosis", False)],
            "explanation": r"The diagram marks active transport as the one needing ATP, because it moves material against the gradient. Diffusion, osmosis, and facilitated diffusion are passive. Pro tip: uphill = active = ATP.",
        },
        # --- Lesson 6: cell division & data ---
        {
            "text": r"What are the main reasons that cells divide?",
            "difficulty": 1,
            "choices": [("Growth and repair (and reproduction in single-celled organisms)", True),
                        ("To make the body colder", False),
                        ("To produce sunlight", False),
                        ("To remove all their DNA", False)],
            "explanation": r"Cell division lets organisms grow, replace damaged or dead cells, and (for single-celled life) reproduce.",
        },
        {
            "text": r"Mitosis produces two daughter cells that are:",
            "difficulty": 2,
            "choices": [("Genetically identical to the original cell", True),
                        ("Completely different from the original", False),
                        ("Half the size and missing DNA", False),
                        ("Always sex cells (eggs and sperm)", False)],
            "explanation": r"Mitosis makes two identical copies of the parent cell, which is what growth and repair require. Meiosis (a different process) makes non-identical sex cells.",
        },
        {
            "text": r"During which part of the cell cycle does the cell grow and copy its DNA, getting ready to divide?",
            "difficulty": 2,
            "choices": [("Interphase", True), ("Mitosis", False),
                        ("Cytokinesis", False), ("Osmosis", False)],
            "explanation": r"Interphase is the long preparation stage: the cell grows, carries out its work, and duplicates its DNA before mitosis splits it.",
        },
        {
            "text": ("Use the cell cycle diagram.\n\n"
                     "[[figure:cell_cycle|The phases of the cell cycle]]\n\n"
                     "According to the diagram, a cell spends MOST of its time in:"),
            "difficulty": 2,
            "choices": [("Interphase", True), ("Mitosis", False),
                        ("Cytokinesis", False), ("Division", False)],
            "explanation": r"The diagram shows interphase taking up most of the circle, while mitosis is a small slice. Pro tip: most of a cell's life is spent growing and preparing in interphase.",
        },
    ],
    "essays": [
        {
            "text": (
                "Compare prokaryotic and eukaryotic cells. In your answer, describe the key structural difference, "
                "give an example of each type, note the difference in size, and explain why cells generally stay "
                "small (use the idea of surface-area-to-volume)."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the key difference -- eukaryotes have a nucleus and membrane-bound organelles; "
                "prokaryotes have neither; (2) examples -- bacteria (prokaryotic) vs. plants/animals/fungi "
                "(eukaryotic); (3) prokaryotes are smaller than eukaryotes; (4) cells stay small because volume "
                "grows faster than surface area, so a too-large cell can't move enough materials across its membrane. "
                "Deduct for saying prokaryotes have no DNA or that they are 'simple animals.'"
            ),
        },
        {
            "text": (
                "Explain the difference between passive and active transport across the cell membrane. Give an "
                "example of each, explain what osmosis is, and describe what happens to a cell placed in a "
                "hypotonic solution versus a hypertonic solution."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) passive transport needs no energy and moves materials down the gradient "
                "(e.g., diffusion or osmosis); (2) active transport uses ATP to move materials against the gradient "
                "(e.g., a protein pump); (3) osmosis is the diffusion of water across the membrane; (4) in a "
                "hypotonic solution water enters and the cell swells (may burst), while in a hypertonic solution "
                "water leaves and the cell shrinks. Deduct for reversing the hypotonic/hypertonic effects or for "
                "saying active transport needs no energy."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: The Cell -- Structure & Function (Deep Dive)' course."

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
