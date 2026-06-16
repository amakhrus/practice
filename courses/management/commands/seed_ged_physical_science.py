"""
Seed data: 'GED Science: Physical Science' -- the chemistry and physics half of
the GED Science test, built comprehensively and visually.

Covers matter and its states, atoms and the periodic table, chemical reactions
and conservation of mass, energy and its forms, forces and motion (Newton's
laws), work, power and simple machines, and waves -- plus the science-reasoning
skill of reading data. Each lesson leads with intuition and a real-world hook,
includes a labeled diagram, a common-misconception warning, and a quick tip.
Practice questions mirror the GED style, including diagram- and calculation-based
items.

Run:
    python manage.py seed_ged_physical_science
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Physical Science",
    "slug": "ged-physical-science",
    "program": "GED",
    "subject": "science",
    "description": (
        "Physical Science is the chemistry-and-physics half of the GED Science test. This course "
        "takes you from the particles inside matter all the way up to the forces that move the "
        "world: states of matter, atoms and the periodic table, chemical reactions and the "
        "conservation of mass, the forms of energy, Newton's laws of motion, work and simple "
        "machines, and waves. Every topic uses plain language, labeled diagrams, and GED-style "
        "practice with full explanations."
    ),
    "lessons": [
        (
            "1. Matter and Its States",
            r"**Matter** is anything that has **mass** and takes up **space** (volume). Everything you can touch — air, water, your phone — is matter. Matter comes in three everyday **states**, and the difference is all about how its tiny particles are arranged and how fast they move." "\n\n"
            r"[[figure:states_of_matter|The same particles, packed three different ways. Heat speeds them up and spreads them out.]]" "\n\n"
            r"- **Solid** — particles are packed tightly in fixed positions, so a solid keeps its **shape and volume** (an ice cube)." "\n"
            r"- **Liquid** — particles are close but can slide past each other, so a liquid keeps its **volume** but takes the **shape** of its container (liquid water)." "\n"
            r"- **Gas** — particles are far apart and move freely, so a gas spreads to fill **any** container (water vapor / steam)." "\n\n"
            r"Adding or removing **heat** drives the **changes of state**: melting (solid→liquid), freezing (liquid→solid), boiling/evaporating (liquid→gas), and condensing (gas→liquid). These are **physical changes** — the substance is still water, just in a different form." "\n\n"
            r"A **physical change** (melting, cutting, dissolving) changes form but not the substance. A **chemical change** (burning, rusting) makes a **new** substance. " "\n\n"
            r"⚠️ Common misconception: melting ice is NOT a chemical change. It is still water — only the state changed." "\n\n"
            r"💡 Tip: heat usually moves matter 'up' the ladder solid → liquid → gas; removing heat moves it back down.",
        ),
        (
            "2. Atoms, Elements & the Periodic Table",
            r"All matter is built from **atoms**, the smallest piece of an element. An atom has a tiny, dense center called the **nucleus** and a cloud of electrons around it." "\n\n"
            r"[[figure:atom_structure|Protons and neutrons sit in the nucleus; light electrons orbit around it.]]" "\n\n"
            r"Three particles make up an atom:" "\n"
            r"- **Proton** — positive charge (+), in the nucleus. The number of protons (the **atomic number**) is what makes an element that element." "\n"
            r"- **Neutron** — no charge, in the nucleus. Adds mass." "\n"
            r"- **Electron** — negative charge (−), orbits the nucleus. Electrons are involved in bonding and electricity." "\n\n"
            r"An **element** is a substance made of just one kind of atom (oxygen, gold, carbon). The **periodic table** lists all the elements in order of atomic number. Each box shows the element's **symbol** (like O for oxygen), its **atomic number** (number of protons), and its **atomic mass**." "\n\n"
            r"When atoms join, they form a **compound** (water, H₂O, is hydrogen + oxygen). A **molecule** is two or more atoms bonded together." "\n\n"
            r"⚠️ Common misconception: the atomic number counts **protons**, not the total of all particles. Carbon is element 6 because it has 6 protons." "\n\n"
            r"💡 Tip: a neutral atom has equal numbers of protons and electrons, so the (+) and (−) charges cancel out.",
        ),
        (
            "3. Chemical Reactions & Conservation of Mass",
            r"A **chemical reaction** rearranges atoms to make new substances. We write it as an **equation**, with **reactants** (what you start with) on the left and **products** (what you make) on the right:" "\n"
            r"\[ \underbrace{2\,H_2 + O_2}_{\text{reactants}} \;\to\; \underbrace{2\,H_2O}_{\text{product}}. \]" "\n\n"
            r"The most important rule is the **Law of Conservation of Mass**: atoms are never created or destroyed in a reaction, only rearranged. So the **total mass of the reactants equals the total mass of the products**." "\n\n"
            r"[[figure:conservation_mass|Count the atoms: 4 hydrogen and 2 oxygen on each side. Nothing is lost.]]" "\n\n"
            r"That is why equations must be **balanced** — the same number of each kind of atom on both sides. In the example, the 2's make sure there are 4 H and 2 O on the left and 4 H and 2 O on the right." "\n\n"
            r"Signs a chemical reaction happened: a color change, a gas (bubbles), a solid forming, or heat/light given off (like burning)." "\n\n"
            r"⚠️ Common misconception: when wood burns and seems to 'lose' mass, no mass disappears — it leaves as gases (carbon dioxide and water vapor) plus ash. Count the escaping gas and the mass is conserved." "\n\n"
            r"💡 Tip: if a question gives the mass of the reactants and asks for the product mass (in a closed container), they are equal.",
        ),
        (
            "4. Energy and Its Forms",
            r"**Energy** is the ability to do work or cause change. It comes in many forms, and the key idea is that energy can **change from one form to another** but is never created or destroyed (the **Law of Conservation of Energy**)." "\n\n"
            r"Common forms of energy:" "\n"
            r"- **Kinetic** — energy of motion (a moving car, wind)." "\n"
            r"- **Potential** — stored energy (a ball at the top of a hill, a stretched spring)." "\n"
            r"- **Chemical** — stored in bonds (food, gasoline, batteries)." "\n"
            r"- **Thermal (heat)**, **electrical**, **light**, and **sound** energy." "\n\n"
            r"[[figure:energy_forms|A flashlight changes chemical energy (battery) into electrical, then into light and heat.]]" "\n\n"
            r"Real devices are just energy converters: a flashlight turns **chemical → electrical → light + heat**; a car engine turns **chemical → kinetic + heat**. Some energy almost always 'escapes' as waste **heat** — which is why no machine is 100% efficient." "\n\n"
            r"A falling ball is a great example: at the top it has maximum **potential** energy; as it falls, that converts into **kinetic** energy, but the total stays the same." "\n\n"
            r"⚠️ Common misconception: energy is not 'used up'. When a battery 'dies', its chemical energy has been converted into light, heat, and other forms — not destroyed." "\n\n"
            r"💡 Tip: trace energy questions as a chain of arrows, form → form, and remember some always leaves as heat.",
        ),
        (
            "5. Forces and Motion (Newton's Laws)",
            r"A **force** is a push or a pull, measured in **newtons (N)**. Forces change how things move. Sir Isaac Newton summed up motion in three laws." "\n\n"
            r"- **First Law (Inertia):** an object stays at rest, or keeps moving at a steady speed in a straight line, **unless a force acts on it**. (A book on a table won't move on its own; a seat belt stops you when the car suddenly stops.)" "\n"
            r"- **Second Law:** \( F = m \times a \). The bigger the **force**, the bigger the **acceleration**; the bigger the **mass**, the smaller the acceleration for the same force." "\n"
            r"- **Third Law:** for every action there is an **equal and opposite reaction**. (A rocket pushes gas down; the gas pushes the rocket up.)" "\n\n"
            r"[[figure:newton_second_law|The same push gives a heavy object less acceleration and a light object more.]]" "\n\n"
            r"**Acceleration** means any change in speed or direction — speeding up, slowing down, or turning. **Gravity** is the force that pulls objects toward Earth, giving everything that falls the same acceleration (about \(9.8\ \text{m/s}^2\)) when air resistance is ignored." "\n\n"
            r"With \( F = m \times a \), you can find any one value from the other two: a 10 kg cart pushed with 20 N accelerates at \( a = F/m = 20/10 = 2\ \text{m/s}^2 \)." "\n\n"
            r"⚠️ Common misconception: heavier objects do not fall faster. Ignoring air resistance, a feather and a hammer fall together — gravity gives the same acceleration." "\n\n"
            r"💡 Tip: in \( F = ma \), cover the value you want with your finger to see the formula — \( a = F/m \), \( m = F/a \).",
        ),
        (
            "6. Work, Power & Simple Machines",
            r"In science, **work** has an exact meaning: you do work only when a **force moves an object** a distance in the direction of the force:" "\n"
            r"\[ \text{Work} = \text{Force} \times \text{Distance}, \qquad W = F \times d. \]" "\n"
            r"Work is measured in **joules (J)**. Holding a heavy box still is tiring, but does **no** scientific work, because nothing moves." "\n\n"
            r"**Power** is how **fast** work is done: \( \text{Power} = \dfrac{\text{Work}}{\text{time}} \), measured in **watts (W)**. The same job done faster takes more power." "\n\n"
            r"A **simple machine** makes work easier by changing the size or direction of a force. The lever, pulley, inclined plane (ramp), wheel and axle, wedge, and screw are the six classic ones." "\n\n"
            r"[[figure:lever_machine|A lever trades distance for force: push the long arm a long way to lift a heavy load a little.]]" "\n\n"
            r"A machine does not create energy — it lets you use **less force over a longer distance** to do the same work. Pushing a load up a long ramp takes less force than lifting it straight up, but you push over a greater distance." "\n\n"
            r"⚠️ Common misconception: a machine does not reduce the total work needed. It trades force for distance — the work (force × distance) stays about the same." "\n\n"
            r"💡 Tip: 'work' needs motion. If the distance is zero, the work is zero, no matter how big the force.",
        ),
        (
            "7. Waves, Energy & Reading Science Data",
            r"A **wave** is a disturbance that carries **energy** from place to place — usually without carrying the matter along with it. Sound, light, and ripples on water are all waves." "\n\n"
            r"[[figure:wave_anatomy|The high points are crests, the low points are troughs. Wavelength and amplitude describe the wave.]]" "\n\n"
            r"The parts of a wave:" "\n"
            r"- **Crest** — the highest point; **trough** — the lowest point." "\n"
            r"- **Wavelength** — the distance from one crest to the next." "\n"
            r"- **Amplitude** — the height from the rest line to a crest; bigger amplitude means **more energy** (a louder sound, a brighter light)." "\n"
            r"- **Frequency** — how many waves pass each second, measured in **hertz (Hz)**." "\n\n"
            r"Two main kinds: **transverse** waves move up-and-down across the direction of travel (light, water ripples); **longitudinal** waves squeeze and stretch along the direction of travel (sound). Sound needs a **medium** (air, water, solid) to travel through; light can travel through empty space." "\n\n"
            r"The GED Science test is as much about **reasoning with data** as memorizing facts. For any graph or table: read the **title, axis labels, and units** first; find the **trend**; and use only what the data **shows** — correlation is not causation." "\n\n"
            r"⚠️ Common misconception: a wave does not carry the water (or air) along with it. The matter mostly bobs in place; only the **energy** moves forward." "\n\n"
            r"💡 Tip: amplitude = energy/loudness/brightness; wavelength and frequency describe the wave's size and pace.",
        ),
    ],
    "mcqs": [
        # --- Matter & states ---
        {
            "text": r"Which best defines matter?",
            "difficulty": 1,
            "choices": [("Anything that has mass and takes up space", True),
                        ("Anything that gives off heat", False),
                        ("Only solids and liquids", False),
                        ("Anything that can be seen", False)],
            "explanation": r"Matter is anything with mass and volume — solids, liquids, and gases all count, whether or not you can see them. Heat and light are forms of energy, not matter.",
        },
        {
            "text": r"In which state of matter are the particles packed tightly in fixed positions?",
            "difficulty": 1,
            "choices": [("Solid", True), ("Liquid", False), ("Gas", False), ("They are the same in all states", False)],
            "explanation": r"In a solid, particles are locked in fixed positions, so a solid keeps its shape and volume. In liquids they slide past each other; in gases they fly far apart.",
        },
        {
            "text": r"A puddle of water slowly disappears on a hot day. Which change of state has occurred?",
            "difficulty": 2,
            "choices": [("Evaporation (liquid to gas)", True), ("Condensation (gas to liquid)", False),
                        ("Freezing (liquid to solid)", False), ("Melting (solid to liquid)", False)],
            "explanation": r"Heat turns the liquid water into water vapor (a gas) that spreads into the air — evaporation. The water is not destroyed; it changed state.",
        },
        {
            "text": r"Which of the following is a CHEMICAL change, not just a physical change?",
            "difficulty": 2,
            "choices": [("Iron rusting", True), ("Ice melting", False),
                        ("Sugar dissolving in water", False), ("Tearing a sheet of paper", False)],
            "explanation": r"Rusting forms a new substance (iron oxide), so it is a chemical change. Melting, dissolving, and tearing change form only — the substance stays the same.",
        },
        # --- Atoms & periodic table ---
        {
            "text": r"Which particle in an atom carries a positive charge?",
            "difficulty": 1,
            "choices": [("Proton", True), ("Electron", False), ("Neutron", False), ("Nucleus", False)],
            "explanation": r"Protons are positive (+) and sit in the nucleus. Electrons are negative (−), and neutrons have no charge. The nucleus is the center, not a single particle.",
        },
        {
            "text": r"What does an element's atomic number tell you?",
            "difficulty": 2,
            "choices": [("The number of protons in the nucleus", True),
                        ("The total number of all particles", False),
                        ("The number of neutrons", False),
                        ("The mass of one atom in grams", False)],
            "explanation": r"The atomic number is the number of protons, which defines the element. Carbon is number 6 because every carbon atom has 6 protons.",
        },
        {
            "text": r"A neutral atom has 8 protons. How many electrons does it have?",
            "difficulty": 2,
            "choices": [("8", True), ("0", False), ("16", False), ("4", False)],
            "explanation": r"In a neutral atom the positive and negative charges balance, so the number of electrons equals the number of protons: 8.",
        },
        {
            "text": r"Water (H₂O) is made of hydrogen and oxygen atoms joined together. Water is best called a:",
            "difficulty": 2,
            "choices": [("Compound", True), ("Element", False), ("Mixture", False), ("Single atom", False)],
            "explanation": r"A compound is two or more different elements chemically bonded in a fixed ratio — here hydrogen and oxygen. An element is just one kind of atom.",
        },
        # --- Reactions & conservation of mass ---
        {
            "text": r"In a chemical equation, the substances you start with (on the left) are called the:",
            "difficulty": 1,
            "choices": [("Reactants", True), ("Products", False), ("Compounds", False), ("Solutions", False)],
            "explanation": r"Reactants are on the left and products are on the right of the arrow. The reaction turns reactants into products.",
        },
        {
            "text": r"10 g of reactants combine completely in a sealed container. What is the total mass of the products?",
            "difficulty": 2,
            "choices": [("10 g", True), ("Less than 10 g", False), ("More than 10 g", False), ("It cannot be known", False)],
            "explanation": r"By the Law of Conservation of Mass, atoms are only rearranged, so the product mass equals the reactant mass: 10 g. In a sealed container nothing can escape.",
        },
        {
            "text": r"A log burns and the ash left behind weighs much less than the log. What happened to the missing mass?",
            "difficulty": 3,
            "choices": [("It left as gases (carbon dioxide and water vapor)", True),
                        ("It was destroyed by the fire", False),
                        ("Mass is not conserved in burning", False),
                        ("It turned into pure energy", False)],
            "explanation": r"Mass is conserved. The 'missing' mass escaped as invisible gases. Counting the gases plus the ash, the total mass is unchanged.",
        },
        # --- Energy ---
        {
            "text": r"A ball held at the top of a hill has energy because of its position. This is called:",
            "difficulty": 1,
            "choices": [("Potential energy", True), ("Kinetic energy", False),
                        ("Chemical energy", False), ("Sound energy", False)],
            "explanation": r"Stored energy due to position is potential energy. As the ball rolls down, it converts to kinetic energy (energy of motion).",
        },
        {
            "text": r"When a flashlight is turned on, the main energy change is:",
            "difficulty": 2,
            "choices": [("Chemical energy to electrical energy to light (and heat)", True),
                        ("Light energy to chemical energy", False),
                        ("Kinetic energy to chemical energy", False),
                        ("Sound energy to light energy", False)],
            "explanation": r"The battery's chemical energy becomes electrical energy in the circuit, which the bulb turns into light (plus some waste heat).",
        },
        {
            "text": r"According to the Law of Conservation of Energy, when a battery 'dies', its energy has been:",
            "difficulty": 2,
            "choices": [("Converted into other forms, such as light and heat", True),
                        ("Completely destroyed", False),
                        ("Created from nothing", False),
                        ("Turned into mass", False)],
            "explanation": r"Energy is never created or destroyed, only converted. The battery's chemical energy was changed into light, heat, and other forms — not destroyed.",
        },
        # --- Forces & motion ---
        {
            "text": r"An object will stay at rest or keep moving at a constant speed unless a force acts on it. This is Newton's:",
            "difficulty": 1,
            "choices": [("First Law (inertia)", True), ("Second Law", False),
                        ("Third Law", False), ("Law of Gravity", False)],
            "explanation": r"The tendency of an object to keep doing what it is doing until a force acts is inertia — Newton's First Law.",
        },
        {
            "text": r"A net force of 20 N acts on a 5 kg cart. Using \(F = m \times a\), what is its acceleration?",
            "difficulty": 2,
            "choices": [(r"\(4\ \text{m/s}^2\)", True), (r"\(100\ \text{m/s}^2\)", False),
                        (r"\(25\ \text{m/s}^2\)", False), (r"\(15\ \text{m/s}^2\)", False)],
            "explanation": r"Rearrange to \(a = F/m = 20 \div 5 = 4\ \text{m/s}^2\). The trap 100 multiplies instead of divides; 15 subtracts.",
        },
        {
            "text": r"The same force is applied to a light cart and a heavy cart. Which accelerates more?",
            "difficulty": 2,
            "choices": [("The light cart", True), ("The heavy cart", False),
                        ("They accelerate equally", False), ("Neither moves", False)],
            "explanation": r"From \(a = F/m\), a smaller mass gives a larger acceleration for the same force. The lighter cart speeds up faster.",
        },
        {
            "text": r"A rocket pushes exhaust gas downward, and the gas pushes the rocket upward. This illustrates Newton's:",
            "difficulty": 2,
            "choices": [("Third Law (equal and opposite reaction)", True),
                        ("First Law", False),
                        ("Law of Conservation of Mass", False),
                        ("Second Law", False)],
            "explanation": r"For every action force there is an equal and opposite reaction force — the rocket pushes the gas down, the gas pushes the rocket up. That is Newton's Third Law.",
        },
        {
            "text": r"Ignoring air resistance, how do a heavy hammer and a light feather fall when dropped together?",
            "difficulty": 3,
            "choices": [("They fall together at the same rate", True),
                        ("The hammer lands much sooner", False),
                        ("The feather lands sooner", False),
                        ("Neither one accelerates", False)],
            "explanation": r"Gravity gives all objects the same acceleration regardless of mass. Without air resistance, the hammer and feather hit the ground together.",
        },
        # --- Work, power & machines ---
        {
            "text": r"In science, you do work on an object only when:",
            "difficulty": 1,
            "choices": [("A force moves the object a distance", True),
                        ("You hold the object still", False),
                        ("You think hard about it", False),
                        ("The object is heavy", False)],
            "explanation": r"Work = force × distance. If nothing moves, no work is done — holding a box still does zero scientific work, no matter how tiring.",
        },
        {
            "text": r"A force of 10 N pushes a box 3 m across the floor. How much work is done?",
            "difficulty": 2,
            "choices": [("30 J", True), ("13 J", False), ("3.3 J", False), ("10 J", False)],
            "explanation": r"\(W = F \times d = 10 \times 3 = 30\) joules. The trap 13 adds the numbers; 3.3 divides.",
        },
        {
            "text": r"How does a simple machine like a ramp make a job easier?",
            "difficulty": 2,
            "choices": [("It lets you use less force over a longer distance", True),
                        ("It reduces the total work needed", False),
                        ("It creates extra energy", False),
                        ("It removes the need for any force", False)],
            "explanation": r"A machine trades force for distance: a ramp needs less force than lifting straight up, but you push over a longer distance. The total work stays about the same — energy is never created.",
        },
        # --- Waves & data ---
        {
            "text": r"What does a wave mainly transfer from one place to another?",
            "difficulty": 1,
            "choices": [("Energy", True), ("Matter", False), ("Mass", False), ("Atoms", False)],
            "explanation": r"A wave carries energy. The matter (like water) mostly bobs in place while the energy moves forward.",
        },
        {
            "text": r"On a wave, the distance from one crest to the next crest is the:",
            "difficulty": 2,
            "choices": [("Wavelength", True), ("Amplitude", False),
                        ("Frequency", False), ("Trough", False)],
            "explanation": r"Wavelength is the distance between matching points, such as crest to crest. Amplitude is the height from the rest line to a crest.",
        },
        {
            "text": r"Two sound waves are identical except that one has a larger amplitude. The larger-amplitude wave sounds:",
            "difficulty": 2,
            "choices": [("Louder", True), ("Quieter", False),
                        ("Higher in pitch", False), ("Exactly the same", False)],
            "explanation": r"Amplitude carries the wave's energy, so a larger amplitude means a louder sound. (Pitch is set by frequency, not amplitude.)",
        },
        {
            "text": r"A graph shows that as the temperature of a gas rises, its volume also rises. The best supported conclusion is:",
            "difficulty": 3,
            "choices": [("Higher temperature is associated with greater volume in this data", True),
                        ("Volume controls the temperature of the room", False),
                        ("The data must be incorrect", False),
                        ("Temperature and volume are unrelated", False)],
            "explanation": r"State only what the data shows: the two rise together. Read the trend from the axes and avoid claiming a cause the graph does not establish.",
        },
        {
            "text": ("Use the diagram of the states of matter.\n\n"
                     "[[figure:states_of_matter|Particle arrangement in solids, liquids, and gases]]\n\n"
                     "In which state are the particles packed closely together in a fixed, orderly arrangement?"),
            "difficulty": 1,
            "choices": [("Solid", True), ("Liquid", False), ("Gas", False), ("They are identical in all three", False)],
            "explanation": r"In a solid, particles are packed tightly in fixed positions, giving it a definite shape. In a liquid they stay close but flow; in a gas they spread far apart. Pro tip: fixed shape = solid; fills its whole container = gas.",
        },
        {
            "text": ("Use the atom diagram.\n\n"
                     "[[figure:atom_structure|An atom's nucleus and electron shells]]\n\n"
                     "Where are the protons and neutrons located?"),
            "difficulty": 2,
            "choices": [("Together in the nucleus at the center", True),
                        ("Orbiting in the outer shells", False),
                        ("Spread evenly throughout the atom", False),
                        ("Outside the atom entirely", False)],
            "explanation": r"Protons and neutrons sit together in the dense central nucleus; the electrons orbit around it in shells. Pro tip: nucleus = protons + neutrons; electrons travel around it.",
        },
        {
            "text": ("Use the wave diagram.\n\n"
                     "[[figure:wave_anatomy|A wave labeled with its parts]]\n\n"
                     "What does the distance labeled wavelength measure?"),
            "difficulty": 2,
            "choices": [("The distance from one crest to the next", True),
                        ("The height of the wave from the rest line", False),
                        ("The speed at which the wave travels", False),
                        ("The number of waves passing each second", False)],
            "explanation": r"Wavelength is the length of one full cycle, such as from one crest to the next crest. The height from the rest line is the amplitude. Pro tip: wavelength = length of one cycle; amplitude = height.",
        },
    ],
    "essays": [
        {
            "text": (
                "A student claims that when a candle burns down to almost nothing, mass has been destroyed. "
                "Use the Law of Conservation of Mass to explain why the student is wrong. In your answer, "
                "describe what really happens to the atoms and where the 'missing' mass goes."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) stating that mass is conserved — atoms are rearranged, not destroyed; "
                "(2) explaining that the wax combines with oxygen and is released as gases (carbon dioxide and "
                "water vapor); (3) concluding that the mass of wax + oxygen used equals the mass of gases + any "
                "remaining material. Deduct for implying mass or atoms disappear."
            ),
        },
        {
            "text": (
                "Describe the energy changes that happen when a roller coaster car is released from the top of "
                "the first big hill and rolls down to the bottom. Use the terms potential energy, kinetic energy, "
                "and conservation of energy, and explain why some energy is 'lost' to the surroundings."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) maximum potential energy at the top due to height; (2) potential energy "
                "converting to kinetic energy as the car speeds up going down; (3) total energy conserved; "
                "(4) some energy converted to heat/sound by friction and air resistance, so it is transformed, "
                "not destroyed. Deduct for reversing potential/kinetic or claiming energy is destroyed."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'GED Science: Physical Science' course."

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
