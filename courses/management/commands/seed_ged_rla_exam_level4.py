"""
Seed a FOURTH full-length 'GED RLA' practice exam -- Level 4, the mastery tier,
harder than ``seed_ged_rla_exam_level3``.

Same test-day structure (46 questions: Reading Comprehension + Language &
Editing; 150 minutes; Extended Response described; scored 100-200, 145 to pass),
but EVERY item is a hard, multi-layered problem: unstated assumptions in an
argument, an unreliable narrator, synthesis across a paired-passage set, satire
and irony, an extended metaphor, and grammar that reaches the subjunctive in
that-clauses, who/whom inside clauses, squinting modifiers, semicolons in complex
lists, and pronoun clarity.

Run:
    python manage.py seed_ged_rla_exam_level4
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Full-Length Practice Exam (Level 4 - Mastery)",
    "slug": "ged-rla-exam-level4",
    "program": "GED",
    "subject": "rla",
    "description": (
        "The fourth and second-hardest full-length GED Reasoning Through Language Arts practice exam, for "
        "students aiming at a top score after clearing Levels 1-3. Same test-day format -- 46 questions "
        "split into Reading Comprehension and Language & Editing, 150 minutes, the Extended Response "
        "described, scored 100-200 (145 to pass) -- but every item is a hard, multi-layered problem: "
        "identifying an argument's unstated assumptions, reading an unreliable narrator, synthesizing a "
        "paired-passage set, decoding satire and irony, tracing an extended metaphor, and grammar that "
        "reaches the subjunctive in that-clauses, who/whom inside clauses, squinting and misplaced "
        "modifiers, semicolons in complex lists, idiomatic prepositions, and pronoun clarity. Every "
        "question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 4: The Mastery Reading Test",
            r"""
This is the **mastery** GED RLA practice exam -- harder than Levels 1-3. The format is unchanged:

- **46 questions** plus the **Extended Response**, in **150 minutes**; scored **100-200**, **145 to pass**.

**What makes Level 4 the hardest yet:** **every** question is a hard, layered item. You will name the **unstated assumption** beneath an argument, judge an **unreliable narrator**, **synthesize** two paired passages into one conclusion, see through **satire**, and follow an **extended metaphor**. The language items reach the finer points of grammar and style. There are no routine questions.

[[check:An argument calls a test 'fair' because everyone takes it the same way. What hidden assumption does that rely on?|that equal treatment equals equal opportunity;;equal treatment is the same as equal opportunity;;same treatment means fair|It assumes identical treatment is the same as an equal chance -- which may not hold.]]
            """,
        ),
        (
            "2. Reading Beneath the Surface",
            r"""
Mastery-level reading is about what a text assumes, implies, and does -- not just what it says.

- **Unstated assumptions** -- the belief an argument takes for granted; challenge it and the argument may fall.
- **Unreliable narration** -- when the narrator's account is shaped by bias, memory, or desire, read past them to the real picture.
- **Synthesis** -- combine two passages into a single, fair conclusion that honors both.
- **Satire and irony** -- when the literal words mock the very thing they pretend to praise.
- **Extended metaphor** -- one comparison carried across a passage to shape its whole meaning.

[[figure:argument|Behind every claim and its evidence sits an assumption -- the unstated link the writer needs you to accept.]]

