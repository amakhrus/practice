"""
Seed a THIRD full-length 'GED RLA' practice exam -- Level 3, the expert tier,
harder than ``seed_ged_rla_exam_level2``.

Same test-day structure (46 questions: Reading Comprehension + Language &
Editing; 150 minutes; Extended Response described; scored 100-200, 145 to pass),
but the items reach the top of the GED's range: a paired-passage comparison set,
irony and symbolism, rhetorical strategy and author's stance, the reconstruction
of memory, and grammar that reaches who/whom, the subjunctive mood, restrictive
vs. nonrestrictive clauses, conjunctive adverbs, and pronoun clarity.

Run:
    python manage.py seed_ged_rla_exam_level3
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Full-Length Practice Exam (Level 3 - Expert)",
    "slug": "ged-rla-exam-level3",
    "program": "GED",
    "subject": "rla",
    "description": (
        "The hardest of the early-tier GED Reasoning Through Language Arts practice exams, for students "
        "who have cleared Levels 1 and 2. Same test-day format -- 46 questions split into Reading "
        "Comprehension and Language & Editing, 150 minutes, the Extended Response described, scored "
        "100-200 (145 to pass) -- but the items sit at the top of the range: a paired-passage comparison "
        "set (comparing two texts on the same topic), irony and symbolism, rhetorical strategy and "
        "author's stance, dense informational reasoning, and grammar that reaches who/whom, the "
        "subjunctive mood, restrictive and nonrestrictive clauses, conjunctive adverbs, parallel "
        "structure, and pronoun clarity. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 3: The Expert Reading Test",
            r"""
This is the **expert** GED RLA practice exam. The format is unchanged:

- **46 questions** plus the **Extended Response**, in **150 minutes**.
- A **Reading Comprehension** part and a **Language & Editing** part; scored **100-200**, with **145 to pass**.

**What makes Level 3 harder:** the passages demand that you read for **strategy and stance**, not just content. A full **paired-passage set** asks you to compare two texts on the same topic -- where they agree, where they clash, and how their tones differ. Other items test **irony, symbolism, and rhetorical devices**. There are no give-away questions.

[[check:When two passages argue opposite sides of one topic, a question about their 'point of disagreement' asks you to find what?|the issue they disagree on;;what they disagree about;;the disagreement;;where they clash|Find the specific claim the two texts take opposite positions on.]]
            """,
        ),
        (
            "2. Comparing Texts, Reading for Strategy",
            r"""
Expert reading questions ask you to step back and see how a text works.

- **Paired passages** -- identify each text's main idea, the exact point they disagree on, any assumption they share, and how their tones differ.
- **Irony** -- when the real meaning is the opposite of the literal words, or when an outcome undercuts a character's intent.
- **Symbolism** -- when an object or image stands for a larger idea.
- **Rhetorical strategy** -- why a writer uses a rhetorical question, a contrast, or a loaded label.

[[figure:comp_supp|Two writers can share a goal yet support opposite conclusions -- read for both the claim and the reasoning behind it.]]

