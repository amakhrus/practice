r"""
Data for the diagnostic pre-test.

A short, stateless quiz (no login required, no database writes) that measures a
student's proficiency in each major topic of a program, then routes them to the
right course. Unlike a one-question screener, each topic carries THREE questions
so a single careless slip doesn't mislead the recommendation.

Structure: each program has a list of TOPICS; each topic has the course to
recommend if the student is weak in it, plus three questions:

    {
        "topic": "Fractions",
        "recommend": "ged-basic-math-fractions-mastery",
        "questions": [ {"text": ..., "choices": [("2/3", True), ...]}, ... x3 ],
    }

Scoring (see topic_needs_review): a topic is "proficient" at two-thirds correct
or better (2 of 3); below that it is flagged for review. A course is recommended
when any of its topics is flagged. Keeping this in code mirrors how the rest of
the project defines content and keeps the diagnostic self-contained.
"""

DIAGNOSTICS = {
    "GED": {
        "label": "GED",
        "blurb": "24 questions across 8 topics in math, science, reading, writing, and social studies (about 20-25 minutes).",
        # Suggested when a student is proficient across every topic.
        "ready_recommend": ["ged-full-length-practice", "ged-science-complete-practice"],
        "topics": [
            {
                "topic": "Fractions",
                "recommend": "ged-basic-math-fractions-mastery",
                "questions": [
                    {"text": r"Simplify the fraction \(\frac{8}{12}\) to lowest terms.",
                     "choices": [(r"\(\frac{2}{3}\)", True), (r"\(\frac{4}{8}\)", False),
                                 (r"\(\frac{8}{12}\)", False), (r"\(\frac{3}{4}\)", False)]},
                    {"text": r"What is \(\frac{1}{2} + \frac{1}{4}\)?",
                     "choices": [(r"\(\frac{3}{4}\)", True), (r"\(\frac{2}{6}\)", False),
                                 (r"\(\frac{1}{8}\)", False), (r"\(\frac{2}{4}\)", False)]},
                    {"text": r"What is \(\frac{2}{3} \times \frac{3}{5}\)?",
                     "choices": [(r"\(\frac{2}{5}\)", True), (r"\(\frac{5}{8}\)", False),
                                 (r"\(\frac{6}{8}\)", False), (r"\(\frac{4}{5}\)", False)]},
                ],
            },
            {
                "topic": "Percents",
                "recommend": "ged-basic-math-percents-mastery",
                "questions": [
                    {"text": r"What is \(20\%\) of \(150\)?",
                     "choices": [(r"\(30\)", True), (r"\(15\)", False), (r"\(50\)", False), (r"\(300\)", False)]},
                    {"text": r"An \$80 item is marked \(25\%\) off. What is the sale price?",
                     "choices": [(r"\$60", True), (r"\$20", False), (r"\$55", False), (r"\$100", False)]},
                    {"text": r"\(45\) is what percent of \(90\)?",
                     "choices": [(r"\(50\%\)", True), (r"\(45\%\)", False), (r"\(2\%\)", False), (r"\(200\%\)", False)]},
                ],
            },
            {
                "topic": "Algebra",
                "recommend": "ged-algebra-in-depth",
                "questions": [
                    {"text": r"Solve for \(x\): \(2x + 5 = 17\).",
                     "choices": [(r"\(x = 6\)", True), (r"\(x = 11\)", False),
                                 (r"\(x = 22\)", False), (r"\(x = 8.5\)", False)]},
                    {"text": r"Solve for \(x\): \(5x - 2 = 18\).",
                     "choices": [(r"\(x = 4\)", True), (r"\(x = 3.2\)", False),
                                 (r"\(x = 20\)", False), (r"\(x = 16\)", False)]},
                    {"text": (r"A phone plan costs \$20 per month plus \$0.10 per text. Which expression "
                              r"gives the monthly cost for \(t\) texts?"),
                     "choices": [(r"\(0.10t + 20\)", True), (r"\(20t + 0.10\)", False),
                                 (r"\(20.10t\)", False), (r"\(0.10t - 20\)", False)]},
                ],
            },
            {
                "topic": "Geometry & Measurement",
                "recommend": "ged-geometry-mixed-review",
                "questions": [
                    {"text": r"What is the area of a rectangle that is \(8\) cm by \(5\) cm?",
                     "choices": [(r"\(40\ \text{cm}^2\)", True), (r"\(26\ \text{cm}^2\)", False),
                                 (r"\(13\ \text{cm}^2\)", False), (r"\(40\ \text{cm}\)", False)]},
                    {"text": r"What is the perimeter of a rectangle that is \(9\) by \(4\)?",
                     "choices": [(r"\(26\)", True), (r"\(36\)", False), (r"\(13\)", False), (r"\(40\)", False)]},
                    {"text": r"A right triangle has legs of \(6\) and \(8\). How long is the hypotenuse?",
                     "choices": [(r"\(10\)", True), (r"\(14\)", False), (r"\(48\)", False), (r"\(100\)", False)]},
                ],
            },
            {
                "topic": "Data & Statistics",
                "recommend": "ged-data-stats-probability",
                "questions": [
                    {"text": r"What is the mean (average) of \(6,\ 9,\ 12\)?",
                     "choices": [(r"\(9\)", True), (r"\(12\)", False), (r"\(27\)", False), (r"\(6\)", False)]},
                    {"text": r"What is the median of \(4,\ 1,\ 7,\ 3,\ 9\)?",
                     "choices": [(r"\(4\)", True), (r"\(7\)", False), (r"\(4.8\)", False), (r"\(8\)", False)]},
                    {"text": (r"A bag holds 3 red and 5 blue marbles. What is the probability of drawing "
                              r"a red one?"),
                     "choices": [(r"\(\frac{3}{8}\)", True), (r"\(\frac{3}{5}\)", False),
                                 (r"\(\frac{5}{8}\)", False), (r"\(\frac{1}{3}\)", False)]},
                ],
            },
            {
                "topic": "Science",
                "recommend": "ged-science-complete-practice",
                "questions": [
                    {"text": "Which organelle is known as the 'powerhouse of the cell'?",
                     "choices": [("Mitochondrion", True), ("Nucleus", False),
                                 ("Ribosome", False), ("Cell wall", False)]},
                    {"text": "Which gas do plants take IN from the air during photosynthesis?",
                     "choices": [("Carbon dioxide", True), ("Oxygen", False),
                                 ("Nitrogen", False), ("Hydrogen", False)]},
                    {"text": ("In an experiment testing whether fertilizer affects plant growth, what is "
                              "the independent variable (the thing the scientist changes)?"),
                     "choices": [("The amount of fertilizer", True), ("The height of the plants", False),
                                 ("The amount of sunlight", False), ("The type of pot used", False)]},
                ],
            },
            {
                "topic": "Reading & Language",
                "recommend": "ged-language-arts",
                "questions": [
                    {"text": ("Read the passage, then answer.\n\n"
                              "\"Honeybees do far more than make honey. As they move from flower to flower, "
                              "they spread pollen, helping plants produce the fruit and seeds we rely on "
                              "for food.\"\n\n"
                              "What is the main idea of the passage?"),
                     "choices": [("Honeybees help plants reproduce by spreading pollen.", True),
                                 ("Honeybees make honey.", False),
                                 ("Bees move from flower to flower.", False),
                                 ("Fruit contains seeds.", False)]},
                    {"text": "Which sentence uses correct subject-verb agreement?",
                     "choices": [("The box of tools is heavy.", True),
                                 ("The box of tools are heavy.", False),
                                 ("The box of tools were heavy.", False),
                                 ("The box of tools have been heavy.", False)]},
                    {"text": "Which sentence is written correctly?",
                     "choices": [("The company increased its profits this year.", True),
                                 ("The company increased it's profits this year.", False),
                                 ("The company increased its' profits this year.", False),
                                 ("The company increased its profit's this year.", False)]},
                ],
            },
            {
                "topic": "Social Studies",
                "recommend": "ged-social-studies",
                "questions": [
                    {"text": "In the United States government, which branch is responsible for making laws?",
                     "choices": [("The legislative branch (Congress)", True),
                                 ("The executive branch (the President)", False),
                                 ("The judicial branch (the courts)", False),
                                 ("The military", False)]},
                    {"text": "The first ten amendments to the U.S. Constitution are known as the:",
                     "choices": [("Bill of Rights", True), ("Preamble", False),
                                 ("Federalist Papers", False), ("Articles of Confederation", False)]},
                    {"text": "The American Civil War was fought primarily over which issue?",
                     "choices": [("Slavery and the survival of the Union", True),
                                 ("A tax on imported tea", False),
                                 ("Independence from Great Britain", False),
                                 ("Women's right to vote", False)]},
                ],
            },
        ],
    },
    "SAT": {
        "label": "SAT",
        "blurb": "18 questions across 6 topics in SAT Math and Reading & Writing (about 15-20 minutes).",
        "ready_recommend": ["sat-full-length-practice"],
        "topics": [
            {
                "topic": "Algebra",
                "recommend": "sat-math-complete-course",
                "questions": [
                    {"text": r"Solve for \(x\): \(3x - 4 = 11\).",
                     "choices": [(r"\(x = 5\)", True), (r"\(x = 15\)", False),
                                 (r"\(x = \frac{7}{3}\)", False), (r"\(x = 45\)", False)]},
                    {"text": r"What is the slope of the line through \((1, 2)\) and \((3, 8)\)?",
                     "choices": [(r"\(3\)", True), (r"\(\frac{1}{3}\)", False), (r"\(2\)", False), (r"\(6\)", False)]},
                    {"text": r"Solve the system \(x + y = 10\) and \(x - y = 4\). What is \(x\)?",
                     "choices": [(r"\(7\)", True), (r"\(3\)", False), (r"\(6\)", False), (r"\(14\)", False)]},
                ],
            },
            {
                "topic": "Advanced Math",
                "recommend": "sat-math-complete-course",
                "questions": [
                    {"text": r"If \(f(x) = 2x + 1\), what is \(f(3)\)?",
                     "choices": [(r"\(7\)", True), (r"\(6\)", False), (r"\(9\)", False), (r"\(23\)", False)]},
                    {"text": r"Solve \(x^2 - 5x + 6 = 0\).",
                     "choices": [(r"\(x = 2\) or \(x = 3\)", True), (r"\(x = -2\) or \(x = -3\)", False),
                                 (r"\(x = 1\) or \(x = 6\)", False), (r"\(x = 5\) or \(x = 6\)", False)]},
                    {"text": r"Simplify \(2^3 \cdot 2^4\).",
                     "choices": [(r"\(128\)", True), (r"\(64\)", False), (r"\(2^{12}\)", False), (r"\(16\)", False)]},
                ],
            },
            {
                "topic": "Problem-Solving & Data",
                "recommend": "sat-math-complete-course",
                "questions": [
                    {"text": r"A shirt costs \$50 and is marked \(20\%\) off. What is the sale price?",
                     "choices": [(r"\$40", True), (r"\$10", False), (r"\$30", False), (r"\$70", False)]},
                    {"text": r"\(30\) is what percent of \(120\)?",
                     "choices": [(r"\(25\%\)", True), (r"\(40\%\)", False), (r"\(4\%\)", False), (r"\(90\%\)", False)]},
                    {"text": r"What is the mean (average) of \(4,\ 8,\ 10,\ 10,\ 8\)?",
                     "choices": [(r"\(8\)", True), (r"\(10\)", False), (r"\(40\)", False), (r"\(9\)", False)]},
                ],
            },
            {
                "topic": "Words in Context",
                "recommend": "sat-reading-writing-complete",
                "questions": [
                    {"text": ("\"The instructions were so ______ that even a complete beginner could "
                              "follow them without any help.\"\n\n"
                              "Which choice completes the text with the most logical and precise word?"),
                     "choices": [("clear", True), ("confusing", False), ("lengthy", False), ("technical", False)]},
                    {"text": ("\"The committee's decision was not final; it was provisional, meant to be "
                              "revisited once more data became available.\"\n\n"
                              "As used in the text, \"provisional\" most nearly means"),
                     "choices": [("temporary.", True), ("permanent.", False), ("popular.", False), ("secret.", False)]},
                    {"text": ("\"Far from being ______, the senator's speech was packed with concrete "
                              "proposals and specific figures.\"\n\n"
                              "Which choice completes the text with the most logical and precise word?"),
                     "choices": [("vague", True), ("detailed", False), ("lengthy", False), ("honest", False)]},
                ],
            },
            {
                "topic": "Command of Evidence",
                "recommend": "sat-reading-writing-complete",
                "questions": [
                    {"text": ("A researcher claims that a new study method improves students' test scores. "
                              "Which finding, if true, would most directly support this claim?"),
                     "choices": [("Students who used the method scored higher than those who did not.", True),
                                 ("The method is quick and easy to learn.", False),
                                 ("Many students say they enjoy studying.", False),
                                 ("The tests are given at the end of the school year.", False)]},
                    {"text": ("A biologist hypothesizes that planting native wildflowers along roadsides "
                              "increases the local bee population. Which finding, if true, would most "
                              "directly support this hypothesis?"),
                     "choices": [("Roadsides planted with wildflowers had more bees than unplanted ones.", True),
                                 ("Native wildflowers are inexpensive to plant.", False),
                                 ("Many people find wildflowers attractive.", False),
                                 ("Bees are important pollinators worldwide.", False)]},
                    {"text": ("\"The streets were soaked, puddles dotted the sidewalks, and people shook "
                              "out their umbrellas as they stepped indoors. It had clearly just ______\"\n\n"
                              "Which choice most logically completes the text?"),
                     "choices": [("rained.", True), ("turned very dry.", False),
                                 ("grown windy.", False), ("become much colder.", False)]},
                ],
            },
            {
                "topic": "Grammar & Conventions",
                "recommend": "sat-reading-writing-complete",
                "questions": [
                    {"text": ("Which choice conforms to the conventions of Standard English?\n\n"
                              "\"After a long season, the team finally celebrated ______ first championship.\""),
                     "choices": [("its", True), ("it's", False), ("its'", False), ("it is", False)]},
                    {"text": ("Which choice conforms to the conventions of Standard English?\n\n"
                              "\"The collection of rare coins ______ on display in a locked case.\""),
                     "choices": [("is", True), ("are", False), ("were", False), ("have been", False)]},
                    {"text": ("Which choice completes the text with the most logical transition?\n\n"
                              "\"The forecast had predicted clear skies. ______ it rained steadily all "
                              "afternoon.\""),
                     "choices": [("However,", True), ("Therefore,", False),
                                 ("For example,", False), ("Similarly,", False)]},
                ],
            },
        ],
    },
}


def get_diagnostic(program):
    """Return the diagnostic dict for a program code, or None."""
    return DIAGNOSTICS.get((program or "").upper())


def iter_questions(data):
    """Yield (global_index, topic_label, recommend_slug, question) across all topics."""
    idx = 0
    for topic in data["topics"]:
        for question in topic["questions"]:
            yield idx, topic["topic"], topic["recommend"], question
            idx += 1


def correct_index(question):
    """Index of the correct choice in a question's choice list."""
    for i, (_text, is_correct) in enumerate(question["choices"]):
        if is_correct:
            return i
    return -1


def topic_needs_review(correct, total):
    """A topic is proficient at two-thirds correct or better; below that, recommend review.

    With three questions per topic this means: 2 or 3 correct = proficient (one
    careless slip is tolerated); 0 or 1 correct = needs review.
    """
    return correct * 3 < total * 2
