"""
Seed data: 'GED Science: The Solar System & Earth in Space (Deep Dive)'.

A focused EXPANSION of Lesson 6 ("The Solar System & Earth in Space") from the
broader 'GED Science: Earth & Space Science' course. The parent course gives a
one-lesson overview; this course goes deeper:

  1. The Sun -- our star, powered by nuclear fusion.
  2. The layout of the solar system and the two families of planets.
  3. Orbits and gravity -- why planets neither fly away nor fall in.
  4. The inner, rocky (terrestrial) planets.
  5. The outer, giant planets and the small bodies (asteroids, comets, meteors).
  6. The scale of space, exploration, and reading astronomy data.

This course uses ALL-NEW diagrams (the Sun's structure, a solar-system layout with
the asteroid belt, an orbit/gravity diagram, the inner and outer planet families,
comet anatomy, and a cosmic-distance scale) rather than reusing the parent
course's 'solar_system' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - NASA Solar System Exploration and NASA Science (planet facts, the Sun, comets).
  - Tarbuck, E. & Lutgens, F., *Earth Science* (Pearson).
  - Kepler's laws of planetary motion (simplified) and Newton's law of gravitation.
  - National Geographic Society, Resource Library: "solar system," "comet."
Note: the Sun holds about 99.8% of the solar system's mass; an astronomical unit
(AU) is the mean Earth-Sun distance (~150 million km); sunlight takes ~8 minutes
to reach Earth; the nearest star (Proxima Centauri) is about 4.2 light-years away.

Run:
    python manage.py seed_ged_solar_system
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: The Solar System & Earth in Space (Deep Dive)",
    "slug": "ged-solar-system",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into our cosmic neighborhood, expanding the single 'Solar System & Earth in Space' "
        "lesson from the GED Earth & Space Science course into a full mini-course. You'll start with the "
        "Sun -- a star powered by nuclear fusion -- then tour the eight planets, split into the small "
        "rocky worlds and the giant gas-and-ice worlds. You'll learn why gravity keeps planets in orbit, "
        "meet the asteroids and comets, and get a feel for the staggering scale of space and how "
        "astronomers measure it. Plain language, all-new labeled diagrams, common-misconception "
        "warnings, and GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. The Sun: Our Star",
            r"At the heart of everything is the **Sun**. It is not a special object that's different from the points of light you see at night — the Sun **is a star**, just much closer than the rest. It is a giant ball of hot gas (mostly hydrogen), and it holds about **99%** of all the mass in the solar system. That enormous mass gives it the **gravity** that keeps every planet in orbit." "\n\n"
            r"[[figure:sun_anatomy|Deep in the Sun's core, hydrogen fuses into helium, releasing the energy that lights and warms the solar system.]]" "\n\n"
            r"Where does the Sun's energy come from? Not from burning like a fire. Deep in its **core**, under crushing pressure and heat, **nuclear fusion** squeezes hydrogen atoms together to form helium, releasing tremendous energy. That energy works its way out and leaves the **surface** (about 5,500°C) as the light and heat we receive." "\n\n"
            r"The Sun even has 'weather': cooler, darker patches called **sunspots**, and a constant stream of particles called the **solar wind** that flows out across the solar system." "\n\n"
            r"⚠️ Common misconception: the Sun is **not** a planet, and it does **not** burn like a campfire. It is a **star** that makes energy by **nuclear fusion** — joining atoms together, not chemical burning." "\n\n"
            r"💡 Tip: the Sun = a **star** + **fusion** (hydrogen → helium) + **99% of the mass** → its gravity rules the solar system.",
        ),
        (
            "2. The Solar System: Layout & Two Families",
            r"Our **solar system** is the Sun plus everything its gravity holds: **eight planets**, their **moons**, and countless **asteroids** and **comets**. The planets all orbit the Sun in the same direction, in roughly the same flat plane." "\n\n"
            r"[[figure:solar_system_layout|The eight planets in order, with the asteroid belt between Mars and Jupiter, split into small inner worlds and giant outer ones.]]" "\n\n"
            r"The order from the Sun is **Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune**, and they fall into two families:" "\n"
            r"- The **inner planets** (Mercury, Venus, Earth, Mars) are **small, rocky**, and closer together — also called **terrestrial** planets." "\n"
            r"- The **outer planets** (Jupiter, Saturn, Uranus, Neptune) are **huge giants** made of gas and ice, cold and far apart." "\n\n"
            r"Between the two families, mostly between **Mars and Jupiter**, lies the **asteroid belt** — a zone of rocky leftovers from the solar system's formation." "\n\n"
            r"⚠️ Common misconception: the diagrams are **not to scale**. The real distances are vast and the gaps between the outer planets are enormous compared with the crowded inner planets." "\n\n"
            r"💡 Tip: a memory sentence for the order — 'My Very Easy Method Just Speeds Up Names' (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune). Inner = small & rocky; outer = giant.",
        ),
        (
            "3. Orbits & Gravity: Why Planets Don't Fly Away",
            r"Why do the planets circle the Sun forever instead of drifting off or crashing in? The answer is a balance between **two things**: the planet's **forward motion** and the Sun's **gravity**." "\n\n"
            r"[[figure:orbit_gravity|An orbit is the balance of forward motion and inward gravity: too little and the planet falls in; too much and it flies away.]]" "\n\n"
            r"Imagine a planet speeding through space. The Sun's gravity constantly pulls it **inward**. If there were no gravity, the planet would fly off in a **straight line**. If it had no motion, gravity would make it **fall straight into the Sun**. Instead, the inward pull bends the straight-line motion into a closed loop — an **orbit**." "\n\n"
            r"A few key facts:" "\n"
            r"- Orbits are **ellipses** (slightly stretched circles), not perfect circles." "\n"
            r"- A planet moves **faster** when it is **closer** to the Sun and slower when farther away." "\n"
            r"- One full orbit around the Sun is that planet's **year** — Earth's is 365 days; Neptune's is about 165 Earth-years." "\n\n"
            r"⚠️ Common misconception: gravity does not just 'hold things down' on Earth — the **same** force of gravity, reaching across space, is what keeps the Moon orbiting Earth and the planets orbiting the Sun." "\n\n"
            r"💡 Tip: orbit = **motion + gravity in balance.** Closer to the Sun → faster orbit → shorter year.",
        ),
        (
            "4. The Inner, Rocky Planets",
            r"The four planets closest to the Sun — **Mercury, Venus, Earth, and Mars** — are the **terrestrial** ('Earth-like') planets. They are small, dense, made mostly of **rock and metal**, and have **solid surfaces** you could stand on." "\n\n"
            r"[[figure:terrestrial_planets|The four inner planets compared — small rocky worlds, with Venus (not Mercury) the hottest.]]" "\n\n"
            r"- **Mercury** — closest to the Sun, smallest planet, with almost no atmosphere. It is heavily **cratered** and has wild temperature swings." "\n"
            r"- **Venus** — similar in size to Earth but wrapped in a **thick carbon-dioxide atmosphere** that traps heat. This **runaway greenhouse effect** makes Venus the **hottest planet** of all (~465°C)." "\n"
            r"- **Earth** — the only planet known to support **life**, thanks to **liquid water**, a protective atmosphere, and a 'just right' distance from the Sun." "\n"
            r"- **Mars** — the 'Red Planet,' colored by **iron oxide (rust)**. It has a thin atmosphere, polar **ice caps**, and signs that liquid water once flowed there." "\n\n"
            r"⚠️ Common misconception: the **closest** planet to the Sun is **not** the hottest. Mercury is closer, but airless Mercury loses heat, while **Venus's** thick CO₂ blanket traps it — so **Venus is hottest**." "\n\n"
            r"💡 Tip: inner four = **small, rocky, solid.** Remember 'Venus is hottest because of its greenhouse atmosphere, not its distance.'",
        ),
        (
            "5. The Outer Giants & the Small Bodies",
            r"Beyond the asteroid belt are the four **giant** planets — enormous, cold worlds with no solid surface to land on." "\n\n"
            r"[[figure:outer_planets|The four giant planets: gas giants Jupiter and Saturn, and the smaller, colder ice giants Uranus and Neptune.]]" "\n\n"
            r"- **Jupiter** — the **largest** planet, a gas giant famous for its **Great Red Spot**, a storm bigger than Earth." "\n"
            r"- **Saturn** — a gas giant best known for its spectacular **rings** of ice and rock." "\n"
            r"- **Uranus** and **Neptune** — the **ice giants**, smaller, bluish, and extremely cold. (Uranus is tipped on its side.)" "\n\n"
            r"The solar system is also full of **small bodies** left over from its birth:" "\n\n"
            r"[[figure:comet_anatomy|A comet's icy nucleus grows a glowing coma and a tail that always points away from the Sun.]]" "\n\n"
            r"- **Asteroids** — rocky chunks, mostly in the belt between Mars and Jupiter." "\n"
            r"- **Comets** — 'dirty snowballs' of **ice and dust**. Near the Sun, they heat up and grow a glowing **coma** and a **tail that always points away from the Sun**." "\n"
            r"- **Meteoroids → meteors → meteorites** — a small space rock is a **meteoroid**; the streak of light when it burns in our atmosphere is a **meteor** ('shooting star'); if a piece survives and lands, it's a **meteorite**." "\n\n"
            r"⚠️ Common misconception: a comet's tail does **not** trail behind its direction of motion like smoke. The solar wind always blows the tail to point **away from the Sun**, even as the comet leaves." "\n\n"
            r"💡 Tip: outer four = **giant, gassy/icy, no surface.** Small bodies: **asteroid = rock, comet = ice + tail, meteor = streak, meteorite = it landed.**",
        ),
        (
            "6. The Scale of Space & Reading Astronomy Data",
            r"The hardest thing to picture about space is how **big** it is. Even light — the fastest thing there is — takes time to cross it: sunlight needs about **8 minutes** to reach Earth, and several **hours** to reach Neptune." "\n\n"
            r"[[figure:cosmic_scale|Distances grow so fast that astronomers switch from kilometers to astronomical units and light-years.]]" "\n\n"
            r"Because kilometers become unwieldy, astronomers use bigger 'rulers':" "\n"
            r"- An **astronomical unit (AU)** is the average distance from **Earth to the Sun** (~150 million km). Neptune is about **30 AU** out." "\n"
            r"- A **light-year** is how far **light travels in one year** (~9.5 trillion km). The **nearest star** beyond the Sun is about **4.2 light-years** away — meaning its light left it more than four years ago." "\n\n"
            r"We explore this vast space with **telescopes**, robotic **probes and rovers**, and crewed missions near Earth. And the GED test rewards **reasoning with data**." "\n\n"
            r"**Reading astronomy data (a GED skill).** Items may give a table of planet distances, orbital periods, or temperatures, or a graph of one against another. Read the **title, columns, and units** first, find the **trend** (for example, planets farther from the Sun take longer to orbit), and conclude only what the data shows." "\n\n"
            r"⚠️ Common misconception: a 'light-year' measures **distance**, not time. It is how far light goes in a year, not how long something takes." "\n\n"
            r"💡 Tip: **AU = Earth–Sun distance; light-year = a distance (how far light travels in a year).** For any data table, read the units and name the trend." "\n\n"
            r"📚 Sources: NASA Solar System Exploration & NASA Science; Tarbuck & Lutgens, *Earth Science*; Kepler's and Newton's laws; National Geographic Resource Library.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: the Sun ---
        {
            "text": r"The Sun is best described as:",
            "difficulty": 1,
            "choices": [("A star — a giant ball of hot gas", True),
                        ("A large rocky planet", False),
                        ("A moon of Earth", False),
                        ("A giant comet", False)],
            "explanation": r"The Sun is a star: a huge sphere of hot gas. It only looks different from other stars because it is so much closer to us.",
        },
        {
            "text": r"How does the Sun produce its enormous energy?",
            "difficulty": 2,
            "choices": [("Nuclear fusion — joining hydrogen atoms into helium", True),
                        ("Burning wood and coal", False),
                        ("Reflecting light from the planets", False),
                        ("Friction from spinning quickly", False)],
            "explanation": r"In its core, the Sun fuses hydrogen into helium, releasing huge amounts of energy. It does not 'burn' chemically like a fire.",
        },
        {
            "text": r"About what fraction of the solar system's mass is contained in the Sun?",
            "difficulty": 2,
            "choices": [("About 99%", True), ("About 50%", False),
                        ("About 10%", False), ("About 1%", False)],
            "explanation": r"The Sun holds roughly 99% of all the mass in the solar system, which is why its gravity controls the orbits of everything else.",
        },
        {
            "text": r"What holds the planets in their orbits around the Sun?",
            "difficulty": 2,
            "choices": [("The Sun's gravity", True), ("The Sun's light", False),
                        ("Earth's magnetic field", False), ("The solar wind", False)],
            "explanation": r"The Sun's enormous mass creates the gravity that keeps every planet in orbit.",
        },
        {
            "text": ("Use the diagram of the Sun.\n\n"
                     "[[figure:sun_anatomy|The structure of the Sun]]\n\n"
                     "According to the diagram, where does nuclear fusion take place?"),
            "difficulty": 1,
            "choices": [("In the core", True), ("On the surface only", False),
                        ("In the sunspots", False), ("In the solar wind", False)],
            "explanation": r"The diagram shows fusion occurring in the Sun's core, where pressure and temperature are highest. Pro tip: fusion happens deep in the core.",
        },
        {
            "text": r"Sunspots look darker than the rest of the Sun's surface because they are:",
            "difficulty": 3,
            "choices": [("Cooler than the surrounding surface", True),
                        ("Holes all the way through the Sun", False),
                        ("Made of solid rock", False),
                        ("Reflections of the planets", False)],
            "explanation": r"Sunspots are regions that are cooler (and so dimmer) than the gas around them, which makes them look dark by comparison.",
        },
        # --- Lesson 2: layout ---
        {
            "text": r"Which list gives the planets in the correct order from the Sun?",
            "difficulty": 1,
            "choices": [("Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune", True),
                        ("Earth, Mercury, Venus, Mars, Saturn, Jupiter, Neptune, Uranus", False),
                        ("Mars, Earth, Venus, Mercury, Neptune, Uranus, Saturn, Jupiter", False),
                        ("Jupiter, Saturn, Earth, Mars, Mercury, Venus, Uranus, Neptune", False)],
            "explanation": r"From the Sun outward: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune.",
        },
        {
            "text": r"Which are the four inner, rocky (terrestrial) planets?",
            "difficulty": 1,
            "choices": [("Mercury, Venus, Earth, Mars", True),
                        ("Jupiter, Saturn, Uranus, Neptune", False),
                        ("Earth, Mars, Jupiter, Saturn", False),
                        ("Venus, Earth, Neptune, Mercury", False)],
            "explanation": r"The inner, rocky planets are Mercury, Venus, Earth, and Mars. The outer giants are Jupiter, Saturn, Uranus, and Neptune.",
        },
        {
            "text": r"The asteroid belt is located mainly between which two planets?",
            "difficulty": 2,
            "choices": [("Mars and Jupiter", True), ("Earth and Mars", False),
                        ("Saturn and Uranus", False), ("Mercury and Venus", False)],
            "explanation": r"The main asteroid belt lies between Mars and Jupiter, separating the inner rocky planets from the outer giants.",
        },
        {
            "text": ("Use the solar system diagram.\n\n"
                     "[[figure:solar_system_layout|The layout of the solar system]]\n\n"
                     "Based on the diagram, the outer planets are mostly:"),
            "difficulty": 2,
            "choices": [("Large giant planets", True),
                        ("Tiny rocky planets", False),
                        ("Made entirely of water", False),
                        ("Closer together than the inner planets", False)],
            "explanation": r"The diagram shows the outer planets as much larger giants, spaced far apart. Pro tip: inner = small & rocky, outer = giant.",
        },
        {
            "text": r"Besides the Sun and the eight planets, the solar system also contains:",
            "difficulty": 2,
            "choices": [("Moons, asteroids, and comets", True),
                        ("Other stars orbiting the Sun", False),
                        ("Nothing else at all", False),
                        ("Several other suns", False)],
            "explanation": r"The Sun's gravity also holds moons, asteroids, comets, and dust — all part of the solar system.",
        },
        # --- Lesson 3: orbits & gravity ---
        {
            "text": r"The path a planet follows around the Sun is called its:",
            "difficulty": 1,
            "choices": [("Orbit", True), ("Axis", False),
                        ("Equator", False), ("Horizon", False)],
            "explanation": r"An orbit is the path one object takes around another under the pull of gravity.",
        },
        {
            "text": r"The shape of a planet's orbit around the Sun is:",
            "difficulty": 2,
            "choices": [("An ellipse (a slightly stretched circle)", True),
                        ("A perfect square", False),
                        ("A straight line", False),
                        ("A tight spiral into the Sun", False)],
            "explanation": r"Planetary orbits are ellipses — ovals — with the Sun at one focus, not perfect circles.",
        },
        {
            "text": r"The length of time it takes a planet to complete one orbit of the Sun is that planet's:",
            "difficulty": 2,
            "choices": [("Year", True), ("Day", False),
                        ("Month", False), ("Season", False)],
            "explanation": r"One full trip around the Sun is a planet's year. (One spin on its axis is a day.)",
        },
        {
            "text": ("Use the orbit diagram.\n\n"
                     "[[figure:orbit_gravity|A planet orbiting the Sun]]\n\n"
                     "According to the diagram, an orbit results from a balance between:"),
            "difficulty": 2,
            "choices": [("The planet's forward motion and the Sun's inward gravity", True),
                        ("The Sun's light and the planet's heat", False),
                        ("The planet's magnetism and its color", False),
                        ("The Moon's pull and the planet's spin", False)],
            "explanation": r"The diagram shows gravity pulling the planet inward while its forward motion would carry it straight; together they create a closed orbit. Pro tip: orbit = motion + gravity.",
        },
        {
            "text": r"A planet moves fastest along its orbit when it is:",
            "difficulty": 3,
            "choices": [("Closest to the Sun", True), ("Farthest from the Sun", False),
                        ("Exactly halfway around", False), ("Behind another planet", False)],
            "explanation": r"A planet speeds up as it nears the Sun and slows down as it moves away — a result of gravity being stronger when it is closer.",
        },
        # --- Lesson 4: inner planets ---
        {
            "text": r"Which planet is known as the 'Red Planet'?",
            "difficulty": 1,
            "choices": [("Mars", True), ("Venus", False),
                        ("Mercury", False), ("Jupiter", False)],
            "explanation": r"Mars looks red because its surface is covered in iron oxide — rust.",
        },
        {
            "text": r"Mercury is closer to the Sun, yet Venus is the hottest planet. Why?",
            "difficulty": 2,
            "choices": [("Venus has a thick carbon-dioxide atmosphere that traps heat (a runaway greenhouse effect)", True),
                        ("Venus is actually closer to the Sun than Mercury", False),
                        ("Mercury produces its own heat", False),
                        ("Venus is made of fire", False)],
            "explanation": r"Venus's dense CO₂ atmosphere traps heat, so it stays hotter than airless Mercury even though Mercury is closer to the Sun.",
        },
        {
            "text": r"Mars appears red because its surface contains a lot of:",
            "difficulty": 2,
            "choices": [("Iron oxide (rust)", True), ("Red water", False),
                        ("Glowing lava", False), ("Red plants", False)],
            "explanation": r"Iron-rich dust on Mars has oxidized (rusted), giving the planet its reddish color.",
        },
        {
            "text": ("Use the inner planets diagram.\n\n"
                     "[[figure:terrestrial_planets|The four inner rocky planets]]\n\n"
                     "Based on the diagram, the inner planets are all:"),
            "difficulty": 1,
            "choices": [("Small and rocky, with solid surfaces", True),
                        ("Huge balls of gas", False),
                        ("Made of ice with rings", False),
                        ("Larger than Jupiter", False)],
            "explanation": r"The diagram shows the inner planets as small, rocky worlds with solid surfaces. Pro tip: terrestrial = rocky and solid.",
        },
        {
            "text": r"What makes Earth uniquely suited to support life as we know it?",
            "difficulty": 3,
            "choices": [("Its 'just right' distance allows liquid water, plus a protective atmosphere", True),
                        ("It is the largest planet", False),
                        ("It is the closest planet to the Sun", False),
                        ("It has no atmosphere at all", False)],
            "explanation": r"Earth orbits at a distance where water can stay liquid, and its atmosphere shields the surface and holds warmth — conditions life depends on.",
        },
        # --- Lesson 5: outer giants & small bodies ---
        {
            "text": r"Which is the largest planet in the solar system?",
            "difficulty": 1,
            "choices": [("Jupiter", True), ("Saturn", False),
                        ("Earth", False), ("Neptune", False)],
            "explanation": r"Jupiter is the largest planet — a gas giant famous for its Great Red Spot.",
        },
        {
            "text": r"Which planet is best known for its bright, spectacular rings?",
            "difficulty": 1,
            "choices": [("Saturn", True), ("Mars", False),
                        ("Mercury", False), ("Earth", False)],
            "explanation": r"Saturn is famous for its bright rings of ice and rock. (The other giants have faint rings, but Saturn's are by far the most prominent.)",
        },
        {
            "text": r"The outer giant planets differ from the inner planets mainly in that the giants are:",
            "difficulty": 2,
            "choices": [("Huge, made of gas and ice, with no solid surface", True),
                        ("Small, rocky, and warm", False),
                        ("Closer to the Sun", False),
                        ("Made entirely of metal", False)],
            "explanation": r"The outer planets are enormous, cold worlds of gas and ice with no solid surface — very different from the small, rocky inner planets.",
        },
        {
            "text": ("Use the comet diagram.\n\n"
                     "[[figure:comet_anatomy|The parts of a comet]]\n\n"
                     "According to the diagram, a comet's tail always points:"),
            "difficulty": 2,
            "choices": [("Away from the Sun", True), ("Toward the Sun", False),
                        ("Straight down to Earth", False), ("In the direction the comet is moving", False)],
            "explanation": r"The Sun's heat and solar wind blow the comet's gas and dust outward, so the tail always points away from the Sun — even as the comet moves away. Pro tip: tail = away from the Sun.",
        },
        {
            "text": r"What is the difference between a meteor and a meteorite?",
            "difficulty": 2,
            "choices": [("A meteor is the streak of light in the sky; a meteorite is a rock that lands on the ground", True),
                        ("A meteor lands on the ground; a meteorite stays in space", False),
                        ("They are exactly the same thing", False),
                        ("A meteor is a planet; a meteorite is a moon", False)],
            "explanation": r"A meteor is the bright streak ('shooting star') as a space rock burns in the atmosphere; if a piece survives and reaches the ground, it is a meteorite.",
        },
        {
            "text": r"A comet is mostly made of:",
            "difficulty": 2,
            "choices": [("Ice and dust", True), ("Molten lava", False),
                        ("Solid iron", False), ("Hot gas like the Sun", False)],
            "explanation": r"Comets are 'dirty snowballs' of ice and dust. Near the Sun the ice vaporizes, forming the glowing coma and tail.",
        },
        # --- Lesson 6: scale & data ---
        {
            "text": r"One astronomical unit (AU) is defined as:",
            "difficulty": 2,
            "choices": [("The average distance from Earth to the Sun", True),
                        ("The distance light travels in one year", False),
                        ("The width of the solar system", False),
                        ("The distance from Earth to the Moon", False)],
            "explanation": r"An AU is the mean Earth–Sun distance (about 150 million km), a handy ruler for distances within the solar system.",
        },
        {
            "text": r"Sunlight takes about 8 minutes to reach Earth. Astronomers use units like the light-year because:",
            "difficulty": 2,
            "choices": [("Distances in space are extremely large", True),
                        ("Light has no speed", False),
                        ("Space is actually very small", False),
                        ("Years are easier than minutes", False)],
            "explanation": r"Space is so vast that ordinary units like kilometers become unwieldy, so astronomers measure distance by how far light travels in a given time (a light-year is a distance).",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain why the planets stay in orbit around the Sun rather than flying off into space or "
                "falling into the Sun. In your answer, describe the roles of gravity and the planet's motion, "
                "and explain what is meant by a planet's 'year.'"
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the Sun's gravity constantly pulls each planet inward; (2) the planet also has "
                "forward motion (it would travel in a straight line without gravity); (3) the balance of inward "
                "gravity and forward motion bends the path into a closed orbit (an ellipse); (4) without gravity it "
                "would fly off straight, and without motion it would fall into the Sun; (5) one complete orbit of the "
                "Sun is the planet's year. Deduct for saying gravity alone, or motion alone, keeps a planet in orbit."
            ),
        },
        {
            "text": (
                "Compare the inner and outer planets. Give the eight planets in order from the Sun, describe the two "
                "families (inner rocky planets and outer giants), and explain why Venus is hotter than Mercury even "
                "though Mercury is closer to the Sun."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the correct order -- Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, "
                "Neptune; (2) the inner four are small, rocky, solid (terrestrial) planets; (3) the outer four are "
                "huge gas/ice giants with no solid surface; (4) noting the asteroid belt between Mars and Jupiter; "
                "(5) Venus is hottest because its thick carbon-dioxide atmosphere traps heat (a runaway greenhouse "
                "effect), while airless Mercury, though closer, loses its heat. Deduct for wrong order or claiming "
                "the closest planet must be the hottest."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: The Solar System & Earth in Space (Deep Dive)' course."

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
