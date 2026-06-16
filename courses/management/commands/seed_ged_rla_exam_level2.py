"""
Seed a SECOND full-length 'GED RLA' practice exam -- Level 2, a harder companion
to ``seed_ged_rla_exam``.

Same test-day structure (46 questions: a Reading Comprehension part and a
Language & Editing part; 150 minutes; Extended Response described; scored
100-200, 145 to pass), but the items are tougher: denser informational and
literary passages, questions about author's stance, tone, text structure, and
evidence evaluation, and grammar that reaches parallelism, modifiers, semicolons,
pronoun case, and concision. No 'easy' items -- everything is medium or hard.

Run:
    python manage.py seed_ged_rla_exam_level2
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Full-Length Practice Exam (Level 2 - Advanced)",
    "slug": "ged-rla-exam-level2",
    "program": "GED",
    "subject": "rla",
    "description": (
        "A tougher, second full-length GED Reasoning Through Language Arts practice exam for students who "
        "have cleared Level 1. Same test-day format -- 46 questions split into Reading Comprehension and "
        "Language & Editing, 150 minutes, the Extended Response described, scored 100-200 (145 to pass) -- "
        "but every item is medium or hard. It pushes into the skills the GED saves for its harder "
        "questions: author's stance and tone, text structure and cause-effect, evaluating evidence and "
        "counterarguments, figurative language, and nuanced vocabulary in context, plus grammar that "
        "reaches parallel structure, misplaced and dangling modifiers, semicolons and colons, pronoun "
        "case, transitions, and concision. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 2: What's Harder",
            r"""
This is the **advanced** GED RLA practice exam. The format matches the real test and Level 1:

- **46 questions** plus the **Extended Response** essay, in **150 minutes** across three sections.
- A **Reading Comprehension** part (informational and literary passages) and a **Language & Editing** part (grammar and conventions).
- Scored **100-200**, with **145 to pass**. No penalty for wrong answers.

**What's harder here than Level 1:** the passages are **denser**, and the questions move past 'find the fact.' Expect to judge an author's **stance and tone**, follow **text structure** (cause and effect, compare and contrast), weigh **evidence and counterarguments**, and read **figurative language**. The language questions reach parallelism, modifiers, and punctuation beyond the basics.

[[check:A reading question asks for an author's 'stance.' Are you identifying a fact in the text or the author's attitude toward the topic?|attitude;;the author's attitude;;attitude toward the topic|Stance is the author's attitude or position, not a stated fact.]]
            """,
        ),
        (
            "2. Reading Past the Surface",
            r"""
Harder reading questions reward attention to **how** a passage is built, not just what it says.

- **Author's purpose and stance** -- is the author informing, persuading, or reflecting, and what attitude do the word choices reveal?
- **Tone** -- the feeling behind the words (cautious, wistful, urgent, ironic).
- **Text structure** -- does the passage compare two things, trace a cause to an effect, or present a problem and a solution?
- **Evidence and counterargument** -- which detail supports the claim, and how does the author handle the other side?
- **Figurative language** -- similes, metaphors, and images that carry meaning beyond the literal.

[[figure:argument|A claim stands on its evidence; a strong writer also answers the opposing view.]]

