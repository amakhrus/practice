"""
Seed the capstone 'GED Full-Length Practice Test' course -- one comprehensive
mixed test that samples all four GED subject tests:

  - Mathematical Reasoning  (~30% here): basic math, algebra, geometry, data
  - Science                 (~25%): life, physical, and earth/space + reasoning
  - Reasoning Through Language Arts (~25%): reading + grammar/editing
  - Social Studies          (~20%): civics, history, geography, economics

On the real GED these are four *separate* tests, each scored 100-200 (145 to
pass). This course mixes them into a single review so a student can rehearse
every subject in one place. Items are fresh (not copied from the subject
courses), written in the capstone style: every explanation names the tempting
wrong answer and ends with a Pro tip, and several questions reuse the diagram
library now that question text supports figures. Multiple choice only (the GED
Extended Response essay is described in the lessons but not auto-graded here).

This course is filed under the 'other' subject because it spans all four.

Run:
    python manage.py seed_ged_full_practice
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Full-Length Practice Test (Math, Science, RLA & Social Studies)",
    "slug": "ged-full-length-practice",
    "program": "GED",
    "subject": "other",
    "description": (
        "A capstone full-length GED practice test that mixes all four subjects into one "
        "comprehensive review: Mathematical Reasoning (basic math, algebra, geometry, and data), "
        "Science (life, physical, and earth and space science plus scientific reasoning), Reasoning "
        "Through Language Arts (reading comprehension and grammar/editing), and Social Studies "
        "(civics, history, geography, and economics). Fresh, exam-style multiple-choice questions "
        "with full explanations and pro tips, plus quick subject recaps and a test-day game plan, "
        "so you can rehearse the whole GED in one place before test day."
    ),
    "lessons": [
        (
            "1. How the GED Works",
            r"""
The GED is made up of **four separate subject tests**, and this practice test mixes all four into one review:

- **Mathematical Reasoning** -- about 46 questions in 115 minutes (a calculator is allowed after the first few questions, and a formula sheet is provided).
- **Reasoning Through Language Arts (RLA)** -- reading comprehension, grammar/editing, and a written **Extended Response** essay.
- **Science** -- about 34 questions in 90 minutes, built around passages, graphs, and data.
- **Social Studies** -- about 35 questions in 70 minutes, built around documents, maps, and charts.

Each test is scored from **100 to 200**, and you need **145 to pass** each one. Importantly, you take the four tests **separately**, not in a single sitting -- so you can prepare for and pass them one at a time.

Two habits carry across every GED subject:
- **Use the source.** Science and Social Studies hand you the passage, graph, or map you need -- the answer is usually right there.
- **It's multiple choice.** When stuck on math, you can test the answer choices instead of doing all the algebra.

[[check:What score do you need to pass each GED subject test?|145|Each test is scored 100-200.]]
            """,
        ),
        (
            "2. Math: Quick Strategy Recap",
            r"""
GED Mathematical Reasoning covers basic math (fractions, decimals, percents, ratios), algebra, geometry, and data.

[[figure:ged_math_roadmap|The major math topics. A mixed test will jump between them, so name the topic first.]]

Smart habits for a mixed math section:
- **Read the last line.** Know whether the question wants the area or the perimeter, the price or the discount.
- **Backsolve.** If the choices are numbers, plug them into the problem (start in the middle) instead of doing all the algebra.
- **Use the formula sheet.** The GED gives you one -- don't try to memorize every area and volume formula.
- **Mind the units.** Length is plain units, area is square units, volume is cubic units.

[[check:On a math question with numeric answer choices, what fast strategy lets you avoid the algebra?|backsolve;;backsolving;;plug in the answers|Test the choices in the problem.]]
            """,
        ),
        (
            "3. Science & Social Studies: Read the Source",
            r"""
Science and Social Studies feel different, but they reward the **same skill**: pulling answers from a passage, graph, table, or map.

