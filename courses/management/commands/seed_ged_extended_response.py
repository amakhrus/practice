"""
Seed data: 'GED RLA: Extended Response & Essay Writing' -- a focused deep dive
into the Extended Response task on the GED Reasoning Through Language Arts test.

Seven lessons take students from understanding what the GED actually asks them
to do, through reading and annotating the source texts, building a strong thesis,
planning and outlining, writing evidence-rich body paragraphs, crafting the
introduction and conclusion, and finally revising using the official rubric.

Practice (28 MCQs, 4 per lesson) tests essay structure, thesis quality, evidence
use, argument analysis, and transitions -- not grammar conventions (covered in the
main GED RLA course).

Run:
    python manage.py seed_ged_extended_response
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Extended Response & Essay Writing",
    "slug": "ged-extended-response",
    "program": "GED",
    "subject": "rla",
    "description": (
        "The Extended Response is the one written essay on the GED RLA test. You have 45 minutes "
        "to read two passages that argue opposite sides of an issue and write an essay explaining "
        "which argument is better supported -- not which side you personally agree with. This "
        "course walks you through every step: understanding the task and scoring rubric, reading "
        "and annotating the source texts, writing a strong thesis, outlining your essay, building "
        "body paragraphs with real evidence, crafting the introduction and conclusion, and using "
        "the GED rubric to self-score and revise. Concrete examples, weak-vs-strong comparisons, "
        "the PEEL method, and GED-style practice throughout."
    ),
    "lessons": [
        (
            "1. Understanding the Extended Response Task",
            "The **Extended Response (ER)** is the only written essay on the GED RLA test. Before "
            "you write a single word, you need to know exactly what the test is asking -- because "
            "many students misread the task and lose points before they even start.\n\n"
            "**What the GED actually asks you to do**\n\n"
            "You will be given two short passages that argue *opposite sides* of the same issue. "
            "Your job is NOT to share your personal opinion about the topic. Your job is to "
            "**analyze the arguments** -- to read both passages carefully and explain which one is "
            "**better supported by evidence and reasoning**.\n\n"
            "Think of yourself as a judge, not a debater. A judge does not pick a side based on "
            "what they personally believe; a judge decides which side presented the stronger case.\n\n"
            "**The 45-minute clock**\n\n"
            "You have about 45 minutes for the entire Extended Response. A smart time split:\n\n"
            "- **5 minutes** -- read and annotate both passages\n"
            "- **5 minutes** -- plan and outline your essay\n"
            "- **30 minutes** -- write the essay\n"
            "- **5 minutes** -- revise and proofread\n\n"
            "That may feel tight, but students who skip the planning step almost always write "
            "weaker, less organized essays.\n\n"
            "**The 3 Scoring Traits**\n\n"
            "GED graders score your essay on three traits:\n\n"
            "- **Trait 1 -- Analysis of Arguments and Evidence:** Did you identify each text's "
            "main claim, judge the quality of the evidence, and explain *why* one argument is "
            "better supported?\n"
            "- **Trait 2 -- Development of Ideas and Organizational Structure:** Is your essay "
            "organized with a clear introduction, focused body paragraphs, and a conclusion? "
            "Does each paragraph develop one idea with specific support?\n"
            "- **Trait 3 -- Clarity and Command of Standard English Conventions:** Are your "
            "sentences clear? Do you use appropriate transitions and mostly correct grammar?\n\n"
            "Trait 1 is worth the most points. A beautiful essay that never actually analyzes "
            "the arguments will score low. Evidence from the passages is essential.\n\n"
            "⚠️ Common mistake: writing about what YOU think is true about the topic. Example: "
            "if the passages debate year-round school, do NOT write about your own school "
            "experience. Write about what EVIDENCE the passages use and which evidence is "
            "stronger.\n\n"
            "💡 Tip: highlight or underline the word 'better-supported' in the prompt. That word "
            "is your entire task. Keep asking yourself: 'Am I explaining why one argument's "
            "evidence is stronger?'"
        ),
        (
            "2. Reading and Analyzing the Source Texts",
            "The two passages you receive on test day are **argument passages** -- each one is "
            "making a case for a position. Your first job is to understand what each argument is "
            "actually claiming and what evidence it uses to back that claim up.\n\n"
            "[[figure:argument|Every argument has three parts: a Claim (what the author believes), "
            "Evidence (facts, data, or examples used as proof), and Reasoning (the explanation of "
            "how the evidence supports the claim).]]\n\n"
            "**Step 1 -- Identify each text's main claim**\n\n"
            "The **claim** is the author's central position: the one thing they most want you to "
            "believe. It is usually stated directly near the beginning or end of the passage. "
            "Ask yourself: 'What is this author trying to convince me of?'\n\n"
            "**Step 2 -- Find the key evidence**\n\n"
            "**Evidence** is what the author offers as proof. There are two kinds:\n\n"
            "- **Strong evidence:** specific facts, statistics, studies, expert testimony, "
            "historical events, concrete examples. Example: 'A Harvard study found that students "
            "in year-round schools scored 12 percent higher on standardized tests.'\n"
            "- **Weak evidence:** vague feelings, personal anecdotes, appeals to emotion, "
            "unsourced generalities. Example: 'Everyone knows year-round school is stressful.'\n\n"
            "**Step 3 -- Annotate the argument structure**\n\n"
            "As you read, jot brief notes beside each passage:\n\n"
            "- Circle or bracket the main claim.\n"
            "- Write 'E' next to each piece of evidence.\n"
            "- Put a '?' next to anything that sounds like opinion rather than fact.\n"
            "- Put a '+' next to evidence that seems specific and verifiable.\n\n"
            "After reading both passages, ask: 'Which passage had more specific, checkable "
            "evidence? Which one relied mostly on feelings or vague claims?'\n\n"
            "**The reasoning link**\n\n"
            "Good arguments don't just list evidence -- they explain *how* the evidence proves "
            "the claim. If an author says 'Statistics show X, therefore Y is true' but X doesn't "
            "really connect to Y, that's a reasoning flaw. Spotting reasoning gaps earns you "
            "Trait 1 points.\n\n"
            "⚠️ Common mistake: assuming the longer passage is automatically stronger. A short "
            "passage with two specific statistics can be stronger than a long passage full of "
            "emotional language and no data.\n\n"
            "💡 Tip: after reading, write a one-sentence summary of each passage in the margin: "
            "'Passage A argues X, using evidence Y.' This forces you to understand both arguments "
            "before you write a single word of your essay."
        ),
        (
            "3. Building a Strong Thesis",
            "Your **thesis statement** is the single most important sentence in your entire essay. "
            "It tells the reader your position, which argument you are siding with, and why -- all "
            "in one clear sentence. Everything else in your essay exists to prove your thesis.\n\n"
            "**What the GED ER thesis must do**\n\n"
            "Your thesis must:\n\n"
            "- Take a **clear position** on WHICH argument is better supported (not 'both sides "
            "have good points').\n"
            "- Name the **reason** -- what specifically makes that argument stronger (its "
            "evidence, its reasoning, or the other side's weakness).\n"
            "- Appear near the **end of your introduction paragraph**.\n\n"
            "**Weak vs. strong thesis -- examples**\n\n"
            "Topic: Two passages debate whether homework should be limited.\n\n"
            "*Weak thesis:* 'Homework is a complicated topic and both sides make interesting "
            "points.'\n"
            "- Problem: Takes no position. Tells the reader nothing. Would score 0 on Trait 1.\n\n"
            "*Weak thesis:* 'I think homework is bad because I always have too much.'\n"
            "- Problem: Personal opinion, not an analysis of the passages. No reference to "
            "evidence quality.\n\n"
            "*Strong thesis:* 'Passage A presents a better-supported argument against unlimited "
            "homework because it cites specific research on student stress and diminishing "
            "academic returns, while Passage B relies mainly on tradition and personal anecdote.'\n"
            "- Strength: Takes a clear side, names the stronger passage, explains WHY (specific "
            "research vs. anecdote), and signals what the body paragraphs will prove.\n\n"
            "**The formula to build your thesis**\n\n"
            "'[Passage A / B] presents a better-supported argument because it [specific evidence "
            "or reasoning strength], while [Passage B / A] relies on [weakness].'\n\n"
            "You don't have to follow this formula word for word, but hitting all three parts "
            "(clear side + why yours is stronger + why the other is weaker) is the goal.\n\n"
            "[[figure:argument|Mapping each passage's claim, evidence, and reasoning before you "
            "write makes building a thesis much easier -- you can see the gap in quality clearly.]]\n\n"
            "⚠️ Common mistake: writing a thesis that summarizes both passages equally. 'Passage "
            "A says X and Passage B says Y' is a summary, not a thesis. A thesis takes a side.\n\n"
            "💡 Tip: write your thesis last in your pre-writing phase, after you have already "
            "decided which passage is stronger. You can't argue a position you haven't chosen yet."
        ),
        (
            "4. Planning Your Essay",
            "Five minutes of planning saves ten minutes of confusion while writing. Students who "
            "skip the outline often stall mid-essay, repeat themselves, or realize their second "
            "body paragraph says the same thing as the first.\n\n"
            "[[figure:essay_structure|A reliable Extended Response structure: Introduction (with "
            "thesis) -- Body Paragraph 1 -- Body Paragraph 2 -- Conclusion. Each body paragraph "
            "makes one distinct point supported by specific evidence from the source texts.]]\n\n"
            "**The 5-minute outline**\n\n"
            "You don't need full sentences. A quick outline might look like this:\n\n"
            "- **Intro:** Hook + context + thesis (Passage A is better because...)\n"
            "- **Body 1:** Main evidence point from Passage A -- quote/detail + explanation of why "
            "this evidence is strong\n"
            "- **Body 2:** Second evidence point from Passage A (or: why Passage B's evidence is "
            "weak) -- quote/detail + explanation\n"
            "- **Conclusion:** Restate thesis in new words + brief significance\n\n"
            "**How to decide which passage wins before you write**\n\n"
            "After reading and annotating (Lesson 2), ask three questions:\n\n"
            "- Which passage has more **specific** evidence (statistics, named studies, concrete "
            "examples) vs. vague generalities?\n"
            "- Which passage's reasoning actually **connects** the evidence to the claim?\n"
            "- Which passage relies more on **emotion or opinion** instead of facts?\n\n"
            "The passage that answers 'more specific evidence' and 'better reasoning' is your "
            "winner. Pick that one and commit -- do not change your thesis mid-essay.\n\n"
            "**Two body paragraphs is enough**\n\n"
            "The GED ER does not require five paragraphs. Two focused, well-supported body "
            "paragraphs score better than three thin, evidence-free ones. Quality beats quantity.\n\n"
            "**Common outline strategies**\n\n"
            "- *All-positive:* Both body paragraphs support the stronger passage.\n"
            "- *Contrast:* Body 1 supports the stronger passage; Body 2 attacks the weaker one.\n"
            "- Either works. The contrast approach often earns extra Trait 1 points by directly "
            "comparing the evidence quality.\n\n"
            "⚠️ Common mistake: spending the full 45 minutes writing without a plan, then "
            "realizing at minute 35 that both body paragraphs make the same point.\n\n"
            "💡 Tip: jot your outline in the scratch area and put a star next to the specific "
            "quote or statistic from each passage that you plan to use in each body paragraph. "
            "Having the evidence pre-located saves time."
        ),
        (
            "5. Writing Body Paragraphs with Evidence",
            "Body paragraphs are the engine of your essay. They are where you actually prove your "
            "thesis by pointing to specific things in the source texts. A body paragraph that "
            "makes a point but never cites evidence will earn low marks on Trait 1 and Trait 2.\n\n"
            "**The PEEL method**\n\n"
            "PEEL is a four-step structure for writing every body paragraph:\n\n"
            "- **P -- Point:** Open the paragraph with a clear topic sentence that states the "
            "one argument you are making in this paragraph. This should connect directly to your "
            "thesis.\n"
            "- **E -- Evidence:** Immediately follow with a specific piece of evidence from the "
            "passage -- a quote, a statistic, a named study, or a concrete example.\n"
            "- **E -- Explain:** This is the most important step most students skip. Explain in "
            "your own words WHY that evidence proves your point. Don't assume the quote speaks "
            "for itself -- connect it.\n"
            "- **L -- Link:** Close the paragraph with a sentence that ties back to your thesis "
            "and signals a transition to the next paragraph.\n\n"
            "**Quoting vs. paraphrasing**\n\n"
            "Both are valid. The key rule: always give the source credit and always explain what "
            "the evidence means.\n\n"
            "- **Quoting** (using the author's exact words): Put quotation marks around the "
            "words. Example: 'Passage A states that \"students lose up to two months of math "
            "skills over summer break,\" which directly contradicts the claim that long breaks "
            "are harmless.'\n"
            "- **Paraphrasing** (restating in your own words): No quotation marks needed, but "
            "still say 'according to Passage A' or 'the first author notes.' Example: 'According "
            "to Passage A, students recover lost ground slowly, suggesting that shorter breaks "
            "would keep skills sharper.'\n\n"
            "**Sample PEEL paragraph**\n\n"
            "Point: 'Passage A is better supported because it backs its central claim with "
            "specific, verifiable data.'\n\n"
            "Evidence: 'For example, Passage A cites a district study showing that schools on "
            "year-round calendars scored eight percent higher on state tests.'\n\n"
            "Explain: 'This statistic is concrete and testable -- it gives a measurable result "
            "linked to a specific school program, which is far more convincing than a general "
            "feeling that one schedule is better than another.'\n\n"
            "Link: 'By contrast, Passage B never offers comparable data, relying instead on the "
            "observation that \"everyone I know loved summer vacation,\" which is personal "
            "anecdote, not evidence that year-round school harms students.'\n\n"
            "Notice how the paragraph NEVER just drops a quote without explaining it. The "
            "explain step is what earns Trait 1 points.\n\n"
            "⚠️ Common mistake: writing 'Passage A says [quote]. This proves my point.' That is "
            "not an explanation -- it just asserts. You must explain the logical connection "
            "between the evidence and your argument.\n\n"
            "💡 Tip: after writing each body paragraph, ask yourself: 'Have I (P) made a clear "
            "point, (E) cited specific evidence, (E) explained why it proves my point, and "
            "(L) linked back to my thesis?' If any letter is missing, add it before moving on."
        ),
        (
            "6. Writing the Introduction and Conclusion",
            "The introduction and conclusion are the frame of your essay. They create a first and "
            "last impression on the grader. Neither needs to be long -- one focused paragraph each "
            "is ideal.\n\n"
            "[[figure:essay_structure|Essay structure at a glance: Introduction sets up the "
            "thesis; Body paragraphs build the case with evidence; Conclusion closes the argument "
            "without introducing new ideas.]]\n\n"
            "**Writing the introduction**\n\n"
            "A strong introduction has three parts:\n\n"
            "- **Hook (1-2 sentences):** An opening that orients the reader to the issue. You can "
            "briefly state what the two passages are about or pose a question. You do NOT need a "
            "creative literary hook -- this is not a personal essay. Keep it simple and relevant.\n"
            "  - Example: 'The question of whether year-round schooling helps students is debated "
            "in both passages, each taking an opposite position on the evidence.'\n"
            "- **Context sentence (1 sentence):** Briefly name what the two passages argue, so "
            "the reader knows what texts are being analyzed.\n"
            "  - Example: 'Passage A argues in favor of year-round school using data, while "
            "Passage B opposes it using personal experience.'\n"
            "- **Thesis (1 sentence):** End the introduction with your thesis statement (see "
            "Lesson 3). This is the most important sentence in the introduction.\n\n"
            "**What NOT to do in the introduction**\n\n"
            "- Do NOT start with 'In this essay I will...' (announces but does not argue).\n"
            "- Do NOT use a dictionary definition ('According to Merriam-Webster...').\n"
            "- Do NOT make it longer than three to four sentences -- graders want to get to the "
            "argument quickly.\n\n"
            "**Writing the conclusion**\n\n"
            "A strong conclusion has two parts:\n\n"
            "- **Restate the thesis in new words:** Do not copy your thesis word for word. "
            "Reframe it. Example: If your thesis said 'Passage A is better supported because it "
            "uses data,' your conclusion might say 'Ultimately, the argument backed by concrete "
            "research is the more persuasive one.'\n"
            "- **End with significance (1 sentence):** Why does it matter which argument is "
            "better? You can briefly note the stakes of the issue or what a strong argument "
            "requires. Example: 'Strong arguments depend on evidence, not emotion -- a "
            "distinction that separates the two passages clearly.'\n\n"
            "**What NOT to do in the conclusion**\n\n"
            "- Do NOT introduce new evidence or a new argument in the conclusion.\n"
            "- Do NOT end with 'In conclusion, as I have shown...' -- it wastes words.\n"
            "- Do NOT simply repeat the introduction word for word.\n\n"
            "⚠️ Common mistake: leaving out the thesis restatement in the conclusion. Without it, "
            "the essay feels unfinished and the grader is left uncertain of your final position.\n\n"
            "💡 Tip: write your introduction AFTER you have written your body paragraphs. It is "
            "much easier to introduce an argument you have already made than to predict what you "
            "are about to write."
        ),
        (
            "7. Revision, Transitions & Scoring Yourself",
            "With five minutes left on the clock, switch from writer to editor. A targeted "
            "revision -- not a full rewrite -- can lift your score on all three GED traits.\n\n"
            "**Transition words between paragraphs**\n\n"
            "Transitions signal to the grader that your essay is organized and your ideas connect. "
            "A body paragraph that begins 'Another reason...' scores better than one that "
            "begins with no connecting word at all.\n\n"
            "[[figure:transition_words|Common transition words and phrases grouped by purpose: "
            "Adding (furthermore, in addition, also), Contrasting (however, by contrast, on the "
            "other hand), Cause/effect (therefore, as a result, consequently), "
            "Illustrating (for example, specifically, to illustrate), Concluding (ultimately, "
            "in summary, overall).]]\n\n"
            "**Quick revision checklist (5 minutes)**\n\n"
            "- Does my **introduction** end with a clear thesis that takes a side?\n"
            "- Does each **body paragraph** start with a topic sentence and include specific "
            "evidence from the passage?\n"
            "- Have I **explained** each piece of evidence (not just quoted it)?\n"
            "- Do I use at least one **transition word** between each paragraph?\n"
            "- Does my **conclusion** restate the thesis in different words?\n"
            "- Are there obvious **run-ons or fragments** I can fix quickly? (One pass for "
            "sentence completeness is enough -- this is revision, not a grammar overhaul.)\n\n"
            "**Using the GED rubric to self-score**\n\n"
            "The GED ER rubric scores each trait on a 0-2 scale:\n\n"
            "- **Trait 1 (Analysis): Score 2** = clearly identifies which argument is stronger, "
            "cites specific evidence from the text, and explains the reasoning. **Score 1** = "
            "some analysis but vague or incomplete. **Score 0** = no analysis; just summarizes "
            "or shares personal opinion.\n"
            "- **Trait 2 (Development/Organization): Score 2** = clear intro-body-conclusion "
            "structure, focused paragraphs, well-developed ideas. **Score 1** = some structure "
            "but uneven development. **Score 0** = no recognizable structure.\n"
            "- **Trait 3 (Conventions): Score 2** = mostly correct grammar and spelling, clear "
            "sentences. **Score 1** = some errors but meaning is clear. **Score 0** = errors "
            "so frequent that meaning is hard to follow.\n\n"
            "**Practice: self-score a sample essay**\n\n"
            "Write a short paragraph (3-5 sentences) arguing which of these two claims is better "
            "supported:\n\n"
            "- Claim A: 'Cities should plant more trees. Studies show urban trees lower air "
            "temperatures by up to 10 degrees and reduce energy costs.'\n"
            "- Claim B: 'Cities do not need more trees. Trees are messy and nobody really "
            "wants them.'\n\n"
            "Then ask: Did you pick a side? Did you cite specific evidence? Did you explain the "
            "connection? If yes to all three -- you have hit a Trait 1 score of 2.\n\n"
            "⚠️ Common mistake: spending revision time rewriting whole paragraphs. In 5 minutes, "
            "focus only on the checklist above -- big rewrites usually make essays worse, not "
            "better.\n\n"
            "💡 Tip: the single highest-impact revision move is to check every body paragraph for "
            "an explanation sentence after the evidence. If you dropped a quote and moved on, "
            "add one sentence explaining why that quote matters. That one change can raise your "
            "Trait 1 score significantly."
        ),
    ],
    "mcqs": [
        # ── Lesson 1: Understanding the Extended Response Task ──────────────
        {
            "text": (
                "The GED Extended Response asks you to read two passages on the same issue and then:"
            ),
            "difficulty": 1,
            "choices": [
                ("Explain which argument is better supported by evidence and reasoning", True),
                ("Share your personal opinion about which side you agree with", False),
                ("Summarize both passages in equal detail", False),
                ("Identify all grammar errors in the passages", False),
            ],
            "explanation": (
                "The GED Extended Response task is an analysis task, not an opinion task. You must "
                "judge which argument uses stronger evidence and reasoning -- even if you personally "
                "agree with the other side. Summarizing equally or hunting grammar errors are not "
                "the goal."
            ),
        },
        {
            "text": (
                "The GED Extended Response is scored on three traits. Which trait is worth the most "
                "and requires you to cite specific evidence from the passages?"
            ),
            "difficulty": 2,
            "choices": [
                ("Trait 1 -- Analysis of Arguments and Evidence", True),
                ("Trait 2 -- Development of Ideas and Organizational Structure", False),
                ("Trait 3 -- Clarity and Command of Standard English Conventions", False),
                ("All three traits are equally weighted", False),
            ],
            "explanation": (
                "Trait 1 (Analysis of Arguments and Evidence) is the highest-weighted trait. It "
                "requires students to identify claims, evaluate evidence quality, and explain "
                "reasoning. A well-written essay that never analyzes the arguments will score "
                "poorly on Trait 1 and therefore overall."
            ),
        },
        {
            "text": (
                "A student has 45 minutes for the Extended Response. Which time plan is best?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "5 min read/annotate, 5 min outline, 30 min write, 5 min revise",
                    True,
                ),
                ("45 min writing with no planning or revision time", False),
                ("20 min reading, 20 min writing, 5 min revising", False),
                ("10 min writing a thesis, then writing the rest", False),
            ],
            "explanation": (
                "A balanced split -- 5 minutes reading, 5 minutes planning, 30 minutes writing, and "
                "5 minutes revising -- is the most effective approach. Skipping planning leads to "
                "disorganized essays, and over-reading wastes time that should go into writing."
            ),
        },
        {
            "text": (
                "Which of the following would most directly lower a student's Trait 1 score on the "
                "Extended Response?"
            ),
            "difficulty": 3,
            "choices": [
                (
                    "Writing about their personal experience with the topic instead of analyzing the passages",
                    True,
                ),
                ("Using transition words between paragraphs", False),
                ("Restating the thesis in the conclusion", False),
                ("Quoting a specific statistic from Passage A", False),
            ],
            "explanation": (
                "Trait 1 scores analysis of the passages' arguments. Writing from personal "
                "experience substitutes the student's opinion for textual analysis -- exactly what "
                "the rubric penalizes. Transitions, restating the thesis, and citing statistics all "
                "help the score."
            ),
        },
        # ── Lesson 2: Reading and Analyzing the Source Texts ─────────────────
        {
            "text": (
                "Read these two pieces of evidence about the same claim, then answer.\n\n"
                "Evidence X: 'A 2019 university study found that students who slept fewer than "
                "7 hours scored 15 percent lower on recall tests the next day.'\n\n"
                "Evidence Y: 'Everyone knows that not sleeping enough makes you feel terrible.'\n\n"
                "Which piece of evidence is stronger, and why?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Evidence X, because it is specific, sourced, and measurable",
                    True,
                ),
                ("Evidence Y, because it is more relatable to the reader", False),
                ("Both are equally strong because they support the same claim", False),
                ("Evidence Y, because it uses common knowledge which is always reliable", False),
            ],
            "explanation": (
                "Strong evidence is specific and verifiable. Evidence X names a source (a 2019 "
                "university study), a specific threshold (fewer than 7 hours), and a measurable "
                "outcome (15 percent lower scores). Evidence Y is a vague appeal to common "
                "knowledge with no checkable data."
            ),
        },
        {
            "text": (
                "When annotating the source texts for the Extended Response, what should you write "
                "next to each piece of evidence in the passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("A note marking whether the evidence is specific/strong or vague/weak", True),
                ("A rewrite of the evidence in better English", False),
                ("Your personal opinion about whether the claim is true", False),
                ("A grammar correction if the sentence is awkward", False),
            ],
            "explanation": (
                "When annotating, your goal is to evaluate the argument structure: circle the "
                "claim, mark evidence with 'E', and note whether each piece of evidence is strong "
                "(specific, checkable) or weak (vague, emotional). Rewriting, personal opinions, "
                "and grammar corrections are not part of argument annotation."
            ),
        },
        {
            "text": (
                "A passage argues: 'We should ban sugary drinks in schools. Childhood obesity has "
                "tripled since 1980, and a study of 12,000 students found that removing vending "
                "machines cut soda consumption by 58 percent.'\n\n"
                "A second passage argues: 'Banning sugary drinks is going too far. Students "
                "deserve choices, and many kids just love soda. Taking away freedom never works.'\n\n"
                "Which passage is better supported, and why?"
            ),
            "difficulty": 3,
            "choices": [
                (
                    "The first, because it uses statistics and a named study rather than appeals to personal freedom and feelings",
                    True,
                ),
                ("The second, because the argument about freedom is always compelling", False),
                ("Both equally, because each makes a valid point", False),
                (
                    "The second, because it is shorter and easier to read",
                    False,
                ),
            ],
            "explanation": (
                "The first passage provides two specific, verifiable data points: a historical "
                "statistic on obesity and a study with a measurable outcome. The second passage "
                "relies on emotional appeals ('students deserve choices', 'kids just love soda') "
                "and an unsupported generalization. Specific evidence beats emotional appeals on "
                "the GED rubric."
            ),
        },
        {
            "text": (
                "After reading both source passages, a student writes in the margin: "
                "'Passage A argues year-round school reduces learning loss, using a district study; "
                "Passage B argues year-round school is harmful, using personal stories.'\n\n"
                "This note is useful because it:"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Summarizes each passage's claim and evidence type, making it easier to write a thesis",
                    True,
                ),
                ("Evaluates the student's personal opinion about the topic", False),
                ("Provides new evidence that is not in the passages", False),
                ("Is a complete draft of the essay introduction", False),
            ],
            "explanation": (
                "A one-sentence annotation capturing the claim and evidence type for each passage "
                "is a pre-writing technique that makes thesis-writing faster and more accurate. It "
                "is not an opinion, not new evidence, and not a draft introduction."
            ),
        },
        # ── Lesson 3: Building a Strong Thesis ───────────────────────────────
        {
            "text": (
                "Which of the following is the strongest thesis statement for a GED Extended "
                "Response essay?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Passage A presents a better-supported argument because it cites a specific study and statistics, while Passage B relies mainly on personal anecdote and emotional appeals.",
                    True,
                ),
                (
                    "Both passages discuss year-round school and make interesting points about education.",
                    False,
                ),
                ("I believe year-round school is a bad idea because it ruins summer vacation.", False),
                ("This essay will explain the two sides of the year-round school debate.", False),
            ],
            "explanation": (
                "A strong GED thesis (1) names which passage is better supported, (2) states why "
                "(evidence quality), and (3) notes the other passage's weakness. 'Both passages "
                "make interesting points' takes no side. 'I believe' uses personal opinion instead "
                "of passage analysis. 'This essay will explain' announces without arguing."
            ),
        },
        {
            "text": (
                "A student writes this thesis: 'Passage B is better because it makes me feel "
                "more strongly about the issue and the writing is more emotional.'\n\n"
                "What is the main problem with this thesis?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "It judges the passage based on emotional impact rather than the quality of its evidence and reasoning",
                    True,
                ),
                ("It is too long and should be one word", False),
                ("It mentions Passage B, but should mention Passage A", False),
                ("It does not begin with the word 'I'", False),
            ],
            "explanation": (
                "The GED rubric asks you to evaluate which argument is better SUPPORTED -- meaning "
                "which has stronger evidence and reasoning. Basing the thesis on emotional impact "
                "('makes me feel more strongly') misunderstands the task. Emotional writing is not "
                "the same as well-evidenced writing."
            ),
        },
        {
            "text": (
                "In the GED Extended Response thesis formula, 'while [other passage] relies on "
                "[weakness]' serves what purpose?"
            ),
            "difficulty": 3,
            "choices": [
                (
                    "It strengthens the argument by showing why the other passage's evidence is less convincing",
                    True,
                ),
                ("It summarizes both passages equally to seem fair", False),
                ("It adds a personal opinion to balance the thesis", False),
                ("It transitions to the conclusion", False),
            ],
            "explanation": (
                "Naming the other passage's weakness (reliance on opinion, anecdote, or vague "
                "claims) is a contrast move that strengthens your thesis. It shows you have "
                "evaluated BOTH arguments -- a key Trait 1 requirement. It is not about fairness, "
                "personal opinion, or conclusions."
            ),
        },
        {
            "text": (
                "Where should the thesis statement appear in the Extended Response essay?"
            ),
            "difficulty": 1,
            "choices": [
                ("At the end of the introduction paragraph", True),
                ("At the beginning of the first body paragraph", False),
                ("At the start of the conclusion", False),
                ("Anywhere in the essay, as long as it is present", False),
            ],
            "explanation": (
                "Convention and GED grader expectations both place the thesis at the end of the "
                "introduction. This signals to the reader what the entire essay will argue. "
                "Placing it in a body paragraph or conclusion paragraph makes the essay harder to "
                "follow and typically lowers the organizational score."
            ),
        },
        # ── Lesson 4: Planning Your Essay ─────────────────────────────────────
        {
            "text": (
                "A student decides to write her Extended Response essay without making an outline "
                "first. What is the most likely result?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Her body paragraphs may repeat the same point or lack clear focus because she has no plan to follow",
                    True,
                ),
                ("Her essay will be longer and earn more points", False),
                ("Her grammar will be better because she is not distracted by planning", False),
                ("She will finish faster and have more time to revise", False),
            ],
            "explanation": (
                "Without an outline, writers frequently repeat points, lose track of their thesis, "
                "or realize mid-essay that their paragraphs overlap. A 5-minute outline prevents "
                "these problems. Essay length is not directly scored, and skipping planning does "
                "not improve grammar or create extra revision time."
            ),
        },
        {
            "text": (
                "In the 'contrast' body paragraph strategy, what does the second body paragraph do?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "It analyzes why the weaker passage's evidence is unconvincing, reinforcing the thesis",
                    True,
                ),
                ("It presents a third argument the student found outside the passages", False),
                ("It summarizes the plot of the stronger passage", False),
                ("It introduces a new thesis different from the introduction", False),
            ],
            "explanation": (
                "In the contrast strategy, the second body paragraph attacks the weaker passage's "
                "evidence or reasoning, showing why it fails to make a convincing case. This "
                "directly supports the thesis by comparison. Introducing outside arguments, "
                "summarizing plots, or changing the thesis are all errors."
            ),
        },
        {
            "text": (
                "Before writing, a student notes: 'Passage A uses a named study with a statistic; "
                "Passage B uses the phrase \"most people agree.\"' Based on this, which passage "
                "should the student argue is better supported?"
            ),
            "difficulty": 1,
            "choices": [
                ("Passage A, because a named study with a statistic is stronger evidence than an unsourced appeal to majority opinion", True),
                ("Passage B, because appealing to what most people think is persuasive", False),
                ("Neither, because both are equally valid types of evidence", False),
                ("Passage B, because shorter evidence is clearer", False),
            ],
            "explanation": (
                "A named study with a statistic is specific and verifiable -- the gold standard of "
                "evidence. 'Most people agree' is an appeal to the majority (a logical fallacy) "
                "with no source or data. The GED rubric rewards identification of this quality "
                "difference."
            ),
        },
        {
            "text": (
                "How many body paragraphs does a GED Extended Response essay require?"
            ),
            "difficulty": 1,
            "choices": [
                (
                    "Two well-supported paragraphs are sufficient; quality matters more than quantity",
                    True,
                ),
                ("Exactly five paragraphs, no more and no less", False),
                ("At least ten paragraphs to demonstrate full coverage", False),
                ("One long paragraph covering all points", False),
            ],
            "explanation": (
                "The GED does not mandate a five-paragraph format. Two focused, evidence-rich body "
                "paragraphs score better than three or four thin, underdeveloped ones. The rubric "
                "rewards depth of analysis and use of evidence, not paragraph count."
            ),
        },
        # ── Lesson 5: Writing Body Paragraphs with Evidence ──────────────────
        {
            "text": (
                "In the PEEL method, what does the second 'E' (Explain) step require the writer "
                "to do?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Connect the evidence to the paragraph's main point by explaining in their own words why it is convincing",
                    True,
                ),
                ("Add a second quote from the passage to reinforce the first", False),
                ("Restate the thesis statement again", False),
                ("Summarize the entire passage in one sentence", False),
            ],
            "explanation": (
                "The Explain step is the most commonly skipped step. After quoting or paraphrasing "
                "evidence, you must explain the logical connection: why does this evidence prove "
                "your point? Simply dropping a quote and moving on leaves the grader to make the "
                "connection for you, which loses Trait 1 points."
            ),
        },
        {
            "text": (
                "A student writes: 'Passage A states that \"students lose two months of math "
                "skills over summer.\" This proves my point.'\n\n"
                "What is wrong with this body paragraph sentence?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "It drops a quote but provides no explanation of how the evidence connects to the argument",
                    True,
                ),
                ("It uses a quotation, which is not allowed in the Extended Response", False),
                ("It correctly applies the full PEEL method", False),
                ("The quote is too short to count as evidence", False),
            ],
            "explanation": (
                "Quotations are allowed -- and encouraged -- in the Extended Response. The problem "
                "is that 'This proves my point' is not an explanation. The student must explain "
                "WHY losing two months of math skills connects to their argument (for example, by "
                "showing the long-term cost of skill loss). That logical explanation is the missing "
                "Explain step."
            ),
        },
        {
            "text": (
                "Which of the following is the best opening sentence for a body paragraph in "
                "an Extended Response arguing that Passage A is stronger?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Passage A's argument is more convincing because it supports its central claim with a specific, verifiable study.",
                    True,
                ),
                ("I agree with Passage A because it makes a good point.", False),
                ("Passage A and Passage B both discuss the same topic.", False),
                ("The study mentioned in Passage A was very interesting.", False),
            ],
            "explanation": (
                "A strong topic sentence (the P in PEEL) states the paragraph's argument -- why "
                "Passage A is stronger -- and signals what evidence will follow. 'Makes a good "
                "point' is vague. 'Both discuss the same topic' is not an argument. 'Very "
                "interesting' is a personal reaction, not a claim about evidence quality."
            ),
        },
        {
            "text": (
                "When paraphrasing evidence from a source passage, which rule must the writer follow?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "Restate the idea in their own words AND include a phrase like 'according to Passage A' to credit the source",
                    True,
                ),
                ("Copy the sentence exactly but remove the quotation marks", False),
                ("Only use evidence that appears in both passages", False),
                ("Avoid paraphrasing entirely and only use direct quotes", False),
            ],
            "explanation": (
                "Paraphrasing means restating in your own words without quotation marks, but you "
                "must still attribute the idea to the passage (e.g., 'According to Passage A...'). "
                "Copying without quotation marks is plagiarism. Evidence from one passage is fine. "
                "Both quoting and paraphrasing are valid -- neither is required exclusively."
            ),
        },
        # ── Lesson 6: Writing the Introduction and Conclusion ────────────────
        {
            "text": (
                "Which is the WORST way to open an Extended Response introduction?"
            ),
            "difficulty": 2,
            "choices": [
                ("In this essay, I will explain which passage is better.", True),
                (
                    "The question of whether cities should invest in public parks divides the two passages in this prompt.",
                    False,
                ),
                (
                    "Passage A and Passage B take opposite positions on the role of public parks in urban life.",
                    False,
                ),
                (
                    "Public parks and urban development are the subjects of two contrasting arguments in this prompt.",
                    False,
                ),
            ],
            "explanation": (
                "'In this essay, I will explain...' is an announcement formula that wastes the "
                "opening sentence without making any argument. It tells the reader what you are "
                "going to do instead of starting to do it. All other options orient the reader to "
                "the issue and the passages without merely announcing an intention."
            ),
        },
        {
            "text": (
                "A student's introduction paragraph ends with: 'Both passages make valid arguments "
                "and it is hard to say which is better.'\n\n"
                "What is the main problem?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "It fails to take a clear side, so the essay has no thesis and the grader does not know what argument to expect",
                    True,
                ),
                ("The introduction should not mention both passages", False),
                ("The sentence is too short to count as a thesis", False),
                ("Conclusions, not introductions, should include a judgment", False),
            ],
            "explanation": (
                "A thesis must take a clear position. 'It is hard to say which is better' refuses "
                "to commit to a side, leaving the essay with no argument to develop. This is the "
                "single most common Extended Response error and results in a Trait 1 score of 0 "
                "or 1."
            ),
        },
        {
            "text": (
                "Which of the following is the best conclusion for a GED Extended Response essay?"
            ),
            "difficulty": 3,
            "choices": [
                (
                    "Ultimately, the argument backed by concrete research is more persuasive than one built on personal feelings, demonstrating that evidence quality is what separates a strong argument from a weak one.",
                    True,
                ),
                (
                    "In conclusion, as I have shown, Passage A is better because it uses a study.",
                    False,
                ),
                (
                    "A new study I found online also supports Passage A's position on this issue.",
                    False,
                ),
                (
                    "To summarize: Passage A talks about year-round school and Passage B talks about year-round school too.",
                    False,
                ),
            ],
            "explanation": (
                "The best conclusion restates the thesis in fresh language and adds a brief "
                "statement of significance ('evidence quality is what separates a strong argument "
                "from a weak one'). 'As I have shown' is a cliche that wastes words. Introducing "
                "outside evidence in the conclusion is an error. Simply summarizing both passages "
                "does not restate an argument."
            ),
        },
        {
            "text": (
                "Why is it often better to write the introduction AFTER writing the body paragraphs?"
            ),
            "difficulty": 3,
            "choices": [
                (
                    "Because after writing the body paragraphs, you know exactly what argument you have made and can introduce it accurately",
                    True,
                ),
                ("Because introductions always get the highest scores so they need the most time", False),
                ("Because the GED grader reads the introduction last", False),
                ("Because body paragraphs must be written first according to GED rules", False),
            ],
            "explanation": (
                "Writing the body first is a practical drafting strategy: once you have developed "
                "your argument in the body paragraphs, you know precisely what your thesis should "
                "claim and what context the introduction needs to set up. There is no GED rule "
                "about writing order; graders read in order but do not penalize writing sequence."
            ),
        },
        # ── Lesson 7: Revision, Transitions & Scoring Yourself ───────────────
        {
            "text": (
                "A student wants to connect the end of her first body paragraph to the beginning "
                "of her second. Her first paragraph argues that Passage A's data is strong. Her "
                "second argues that Passage B's evidence is weak.\n\n"
                "Which transition best bridges the two paragraphs?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "By contrast, Passage B fails to match this standard of evidence, relying instead on emotional appeals with no supporting data.",
                    True,
                ),
                ("Also, Passage A has a lot of good evidence.", False),
                ("In conclusion, Passage B is weaker.", False),
                ("For example, Passage A uses a study.", False),
            ],
            "explanation": (
                "'By contrast' signals a shift from supporting the stronger passage to critiquing "
                "the weaker one -- exactly what the second paragraph does. 'Also' adds rather than "
                "contrasts. 'In conclusion' is a closing signal, not a bridge between body "
                "paragraphs. 'For example' introduces an illustration, not a contrast."
            ),
        },
        {
            "text": (
                "According to the GED rubric, what does a Trait 1 score of 0 indicate?"
            ),
            "difficulty": 2,
            "choices": [
                (
                    "The response does not analyze the arguments -- it only summarizes the passages or shares the writer's personal opinion",
                    True,
                ),
                ("The response has too many grammar errors to be understood", False),
                ("The response is missing a conclusion paragraph", False),
                ("The response uses too many quotations from the passages", False),
            ],
            "explanation": (
                "A Trait 1 score of 0 means the response fails to analyze arguments at all -- "
                "typically because the writer summarized or shared personal views instead of "
                "evaluating evidence. Grammar errors lower Trait 3, not Trait 1. A missing "
                "conclusion affects Trait 2. Using many quotations, if explained, can help Trait 1."
            ),
        },
        {
            "text": (
                "During the 5-minute revision window, which action will most directly improve "
                "a student's Trait 1 score?"
            ),
            "difficulty": 3,
            "choices": [
                (
                    "Checking that every piece of quoted or paraphrased evidence is followed by a sentence explaining how it supports the argument",
                    True,
                ),
                ("Rewriting the entire introduction with different vocabulary", False),
                ("Adding more commas to make sentences sound more academic", False),
                ("Changing the font size to make the essay look longer", False),
            ],
            "explanation": (
                "Trait 1 is specifically about analysis of evidence. The most common gap is "
                "dropped evidence with no explanation. Adding an explanation sentence after each "
                "piece of evidence is a targeted, high-impact revision move. Rewriting the "
                "introduction or adding commas does not directly improve argument analysis."
            ),
        },
        {
            "text": (
                "Which of the following transition words is most appropriate for introducing "
                "an example that supports a point already made?"
            ),
            "difficulty": 1,
            "choices": [
                ("For example", True),
                ("However", False),
                ("Therefore", False),
                ("On the other hand", False),
            ],
            "explanation": (
                "'For example' (or 'for instance', 'specifically', 'to illustrate') signals that "
                "an illustration is coming. 'However' and 'on the other hand' signal contrast. "
                "'Therefore' signals a conclusion drawn from prior evidence. Using the wrong "
                "transition type confuses the reader about the relationship between ideas."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed GED RLA: Extended Response & Essay Writing course"

    def handle(self, *args, **options):
        course, _ = Course.objects.update_or_create(
            slug=COURSE["slug"],
            defaults={
                "title": COURSE["title"],
                "program": COURSE["program"],
                "subject": COURSE["subject"],
                "description": COURSE["description"],
            },
        )
        course.lessons.all().delete()
        for order, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=order)

        course.questions.all().delete()
        for item in COURSE["mcqs"]:
            q = Question.objects.create(
                course=course,
                text=item["text"],
                qtype="mcq",
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=q, text=text, is_correct=is_correct)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with {len(COURSE['lessons'])} lessons and {len(COURSE['mcqs'])} questions."
            )
        )
