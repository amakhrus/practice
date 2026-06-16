"""
Seed data: 'SAT Reading & Writing: Craft & Structure' -- a deep-dive course
covering the Craft & Structure domain of the digital SAT Reading and Writing
section (approximately 28% of the section).

Topics covered:
  - Words in Context (vocabulary from context, connotation vs. denotation)
  - Text Structure and Organization
  - Author Perspective and Point of View
  - Evaluating Arguments
  - Analyzing Rhetorical Choices
  - Cross-Text Connections
  - SAT Craft & Structure Strategy (test-day approach)

Run:
    python manage.py seed_sat_rw_craft_structure
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "SAT Reading & Writing: Craft & Structure",
    "slug": "sat-rw-craft-structure",
    "program": "SAT",
    "subject": "rla",
    "description": (
        "Master the Craft & Structure domain of the digital SAT Reading and Writing section by "
        "learning to decode vocabulary in context, analyze how authors organize and develop texts, "
        "identify perspective and rhetorical purpose, and compare two passages on the same topic. "
        "Targeted lessons, worked examples, and 28 realistic practice questions with full "
        "explanations prepare you to handle every Craft & Structure question type on test day."
    ),
    "lessons": [
        (
            "1. Words in Context",
            "**Words in Context** questions ask you to figure out the meaning of a word or phrase "
            "from how it is used in a specific passage -- not from a dictionary definition. The "
            "SAT tests *precise* word meaning, so two words that seem like synonyms (e.g., "
            "\"happy\" and \"elated\") can produce different right and wrong answers depending on "
            "the passage's tone and surrounding details.\n\n"
            "**Sample passage:**\n"
            "\"The committee's decision to table the proposal surprised the delegates. After months "
            "of heated debate, the chair's calm, measured tone had done little to *bridge* the "
            "divide between the two factions, and many members left the hall feeling that the "
            "process had been deliberately *obscured*.\"\n\n"
            "**Connotation vs. Denotation**\n"
            "- **Denotation** is the literal dictionary meaning of a word.\n"
            "- **Connotation** is the emotional or associative weight a word carries.\n"
            "- SAT questions probe connotation. \"Inquisitive\" and \"nosy\" both mean curious, "
            "but only one fits a sentence praising a scientist.\n\n"
            "**Tone signals** help you predict meaning. Words like *despite*, *yet*, "
            "*surprisingly*, or *although* signal a shift -- the second idea contrasts the first. "
            "Words like *therefore*, *thus*, and *as a result* signal that the author is "
            "reinforcing or explaining.\n\n"
            "**Worked example:**\n"
            "\"As used in the passage, *bridge* most nearly means --\"\n"
            "Predict first: the passage says the chair's calm tone *failed* to heal the divide, "
            "so *bridge* here means to close or overcome a gap. Eliminate any choice that means "
            "something physical or unrelated to resolving conflict.\n\n"
            "⚠️ Common mistake: choosing the most common meaning of the word (e.g., a structure "
            "over water) instead of the meaning supported by the passage context.\n\n"
            "💡 Tip: cover the answer choices, read the sentence, and substitute your own word "
            "before looking at the options. Your substitution guides you to the best match."
        ),
        (
            "2. Text Structure and Organization",
            "**Text Structure** questions ask about how a passage is organized and why the author "
            "arranged the information in a particular way. The SAT tests four main patterns, and "
            "recognizing the pattern quickly helps you predict the purpose of each paragraph.\n\n"
            "**Sample passage:**\n"
            "\"Coral reefs have declined sharply over the past three decades. Rising ocean "
            "temperatures bleach and kill coral, while agricultural runoff delivers excess "
            "nutrients that fuel algae overgrowth. Conservation programs that regulate fishing "
            "and reduce coastal pollution have slowed the decline in some regions, offering a "
            "model for broader policy reform.\"\n\n"
            "**The four key patterns:**\n"
            "- **Problem-Solution**: author identifies a problem, then presents a remedy.\n"
            "- **Compare-Contrast**: author places two or more things side by side to highlight "
            "similarities or differences.\n"
            "- **Cause-Effect**: author explains what causes something or what results from it.\n"
            "- **Chronological**: author traces events in the order they occurred.\n\n"
            "The passage above follows a **cause-effect-to-problem-solution** arc: the problem "
            "(reef decline) leads to its causes (temperature, runoff), which leads to a solution "
            "(conservation programs).\n\n"
            "**Worked example:**\n"
            "\"The main purpose of the final sentence is to --\"\n"
            "The final sentence shifts from describing causes to describing a solution and "
            "explicitly calls it a \"model.\" The purpose is to introduce a potential remedy, "
            "not to introduce a new problem or summarize causes.\n\n"
            "⚠️ Common mistake: choosing \"to provide an example\" when the sentence is actually "
            "offering a solution or recommendation -- read the function, not just the topic.\n\n"
            "💡 Tip: label each paragraph with one word (problem, cause, solution, contrast) "
            "before reading the questions. This mental map makes structure questions fast."
        ),
        (
            "3. Author Perspective and Point of View",
            "**Author Perspective** questions ask you to identify the author's attitude, stance, "
            "or purpose -- not just what the passage says, but *how* and *why* the author says "
            "it. You must distinguish the author's own voice from the voices of sources the "
            "author cites.\n\n"
            "**Sample passage:**\n"
            "\"Dr. Ellis argues that standardized testing is an indispensable measure of academic "
            "readiness. While her data are compelling, critics note that a single exam score "
            "captures only a narrow slice of student potential. A more nuanced assessment "
            "framework, one that incorporates teacher evaluations and project-based work, would "
            "serve students far better.\"\n\n"
            "**Identifying author attitude:**\n"
            "- Look for evaluative adjectives: *compelling*, *flawed*, *insightful*, *limited*.\n"
            "- Look for hedging language: *while*, *although*, *despite* -- these signal the "
            "author is about to qualify or contradict the preceding idea.\n"
            "- The author's thesis is usually the final or near-final sentence of a passage.\n\n"
            "**Distinguishing author voice from cited sources:**\n"
            "In the sample, Dr. Ellis *argues* for standardized testing -- that is her view. The "
            "author's own position appears in the last sentence (a \"more nuanced framework\"). "
            "The author acknowledges Ellis's data but ultimately disagrees with her conclusion.\n\n"
            "**Worked example:**\n"
            "\"Which choice best describes the author's perspective on standardized testing?\"\n"
            "The author calls Ellis's data \"compelling\" (a concession) but then advocates for "
            "a \"more nuanced\" approach. The author's view is that standardized testing is "
            "insufficient on its own -- a position of qualified skepticism.\n\n"
            "⚠️ Common mistake: attributing a cited source's view to the author. Always ask: "
            "does the author endorse this view or merely report it?\n\n"
            "💡 Tip: underline every verb of attribution (argues, claims, contends, suggests). "
            "Sentences without such verbs are usually the author speaking directly."
        ),
        (
            "4. Evaluating Arguments",
            "**Evaluating Arguments** questions ask you to assess the logical structure of a "
            "passage -- identifying premises, conclusions, assumptions, and the quality of the "
            "evidence used. These questions appear less frequently than vocabulary questions but "
            "reward students who understand basic informal logic.\n\n"
            "**Sample passage:**\n"
            "\"Every student who participated in the school's mentorship program last year earned "
            "a GPA above 3.0. Therefore, expanding the program to all students will raise overall "
            "academic performance across the school.\"\n\n"
            "**Key terms:**\n"
            "- **Premise**: a stated reason or piece of evidence (all participants earned above "
            "3.0).\n"
            "- **Conclusion**: the claim the author draws from the premises (expanding the program "
            "will raise performance).\n"
            "- **Assumption**: an unstated belief the argument requires to be true (that the "
            "program itself caused the high GPA, not pre-existing student motivation).\n\n"
            "**Types of evidence:**\n"
            "- **Anecdotal**: based on individual stories or a single example -- weak.\n"
            "- **Statistical**: based on large-scale data -- stronger, but watch for sample bias.\n\n"
            "**Worked example:**\n"
            "\"Which of the following, if true, would most weaken the argument?\"\n"
            "The argument assumes the mentorship program *caused* the high GPAs. A weakener would "
            "show an alternative cause: e.g., that only high-achieving students were selected for "
            "the program in the first place. That would expose the assumption and undercut the "
            "conclusion.\n\n"
            "⚠️ Common mistake: choosing an answer that attacks a side point rather than the "
            "central assumption. Target the link between the premise and the conclusion.\n\n"
            "💡 Tip: always locate the conclusion first (look for *therefore*, *thus*, *so*, "
            "*hence*). Everything before it is a premise; the assumption is what connects them."
        ),
        (
            "5. Analyzing Rhetorical Choices",
            "**Rhetorical Choices** questions ask *why* an author chose a particular word, "
            "detail, example, or structural move -- not just *what* was said but the effect the "
            "choice creates. These questions overlap with text structure and author perspective "
            "but focus specifically on craft decisions.\n\n"
            "**Sample passage:**\n"
            "\"When the factory closed, 400 families lost their primary income overnight. Maria, "
            "a single mother of three, described standing in her empty kitchen and wondering how "
            "she would pay the next month's rent. Statistics alone rarely convey the human cost "
            "of economic disruption.\"\n\n"
            "**Rhetorical appeals:**\n"
            "- **Ethos**: the author builds credibility (citing credentials, peer-reviewed data).\n"
            "- **Pathos**: the author appeals to emotion (personal story, vivid imagery).\n"
            "- **Logos**: the author uses logic and evidence (statistics, causal reasoning).\n\n"
            "**Tone** is the author's emotional attitude toward the subject. Common SAT tone "
            "words: *critical*, *celebratory*, *cautionary*, *nostalgic*, *ironic*, *objective*.\n\n"
            "**Worked example:**\n"
            "\"Why does the author include the detail about Maria?\"\n"
            "Maria's story follows a statistic about 400 families. The author's next sentence "
            "says statistics alone do not convey human cost. Maria's story is therefore included "
            "to illustrate the *emotional and human reality* behind the numbers -- a **pathos** "
            "appeal that makes the statistic concrete.\n\n"
            "⚠️ Common mistake: saying the detail \"provides additional evidence\" when it is "
            "actually shifting the register from logical to emotional.\n\n"
            "💡 Tip: ask yourself: what would the passage *lose* if this detail were removed? "
            "That loss is the rhetorical function of the detail."
        ),
        (
            "6. Cross-Text Connections",
            "**Cross-Text Connections** questions give you two short passages on the same topic "
            "written from different perspectives. Questions ask how the authors agree, disagree, "
            "or would respond to each other. This is a high-value skill because these questions "
            "reward systematic comparison, not guesswork.\n\n"
            "**Sample passages:**\n"
            "*Passage 1:* \"Remote work dramatically improves employee well-being by eliminating "
            "lengthy commutes and allowing workers to manage personal obligations. Companies that "
            "embrace flexible schedules report higher retention rates.\"\n\n"
            "*Passage 2:* \"While remote work offers individual convenience, the absence of "
            "in-person collaboration stunts innovation. Research shows that spontaneous office "
            "interactions generate the majority of new product ideas at technology firms.\"\n\n"
            "**How to map agreement and disagreement:**\n"
            "- **Where they agree**: both authors acknowledge that remote work benefits individual "
            "employees.\n"
            "- **Where they disagree**: Passage 1 focuses on benefits (well-being, retention); "
            "Passage 2 focuses on a cost (reduced innovation).\n"
            "- **The key question format**: \"Author A would most likely respond to Author B's "
            "claim by ...\" -- always anchor your answer in Author A's text, not your opinion.\n\n"
            "**Worked example:**\n"
            "\"How would the author of Passage 1 most likely respond to the claim in Passage 2 "
            "that remote work stunts innovation?\"\n"
            "Passage 1 does not address innovation directly, but it emphasizes retention and "
            "well-being. Author 1 would likely *acknowledge* the concern but argue that happier "
            "employees are ultimately more productive -- a concede-but-counter move.\n\n"
            "⚠️ Common mistake: inventing a response that is logical but not grounded in "
            "Passage 1's actual content. Stick to what Author 1 actually says.\n\n"
            "💡 Tip: read both passages, then write one sentence summarizing each author's main "
            "claim before tackling the questions. This prevents you from conflating the two."
        ),
        (
            "7. SAT Craft & Structure Strategy",
            "This lesson consolidates the strategies from Lessons 1-6 into a repeatable test-day "
            "process for every Craft & Structure question type.\n\n"
            "**Vocabulary question approach (Words in Context):**\n"
            "- Cover the answer choices.\n"
            "- Re-read the sentence and one sentence on either side for context.\n"
            "- Substitute your own word based on context and tone.\n"
            "- Match your word to the choice that is closest in meaning *and* connotation.\n"
            "- Plug the choice back into the sentence to confirm it sounds precise, not just "
            "acceptable.\n\n"
            "**Avoiding the 'sounds good' trap:**\n"
            "- Every wrong answer on a Craft & Structure question is designed to sound plausible.\n"
            "- The most common wrong-answer traps are: (1) the most common meaning of the word "
            "rather than the contextual meaning, (2) the author's topic rather than the author's "
            "purpose, and (3) a cited source's view mistaken for the author's view.\n"
            "- Always ask: *what does the passage explicitly support?*\n\n"
            "**Cross-text process (two-passage questions):**\n"
            "- Summarize Passage 1 in one sentence (author + main claim).\n"
            "- Summarize Passage 2 in one sentence.\n"
            "- Note whether they agree, disagree, or one extends the other.\n"
            "- For 'Author A would most likely respond' questions, stay in Author A's lane.\n\n"
            "**Sample passage (strategy in action):**\n"
            "\"The report *underscored* the urgent need for infrastructure investment, citing "
            "decades of deferred maintenance across the nation's bridges and tunnels.\"\n"
            "Question: \"As used in the passage, *underscored* most nearly means --\"\n"
            "Predict: something like *emphasized* or *highlighted*. Match to answer choices.\n\n"
            "⚠️ Common mistake: skipping the prediction step and reading all four choices first. "
            "This makes you vulnerable to the attractive wrong answers.\n\n"
            "💡 Tip: on test day, budget roughly 70-80 seconds per question. If a vocabulary "
            "question takes more than 90 seconds, mark it, move on, and return with fresh eyes."
        ),
    ],
    "mcqs": [
        # ── Lesson 1: Words in Context ──────────────────────────────────────────
        {
            "text": (
                "Passage: \"The scientist's early findings were *tentative*, based on a small "
                "sample and subject to revision as more data emerged.\"\n\n"
                "As used in the passage, \"tentative\" most nearly means --"
            ),
            "difficulty": 1,
            "choices": [
                ("hesitant and lacking confidence", False),
                ("preliminary and uncertain", True),
                ("bold and experimental", False),
                ("carefully recorded", False),
            ],
            "explanation": (
                "In context, the findings are \"subject to revision\" because the sample is "
                "small -- they are not yet confirmed. \"Preliminary and uncertain\" captures "
                "that meaning precisely. \"Hesitant\" describes a person's manner, not a "
                "finding's status. \"Bold\" contradicts the passage's cautious tone. "
                "\"Carefully recorded\" ignores the uncertainty implied by the sentence. "
                "Pro tip: always look for the context clue that tells you *why* the word is "
                "used -- here it is \"subject to revision.\""
            ),
        },
        {
            "text": (
                "Passage: \"After the merger, the company *shed* its legacy divisions, "
                "selling off units that no longer aligned with its streamlined vision.\"\n\n"
                "As used in the passage, \"shed\" most nearly means --"
            ),
            "difficulty": 1,
            "choices": [
                ("a small outbuilding on a property", False),
                ("illuminated or cast light on", False),
                ("eliminated or got rid of", True),
                ("protected from external threats", False),
            ],
            "explanation": (
                "\"Shed\" has multiple meanings. In context, the company is *selling off* "
                "divisions -- discarding them. \"Eliminated or got rid of\" matches that "
                "meaning. The outbuilding meaning is a noun, not a verb, so it cannot fit. "
                "\"Illuminated\" is another common meaning of *shed* (as in shed light) but "
                "does not make sense with \"divisions.\" \"Protected\" is the opposite of "
                "what the passage describes. Pro tip: the most common meaning of a word is "
                "almost never the right answer on a Craft & Structure vocabulary question."
            ),
        },
        {
            "text": (
                "Passage: \"The documentary was praised for its *unflinching* portrayal of "
                "poverty, refusing to soften the harsh realities faced by the families it "
                "followed.\"\n\n"
                "As used in the passage, \"unflinching\" most nearly means --"
            ),
            "difficulty": 2,
            "choices": [
                ("emotionally detached and clinical", False),
                ("steady and unwilling to look away", True),
                ("exaggerated and sensationalized", False),
                ("sympathetic and warm-hearted", False),
            ],
            "explanation": (
                "\"Unflinching\" means not pulling back or turning away. The passage "
                "reinforces this with \"refusing to soften the harsh realities\" -- the "
                "filmmakers maintained a direct, steady gaze. \"Emotionally detached\" adds "
                "a connotation of coldness that the passage does not support. \"Exaggerated\" "
                "contradicts \"refusing to soften,\" which implies accuracy, not distortion. "
                "\"Sympathetic\" is possible in tone but does not capture the *steadiness* "
                "that \"unflinching\" conveys. Pro tip: connotation matters -- the correct "
                "choice must match both meaning and emotional register."
            ),
        },
        {
            "text": (
                "Passage: \"Critics *lauded* the architect's design, calling it a landmark "
                "achievement that would define urban aesthetics for decades.\"\n\n"
                "As used in the passage, \"lauded\" most nearly means --"
            ),
            "difficulty": 1,
            "choices": [
                ("criticized sharply", False),
                ("examined carefully", False),
                ("praised enthusiastically", True),
                ("debated publicly", False),
            ],
            "explanation": (
                "The passage describes the design as \"a landmark achievement\" -- clearly a "
                "positive evaluation. \"Praised enthusiastically\" aligns with both the word's "
                "meaning and the passage's positive tone. \"Criticized\" is the opposite of "
                "what the context signals. \"Examined\" is too neutral -- it lacks the "
                "approving connotation. \"Debated\" suggests disagreement, which contradicts "
                "the uniformly positive framing. Pro tip: tone cues like \"landmark "
                "achievement\" help you predict the right answer before reading the choices."
            ),
        },
        # ── Lesson 2: Text Structure and Organization ────────────────────────
        {
            "text": (
                "Passage: \"Global bee populations have declined by nearly 30 percent over "
                "the past two decades, threatening the pollination of crops that feed billions. "
                "Habitat loss, pesticide use, and climate change are the primary drivers of "
                "this collapse. Researchers at several universities have begun testing "
                "rewilding corridors -- strips of diverse flowering plants linking fragmented "
                "habitats -- with promising early results.\"\n\n"
                "The passage is best described as following which organizational pattern?"
            ),
            "difficulty": 2,
            "choices": [
                ("Chronological: tracing the decline of bees year by year", False),
                ("Compare-contrast: weighing two competing theories about bee decline", False),
                ("Problem-solution: identifying a crisis and introducing a remedy", True),
                ("Cause-effect only: listing factors that harm bees", False),
            ],
            "explanation": (
                "The passage opens with a problem (bee decline threatening crops), moves to "
                "causes (habitat loss, pesticides, climate change), and ends with a solution "
                "(rewilding corridors with promising results). That arc is problem-solution, "
                "even though causes are mentioned. \"Chronological\" does not fit because no "
                "year-by-year sequence is given. \"Compare-contrast\" requires two things "
                "placed side by side, which does not happen here. \"Cause-effect only\" is "
                "too narrow -- the solution in the final sentence is a key structural element. "
                "Pro tip: always read the *last* sentence carefully; it often reveals the "
                "overall organizational purpose."
            ),
        },
        {
            "text": (
                "Passage: \"In the 1950s, television was a novelty confined to wealthy "
                "households. By the 1960s, it had become a fixture in most American homes, "
                "reshaping family routines and public discourse alike. The assassination of "
                "President Kennedy in 1963 marked the first time millions of Americans "
                "collectively experienced a national crisis through a shared screen.\"\n\n"
                "The main purpose of the final sentence is to --"
            ),
            "difficulty": 2,
            "choices": [
                ("introduce a counterargument about the influence of television", False),
                ("provide a specific historical example that illustrates the passage's claim", True),
                ("shift the focus from television to political history", False),
                ("compare the 1950s and 1960s experience of television", False),
            ],
            "explanation": (
                "The passage traces television's spread and claims it reshaped \"public "
                "discourse.\" The final sentence gives a concrete historical event -- Kennedy's "
                "assassination -- as an example of television's collective power. Its purpose "
                "is to *illustrate* the broader claim. It does not introduce a counterargument "
                "(no opposing view is raised). It does not shift focus away from television "
                "(Kennedy is mentioned as evidence of television's impact). The compare-contrast "
                "choice is tempting because the passage does compare decades, but the final "
                "sentence does not do that -- it focuses on one event. Pro tip: ask what job "
                "the sentence performs in relation to the sentence before it."
            ),
        },
        {
            "text": (
                "Passage: \"The human appendix was long dismissed as a vestigial organ with "
                "no useful function. Recent studies, however, have proposed that it may serve "
                "as a reservoir for beneficial gut bacteria, allowing the microbiome to "
                "repopulate after illness. This revised understanding has prompted researchers "
                "to reconsider how quickly the appendix should be removed during non-emergency "
                "appendicitis cases.\"\n\n"
                "Which choice best describes the overall structure of the passage?"
            ),
            "difficulty": 2,
            "choices": [
                ("A hypothesis is introduced, tested, and ultimately disproven.", False),
                ("An accepted view is challenged by new evidence, leading to a revised approach.", True),
                ("Two competing scientific theories are compared and contrasted in detail.", False),
                ("A problem is identified and then solved through a step-by-step process.", False),
            ],
            "explanation": (
                "The passage begins with an old view (appendix is vestigial), then uses "
                "\"however\" to signal new evidence (it may house gut bacteria), and ends "
                "with a changed medical approach (reconsider removal). That is: accepted "
                "view challenged by new evidence, leading to revision. \"Hypothesis tested "
                "and disproven\" does not fit -- nothing is disproven outright; instead, a "
                "new possibility is raised. \"Two competing theories compared\" would require "
                "two theories developed equally, but the old view is dismissed quickly. "
                "\"Problem-solution\" does not apply because the passage is about revising "
                "scientific understanding, not solving a crisis. Pro tip: transition words "
                "like *however* and *recent studies* are structural signposts -- underline them."
            ),
        },
        {
            "text": (
                "Passage: \"Forests in the Northern Hemisphere store vast amounts of carbon. "
                "When these forests burn, that stored carbon is released into the atmosphere. "
                "The increase in atmospheric carbon contributes to the greenhouse effect, "
                "which in turn accelerates global warming and creates the drier conditions "
                "that make forests more susceptible to fire.\"\n\n"
                "The passage primarily uses which organizational pattern?"
            ),
            "difficulty": 1,
            "choices": [
                ("Problem-solution", False),
                ("Compare-contrast", False),
                ("Chronological sequence", False),
                ("Cause-effect chain", True),
            ],
            "explanation": (
                "Each sentence in the passage triggers the next: forests store carbon "
                "-> burning releases it -> atmospheric carbon increases -> greenhouse effect "
                "-> warming -> drier conditions -> more fires. This is a classic cause-effect "
                "chain, where one cause produces an effect that becomes the next cause. "
                "Problem-solution does not fit because no remedy is proposed. "
                "Compare-contrast requires two things being weighed, which does not happen. "
                "Chronological sequence tracks time order, but this passage tracks logical "
                "causation, not specific dates or events. Pro tip: look for causal connectors "
                "(*when*, *which in turn*, *contributes to*) as signals of cause-effect structure."
            ),
        },
        # ── Lesson 3: Author Perspective and Point of View ────────────────────
        {
            "text": (
                "Passage: \"Professor Nkosi contends that urban farming can solve urban food "
                "deserts entirely. While her optimism is admirable, the logistical challenges "
                "of scaling rooftop gardens to feed a major city remain formidable, and "
                "policymakers would be wise to treat urban farming as one tool among many "
                "rather than a singular solution.\"\n\n"
                "Which choice best describes the author's perspective on urban farming?"
            ),
            "difficulty": 2,
            "choices": [
                ("Enthusiastic support for Professor Nkosi's position", False),
                ("Skepticism about the value of urban farming in any context", False),
                ("Qualified endorsement: useful but not a complete solution", True),
                ("Indifference, presenting the debate without taking a position", False),
            ],
            "explanation": (
                "The author calls Nkosi's optimism \"admirable\" (a mild concession) but "
                "then says the challenges are \"formidable\" and recommends treating urban "
                "farming as \"one tool among many.\" That is a qualified endorsement -- the "
                "author sees value in urban farming but disagrees that it can solve the problem "
                "alone. \"Enthusiastic support\" ignores the critical second half of the "
                "passage. \"Skepticism about any context\" overstates the author's critique. "
                "\"Indifference\" is wrong because the author explicitly recommends a policy "
                "position. Pro tip: the phrase *would be wise to* is a direct signal of the "
                "author's own recommendation."
            ),
        },
        {
            "text": (
                "Passage: \"Some historians celebrate the Industrial Revolution as an era of "
                "unprecedented progress. The data tell a more complicated story: child labor "
                "was rampant, life expectancy in factory towns actually fell in the early "
                "decades, and the wealth generated flowed almost exclusively to a small "
                "ownership class.\"\n\n"
                "The author's attitude toward the Industrial Revolution can best be described as --"
            ),
            "difficulty": 2,
            "choices": [
                ("uncritically celebratory", False),
                ("deeply nostalgic", False),
                ("critically revisionist", True),
                ("cautiously optimistic", False),
            ],
            "explanation": (
                "The author opens by acknowledging the celebratory view but immediately "
                "pivots with \"the data tell a more complicated story\" and proceeds to list "
                "three negative facts (child labor, falling life expectancy, concentrated "
                "wealth). The author is *revising* the celebratory narrative with critical "
                "evidence -- that is a critically revisionist stance. \"Uncritically "
                "celebratory\" describes the historians the author is pushing back against, "
                "not the author. \"Nostalgic\" implies the author longs for the past, which "
                "is not supported. \"Cautiously optimistic\" would require the author to "
                "express some hope, which does not appear in the passage. Pro tip: words "
                "like *actually* and *more complicated* signal that the author is correcting "
                "a prevailing assumption."
            ),
        },
        {
            "text": (
                "Passage: \"Dr. Patel insists that social media is uniquely harmful to "
                "adolescent mental health. Subsequent longitudinal studies, however, have "
                "produced inconsistent results, with several finding no significant effect "
                "once confounding variables such as pre-existing anxiety disorders are "
                "controlled for.\"\n\n"
                "Based on the passage, how does the author view Dr. Patel's claim?"
            ),
            "difficulty": 3,
            "choices": [
                ("As well-supported by the most recent evidence", False),
                ("As overstated given the mixed findings of later research", True),
                ("As completely discredited and no longer worth discussing", False),
                ("As the consensus position among researchers in the field", False),
            ],
            "explanation": (
                "The author presents Dr. Patel's claim and then immediately follows it with "
                "\"however\" and evidence of \"inconsistent results\" and studies finding "
                "\"no significant effect\" once confounders are controlled. The author does "
                "not endorse Patel's view -- the word *however* signals a direct challenge. "
                "But the author does not say Patel is *completely discredited* either; the "
                "evidence is described as inconsistent, not conclusively negative. \"Overstated "
                "given mixed findings\" correctly captures this nuance. \"Consensus position\" "
                "is contradicted by the phrase \"inconsistent results.\" Pro tip: *however* "
                "is the most important word in the passage -- it marks the author's pivot away "
                "from Patel's position."
            ),
        },
        {
            "text": (
                "Passage: \"The mayor dismissed the rezoning proposal as unnecessary, citing "
                "low vacancy rates in the neighborhood. Residents, however, pointed to "
                "skyrocketing rents and long waitlists at local shelters as evidence of an "
                "acute housing shortage. The truth, as is so often the case with urban policy, "
                "lies somewhere between the data each side selectively presents.\"\n\n"
                "Which choice best describes the author's point of view?"
            ),
            "difficulty": 2,
            "choices": [
                ("Strongly in favor of the mayor's position", False),
                ("Strongly in favor of the residents' position", False),
                ("Neutral but suggesting both sides present incomplete pictures", True),
                ("Uncertain and unable to draw any conclusion", False),
            ],
            "explanation": (
                "The author presents the mayor's view and the residents' view, then states "
                "that \"the truth lies somewhere between the data each side selectively "
                "presents.\" The key word is *selectively* -- the author accuses both sides "
                "of cherry-picking data, implying neither has the full picture. That is a "
                "neutral-but-critical stance, not endorsement of either side. \"Uncertain "
                "and unable to draw any conclusion\" misreads the passage -- the author is "
                "not confused; the author is making a deliberate evaluative point. Pro tip: "
                "when an author acknowledges two opposing views and then says \"the truth "
                "lies between,\" the author's own position is that both are incomplete."
            ),
        },
        # ── Lesson 4: Evaluating Arguments ────────────────────────────────────
        {
            "text": (
                "Argument: \"Students who eat breakfast perform better academically. "
                "Therefore, serving free breakfast at all public schools will improve "
                "standardized test scores district-wide.\"\n\n"
                "Which of the following, if true, most strengthens this argument?"
            ),
            "difficulty": 2,
            "choices": [
                ("Many students already eat breakfast before arriving at school.", False),
                ("Standardized test scores are an imperfect measure of academic performance.", False),
                ("Studies show that students who previously skipped breakfast scored higher after a free breakfast program was introduced.", True),
                ("The cost of providing free breakfast is substantial for most school districts.", False),
            ],
            "explanation": (
                "The argument's key assumption is that providing breakfast causes better test "
                "performance. A strengthener must support that causal link directly. Option C "
                "does exactly that: it shows that students who skipped breakfast (and therefore "
                "were not eating it) scored higher *after* a breakfast program began -- direct "
                "causal evidence. Option A weakens the argument by suggesting the program would "
                "not reach students who need it. Option B undermines the measure used (test "
                "scores). Option D raises a cost concern, which is a practical objection, not "
                "a logical strengthener. Pro tip: strengtheners add new evidence that supports "
                "the link between the premise and the conclusion."
            ),
        },
        {
            "text": (
                "Argument: \"Our city's crime rate dropped 15 percent in the year after the "
                "new street-lighting program was installed. The lighting program is therefore "
                "responsible for the reduction in crime.\"\n\n"
                "The argument above is most vulnerable to which criticism?"
            ),
            "difficulty": 3,
            "choices": [
                ("It relies on a statistic that has not been independently verified.", False),
                ("It assumes that correlation between lighting and crime reduction implies causation.", True),
                ("It ignores the possibility that street lighting could increase crime.", False),
                ("It overstates the size of the crime reduction.", False),
            ],
            "explanation": (
                "The argument observes that crime fell *after* the lighting program was "
                "installed and concludes the program *caused* the drop. This is the classic "
                "post hoc ergo propter hoc (after this, therefore because of this) fallacy -- "
                "confusing correlation with causation. Other factors (economic changes, "
                "additional policing, seasonal variation) could explain the decline. Option B "
                "identifies this flaw precisely. Option A raises an unverified statistic "
                "concern, but the passage does not question the statistic itself. Option C "
                "introduces a possibility the argument does not address, but that is not the "
                "argument's primary logical flaw. Option D is not supported -- 15 percent is "
                "not described as an overstatement. Pro tip: whenever an argument moves from "
                "*after* to *because of*, look for the correlation-causation flaw."
            ),
        },
        {
            "text": (
                "Argument: \"Dr. Reyes, a nutritionist with 20 years of experience, recommends "
                "this supplement. If Dr. Reyes endorses it, it must be effective.\"\n\n"
                "Which of the following best identifies the assumption underlying this argument?"
            ),
            "difficulty": 2,
            "choices": [
                ("Dr. Reyes has no financial incentive to endorse the supplement.", True),
                ("The supplement is affordable for most consumers.", False),
                ("Nutritionists always prefer natural remedies over synthetic ones.", False),
                ("Twenty years of experience is the minimum required for dietary expertise.", False),
            ],
            "explanation": (
                "The argument moves from \"Dr. Reyes endorses it\" to \"it must be effective,\" "
                "assuming that her endorsement is based purely on scientific merit. But if she "
                "has a financial incentive (a paid sponsorship, for example), her endorsement "
                "does not necessarily reflect the supplement's efficacy. The argument requires "
                "that her endorsement is unbiased -- i.e., that she has no financial incentive. "
                "That is the hidden assumption, making Option A correct. The affordability and "
                "\"natural vs. synthetic\" preferences are irrelevant to the logical structure "
                "of the argument. The years-of-experience threshold is arbitrary and not what "
                "the argument hinges on. Pro tip: to find an assumption, ask: what must be true "
                "for the conclusion to follow from the premise?"
            ),
        },
        {
            "text": (
                "Passage: \"My neighbor switched to a plant-based diet and lost 20 pounds in "
                "three months. Plant-based diets are clearly the most effective weight-loss "
                "strategy available.\"\n\n"
                "The evidence presented in this argument is best described as --"
            ),
            "difficulty": 1,
            "choices": [
                ("Statistical, because it involves a measurable outcome (20 pounds)", False),
                ("Anecdotal, because it is based on a single individual's experience", True),
                ("Expert testimony, because neighbors are familiar with local health trends", False),
                ("Causal, because it traces a direct mechanism from diet to weight loss", False),
            ],
            "explanation": (
                "The evidence is one person's experience -- a sample size of one. That is the "
                "definition of anecdotal evidence: a conclusion drawn from a single personal "
                "story rather than systematic data. Option A is tempting because \"20 pounds\" "
                "is a number, but a single data point does not constitute statistical evidence. "
                "Option C misuses the term \"expert testimony\" -- neighbors are not experts. "
                "Option D calls the evidence \"causal,\" but no mechanism is explained; the "
                "argument simply asserts the outcome. Pro tip: anecdotal evidence is weak "
                "because one case cannot establish a pattern -- look for this flaw whenever "
                "an argument generalizes from a small example."
            ),
        },
        # ── Lesson 5: Analyzing Rhetorical Choices ────────────────────────────
        {
            "text": (
                "Passage: \"In 1944, Irena Sendler smuggled approximately 2,500 Jewish "
                "children out of the Warsaw Ghetto, hiding their identities in jars buried "
                "beneath an apple tree. She was captured, tortured, and sentenced to death "
                "-- yet she refused to betray a single name. To call her actions merely "
                "heroic seems almost insufficient.\"\n\n"
                "Why does the author include the detail about the jars buried beneath an "
                "apple tree?"
            ),
            "difficulty": 2,
            "choices": [
                ("To provide verifiable archival evidence of Sendler's actions", False),
                ("To introduce a contrast between Sendler's methods and those of other rescuers", False),
                ("To make the abstract act of rescue concrete and emotionally vivid", True),
                ("To explain the historical context of World War II Poland", False),
            ],
            "explanation": (
                "The detail of jars buried under an apple tree transforms an abstract "
                "statistic (2,500 children) into a specific, sensory image. It makes the "
                "reader *see* the act of rescue rather than simply register it as a fact. "
                "This is a pathos technique -- using vivid, concrete detail to generate "
                "an emotional response. Option A is wrong because the jar detail is not "
                "cited as archival evidence. Option B is wrong because no other rescuers "
                "are mentioned. Option D is wrong because the passage provides no broader "
                "historical context beyond this single scene. Pro tip: when a specific, "
                "sensory detail follows a broad claim, its rhetorical purpose is almost "
                "always to make the claim emotionally resonant."
            ),
        },
        {
            "text": (
                "Passage: \"The proposed highway expansion will, according to the city's own "
                "traffic engineers, reduce commute times by a mere four minutes on average. "
                "For this negligible benefit, the city would demolish 47 homes, displace "
                "120 families, and spend $340 million in public funds.\"\n\n"
                "The author's use of the word \"negligible\" serves primarily to --"
            ),
            "difficulty": 2,
            "choices": [
                ("acknowledge that the city's engineers are reliable sources", False),
                ("emphasize that the benefit is too small to justify the costs", True),
                ("provide a neutral description of the four-minute reduction", False),
                ("shift the reader's attention from the financial cost to the human cost", False),
            ],
            "explanation": (
                "\"Negligible\" means too small to be worth considering. The author uses this "
                "word immediately after citing the city's own statistic, framing four minutes "
                "as trivially small compared to the costs enumerated in the next sentence. "
                "The word performs a rhetorical function: it pre-judges the benefit as "
                "unworthy of the price, building the author's argument against the expansion. "
                "Option A contradicts the author's intent -- citing the engineers' data to "
                "then call it \"negligible\" actually *undermines* the engineers' conclusion. "
                "Option C is wrong because \"negligible\" is evaluative, not neutral. "
                "Option D misidentifies what the word does -- it addresses the benefit, not "
                "a shift between cost types. Pro tip: evaluative adjectives (*negligible*, "
                "*critical*, *alarming*) reveal the author's position, not just description."
            ),
        },
        {
            "text": (
                "Passage: \"As a board-certified cardiologist with 25 years of clinical "
                "experience and the author of three peer-reviewed studies on dietary fat, "
                "Dr. Okafor is uniquely positioned to evaluate the new guidelines.\"\n\n"
                "This sentence primarily uses which rhetorical appeal?"
            ),
            "difficulty": 1,
            "choices": [
                ("Pathos, by evoking sympathy for patients affected by the guidelines", False),
                ("Logos, by presenting statistical data about dietary fat", False),
                ("Ethos, by establishing Dr. Okafor's credibility and expertise", True),
                ("Kairos, by emphasizing the urgency of the moment", False),
            ],
            "explanation": (
                "The sentence lists credentials: board certification, years of experience, "
                "peer-reviewed publications. Establishing credibility through credentials is "
                "the definition of ethos -- persuading through trustworthiness and authority. "
                "Pathos requires emotional content, which is absent here. Logos requires "
                "logical or statistical argument, and the sentence makes no logical claim "
                "about dietary fat itself. Kairos refers to timeliness and urgency, which "
                "also does not appear. Pro tip: ethos is signaled by credential language "
                "(certifications, degrees, years of experience, publications)."
            ),
        },
        {
            "text": (
                "Passage: \"The factory farm confines 80,000 chickens in a space the size "
                "of two basketball courts. Each bird has less room to move than a sheet of "
                "paper. Is this the future of food we are willing to accept?\"\n\n"
                "The author's rhetorical question at the end of the passage primarily serves to --"
            ),
            "difficulty": 2,
            "choices": [
                ("request statistical information from the reader", False),
                ("introduce a counterargument the author will address", False),
                ("invite the reader to draw a moral conclusion from the evidence presented", True),
                ("provide a transition to a new section of the passage", False),
            ],
            "explanation": (
                "A rhetorical question does not expect a literal answer -- it is designed to "
                "make the reader reflect and, in this case, feel discomfort. After two vivid, "
                "shocking statistics, the author asks whether this is \"the future we are "
                "willing to accept,\" implying the reader should not accept it. The question "
                "converts factual information into a moral challenge. Option A is wrong "
                "because the author is not actually requesting data. Option B is wrong because "
                "no counterargument follows. Option D is wrong because there is no \"next "
                "section\" indicated. Pro tip: rhetorical questions at the end of a passage "
                "almost always function to engage the reader's emotions or moral judgment."
            ),
        },
        # ── Lesson 6: Cross-Text Connections ─────────────────────────────────
        {
            "text": (
                "Passage 1: \"Exposure to classical music in early childhood strengthens the "
                "neural pathways associated with mathematical reasoning, giving musically "
                "trained children a measurable advantage in STEM subjects.\"\n\n"
                "Passage 2: \"Claims that classical music enhances intelligence have been "
                "repeatedly overstated. While music education develops fine motor skills and "
                "discipline, controlled studies find no reliable transfer effect to unrelated "
                "cognitive domains such as mathematics.\"\n\n"
                "The author of Passage 2 would most likely respond to the claim in Passage 1 by --"
            ),
            "difficulty": 3,
            "choices": [
                ("agreeing that music education is valuable but arguing the benefit is limited to motor skills", True),
                ("arguing that classical music is superior to other genres for cognitive development", False),
                ("endorsing the view that STEM performance is the best measure of musical training", False),
                ("claiming that early childhood is too early to begin formal music education", False),
            ],
            "explanation": (
                "Passage 2 concedes that music education develops \"fine motor skills and "
                "discipline\" -- that is agreement with some value. But it explicitly rejects "
                "the \"transfer effect to unrelated cognitive domains such as mathematics.\" "
                "So Author 2 would agree music is useful but deny the specific math-transfer "
                "claim in Passage 1. Option A captures this concede-but-deny structure. "
                "Option B is not supported by Passage 2, which never mentions genre comparisons. "
                "Option C inverts Passage 2's position -- Author 2 does not endorse STEM as a "
                "benchmark. Option D is not mentioned in either passage. Pro tip: for "
                "Author A-responds-to-Author B questions, first identify what Author B "
                "concedes and what Author B disputes, then match to an answer."
            ),
        },
        {
            "text": (
                "Passage 1: \"Space exploration has returned enormous scientific dividends: "
                "satellite technology, GPS, weather forecasting, and advances in materials "
                "science all trace roots to the space program.\"\n\n"
                "Passage 2: \"The benefits attributed to space exploration are largely "
                "overstated. GPS and satellite communications could have been developed "
                "through direct civilian research investment at a fraction of the cost.\"\n\n"
                "On which point would the authors of both passages most likely agree?"
            ),
            "difficulty": 3,
            "choices": [
                ("Space exploration has produced technologies now used in everyday life.", True),
                ("Space exploration is the most cost-effective way to develop new technology.", False),
                ("Civilian research investment is superior to government space programs.", False),
                ("Weather forecasting would not exist without the space program.", False),
            ],
            "explanation": (
                "Both passages reference GPS and satellite technology -- Passage 1 as evidence "
                "of space exploration's value, Passage 2 as technologies it claims could have "
                "been developed another way. Both authors therefore agree that these technologies "
                "exist and are connected to the space program. The disagreement is about whether "
                "space exploration deserves credit or was cost-effective. Option A is the only "
                "statement both authors would accept. Option B is contradicted by Passage 2 "
                "(which calls space exploration costly). Option C is Passage 2's implied "
                "preference but not stated in Passage 1. Option D is a specific claim from "
                "Passage 1 that Passage 2 does not address. Pro tip: agreement questions "
                "require finding the *overlap* -- what does each passage accept without dispute?"
            ),
        },
        {
            "text": (
                "Passage 1: \"Universal basic income (UBI) trials in Finland and Kenya showed "
                "that recipients used the funds responsibly: they invested in education, health, "
                "and small businesses rather than spending on alcohol or tobacco.\"\n\n"
                "Passage 2: \"UBI pilots are typically short-term and involve self-selected or "
                "small populations. Behavior observed in a two-year pilot may not predict how "
                "behavior would change under a permanent, nationwide program with different "
                "economic incentives.\"\n\n"
                "The author of Passage 2 would most likely characterize the evidence cited "
                "in Passage 1 as --"
            ),
            "difficulty": 3,
            "choices": [
                ("compelling proof that UBI should be implemented immediately", False),
                ("irrelevant because Finland and Kenya are too different from each other", False),
                ("insufficient to draw conclusions about a large-scale permanent program", True),
                ("strong evidence that UBI reduces alcohol and tobacco consumption", False),
            ],
            "explanation": (
                "Passage 2 specifically argues that short-term pilots with small or "
                "self-selected populations cannot predict behavior under a permanent, "
                "nationwide system. The Finland and Kenya trials described in Passage 1 "
                "are exactly that: pilot programs. Author 2 would therefore view Passage 1's "
                "evidence as insufficient -- interesting, perhaps, but not generalizable. "
                "Option A is the opposite of Passage 2's skeptical position. Option B "
                "introduces a geographic comparison argument that Passage 2 does not make. "
                "Option D would require Author 2 to endorse Passage 1's findings, which "
                "contradicts Passage 2's entire argument. Pro tip: Passage 2's critique "
                "is methodological (pilot vs. permanent), so the answer must reflect that "
                "specific objection."
            ),
        },
        {
            "text": (
                "Passage 1: \"The decline in cursive writing instruction has left a generation "
                "unable to read historical documents, personal letters, and legal records "
                "written before 1980 -- a significant cultural and archival loss.\"\n\n"
                "Passage 2: \"Cursive writing is a legacy skill with rapidly diminishing "
                "practical utility. In an age of keyboards and touchscreens, classroom time "
                "is better spent on digital literacy, critical thinking, and data "
                "interpretation.\"\n\n"
                "Which statement best describes the relationship between the two passages?"
            ),
            "difficulty": 2,
            "choices": [
                ("Both passages agree that cursive writing should be removed from curricula.", False),
                ("Passage 1 presents a cultural argument for cursive; Passage 2 counters with a practical argument against it.", True),
                ("Passage 1 argues from historical data; Passage 2 argues from personal experience.", False),
                ("Both passages focus primarily on the cognitive benefits of handwriting.", False),
            ],
            "explanation": (
                "Passage 1 argues that losing cursive means losing access to historical and "
                "cultural records -- a cultural preservation argument. Passage 2 argues that "
                "limited school time should go to more useful modern skills -- a practical "
                "efficiency argument. They disagree on whether cursive should be taught, and "
                "their arguments use different frames (cultural vs. practical). Option A is "
                "wrong because Passage 1 supports teaching cursive. Option C mischaracterizes "
                "the evidence: Passage 1 does not cite historical data, and Passage 2 does "
                "not use personal experience. Option D is wrong because neither passage "
                "discusses cognitive benefits of handwriting. Pro tip: identify each author's "
                "*type* of argument (cultural, economic, practical, moral) before answering."
            ),
        },
        # ── Lesson 7: SAT Craft & Structure Strategy ──────────────────────────
        {
            "text": (
                "Passage: \"The policy change was *precipitated* by a series of whistleblower "
                "reports that exposed widespread accounting irregularities at the firm.\"\n\n"
                "As used in the passage, \"precipitated\" most nearly means --"
            ),
            "difficulty": 2,
            "choices": [
                ("slowed down or delayed", False),
                ("triggered or brought about suddenly", True),
                ("discovered or uncovered through investigation", False),
                ("predicted in advance by analysts", False),
            ],
            "explanation": (
                "Context: the whistleblower reports *caused* the policy change to happen. "
                "\"Precipitated\" means triggered or brought about, often suddenly. The "
                "passage's causal structure (reports -> policy change) confirms this. "
                "\"Slowed down\" is the opposite. \"Discovered\" describes what the reports "
                "did (exposed irregularities), not what they did to the policy change. "
                "\"Predicted\" introduces a foresight meaning not supported by the text. "
                "Strategy recap: cover choices, predict (caused/triggered), then match. "
                "Pro tip: *precipitated* looks like \"precipitation\" (weather), but in "
                "formal writing it almost always means caused to happen suddenly."
            ),
        },
        {
            "text": (
                "Passage: \"For decades, the prevailing view was that dinosaurs were "
                "slow-moving, cold-blooded reptiles. Fossil evidence of growth rings, bone "
                "density, and feather impressions has since *overturned* that picture, "
                "suggesting instead that many dinosaurs were warm-blooded, fast-moving, and "
                "closely related to modern birds.\"\n\n"
                "The main purpose of the second sentence is to --"
            ),
            "difficulty": 1,
            "choices": [
                ("provide a counterexample to the revised view of dinosaurs", False),
                ("list the types of fossils discovered in North America", False),
                ("present evidence that challenges and replaces the view described in the first sentence", True),
                ("explain why scientists were mistaken about cold-blooded animals generally", False),
            ],
            "explanation": (
                "The first sentence establishes the old view (slow, cold-blooded). The "
                "second sentence introduces evidence (growth rings, bone density, feathers) "
                "and explicitly says this evidence \"overturned\" the picture, replacing it "
                "with a new view. The second sentence's job is to challenge and replace the "
                "old view. Option A is backwards -- the second sentence challenges the "
                "old view, not the new one. Option B is too specific and factually off -- "
                "no geographic location is mentioned. Option D over-generalizes: the passage "
                "is about dinosaurs specifically, not cold-blooded animals broadly. "
                "Pro tip: the word *overturned* is the structural key -- it tells you the "
                "second sentence is doing the work of revision."
            ),
        },
        {
            "text": (
                "Passage 1: \"Homework reinforces classroom learning and teaches students "
                "self-discipline and time management -- skills essential for success in "
                "higher education and professional life.\"\n\n"
                "Passage 2: \"Research on the effectiveness of homework is mixed at best. "
                "Below the high school level, studies consistently find no positive "
                "correlation between homework load and academic achievement, while excess "
                "homework is associated with increased stress and reduced family time.\"\n\n"
                "Which of the following claims from Passage 1 is most directly challenged "
                "by evidence in Passage 2?"
            ),
            "difficulty": 3,
            "choices": [
                ("Homework teaches self-discipline and time management.", False),
                ("Homework reinforces classroom learning and improves academic achievement.", True),
                ("Self-discipline is essential for success in higher education.", False),
                ("Homework prepares students for professional life.", False),
            ],
            "explanation": (
                "Passage 2 directly challenges the academic effectiveness of homework, "
                "stating there is \"no positive correlation between homework load and "
                "academic achievement\" below high school. This targets Passage 1's claim "
                "that homework \"reinforces classroom learning\" -- the academic achievement "
                "claim. Passage 2 does not provide evidence about self-discipline (Option A), "
                "higher education success (Option C), or professional preparation (Option D) "
                "-- those claims from Passage 1 are simply not addressed. The rule: a claim "
                "is *challenged* only if the other passage provides *evidence against it*, "
                "not just silence. Pro tip: map each claim in Passage 1 to what Passage 2 "
                "says about it before choosing."
            ),
        },
        {
            "text": (
                "Passage: \"The auditors' report was *equivocal*: it neither confirmed nor "
                "denied that funds had been misappropriated, citing insufficient documentation "
                "to reach a definitive conclusion.\"\n\n"
                "As used in the passage, \"equivocal\" most nearly means --"
            ),
            "difficulty": 2,
            "choices": [
                ("dishonest and deliberately misleading", False),
                ("ambiguous and open to multiple interpretations", True),
                ("thorough and methodically detailed", False),
                ("critical and strongly worded", False),
            ],
            "explanation": (
                "The passage explains what the report was: it \"neither confirmed nor denied\" "
                "and cited \"insufficient documentation.\" The report did not take a clear "
                "stance. \"Ambiguous and open to multiple interpretations\" captures that "
                "meaning. \"Dishonest\" adds a moral judgment the passage does not support -- "
                "the auditors said they lacked documentation, not that they were hiding "
                "something. \"Thorough and methodically detailed\" contradicts \"insufficient "
                "documentation.\" \"Critical and strongly worded\" contradicts the neutral, "
                "indeterminate tone described. Strategy recap: the context clue is \"neither "
                "confirmed nor denied\" -- that phrase directly defines *equivocal*. "
                "Pro tip: when the passage defines the word for you with surrounding context, "
                "trust that definition over any memorized vocabulary knowledge."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed the SAT Reading & Writing: Craft & Structure deep-dive course"

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
            Lesson.objects.create(
                course=course, title=title, content=content, order=order
            )
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
                f"Created '{course.title}' with {len(COURSE['lessons'])} lessons "
                f"and {len(COURSE['mcqs'])} questions."
            )
        )
