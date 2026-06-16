"""
Seed data: 'GED Language Arts (RLA): Reading & Writing' -- the GED Reasoning
Through Language Arts subject, built comprehensively.

Covers the three things the RLA test measures: reading for meaning, editing for
grammar and conventions, and writing the Extended Response essay. Lessons lead
with intuition, give clear examples, and include argument/essay diagrams.
Practice includes passage-based reading questions, grammar/editing items, and
full Extended Response prompts (graded by the AI essay grader).

Run:
    python manage.py seed_ged_rla
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Language Arts (RLA): Reading & Writing",
    "slug": "ged-language-arts",
    "program": "GED",
    "subject": "rla",
    "description": (
        "Reasoning Through Language Arts (RLA) is the GED's English test. It measures three "
        "skills: reading closely for meaning, editing writing for correct grammar, and writing "
        "a clear, evidence-based essay. This course builds all three from the ground up, with "
        "short practice passages, common-error grammar drills, and a full guide to the "
        "Extended Response essay."
    ),
    "lessons": [
        (
            "1. How to Read for Meaning",
            "Most of the RLA test is reading. The good news: you don't need to know the topic in "
            "advance — every answer is supported somewhere in the passage. Your job is to read "
            "**actively** and find it.\n\n"
            "Active reading means doing something as you read, not just letting your eyes pass over "
            "words. As you read a passage, keep asking:\n\n"
            "- **What is this mostly about?** (the topic)\n"
            "- **What is the author saying about that topic?** (the main idea)\n"
            "- **What details back it up?** (supporting evidence)\n\n"
            "Think of a passage like a table: the **main idea** is the tabletop, and the "
            "**supporting details** are the legs that hold it up. The details are specific — names, "
            "numbers, examples, reasons. The main idea is the bigger point they all add up to.\n\n"
            "**Answer from the text, not from yourself.** The most common wrong answers are "
            "statements that are *true in real life* but are never actually said in the passage. On "
            "the GED, 'supported by the passage' always beats 'sounds right'.\n\n"
            "⚠️ Common mistake: picking an answer because you personally agree with it. Always ask, "
            "'Where does the passage actually say this?'\n\n"
            "💡 Tip: when a question asks about a specific line, go back and re-read the sentence "
            "before it and after it. Context usually hands you the answer.",
        ),
        (
            "2. Finding the Main Idea & Summarizing",
            "The **main idea** is the single most important point a passage makes. Everything else "
            "in the passage exists to explain or support it.\n\n"
            "How to find it:\n\n"
            "- Check the **first and last sentences** of a paragraph — main ideas often live there.\n"
            "- Ask, 'If I had to tell a friend this passage in one sentence, what would I say?'\n"
            "- Make sure your choice covers the **whole** passage, not just one detail.\n\n"
            "A good test: an answer that is **too narrow** (only one detail) or **too broad** "
            "(bigger than the passage) is usually wrong. The main idea is 'just right' — it matches "
            "the scope of the passage exactly.\n\n"
            "A **summary** is a short retelling of the main idea plus the most important supporting "
            "points, in your own words. A good summary leaves out minor examples and keeps the "
            "backbone of the passage.\n\n"
            "⚠️ Common mistake: confusing the **topic** (a word or phrase, like 'honeybees') with "
            "the **main idea** (a full sentence, like 'honeybees matter because they pollinate our "
            "food crops').\n\n"
            "💡 Tip: a main idea is always a complete sentence. If your answer is just a noun, you "
            "have found the topic, not the main idea.",
        ),
        (
            "3. Making Inferences",
            "An **inference** is a logical conclusion you draw from clues in the text plus common "
            "sense — it is 'reading between the lines'. The author doesn't say it directly, but the "
            "evidence points to it.\n\n"
            "Inference works like a detective:\n\n"
            "- **Clue** (from the text): 'Maria checked the clock for the third time and tapped her "
            "pen against the desk.'\n"
            "- **Common sense:** people check clocks repeatedly and fidget when they are anxious or "
            "waiting.\n"
            "- **Inference:** Maria is feeling anxious and waiting for something.\n\n"
            "A solid inference is always **anchored to evidence**. If you cannot point to the words "
            "that led you there, it is a guess, not an inference.\n\n"
            "⚠️ Common mistake: inferring too much. 'Maria is going to fail her exam' goes far beyond "
            "the clues. Stay close to what the text actually supports.\n\n"
            "💡 Tip: for an inference question, find the specific sentence(s) that make your answer "
            "the most likely one. The best answer needs the *least* outside assumption.",
        ),
        (
            "4. Author's Purpose, Tone & Point of View",
            "Every text is written for a reason. **Author's purpose** is usually one of three:\n\n"
            "- **To inform** — explain facts (a news report, an instruction manual).\n"
            "- **To persuade** — convince you of an opinion (an editorial, an ad).\n"
            "- **To entertain** — tell a story or amuse (a novel, a funny essay).\n\n"
            "**Tone** is the author's attitude, shown through word choice. Words like 'waste', "
            "'regret', and 'the last thing we need' signal a **critical, disapproving** tone. Words "
            "like 'wonderful' and 'exciting' signal an **enthusiastic** one. Tone is *how* something "
            "is said, not *what* is said.\n\n"
            "**Point of view** is the perspective: first person ('I', 'we') shares a personal view; "
            "third person ('he', 'she', 'they') describes from outside.\n\n"
            "⚠️ Common mistake: treating a persuasive passage as if it were neutral information. If "
            "the author is taking a side, the purpose is to persuade — and the 'facts' may be chosen "
            "to support that side.\n\n"
            "💡 Tip: loaded, emotional words are your biggest clue to both tone and purpose. Underline "
            "them as you read.",
        ),
        (
            "5. Analyzing Arguments: Claims & Evidence",
            "An **argument** tries to convince you of a **claim** (a position) using **evidence** "
            "(facts, examples, data) and **reasoning** (the logic that connects them).\n\n"
            "[[figure:argument|A strong argument connects every claim to evidence, and explains how "
            "that evidence supports the claim.]]\n\n"
            "To judge how strong an argument is, ask:\n\n"
            "- Is the **evidence relevant** and specific, or vague?\n"
            "- Is there **enough** evidence, or just one example?\n"
            "- Does the **reasoning** actually connect the evidence to the claim?\n"
            "- Does the author rely on **facts** (checkable) or just **opinions** and feelings?\n\n"
            "A **well-supported** argument uses relevant facts and sound logic. A **weak** argument "
            "leans on opinion, emotion, or evidence that doesn't really prove the point. Spotting "
            "the difference is exactly what the Extended Response essay will ask you to do.\n\n"
            "⚠️ Common mistake: assuming the argument with stronger *feelings* is the stronger "
            "argument. Strong language is not the same as strong evidence.\n\n"
            "💡 Tip: separate **fact** ('sales rose 12% last year') from **opinion** ('this is the "
            "best plan'). Facts can be checked; opinions cannot.",
        ),
        (
            "6. Grammar & Conventions",
            "About a quarter of the RLA test asks you to **edit** writing — choosing the version of a "
            "sentence that follows the rules of standard English. A few errors show up again and "
            "again.\n\n"
            "**Subject-verb agreement** — the verb must match the subject in number:\n\n"
            "- Correct: 'The **list** of items **is** on the table.' (the subject is 'list', not "
            "'items')\n"
            "- Wrong: 'The list of items are on the table.'\n\n"
            "**Run-ons and fragments** — a complete sentence needs a subject and a verb and a full "
            "thought:\n\n"
            "- Fragment (incomplete): 'Because she was late.'\n"
            "- Run-on (two sentences jammed together): 'She was late she missed the bus.'\n"
            "- Correct: 'She was late because she missed the bus.'\n\n"
            "**Common confusions** — know these pairs:\n\n"
            "- **its** (belonging to it) vs **it's** (it is): 'The dog wagged **its** tail.'\n"
            "- **their / there / they're** and **your / you're**.\n\n"
            "⚠️ Common mistake: matching the verb to the closest noun instead of the real subject. In "
            "'the box of nails *is* heavy', the subject is 'box', so the verb is 'is'.\n\n"
            "💡 Tip: read the sentence out loud in your head. Many errors *sound* wrong once you hear "
            "them.",
        ),
        (
            "7. The Extended Response: Writing the GED Essay",
            "The **Extended Response** gives you two passages that argue opposite sides of an issue "
            "and asks you to write an essay explaining **which argument is better supported** — not "
            "which one you personally agree with. You have about 45 minutes.\n\n"
            "The graders score three things: (1) how well you **analyze the arguments and use "
            "evidence**, (2) how well your essay is **organized and developed**, and (3) your "
            "**command of standard English**.\n\n"
            "Use a clear five-paragraph structure:\n\n"
            "[[figure:essay_structure|A reliable shape for the essay: introduce your thesis, support "
            "it across three body paragraphs, then conclude.]]\n\n"
            "A winning approach:\n\n"
            "- **Read both passages** and decide which is better supported by evidence.\n"
            "- **State a clear thesis** in your introduction naming which side is stronger and why.\n"
            "- In each **body paragraph**, make one point and back it with a **specific quote or "
            "detail** from the passage.\n"
            "- **Explain** how that evidence proves your point (don't just drop a quote).\n"
            "- **Conclude** by restating your thesis in fresh words.\n\n"
            "⚠️ Common mistake: writing about your own opinion on the topic. Your job is to judge the "
            "*arguments*, using evidence from the passages.\n\n"
            "💡 Tip: leave two minutes at the end to proofread for the grammar errors from Lesson 6 "
            "— it directly raises your conventions score.",
        ),
    ],
    "mcqs": [
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Honeybees do far more than make honey. As they move from flower to flower "
                     "collecting nectar, they carry pollen with them, fertilizing plants so the plants "
                     "can produce fruit and seeds. In fact, about one-third of the food we eat depends "
                     "on pollinators like bees.\"\n\n"
                     "What is the main idea of the passage?"),
            "difficulty": 2,
            "choices": [("Honeybees are important because they pollinate many of the plants we rely on for food", True),
                        ("Honeybees make honey", False),
                        ("Bees move from flower to flower", False),
                        ("People should be afraid of bees", False)],
            "explanation": ("The whole passage supports one big point: bees matter because they "
                            "pollinate food crops. 'Honeybees make honey' and 'bees move from flower to "
                            "flower' are only details, and fear of bees is never mentioned."),
        },
        {
            "text": ("According to the same passage, about how much of the food we eat depends on "
                     "pollinators?"),
            "difficulty": 1,
            "choices": [("About one-third", True), ("All of it", False),
                        ("About one-half", False), ("None of it", False)],
            "explanation": "The passage states directly that 'about one-third of the food we eat depends on pollinators like bees.'",
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Maria checked the clock for the third time and tapped her pen against the desk. "
                     "She had read the same paragraph twice without remembering a word of it. When her "
                     "phone finally buzzed, she grabbed it before the first ring finished.\"\n\n"
                     "What can you infer about Maria?"),
            "difficulty": 2,
            "choices": [("She is anxious and waiting for something", True),
                        ("She is bored and about to fall asleep", False),
                        ("She dislikes reading in general", False),
                        ("She is angry at her friend", False)],
            "explanation": ("Checking the clock repeatedly, fidgeting, not absorbing what she reads, and "
                            "grabbing the phone instantly all point to anxiety and waiting. The text gives "
                            "no clues about sleepiness, disliking reading, or anger."),
        },
        {
            "text": ("Read the passage, then answer.\n\n"
                     "\"Let's be honest: another shopping mall is the last thing this town needs. We "
                     "already have three within ten miles, half of them half-empty. Paving over the "
                     "Miller farm for more parking lots would be a waste of good land.\"\n\n"
                     "What is the author's main purpose?"),
            "difficulty": 2,
            "choices": [("To persuade readers to oppose building a new mall", True),
                        ("To inform readers about local farms", False),
                        ("To entertain readers with a funny story", False),
                        ("To describe how malls are built", False)],
            "explanation": ("The author takes a clear side ('the last thing this town needs', 'a waste of "
                            "good land'), which signals a persuasive purpose — to convince readers to "
                            "oppose the mall."),
        },
        {
            "text": ("In the mall passage above, the word 'waste' helps create which tone?"),
            "difficulty": 2,
            "choices": [("Critical / disapproving", True), ("Cheerful / enthusiastic", False),
                        ("Neutral / objective", False), ("Sad / mournful", False)],
            "explanation": ("'Waste', along with 'the last thing this town needs', expresses disapproval. "
                            "The author's attitude (tone) toward the mall is clearly critical."),
        },
        {
            "text": ("Read the sentence, then answer.\n\n"
                     "\"The new manager was known for her candid feedback; she told employees exactly "
                     "what she thought, even when the truth was uncomfortable.\"\n\n"
                     "As used here, 'candid' most nearly means:"),
            "difficulty": 2,
            "choices": [("Honest and direct", True), ("Gentle and vague", False),
                        ("Cheerful", False), ("Secretive", False)],
            "explanation": ("The clue 'told employees exactly what she thought, even when the truth was "
                            "uncomfortable' shows 'candid' means honest and direct."),
        },
        {
            "text": "Which sentence uses correct subject-verb agreement?",
            "difficulty": 2,
            "choices": [("The list of items is on the table.", True),
                        ("The list of items are on the table.", False),
                        ("The list of items were on the table.", False),
                        ("The list of items have been on the table.", False)],
            "explanation": ("The subject is 'list' (singular), not 'items'. A singular subject takes the "
                            "singular verb 'is'. The phrase 'of items' does not change the subject."),
        },
        {
            "text": "Which of the following is a complete, correctly written sentence?",
            "difficulty": 2,
            "choices": [("She was late because she missed the bus.", True),
                        ("Because she was late.", False),
                        ("She was late she missed the bus.", False),
                        ("Late for the bus this morning.", False)],
            "explanation": ("'She was late because she missed the bus' has a subject, a verb, and a "
                            "complete thought. 'Because she was late' is a fragment; 'She was late she "
                            "missed the bus' is a run-on; the last option has no subject."),
        },
        {
            "text": "Choose the sentence that is punctuated correctly.",
            "difficulty": 2,
            "choices": [("The dog wagged its tail happily.", True),
                        ("The dog wagged it's tail happily.", False),
                        ("The dog wagged its' tail happily.", False),
                        ("The dog wagged its tail happily'.", False)],
            "explanation": ("'Its' shows possession (the tail belonging to it). 'It's' means 'it is', "
                            "which makes no sense here. So 'its tail' is correct."),
        },
        {
            "text": "Which sentence uses the correct word?",
            "difficulty": 1,
            "choices": [("They're going to leave their car over there.", True),
                        ("There going to leave they're car over their.", False),
                        ("Their going to leave there car over they're.", False),
                        ("They're going to leave there car over their.", False)],
            "explanation": ("'They're' = they are; 'their' = belonging to them; 'there' = a place. The "
                            "correct sentence is 'They're going to leave their car over there.'"),
        },
        {
            "text": ("A student writes: 'Me and him went to the store.' What is the best correction?"),
            "difficulty": 2,
            "choices": [("He and I went to the store.", True),
                        ("Him and me went to the store.", False),
                        ("Me and he went to the store.", False),
                        ("I and him went to the store.", False)],
            "explanation": ("As the subject of the sentence, use the subject pronouns 'He and I'. A quick "
                            "test: you would say 'I went to the store', not 'me went to the store'."),
        },
        {
            "text": ("In an argument, which of these counts as the strongest EVIDENCE for the claim "
                     "'our town should add bike lanes'?"),
            "difficulty": 3,
            "choices": [("A study showing towns with bike lanes saw a 30% drop in traffic accidents", True),
                        ("The writer feels bikes are nicer than cars", False),
                        ("Everyone knows bike lanes are a good idea", False),
                        ("Bike lanes are popular in other countries, probably", False)],
            "explanation": ("Strong evidence is specific and checkable. A study with a concrete statistic "
                            "directly supports the claim. Feelings, vague 'everyone knows', and a hedged "
                            "'probably' are opinions, not solid evidence."),
        },
    ],
    "essays": [
        {
            "text": ("Extended Response. Read the two short arguments, then write an essay explaining "
                     "which argument is better supported. Use specific evidence from the passages. (Your "
                     "own opinion on the topic is not what is being graded.)\n\n"
                     "ARGUMENT A: \"Our school should switch to year-round classes. A recent district "
                     "study found that students lose up to two months of math skills over the long "
                     "summer break, and that schools on year-round calendars scored 8% higher on state "
                     "tests. Shorter, more frequent breaks help students remember what they learn.\"\n\n"
                     "ARGUMENT B: \"Year-round school is a bad idea. Summer is a special time, and kids "
                     "deserve a long break. Everyone I know loved summer vacation as a child, and it "
                     "would be sad to take that away. School is already stressful enough.\"\n\n"
                     "Which argument is better supported, and why?"),
            "difficulty": 3,
            "rubric": ("Score for three traits. (1) Analysis & evidence: a top response argues that "
                       "Argument A is better supported because it uses specific, checkable evidence (the "
                       "district study, the two-month skill loss, the 8% higher scores), while Argument B "
                       "relies on feelings and personal anecdote ('everyone I know', 'it would be sad'). "
                       "(2) Organization: clear thesis, body paragraphs each with evidence, and a "
                       "conclusion. (3) Conventions: correct grammar, spelling, and sentence structure. "
                       "Reward citing specific details from the passages; deduct for arguing personal "
                       "opinion about year-round school instead of analyzing the arguments."),
        },
        {
            "text": ("Extended Response practice. Some people believe that smartphones should be banned "
                     "in classrooms because they distract students. Others believe smartphones are "
                     "useful learning tools when used responsibly. Write a well-organized essay that "
                     "states a clear position and supports it with specific reasons and examples. Use a "
                     "clear introduction, body paragraphs, and a conclusion."),
            "difficulty": 3,
            "rubric": ("Score for three traits. (1) Development & support: a clear thesis taking one "
                       "side, supported by specific, relevant reasons and examples (not just opinions). "
                       "(2) Organization: an introduction with a thesis, focused body paragraphs each "
                       "making one point, and a conclusion that restates the position. (3) Conventions: "
                       "correct grammar, punctuation, and varied sentence structure. Deduct for a missing "
                       "thesis, disorganized paragraphs, or frequent grammar errors."),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'GED Language Arts (RLA)' course."

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
