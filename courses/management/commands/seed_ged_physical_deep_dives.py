"""
Seed focused deep-dive companion courses for 'GED Science: Physical Science'.

The parent Physical Science course gives seven one-lesson overviews. This command
creates a full mini-course for each overview lesson:

  1. Matter and Its States
  2. Atoms, Elements & the Periodic Table
  3. Chemical Reactions & Conservation of Mass
  4. Energy and Its Forms
  5. Forces and Motion
  6. Work, Power & Simple Machines
  7. Waves, Energy & Reading Science Data

Each course follows the same style as the Earth & Space Science deep dives:
plain-language lessons, labeled diagrams, common-misconception warnings, quick
tips, and GED-style multiple-choice practice with explanations. Written-response
prompts are intentionally not seeded in this MCQ-only phase.

Run:
    python manage.py seed_ged_physical_deep_dives
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSES = [
    {
        "title": "GED Science: Matter and Its States (Deep Dive)",
        "slug": "ged-matter-states",
        "program": "GED",
        "subject": "science",
        "description": (
            "A deep dive into matter, expanding the Physical Science overview lesson into a "
            "full mini-course. Students learn the particle model, solids, liquids, gases, "
            "phase changes, density, physical and chemical changes, mixtures, solutions, and "
            "how to read basic matter data. Includes labeled diagrams, misconception warnings, "
            "and GED-style practice."
        ),
        "lessons": [
            (
                "1. Matter, Mass & Volume",
                r"Matter is anything that has **mass** and takes up **space**. Mass tells how much material is present; volume tells how much space it occupies. Air counts as matter even though you cannot see it, because it has mass and fills space." "\n\n"
                r"[[figure:states_of_matter|The same particles can behave as a solid, liquid, or gas depending on their energy and spacing.]]" "\n\n"
                r"The GED often asks you to separate **matter** from **energy**. A rock, water, oxygen gas, and metal are matter. Light, heat, sound, and motion are forms of energy, not matter by themselves." "\n\n"
                r"⚠️ Common misconception: if you cannot see it, it is not matter. Air is invisible, but it still has mass and volume." "\n\n"
                r"💡 Tip: matter has mass and volume; energy causes change.",
            ),
            (
                "2. The Particle Model of Solids, Liquids & Gases",
                r"The easiest way to understand states of matter is to picture particles. In a **solid**, particles vibrate in fixed positions. In a **liquid**, particles stay close but slide around. In a **gas**, particles move fast, spread far apart, and fill the entire container." "\n\n"
                r"[[figure:states_of_matter|Particles are tight and fixed in solids, close but flowing in liquids, and far apart in gases.]]" "\n\n"
                r"This particle model explains the properties: solids keep shape and volume; liquids keep volume but change shape; gases change both shape and volume." "\n\n"
                r"⚠️ Common misconception: particles in a solid are not frozen still. They vibrate, but they cannot easily move past each other." "\n\n"
                r"💡 Tip: fixed shape = solid; fixed volume only = liquid; fills container = gas.",
            ),
            (
                "3. Changes of State: Heating and Cooling",
                r"Adding thermal energy usually moves matter from solid -> liquid -> gas. Removing thermal energy moves it back: gas -> liquid -> solid." "\n\n"
                r"- **Melting:** solid to liquid." "\n"
                r"- **Freezing:** liquid to solid." "\n"
                r"- **Evaporation/boiling:** liquid to gas." "\n"
                r"- **Condensation:** gas to liquid." "\n\n"
                r"During a change of state, the substance stays the same. Ice, liquid water, and water vapor are all still \(H_2O\)." "\n\n"
                r"⚠️ Common misconception: boiling water destroys water. It only changes liquid water into water vapor." "\n\n"
                r"💡 Tip: if no new substance forms, the change is physical.",
            ),
            (
                "4. Density: Why Some Things Float",
                r"**Density** compares mass to volume:" "\n"
                r"\[ \text{Density} = \frac{\text{mass}}{\text{volume}}. \]" "\n\n"
                r"A small object can be very dense if it packs a lot of mass into little space. Floating depends on density: an object floats in a fluid if it is less dense than the fluid and sinks if it is more dense." "\n\n"
                r"Worked example: a block has mass \(60\text{ g}\) and volume \(20\text{ cm}^3\). Its density is \(60/20 = 3\text{ g/cm}^3\)." "\n\n"
                r"⚠️ Common misconception: heavy things always sink. A huge ship is heavy, but its overall density can be less than water because it contains a lot of air space." "\n\n"
                r"💡 Tip: density is not just mass; it is mass packed into volume.",
            ),
            (
                "5. Physical Changes, Chemical Changes & Mixtures",
                r"A **physical change** changes form, size, shape, or state, but keeps the same substance. Melting, cutting, crushing, and dissolving are common examples. A **chemical change** makes a new substance, as in burning, rusting, cooking an egg, or reacting vinegar with baking soda." "\n\n"
                r"A **mixture** combines substances without chemically bonding them. Salt water is a mixture; the water and salt can be separated by evaporation. A **solution** is a mixture that looks uniform throughout." "\n\n"
                r"**Reading matter data (GED skill).** If a table lists mass and volume, compute density. If a graph shows temperature rising during heating, look for flat sections where a state change is happening." "\n\n"
                r"⚠️ Common misconception: dissolving always means a chemical reaction happened. Often it is only a physical change because the substance can be recovered." "\n\n"
                r"💡 Tip: new substance = chemical change; same substance in a new form = physical change.",
            ),
        ],
        "mcqs": [
            {"text": r"Which best defines matter?", "difficulty": 1, "choices": [("Anything that has mass and takes up space", True), ("Anything that gives off light", False), ("Only things you can see", False), ("Only solids", False)], "explanation": r"Matter has mass and volume. Air is matter even though it is invisible."},
            {"text": r"Which is a form of energy rather than matter?", "difficulty": 1, "choices": [("Sound", True), ("Oxygen gas", False), ("Water", False), ("Iron", False)], "explanation": r"Sound is energy traveling as a wave. Oxygen, water, and iron are matter."},
            {"text": r"Which state of matter has a definite volume but takes the shape of its container?", "difficulty": 1, "choices": [("Liquid", True), ("Solid", False), ("Gas", False), ("Plasma", False)], "explanation": r"A liquid keeps volume but changes shape to match its container."},
            {"text": r"When water vapor turns into liquid droplets, the change is called:", "difficulty": 2, "choices": [("Condensation", True), ("Evaporation", False), ("Melting", False), ("Freezing", False)], "explanation": r"Condensation is gas turning into liquid."},
            {"text": r"A block has mass \(80\text{ g}\) and volume \(40\text{ cm}^3\). What is its density?", "difficulty": 2, "choices": [(r"\(2\text{ g/cm}^3\)", True), (r"\(120\text{ g/cm}^3\)", False), (r"\(40\text{ g/cm}^3\)", False), (r"\(0.5\text{ g/cm}^3\)", False)], "explanation": r"Density \(= 80/40 = 2\text{ g/cm}^3\)."},
            {"text": r"Which is a chemical change?", "difficulty": 2, "choices": [("Wood burning", True), ("Ice melting", False), ("Paper being cut", False), ("Water freezing", False)], "explanation": r"Burning creates new substances, so it is chemical. The others are physical changes."},
            {"text": r"Which is a physical change?", "difficulty": 2, "choices": [("Sugar dissolving in water", True), ("Iron rusting", False), ("Gasoline burning", False), ("An egg cooking", False)], "explanation": r"Dissolving sugar changes its form and distribution, but it does not make a new substance."},
            {"text": r"According to the particle model, gas particles are usually:", "difficulty": 2, "choices": [("Far apart and moving freely", True), ("Locked in fixed positions", False), ("Close together and sliding only", False), ("Not moving at all", False)], "explanation": r"Gas particles have high energy, large spacing, and free motion."},
            {"text": r"An object floats in water because its overall density is:", "difficulty": 2, "choices": [("Less than water's density", True), ("Greater than water's density", False), ("Exactly zero", False), ("Always greater if the object is heavy", False)], "explanation": r"Objects float when their overall density is less than the fluid's density."},
            {"text": r"A heating graph has a flat section while heat is still being added. The best explanation is:", "difficulty": 3, "choices": [("A change of state is happening", True), ("The substance has disappeared", False), ("Temperature can never change", False), ("Mass is being created", False)], "explanation": r"During a phase change, added energy changes particle arrangement instead of raising temperature."},
        ],
    },
    {
        "title": "GED Science: Atoms, Elements & the Periodic Table (Deep Dive)",
        "slug": "ged-atoms-periodic-table",
        "program": "GED",
        "subject": "science",
        "description": (
            "A focused mini-course on atoms, subatomic particles, elements, compounds, and "
            "the periodic table. Students learn how atomic number identifies an element, how "
            "to read periodic-table boxes, why groups behave similarly, and how atoms bond "
            "into compounds."
        ),
        "lessons": [
            (
                "1. Inside an Atom",
                r"An **atom** is the smallest piece of an element that still behaves like that element. It has a tiny center, the **nucleus**, with electrons moving around it." "\n\n"
                r"[[figure:atom_structure|Protons and neutrons are in the nucleus; electrons occupy the space around it.]]" "\n\n"
                r"- **Protons** have positive charge and identify the element." "\n"
                r"- **Neutrons** have no charge and add mass." "\n"
                r"- **Electrons** have negative charge and are involved in bonding and electricity." "\n\n"
                r"⚠️ Common misconception: the nucleus is not most of the atom's size. It holds most of the mass, but the atom is mostly empty space." "\n\n"
                r"💡 Tip: proton = positive; neutron = neutral; electron = negative.",
            ),
            (
                "2. Atomic Number, Mass Number & Isotopes",
                r"The **atomic number** is the number of protons. It decides the element. Every carbon atom has 6 protons; if the proton number changes, it is no longer carbon." "\n\n"
                r"The **mass number** is protons plus neutrons. Atoms of the same element can have different neutron counts; these versions are called **isotopes**. Carbon-12 and carbon-14 are both carbon because both have 6 protons." "\n\n"
                r"⚠️ Common misconception: atomic number is not total particles. It counts protons only." "\n\n"
                r"💡 Tip: protons name the element; neutrons change the isotope.",
            ),
            (
                "3. Reading the Periodic Table",
                r"The periodic table is arranged by **atomic number**, increasing from left to right. A typical box gives the element's name, symbol, atomic number, and average atomic mass." "\n\n"
                r"Rows are called **periods**. Columns are called **groups** or families. Elements in the same group often behave similarly because they have similar outer-electron patterns." "\n\n"
                r"Metals are mostly on the left and center; nonmetals are mostly on the right; metalloids sit along a stair-step boundary." "\n\n"
                r"⚠️ Common misconception: elements in a column do not have the same mass. They have similar chemical behavior." "\n\n"
                r"💡 Tip: columns are chemical families.",
            ),
            (
                "4. Elements, Molecules & Compounds",
                r"An **element** contains one kind of atom. Oxygen (\(O\)), carbon (\(C\)), and gold (\(Au\)) are elements. A **molecule** is two or more atoms bonded together. A **compound** has atoms from two or more different elements bonded in a fixed ratio." "\n\n"
                r"Water, \(H_2O\), is a compound: two hydrogen atoms bonded to one oxygen atom. Oxygen gas, \(O_2\), is a molecule but not a compound because it contains only oxygen." "\n\n"
                r"⚠️ Common misconception: every molecule is not a compound. \(O_2\) is a molecule of one element." "\n\n"
                r"💡 Tip: compound = different elements chemically bonded.",
            ),
            (
                "5. Ions, Bonds & Periodic-Table Data",
                r"Atoms can gain or lose electrons to become **ions**. Losing electrons makes a positive ion; gaining electrons makes a negative ion. Opposite charges attract, which helps form **ionic bonds**. Atoms can also share electrons in **covalent bonds**." "\n\n"
                r"**Reading periodic-table data (GED skill).** If a question gives atomic number, use it as the proton count. For a neutral atom, electrons equal protons. If it gives mass number, subtract protons to find neutrons." "\n\n"
                r"Worked example: an atom has atomic number 8 and mass number 16. It has 8 protons and \(16 - 8 = 8\) neutrons. If neutral, it also has 8 electrons." "\n\n"
                r"⚠️ Common misconception: gaining an electron does not make an atom heavier in the same way adding a neutron does; electron mass is tiny for GED-level mass-number questions." "\n\n"
                r"💡 Tip: neutral atom: protons = electrons.",
            ),
        ],
        "mcqs": [
            {"text": r"Which particle has a positive charge?", "difficulty": 1, "choices": [("Proton", True), ("Electron", False), ("Neutron", False), ("Molecule", False)], "explanation": r"Protons are positive. Electrons are negative and neutrons are neutral."},
            {"text": r"What does atomic number tell you?", "difficulty": 1, "choices": [("Number of protons", True), ("Number of neutrons", False), ("Total mass in grams", False), ("Number of molecules", False)], "explanation": r"Atomic number is the proton count."},
            {"text": r"A neutral atom has 11 protons. How many electrons does it have?", "difficulty": 2, "choices": [("11", True), ("22", False), ("0", False), ("10", False)], "explanation": r"A neutral atom has equal protons and electrons."},
            {"text": r"Carbon-12 and carbon-14 are isotopes because they have:", "difficulty": 2, "choices": [("The same protons but different neutrons", True), ("Different protons", False), ("No electrons", False), ("The same mass number", False)], "explanation": r"Isotopes are versions of an element with different neutron counts."},
            {"text": r"Elements in the same group of the periodic table usually have:", "difficulty": 2, "choices": [("Similar chemical properties", True), ("The exact same mass", False), ("The same number of neutrons", False), ("No electrons", False)], "explanation": r"Groups are chemical families with similar behavior."},
            {"text": r"Water, \(H_2O\), is a compound because it contains:", "difficulty": 1, "choices": [("Different elements chemically bonded", True), ("Only one kind of atom", False), ("No atoms", False), ("Only loose mixtures", False)], "explanation": r"Water contains hydrogen and oxygen bonded in a fixed ratio."},
            {"text": r"Which is a molecule but not a compound?", "difficulty": 3, "choices": [(r"\(O_2\)", True), (r"\(H_2O\)", False), (r"\(CO_2\)", False), (r"\(NaCl\)", False)], "explanation": r"\(O_2\) has two atoms bonded, but both atoms are oxygen, so it is not a compound."},
            {"text": r"An atom with atomic number 8 and mass number 17 has how many neutrons?", "difficulty": 2, "choices": [("9", True), ("8", False), ("17", False), ("25", False)], "explanation": r"Neutrons = mass number - protons = 17 - 8 = 9."},
            {"text": r"When an atom gains electrons, it becomes:", "difficulty": 3, "choices": [("A negative ion", True), ("A positive ion", False), ("A different element", False), ("A neutron", False)], "explanation": r"Electrons are negative, so gaining them makes the atom negatively charged."},
            {"text": r"Which is found in the nucleus?", "difficulty": 1, "choices": [("Protons and neutrons", True), ("Electrons only", False), ("Electrons and molecules", False), ("Compounds only", False)], "explanation": r"The nucleus contains protons and neutrons."},
        ],
    },
    {
        "title": "GED Science: Chemical Reactions & Conservation of Mass (Deep Dive)",
        "slug": "ged-chemical-reactions-conservation",
        "program": "GED",
        "subject": "science",
        "description": (
            "A deep dive into chemical reactions, balancing equations, conservation of mass, "
            "reaction evidence, acids and bases, and reading reaction data. Built as a focused "
            "companion to the Physical Science overview lesson."
        ),
        "lessons": [
            (
                "1. Reactants, Products & Chemical Equations",
                r"A **chemical reaction** rearranges atoms to make new substances. The starting substances are **reactants**; the substances formed are **products**." "\n\n"
                r"\[ \text{reactants} \rightarrow \text{products} \]" "\n\n"
                r"Example: hydrogen and oxygen can react to form water:" "\n"
                r"\[ 2H_2 + O_2 \rightarrow 2H_2O. \]" "\n\n"
                r"⚠️ Common misconception: the arrow does not mean 'equals' in the algebra sense. It means 'reacts to form.'" "\n\n"
                r"💡 Tip: left side starts; right side forms.",
            ),
            (
                "2. Conservation of Mass",
                r"The **Law of Conservation of Mass** says matter is not created or destroyed in a chemical reaction. Atoms are only rearranged. In a closed container, total mass before a reaction equals total mass after." "\n\n"
                r"[[figure:conservation_mass|The number of each kind of atom is the same before and after a balanced reaction.]]" "\n\n"
                r"If 12 g of carbon reacts completely with 32 g of oxygen in a sealed container, the product mass is \(12 + 32 = 44\) g." "\n\n"
                r"⚠️ Common misconception: burning destroys mass. The mass often leaves as invisible gases; it is not destroyed." "\n\n"
                r"💡 Tip: in a closed system, mass in = mass out.",
            ),
            (
                "3. Balancing Equations",
                r"A chemical equation is **balanced** when each element has the same number of atoms on both sides. You balance by changing coefficients in front of formulas, not by changing subscripts inside formulas." "\n\n"
                r"Example: \(H_2 + O_2 \rightarrow H_2O\) is not balanced. Use coefficients:" "\n"
                r"\[ 2H_2 + O_2 \rightarrow 2H_2O. \]" "\n\n"
                r"Now both sides have 4 hydrogen atoms and 2 oxygen atoms." "\n\n"
                r"⚠️ Common misconception: changing \(H_2O\) to \(H_2O_2\) would balance oxygen, but it changes the substance from water to hydrogen peroxide." "\n\n"
                r"💡 Tip: coefficients change amounts; subscripts change identity.",
            ),
            (
                "4. Evidence of a Chemical Reaction",
                r"Common evidence of chemical reaction includes a color change, gas bubbles, a new solid (**precipitate**), heat or light given off, temperature change, or a new odor. These clues are useful, but they must be interpreted carefully." "\n\n"
                r"Some physical changes also make bubbles or temperature changes. Boiling water bubbles because of a physical state change; vinegar and baking soda bubble because a new gas forms in a reaction." "\n\n"
                r"⚠️ Common misconception: every bubble means chemical reaction. Boiling makes bubbles too, but no new substance forms." "\n\n"
                r"💡 Tip: look for evidence that a new substance formed.",
            ),
            (
                "5. Acids, Bases & Reaction Data",
                r"The **pH scale** measures how acidic or basic a solution is. A pH below 7 is acidic; 7 is neutral; above 7 is basic. Strong acids have very low pH; strong bases have very high pH." "\n\n"
                r"Acids and bases can react in **neutralization** reactions, often forming water and a salt. GED questions may give a pH table or before/after mass data." "\n\n"
                r"**Reading reaction data (GED skill).** If mass appears to decrease in an open container, ask whether gas escaped. If the system is closed, total mass should stay the same." "\n\n"
                r"⚠️ Common misconception: acid means dangerous and base means safe. Strong bases can be very dangerous too." "\n\n"
                r"💡 Tip: pH less than 7 acid; pH 7 neutral; pH greater than 7 base.",
            ),
        ],
        "mcqs": [
            {"text": r"In a chemical equation, reactants are usually written:", "difficulty": 1, "choices": [("On the left side", True), ("On the right side", False), ("Under the arrow", False), ("Only above the equation", False)], "explanation": r"Reactants are the starting substances on the left side."},
            {"text": r"Which statement best describes conservation of mass?", "difficulty": 1, "choices": [("Atoms are rearranged, not created or destroyed", True), ("Mass disappears in reactions", False), ("Products always weigh less", False), ("Reactants are destroyed completely", False)], "explanation": r"Chemical reactions rearrange atoms while conserving total mass."},
            {"text": r"5 g of reactant A combines with 7 g of reactant B in a sealed container. What is the product mass?", "difficulty": 2, "choices": [("12 g", True), ("7 g", False), ("2 g", False), ("35 g", False)], "explanation": r"In a sealed container mass is conserved, so \(5 + 7 = 12\) g."},
            {"text": r"To balance a chemical equation, you should change:", "difficulty": 2, "choices": [("Coefficients", True), ("Subscripts inside formulas", False), ("Element symbols", False), ("The law of mass", False)], "explanation": r"Coefficients change how many molecules are present; subscripts change the substance."},
            {"text": r"Which is strong evidence that a new substance formed?", "difficulty": 2, "choices": [("A precipitate forms when two clear liquids are mixed", True), ("Ice melts", False), ("Paper is folded", False), ("Water is poured", False)], "explanation": r"A new solid forming from mixed solutions is evidence of a chemical reaction."},
            {"text": r"Wood burns and the ash weighs less than the original wood. In an open fireplace, the missing mass mostly:", "difficulty": 3, "choices": [("Escaped as gases", True), ("Was destroyed", False), ("Turned into nothing", False), ("Became pure light only", False)], "explanation": r"Mass leaves as carbon dioxide, water vapor, and other gases."},
            {"text": r"Which pH value is acidic?", "difficulty": 1, "choices": [("3", True), ("7", False), ("9", False), ("12", False)], "explanation": r"pH below 7 is acidic."},
            {"text": r"Which pH value is basic?", "difficulty": 1, "choices": [("11", True), ("7", False), ("5", False), ("1", False)], "explanation": r"pH above 7 is basic."},
            {"text": r"Why is \(2H_2 + O_2 \rightarrow 2H_2O\) balanced?", "difficulty": 3, "choices": [("Both sides have 4 H atoms and 2 O atoms", True), ("Both sides have one molecule", False), ("It has no products", False), ("The subscripts are all equal", False)], "explanation": r"Count atoms: 4 hydrogen and 2 oxygen on each side."},
            {"text": r"Which situation is a physical change, not a chemical reaction?", "difficulty": 2, "choices": [("Water boiling", True), ("Iron rusting", False), ("Gasoline burning", False), ("Vinegar reacting with baking soda", False)], "explanation": r"Boiling changes state only; the substance is still water."},
        ],
    },
    {
        "title": "GED Science: Energy and Its Forms (Deep Dive)",
        "slug": "ged-energy-forms-transformations",
        "program": "GED",
        "subject": "science",
        "description": (
            "A focused Physical Science deep dive on kinetic and potential energy, chemical, "
            "thermal, electrical, light, and sound energy, energy transformations, conservation "
            "of energy, heat transfer, efficiency, and GED data reasoning."
        ),
        "lessons": [
            (
                "1. What Energy Does",
                r"**Energy** is the ability to do work or cause change. It is not matter, but it affects matter: it can move it, heat it, stretch it, lift it, or make it glow." "\n\n"
                r"[[figure:energy_forms|A flashlight transforms stored chemical energy into electrical energy, then light and heat.]]" "\n\n"
                r"Common forms include kinetic, potential, chemical, thermal, electrical, light, and sound energy." "\n\n"
                r"⚠️ Common misconception: energy is not a material that disappears. It changes form." "\n\n"
                r"💡 Tip: ask, 'What changed?' Energy is what made the change possible.",
            ),
            (
                "2. Kinetic and Potential Energy",
                r"**Kinetic energy** is energy of motion. A moving car, flowing water, and vibrating speaker all have kinetic energy. **Potential energy** is stored energy due to position, shape, or arrangement." "\n\n"
                r"A ball at the top of a hill has gravitational potential energy. As it rolls down, that potential energy changes into kinetic energy." "\n\n"
                r"⚠️ Common misconception: an object at rest can still have energy. A raised object can have stored potential energy." "\n\n"
                r"💡 Tip: motion = kinetic; stored by position = potential.",
            ),
            (
                "3. Energy Transformations",
                r"Most devices are energy converters. A toaster changes electrical energy into thermal energy. A speaker changes electrical energy into sound energy. A car engine changes chemical energy into motion and heat." "\n\n"
                r"[[figure:energy_forms|Trace the energy chain: chemical -> electrical -> light plus heat.]]" "\n\n"
                r"Useful energy is the energy you wanted. Waste energy is usually heat or sound that spreads into the surroundings." "\n\n"
                r"⚠️ Common misconception: waste energy is destroyed. It is still energy, just spread out in a less useful form." "\n\n"
                r"💡 Tip: write energy chains with arrows.",
            ),
            (
                "4. Conservation of Energy and Efficiency",
                r"The **Law of Conservation of Energy** says energy cannot be created or destroyed. It can only be transferred or transformed." "\n\n"
                r"No real machine is 100% efficient because some energy spreads as thermal energy due to friction, electrical resistance, sound, or air resistance. Efficiency compares useful output energy to total input energy." "\n\n"
                r"\[ \text{Efficiency} = \frac{\text{useful output}}{\text{total input}} \times 100\%. \]" "\n\n"
                r"⚠️ Common misconception: low efficiency means energy vanished. It means more energy became less useful forms." "\n\n"
                r"💡 Tip: total energy is conserved; useful energy may decrease.",
            ),
            (
                "5. Heat Transfer and Energy Data",
                r"Thermal energy moves from warmer objects to cooler objects. It transfers by **conduction** (direct contact), **convection** (moving fluids), and **radiation** (waves through space)." "\n\n"
                r"**Reading energy data (GED skill).** In a graph of height and speed for a roller coaster, high points usually mean more potential energy; low fast points mean more kinetic energy. In a temperature graph, follow the trend and read the units." "\n\n"
                r"⚠️ Common misconception: cold moves into warm objects. In science, heat transfer is thermal energy moving from warmer to cooler." "\n\n"
                r"💡 Tip: conduction touches, convection flows, radiation travels as waves.",
            ),
        ],
        "mcqs": [
            {"text": r"A moving bicycle has mostly:", "difficulty": 1, "choices": [("Kinetic energy", True), ("No energy", False), ("Only chemical energy", False), ("Nuclear energy", False)], "explanation": r"Kinetic energy is energy of motion."},
            {"text": r"A book sitting on a high shelf has gravitational:", "difficulty": 1, "choices": [("Potential energy", True), ("Kinetic energy", False), ("Sound energy", False), ("No energy", False)], "explanation": r"Height gives stored gravitational potential energy."},
            {"text": r"A flashlight mainly changes chemical energy into:", "difficulty": 2, "choices": [("Electrical energy, then light and heat", True), ("Sound only", False), ("Nuclear energy", False), ("Mass only", False)], "explanation": r"The battery's chemical energy becomes electrical energy, then light and heat."},
            {"text": r"Energy conservation means energy:", "difficulty": 1, "choices": [("Changes form but is not created or destroyed", True), ("Is destroyed when used", False), ("Can only be kinetic", False), ("Has mass and volume", False)], "explanation": r"Energy is conserved across transformations."},
            {"text": r"A machine uses 200 J of input energy and produces 50 J of useful output. Its efficiency is:", "difficulty": 2, "choices": [("25%", True), ("4%", False), ("150%", False), ("250%", False)], "explanation": r"\(50/200 \times 100\% = 25\%\)."},
            {"text": r"Thermal energy moving through direct contact is:", "difficulty": 1, "choices": [("Conduction", True), ("Convection", False), ("Radiation", False), ("Reflection", False)], "explanation": r"Conduction is heat transfer by contact."},
            {"text": r"Warm air rising is an example of:", "difficulty": 2, "choices": [("Convection", True), ("Conduction", False), ("Chemical bonding", False), ("Mass conservation", False)], "explanation": r"Convection transfers heat by movement of a fluid such as air."},
            {"text": r"Sunlight warming your skin is heat transfer by:", "difficulty": 2, "choices": [("Radiation", True), ("Conduction", False), ("Convection", False), ("Freezing", False)], "explanation": r"Radiation transfers energy by electromagnetic waves and can travel through space."},
            {"text": r"When a roller coaster car moves downhill, potential energy is mostly changing into:", "difficulty": 2, "choices": [("Kinetic energy", True), ("New mass", False), ("Nothing", False), ("Only chemical energy", False)], "explanation": r"As height decreases, stored gravitational potential energy changes into motion."},
            {"text": r"Friction usually converts useful mechanical energy into:", "difficulty": 2, "choices": [("Thermal energy", True), ("More height", False), ("New atoms", False), ("Gravity", False)], "explanation": r"Friction spreads energy out as heat."},
        ],
    },
    {
        "title": "GED Science: Forces and Motion (Deep Dive)",
        "slug": "ged-forces-motion",
        "program": "GED",
        "subject": "science",
        "description": (
            "A Physical Science deep dive into pushes and pulls, net force, inertia, Newton's "
            "laws, gravity, friction, acceleration, speed, and reading motion graphs."
        ),
        "lessons": [
            (
                "1. Forces, Net Force & Balanced Forces",
                r"A **force** is a push or pull. Forces can start motion, stop motion, speed something up, slow it down, or change direction. The important idea is **net force**: the overall force after all pushes and pulls are combined." "\n\n"
                r"If forces are balanced, net force is zero and motion does not change. If forces are unbalanced, motion changes." "\n\n"
                r"⚠️ Common misconception: an object moving at constant speed needs a net force to keep moving. With no net force, it keeps moving at constant velocity." "\n\n"
                r"💡 Tip: unbalanced force changes motion.",
            ),
            (
                "2. Newton's First Law: Inertia",
                r"Newton's First Law says an object at rest stays at rest, and an object in motion keeps moving at constant velocity, unless acted on by a net external force. This tendency is **inertia**." "\n\n"
                r"Seat belts matter because your body tends to keep moving when the car suddenly stops." "\n\n"
                r"⚠️ Common misconception: inertia is a force. It is not; it is an object's resistance to change in motion." "\n\n"
                r"💡 Tip: more mass means more inertia.",
            ),
            (
                "3. Newton's Second Law: \(F = ma\)",
                r"Newton's Second Law connects force, mass, and acceleration:" "\n"
                r"\[ F = m \times a. \]" "\n\n"
                r"[[figure:newton_second_law|The same push gives less acceleration to a heavier object and more acceleration to a lighter object.]]" "\n\n"
                r"For the same mass, more force means more acceleration. For the same force, more mass means less acceleration." "\n\n"
                r"Worked example: a \(5\text{ kg}\) cart pushed by \(20\text{ N}\) accelerates at \(a = F/m = 20/5 = 4\text{ m/s}^2\)." "\n\n"
                r"⚠️ Common misconception: students often multiply when they should divide to find acceleration." "\n\n"
                r"💡 Tip: \(a = F/m\).",
            ),
            (
                "4. Newton's Third Law, Gravity & Friction",
                r"Newton's Third Law says every action force has an equal and opposite reaction force. A rocket pushes exhaust gas down; the gas pushes the rocket up." "\n\n"
                r"**Gravity** pulls masses together. Near Earth's surface it accelerates falling objects at about \(9.8\text{ m/s}^2\) if air resistance is ignored. **Friction** resists motion between surfaces and often turns mechanical energy into heat." "\n\n"
                r"⚠️ Common misconception: heavier objects fall faster. Without air resistance, objects fall with the same acceleration." "\n\n"
                r"💡 Tip: action-reaction forces act on different objects.",
            ),
            (
                "5. Speed, Acceleration & Motion Data",
                r"Speed is distance divided by time:" "\n"
                r"\[ \text{speed} = \frac{\text{distance}}{\text{time}}. \]" "\n\n"
                r"Acceleration is a change in velocity, which can mean speeding up, slowing down, or changing direction." "\n\n"
                r"**Reading motion data (GED skill).** On a distance-time graph, a steeper line means greater speed. A flat line means no change in distance, so the object is stopped. On a speed-time graph, a rising line means acceleration." "\n\n"
                r"⚠️ Common misconception: acceleration only means speeding up. Slowing down and turning are acceleration too because velocity changes." "\n\n"
                r"💡 Tip: graph slope often tells the story.",
            ),
        ],
        "mcqs": [
            {"text": r"A force is best described as:", "difficulty": 1, "choices": [("A push or pull", True), ("A type of atom", False), ("Stored chemical energy", False), ("Only gravity", False)], "explanation": r"A force is a push or pull."},
            {"text": r"If forces on an object are balanced, the net force is:", "difficulty": 1, "choices": [("0 N", True), ("Always 10 N", False), ("Infinite", False), ("Equal to mass", False)], "explanation": r"Balanced forces cancel, so net force is zero."},
            {"text": r"Newton's First Law is also called the law of:", "difficulty": 1, "choices": [("Inertia", True), ("Density", False), ("Conservation of mass", False), ("pH", False)], "explanation": r"Inertia is resistance to change in motion."},
            {"text": r"A \(4\text{ kg}\) object accelerates at \(3\text{ m/s}^2\). What net force acts on it?", "difficulty": 2, "choices": [("12 N", True), ("7 N", False), ("1.3 N", False), ("0 N", False)], "explanation": r"\(F = ma = 4 \times 3 = 12\text{ N}\)."},
            {"text": r"A \(10\text{ kg}\) cart is pushed with \(50\text{ N}\). What is its acceleration?", "difficulty": 2, "choices": [(r"\(5\text{ m/s}^2\)", True), (r"\(500\text{ m/s}^2\)", False), (r"\(60\text{ m/s}^2\)", False), (r"\(0.2\text{ m/s}^2\)", False)], "explanation": r"\(a = F/m = 50/10 = 5\text{ m/s}^2\)."},
            {"text": r"A rocket pushes exhaust downward and the exhaust pushes the rocket upward. This is Newton's:", "difficulty": 2, "choices": [("Third Law", True), ("First Law", False), ("Law of density", False), ("Conservation of mass only", False)], "explanation": r"This is an action-reaction force pair."},
            {"text": r"Ignoring air resistance, a hammer and feather dropped together:", "difficulty": 2, "choices": [("Fall with the same acceleration", True), ("Have no gravity", False), ("The feather falls faster", False), ("The hammer always accelerates more", False)], "explanation": r"Gravity gives the same acceleration when air resistance is ignored."},
            {"text": r"A car travels 120 km in 2 hours. Its average speed is:", "difficulty": 1, "choices": [("60 km/h", True), ("240 km/h", False), ("122 km/h", False), ("2 km/h", False)], "explanation": r"Speed \(= 120/2 = 60\text{ km/h}\)."},
            {"text": r"On a distance-time graph, a steeper line means:", "difficulty": 2, "choices": [("Greater speed", True), ("Less mass", False), ("Lower temperature", False), ("No motion", False)], "explanation": r"Slope on a distance-time graph represents speed."},
            {"text": r"Which is an example of acceleration?", "difficulty": 2, "choices": [("A car turning at constant speed", True), ("A book resting on a table", False), ("A train moving straight at constant velocity", False), ("A parked bicycle", False)], "explanation": r"Changing direction changes velocity, so it is acceleration."},
        ],
    },
    {
        "title": "GED Science: Work, Power & Simple Machines (Deep Dive)",
        "slug": "ged-work-power-simple-machines",
        "program": "GED",
        "subject": "science",
        "description": (
            "A focused companion course on scientific work, power, mechanical advantage, "
            "simple machines, ramps, levers, pulleys, efficiency, and GED-style formula/data "
            "questions."
        ),
        "lessons": [
            (
                "1. Scientific Work",
                r"In science, **work** happens only when a force moves an object a distance in the direction of the force:" "\n"
                r"\[ W = F \times d. \]" "\n\n"
                r"Work is measured in joules (J). Pushing a box across the floor is work. Holding a heavy box still is not scientific work because the distance moved is zero." "\n\n"
                r"⚠️ Common misconception: if it feels tiring, it must be work. In physics, no movement means no work." "\n\n"
                r"💡 Tip: work needs both force and distance.",
            ),
            (
                "2. Power: How Fast Work Gets Done",
                r"**Power** measures the rate of doing work:" "\n"
                r"\[ P = \frac{W}{t}. \]" "\n\n"
                r"Power is measured in watts (W). Two people can do the same work lifting boxes, but the person who does it faster uses more power." "\n\n"
                r"⚠️ Common misconception: work and power mean the same thing. Work is energy transferred; power is how fast it is transferred." "\n\n"
                r"💡 Tip: power includes time.",
            ),
            (
                "3. Simple Machines and Mechanical Advantage",
                r"A **simple machine** makes work easier by changing the size or direction of a force. The six classic machines are lever, pulley, wheel and axle, inclined plane, wedge, and screw." "\n\n"
                r"[[figure:lever_machine|A lever can lift a load with less input force by moving the input side a longer distance.]]" "\n\n"
                r"Mechanical advantage tells how much a machine multiplies force. But the trade-off is distance: less force usually means pushing or pulling through a longer distance." "\n\n"
                r"⚠️ Common misconception: machines create energy. They do not; they trade force for distance." "\n\n"
                r"💡 Tip: easier force, longer distance.",
            ),
            (
                "4. Ramps, Levers and Pulleys",
                r"A **ramp** or inclined plane lets you lift an object using less force over a longer distance. A **lever** rotates around a fulcrum. A **pulley** changes the direction of a pull and, in combinations, can reduce the force needed." "\n\n"
                r"The total work is ideally the same: lifting a box straight up takes large force over short distance; pushing it up a ramp takes smaller force over longer distance." "\n\n"
                r"⚠️ Common misconception: a longer ramp removes work. It reduces force, but distance increases." "\n\n"
                r"💡 Tip: ramps trade force for distance.",
            ),
            (
                "5. Efficiency and Machine Data",
                r"Real machines lose some input energy to friction and heat, so useful output work is less than input work. Efficiency is:" "\n"
                r"\[ \text{Efficiency} = \frac{\text{useful output work}}{\text{input work}} \times 100\%. \]" "\n\n"
                r"**Reading machine data (GED skill).** For formula questions, identify what is given, write the formula, substitute units, and solve. If a table compares ramps, longer ramps usually require less force but more distance." "\n\n"
                r"⚠️ Common misconception: an efficiency greater than 100% is realistic. It would mean output energy exceeds input energy, violating conservation of energy." "\n\n"
                r"💡 Tip: no real machine is 100% efficient.",
            ),
        ],
        "mcqs": [
            {"text": r"Scientific work requires:", "difficulty": 1, "choices": [("Force and movement through distance", True), ("Only effort", False), ("Only mass", False), ("No motion", False)], "explanation": r"Work needs force applied over a distance."},
            {"text": r"A 20 N force moves a box 4 m. How much work is done?", "difficulty": 1, "choices": [("80 J", True), ("24 J", False), ("5 J", False), ("16 J", False)], "explanation": r"\(W = Fd = 20 \times 4 = 80\text{ J}\)."},
            {"text": r"If a box does not move, the scientific work done on it is:", "difficulty": 1, "choices": [("0 J", True), ("Equal to its mass", False), ("Always 100 J", False), ("Impossible to know", False)], "explanation": r"Distance is zero, so work is zero."},
            {"text": r"Power measures:", "difficulty": 1, "choices": [("How fast work is done", True), ("Only distance", False), ("Only mass", False), ("pH level", False)], "explanation": r"Power is work divided by time."},
            {"text": r"100 J of work is done in 5 s. What is the power?", "difficulty": 2, "choices": [("20 W", True), ("500 W", False), ("105 W", False), ("5 W", False)], "explanation": r"\(P = W/t = 100/5 = 20\text{ W}\)."},
            {"text": r"A ramp helps by letting you use:", "difficulty": 2, "choices": [("Less force over a longer distance", True), ("More force over zero distance", False), ("No energy at all", False), ("Less distance and less force with no trade-off", False)], "explanation": r"A ramp trades force for distance."},
            {"text": r"Which is a simple machine?", "difficulty": 1, "choices": [("Pulley", True), ("Battery", False), ("Atom", False), ("Thermometer liquid", False)], "explanation": r"A pulley is one of the six simple machines."},
            {"text": r"A lever rotates around a point called the:", "difficulty": 2, "choices": [("Fulcrum", True), ("Nucleus", False), ("Crest", False), ("Ion", False)], "explanation": r"The fulcrum is the pivot point of a lever."},
            {"text": r"A machine has 300 J input work and 240 J useful output work. Its efficiency is:", "difficulty": 2, "choices": [("80%", True), ("125%", False), ("60%", False), ("540%", False)], "explanation": r"\(240/300 \times 100\% = 80\%\)."},
            {"text": r"No real machine is 100% efficient mainly because:", "difficulty": 2, "choices": [("Some energy becomes heat due to friction and other losses", True), ("Energy is destroyed", False), ("Machines create mass", False), ("Forces do not exist", False)], "explanation": r"Energy is conserved, but some spreads into less useful forms such as heat."},
        ],
    },
    {
        "title": "GED Science: Waves, Energy & Reading Science Data (Deep Dive)",
        "slug": "ged-waves-energy-data",
        "program": "GED",
        "subject": "science",
        "description": (
            "A focused deep dive into waves as energy transfer, wave anatomy, amplitude, "
            "wavelength, frequency, transverse and longitudinal waves, sound, light, and "
            "wave-data interpretation."
        ),
        "lessons": [
            (
                "1. Waves Transfer Energy",
                r"A **wave** is a disturbance that transfers energy from place to place. The medium may wiggle, but the energy travels onward. Water waves move energy across the surface while the water mostly moves up and down." "\n\n"
                r"[[figure:wave_anatomy|A wave is described by crest, trough, amplitude, wavelength, and frequency.]]" "\n\n"
                r"⚠️ Common misconception: waves carry the material all the way with them. Usually the material vibrates around a resting position while energy moves." "\n\n"
                r"💡 Tip: wave = energy transfer.",
            ),
            (
                "2. Wave Anatomy: Amplitude and Wavelength",
                r"The **crest** is the high point of a wave; the **trough** is the low point. **Amplitude** is the height from the rest position to a crest or trough. Bigger amplitude means more energy." "\n\n"
                r"**Wavelength** is the distance from one matching point to the next, such as crest to crest." "\n\n"
                r"[[figure:wave_anatomy|Amplitude measures height; wavelength measures one full cycle.]]" "\n\n"
                r"⚠️ Common misconception: amplitude and wavelength are the same measurement. Amplitude is height; wavelength is length." "\n\n"
                r"💡 Tip: amplitude = height; wavelength = cycle length.",
            ),
            (
                "3. Frequency, Speed and the Wave Equation",
                r"**Frequency** is how many waves pass a point each second, measured in hertz (Hz). For a wave traveling at fixed speed, higher frequency means shorter wavelength." "\n\n"
                r"The relationship is:" "\n"
                r"\[ v = f \lambda \]" "\n"
                r"where \(v\) is wave speed, \(f\) is frequency, and \(\lambda\) is wavelength." "\n\n"
                r"⚠️ Common misconception: frequency and wavelength always increase together. At the same speed, they move in opposite directions." "\n\n"
                r"💡 Tip: more waves per second means each wave is shorter.",
            ),
            (
                "4. Transverse, Longitudinal, Sound and Light",
                r"In a **transverse** wave, the vibration is perpendicular to the direction the wave travels. Light and many water-wave models are transverse. In a **longitudinal** wave, particles vibrate back and forth along the direction of travel; sound is longitudinal." "\n\n"
                r"Sound needs a medium such as air, water, or solid material. Light is an electromagnetic wave and can travel through empty space." "\n\n"
                r"⚠️ Common misconception: sound can travel through outer space like it does through air. Without a medium, sound cannot travel." "\n\n"
                r"💡 Tip: sound needs matter; light can cross space.",
            ),
            (
                "5. Reading Wave Data",
                r"GED wave questions often use diagrams, tables, or graphs. First read the title, axis labels, and units. If a graph shows amplitude, think energy/loudness/brightness. If it shows frequency, think waves per second. If frequency rises while speed is constant, wavelength falls." "\n\n"
                r"Worked example: a sound wave with higher amplitude is louder. A sound wave with higher frequency has higher pitch." "\n\n"
                r"⚠️ Common misconception: loudness and pitch are the same. Loudness depends mainly on amplitude; pitch depends on frequency." "\n\n"
                r"💡 Tip: amplitude -> loudness/energy; frequency -> pitch/color.",
            ),
        ],
        "mcqs": [
            {"text": r"What does a wave transfer?", "difficulty": 1, "choices": [("Energy", True), ("Only atoms permanently", False), ("Only mass", False), ("Nothing", False)], "explanation": r"Waves transfer energy from place to place."},
            {"text": r"The highest point of a wave is the:", "difficulty": 1, "choices": [("Crest", True), ("Trough", False), ("Wavelength", False), ("Frequency", False)], "explanation": r"The crest is the high point."},
            {"text": r"The lowest point of a wave is the:", "difficulty": 1, "choices": [("Trough", True), ("Crest", False), ("Amplitude", False), ("Hertz", False)], "explanation": r"The trough is the low point."},
            {"text": r"Amplitude measures:", "difficulty": 2, "choices": [("Wave height from rest position", True), ("Distance from crest to crest", False), ("Waves per second", False), ("Mass of the medium", False)], "explanation": r"Amplitude is wave height."},
            {"text": r"Wavelength is the distance:", "difficulty": 2, "choices": [("From one crest to the next crest", True), ("From rest line to crest", False), ("A wave travels in one hour only", False), ("Between two atoms only", False)], "explanation": r"Wavelength is one full cycle length, often crest to crest."},
            {"text": r"Frequency is measured in:", "difficulty": 1, "choices": [("Hertz", True), ("Newtons", False), ("Joules", False), ("Watts", False)], "explanation": r"Frequency is waves per second, measured in hertz."},
            {"text": r"If wave speed stays constant and frequency increases, wavelength:", "difficulty": 2, "choices": [("Decreases", True), ("Increases", False), ("Stays exactly the same always", False), ("Becomes mass", False)], "explanation": r"With constant speed, frequency and wavelength are inversely related."},
            {"text": r"Sound is best described as:", "difficulty": 2, "choices": [("A longitudinal wave that needs a medium", True), ("A transverse wave that needs no matter", False), ("A chemical reaction", False), ("A static object", False)], "explanation": r"Sound travels by compressions and rarefactions through matter."},
            {"text": r"Light can travel through empty space because it is:", "difficulty": 2, "choices": [("An electromagnetic wave", True), ("A sound wave", False), ("A liquid", False), ("A chemical compound", False)], "explanation": r"Light is electromagnetic and does not need a material medium."},
            {"text": r"A sound wave with greater amplitude is usually heard as:", "difficulty": 2, "choices": [("Louder", True), ("Higher pitch", False), ("Lower frequency", False), ("Invisible", False)], "explanation": r"Loudness depends mainly on amplitude; pitch depends on frequency."},
        ],
    },
]


LESSON_EXPANSIONS = {
    "ged-matter-states": [
        r"""
