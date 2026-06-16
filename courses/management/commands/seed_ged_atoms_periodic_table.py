"""
Seed data: 'GED Science: Atoms, Elements & the Periodic Table (Deep Dive)'.

A focused EXPANSION of Lesson 2 ("Atoms, Elements & the Periodic Table") from the
broader 'GED Science: Physical Science' course, brought up to the full deep-dive
standard (6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. Inside the atom (protons, neutrons, electrons).
  2. Atomic number, mass & reading an element box.
  3. Electron shells (the Bohr model).
  4. The periodic table: organization.
  5. Elements, compounds & molecules.
  6. Ions, isotopes & reading atomic data.

This course uses ALL-NEW diagrams (atom anatomy, an element box, Bohr models, a
periodic-table organization map, elements vs. compounds, and ions/isotopes)
rather than reusing the parent course's 'atom_structure' and 'periodic_table_guide'
figures.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Chemistry* and *Chemistry: Atoms First*; CK-12 Physical Science.
  - IUPAC Periodic Table of the Elements.
Note: protons (+) define the element (atomic number); a neutral atom has equal
protons and electrons; mass number = protons + neutrons. Ions form by gaining or
losing ELECTRONS (charge); isotopes differ in NEUTRONS (mass).

Run:
    python manage.py seed_ged_atoms_periodic_table
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Atoms, Elements & the Periodic Table (Deep Dive)",
    "slug": "ged-atoms-periodic-table",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the building blocks of matter, expanding the single 'Atoms, Elements & the "
        "Periodic Table' lesson from the GED Physical Science course into a full mini-course. You'll "
        "explore the structure of the atom, learn to read an element box and count protons, neutrons, "
        "and electrons, see how electrons fill shells, understand how the periodic table is organized, "
        "and tell elements from compounds and ions from isotopes. Plain language, all-new labeled "
        "diagrams, common-misconception warnings, and GED-style practice with full explanations."
    ),
    "lessons": [
        (
            "1. Inside the Atom",
            r"Everything is made of **atoms** — and atoms are made of three smaller particles. Knowing their charges and locations unlocks most chemistry questions." "\n\n"
            r"[[figure:atom_anatomy|Protons and neutrons sit in the nucleus; electrons move around it in shells.]]" "\n\n"
            r"The three subatomic particles are:" "\n"
            r"- **Protons** — **positive (+)** charge, found in the **nucleus** (center)." "\n"
            r"- **Neutrons** — **no charge (0)**, also in the **nucleus**." "\n"
            r"- **Electrons** — **negative (−)** charge, moving around the nucleus in **shells (energy levels)**." "\n\n"
            r"The **nucleus** holds nearly all of the atom's **mass** (protons and neutrons are heavy; electrons are almost massless). In a **neutral** atom, the number of **protons equals the number of electrons**, so the positive and negative charges balance." "\n\n"
            r"⚠️ Common misconception: an atom is mostly **empty space** — the tiny nucleus is surrounded by a relatively huge region where the light electrons move. (The neat circular orbits are a useful simplification, not a literal path.)" "\n\n"
            r"💡 Tip: **protons +, neutrons 0, electrons −.** Protons and neutrons are in the nucleus; electrons are outside it.",
        ),
        (
            "2. Atomic Number, Mass & Reading an Element Box",
            r"Each element has a box on the periodic table packed with information. Two numbers do most of the work." "\n\n"
            r"[[figure:atomic_number_mass|The atomic number gives the protons; the atomic mass is about protons plus neutrons.]]" "\n\n"
            r"- The **atomic number** is the number of **protons**. It **identifies the element** — every carbon atom has 6 protons, and anything with 6 protons is carbon." "\n"
            r"- The **mass number** is the number of **protons + neutrons** (the atomic mass on the table is close to this)." "\n\n"
            r"From those, you can count all three particles in a **neutral** atom:" "\n"
            r"- **Protons** = atomic number." "\n"
            r"- **Electrons** = protons (in a neutral atom)." "\n"
            r"- **Neutrons** = mass number − atomic number." "\n\n"
            r"For example, carbon (atomic number 6, mass ≈ 12) has **6 protons, 6 electrons, and 6 neutrons**." "\n\n"
            r"⚠️ Common misconception: the **atomic number** is the number of **protons**, not the mass and not the electrons. (Protons are what truly define the element.)" "\n\n"
            r"💡 Tip: **protons = atomic number; neutrons = mass − atomic number; electrons = protons (if neutral).**",
        ),
        (
            "3. Electron Shells (the Bohr Model)",
            r"Electrons aren't scattered randomly — they occupy **shells**, or **energy levels**, around the nucleus. The simple **Bohr model** pictures these as rings." "\n\n"
            r"[[figure:bohr_models|Electrons fill the inner shell first (up to 2), then the next shell (up to 8).]]" "\n\n"
            r"Shells fill from the inside out:" "\n"
            r"- The **first** shell holds up to **2** electrons." "\n"
            r"- The **second** shell holds up to **8**." "\n\n"
            r"So carbon's 6 electrons fill as **2 in the inner shell and 4 in the outer**; oxygen's 8 fill as **2 and 6**. The electrons in the **outermost** shell are called **valence electrons**, and they are the ones that determine how an atom **bonds and reacts**. Atoms 'want' a full outer shell, which drives most chemistry." "\n\n"
            r"⚠️ Common misconception: the shells do **not** all hold the same number. The first shell holds only **2**; later shells hold more." "\n\n"
            r"💡 Tip: fill the inner shell first (max 2), then the next (max 8). **Valence (outer) electrons drive chemistry.**",
        ),
        (
            "4. The Periodic Table: Organization",
            r"The **periodic table** isn't a random chart — it's a brilliant filing system. Elements are arranged in order of increasing **atomic number** (number of protons), and the layout groups elements with similar behavior together." "\n\n"
            r"[[figure:periodic_table_map|Rows are periods; columns are groups. Metals are on the left, nonmetals on the right, with metalloids between.]]" "\n\n"
            r"- The **rows** are called **periods**." "\n"
            r"- The **columns** are called **groups** (or families). Elements in the same group have **similar chemical properties** because they have the same number of **valence electrons**." "\n\n"
            r"The table also sorts elements by type: **metals** (most of the table, on the **left and center** — shiny, good conductors, bendable), **nonmetals** (upper **right**), and **metalloids** (along the 'staircase,' with in-between properties). Two famous groups: **Group 1 alkali metals** are very **reactive**, while **Group 18 noble gases** are very **unreactive** (their outer shells are full)." "\n\n"
            r"⚠️ Common misconception: the table is ordered by **atomic number** (protons), **not** by atomic mass and **not** alphabetically." "\n\n"
            r"💡 Tip: **rows = periods; columns = groups** (similar properties). Metals left, nonmetals right.",
        ),
        (
            "5. Elements, Compounds & Molecules",
            r"Atoms combine to make the huge variety of substances around us. Three words keep it straight." "\n\n"
            r"[[figure:element_vs_compound|An element is one kind of atom; a compound is different atoms chemically bonded in a fixed ratio.]]" "\n\n"
            r"- An **element** is a substance made of only **one kind of atom** (oxygen, gold, carbon). It can't be broken into simpler substances by chemical means." "\n"
            r"- A **compound** is two or more **different elements chemically bonded** in a **fixed ratio** — like water (**H₂O**) or table salt (**NaCl**). A compound has **new properties**, different from the elements in it." "\n"
            r"- A **molecule** is two or more atoms bonded together. It can be an element (**O₂**, two oxygen atoms) or a compound (**H₂O**)." "\n\n"
            r"A **chemical formula** shows the ratio of atoms: **H₂O** means 2 hydrogen atoms bonded to 1 oxygen atom." "\n\n"
            r"⚠️ Common misconception: a compound's properties are **not** just a mix of its elements. Hydrogen and oxygen are both **gases**, yet bonded as water they form a **liquid** you can drink." "\n\n"
            r"💡 Tip: **element = one kind of atom; compound = different atoms bonded in a fixed ratio** (with new properties).",
        ),
        (
            "6. Ions, Isotopes & Reading Atomic Data",
            r"Atoms can change in two ways without becoming a different element — and one way that **does** change the element. The key is knowing which particle changes." "\n\n"
            r"[[figure:ions_isotopes|Changing electrons makes an ion (a charge); changing neutrons makes an isotope (a different mass).]]" "\n\n"
            r"- An **ion** forms when an atom **gains or loses electrons**, giving it a **charge**. Lose an electron → a **positive** ion (cation); gain an electron → a **negative** ion (anion)." "\n"
            r"- An **isotope** is an atom of the **same element** (same number of protons) with a **different number of neutrons**, so it has a different **mass**. **Carbon-12** and **Carbon-14** both have 6 protons, but 6 vs. 8 neutrons." "\n"
            r"- Change the number of **protons**, and you have a **different element** entirely." "\n\n"
            r"**Reading atomic data (a GED skill).** A table might list protons, neutrons, electrons, charge, or mass. Use the rules: protons = atomic number, neutrons = mass − atomic number, and a charge tells you electrons were gained or lost." "\n\n"
            r"⚠️ Common misconception: don't confuse the three. **Electrons** change → **ion** (charge); **neutrons** change → **isotope** (mass); **protons** change → a **different element**." "\n\n"
            r"💡 Tip: **protons = identity; electrons = charge (ions); neutrons = mass (isotopes).**" "\n\n"
            r"📚 Sources: OpenStax *Chemistry* / *Chemistry: Atoms First*; CK-12 Physical Science; IUPAC Periodic Table.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: inside the atom ---
        {
            "text": r"What are the three main particles that make up an atom?",
            "difficulty": 1,
            "choices": [("Protons, neutrons, and electrons", True),
                        ("Solids, liquids, and gases", False),
                        ("Atoms, molecules, and compounds", False),
                        ("Acids, bases, and salts", False)],
            "explanation": r"Atoms are built from protons, neutrons, and electrons.",
        },
        {
            "text": r"Which particle has a POSITIVE charge?",
            "difficulty": 1,
            "choices": [("Proton", True), ("Electron", False),
                        ("Neutron", False), ("Photon", False)],
            "explanation": r"Protons are positive, electrons are negative, and neutrons have no charge.",
        },
        {
            "text": r"Which particle has a NEGATIVE charge?",
            "difficulty": 1,
            "choices": [("Electron", True), ("Proton", False),
                        ("Neutron", False), ("Nucleus", False)],
            "explanation": r"Electrons carry a negative charge and move around the nucleus.",
        },
        {
            "text": r"The nucleus of an atom contains:",
            "difficulty": 2,
            "choices": [("Protons and neutrons", True),
                        ("Electrons only", False),
                        ("Protons and electrons", False),
                        ("Neutrons and electrons", False)],
            "explanation": r"The nucleus holds the protons and neutrons (and most of the atom's mass). Electrons move outside it.",
        },
        {
            "text": r"In a neutral atom, the number of protons equals the number of:",
            "difficulty": 2,
            "choices": [("Electrons", True), ("Neutrons", False),
                        ("Molecules", False), ("Shells", False)],
            "explanation": r"A neutral atom has balanced charge, so its positive protons are matched by an equal number of negative electrons.",
        },
        {
            "text": ("Use the atom diagram.\n\n"
                     "[[figure:atom_anatomy|The parts of an atom]]\n\n"
                     "According to the diagram, the electrons are located:"),
            "difficulty": 2,
            "choices": [("Outside the nucleus, in shells", True),
                        ("Inside the nucleus", False),
                        ("In the center with the protons", False),
                        ("Nowhere in the atom", False)],
            "explanation": r"The diagram shows electrons in shells around the nucleus, while protons and neutrons sit inside it. Pro tip: nucleus = protons + neutrons; electrons orbit outside.",
        },
        # --- Lesson 2: atomic number & mass ---
        {
            "text": r"The atomic number of an element is equal to its number of:",
            "difficulty": 1,
            "choices": [("Protons", True), ("Neutrons", False),
                        ("Molecules", False), ("Electron shells", False)],
            "explanation": r"The atomic number equals the number of protons, which identifies the element.",
        },
        {
            "text": r"An atom has 8 protons and 8 neutrons. What is its mass number?",
            "difficulty": 2,
            "choices": [("16", True), ("8", False), ("0", False), ("64", False)],
            "explanation": r"Mass number = protons + neutrons = 8 + 8 = 16.",
        },
        {
            "text": r"Carbon has atomic number 6. How many electrons are in a NEUTRAL carbon atom?",
            "difficulty": 2,
            "choices": [("6", True), ("12", False), ("3", False), ("0", False)],
            "explanation": r"In a neutral atom, electrons equal protons, so neutral carbon has 6 electrons.",
        },
        {
            "text": r"An atom has a mass number of 23 and an atomic number of 11. How many neutrons does it have?",
            "difficulty": 2,
            "choices": [("12", True), ("11", False), ("23", False), ("34", False)],
            "explanation": r"Neutrons = mass number - atomic number = 23 - 11 = 12.",
        },
        {
            "text": ("Use the element box.\n\n"
                     "[[figure:atomic_number_mass|An element box for carbon]]\n\n"
                     "According to the box, the atomic number tells you the number of:"),
            "difficulty": 2,
            "choices": [("Protons", True), ("Neutrons", False),
                        ("Total atoms", False), ("Bonds", False)],
            "explanation": r"The atomic number is the proton count. For a neutral atom, that also equals the number of electrons. Pro tip: atomic number = protons.",
        },
        # --- Lesson 3: electron shells ---
        {
            "text": r"What is the maximum number of electrons the FIRST electron shell can hold?",
            "difficulty": 2,
            "choices": [("2", True), ("8", False), ("6", False), ("18", False)],
            "explanation": r"The first shell holds up to 2 electrons; the second holds up to 8.",
        },
        {
            "text": r"The electrons in the outermost shell, which determine how an atom bonds, are called:",
            "difficulty": 2,
            "choices": [("Valence electrons", True), ("Neutrons", False),
                        ("Protons", False), ("Isotopes", False)],
            "explanation": r"Valence electrons are the outer-shell electrons that drive an atom's chemical behavior.",
        },
        {
            "text": ("Use the Bohr models.\n\n"
                     "[[figure:bohr_models|Bohr models of several atoms]]\n\n"
                     "In a Bohr model, the electrons are shown:"),
            "difficulty": 2,
            "choices": [("In shells (energy levels) around the nucleus", True),
                        ("Packed inside the nucleus", False),
                        ("Scattered randomly with no pattern", False),
                        ("Only on one side of the atom", False)],
            "explanation": r"The Bohr model places electrons in shells around the nucleus, filling the inner shell first. Pro tip: inner shell fills first (max 2).",
        },
        # --- Lesson 4: the periodic table ---
        {
            "text": r"The periodic table arranges the elements in order of increasing:",
            "difficulty": 1,
            "choices": [("Atomic number", True), ("Atomic mass only", False),
                        ("Alphabetical name", False), ("Discovery date", False)],
            "explanation": r"Elements are ordered by atomic number (number of protons).",
        },
        {
            "text": r"The horizontal ROWS of the periodic table are called:",
            "difficulty": 1,
            "choices": [("Periods", True), ("Groups", False),
                        ("Families", False), ("Shells", False)],
            "explanation": r"Rows are periods; columns are groups (families).",
        },
        {
            "text": r"Elements in the same GROUP (column) of the periodic table tend to have:",
            "difficulty": 2,
            "choices": [("Similar chemical properties", True),
                        ("Exactly the same mass", False),
                        ("No relationship to each other", False),
                        ("Completely different valence electrons", False)],
            "explanation": r"Elements in a group share the same number of valence electrons, giving them similar chemical properties.",
        },
        {
            "text": r"Group 18 elements (the noble gases) are best known for being:",
            "difficulty": 2,
            "choices": [("Very unreactive", True), ("Highly explosive", False),
                        ("Liquid metals", False), ("The most reactive of all", False)],
            "explanation": r"Noble gases have full outer shells, so they are very stable and unreactive.",
        },
        {
            "text": ("Use the periodic table map.\n\n"
                     "[[figure:periodic_table_map|Regions of the periodic table]]\n\n"
                     "According to the diagram, metals are found mostly on the:"),
            "difficulty": 2,
            "choices": [("Left and center", True), ("Far upper right", False),
                        ("Bottom row only", False), ("Outside the table", False)],
            "explanation": r"Most of the periodic table is metals (left and center); nonmetals are on the upper right, with metalloids between. Pro tip: metals left, nonmetals right.",
        },
        {
            "text": r"Elements along the 'staircase' with properties between metals and nonmetals are called:",
            "difficulty": 2,
            "choices": [("Metalloids", True), ("Noble gases", False),
                        ("Isotopes", False), ("Compounds", False)],
            "explanation": r"Metalloids (like silicon) sit along the staircase line and have properties of both metals and nonmetals.",
        },
        # --- Lesson 5: elements, compounds, molecules ---
        {
            "text": r"An element is:",
            "difficulty": 1,
            "choices": [("A substance made of only one kind of atom", True),
                        ("Two different atoms bonded together", False),
                        ("A mixture of several substances", False),
                        ("A type of energy", False)],
            "explanation": r"An element contains only one kind of atom and cannot be broken into simpler substances chemically.",
        },
        {
            "text": r"Water (H2O) is an example of a:",
            "difficulty": 2,
            "choices": [("Compound", True), ("Element", False),
                        ("Single atom", False), ("Mixture only", False)],
            "explanation": r"Water is a compound: two different elements (hydrogen and oxygen) chemically bonded in a fixed ratio.",
        },
        {
            "text": r"A compound differs from the elements that make it up because the compound:",
            "difficulty": 2,
            "choices": [("Has new, different properties", True),
                        ("Always keeps the exact properties of its elements", False),
                        ("Contains no atoms", False),
                        ("Cannot exist", False)],
            "explanation": r"Bonding changes properties: hydrogen and oxygen are gases, but the compound water is a liquid.",
        },
        {
            "text": ("Use the diagram.\n\n"
                     "[[figure:element_vs_compound|Elements versus compounds]]\n\n"
                     "Which represents a COMPOUND?"),
            "difficulty": 2,
            "choices": [("Different atoms bonded together (such as H2O)", True),
                        ("Many identical atoms of one kind", False),
                        ("A single atom by itself", False),
                        ("A beam of light", False)],
            "explanation": r"A compound is made of different atoms chemically bonded, like the H2O shown. An element has only one kind of atom. Pro tip: different bonded atoms = compound.",
        },
        {
            "text": r"The chemical formula H2O means each molecule contains:",
            "difficulty": 2,
            "choices": [("2 hydrogen atoms and 1 oxygen atom", True),
                        ("1 hydrogen atom and 2 oxygen atoms", False),
                        ("2 hydrogen atoms only", False),
                        ("20 water atoms", False)],
            "explanation": r"The subscript 2 applies to hydrogen, so H2O is 2 hydrogen atoms bonded to 1 oxygen atom.",
        },
        # --- Lesson 6: ions & isotopes ---
        {
            "text": r"An atom that has gained or lost electrons and now carries a charge is called a(n):",
            "difficulty": 1,
            "choices": [("Ion", True), ("Isotope", False),
                        ("Molecule", False), ("Compound", False)],
            "explanation": r"An ion is a charged atom, formed by gaining electrons (negative) or losing electrons (positive).",
        },
        {
            "text": r"An atom LOSES one electron. Its overall charge becomes:",
            "difficulty": 2,
            "choices": [("Positive", True), ("Negative", False),
                        ("Zero", False), ("Doubled in mass", False)],
            "explanation": r"Losing a negative electron leaves more protons than electrons, so the atom becomes a positive ion.",
        },
        {
            "text": r"Two atoms of the same element that have different numbers of neutrons are called:",
            "difficulty": 2,
            "choices": [("Isotopes", True), ("Ions", False),
                        ("Compounds", False), ("Molecules", False)],
            "explanation": r"Isotopes are atoms of one element (same protons) that differ in their number of neutrons, and so in mass.",
        },
        {
            "text": r"Carbon-12 and Carbon-14 both have 6 protons. They differ in their number of:",
            "difficulty": 3,
            "choices": [("Neutrons", True), ("Protons", False),
                        ("Electrons (when neutral)", False), ("Nuclei", False)],
            "explanation": r"Same element means same protons (6). The 12 vs 14 difference comes from neutrons (6 vs 8), making them isotopes.",
        },
        {
            "text": r"If you changed the number of PROTONS in an atom, you would:",
            "difficulty": 3,
            "choices": [("Make it a different element", True),
                        ("Make it an isotope of the same element", False),
                        ("Only change its charge", False),
                        ("Have no effect at all", False)],
            "explanation": r"The proton count defines the element, so changing it creates a different element entirely. (Changing neutrons makes an isotope; changing electrons makes an ion.)",
        },
    ],
    "essays": [
        {
            "text": (
                "Describe the structure of an atom. Name the three main particles, their charges, and where each is "
                "located. Then explain how to find the number of protons, neutrons, and electrons in a neutral atom "
                "using its atomic number and mass number."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) protons (+) and neutrons (0) in the nucleus, electrons (-) in shells around it; "
                "(2) the nucleus holds most of the mass; (3) protons = atomic number; (4) electrons = protons in a "
                "neutral atom; (5) neutrons = mass number - atomic number. Deduct for misplacing electrons in the "
                "nucleus or saying the atomic number is the mass."
            ),
        },
        {
            "text": (
                "Explain how the periodic table is organized. Describe what determines the order of the elements, "
                "what periods and groups are, and why elements in the same group have similar chemical properties. "
                "Include where metals and nonmetals are found."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) elements are ordered by increasing atomic number (protons); (2) rows are periods, "
                "columns are groups/families; (3) elements in the same group share the same number of valence "
                "electrons, giving similar properties; (4) metals are on the left/center, nonmetals on the upper "
                "right, with metalloids between. Deduct for saying the table is ordered by mass or alphabetically."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Atoms, Elements & the Periodic Table (Deep Dive)' course."

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
