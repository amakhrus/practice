"""
Seed data: 'GED Science: Chemical Reactions & Conservation of Mass (Deep Dive)'.

A focused EXPANSION of Lesson 3 ("Chemical Reactions & Conservation of Mass") from
the broader 'GED Science: Physical Science' course, brought up to the full
deep-dive standard (6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. What is a chemical reaction? (reactants, products, signs)
  2. Conservation of mass.
  3. Balancing chemical equations.
  4. Types of reactions.
  5. Energy in reactions (exothermic vs. endothermic).
  6. Reaction rates, catalysts & reading data.

This course uses ALL-NEW diagrams (reactants-to-products, a conservation-of-mass
balance, a balanced-equation atom count, reaction types, exothermic/endothermic
energy diagrams, and reaction-rate factors) rather than reusing the parent
course's 'conservation_mass' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Chemistry* and *Chemistry: Atoms First*; CK-12 Physical Science.
  - Law of conservation of mass (Antoine Lavoisier).
Note: in a chemical reaction atoms are rearranged, not created or destroyed, so
the total mass of reactants equals the total mass of products (in a closed
system). Equations are balanced with coefficients, not by changing subscripts.

Run:
    python manage.py seed_ged_chemical_reactions_conservation
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Chemical Reactions & Conservation of Mass (Deep Dive)",
    "slug": "ged-chemical-reactions-conservation",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into chemical change, expanding the single 'Chemical Reactions & Conservation of "
        "Mass' lesson from the GED Physical Science course into a full mini-course. You'll learn what "
        "happens in a reaction, why mass is conserved, how to balance equations, the main types of "
        "reactions, how reactions absorb or release energy, and what makes reactions speed up. Plain "
        "language, all-new labeled diagrams, common-misconception warnings, and GED-style practice with "
        "full explanations throughout."
    ),
    "lessons": [
        (
            "1. What Is a Chemical Reaction?",
            r"In a **chemical reaction**, one or more substances change into **new substances** with different properties. The bonds between atoms **break and re-form**, rearranging the atoms into new combinations." "\n\n"
            r"[[figure:reactants_products|The starting substances (reactants) rearrange their atoms into new substances (products).]]" "\n\n"
            r"Chemists write reactions as an equation:" "\n"
            r"- The **reactants** are the starting substances (on the left)." "\n"
            r"- The **products** are the new substances formed (on the right)." "\n"
            r"- The **arrow** (→) means **'yields'** — reactants form products." "\n\n"
            r"How can you tell a chemical reaction happened? Look for the **signs**: a **color change**, **gas or bubbles** forming, a **temperature change** (or light), a **precipitate** (a solid appearing in a liquid), or a new **odor**." "\n\n"
            r"⚠️ Common misconception: atoms are **not** created or destroyed in a reaction. They are just **rearranged** — the same atoms end up in new substances." "\n\n"
            r"💡 Tip: **reactants → products.** Bonds break and re-form; watch for signs like bubbles, color change, or heat.",
        ),
        (
            "2. Conservation of Mass",
            r"Since atoms are only **rearranged** in a reaction (not created or destroyed), the **total mass** doesn't change. This is the **law of conservation of mass**: the mass of the **reactants equals** the mass of the **products**." "\n\n"
            r"[[figure:conservation_mass_balance|The same atoms are present before and after, so the mass before a reaction equals the mass after.]]" "\n\n"
            r"If **10 grams** of reactants fully react, you end up with exactly **10 grams** of products — every atom is accounted for. This holds true as long as you measure in a **closed system**, so that any **gases** produced are still counted." "\n\n"
            r"This is why a burning candle **seems** to lose mass: it isn't destroying matter, it's releasing **carbon dioxide and water vapor** into the air. Seal the same reaction in a closed container and the mass stays the **same**." "\n\n"
            r"⚠️ Common misconception: burning does **not** destroy matter. In an open container the **gases escape**, so the leftover solid weighs less — but the total mass (including the gases) is unchanged." "\n\n"
            r"💡 Tip: **mass before = mass after.** If mass seems to change, look for a gas entering or leaving.",
        ),
        (
            "3. Balancing Chemical Equations",
            r"Because atoms are conserved, a chemical equation must be **balanced** — there has to be the **same number of each kind of atom** on both sides of the arrow." "\n\n"
            r"[[figure:balancing_equation|A balanced equation has equal atom counts on both sides: 2 H2 + O2 yields 2 H2O.]]" "\n\n"
            r"You balance by adjusting the **coefficients** — the big numbers **in front** of each formula. You must **never** change the **subscripts** (the small numbers inside a formula), because that would change the substance itself." "\n\n"
            r"Take the formation of water: **2 H₂ + O₂ → 2 H₂O**. Count the atoms:" "\n"
            r"- **Hydrogen:** left = 2 × 2 = **4**; right = 2 × 2 = **4**. ✓" "\n"
            r"- **Oxygen:** left = **2**; right = 2 × 1 = **2**. ✓" "\n\n"
            r"Both sides match, so the equation is balanced — and it obeys conservation of mass." "\n\n"
            r"⚠️ Common misconception: to balance, change the **coefficients**, not the **subscripts**. Changing H₂O to H₂O₂ makes a different substance (hydrogen peroxide), not balanced water." "\n\n"
            r"💡 Tip: **count each element on both sides; adjust the coefficients** until they match.",
        ),
        (
            "4. Types of Reactions",
            r"Most reactions fit a few recognizable patterns. Knowing the common types helps you predict what happens." "\n\n"
            r"[[figure:reaction_types|Synthesis combines, decomposition breaks apart, and combustion burns a fuel in oxygen.]]" "\n\n"
            r"- **Synthesis (combination)** — two or more substances combine into **one**: **A + B → AB**." "\n"
            r"- **Decomposition** — one substance breaks down into **two or more**: **AB → A + B**." "\n"
            r"- **Combustion** — a **fuel** burns in **oxygen**, releasing energy; for a hydrocarbon fuel the products are **carbon dioxide and water**: **fuel + O₂ → CO₂ + H₂O + energy**." "\n\n"
            r"(You may also see **replacement** reactions, where atoms switch partners.) In every case, atoms are conserved and the equation can be balanced." "\n\n"
            r"⚠️ Common misconception: combustion isn't just 'fire' — it's a chemical reaction with **oxygen** that releases energy, and burning a hydrocarbon always produces **CO₂ and water**." "\n\n"
            r"💡 Tip: **synthesis = build up; decomposition = break down; combustion = burn with oxygen.**",
        ),
        (
            "5. Energy in Reactions",
            r"Every reaction involves **energy**, because breaking and forming bonds takes and releases energy. The overall result puts reactions into two groups." "\n\n"
            r"[[figure:exothermic_endothermic|Exothermic reactions release energy (products lower); endothermic reactions absorb energy (products higher).]]" "\n\n"
            r"- An **exothermic** reaction **releases** energy (usually as heat or light), so the **products have less energy** than the reactants. Examples: **burning** fuel, an instant **hand warmer**, explosions." "\n"
            r"- An **endothermic** reaction **absorbs** energy, so the **products have more energy** than the reactants. Examples: an instant **cold pack**, and **photosynthesis** (which stores the Sun's energy)." "\n\n"
            r"Reactions also need a starting push called the **activation energy** — the minimum energy to get the reaction going (like a spark to start combustion)." "\n\n"
            r"⚠️ Common misconception: don't swap the terms. **Exo**thermic = energy **exits** (released); **endo**thermic = energy goes **in** (absorbed)." "\n\n"
            r"💡 Tip: **exo = exit/release (gets warmer); endo = energy in/absorb (gets colder).**",
        ),
        (
            "6. Reaction Rates, Catalysts & Reading Data",
            r"Some reactions are fast (an explosion) and some are slow (iron rusting). The **reaction rate** is **how fast** a reaction happens, and several factors can change it." "\n\n"
            r"[[figure:reaction_rate_factors|Higher temperature, higher concentration, more surface area, and a catalyst all speed up a reaction.]]" "\n\n"
            r"A reaction goes **faster** when:" "\n"
            r"- **Temperature** is higher — particles move and collide faster." "\n"
            r"- **Concentration** is higher — more particles are present to collide." "\n"
            r"- **Surface area** is greater — breaking a solid into smaller pieces exposes more of it." "\n"
            r"- A **catalyst** is added — it **lowers the activation energy**, and it is **not used up** in the reaction (it can be reused)." "\n\n"
            r"**Reading reaction data (a GED skill).** A graph of product formed vs. time shows the rate: a **steeper** line means a **faster** reaction. Read the **axes and units**, compare the slopes, and use only what the data shows." "\n\n"
            r"⚠️ Common misconception: a **catalyst is not consumed**. It speeds up the reaction and remains afterward, ready to work again." "\n\n"
            r"💡 Tip: **heat, concentration, surface area, and catalysts** all speed reactions up — they make collisions happen more often or more easily." "\n\n"
            r"📚 Sources: OpenStax *Chemistry* / *Chemistry: Atoms First*; CK-12 Physical Science; Lavoisier's law of conservation of mass.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: what is a reaction ---
        {
            "text": r"In a chemical reaction, the starting substances are called the:",
            "difficulty": 1,
            "choices": [("Reactants", True), ("Products", False),
                        ("Catalysts", False), ("Mixtures", False)],
            "explanation": r"Reactants are the substances you start with; they react to form products.",
        },
        {
            "text": r"The new substances formed in a chemical reaction are called the:",
            "difficulty": 1,
            "choices": [("Products", True), ("Reactants", False),
                        ("Elements", False), ("Ions", False)],
            "explanation": r"Products are the new substances produced by the reaction (written on the right of the arrow).",
        },
        {
            "text": r"In a chemical equation, the arrow between reactants and products means:",
            "difficulty": 2,
            "choices": [("'Yields' (reactants form products)", True),
                        ("'Equals' a number", False),
                        ("'Mixed with'", False),
                        ("'Greater than'", False)],
            "explanation": r"The arrow is read as 'yields' or 'produces,' showing the direction of the change.",
        },
        {
            "text": r"Which of the following is a SIGN that a chemical reaction has occurred?",
            "difficulty": 2,
            "choices": [("Gas bubbles, a color change, or a temperature change", True),
                        ("The object is moved to a new shelf", False),
                        ("The object is weighed", False),
                        ("The lights are turned on", False)],
            "explanation": r"Bubbles/gas, color change, temperature/light change, a precipitate, or an odor are signs that new substances formed.",
        },
        {
            "text": ("Use the reaction diagram.\n\n"
                     "[[figure:reactants_products|Reactants rearranging into products]]\n\n"
                     "According to the diagram, during a reaction the atoms are:"),
            "difficulty": 2,
            "choices": [("Rearranged into new substances", True),
                        ("Created out of nothing", False),
                        ("Completely destroyed", False),
                        ("Turned into energy", False)],
            "explanation": r"The diagram shows the same atoms regrouping into new molecules. Pro tip: atoms are rearranged, not created or destroyed.",
        },
        # --- Lesson 2: conservation of mass ---
        {
            "text": r"The law of conservation of mass states that:",
            "difficulty": 1,
            "choices": [("Mass is not created or destroyed in a chemical reaction", True),
                        ("Mass always increases during a reaction", False),
                        ("Mass always decreases during a reaction", False),
                        ("Mass turns into energy in every reaction", False)],
            "explanation": r"Because atoms are only rearranged, the total mass of the reactants equals the total mass of the products.",
        },
        {
            "text": r"If 10 grams of reactants fully react in a sealed (closed) container, the mass of the products will be:",
            "difficulty": 2,
            "choices": [("10 grams", True), ("More than 10 grams", False),
                        ("Less than 10 grams", False), ("0 grams", False)],
            "explanation": r"Mass is conserved, so the products have the same total mass as the reactants: 10 grams.",
        },
        {
            "text": r"A candle burns and the leftover wax weighs less than before. What best explains the 'missing' mass?",
            "difficulty": 2,
            "choices": [("It left as gases (carbon dioxide and water vapor) into the air", True),
                        ("The matter was destroyed", False),
                        ("Mass turned into pure light", False),
                        ("The wax became heavier elsewhere", False)],
            "explanation": r"Burning is an open-system reaction; the gases escape into the air. Capture everything and the total mass is unchanged.",
        },
        {
            "text": ("Use the balance diagram.\n\n"
                     "[[figure:conservation_mass_balance|A balance of reactants and products]]\n\n"
                     "The balance shows that the mass before a reaction:"),
            "difficulty": 2,
            "choices": [("Equals the mass after the reaction", True),
                        ("Is always greater than the mass after", False),
                        ("Is always less than the mass after", False),
                        ("Has nothing to do with the mass after", False)],
            "explanation": r"The level balance shows equal mass on both sides, illustrating conservation of mass. Pro tip: mass before = mass after.",
        },
        {
            "text": r"Why is mass conserved in a chemical reaction?",
            "difficulty": 3,
            "choices": [("The same atoms are present before and after; they are only rearranged", True),
                        ("New atoms are created to replace lost ones", False),
                        ("Atoms are destroyed and rebuilt with equal mass", False),
                        ("Energy is converted into the missing mass", False)],
            "explanation": r"Atoms are neither created nor destroyed in a chemical reaction, so the same atoms (and same total mass) appear in the products.",
        },
        # --- Lesson 3: balancing ---
        {
            "text": r"A balanced chemical equation has:",
            "difficulty": 1,
            "choices": [("The same number of each kind of atom on both sides", True),
                        ("More atoms on the product side", False),
                        ("More atoms on the reactant side", False),
                        ("No atoms at all", False)],
            "explanation": r"Balancing reflects conservation of mass: each element has equal atom counts on both sides.",
        },
        {
            "text": r"To balance a chemical equation, you should change the:",
            "difficulty": 2,
            "choices": [("Coefficients (numbers in front of the formulas)", True),
                        ("Subscripts (small numbers inside the formulas)", False),
                        ("Element symbols", False),
                        ("Arrow direction", False)],
            "explanation": r"Coefficients change how many molecules there are. Changing a subscript would change the substance itself.",
        },
        {
            "text": ("Use the balanced equation.\n\n"
                     "[[figure:balancing_equation|2 H2 + O2 yields 2 H2O]]\n\n"
                     "In this equation, how many HYDROGEN atoms are on each side?"),
            "difficulty": 2,
            "choices": [("4", True), ("2", False), ("6", False), ("1", False)],
            "explanation": r"2 H2 is 2 x 2 = 4 hydrogen atoms on the left, and 2 H2O is also 4 hydrogen atoms on the right. Pro tip: multiply the coefficient by the subscript.",
        },
        {
            "text": r"In 2 H2 + O2 -> 2 H2O, how many OXYGEN atoms are on each side?",
            "difficulty": 2,
            "choices": [("2", True), ("1", False), ("4", False), ("3", False)],
            "explanation": r"O2 gives 2 oxygen atoms on the left, and 2 H2O gives 2 x 1 = 2 oxygen atoms on the right.",
        },
        {
            "text": r"Why must a chemical equation be balanced?",
            "difficulty": 3,
            "choices": [("To obey conservation of mass (atoms are not created or destroyed)", True),
                        ("To make the equation look shorter", False),
                        ("Because reactions add new atoms", False),
                        ("It does not actually need to be balanced", False)],
            "explanation": r"Since atoms are conserved, the equation must show the same number of each atom on both sides.",
        },
        # --- Lesson 4: reaction types ---
        {
            "text": r"A reaction in which two substances combine to form one (A + B -> AB) is called:",
            "difficulty": 1,
            "choices": [("Synthesis (combination)", True), ("Decomposition", False),
                        ("Combustion", False), ("Evaporation", False)],
            "explanation": r"Synthesis (or combination) joins substances into a single product.",
        },
        {
            "text": r"A reaction in which one substance breaks down into two or more (AB -> A + B) is called:",
            "difficulty": 1,
            "choices": [("Decomposition", True), ("Synthesis", False),
                        ("Combustion", False), ("Condensation", False)],
            "explanation": r"Decomposition splits a single compound into simpler substances.",
        },
        {
            "text": r"Burning a fuel in oxygen to produce carbon dioxide and water is an example of:",
            "difficulty": 2,
            "choices": [("Combustion", True), ("Synthesis", False),
                        ("Decomposition", False), ("Filtration", False)],
            "explanation": r"Combustion is a reaction of a fuel with oxygen that releases energy; hydrocarbons produce CO2 and water.",
        },
        {
            "text": ("Use the reaction-types diagram.\n\n"
                     "[[figure:reaction_types|Synthesis, decomposition, and combustion]]\n\n"
                     "Which type breaks ONE compound into simpler substances?"),
            "difficulty": 2,
            "choices": [("Decomposition", True), ("Synthesis", False),
                        ("Combustion", False), ("Neutralization", False)],
            "explanation": r"Decomposition is the AB -> A + B pattern, breaking a compound apart. Pro tip: 'de-' = break down.",
        },
        # --- Lesson 5: energy in reactions ---
        {
            "text": r"A reaction that RELEASES energy (often as heat or light) is called:",
            "difficulty": 1,
            "choices": [("Exothermic", True), ("Endothermic", False),
                        ("Decomposition", False), ("A catalyst", False)],
            "explanation": r"Exothermic reactions release energy, so the surroundings get warmer (think 'exit' = energy out).",
        },
        {
            "text": r"A reaction that ABSORBS energy from its surroundings is called:",
            "difficulty": 1,
            "choices": [("Endothermic", True), ("Exothermic", False),
                        ("Synthesis", False), ("Combustion", False)],
            "explanation": r"Endothermic reactions take in energy, so the surroundings get colder (think 'endo' = energy in).",
        },
        {
            "text": r"An instant hand warmer that gets hot is an example of a(n):",
            "difficulty": 2,
            "choices": [("Exothermic reaction", True), ("Endothermic reaction", False),
                        ("Decomposition only", False), ("Physical change only", False)],
            "explanation": r"It releases heat to the surroundings, which is exothermic.",
        },
        {
            "text": r"A cold pack that gets cold when activated absorbs energy. It is therefore:",
            "difficulty": 2,
            "choices": [("Endothermic", True), ("Exothermic", False),
                        ("A combustion reaction", False), ("Not a reaction at all", False)],
            "explanation": r"Absorbing energy from the surroundings (making them colder) is endothermic.",
        },
        {
            "text": ("Use the energy diagrams.\n\n"
                     "[[figure:exothermic_endothermic|Exothermic and endothermic energy diagrams]]\n\n"
                     "In an EXOTHERMIC reaction, the products have ______ energy than the reactants."),
            "difficulty": 2,
            "choices": [("Less", True), ("More", False),
                        ("Exactly the same", False), ("No", False)],
            "explanation": r"Exothermic reactions release energy, so the products end up at a lower energy than the reactants. Pro tip: energy released -> products lower.",
        },
        {
            "text": r"The minimum amount of energy needed to START a reaction is called the:",
            "difficulty": 2,
            "choices": [("Activation energy", True), ("Potential energy", False),
                        ("Conservation energy", False), ("Kinetic mass", False)],
            "explanation": r"Activation energy is the initial 'push' (like a spark) needed to get a reaction going.",
        },
        # --- Lesson 6: rates & catalysts ---
        {
            "text": r"The reaction rate measures:",
            "difficulty": 1,
            "choices": [("How fast a reaction happens", True),
                        ("How much a reaction weighs", False),
                        ("The color of the products", False),
                        ("The number of atoms created", False)],
            "explanation": r"Reaction rate is the speed of a reaction (how quickly reactants turn into products).",
        },
        {
            "text": r"Which change would generally make a reaction go FASTER?",
            "difficulty": 2,
            "choices": [("Raising the temperature", True),
                        ("Cooling the reactants", False),
                        ("Lowering the concentration", False),
                        ("Using one large chunk instead of powder", False)],
            "explanation": r"Higher temperature makes particles move and collide faster, speeding the reaction. (Higher concentration, more surface area, and catalysts also speed it up.)",
        },
        {
            "text": r"A catalyst speeds up a reaction by:",
            "difficulty": 2,
            "choices": [("Lowering the activation energy", True),
                        ("Adding more reactant atoms", False),
                        ("Increasing the mass of the products", False),
                        ("Cooling the reaction down", False)],
            "explanation": r"A catalyst provides an easier path with lower activation energy, so the reaction proceeds faster.",
        },
        {
            "text": r"After a reaction is finished, a catalyst is:",
            "difficulty": 2,
            "choices": [("Not used up; it can be reused", True),
                        ("Completely destroyed", False),
                        ("Turned into a product", False),
                        ("Always a gas", False)],
            "explanation": r"A catalyst is not consumed by the reaction, so it remains afterward and can be used again.",
        },
        {
            "text": ("Use the reaction-rate diagram.\n\n"
                     "[[figure:reaction_rate_factors|Factors that speed up a reaction]]\n\n"
                     "Breaking a solid reactant into smaller pieces speeds up the reaction because it:"),
            "difficulty": 2,
            "choices": [("Increases the surface area exposed to react", True),
                        ("Lowers the temperature", False),
                        ("Removes the reactant", False),
                        ("Destroys the atoms", False)],
            "explanation": r"Smaller pieces expose more surface area, so more particles can collide and react at once. Pro tip: more surface area -> faster.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain the law of conservation of mass. Describe why mass is conserved in a chemical reaction, how "
                "a balanced equation (such as 2 H2 + O2 -> 2 H2O) reflects this law, and why a candle appears to lose "
                "mass as it burns."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the law -- mass of reactants equals mass of products; (2) the reason -- atoms are "
                "only rearranged, not created or destroyed; (3) a balanced equation has equal atom counts on both "
                "sides (e.g., 4 H and 2 O on each side of 2 H2 + O2 -> 2 H2O); (4) a candle appears to lose mass "
                "because gases (CO2 and water vapor) escape into the air in an open system, but total mass is "
                "conserved. Deduct for saying burning destroys matter or that atoms are created."
            ),
        },
        {
            "text": (
                "Explain the difference between exothermic and endothermic reactions, giving one real example of each. "
                "Then describe at least three factors that can change how fast a reaction happens (the reaction rate) "
                "and explain how a catalyst works."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) exothermic -- releases energy, products lower in energy (e.g., burning, hand "
                "warmer); (2) endothermic -- absorbs energy, products higher in energy (e.g., cold pack, "
                "photosynthesis); (3) at least three rate factors -- higher temperature, higher concentration, greater "
                "surface area, or a catalyst; (4) a catalyst speeds the reaction by lowering the activation energy and "
                "is not used up. Deduct for swapping exothermic/endothermic or saying a catalyst is consumed."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Chemical Reactions & Conservation of Mass (Deep Dive)' course."

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