**Deep explanation.** Mass and volume are measured in different ways, and GED questions often expect you to tell them apart. Mass is the amount of matter in an object, usually measured in grams or kilograms. Volume is the amount of space the matter takes up, measured in units such as milliliters, liters, cubic centimeters, or cubic meters. A brick and a sponge may have similar volume, but the brick usually has more mass because its particles are packed more tightly.

For regular shapes, volume can be calculated with a formula. For example, a rectangular box has volume \(V = l \times w \times h\). For irregular objects, scientists often use water displacement: place water in a graduated cylinder, record the starting volume, drop in the object, and subtract the starting volume from the ending volume. If the water rises from \(50\text{ mL}\) to \(67\text{ mL}\), the object's volume is \(17\text{ mL}\), which is the same as \(17\text{ cm}^3\).

**How GED may ask it.** A question might describe air in a balloon, water in a bottle, or metal in a cube and ask whether it is matter. Use the test: does it have mass and take up space? If yes, it is matter. Light from a lamp and sound from a speaker can move through matter, but they are forms of energy rather than matter themselves.
""",
        r"""
**Deep explanation.** The particle model connects invisible particle behavior to visible properties. Solids keep their shape because particles are locked into a pattern and only vibrate around fixed positions. Liquids flow because particles stay close but can slide past one another. Gases fill the container because particles are far apart, move quickly, and collide with the container walls.

