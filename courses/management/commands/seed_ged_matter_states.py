"""
Seed data: 'GED Science: Matter and Its States (Deep Dive)'.

A focused EXPANSION of Lesson 1 ("Matter and Its States") from the broader
'GED Science: Physical Science' course, brought up to the full deep-dive standard
(6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. Matter & the three states (mass, volume, particle model).
  2. Changes of state.
  3. Heating & cooling curves.
  4. Density.
  5. Physical vs. chemical changes.
  6. Mixtures, solutions & reading matter data.

This course uses ALL-NEW diagrams (the particle model, a changes-of-state
diagram, a heating curve, a density comparison, physical vs. chemical change,
and mixtures/solutions) rather than reusing the parent course's 'states_of_matter'
figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Chemistry* and *Chemistry: Atoms First*; CK-12 Physical Science.
  - National Institute of Standards and Technology (NIST) reference data.
Note: changes of state are physical changes -- the substance stays the same.
During melting or boiling, temperature stays constant while heat breaks bonds.
Density = mass / volume; an object floats if it is less dense than the fluid.

Run:
    python manage.py seed_ged_matter_states
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Matter and Its States (Deep Dive)",
    "slug": "ged-matter-states",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into matter, expanding the single 'Matter and Its States' lesson from the GED "
        "Physical Science course into a full mini-course. You'll use the particle model to understand "
        "solids, liquids, and gases, follow how matter changes state, read heating curves, calculate and "
        "compare density, tell physical changes from chemical changes, and learn about mixtures and "
        "solutions. Plain language, all-new labeled diagrams, common-misconception warnings, and "
        "GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. Matter & the Three States",
            r"**Matter** is anything that has **mass** and takes up **space** (volume). Mass is how much material is present; volume is how much space it fills. Even invisible **air** is matter, because it has mass and volume — energy like light, heat, and sound is **not** matter." "\n\n"
            r"[[figure:particle_model|All matter is made of tiny particles. Their spacing and energy decide whether it's a solid, liquid, or gas.]]" "\n\n"
            r"All matter is made of tiny moving **particles**, and how those particles are arranged gives the three common **states**:" "\n"
            r"- **Solid** — particles are packed closely in **fixed positions** and only vibrate. A solid keeps both its **shape and volume**." "\n"
            r"- **Liquid** — particles are still close but can **slide past** each other. A liquid keeps its **volume** but takes the **shape** of its container." "\n"
            r"- **Gas** — particles are **far apart** and move **fast**, so a gas **fills its container** — it has no fixed shape or volume and can be squeezed (compressed)." "\n\n"
            r"⚠️ Common misconception: the particles in a solid are not frozen perfectly still — they **vibrate** in place; they just can't move past one another. And invisible air **is** matter." "\n\n"
            r"💡 Tip: **solid = shape + volume; liquid = volume only; gas = neither (fills the container).**",
        ),
        (
            "2. Changes of State",
            r"When you heat or cool matter, it can change from one state to another. Each change has a name, and the **same substance** stays the same throughout — only its **state** changes." "\n\n"
            r"[[figure:phase_change_diagram|Adding energy moves matter toward gas; removing energy moves it toward solid.]]" "\n\n"
            r"The changes of state are:" "\n"
            r"- **Melting** — solid → liquid (ice → water)." "\n"
            r"- **Freezing** — liquid → solid (water → ice)." "\n"
            r"- **Evaporation / boiling** — liquid → gas (water → water vapor)." "\n"
            r"- **Condensation** — gas → liquid (water vapor → water)." "\n"
            r"- **Sublimation** — solid → gas directly (dry ice → CO₂ gas)." "\n"
            r"- **Deposition** — gas → solid directly (water vapor → frost)." "\n\n"
            r"**Adding** energy (heat) pushes matter **toward gas**; **removing** energy pushes it **toward solid**. Because it's still the same substance, changes of state are **physical changes** — melt the water again and it's still water." "\n\n"
            r"⚠️ Common misconception: melting or boiling does **not** make a new substance. Ice, liquid water, and steam are **all water** — just in different states." "\n\n"
            r"💡 Tip: **add heat → toward gas (melt, evaporate); remove heat → toward solid (condense, freeze).**",
        ),
        (
            "3. Heating & Cooling Curves",
            r"Heat a solid steadily and something surprising happens to its temperature. It rises — but then **pauses** while the substance changes state, even though you keep adding heat." "\n\n"
            r"[[figure:heating_curve|Temperature rises, then stays flat during melting and boiling, then rises again.]]" "\n\n"
            r"On a **heating curve** (temperature vs. heat added):" "\n"
            r"- The **slanted** parts are where the temperature **rises** (the solid, liquid, or gas warming up)." "\n"
            r"- The **flat (horizontal)** parts are where the substance is **changing state** (melting or boiling). The temperature **stays constant** because the added energy is breaking the bonds between particles instead of speeding them up." "\n\n"
            r"The temperature where a solid melts is its **melting point**; where a liquid boils is its **boiling point**. For water these are 0°C and 100°C." "\n\n"
            r"⚠️ Common misconception: temperature does **not** keep climbing while ice melts or water boils. It **plateaus** until the change of state is complete." "\n\n"
            r"💡 Tip: the **flat parts** of a heating curve are **changes of state**; the **slanted parts** are warming.",
        ),
        (
            "4. Density",
            r"Why does a small steel bolt sink while a huge log floats? The answer is **density** — how much **mass** is packed into a given **volume**." "\n\n"
            r"[[figure:density_compare|Density compares mass in the same volume; less dense objects float and denser ones sink.]]" "\n\n"
            r"**Density = mass ÷ volume.** If two objects are the **same size** (volume) but one has **more mass**, that one is **denser**. Density is a property of the material itself — a small piece and a large piece of the same metal have the **same** density." "\n\n"
            r"Density decides floating and sinking: an object **less dense** than the liquid **floats**, and one **more dense sinks**. That's why a cork floats on water and a rock sinks." "\n\n"
            r"⚠️ Common misconception: 'heavy things always sink.' What matters is **density**, not weight. A massive steel **ship** floats because its shape makes its **overall (average) density** less than water." "\n\n"
            r"💡 Tip: **density = mass ÷ volume.** Less dense than the liquid → floats; more dense → sinks.",
        ),
        (
            "5. Physical vs. Chemical Changes",
            r"Matter can change in two very different ways, and telling them apart is a favorite GED topic." "\n\n"
            r"[[figure:physical_vs_chemical|A physical change keeps the same substance; a chemical change makes a new one.]]" "\n\n"
            r"- A **physical change** changes the **form** of matter but **not** what it is. Melting ice, cutting paper, bending a wire, and **dissolving** sugar in water are physical changes — you still have the same substance, and they're usually easy to reverse." "\n"
            r"- A **chemical change** forms a **new substance** with new properties. Burning wood, **rusting** iron, baking a cake, and digesting food are chemical changes." "\n\n"
            r"**Signs of a chemical change** include a **color change**, **gas or bubbles** forming, **light or heat** being given off, an **odor**, or a solid (precipitate) appearing — and it's usually **hard to reverse**." "\n\n"
            r"⚠️ Common misconception: **dissolving** sugar is a **physical** change — the sugar is still sugar, just spread through the water. **Burning** sugar is a **chemical** change, because new substances form." "\n\n"
            r"💡 Tip: ask **'did a NEW substance form?'** If yes → **chemical**; if it's the same substance in a new form → **physical**.",
        ),
        (
            "6. Mixtures, Solutions & Reading Matter Data",
            r"Most everyday matter isn't pure — it's **mixed**. A **mixture** is two or more substances **physically combined** (not chemically), so each keeps its own properties and the mixture can be **separated by physical means**." "\n\n"
            r"[[figure:mixtures_solutions|A heterogeneous mixture has visible parts; a solution is uniform; mixtures can be separated physically.]]" "\n\n"
            r"- A **heterogeneous** mixture has **visibly different** parts (a salad, sand in water)." "\n"
            r"- A **homogeneous** mixture is **uniform** throughout. A **solution** (like **salt water**) is a homogeneous mixture where one substance is **dissolved** in another (solute dissolved in solvent)." "\n\n"
            r"Because the parts keep their properties, mixtures can be **separated**: **filtration** traps an undissolved solid (sand from water), while **evaporation** leaves behind a **dissolved** solid (salt from salt water)." "\n\n"
            r"**Reading matter data (a GED skill).** Tables may list properties like **density**, **melting point**, or **boiling point**. Read the **headings and units**, then compare values — for example, a substance with a higher density than water will sink." "\n\n"
            r"⚠️ Common misconception: a **solution** is still a **mixture** — the dissolved substance hasn't chemically changed and can be recovered (e.g., by evaporation)." "\n\n"
            r"💡 Tip: **mixtures can be separated by physical means**; a **solution** is a uniform mixture (dissolved, but still a mixture)." "\n\n"
            r"📚 Sources: OpenStax *Chemistry* / *Chemistry: Atoms First*; CK-12 Physical Science; NIST reference data.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: matter & states ---
        {
            "text": r"Matter is anything that:",
            "difficulty": 1,
            "choices": [("Has mass and takes up space", True),
                        ("Can be seen with the eyes", False),
                        ("Gives off light", False),
                        ("Is always solid", False)],
            "explanation": r"Matter is defined by having mass and volume. (Air is matter even though it is invisible.)",
        },
        {
            "text": r"Which of the following is matter?",
            "difficulty": 2,
            "choices": [("Air", True), ("Light", False),
                        ("Heat", False), ("Sound", False)],
            "explanation": r"Air has mass and takes up space, so it is matter. Light, heat, and sound are forms of energy, not matter.",
        },
        {
            "text": r"In which state of matter do the particles fill the entire container?",
            "difficulty": 1,
            "choices": [("Gas", True), ("Solid", False),
                        ("Liquid", False), ("None of them", False)],
            "explanation": r"Gas particles spread far apart and move fast, so a gas expands to fill whatever container it is in.",
        },
        {
            "text": r"A liquid:",
            "difficulty": 2,
            "choices": [("Keeps its volume but takes the shape of its container", True),
                        ("Keeps both its shape and volume", False),
                        ("Has no volume", False),
                        ("Always fills any container completely", False)],
            "explanation": r"In a liquid, particles stay close (fixed volume) but slide past each other, so it takes the container's shape.",
        },
        {
            "text": ("Use the particle diagram.\n\n"
                     "[[figure:particle_model|Particles in solids, liquids, and gases]]\n\n"
                     "According to the diagram, in a SOLID the particles are:"),
            "difficulty": 2,
            "choices": [("Packed closely in fixed positions (vibrating)", True),
                        ("Far apart and moving fast", False),
                        ("Spread evenly to fill the container", False),
                        ("Not present at all", False)],
            "explanation": r"The diagram shows solid particles tightly packed and fixed in place, only vibrating. Pro tip: solid = fixed positions, gas = far apart.",
        },
        # --- Lesson 2: changes of state ---
        {
            "text": r"The change of state from a solid to a liquid is called:",
            "difficulty": 1,
            "choices": [("Melting", True), ("Freezing", False),
                        ("Condensation", False), ("Evaporation", False)],
            "explanation": r"Melting is solid to liquid (ice to water). Freezing is the reverse.",
        },
        {
            "text": r"The change of state from a gas to a liquid is called:",
            "difficulty": 1,
            "choices": [("Condensation", True), ("Evaporation", False),
                        ("Sublimation", False), ("Melting", False)],
            "explanation": r"Condensation is gas to liquid (water vapor forming droplets). Evaporation is the reverse.",
        },
        {
            "text": r"Adding heat energy to matter generally moves it:",
            "difficulty": 2,
            "choices": [("Toward the gas state", True),
                        ("Toward the solid state", False),
                        ("Toward becoming a new substance", False),
                        ("Toward having less mass", False)],
            "explanation": r"Heat speeds up particles and spreads them out, so adding energy moves matter from solid toward liquid toward gas.",
        },
        {
            "text": r"Dry ice (solid carbon dioxide) turns directly into a gas without becoming a liquid. This change is called:",
            "difficulty": 2,
            "choices": [("Sublimation", True), ("Melting", False),
                        ("Condensation", False), ("Freezing", False)],
            "explanation": r"Sublimation is the change directly from solid to gas. (Gas directly to solid is deposition.)",
        },
        {
            "text": ("Use the changes-of-state diagram.\n\n"
                     "[[figure:phase_change_diagram|Changes of state]]\n\n"
                     "According to the diagram, freezing is the change from:"),
            "difficulty": 2,
            "choices": [("Liquid to solid", True), ("Solid to liquid", False),
                        ("Liquid to gas", False), ("Gas to solid", False)],
            "explanation": r"The diagram shows freezing as liquid turning into solid (removing energy). Pro tip: freezing and condensation both release energy.",
        },
        {
            "text": r"When ice melts into liquid water, the substance:",
            "difficulty": 2,
            "choices": [("Stays the same (it is still water)", True),
                        ("Becomes a brand-new substance", False),
                        ("Loses all of its mass", False),
                        ("Turns into a gas immediately", False)],
            "explanation": r"Melting is a physical change. Ice and liquid water are the same substance (water) in different states.",
        },
        # --- Lesson 3: heating curves ---
        {
            "text": ("Use the heating curve.\n\n"
                     "[[figure:heating_curve|Temperature versus heat added]]\n\n"
                     "On the heating curve, the FLAT (horizontal) parts represent:"),
            "difficulty": 2,
            "choices": [("A change of state (melting or boiling)", True),
                        ("The substance getting colder", False),
                        ("The substance disappearing", False),
                        ("A chemical reaction", False)],
            "explanation": r"During a state change, added heat breaks bonds rather than raising temperature, so the curve is flat. Pro tip: flat = changing state.",
        },
        {
            "text": r"While ice is melting, its temperature:",
            "difficulty": 2,
            "choices": [("Stays the same until all the ice has melted", True),
                        ("Keeps rising quickly", False),
                        ("Drops below freezing", False),
                        ("Rises and falls randomly", False)],
            "explanation": r"The temperature holds steady at the melting point while the added energy converts solid to liquid.",
        },
        {
            "text": r"The temperature at which a solid turns into a liquid is called its:",
            "difficulty": 1,
            "choices": [("Melting point", True), ("Boiling point", False),
                        ("Density", False), ("Volume", False)],
            "explanation": r"The melting point is where a solid becomes a liquid (for water, 0 degrees Celsius).",
        },
        # --- Lesson 4: density ---
        {
            "text": r"Density is defined as:",
            "difficulty": 1,
            "choices": [("Mass divided by volume", True),
                        ("Volume divided by mass", False),
                        ("Mass times temperature", False),
                        ("Weight minus volume", False)],
            "explanation": r"Density = mass / volume. It measures how much matter is packed into a given space.",
        },
        {
            "text": r"An object that is LESS dense than water will:",
            "difficulty": 2,
            "choices": [("Float", True), ("Sink", False),
                        ("Dissolve", False), ("Evaporate", False)],
            "explanation": r"Objects less dense than the surrounding liquid float; objects more dense sink.",
        },
        {
            "text": r"Two cubes are exactly the same size, but cube A has more mass than cube B. Cube A is:",
            "difficulty": 2,
            "choices": [("More dense", True), ("Less dense", False),
                        ("The same density", False), ("Not matter", False)],
            "explanation": r"Same volume but more mass means more mass packed into the same space, so cube A is denser.",
        },
        {
            "text": r"A huge steel ship floats even though steel is denser than water. The best explanation is that:",
            "difficulty": 3,
            "choices": [("Its shape makes the ship's overall (average) density less than water", True),
                        ("Steel is actually less dense than water", False),
                        ("The ship has no mass", False),
                        ("Water pushes all heavy things up", False)],
            "explanation": r"A hull encloses a lot of air, so the ship's average density (mass divided by its large volume) is less than water, and it floats.",
        },
        {
            "text": ("Use the density diagram.\n\n"
                     "[[figure:density_compare|Floating and sinking]]\n\n"
                     "In the diagram, the object that SINKS is the one that is:"),
            "difficulty": 2,
            "choices": [("More dense than the water", True),
                        ("Less dense than the water", False),
                        ("Larger than the beaker", False),
                        ("Made of gas", False)],
            "explanation": r"The diagram shows the denser object sinking and the less dense object floating. Pro tip: compare the object's density to the liquid's.",
        },
        # --- Lesson 5: physical vs chemical ---
        {
            "text": r"Which of the following is a CHEMICAL change?",
            "difficulty": 1,
            "choices": [("Burning wood", True), ("Melting ice", False),
                        ("Cutting paper", False), ("Dissolving sugar in water", False)],
            "explanation": r"Burning wood forms new substances (ash, gases), so it is a chemical change. The others keep the same substance.",
        },
        {
            "text": r"Melting ice is considered a PHYSICAL change because:",
            "difficulty": 2,
            "choices": [("It is still water (no new substance forms)", True),
                        ("It creates a brand-new substance", False),
                        ("It gives off light", False),
                        ("It cannot be reversed", False)],
            "explanation": r"A physical change alters form but not identity. Melted ice is still water.",
        },
        {
            "text": r"Which of these is a SIGN that a chemical change has occurred?",
            "difficulty": 2,
            "choices": [("A new color, gas bubbles, or light/heat is produced", True),
                        ("The object simply changes shape", False),
                        ("The object is cut into pieces", False),
                        ("A solid is crushed into powder", False)],
            "explanation": r"Color change, bubbling gas, light/heat, an odor, or a precipitate are signs that new substances formed (a chemical change).",
        },
        {
            "text": r"Dissolving sugar in water is a:",
            "difficulty": 2,
            "choices": [("Physical change (it is still sugar)", True),
                        ("Chemical change (new substance forms)", False),
                        ("Change of state", False),
                        ("Nuclear change", False)],
            "explanation": r"The sugar spreads through the water but remains sugar, and it can be recovered by evaporating the water, so it is a physical change.",
        },
        {
            "text": r"Iron rusting is a chemical change because:",
            "difficulty": 3,
            "choices": [("A new substance (rust) forms with new properties", True),
                        ("The iron only changes shape", False),
                        ("The iron melts", False),
                        ("It can be easily reversed", False)],
            "explanation": r"Rust (iron oxide) is a new substance formed when iron reacts with oxygen and water, so rusting is a chemical change.",
        },
        # --- Lesson 6: mixtures, solutions, data ---
        {
            "text": r"A mixture is:",
            "difficulty": 1,
            "choices": [("Two or more substances physically combined and separable by physical means", True),
                        ("A single pure substance", False),
                        ("A substance that has chemically reacted into a new one", False),
                        ("Only found in gases", False)],
            "explanation": r"In a mixture, substances are physically (not chemically) combined, keep their properties, and can be separated physically.",
        },
        {
            "text": r"Salt water is an example of a:",
            "difficulty": 2,
            "choices": [("Solution (a homogeneous mixture)", True),
                        ("Pure substance", False),
                        ("Heterogeneous mixture", False),
                        ("Chemical compound only", False)],
            "explanation": r"Salt dissolves uniformly in water, making a homogeneous mixture called a solution.",
        },
        {
            "text": r"Which method best separates a DISSOLVED solid (like salt) from water?",
            "difficulty": 2,
            "choices": [("Evaporation", True), ("Filtration", False),
                        ("Burning", False), ("Freezing the salt", False)],
            "explanation": r"Evaporating the water leaves the dissolved salt behind. Filtration would not work because the salt passes through the filter with the water.",
        },
        {
            "text": r"Which method best separates an INSOLUBLE solid (like sand) from water?",
            "difficulty": 2,
            "choices": [("Filtration", True), ("Evaporation only", False),
                        ("Dissolving it further", False), ("A chemical reaction", False)],
            "explanation": r"Sand does not dissolve, so a filter traps the sand while the water passes through.",
        },
        {
            "text": ("Use the mixtures diagram.\n\n"
                     "[[figure:mixtures_solutions|Mixtures and how to separate them]]\n\n"
                     "A mixture in which you can SEE the different parts is described as:"),
            "difficulty": 2,
            "choices": [("Heterogeneous", True), ("Homogeneous", False),
                        ("A pure element", False), ("A compound", False)],
            "explanation": r"Heterogeneous mixtures have visibly different parts. Homogeneous mixtures (solutions) look uniform. Pro tip: 'hetero' = different/visible parts.",
        },
    ],
    "essays": [
        {
            "text": (
                "Using the particle model, explain what happens when a solid is heated until it melts and then "
                "boils. Describe what happens to the particles and the energy at each step, what happens to the "
                "temperature during melting and boiling, and explain why the substance is still the same throughout."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) in a solid, particles are packed and vibrate; adding heat makes them vibrate "
                "faster; (2) at the melting point, added energy breaks bonds so particles slide (liquid) while the "
                "temperature stays constant; (3) more heat speeds the liquid until the boiling point, where energy "
                "again goes into separating particles (gas) and temperature is constant; (4) it remains the same "
                "substance because changes of state are physical changes. Deduct for saying temperature keeps rising "
                "during melting/boiling or that a new substance forms."
            ),
        },
        {
            "text": (
                "Explain the difference between a physical change and a chemical change. Give two examples of each, "
                "and list at least three signs that a chemical change has taken place."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) a physical change alters form but keeps the same substance (e.g., melting ice, "
                "dissolving sugar); (2) a chemical change forms a new substance (e.g., burning wood, rusting iron); "
                "(3) at least three signs of a chemical change -- color change, gas/bubbles, light or heat given off, "
                "an odor, a precipitate, or being hard to reverse. Deduct for classifying dissolving or melting as "
                "chemical, or burning as physical."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Matter and Its States (Deep Dive)' course."

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