[[check:If a character brags about always being on time, and the brag itself makes others late, what is that an example of?|irony;;situational irony|The outcome contradicts the character's intent, which is irony.]]
            """,
        ),
        (
            "3. Expert Language & the Extended Response",
            r"""
The language items now reach the subtler rules of standard written English:

- **Who vs. whom** -- 'who' for the subject, 'whom' for the object.
- **Subjunctive mood** -- 'If I were you...' for hypotheticals.
- **Restrictive vs. nonrestrictive clauses** -- use commas only around information that could be removed without changing the core meaning.
- **Conjunctive adverbs** -- 'however' and 'therefore' need a semicolon before and a comma after when joining two complete thoughts.
- **Pronoun clarity** -- every pronoun must point to one clear noun.

The **Extended Response** rule never changes: argue which side is **better supported by evidence**, with a clear claim, support from both passages, and organized paragraphs.

[[check:In 'If I ___ you, I would apologize,' which verb form is correct -- was or were?|were|The subjunctive uses 'were' for a hypothetical: 'If I were you.']]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  READING COMPREHENSION ======================
        # =====================================================================
        # ----- Passage 1: Automation (argument) -----
        {
            "text": ("**Reading section.** Read the passage, then answer.\n\n"
                     "\"It is fashionable to fear that automation will erase work itself. History suggests "
                     "a subtler truth. When automated looms arrived, weavers suffered, but cloth grew "
                     "cheap, demand soared, and new jobs appeared that no one had imagined. The danger of "
                     "automation is rarely the disappearance of work; it is the painful gap between the "
                     "jobs that vanish and the ones that take their place. Easing that transition, not "
                     "halting the machines, is the real task.\"\n\n"
                     "What is the author's central argument?"),
            "difficulty": 3,
            "choices": [("The real problem of automation is the hard transition between lost jobs and new ones.", True),
                        ("Automation will inevitably erase all human work.", False),
                        ("Automation should be halted to protect jobs.", False),
                        ("Weaving will be the most important job of the future.", False)],
            "explanation": r"The author rejects the fear that work will vanish and locates the danger in 'the painful gap' between old and new jobs. The trap 'erase all human work' is the very view being refuted. Pro tip: when a passage says a common fear is wrong, the claim is the corrected version.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"When automated looms arrived, weavers suffered, but cloth grew cheap, demand "
                     "soared, and new jobs appeared that no one had imagined.\"\n\n"
                     "Why does the author include the example of automated looms?"),
            "difficulty": 3,
            "choices": [("To illustrate a historical pattern that supports the argument", True),
                        ("To prove weavers stayed unemployed forever", False),
                        ("To argue that cheap cloth is harmful", False),
                        ("To explain the mechanics of how a loom works", False)],
            "explanation": r"The loom story models the pattern the author claims repeats: disruption, then new jobs. The trap 'unemployed forever' contradicts 'new jobs appeared.' Pro tip: a historical example usually works as evidence for the writer's general point.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Easing that transition, not halting the machines, is the real task.\"\n\n"
                     "Based on the passage, the author would most likely:"),
            "difficulty": 3,
            "choices": [("oppose halting automation and support easing the transition", True),
                        ("support banning all new machines", False),
                        ("claim automation has no downsides at all", False),
                        ("argue that work will soon disappear", False)],
            "explanation": r"The closing line states the author's position directly. The trap 'banning all new machines' is what the author rejects ('not halting the machines'). Pro tip: a stance question is answered by the sentence that states what the author thinks should be done.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"History suggests a subtler truth.\"\n\n"
                     "As used here, \"subtler\" most nearly means:"),
            "difficulty": 2,
            "choices": [("more nuanced and less obvious", True), ("much louder", False),
                        ("simpler and more extreme", False), ("far older", False)],
            "explanation": r"A 'subtler truth' is a more nuanced one than the simple fear it replaces. The trap 'simpler and more extreme' is the opposite of subtle. Pro tip: 'subtle' means fine or nuanced, not loud or extreme.",
        },
        # ----- Passage 2: Gerald and punctuality (literary, irony) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Gerald prided himself on his punctuality. He arrived precisely on time to every "
                     "meeting, every dinner, every appointment -- a fact he mentioned often, and at "
                     "length, to anyone who would listen. His friends had learned that the surest way to "
                     "be late was to wait for Gerald to finish explaining how he never was.\"\n\n"
                     "The humor of the passage comes mainly from the fact that:"),
            "difficulty": 3,
            "choices": [("Gerald's long boasts about being on time end up making others late", True),
                        ("Gerald is secretly late to everything himself", False),
                        ("Gerald has no friends at all", False),
                        ("Gerald hates attending meetings", False)],
            "explanation": r"The irony is that his bragging about punctuality is exactly what makes people late. The trap 'late himself' misses that he really is punctual -- the talking is the problem. Pro tip: situational irony is an outcome that twists against the character's own point.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...a fact he mentioned often, and at length, to anyone who would listen.\"\n\n"
                     "Gerald is best characterized as:"),
            "difficulty": 3,
            "choices": [("proud and self-absorbed", True), ("shy and humble", False),
                        ("cruel and dishonest", False), ("forgetful and lazy", False)],
            "explanation": r"Bragging 'often, and at length' about himself marks him as proud and self-absorbed. The trap 'shy and humble' is the opposite. Pro tip: let a character's repeated behavior define them -- constant self-praise signals self-absorption.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...to anyone who would listen.\"\n\n"
                     "This phrase most strongly suggests that Gerald:"),
            "difficulty": 3,
            "choices": [("talks about himself more than others care to hear", True),
                        ("is rarely willing to speak", False),
                        ("is impossible to hear when he talks", False),
                        ("is beloved for his fascinating stories", False)],
            "explanation": r"'Anyone who would listen' hints that listeners are in short supply -- he over-shares. The trap 'beloved for his stories' misreads the dry tone. Pro tip: the phrase implies he'll corner whoever is willing, suggesting people tire of it.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The author's tone toward Gerald is best described as:"),
            "difficulty": 3,
            "choices": [("gently mocking", True), ("deeply admiring", False),
                        ("furious and bitter", False), ("mournful and sad", False)],
            "explanation": r"The wry final sentence pokes fun at Gerald without cruelty -- gentle mockery. The trap 'deeply admiring' misses the joke at his expense. Pro tip: humor at a character's expense, without malice, is a gently mocking tone.",
        },
        # ----- Passage 3: PAIRED PASSAGES on zoos -----
        {
            "text": ("Read both short texts, then answer.\n\n"
                     "TEXT 1: \"Modern zoos are arks of conservation. They breed endangered species, fund "
                     "field research, and introduce millions of visitors to animals they would otherwise "
                     "never see -- sparking the very concern that protects wildlife. A child who meets a "
                     "tiger may grow into an adult who fights to save it.\"\n\n"
                     "TEXT 2: \"No enclosure, however spacious, can replace the wild. A tiger that paces a "
                     "concrete yard is not an ambassador; it is a prisoner. Whatever good zoos claim to do "
                     "for conservation could be done in protected habitats, without confining the very "
                     "animals we say we admire.\"\n\n"
                     "What is the main idea of TEXT 1?"),
            "difficulty": 3,
            "choices": [("Zoos aid conservation and inspire people to protect wildlife.", True),
                        ("Zoos are cruel prisons that should be shut down.", False),
                        ("Children generally dislike seeing tigers.", False),
                        ("Conservation is hopeless and not worth attempting.", False)],
            "explanation": r"Text 1 calls zoos 'arks of conservation' and stresses how they inspire people to protect animals. The trap 'cruel prisons' is actually Text 2's view. Pro tip: anchor each text's main idea separately before you compare them.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "What is the main idea of TEXT 2?"),
            "difficulty": 3,
            "choices": [("No enclosure can replace the wild, so zoos needlessly confine animals.", True),
                        ("Zoos are arks of conservation that save species.", False),
                        ("Tigers are perfectly content in concrete yards.", False),
                        ("Conservation can only ever happen inside zoos.", False)],
            "explanation": r"Text 2 argues confinement can't replace the wild and isn't needed for conservation. The trap 'arks of conservation' borrows Text 1's phrase. Pro tip: don't let one text's memorable wording bleed into your reading of the other.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "The two texts most clearly disagree about whether:"),
            "difficulty": 3,
            "choices": [("zoos truly serve conservation and the animals' interests", True),
                        ("tigers are real animals", False),
                        ("children ever visit zoos", False),
                        ("the wild can be a dangerous place", False)],
            "explanation": r"Text 1 says zoos help wildlife; Text 2 says they needlessly confine it -- they clash on whether zoos genuinely serve conservation and the animals. The traps name points neither text disputes. Pro tip: the disagreement is the single claim on which the two texts take opposite sides.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "Compared with Text 1, the tone of Text 2 is:"),
            "difficulty": 3,
            "choices": [("more critical and indignant", True), ("more cheerful and approving", False),
                        ("exactly the same in attitude", False), ("more neutral and detached", False)],
            "explanation": r"Words like 'prisoner' and 'confining the very animals we say we admire' make Text 2 pointed and indignant, while Text 1 is hopeful. The trap 'cheerful and approving' fits Text 1, not Text 2. Pro tip: charged words ('prisoner') reveal a critical tone.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "Which assumption do BOTH texts share?"),
            "difficulty": 3,
            "choices": [("Protecting wildlife is a worthwhile goal.", True),
                        ("Zoos should be expanded everywhere.", False),
                        ("Animals do not experience any suffering.", False),
                        ("The wild no longer exists anywhere.", False)],
            "explanation": r"Text 1 wants to spark concern that 'protects wildlife'; Text 2 wants conservation done 'in protected habitats' -- both value protecting wildlife. The trap 'zoos should be expanded' is only Text 1-ish, not shared. Pro tip: a shared assumption is the common ground beneath two opposing arguments.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "In Text 2, calling the tiger \"a prisoner\" instead of \"an ambassador\" is meant to:"),
            "difficulty": 3,
            "choices": [("frame the zoo as unjust confinement", True),
                        ("praise the zoo's spacious design", False),
                        ("warn that tigers are dangerous to people", False),
                        ("describe a literal human prison", False)],
            "explanation": r"Rejecting 'ambassador' for 'prisoner' reframes the zoo as imprisonment, strengthening Text 2's argument. The trap 'praise the design' is the opposite effect. Pro tip: a writer's word choice ('prisoner') is a rhetorical move that shapes how you judge the subject.",
        },
        # ----- Passage 4: Memory as reconstruction (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"We tend to trust our memories as if they were recordings, faithfully preserving "
                     "what happened. In truth, memory is less a recording than a reconstruction, rebuilt "
                     "each time we recall it and quietly altered in the process. Studies show that "
                     "confident eyewitnesses are frequently mistaken, their certainty no guarantee of "
                     "accuracy. A leading question, asked weeks later, can plant details that were never "
                     "there.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 3,
            "choices": [("Memory is a fallible reconstruction, so confidence does not ensure accuracy.", True),
                        ("Memory works like a perfect, faithful recording.", False),
                        ("Eyewitnesses are essentially always correct.", False),
                        ("Leading questions reliably improve memory.", False)],
            "explanation": r"The passage replaces the 'recording' myth with memory as a changeable reconstruction. The trap 'perfect recording' is the belief being corrected. Pro tip: when a passage says 'in truth,' the words after it usually carry the main idea.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...memory is less a recording than a reconstruction...\"\n\n"
                     "The contrast between a \"recording\" and a \"reconstruction\" emphasizes that memory:"),
            "difficulty": 3,
            "choices": [("is actively rebuilt and can change, not fixed and exact", True),
                        ("is stored permanently on tape", False),
                        ("never changes once it forms", False),
                        ("cannot be studied by scientists", False)],
            "explanation": r"A recording stays fixed; a reconstruction is rebuilt and can shift -- the contrast stresses memory's changeability. The trap 'never changes' is the recording idea. Pro tip: a deliberate contrast highlights the quality the author wants you to notice -- here, instability.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...confident eyewitnesses are frequently mistaken, their certainty no guarantee of "
                     "accuracy.\"\n\n"
                     "What does the passage imply about a confident eyewitness?"),
            "difficulty": 3,
            "choices": [("They can be wrong despite feeling certain.", True),
                        ("They are always accurate.", False),
                        ("They never actually exist.", False),
                        ("They have flawless memories.", False)],
            "explanation": r"'Certainty no guarantee of accuracy' means confidence and correctness can come apart. The trap 'always accurate' is what the passage denies. Pro tip: 'no guarantee' signals that the two things -- confidence and accuracy -- don't always match.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"A leading question, asked weeks later, can plant details that were never there.\"\n\n"
                     "According to the passage, a leading question can:"),
            "difficulty": 2,
            "choices": [("add false details to a memory", True),
                        ("erase a memory completely", False),
                        ("improve a memory's accuracy", False),
                        ("record events perfectly", False)],
            "explanation": r"'Plant details that were never there' means it can add false memories. The trap 'improve accuracy' is the opposite. Pro tip: 'plant' here means to introduce something that wasn't real.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "As used in the passage, \"reconstruction\" most nearly means:"),
            "difficulty": 3,
            "choices": [("something rebuilt, not simply played back", True),
                        ("a permanent recording", False),
                        ("a complete deletion", False),
                        ("a printed photograph", False)],
            "explanation": r"The passage opposes 'reconstruction' to 'recording,' so it means something rebuilt each time, not replayed. The trap 'permanent recording' is the contrast term. Pro tip: when a word is defined against another, take the opposite of that other word.",
        },
        # ----- Passage 5: Persuasive speech -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"We are told that change is too costly, too slow, too hard. But ask yourselves: "
                     "what is the cost of standing still? Every year we delay, the problem deepens and the "
                     "price climbs. The easy road today is the expensive road tomorrow. I do not ask you "
                     "to act because it is comfortable. I ask you to act because it is right -- and "
                     "because waiting is a choice we can no longer afford.\"\n\n"
                     "What is the speaker's main purpose?"),
            "difficulty": 3,
            "choices": [("To urge the audience to act now instead of waiting", True),
                        ("To explain the technical steps of a process", False),
                        ("To entertain listeners with a humorous story", False),
                        ("To describe past events in a neutral way", False)],
            "explanation": r"The speech pushes the audience to act ('I ask you to act... waiting is a choice we can no longer afford'). The trap 'explain technical steps' mistakes a persuasive call for an explanation. Pro tip: repeated calls to 'act' mark a persuasive purpose.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"But ask yourselves: what is the cost of standing still?\"\n\n"
                     "The speaker asks this question mainly to:"),
            "difficulty": 3,
            "choices": [("make listeners weigh the cost of doing nothing", True),
                        ("request a specific dollar amount", False),
                        ("admit the plan is too expensive", False),
                        ("change the subject of the speech", False)],
            "explanation": r"It's a rhetorical question that nudges the audience to consider inaction's price. The trap 'request a dollar amount' takes it literally. Pro tip: a rhetorical question isn't seeking an answer -- it's steering the audience's thinking.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The easy road today is the expensive road tomorrow.\"\n\n"
                     "This sentence makes its point by:"),
            "difficulty": 3,
            "choices": [("contrasting present comfort with future cost", True),
                        ("describing an actual highway", False),
                        ("listing different types of roads", False),
                        ("praising the benefits of delay", False)],
            "explanation": r"It sets 'easy... today' against 'expensive... tomorrow' -- a contrast that warns against delay. The trap 'actual highway' reads the metaphor literally. Pro tip: a balanced 'today vs. tomorrow' structure is a contrast used for emphasis.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The speaker's tone is best described as:"),
            "difficulty": 3,
            "choices": [("urgent and resolute", True), ("casual and indifferent", False),
                        ("playful and joking", False), ("uncertain and timid", False)],
            "explanation": r"Phrases like 'we can no longer afford' and 'act because it is right' are urgent and firm. The trap 'casual and indifferent' clashes with that intensity. Pro tip: strong, pressing language signals an urgent, resolute tone.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The speaker most directly answers the objection that:"),
            "difficulty": 3,
            "choices": [("change costs too much", True),
                        ("the audience is too small to matter", False),
                        ("the problem has already been solved", False),
                        ("waiting costs nothing at all", False)],
            "explanation": r"The speech opens by naming the objection ('change is too costly') and then argues that delay costs even more. The trap 'waiting costs nothing' is what the speaker refutes. Pro tip: a speaker often states the opposing objection in order to knock it down.",
        },
        # ----- Passage 6: The lighthouse keeper (literary, symbol) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The lighthouse had not lit in forty years, yet the old keeper climbed its stairs "
                     "each evening out of habit, as if the dark might forget how to fall without him. At "
                     "the top he would stand a while, looking out at ships that no longer needed his lamp, "
                     "and then descend, satisfied, as though he had done his part.\"\n\n"
                     "The unlit lighthouse most likely symbolizes:"),
            "difficulty": 3,
            "choices": [("a role that is no longer needed but still gives the keeper purpose", True),
                        ("the latest advance in shipping technology", False),
                        ("a dangerous approaching storm", False),
                        ("the keeper's hidden wealth", False)],
            "explanation": r"A lighthouse that no longer lights yet still draws the keeper stands for an outlived purpose that still matters to him. The trap 'shipping technology' misses the emotional symbolism. Pro tip: a symbol links a physical object to a larger idea -- here, fading purpose.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...the old keeper climbed its stairs each evening out of habit...\"\n\n"
                     "Why does the keeper most likely continue his nightly climb?"),
            "difficulty": 3,
            "choices": [("The routine still gives his life a sense of purpose.", True),
                        ("The lighthouse still guides passing ships.", False),
                        ("He is paid a high wage to do it.", False),
                        ("He is afraid of the staircase.", False)],
            "explanation": r"He climbs 'out of habit' and descends 'satisfied... as though he had done his part' -- the ritual gives him meaning. The trap 'still guides ships' contradicts 'ships that no longer needed his lamp.' Pro tip: a character's satisfaction reveals the emotional reason behind an unnecessary act.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...as if the dark might forget how to fall without him.\"\n\n"
                     "This phrase most reasonably suggests that the keeper:"),
            "difficulty": 3,
            "choices": [("clings to a sense of being needed, though his task is unnecessary", True),
                        ("literally controls when night falls", False),
                        ("believes night will never come again", False),
                        ("knows the lighthouse still works", False)],
            "explanation": r"The gentle exaggeration shows he holds onto feeling needed, even though night clearly falls without him. The trap 'literally controls night' takes the image at face value. Pro tip: 'as if' marks a figurative idea -- read it for feeling, not fact.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The tone of the passage is best described as:"),
            "difficulty": 3,
            "choices": [("tender and bittersweet", True), ("frightening and tense", False),
                        ("comic and absurd", False), ("cold and angry", False)],
            "explanation": r"The quiet devotion to an obsolete duty creates a gentle, bittersweet feeling. The trap 'frightening and tense' fits nothing in the calm scene. Pro tip: affection mixed with a sense of loss produces a bittersweet tone.",
        },
        # =====================================================================
        # ============ PART 2  --  LANGUAGE & EDITING =========================
        # =====================================================================
        {
            "text": ("**Language section.** Choose the correct word.\n\n"
                     "\"To ______ should I address the complaint?\""),
            "difficulty": 3,
            "choices": [("whom", True), ("who", False), ("whose", False), ("who's", False)],
            "explanation": r"After the preposition 'to,' use the object form 'whom.' The trap 'who' is a subject pronoun. Pro tip: if you could answer with 'him' (address it to him), use 'whom.'",
        },
        {
            "text": ("Choose the correct verb form.\n\n"
                     "\"If I ______ you, I would apologize right away.\""),
            "difficulty": 3,
            "choices": [("were", True), ("was", False), ("am", False), ("be", False)],
            "explanation": r"A hypothetical 'if' uses the subjunctive 'were': 'If I were you.' The trap 'was' is the common error. Pro tip: for an imaginary or contrary-to-fact situation, use 'were' for every subject.",
        },
        {
            "text": "Which sentence punctuates a nonessential clause correctly?",
            "difficulty": 3,
            "choices": [("The book, which I bought yesterday, is on the table.", True),
                        ("The book which I bought yesterday, is on the table.", False),
                        ("The book, which I bought yesterday is on the table.", False),
                        ("The book which, I bought yesterday, is on the table.", False)],
            "explanation": r"A nonessential clause is set off by a comma on each side: 'The book, which I bought yesterday, is...' The traps drop one comma. Pro tip: extra information that could be removed needs a comma before AND after it.",
        },
        {
            "text": "Which sentence avoids an unclear pronoun reference?",
            "difficulty": 3,
            "choices": [("When Sara met Lily, Sara was the nervous one.", True),
                        ("When Sara met Lily, she was nervous.", False),
                        ("When Sara met Lily, she was nervous about her.", False),
                        ("Meeting her, she was nervous.", False)],
            "explanation": r"With two women in the sentence, 'she' is ambiguous; naming 'Sara' makes it clear. The traps leave 'she' pointing to either woman. Pro tip: if a pronoun could refer to more than one noun, repeat the name.",
        },
        {
            "text": ("Choose the correct verb for the collective noun.\n\n"
                     "\"The committee ______ deeply divided on the new policy.\""),
            "difficulty": 3,
            "choices": [("is", True), ("are", False), ("am", False), ("be", False)],
            "explanation": r"Treated as a single unit, 'committee' takes the singular 'is.' The trap 'are' treats the group as individuals. Pro tip: a collective noun acting as one body usually takes a singular verb.",
        },
        {
            "text": ("Choose the option that keeps the correlative pair parallel.\n\n"
                     "\"She is not only talented but also ______.\""),
            "difficulty": 3,
            "choices": [("hardworking", True), ("works very hard", False),
                        ("a person who works hard", False), ("to work hard", False)],
            "explanation": r"'Not only... but also' must join matching forms; 'talented' is an adjective, so the partner is the adjective 'hardworking.' The trap 'works very hard' is a verb phrase. Pro tip: correlative conjunctions (not only/but also) need the same grammatical form on both sides.",
        },
        {
            "text": ("Choose the option with correct subject-verb agreement.\n\n"
                     "\"Each of the proposals ______ real merit.\""),
            "difficulty": 2,
            "choices": [("has", True), ("have", False), ("were", False), ("having", False)],
            "explanation": r"'Each' is singular, so it takes 'has' -- 'of the proposals' doesn't change it. The trap 'have' agrees with 'proposals.' Pro tip: 'each,' 'either,' and 'neither' are singular.",
        },
        {
            "text": "Which sentence places \"only\" so that it means the speaker eats vegetables on no other day?",
            "difficulty": 3,
            "choices": [("He eats vegetables only on Mondays.", True),
                        ("He only eats vegetables on Mondays.", False),
                        ("Only he eats vegetables on Mondays.", False),
                        ("He eats only vegetables on Mondays.", False)],
            "explanation": r"To limit the day, 'only' must sit right before 'on Mondays.' The trap 'only eats' limits the action (eating) instead of the day. Pro tip: place 'only' directly before the word it is meant to restrict.",
        },
        {
            "text": "Which sentence correctly punctuates the conjunctive adverb \"however\"?",
            "difficulty": 3,
            "choices": [("I studied hard; however, I still failed the test.", True),
                        ("I studied hard, however I still failed the test.", False),
                        ("I studied hard however; I still failed the test.", False),
                        ("I studied hard however, I still failed the test.", False)],
            "explanation": r"When 'however' joins two complete thoughts, use a semicolon before it and a comma after: '...hard; however, I...' The traps misplace the punctuation. Pro tip: 'however' between two sentences takes 'semicolon-however-comma.'",
        },
        {
            "text": ("Choose the option that keeps the pronoun consistent in formal usage.\n\n"
                     "\"When one studies regularly, ______ tends to perform better.\""),
            "difficulty": 3,
            "choices": [("one", True), ("you", False), ("they", False), ("we", False)],
            "explanation": r"A sentence that begins with 'one' should continue with 'one' to avoid a pronoun shift. The trap 'you' switches person mid-sentence. Pro tip: don't shift from 'one' to 'you' or 'they' within the same sentence.",
        },
        {
            "text": ("Choose the correct verb form.\n\n"
                     "\"By the time we arrived at the station, the train ______.\""),
            "difficulty": 3,
            "choices": [("had left", True), ("has left", False), ("leaves", False), ("will leave", False)],
            "explanation": r"The leaving happened before the arriving, so use the past perfect 'had left.' The trap 'has left' is present perfect, which doesn't fit a past timeline. Pro tip: for an action completed before another past action, use 'had' + past participle.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"______ been raining all day, so the dog wants to stay inside.\""),
            "difficulty": 2,
            "choices": [("It's", True), ("Its", False), ("Its'", False), ("It", False)],
            "explanation": r"'It's' means 'it has' here ('It has been raining'). 'Its' shows possession. Pro tip: 'it's' can stand for 'it is' OR 'it has' -- both use the apostrophe.",
        },
        {
            "text": ("Choose the correct pronoun.\n\n"
                     "\"My brother is taller than ______.\""),
            "difficulty": 3,
            "choices": [("I am", True), ("me am", False), ("myself", False), ("mine", False)],
            "explanation": r"The comparison is short for 'taller than I am,' so the subject pronoun 'I' is correct. The trap 'myself' is a reflexive, used only when the subject acts on itself. Pro tip: finish the comparison in your head ('than I am') to pick the right pronoun.",
        },
        {
            "text": "Which sentence has no dangling modifier?",
            "difficulty": 3,
            "choices": [("While walking home, I got caught in the rain.", True),
                        ("While walking home, the rain caught me.", False),
                        ("While walking home, the rain began to fall on me.", False),
                        ("Walking home, the storm soaked everything.", False)],
            "explanation": r"'While walking home' must describe a person; only 'I got caught' supplies one. The traps make 'the rain' or 'the storm' do the walking. Pro tip: the noun right after an opening -ing phrase must be the one performing that action.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"The medicine had a positive ______ on her recovery.\""),
            "difficulty": 2,
            "choices": [("effect", True), ("affect", False), ("affects", False), ("effected", False)],
            "explanation": r"Here the word is a noun meaning 'result,' so 'effect' is correct. The trap 'affect' is normally the verb. Pro tip: after 'a' or 'an' and an adjective ('a positive ___'), you need the noun 'effect.'",
        },
        {
            "text": "Which sentence is punctuated correctly after its introductory clause?",
            "difficulty": 2,
            "choices": [("After the meeting ended, we went to lunch.", True),
                        ("After the meeting ended we went to lunch.", False),
                        ("After the meeting, ended we went to lunch.", False),
                        ("After, the meeting ended we went to lunch.", False)],
            "explanation": r"An introductory clause is followed by a comma: 'After the meeting ended, we...' The traps omit or misplace the comma. Pro tip: put a comma after an introductory clause before the main sentence begins.",
        },
        {
            "text": "Which sentence states the idea most concisely?",
            "difficulty": 2,
            "choices": [("We must decide now.", True),
                        ("At this point in time, we must make a decision.", False),
                        ("In the current moment we are now in, a decision must be made.", False),
                        ("We must, at this present time, come to a decision now.", False)],
            "explanation": r"'We must decide now' carries the full meaning with no padding. The traps inflate it with phrases like 'at this point in time.' Pro tip: prefer a single strong verb ('decide') and cut filler time-phrases.",
        },
        {
            "text": ("Choose the option that keeps the list parallel.\n\n"
                     "\"The coach told the team to rest, to hydrate, and ______.\""),
            "difficulty": 2,
            "choices": [("to stretch", True), ("stretching", False),
                        ("they should stretch", False), ("stretch it all out", False)],
            "explanation": r"To match 'to rest' and 'to hydrate,' the third item is 'to stretch.' The trap 'stretching' breaks the to-verb pattern. Pro tip: once a list starts with 'to + verb,' every item should follow that form.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the expert (Level 3) full-length GED RLA practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 28 reading incl. a paired-passage set, Part 2: 18 language)."
        ))