Pressure in a gas comes from collisions. When gas particles hit the inside of a tire or balloon, those impacts create pressure. If the same amount of gas is squeezed into a smaller volume, particles collide with the walls more often, so pressure usually increases. That is why a sealed syringe gets harder to push as the trapped air is compressed.

**Useful comparison.** A solid has definite shape and definite volume. A liquid has no definite shape but does have definite volume. A gas has neither definite shape nor definite volume because it expands to fill the available space. This table-like comparison is common on GED science items.
""",
        r"""
**Deep explanation.** During heating, added energy can do two different jobs. It can increase particle motion, which raises temperature, or it can break particles out of a more fixed arrangement, which changes state. During melting or boiling, temperature may stay flat for a while even though heat is still being added because the energy is being used to rearrange particles rather than speed them up.

Evaporation and boiling both turn liquid into gas, but they are not identical. Evaporation happens at the surface and can happen below the boiling point, such as a puddle slowly drying. Boiling happens throughout the liquid when vapor bubbles form inside it. Sublimation is solid directly to gas, as with dry ice; deposition is gas directly to solid, as with frost forming from water vapor.

**How to read a heating curve.** Rising line segments usually mean temperature is increasing within one state. Flat line segments usually mean a phase change is happening. The substance is still the same substance unless the problem says a new substance formed.
""",
        r"""
