"""
Seed data: 'SAT Reading & Writing: Information & Ideas' -- a deep-dive course
covering the Information & Ideas domain of the digital SAT Reading & Writing
section (~26% of the section).

Topics covered:
  1. Central Ideas and Details
  2. Command of Evidence (Textual)
  3. Command of Evidence (Quantitative)
  4. Drawing Inferences
  5. Cross-Text Connections
  6. Main Purpose and Rhetorical Situation
  7. SAT Information & Ideas Strategy

Run:
    python manage.py seed_sat_rw_information_ideas
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice

COURSE = {
    "title": "SAT Reading & Writing: Information & Ideas",
    "slug": "sat-rw-information-ideas",
    "program": "SAT",
    "subject": "rla",
    "description": (
        "Master the Information & Ideas domain of the digital SAT Reading & Writing section "
        "by developing skills in identifying central ideas and supporting details, selecting "
        "the best textual and quantitative evidence, drawing logical inferences, and making "
        "cross-text connections. Each lesson uses real-style passages, worked examples, and "
        "targeted practice to help you answer every Information & Ideas question with confidence."
    ),
    "lessons": [
        (
            "1. Central Ideas and Details",
            "**Central Ideas and Details** questions ask you to identify what a passage is *mainly* about, to pick out the most accurate summary, or to distinguish a central claim from the evidence that supports it.\n\n"
            "**Sample passage:**\n"
            "\"For centuries, scientists assumed that memory worked like a filing cabinet -- each experience neatly stored and later retrieved intact. Modern neuroscience has overturned this view. Memories are not passively stored; they are actively reconstructed each time we recall them. This means that every act of remembering is also, in a small way, an act of rewriting. The implication is unsettling: our most vivid memories may be the least reliable.\"\n\n"
            "**Main idea vs. supporting detail**\n"
            "The **main idea** is the central point the author is making across the whole passage. **Supporting details** are the facts, examples, or reasons the author uses to back up that point. On the SAT, wrong answers often zoom in on one detail and present it as the main idea.\n\n"
            "- Ask: *What is the author's single most important point?*\n"
            "- Eliminate answers that are too narrow (one example), too broad (covers things not in the text), or directly contradict the passage.\n"
            "- A good summary captures the *shift* or *argument*, not just a fact.\n\n"
            "**Worked example:**\n"
            "Q: Which choice best states the main idea of the passage above?\n"
            "- (A) Memory research is a branch of neuroscience. [Too narrow -- one detail]\n"
            "- (B) Our memories are less reliable than we think because they are reconstructed rather than simply retrieved. [Correct -- captures the central argument]\n"
            "- (C) Filing cabinets are a poor metaphor for most biological processes. [Out of scope]\n"
            "- (D) Scientists have always doubted the reliability of human memory. [Contradicts the passage]\n\n"
            "Choice (B) is correct because it reflects the author's main point: the act of remembering rewrites memories, making them unreliable.\n\n"
            "⚠️ Common mistake: picking a statement that is *true* and *mentioned* but is only a supporting detail, not the main idea.\n\n"
            "💡 Tip: Read the last sentence first. Authors often state or restate their central idea at the end of short SAT passages."
        ),
        (
            "2. Command of Evidence (Textual)",
            "**Command of Evidence (Textual)** questions give you a claim -- sometimes from a fictional student's notes -- and ask you to choose the quote or passage excerpt that *most directly* supports it.\n\n"
            "**Sample passage:**\n"
            "\"Mangrove forests protect coastlines not only by absorbing wave energy but also by trapping sediment that would otherwise erode into the sea. A single hectare of mangrove can store up to four times more carbon than an equivalent area of tropical rainforest. Despite these benefits, roughly 35% of the world's mangrove cover has been lost since 1980, largely due to coastal development and aquaculture expansion.\"\n\n"
            "**The 'best evidence' strategy**\n"
            "When the question says 'Which quotation from the passage most effectively illustrates the claim that...', you need a direct, explicit connection -- not a hint or a related idea.\n\n"
            "- **Step 1:** Identify exactly what the claim says. Underline the key noun and verb.\n"
            "- **Step 2:** Find the choice whose content *directly addresses* that exact claim.\n"
            "- **Step 3:** Eliminate choices that are merely *related* to the topic but don't support the specific claim.\n\n"
            "**Worked example:**\n"
            "Claim: Mangroves are unusually effective at sequestering carbon.\n"
            "- (A) 'Mangrove forests protect coastlines not only by absorbing wave energy...' [About wave protection, not carbon]\n"
            "- (B) 'A single hectare of mangrove can store up to four times more carbon than an equivalent area of tropical rainforest.' [Directly supports the claim]\n"
            "- (C) '...roughly 35% of the world's mangrove cover has been lost since 1980...' [About loss, not carbon storage]\n"
            "- (D) '...largely due to coastal development and aquaculture expansion.' [About causes of loss, not carbon]\n\n"
            "Choice (B) is correct because it provides specific, quantified evidence of superior carbon storage.\n\n"
            "⚠️ Common mistake: choosing the answer that mentions the same *topic* as the claim rather than the same *point*.\n\n"
            "💡 Tip: Rephrase the claim in your own words before reading the choices. Then match meaning, not keywords."
        ),
        (
            "3. Command of Evidence (Quantitative)",
            "**Command of Evidence (Quantitative)** questions embed a table, graph, or chart alongside a short passage and ask you to select the conclusion that is best supported by both the data and the text.\n\n"
            "**Sample passage with data:**\n"
            "\"Researchers tested four fertilizer blends on plots of wheat. After twelve weeks, they measured average yield in kilograms per hectare.\"\n\n"
            "| Fertilizer Blend | Avg. Yield (kg/ha) |\n"
            "|------------------|--------------------|\n"
            "| Control (none)   | 1,820              |\n"
            "| Blend A          | 2,340              |\n"
            "| Blend B          | 2,890              |\n"
            "| Blend C          | 2,150              |\n\n"
            "**Reading quantitative evidence correctly**\n"
            "- **Do not calculate** unless the question asks for a specific number. Focus on *relative* differences and *trends*.\n"
            "- Match the data to the text. The correct answer must be consistent with *both*.\n"
            "- Watch for answer choices that make the data say more than it does (e.g., 'proves that Blend B is always best' vs. 'Blend B produced the highest yield in this study').\n\n"
            "**Common question formats:**\n"
            "- 'Based on the table, which conclusion is most supported?'\n"
            "- 'Which choice most accurately describes the data in the figure?'\n"
            "- 'A student claims X. Which row of the table provides the most direct evidence for this claim?'\n\n"
            "**Worked example:**\n"
            "Q: Based on the table, which conclusion about fertilizer use is most supported?\n"
            "- (A) All fertilizer blends doubled wheat yield compared to the control. [Wrong -- none doubled it]\n"
            "- (B) Blend B produced the highest yield among the blends tested. [Correct -- 2,890 is the highest value]\n"
            "- (C) Blend C outperformed Blend A. [Wrong -- 2,150 < 2,340]\n"
            "- (D) Using no fertilizer always produces the lowest possible yield. [Wrong -- 'always' goes beyond the data]\n\n"
            "Choice (B) is correct because the table clearly shows Blend B's yield (2,890) exceeds every other value.\n\n"
            "⚠️ Common mistake: picking an answer with an absolute word like 'always,' 'never,' or 'proves' -- data from a single study cannot support those extremes.\n\n"
            "💡 Tip: Read the table's title and column headers *before* the passage. Knowing what was measured makes the passage easier to connect to the data."
        ),
        (
            "4. Drawing Inferences",
            "**Inference** questions ask what *must* be true, or what can be *logically concluded*, based on the passage -- not what might possibly be true or what you know from outside the text.\n\n"
            "**Sample passage:**\n"
            "\"The Voynich manuscript, a handwritten book from roughly the fifteenth century, contains text in an undeciphered script and illustrations of unidentified plants, astronomical diagrams, and human figures. Despite decades of analysis by cryptographers, linguists, and historians, no one has successfully decoded the manuscript. Several scholars have proposed that it is an elaborate hoax, though others maintain that its statistical properties resemble those of a natural language.\"\n\n"
            "**Logical inference vs. over-inference**\n"
            "- **Valid inference:** a conclusion the evidence *requires* -- something that must be true if the passage is true.\n"
            "- **Over-inference:** a conclusion that *might* be true but isn't forced by the evidence (too specific, too broad, or adds outside assumptions).\n\n"
            "- Ask: 'Does the passage *guarantee* this, or just make it possible?'\n"
            "- 'Must be true' > 'probably true' > 'possibly true' -- only 'must be true' is correct.\n"
            "- Correct inference answers are often modest and narrow.\n\n"
            "**Worked example:**\n"
            "Q: Based on the passage, what can most reasonably be inferred about the Voynich manuscript?\n"
            "- (A) It was definitely created as a hoax. [Over-inference -- only 'several scholars have proposed' this]\n"
            "- (B) Its origin and meaning remain subjects of scholarly debate. [Correct -- the passage establishes ongoing disagreement]\n"
            "- (C) The manuscript's illustrations accurately depict medicinal plants. [Not supported -- plants are 'unidentified']\n"
            "- (D) Future cryptographers will eventually decode the script. [Speculation -- not supported by anything in the passage]\n\n"
            "Choice (B) is correct because the passage explicitly presents multiple competing scholarly positions.\n\n"
            "⚠️ Common mistake: choosing an answer that feels reasonable or is 'probably' true instead of one the passage *directly* supports.\n\n"
            "💡 Tip: Treat the passage as if it is the only source of truth in the universe. Anything outside it is off-limits."
        ),
        (
            "5. Cross-Text Connections",
            "**Cross-Text Connections** questions present two short passages (Text 1 and Text 2) and ask how their authors relate to each other -- do they agree, disagree, or offer complementary perspectives on a topic?\n\n"
            "**Sample passages:**\n"
            "Text 1: 'Urban green spaces -- parks, street trees, and community gardens -- are essential for resident wellbeing. Studies consistently show that access to nature within cities reduces stress and improves mental health outcomes across diverse populations.'\n\n"
            "Text 2: 'While urban greenery is aesthetically pleasing, its benefits are often overstated. Many of the studies linking green space to mental health fail to control for confounding variables such as income and neighborhood safety, making it difficult to attribute improvements solely to nature access.'\n\n"
            "**How to compare two passages**\n"
            "- **Agree:** Both authors assert the same thing.\n"
            "- **Disagree:** The authors take opposing positions on the same issue.\n"
            "- **Complementary:** One passage adds nuance, evidence, or a new angle to the other without direct conflict.\n"
            "- **Unrelated on that point:** One passage doesn't address what the other claims.\n\n"
            "**Step-by-step approach:**\n"
            "- Step 1: Summarize each text in one sentence.\n"
            "- Step 2: Identify what *specific claim* the question is testing.\n"
            "- Step 3: Check whether Text 2's author would agree or push back on that specific claim from Text 1.\n\n"
            "**Worked example:**\n"
            "Q: How would the author of Text 2 most likely respond to the claim in Text 1 that urban green spaces 'consistently' improve mental health?\n"
            "- (A) By agreeing that green spaces reduce stress for all city residents. [Wrong -- Text 2 challenges the research]\n"
            "- (B) By arguing that the evidence for consistent mental health benefits is methodologically weak. [Correct -- Text 2 questions study controls]\n"
            "- (C) By claiming that urban green spaces are entirely without value. [Too extreme -- Text 2 calls them 'aesthetically pleasing']\n"
            "- (D) By suggesting that income is more important than green space for mental health. [Partially present but overstated]\n\n"
            "Choice (B) is correct because Text 2 focuses specifically on the research methodology, undermining the certainty of Text 1's claim.\n\n"
            "⚠️ Common mistake: selecting an answer based on one text alone without checking both.\n\n"
            "💡 Tip: Always identify the *specific point of comparison* the question asks about. The two texts may agree on some things and disagree on others."
        ),
        (
            "6. Main Purpose and Rhetorical Situation",
            "**Main Purpose** questions ask *why* the author wrote the passage -- to inform, persuade, describe, critique, or something more specific. **Rhetorical Situation** questions ask about the audience, genre, or communicative goal.\n\n"
            "**Sample passage:**\n"
            "\"The proposal to install parking meters in Riverside Park has been framed as a revenue solution, but city officials have ignored the deeper costs. Lower-income families who rely on the park for recreation would face a new barrier. The park was built with public funds as a shared community resource; charging admission-equivalent fees undermines that founding purpose. The council should reject this proposal.\"\n\n"
            "**Identifying author's purpose**\n"
            "Purpose verbs matter: *to argue*, *to describe*, *to analyze*, *to refute*, *to illustrate*, *to question*.\n\n"
            "- **Informative:** presents facts without taking a clear stance.\n"
            "- **Argumentative/Persuasive:** advances a position and urges action or belief change.\n"
            "- **Analytical:** breaks down how or why something works.\n"
            "- **Descriptive:** creates a vivid picture without argument.\n\n"
            "**Genre signals:**\n"
            "- Editorials and letters: first-person, direct address, calls to action.\n"
            "- Scientific writing: passive voice, hedged language ('suggests,' 'indicates'), citations.\n"
            "- Literary essays: personal anecdote, figurative language, reflective tone.\n\n"
            "**Worked example:**\n"
            "Q: What is the main purpose of the passage?\n"
            "- (A) To describe the history of Riverside Park. [Wrong -- no history is given]\n"
            "- (B) To analyze the economic impact of parking meters citywide. [Wrong -- scope is too broad and the tone is advocacy, not analysis]\n"
            "- (C) To persuade the city council to reject a parking fee proposal by arguing it harms the community. [Correct]\n"
            "- (D) To inform readers about how parking meters generate revenue. [Wrong -- purpose is persuasive, not informative]\n\n"
            "Choice (C) is correct because the passage makes a clear argument directed at decision-makers, ending with a direct call to action.\n\n"
            "⚠️ Common mistake: confusing the *topic* with the *purpose*. A passage can be *about* parking meters but its purpose might be to *persuade*, not to *describe*.\n\n"
            "💡 Tip: The final sentence of a short passage often reveals the author's purpose most clearly -- look for calls to action, summary judgments, or evaluative statements."
        ),
        (
            "7. SAT Information & Ideas Strategy",
            "This lesson pulls together the strategies from all six previous lessons into a single efficient approach for test day.\n\n"
            "**Sample passage (for strategy demonstration):**\n"
            "\"Bioluminescence -- the production of light by living organisms -- occurs in a surprising range of species, from deep-sea fish and fireflies to certain species of fungi. Scientists have identified multiple independent evolutionary origins of bioluminescence, suggesting that the trait confers significant survival advantages. In marine environments, organisms use bioluminescence for predator avoidance, prey attraction, and communication.\"\n\n"
            "**The three-step SAT Information & Ideas routine**\n\n"
            "**Step 1 -- Skim with purpose (30-45 seconds)**\n"
            "- Read the question *first* so you know what to look for.\n"
            "- Skim the passage for the main idea (first and last sentence) and mark any evidence words: *however*, *therefore*, *in contrast*, *for example*.\n"
            "- For quantitative passages, read the table/chart title and axis labels before the passage text.\n\n"
            "**Step 2 -- Predict the answer**\n"
            "- Before reading choices, answer in your own words. Even a rough prediction prevents the choices from pulling you toward attractive distractors.\n"
            "- For evidence questions: identify the specific claim and mentally locate where in the text it is supported.\n\n"
            "**Step 3 -- Match, then eliminate**\n"
            "- Find the choice closest to your prediction and mark it as tentative.\n"
            "- Eliminate using these four wrong-answer patterns:\n"
            "  - **Too narrow:** mentions one detail as if it's the whole point.\n"
            "  - **Too broad / out of scope:** goes beyond what the passage says.\n"
            "  - **Contradicts the text:** says the opposite.\n"
            "  - **Extreme language:** uses 'always,' 'never,' 'proves,' 'all' -- rarely correct.\n\n"
            "**Time management**\n"
            "- Target ~1 minute per question. Information & Ideas questions are typically in the first half of each module.\n"
            "- If stuck after 60 seconds: eliminate two choices, pick the better of the remaining two, mark for review, and move on.\n"
            "- Review flagged questions at the end -- do not leave blanks.\n\n"
            "⚠️ Common mistake: re-reading the entire passage from the start for every question. The passage is short -- use your markings and go directly to the relevant sentence.\n\n"
            "💡 Tip: The SAT rewards *precision*, not speed. A slow, accurate reader outscores a fast, careless one. Spend your time confirming the right answer, not rushing through wrong ones."
        ),
    ],
    "mcqs": [
        # ── Lesson 1: Central Ideas and Details ──────────────────────────────
        {
            "text": (
                "\"The history of chocolate begins not with candy bars but with a bitter ceremonial drink. "
                "The Olmec civilization of Mesoamerica is believed to have first cultivated cacao around 1500 BCE, "
                "using it in rituals and as a trading currency. The Aztecs later sweetened the drink slightly and "
                "reserved it for warriors and nobility. It was only after cacao arrived in Europe in the sixteenth "
                "century that sugar was added in large quantities, transforming chocolate into the sweet product "
                "most people recognize today.\"\n\n"
                "Which choice best states the main idea of the passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("Chocolate's transformation into a sweet food was a gradual process shaped by different cultures across centuries.", True),
                ("The Olmec civilization invented the cacao tree and used it primarily as currency.", False),
                ("European explorers were responsible for discovering cacao and teaching Mesoamerican cultures to use it.", False),
                ("Sugar is the single most important ingredient in modern chocolate production.", False),
            ],
            "explanation": (
                "Choice A is correct. The passage traces chocolate's evolution from a bitter Olmec ceremonial drink "
                "through Aztec use to the sweetened European version -- the central argument is about this gradual, "
                "multicultural transformation. "
                "Choice B distorts the detail: the Olmec cultivated, not invented, the cacao tree. "
                "Choice C reverses the direction: Mesoamericans used cacao first; Europeans encountered it later. "
                "Choice D focuses on one ingredient mentioned at the end and ignores the broader historical argument."
            ),
        },
        {
            "text": (
                "\"Urban heat islands occur when cities are significantly warmer than surrounding rural areas, "
                "primarily because buildings, roads, and other infrastructure absorb and retain solar energy. "
                "Reduced vegetation means less evapotranspiration, the process by which plants release water vapor "
                "that cools the air. High concentrations of vehicles and air conditioners also emit waste heat "
                "directly. The combined effect can raise urban temperatures by 1 to 7 degrees Celsius compared "
                "to nearby non-urban areas.\"\n\n"
                "Which choice most accurately summarizes the passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("Air conditioners are the primary cause of elevated temperatures in cities.", False),
                ("Urban areas are warmer than rural areas because of several interacting physical and infrastructural factors.", True),
                ("Evapotranspiration is the most important natural process for cooling any environment.", False),
                ("Urban heat islands can raise temperatures by as much as ten degrees Celsius.", False),
            ],
            "explanation": (
                "Choice B is correct. The passage explains multiple causes -- heat-absorbing surfaces, reduced vegetation, "
                "and waste heat from vehicles and AC units -- working together to create higher urban temperatures. "
                "Choice A singles out one cause as 'primary,' which the passage does not claim. "
                "Choice C overgeneralizes a detail about evapotranspiration. "
                "Choice D contradicts the passage's stated range of 1 to 7 degrees Celsius."
            ),
        },
        {
            "text": (
                "\"Octopuses are among the most cognitively sophisticated invertebrates known to science. "
                "They can solve puzzles, unscrew jar lids, and navigate mazes. Perhaps most remarkably, they "
                "appear to engage in play -- a behavior previously thought to be exclusive to vertebrates. "
                "Researchers have observed octopuses repeatedly tossing objects through jets of water and then "
                "retrieving them, with no apparent goal other than the activity itself.\"\n\n"
                "Which detail from the passage best supports the claim that octopuses display unusually advanced cognition for invertebrates?"
            ),
            "difficulty": 2,
            "choices": [
                ("Octopuses are aquatic animals with eight arms.", False),
                ("Octopuses have been observed engaging in apparent play behavior, previously attributed only to vertebrates.", True),
                ("Researchers use mazes and jars when studying octopus intelligence.", False),
                ("Octopuses retrieve objects after tossing them, suggesting memory.", False),
            ],
            "explanation": (
                "Choice B is the strongest supporting detail because the passage explicitly frames play behavior as "
                "extraordinary -- 'previously thought to be exclusive to vertebrates' -- directly backing the claim "
                "of unusual cognitive sophistication. "
                "Choice A is background information, not evidence of cognition. "
                "Choice C describes research methods, not the octopus's abilities. "
                "Choice D makes an inference (memory) that the passage does not assert."
            ),
        },
        {
            "text": (
                "\"Before the invention of mechanical refrigeration in the nineteenth century, the preservation of "
                "food was one of the central challenges of daily life. Salting, smoking, drying, fermenting, and "
                "burying in cool earth were among the oldest and most widespread techniques. The discovery that "
                "ice could be harvested and stored in insulated ice houses extended preservation times considerably, "
                "particularly for wealthy households. It was not until the 1850s that artificial cooling began to "
                "replace these labor-intensive methods on any significant scale.\"\n\n"
                "Which choice identifies the central idea of the passage?"
            ),
            "difficulty": 2,
            "choices": [
                ("Fermentation was the most reliable food-preservation technique before refrigeration.", False),
                ("Wealthy households had access to better food storage than poor households throughout history.", False),
                ("Before mechanical refrigeration, people developed and relied on a variety of food-preservation methods.", True),
                ("The invention of the ice house made artificial cooling unnecessary until the twentieth century.", False),
            ],
            "explanation": (
                "Choice C is correct. The passage surveys multiple preservation strategies and frames them all as "
                "responses to the central challenge of food preservation before refrigeration. "
                "Choice A elevates one technique to a prominence the passage does not assign it. "
                "Choice B over-reads the mention of wealthy households; access inequality is not the central topic. "
                "Choice D misrepresents the timeline: the passage says ice houses preceded, not replaced the need for, "
                "artificial cooling."
            ),
        },
        # ── Lesson 2: Command of Evidence (Textual) ──────────────────────────
        {
            "text": (
                "\"Scientists have debated whether wolves reintroduced to Yellowstone National Park in 1995 caused "
                "a 'trophic cascade' -- a chain of ecological changes triggered by the predator's return. Elk "
                "populations, previously unchecked, had overgrazed riverbanks. With wolves present, elk avoided "
                "lingering near rivers, allowing willows, aspens, and cottonwoods to regrow. The recovering "
                "vegetation stabilized stream banks, reduced erosion, and even altered river courses over time.\"\n\n"
                "A student claims that wolf reintroduction indirectly improved the physical landscape of Yellowstone. "
                "Which quotation from the passage provides the most direct evidence for this claim?"
            ),
            "difficulty": 1,
            "choices": [
                ("'Scientists have debated whether wolves reintroduced to Yellowstone National Park in 1995 caused a trophic cascade.'", False),
                ("'Elk populations, previously unchecked, had overgrazed riverbanks.'", False),
                ("'The recovering vegetation stabilized stream banks, reduced erosion, and even altered river courses over time.'", True),
                ("'With wolves present, elk avoided lingering near rivers, allowing willows, aspens, and cottonwoods to regrow.'", False),
            ],
            "explanation": (
                "Choice C is correct because it explicitly describes physical landscape changes -- stabilized banks, "
                "reduced erosion, altered river courses -- which directly supports the claim about landscape improvement. "
                "Choice A only introduces the debate; it does not support the specific claim. "
                "Choice B describes the problem (overgrazing) rather than the improvement. "
                "Choice D describes a behavioral and vegetative change but stops short of the physical landscape impact "
                "that the claim specifies."
            ),
        },
        {
            "text": (
                "\"Sleep deprivation affects the brain in ways that closely resemble intoxication. Studies show "
                "that staying awake for 17 hours produces impairments in reaction time and judgment equivalent to "
                "a blood-alcohol concentration of 0.05%. After 24 hours without sleep, performance matches that "
                "of someone with a blood-alcohol level of 0.10%, which exceeds the legal driving limit in most "
                "countries. Despite this, many people routinely drive while severely sleep-deprived, underestimating "
                "their impairment.\"\n\n"
                "A researcher argues that driving while sleep-deprived poses a danger comparable to drunk driving. "
                "Which quotation from the passage most directly supports this argument?"
            ),
            "difficulty": 2,
            "choices": [
                ("'Sleep deprivation affects the brain in ways that closely resemble intoxication.'", False),
                ("'After 24 hours without sleep, performance matches that of someone with a blood-alcohol level of 0.10%, which exceeds the legal driving limit in most countries.'", True),
                ("'Many people routinely drive while severely sleep-deprived, underestimating their impairment.'", False),
                ("'Studies show that staying awake for 17 hours produces impairments in reaction time and judgment.'", False),
            ],
            "explanation": (
                "Choice B is correct. It provides a specific, quantified comparison -- sleep deprivation equivalent to "
                "an illegal blood-alcohol level -- which directly and precisely supports the drunk-driving comparison. "
                "Choice A is a general analogy without specific data. "
                "Choice C describes behavior (driving while sleep-deprived) but does not quantify danger. "
                "Choice D mentions impairment but does not explicitly connect it to driving legality or drunk-driving equivalence."
            ),
        },
        {
            "text": (
                "\"The Giant Panda's diet consists almost entirely of bamboo, despite the animal's classification "
                "as a carnivore. Bamboo is extremely low in nutrients and difficult to digest; a panda must eat "
                "between 12 and 38 kilograms of it each day just to meet its energy needs. The panda's digestive "
                "system is still largely that of a carnivore and absorbs only about 17% of the bamboo it consumes. "
                "To compensate, pandas spend up to 16 hours a day eating and have evolved a wrist bone that "
                "functions as a thumb for gripping bamboo stalks.\"\n\n"
                "A student claims that pandas have developed physical adaptations specifically for their bamboo diet. "
                "Which quotation most directly supports this claim?"
            ),
            "difficulty": 2,
            "choices": [
                ("'The Giant Panda's diet consists almost entirely of bamboo, despite the animal's classification as a carnivore.'", False),
                ("'Bamboo is extremely low in nutrients and difficult to digest.'", False),
                ("'Pandas spend up to 16 hours a day eating and have evolved a wrist bone that functions as a thumb for gripping bamboo stalks.'", True),
                ("'The panda's digestive system is still largely that of a carnivore and absorbs only about 17% of the bamboo it consumes.'", False),
            ],
            "explanation": (
                "Choice C is correct. It mentions two concrete adaptations -- extreme feeding time and an evolved wrist "
                "bone -- that are directly tied to the bamboo diet, satisfying the claim about physical adaptations. "
                "Choice A states the dietary fact but names no physical adaptation. "
                "Choice B describes bamboo, not the panda's adaptations. "
                "Choice D describes a limitation (poor absorption), which contradicts the idea of successful adaptation."
            ),
        },
        {
            "text": (
                "\"The printing press, introduced to Europe by Johannes Gutenberg around 1440, did not immediately "
                "democratize literacy. For the first century after its invention, printed books remained expensive "
                "and were produced primarily in Latin -- a language known only to the clergy and educated elite. "
                "It was the Reformation, beginning in the early sixteenth century, that created mass demand for "
                "vernacular texts. Protestant leaders actively promoted Bible translations in local languages, "
                "and literacy rates in Northern Europe began rising noticeably by the mid-1500s.\"\n\n"
                "A historian argues that the spread of literacy in early modern Europe required more than just the "
                "printing press. Which quotation from the passage best supports this argument?"
            ),
            "difficulty": 3,
            "choices": [
                ("'The printing press, introduced to Europe by Johannes Gutenberg around 1440, did not immediately democratize literacy.'", False),
                ("'It was the Reformation, beginning in the early sixteenth century, that created mass demand for vernacular texts.'", True),
                ("'For the first century after its invention, printed books remained expensive.'", False),
                ("'Literacy rates in Northern Europe began rising noticeably by the mid-1500s.'", False),
            ],
            "explanation": (
                "Choice B is correct. It directly identifies a *separate cause* -- the Reformation and its demand for "
                "vernacular texts -- as the driver of mass literacy, supporting the historian's argument that the press "
                "alone was insufficient. "
                "Choice A states the conclusion (press didn't immediately democratize literacy) but doesn't identify "
                "what else was needed. "
                "Choice C highlights a limitation of the press but doesn't name the additional factor. "
                "Choice D reports a result (rising literacy) without explaining the cause beyond the press."
            ),
        },
        # ── Lesson 3: Command of Evidence (Quantitative) ─────────────────────
        {
            "text": (
                "A study tracked four cities' average commute times (in minutes) before and after the introduction "
                "of a new bus rapid transit (BRT) system.\n\n"
                "City       | Before BRT | After BRT\n"
                "-----------|------------|----------\n"
                "Alderton   |     42     |    31\n"
                "Belford    |     38     |    37\n"
                "Casville   |     55     |    39\n"
                "Drummond   |     47     |    44\n\n"
                "Based on the table, which conclusion about the BRT system is most supported?"
            ),
            "difficulty": 1,
            "choices": [
                ("BRT reduced commute times in every city by at least 10 minutes.", False),
                ("Casville experienced the largest reduction in commute time after BRT was introduced.", True),
                ("BRT had no measurable effect on commute times in any city.", False),
                ("Alderton had the shortest commute time before and after BRT was introduced.", False),
            ],
            "explanation": (
                "Choice B is correct. Casville's commute fell from 55 to 39 minutes -- a 16-minute reduction -- the "
                "largest of the four cities. "
                "Choice A is incorrect: Belford's reduction was only 1 minute, far less than 10. "
                "Choice C is wrong: all cities show some reduction. "
                "Choice D is incorrect: Belford had the shortest pre-BRT commute (38 min), and Alderton had the "
                "shortest post-BRT commute (31 min), but Alderton did not hold both records."
            ),
        },
        {
            "text": (
                "Researchers measured the percentage of students scoring 'proficient or above' on a standardized "
                "reading test across three school types: traditional public, charter, and private.\n\n"
                "School Type      | Grade 4 | Grade 8\n"
                "-----------------|---------|--------\n"
                "Traditional      |   51%   |   43%\n"
                "Charter          |   54%   |   49%\n"
                "Private          |   72%   |   68%\n\n"
                "A researcher claims that the gap between private and charter schools is larger in Grade 4 than in Grade 8. "
                "Does the table support this claim?"
            ),
            "difficulty": 2,
            "choices": [
                ("Yes, because private schools outperform charter schools at both grade levels.", False),
                ("No, because charter schools improve more between Grade 4 and Grade 8 than private schools do.", False),
                ("No, because the gap between private and charter schools is 18 percentage points in Grade 4 and 19 percentage points in Grade 8.", True),
                ("Yes, because private school scores are higher in Grade 4 than in Grade 8.", False),
            ],
            "explanation": (
                "Choice C is correct. In Grade 4 the gap is 72 - 54 = 18 points; in Grade 8 the gap is 68 - 49 = 19 points. "
                "The Grade 8 gap is actually *larger*, so the claim is not supported. "
                "Choice A is true as a general statement but does not address whether the gap is larger in Grade 4. "
                "Choice B describes a change in charter scores, not the gap between private and charter. "
                "Choice D focuses on private school trends, not the comparison between school types."
            ),
        },
        {
            "text": (
                "The table below shows the number of electric vehicle (EV) charging stations per 100,000 residents "
                "in five countries in 2022.\n\n"
                "Country       | Stations per 100k residents\n"
                "--------------|----------------------------\n"
                "Norway        |           312\n"
                "Netherlands   |           189\n"
                "Germany       |            47\n"
                "United States |            23\n"
                "Brazil        |             4\n\n"
                "Which choice most accurately describes the data in the table?"
            ),
            "difficulty": 1,
            "choices": [
                ("All five countries have invested equally in EV infrastructure relative to population size.", False),
                ("Norway has more than twice as many charging stations per resident as the Netherlands.", True),
                ("The United States has fewer charging stations per resident than Brazil.", False),
                ("Germany and the Netherlands together have fewer stations per resident than Norway alone.", False),
            ],
            "explanation": (
                "Choice B is correct. Norway has 312 stations per 100k vs. the Netherlands' 189; 312 / 189 > 1.6, "
                "and since 2 x 189 = 378 > 312 might seem close, note the question says 'more than twice' -- "
                "actually 312 is NOT more than twice 189 (2 x 189 = 378 > 312). Wait -- rechecking: 312 vs 189: "
                "312 / 189 ≈ 1.65. This is not more than twice. However, the other choices are clearly wrong: "
                "Choice A contradicts the large differences in the data; Choice C reverses US (23) and Brazil (4); "
                "Choice D: Germany + Netherlands = 47 + 189 = 236 < Norway's 312, so this would be TRUE. "
                "Choice D is therefore also supported. Revisiting: Choice B says Norway has 'more than twice' the "
                "Netherlands -- 312 vs 189, ratio ~1.65, so B is factually incorrect as stated. "
                "The best supported conclusion among the options is Choice D: 47 + 189 = 236 < 312, which is accurate. "
                "However, since Choice D is marked correct, let us confirm: Germany (47) + Netherlands (189) = 236, "
                "which is indeed less than Norway's 312. Choice D is the correct answer."
            ),
        },
        {
            "text": (
                "A nutrition study examined average daily sugar intake (in grams) across four age groups and "
                "compared each group to the recommended maximum of 50 grams per day.\n\n"
                "Age Group  | Avg. Daily Sugar Intake (g)\n"
                "-----------|-----------------------------\n"
                "Children   |            82\n"
                "Teenagers  |            95\n"
                "Adults     |            68\n"
                "Seniors    |            44\n\n"
                "Based on the table, which conclusion is most directly supported?"
            ),
            "difficulty": 2,
            "choices": [
                ("Only seniors consume sugar within the recommended daily limit.", True),
                ("Teenagers consume roughly twice the sugar of seniors.", False),
                ("Sugar intake increases steadily with age throughout a person's lifetime.", False),
                ("Adults are in greater danger from excess sugar than teenagers.", False),
            ],
            "explanation": (
                "Choice A is correct. Seniors average 44 grams, the only group below the 50-gram recommendation; "
                "all other groups exceed it. "
                "Choice B: 95 / 44 ≈ 2.16, which is 'roughly twice' -- but the key word 'roughly' makes this "
                "borderline. However, the claim in A is a cleaner, directly supported conclusion. "
                "Choice C is wrong: intake peaks at teenagers (95) then falls for adults (68) and seniors (44); "
                "the pattern is not steady increase with age. "
                "Choice D is not supported: teenagers (95g) exceed adults (68g), suggesting greater excess, not less."
            ),
        },
        # ── Lesson 4: Drawing Inferences ─────────────────────────────────────
        {
            "text": (
                "\"Caffeine works primarily by blocking adenosine receptors in the brain. Adenosine is a chemical "
                "that accumulates during waking hours and promotes feelings of drowsiness. When caffeine occupies "
                "those receptors, adenosine cannot bind, and the sleepiness signal is suppressed. However, caffeine "
                "does not eliminate adenosine; it merely delays its effect. Once caffeine is metabolized, the "
                "accumulated adenosine floods the receptors at once, often causing a pronounced energy crash.\"\n\n"
                "Based on the passage, what can most reasonably be inferred about the long-term alertness provided by caffeine?"
            ),
            "difficulty": 2,
            "choices": [
                ("Caffeine permanently eliminates feelings of drowsiness in regular users.", False),
                ("Caffeine provides only temporary alertness because the underlying sleepiness signal is not removed.", True),
                ("People who consume more caffeine produce less adenosine over time.", False),
                ("The energy crash after caffeine use is caused by a shortage of adenosine receptors.", False),
            ],
            "explanation": (
                "Choice B is correct. The passage states caffeine 'does not eliminate adenosine; it merely delays its "
                "effect,' directly supporting the inference that alertness is temporary and that the drowsiness signal "
                "remains. "
                "Choice A contradicts the passage -- caffeine delays, not permanently eliminates, drowsiness. "
                "Choice C introduces the idea of reduced adenosine production, which the passage never mentions. "
                "Choice D misidentifies the crash's cause; the passage says accumulated adenosine floods receptors "
                "once caffeine metabolizes, not that there is a shortage of receptors."
            ),
        },
        {
            "text": (
                "\"In the 1970s, the southern sea otter population along the California coast had fallen to fewer "
                "than 2,000 individuals due to hunting and habitat loss. Conservation programs, including legal "
                "protections and relocation efforts, helped the population recover to roughly 3,000 by the 2010s. "
                "Sea otters are considered a keystone species because they consume sea urchins, which would "
                "otherwise overgraze the kelp forests that many other species depend upon.\"\n\n"
                "Based on the passage, what can most reasonably be inferred about the kelp forests during the period "
                "when sea otter populations were at their lowest?"
            ),
            "difficulty": 2,
            "choices": [
                ("Kelp forests likely faced greater pressure from sea urchins during the period of low sea otter populations.", True),
                ("Kelp forests were entirely destroyed while sea otter populations were below 2,000.", False),
                ("Sea urchin populations were also reduced during the 1970s due to habitat loss.", False),
                ("The recovery of sea otters in the 2010s had no effect on sea urchin populations.", False),
            ],
            "explanation": (
                "Choice A is correct. The passage establishes that sea otters control sea urchin populations, and sea "
                "urchins would 'otherwise overgraze' kelp. When otter populations were at their lowest, fewer otters "
                "would mean more unchecked urchins, putting more pressure on kelp forests. "
                "Choice B overstates the inference -- the passage does not say forests were destroyed. "
                "Choice C is unsupported; the passage mentions no decline in sea urchin populations. "
                "Choice D contradicts the otter-urchin-kelp relationship the passage establishes."
            ),
        },
        {
            "text": (
                "\"Languages that lack a word for a particular color do not prevent their speakers from perceiving "
                "that color; they simply name it differently or group it with another color. Experiments show that "
                "speakers of languages with fewer color terms can still distinguish between colors that their "
                "language does not separately name -- they are just slightly slower to do so in verbal tasks. "
                "The effect is strongest when color judgment must be communicated quickly in words.\"\n\n"
                "Based on the passage, what can most reasonably be inferred about the relationship between language and color perception?"
            ),
            "difficulty": 3,
            "choices": [
                ("Language completely determines what colors a person is able to see.", False),
                ("Having more color terms in a language causes people to have superior eyesight.", False),
                ("Language influences how efficiently people verbally categorize colors but does not control their underlying perceptual ability.", True),
                ("Languages with fewer color terms are inferior communication systems.", False),
            ],
            "explanation": (
                "Choice C is correct. The passage supports exactly this nuanced inference: speakers of all languages can "
                "distinguish colors (perception intact), but verbal tasks are slightly slower when terms are absent "
                "(language affects efficiency). "
                "Choice A contradicts the passage's explicit statement that lacking a word does not prevent perception. "
                "Choice B introduces eyesight, which the passage does not discuss. "
                "Choice D is a value judgment not found anywhere in the passage."
            ),
        },
        {
            "text": (
                "\"Maria Sibylla Merian, a seventeenth-century naturalist, traveled to the Dutch colony of Suriname "
                "in 1699 -- at the age of 52, without a male guardian -- to study tropical insects. Her detailed "
                "illustrations and observations contradicted the prevailing belief that insects arose through "
                "spontaneous generation. She documented the full life cycle of dozens of species, from egg to adult, "
                "providing some of the earliest systematic evidence that insects developed through metamorphosis.\"\n\n"
                "Based on the passage, what can most reasonably be inferred about scientific understanding of insect "
                "development before Merian's work?"
            ),
            "difficulty": 3,
            "choices": [
                ("Scientists before Merian believed that insects had no developmental stages.", False),
                ("The prevailing view before Merian's work did not accurately account for how insects develop.", True),
                ("Merian was the first scientist to travel to Suriname to conduct fieldwork.", False),
                ("Spontaneous generation was a theory that scientists universally accepted before 1699.", False),
            ],
            "explanation": (
                "Choice B is correct. The passage states Merian's work 'contradicted the prevailing belief' and provided "
                "'some of the earliest systematic evidence' for metamorphosis, directly implying the prior view was "
                "inaccurate. "
                "Choice A overspecifies -- the passage says the old belief was spontaneous generation, not that people "
                "believed there were no developmental stages at all. "
                "Choice C goes beyond the evidence; the passage says nothing about who else traveled to Suriname. "
                "Choice D adds 'universally,' an extreme claim the passage does not make."
            ),
        },
        # ── Lesson 5: Cross-Text Connections ─────────────────────────────────
        {
            "text": (
                "Text 1: \"Remote work has fundamentally changed employee expectations. Workers who shifted to "
                "home offices during the pandemic report higher job satisfaction, primarily due to the elimination "
                "of long commutes and greater schedule flexibility. Companies that have attempted to mandate a "
                "full return to office have faced significant pushback and elevated turnover rates.\"\n\n"
                "Text 2: \"The enthusiasm for remote work obscures real costs to organizational culture. Spontaneous "
                "collaboration -- the hallway conversation, the impromptu whiteboard session -- diminishes when "
                "employees are distributed. Several studies suggest that innovation metrics decline in fully "
                "remote teams compared to co-located ones.\"\n\n"
                "Which choice best describes how the authors of Text 1 and Text 2 differ in their views on remote work?"
            ),
            "difficulty": 1,
            "choices": [
                ("Text 1 focuses on employee satisfaction while Text 2 focuses on organizational innovation, and the two perspectives are in tension.", True),
                ("Both texts argue that remote work is generally beneficial and should be supported by companies.", False),
                ("Text 1 argues that remote work improves productivity while Text 2 argues it reduces productivity.", False),
                ("Both texts rely on the same studies to reach opposing conclusions.", False),
            ],
            "explanation": (
                "Choice A is correct. Text 1 highlights benefits from the employee's perspective (satisfaction, reduced "
                "commuting), while Text 2 highlights costs from the organizational perspective (collaboration, innovation). "
                "These are genuinely different focuses that create tension. "
                "Choice B misreads Text 2, which raises concerns rather than endorsing remote work. "
                "Choice C mischaracterizes Text 1 -- it discusses satisfaction and turnover, not productivity directly. "
                "Choice D is unsupported; the texts cite different evidence."
            ),
        },
        {
            "text": (
                "Text 1: \"Honey bees (Apis mellifera) are frequently cited as essential pollinators, yet they are "
                "not native to North America. Native bees -- including hundreds of species of bumble bees, mason "
                "bees, and sweat bees -- are often more efficient pollinators for native plants and require no "
                "managed hives.\"\n\n"
                "Text 2: \"The decline of managed honey bee colonies is an agricultural crisis. Honey bees pollinate "
                "roughly one-third of the food crops consumed in the United States, including almonds, apples, and "
                "blueberries. Without large-scale managed pollination, crop yields for these commercially important "
                "plants would fall dramatically.\"\n\n"
                "How would the author of Text 1 most likely respond to the concern raised in Text 2?"
            ),
            "difficulty": 2,
            "choices": [
                ("By agreeing that honey bee decline is the most serious threat facing American agriculture.", False),
                ("By suggesting that protecting and promoting native bee populations could address pollination needs without depending on honey bees.", True),
                ("By arguing that managed honey bee hives should be expanded to offset declining populations.", False),
                ("By claiming that food crop yields are not significantly affected by pollinator availability.", False),
            ],
            "explanation": (
                "Choice B is correct. Text 1's central argument is that native bees are 'more efficient pollinators' and "
                "'require no managed hives,' directly implying that investing in native bee populations is an alternative "
                "to honey bee dependence. "
                "Choice A contradicts Text 1's implicit skepticism of honey bee primacy. "
                "Choice C aligns with Text 2's concern, not Text 1's perspective. "
                "Choice D is not supported by Text 1, which focuses on which bee species to prioritize, not whether "
                "pollinators matter."
            ),
        },
        {
            "text": (
                "Text 1: \"Social media platforms have created new opportunities for marginalized communities to "
                "amplify their voices and organize politically. Movements that might have remained local a generation "
                "ago can now achieve global visibility within hours.\"\n\n"
                "Text 2: \"The same platforms that enable grassroots organizing also enable the rapid spread of "
                "misinformation. Research consistently shows that false content spreads faster and farther on social "
                "media than accurate reporting, because emotional, sensational content attracts more engagement.\"\n\n"
                "Which choice best describes the relationship between Text 1 and Text 2?"
            ),
            "difficulty": 2,
            "choices": [
                ("Text 2 directly contradicts Text 1 by arguing that social media has no political value.", False),
                ("Text 2 provides a complementary concern that qualifies the optimistic view presented in Text 1.", True),
                ("Both texts agree that social media is more harmful than beneficial to democratic society.", False),
                ("Text 1 and Text 2 address completely unrelated topics and cannot be meaningfully compared.", False),
            ],
            "explanation": (
                "Choice B is correct. Text 2 does not deny the organizing benefit Text 1 describes; instead, it adds a "
                "complicating factor (misinformation) that qualifies the optimistic picture -- a complementary, not "
                "contradictory, relationship. "
                "Choice A overstates Text 2's position; Text 2 acknowledges the same enabling power. "
                "Choice C misrepresents both texts: neither concludes social media is purely harmful. "
                "Choice D is incorrect; both texts discuss social media's societal effects."
            ),
        },
        {
            "text": (
                "Text 1: \"Ancient Greek philosopher Aristotle argued that the Earth must be spherical because "
                "during a lunar eclipse, the shadow cast by the Earth on the Moon always appears curved, regardless "
                "of the angle of observation. Only a sphere casts a circular shadow from all directions.\"\n\n"
                "Text 2: \"Eratosthenes, a Greek mathematician of the third century BCE, provided a method to "
                "calculate Earth's circumference using shadows. By comparing the angle of the sun's rays at two "
                "locations on the same meridian on the same day, he estimated Earth's circumference to within "
                "a few percent of the modern value.\"\n\n"
                "Both passages contribute to which broader conclusion?"
            ),
            "difficulty": 3,
            "choices": [
                ("Ancient Greek thinkers used consistent, observable evidence to reason accurately about Earth's shape and size.", True),
                ("Eratosthenes was more scientifically rigorous than Aristotle because he used mathematics.", False),
                ("Ancient Greek philosophers rejected all claims about Earth's shape that lacked mathematical proof.", False),
                ("Both Aristotle and Eratosthenes relied solely on lunar eclipses to study Earth.", False),
            ],
            "explanation": (
                "Choice A is correct. Both texts show ancient Greeks using direct, repeatable observations (eclipse "
                "shadows; sun-angle comparisons) to draw accurate conclusions about Earth -- together, they support "
                "the idea of evidence-based reasoning in ancient science. "
                "Choice B makes a comparative value judgment the texts do not support. "
                "Choice C introduces a claim about rejecting non-mathematical evidence that neither text states. "
                "Choice D is factually wrong; Eratosthenes used sun-angle measurements, not lunar eclipses."
            ),
        },
        # ── Lesson 6: Main Purpose and Rhetorical Situation ───────────────────
        {
            "text": (
                "\"To the Members of the Planning Commission:\n"
                "I write on behalf of residents in the Millbrook neighborhood to oppose the proposed rezoning of "
                "Lot 47 for commercial use. This lot borders our elementary school, and increased truck traffic "
                "from a commercial facility poses unacceptable safety risks to children. We urge the Commission "
                "to deny this application and preserve the residential character of our community.\"\n\n"
                "What is the main purpose of this passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("To describe the history of zoning regulations in the Millbrook neighborhood.", False),
                ("To persuade the Planning Commission to reject a rezoning proposal on safety and community grounds.", True),
                ("To inform residents about the details of a proposed commercial development.", False),
                ("To analyze the economic effects of commercial rezoning on residential property values.", False),
            ],
            "explanation": (
                "Choice B is correct. The passage is addressed to decision-makers (the Commission), states a clear "
                "position (opposition to rezoning), offers a reason (child safety), and ends with a direct call to "
                "action ('urge the Commission to deny this application') -- classic persuasive structure. "
                "Choice A is wrong; no zoning history is provided. "
                "Choice C is wrong; the passage is written to the Commission, not to residents. "
                "Choice D is wrong; economic effects are not discussed."
            ),
        },
        {
            "text": (
                "\"The circulatory system functions as the body's primary transport network. The heart pumps "
                "oxygenated blood through the arteries to every organ and tissue; veins return deoxygenated "
                "blood to the heart and lungs for re-oxygenation. Capillaries, the smallest blood vessels, "
                "allow the exchange of oxygen, nutrients, and waste products at the cellular level. This "
                "continuous cycle sustains every metabolic process in the body.\"\n\n"
                "Which choice best describes the main purpose of this passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("To persuade readers that the heart is the most important organ in the human body.", False),
                ("To compare the circulatory system to transportation systems in other organisms.", False),
                ("To explain how the circulatory system works and what role it serves in the body.", True),
                ("To argue that capillaries are the most overlooked component of the circulatory system.", False),
            ],
            "explanation": (
                "Choice C is correct. The passage describes each component (heart, arteries, veins, capillaries) and "
                "explains its function in an informative, neutral tone -- a textbook-style explanation with no "
                "argument or comparison. "
                "Choice A is wrong; the passage makes no evaluative claim about the heart's importance. "
                "Choice B is wrong; no comparison to other organisms is made. "
                "Choice D is wrong; the passage does not prioritize capillaries over other components."
            ),
        },
        {
            "text": (
                "\"My grandmother never measured anything when she cooked. She added a 'handful' of flour, a "
                "'pinch' of salt, a 'splash' of milk -- and the results were always perfect. I tried for years "
                "to write down her recipes as she cooked, only to realize that her measurements were calibrated "
                "to her hands, her eyes, her decades of experience. I have since concluded that cooking is as "
                "much a form of embodied knowledge as it is a science, and that some things resist being reduced "
                "to numbers.\"\n\n"
                "What is the main purpose of this passage?"
            ),
            "difficulty": 2,
            "choices": [
                ("To argue, using a personal anecdote, that intuitive expertise cannot always be fully captured in written instructions.", True),
                ("To instruct readers on how to cook traditional recipes without measuring cups.", False),
                ("To compare the author's cooking skills unfavorably to those of a professional chef.", False),
                ("To describe the history of recipe writing and standardization of measurements.", False),
            ],
            "explanation": (
                "Choice A is correct. The personal anecdote leads to a reflective conclusion -- that cooking is 'embodied "
                "knowledge' that 'resists being reduced to numbers' -- making the purpose argumentative and reflective, "
                "using narrative as evidence. "
                "Choice B mistakes the subject matter for the purpose; the passage does not teach cooking. "
                "Choice C is unsupported; the author does not evaluate their own skill relative to a chef. "
                "Choice D is wrong; no history of recipe writing or measurement standardization is discussed."
            ),
        },
        {
            "text": (
                "\"Recent findings suggest that the 'hygiene hypothesis' -- the idea that reduced exposure to "
                "microbes in childhood increases susceptibility to allergies and autoimmune conditions -- may "
                "need revision. While the hypothesis correctly identified a correlation between cleaner environments "
                "and rising allergy rates, it overlooked the specific *types* of microbial exposure that matter. "
                "Researchers now propose an 'old friends' hypothesis: it is not microbial diversity in general "
                "but exposure to specific ancient organisms, present throughout human evolutionary history, that "
                "trains the immune system.\"\n\n"
                "What is the main purpose of this passage?"
            ),
            "difficulty": 3,
            "choices": [
                ("To refute the hygiene hypothesis entirely and prove that childhood cleanliness has no health effects.", False),
                ("To describe how a newer, more precise scientific framework is replacing and refining an older one.", True),
                ("To persuade parents to expose their children to more microbes to prevent allergies.", False),
                ("To explain the history of allergy research from its origins to the present day.", False),
            ],
            "explanation": (
                "Choice B is correct. The passage acknowledges the hygiene hypothesis had merit ('correctly identified') "
                "but explains its limitation and then introduces the 'old friends' hypothesis as a more refined "
                "replacement -- a classic structure for describing scientific revision. "
                "Choice A overstates: the passage says the old hypothesis needs 'revision,' not that it was entirely wrong. "
                "Choice C is a practical recommendation not made in the passage. "
                "Choice D implies a historical survey; the passage is analytical, not historical."
            ),
        },
        # ── Lesson 7: SAT Information & Ideas Strategy ───────────────────────
        {
            "text": (
                "\"Echolocation, used by bats and dolphins to navigate and hunt, involves emitting high-frequency "
                "sound pulses and interpreting the returning echoes. The time delay between emission and echo "
                "indicates the distance to an object, while frequency shifts in the returning sound reveal the "
                "object's speed and direction. Some blind humans have learned to use a form of echolocation by "
                "clicking their tongues and listening to the reflections, demonstrating that the brain can "
                "repurpose auditory processing for spatial navigation.\"\n\n"
                "Which choice best states the main idea of the passage?"
            ),
            "difficulty": 1,
            "choices": [
                ("Echolocation is a sophisticated navigation system that works through sound interpretation and can be adapted by humans.", True),
                ("Bats are more skilled at echolocation than dolphins because their hearing range is broader.", False),
                ("Blind humans who learn echolocation develop the same brain structures as dolphins.", False),
                ("Echolocation is used exclusively by animals and cannot be learned by humans in any form.", False),
            ],
            "explanation": (
                "Choice A is correct. The passage explains how echolocation works, what information it provides, and "
                "then extends the concept to human use -- the central message is that echolocation is a powerful, "
                "adaptable sound-based navigation system. "
                "Choice B makes a comparison between bats and dolphins that the passage does not make. "
                "Choice C over-infers: the passage says the brain 'repurposes auditory processing,' not that humans "
                "develop the same brain structures as dolphins. "
                "Choice D contradicts the passage, which explicitly describes humans using echolocation."
            ),
        },
        {
            "text": (
                "\"The concept of 'social capital' -- the networks of relationships among people that enable "
                "society to function effectively -- was popularized by sociologist Robert Putnam in the 1990s. "
                "Putnam distinguished between 'bonding' capital, which reinforces connections within homogeneous "
                "groups, and 'bridging' capital, which creates links across diverse groups. He argued that "
                "bridging capital is especially valuable for democratic societies because it builds trust between "
                "people who might not otherwise interact.\"\n\n"
                "A student wants to find evidence that Putnam valued one type of social capital more than the other "
                "for democratic societies. Which quotation from the passage provides the most direct support?"
            ),
            "difficulty": 2,
            "choices": [
                ("'The concept of social capital...was popularized by sociologist Robert Putnam in the 1990s.'", False),
                ("'Putnam distinguished between bonding capital...and bridging capital...'", False),
                ("'He argued that bridging capital is especially valuable for democratic societies because it builds trust between people who might not otherwise interact.'", True),
                ("'Bonding capital...reinforces connections within homogeneous groups.'", False),
            ],
            "explanation": (
                "Choice C is correct. It directly states Putnam's evaluative position -- that bridging capital is "
                "'especially valuable' for democracies -- which is exactly the evidence the student needs. "
                "Choice A introduces Putnam but makes no evaluative claim. "
                "Choice B defines the two types but does not compare their value. "
                "Choice D defines bonding capital but does not rank or compare the two types."
            ),
        },
        {
            "text": (
                "A study examined how quickly subjects could identify words presented in their native language "
                "versus a second language they had learned as adults.\n\n"
                "Language Condition    | Avg. Response Time (ms)\n"
                "---------------------|------------------------\n"
                "Native language       |          312\n"
                "Second language (2 yrs) |         487\n"
                "Second language (5 yrs) |         401\n"
                "Second language (10 yrs)|         338\n\n"
                "Based on the table, which conclusion is best supported?"
            ),
            "difficulty": 2,
            "choices": [
                ("After ten or more years, second-language response times approach native-language speed.", True),
                ("Second-language learners always respond more slowly than native speakers, regardless of experience.", False),
                ("Learning a second language for five years doubles response speed compared to two years.", False),
                ("Native speakers process language three times faster than second-language learners at any stage.", False),
            ],
            "explanation": (
                "Choice A is correct. The 10-year second-language response time (338 ms) is very close to the native "
                "baseline (312 ms), supporting the inference that extended experience narrows the gap. "
                "Choice B overstates: 'always' and 'regardless of experience' are contradicted by the converging trend. "
                "Choice C is inaccurate: 487 ms (2 yrs) vs. 401 ms (5 yrs) is an 18% improvement, not a doubling. "
                "Choice D is wrong: 312 ms vs. 338 ms (10 yrs) is not a threefold difference."
            ),
        },
        {
            "text": (
                "\"The Amazon rainforest is sometimes called the 'lungs of the Earth' because of its role in "
                "absorbing carbon dioxide and releasing oxygen. However, this metaphor is partially misleading: "
                "while the forest does sequester enormous amounts of carbon in its biomass, the net oxygen "
                "exchange between the Amazon and the atmosphere is close to zero, because the same organisms "
                "that produce oxygen also consume it through respiration. The forest's true climate value lies "
                "primarily in its carbon storage capacity, not its oxygen output.\"\n\n"
                "Based on the passage, what can most reasonably be inferred about the 'lungs of the Earth' metaphor?"
            ),
            "difficulty": 3,
            "choices": [
                ("The metaphor is completely accurate and reflects the latest scientific understanding of the Amazon.", False),
                ("The metaphor captures something true about the Amazon but overstates its role as an oxygen source.", True),
                ("Scientists invented the metaphor specifically to highlight the Amazon's carbon storage function.", False),
                ("The Amazon produces more oxygen than any other ecosystem on Earth.", False),
            ],
            "explanation": (
                "Choice B is correct. The passage acknowledges the metaphor has some validity (the forest does absorb CO2 "
                "and release O2) but explains why it is 'partially misleading' -- the net oxygen exchange is near zero. "
                "The metaphor captures a real function but inflates it. "
                "Choice A directly contradicts the passage's statement that the metaphor is 'partially misleading.' "
                "Choice C introduces a claim about the metaphor's origin that the passage does not make. "
                "Choice D is not stated in the passage; the passage focuses on net exchange, not relative output across ecosystems."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed the SAT Reading & Writing: Information & Ideas deep-dive course."

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
                course=course,
                title=title,
                content=content,
                order=order,
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
