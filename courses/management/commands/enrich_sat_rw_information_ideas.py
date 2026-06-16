"""
Enrich lesson content for the course with slug "sat-rw-information-ideas".
Each lesson is updated by (course__slug, order) so the command is idempotent.

Run:
    python manage.py enrich_sat_rw_information_ideas
"""
from django.core.management.base import BaseCommand
from courses.models import Lesson


LESSONS = [
    (
        1,
        # ── Lesson 1: Central Ideas and Details ──────────────────────────────
        "**Central Ideas and Details**\n\n"

        "**What the SAT tests**\n"
        "Central-idea questions ask you to identify what the whole passage is *about* — not a detail, not an example, but the single most important point the author is making. Typical stems: \"Which choice best states the main idea of the text?\", \"Which choice most accurately summarizes the text?\", or \"What is the central claim of the passage?\" Detail questions, by contrast, ask you to locate a specific fact the author states directly.\n\n"

        "**How to find the main idea**\n"
        "Ask yourself: \"If I had to describe this passage in one sentence to someone who hadn't read it, what would I say?\" Two reliable shortcuts: (1) Check the last sentence — authors often restate or conclude with their main point. (2) Look for a concept mentioned repeatedly throughout the passage; repetition signals importance.\n\n"

        "**Main idea vs. supporting detail**\n"
        "Details are facts, examples, statistics, or reasons that *support* the main point. They are not the main point itself. A detail might be fascinating and take up a whole paragraph, yet still be only one piece of evidence for a bigger claim. Always ask: \"Is this what the whole passage is about, or is it just one part of the argument?\"\n\n"

        "**Sample passage**\n"
        "For most of human history, sleep was considered little more than an unavoidable interruption to productive life. Scientists now know that sleep is one of the most biologically active periods of the day. During the deep stages of sleep, the brain clears out metabolic waste products that accumulate during waking hours. The hippocampus consolidates new memories by replaying recent experiences and transferring them to long-term storage. Immune cells reproduce at higher rates during sleep, making adequate rest essential for fighting infection. Hormones that regulate appetite and stress response are calibrated while we sleep, and disrupting this calibration can contribute to obesity and anxiety disorders. Athletes who extend their sleep show measurable improvements in speed, accuracy, and reaction time. Even a single night of shortened sleep impairs judgment to a degree comparable to legal intoxication. Across the animal kingdom, from fruit flies to elephants, every species studied sleeps — suggesting that whatever sleep does, it is too important to skip. Far from being wasted time, sleep is the foundation on which healthy waking life is built.\n\n"

        "**Worked example**\n"
        "Question: Which choice best states the main idea of the passage?\n\n"
        "A) During sleep, the hippocampus transfers memories to long-term storage.\n"
        "B) Sleep is a biologically essential process that supports brain, body, and immune function.\n"
        "C) Athletes perform better when they get more sleep.\n"
        "D) Scientists once believed sleep was an unproductive period.\n\n"
        "Correct answer: **B**\n\n"
        "Why B is correct: It covers the whole passage — the passage discusses memory, immune function, hormones, athletic performance, and judgment, all pointing to sleep's essential role across brain and body systems. Choice B is broad enough to include all these details without going beyond what the text says.\n\n"
        "Why A is wrong (too narrow): The hippocampus sentence is one detail in the middle of the passage. The passage is not *only* about memory consolidation.\n\n"
        "Why C is wrong (too narrow): Athlete performance is one supporting example, not the central claim.\n\n"
        "Why D is wrong (contradicts the main point): The passage mentions the historical misunderstanding only to contrast it with modern knowledge; this is background, not the main idea. Choosing D would mean the passage is arguing that scientists used to be wrong — but the passage is actually arguing that sleep is essential.\n\n"

        "**Three quick examples of wrong-answer traps**\n"
        "- *Too narrow*: A passage about the decline of coral reefs discusses warming oceans, bleaching, and acidification. A too-narrow answer says \"Rising ocean temperatures cause coral bleaching.\" True, but it covers only one cause, not the whole passage.\n"
        "- *Too broad*: The same passage ends with a sentence about conservation efforts. A too-broad answer says \"Human activity threatens all ocean life.\" The passage never claims this; it stays focused on coral reefs specifically.\n"
        "- *Contradicts text*: An answer that says \"Coral reefs are recovering rapidly\" would directly contradict a passage describing their decline.\n\n"

        "**Key strategies**\n"
        "- Read the first and last sentences of each paragraph; the main idea usually appears there.\n"
        "- Ask: does this answer cover *all* the paragraphs, or only one?\n"
        "- Eliminate answers that use words like \"always,\" \"never,\" or \"proves\" unless the passage itself is that strong.\n\n"

        "**⚠️ Common mistake**\n"
        "Picking the answer that discusses the most interesting or most detailed part of the passage. The most-discussed detail is not the same as the main idea.\n\n"

        "**\U0001f4a1 Tip**\n"
        "After you choose an answer, do a quick check: read your chosen answer and then ask \"Does every paragraph in the passage relate to this idea?\" If a paragraph feels left out, your answer may be too narrow."
    ),
    (
        2,
        # ── Lesson 2: Command of Evidence (Textual) ──────────────────────────
        "**Command of Evidence (Textual)**\n\n"

        "**What the SAT tests**\n"
        "These questions give you a *claim* — a hypothesis, a conclusion, or a generalization — and ask which answer choice from a passage (or which hypothetical finding) most directly supports or strengthens that claim. The key word is *directly*: the right answer must connect specifically to the claim being evaluated, not just to the same general topic.\n\n"

        "**The best-evidence strategy**\n"
        "Step 1 — Identify the claim's key noun and verb. What thing is the claim about, and what does it say that thing does or is?\n"
        "Step 2 — Eliminate choices that are about the same topic but make a different point. \"Related to the topic\" is not good enough; the answer must address *this specific claim*.\n"
        "Step 3 — Pick the choice whose content directly proves the claim. The best evidence makes the claim more believable *on its own*; you should not need additional logic to connect it.\n\n"

        "**The crucial distinction: relevant vs. directly supportive**\n"
        "A choice can be true, interesting, and related to the topic — yet still be the wrong answer because it does not actually prove the claim. If a researcher claims \"students who sleep more score higher on tests,\" evidence that \"sleep deprivation impairs attention\" is *related* but indirect. Direct evidence would be: \"Students averaging eight hours of sleep scored 12% higher than students averaging five hours.\"\n\n"

        "**Sample passage**\n"
        "Urban community gardens have expanded rapidly in cities across North America. Proponents argue that these gardens do more than produce food: they serve as informal gathering places where neighbors who might otherwise never meet begin to talk and collaborate. A 2021 survey of residents living within two blocks of a community garden in Detroit found that 68% reported knowing more of their neighbors by name after the garden opened than before. The same survey found that block association meetings in those neighborhoods saw attendance rise by an average of 40% in the two years following the garden's establishment. Garden coordinators note that residents often trade not just vegetables but recipes, childcare, and home-repair skills. Several neighborhoods credit their gardens with organizing the block cleanups and mural projects that followed. Critics point out that gardens require sustained volunteer effort and that many close within three years of opening. Nonetheless, even short-lived gardens appear to produce lasting social effects, as friendships formed over planting beds tend to outlast the gardens themselves.\n\n"

        "**Worked example**\n"
        "Claim: Community gardens strengthen social connections among urban residents.\n\n"
        "Which finding from the passage most directly supports this claim?\n\n"
        "A) Community gardens have expanded rapidly across North American cities.\n"
        "B) 68% of residents near a Detroit garden reported knowing more neighbors by name after the garden opened.\n"
        "C) Many community gardens close within three years of opening.\n"
        "D) Garden coordinators note that residents trade recipes and childcare.\n\n"
        "Correct answer: **B**\n\n"
        "Why B is correct: The claim is specifically about *strengthening social connections*. Knowing more neighbors by name is a direct, measurable indicator of stronger social connection. The statistic — 68% of residents — makes the claim quantifiably more believable.\n\n"
        "Why A is wrong: Expansion of gardens tells us about the *spread* of gardens, not about whether they strengthen social bonds. It is relevant to gardens but not to this claim.\n\n"
        "Why C is wrong: Closure rates are actually a potential *weakness* of gardens, and do not speak to whether they strengthen connections while they exist.\n\n"
        "Why D is wrong: Trading recipes and childcare does suggest social connection, but it is the coordinator's anecdotal observation. Choice B provides a specific percentage from a survey — far more direct and quantifiable support for the claim.\n\n"

        "**⚠️ Common mistake**\n"
        "Choosing an answer because it discusses a detail that *sounds impressive* or is mentioned prominently. The correct evidence is the one that logically proves the claim, not the one you find most interesting.\n\n"

        "**\U0001f4a1 Tip**\n"
        "Before reading the answer choices, rephrase the claim in your own words and think: \"What kind of fact would make me believe this?\" Then look for the answer that matches that type of fact."
    ),
    (
        3,
        # ── Lesson 3: Command of Evidence (Quantitative) ──────────────────────
        "**Command of Evidence (Quantitative)**\n\n"

        "**What the SAT tests**\n"
        "These questions pair a short passage with a data table or graph. You must choose which specific data point or data comparison, when combined with the passage's argument, best supports a stated conclusion. The challenge is not reading the table — it is connecting the right piece of data to the right claim.\n\n"

        "**Reading quantitative data**\n"
        "Before answering, spend 20 seconds on the table or graph: (1) Read the title — it tells you what the whole thing is measuring. (2) Read the column and row headers — they tell you the categories and units. (3) Identify the range: what are the highest and lowest values? This prevents misreading scale.\n\n"

        "**Connecting data to text**\n"
        "The passage makes a claim; the data is your evidence pool. Your job is to match the *right data point or comparison* to the *specific claim* — not just any number from the table. A number can be accurate and still be the wrong answer if it supports a different point.\n\n"

        "**Sample passage with data table**\n"
        "A nutrition researcher argues that increasing daily protein intake is associated with higher muscle retention in adults over 60 during a 12-week exercise program. Participants were divided into four groups based on grams of protein consumed per kilogram of body weight per day. At the end of the study, each group's average percentage of muscle mass retained was recorded.\n\n"
        "Protein Intake and Muscle Retention (Adults 60+, 12-week program)\n"
        "| Protein (g/kg/day) | Avg. Muscle Retained (%) |\n"
        "|---|---|\n"
        "| 0.6 | 81% |\n"
        "| 0.8 | 87% |\n"
        "| 1.0 | 92% |\n"
        "| 1.2 | 96% |\n\n"

        "**Worked example**\n"
        "Which choice best uses data from the table to support the researcher's argument?\n\n"
        "A) Participants consuming 0.6 g/kg/day retained an average of 81% of their muscle mass.\n"
        "B) As protein intake increased from 0.6 to 1.2 g/kg/day, average muscle retention rose from 81% to 96%.\n"
        "C) Participants consuming 1.0 g/kg/day retained more muscle than those consuming 0.8 g/kg/day.\n"
        "D) Protein intake was measured in grams per kilogram of body weight per day.\n\n"
        "Correct answer: **B**\n\n"
        "Why B is correct: The researcher's argument is that *more protein = more muscle retention*. To support this association, you need data that shows the trend across intake levels. Choice B cites the full range — lowest protein with lowest retention (81%) to highest protein with highest retention (96%) — directly demonstrating the pattern the researcher claims.\n\n"
        "Why A is wrong: One data point shows what one group retained, but it says nothing about whether *more* protein leads to *more* retention. A single row cannot demonstrate an association.\n\n"
        "Why C is wrong: Comparing only two adjacent groups (1.0 vs. 0.8) supports a trend claim weakly; it does not show the full picture. More importantly, the question asks for the data that best supports the claim, and B does this more completely.\n\n"
        "Why D is wrong: This simply describes how protein intake was measured. It provides no information about the outcome (muscle retention) and therefore supports nothing.\n\n"

        "**Common traps**\n"
        "- Citing a data point that is true but addresses a different aspect of the table than what the claim requires.\n"
        "- Choosing an answer with an impressive-sounding number that does not actually show the relationship stated in the claim.\n"
        "- Misreading units (confusing percentages with raw counts, or grams with kilograms).\n\n"

        "**⚠️ Common mistake**\n"
        "Picking the largest number in the table. The largest number is not automatically the correct evidence; the correct evidence is the data that logically proves the specific claim.\n\n"

        "**\U0001f4a1 Tip**\n"
        "For claims about a *trend* or *association*, the correct answer almost always cites two or more data points that together show the direction of the relationship — not a single isolated value."
    ),
    (
        4,
        # ── Lesson 4: Drawing Inferences ─────────────────────────────────────
        "**Drawing Inferences**\n\n"

        "**What the SAT tests**\n"
        "Inference questions ask what can be *logically concluded* from the passage — what must be true if everything the passage says is true. Common stems: \"Which choice most logically completes the text?\" or \"Based on the text, which conclusion is best supported?\" The answer is always something the passage *implies* through its stated facts, not something you happen to know from outside the text.\n\n"

        "**Inference vs. assumption**\n"
        "An *inference* follows necessarily from clues in the text — it is the next logical step given what the passage states. An *assumption* is something you bring from outside the passage — knowledge you have that the text never actually provides. SAT answers that require outside knowledge are always wrong, no matter how true that outside knowledge is.\n\n"

        "**The \"must be true\" vs. \"could be true\" distinction**\n"
        "The SAT wants what *must* be true — what you are *forced* to conclude from the passage, not what might possibly be true. If an answer could be true but the passage does not actually make it necessary, it is wrong. A strong inference is one you can defend by pointing to specific words in the passage.\n\n"

        "**Over-inference traps**\n"
        "The SAT routinely offers choices that are reasonable-sounding but go one step further than the text supports. If the text says \"the treatment appeared to reduce symptoms in most patients,\" an inference that \"the treatment cures the disease\" goes far beyond what the evidence warrants. Watch for extreme words: *always, never, proves, guarantees, all, none*.\n\n"

        "**Sample passage**\n"
        "The Venus flytrap is one of the few plant species that actively captures and digests animal prey. When an insect lands on an open trap leaf and touches two trigger hairs within about 20 seconds, the leaf snaps shut. The plant then secretes digestive enzymes that break down the insect's soft tissues over the course of several days. Researchers have found that the trapping mechanism requires a burst of electrical activity similar to the nerve impulses in animal muscles. If a trap is triggered but catches nothing, it reopens within 12 hours — but each leaf can only open and close successfully a limited number of times before it loses function. Venus flytraps grow in nitrogen-poor, waterlogged soils where most other plants cannot thrive; the ability to digest insects appears to compensate for the lack of nitrogen in their environment. Scientists note that flytraps have evolved this complex hunting mechanism independently of any animal lineage. The plant's digestive process slows significantly in cold temperatures, making warm conditions essential for effective nutrient absorption.\n\n"

        "**Inference question 1**\n"
        "Which conclusion is most directly supported by the passage?\n\n"
        "A) Venus flytraps are the only carnivorous plants in the world.\n"
        "B) Venus flytraps likely struggle to survive in soil rich with nutrients.\n"
        "C) Insect capture allows Venus flytraps to compensate for low nitrogen in their environment.\n"
        "D) The electrical activity in Venus flytraps is identical to that in animal nerve cells.\n\n"
        "Correct answer: **C** — The passage directly states that the ability to digest insects \"appears to compensate for the lack of nitrogen in their environment.\"\n"
        "Why A is wrong: The passage says \"one of the few\" carnivorous plants, not the only one.\n"
        "Why B is wrong: The passage never discusses how the plant performs in nutrient-rich soil — this requires an assumption.\n"
        "Why D is wrong: The passage says electrical activity is \"similar to\" nerve impulses, not \"identical.\"\n\n"

        "**Inference question 2**\n"
        "Based on the passage, what would most likely happen if a Venus flytrap were kept in very cold temperatures?\n\n"
        "A) The plant would trap insects more efficiently.\n"
        "B) The plant would absorb nutrients less effectively.\n"
        "C) The plant's trigger hairs would become more sensitive.\n"
        "D) The plant would stop growing in nitrogen-poor soil.\n\n"
        "Correct answer: **B** — The passage states that \"the plant's digestive process slows significantly in cold temperatures, making warm conditions essential for effective nutrient absorption.\" Slower digestion logically leads to less effective absorption.\n\n"

        "**Inference question 3**\n"
        "Which statement about Venus flytrap traps can be inferred from the passage?\n\n"
        "A) Traps are most effective when triggered multiple times in a row.\n"
        "B) A trap that closes on an empty leaf will eventually open again.\n"
        "C) Each leaf can snap shut an unlimited number of times.\n"
        "D) Traps only close when both trigger hairs are touched simultaneously.\n\n"
        "Correct answer: **B** — The passage states \"it reopens within 12 hours\" when a trap catches nothing, directly supporting B.\n\n"

        "**⚠️ Common mistake**\n"
        "Choosing an answer that *sounds scientific* or that you know to be true from outside the passage. On inference questions, outside knowledge is never a valid justification. Everything must come from the text.\n\n"

        "**\U0001f4a1 Tip**\n"
        "After choosing an answer, ask: \"Can I point to specific words in the passage that make this true?\" If you cannot, reconsider."
    ),
    (
        5,
        # ── Lesson 5: Cross-Text Connections ─────────────────────────────────
        "**Cross-Text Connections**\n\n"

        "**What the SAT tests**\n"
        "Cross-text questions give you two short passages (Text 1 and Text 2) on the same topic, each written by a different author or expressing a different perspective. Questions ask how the authors relate: Do they agree? Disagree? Does one provide evidence the other uses? Does one expand on the other's ideas?\n\n"

        "**Mapping strategy**\n"
        "Before reading the questions, read both texts and write (or mentally note) each author's main claim in one sentence. Use a simple label: \"Text 1 says: X. Text 2 says: Y.\" This map is your anchor for every question. Without it, you risk confusing which author said what under time pressure.\n\n"

        "**Types of relationships**\n"
        "- *Direct agreement*: Both authors make essentially the same point.\n"
        "- *Direct disagreement*: The authors take opposing positions on the same question.\n"
        "- *Partial agreement with qualification*: One author agrees with part of the other's argument but adds a limitation or condition.\n"
        "- *One expands the other*: Text 2 provides more detail, evidence, or context for the claim Text 1 makes.\n"
        "- *One provides evidence the other uses*: Text 1 reports data or findings; Text 2 interprets or applies them.\n\n"

        "**Sample paired passages**\n\n"
        "Text 1 (Dr. Amara Osei, educational psychologist):\n"
        "\"The widespread belief that students learn best through a single preferred 'learning style' — visual, auditory, or kinesthetic — has shaped curriculum design for decades. Schools have invested enormous resources in tailoring lessons to match individual style profiles. Emerging research, however, suggests that this entire framework is built on shaky foundations. Controlled studies consistently find that students do not perform better when taught in their supposed preferred style. The theory's intuitive appeal has led educators to accept it without adequate scrutiny. It is time to retire the learning styles myth and redirect those resources toward evidence-based instructional strategies. Instruction that integrates multiple modalities appears to benefit all learners, regardless of any supposed style preference.\"\n\n"
        "Text 2 (Professor Lin Wei, curriculum design):\n"
        "\"Critics of learning styles theory are right to demand rigorous evidence before educational practice is shaped by any model. The specific claim that matching instruction to a student's preferred modality improves performance has not held up well under controlled testing. Yet the broader insight that students differ meaningfully in the ways they engage with material should not be abandoned. Individual differences in background knowledge, working memory capacity, and prior exposure to a topic are all real and well-documented. Effective teachers have always adapted their methods to the students in front of them. The lesson is not that student differences are irrelevant, but that the particular sorting mechanism of learning styles was the wrong tool for capturing those differences.\"\n\n"

        "**Worked example 1**\n"
        "How would the author of Text 2 most likely respond to the argument in Text 1?\n\n"
        "A) By fully agreeing that learning styles theory should be discarded and resources reallocated.\n"
        "B) By agreeing that the specific learning styles model is unsupported, but arguing that individual student differences still matter.\n"
        "C) By defending learning styles theory against the critique in Text 1.\n"
        "D) By arguing that controlled studies are an inappropriate method for evaluating learning theories.\n\n"
        "Correct answer: **B** — Text 2's author agrees with the critique of learning styles but explicitly argues that \"individual differences... should not be abandoned.\" This is a partial agreement with a qualification — Text 2 accepts Text 1's main critique but resists the conclusion that student differences are irrelevant.\n\n"

        "**Worked example 2**\n"
        "On which point would the authors of both texts most likely agree?\n\n"
        "A) The learning styles framework is a useful tool that has been unfairly criticized.\n"
        "B) Controlled studies have failed to confirm that teaching to a student's preferred learning style improves performance.\n"
        "C) All student differences in learning are largely irrelevant to instructional design.\n"
        "D) Schools should stop using any form of differentiated instruction.\n\n"
        "Correct answer: **B** — Both texts explicitly state that controlled studies do not support the learning-styles matching hypothesis. Text 1: \"Controlled studies consistently find that students do not perform better.\" Text 2: \"The specific claim... has not held up well under controlled testing.\"\n\n"

        "**⚠️ Common mistake**\n"
        "Mixing up which author said what. Under time pressure, it is easy to attribute a point from Text 2 to Text 1, or vice versa. Always confirm which text you are quoting before choosing.\n\n"

        "**\U0001f4a1 Tip**\n"
        "For \"how would Author B respond to Author A\" questions, find the sentence in Text 2 that most directly addresses the specific claim from Text 1 that the question names. The answer is almost always a direct quotable connection between those two sentences."
    ),
    (
        6,
        # ── Lesson 6: Main Purpose and Rhetorical Situation ──────────────────
        "**Main Purpose and Rhetorical Situation**\n\n"

        "**What the SAT tests**\n"
        "These questions move beyond *what* the passage says to *why* the author wrote it and *for whom*. Stems include: \"What is the main purpose of the text?\", \"Which choice best describes the overall function of the text?\", \"The author most likely wrote this text for an audience of ______.\"\n\n"

        "**Author purpose categories**\n"
        "Every passage on the SAT is written for a reason. The most common purposes:\n"
        "- *To inform*: present facts, findings, or explanations without taking a side.\n"
        "- *To persuade*: argue for a position; advocate for a course of action.\n"
        "- *To describe*: paint a detailed picture of a person, place, event, or process.\n"
        "- *To analyze*: examine how or why something works, or what it means.\n"
        "- *To challenge or critique*: question, complicate, or refute a common belief or practice.\n\n"

        "**The rhetorical situation**\n"
        "The *rhetorical situation* is the full context surrounding a piece of writing:\n"
        "- *Author (who)*: an expert? a journalist? a student? This affects tone and credibility claims.\n"
        "- *Audience (for whom)*: specialists? the general public? policymakers? Audience shapes vocabulary level, assumed knowledge, and the types of evidence used.\n"
        "- *Purpose (why)*: see the categories above.\n"
        "- *Context (when/where)*: a scientific journal? an op-ed? a museum placard? Context shapes every stylistic choice.\n\n"

        "**Genre signals**\n"
        "- *Academic paper*: passive voice (\"it was found that\"), hedging (\"suggests,\" \"may indicate\"), citations, technical vocabulary.\n"
        "- *Op-ed / opinion column*: first person, direct opinion statements (\"we must,\" \"it is clear that\"), appeals to shared values.\n"
        "- *Research summary*: third person, past tense for findings (\"the study found\"), hedged language.\n"
        "- *Narrative or literary nonfiction*: past tense, sensory detail, character perspective, scene-building.\n\n"

        "**Sample passage**\n"
        "Marine biologists have long known that dolphins communicate using clicks and whistles, but the question of whether these vocalizations constitute a true language has been intensely debated. A true language, most linguists argue, must be generative — capable of combining a finite set of elements to express an infinite range of meanings. Recent research using acoustic analysis software suggests that bottlenose dolphins vary the structure of their whistle sequences in ways that correspond to specific social contexts, such as greeting, alarm, and play. Individual dolphins appear to maintain a unique signature whistle that functions similarly to a name. Young dolphins spend years learning the vocal repertoire of their social group in a process that resembles the acquisition of language in human children. However, no study has yet demonstrated that dolphins can generate entirely novel messages about situations they have not previously encountered — the definitive test of generative capacity. The question remains open, and the stakes are high: if dolphin communication proves to be a true language, it would be the first known case outside the human lineage. Until that threshold is crossed, most researchers prefer the cautious term \"sophisticated communication system\" to the loaded word \"language.\"\n\n"

        "**Worked example 1**\n"
        "What is the main purpose of the text?\n\n"
        "A) To argue that dolphin communication should be classified as a true language.\n"
        "B) To describe recent discoveries about dolphin behavior for a general audience.\n"
        "C) To analyze the current state of evidence on whether dolphin communication qualifies as language.\n"
        "D) To persuade policymakers to fund more research into animal communication.\n\n"
        "Correct answer: **C** — The passage presents evidence on both sides of the debate (features that suggest language; the missing criterion of generativity) and concludes that \"the question remains open.\" This is analysis of a debate, not advocacy for one position.\n\n"

        "**Worked example 2**\n"
        "The author most likely wrote this text for an audience of\n\n"
        "A) professional marine biologists writing for a peer-reviewed journal.\n"
        "B) policymakers deciding on conservation budgets.\n"
        "C) educated general readers interested in science.\n"
        "D) children learning about ocean animals.\n\n"
        "Correct answer: **C** — The passage uses some technical terms (\"generative,\" \"acoustic analysis\") but defines them in plain language and avoids citations, statistical notation, and jargon-heavy prose. This matches a science magazine or long-form journalism aimed at informed non-specialists.\n\n"

        "**⚠️ Common mistake**\n"
        "Confusing *what* the passage says with *why* it was written. A passage that *mentions* a problem is not necessarily written *to persuade* readers to solve it. Purpose answers must reflect the author's dominant intent, not a single sentence.\n\n"

        "**\U0001f4a1 Tip**\n"
        "The verb in the purpose answer is crucial: \"to inform\" vs. \"to argue\" vs. \"to analyze\" carry very different meanings. Match the verb to the overall tone of the passage before looking at the rest of the answer choice."
    ),
    (
        7,
        # ── Lesson 7: SAT Information & Ideas Strategy ───────────────────────
        "**SAT Information & Ideas: Full Strategy Guide**\n\n"

        "**The 4-step approach**\n"
        "1. *Read the question stem first.* Before reading the passage, know what you are looking for. \"Main idea\" and \"which finding supports\" are very different tasks; the stem tells you how to read.\n"
        "2. *Skim for structure, not every word.* Note where the passage is going: what does the first sentence claim? Does the author turn (\"however,\" \"but\")? Where does evidence appear? You do not need to absorb every detail on the first pass.\n"
        "3. *Find the relevant section.* Once you know what the question asks, locate the specific sentence or paragraph that answers it. For main-idea questions, consider the whole passage. For evidence or detail questions, pin down the one or two sentences that contain the answer.\n"
        "4. *Eliminate before selecting.* Cross off answers that are clearly wrong before committing. You should be able to name *why* a wrong answer is wrong (too narrow, contradicts text, etc.).\n\n"

        "**Time management**\n"
        "The SAT Reading & Writing section gives you roughly 64 minutes for approximately 54 questions — about 70 seconds each. Information & Ideas questions typically require more reading than grammar or vocabulary questions, so budget accordingly:\n"
        "- *Fast questions* (vocabulary, grammar, transitions): aim for 45-60 seconds.\n"
        "- *Reading questions* (main idea, inference, evidence): allow up to 90 seconds.\n"
        "- *When to skip*: if you are stuck after 60 seconds, mark the question, make your best guess, and return if time allows. A skipped question answered at the end is worth the same as one answered first.\n\n"

        "**The \"passage-based only\" rule**\n"
        "This is the single most important rule for Information & Ideas questions: every correct answer must be supported by words in the passage. Your outside knowledge — even if accurate — is never the source of a correct answer. If you find yourself thinking \"I know from science class that...,\" stop. Return to the passage.\n\n"

        "**Elimination checklist**\n"
        "Eliminate any answer choice that:\n"
        "- Contradicts something explicitly stated in the passage.\n"
        "- Goes beyond what the passage says (makes a stronger claim than the evidence supports).\n"
        "- Addresses the wrong part of the passage (answers a different question than the one asked).\n"
        "- Uses extreme language (\"always,\" \"never,\" \"proves,\" \"all\") when the passage uses qualified language (\"often,\" \"suggests,\" \"many\").\n"
        "- Requires you to know something the passage never mentions.\n\n"

        "**Practice application 1 — Main idea**\n"
        "Passage summary: A text describes how urban heat islands form, explains why dark surfaces absorb more heat, notes that cities are warming faster than rural areas, and ends by proposing green roofs and light-colored pavement as mitigation strategies.\n\n"
        "Question: Which choice best states the main idea?\n"
        "A) Dark surfaces are the primary cause of urban warming. [Too narrow — one detail]\n"
        "B) Urban heat islands form and worsen because of surface materials, and mitigation strategies exist. [Correct — covers all sections]\n"
        "C) Green roofs are the best solution to climate change. [Too broad — the passage only discusses urban heat islands]\n"
        "D) Cities are always hotter than rural areas. [Extreme language — \"always\" is not supported]\n\n"

        "**Practice application 2 — Evidence**\n"
        "Claim: Regular physical activity reduces the risk of cognitive decline in older adults.\n\n"
        "Which finding most directly supports this claim?\n"
        "A) Older adults who walked at least 30 minutes per day for six months scored higher on memory tests than sedentary peers. [Correct — directly connects activity to cognitive outcome]\n"
        "B) Physical activity improves cardiovascular health in people of all ages. [Related but indirect — says nothing about cognitive decline specifically]\n"
        "C) Cognitive decline is more common in adults over 70. [Relevant topic but does not connect activity to risk reduction]\n"
        "D) Many gyms now offer programs specifically designed for seniors. [Completely off-claim]\n\n"

        "**Practice application 3 — Inference**\n"
        "Passage: A scientist notes that a newly discovered deep-sea fish species can only survive at pressures exceeding 600 atmospheres — pressures found only below 6,000 meters — and that it has never been observed in shallower water.\n\n"
        "Which inference is best supported?\n"
        "A) The fish cannot survive at depths shallower than 6,000 meters. [Correct — follows directly from \"only survive at pressures exceeding 600 atmospheres\"]\n"
        "B) The fish is the deepest-living creature on Earth. [Goes beyond the text — no comparison to other species is made]\n"
        "C) Deep-sea fish are more intelligent than shallow-water fish. [Completely outside the passage]\n"
        "D) The species was discovered using a remotely operated vehicle. [The method of discovery is never mentioned]\n\n"

        "**⚠️ Common mistake**\n"
        "Trying to answer from memory instead of returning to the text. Even when you feel confident about what the passage said, always verify by scanning the relevant sentence. Memory is less reliable under test pressure than a quick glance at the text.\n\n"

        "**\U0001f4a1 Tip**\n"
        "The correct answer to an Information & Ideas question is almost always the *most modest* accurate statement the passage supports. When two answers look similar, the one that does not overreach — that stays close to what the passage actually says — is usually right."
    ),
]


class Command(BaseCommand):
    help = "Enrich lesson content for SAT RW: Information & Ideas"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(
                course__slug="sat-rw-information-ideas", order=order
            ).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(
            self.style.SUCCESS(
                "Done enriching SAT RW: Information & Ideas lessons."
            )
        )