**Deep explanation.** Density is an intensive property, meaning it does not depend only on the size of the sample. If you cut a block of pure aluminum in half, the mass and volume both decrease, but the density stays about the same because the same material is packed the same way. That is why density can help identify substances.

Use units carefully. If mass is in grams and volume is in cubic centimeters, density is in \(\text{g/cm}^3\). If mass is in kilograms and volume is in liters, density might be \(\text{kg/L}\). On GED problems, the formula is often enough: divide mass by volume. Do not add them or multiply them unless the question asks for a different quantity.

**Floating logic.** Water has a density of about \(1\text{ g/cm}^3\). An object with an overall density less than water floats; one with greater density sinks. "Overall" matters because a hollow steel ship includes air space, so the ship-and-air combination can be less dense than water even though solid steel itself is denser than water.
""",
        r"""
**Deep explanation.** A physical change changes the arrangement, size, shape, or state of matter without changing what the substance is. Crushing chalk, melting ice, tearing paper, and dissolving sugar in water are physical changes. A chemical change rearranges atoms into new substances. Evidence can include gas production, a lasting color change, heat or light release, odor change, or a solid precipitate forming when two liquids are mixed.

Mixtures are different from compounds. In a mixture, substances are together but not chemically bonded in a fixed ratio. Trail mix, air, salt water, and muddy water are mixtures. A solution is a uniform mixture, so the same composition is found throughout. A compound such as water has a fixed formula and can only be separated by chemical means.