A reliable routine for any source:
- Read the **title** and any **labels or units** first -- what is being shown?
- Find the **specific value or trend** the question asks about.
- Stick to what the source **shows**; don't add outside assumptions.

Two ideas the GED tests over and over:
- **Correlation is not causation.** Two things rising together doesn't prove one caused the other.
- **Read graphs carefully.** Check the scale -- a small-looking bar can stand for a large number.

In Social Studies, also watch for **point of view and purpose**: a political cartoon or speech is often trying to persuade, so ask what side it is taking.

[[check:Two things rise together in a graph. Does that prove one caused the other? Answer yes or no.|no|A third factor could cause both.]]
            """,
        ),
        (
            "4. Reading & Language (RLA) + the Extended Response",
            r"""
RLA measures three things: **reading** for meaning, **editing** for correct grammar, and **writing** the Extended Response essay.

For **reading** questions:
- The **main idea** must cover the whole passage, not one detail.
- An **inference** is supported by clues in the text -- you should be able to point to the words behind your answer.
- The best **evidence** for a claim is specific and checkable, not just a strong opinion.

For **grammar/editing** questions, watch the usual suspects:
- **Subject-verb agreement** (match the verb to the real subject).
- **Run-ons and fragments** (a sentence needs a subject, a verb, and a complete thought).
- **Commonly confused words:** its/it's, their/there/they're, your/you're.

