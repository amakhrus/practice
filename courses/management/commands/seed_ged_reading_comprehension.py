"""
Seed data: 'GED RLA: Reading Comprehension' — a focused deep dive into the
reading strand of the GED Reasoning Through Language Arts test.

About 75% of GED RLA questions are reading-based. This course teaches every
skill tested: identifying main idea, making inferences, recognising author's
purpose and point of view, navigating text structure, understanding vocabulary
in context, comparing two texts, and handling both informational and literary
passages.

Run:
    python manage.py seed_ged_reading_comprehension
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Reading Comprehension",
    "slug": "ged-reading-comprehension",
    "program": "GED",
    "subject": "rla",
    "description": (
        "About 75% of GED RLA questions require close reading. This deep-dive course builds "
        "every skill tested: finding the main idea, making inferences, recognising author's "
        "purpose and tone, understanding text structure, decoding unfamiliar vocabulary in context, "
        "comparing two passages on the same topic, and handling both informational and literary "
        "texts. Every lesson uses real passage examples, plain explanations, and GED-style "
        "practice questions with full explanations."
    ),
    "lessons": [
        (
            "1. Main Idea and Supporting Details",
            "The most common GED reading question asks you to identify the **main idea** — "
            "the central point the whole passage is making. This is different from the **topic** "
            "(what the passage is about) and from a single **detail** (one piece of evidence).\n\n"
            "Think of a passage as a table:\n"
            "- The **main idea** is the tabletop — the one claim everything supports.\n"
            "- **Supporting details** are the legs — specific facts, examples, statistics, or reasons.\n"
            "- The **topic** is just the label on the table — a word or short phrase.\n\n"
            "**Explicit vs. implicit main idea:**\n"
            "- **Explicit** — the author states the main idea directly, often in the first or last "
            "sentence of a paragraph (the **topic sentence**).\n"
            "- **Implicit** — the main idea is never stated outright; you must infer it from "
            "what the details add up to.\n\n"
            "**How to find the main idea in three steps:**\n"
            "1. Read the first and last sentences of each paragraph — authors often signal the "
            "main point there.\n"
            "2. Ask: 'What are ALL the details in this passage trying to prove or show?'\n"
            "3. Rule out answers that are too narrow (just one detail) or too broad (a vague "
            "generalisation the passage never makes).\n\n"
            "**Common wrong-answer traps:**\n"
            "- An answer that is **true** but only mentioned once — too narrow, it's a detail.\n"
            "- An answer that **sounds reasonable** but is never stated or implied — outside the passage.\n"
            "- An answer that is so **general** it could describe hundreds of passages — too broad.\n\n"
            "⚠️ Common mistake: choosing an answer because it is a true fact about the world, not "
            "because the passage actually says it. Always ask: 'Where does this passage support this?'\n\n"
            "💡 Tip: after reading a passage, try to summarise it in one sentence before looking at "
            "the answer choices. Match your summary to the closest option."
        ),
        (
            "2. Inference and Drawing Conclusions",
            "An **inference** is a conclusion you reach based on evidence — reading between the "
            "lines to understand what the author implies but does not state directly.\n\n"
            "Inference is not guessing. It is a **logical step** from what the text says to what "
            "it means. Every inference must be **supported by specific evidence** in the passage.\n\n"
            "**Types of inference questions:**\n"
            "- 'What can be *inferred* from the passage?'\n"
            "- 'What does the author *imply*?'\n"
            "- 'Based on the passage, what is *most likely* true?'\n"
            "- 'What conclusion is *best supported* by the passage?'\n\n"
            "**How to approach inference questions:**\n"
            "1. Find the relevant section of the passage.\n"
            "2. Ask: 'What must be true if this statement is true?'\n"
            "3. Eliminate answers that require information **not** in the passage.\n"
            "4. Choose the answer that is the **smallest logical step** from what the text says.\n\n"
            "**Example:** A passage says a factory was built in 1905 and 'by 1910 the town's "
            "population had tripled.' You can infer the factory attracted workers. You cannot infer "
            "the factory was profitable (not stated) or that the mayor supported it (never mentioned).\n\n"
            "**Unstated assumptions** are ideas the author takes for granted without stating. "
            "On the GED, you may be asked to identify what assumption an argument depends on.\n\n"
            "⚠️ Common mistake: making inferences that go too far. 'The character seemed nervous' "
            "supports the inference she was anxious — not that she was planning to lie.\n\n"
            "💡 Tip: the correct inference answer is almost always the most *conservative* one — "
            "the one that requires the least amount of new information beyond what the passage says."
        ),
        (
            "3. Author's Purpose and Point of View",
            "Every passage is written for a reason. Understanding the author's **purpose** and "
            "**point of view** helps you answer questions about why the author includes certain "
            "details, uses specific words, or structures the text a particular way.\n\n"
            "**The three main purposes:**\n"
            "- **To inform** — presents facts, explains a concept, or describes a process. "
            "Tone is neutral and objective. (textbooks, news articles, encyclopedia entries)\n"
            "- **To persuade** — argues for a position or tries to change the reader's mind. "
            "Tone is opinionated; includes emotional appeals and loaded language. (editorials, speeches, ads)\n"
            "- **To entertain** — engages the reader with narrative, humour, or vivid description. "
            "(short stories, memoirs, personal essays)\n\n"
            "**Point of view** is the author's perspective or position on the topic. Even informational "
            "texts reveal a point of view through word choice and what details the author includes or omits.\n\n"
            "**Reading for tone:**\n"
            "Tone is the author's attitude toward the subject. Clue words that signal tone:\n"
            "- Positive tone: *innovative, crucial, remarkable, vital*\n"
            "- Negative tone: *reckless, misguided, alarming, wasteful*\n"
            "- Neutral tone: *reported, stated, indicated, noted*\n\n"
            "**Bias** occurs when an author presents only one side of an issue or uses emotionally "
            "loaded language to sway the reader. A biased source may still contain true facts, "
            "but it selects and frames them to support one conclusion.\n\n"
            "[[figure:argument|An argument has a claim, evidence that supports it, and reasoning that connects them. Identifying these parts reveals the author's purpose and point of view.]]\n\n"
            "⚠️ Common mistake: confusing the author's purpose with the passage's topic. The purpose "
            "is WHY it was written, not WHAT it is about.\n\n"
            "💡 Tip: to identify purpose, ask 'What does the author want me to think, feel, or do "
            "after reading this?' Inform = know something. Persuade = believe/do something. "
            "Entertain = experience something."
        ),
        (
            "4. Text Structure and Organisation",
            "Authors organise their writing deliberately. Recognising the **text structure** helps "
            "you predict where to find information and understand how ideas relate to each other.\n\n"
            "**The five main informational text structures:**\n\n"
            "- **Chronological / Sequence** — events in time order.\n"
            "  Signal words: *first, then, next, finally, afterward, subsequently*\n\n"
            "- **Cause and Effect** — explains why something happened and what resulted.\n"
            "  Signal words: *because, as a result, therefore, consequently, led to, caused*\n\n"
            "- **Compare and Contrast** — shows how two or more things are alike or different.\n"
            "  Signal words: *however, in contrast, similarly, on the other hand, both, whereas*\n\n"
            "- **Problem and Solution** — describes a problem and one or more solutions.\n"
            "  Signal words: *the problem is, one solution, to address this, resolved by*\n\n"
            "- **Description / Definition** — describes characteristics or explains what something is.\n"
            "  Signal words: *for example, such as, in other words, is defined as, consists of*\n\n"
            "**Why structure matters for answering questions:**\n"
            "- A cause-effect passage will have questions like 'What caused X?' or 'What resulted from Y?'\n"
            "- A compare-contrast passage will ask how two things are alike or different.\n"
            "- Knowing the structure tells you WHERE to look for the answer.\n\n"
            "**Paragraph structure:** Most body paragraphs follow: **topic sentence → supporting "
            "details → concluding sentence.**\n\n"
            "⚠️ Common mistake: assuming all passages use only one structure. Many passages mix "
            "structures — a problem-solution text may include cause-effect elements.\n\n"
            "💡 Tip: scan the first sentence of each paragraph and look for signal words before "
            "answering structure questions. The signal words are your fastest shortcut."
        ),
        (
            "5. Vocabulary in Context",
            "The GED does not test obscure vocabulary by itself — it tests whether you can "
            "figure out what a word means **from the surrounding text**. This is called "
            "understanding vocabulary **in context**.\n\n"
            "**Step-by-step strategy:**\n"
            "1. Find the word in the passage.\n"
            "2. Re-read the full sentence AND the sentence before and after it.\n"
            "3. Replace the word with each answer choice and ask: 'Does this make sense in the passage?'\n"
            "4. Choose the answer that fits the passage's meaning best.\n\n"
            "**Connotation vs. Denotation:**\n"
            "- **Denotation** — the dictionary definition (*home* = a place one lives).\n"
            "- **Connotation** — the emotional associations (*home* = warmth, comfort, safety).\n"
            "GED questions often test whether you can distinguish the connotation an author intended.\n\n"
            "**Using word parts:**\n"
            "When context is not enough, break the word into parts:\n"
            "- **Prefixes** change meaning: *un-* (not), *re-* (again), *pre-* (before), *mis-* (wrongly)\n"
            "- **Roots** carry core meaning: *port* (carry), *dict* (say), *rupt* (break), *vis* (see)\n"
            "- **Suffixes** indicate part of speech: *-tion* (noun), *-ous* (adjective), *-ly* (adverb)\n\n"
            "**Example:** 'The scientist remained *sceptical*, demanding more data before accepting "
            "the results.' Even without knowing *sceptical*, context tells you the scientist was "
            "doubtful — not excited or satisfied.\n\n"
            "⚠️ Common mistake: choosing the most common meaning of a word rather than the meaning "
            "it has in this specific passage. Words often have multiple meanings.\n\n"
            "💡 Tip: always go back to the passage. Never answer a vocabulary question from memory "
            "alone — the passage gives you the context clues you need."
        ),
        (
            "6. Comparing Two Texts",
            "Many GED RLA passages come in **pairs** — two short texts on the same topic, "
            "often with different perspectives. You will be asked to compare them: how do the "
            "authors agree, disagree, or approach the topic differently?\n\n"
            "**What to look for when comparing two texts:**\n"
            "- **Main claim:** What is each author arguing or asserting?\n"
            "- **Evidence:** What types does each use (statistics, anecdotes, expert quotes)?\n"
            "- **Tone:** Is each author's tone formal or informal, optimistic or pessimistic?\n"
            "- **Points of agreement:** Where do both authors say essentially the same thing?\n"
            "- **Points of disagreement:** Where do they contradict or challenge each other?\n\n"
            "**Common comparison question types:**\n"
            "- 'How do the two authors differ in their approach to X?'\n"
            "- 'Which statement would BOTH authors most likely agree with?'\n"
            "- 'What evidence does Author B provide that Author A does not address?'\n"
            "- 'How does Author B's tone differ from Author A's?'\n\n"
            "**Synthesis:** Sometimes you must pull ideas from both passages to answer one question. "
            "Read both passages before answering synthesis questions.\n\n"
            "**Strategy for paired passages:**\n"
            "1. Read Passage 1, identify its main claim.\n"
            "2. Read Passage 2, identify its main claim.\n"
            "3. Note: do they agree, disagree, or discuss different aspects?\n"
            "4. Answer single-passage questions first, then tackle comparison questions.\n\n"
            "⚠️ Common mistake: answering a comparison question from only one passage. Comparison "
            "questions require you to account for BOTH texts.\n\n"
            "💡 Tip: mark each passage's main claim as you read. When asked how the authors differ, "
            "refer directly to those marked claims."
        ),
        (
            "7. Informational vs. Literary Texts",
            "The GED RLA reading section includes both **informational** and **literary** texts, "
            "and each type requires slightly different reading strategies.\n\n"
            "**Informational texts** (non-fiction):\n"
            "- Include: articles, essays, speeches, workplace documents, historical documents.\n"
            "- Goal: to inform, explain, or persuade.\n"
            "- Key skills: identify main idea, evaluate evidence, recognise author's purpose and bias.\n"
            "- Look for: thesis, topic sentences, transitions, logical argument structure.\n\n"
            "**Literary texts** (fiction and literary non-fiction):\n"
            "- Include: short stories, novel excerpts, poems, personal essays, memoirs.\n"
            "- Goal: to entertain, evoke emotion, or explore the human experience.\n"
            "- Key skills: identify theme, analyse characters and motivations, understand "
            "figurative language, recognise mood and tone.\n\n"
            "**Theme vs. Main Idea:**\n"
            "- **Main idea** (informational) — the central claim of a non-fiction text, directly "
            "statable: 'Exercise reduces the risk of heart disease.'\n"
            "- **Theme** (literary) — an underlying message about life, usually implied: "
            "'Courage requires accepting uncertainty.' Themes are NOT plot summaries.\n\n"
            "**Figurative language in literary texts:**\n"
            "- **Simile** — comparison using *like* or *as*: 'The room was like a furnace.'\n"
            "- **Metaphor** — direct comparison: 'The world is a stage.'\n"
            "- **Personification** — giving human qualities to non-human things: 'The wind whispered.'\n"
            "- **Irony** — saying the opposite of what is meant, or events contradicting expectations.\n\n"
            "**Character motivation** — why a character acts as they do. Always infer motivation "
            "from the character's words, actions, and the context around them.\n\n"
            "⚠️ Common mistake: treating theme as a plot summary. 'A boy learns to be brave' is "
            "a plot event. 'True courage means acting despite fear' is the theme.\n\n"
            "💡 Tip: for literary passages, ask 'What lesson about life could a reader take away "
            "from this story?' That question leads you straight to the theme."
        ),
    ],
    "mcqs": [
        # Lesson 1 — Main Idea and Supporting Details
        {
            "text": (
                "Read the passage:\n\n"
                "\"Regular physical activity offers benefits that extend far beyond weight control. "
                "Studies show it reduces the risk of heart disease, type 2 diabetes, and several "
                "cancers. It also improves mood, reduces anxiety, and sharpens memory and focus.\"\n\n"
                "What is the main idea of this passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("Regular physical activity provides wide-ranging health benefits beyond weight control.", True),
                ("Exercise helps people lose weight.", False),
                ("Heart disease and diabetes can be prevented through diet.", False),
                ("Memory and focus are the most important benefits of exercise.", False),
            ],
            "explanation": "The first sentence signals the main idea: benefits extend beyond weight control. The remaining sentences are supporting details. The other options are either a single detail or introduce information not in the passage.",
        },
        {
            "text": (
                "A passage discusses the decline of coral reefs, mentions rising ocean temperatures, "
                "describes bleaching events, and explains how bleaching kills coral over time. "
                "Which answer best states the main idea?"
            ),
            "difficulty": 2,
            "choices": [
                ("Rising ocean temperatures are causing widespread coral reef decline through bleaching.", True),
                ("Coral bleaching occurs when water temperatures rise.", False),
                ("Coral reefs are beautiful and important ecosystems.", False),
                ("Marine biologists study coral reefs to understand ocean health.", False),
            ],
            "explanation": "The correct answer combines cause (rising temperatures), process (bleaching), and result (reef decline) — capturing what all the details support. The other options are either a single detail, too vague, or not stated in the passage.",
        },
        {
            "text": "Which of the following is a SUPPORTING DETAIL rather than a main idea?",
            "difficulty": 1,
            "choices": [
                ("In 2022, the city's recycling rate increased by 12 percent.", True),
                ("The city's environmental policies have significantly improved sustainability.", False),
                ("Urban planning decisions have long-term consequences for communities.", False),
                ("Infrastructure investment benefits both residents and local businesses.", False),
            ],
            "explanation": "A specific statistic (12% increase in one year) is a supporting detail — it illustrates a point but cannot stand alone as a passage's central claim. The other three are broad enough to serve as main ideas of whole passages.",
        },
        {
            "text": (
                "A student identifies this as the main idea: 'The Industrial Revolution changed "
                "working conditions for millions of people.' The passage also mentions child labour "
                "laws, 14-hour workdays, and the rise of trade unions. What role do these details play?"
            ),
            "difficulty": 2,
            "choices": [
                ("They are supporting details that provide specific evidence for the main idea.", True),
                ("They are separate main ideas unrelated to the first sentence.", False),
                ("They contradict the main idea.", False),
                ("They replace the main idea since they are more specific.", False),
            ],
            "explanation": "Child labour laws, long workdays, and unions are all specific examples of how working conditions changed — they support the main idea. Details do not replace a main idea; they provide evidence for it.",
        },

        # Lesson 2 — Inference and Drawing Conclusions
        {
            "text": (
                "Read the passage:\n\n"
                "\"Maria arrived twenty minutes late to the interview, her jacket still damp from "
                "the rain. She apologised breathlessly and sat down, smoothing her wet hair.\"\n\n"
                "What can be inferred about Maria's situation?"
            ),
            "difficulty": 1,
            "choices": [
                ("She was caught in the rain and hurried to arrive as quickly as she could.", True),
                ("She did not want to attend the interview.", False),
                ("She had forgotten about the interview until the last moment.", False),
                ("The interviewer was angry with her for being late.", False),
            ],
            "explanation": "The damp jacket, wet hair, and breathless apology directly indicate she was caught in rain and rushed. The other choices introduce information not supported — no evidence of reluctance, forgetfulness, or the interviewer's mood.",
        },
        {
            "text": (
                "A passage states: 'The factory, once the town's largest employer, had been silent "
                "for three years. Weeds pushed through the cracked parking lot, and the windows "
                "were boarded up.'\n\n"
                "What conclusion is BEST supported by the passage?"
            ),
            "difficulty": 2,
            "choices": [
                ("The factory has been closed and abandoned for several years.", True),
                ("The factory was destroyed by a fire.", False),
                ("The town has no other employers.", False),
                ("Workers chose to leave because wages were too low.", False),
            ],
            "explanation": "Three years of silence, weeds, and boarded windows point to closure and abandonment. Fire, wage disputes, and sole-employer status are not mentioned or implied — they go beyond what the evidence supports.",
        },
        {
            "text": (
                "An informational passage states: 'Installation costs for solar panels have fallen "
                "89% over the last decade, and solar now accounts for the largest share of new "
                "electricity generation capacity added in the U.S.'\n\n"
                "Which inference is BEST supported?"
            ),
            "difficulty": 2,
            "choices": [
                ("Solar energy has become significantly more economically competitive over the past decade.", True),
                ("Solar energy is now cheaper than all other energy sources.", False),
                ("The government mandated the switch to solar energy.", False),
                ("Solar will completely replace fossil fuels within five years.", False),
            ],
            "explanation": "An 89% cost drop and leading market share directly support the inference that solar is more economically competitive. The passage does not claim it is cheapest of all, nor does it mention government mandates or a five-year timeline.",
        },
        {
            "text": "A character 'refused to meet anyone's eyes, spoke in a barely audible voice, and kept her hands tightly folded in her lap.' What can be INFERRED about the character?",
            "difficulty": 1,
            "choices": [
                ("She is nervous or uncomfortable in the situation.", True),
                ("She is angry at the people around her.", False),
                ("She is planning to leave the room soon.", False),
                ("She is bored and disinterested.", False),
            ],
            "explanation": "Avoiding eye contact, speaking quietly, and tense body language are classic signals of nervousness. Anger, boredom, or intent to leave are not supported by the described behaviours.",
        },

        # Lesson 3 — Author's Purpose and Point of View
        {
            "text": (
                "A passage begins: 'The proposed highway expansion is a reckless waste of taxpayer "
                "money that will devastate the neighbourhood and benefit only wealthy developers.'\n\n"
                "What is the author's PRIMARY purpose?"
            ),
            "difficulty": 1,
            "choices": [
                ("To persuade readers to oppose the highway expansion.", True),
                ("To inform readers about the details of the highway expansion project.", False),
                ("To entertain readers with a story about neighbourhood life.", False),
                ("To objectively compare the pros and cons of the expansion.", False),
            ],
            "explanation": "Words like 'reckless,' 'waste,' and 'devastate' are emotionally loaded and take a clear negative position — this is persuasion. An informative passage would present facts neutrally.",
        },
        {
            "text": "Which phrase MOST strongly signals a persuasive purpose?",
            "difficulty": 1,
            "choices": [
                ("'Citizens must demand action before it is too late.'", True),
                ("'The study was conducted over a period of five years.'", False),
                ("'The character walked slowly down the empty street.'", False),
                ("'The treaty was signed on November 11, 1918.'", False),
            ],
            "explanation": "'Must demand' is a call to action — a hallmark of persuasive writing. The other choices are neutral factual statements with no persuasive intent.",
        },
        {
            "text": "An author writing to INFORM would most likely use which type of language?",
            "difficulty": 1,
            "choices": [
                ("Neutral, factual language presenting evidence without taking sides.", True),
                ("Emotionally charged words designed to provoke a reaction.", False),
                ("Vivid sensory descriptions and narrative dialogue.", False),
                ("Exaggerated claims and direct calls to action.", False),
            ],
            "explanation": "Informational writing aims to explain or present facts objectively. Emotional language signals persuasion; vivid sensory description signals literary writing; calls to action signal persuasion.",
        },

        # Lesson 4 — Text Structure and Organisation
        {
            "text": "A passage uses 'as a result,' 'because,' and 'therefore' throughout. What text structure is MOST likely being used?",
            "difficulty": 1,
            "choices": [
                ("Cause and effect.", True),
                ("Compare and contrast.", False),
                ("Chronological order.", False),
                ("Problem and solution.", False),
            ],
            "explanation": "'As a result,' 'because,' and 'therefore' signal cause-and-effect relationships. 'However' and 'in contrast' signal compare-contrast; dates and 'then/next' signal chronological order.",
        },
        {
            "text": (
                "A passage describes how urban heat islands form, explains the problems they cause, "
                "and proposes green roofs and urban trees as remedies. What structure does this PRIMARILY use?"
            ),
            "difficulty": 2,
            "choices": [
                ("Problem and solution.", True),
                ("Compare and contrast.", False),
                ("Chronological order.", False),
                ("Definition and description.", False),
            ],
            "explanation": "The passage presents a problem (heat islands) and then offers solutions (green roofs, urban trees) — the defining pattern of problem-solution structure.",
        },
        {
            "text": "Which signal word BEST indicates a compare-and-contrast text structure?",
            "difficulty": 1,
            "choices": [
                ("'In contrast'", True),
                ("'Subsequently'", False),
                ("'As a result'", False),
                ("'For example'", False),
            ],
            "explanation": "'In contrast' directly signals comparison of two different things. 'Subsequently' signals chronological order; 'as a result' signals cause-effect; 'for example' signals description.",
        },

        # Lesson 5 — Vocabulary in Context
        {
            "text": (
                "Read the sentence:\n\n"
                "\"The scientist's explanation was so *lucid* that even students who had struggled "
                "with the concept immediately understood it.\"\n\n"
                "Based on context, what does *lucid* most likely mean?"
            ),
            "difficulty": 1,
            "choices": [
                ("Clear and easy to understand.", True),
                ("Long and detailed.", False),
                ("Controversial and disputed.", False),
                ("Technical and complex.", False),
            ],
            "explanation": "The context clue is the result: students 'immediately understood.' That outcome signals the explanation was clear. Long, controversial, or technical would not produce immediate understanding.",
        },
        {
            "text": (
                "The passage states: 'The company's *frugal* approach — reusing materials, avoiding "
                "unnecessary purchases, and negotiating lower prices — kept it profitable during the recession.'\n\n"
                "What does *frugal* most likely mean here?"
            ),
            "difficulty": 1,
            "choices": [
                ("Careful and economical with money.", True),
                ("Generous and free-spending.", False),
                ("Innovative and forward-thinking.", False),
                ("Risky and unpredictable.", False),
            ],
            "explanation": "Reusing materials, avoiding purchases, and negotiating lower prices all describe saving money carefully. 'Frugal' means thrifty or economical.",
        },
        {
            "text": (
                "A passage describes a politician's speech as 'inflammatory rhetoric.' The next "
                "sentence notes the speech 'angered many citizens and prompted protests.'\n\n"
                "Based on context, what does *inflammatory* most likely mean?"
            ),
            "difficulty": 2,
            "choices": [
                ("Likely to provoke strong, angry reactions.", True),
                ("Calm and intended to resolve conflict.", False),
                ("Factual and evidence-based.", False),
                ("Confusing and difficult to understand.", False),
            ],
            "explanation": "The result — anger and protests — directly signals the meaning. 'Inflammatory' means tending to provoke anger. The context contradicts calm, factual, or confusing.",
        },
        {
            "text": "A student encounters 'benevolent' in a passage about a charity founder who gave away most of her fortune. The root 'bene-' means 'good.' What does 'benevolent' most likely mean?",
            "difficulty": 2,
            "choices": [
                ("Kind and generous.", True),
                ("Wealthy and powerful.", False),
                ("Strict and demanding.", False),
                ("Cautious and reserved.", False),
            ],
            "explanation": "Root 'bene-' = good + context (charity, giving away fortune) = well-meaning, kind, and generous. Wealthy, strict, and cautious are not supported by the root or the context.",
        },

        # Lesson 6 — Comparing Two Texts
        {
            "text": (
                "Passage A argues social media connects isolated individuals and fosters community. "
                "Passage B argues social media replaces meaningful in-person relationships with "
                "shallow online interactions.\n\n"
                "Which statement describes the MAIN difference between the two authors' views?"
            ),
            "difficulty": 2,
            "choices": [
                ("Passage A sees social media as beneficial for relationships; Passage B sees it as harmful.", True),
                ("Both authors agree that social media has replaced in-person relationships.", False),
                ("Passage A focuses on teenagers; Passage B focuses on adults.", False),
                ("Both authors argue social media should be regulated.", False),
            ],
            "explanation": "Passage A is positive (connects, fosters community); Passage B is negative (replaces meaningful relationships with shallow ones). Age groups and government regulation are not mentioned.",
        },
        {
            "text": (
                "Passage A uses government statistics and academic studies to argue minimum wage "
                "increases reduce poverty. Passage B uses interviews with small business owners "
                "to argue they cause job losses.\n\n"
                "How do the passages PRIMARILY differ in their use of evidence?"
            ),
            "difficulty": 2,
            "choices": [
                ("Passage A uses large-scale quantitative data; Passage B uses individual personal accounts.", True),
                ("Passage A uses personal anecdotes; Passage B uses scientific studies.", False),
                ("Both passages rely entirely on government statistics.", False),
                ("Neither passage provides evidence for its claims.", False),
            ],
            "explanation": "Government statistics and academic studies = large-scale quantitative data. Interviews with business owners = individual personal accounts (anecdotal evidence).",
        },
        {
            "text": (
                "Two passages both acknowledge that global temperatures have risen over the last century. "
                "Passage A attributes this to human greenhouse gas emissions. Passage B attributes it "
                "to natural solar cycles.\n\nOn which point do the two authors AGREE?"
            ),
            "difficulty": 1,
            "choices": [
                ("Global temperatures have risen over the last century.", True),
                ("Human activity is the primary cause of climate change.", False),
                ("Natural solar cycles fully explain temperature changes.", False),
                ("Government policy should not address climate change.", False),
            ],
            "explanation": "Both passages accept that temperatures have risen — that is their shared starting point. They disagree only about the cause.",
        },

        # Lesson 7 — Informational vs. Literary Texts
        {
            "text": (
                "Read the passage:\n\n"
                "\"The last maple on Elm Street had shed its leaves, and the boy stood beneath "
                "its bare branches, thinking of his grandfather who had planted it forty years ago.\"\n\n"
                "This passage is an example of what type of text?"
            ),
            "difficulty": 1,
            "choices": [
                ("Literary text — it uses narrative, imagery, and emotional resonance.", True),
                ("Informational text — it contains factual information about a tree.", False),
                ("Persuasive text — it argues that trees should be preserved.", False),
                ("Technical text — it describes the biology of maple trees.", False),
            ],
            "explanation": "Narrative storytelling, vivid imagery, and emotional content are hallmarks of literary text. The passage does not argue, explain a concept, or provide scientific information.",
        },
        {
            "text": "A short story ends with a once-greedy character giving away his possessions after losing everything. What is the most likely THEME?",
            "difficulty": 2,
            "choices": [
                ("True happiness comes from generosity, not material wealth.", True),
                ("The character lost all his money.", False),
                ("Greed always leads to financial ruin.", False),
                ("The story is about a man who gives away possessions.", False),
            ],
            "explanation": "Theme is the universal life lesson. 'True happiness comes from generosity, not material wealth' expresses that lesson. The other options describe plot events, not the underlying message.",
        },
        {
            "text": "Which sentence contains an example of PERSONIFICATION?",
            "difficulty": 1,
            "choices": [
                ("'The ancient oak reached its arms toward the pale winter sky.'", True),
                ("'The temperature dropped ten degrees overnight.'", False),
                ("'She ran as fast as a cheetah.'", False),
                ("'The report concluded that costs had doubled.'", False),
            ],
            "explanation": "Personification gives human qualities to non-human things. A tree having 'arms' and 'reaching' is personification. 'Fast as a cheetah' is a simile. The other two are factual statements.",
        },
        {
            "text": (
                "A GED passage is from a 19th-century speech arguing that women should have the "
                "right to vote. What type of text is it, and what is its primary purpose?"
            ),
            "difficulty": 2,
            "choices": [
                ("Informational/persuasive text; to argue for women's suffrage.", True),
                ("Literary text; to entertain readers with a historical story.", False),
                ("Technical text; to explain the mechanics of voting procedures.", False),
                ("Narrative text; to describe the life of a suffragette.", False),
            ],
            "explanation": "A speech making a political argument is a persuasive informational text. It is not fictional narrative, not a how-to explanation, and not a personal story.",
        },
    ],
}


class Command(BaseCommand):
    help = "Seed GED RLA: Reading Comprehension course"

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

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' with {len(COURSE['lessons'])} lessons and {len(COURSE['mcqs'])} questions."
        ))