**GED data routine.** When a question gives observations, ask: did a new substance form? Bubbles alone are not always enough, because boiling makes bubbles without a chemical reaction. If the bubbles come from mixing substances and a new gas forms, that supports a chemical-change answer.
""",
    ],
    "ged-atoms-periodic-table": [
        r"""
**Deep explanation.** The atom's nucleus is extremely small compared with the whole atom, but it contains nearly all of the atom's mass because protons and neutrons are much heavier than electrons. Electrons occupy the space around the nucleus and are responsible for many chemical and electrical behaviors. When atoms bond, gain charge, or conduct electricity, the electron arrangement is usually the important part.

Charges also matter. Protons are positive, electrons are negative, and neutrons are neutral. Opposite charges attract, so negatively charged electrons are attracted to the positively charged nucleus. A neutral atom has the same number of protons and electrons, which makes the total charge zero.

**GED shortcut.** If the question asks what identifies an element, choose protons or atomic number. If it asks what mostly affects bonding, choose electrons, especially outer electrons. If it asks where most mass is located, choose the nucleus.
""",
        r"""
**Deep explanation.** The atomic number is like an element's ID number because it counts protons. A neutral atom with atomic number 6 is carbon and has 6 electrons. If it has mass number 12, then neutrons \(= 12 - 6 = 6\). If it has mass number 14, then neutrons \(= 14 - 6 = 8\). Both atoms are still carbon because the proton number stayed 6.

