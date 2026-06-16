"""
Enrich lesson content for the course with slug "sat-reading-writing-complete".
Each lesson is updated by (course__slug, order) so the command is idempotent.

Run:
    python manage.py enrich_sat_rw_complete
"""
from django.core.management.base import BaseCommand
from courses.models import Lesson


LESSONS = [
    (
        1,
        # ── Lesson 1: How the Digital SAT Reading & Writing Works ─────────────
        "**How the Digital SAT Reading & Writing Works**\n\n"

        "**The format at a glance**\n"
        "The digital SAT Reading & Writing section is divided into **two adaptive modules**, each containing approximately 27 questions with a 32-minute time limit. That gives you 54 questions across 64 minutes total — just over **1.1 minutes per question**. Unlike the old paper SAT, there are no long passages with several questions attached. Every question on the digital SAT comes paired with its own short passage of 25 to 150 words, and you answer exactly one question about it before moving on.\n\n"

        "**The four domains**\n"
        "All Reading & Writing questions belong to one of four content domains. Knowing the domains lets you recognize the type of thinking each question requires before you even read the passage:\n\n"
        "- **Craft & Structure (~28%)** — vocabulary in context, text structure and purpose, cross-text connections\n"
        "- **Information & Ideas (~26%)** — central ideas and details, command of evidence (textual and quantitative), inferences\n"
        "- **Standard English Conventions (~26%)** — sentence boundaries (punctuation), grammar (form, structure, and sense)\n"
        "- **Expression of Ideas (~20%)** — transitions, rhetorical synthesis\n\n"

        "**How adaptive scoring works**\n"
        "Module 1 contains a mix of easy, medium, and hard questions. Your performance on Module 1 determines the difficulty level of Module 2: strong performance routes you to a harder Module 2, while weaker performance routes you to an easier one. **Both modules count toward your final score.** A harder Module 2 gives you access to higher scores; an easier one caps your potential. This means every question in Module 1 matters — there are no throwaway items.\n\n"

        "**Sample passage and question type preview**\n"
        "\"Migratory birds navigate using multiple systems simultaneously: the position of the sun, the pattern of stars, the Earth's magnetic field, and even smell. Researchers have found that disrupting any single system rarely causes birds to become completely lost, suggesting that these navigation tools function as overlapping backups rather than a single primary mechanism.\"\n\n"
        "This 54-word passage would be paired with exactly one question — for example, a Words in Context question asking what \"overlapping\" most nearly means, or an inference question asking what the passage most logically implies about bird navigation. You will never be asked two questions about the same short passage.\n\n"

        "**Two golden rules for every question**\n"
        "Rule 1: **The answer is in the passage.** The digital SAT is an open-book test. Every correct answer is directly supported by the text you are given. Outside knowledge, personal opinions, or facts you remember from science class do not belong in your reasoning.\n\n"
        "Rule 2: **Predict before you read the choices.** Before you look at the four answer options, form your own answer in plain language. Students who predict first are far less likely to be seduced by attractive wrong answers that are designed to sound plausible.\n\n"

        "**How to pace yourself**\n"
        "At 1.1 minutes per question, you cannot afford to stall. A reliable routine: (1) read the question stem to know what job you are doing, (2) skim the passage for structure, (3) read only what you need to answer the question, (4) predict your answer, (5) match it to the best choice. If a question takes more than 90 seconds, make your best guess, flag it, and return at the end.\n\n"

        "**No penalty for wrong answers**\n"
        "The digital SAT does not deduct points for incorrect answers. A blank is always strictly worse than a guess. If you are truly stuck after eliminating two choices, pick between the remaining two and move on. Never leave a question blank.\n\n"

        "⚠️ Common mistake: treating the digital SAT like the old paper SAT and expecting to read long passages. Students who try to read the short passage too deeply before checking what the question actually asks waste time and often over-think simple questions. Read the stem first — always.\n\n"

        "💡 Tip: write the domain abbreviation next to each question stem as you practice (C&S, I&I, SEC, EI). After a few weeks you will recognize the domain instantly, and that recognition alone tells you which mental strategy to apply before you read a single word of the passage."
    ),
    (
        2,
        # ── Lesson 2: Craft & Structure I: Words in Context ───────────────────
        "**Craft & Structure I: Words in Context**\n\n"

        "**What the question asks**\n"
        "Words in Context questions appear in two forms. The first asks: \"As used in the text, what does [word] most nearly mean?\" The second presents a blank in the passage and asks: \"Which choice completes the text with the most logical and precise word or phrase?\" Both forms test the same skill — using the surrounding context to determine the precise meaning or the best fit, not the most common dictionary definition.\n\n"

        "**The 3-step method**\n"
        "Step 1 — **Remove the word (or ignore the blank)** and read the sentence and the one or two sentences around it. Ask: what idea must fill this gap for the sentence to make logical sense?\n\n"
        "Step 2 — **Predict your own replacement word** based entirely on the context clues in the passage. Write it mentally (or on your scratch paper) before looking at the choices.\n\n"
        "Step 3 — **Match your prediction to the answer choice** that is closest in both meaning and connotation. Plug that choice back into the sentence and confirm it reads naturally and precisely.\n\n"

        "**Context clue signals**\n"
        "Two types of signal words dramatically narrow the prediction:\n\n"
        "- **Contrast signals** (but, however, far from, unlike, yet, although, while) tell you the answer is the *opposite* of a nearby idea. If the sentence reads \"Far from being ______, the scientist's explanation was surprisingly accessible,\" the blank must mean something like \"complicated\" because the contrast clue \"far from\" flips the meaning of what follows.\n"
        "- **Cause signals** (because, since, so, therefore, as a result) tell you the answer is the *result or cause* of a nearby idea. \"Because the funding was ______, the research team had to cancel three planned experiments\" needs a word that explains a financial shortfall — something like \"insufficient\" or \"depleted.\"\n\n"

        "**Connotation: the hidden layer**\n"
        "Two words can share a denotation (literal meaning) yet carry very different connotations (emotional weight). \"Persistent\" and \"stubborn\" both mean continuing despite obstacles, but \"persistent\" is admiring and \"stubborn\" is critical. \"Frugal\" and \"miserly\" both involve spending little money, but one is praised and the other condemned. The SAT frequently puts a denotation-match as a wrong answer to catch readers who stop at the surface meaning.\n\n"

        "**Sample passage**\n"
        "\"For centuries, philosophers debated whether moral intuition was a reliable guide to ethical action or merely a reflection of cultural conditioning. Contemporary neuroscientists have complicated this picture further: brain-imaging studies show that moral judgments engage both rapid, automatic emotional responses and slower, deliberate reasoning processes. The finding suggests that intuition is neither purely trustworthy nor entirely ______, but rather a starting point that careful reflection can refine.\"\n\n"

        "**Worked example**\n"
        "Question: Which choice completes the text with the most logical and precise word?\n\n"
        "(A) irrelevant — The passage says intuition is \"a starting point that careful reflection can refine,\" which means it has some value. If it were entirely irrelevant, there would be no starting point to refine. The contrast structure \"neither trustworthy nor ______\" needs a negative word, but \"irrelevant\" goes too far — the passage never dismisses intuition entirely. Eliminate.\n\n"
        "(B) accurate — \"Accurate\" is positive, and the \"nor\" requires a negative word (the opposite of \"trustworthy\"). An accurate intuition would be trustworthy. This confuses the direction of the contrast. Eliminate.\n\n"
        "(C) dismissible — This fits the structure. The passage argues intuition is neither fully trustworthy nor something that can be wholly set aside (dismissible). The refinement process implies it has partial value. This is the correct answer.\n\n"
        "(D) logical — \"Logical\" is a positive quality and does not complete the contrast with \"trustworthy.\" If both sides of the \"neither/nor\" were positive, the sentence would not make sense as a contrast. Eliminate.\n\n"

        "⚠️ Common mistake: choosing the most familiar or \"dictionary-default\" meaning of the target word rather than the meaning the passage context requires. The SAT deliberately includes the everyday meaning as a wrong answer. For the word \"table,\" a student who defaults to the furniture definition will miss that in a political context it means \"postpone.\"\n\n"

        "💡 Tip: before looking at the choices, cover them with your hand and say your prediction aloud (or write it). The single most effective habit for Words in Context questions is committing to a prediction before the choices can influence you. Students who skip this step choose attractive wrong answers at a much higher rate."
    ),
    (
        3,
        # ── Lesson 3: Craft & Structure II: Structure, Purpose & Cross-Text ───
        "**Craft & Structure II: Text Structure, Purpose & Cross-Text Connections**\n\n"

        "**Text structure: the five patterns**\n"
        "Text Structure questions ask how a passage is organized, not just what it is about. The five patterns you will encounter most often are:\n\n"
        "- **Problem-Solution**: the author identifies a crisis or need, then presents one or more responses or fixes\n"
        "- **Cause-Effect**: the author traces what causes something or what results from a given cause\n"
        "- **Compare-Contrast**: two or more subjects are placed side by side to highlight similarities or differences\n"
        "- **Chronological**: events or developments are presented in the order they occurred\n"
        "- **General-to-Specific**: a broad claim or observation is followed by increasingly detailed evidence or examples\n\n"

        "**Author's purpose: what the text is doing, not saying**\n"
        "Purpose questions ask why the author wrote something: to **inform**, to **persuade**, to **challenge** a prevailing view, or to **describe**. They also ask about the function of a single sentence or paragraph within the whole passage — for example, \"What is the function of the second paragraph?\"\n\n"
        "The key move: shift from *what* the text says to *why* the author included it. A sentence that mentions a historical failure is not just providing information — it might be providing evidence for a claim, illustrating a counterexample, or creating contrast with a present-day success.\n\n"

        "**Transition words identify structure**\n"
        "Transition words are the fastest clue to an author's organizational logic:\n\n"
        "- \"However,\" \"in contrast,\" \"yet,\" \"while\" → **contrast or compare-contrast**\n"
        "- \"As a result,\" \"therefore,\" \"consequently,\" \"because\" → **cause-effect**\n"
        "- \"For example,\" \"specifically,\" \"in particular\" → **general-to-specific**\n"
        "- \"First... then... finally\" → **chronological**\n"
        "- \"In response,\" \"one solution,\" \"to address this\" → **problem-solution**\n\n"

        "**Sample passage (structure)**\n"
        "\"Urban heat islands form when cities replace natural surfaces — soil, trees, water — with concrete and asphalt that absorb and retain solar energy. In Phoenix, summer surface temperatures regularly exceed those of the surrounding desert by more than 20 degrees Fahrenheit. The consequences extend beyond discomfort: hospital admissions for heat-related illness spike during heat events, and peak electricity demand strains grids to the breaking point. Researchers have proposed several mitigation strategies, including cool roofs coated with reflective paint, expanded tree canopies along major corridors, and permeable pavements that allow water to cool surfaces through evaporation. Each strategy is technically feasible; the obstacle is coordinating policy and funding across dozens of independent municipal agencies.\"\n\n"

        "This passage follows a **problem-solution** structure: sentences 1-3 define the problem (heat islands and their consequences), sentences 4-5 present solutions, and the final sentence identifies the real obstacle.\n\n"

        "**Cross-text connections: the mapping strategy**\n"
        "Cross-Text questions give you two short passages on the same topic and ask how they relate — usually \"How would the author of Text 2 most likely respond to the claim in Text 1?\" The method:\n\n"
        "Step 1 — After reading both texts, write one sentence summarizing each author's main claim before reading the questions.\n"
        "Step 2 — Identify one point of **agreement** and one point of **disagreement** between the two authors.\n"
        "Step 3 — When answering a response question, stay strictly inside what Author 2 actually says. Do not invent a response that sounds logical but goes beyond the text.\n\n"

        "**Paired passage example**\n"
        "Text 1: \"Standardized testing provides the only consistent, objective measure of academic readiness available to college admissions officers. Without it, decisions rest entirely on grades that vary widely in meaning across thousands of different schools.\"\n\n"
        "Text 2: \"Standardized test scores correlate strongly with family income, giving wealthier students — who can afford expensive preparation courses — a systematic advantage that has nothing to do with intellectual potential.\"\n\n"
        "Author 1's claim: standardized tests are the only consistent objective measure. Author 2's claim: test scores reflect income more than potential. They agree that tests measure something consistently; they disagree about whether that something is meaningful or fair.\n\n"

        "⚠️ Common mistake: confusing what a sentence *says* with what it *does*. A question that asks for a paragraph's \"function\" wants the purpose (\"it provides a counterexample to the previous claim\"), not a summary of its content (\"it talks about Phoenix summers\"). Practice asking \"what work is this doing?\" for every sentence you read.\n\n"

        "💡 Tip: for every Cross-Text question, physically write Author 1 = [one word] and Author 2 = [one word] before reading the answer choices. This two-word map takes ten seconds and prevents the most common error — confusing which author said what."
    ),
    (
        4,
        # ── Lesson 4: Information & Ideas I: Central Ideas & Evidence ─────────
        "**Information & Ideas I: Central Ideas & Evidence**\n\n"

        "**Central idea questions: the whole, not a part**\n"
        "A central idea question asks: \"Which choice best states the main idea of the text?\" or \"Which choice most accurately summarizes the text?\" The correct answer must cover the **entire** passage — not one detail, not one paragraph, not one example. The most common wrong answers are:\n\n"
        "- **Too narrow**: accurately describes one sentence or one detail, but the passage covers much more\n"
        "- **Too broad**: goes beyond what the passage actually claims, attributing to the author a grand conclusion the text never states\n"
        "- **Contradicts text**: states the opposite of what the passage says\n\n"
        "To find the main idea, ask: \"What single sentence could I write that every paragraph in this passage serves to support?\"\n\n"

        "**Sample passage**\n"
        "\"Before the invention of artificial refrigeration in the 19th century, ice was a luxury commodity harvested from frozen lakes in winter and shipped to warmer climates. The ice trade required enormous logistical infrastructure: insulated warehouses, specialized transport, and a labor force that worked in extreme cold. Despite these costs, ice became essential to restaurants, hospitals, and breweries in cities as far south as Havana and Calcutta. The trade collapsed almost overnight when mechanical refrigeration became commercially available in the 1880s, displacing thousands of workers and rendering the entire supply chain obsolete. The ice trade is a striking example of how a single technological innovation can simultaneously create and destroy entire industries and the communities built around them.\"\n\n"

        "**Central idea worked example**\n"
        "Question: Which choice best states the main idea of the passage?\n\n"
        "(A) Ice was harvested from frozen lakes and shipped to warm climates before refrigeration existed.\n"
        "This is a true detail from the passage (sentences 1-2), but it does not cover the passage's larger argument about technological disruption. Too narrow. Eliminate.\n\n"
        "(B) The ice trade illustrates how a technological innovation can simultaneously create and destroy industries.\n"
        "This is the main claim — stated explicitly in the final sentence and supported by every earlier detail. Correct.\n\n"
        "(C) Mechanical refrigeration was invented in the 1880s and improved food safety worldwide.\n"
        "The passage does not discuss food safety improvements from refrigeration. This goes beyond what the text states. Too broad/contradicts text. Eliminate.\n\n"
        "(D) The ice trade required expensive infrastructure that made it unsustainable long-term.\n"
        "The passage says the ice trade collapsed not because of costs but because of technological replacement. This misidentifies the cause. Contradicts the text. Eliminate.\n\n"

        "**Textual evidence: match the claim to the quote**\n"
        "Command of Evidence (textual) questions give you a claim and ask: \"Which quote from the passage most directly supports this claim?\" The wrong answer traps are:\n\n"
        "- **Related topic but wrong claim**: the quote is about the same subject but supports a different point\n"
        "- **Too vague**: the quote is generally relevant but does not speak directly to the specific claim\n"
        "- **Opposite direction**: the quote actually weakens the claim rather than supports it\n\n"
        "To find the correct evidence, first restate the claim in your own plain words, then test each quote: does this quote, and only this quote, make the claim more convincing? The best evidence is the most **specific and direct**.\n\n"

        "**Evidence worked example**\n"
        "Claim: the ice trade's workforce was large enough that its displacement was significant.\n\n"
        "(A) \"ice became essential to restaurants, hospitals, and breweries\" — This is about who used ice, not about the size of the workforce. Does not support the claim. Eliminate.\n\n"
        "(B) \"displacing thousands of workers and rendering the entire supply chain obsolete\" — The word \"thousands\" directly speaks to scale, and \"displacing\" speaks to impact. This is the most direct support. Correct.\n\n"
        "(C) \"The trade collapsed almost overnight\" — This describes speed, not workforce size. Related but not about the claim. Eliminate.\n\n"
        "(D) \"a single technological innovation can simultaneously create and destroy entire industries\" — This is the passage's main idea statement, not specific evidence about labor displacement. Eliminate.\n\n"

        "⚠️ Common mistake: choosing an evidence quote because it is interesting or because it is about the same topic as the claim, rather than because it directly and specifically supports the exact claim being made. \"Related topic\" is not the same as \"supports this specific claim.\"\n\n"

        "💡 Tip: for evidence questions, convert the claim into a simple yes/no test. For each quote, ask: \"If someone doubted the claim, would reading this quote change their mind?\" The quote that best answers \"yes\" is the correct evidence."
    ),
    (
        5,
        # ── Lesson 5: Information & Ideas II: Data & Inferences ───────────────
        "**Information & Ideas II: Quantitative Evidence & Inferences**\n\n"

        "**Quantitative evidence: text plus table or graph**\n"
        "Command of Evidence (quantitative) questions pair a short passage with a table, bar chart, or line graph. You are asked to choose the statement that **accurately uses the data** to accomplish a stated purpose — usually to support a claim in the passage or to complete an example. Two types of errors trap students:\n\n"
        "- **Accurate but irrelevant**: the choice states a true data value but does not speak to the specific claim being made\n"
        "- **Inaccurate**: the choice misstates or misreads the data\n\n"
        "Always read the table's **title, column labels, and units** before reading the passage or the questions. Sixty seconds spent orienting yourself to the data saves time and prevents misreads.\n\n"

        "**Sample data table**\n"
        "A researcher studying exercise habits recorded the following average weekly exercise times and corresponding average systolic blood pressure readings for five age groups:\n\n"
        "- Ages 20-29: 5.2 hours/week exercise, 118 mmHg blood pressure\n"
        "- Ages 30-39: 4.6 hours/week exercise, 122 mmHg blood pressure\n"
        "- Ages 40-49: 3.9 hours/week exercise, 128 mmHg blood pressure\n"
        "- Ages 50-59: 3.1 hours/week exercise, 135 mmHg blood pressure\n"
        "- Ages 60-69: 2.5 hours/week exercise, 141 mmHg blood pressure\n\n"
        "The passage states: \"The data suggest that higher levels of weekly exercise are associated with lower systolic blood pressure across all age groups studied.\"\n\n"

        "**Quantitative evidence worked example**\n"
        "Question: Which choice most effectively uses data from the table to support the passage's claim?\n\n"
        "(A) The 20-29 age group exercises an average of 5.2 hours per week.\n"
        "This states a single data point from one age group. It does not show the relationship between exercise and blood pressure, and it does not compare groups. Does not support the trend claim. Eliminate.\n\n"
        "(B) As average weekly exercise decreases from 5.2 hours in the 20-29 age group to 2.5 hours in the 60-69 age group, average blood pressure rises from 118 to 141 mmHg.\n"
        "This cites both the exercise trend and the blood pressure trend across the full range of the data, directly demonstrating the inverse relationship the claim describes. Correct.\n\n"
        "(C) Participants in their 60s had the highest blood pressure of any group in the study.\n"
        "This is accurate but it says nothing about the role of exercise. A reader would still not know whether exercise, age, or something else explains the difference. Eliminate.\n\n"
        "(D) Exercise habits and blood pressure were measured in the same study.\n"
        "This is a methodological fact, not evidence of a relationship. It does not support the specific association being claimed. Eliminate.\n\n"

        "**Inferences: the least-added-assumption rule**\n"
        "Inference questions end a passage mid-thought and ask: \"Which choice most logically completes the text?\" The correct answer is the conclusion the passage's premises most directly point toward — with the **fewest added assumptions**. A wrong answer either over-infers (goes further than the evidence allows) or under-infers (states something too weak to count as a conclusion).\n\n"
        "To test a potential inference: ask \"Does the passage explicitly state or clearly imply every step needed to reach this conclusion?\" If you need to assume something the passage never mentions, the inference is too strong.\n\n"

        "**Inference worked example**\n"
        "\"A team of ornithologists studying songbird populations in fragmented forests found that species requiring large continuous territories showed the steepest population declines. Species that tolerate smaller, isolated patches of habitat maintained stable populations even as development reduced total forest coverage. The researchers concluded that habitat fragmentation affects bird species ______\"\n\n"
        "(A) equally, regardless of their territorial requirements — Contradicts the data, which showed different species responded differently. Eliminate.\n\n"
        "(B) in ways that depend on each species' territorial range and tolerance for habitat fragmentation — Directly follows from the two-finding structure: large-territory species declined, fragment-tolerant species did not. No assumptions added. Correct.\n\n"
        "(C) only when total forest coverage drops below fifty percent — The passage gives no threshold or percentage. This specific claim is not supported by the data given. Over-inference. Eliminate.\n\n"
        "(D) permanently, because fragmented habitat cannot be restored — The passage says nothing about restoration or permanence. This adds an entirely new claim. Eliminate.\n\n"

        "⚠️ Common mistake: over-inferring. If the passage supports \"the lights probably helped,\" do not choose \"the lights guaranteed success.\" The word \"probably\" in a passage signals limited inference; \"guaranteed\" requires certainty the text never provides.\n\n"

        "💡 Tip: for every inference question, point to the specific words in the passage that justify the conclusion. If you cannot point to them, the answer is a guess, not an inference. The correct answer will always have a textual anchor you can cite."
    ),
    (
        6,
        # ── Lesson 6: Standard English Conventions I: Boundaries ──────────────
        "**Standard English Conventions I: Sentence Boundaries**\n\n"

        "**What the question asks**\n"
        "Boundaries questions test whether you can correctly join, separate, and punctuate ideas. Every question uses the same stem: \"Which choice completes the text so that it conforms to the conventions of Standard English?\" The four answer choices show different punctuation marks in the same location. Your job is to identify the grammatical relationship between the ideas on each side of the punctuation mark, then choose the mark that correctly expresses that relationship.\n\n"

        "**The foundation: independent vs. dependent clauses**\n"
        "An **independent clause** (IC) has a subject, a finite verb, and expresses a complete thought. It can stand alone as a sentence. A **dependent clause** has a subject and verb but begins with a subordinating word (because, although, when, which, that) and cannot stand alone.\n\n"
        "Recognizing whether each side of a punctuation mark is an IC is the single most important Boundaries skill.\n\n"

        "**The rules for joining two independent clauses**\n"
        "When you have two ICs, you have exactly three correct options:\n\n"
        "- **Period**: The proposal was rejected. The team revised it.\n"
        "- **Semicolon (;)**: The proposal was rejected; the team revised it.\n"
        "- **Comma + FANBOYS**: The proposal was rejected, but the team revised it.\n\n"
        "The seven FANBOYS coordinating conjunctions are: **for, and, nor, but, or, yet, so**.\n\n"
        "A **comma alone** between two ICs is always wrong — this is called a **comma splice**. A **semicolon** followed by a coordinating conjunction (e.g., \"; but\") is also wrong.\n\n"

        "**Fragments and run-ons**\n"
        "A **fragment** is a group of words punctuated as a sentence but missing a subject, a finite verb, or a complete thought. Common fragment traps: a dependent clause alone (\"Because the funding was cut.\") or a participial phrase alone (\"Having reviewed the data.\").\n\n"
        "A **run-on** is two ICs with no punctuation between them at all.\n\n"

        "**Correction examples**\n"
        "Before: \"The bridge was designed in 1910, it has been renovated three times.\" (comma splice)\n"
        "After: \"The bridge was designed in 1910; it has been renovated three times.\"\n\n"
        "Before: \"Although the study was promising. More replication is needed.\"\n"
        "After: \"Although the study was promising, more replication is needed.\"\n\n"
        "Before: \"The scientist published her findings the journal rejected them.\"\n"
        "After: \"The scientist published her findings, but the journal rejected them.\"\n\n"
        "Before: \"She brought everything she needed: her notes, her laptop, and her charger she forgot her ID.\"\n"
        "After: \"She brought everything she needed — her notes, her laptop, and her charger — but she forgot her ID.\"\n\n"

        "**SAT-style question with 4-choice analysis**\n"
        "\"The ancient city of Petra was carved directly into rose-red sandstone cliffs ______ its elaborate facades have survived more than two thousand years of exposure to wind and rain.\"\n\n"
        "(A) cliffs, its — Comma between two ICs = comma splice. Wrong.\n"
        "(B) cliffs; its — Semicolon between two ICs. Both sides are complete sentences. Correct.\n"
        "(C) cliffs its — No punctuation between two ICs = run-on. Wrong.\n"
        "(D) cliffs: its — A colon requires that the first side makes a complete statement that is then explained or listed by the second side. While both sides are ICs, the colon signals an explanation relationship that the word \"its\" does not naturally introduce. The semicolon is the cleaner, unambiguous choice. Wrong.\n\n"

        "⚠️ Common mistake: using a comma to join two complete sentences because it \"sounds like a natural pause.\" Pauses do not determine punctuation — grammatical structure does. If both sides are independent clauses, a comma alone is always wrong.\n\n"

        "💡 Tip: test every answer choice by reading each side of the punctuation mark separately. Ask: \"Can this side stand alone as a sentence?\" If both sides can, you need a period, semicolon, or comma + FANBOYS. If only one side can, you may use a comma or nothing, depending on what the other side is."
    ),
    (
        7,
        # ── Lesson 7: Standard English Conventions II: Form & Sense ───────────
        "**Standard English Conventions II: Form, Structure & Sense**\n\n"

        "**What the question tests**\n"
        "Form, Structure & Sense questions cover grammar: making verbs agree with their subjects, ensuring pronouns match their antecedents, keeping items in a list grammatically parallel, placing modifiers correctly, and maintaining consistent and logical verb tenses. Like all SEC questions, the stem is always: \"Which choice completes the text so that it conforms to the conventions of Standard English?\"\n\n"

        "**Subject-verb agreement**\n"
        "The verb must agree in number with its **true subject** — not the nearest noun. Prepositional phrases and parenthetical information between the subject and verb frequently create false agreement traps.\n\n"
        "Before: \"The collection of ancient manuscripts are stored in a climate-controlled vault.\"\n"
        "After: \"The collection of ancient manuscripts **is** stored in a climate-controlled vault.\"\n"
        "(Subject = \"collection,\" singular — ignore \"of ancient manuscripts.\")\n\n"
        "**Indefinite pronouns** are singular: each, every, either, neither, anyone, someone, everyone, no one, nothing, everything.\n"
        "Example: \"Each of the proposed solutions **requires** further testing.\"\n\n"

        "**Pronoun case**\n"
        "Use **subject pronouns** (I, he, she, they, we, who) when the pronoun is performing the action. Use **object pronouns** (me, him, her, them, us, whom) when the pronoun receives the action or follows a preposition.\n\n"
        "Before: \"The award was given to she and the other finalists.\"\n"
        "After: \"The award was given to **her** and the other finalists.\" (follows preposition \"to\")\n\n"
        "A quick test: remove the other person and try the pronoun alone. \"The award was given to she\" is obviously wrong; \"the award was given to her\" is correct.\n\n"

        "**Parallel structure**\n"
        "Items in a list or comparison must use the same grammatical form. Mix a gerund (-ing noun) with an infinitive (to + verb) and you break parallelism.\n\n"
        "Before: \"The program teaches writing, to analyze arguments, and critical reading.\"\n"
        "After: \"The program teaches **writing**, **analyzing** arguments, and **reading** critically.\"\n\n"

        "**Modifiers: place them next to what they modify**\n"
        "An opening participial phrase (-ing or -ed phrase at the start of a sentence) must describe the **grammatical subject** of the main clause that follows the comma.\n\n"
        "Before: \"Exhausted after the long climb, the summit finally came into view.\"\n"
        "After: \"Exhausted after the long climb, **the hikers** finally reached the summit.\"\n"
        "(Who was exhausted? The hikers — so \"the hikers\" must follow the comma.)\n\n"

        "**Verb tense consistency**\n"
        "Tenses must follow a logical time sequence. Use the **past perfect** (had + past participle) for an event that was completed before another past event.\n\n"
        "Before: \"By the time the inspector arrived, the workers already removed the equipment.\"\n"
        "After: \"By the time the inspector arrived, the workers **had** already removed the equipment.\"\n\n"
        "Use the **subjunctive** (were, not was) for hypothetical or contrary-to-fact statements:\n"
        "\"If the data **were** conclusive, the committee would act immediately.\"\n\n"

        "**SAT-style question with 4-choice analysis**\n"
        "\"Neither the lead researcher nor the two lab assistants ______ aware that the experiment had already been replicated elsewhere.\"\n\n"
        "(A) was — With \"neither/nor,\" the verb agrees with the **nearer** subject (\"two lab assistants,\" plural). \"Was\" is singular. Wrong.\n"
        "(B) were — Agrees with \"two lab assistants\" (plural). Correct.\n"
        "(C) are — Present tense is inconsistent with the past-tense context of the sentence. Wrong.\n"
        "(D) have been — Present perfect is also inconsistent with the simple-past context. Wrong.\n\n"

        "⚠️ Common mistake: matching the verb to the noun immediately before it rather than to the true subject. Mentally cross out all prepositional phrases and parenthetical information, then check subject-verb agreement on what remains.\n\n"

        "💡 Tip: for dangling or misplaced modifiers, ask \"who or what is doing this action?\" — the answer to that question must be the noun placed immediately after the modifying phrase. If it is not, the answer choice creates a dangling modifier and is wrong."
    ),
    (
        8,
        # ── Lesson 8: Expression of Ideas: Transitions & Synthesis ───────────
        "**Expression of Ideas: Transitions & Rhetorical Synthesis**\n\n"

        "**What Expression of Ideas tests**\n"
        "Expression of Ideas questions make up about 20% of the SAT Reading & Writing section and come in two distinct types. **Transition questions** ask you to choose the word or phrase that best connects two sentences. **Rhetorical Synthesis questions** give you a set of bullet-point notes and a stated goal, then ask you to choose the sentence that most effectively accomplishes that goal using the relevant notes.\n\n"

        "**Transitions: identify the logical relationship first**\n"
        "Every transition word signals a specific logical relationship between the ideas on either side of it. The single most important rule: **determine the relationship before looking at the choices**, then choose the transition from the matching category.\n\n"
        "- **Addition** (the second idea continues in the same direction): furthermore, additionally, moreover, also, in addition\n"
        "- **Contrast** (the second idea turns against or qualifies the first): however, nevertheless, on the other hand, in contrast, yet, still, that said\n"
        "- **Cause/Effect** (the second idea results from the first): therefore, as a result, consequently, thus, hence\n"
        "- **Illustration** (the second idea is a specific example of the first): for example, for instance, specifically, to illustrate\n"
        "- **Concession** (acknowledging the opposing side before returning to your own): although, while, even though, despite, granted\n\n"

        "**Sample passage (transitions)**\n"
        "\"Early conservationists believed that protecting wilderness required keeping humans entirely out of designated natural areas. Decades of research have shown that this exclusionary model often displaced indigenous communities who had managed those landscapes sustainably for generations. ______, some of the most successful modern conservation programs actively incorporate indigenous land management practices and give local communities formal authority over protected areas.\"\n\n"

        "**Transition worked example**\n"
        "The first two sentences describe a problem with the old model (exclusion harmed indigenous communities). The third sentence introduces a better, alternative approach. This is a **contrast** relationship — the new model is different from and better than the old one.\n\n"
        "(A) Furthermore — signals addition (more of the same direction). The new approach is not \"more\" of the exclusionary model. Wrong.\n"
        "(B) For instance — signals that what follows is an example of what preceded. The third sentence is not an example of displacing communities; it is the opposite. Wrong.\n"
        "(C) In contrast — signals a turn to the opposite idea. The successful modern programs are the alternative to the exclusionary model. Correct.\n"
        "(D) As a result — signals cause-effect (the third idea results from the first two). The third sentence is not a consequence of the problem; it is a solution to it. Wrong.\n\n"

        "**Rhetorical Synthesis: match the sentence to the stated goal**\n"
        "The synthesis question gives you 3-4 bullet-point notes and tells you exactly what goal a student wants to achieve (\"emphasize X,\" \"compare X and Y,\" \"explain why Z\"). The correct answer uses the **relevant notes** to **precisely accomplish that goal** — and only that goal. Wrong answers typically use accurate notes but serve a different purpose.\n\n"

        "**Synthesis worked example**\n"
        "Notes:\n"
        "- The monarch butterfly migrates up to 3,000 miles between Mexico and Canada each year\n"
        "- Monarch populations have declined by more than 80% since the 1990s\n"
        "- Milkweed, the only plant on which monarchs lay eggs, has been largely eliminated from agricultural areas\n"
        "- Restoration of milkweed along migration corridors has begun in several US states\n\n"
        "Goal: The student wants to **explain a key cause of the monarch butterfly's population decline**.\n\n"
        "(A) Monarch butterflies migrate up to 3,000 miles each year between Mexico and Canada. — True, but describes the migration route, not a cause of decline. Wrong goal.\n"
        "(B) The elimination of milkweed from agricultural areas has deprived monarchs of the only plant on which they can reproduce, contributing to a population decline of more than 80% since the 1990s. — Uses the milkweed loss note (cause) and connects it to the population decline (effect), directly accomplishing the goal. Correct.\n"
        "(C) Several US states have begun restoring milkweed along migration corridors. — True, but describes the solution, not the cause of decline. Wrong goal.\n"
        "(D) Monarch populations have declined by more than 80% since the 1990s. — States the decline as a fact but does not explain a cause. Wrong goal.\n\n"

        "⚠️ Common mistake: on transition questions, choosing a transition that \"sounds smooth\" rather than checking the logical relationship. \"Therefore\" and \"however\" both sound natural in many contexts, but only one is logically correct. Always test the relationship first.\n\n"

        "💡 Tip: for synthesis questions, underline the goal word in the prompt (\"emphasize,\" \"compare,\" \"illustrate\") before reading the choices. Then eliminate every answer that serves a different goal, even if it uses accurate notes. The correct answer must accomplish the stated goal, not just state true information."
    ),
    (
        9,
        # ── Lesson 9: Test-Day Strategy & Pacing ──────────────────────────────
        "**Test-Day Strategy & Pacing**\n\n"

        "**Pacing: 1.1 minutes per question**\n"
        "You have approximately 64 minutes for 54 questions — just over 1 minute and 6 seconds each. This is tight but manageable if you never stall. The rule is simple: if a question is taking longer than 90 seconds, make your best guess, flag it, and move on. Do not let one difficult question consume time that belongs to three easier ones later in the module. Return to flagged questions only if time permits.\n\n"
        "SEC (grammar and punctuation) questions are typically the fastest — many can be answered in 30-40 seconds once you identify the rule being tested. Transition questions are also quick. Bank that time for reading-intensive questions that require careful passage analysis.\n\n"

        "**The per-question routine**\n"
        "A reliable four-step routine keeps you consistent under pressure:\n\n"
        "- **Step 1 — Read the question stem first**: know what job you are doing (main idea? evidence? transition? word meaning?) before reading the passage. This focuses your reading.\n"
        "- **Step 2 — Skim the passage for structure**: identify the topic, the author's main claim, and the overall structure in 20 seconds. For SEC questions, locate the relevant grammatical unit.\n"
        "- **Step 3 — Predict**: form your own answer in plain language before reading the choices. For vocabulary, predict a replacement word. For transitions, predict the logical relationship. For SEC, identify the rule.\n"
        "- **Step 4 — Eliminate and match**: cross out choices that contradict the passage, go beyond the passage, address the wrong detail, or are too extreme. Match the remaining choices to your prediction.\n\n"

        "**Elimination: the four wrong-answer patterns**\n"
        "Every wrong answer on the SAT Reading & Writing section falls into one of four categories:\n\n"
        "- **Contradicts the passage**: states the opposite of what the passage says\n"
        "- **Goes beyond the passage**: makes a claim the passage never supports — often uses absolute language (\"always,\" \"never,\" \"proves,\" \"all studies show\")\n"
        "- **Addresses the wrong detail**: accurately describes something in the passage but answers a different question than the one being asked\n"
        "- **Too extreme**: the passage suggests or implies something moderate, but the choice overstates it with words like \"definitely,\" \"certainly,\" or \"inevitably\"\n\n"

        "**Domain-specific shortcuts**\n"
        "- **Vocabulary (Words in Context)**: always predict a replacement word before reading choices; context clues (contrast signals, cause signals) narrow the prediction instantly\n"
        "- **Evidence (textual)**: restate the claim in your own words, then test each quote for direct relevance to that specific claim\n"
        "- **SEC (grammar and punctuation)**: identify the rule first (boundary? subject-verb? modifier?), then evaluate each choice against the rule\n"
        "- **Transitions**: read the two sentences, determine the logical relationship, then choose from the matching category\n\n"

        "**Managing the adaptive format**\n"
        "If Module 2 feels harder than Module 1, that is a good sign — it means your Module 1 performance was strong enough to route you to the higher-scoring tier. Do not panic at difficult questions in Module 2; they carry higher score potential, not higher penalty. Stay calm, apply your strategies, and trust that hard questions are designed to challenge everyone who reaches that tier.\n\n"

        "**Test-day logistics**\n"
        "- Arrive at least 15 minutes early; late arrivals may not be admitted\n"
        "- Bring a valid photo ID (school ID, driver's license, or passport)\n"
        "- No phone use during the test, including during breaks\n"
        "- You will have two breaks: a 10-minute break after the Reading & Writing section and a 5-minute break between Math modules\n"
        "- Bring water and a snack for breaks; test centers do not provide food\n\n"

        "**Mental strategies for test day**\n"
        "- **Skip and return**: flagging a question and moving on is a skill, not a failure. Every question is worth exactly one point — a hard question is worth no more than an easy one\n"
        "- **Stay calm on hard questions**: a question that stops you cold may be hard for most test-takers. Spend 90 seconds, eliminate what you can, pick the better remaining choice, flag it, and move on\n"
        "- **Trust the modest answer**: when two choices remain, the less extreme, more carefully qualified choice is almost always correct. The SAT rarely rewards absolute statements\n"
        "- **No outside knowledge**: if you find yourself thinking \"but I know from biology class that...\" stop. Return to the passage. The answer is always there\n\n"

        "⚠️ Common mistake: spending three or four minutes on one question that feels important and running out of time for several easier questions at the end of the module. Time management is as important as content knowledge on the digital SAT. Practice with a timer from day one.\n\n"

        "💡 Tip: during your practice sessions, track which domain costs you the most time per question. If transitions take you longer than vocabulary, do more timed transition drills. Test day should feel like an accelerated version of a familiar routine, not an encounter with the unknown."
    ),
]


class Command(BaseCommand):
    help = "Enrich lesson content for SAT Reading & Writing: Complete Course"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(
                course__slug="sat-reading-writing-complete", order=order
            ).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(
            self.style.SUCCESS(
                "Done enriching SAT RW: Complete Course lessons."
            )
        )
