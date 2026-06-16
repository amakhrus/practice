"""
Seed data: 'SAT Reading & Writing: Complete Course & Test Prep' -- a full course
for the digital SAT Reading and Writing section (2024 format).

The digital SAT R&W section is one combined section of two modules. Every
question is tied to its own short passage (about 25-150 words) with four answer
choices, and the questions fall into four content domains:

  1. Craft and Structure (~28%)        -- words in context, text structure &
                                           purpose, cross-text connections
  2. Information and Ideas (~26%)       -- central ideas & details, command of
                                           evidence (textual + quantitative),
                                           inferences
  3. Standard English Conventions (~26%)-- boundaries (punctuation), form,
                                           structure & sense (grammar)
  4. Expression of Ideas (~20%)         -- transitions, rhetorical synthesis

The modern SAT has NO essay, so this course is multiple choice throughout.
Lessons lead with intuition, give worked examples, and include diagrams.
Question text is rendered as plain text (no markdown), so passages use quotes
and blank lines; every explanation names the trap and ends with a Pro tip.

Run:
    python manage.py seed_sat_reading_writing
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "SAT Reading & Writing: Complete Course & Test Prep",
    "slug": "sat-reading-writing-complete",
    "program": "SAT",
    "subject": "rla",
    "description": (
        "A complete course for the digital SAT Reading and Writing section. It covers all four "
        "tested domains -- Craft and Structure (words in context, text structure and purpose, "
        "cross-text connections), Information and Ideas (central ideas, command of evidence, "
        "inferences), Standard English Conventions (punctuation and grammar), and Expression of "
        "Ideas (transitions and rhetorical synthesis). Clear lessons with examples and diagrams, "
        "plus a large bank of realistic, single-passage practice questions with full explanations "
        "and pro tips, so you can master every question type before test day."
    ),
    "lessons": [
        (
            "1. How the Digital SAT Reading & Writing Works",
            r"The SAT Reading and Writing (R&W) section is **digital and adaptive**. It is one combined section split into two short modules; you get about **64 minutes for roughly 54 questions**, a little over a minute each." "\n\n"
            r"The single most important fact about the format: **each question has its own short passage** (about 25-150 words) and **four answer choices**. There are no long passages with many questions anymore — read the short text, answer one question, move on." "\n\n"
            r"Every question belongs to one of **four domains**, and they appear grouped by domain, roughly easy-to-hard within each group:" "\n\n"
            r"[[figure:sat_rw_roadmap|The four domains and their approximate share of the section. This course has a lesson for each.]]" "\n\n"
            r"Two habits win points on every domain:" "\n"
            r"- **The answer is in the text.** SAT R&W is an open-book test. The right answer is *supported by the passage*, not by what you already know." "\n"
            r"- **Predict, then match.** Before reading the choices, decide in your own words what the answer should be. Then find the choice closest to your prediction." "\n\n"
            r"⚠️ Common mistake: choosing an answer because it is *true in real life*. If the passage doesn't support it, it's wrong — no matter how factual it sounds." "\n\n"
            r"💡 Tip: there is **no penalty for wrong answers**. Never leave a blank; eliminate what you can and choose.",
        ),
        (
            "2. Craft & Structure I: Words in Context",
            r"**Words in Context** is the most common question type on the test. You'll see it two ways: 'As used in the text, what does *word* most nearly mean?' or a sentence with a **blank** to fill with 'the most logical and precise word or phrase.'" "\n\n"
            r"The method is the same for both: the surrounding sentence defines the word. Use the **context clues**, not your gut feeling about the word." "\n\n"
            r"- **Predict first.** Cover the choices. Read the sentence and put your *own* simple word in the blank." "\n"
            r"- **Look for signal words.** 'But', 'however', and 'far from' signal a **contrast** (the answer is the opposite of a nearby idea). 'Because' and 'so' signal **cause**." "\n"
            r"- **Match, then check precision.** Several choices may be close; pick the one that fits the exact shade of meaning the sentence needs." "\n\n"
            r"Example: 'Far from being *brief*, the report was exhaustive, running over three hundred pages.' The clue 'exhaustive… three hundred pages' tells you the blank means *long/thorough*, so 'brief' would be wrong and a word like **detailed** fits." "\n\n"
            r"⚠️ Common mistake: picking the word's most *familiar* meaning. SAT loves words with a second meaning ('novel' can mean *new*, not just a book)." "\n\n"
            r"💡 Tip: plug your chosen word back into the sentence and read it aloud in your head. The right answer keeps the sentence's logic intact.",
        ),
        (
            "3. Craft & Structure II: Structure, Purpose & Cross-Text",
            r"This lesson covers two more Craft and Structure types." "\n\n"
            r"**Text Structure & Purpose** asks what a sentence *does* or how the text is *built* — its job, not its topic. Common questions: 'Which choice best describes the **function** of the underlined sentence?' or 'the **overall structure** of the text?'" "\n\n"
            r"Think about the *role* each sentence plays: Does it introduce an idea? Give an example? Raise an objection? Offer a solution? Signal a turn ('but', 'however')?" "\n\n"
            r"- A sentence that starts with 'For example' is **illustrating** the previous claim." "\n"
            r"- A sentence that starts with 'However' is **qualifying or contradicting** it." "\n"
            r"- A final sentence often **draws a conclusion** from what came before." "\n\n"
            r"**Cross-Text Connections** gives you **two short texts** on one topic and asks how they relate — usually, 'How would the author of Text 2 most likely **respond** to Text 1?' Pin down each author's **position** first, then ask whether they agree, disagree, qualify, or add to each other." "\n\n"
            r"⚠️ Common mistake: confusing what a sentence *says* with what it *does*. The question is about its function, like 'it provides counter-evidence', not its content." "\n\n"
            r"💡 Tip: for cross-text questions, label each author in a word — 'Text 1: pro; Text 2: skeptical' — before reading the choices.",
        ),
        (
            "4. Information & Ideas I: Central Ideas & Evidence",
            r"**Central Ideas & Details** questions ask for the main point ('Which choice best states the **main idea**?') or a specific stated fact ('According to the text, …')." "\n\n"
            r"- The **main idea** must cover the *whole* passage — not one detail (too narrow) and not a grander claim than the text makes (too broad)." "\n"
            r"- For a **detail** question, the answer is stated *directly* in the text. Go back and point to the exact sentence." "\n\n"
            r"**Command of Evidence (textual)** is a signature SAT skill. It gives a claim or hypothesis and asks: 'Which finding, if true, would most strongly **support** (or **weaken**) it?'" "\n\n"
            r"[[figure:argument|Strong evidence directly and specifically connects to the claim being made.]]" "\n\n"
            r"To answer, hold the claim in mind and test each choice: does it *directly* make the claim more (or less) likely? The best evidence is **specific and on-target**; wrong choices are true-but-irrelevant, too vague, or about a slightly different point." "\n\n"
            r"⚠️ Common mistake: picking a choice that is interesting or generally related but doesn't actually bear on *this* claim. Relevance beats interest." "\n\n"
            r"💡 Tip: for support/weaken questions, restate the claim in your own words first, then ask of each choice, 'so what — does this change my belief in the claim?'",
        ),
        (
            "5. Information & Ideas II: Data & Inferences",
            r"**Command of Evidence (quantitative)** pairs the text with a small **graph or table**. You must pick the choice that **accurately uses the data** to do a stated job (support a claim, complete an example)." "\n\n"
            r"- Read the table's **labels and units** first." "\n"
            r"- The right choice must be **true to the data** *and* must actually serve the point being made. A choice can state a real number yet fail because it doesn't support the claim." "\n\n"
            r"Here is a worked example. This bar graph shows recycling rates for four materials:" "\n\n"
            r"[[figure:bar_recycling|Always read the exact height of each bar before you judge a claim about the data.]]" "\n\n"
            r"Suppose a claim says *paper is recycled at more than twice the rate of any other material shown*. Test it against the bars: paper is at 68%, and the next-highest is glass at 31%. Since 68 is more than twice 31, the data **support** the claim — and the right answer would cite exactly those two numbers. A trap choice might state a true value like 'plastic is recycled at 9%' that is accurate but says nothing about the comparison being made." "\n\n"
            r"The same logic works for a trend: to support 'more screen time is linked to less sleep,' the right choice describes the **whole downward trend**, not a single data point." "\n\n"
            r"**Inferences** end with a logical blank: 'Which choice most logically **completes** the text?' The passage gives premises; the answer is the conclusion they point to — *with the least added assumption*." "\n\n"
            r"- Follow the logic of the passage to its natural next step." "\n"
            r"- Stay **anchored to the evidence**; don't pick a choice that requires facts the text never gives." "\n\n"
            r"⚠️ Common mistake: over-inferring. If the text supports 'the lights probably helped,' don't choose 'the lights guaranteed success.'" "\n\n"
            r"💡 Tip: a good inference could be defended by pointing to specific words in the passage. If you can't point, it's a guess.",
        ),
        (
            "6. Standard English Conventions I: Boundaries",
            r"**Boundaries** questions test **punctuation** — how to correctly join, separate, and end ideas. The question stem is always: 'Which choice completes the text so that it conforms to the conventions of Standard English?'" "\n\n"
            r"The key idea is whether a group of words is an **independent clause** (a complete sentence that can stand alone) or not." "\n\n"
            r"- **Two independent clauses** can be joined by a **period**, a **semicolon (;)**, or a **comma + FANBOYS** (for, and, nor, but, or, yet, so). A comma *alone* between two sentences is a **comma splice** — wrong." "\n"
            r"- A **colon (:)** follows a complete sentence and introduces a list or explanation: 'She packed three things: a map, water, and a knife.'" "\n"
            r"- **Commas** set off nonessential information: 'The reef, which is enormous, can be seen from space.' (Remove the middle and the sentence still works.)" "\n"
            r"- **Apostrophes** show possession: singular 'the *dog's* bone'; plural 'the *dogs'* bones'. 'Its' = belonging to it; 'it's' = it is." "\n\n"
            r"⚠️ Common mistake: the **comma splice** — using a comma to glue two full sentences together. Upgrade it to a semicolon or period." "\n\n"
            r"💡 Tip: test each side of the punctuation. If both sides are complete sentences, you need a period, a semicolon, or a comma + FANBOYS — never a lone comma.",
        ),
        (
            "7. Standard English Conventions II: Form & Sense",
            r"**Form, Structure & Sense** questions test **grammar**: making verbs and pronouns fit, keeping tenses consistent, and placing modifiers logically." "\n\n"
            r"- **Subject-verb agreement.** The verb matches the *real* subject, even when words come between them: 'The *collection* of rare coins **is** valuable' (subject = collection, not coins)." "\n"
            r"- **Neither/nor (and either/or).** The verb agrees with the **nearer** subject: 'Neither the coach nor the *players* **were** ready.'" "\n"
            r"- **Verb tense.** Keep events in a logical order. Use the **past perfect** ('had spread') for an action completed before another past action: 'By the time help arrived, the fire **had** already spread.'" "\n"
            r"- **Pronoun agreement.** A pronoun matches its noun in number. A company or team is singular: 'The company said **it** would expand,' not 'they.'" "\n"
            r"- **Modifiers.** An opening descriptive phrase must attach to the right noun: 'Walking to school, **Jamal** noticed the leaves' — Jamal is doing the walking, not the leaves." "\n\n"
            r"⚠️ Common mistake: matching the verb to the closest noun instead of the true subject. Mentally cross out the phrase between subject and verb." "\n\n"
            r"💡 Tip: for a dangling modifier, ask 'who or what is doing this action?' — that noun must come right after the comma.",
        ),
        (
            "8. Expression of Ideas: Transitions & Synthesis",
            r"**Transitions** questions ask for 'the most logical transition' to connect two sentences. The trick is to figure out the **relationship** between the ideas, then choose the word that signals it." "\n\n"
            r"[[figure:transition_words|First decide the logic between the two sentences; then pick a transition from that group.]]" "\n\n"
            r"- Same direction / adds on → 'in addition', 'furthermore', 'also'." "\n"
            r"- Opposite direction / turn → 'however', 'nevertheless', 'on the other hand'." "\n"
            r"- Cause leads to effect → 'therefore', 'consequently', 'as a result'." "\n"
            r"- Giving an instance → 'for example', 'for instance'." "\n\n"
            r"Always ask: does the second sentence *agree with*, *contradict*, *result from*, or *illustrate* the first? Pick the matching group." "\n\n"
            r"**Rhetorical Synthesis** gives you a set of **bulleted notes** and a stated goal ('The student wants to emphasize X'). Choose the sentence that **uses the relevant notes to meet that exact goal**. The other choices are usually accurate but serve a *different* goal." "\n\n"
            r"⚠️ Common mistake: on transitions, defaulting to a word that 'sounds smooth' (like 'therefore') without checking the logic. The relationship decides the word." "\n\n"
            r"💡 Tip: for synthesis, underline the **goal** in the prompt first. The right choice is the one that hits *that* goal, not just any true statement.",
        ),
        (
            "9. Test-Day Strategy & Pacing",
            r"You now have a method for all four domains. This lesson is about using them under time pressure." "\n\n"
            r"**Pacing.** About 64 minutes for ~54 questions is roughly **70 seconds each**. Conventions and transitions questions are often fast — bank that time for the reading questions that need a careful re-read." "\n\n"
            r"A reliable per-question routine:" "\n"
            r"- **Read the question stem first** so you know the job (main idea? function? transition?)." "\n"
            r"- **Read the short passage** and, for reading questions, **predict** the answer in your own words." "\n"
            r"- **Eliminate** aggressively. Cross out choices that are off-topic, too extreme ('always', 'never', 'proves'), or true-but-irrelevant." "\n"
            r"- **Match** the remaining choice to the text or your prediction." "\n\n"
            r"**The adaptive format.** The second module gets harder or easier based on your first-module performance, so every question in Module 1 matters — don't rush the early, easier points." "\n\n"
            r"**Guess smart, never blank.** No penalty for wrong answers means a blank is strictly worse than a guess. If you're stuck, eliminate what you can and pick." "\n\n"
            r"⚠️ Common mistake: burning three minutes on one hard question and running out of time for three easy ones later. Mark it, guess, and move on." "\n\n"
            r"💡 Tip: the best answer is usually the most **modest** one the text supports. When two choices remain, the less extreme one is usually right.",
        ),
    ],
    "mcqs": [
        # ===================== CRAFT & STRUCTURE (~28%) =====================
        # -- Words in Context --
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The committee's decision was not final; it was provisional, meant to be "
                     "revisited once more data became available.\"\n\n"
                     "As used in the text, \"provisional\" most nearly means"),
            "difficulty": 2,
            "choices": [("temporary.", True), ("permanent.", False), ("popular.", False), ("secret.", False)],
            "explanation": ("The clues 'not final' and 'meant to be revisited' show the decision was "
                            "temporary. 'Permanent' is the opposite. Pro tip: let the sentence define the "
                            "word -- here, 'not final' hands you the meaning."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Dr. Owusu's lab notebook is remarkably ______: every measurement is recorded "
                     "with the date, time, and exact conditions of the experiment.\"\n\n"
                     "Which choice completes the text with the most logical and precise word?"),
            "difficulty": 2,
            "choices": [("meticulous", True), ("outdated", False), ("brief", False), ("confusing", False)],
            "explanation": ("Recording every measurement with full detail shows great care, so 'meticulous' "
                            "(careful and precise) fits. 'Brief' contradicts all that detail. Pro tip: the "
                            "part after the colon explains the blank -- match the word to it."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Far from being ______, the senator's speech was packed with concrete proposals "
                     "and specific figures.\"\n\n"
                     "Which choice completes the text with the most logical and precise word?"),
            "difficulty": 2,
            "choices": [("vague", True), ("detailed", False), ("lengthy", False), ("honest", False)],
            "explanation": ("'Far from being' signals a contrast, so the blank is the opposite of 'concrete "
                            "proposals and specific figures' -- that is, 'vague.' The trap 'detailed' is the "
                            "very opposite of what 'far from' requires. Pro tip: 'far from' flips the meaning."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Because the evidence against the company was ______, the jury reached a "
                     "guilty verdict in under an hour.\"\n\n"
                     "Which choice completes the text with the most logical and precise word?"),
            "difficulty": 2,
            "choices": [("overwhelming", True), ("ambiguous", False), ("missing", False), ("recent", False)],
            "explanation": ("A verdict reached 'in under an hour' implies the evidence was strong and "
                            "convincing -- 'overwhelming.' 'Ambiguous' or 'missing' would slow a jury down. "
                            "Pro tip: the result (a fast verdict) tells you the cause (strong evidence)."),
        },
        # -- Text Structure & Purpose --
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Honeybee populations have declined sharply over the past two decades. This trend "
                     "is alarming because bees pollinate roughly a third of the crops humans eat. "
                     "Researchers are now racing to identify the cause.\"\n\n"
                     "Which choice best describes the function of the second sentence in the text overall?"),
            "difficulty": 2,
            "choices": [("It explains why the decline mentioned in the first sentence matters.", True),
                        ("It offers a solution to the problem.", False),
                        ("It questions the accuracy of the first sentence.", False),
                        ("It introduces a new and unrelated topic.", False)],
            "explanation": ("The second sentence gives the reason the decline is 'alarming' -- its "
                            "significance. It doesn't solve, doubt, or change the subject. Pro tip: ask what "
                            "the sentence DOES (here, explains importance), not just what it says."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"At first, the team assumed the strange readings were equipment errors. Only after "
                     "months of rechecking did they realize the data were correct -- and that they had "
                     "stumbled onto something entirely new.\"\n\n"
                     "Which choice best describes the overall structure of the text?"),
            "difficulty": 2,
            "choices": [("It moves from an initial assumption to an unexpected realization.", True),
                        ("It lists several unrelated discoveries in time order.", False),
                        ("It compares two competing scientific theories.", False),
                        ("It defines a term and then gives examples of it.", False)],
            "explanation": ("The text starts with what the team first assumed (errors) and ends with what "
                            "they finally realized (a discovery) -- a shift from assumption to realization. "
                            "Pro tip: track the turn signaled by 'At first… Only after.'"),
        },
        # -- Cross-Text Connections --
        {
            "text": ("Read the two texts, then answer.\n\n"
                     "Text 1: \"Remote work boosts productivity. Freed from commutes and constant office "
                     "interruptions, employees focus better and get more done.\"\n\n"
                     "Text 2: \"Although remote workers do report fewer interruptions, studies find that "
                     "collaboration and the mentoring of junior staff suffer when teams rarely meet in "
                     "person.\"\n\n"
                     "Based on the texts, how would the author of Text 2 most likely respond to the claim "
                     "in Text 1?"),
            "difficulty": 3,
            "choices": [("By agreeing that focus improves but noting a downside Text 1 overlooks", True),
                        ("By fully agreeing that remote work has no drawbacks", False),
                        ("By denying that remote workers face fewer interruptions", False),
                        ("By arguing that commuting itself improves productivity", False)],
            "explanation": ("Text 2 concedes the fewer-interruptions point ('Although remote workers do "
                            "report fewer interruptions') but adds that collaboration and mentoring suffer -- "
                            "a downside Text 1 ignored. Pro tip: 'Although' marks a partial agreement plus a "
                            "counterpoint."),
        },
        # ===================== INFORMATION & IDEAS (~26%) =====================
        # -- Central Ideas & Details --
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The Sahara was not always a desert. Cave paintings show people swimming, and "
                     "fossilized riverbeds wind beneath the sand. Just six thousand years ago, the region "
                     "was green, dotted with lakes and grasslands.\"\n\n"
                     "Which choice best states the main idea of the text?"),
            "difficulty": 2,
            "choices": [("The Sahara was once a much greener, wetter place than it is today.", True),
                        ("People have always lived in the Sahara Desert.", False),
                        ("Cave paintings can be found across Africa.", False),
                        ("Deserts are difficult environments to study.", False)],
            "explanation": ("Every detail -- swimmers, riverbeds, lakes, grasslands -- supports one point: "
                            "the Sahara used to be green and wet. The other choices are off-topic or not "
                            "stated. Pro tip: the main idea must cover ALL the details, not just one."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The Sahara was not always a desert. Cave paintings show people swimming, and "
                     "fossilized riverbeds wind beneath the sand. Just six thousand years ago, the region "
                     "was green, dotted with lakes and grasslands.\"\n\n"
                     "According to the text, which evidence suggests the Sahara was once green?"),
            "difficulty": 1,
            "choices": [("Cave paintings of swimmers and fossilized riverbeds", True),
                        ("Modern satellite photographs", False),
                        ("Written records from ancient cities", False),
                        ("The region's current climate", False)],
            "explanation": ("The text directly names the cave paintings of swimmers and the fossilized "
                            "riverbeds as the evidence. The others are never mentioned. Pro tip: for a "
                            "detail question, point to the exact words in the passage."),
        },
        # -- Command of Evidence (textual) --
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"A researcher hypothesizes that access to nearby parks reduces stress for city "
                     "residents.\"\n\n"
                     "Which finding, if true, would most directly support the researcher's hypothesis?"),
            "difficulty": 2,
            "choices": [("Residents living within a short walk of a park report lower stress than those living farther away.", True),
                        ("City parks are expensive for local governments to maintain.", False),
                        ("Many people enjoy looking at photographs of nature.", False),
                        ("Parks tend to attract more visitors on weekends.", False)],
            "explanation": ("The hypothesis links park access to lower stress, so evidence comparing stress "
                            "by distance to a park is directly on point. Cost, photos, and weekend crowds are "
                            "true-but-irrelevant. Pro tip: the best evidence speaks to THIS claim, not the "
                            "general topic."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Some educators claim that students build vocabulary more effectively by reading "
                     "widely than by memorizing word lists.\"\n\n"
                     "Which finding, if true, would most strongly support this claim?"),
            "difficulty": 2,
            "choices": [("Students who read widely scored higher on vocabulary tests than students who only memorized lists.", True),
                        ("Word lists are quick and easy to create.", False),
                        ("Reading is an enjoyable activity for many students.", False),
                        ("Some students dislike memorizing anything.", False)],
            "explanation": ("The claim compares two methods, so a study comparing their vocabulary outcomes "
                            "supports it directly. The other choices are about convenience or enjoyment, not "
                            "effectiveness. Pro tip: a comparison claim needs comparison evidence."),
        },
        # -- Command of Evidence (quantitative) --
        {
            "text": ("Read the text, then answer.\n\n"
                     "A study measured average daily screen time and average nightly sleep for four groups "
                     "of teenagers:\n\n"
                     "2 hours of screen time -- 8.5 hours of sleep\n"
                     "4 hours of screen time -- 7.8 hours of sleep\n"
                     "6 hours of screen time -- 7.0 hours of sleep\n"
                     "8 hours of screen time -- 6.3 hours of sleep\n\n"
                     "Which choice best uses the data to support the conclusion that more screen time is "
                     "associated with less sleep?"),
            "difficulty": 3,
            "choices": [("As screen time rises from 2 to 8 hours, average sleep falls from 8.5 to 6.3 hours.", True),
                        ("Teens with 2 hours of screen time slept 8.5 hours.", False),
                        ("Both screen time and sleep were measured in hours.", False),
                        ("Teenagers generally need a lot of sleep.", False)],
            "explanation": ("The conclusion is about a trend, so the support must describe the whole "
                            "downward pattern -- more screen time, less sleep. A single data point (8.5 "
                            "hours) doesn't show the association by itself. Pro tip: to support a trend, cite "
                            "the trend, not one row."),
        },
        {
            "text": ("Read the text and bar graph, then answer.\n\n"
                     "A city's sustainability report claims that, among the four materials shown, paper is "
                     "recycled at more than twice the rate of any other material.\n\n"
                     "[[figure:bar_recycling|Recycling rate by material (%)]]\n\n"
                     "Which choice best uses data from the graph to support this claim?"),
            "difficulty": 3,
            "choices": [("Paper is recycled at 68%, while no other material shown exceeds 31%.", True),
                        ("Plastic is recycled at only 9%, the lowest rate shown.", False),
                        ("Glass and metal have fairly similar recycling rates.", False),
                        ("Metal is recycled at a higher rate than plastic.", False)],
            "explanation": ("The claim compares paper to the others, so the support must put paper's 68% "
                            "against the next-highest rate, glass at 31% (and 68 is more than twice 31). The "
                            "other choices state true numbers that never address the comparison. Pro tip: "
                            "support a comparison claim with the two numbers being compared."),
        },
        {
            "text": ("Read the text and line graph, then answer.\n\n"
                     "A student writes that global solar capacity grew dramatically over the decade shown.\n\n"
                     "[[figure:line_solar|Global solar capacity, 2011-2021]]\n\n"
                     "Which choice most effectively uses data from the graph to support this statement?"),
            "difficulty": 2,
            "choices": [("Global solar capacity rose from about 70 gigawatts in 2011 to about 850 gigawatts in 2021.", True),
                        ("Global solar capacity was about 70 gigawatts in 2011.", False),
                        ("Global solar capacity changed between 2011 and 2021.", False),
                        ("Solar capacity grew faster than wind capacity over this period.", False)],
            "explanation": ("To support 'grew dramatically,' cite both endpoints so the size of the rise is "
                            "clear (about 70 to 850 GW). A single year is incomplete, 'changed' is too vague, "
                            "and wind capacity is not on the graph. Pro tip: to prove growth, give the before "
                            "and after numbers."),
        },
        {
            "text": ("Read the line graph, then answer.\n\n"
                     "[[figure:line_solar|Global solar capacity, 2011-2021]]\n\n"
                     "Which statement is best supported by the graph?"),
            "difficulty": 2,
            "choices": [("Global solar capacity increased across every interval shown from 2011 to 2021.", True),
                        ("Global solar capacity stayed flat after 2017.", False),
                        ("Global solar capacity peaked in 2015 and then declined.", False),
                        ("Global solar capacity was higher in 2011 than in 2013.", False)],
            "explanation": ("Each plotted point is higher than the one before, so capacity rose across every "
                            "interval. The other statements contradict the steadily rising line. Pro tip: for "
                            "'which is supported,' eliminate any choice the graph visibly contradicts."),
        },
        # -- Inferences --
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The deep-sea anglerfish lives where almost no sunlight reaches. To find prey in "
                     "this darkness, it dangles a glowing lure in front of its mouth. Any small fish drawn "
                     "to the light ______\"\n\n"
                     "Which choice most logically completes the text?"),
            "difficulty": 2,
            "choices": [("swims straight toward the anglerfish's waiting jaws.", True),
                        ("quickly loses interest and swims away.", False),
                        ("produces an even brighter light of its own.", False),
                        ("helps the anglerfish locate sunlight.", False)],
            "explanation": ("The lure exists to catch prey, so a fish drawn to the light ends up at the "
                            "anglerfish's mouth. The other options defeat the lure's stated purpose. Pro "
                            "tip: an inference follows the passage's own logic to its next step."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"For years, the bakery's signature bread relied on a recipe known only to its "
                     "founder, who never wrote it down. After she retired and moved abroad, the remaining "
                     "staff found that ______\"\n\n"
                     "Which choice most logically completes the text?"),
            "difficulty": 2,
            "choices": [("they could no longer reproduce the bakery's most famous bread.", True),
                        ("customers had always preferred a rival bakery.", False),
                        ("the recipe had been published online for years.", False),
                        ("the founder had secretly trained a replacement.", False)],
            "explanation": ("If only the founder knew the unwritten recipe and she left, the staff logically "
                            "can't make that bread. The other choices contradict the setup (an unwritten, "
                            "secret recipe). Pro tip: the inference must fit every clue, not just sound "
                            "dramatic."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The library replaced its dim lighting with bright lamps and added comfortable "
                     "chairs and quiet study pods. Within a month, the number of students using the "
                     "library after school ______\"\n\n"
                     "Which choice most logically completes the text?"),
            "difficulty": 1,
            "choices": [("had noticeably increased.", True),
                        ("had fallen to almost zero.", False),
                        ("remained exactly the same.", False),
                        ("was never recorded by staff.", False)],
            "explanation": ("Making the space brighter and more comfortable would draw more students, so a "
                            "noticeable increase follows. A drop or no change contradicts the improvements. "
                            "Pro tip: match the result to the cause the passage describes."),
        },
        # ===================== STANDARD ENGLISH CONVENTIONS (~26%) =====================
        # -- Boundaries (punctuation) --
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"My grandmother immigrated to the United States in 1955 ______ she still remembers "
                     "her first snowy winter in Chicago vividly.\""),
            "difficulty": 2,
            "choices": [("1955; she", True), ("1955, she", False), ("1955 she", False), ("1955: she", False)],
            "explanation": ("Both sides are complete sentences, so a semicolon correctly joins them. A comma "
                            "alone is a comma splice; no punctuation is a run-on; a colon wrongly signals an "
                            "explanation or list. Pro tip: two full sentences need a period, semicolon, or "
                            "comma + FANBOYS -- never a lone comma."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The recipe calls for just three ______ flour, sugar, and butter.\""),
            "difficulty": 2,
            "choices": [("ingredients:", True), ("ingredients,", False), ("ingredients;", False), ("ingredients", False)],
            "explanation": ("'The recipe calls for just three ingredients' is a complete sentence, and a "
                            "list follows, so a colon is correct. A semicolon needs a full sentence after it; "
                            "a comma or nothing leaves the list improperly attached. Pro tip: a complete "
                            "sentence + a list = colon."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The Great Barrier ______ the largest living structure on Earth, can be seen from "
                     "space.\""),
            "difficulty": 2,
            "choices": [("Reef, which is", True), ("Reef which is", False), ("Reef. Which is", False), ("Reef; which is", False)],
            "explanation": ("'which is the largest living structure on Earth' is nonessential information and "
                            "must be set off with a comma (matching the comma after 'Earth'). Starting a new "
                            "sentence or clause with 'Which' is a fragment. Pro tip: nonessential "
                            "descriptions get commas on both sides."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The three sisters opened a bakery together; the ______ recipes had been passed "
                     "down for generations.\""),
            "difficulty": 2,
            "choices": [("sisters'", True), ("sister's", False), ("sisters", False), ("sisters's", False)],
            "explanation": ("The recipes belong to more than one sister, so use the plural possessive "
                            "'sisters'' (apostrophe after the s). 'Sister's' is singular; 'sisters' is just "
                            "plural with no possession. Pro tip: plural noun ending in s -> add only an "
                            "apostrophe."),
        },
        # -- Form, Structure & Sense (grammar) --
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The museum's collection of ancient coins ______ displayed in a single locked "
                     "case.\""),
            "difficulty": 2,
            "choices": [("is", True), ("are", False), ("were", False), ("have been", False)],
            "explanation": ("The subject is 'collection' (singular), not 'coins,' so the singular verb 'is' "
                            "is correct. The plural-sounding 'coins' is just part of a prepositional phrase. "
                            "Pro tip: cross out the 'of …' phrase to find the real subject."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"Neither the head coach nor the players ______ aware that the game had been moved "
                     "to Friday.\""),
            "difficulty": 3,
            "choices": [("were", True), ("was", False), ("is", False), ("has been", False)],
            "explanation": ("With 'neither … nor,' the verb agrees with the nearer subject -- here 'players' "
                            "(plural) -- so 'were' is correct. The trap 'was' agrees with the farther, "
                            "singular 'coach.' Pro tip: for neither/nor, match the verb to whatever comes "
                            "right before it."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"By the time the firefighters arrived, the flames ______ already spread to the "
                     "second floor.\""),
            "difficulty": 2,
            "choices": [("had", True), ("have", False), ("has", False), ("will have", False)],
            "explanation": ("The spreading happened before the firefighters arrived (also past), so the "
                            "past perfect 'had spread' shows the earlier action. 'Have/has' are present "
                            "perfect; 'will have' is future. Pro tip: for the earlier of two past events, "
                            "use 'had + verb.'"),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"After reviewing its quarterly results, the company announced that ______ would "
                     "expand into three new markets.\""),
            "difficulty": 2,
            "choices": [("it", True), ("they", False), ("them", False), ("those", False)],
            "explanation": ("'Company' is a singular noun, so the singular pronoun 'it' agrees. 'They' and "
                            "'them' are plural and don't match. Pro tip: organizations (company, team, "
                            "committee) are singular -- use 'it.'"),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"Walking to school on the first chilly morning of fall, ______\""),
            "difficulty": 3,
            "choices": [("Jamal noticed that the leaves had begun to change color.", True),
                        ("the leaves had begun to change color, Jamal noticed.", False),
                        ("the changing leaves were noticed by Jamal.", False),
                        ("it seemed to Jamal that the leaves were changing.", False)],
            "explanation": ("The opening phrase describes someone walking, so the noun right after the comma "
                            "must be the walker -- Jamal. The other versions make 'the leaves' or 'it' do the "
                            "walking, a dangling modifier. Pro tip: after an '-ing' opener, name the doer "
                            "immediately."),
        },
        # ===================== EXPRESSION OF IDEAS (~20%) =====================
        # -- Transitions --
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"The first prototype failed every safety test. ______ the engineers refused to "
                     "give up and began redesigning it that same week.\""),
            "difficulty": 2,
            "choices": [("Nevertheless,", True), ("Therefore,", False), ("For example,", False), ("Similarly,", False)],
            "explanation": ("Failing the tests would normally stop a project, but the engineers pushed on -- "
                            "a contrast, so 'Nevertheless' fits. 'Therefore' implies the failure caused them "
                            "to continue, which reverses the logic. Pro tip: a surprising turn calls for a "
                            "contrast transition."),
        },
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"The bridge had not been inspected in over a decade. ______ engineers were not "
                     "surprised to find significant rust and structural cracks.\""),
            "difficulty": 2,
            "choices": [("Consequently,", True), ("However,", False), ("In contrast,", False), ("Nonetheless,", False)],
            "explanation": ("The long gap in inspections is the cause; the rust and cracks are the expected "
                            "result, so a cause-effect transition ('Consequently') fits. 'However' and 'In "
                            "contrast' wrongly signal opposition. Pro tip: cause then expected result = "
                            "'consequently/therefore.'"),
        },
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"Some animals can regrow lost body parts. ______ a starfish can regenerate an "
                     "entire arm, and certain species can rebuild a whole body from a single arm.\""),
            "difficulty": 1,
            "choices": [("For instance,", True), ("However,", False), ("In conclusion,", False), ("Therefore,", False)],
            "explanation": ("The starfish is a specific case of the general claim, so 'For instance' "
                            "introduces the example. 'However' signals contrast and 'In conclusion' signals "
                            "an ending, neither of which fits. Pro tip: a specific case after a general claim "
                            "= 'for example/for instance.'"),
        },
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"The director insisted the film was completely finished. ______ several key scenes "
                     "had not yet been shot.\""),
            "difficulty": 2,
            "choices": [("In fact,", True), ("Likewise,", False), ("For example,", False), ("Therefore,", False)],
            "explanation": ("The second sentence corrects and intensifies against the director's claim, so "
                            "'In fact' fits. 'Likewise' signals similarity and 'Therefore' signals a result, "
                            "both of which miss the contradiction. Pro tip: 'in fact' sharpens or corrects "
                            "the previous statement."),
        },
        # -- Rhetorical Synthesis --
        {
            "text": ("While researching a topic, a student took the following notes:\n\n"
                     "- The axolotl is a salamander native to lakes near Mexico City.\n"
                     "- Unlike most amphibians, it keeps its larval features for its entire life.\n"
                     "- It can regenerate lost limbs, parts of its heart, and even portions of its brain.\n"
                     "- It is critically endangered in the wild.\n\n"
                     "The student wants to emphasize the axolotl's unusual regenerative ability. Which "
                     "choice most effectively uses relevant information from the notes to accomplish this "
                     "goal?"),
            "difficulty": 2,
            "choices": [("The axolotl can regenerate not only lost limbs but even parts of its heart and brain.", True),
                        ("The axolotl is a salamander native to lakes near Mexico City.", False),
                        ("The axolotl is critically endangered in the wild.", False),
                        ("Unlike most amphibians, the axolotl keeps its larval features for life.", False)],
            "explanation": ("Only the first choice is about regeneration, which is the stated goal. The "
                            "others are true notes but emphasize habitat, conservation status, or life cycle "
                            "instead. Pro tip: match the sentence to the GOAL, not just to a true fact."),
        },
        {
            "text": ("While researching a topic, a student took the following notes:\n\n"
                     "- Solar power is electricity generated from sunlight.\n"
                     "- In 2010, solar provided only a tiny share of global electricity.\n"
                     "- By 2023, solar had become one of the fastest-growing energy sources in the world.\n"
                     "- The cost of solar panels fell roughly 80% between 2010 and 2020.\n\n"
                     "The student wants to emphasize how quickly solar power has grown. Which choice most "
                     "effectively uses relevant information from the notes to accomplish this goal?"),
            "difficulty": 2,
            "choices": [("Once only a tiny share of global electricity in 2010, solar had become one of the world's fastest-growing energy sources by 2023.", True),
                        ("Solar power is electricity that is generated from sunlight.", False),
                        ("Solar power depends on the availability of sunlight.", False),
                        ("Solar panels are manufactured from a variety of materials.", False)],
            "explanation": ("The goal is to stress rapid growth, and the first choice contrasts 2010 with "
                            "2023 to show exactly that. The others merely define solar power and ignore the "
                            "growth. Pro tip: to show change, pick the choice that contrasts 'before' and "
                            "'after.'"),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the 'SAT Reading & Writing: Complete Course & Test Prep' course (MCQ only)."

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

        # The modern SAT has no essay, so no written-response prompts are seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