Periodic tables usually show average atomic mass, not one exact mass number. Average atomic mass is a weighted average of the naturally occurring isotopes. For GED-level problems, if a question tells you to estimate mass number from the table, round the atomic mass to the nearest whole number, then subtract the atomic number to estimate neutrons.

**Worked example.** Chlorine has atomic number 17. A neutral chlorine atom has 17 protons and 17 electrons. If the problem gives chlorine-35, it has \(35 - 17 = 18\) neutrons.
""",
        r"""
[[figure:periodic_table_guide|A simplified periodic table guide: use atomic number for protons, read groups as columns, and use rounded atomic mass to estimate neutrons.]]

**Deep explanation.** A periodic-table box is a compact data card. The atomic number is usually the whole number at the top; it tells the number of protons. The large letter or letters are the chemical symbol. The element name may be written below the symbol. The decimal number is the average atomic mass; GED questions may ask you to round it when estimating mass number.

**How to use it step by step.**
1. Find the element box named in the question.
2. Read the atomic number. That is the proton count.
3. For a neutral atom, set electrons equal to protons.
4. If you need neutrons, round the atomic mass to a whole number and subtract protons.
5. Use the element's column, or group, to infer similar chemical behavior.

Rows are periods, and columns are groups. Metals are mostly left and center. Nonmetals are mostly on the right. Metalloids sit near the stair-step boundary and have mixed properties. GED questions usually use these patterns for broad classification, not advanced memorization.
""",
        r"""
**Deep explanation.** Chemical formulas use symbols and subscripts to show what is bonded. In \(H_2O\), the subscript 2 applies only to hydrogen, so one water molecule has 2 hydrogen atoms and 1 oxygen atom. In \(CO_2\), one carbon atom is bonded with 2 oxygen atoms. If there is no subscript, read it as 1.

A molecule can be made of the same element or different elements. \(O_2\) is a molecule because two oxygen atoms are bonded, but it is not a compound because it contains only oxygen. \(CO_2\) is both a molecule and a compound because it contains carbon and oxygen chemically bonded in a fixed ratio.

**Mixture comparison.** Salt water is a mixture because salt and water are physically combined and can be separated. Water itself is a compound because hydrogen and oxygen atoms are chemically bonded in a fixed formula.
""",
        r"""
**Deep explanation.** Ions form when electrons move. If an atom loses electrons, it has more protons than electrons and becomes positively charged. If it gains electrons, it has more electrons than protons and becomes negatively charged. The nucleus does not usually change in ordinary chemical bonding; the atom's electron arrangement changes.

Ionic bonds often form between metals and nonmetals because one atom transfers electrons and opposite ions attract. Covalent bonds often form between nonmetals because atoms share electrons. GED questions usually ask for the big pattern rather than detailed electron diagrams.

**Data routine.** For charge questions, compare protons and electrons. Example: an atom has 12 protons and 10 electrons. It has two more positive charges than negative charges, so its charge is \(2+\). If it has 17 protons and 18 electrons, it has one extra electron, so its charge is \(1-\).
""",
    ],
    "ged-chemical-reactions-conservation": [
        r"""
**Deep explanation.** A chemical equation is a sentence written with formulas. Reactants are on the left because they are present before the reaction. Products are on the right because they form after the reaction. The arrow means "reacts to form," so it shows the direction of change.

Subscripts and coefficients carry different meanings. A subscript is part of a chemical formula, such as the 2 in \(H_2O\), and tells how many atoms are in one unit of the substance. A coefficient is placed in front of a formula, such as the 2 in \(2H_2O\), and tells how many units of that substance are involved. \(2H_2O\) means two water molecules, for a total of 4 hydrogen atoms and 2 oxygen atoms.

**How GED asks it.** If a question asks which substances are products, look to the right of the arrow. If it asks which substances are reactants, look to the left. If it asks how many atoms are present, multiply coefficients by subscripts.
""",
        r"""
**Deep explanation.** Conservation of mass depends on tracking atoms, not just what you can see. When wood burns, solid material seems to disappear, but many atoms become gases such as carbon dioxide and water vapor. In an open system, those gases can escape, so the remaining ash weighs less. In a closed system, the gases stay inside, so total mass is conserved and measurable.

This law is why balanced equations matter. If the reactant side has 2 carbon atoms, the product side must also have 2 carbon atoms. The atoms can be rearranged into different molecules, but the number of each type of atom cannot change in an ordinary chemical reaction.