The **Extended Response** gives you two passages arguing opposite sides and asks which argument is **better supported by evidence** -- not which you personally agree with. You have about 45 minutes. (This practice test is multiple choice, so the essay isn't graded here, but the reading and grammar questions build exactly the skills it needs.)

[[check:In the Extended Response, are you graded on your personal opinion or on which argument is better supported? Answer with one word: opinion or supported.|supported|Judge the arguments using evidence.]]
            """,
        ),
        (
            "5. Test-Day Game Plan",
            r"""
You have the subject skills; this is about using them well.

**Pacing.** Each GED test gives you a bit over a minute per question. If one stalls you, mark your best guess and move on -- there's time to come back.

**Never leave a blank.** There is **no penalty** for a wrong answer, so a guess always beats an empty box. Eliminate what you can, then choose.

**Take the tests one at a time.** Because the four subjects are separate tests, you can focus your studying and schedule them when you're ready for each. Pass them one by one.

**Use what the test gives you:** the calculator and formula sheet in math, and the passages, graphs, and maps in every subject.

[[check:Is there any penalty for a wrong answer on the GED? Answer yes or no.|no|So always guess rather than leave a blank.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ===================== MATHEMATICAL REASONING ========================
        # =====================================================================
        {
            "text": r"What is \(\frac{2}{3} + \frac{1}{6}\)?",
            "difficulty": 2,
            "choices": [(r"\(\frac{5}{6}\)", True), (r"\(\frac{3}{9}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(\frac{3}{6}\)", False)],
            "explanation": r"Use a common denominator of 6: \(\frac{2}{3} = \frac{4}{6}\), so \(\frac{4}{6} + \frac{1}{6} = \frac{5}{6}\). The trap \(\frac{3}{9}\) adds tops and bottoms separately. Pro tip: you can only add fractions once the denominators match.",
        },
        {
            "text": r"A \$60 jacket is marked \(15\%\) off. What is the sale price?",
            "difficulty": 2,
            "choices": [(r"\$51", True), (r"\$9", False), (r"\$45", False), (r"\$69", False)],
            "explanation": r"The discount is \(0.15 \times 60 = \$9\), so the price is \(60 - 9 = \$51\). The trap \$9 gives only the discount; \$45 over-subtracts. Pro tip: 15% off means you pay 85%: \(0.85 \times 60 = 51\).",
        },
        {
            "text": r"A recipe uses 3 cups of flour to make 12 cookies. How many cups are needed for 20 cookies?",
            "difficulty": 2,
            "choices": [(r"\(5\) cups", True), (r"\(9\) cups", False), (r"\(80\) cups", False), (r"\(4\) cups", False)],
            "explanation": r"Set up a proportion: \(\frac{3}{12} = \frac{x}{20}\), so \(12x = 60\) and \(x = 5\). The trap 80 cross-multiplies the wrong pair. Pro tip: keep the same units across from each other (cups over cookies).",
        },
        {
            "text": r"Solve for \(x\): \(4x - 3 = 17\).",
            "difficulty": 1,
            "choices": [(r"\(x = 5\)", True), (r"\(x = 20\)", False), (r"\(x = 3.5\)", False), (r"\(x = 14\)", False)],
            "explanation": r"Add 3: \(4x = 20\). Divide by 4: \(x = 5\). The trap 20 forgets to divide. Pro tip: undo the \(-3\) first, then the \(\times 4\).",
        },
        {
            "text": (r"A gym charges a \$25 sign-up fee plus \$15 per month. Which expression gives the total "
                     r"cost for \(m\) months?"),
            "difficulty": 2,
            "choices": [(r"\(15m + 25\)", True), (r"\(25m + 15\)", False), (r"\(40m\)", False), (r"\(15m - 25\)", False)],
            "explanation": r"The monthly cost \(15m\) is added to the one-time \$25 fee: \(15m + 25\). The trap \(25m + 15\) swaps the rate and the fee. Pro tip: the 'per month' amount multiplies the variable; the one-time fee is the constant.",
        },
        {
            "text": r"Solve the inequality \(2x + 1 \le 9\).",
            "difficulty": 2,
            "choices": [(r"\(x \le 4\)", True), (r"\(x \ge 4\)", False), (r"\(x \le 5\)", False), (r"\(x \le 8\)", False)],
            "explanation": r"Subtract 1: \(2x \le 8\). Divide by 2: \(x \le 4\). The sign does not flip because 2 is positive. Pro tip: only flip the inequality when you divide by a negative.",
        },
        {
            "text": r"What is the area of a triangle with a base of \(10\) cm and a height of \(6\) cm?",
            "difficulty": 1,
            "choices": [(r"\(30\ \text{cm}^2\)", True), (r"\(60\ \text{cm}^2\)", False), (r"\(16\ \text{cm}^2\)", False), (r"\(8\ \text{cm}^2\)", False)],
            "explanation": r"\(A = \tfrac{1}{2} b h = \tfrac{1}{2}(10)(6) = 30\ \text{cm}^2\). The trap 60 forgets the \(\tfrac{1}{2}\). Pro tip: every triangle area starts with one-half.",
        },
        {
            "text": r"What is the volume of a box measuring \(4 \times 3 \times 5\)?",
            "difficulty": 1,
            "choices": [(r"\(60\)", True), (r"\(12\)", False), (r"\(47\)", False), (r"\(23\)", False)],
            "explanation": r"Volume multiplies all three dimensions: \(4 \times 3 \times 5 = 60\). The trap 12 multiplies only two. Pro tip: volume uses cubic units and all three sides.",
        },
        {
            "text": ("Use the right triangle shown.\n\n"
                     "[[figure:pythagorean_triangle|The two legs and the hypotenuse of a right triangle]]\n\n"
                     "If the two legs of a right triangle are 9 and 12, how long is the hypotenuse?"),
            "difficulty": 2,
            "choices": [(r"\(15\)", True), (r"\(21\)", False), (r"\(225\)", False), (r"\(18\)", False)],
            "explanation": r"\(c = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15\). The trap 21 adds the legs; 225 forgets the square root. Pro tip: 9-12-15 is the 3-4-5 triple times 3.",
        },
        {
            "text": r"What is the mean (average) of \(5,\ 7,\ 9,\ 11\)?",
            "difficulty": 1,
            "choices": [(r"\(8\)", True), (r"\(9\)", False), (r"\(32\)", False), (r"\(7\)", False)],
            "explanation": r"Add them: \(5+7+9+11 = 32\); divide by 4: \(32 \div 4 = 8\). The trap 32 forgets to divide. Pro tip: mean = total divided by how many values.",
        },
        {
            "text": r"What is the median of \(4,\ 1,\ 7,\ 3,\ 9\)?",
            "difficulty": 2,
            "choices": [(r"\(4\)", True), (r"\(7\)", False), (r"\(4.8\)", False), (r"\(8\)", False)],
            "explanation": r"Put them in order first: \(1, 3, 4, 7, 9\). The middle value is 4. The trap 4.8 is the mean; 8 is the range. Pro tip: always sort the list before finding the median.",
        },
        {
            "text": (r"A bag holds 3 red marbles and 5 blue marbles. If you draw one at random, what is the "
                     r"probability it is red?"),
            "difficulty": 2,
            "choices": [(r"\(\frac{3}{8}\)", True), (r"\(\frac{3}{5}\)", False), (r"\(\frac{5}{8}\)", False), (r"\(\frac{1}{3}\)", False)],
            "explanation": r"There are \(3 + 5 = 8\) marbles total, 3 of them red, so \(P(\text{red}) = \frac{3}{8}\). The trap \(\frac{3}{5}\) compares red to blue instead of to the total. Pro tip: probability is the favorable count over the TOTAL count.",
        },
        {
            "text": ("Use the line graph below.\n\n"
                     "[[figure:line_sales|A store's monthly sales in dollars]]\n\n"
                     "According to the graph, by about how much did sales increase from January to "
                     "February?"),
            "difficulty": 2,
            "choices": [(r"about \$150", True), (r"about \$550", False), (r"about \$350", False), (r"about \$100", False)],
            "explanation": r"Sales rose from about \$200 in January to about \$350 in February, an increase of \(350 - 200 = \$150\). The trap \$350 is February's total, not the increase. Pro tip: an 'increase' is the difference between the two values, not one of them.",
        },
        {
            "text": r"A store's revenue rose from \$2{,}000 to \$2{,}500 in a month. What was the percent increase?",
            "difficulty": 3,
            "choices": [(r"\(25\%\)", True), (r"\(20\%\)", False), (r"\(50\%\)", False), (r"\(500\%\)", False)],
            "explanation": r"Percent change \(= \frac{\text{new}-\text{old}}{\text{old}} = \frac{2500-2000}{2000} = \frac{500}{2000} = 0.25 = 25\%\). The trap 20% divides by the new amount. Pro tip: for percent change, always divide by the ORIGINAL value.",
        },
        # =====================================================================
        # ============================= SCIENCE ===============================
        # =====================================================================
        {
            "text": r"Which organelle is the control center of the cell, holding its DNA?",
            "difficulty": 1,
            "choices": [("The nucleus", True), ("The mitochondrion", False), ("The ribosome", False), ("The cell wall", False)],
            "explanation": r"The nucleus stores the cell's DNA and directs its activities. The trap, the mitochondrion, is the 'powerhouse' that releases energy. Pro tip: nucleus = control center; mitochondria = energy.",
        },
        {
            "text": r"Which gas do plants take IN from the air during photosynthesis?",
            "difficulty": 1,
            "choices": [("Carbon dioxide", True), ("Oxygen", False), ("Nitrogen", False), ("Hydrogen", False)],
            "explanation": r"Plants take in carbon dioxide and release oxygen during photosynthesis. The trap, oxygen, is what they give off. Pro tip: photosynthesis takes in CO2 and water and makes sugar and oxygen.",
        },
        {
            "text": (r"Two parents are each Bb, where B (brown) is dominant over b (blue). What fraction of "
                     r"their offspring is expected to show the blue (recessive) trait?"),
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{3}{4}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(0\)", False)],
            "explanation": r"A Bb x Bb cross gives BB, Bb, Bb, bb. Only bb (1 of 4) shows the recessive trait, so \(\frac{1}{4}\). The trap \(\frac{3}{4}\) is the dominant share. Pro tip: a recessive trait needs two recessive alleles.",
        },
        {
            "text": ("Use the food chain shown.\n\n"
                     "[[figure:food_chain|A simple food chain with arrows]]\n\n"
                     "What do the arrows in a food chain represent?"),
            "difficulty": 2,
            "choices": [("The flow of energy from one organism to the next", True),
                        ("The direction in which animals migrate", False),
                        ("Which animal is the largest", False),
                        ("Where the animals sleep at night", False)],
            "explanation": r"Arrows point from the organism being eaten toward the one eating it, showing the direction energy flows. The traps invent unrelated meanings. Pro tip: follow the arrow to see where the energy goes.",
        },
        {
            "text": r"When a solid is heated until it melts into a liquid, its particles:",
            "difficulty": 2,
            "choices": [("Gain energy and move faster, spreading farther apart", True),
                        ("Lose energy and pack closer together", False),
                        ("Disappear completely", False),
                        ("Turn into a different element", False)],
            "explanation": r"Heat adds energy, so particles move faster and spread out as a solid becomes a liquid. The trap reverses this. Pro tip: more heat means more particle motion.",
        },
        {
            "text": r"Which subatomic particle carries a negative charge?",
            "difficulty": 1,
            "choices": [("The electron", True), ("The proton", False), ("The neutron", False), ("The nucleus", False)],
            "explanation": r"Electrons are negative and orbit the nucleus. The trap, the proton, is positive; neutrons are neutral. Pro tip: electron = negative, proton = positive, neutron = neutral.",
        },
        {
            "text": r"Which of the following is a chemical change?",
            "difficulty": 2,
            "choices": [("Wood burning into ash", True), ("Ice melting into water", False),
                        ("Water boiling into steam", False), ("A glass shattering", False)],
            "explanation": r"Burning forms new substances (ash, smoke, gases), so it is a chemical change. The traps are physical changes -- same substance in a new form. Pro tip: new substance = chemical; same substance = physical.",
        },
        {
            "text": ("Use the water cycle diagram.\n\n"
                     "[[figure:water_cycle|The stages of the water cycle]]\n\n"
                     "Which process in the water cycle turns liquid water into water vapor?"),
            "difficulty": 2,
            "choices": [("Evaporation", True), ("Condensation", False), ("Precipitation", False), ("Collection", False)],
            "explanation": r"Evaporation uses the Sun's heat to turn liquid water into vapor. The trap, condensation, is the reverse (vapor back to liquid). Pro tip: evaporation goes up as vapor; condensation comes back as droplets.",
        },
        {
            "text": r"What causes the seasons on Earth?",
            "difficulty": 2,
            "choices": [("The tilt of Earth's axis", True),
                        ("Earth's changing distance from the Sun", False),
                        ("The phases of the Moon", False),
                        ("Solar flares from the Sun", False)],
            "explanation": r"Earth's tilt means each hemisphere leans toward or away from the Sun across the year. The trap (distance) is a common misconception -- Earth is actually closest to the Sun in northern winter. Pro tip: seasons come from tilt, not distance.",
        },
        {
            "text": (r"A scientist tests whether playing music helps tomato plants grow taller. To make it a "
                     r"fair test, what should she keep the SAME for both groups of plants?"),
            "difficulty": 2,
            "choices": [("The water, sunlight, and soil", True),
                        ("Whether or not music is played", False),
                        ("The final height of the plants", False),
                        ("Nothing needs to be kept the same", False)],
            "explanation": r"Controlled variables (water, sunlight, soil) must be identical so the only difference is the music. The trap (whether music plays) is the variable she is testing. Pro tip: a fair test changes only one thing and holds the rest constant.",
        },
        {
            "text": (r"A town finds that as ice-cream sales rise, the number of sunburns also rises. What is "
                     r"the best conclusion?"),
            "difficulty": 3,
            "choices": [("A third factor, like hot sunny weather, likely causes both", True),
                        ("Eating ice cream causes sunburns", False),
                        ("Sunburns make people buy ice cream", False),
                        ("The data must be incorrect", False)],
            "explanation": r"This is correlation, not causation -- hot weather drives both. The traps invent a direct cause the data can't support. Pro tip: when two things rise together, ask whether a third factor explains both.",
        },
        # =====================================================================
        # =============== REASONING THROUGH LANGUAGE ARTS (RLA) ===============
        # =====================================================================
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Sea otters are more than charming sea creatures. By eating sea urchins, they "
                     "protect kelp forests, which the urchins would otherwise devour. Healthy kelp "
                     "forests, in turn, shelter countless other ocean species.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Sea otters help keep entire kelp-forest ecosystems healthy.", True),
                        ("Sea otters are charming animals.", False),
                        ("Sea urchins eat kelp.", False),
                        ("Many species live in the ocean.", False)],
            "explanation": r"The whole passage builds to one point: by eating urchins, otters protect kelp forests and the species that depend on them. The other choices are single details. Pro tip: the main idea must cover the whole passage, not one fact.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Sea otters are more than charming sea creatures. By eating sea urchins, they "
                     "protect kelp forests, which the urchins would otherwise devour.\"\n\n"
                     "According to the passage, what do sea otters eat that protects the kelp forests?"),
            "difficulty": 1,
            "choices": [("Sea urchins", True), ("Kelp", False), ("Fish", False), ("Crabs", False)],
            "explanation": r"The passage states directly that otters protect kelp by eating sea urchins. The traps are never mentioned. Pro tip: for a detail question, point to the exact words in the text.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Dark clouds gathered overhead, the wind picked up sharply, and the vendors began "
                     "hurriedly covering their stalls with tarps.\"\n\n"
                     "What can you most reasonably infer from this passage?"),
            "difficulty": 2,
            "choices": [("A storm is about to arrive.", True),
                        ("It is the middle of the night.", False),
                        ("The market is closing down for good.", False),
                        ("A parade is about to begin.", False)],
            "explanation": r"Gathering clouds, rising wind, and vendors covering stalls all point to an approaching storm. The other choices aren't supported by those clues. Pro tip: a good inference is backed by specific words in the text.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"You owe it to yourself and your community to vote in every election. Your voice "
                     "matters, and a healthy democracy depends on people like you showing up.\"\n\n"
                     "What is the author's main purpose?"),
            "difficulty": 2,
            "choices": [("To persuade readers to vote", True),
                        ("To inform readers of election dates", False),
                        ("To entertain readers with a story", False),
                        ("To describe what a polling place looks like", False)],
            "explanation": r"The author urges a course of action ('you owe it to yourself … to vote'), which is persuasion. The traps describe other purposes the passage doesn't serve. Pro tip: language that pushes you to act or believe signals a persuasive purpose.",
        },
        {
            "text": ("Read the sentence, then answer.\n\n"
                     "\"The so-called 'improvement' to the old park was a disaster that wasted millions of "
                     "dollars.\"\n\n"
                     "The author's tone in this sentence is best described as:"),
            "difficulty": 2,
            "choices": [("Critical and disapproving", True),
                        ("Cheerful and enthusiastic", False),
                        ("Neutral and objective", False),
                        ("Joyful and hopeful", False)],
            "explanation": r"'So-called,' 'disaster,' and 'wasted millions' all express strong disapproval. The traps describe the opposite or a neutral tone. Pro tip: loaded, negative word choices reveal a critical tone.",
        },
        {
            "text": ("Read the sentence, then answer.\n\n"
                     "\"The evidence against the suspect was irrefutable; not a single person in the "
                     "courtroom could argue against it.\"\n\n"
                     "As used here, \"irrefutable\" most nearly means:"),
            "difficulty": 2,
            "choices": [("Impossible to disprove", True), ("Easy to ignore", False),
                        ("Against the law", False), ("Small and unimportant", False)],
            "explanation": r"The clue 'not a single person … could argue against it' shows 'irrefutable' means impossible to disprove. Pro tip: the rest of the sentence usually defines a hard vocabulary word.",
        },
        {
            "text": ("Which of the following would be the STRONGEST evidence to support the claim that "
                     "\"our town needs a new library\"?"),
            "difficulty": 3,
            "choices": [("A survey showing that 80% of residents live far from any library", True),
                        ("The writer's personal love of reading books", False),
                        ("The general idea that libraries are nice to have", False),
                        ("The fact that some other towns have new libraries", False)],
            "explanation": r"Strong evidence is specific and checkable -- a survey with a concrete statistic directly supports the need. Feelings and vague generalities are not solid evidence. Pro tip: the best evidence is factual and directly tied to the claim.",
        },
        {
            "text": "Which sentence uses correct subject-verb agreement?",
            "difficulty": 2,
            "choices": [("Each of the students has a locker.", True),
                        ("Each of the students have a locker.", False),
                        ("Each of the students were a locker.", False),
                        ("Each of the students having a locker.", False)],
            "explanation": r"The subject is 'Each' (singular), so it takes the singular verb 'has' -- the phrase 'of the students' doesn't change that. Pro tip: words like 'each,' 'every,' and 'one' are singular.",
        },
        {
            "text": "Which of the following is a complete, correctly written sentence?",
            "difficulty": 2,
            "choices": [("The rain finally stopped, so we went outside.", True),
                        ("Because the rain finally stopped.", False),
                        ("The rain finally stopped we went outside.", False),
                        ("Finally stopped and went outside.", False)],
            "explanation": r"The correct option has two complete ideas joined properly by 'so.' 'Because the rain finally stopped' is a fragment; the third option is a run-on; the last has no subject. Pro tip: a sentence needs a subject, a verb, and a complete thought.",
        },
        {
            "text": "Which sentence uses the correct words?",
            "difficulty": 1,
            "choices": [("They're bringing their lunches over there.", True),
                        ("Their bringing they're lunches over there.", False),
                        ("There bringing their lunches over they're.", False),
                        ("They're bringing there lunches over their.", False)],
            "explanation": r"'They're' = they are; 'their' = belonging to them; 'there' = a place. Only the first sentence uses all three correctly. Pro tip: expand 'they're' to 'they are' to test it.",
        },
        {
            "text": ("Which choice is the most logical transition?\n\n"
                     "\"The new plan was expensive. ______ the council approved it, because the long-term "
                     "benefits were clear.\""),
            "difficulty": 2,
            "choices": [("Nevertheless,", True), ("Therefore,", False), ("For example,", False), ("Meanwhile,", False)],
            "explanation": r"The cost would normally argue against approval, but the council approved it anyway -- a contrast, so 'Nevertheless' fits. 'Therefore' would wrongly make the cost the reason for approval. Pro tip: a surprising result calls for a contrast word.",
        },
        # =====================================================================
        # ========================= SOCIAL STUDIES ============================
        # =====================================================================
        {
            "text": ("Use the diagram of the U.S. government.\n\n"
                     "[[figure:three_branches|The three branches of the U.S. government]]\n\n"
                     "Based on the diagram, which branch is responsible for enforcing the laws?"),
            "difficulty": 2,
            "choices": [("The executive branch (the President)", True),
                        ("The legislative branch (Congress)", False),
                        ("The judicial branch (the courts)", False),
                        ("The state governments", False)],
            "explanation": r"The diagram shows the executive branch (the President) enforcing the laws. The legislative branch makes them and the judicial branch interprets them. Pro tip: read the role labeled under each branch in the source.",
        },
        {
            "text": r"Which document begins with the words 'We the People' and establishes the framework of the U.S. government?",
            "difficulty": 2,
            "choices": [("The U.S. Constitution", True),
                        ("The Declaration of Independence", False),
                        ("The Emancipation Proclamation", False),
                        ("The Articles of Confederation", False)],
            "explanation": r"The Constitution's Preamble begins 'We the People' and sets up the government. The Declaration of Independence (1776) announced separation from Britain instead. Pro tip: Constitution = the rules of government; Declaration = the break from Britain.",
        },
        {
            "text": r"The first ten amendments to the U.S. Constitution are collectively known as the:",
            "difficulty": 1,
            "choices": [("Bill of Rights", True), ("Preamble", False),
                        ("Federalist Papers", False), ("Articles of Confederation", False)],
            "explanation": r"The first ten amendments are the Bill of Rights, protecting freedoms like speech and religion. The Federalist Papers were essays arguing for the Constitution, not part of it. Pro tip: 'first ten amendments' = Bill of Rights.",
        },
        {
            "text": (r"The President can veto a bill, but Congress can override that veto with a two-thirds "
                     r"vote. This is an example of:"),
            "difficulty": 2,
            "choices": [("Checks and balances", True), ("Federalism", False),
                        ("Free enterprise", False), ("Popular sovereignty", False)],
            "explanation": r"Each branch can limit the others (veto vs. override), which is checks and balances. Federalism is the split between national and state power -- a different idea. Pro tip: when branches limit each other, that's checks and balances.",
        },
        {
            "text": r"The American Civil War (1861-1865) was fought primarily over which issue?",
            "difficulty": 2,
            "choices": [("Slavery and the survival of the Union", True),
                        ("A tax on imported tea", False),
                        ("Independence from Great Britain", False),
                        ("Women's right to vote", False)],
            "explanation": r"The Civil War centered on slavery and whether the Union would hold together. The tea tax and independence belong to the Revolutionary era; women's suffrage came later. Pro tip: match the event to its time period to rule out wrong eras.",
        },
        {
            "text": ("Use the graph of supply and demand.\n\n"
                     "[[figure:supply_demand|Supply and demand curves for a good]]\n\n"
                     "Based on the demand curve, as the price of a good increases, the quantity that "
                     "consumers demand usually:"),
            "difficulty": 2,
            "choices": [("Decreases", True), ("Increases", False),
                        ("Stays exactly the same", False), ("Doubles", False)],
            "explanation": r"The downward-sloping demand curve shows that higher prices lead to lower quantity demanded -- the law of demand. The trap 'increases' describes supply, not demand. Pro tip: demand slopes down; as price goes up, buyers want less.",
        },
        {
            "text": r"A tax that a government places on goods brought in from other countries is called a:",
            "difficulty": 2,
            "choices": [("Tariff", True), ("Subsidy", False), ("Surplus", False), ("Deficit", False)],
            "explanation": r"A tariff is a tax on imports. A subsidy is government money given to support a business; a deficit is spending more than you take in. Pro tip: tariff = tax at the border on imported goods.",
        },
        {
            "text": r"On a map, the lines that run east-west and measure distance north or south of the equator are called:",
            "difficulty": 2,
            "choices": [("Lines of latitude", True), ("Lines of longitude", False),
                        ("Prime meridians", False), ("Time zones", False)],
            "explanation": r"Latitude lines run east-west and measure north-south position (the equator is 0 degrees latitude). Longitude lines run north-south instead. Pro tip: latitude is like the rungs of a ladder -- flat, going up and down.",
        },
        {
            "text": r"Which of the following is a basic responsibility of citizens in a democracy?",
            "difficulty": 1,
            "choices": [("Voting in elections", True),
                        ("Owning a home", False),
                        ("Serving as President", False),
                        ("Starting a business", False)],
            "explanation": r"Voting is a core civic responsibility that keeps a democracy working. The other choices are personal choices or opportunities, not duties of citizenship. Pro tip: think about what keeps self-government running -- participation like voting.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the capstone full-length GED practice-test course (all four subjects; MCQ only)."

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
            Lesson.objects.create(course=course, title=title, content=content.strip(), order=i)

        for q in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course, qtype="mcq", text=q["text"],
                difficulty=q["difficulty"], explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)

        # The GED Extended Response essay is described in the lessons but not auto-graded here.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
