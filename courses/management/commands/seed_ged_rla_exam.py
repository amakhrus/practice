"""
Seed a full-length 'GED Reasoning Through Language Arts (RLA)' practice exam that
mirrors the real test environment as closely as a multiple-choice LMS can:

  - 46 questions total, modeled on the real GED RLA test length.
  - Two question parts, like test day:
        Part 1 -- Reading Comprehension (informational + literary passages).
        Part 2 -- Language & Editing (grammar and conventions).
  - 150 minutes total, scored 100-200 (145 to pass), with an Extended Response
    essay that the real test grades but this practice exam only describes (the
    reading and language items build exactly the skills the essay needs).
  - A realistic difficulty spread (easy / medium / hard) -- this is Level 1,
    the foundational tier.

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip.

Run:
    python manage.py seed_ged_rla_exam
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Full-Length Practice Exam (Level 1 - Foundational)",
    "slug": "ged-rla-exam",
    "program": "GED",
    "subject": "rla",
    "description": (
        "A full-length, test-day-style GED Reasoning Through Language Arts (RLA) practice exam: 46 "
        "questions modeled on the real blueprint, split into a Reading Comprehension section "
        "(informational and literary passages) and a Language & Editing section (grammar and "
        "conventions), with the Extended Response essay described in the lessons. It covers the core "
        "tested skills -- main idea and details, inference, author's purpose and tone, vocabulary in "
        "context, sentence structure, subject-verb agreement, punctuation, and commonly confused words "
        "-- at a foundational, easy-to-hard difficulty spread. Every question includes a worked "
        "explanation and a pro tip. Use the lessons to learn the test format (150 minutes, scored "
        "100-200, 145 to pass) before taking the 46 questions as one timed rehearsal."
    ),
    "lessons": [
        (
            "1. How the GED RLA Test Works",
            r"""
This exam is built to feel like the **real GED Reasoning Through Language Arts (RLA) test**. Here is what you are walking into:

- **About 46 questions** plus one **Extended Response essay**, in **150 minutes** total.
- The real test comes in **three timed sections**:
  - **Section 1** -- reading and language questions (about 35 minutes).
  - **Section 2** -- the **Extended Response** essay (45 minutes).
  - **Section 3** -- more reading and language questions (about 60 minutes), after a short break.
- Most questions (about **75%**) are **reading comprehension** -- you are given a passage and asked about it. The rest test **language and editing** (grammar, sentence structure, and word choice).
- The **Extended Response** gives you two passages arguing opposite sides and asks which argument is **better supported by evidence**. This practice exam is multiple choice, so the essay isn't graded here -- but the reading and language questions build exactly the skills it needs.

**Scoring:** the RLA test is scored from **100 to 200**, and you need **145 to pass**. There is **no penalty for a wrong answer**, so never leave a question blank.

[[check:What score do you need to pass the GED RLA test?|145|Each GED test is scored 100-200, and 145 passes.]]
            """,
        ),
        (
            "2. Reading Skills the Test Rewards",
            r"""
Three out of four questions ask you to read closely. The skills tested over and over:

- **Main idea** -- the one point the *whole* passage makes, not a single detail and not a vague generalization.
- **Supporting details** -- specific facts the passage actually states; for these, point to the exact words.
- **Inference** -- a conclusion the passage supports without saying outright; you should be able to name the clue behind it.
- **Author's purpose and tone** -- why the author wrote this (to inform, persuade, or entertain) and the attitude behind the words.
- **Vocabulary in context** -- what a word means *in this sentence*, using the surrounding clues.

[[figure:comp_supp|A main idea sits on top of the specific details that support it.]]

A reliable routine for any passage:
- Read for the **big point** first, then the details.
- For a detail question, **find the line** that answers it.
- Rule out choices that are **true but never stated** or **too narrow / too broad**.

[[check:An answer choice is a true fact about the world but the passage never says it. Should you pick it? Answer yes or no.|no|Reading answers must be supported by the passage itself.]]
            """,
        ),
        (
            "3. Language & the Extended Response",
            r"""