**Worked example.** In a sealed flask, \(5\text{ g}\) of substance A reacts with \(7\text{ g}\) of substance B. If they react completely, the total mass of products is \(12\text{ g}\). If the measured product mass is less in an open container, escaped gas is a likely explanation.
""",
        r"""
**Deep explanation.** Balancing is an atom-counting process. Start by listing each element on both sides. Count atoms using subscripts. Then add or adjust coefficients to make the counts match. Never change a subscript to balance an equation because that would change the identity of the substance.

For \(H_2 + O_2 \rightarrow H_2O\), oxygen is unbalanced: the left has 2 oxygen atoms, but the right has 1. Put a 2 before \(H_2O\), giving \(2H_2O\), so the right side has 2 oxygen atoms. Now hydrogen on the right is 4, so put a 2 before \(H_2\). The balanced equation is \(2H_2 + O_2 \rightarrow 2H_2O\).

**GED routine.** Balance one element at a time, save hydrogen and oxygen for later when possible, and re-count after every coefficient change. The final check is simple: each element must have equal atom counts on both sides.
""",
        r"""
**Deep explanation.** Evidence of a chemical reaction is strongest when several observations point to a new substance. Temperature change can suggest energy release or absorption. Color change can suggest new products. Bubbles can indicate a gas forming. A precipitate is a solid that forms when two solutions react. Light, odor change, or a hard-to-reverse change can also be clues.

However, one clue by itself can be misleading. Boiling water makes bubbles, but it is a physical change because the bubbles are water vapor. Melting wax changes state, but the wax is still wax. Dissolving salt changes how the salt is distributed, but the salt can be recovered by evaporating the water.

**How GED asks it.** Read the exact situation. "Gas forms when two clear liquids are mixed" points toward a chemical reaction. "Bubbles appear as water is heated" points toward boiling, a physical change.
""",
        r"""
**Deep explanation.** Acids and bases are often tested through pH data. The pH scale usually runs from 0 to 14. A pH below 7 is acidic, a pH of 7 is neutral, and a pH above 7 is basic. Stronger acids have lower pH values; stronger bases have higher pH values.

Neutralization happens when an acid and base react to form products that are closer to neutral, often including water and a salt. The GED does not usually require advanced acid-base equations, but it may ask you to interpret a table showing pH before and after substances are mixed.

**Data routine.** First identify whether each substance is acid, base, or neutral. Then compare changes. If pH moves from 2 toward 7 after adding a base, the solution became less acidic. If pH moves from 12 toward 7 after adding an acid, the solution became less basic.
""",
    ],
    "ged-energy-forms-transformations": [
        r"""
**Deep explanation.** Energy is the ability to cause change, and it appears in many forms. Chemical energy is stored in fuels, food, and batteries. Electrical energy moves through circuits. Thermal energy is related to particle motion. Light energy travels as electromagnetic waves. Mechanical energy is associated with motion and position.

Energy is useful because it can transfer or transform. When a lamp turns on, chemical energy in a battery may become electrical energy in a circuit, then light and thermal energy in the bulb. When your body moves, chemical energy from food becomes motion and heat.

**GED routine.** Ask what is changing. If something starts moving, kinetic energy increased. If something gets warmer, thermal energy increased. If a battery or fuel is used, chemical energy is being transformed.
""",
        r"""
**Deep explanation.** Kinetic energy is energy of motion. A moving car, flowing water, and a thrown ball all have kinetic energy. The faster an object moves and the more mass it has, the more kinetic energy it has. GED questions may not require the full formula, but they often expect the relationship: more speed means more kinetic energy.

Potential energy is stored energy due to position, shape, or chemical arrangement. A book on a shelf has gravitational potential energy because it can fall. A stretched rubber band has elastic potential energy because it can snap back. Fuel has chemical potential energy because chemical bonds can rearrange and release energy.

**Worked example.** A roller coaster at the top of a hill has high gravitational potential energy. As it rolls downhill, potential energy decreases while kinetic energy increases. Some energy also becomes heat and sound because of friction.
""",
        r"""
**Deep explanation.** Energy transformations rarely produce only one output. A toaster changes electrical energy into thermal energy, but it may also produce light. A car engine changes chemical energy in fuel into motion, but much of the energy becomes heat and sound. A solar panel changes light energy into electrical energy.

The total energy is conserved, but the useful form may change. This is why devices can feel inefficient: energy has not disappeared, but some of it has spread into forms that are less useful for the intended task.

**How GED asks it.** Look at the starting source and the final effect. Battery -> current -> motor motion is chemical to electrical to mechanical. Food -> muscles -> running is chemical to mechanical plus thermal. Sunlight -> plant sugar is light to chemical.
""",
        r"""
**Deep explanation.** Conservation of energy means energy cannot be created or destroyed in an isolated system. It can move from object to object and change form. Efficiency measures how much input energy becomes the useful output energy you wanted.

Efficiency is always less than 100 percent for real machines because friction, air resistance, electrical resistance, and sound carry energy away from the useful output. A light bulb may use electrical energy, but only part becomes visible light; the rest becomes thermal energy.

**Formula routine.** Use \(\text{efficiency} = \frac{\text{useful output energy}}{\text{input energy}} \times 100\%\). If a machine uses \(200\text{ J}\) and produces \(150\text{ J}\) of useful work, efficiency is \(150/200 \times 100\% = 75\%\). If an answer is above 100 percent for a real device, recheck the calculation.
""",
        r"""
**Deep explanation.** Heat is thermal energy transferred because of a temperature difference. Temperature measures the average kinetic energy of particles, while thermal energy depends on both temperature and the amount of matter. A bathtub of warm water can contain more thermal energy than a small cup of hotter water because there is much more matter.

Heat transfers in three main ways. Conduction is direct contact, such as a spoon warming in hot soup. Convection is movement of warmer and cooler fluids, such as boiling water circulating in a pot. Radiation is energy transfer by electromagnetic waves, such as sunlight warming your skin.

**Reading energy data.** Check labels and units first. If a table lists temperature over time, identify which object warmed or cooled faster. If a graph flattens during heating, a phase change may be using energy without raising temperature.
""",
    ],
    "ged-forces-motion": [
        r"""
**Deep explanation.** A force is a vector, meaning it has both size and direction. Net force is the overall force after all pushes and pulls are combined. If two equal forces pull in opposite directions, they cancel. If one force is larger, the object accelerates in the direction of the larger force.

Balanced forces do not always mean an object is sitting still. They mean the object's motion is not changing. A book at rest on a table has balanced forces. A hockey puck sliding at constant velocity on nearly frictionless ice also has balanced forces because its speed and direction stay constant.

**GED routine.** Draw arrows mentally or on scratch paper. Add forces in the same direction. Subtract forces in opposite directions. If the net force is zero, motion stays the same. If the net force is not zero, velocity changes.
""",
        r"""
**Deep explanation.** Newton's First Law says an object keeps its state of motion unless acted on by a net external force. This property is inertia. Objects at rest tend to stay at rest; moving objects tend to keep moving in a straight line at constant speed.

Mass affects inertia. A bowling ball has more inertia than a tennis ball because it has more mass, so it is harder to start, stop, or turn. Seat belts are a practical example: when a car stops suddenly, your body tends to keep moving forward, and the seat belt supplies the force needed to slow you down.

**How GED asks it.** If an answer says an object changes motion "by itself," be suspicious. Look for the outside force: friction, gravity, a push, a pull, air resistance, or tension.
""",
        r"""
**Deep explanation.** Newton's Second Law connects force, mass, and acceleration: \(F = ma\). More net force causes more acceleration when mass is constant. More mass causes less acceleration when the same net force is applied.

The units also tell the story. Force is measured in newtons. One newton is the force needed to accelerate \(1\text{ kg}\) at \(1\text{ m/s}^2\). If the problem gives force and mass, divide to find acceleration. If it gives mass and acceleration, multiply to find force.

**Worked examples.** A \(6\text{ kg}\) object pushed by \(18\text{ N}\) accelerates at \(18/6 = 3\text{ m/s}^2\). A \(2\text{ kg}\) object accelerating at \(5\text{ m/s}^2\) has net force \(2 \times 5 = 10\text{ N}\).
""",
        r"""
**Deep explanation.** Newton's Third Law says forces come in pairs: if object A pushes on object B, object B pushes back on object A with equal strength in the opposite direction. These forces do not cancel each other because they act on different objects. A swimmer pushes water backward; the water pushes the swimmer forward.

Gravity and friction are common forces in GED items. Gravity pulls masses together. Near Earth's surface, ignoring air resistance, falling objects accelerate at about \(9.8\text{ m/s}^2\). Friction resists sliding or rolling motion and often changes mechanical energy into thermal energy.

**Careful distinction.** The normal force from a table holding up a book and the book's weight can balance on the same object. An action-reaction pair acts on two different objects, such as the book pushing down on the table and the table pushing up on the book.
""",
        r"""
**Deep explanation.** Speed tells how fast distance changes: \(\text{speed} = \frac{\text{distance}}{\text{time}}\). Velocity includes direction, so a car traveling \(40\text{ km/h}\) east has a different velocity from a car traveling \(40\text{ km/h}\) west. Acceleration means velocity changes, so speeding up, slowing down, and turning all count.

Graphs are a major GED skill. On a distance-time graph, slope represents speed. A steeper line means faster motion, and a flat line means no change in distance. On a speed-time graph, a rising line means speeding up, a falling line means slowing down, and a flat line means constant speed.

**Data routine.** Read the axes before interpreting the shape. Distance-time and speed-time graphs look similar but mean different things. Ask, "What is on the y-axis?" before deciding whether slope means speed or acceleration.
""",
    ],
    "ged-work-power-simple-machines": [
        r"""