[[check:When an author admits a weakness in their own argument and then explains why the benefits still win, what are they responding to?|the counterargument;;a counterargument;;the opposing view;;counterargument|They are addressing the counterargument, the opposing side's point.]]
            """,
        ),
        (
            "3. Sharper Language & the Extended Response",
            r"""
The language items now test the finer rules of standard written English:

- **Parallel structure** -- items in a list or pair should share the same grammatical form.
- **Modifiers** -- an opening phrase must clearly describe the right noun (watch for misplaced and dangling modifiers).
- **Punctuation** -- semicolons join two complete thoughts; colons introduce a list or explanation.
- **Pronoun case and agreement** -- 'between you and me,' and pronouns that match their antecedents.
- **Transitions and concision** -- the right connector for the logic, with no wasted words.

For the **Extended Response**, the same rule holds at every level: argue which side is **better supported by evidence**, not which you prefer. A clear claim, evidence drawn from both passages, and tidy paragraphs win the points.

[[check:Should items in a list be written in the same grammatical form? Answer yes or no.|yes|Parallel structure keeps list items in matching form.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  READING COMPREHENSION ======================
        # =====================================================================
        # ----- Passage 1: Smartphones & attention (informational/argument) -----
        {
            "text": ("**Reading section.** Read the passage, then answer.\n\n"
                     "\"Smartphones promise to keep us connected, yet a growing body of research suggests "
                     "they may be fracturing our attention. Studies find that the mere presence of a phone "
                     "on a desk -- even face-down and silent -- can lower performance on demanding tasks. "
                     "The brain, it seems, spends a sliver of energy resisting the urge to check it. The "
                     "device need not buzz to distract; its potential is distraction enough.\"\n\n"
                     "What is the central claim of the passage?"),
            "difficulty": 3,
            "choices": [("A phone can reduce focus even when it is silent and unused.", True),
                        ("Smartphones are excellent at keeping people connected.", False),
                        ("A phone must buzz or ring before it can distract anyone.", False),
                        ("Scientific research is usually unreliable.", False)],
            "explanation": r"The passage argues a phone distracts by its 'mere presence' -- 'its potential is distraction enough.' The trap about staying connected is the promise the passage pushes against. Pro tip: the central claim is the point the evidence is gathered to prove.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The device need not buzz to distract; its potential is distraction enough.\"\n\n"
                     "What does this sentence most nearly imply?"),
            "difficulty": 3,
            "choices": [("Merely knowing the phone is nearby uses up some of our focus.", True),
                        ("Phones should always be turned off at night.", False),
                        ("People genuinely enjoy checking their phones.", False),
                        ("Silent phones are completely useless.", False)],
            "explanation": r"If the 'potential' to check is itself distracting, then just knowing the phone is there costs focus. The trap about night-time has no basis in the text. Pro tip: an inference should restate the sentence's logic, not add new advice.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Smartphones promise to keep us connected, yet a growing body of research suggests "
                     "they may be fracturing our attention.\"\n\n"
                     "The author's attitude toward smartphones is best described as:"),
            "difficulty": 2,
            "choices": [("cautiously concerned", True), ("enthusiastically positive", False),
                        ("completely neutral and uninterested", False), ("openly mocking and hostile", False)],
            "explanation": r"Words like 'fracturing our attention' and 'distraction enough' show worry, but the measured, research-based tone isn't hostile. The trap 'enthusiastically positive' misses the concern. Pro tip: tone lives in word choice -- 'fracturing' signals concern, not praise.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...they may be fracturing our attention.\"\n\n"
                     "As used here, \"fracturing\" most nearly means:"),
            "difficulty": 2,
            "choices": [("breaking apart", True), ("strengthening", False),
                        ("ignoring", False), ("healing", False)],
            "explanation": r"To 'fracture' attention is to break it into pieces. The trap 'strengthening' is the opposite of the author's worry. Pro tip: a fracture is a break -- the surrounding concern confirms the negative meaning.",
        },
        # ----- Passage 2: Mr. Alvarez and the letter (literary) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Mr. Alvarez read the letter twice, then folded it with exaggerated care, as though "
                     "the creases mattered more than the words. He set it on the mantel beside the "
                     "photograph and went to water the garden, though it had rained that morning. For the "
                     "rest of the afternoon he hummed tunes he had not thought of in years.\"\n\n"
                     "What can you most reasonably infer about how the letter affected Mr. Alvarez?"),
            "difficulty": 3,
            "choices": [("It moved him deeply and stirred old memories.", True),
                        ("It made him furious.", False),
                        ("It bored him completely.", False),
                        ("It demanded an immediate payment.", False)],
            "explanation": r"Folding it 'with exaggerated care,' placing it by a photograph, and humming forgotten tunes all signal deep, tender feeling. The trap 'furious' fits none of the gentle clues. Pro tip: gather the small actions -- together they reveal an emotion the text never names outright.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...he went to water the garden, though it had rained that morning.\"\n\n"
                     "What does this detail most suggest about Mr. Alvarez?"),
            "difficulty": 3,
            "choices": [("He is preoccupied and acting out of habit, not need.", True),
                        ("The garden was extremely dry that day.", False),
                        ("He strongly dislikes rainy weather.", False),
                        ("He waters gardens for a living.", False)],
            "explanation": r"Watering a garden that the rain already soaked shows his mind is elsewhere. The trap 'extremely dry' contradicts 'it had rained.' Pro tip: a detail that doesn't quite make practical sense often reveals a character's state of mind.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...he folded it with exaggerated care, as though the creases mattered more than "
                     "the words.\"\n\n"
                     "This description suggests that, to Mr. Alvarez, the letter is:"),
            "difficulty": 2,
            "choices": [("deeply meaningful", True), ("junk mail to be thrown away", False),
                        ("a routine bill", False), ("impossible to read", False)],
            "explanation": r"Handling something with 'exaggerated care' shows it matters greatly to him. The trap 'junk mail' clashes with that care. Pro tip: how a character treats an object signals how much it means to them.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"For the rest of the afternoon he hummed tunes he had not thought of in years.\"\n\n"
                     "The overall mood of the passage is best described as:"),
            "difficulty": 3,
            "choices": [("wistful and reflective", True), ("tense and frightening", False),
                        ("comic and silly", False), ("angry and bitter", False)],
            "explanation": r"Quiet care and long-forgotten tunes create a gentle, memory-tinged mood -- wistful. The trap 'tense and frightening' fits nothing in the scene. Pro tip: let the imagery -- old songs, careful folding -- set the emotional tone.",
        },
        # ----- Passage 3: Later school start times (persuasive) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Pushing high school start times later is not mere indulgence. Adolescent biology "
                     "shifts sleep cycles, making early mornings physiologically harsh for teenagers. "
                     "Districts that delayed their bells report better attendance, higher grades, and "
                     "fewer car accidents among student drivers. Critics cite bus-scheduling costs, but "
                     "the measurable gains in health and safety are difficult to dismiss.\"\n\n"
                     "What is the writer's central claim?"),
            "difficulty": 2,
            "choices": [("High schools should begin later in the morning.", True),
                        ("Teenagers are simply lazy.", False),
                        ("School buses are too expensive to run.", False),
                        ("Grades do not really matter.", False)],
            "explanation": r"The whole passage argues for later start times, opening by calling it 'not mere indulgence.' The trap 'teenagers are lazy' is the view the writer refutes. Pro tip: the claim is the action or position the passage defends.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Districts that delayed their bells report better attendance, higher grades, and "
                     "fewer car accidents among student drivers.\"\n\n"
                     "Which of the following best serves as evidence for the writer's claim?"),
            "difficulty": 3,
            "choices": [("Districts with later start times reported better attendance and fewer accidents.", True),
                        ("Teenagers would rather sleep than go to school.", False),
                        ("Buses must run on tight schedules.", False),
                        ("Critics of the plan are always wrong.", False)],
            "explanation": r"Concrete outcomes from real districts are the evidence backing the claim. The trap about buses is the opposing concern, not support. Pro tip: evidence is specific and measurable -- attendance, grades, accident rates.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Critics cite bus-scheduling costs, but the measurable gains in health and safety "
                     "are difficult to dismiss.\"\n\n"
                     "How does the writer handle the opposing view about bus costs?"),
            "difficulty": 3,
            "choices": [("Acknowledges it, then argues the health and safety gains outweigh it.", True),
                        ("Ignores the opposing view entirely.", False),
                        ("Agrees that the costs make the plan impossible.", False),
                        ("Claims that buses are completely unnecessary.", False)],
            "explanation": r"The writer names the cost objection ('Critics cite...') but counters that the gains outweigh it. The trap 'ignores it entirely' misreads that the objection is stated. Pro tip: 'but' after a concession signals the writer is answering a counterargument.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Pushing high school start times later is not mere indulgence.\"\n\n"
                     "As used here, \"indulgence\" most nearly means:"),
            "difficulty": 3,
            "choices": [("an unnecessary luxury or favor", True), ("a strict new rule", False),
                        ("a harsh punishment", False), ("a proven scientific law", False)],
            "explanation": r"Saying it is 'not mere indulgence' means it is more than a soft favor for teens -- so 'indulgence' is an unnecessary luxury. The trap 'punishment' is nearly opposite. Pro tip: the word 'mere' frames indulgence as something trivial or self-pampering.",
        },
        # ----- Passage 4: Coral reefs (informational/science) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Coral reefs cover less than one percent of the ocean floor, yet they shelter "
                     "roughly a quarter of all marine species. This staggering biodiversity makes them "
                     "the rainforests of the sea. But reefs are fragile. When ocean temperatures rise "
                     "even slightly, corals expel the algae that feed them and turn a ghostly white -- a "
                     "process called bleaching. A bleached reef is not yet dead, but it is starving, and "
                     "without relief it soon will be.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 3,
            "choices": [("Coral reefs are extraordinarily biodiverse yet highly vulnerable.", True),
                        ("Coral reefs cover most of the ocean floor.", False),
                        ("Bleaching means a reef has already died.", False),
                        ("Algae are harmful invaders that damage coral.", False)],
            "explanation": r"The passage pairs the reefs' huge biodiversity with their fragility -- two ideas joined by 'But.' The trap 'cover most of the ocean floor' contradicts 'less than one percent.' Pro tip: when a passage turns on 'but,' the main idea usually balances both halves.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...they shelter roughly a quarter of all marine species.\"\n\n"
                     "According to the passage, coral reefs shelter about what share of marine species?"),
            "difficulty": 2,
            "choices": [("About one quarter", True), ("Less than one percent", False),
                        ("All of them", False), ("None of them", False)],
            "explanation": r"The text states 'roughly a quarter.' The trap 'less than one percent' is the share of ocean floor they cover, not the species figure. Pro tip: watch which number goes with which idea -- the passage gives two different fractions.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"When ocean temperatures rise even slightly, corals expel the algae that feed "
                     "them...\"\n\n"
                     "According to the passage, what causes bleaching?"),
            "difficulty": 2,
            "choices": [("A rise in ocean temperature", True), ("Too many fish on the reef", False),
                        ("A lack of sunlight", False), ("The algae leaving for no reason", False)],
            "explanation": r"The passage names rising temperature as the trigger that makes corals expel their algae. The trap 'too many fish' isn't mentioned. Pro tip: cause-and-effect questions hinge on the 'when... then...' structure in the text.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"A bleached reef is not yet dead, but it is starving, and without relief it soon "
                     "will be.\"\n\n"
                     "What does this sentence most reasonably imply?"),
            "difficulty": 3,
            "choices": [("A bleached reef can still recover if conditions improve.", True),
                        ("A bleached reef always dies instantly.", False),
                        ("Reefs cannot be harmed by temperature.", False),
                        ("Warm water is good for coral.", False)],
            "explanation": r"'Not yet dead' and 'without relief' imply that relief could save it -- recovery is possible. The trap 'dies instantly' contradicts 'not yet dead.' Pro tip: the phrase 'without relief it soon will be' hints that with relief, it might not.",
        },
        # ----- Passage 5: The gig economy (author's perspective) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Supporters of the gig economy praise its flexibility: drive, deliver, or "
                     "freelance whenever you choose. Yet that freedom comes wrapped in uncertainty. Gig "
                     "workers rarely receive health insurance, paid leave, or a guaranteed wage, and a "
                     "slow week is simply a smaller paycheck. The arrangement can suit a student with "
                     "spare hours; it can crush a parent who depends on it to pay rent.\"\n\n"
                     "The author's perspective on the gig economy is best described as:"),
            "difficulty": 3,
            "choices": [("balanced -- recognizing its flexibility but stressing its risks", True),
                        ("wholly enthusiastic about it", False),
                        ("completely opposed to any flexible work", False),
                        ("uninterested in the subject", False)],
            "explanation": r"The author grants the flexibility ('whenever you choose') but devotes most of the passage to insecurity ('uncertainty,' 'crush a parent'). The trap 'wholly enthusiastic' ignores that emphasis. Pro tip: 'Yet' marks the pivot to the author's real emphasis -- the risks.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The arrangement can suit a student with spare hours; it can crush a parent who "
                     "depends on it to pay rent.\"\n\n"
                     "What does this contrast most suggest?"),
            "difficulty": 3,
            "choices": [("The gig economy works well for some people but poorly for others.", True),
                        ("The gig economy is ideal for everyone.", False),
                        ("Gig work is against the law.", False),
                        ("Gig work involves only driving.", False)],
            "explanation": r"Setting 'suit a student' against 'crush a parent' shows the same system affects people very differently. The trap 'ideal for everyone' erases the contrast. Pro tip: a sentence built on a contrast is making a point about difference, not sameness.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Gig workers rarely receive health insurance, paid leave, or a guaranteed wage...\"\n\n"
                     "According to the passage, what do gig workers rarely receive?"),
            "difficulty": 2,
            "choices": [("Health insurance, paid leave, or a guaranteed wage", True),
                        ("Any work at all", False), ("Flexibility in their hours", False),
                        ("Access to a smartphone", False)],
            "explanation": r"The sentence lists exactly these three. The trap 'flexibility' is the one thing the passage says they DO get. Pro tip: don't let a nearby positive detail get swapped into a 'what's missing' question.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Yet that freedom comes wrapped in uncertainty.\"\n\n"
                     "As used here, \"uncertainty\" most nearly means:"),
            "difficulty": 2,
            "choices": [("unpredictability and lack of security", True), ("boredom", False),
                        ("great wealth", False), ("honesty", False)],
            "explanation": r"The next sentences -- no insurance, no guaranteed wage -- define the uncertainty as insecurity. The trap 'great wealth' is unrelated. Pro tip: read the sentences that follow a key word; they often spell out its meaning.",
        },
        # ----- Passage 6: The printing press (historical/informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"When Gutenberg pressed ink to paper in the 1450s, he did more than reproduce books "
                     "quickly. He loosened the grip of the few who controlled knowledge. Before the press, "
                     "copying a single book took a scribe months; afterward, identical copies streamed out "
                     "by the hundreds. Ideas once confined to monasteries spilled into towns and markets, "
                     "and ordinary people, for the first time, could own the words of others.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 3,
            "choices": [("The printing press spread knowledge far beyond a privileged few.", True),
                        ("Gutenberg invented paper in the 1450s.", False),
                        ("Scribes were able to copy books very quickly.", False),
                        ("Books became rarer after the printing press.", False)],
            "explanation": r"The passage's point is that the press broke a few people's control of knowledge and spread it widely. The trap 'invented paper' isn't what the passage says he did. Pro tip: the main idea is the change the passage keeps illustrating -- here, the spread of knowledge.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"He loosened the grip of the few who controlled knowledge.\"\n\n"
                     "What does this sentence imply about the time before the printing press?"),
            "difficulty": 3,
            "choices": [("A small, powerful group had controlled access to knowledge.", True),
                        ("Everyone could already read and own books.", False),
                        ("Books were considered worthless.", False),
                        ("No one had any interest in books.", False)],
            "explanation": r"If the press 'loosened the grip of the few,' then before it, a few controlled knowledge. The trap 'everyone could already read' is the opposite. Pro tip: a phrase about a change tells you what the situation was like beforehand.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Before the press, copying a single book took a scribe months...\"\n\n"
                     "According to the passage, how long did copying one book take before the press?"),
            "difficulty": 2,
            "choices": [("Months", True), ("A few minutes", False),
                        ("A few seconds", False), ("Only one hour", False)],
            "explanation": r"The text says copying 'took a scribe months.' The traps shrink the time. Pro tip: detail questions are answered exactly by the text -- here, 'months.'",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...ordinary people, for the first time, could own the words of others.\"\n\n"
                     "What is the author's main purpose?"),
            "difficulty": 2,
            "choices": [("To explain how the printing press changed society", True),
                        ("To teach readers how to build a printing press", False),
                        ("To criticize Gutenberg's character", False),
                        ("To describe what people ate in the 1450s", False)],
            "explanation": r"The passage traces the press's broad social effects, not how to build one. The trap 'how to build a press' confuses topic with purpose. Pro tip: purpose answers 'why was this written' -- here, to explain a historical change.",
        },
        # ----- Passage 7: The city at dawn (literary, figurative) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The city woke slowly. Streetlights blinked off one by one, surrendering to a pale "
                     "gold light that crept between the buildings. A lone bus sighed at the corner, and "
                     "somewhere a shop gate rattled upward like a yawn. For a few quiet minutes, before "
                     "the crowds, the streets belonged to no one and everyone.\"\n\n"
                     "What does the comparison \"a shop gate rattled upward like a yawn\" mainly suggest?"),
            "difficulty": 3,
            "choices": [("The city is slowly, sleepily coming awake.", True),
                        ("The shop's gate is broken and dangerous.", False),
                        ("The shopkeepers are angry that morning.", False),
                        ("It is the middle of the night.", False)],
            "explanation": r"Comparing the gate to 'a yawn' extends the image of a city waking up sleepily. The trap 'broken and dangerous' ignores the gentle, drowsy tone. Pro tip: a simile usually reinforces the passage's larger image -- here, waking slowly.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...a pale gold light that crept between the buildings.\"\n\n"
                     "The mood of the passage is best described as:"),
            "difficulty": 2,
            "choices": [("calm and peaceful", True), ("violent and chaotic", False),
                        ("gloomy and hopeless", False), ("tense and fearful", False)],
            "explanation": r"Soft gold light, a 'lone bus,' and 'quiet minutes' build a calm, peaceful mood. The trap 'violent and chaotic' contradicts the stillness. Pro tip: gentle imagery and quiet sounds create a calm mood.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"For a few quiet minutes, before the crowds, the streets belonged to no one and "
                     "everyone.\"\n\n"
                     "What does this line most reasonably suggest?"),
            "difficulty": 3,
            "choices": [("For a brief moment the city feels open and shared by all.", True),
                        ("The streets are privately owned by one person.", False),
                        ("No one actually lives in the city.", False),
                        ("The city has been abandoned forever.", False)],
            "explanation": r"'Belonged to no one and everyone' captures a shared, open moment before the crowds arrive. The trap 'privately owned' is the opposite of 'no one.' Pro tip: a seeming contradiction ('no one and everyone') usually expresses a feeling -- here, a shared openness.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Streetlights blinked off one by one, surrendering to a pale gold light...\"\n\n"
                     "As used here, \"surrendering\" most nearly means:"),
            "difficulty": 2,
            "choices": [("yielding or giving way", True), ("fighting back hard", False),
                        ("shining more brightly", False), ("breaking into pieces", False)],
            "explanation": r"The lights 'surrender' to daylight -- they yield as the gold light takes over. The trap 'fighting back' is the opposite. Pro tip: in context, surrendering to the dawn means giving way to it.",
        },
        # =====================================================================
        # ============ PART 2  --  LANGUAGE & EDITING =========================
        # =====================================================================
        {
            "text": ("**Language section.** Choose the option that keeps the sentence parallel.\n\n"
                     "\"The job requires typing quickly, answering phones, and ______.\""),
            "difficulty": 2,
            "choices": [("filing reports", True), ("to file reports", False),
                        ("reports must be filed", False), ("she files reports", False)],
            "explanation": r"To match 'typing' and 'answering,' the third item needs the -ing form: 'filing reports.' The trap 'to file reports' breaks the pattern. Pro tip: list items should share the same grammatical form.",
        },
        {
            "text": "Which sentence places its description clearly, with no misplaced modifier?",
            "difficulty": 3,
            "choices": [("I devoured the strawberries, which were covered in chocolate.", True),
                        ("Covered in chocolate, I devoured the strawberries.", False),
                        ("I devoured, covered in chocolate, the strawberries.", False),
                        ("Covered in chocolate I the strawberries devoured.", False)],
            "explanation": r"The chocolate covers the strawberries, not the speaker, so the modifier must sit next to 'strawberries.' The trap makes it sound like the speaker is covered in chocolate. Pro tip: keep a describing phrase right beside the word it actually describes.",
        },
        {
            "text": ("Choose the option with correct pronoun-antecedent agreement (formal usage).\n\n"
                     "\"Every employee should submit ______ timesheet by Friday.\""),
            "difficulty": 3,
            "choices": [("his or her", True), ("they're", False), ("its", False), ("our", False)],
            "explanation": r"'Every employee' is singular, so formal usage takes the singular 'his or her.' The trap 'they're' means 'they are,' which is a verb, not a possessive. Pro tip: match the pronoun to a singular antecedent like 'every employee.'",
        },
        {
            "text": "Which sentence uses a semicolon correctly?",
            "difficulty": 3,
            "choices": [("I have a big test tomorrow; I cannot go out tonight.", True),
                        ("I have a big test tomorrow; because I must study.", False),
                        ("I have a big test; tomorrow night.", False),
                        ("I have; a big test tomorrow night.", False)],
            "explanation": r"A semicolon joins two complete, related thoughts: 'I have a big test tomorrow' and 'I cannot go out tonight.' The traps put a fragment on one side. Pro tip: a semicolon needs a complete sentence on both sides.",
        },
        {
            "text": ("Which version correctly fixes the comma splice?\n\n"
                     "\"The movie was long, I enjoyed it.\""),
            "difficulty": 2,
            "choices": [("The movie was long, but I enjoyed it.", True),
                        ("The movie was long, I enjoyed it.", False),
                        ("The movie was long I enjoyed it.", False),
                        ("The movie, was long but I enjoyed it.", False)],
            "explanation": r"Two complete thoughts need a joining word: 'long, but I enjoyed it.' Leaving just the comma is the original splice; removing it makes a run-on. Pro tip: fix a comma splice by adding a conjunction or changing the comma to a period or semicolon.",
        },
        {
            "text": ("Choose the option with correct subject-verb agreement.\n\n"
                     "\"The box of old photographs ______ in the attic.\""),
            "difficulty": 3,
            "choices": [("sits", True), ("sit", False), ("are sitting", False), ("have sat", False)],
            "explanation": r"The subject is 'box' (singular), so the verb is 'sits' -- 'of old photographs' is just a describing phrase. The trap 'sit' agrees with 'photographs' by mistake. Pro tip: find the true subject before the prepositional phrase, then match the verb to it.",
        },
        {
            "text": ("Choose the option that keeps the verb tenses consistent.\n\n"
                     "\"She studied all night and then ______ the exam in the morning.\""),
            "difficulty": 2,
            "choices": [("took", True), ("takes", False), ("will take", False), ("take", False)],
            "explanation": r"'Studied' is past tense, so the matching verb is 'took.' The trap 'takes' shifts to the present. Pro tip: keep tenses consistent -- a past-tense sentence stays in the past.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"There were ______ cars on the road than usual this morning.\""),
            "difficulty": 3,
            "choices": [("fewer", True), ("less", False), ("lesser", False), ("least", False)],
            "explanation": r"Use 'fewer' for things you can count, like cars; 'less' is for amounts you can't count. The trap 'less' is the common error. Pro tip: fewer items, less stuff -- count nouns take 'fewer.'",
        },
        {
            "text": ("Choose the correct possessive form.\n\n"
                     "\"The ______ lounge is on the second floor.\" (a lounge for the teachers)"),
            "difficulty": 2,
            "choices": [("teachers'", True), ("teacher's", False), ("teachers", False), ("teachers's", False)],
            "explanation": r"The lounge belongs to more than one teacher, so the plural possessive is 'teachers'' (apostrophe after the s). The trap 'teacher's' means a single teacher. Pro tip: for a plural noun ending in s, add just an apostrophe to show possession.",
        },
        {
            "text": ("Choose the most logical transition.\n\n"
                     "\"The plan was expensive; ______, the council approved it because the benefits were "
                     "clear.\""),
            "difficulty": 3,
            "choices": [("nevertheless", True), ("therefore", False),
                        ("for instance", False), ("in addition", False)],
            "explanation": r"The cost would normally argue against approval, but the council approved it anyway -- a contrast, so 'nevertheless' fits. 'Therefore' would wrongly make the cost the reason for approval. Pro tip: a surprising result calls for a contrast word like 'nevertheless.'",
        },
        {
            "text": "Which sentence is written most concisely without losing meaning?",
            "difficulty": 2,
            "choices": [("Because it rained, we left early.", True),
                        ("Due to the fact that it was raining, we left early.", False),
                        ("On account of the reason that it rained, we left early.", False),
                        ("It being the case that it rained, we left early.", False)],
            "explanation": r"'Because it rained' says the same thing in far fewer words. The traps pad the sentence with wordy phrases like 'due to the fact that.' Pro tip: replace bloated phrases with a single word -- 'because' beats 'due to the fact that.'",
        },
        {
            "text": ("Choose the best way to combine the sentences.\n\n"
                     "\"The bridge is old. It is still safe to cross.\""),
            "difficulty": 3,
            "choices": [("Although the bridge is old, it is still safe to cross.", True),
                        ("The bridge is old, it is still safe to cross.", False),
                        ("The bridge is old it is still safe to cross.", False),
                        ("The bridge is old so it is still safe to cross.", False)],
            "explanation": r"'Although' shows the right relationship -- being old contrasts with being safe. The trap with just a comma is a comma splice; 'so' wrongly makes age the reason for safety. Pro tip: use a subordinating word like 'although' to show contrast between two ideas.",
        },
        {
            "text": ("Choose the correct pronoun.\n\n"
                     "\"Between you and ______, the surprise party is all set.\""),
            "difficulty": 3,
            "choices": [("me", True), ("I", False), ("myself", False), ("mine", False)],
            "explanation": r"After the preposition 'between,' use the object pronoun 'me.' The trap 'I' is a subject pronoun and sounds formal but is wrong here. Pro tip: 'between you and me' is always correct -- prepositions take object pronouns.",
        },
        {
            "text": "Which sentence uses a colon correctly?",
            "difficulty": 2,
            "choices": [("She packed three things: a map, water, and snacks.", True),
                        ("She packed: a map, water, and snacks for three.", False),
                        ("She packed three things, a map: water and snacks.", False),
                        ("She: packed three things a map water and snacks.", False)],
            "explanation": r"A colon follows a complete thought to introduce a list: 'She packed three things: ...' The traps put the colon mid-sentence after an incomplete clause. Pro tip: a colon needs a full sentence before it.",
        },
        {
            "text": ("Choose the version that corrects the dangling modifier.\n\n"
                     "\"After finishing the report, the printer jammed.\""),
            "difficulty": 3,
            "choices": [("After I finished the report, the printer jammed.", True),
                        ("After finishing the report, the printer jammed.", False),
                        ("The printer jammed after finishing the report.", False),
                        ("Finishing the report, jammed the printer.", False)],
            "explanation": r"A printer can't finish a report, so the sentence needs a person: 'After I finished the report...' The trap leaves the printer doing the finishing. Pro tip: make sure the opening phrase describes a real subject that can perform the action.",
        },
        {
            "text": ("Choose the option with correct subject-verb agreement.\n\n"
                     "\"Neither the manager nor the workers ______ satisfied with the result.\""),
            "difficulty": 3,
            "choices": [("are", True), ("is", False), ("was", False), ("has been", False)],
            "explanation": r"With 'neither... nor,' the verb agrees with the nearer subject, 'workers' (plural), so 'are.' The trap 'is' would agree with 'manager' instead. Pro tip: in neither/nor (or either/or), match the verb to the subject closest to it.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"The new policy will ______ every department in the company.\""),
            "difficulty": 2,
            "choices": [("affect", True), ("effect", False), ("affects", False), ("effected", False)],
            "explanation": r"'Affect' is the verb meaning to influence; 'effect' is usually the noun (a result). The trap 'effect' would need to be a noun here, but the sentence needs an action. Pro tip: affect is the action (a verb), effect is the result (a noun).",
        },
        {
            "text": "Which sentence avoids redundancy?",
            "difficulty": 2,
            "choices": [("She returned the book to the library.", True),
                        ("She returned the book back to the library again.", False),
                        ("She returned back the book to the library again.", False),
                        ("She again returned the book back to the library.", False)],
            "explanation": r"'Returned' already means giving back, so 'back' and 'again' are redundant. The traps repeat the idea of returning. Pro tip: cut words that restate a meaning already in the verb -- 'return back' says 'back' twice.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the advanced (Level 2) full-length GED RLA practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 28 reading, Part 2: 18 language; all medium/hard)."
        ))
