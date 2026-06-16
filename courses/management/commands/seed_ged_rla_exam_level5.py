"""
Seed a FIFTH and FINAL full-length 'GED RLA' practice exam -- Level 5, the elite
tier, the hardest of the whole set.

Same test-day structure (46 questions: Reading Comprehension + Language &
Editing; 150 minutes; Extended Response described; scored 100-200, 145 to pass).
Every item is a hard, multi-layered problem at the absolute ceiling of the GED's
range: argument logic with concession and analogy, literary diction and theme,
a paired-passage set that asks which text is better supported and how one author
would answer the other, the paradox of choice, tone-shift rhetoric, multi-device
literary analysis, and grammar that reaches faulty comparisons, inverted
subject-verb agreement, the conditional-perfect mood, complex who/whom, and
precise diction.

Run:
    python manage.py seed_ged_rla_exam_level5
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Full-Length Practice Exam (Level 5 - Elite)",
    "slug": "ged-rla-exam-level5",
    "program": "GED",
    "subject": "rla",
    "description": (
        "The fifth and hardest full-length GED Reasoning Through Language Arts practice exam -- the elite "
        "tier, for students who have cleared Levels 1-4 and want the toughest possible rehearsal. Same "
        "test-day format -- 46 questions split into Reading Comprehension and Language & Editing, 150 "
        "minutes, the Extended Response described, scored 100-200 (145 to pass) -- but every item sits at "
        "the ceiling of the range: argument logic with concession and analogy, literary diction and "
        "theme, a paired-passage set that weighs which argument is better supported and how one author "
        "would answer the other, the paradox of choice, tone-shift rhetoric, multi-device literary "
        "analysis, and grammar that reaches faulty comparisons, inverted subject-verb agreement, the "
        "conditional-perfect mood, complex who/whom, idiomatic usage, and precise diction. Every question "
        "includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 5: The Elite Reading Test",
            r"""
This is the **elite** GED RLA practice exam -- the toughest of all five. The format never changes:

- **46 questions** plus the **Extended Response**, in **150 minutes**; scored **100-200**, **145 to pass**.

**What makes Level 5 the hardest of all:** there is not a single routine question. You will trace an argument's **logic** (its concession, its analogy, the limit it sets), analyze a passage's **diction and theme**, decide **which of two texts is better supported** and how one author would **answer** the other, and read literary passages that stack **several devices** at once. If you can score well here, the real GED RLA test will feel comfortable.

[[check:An author admits 'many ideas deserve no respect' before defending free speech anyway. What is that opening move called?|a concession;;concession|It is a concession -- granting a point to the other side before arguing past it.]]
            """,
        ),
        (
            "2. Reading at the Highest Level",
            r"""
Elite reading is about evaluating and weighing, not just understanding.

- **Argument logic** -- separate the claim, the concession, the analogy, and the limit the author sets.
- **Diction and theme** -- how precise word choices ('blinded windows,' weeds with 'the confidence of an heir') build a passage's deeper meaning.
- **Evaluating evidence** -- in a paired set, decide which text is better supported and predict how each author would answer the other.
- **Tone shifts** -- track where and why a writer's attitude changes, and what triggers it.
- **Layered literary devices** -- personification, irony, symbol, and theme working together in one passage.

[[figure:argument|At this level, judge not just what each side claims but how well each claim is supported.]]

[[check:In a paired set, a question asks which passage is 'better supported.' Are you judging which view you prefer or which text backs its claim with stronger evidence?|which has stronger evidence;;stronger evidence;;the one with better evidence;;evidence|Judge the strength of the support, not your own preference.]]
            """,
        ),
        (
            "3. Elite Language & the Extended Response",
            r"""
The language items now test grammar and style at the very top of the range:

- **Faulty comparisons** -- 'more original than any OTHER writer'; compare like with like.
- **Inverted agreement** -- find the true subject when it follows the verb ('Among the files was a contract').
- **Conditional-perfect mood** -- 'If she had known, she would have left.'
- **Complex who/whom** -- the pronoun's role inside its own clause decides the form.
- **Precise diction and concision** -- the exact word, with nothing wasted.

The **Extended Response** standard never changes: argue which side is **better supported by evidence**, with a clear claim, support drawn from both passages, and organized paragraphs. At this level, the strongest essays also weigh and answer the opposing argument.

