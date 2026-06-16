"""
Seed data: 'GED Science: The Moon, Seasons & Earth's Cycles (Deep Dive)'.

A focused EXPANSION of Lesson 7 ("The Moon, Seasons & Reading Science Data") from
the broader 'GED Science: Earth & Space Science' course. The parent course gives a
one-lesson overview of phases and seasons; this course goes deeper:

  1. Day and night, and Earth's two motions (rotation vs. revolution).
  2. The Moon -- our companion: reflected light, synchronous rotation, craters.
  3. The phases of the Moon and why they happen.
  4. Eclipses -- solar vs. lunar, and why they don't happen every month.
  5. The seasons and Earth's axial tilt (the tilt, not distance).
  6. Tides, and reading science data (correlation vs. causation).

This course uses ALL-NEW diagrams (Earth's rotation/revolution, the Earth-Moon
system, a phases diagram, solar/lunar eclipses, the seasons from axial tilt, and
the tides) rather than reusing the parent course's 'moon_phases' and 'seasons'
figures.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - NASA Science (Moon phases, eclipses) and NOAA (tides and currents).
  - Tarbuck, E. & Lutgens, F., *Earth Science* (Pearson).
  - National Geographic Society, Resource Library: "moon," "season," "tide."
Note: Earth's axis is tilted about 23.5 degrees; the Moon orbits Earth about every
27.3 days (sidereal) but the phase cycle is about 29.5 days (synodic); the Moon's
orbit is tilted about 5 degrees, which is why eclipses do not occur every month.

Run:
    python manage.py seed_ged_moon_seasons
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: The Moon, Seasons & Earth's Cycles (Deep Dive)",
    "slug": "ged-moon-seasons",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into the rhythms of the sky, expanding the single 'Moon, Seasons & Reading Science "
        "Data' lesson from the GED Earth & Space Science course into a full mini-course. You'll learn how "
        "Earth's spin and orbit make days and years, why the Moon shows phases and sometimes causes "
        "eclipses, why the seasons come from Earth's tilt (not its distance from the Sun), and how the "
        "Moon's gravity makes the tides. You'll also practice reading science data carefully. Plain "
        "language, all-new labeled diagrams, common-misconception warnings, and GED-style practice with "
        "full explanations throughout."
    ),
    "lessons": [
        (
            "1. Day & Night: Earth's Two Motions",
            r"Earth is always doing two things at once, and mixing them up causes a lot of confusion. It **spins** like a top, and it **travels** around the Sun." "\n\n"
            r"[[figure:earth_rotation_revolution|Rotation (Earth spinning on its axis) makes day and night; revolution (Earth orbiting the Sun) makes the year.]]" "\n\n"
            r"- **Rotation** is Earth **spinning on its axis**, an imaginary line through the North and South Poles. One full spin takes about **24 hours** — that's what gives us **day and night**. The side facing the Sun has day; the side facing away has night." "\n"
            r"- **Revolution** is Earth **orbiting the Sun**. One full trip takes about **365 days** — that's one **year**." "\n\n"
            r"Earth's axis is **tilted** (about 23.5°), and it stays pointed in the same direction as Earth orbits. That steady tilt is the secret behind the seasons (Lesson 5)." "\n\n"
            r"⚠️ Common misconception: day and night are **not** caused by Earth moving closer to or farther from the Sun, and the Sun does not actually 'rise' and travel across the sky. It is **Earth's rotation** that carries us into and out of sunlight." "\n\n"
            r"💡 Tip: **Rotation = spin = 1 day; Revolution = orbit = 1 year.** Don't confuse the two.",
        ),
        (
            "2. The Moon: Earth's Companion",
            r"The **Moon** is Earth's only natural satellite — a rocky, cratered world about a quarter of Earth's width that orbits us roughly every **27 days**. It has almost no atmosphere, so its surface bakes in sunlight and freezes in shadow, and its craters never erode away." "\n\n"
            r"[[figure:moon_overview|The Moon makes no light of its own — it reflects sunlight — and it always keeps the same near side facing Earth.]]" "\n\n"
            r"Two key facts shape everything we see:" "\n"
            r"- **The Moon makes no light of its own.** It only **reflects sunlight**. At any moment the Sun lights up one half of the Moon — and which part of that lit half we can see produces the **phases** (Lesson 3)." "\n"
            r"- **The Moon keeps the same face toward Earth.** It spins exactly once for each orbit (this is called **synchronous rotation**), so we always see the same **near side** and never the **far side** from Earth." "\n\n"
            r"⚠️ Common misconception: there is no permanently 'dark side' of the Moon. The far side gets just as much sunlight as the near side — we simply never see it from Earth. (It's the *far* side, not the *dark* side.)" "\n\n"
            r"💡 Tip: the Moon **reflects** sunlight and is locked so the **same side always faces Earth.**",
        ),
        (
            "3. The Phases of the Moon",
            r"Why does the Moon seem to change shape over the month? It isn't really changing — we are just seeing **different amounts of its lit half** as it orbits Earth." "\n\n"
            r"[[figure:moon_phases_detailed|The Sun always lights one half of the Moon; as the Moon orbits, we see more or less of that lit half — the phases.]]" "\n\n"
            r"The cycle takes about **29.5 days** and runs through eight phases:" "\n"
            r"- **New moon** — the Moon is between Earth and the Sun, so the lit half faces away and we see darkness." "\n"
            r"- **Waxing** phases (crescent → first quarter → gibbous) — the lit part we see is **growing**." "\n"
            r"- **Full moon** — Earth is between the Sun and Moon, so we see the entire near side lit." "\n"
            r"- **Waning** phases (gibbous → last quarter → crescent) — the lit part we see is **shrinking** back to new." "\n\n"
            r"'**Waxing**' means getting bigger; '**waning**' means getting smaller. A thin sliver is a **crescent**; more than half is a **gibbous**." "\n\n"
            r"⚠️ Common misconception: the phases are **not** caused by Earth's shadow falling on the Moon. (That's a lunar eclipse, which is rare.) Phases come from the **angle** at which we view the Moon's sunlit half." "\n\n"
            r"💡 Tip: **waxing = growing toward full; waning = shrinking toward new.** Phases come from the viewing angle, not Earth's shadow.",
        ),
        (
            "4. Eclipses: When Sun, Earth & Moon Line Up",
            r"Once in a while the Sun, Earth, and Moon line up in a straight line, and one casts its shadow on another. That's an **eclipse**, and there are two kinds." "\n\n"
            r"[[figure:eclipses|A solar eclipse: the Moon's shadow falls on Earth (at new moon). A lunar eclipse: Earth's shadow falls on the Moon (at full moon).]]" "\n\n"
            r"- **Solar eclipse** — the **Moon** passes **between** the Sun and Earth, so the **Moon blocks the Sun** and casts its shadow on part of Earth. This can only happen at **new moon**, and turns day briefly to twilight along a narrow path." "\n"
            r"- **Lunar eclipse** — **Earth** passes **between** the Sun and Moon, so **Earth's shadow falls on the Moon**. This can only happen at **full moon**, and often turns the Moon a dim red." "\n\n"
            r"So why don't we get an eclipse every month at every new and full moon? Because the Moon's orbit is **tilted** about 5° compared with Earth's orbit. Most months the Moon passes a little above or below the line, and the shadows miss. Only when the alignment is just right do we get an eclipse." "\n\n"
            r"⚠️ Common misconception: eclipses are **not** rare because the Moon is far away — they're 'rare' because the Moon's tilted orbit usually carries its shadow just above or below the perfect line-up." "\n\n"
            r"💡 Tip: **Solar = Moon blocks Sun (new moon); Lunar = Earth's shadow on Moon (full moon).** Tilt is why they're not monthly.",
        ),
        (
            "5. The Seasons & Earth's Tilt",
            r"Here is the single most misunderstood idea in Earth science. Seasons are **not** caused by Earth being closer to or farther from the Sun. (In fact, Earth is **closest** to the Sun in early January, during Northern Hemisphere winter!) The real cause is Earth's **axial tilt** of about **23.5°**." "\n\n"
            r"[[figure:seasons_detailed|Earth's axis stays pointed the same way all year, so each hemisphere takes turns leaning toward the Sun.]]" "\n\n"
            r"Because the axis stays tilted in the same direction all year, each hemisphere takes turns leaning toward the Sun:" "\n"
            r"- The hemisphere tilted **toward** the Sun gets more **direct** sunlight and **longer days** — that's **summer**." "\n"
            r"- The hemisphere tilted **away** gets slanted, weaker sunlight and shorter days — that's **winter**." "\n"
            r"- The two hemispheres always have **opposite** seasons: when it's summer in the north, it's winter in the south." "\n\n"
            r"The turning points have names: the **solstices** (longest and shortest days, around June 21 and December 21) and the **equinoxes** (equal day and night, around March 21 and September 21)." "\n\n"
            r"⚠️ Common misconception: seasons are **not** caused by distance from the Sun. It's the **tilt** — which hemisphere is leaning toward the Sun and getting direct rays." "\n\n"
            r"💡 Tip: **tilt, not distance.** Tilted toward the Sun = direct rays + long days = summer.",
        ),
        (
            "6. Tides & Reading Science Data",
            r"The Moon doesn't just light up the night — its **gravity** tugs on Earth, and that pull is strong enough to move the **oceans**. The result is the **tides**: the slow, daily rise and fall of the sea." "\n\n"
            r"[[figure:tides|The Moon's gravity pulls ocean water into bulges on the near and far sides of Earth, creating high and low tides.]]" "\n\n"
            r"The Moon's gravity pulls hardest on the side of Earth facing it, raising a bulge of water there — a **high tide**. A second high-tide bulge forms on the **opposite** side. In between, the water is lower — **low tide**. As Earth rotates, most coasts pass through about **two high tides and two low tides each day**." "\n\n"
            r"The **Sun's** gravity adds to the effect. When the Sun, Earth, and Moon line up (new and full moon), their pulls combine into extra-large **spring tides**; when they're at right angles (quarter moons), the pulls partly cancel into smaller **neap tides**." "\n\n"
            r"**Reading science data (a GED skill).** Astronomy and Earth-science questions love graphs and tables — tide heights over a day, daylight hours over a year, or temperature versus distance. Read the **title, axes, and units** first, find the **trend**, and use only what the data shows. Remember: **correlation is not causation** — two things changing together doesn't prove one causes the other." "\n\n"
            r"⚠️ Common misconception: tides are caused mainly by the Moon, **not** by the wind or by the Sun alone. The Sun contributes, but the closer Moon dominates." "\n\n"
            r"💡 Tip: tides = the **Moon's gravity** (with a Sun assist). For any graph, read the **axes and units**, name the **trend**, and don't assume correlation proves causation." "\n\n"
            r"📚 Sources: NASA Science (Moon, eclipses); NOAA Tides & Currents; Tarbuck & Lutgens, *Earth Science*; National Geographic Resource Library.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: rotation & revolution ---
        {
            "text": r"What causes day and night on Earth?",
            "difficulty": 1,
            "choices": [("Earth rotating (spinning) on its axis", True),
                        ("Earth moving closer to and farther from the Sun", False),
                        ("The Sun orbiting the Earth", False),
                        ("The Moon blocking the Sun each night", False)],
            "explanation": r"Earth spins on its axis about once every 24 hours. The side facing the Sun has day; the side facing away has night.",
        },
        {
            "text": r"Earth's revolution around the Sun takes about one:",
            "difficulty": 1,
            "choices": [("Year", True), ("Day", False),
                        ("Hour", False), ("Month", False)],
            "explanation": r"One revolution (orbit) of the Sun takes about 365 days — one year. One rotation (spin) takes about 24 hours — one day.",
        },
        {
            "text": r"What is the difference between Earth's rotation and its revolution?",
            "difficulty": 2,
            "choices": [("Rotation is Earth spinning on its axis; revolution is Earth orbiting the Sun", True),
                        ("Rotation is the orbit; revolution is the spin", False),
                        ("They both take exactly one day", False),
                        ("They are two words for the same motion", False)],
            "explanation": r"Rotation is the daily spin on Earth's axis (day/night); revolution is the yearly trip around the Sun.",
        },
        {
            "text": ("Use the diagram of Earth's motions.\n\n"
                     "[[figure:earth_rotation_revolution|Earth's rotation and revolution]]\n\n"
                     "According to the diagram, Earth's rotation on its axis is responsible for:"),
            "difficulty": 2,
            "choices": [("Day and night", True), ("The year", False),
                        ("The phases of the Moon", False), ("The tides", False)],
            "explanation": r"The diagram links the daily spin (rotation) to day and night, and the yearly orbit (revolution) to the year. Pro tip: spin = day, orbit = year.",
        },
        # --- Lesson 2: the Moon ---
        {
            "text": r"Why does the Moon appear to shine?",
            "difficulty": 1,
            "choices": [("It reflects sunlight", True), ("It produces its own light", False),
                        ("It is on fire", False), ("It glows from Earth's heat", False)],
            "explanation": r"The Moon makes no light of its own; it reflects light from the Sun. We see whichever part of its sunlit half is facing us.",
        },
        {
            "text": r"We always see the same side of the Moon from Earth because the Moon:",
            "difficulty": 2,
            "choices": [("Spins exactly once for each orbit of Earth (synchronous rotation)", True),
                        ("Does not rotate at all", False),
                        ("Stops moving when we look at it", False),
                        ("Is too far away to turn", False)],
            "explanation": r"The Moon's spin is locked to its orbit (synchronous rotation), so the same near side always faces Earth and we never see the far side.",
        },
        {
            "text": r"Which statement about the 'far side' of the Moon is correct?",
            "difficulty": 3,
            "choices": [("It receives sunlight too; we just never see it from Earth", True),
                        ("It is always completely dark", False),
                        ("It does not really exist", False),
                        ("It faces the Sun at all times", False)],
            "explanation": r"The far side gets as much sunlight as the near side over a month — it's the side we can't see from Earth, not a permanently 'dark' side.",
        },
        # --- Lesson 3: phases ---
        {
            "text": r"The phases of the Moon are caused by:",
            "difficulty": 2,
            "choices": [("Seeing different amounts of the Moon's sunlit half as it orbits Earth", True),
                        ("Earth's shadow falling on the Moon", False),
                        ("Clouds covering part of the Moon", False),
                        ("The Moon changing its actual shape", False)],
            "explanation": r"The Sun always lights half the Moon; as the Moon orbits, we view that lit half from different angles, so we see more or less of it — the phases.",
        },
        {
            "text": r"At which phase is the entire near side of the Moon lit, so we see a full circle?",
            "difficulty": 1,
            "choices": [("Full moon", True), ("New moon", False),
                        ("First quarter", False), ("Waning crescent", False)],
            "explanation": r"At full moon, Earth is between the Sun and Moon, so the whole near side is sunlit. At new moon the near side is dark.",
        },
        {
            "text": r"When the lit part of the Moon we see is growing larger each night, the Moon is said to be:",
            "difficulty": 2,
            "choices": [("Waxing", True), ("Waning", False),
                        ("Eclipsing", False), ("Setting", False)],
            "explanation": r"'Waxing' means the visible lit portion is growing (new toward full); 'waning' means it is shrinking (full toward new).",
        },
        {
            "text": ("Use the Moon phases diagram.\n\n"
                     "[[figure:moon_phases_detailed|Why the Moon has phases]]\n\n"
                     "According to the diagram, a new moon occurs when the Moon is:"),
            "difficulty": 2,
            "choices": [("Between Earth and the Sun, so its lit half faces away from us", True),
                        ("On the opposite side of Earth from the Sun", False),
                        ("Hidden inside Earth's shadow every month", False),
                        ("Producing no light because it has cooled", False)],
            "explanation": r"The diagram shows the new moon between Earth and the Sun, with its sunlit half pointing away from Earth, so the near side looks dark. Pro tip: new moon = between Earth and Sun.",
        },
        # --- Lesson 4: eclipses ---
        {
            "text": r"A solar eclipse happens when:",
            "difficulty": 2,
            "choices": [("The Moon passes between the Sun and Earth, blocking the Sun", True),
                        ("Earth passes between the Sun and the Moon", False),
                        ("The Moon stops reflecting light", False),
                        ("The Sun passes behind Earth's core", False)],
            "explanation": r"In a solar eclipse the Moon lines up between the Sun and Earth and casts its shadow on Earth, briefly blocking the Sun. It happens at new moon.",
        },
        {
            "text": r"A lunar eclipse happens when:",
            "difficulty": 2,
            "choices": [("Earth's shadow falls on the Moon", True),
                        ("The Moon's shadow falls on Earth", False),
                        ("The Moon moves in front of the Sun", False),
                        ("The Moon leaves its orbit", False)],
            "explanation": r"In a lunar eclipse, Earth is between the Sun and Moon, so Earth's shadow falls across the Moon. It happens at full moon.",
        },
        {
            "text": r"Why don't we see a solar and a lunar eclipse every single month?",
            "difficulty": 3,
            "choices": [("The Moon's orbit is tilted, so its shadow usually misses just above or below the line-up", True),
                        ("The Moon disappears for most of the month", False),
                        ("The Sun turns off part of the year", False),
                        ("Eclipses can only happen in winter", False)],
            "explanation": r"The Moon's orbit is tilted about 5° from Earth's orbit, so most months the alignment isn't exact and the shadows miss. Eclipses need a near-perfect line-up.",
        },
        {
            "text": ("Use the eclipse diagram.\n\n"
                     "[[figure:eclipses|Solar and lunar eclipses]]\n\n"
                     "In the diagram, which object is in the MIDDLE during a solar eclipse?"),
            "difficulty": 2,
            "choices": [("The Moon", True), ("The Earth", False),
                        ("The Sun", False), ("A comet", False)],
            "explanation": r"The diagram shows the Moon between the Sun and Earth for a solar eclipse (Earth is in the middle for a lunar eclipse). Pro tip: SOLar eclipse = Moon blocks the Sun.",
        },
        # --- Lesson 5: seasons ---
        {
            "text": r"What actually causes Earth's seasons?",
            "difficulty": 2,
            "choices": [("The tilt of Earth's axis (about 23.5 degrees)", True),
                        ("Earth moving closer to and farther from the Sun", False),
                        ("The phases of the Moon", False),
                        ("Changes in the Sun's brightness", False)],
            "explanation": r"Seasons come from Earth's axial tilt: the hemisphere tilted toward the Sun gets more direct light (summer). Distance from the Sun is not the cause.",
        },
        {
            "text": r"It is summer in the Northern Hemisphere. What is happening with Earth's tilt?",
            "difficulty": 2,
            "choices": [("The Northern Hemisphere is tilted toward the Sun", True),
                        ("The Northern Hemisphere is tilted away from the Sun", False),
                        ("Earth is closest to the Sun", False),
                        ("Earth has no tilt in summer", False)],
            "explanation": r"In Northern summer, the North Pole leans toward the Sun, so that hemisphere gets more direct sunlight and longer days. It is winter in the south at the same time.",
        },
        {
            "text": r"When it is summer in the Northern Hemisphere, what season is it in the Southern Hemisphere?",
            "difficulty": 1,
            "choices": [("Winter", True), ("Summer", False),
                        ("Also spring", False), ("There are no seasons there", False)],
            "explanation": r"The hemispheres are tilted opposite ways relative to the Sun, so they always have opposite seasons.",
        },
        {
            "text": r"Earth is actually closest to the Sun in early January, during Northern winter. This fact best shows that:",
            "difficulty": 3,
            "choices": [("Distance from the Sun does not cause the seasons; the tilt does", True),
                        ("Winter is caused by Earth being far from the Sun", False),
                        ("The Northern and Southern Hemispheres have the same season", False),
                        ("Earth's orbit is a perfect circle", False)],
            "explanation": r"If distance caused the seasons, January (closest) would be summer everywhere — but it's Northern winter. So the tilt, not distance, drives the seasons.",
        },
        {
            "text": ("Use the seasons diagram.\n\n"
                     "[[figure:seasons_detailed|Earth's tilt as it orbits the Sun]]\n\n"
                     "Based on the diagram, what makes one hemisphere have summer?"),
            "difficulty": 2,
            "choices": [("That hemisphere is tilted toward the Sun, getting more direct light", True),
                        ("That hemisphere is closest to the Sun", False),
                        ("The Sun temporarily gives off more heat", False),
                        ("The Moon blocks less sunlight there", False)],
            "explanation": r"The diagram shows the axis pointing the same way all year, so each hemisphere takes turns tilting toward the Sun for summer. Pro tip: tilted toward = summer.",
        },
        # --- Lesson 6: tides & data ---
        {
            "text": r"What is the main cause of Earth's ocean tides?",
            "difficulty": 1,
            "choices": [("The Moon's gravity pulling on the oceans", True),
                        ("The wind pushing the water", False),
                        ("Earth's magnetic field", False),
                        ("Rivers flowing into the sea", False)],
            "explanation": r"The Moon's gravity pulls Earth's oceans into bulges, creating high and low tides. The Sun adds a smaller effect.",
        },
        {
            "text": r"Most coastlines experience about how many high tides each day?",
            "difficulty": 2,
            "choices": [("Two", True), ("One", False),
                        ("Five", False), ("Twenty", False)],
            "explanation": r"There are high-tide bulges on the near and far sides of Earth, so as the planet rotates, most coasts pass through about two high tides (and two low tides) per day.",
        },
        {
            "text": r"Extra-large 'spring tides' happen when:",
            "difficulty": 3,
            "choices": [("The Sun, Earth, and Moon line up (new and full moon), so their pulls combine", True),
                        ("The Sun and Moon pull at right angles", False),
                        ("Only in the spring season", False),
                        ("The Moon is farthest from Earth", False)],
            "explanation": r"When the Sun and Moon line up (at new and full moon), their gravitational pulls add together to make the largest (spring) tides. At right angles they partly cancel, making smaller neap tides.",
        },
        {
            "text": ("A graph shows that as the Moon's position shifts over a day, the tide height rises and falls in a regular pattern.\n\n"
                     "What is the best conclusion the data supports?"),
            "difficulty": 3,
            "choices": [("Tide height is closely related to the Moon's position", True),
                        ("The Moon is made of water", False),
                        ("Tides have nothing to do with the Moon", False),
                        ("The graph must be wrong", False)],
            "explanation": r"The data shows tide height changing in step with the Moon's position, supporting a link between them. Read what the data shows — and remember a correlation should match a known cause (here, the Moon's gravity).",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain why we experience seasons on Earth. A friend tells you that summer happens because "
                "Earth is closer to the Sun. Use Earth's axial tilt to explain why your friend is mistaken, and "
                "describe what makes one hemisphere experience summer while the other has winter."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) stating seasons are caused by Earth's ~23.5 degree axial tilt, not distance; "
                "(2) explaining the hemisphere tilted toward the Sun gets more direct sunlight and longer days "
                "(summer) while the other is tilted away (winter); (3) noting the two hemispheres have opposite "
                "seasons at the same time; (4) bonus: Earth is actually closest to the Sun during Northern winter, "
                "which disproves the distance idea. Deduct for attributing seasons mainly to distance from the Sun."
            ),
        },
        {
            "text": (
                "Explain why the Moon goes through phases, and how a lunar eclipse is different from the phases. "
                "In your answer, describe what causes the phases, name what a full moon and a new moon look like, "
                "and explain what actually happens during a lunar eclipse."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the Sun always lights half the Moon, and phases come from seeing different "
                "amounts of that lit half as the Moon orbits Earth; (2) a full moon shows the whole near side lit "
                "(Earth between Sun and Moon), a new moon shows the near side dark (Moon between Earth and Sun); "
                "(3) phases are NOT caused by Earth's shadow; (4) a lunar eclipse is when Earth's shadow actually "
                "falls on the Moon (at full moon), which is a separate, rarer event. Deduct for saying phases are "
                "caused by Earth's shadow."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: The Moon, Seasons & Earth's Cycles (Deep Dive)' course."

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