The **Language & Editing** questions test the rules of standard written English:

- **Complete sentences** -- a sentence needs a subject, a verb, and a complete thought (watch for fragments and run-ons).
- **Subject-verb agreement** -- match the verb to the real subject (singular or plural).
- **Verb tense** -- keep tenses consistent within a passage.
- **Punctuation** -- commas in a series, apostrophes for contractions and possession.
- **Commonly confused words** -- its/it's, their/there/they're, your/you're, to/too/two.

For the **Extended Response**, remember the single most important rule: you are graded on which argument is **better supported by evidence**, *not* on which side you personally agree with. Plan briefly, state your claim, support it with details from the passages, and organize it into clear paragraphs.

[[check:In the Extended Response, are you graded on your personal opinion or on which argument is better supported? Answer with one word: opinion or supported.|supported|Judge the two arguments by their evidence.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  READING COMPREHENSION ======================
        # =====================================================================
        # ----- Passage 1: Honeybees (informational) -----
        {
            "text": ("**Reading section.** Read the passage, then answer.\n\n"
                     "\"Honeybees do far more than make honey. As they move from flower to flower "
                     "collecting nectar, they carry pollen with them, fertilizing plants so the plants "
                     "can produce fruits and seeds. Roughly a third of the food we eat depends on this "
                     "pollination. Without bees, grocery shelves would hold far fewer apples, almonds, "
                     "and berries.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Honeybees are important pollinators that much of our food supply depends on.", True),
                        ("Honeybees are mainly useful because they make honey.", False),
                        ("Apples and almonds grow on trees.", False),
                        ("Grocery stores sell many kinds of fruit.", False)],
            "explanation": r"The whole passage builds to one point: by carrying pollen, bees fertilize the plants that give us much of our food. The trap about honey is a single detail the passage actually plays down ('far more than make honey'). Pro tip: the main idea must cover the whole passage, not one fact.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Honeybees do far more than make honey. As they move from flower to flower "
                     "collecting nectar, they carry pollen with them, fertilizing plants so the plants "
                     "can produce fruits and seeds. Roughly a third of the food we eat depends on this "
                     "pollination.\"\n\n"
                     "According to the passage, about how much of the food we eat depends on pollination?"),
            "difficulty": 1,
            "choices": [("About one third", True), ("All of it", False), ("None of it", False), ("Exactly half", False)],
            "explanation": r"The passage states 'roughly a third of the food we eat depends on this pollination.' The traps exaggerate or invent a fraction. Pro tip: for a detail question, find the exact words in the text.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Roughly a third of the food we eat depends on this pollination. Without bees, "
                     "grocery shelves would hold far fewer apples, almonds, and berries.\"\n\n"
                     "What can you most reasonably infer would happen if honeybees disappeared?"),
            "difficulty": 2,
            "choices": [("Many fruits and nuts would become harder to find.", True),
                        ("People would stop eating entirely.", False),
                        ("Honey would taste sweeter.", False),
                        ("Flowers would grow faster.", False)],
            "explanation": r"Since a third of our food depends on bee pollination, losing bees would mean fewer of those foods -- the passage names apples, almonds, and berries. The trap 'stop eating entirely' overstates it. Pro tip: a good inference follows directly from the stated facts, without exaggeration.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"As they move from flower to flower collecting nectar, they carry pollen with "
                     "them, fertilizing plants so the plants can produce fruits and seeds.\"\n\n"
                     "As used in this sentence, \"fertilizing\" most nearly means:"),
            "difficulty": 2,
            "choices": [("enabling the plants to produce fruits and seeds", True),
                        ("watering the plants", False),
                        ("cutting the plants down", False),
                        ("changing the color of the plants", False)],
            "explanation": r"The sentence itself defines it: fertilizing lets 'the plants produce fruits and seeds.' The trap 'watering' is a different garden task not mentioned. Pro tip: the rest of the sentence usually tells you what a word means in context.",
        },
        # ----- Passage 2: Recycling aluminum (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Recycling an aluminum can is one of the most worthwhile things you can do for the "
                     "environment. Making a new can from recycled aluminum uses about 95 percent less "
                     "energy than making one from raw materials. Because aluminum can be melted down and "
                     "reused again and again without losing quality, a single can might return to a store "
                     "shelf in as little as two months.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Recycling aluminum saves energy, and the metal can be reused again and again.", True),
                        ("Aluminum cans take two months to manufacture.", False),
                        ("Cans are sold in grocery stores.", False),
                        ("Raw materials are expensive to buy.", False)],
            "explanation": r"Both supporting facts -- huge energy savings and endless reuse -- point to one idea: recycling aluminum is worthwhile. The trap about two months twists a detail into the main point. Pro tip: the main idea ties the details together.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Making a new can from recycled aluminum uses about 95 percent less energy than "
                     "making one from raw materials.\"\n\n"
                     "According to the passage, recycling a can instead of using raw materials uses about:"),
            "difficulty": 1,
            "choices": [("95 percent less energy", True), ("5 percent less energy", False),
                        ("50 percent more energy", False), ("twice as much energy", False)],
            "explanation": r"The passage gives the figure directly: 'about 95 percent less energy.' The trap '5 percent' flips the number. Pro tip: read percentage details carefully -- 'less' and 'more' change everything.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Recycling an aluminum can is one of the most worthwhile things you can do for the "
                     "environment.\"\n\n"
                     "What is the author's main purpose?"),
            "difficulty": 2,
            "choices": [("To encourage readers to recycle aluminum", True),
                        ("To explain how cans are shaped in a factory", False),
                        ("To tell a story about a single can", False),
                        ("To describe the color of aluminum", False)],
            "explanation": r"Calling recycling 'one of the most worthwhile things you can do' is meant to move the reader to act -- that's persuasion. The traps describe purposes the passage never serves. Pro tip: praise plus a call toward action signals a persuasive purpose.",
        },
        # ----- Passage 3: Maria on the diving board (literary) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Maria stood at the edge of the diving board, her toes curling over the rough "
                     "surface. Below, the pool shimmered, impossibly far away. Her teammates' voices "
                     "blurred into a distant hum. She had practiced this dive a hundred times in her "
                     "mind. Taking one slow breath, she lifted her arms -- and stepped forward into the "
                     "air.\"\n\n"
                     "What can you most reasonably infer about how Maria feels?"),
            "difficulty": 2,
            "choices": [("Nervous, but determined to make the dive", True),
                        ("Bored and ready to go home", False),
                        ("Angry at her teammates", False),
                        ("Afraid of the water and refusing to dive", False)],
            "explanation": r"The pool feels 'impossibly far away' and she takes 'one slow breath' (nervous), yet she has rehearsed the dive and steps forward (determined). The trap 'refusing to dive' contradicts the last line. Pro tip: weigh all the clues -- her fear and her action together show nerves plus resolve.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Maria stood at the edge of the diving board, her toes curling over the rough "
                     "surface. Below, the pool shimmered, impossibly far away.\"\n\n"
                     "Where is Maria at the start of the passage?"),
            "difficulty": 1,
            "choices": [("On the edge of a diving board", True), ("In the pool", False),
                        ("In the stands watching", False), ("At home in bed", False)],
            "explanation": r"The first sentence places her 'at the edge of the diving board.' The traps ignore that line. Pro tip: the opening sentence often sets the scene -- read it for the where and when.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Below, the pool shimmered, impossibly far away. Her teammates' voices blurred into "
                     "a distant hum.\"\n\n"
                     "The mood of the passage is best described as:"),
            "difficulty": 2,
            "choices": [("Tense and suspenseful", True), ("Cheerful and silly", False),
                        ("Calm and dull", False), ("Sad and hopeless", False)],
            "explanation": r"The far-away pool and the blurred, distant voices build tension before the dive. The trap 'cheerful and silly' doesn't fit the focused, anxious tone. Pro tip: let the imagery set the mood -- 'impossibly far away' creates suspense, not cheer.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Her teammates' voices blurred into a distant hum.\"\n\n"
                     "This sentence most likely suggests that Maria is:"),
            "difficulty": 2,
            "choices": [("concentrating so hard that she barely hears them", True),
                        ("unable to hear anything ever again", False),
                        ("standing very far from the pool", False),
                        ("annoyed with her teammates", False)],
            "explanation": r"Voices fading to a 'distant hum' shows her focus narrowing to the dive, not a real loss of hearing. The trap takes the image literally. Pro tip: figurative descriptions reveal a character's state of mind, not literal facts.",
        },
        # ----- Passage 4: Sleep and study (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Many students try to do better in school by staying up late to study. Research "
                     "suggests this plan often backfires. During sleep, the brain strengthens memories "
                     "and clears away waste. A student who sleeps well after studying usually remembers "
                     "more than one who skips sleep to cram. In other words, a full night's rest can be "
                     "as important as the studying itself.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Getting enough sleep helps students remember what they study.", True),
                        ("Students should never study for tests.", False),
                        ("Staying up all night is the best way to learn.", False),
                        ("The brain stops working during sleep.", False)],
            "explanation": r"The passage's point, stated in the last line, is that rest matters as much as studying. The trap 'never study' is the opposite of the message. Pro tip: a closing sentence beginning 'in other words' often states the main idea plainly.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"During sleep, the brain strengthens memories and clears away waste.\"\n\n"
                     "According to the passage, what does the brain do during sleep?"),
            "difficulty": 1,
            "choices": [("Strengthens memories and clears away waste", True),
                        ("Stops working completely", False),
                        ("Forgets everything from the day", False),
                        ("Grows physically larger", False)],
            "explanation": r"The sentence states both jobs directly. The trap 'stops working completely' is contradicted by the very idea of strengthening memories. Pro tip: when the answer is in one sentence, quote it to yourself before choosing.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"A student who sleeps well after studying usually remembers more than one who "
                     "skips sleep to cram.\"\n\n"
                     "The passage suggests that staying up all night to cram is:"),
            "difficulty": 2,
            "choices": [("often less effective than getting a full night's sleep", True),
                        ("the only way to pass a test", False),
                        ("good for the brain in every case", False),
                        ("required by most teachers", False)],
            "explanation": r"If the well-rested student remembers more, then cramming without sleep works less well. The trap 'only way to pass' has no support. Pro tip: a comparison ('more than') lets you infer which option the passage favors.",
        },
        # ----- Passage 5: Letter for a public pool (persuasive) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"To the Editor: Our town should build a new public pool. Last summer, temperatures "
                     "reached record highs, and families had nowhere nearby to cool off safely. A public "
                     "pool would give children a healthy place to exercise and keep the whole community "
                     "more comfortable during heat waves. The cost is real, but the benefits to public "
                     "health are worth it.\"\n\n"
                     "What is the writer's main argument?"),
            "difficulty": 2,
            "choices": [("The town should build a public pool.", True),
                        ("Last summer was unusually hot.", False),
                        ("Children should exercise more.", False),
                        ("Public pools are expensive to build.", False)],
            "explanation": r"The claim is stated in the first sentence and the whole letter supports it. The traps are supporting details, not the central argument. Pro tip: in a persuasive letter, the main argument is the action the writer wants taken.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Last summer, temperatures reached record highs, and families had nowhere nearby "
                     "to cool off safely.\"\n\n"
                     "Which detail does the writer use to support the argument?"),
            "difficulty": 2,
            "choices": [("Record-high temperatures left families with nowhere to cool off.", True),
                        ("The pool would be painted blue.", False),
                        ("The editor is a friendly person.", False),
                        ("Many cities already have pools.", False)],
            "explanation": r"The record heat with no safe place to cool off is the evidence for needing a pool. The traps are irrelevant or never stated. Pro tip: supporting evidence is the specific reason that backs the writer's claim.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"To the Editor: Our town should build a new public pool...\"\n\n"
                     "This passage is best described as:"),
            "difficulty": 1,
            "choices": [("a persuasive letter urging an action", True),
                        ("a short fictional story", False),
                        ("a set of step-by-step instructions", False),
                        ("a weather report", False)],
            "explanation": r"It opens 'To the Editor' and argues for building a pool -- a persuasive letter. The traps name genres the text doesn't fit. Pro tip: the form ('To the Editor') and the call to act mark it as persuasive.",
        },
        # ----- Passage 6: Walking as exercise (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Walking is often overlooked as exercise, but it offers powerful benefits. A brisk "
                     "daily walk can lower blood pressure, improve mood, and strengthen the heart. Unlike "
                     "many sports, walking needs no special equipment and can be done almost anywhere. "
                     "For people who find the gym intimidating, it is an easy and free place to start.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Walking is a simple, free exercise with real health benefits.", True),
                        ("Walking requires expensive special equipment.", False),
                        ("Gyms are too intimidating to ever use.", False),
                        ("Sports are always better than walking.", False)],
            "explanation": r"The passage praises walking as easy, free, and good for health. The trap about equipment contradicts the text ('needs no special equipment'). Pro tip: watch for an answer that says the opposite of the passage.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"A brisk daily walk can lower blood pressure, improve mood, and strengthen the "
                     "heart.\"\n\n"
                     "According to the passage, a brisk daily walk can:"),
            "difficulty": 1,
            "choices": [("lower blood pressure and strengthen the heart", True),
                        ("cure every disease", False),
                        ("replace a night of sleep", False),
                        ("make a person grow taller", False)],
            "explanation": r"The sentence lists exactly these benefits. The trap 'cure every disease' overstates what the passage claims. Pro tip: stick to the benefits the passage actually names.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"A brisk daily walk can lower blood pressure...\"\n\n"
                     "As used here, \"brisk\" most nearly means:"),
            "difficulty": 2,
            "choices": [("quick and energetic", True), ("slow and lazy", False),
                        ("extremely long", False), ("dangerous", False)],
            "explanation": r"A 'brisk' walk that strengthens the heart is a quick, energetic one. The trap 'slow and lazy' is the opposite. Pro tip: think about the effect described -- a heart-strengthening walk has to have some pace.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"For people who find the gym intimidating, walking is an easy and free place to "
                     "start.\"\n\n"
                     "What is the author's main purpose in the passage?"),
            "difficulty": 2,
            "choices": [("To encourage readers to walk for their health", True),
                        ("To warn readers that exercise is dangerous", False),
                        ("To describe what a gym looks like inside", False),
                        ("To sell a brand of walking shoes", False)],
            "explanation": r"The passage praises walking's benefits and calls it 'an easy and free place to start' -- it wants readers to try it. The trap 'warn readers' misreads the positive tone. Pro tip: an upbeat list of benefits points to an encouraging purpose.",
        },
        # ----- Passage 7: Emperor penguins (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Emperor penguins endure one of the harshest winters on Earth. While other animals "
                     "flee the Antarctic cold, the males stay behind, huddling together in groups to "
                     "share warmth. Each male balances a single egg on his feet for months, eating "
                     "nothing, until the chick hatches. Their patience and teamwork make survival "
                     "possible where little else can live.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Emperor penguins survive harsh winters through teamwork and patience.", True),
                        ("Penguins eat constantly during the winter.", False),
                        ("Antarctica has a warm, mild climate.", False),
                        ("Penguins fly south to escape the cold.", False)],
            "explanation": r"The last sentence states it: patience and teamwork make survival possible. The trap 'eat constantly' contradicts 'eating nothing.' Pro tip: when a closing sentence sums things up, it usually holds the main idea.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Each male balances a single egg on his feet for months, eating nothing, until the "
                     "chick hatches.\"\n\n"
                     "According to the passage, what do the male penguins do with the egg?"),
            "difficulty": 1,
            "choices": [("Balance it on their feet for months without eating", True),
                        ("Bury it deep in the snow", False),
                        ("Leave it behind and swim away", False),
                        ("Give it to other animals", False)],
            "explanation": r"The sentence describes exactly this. The traps invent actions the passage rules out. Pro tip: for a detail, match the answer word-for-word to the text.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Emperor penguins endure one of the harshest winters on Earth.\"\n\n"
                     "As used here, \"endure\" most nearly means:"),
            "difficulty": 2,
            "choices": [("withstand or survive", True), ("enjoy and celebrate", False),
                        ("avoid completely", False), ("create from nothing", False)],
            "explanation": r"To 'endure' the harshest winter means to withstand it. The trap 'avoid completely' is contradicted by the penguins staying behind. Pro tip: use the surrounding situation -- they stay in brutal cold, so they are withstanding it.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The males stay behind, huddling together in groups to share warmth... Their "
                     "patience and teamwork make survival possible.\"\n\n"
                     "The passage suggests that the penguins' survival depends mainly on:"),
            "difficulty": 2,
            "choices": [("working together", True),
                        ("competing against one another", False),
                        ("leaving the cold behind", False),
                        ("eating as much as possible", False)],
            "explanation": r"Huddling to share warmth and 'teamwork' show survival comes from cooperation. The trap 'competing' is the opposite of huddling together. Pro tip: repeated words like 'share' and 'teamwork' signal the passage's point about cooperation.",
        },
        # ----- Passage 8: Modern libraries (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Modern libraries are about much more than books. Many now lend tools, musical "
                     "instruments, and even telescopes. They offer free internet access, job-search "
                     "help, and quiet spaces to study. For people who cannot afford these resources at "
                     "home, the local library can be a lifeline.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Today's libraries provide many free services beyond lending books.", True),
                        ("Libraries only lend printed books.", False),
                        ("Telescopes are too expensive to own.", False),
                        ("Everyone already has fast internet at home.", False)],
            "explanation": r"The opening line and the examples show libraries do 'much more than books.' The trap 'only lend printed books' directly contradicts that. Pro tip: when a passage opens with a claim and then lists examples, that claim is the main idea.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Many now lend tools, musical instruments, and even telescopes.\"\n\n"
                     "According to the passage, what can some libraries lend besides books?"),
            "difficulty": 1,
            "choices": [("Tools, instruments, and telescopes", True),
                        ("Cars and houses", False),
                        ("Food and clothing", False),
                        ("Nothing besides books", False)],
            "explanation": r"The sentence lists exactly these items. The traps name things the passage never mentions. Pro tip: a detail question is answered by the list right in the text.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"For people who cannot afford these resources at home, the local library can be a "
                     "lifeline.\"\n\n"
                     "The word \"lifeline\" suggests that, for some people, the library is:"),
            "difficulty": 2,
            "choices": [("extremely important to their daily lives", True),
                        ("a place they prefer to avoid", False),
                        ("useful only to young children", False),
                        ("rarely worth visiting", False)],
            "explanation": r"A 'lifeline' is something you depend on, so the library is vital to them. The trap 'prefer to avoid' is the opposite. Pro tip: figurative words like 'lifeline' carry strong meaning -- here, essential support.",
        },
        # =====================================================================
        # ============ PART 2  --  LANGUAGE & EDITING =========================
        # =====================================================================
        {
            "text": ("**Language section.** Choose the option that completes the sentence with correct "
                     "subject-verb agreement.\n\n"
                     "\"The list of items ______ on the desk.\""),
            "difficulty": 2,
            "choices": [("is", True), ("are", False), ("were", False), ("be", False)],
            "explanation": r"The subject is 'list' (singular), not 'items,' so the verb is 'is.' The trap 'are' agrees with the nearer word 'items' instead of the real subject. Pro tip: ignore the phrase between the subject and verb -- match the verb to the true subject.",
        },
        {
            "text": "Which of the following is a complete sentence?",
            "difficulty": 1,
            "choices": [("The dog barked loudly at the mail carrier.", True),
                        ("Barking loudly at the mail carrier.", False),
                        ("Because the dog barked loudly.", False),
                        ("The loud dog by the door.", False)],
            "explanation": r"The correct option has a subject ('dog'), a verb ('barked'), and a complete thought. The others are fragments -- missing a subject or left hanging. Pro tip: a sentence needs a who/what, an action, and a finished idea.",
        },
        {
            "text": ("Which version correctly fixes the run-on sentence?\n\n"
                     "\"I was tired I went to bed.\""),
            "difficulty": 2,
            "choices": [("I was tired, so I went to bed.", True),
                        ("I was tired I went to bed.", False),
                        ("I was tired, I went to bed.", False),
                        ("I was tired so I went to bed I slept.", False)],
            "explanation": r"Joining two complete thoughts needs a comma plus a connecting word: 'I was tired, so I went to bed.' The version with just a comma is a comma splice; leaving it as-is is a run-on. Pro tip: two complete ideas need a conjunction (and, but, so) or a period between them.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"The cat licked ______ paws.\""),
            "difficulty": 1,
            "choices": [("its", True), ("it's", False), ("its'", False), ("it is", False)],
            "explanation": r"'Its' shows possession (the cat's paws); 'it's' means 'it is.' The trap 'it's' would read 'the cat licked it is paws.' Pro tip: if you can replace it with 'it is,' use 'it's' -- otherwise use 'its.'",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"______ going to the park after lunch.\""),
            "difficulty": 2,
            "choices": [("They're", True), ("Their", False), ("There", False), ("Theyre", False)],
            "explanation": r"'They're' means 'they are,' which fits 'They are going.' 'Their' shows possession and 'there' is a place. Pro tip: expand the contraction -- if 'they are' works, the answer is 'they're.'",
        },
        {
            "text": ("Choose the option that keeps the verb tense consistent and correct.\n\n"
                     "\"Yesterday, she ______ to school.\""),
            "difficulty": 1,
            "choices": [("walked", True), ("walks", False), ("will walk", False), ("walking", False)],
            "explanation": r"'Yesterday' signals the past, so the past-tense 'walked' is correct. The trap 'walks' is present tense. Pro tip: time words like 'yesterday' tell you which tense the verb needs.",
        },
        {
            "text": ("Choose the correct possessive form.\n\n"
                     "\"The ______ toys were scattered across the floor.\" (the toys belong to the children)"),
            "difficulty": 2,
            "choices": [("children's", True), ("childrens", False), ("childrens'", False), ("children", False)],
            "explanation": r"'Children' is already plural, so the possessive adds apostrophe-s: 'children's.' The trap 'childrens'' wrongly treats it like a regular plural. Pro tip: for irregular plurals (children, men, women), add 's to show possession.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"______ doing a great job on this project.\""),
            "difficulty": 1,
            "choices": [("You're", True), ("Your", False), ("Youre", False), ("Yours", False)],
            "explanation": r"'You're' means 'you are,' which fits 'You are doing.' 'Your' shows possession. Pro tip: if 'you are' fits, write 'you're.'",
        },
        {
            "text": "Which sentence is capitalized correctly?",
            "difficulty": 2,
            "choices": [("We visited New York in July.", True),
                        ("we visited new york in july.", False),
                        ("We Visited New York In July.", False),
                        ("we visited New york in July.", False)],
            "explanation": r"Capitalize the first word, the proper noun 'New York,' and the month 'July' -- but not ordinary words. The trap that capitalizes every word is wrong. Pro tip: capitalize sentence starts, names, and months/days, not common words.",
        },
        {
            "text": "Which sentence uses commas correctly in a list?",
            "difficulty": 1,
            "choices": [("I bought apples, oranges, and bananas.", True),
                        ("I bought apples oranges and bananas.", False),
                        ("I bought, apples oranges and bananas.", False),
                        ("I bought apples, oranges and, bananas.", False)],
            "explanation": r"Items in a series are separated by commas: 'apples, oranges, and bananas.' The traps drop commas or place them wrongly. Pro tip: put a comma after each item in a list of three or more.",
        },
        {
            "text": ("Choose the option with correct subject-verb agreement.\n\n"
                     "\"Each of the players ______ a uniform.\""),
            "difficulty": 2,
            "choices": [("has", True), ("have", False), ("were", False), ("having", False)],
            "explanation": r"'Each' is singular, so it takes 'has' -- the phrase 'of the players' doesn't change that. The trap 'have' agrees with 'players' by mistake. Pro tip: words like 'each,' 'every,' and 'one' are singular.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"I would like to go to the movie ______.\" (meaning 'also')"),
            "difficulty": 1,
            "choices": [("too", True), ("to", False), ("two", False), ("tow", False)],
            "explanation": r"'Too' means 'also,' which fits the meaning here. 'To' is a preposition and 'two' is the number 2. Pro tip: 'too' (with two o's) means 'also' or 'excessively.'",
        },
        {
            "text": ("Choose the most logical transition word.\n\n"
                     "\"It was raining hard. ______, we decided to stay inside.\""),
            "difficulty": 2,
            "choices": [("Therefore", True), ("However", False), ("Meanwhile", False), ("For example", False)],
            "explanation": r"Staying inside is the result of the rain, so 'Therefore' (showing cause and effect) fits. 'However' would signal a contrast that isn't there. Pro tip: match the transition to the relationship -- a result calls for 'therefore' or 'so.'",
        },
        {
            "text": "Which sentence is written most clearly, with no misplaced description?",
            "difficulty": 2,
            "choices": [("Walking to school, Maria got soaked by the rain.", True),
                        ("Walking to school, the rain soaked Maria.", False),
                        ("Soaked by the rain walking, Maria to school.", False),
                        ("The rain, walking to school, soaked Maria.", False)],
            "explanation": r"The opening phrase 'Walking to school' should describe a person -- Maria -- not 'the rain.' The trap makes it sound like the rain was walking to school. Pro tip: an opening -ing phrase must describe the noun right after the comma.",
        },
        {
            "text": ("Choose the option that avoids a double negative.\n\n"
                     "\"I don't have ______ money with me.\""),
            "difficulty": 2,
            "choices": [("any", True), ("no", False), ("none", False), ("nothing", False)],
            "explanation": r"'Don't have any' is correct; 'don't have no' is a double negative. The traps 'no,' 'none,' and 'nothing' all double the negative with 'don't.' Pro tip: use only one negative word per idea -- pair 'don't' with 'any,' not 'no.'",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"______ almost time for lunch.\" (meaning 'it is')"),
            "difficulty": 1,
            "choices": [("It's", True), ("Its", False), ("Its'", False), ("Its is", False)],
            "explanation": r"'It's' means 'it is,' which fits 'It is almost time.' 'Its' shows possession. Pro tip: the apostrophe in 'it's' stands for the missing letter in 'it is.'",
        },
        {
            "text": ("Choose the option that keeps the list parallel.\n\n"
                     "\"On weekends she enjoys reading, writing, and ______.\""),
            "difficulty": 2,
            "choices": [("drawing", True), ("to draw", False), ("she draws", False), ("drew", False)],
            "explanation": r"To match 'reading' and 'writing,' the third item must also end in -ing: 'drawing.' The trap 'to draw' breaks the pattern. Pro tip: items in a list should share the same grammatical form.",
        },
        {
            "text": ("Choose the option that corrects the sentence fragment into a complete sentence.\n\n"
                     "\"Running across the field as fast as she could.\""),
            "difficulty": 2,
            "choices": [("She was running across the field as fast as she could.", True),
                        ("Running across the field as fast as she could.", False),
                        ("Across the field running fast.", False),
                        ("As fast as she could running.", False)],
            "explanation": r"The fragment has no subject and no main verb; adding 'She was' gives it both. The traps remain fragments. Pro tip: a string of describing words isn't a sentence until it has a subject and a complete verb.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the foundational (Level 1) full-length GED RLA practice exam (46 questions; MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent re-seed
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

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions "
            f"(Part 1: 28 reading, Part 2: 18 language)."
        ))