**Deep explanation.** Scientific work is not the same as everyday effort. Work requires force and displacement in the direction of the force. If you push a wall and it does not move, you may get tired, but the work done on the wall is \(0\text{ J}\) because distance is zero. If you lift a box upward, your upward force and the box's upward motion are in the same direction, so work is done.

Units help you choose the formula. Force is in newtons, distance is in meters, and work is in joules. One joule equals one newton-meter. If a \(30\text{ N}\) force moves an object \(2\text{ m}\), the work is \(60\text{ J}\).

**GED routine.** Identify the force, identify the distance moved in the force's direction, then multiply. If the object does not move, work is zero. If the force is not in the direction of motion, only the force component in that direction does work.
""",
        r"""
**Deep explanation.** Power adds time to the work idea. Two machines may do the same \(600\text{ J}\) of work, but the one that does it in less time has greater power. This is why power is a rate, similar to speed being a rate of distance over time.

A watt is one joule per second. If \(120\text{ J}\) of work is done in \(6\text{ s}\), power is \(120/6 = 20\text{ W}\). If the same work is done in \(3\text{ s}\), power is \(40\text{ W}\), even though the total work stayed the same.

**How GED asks it.** If the question says "how fast work is done," choose power. If it gives force and distance, use work first. If it gives work and time, divide to find power.
""",
        r"""
**Deep explanation.** A simple machine helps by changing force, distance, or direction. A lever can let a small input force lift a heavier load if the input force moves through a larger distance. A pulley can change the direction of a pull, making it easier to use body weight or a more convenient motion. A ramp spreads lifting over a longer distance so less force is needed.

Mechanical advantage compares output force to input force. A machine with mechanical advantage greater than 1 multiplies force, but it does not multiply energy. The trade-off is distance: the input side usually moves farther than the output side.

**Key idea.** Machines make tasks easier; they do not make energy for free. In an ideal machine, input work equals output work. In a real machine, output work is lower because friction and other losses convert some energy to heat and sound.
""",
        r"""
**Deep explanation.** Ramps, levers, and pulleys all show the same trade-off. A ramp reduces the force needed to lift an object, but the object must be pushed a longer distance. A lever uses a fulcrum; moving the fulcrum changes how much force is needed and how far the effort side must move. Pulley systems with multiple supporting rope segments can reduce the input force, but the rope must be pulled farther.

For a ramp, a longer and less steep ramp generally needs less force than a shorter, steeper ramp for the same height. The height determines the useful output work, while ramp length affects the input force.

**GED data routine.** When comparing machines, do not assume the shortest path is easiest. Look for force and distance together. Less force usually comes with more distance.
""",
        r"""
**Deep explanation.** Efficiency measures how much of the input work becomes useful output work. Real machines are never perfectly efficient because friction, deformation, sound, and heat take away some useful energy. The "lost" energy is not destroyed; it is transformed into less useful forms.

Use the formula carefully: \(\text{efficiency} = \frac{\text{useful output work}}{\text{input work}} \times 100\%\). If useful output is \(180\text{ J}\) and input is \(240\text{ J}\), efficiency is \(180/240 \times 100\% = 75\%\). The remaining \(25\%\) became less useful energy forms.

**Checking answers.** Output work should not be greater than input work for a real machine. An efficiency of 125 percent usually means the numerator and denominator were reversed or the wrong numbers were used.
""",
    ],
    "ged-waves-energy-data": [
        r"""
**Deep explanation.** Waves transfer energy without usually carrying matter from start to finish. In a water wave, a floating object mostly moves up and down as the wave passes; it does not travel across the whole lake with the wave. In sound, air particles vibrate back and forth while the sound energy moves outward.

Some waves need a medium, which is the matter the wave travels through. Sound needs air, water, or another material. Water waves need water. Light is different because it is electromagnetic and can travel through empty space.

**How GED asks it.** If a question asks what waves carry, the best answer is energy. If it asks what the medium does, the medium vibrates or is disturbed as the energy passes through.
""",
        r"""
**Deep explanation.** Wave diagrams can look busy, but the labels are predictable. The rest position is the middle line. A crest is the highest point, and a trough is the lowest point. Amplitude is measured from the rest position to a crest or trough, not from crest to trough. Wavelength is one full cycle, such as crest to crest or trough to trough.

Amplitude relates to energy. For sound, greater amplitude usually means louder sound. For light, greater amplitude is related to intensity or brightness. Wavelength relates to the type of wave or color for light and is paired with frequency through the wave equation.

**Measurement routine.** Use matching points for wavelength. Crest to next crest works. Trough to next trough works. Rest position crossing to the next identical rest-position crossing also works, but only if the direction of crossing is the same.
""",
        r"""
**Deep explanation.** Frequency is the number of wave cycles passing a point each second. It is measured in hertz, where \(1\text{ Hz}\) means one cycle per second. Wavelength is the length of one cycle. Wave speed connects them: \(v = f\lambda\).

For a wave moving at a fixed speed, frequency and wavelength move in opposite directions. If frequency increases, more cycles must fit into the same distance per second, so wavelength decreases. If wavelength increases, fewer cycles pass each second, so frequency decreases.

**Worked example.** A wave has frequency \(4\text{ Hz}\) and wavelength \(3\text{ m}\). Its speed is \(v = 4 \times 3 = 12\text{ m/s}\). If speed is \(20\text{ m/s}\) and frequency is \(5\text{ Hz}\), wavelength is \(20/5 = 4\text{ m}\).
""",
        r"""
**Deep explanation.** In a transverse wave, the vibration is at right angles to the direction the wave travels. A rope wave moving horizontally while the rope moves up and down is a good model. In a longitudinal wave, particles vibrate parallel to the direction the wave travels. Sound in air is longitudinal because air particles compress and spread out along the path of travel.

Sound and light also differ in whether they need matter. Sound needs a medium, so it cannot travel through a vacuum. Light is electromagnetic, so it can travel through empty space from the Sun to Earth. Light also travels much faster than sound, which is why lightning is seen before thunder is heard.

**GED routine.** Match the behavior to the wave type. Perpendicular vibration points to transverse. Compression and rarefaction point to longitudinal. Vacuum travel points to light, not sound.
""",
        r"""
**Deep explanation.** Wave-data questions often test graph reading more than memorization. First read the title, axis labels, and units. Then decide what each variable means. Amplitude is tied to energy, loudness, or brightness. Frequency is tied to waves per second, pitch for sound, and color for visible light. Wavelength is one cycle length.

If a graph shows two waves, compare one feature at a time. Taller wave means greater amplitude. More cycles squeezed into the same horizontal distance means shorter wavelength and higher frequency if speed is the same. Fewer cycles in the same space means longer wavelength and lower frequency.

**Worked example.** If wave A has twice as many crests as wave B across the same distance, wave A has a higher frequency and shorter wavelength. If wave B is taller, wave B has greater amplitude and usually more energy.
""",
    ],
}


def _insert_expanded_deep_dive_details():
    for data in COURSES:
        expansions = LESSON_EXPANSIONS.get(data["slug"], [])
        if not expansions:
            continue
        if len(expansions) != len(data["lessons"]):
            raise ValueError(f"Expansion count mismatch for {data['slug']}")

        enriched_lessons = []
        for (title, content), expansion in zip(data["lessons"], expansions):
            detail = expansion.strip()
            marker = "\n\n⚠️ Common misconception"
            if marker in content:
                content = content.replace(marker, f"\n\n{detail}{marker}", 1)
            else:
                content = f"{content}\n\n{detail}"
            enriched_lessons.append((title, content))
        data["lessons"] = enriched_lessons


_insert_expanded_deep_dive_details()


class Command(BaseCommand):
    help = "Create all in-depth Physical Science companion courses (Deep Dive)."

    # Topics that now have their own dedicated, full-standard seed command.
    # Their inline definitions below are superseded and skipped (kept until the
    # remaining topics are migrated out, after which COURSES can be removed).
    DEDICATED_COMMANDS = (
        "seed_ged_matter_states",
        "seed_ged_atoms_periodic_table",
        "seed_ged_chemical_reactions_conservation",
    )
    MIGRATED_SLUGS = {
        "ged-matter-states",
        "ged-atoms-periodic-table",
        "ged-chemical-reactions-conservation",
    }

    def handle(self, *args, **options):
        for command_name in self.DEDICATED_COMMANDS:
            call_command(command_name, verbosity=options.get("verbosity", 1))

        for data in COURSES:
            if data["slug"] in self.MIGRATED_SLUGS:
                continue  # already created above by its dedicated command
            Course.objects.filter(slug=data["slug"]).delete()
            course = Course.objects.create(
                title=data["title"],
                slug=data["slug"],
                program=data["program"],
                subject=data["subject"],
                description=data["description"],
            )

            for index, (title, content) in enumerate(data["lessons"], start=1):
                Lesson.objects.create(course=course, title=title, content=content.strip(), order=index)

            for item in data["mcqs"]:
                question = Question.objects.create(
                    course=course,
                    qtype="mcq",
                    text=item["text"],
                    difficulty=item["difficulty"],
                    explanation=item["explanation"],
                )
                for text, is_correct in item["choices"]:
                    Choice.objects.create(question=question, text=text, is_correct=is_correct)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Created '{course.title}' -- "
                    f"{course.lessons.count()} lessons, {course.questions.count()} questions."
                )
            )

        self.stdout.write(self.style.SUCCESS("All Physical Science deep dives seeded."))