[[check:When an essay seriously proposes a 'luxury parking garage' while listing the city's broken sidewalks and late buses, what technique is at work?|satire;;irony;;sarcasm|It is satire/irony -- praising the opposite of what the author truly wants.]]
            """,
        ),
        (
            "3. Mastery Language & the Extended Response",
            r"""
The language items now test grammar and style at their most demanding:

- **Subjunctive in that-clauses** -- 'The board recommends that each member submit the form' (base verb).
- **Tricky agreement** -- 'a number of students are' (plural) vs. 'the number of students is' (singular).
- **Modifier clarity** -- squinting modifiers that could attach to either side, and 'only/almost' placed precisely.
- **Pronoun clarity** -- a vague 'this' or 'it' must be pinned to a clear noun.
- **Parallel structure and concision** -- matching forms across correlatives, with no wasted words.

The **Extended Response** standard is constant: argue which side is **better supported by evidence**, with a clear claim, support drawn from both passages, and clean paragraphs.

[[check:In 'The committee recommends that he ___ present,' which verb form is correct -- is or be?|be|That-clauses after 'recommend' take the base form: 'that he be present.']]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  READING COMPREHENSION ======================
        # =====================================================================
        # ----- Passage 1: Standardized testing (argument w/ assumption) -----
        {
            "text": ("**Reading section.** Read the passage, then answer.\n\n"
                     "\"Defenders of standardized testing argue that a single exam offers an objective "
                     "yardstick, free of the favoritism that can color a teacher's grades. Yet objectivity "
                     "is not the same as fairness. A test administered identically to every student still "
                     "rewards those who can afford tutoring and quiet homes to study in. To call such a "
                     "measure 'fair' is to assume that equal treatment and equal opportunity are the same "
                     "thing -- and they are not.\"\n\n"
                     "What is the author's central claim?"),
            "difficulty": 3,
            "choices": [("Standardized tests can be objective and yet still unfair.", True),
                        ("Standardized tests are completely fair to every student.", False),
                        ("Teachers' grades are always hopelessly biased.", False),
                        ("Private tutoring should be made illegal.", False)],
            "explanation": r"The author concedes tests are objective but argues that doesn't make them fair. The trap 'completely fair' is exactly the view being challenged. Pro tip: when a passage says 'X is not the same as Y,' its claim usually rests on keeping those two apart.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"To call such a measure 'fair' is to assume that equal treatment and equal "
                     "opportunity are the same thing -- and they are not.\"\n\n"
                     "Which unstated assumption does the author argue against?"),
            "difficulty": 3,
            "choices": [("that treating everyone identically gives everyone an equal chance", True),
                        ("that tests are scored by computers", False),
                        ("that students dislike taking tests", False),
                        ("that teachers grade unfairly on purpose", False)],
            "explanation": r"The author names the hidden assumption -- that equal treatment equals equal opportunity -- and rejects it. The traps are details, not the assumption. Pro tip: an assumption is the unstated belief an argument needs you to accept; here the author drags it into the open.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Yet objectivity is not the same as fairness.\"\n\n"
                     "The author's argument turns on a distinction between:"),
            "difficulty": 3,
            "choices": [("being objective and being fair", True),
                        ("teachers and students", False),
                        ("tests and homework assignments", False),
                        ("quiet homes and noisy homes", False)],
            "explanation": r"The whole argument hinges on separating objectivity (treating all alike) from fairness (equal opportunity). The traps name pairs the passage doesn't build on. Pro tip: find the two ideas the author insists are different -- that gap is the argument.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...still rewards those who can afford tutoring and quiet homes to study in.\"\n\n"
                     "This detail mainly serves to:"),
            "difficulty": 3,
            "choices": [("show how outside advantages shape test results", True),
                        ("prove that tutoring never helps anyone", False),
                        ("argue that homes should simply be quieter", False),
                        ("praise the fairness of standardized tests", False)],
            "explanation": r"Tutoring and quiet homes are advantages some students lack, showing the test isn't a level field. The trap 'praise the fairness' is the opposite of the author's point. Pro tip: a concrete example usually backs the author's larger claim -- here, that advantages skew scores.",
        },
        # ----- Passage 2: Memory of summer (unreliable narrator) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"I remember the summer as endless gold, though my sister insists it rained for "
                     "weeks. Perhaps she is right; she usually is. But memory keeps what it wishes, and "
                     "mine has chosen to keep the light. I see no reason to correct it. A childhood, after "
                     "all, is not a weather report.\"\n\n"
                     "What does the passage most strongly suggest about the narrator's memory?"),
            "difficulty": 3,
            "choices": [("It is shaped by what the narrator wishes to remember, not strict fact.", True),
                        ("It is a perfect, accurate record of events.", False),
                        ("It matches the sister's memory exactly.", False),
                        ("It is based on official weather records.", False)],
            "explanation": r"'Memory keeps what it wishes' and 'mine has chosen to keep the light' show a memory shaped by desire. The trap 'perfect record' is what the narrator admits it is not. Pro tip: a narrator who admits choosing what to remember is signaling unreliability.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"A childhood, after all, is not a weather report.\"\n\n"
                     "What does this final sentence most nearly imply?"),
            "difficulty": 3,
            "choices": [("Childhood memory is about emotional truth, not literal accuracy.", True),
                        ("The narrator once studied meteorology.", False),
                        ("It never actually rained that summer.", False),
                        ("The sister is deliberately lying.", False)],
            "explanation": r"Contrasting childhood with a 'weather report' says memory is about feeling, not factual precision. The trap 'never rained' ignores that he grants his sister may be right. Pro tip: a closing metaphor often states the passage's theme -- here, emotional over literal truth.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The narrator's tone is best described as:"),
            "difficulty": 3,
            "choices": [("fond and gently self-aware", True), ("bitter and accusing", False),
                        ("cold and clinical", False), ("panicked and anxious", False)],
            "explanation": r"He warmly recalls 'endless gold' while knowingly admitting memory's bias -- fond and self-aware. The trap 'bitter and accusing' fits none of the gentle wording. Pro tip: a narrator who smiles at his own faults has a fond, self-aware tone.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Perhaps she is right; she usually is.\"\n\n"
                     "This line suggests that the narrator:"),
            "difficulty": 3,
            "choices": [("admits his sister is usually right but still keeps his rosier memory", True),
                        ("thinks his sister always lies", False),
                        ("has completely forgotten his sister", False),
                        ("now agrees the summer was mostly rainy", False)],
            "explanation": r"He concedes her accuracy ('she usually is') yet chooses his sunlit version anyway. The trap 'now agrees... rainy' ignores 'I see no reason to correct it.' Pro tip: a concession followed by 'but' shows what the speaker acknowledges versus what he still chooses.",
        },
        # ----- Passage 3: PAIRED PASSAGES on remote work (synthesis) -----
        {
            "text": ("Read both short texts, then answer.\n\n"
                     "TEXT 1: \"Remote work has quietly redrawn the map of opportunity. A talented worker "
                     "in a small town no longer must move to a coastal city to find good pay; the job "
                     "comes to them. Companies, too, can hire from anywhere, drawing on talent they once "
                     "ignored. Distance, long a barrier, has become almost an afterthought.\"\n\n"
                     "TEXT 2: \"The promise of remote work hides a quieter cost. Careers are built not only "
                     "on tasks completed but on the unplanned conversation, the mentor who notices you, "
                     "the trust that grows over shared lunches. On a screen, the junior worker becomes a "
                     "name in a grid, easy to overlook. We have gained flexibility and lost the accidents "
                     "that once made careers.\"\n\n"
                     "What is the main idea of TEXT 1?"),
            "difficulty": 3,
            "choices": [("Remote work expands opportunity by making location almost irrelevant.", True),
                        ("Remote work isolates and overlooks junior workers.", False),
                        ("Remote work is a passing fad that will fade.", False),
                        ("Good jobs can exist only in coastal cities.", False)],
            "explanation": r"Text 1 celebrates how remote work erases distance and widens opportunity. The trap 'isolates junior workers' is Text 2's point. Pro tip: fix each text's thesis on its own before comparing -- Text 1 is the optimistic case.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "What is the main idea of TEXT 2?"),
            "difficulty": 3,
            "choices": [("Remote work weakens the informal bonds and mentoring that build careers.", True),
                        ("Remote work erases distance as a barrier to opportunity.", False),
                        ("Remote work always pays better than office work.", False),
                        ("Shared lunches are a waste of working time.", False)],
            "explanation": r"Text 2 mourns the lost 'unplanned conversation' and mentoring that careers depend on. The trap 'erases distance' belongs to Text 1. Pro tip: Text 2 is the cautionary case -- it counts what remote work costs.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "The relationship between the two texts is best described as:"),
            "difficulty": 3,
            "choices": [("offering opposing assessments of the same development", True),
                        ("agreeing completely on every point", False),
                        ("discussing two unrelated subjects", False),
                        ("both strongly opposing remote work", False)],
            "explanation": r"Both judge remote work, but Text 1 praises it and Text 2 warns about it -- opposing assessments of one trend. The trap 'both opposing' miscasts Text 1. Pro tip: same topic, opposite evaluations is a classic paired-passage relationship.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "A reader who weighed both texts together would most reasonably conclude that remote "
                     "work:"),
            "difficulty": 3,
            "choices": [("brings real gains in access but real losses in mentorship and connection", True),
                        ("is purely and entirely beneficial", False),
                        ("is purely and entirely harmful", False),
                        ("has no real effect on anyone's career", False)],
            "explanation": r"Synthesizing the optimistic and cautionary cases yields a both/and conclusion: gains in access, losses in connection. The traps pick only one side. Pro tip: a synthesis honors both passages rather than declaring one the winner.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "In Text 2, the phrase \"a name in a grid\" mainly serves to:"),
            "difficulty": 3,
            "choices": [("emphasize how easily a remote junior worker is overlooked", True),
                        ("praise the efficiency of video software", False),
                        ("describe a particular spreadsheet program", False),
                        ("argue that grids are well designed", False)],
            "explanation": r"Reducing a person to 'a name in a grid' dramatizes how invisible junior workers become on screen. The trap 'praise the efficiency' misreads the critical intent. Pro tip: a dehumanizing image is usually a rhetorical move to make you feel a loss.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "Against Text 2, the author of Text 1 would most likely emphasize that:"),
            "difficulty": 3,
            "choices": [("remote work opens doors that distance once kept closed", True),
                        ("office lunches are essential to every career", False),
                        ("junior workers can never succeed remotely", False),
                        ("physical distance still matters more than anything", False)],
            "explanation": r"Text 1's whole case is expanded access -- 'the job comes to them' -- which it would press against Text 2's worries. The traps state Text 2's view or its opposite. Pro tip: to predict an author's rebuttal, return to that author's core claim.",
        },
        # ----- Passage 4: The placebo effect (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The placebo effect is often dismissed as 'all in the mind,' as if that made it "
                     "unreal. But the mind is not separate from the body it governs. A sugar pill, "
                     "believed to be medicine, can trigger measurable changes -- lowered pain, a steadier "
                     "heart rate, the release of the body's own chemicals. The belief does not imagine the "
                     "relief; it helps produce it. To call the effect imaginary is to misunderstand how "
                     "thoroughly expectation shapes experience.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 3,
            "choices": [("The placebo effect is genuine because belief triggers real physical changes.", True),
                        ("The placebo effect is purely imaginary and unreal.", False),
                        ("Sugar pills are dangerous and should be banned.", False),
                        ("The mind and the body are entirely unrelated.", False)],
            "explanation": r"The passage argues the effect is real because expectation produces measurable bodily change. The trap 'purely imaginary' is the view it refutes. Pro tip: 'often dismissed as... but' sets up the author to overturn that dismissal.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...the mind is not separate from the body it governs.\"\n\n"
                     "The author uses this idea mainly to respond to the claim that the placebo effect is:"),
            "difficulty": 3,
            "choices": [("'all in the mind,' and therefore not real", True),
                        ("caused by powerful new medicines", False),
                        ("a danger that should replace real medicine", False),
                        ("impossible to measure in any way", False)],
            "explanation": r"By denying a mind-body split, the author answers the 'all in the mind, so unreal' dismissal. The trap about 'replace real medicine' isn't claimed anywhere. Pro tip: find the exact objection the author is rebutting -- here, the 'all in the mind' line.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The belief does not imagine the relief; it helps produce it.\"\n\n"
                     "What does this sentence most nearly imply?"),
            "difficulty": 3,
            "choices": [("Expecting relief can actually bring about real relief.", True),
                        ("Relief from a placebo is always faked.", False),
                        ("Belief has no power over the body.", False),
                        ("Medicine never works on anyone.", False)],
            "explanation": r"'Does not imagine... helps produce' means belief causes genuine relief. The trap 'always faked' is the opposite. Pro tip: a 'not X but Y' sentence asserts Y -- here, that belief produces real effects.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...the body it governs.\"\n\n"
                     "As used here, \"governs\" most nearly means:"),
            "difficulty": 3,
            "choices": [("directs or controls", True), ("ignores entirely", False),
                        ("closely resembles", False), ("completely replaces", False)],
            "explanation": r"The mind 'governs' the body -- it directs and controls it. The trap 'ignores entirely' is the opposite of governing. Pro tip: 'govern' shares a root with 'government' -- it means to control or direct.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The author's main purpose in the passage is to:"),
            "difficulty": 3,
            "choices": [("correct a common misunderstanding about the placebo effect", True),
                        ("warn readers never to take any pills", False),
                        ("share a personal story about an illness", False),
                        ("compare two competing doctors", False)],
            "explanation": r"The passage exists to overturn the idea that the placebo effect is 'imaginary' -- a correction. The trap 'warn against all pills' isn't the point. Pro tip: a passage that says a common belief 'misunderstands' something is written to correct it.",
        },
        # ----- Passage 5: Satirical essay (parking garage) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"What our city truly needs, clearly, is another luxury parking garage. Never mind "
                     "the buses that arrive late or not at all, or the cracked sidewalks that send "
                     "pedestrians into the street. Let us pour our millions into yet more concrete for the "
                     "cars of those who already have everywhere to be. The rest can walk -- carefully.\"\n\n"
                     "What does the author actually believe the city should do?"),
            "difficulty": 3,
            "choices": [("Invest in transit and sidewalks rather than another luxury garage", True),
                        ("Build several more luxury parking garages", False),
                        ("Ban all private cars immediately", False),
                        ("Stop funding the city entirely", False)],
            "explanation": r"The praise of a garage is sarcastic; the real concern is the neglected buses and sidewalks. The trap 'build more garages' takes the irony literally. Pro tip: in satire, the author's true view is the opposite of the words on the page.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The author's tone is best described as:"),
            "difficulty": 3,
            "choices": [("sarcastic", True), ("sincerely admiring", False),
                        ("neutral and factual", False), ("frightened and anxious", False)],
            "explanation": r"'What our city truly needs, clearly' drips with mock approval -- sarcasm. The trap 'sincerely admiring' misses that the praise is fake. Pro tip: exaggerated agreement with a bad idea signals a sarcastic tone.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The rest can walk -- carefully.\"\n\n"
                     "The final word \"carefully\" mainly serves to:"),
            "difficulty": 3,
            "choices": [("highlight the danger that neglected pedestrians face", True),
                        ("praise people who walk cautiously", False),
                        ("explain a new parking regulation", False),
                        ("thank the city for its hard work", False)],
            "explanation": r"After the cracked sidewalks 'that send pedestrians into the street,' 'carefully' bitterly underlines the danger. The trap 'praise cautious walkers' misses the sting. Pro tip: a pointed final word in satire often twists the knife -- read it for irony.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The author is most concerned about:"),
            "difficulty": 3,
            "choices": [("the city neglecting basic needs in favor of luxuries", True),
                        ("a shortage of available parking spaces", False),
                        ("buses that travel too quickly", False),
                        ("the city building too many sidewalks", False)],
            "explanation": r"The real worry is spending 'millions' on luxury concrete while buses and sidewalks fail. The trap 'shortage of parking' is the fake concern the satire mocks. Pro tip: behind the sarcasm, look for the genuine problem the author wants fixed.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The passage makes its point chiefly through:"),
            "difficulty": 3,
            "choices": [("irony -- stating the opposite of what is truly meant", True),
                        ("straightforward step-by-step instructions", False),
                        ("detailed statistical evidence", False),
                        ("a heartfelt personal anecdote", False)],
            "explanation": r"The author argues by saying the reverse of the real message -- irony. The trap 'statistical evidence' describes a method the passage never uses. Pro tip: when praise and reality clearly clash, the technique is irony.",
        },
        # ----- Passage 6: Grief as weather (literary, extended metaphor) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Grief, she discovered, was not a wall but a weather. It did not stay put to be "
                     "climbed over and left behind; it moved through her in fronts and seasons. Some "
                     "mornings the sky was clear for hours before a sudden squall. She stopped waiting for "
                     "it to end, as one does not wait for winter to end, and learned instead to dress for "
                     "it.\"\n\n"
                     "Grief is compared to \"weather\" mainly to convey that it:"),
            "difficulty": 3,
            "choices": [("recurs unpredictably and cannot simply be passed and left behind", True),
                        ("is always cold and unpleasant", False),
                        ("can be controlled like a thermostat", False),
                        ("lasts for exactly one season", False)],
            "explanation": r"Weather 'in fronts and seasons,' with sudden squalls, captures grief's unpredictable return. The trap 'exactly one season' contradicts 'fronts and seasons.' Pro tip: an extended metaphor builds meaning across the passage -- here, grief's recurring, shifting nature.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...learned instead to dress for it.\"\n\n"
                     "This phrase most nearly suggests that she:"),
            "difficulty": 3,
            "choices": [("accepted living with grief and prepared to cope with it", True),
                        ("simply bought warmer winter clothing", False),
                        ("moved to a milder climate", False),
                        ("decided to ignore her grief completely", False)],
            "explanation": r"Within the weather metaphor, 'dressing for it' means adapting to live with grief rather than waiting it out. The trap 'warmer clothing' reads the metaphor literally. Pro tip: translate each part of an extended metaphor -- 'dressing for it' = preparing to cope.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "Calling grief \"not a wall but a weather\" rejects the idea that grief:"),
            "difficulty": 3,
            "choices": [("is a single obstacle you get past once and for all", True),
                        ("is genuinely a matter of the weather", False),
                        ("can never be survived at all", False),
                        ("is easy to ignore and forget", False)],
            "explanation": r"A wall is climbed once and left behind; rejecting that image says grief isn't a one-time obstacle. The trap 'genuinely about weather' takes the metaphor literally. Pro tip: a 'not X but Y' metaphor tells you what the writer is denying -- here, the one-and-done 'wall.'",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The tone of the passage is best described as:"),
            "difficulty": 3,
            "choices": [("reflective and quietly accepting", True), ("bitter and resentful", False),
                        ("cheerful and carefree", False), ("panicked and frantic", False)],
            "explanation": r"Discovering how to live with grief, calmly 'dressing for it,' creates a reflective, accepting tone. The trap 'bitter and resentful' clashes with that calm acceptance. Pro tip: a passage about coming to terms with hardship usually carries a reflective, accepting tone.",
        },
        # =====================================================================
        # ============ PART 2  --  LANGUAGE & EDITING =========================
        # =====================================================================
        {
            "text": ("**Language section.** Choose the correct verb form.\n\n"
                     "\"The board recommends that each member ______ the form before Friday.\""),
            "difficulty": 3,
            "choices": [("submit", True), ("submits", False), ("submitted", False), ("submitting", False)],
            "explanation": r"After 'recommends that,' the verb takes the base subjunctive form: 'that each member submit.' The trap 'submits' adds an -s that the subjunctive drops. Pro tip: verbs after 'recommend/require/insist that' use the plain base form.",
        },
        {
            "text": ("Choose the correct verb.\n\n"
                     "\"A number of students ______ absent from class today.\""),
            "difficulty": 3,
            "choices": [("are", True), ("is", False), ("was", False), ("has been", False)],
            "explanation": r"'A number of' means 'several' and takes a plural verb: 'a number of students are.' (Compare 'the number of students is.') The trap 'is' confuses the two phrases. Pro tip: 'a number of' = plural; 'the number of' = singular.",
        },
        {
            "text": ("Choose the option that keeps the sentence parallel.\n\n"
                     "\"She prefers hiking to ______.\""),
            "difficulty": 3,
            "choices": [("swimming", True), ("swim", False), ("to swim", False), ("a swim", False)],
            "explanation": r"To match the gerund 'hiking,' the comparison needs the gerund 'swimming.' The trap 'to swim' mixes an infinitive with a gerund. Pro tip: keep both sides of a comparison in the same form -- gerund with gerund.",
        },
        {
            "text": "Which sentence most clearly shows that the regular activity is the exercising (no squinting modifier)?",
            "difficulty": 3,
            "choices": [("People who regularly exercise become healthier.", True),
                        ("People who exercise regularly become healthier.", False),
                        ("People who exercise become regularly healthier.", False),
                        ("Regularly people who exercise become healthier.", False)],
            "explanation": r"Placing 'regularly' right before 'exercise' makes clear it describes the exercising, not the becoming. The trap 'exercise regularly become' could attach 'regularly' to either verb (a squinting modifier). Pro tip: put an adverb next to the exact verb it modifies to avoid ambiguity.",
        },
        {
            "text": "Which sentence uses semicolons correctly to separate complex list items?",
            "difficulty": 3,
            "choices": [("We visited Paris, France; Rome, Italy; and Madrid, Spain.", True),
                        ("We visited Paris, France, Rome, Italy, and Madrid, Spain.", False),
                        ("We visited Paris; France, Rome; Italy, and Madrid; Spain.", False),
                        ("We visited Paris France; Rome Italy; and Madrid Spain.", False)],
            "explanation": r"When list items already contain commas, separate the items with semicolons: 'Paris, France; Rome, Italy; ...' The trap with all commas blurs where each item ends. Pro tip: use semicolons as 'super-commas' when the items themselves contain commas.",
        },
        {
            "text": ("Choose the correct pronoun for the collective noun acting as a unit.\n\n"
                     "\"The team celebrated ______ hard-won victory.\""),
            "difficulty": 3,
            "choices": [("its", True), ("their", False), ("it's", False), ("they're", False)],
            "explanation": r"Treated as one unit, 'team' takes the singular possessive 'its.' The trap 'it's' means 'it is.' Pro tip: a collective noun acting as a single body pairs with the singular 'its.'",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"She is the candidate ______ we believe will win the election.\""),
            "difficulty": 3,
            "choices": [("who", True), ("whom", False), ("whose", False), ("which", False)],
            "explanation": r"The pronoun is the subject of 'will win,' so use 'who' -- the 'we believe' is just inserted. The trap 'whom' wrongly treats it as an object. Pro tip: ignore an inserted 'we believe/think' and check the pronoun's job in its own clause.",
        },
        {
            "text": ("Choose the correct verb form.\n\n"
                     "\"If the proposal ______ approved, the staff would celebrate.\""),
            "difficulty": 3,
            "choices": [("were", True), ("was", False), ("is", False), ("be", False)],
            "explanation": r"A hypothetical 'if' uses the subjunctive 'were': 'If the proposal were approved.' The trap 'was' is the common slip. Pro tip: pair a 'would' result clause with 'were' in the 'if' clause.",
        },
        {
            "text": ("Choose the correct preposition (idiom).\n\n"
                     "\"The new manager is fully capable ______ handling the project.\""),
            "difficulty": 3,
            "choices": [("of", True), ("to", False), ("for", False), ("in", False)],
            "explanation": r"The idiom is 'capable of' + an -ing verb. The trap 'to' would pair with 'able' ('able to handle'), not 'capable.' Pro tip: 'capable of doing' but 'able to do' -- the preposition depends on the adjective.",
        },
        {
            "text": "Which sentence clearly means the speaker failed nearly all of the tests?",
            "difficulty": 3,
            "choices": [("He failed almost every test.", True),
                        ("He almost failed every test.", False),
                        ("Almost, he failed every test.", False),
                        ("He failed every almost test.", False)],
            "explanation": r"'Almost every test' means nearly all tests were failed. The trap 'almost failed' means he nearly failed but didn't -- the opposite outcome. Pro tip: place 'almost' next to the word it limits; here it must modify 'every test.'",
        },
        {
            "text": ("Choose the option that keeps the correlative pair parallel.\n\n"
                     "\"You may either call the office or ______ the form.\""),
            "difficulty": 3,
            "choices": [("email", True), ("emailing", False), ("an email of", False), ("to email", False)],
            "explanation": r"'Either... or' must join matching forms; 'call' is a base verb, so its partner is 'email.' The trap 'emailing' breaks the parallel. Pro tip: both options after 'either/or' should take the same verb form.",
        },
        {
            "text": "Which sentence states the idea without redundancy?",
            "difficulty": 3,
            "choices": [("In my opinion, the plan is sound.", True),
                        ("In my own personal opinion, I personally think the plan is sound.", False),
                        ("I personally feel, in my opinion, that the plan is sound.", False),
                        ("My own personal view and opinion is the plan is sound.", False)],
            "explanation": r"'In my opinion' already signals a personal view, so 'own personal' and 'I personally' just repeat it. The traps stack redundant phrases. Pro tip: 'opinion' already implies it's yours -- cut 'personal,' 'own,' and 'I personally.'",
        },
        {
            "text": ("Choose the correct verb form in reported speech.\n\n"
                     "\"She said that she ______ tired after the long trip.\""),
            "difficulty": 3,
            "choices": [("was", True), ("is", False), ("will be", False), ("be", False)],
            "explanation": r"After the past-tense 'said,' the reported verb shifts to the past: 'said that she was tired.' The trap 'is' fails to match the past frame. Pro tip: in reported speech introduced by a past verb, the inner verb usually moves to the past too.",
        },
        {
            "text": "Which sentence correctly uses a comma between coordinate adjectives?",
            "difficulty": 3,
            "choices": [("It was a long, difficult journey.", True),
                        ("It was a long difficult, journey.", False),
                        ("It was a, long difficult journey.", False),
                        ("It was a long difficult journey,.", False)],
            "explanation": r"Two coordinate adjectives ('long' and 'difficult') describing 'journey' are separated by a comma between them: 'a long, difficult journey.' The traps misplace the comma. Pro tip: if you could put 'and' between the adjectives, use a comma there instead.",
        },
        {
            "text": "Which sentence fixes the vague pronoun \"this\"?",
            "difficulty": 3,
            "choices": [("The budget was cut and morale fell; this decline worried managers.", True),
                        ("The budget was cut and morale fell. This worried managers.", False),
                        ("The budget was cut and morale fell, this worried the managers a lot.", False),
                        ("The budget was cut and morale fell; this is what worried them.", False)],
            "explanation": r"A bare 'this' could point to the budget cut or the morale drop; adding a noun ('this decline') makes it clear. The traps leave 'this' standing alone. Pro tip: follow a vague 'this' with a noun that names exactly what it refers to.",
        },
        {
            "text": ("Choose the correct verb.\n\n"
                     "\"Neither of the proposed answers ______ entirely correct.\""),
            "difficulty": 3,
            "choices": [("is", True), ("are", False), ("were", False), ("have been", False)],
            "explanation": r"'Neither' is singular, so it takes 'is' -- 'of the proposed answers' doesn't change that. The trap 'are' agrees with 'answers.' Pro tip: 'neither' and 'either' as subjects are singular.",
        },
        {
            "text": ("Choose the option that keeps the list parallel.\n\n"
                     "\"The report was praised for being thorough, accurate, and ______.\""),
            "difficulty": 3,
            "choices": [("concise", True), ("it was concise", False),
                        ("having concision", False), ("to be concise", False)],
            "explanation": r"To match the adjectives 'thorough' and 'accurate,' the third item is the adjective 'concise.' The trap 'it was concise' breaks the pattern with a full clause. Pro tip: a list of adjectives must end with another adjective.",
        },
        {
            "text": "Which sentence has no dangling modifier?",
            "difficulty": 3,
            "choices": [("By studying hard, she passed the exam.", True),
                        ("By studying hard, the exam was passed.", False),
                        ("By studying hard, the exam became easy to pass.", False),
                        ("By studying hard, passing the exam happened.", False)],
            "explanation": r"'By studying hard' must describe a person who studies -- 'she.' The traps make 'the exam' or 'passing' do the studying. Pro tip: an opening 'By + -ing' phrase needs a human subject right after the comma.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the mastery (Level 4) full-length GED RLA practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 28 reading incl. a paired-passage set, Part 2: 18 language; all hard)."
        ))