[[check:'If she had known, she ___ earlier.' Which completes the conditional-perfect correctly -- 'would leave' or 'would have left'?|would have left|A past hypothetical takes 'would have' + past participle: 'would have left.']]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ PART 1  --  READING COMPREHENSION ======================
        # =====================================================================
        # ----- Passage 1: Free speech (argument w/ concession & analogy) -----
        {
            "text": ("**Reading section.** Read the passage, then answer.\n\n"
                     "\"The strongest case for free speech is not that every idea deserves respect; many "
                     "ideas deserve none. It is that no one can be trusted to decide, once and for all, "
                     "which ideas those are. Hand that power to a wise authority and it may silence folly; "
                     "hand it to a foolish one, and it will silence wisdom. Since we cannot guarantee the "
                     "wise hand, we are safer leaving the gate open -- and answering bad speech with "
                     "better.\"\n\n"
                     "What is the author's central argument?"),
            "difficulty": 3,
            "choices": [("No authority can be safely trusted to decide which ideas to suppress.", True),
                        ("Every idea deserves equal respect and protection.", False),
                        ("A wise authority should decide which ideas to ban.", False),
                        ("Speech never has any real consequences.", False)],
            "explanation": r"The argument is that the power to censor can't be safely entrusted to anyone, so the gate should stay open. The trap 'every idea deserves respect' is explicitly denied in the first line. Pro tip: the real claim is what survives after the author rejects the obvious version.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...many ideas deserve none.\"\n\n"
                     "In making this statement, the author is:"),
            "difficulty": 3,
            "choices": [("conceding a point before arguing past it", True),
                        ("claiming free speech is always harmful", False),
                        ("insisting authorities are always wise", False),
                        ("denying that any idea can be foolish", False)],
            "explanation": r"Admitting 'many ideas deserve none' grants ground to opponents, then the argument moves on -- a concession. The trap 'always harmful' misreads the move. Pro tip: a concession strengthens an argument by showing the author isn't ignoring the other side.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Hand that power to a wise authority and it may silence folly; hand it to a foolish "
                     "one, and it will silence wisdom.\"\n\n"
                     "This balanced pair mainly serves to show that:"),
            "difficulty": 3,
            "choices": [("the same censoring power could destroy good ideas as easily as bad", True),
                        ("wise authorities never make any mistakes", False),
                        ("folly and wisdom are exactly the same thing", False),
                        ("speech should always be silenced by experts", False)],
            "explanation": r"The mirror-image sentence shows that the very power meant to remove folly could just as easily remove wisdom. The trap 'never make mistakes' is the opposite of the warning. Pro tip: a deliberately balanced contrast highlights a risk that cuts both ways.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...answering bad speech with better.\"\n\n"
                     "This phrase implies that the author favors:"),
            "difficulty": 3,
            "choices": [("countering harmful ideas with stronger argument rather than suppression", True),
                        ("ignoring all speech entirely", False),
                        ("punishing those who speak badly", False),
                        ("permanently closing the gate to ideas", False)],
            "explanation": r"'Answering bad speech with better' means refuting bad ideas through better ones, not banning them. The trap 'punishing speakers' contradicts the open-gate stance. Pro tip: the author's proposed remedy is the alternative to the thing they argued against -- here, argument instead of censorship.",
        },
        # ----- Passage 2: The grand house (literary, diction/theme) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The house had been grand once. You could still read its former dignity in the tall "
                     "windows, now blinded with plywood, and in the marble steps worn to a gentle slope by "
                     "a century of feet that no longer came. Weeds had taken the garden with the quiet "
                     "confidence of an heir. Nothing about the place was loud; it was simply, patiently, "
                     "returning to the earth.\"\n\n"
                     "What is the central idea of the passage?"),
            "difficulty": 3,
            "choices": [("Time and neglect are quietly reclaiming what was once grand.", True),
                        ("The house will soon be fully restored.", False),
                        ("The garden is being carefully maintained.", False),
                        ("The house was never actually impressive.", False)],
            "explanation": r"'Returning to the earth,' worn steps, and overtaking weeds all show slow decay reclaiming a once-grand house. The trap 'never impressive' contradicts 'had been grand once.' Pro tip: gather the images of decline -- together they state the theme of quiet reclamation.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Weeds had taken the garden with the quiet confidence of an heir.\"\n\n"
                     "This comparison most nearly suggests that:"),
            "difficulty": 3,
            "choices": [("nature is calmly and rightfully taking possession of the property", True),
                        ("the weeds had only recently been planted", False),
                        ("a human heir legally owns the house", False),
                        ("the garden is thriving under careful care", False)],
            "explanation": r"An heir inherits by right and without hurry; the weeds take over with that same calm entitlement. The trap 'a human heir owns it' takes the figure literally. Pro tip: a simile transfers a quality -- here, the unhurried certainty of rightful inheritance -- onto nature.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...the tall windows, now blinded with plywood...\"\n\n"
                     "As used here, \"blinded\" most nearly means:"),
            "difficulty": 3,
            "choices": [("covered over so no light passes through", True),
                        ("polished until they shone", False),
                        ("freshly installed and new", False),
                        ("left wide open to the air", False)],
            "explanation": r"Windows 'blinded with plywood' are boarded so they can't let in light, like blinded eyes. The trap 'polished until they shone' is the opposite. Pro tip: the personifying word 'blinded' treats windows like eyes -- covered, unable to 'see' or admit light.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The tone of the passage is best described as:"),
            "difficulty": 3,
            "choices": [("elegiac and quietly mournful", True), ("cheerful and lively", False),
                        ("tense and suspenseful", False), ("comic and mocking", False)],
            "explanation": r"The gentle dwelling on lost grandeur and slow decay creates an elegiac, mournful tone. The trap 'cheerful and lively' clashes with the imagery of decline. Pro tip: a passage that lingers tenderly over loss carries an elegiac tone.",
        },
        # ----- Passage 3: PAIRED PASSAGES on the internet and deep reading -----
        {
            "text": ("Read both short texts, then answer.\n\n"
                     "TEXT 1: \"Critics mourn that the internet has destroyed our capacity for deep "
                     "reading. The complaint is as old as every new medium; Socrates feared that writing "
                     "itself would ruin memory. People still read long and hard when a text rewards it. "
                     "What has changed is not our brains but the sheer volume of trivial things now "
                     "competing for a glance.\"\n\n"
                     "TEXT 2: \"It is comforting to say our minds are unchanged, but the evidence is less "
                     "kind. Studies find that habitual skimming reshapes how we read even books, training "
                     "the eye to hunt for keywords and the mind to resist the slow, linear attention that "
                     "long arguments require. A tool used daily does not leave its user untouched.\"\n\n"
                     "What is the position of TEXT 1?"),
            "difficulty": 3,
            "choices": [("Our capacity for deep reading is intact; only the distractions have grown.", True),
                        ("The internet has permanently destroyed deep reading.", False),
                        ("No one reads anything at all anymore.", False),
                        ("Writing truly did ruin human memory.", False)],
            "explanation": r"Text 1 says 'what has changed is not our brains but the... volume of trivial things' -- the ability survives. The trap 'destroyed deep reading' is the view Text 1 resists. Pro tip: Text 1 is the reassuring case; pin its thesis before comparing.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "What is the position of TEXT 2?"),
            "difficulty": 3,
            "choices": [("Habitual skimming actually changes how we read, even books.", True),
                        ("Our minds are completely unchanged by the internet.", False),
                        ("Long arguments are worthless and should be avoided.", False),
                        ("Socrates was right that writing ruins memory.", False)],
            "explanation": r"Text 2 argues 'habitual skimming reshapes how we read even books.' The trap 'completely unchanged' is Text 1's view, which Text 2 rejects. Pro tip: Text 2 is the cautionary, evidence-based case.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "Text 2 most directly counters Text 1's claim that:"),
            "difficulty": 3,
            "choices": [("our brains are unchanged -- only our environment has changed", True),
                        ("Socrates feared the invention of writing", False),
                        ("trivial things compete for our attention", False),
                        ("people still enjoy reading long texts", False)],
            "explanation": r"Text 1 insists the change is environmental, not mental; Text 2 answers that skimming 'reshapes how we read,' i.e., the brain itself. The traps name points Text 2 doesn't dispute. Pro tip: to find the rebuttal, locate the exact claim the second text sets out to overturn.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "Text 1 mentions Socrates' fear of writing mainly to:"),
            "difficulty": 3,
            "choices": [("imply that alarm over each new medium is a recurring, exaggerated pattern", True),
                        ("prove that writing really did ruin memory", False),
                        ("argue that Socrates personally disliked reading", False),
                        ("suggest that the internet is an ancient invention", False)],
            "explanation": r"Citing an ancient, overblown fear suggests today's panic is just the latest in a long, exaggerated line. The trap 'writing did ruin memory' would undercut Text 1's own point. Pro tip: a historical parallel is usually offered to make a current worry look familiar and overstated.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "Compared with Text 1, Text 2 relies more heavily on:"),
            "difficulty": 3,
            "choices": [("cited research findings", True),
                        ("a famous historical anecdote", False),
                        ("pure personal speculation", False),
                        ("insults aimed at its opponents", False)],
            "explanation": r"Text 2 grounds its case in 'studies find...,' while Text 1 leans on the Socrates anecdote. The trap 'historical anecdote' describes Text 1's method. Pro tip: notice each text's kind of support -- research data versus historical illustration.",
        },
        {
            "text": ("Refer to the two texts above.\n\n"
                     "The central unresolved disagreement between the texts is whether:"),
            "difficulty": 3,
            "choices": [("the real change is in our surroundings or in our minds themselves", True),
                        ("people read at all anymore", False),
                        ("Socrates actually existed", False),
                        ("books are still being printed", False)],
            "explanation": r"Text 1 locates the change outside us (distractions); Text 2 locates it inside us (rewired reading). That is the core clash. The traps name points neither disputes. Pro tip: the deepest disagreement is the single question the two texts answer in opposite ways.",
        },
        # ----- Passage 4: The paradox of choice (informational) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"We assume that more choice always means more freedom, and to a point it does. But "
                     "beyond that point, abundance curdles into paralysis. Faced with forty kinds of jam, "
                     "shoppers in one study were less likely to buy any than those offered six. Each "
                     "rejected option becomes a small regret, and the sum of those regrets can sour the "
                     "very satisfaction the choice was meant to provide. Freedom, it turns out, can be a "
                     "burden as well as a gift.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 3,
            "choices": [("Beyond a point, more choice can paralyze us and reduce satisfaction.", True),
                        ("More choice always and only increases freedom.", False),
                        ("Choice has no measurable effect on people.", False),
                        ("Shoppers always prefer forty options to six.", False)],
            "explanation": r"The passage qualifies the 'more choice = more freedom' idea, arguing that excess choice can paralyze and dissatisfy. The trap 'always and only increases freedom' is the belief the passage limits. Pro tip: when a passage says 'to a point... but beyond that point,' the main idea lives in the 'but.'",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Faced with forty kinds of jam, shoppers in one study were less likely to buy any "
                     "than those offered six.\"\n\n"
                     "The jam study is included mainly to:"),
            "difficulty": 3,
            "choices": [("provide concrete evidence that too many options can discourage choosing", True),
                        ("prove that people generally dislike jam", False),
                        ("show that six is the perfect number forever", False),
                        ("argue against shopping of any kind", False)],
            "explanation": r"The study is evidence for the claim that abundance can paralyze. The trap 'six is perfect forever' over-reads one example. Pro tip: a specific study in an argument almost always functions as supporting evidence, not the conclusion itself.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...abundance curdles into paralysis.\"\n\n"
                     "This phrase suggests that too much choice:"),
            "difficulty": 3,
            "choices": [("spoils into an inability to decide", True),
                        ("improves the quality of decisions", False),
                        ("simply produces more jam", False),
                        ("has no downside at all", False)],
            "explanation": r"'Curdles' (like milk going bad) into 'paralysis' means abundance spoils into an inability to act. The trap 'improves decisions' is the opposite. Pro tip: the verb 'curdles' carries a negative turn -- something good going bad.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The passage most strongly implies that the ideal amount of choice is:"),
            "difficulty": 3,
            "choices": [("moderate -- enough to matter without overwhelming", True),
                        ("as large as it can possibly be", False),
                        ("zero, with no options at all", False),
                        ("exactly forty options", False)],
            "explanation": r"Since 'to a point' choice helps but 'beyond that point' it harms, the implied ideal is moderate. The trap 'as large as possible' is what the passage warns against. Pro tip: when a passage describes a tipping point, it implies a middle amount is best.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Freedom, it turns out, can be a burden as well as a gift.\"\n\n"
                     "The author concludes that freedom:"),
            "difficulty": 3,
            "choices": [("can be both a gift and a burden", True),
                        ("is always purely a gift", False),
                        ("is always purely a burden", False),
                        ("has nothing to do with choice", False)],
            "explanation": r"The closing line explicitly calls freedom both 'a burden as well as a gift.' The traps pick only one side. Pro tip: a 'both... and...' conclusion resists either extreme -- match it exactly.",
        },
        # ----- Passage 5: The old library (rhetoric, tone shift) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"For years I defended the old library building out of pure sentiment. Its leaks, "
                     "its drafts, its groaning radiators were, I told myself, the marks of character. Then "
                     "I watched a child turn away from a ruined, water-stained book, and my sentiment "
                     "curdled into something harder. Affection for a building is a fine thing -- until it "
                     "costs a reader a page. We do not honor the past by letting it fail the present.\"\n\n"
                     "What does the writer ultimately argue?"),
            "difficulty": 3,
            "choices": [("Sentiment for an old building must not be allowed to fail today's readers.", True),
                        ("The old library should be preserved exactly as it is.", False),
                        ("Children should not be allowed to read library books.", False),
                        ("Old buildings have no value whatsoever.", False)],
            "explanation": r"The writer moves from defending the building to insisting it must not 'fail the present' -- readers come first. The trap 'preserved exactly as it is' is the position the writer abandons. Pro tip: in a passage with a turn, the final claim, not the opening stance, is the argument.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "Over the course of the passage, the writer's attitude shifts from:"),
            "difficulty": 3,
            "choices": [("fond sentiment to firmer resolve", True),
                        ("anger to total indifference", False),
                        ("joy to hopeless despair", False),
                        ("neutrality to confusion", False)],
            "explanation": r"It begins in 'pure sentiment' and hardens into resolve once a child is failed by the building. The trap 'anger to indifference' misreads both ends. Pro tip: track the emotional words at the start ('sentiment') and end ('something harder') to name a tone shift.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Then I watched a child turn away from a ruined, water-stained book...\"\n\n"
                     "This moment functions in the passage as:"),
            "difficulty": 3,
            "choices": [("the turning point that changes the writer's view", True),
                        ("a minor, unrelated background detail", False),
                        ("evidence that the building is in fine shape", False),
                        ("a fond and happy memory", False)],
            "explanation": r"The word 'Then' marks the pivot: seeing the child fail with a ruined book hardens the writer's sentiment. The trap 'building is in fine shape' is the opposite of what the moment shows. Pro tip: a sentence beginning 'Then' often marks the passage's turning point.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"We do not honor the past by letting it fail the present.\"\n\n"
                     "This sentence most nearly implies that:"),
            "difficulty": 3,
            "choices": [("truly respecting the past means not sacrificing the present to it", True),
                        ("the past should be entirely forgotten", False),
                        ("the present does not matter at all", False),
                        ("old buildings can never be saved", False)],
            "explanation": r"Honoring the past 'by letting it fail the present' is rejected, so real honor serves the present too. The trap 'entirely forgotten' overshoots. Pro tip: a 'we do not X by doing Y' line tells you the author's real definition of doing X well.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Affection for a building is a fine thing -- until it costs a reader a page.\"\n\n"
                     "This sentence works by:"),
            "difficulty": 3,
            "choices": [("granting the value of sentiment, then marking where it must yield", True),
                        ("rejecting all affection for buildings outright", False),
                        ("praising water-stained, ruined books", False),
                        ("ignoring the needs of readers", False)],
            "explanation": r"It concedes that affection is 'a fine thing,' then sets its limit with 'until.' The trap 'rejecting all affection outright' ignores the concession. Pro tip: a concession-plus-limit ('fine... until') grants a point only so far, then draws a line.",
        },
        # ----- Passage 6: The old clock (literary, multiple devices) -----
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"The old clock on the landing kept a stubborn, private time, always eleven minutes "
                     "slow, as if it refused to hurry for anyone. The family scolded it for years, then "
                     "set their watches by its lie, and at last grew fond of the small rebellion ticking "
                     "in the hall. When it finally stopped, the silence felt less like peace than like "
                     "the loss of an old friend who had always, gently, disagreed.\"\n\n"
                     "The clock is described as if it:"),
            "difficulty": 3,
            "choices": [("had a stubborn will of its own, quietly resisting the family", True),
                        ("were a sleek modern digital device", False),
                        ("kept perfectly accurate time", False),
                        ("badly frightened the whole family", False)],
            "explanation": r"'Stubborn,' 'refused to hurry,' and 'rebellion' give the clock a willful personality. The trap 'kept perfectly accurate time' contradicts 'always eleven minutes slow.' Pro tip: personification gives an object human traits -- here, stubborn defiance.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...then set their watches by its lie...\"\n\n"
                     "This detail suggests that the family:"),
            "difficulty": 3,
            "choices": [("came to accept and even rely on the clock's imperfection", True),
                        ("replaced the clock right away", False),
                        ("discovered the clock was perfectly accurate", False),
                        ("never actually used the clock at all", False)],
            "explanation": r"Setting their watches by 'its lie' means they adapted to and depended on its flaw. The trap 'replaced it right away' contradicts their growing fondness. Pro tip: an apparent contradiction ('set their watches by its lie') often shows acceptance of a known flaw.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"...the loss of an old friend who had always, gently, disagreed.\"\n\n"
                     "This closing simile implies that the family:"),
            "difficulty": 3,
            "choices": [("grieved the clock like a dear friend whose quirks they had come to love", True),
                        ("felt relieved that the clock had finally stopped", False),
                        ("had always secretly hated the clock", False),
                        ("felt nothing at all when it stopped", False)],
            "explanation": r"Comparing the loss to a gently disagreeing friend shows affectionate grief. The trap 'felt relieved' clashes with 'less like peace than like the loss.' Pro tip: a closing simile often carries the emotional payoff -- here, mourning a loved, contrary companion.",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "The deeper theme of the passage is best described as:"),
            "difficulty": 3,
            "choices": [("we often come to cherish the very imperfections of familiar things", True),
                        ("clocks should always keep accurate time", False),
                        ("rebellion of any kind must be punished", False),
                        ("silence is always a form of peace", False)],
            "explanation": r"The family grows fond of the clock's flaw and mourns it -- the theme is loving imperfection in the familiar. The trap 'silence is always peace' is denied by 'less like peace than like the loss.' Pro tip: a theme is the broad human truth the specific story illustrates.",
        },
        # =====================================================================
        # ============ PART 2  --  LANGUAGE & EDITING =========================
        # =====================================================================
        {
            "text": ("**Language section.** Choose the option that corrects the faulty comparison.\n\n"
                     "\"Her novel is more original than ______ writer in her class.\""),
            "difficulty": 3,
            "choices": [("any other", True), ("any", False), ("other", False), ("all", False)],
            "explanation": r"Since her novel is itself in the class, she must be compared with 'any other' writer, not 'any' (which would include herself). The trap 'any' creates an illogical comparison. Pro tip: add 'other' when comparing a member of a group with the rest of that group.",
        },
        {
            "text": ("Choose the option that keeps the list parallel.\n\n"
                     "\"The director was respected for her vision, her discipline, and ______.\""),
            "difficulty": 3,
            "choices": [("her honesty", True), ("being honest", False),
                        ("she was honest", False), ("to be honest", False)],
            "explanation": r"To match 'her vision' and 'her discipline,' the third item must be the noun phrase 'her honesty.' The trap 'being honest' breaks the noun pattern. Pro tip: a list of noun phrases must end with another noun phrase.",
        },
        {
            "text": ("Choose the correct verb form.\n\n"
                     "\"The supervisor insisted that the report ______ by Friday.\""),
            "difficulty": 3,
            "choices": [("be submitted", True), ("is submitted", False),
                        ("was submitted", False), ("submits", False)],
            "explanation": r"After 'insisted that,' the subjunctive uses the base form: 'that the report be submitted.' The trap 'is submitted' adds an unnecessary present-tense verb. Pro tip: 'insist/demand/require that' triggers the base-form subjunctive.",
        },
        {
            "text": ("Choose the correct verb for this inverted sentence.\n\n"
                     "\"Among the old documents ______ a signed contract.\""),
            "difficulty": 3,
            "choices": [("was", True), ("were", False), ("have been", False), ("are", False)],
            "explanation": r"The real subject is 'a signed contract' (singular), which follows the verb, so use 'was.' The trap 'were' agrees with 'documents,' which is not the subject. Pro tip: in an inverted sentence, find the true subject after the verb and match it.",
        },
        {
            "text": "Which sentence corrects the dangling modifier?",
            "difficulty": 3,
            "choices": [("Hoping to save money, she clipped the coupons.", True),
                        ("Hoping to save money, the coupons were clipped.", False),
                        ("Hoping to save money, the clipping of coupons was done.", False),
                        ("The coupons, hoping to save money, were clipped.", False)],
            "explanation": r"'Hoping to save money' must describe a person -- 'she.' The traps make 'the coupons' do the hoping. Pro tip: an opening participial phrase must attach to the noun right after the comma, and only a person can hope.",
        },
        {
            "text": "Which sentence makes the pronoun reference unmistakably clear?",
            "difficulty": 3,
            "choices": [("The manager said to the clerk, \"I made an error.\"", True),
                        ("The manager told the clerk that he had made an error.", False),
                        ("The manager told the clerk he made his error.", False),
                        ("Telling the clerk, he said he made an error.", False)],
            "explanation": r"With two men in the sentence, 'he' is ambiguous; the direct quotation makes the speaker's meaning exact. The traps leave 'he' pointing to either man. Pro tip: when 'he' or 'she' could refer to two people, rewrite -- a direct quote removes all doubt.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"The scientist ______ the committee honored gave a moving speech.\""),
            "difficulty": 3,
            "choices": [("whom", True), ("who", False), ("whose", False), ("which", False)],
            "explanation": r"In its clause the pronoun is the object of 'honored' ('the committee honored whom'), so 'whom' is correct. The trap 'who' is for subjects. Pro tip: rearrange the clause -- if the answer would be 'him' (honored him), use 'whom.'",
        },
        {
            "text": ("Choose the correct word (idiom).\n\n"
                     "\"This new policy is quite different ______ the previous one.\""),
            "difficulty": 3,
            "choices": [("from", True), ("than", False), ("to", False), ("of", False)],
            "explanation": r"Standard usage is 'different from.' The trap 'different than' is common in speech but not preferred in formal writing. Pro tip: in formal writing, things differ 'from' one another.",
        },
        {
            "text": ("Choose the correct verb form (conditional perfect).\n\n"
                     "\"If she had known about the change, she ______ earlier.\""),
            "difficulty": 3,
            "choices": [("would have left", True), ("would leave", False),
                        ("will leave", False), ("had left", False)],
            "explanation": r"A past hypothetical pairs 'had known' with 'would have left.' The trap 'would leave' is for present/future hypotheticals. Pro tip: 'If... had + past participle' takes 'would have + past participle' in the result.",
        },
        {
            "text": "Which sentence states the idea most precisely and concisely?",
            "difficulty": 3,
            "choices": [("The committee decided to postpone the event.", True),
                        ("The committee made the decision to postpone the event.", False),
                        ("The committee came to a decision that the event should be postponed.", False),
                        ("A decision was made by the committee to postpone the event.", False)],
            "explanation": r"'Decided to postpone' replaces the wordy 'made the decision to postpone' with one strong verb. The traps bury the verb in a noun phrase ('made a decision'). Pro tip: turn 'make a decision' into 'decide' -- prefer a strong verb over a noun phrase.",
        },
        {
            "text": "Which sentence places its phrase so that the children, not the sandwiches, are clearly the focus of serving?",
            "difficulty": 3,
            "choices": [("She served the children sandwiches on paper plates.", True),
                        ("She served sandwiches to the children on paper plates.", False),
                        ("On paper plates, she served sandwiches to the children.", False),
                        ("She served sandwiches on paper plates to the children.", False)],
            "explanation": r"Placing 'on paper plates' right after 'sandwiches' (in the first option's structure 'children sandwiches on paper plates') keeps the modifier next to what's on the plates. The trap '...to the children on paper plates' makes it sound like the children are on the plates. Pro tip: keep a modifying phrase beside the noun it actually describes.",
        },
        {
            "text": "Which sentence uses a colon correctly?",
            "difficulty": 3,
            "choices": [("He had only one goal: to win the championship.", True),
                        ("He had only one: goal to win the championship.", False),
                        ("He had: only one goal to win the championship.", False),
                        ("He had only one goal to win: the championship.", False)],
            "explanation": r"A colon follows a complete thought to introduce what completes it: 'one goal: to win.' The traps drop the colon mid-clause. Pro tip: a colon needs a full sentence before it and an explanation or list after it.",
        },
        {
            "text": ("Choose the correct word.\n\n"
                     "\"The final choice is between accepting the offer ______ walking away.\""),
            "difficulty": 3,
            "choices": [("and", True), ("or", False), ("to", False), ("with", False)],
            "explanation": r"The idiom is 'between X and Y,' so 'between accepting... and walking.' The trap 'or' breaks the 'between... and' pairing. Pro tip: 'between' is always followed by 'and,' never 'or' or 'to.'",
        },
        {
            "text": ("Choose the option that keeps the correlative pair parallel.\n\n"
                     "\"She not only wrote the report but also ______ it to the board.\""),
            "difficulty": 3,
            "choices": [("presented", True), ("presenting", False),
                        ("the presentation of", False), ("to present", False)],
            "explanation": r"'Not only wrote... but also presented' keeps both verbs in matching past-tense form. The trap 'presenting' breaks the parallel. Pro tip: 'not only... but also' must join the same grammatical form on each side.",
        },
        {
            "text": ("Choose the correct verb.\n\n"
                     "\"The quality of the products ______ improved dramatically this year.\""),
            "difficulty": 3,
            "choices": [("has", True), ("have", False), ("were", False), ("are", False)],
            "explanation": r"The subject is 'quality' (singular), so 'has' -- 'of the products' is just a modifier. The trap 'have' agrees with 'products.' Pro tip: strip the prepositional phrase ('of the products') and match the verb to the real subject.",
        },
        {
            "text": "Which version places the time phrase to clearly mean the announcement happened on Friday?",
            "difficulty": 3,
            "choices": [("On Friday, the instructor said she would return the essays.", True),
                        ("The instructor said on Friday she would return the essays.", False),
                        ("The instructor said she would return the essays on Friday she said.", False),
                        ("The instructor said she on Friday would return the essays.", False)],
            "explanation": r"Moving 'On Friday' to the front makes clear it modifies 'said,' not 'return.' The trap '...said on Friday she would return...' is squinting -- Friday could attach to either verb. Pro tip: front a time phrase to fix a squinting modifier and pin down which verb it describes.",
        },
        {
            "text": "Which sentence is logically complete and correct?",
            "difficulty": 3,
            "choices": [("It is one of the best films I have seen, if not the best.", True),
                        ("It is one of the best, if not the best, film I have seen.", False),
                        ("It is one of the best film, if not the best ones.", False),
                        ("It is one of the best, if not the best film I seen.", False)],
            "explanation": r"'One of the best films' needs the plural 'films,' and 'if not the best' tucks in cleanly after it. The trap 'one of the best... film' mismatches plural 'best' with singular 'film.' Pro tip: 'one of the best' requires a plural noun -- 'films,' not 'film.'",
        },
        {
            "text": "Which sentence is the clearest and most active?",
            "difficulty": 3,
            "choices": [("The team completed the project ahead of schedule.", True),
                        ("The project was completed by the team ahead of schedule.", False),
                        ("It was the case that the project had been completed by the team early.", False),
                        ("Ahead of schedule, completion of the project was achieved by the team.", False)],
            "explanation": r"The active 'The team completed the project' is direct and concise. The traps use the passive voice or empty filler ('It was the case that'). Pro tip: prefer the active voice -- name the doer ('the team') and let it perform the verb.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the elite (Level 5) full-length GED RLA practice exam (46 questions; MCQ only)."

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
            f"(Part 1: 28 reading incl. a paired-passage set, Part 2: 18 language; elite level)."
        ))
