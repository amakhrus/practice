"""
Seed the capstone 'SAT Full-Length Practice Test' course -- one mixed test that
pulls from BOTH sections of the digital SAT:

  - Reading & Writing  (~55% of questions): Craft & Structure, Information &
    Ideas, Standard English Conventions, Expression of Ideas
  - Math               (~45% of questions): Algebra, Advanced Math,
    Problem-Solving & Data Analysis, Geometry & Trigonometry

The items are fresh (not copied from the single-section courses) so students get
new practice, written in the same style: every Reading & Writing question has its
own short passage; every explanation names the tempting wrong answer and ends
with a Pro tip. Concise recap/strategy lessons (with Quick Checks and diagrams)
frame the test. Multiple choice only -- the modern SAT has no essay.

This course is filed under the 'other' subject because it spans both subjects.

Run:
    python manage.py seed_sat_full_practice
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "SAT Full-Length Practice Test (Reading, Writing & Math)",
    "slug": "sat-full-length-practice",
    "program": "SAT",
    "subject": "other",
    "description": (
        "A capstone full-length SAT practice test that mixes both sections of the digital exam in "
        "realistic proportions: Reading and Writing (words in context, text structure, command of "
        "evidence, inferences, punctuation, grammar, transitions, and rhetorical synthesis) and "
        "Math (algebra, advanced math, problem-solving and data analysis, and geometry and "
        "trigonometry). Fresh, exam-style multiple-choice questions with full explanations and pro "
        "tips, plus quick strategy recaps and a test-day game plan, so you can rehearse the whole "
        "SAT in one place before test day."
    ),
    "lessons": [
        (
            "1. How the Full SAT Works",
            r"""
The digital SAT has **two sections**, and this practice test mixes both, just like the real exam.

- **Reading & Writing:** about **64 minutes** for **54 questions**, split into two modules. Every question has its own short passage.
- **Math:** about **70 minutes** for **44 questions**, also two modules. A calculator is allowed on the whole math section.

That is roughly **98 questions** in just over two hours. The two section scores (each 200-800) add up to the famous **400-1600** total.

The test is **adaptive**: how you do on the first module of a section sets the difficulty of the second module, so early questions matter. Because the questions are grouped by type, this practice test is organized the same way -- Reading & Writing first, then Math.

The two habits that win points across the whole test:
- **Reading & Writing is open-book.** The right answer is supported by the passage, not by outside knowledge.
- **Math is multiple choice.** When you are stuck, you can test the answer choices instead of doing all the algebra.

[[check:The two SAT section scores add up to what maximum total?|1600|Each section is 200-800.]]
            """,
        ),
        (
            "2. Reading & Writing: Strategy Recap",
            r"""
Reading & Writing has four question domains. Knowing which one you are looking at tells you how to attack it.

[[figure:sat_rw_roadmap|Each question belongs to one of these four domains. Spot the type, then apply its method.]]

Fast methods by domain:
- **Craft & Structure:** for words in context, use the sentence's clues and **predict** the meaning before reading choices; for structure/purpose, ask what a sentence *does*, not just what it says.
- **Information & Ideas:** the main idea must cover the *whole* passage; for command of evidence, pick the choice that *directly* supports or weakens the stated claim.
- **Standard English Conventions:** test whether each side of a punctuation mark is a complete sentence; match verbs and pronouns to the *real* subject.
- **Expression of Ideas:** for transitions, decide the logic (add, contrast, cause, example) first; for synthesis, match the choice to the stated *goal*.

The golden rule: **predict, then match.** Decide what the answer should be, then find the choice closest to it. And eliminate any choice that is too extreme (*always, never, proves*).

[[check:On a reading question, the correct answer must be supported by the what?|passage;;text;;the passage|The SAT reading test is open-book.]]
            """,
        ),
        (
            "3. Math: Strategy Recap",
            r"""
SAT Math also has four domains: **Algebra** (the largest), **Advanced Math** (functions, quadratics, exponents), **Problem-Solving & Data Analysis** (percents, rates, statistics), and **Geometry & Trigonometry**.

Two strategies turn hard problems into easy arithmetic, because the questions are multiple choice:
- **Backsolve.** If the question asks for a value and the choices are numbers, **plug the choices in** (start in the middle). The one that works is the answer.
- **Plug in numbers.** If the question and choices contain variables, pick a simple number (like \(x = 2\); avoid 0 and 1) and compare results.

Test-day habits that save points:
- **Read the last line.** The question may want \(x + 3\), not \(x\).
- **Use the calculator wisely** -- it is allowed throughout, but setting up the problem matters more.
- **Estimate** to eliminate answers that are clearly too big or too small.

[[check:If a question asks for x and the answer choices are numbers, what fast strategy can you use?|backsolve;;backsolving;;plug in the answers|Test the choices in the equation.]]
            """,
        ),
        (
            "4. Test-Day Game Plan: Pacing & Stamina",
            r"""
You have the methods; this is about using them under time pressure for two-plus hours.

**Pacing.** The two sections move at different speeds:
- Reading & Writing: ~54 questions in ~64 minutes is about **70 seconds each**.
- Math: ~44 questions in ~70 minutes is about **95 seconds each**.

A per-question routine: read the question first, predict or set up, eliminate aggressively, then choose.

**Never leave a blank.** There is **no penalty** for a wrong answer, so a guess always beats an empty box. If a question stalls you, eliminate what you can, pick, flag it, and move on.

**Respect the adaptive format.** Your first-module performance sets the second module's difficulty, so don't rush the earlier, easier points -- they count.

**Manage stamina.** It is a long test. Use the section break, keep a steady rhythm, and don't let one hard question drain the time (and focus) you need for several easy ones later.

[[check:Is there any penalty for a wrong answer on the SAT? Answer yes or no.|no|So you should always guess rather than leave a blank.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ============ READING & WRITING (~55% of the test) ===================
        # =====================================================================
        # ---- Craft & Structure: Words in Context ----
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The scientist's explanation was admirably ______: in just three sentences she "
                     "captured an idea that others needed whole chapters to convey.\"\n\n"
                     "Which choice completes the text with the most logical and precise word?"),
            "difficulty": 2,
            "choices": [("concise", True), ("lengthy", False), ("vague", False), ("technical", False)],
            "explanation": ("'Three sentences' versus 'whole chapters' signals brevity, so 'concise' fits. "
                            "'Lengthy' is the opposite. Pro tip: the contrast in the sentence defines the "
                            "blank."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Although the city council had promised swift action, the actual reforms were "
                     "______, trickling out over nearly a decade.\"\n\n"
                     "Which choice completes the text with the most logical and precise word?"),
            "difficulty": 2,
            "choices": [("gradual", True), ("immediate", False), ("costly", False), ("popular", False)],
            "explanation": ("'Although … swift' sets up a contrast, and 'trickling out over nearly a decade' "
                            "means slow -- 'gradual.' 'Immediate' matches 'swift,' which the contrast rules "
                            "out. Pro tip: 'Although' flips the expected meaning."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The treaty was meant to be binding, yet within months several nations began to "
                     "disregard its terms entirely.\"\n\n"
                     "As used in the text, \"binding\" most nearly means"),
            "difficulty": 2,
            "choices": [("obligatory.", True), ("flexible.", False), ("temporary.", False), ("written.", False)],
            "explanation": ("A treaty 'meant to be binding' is one nations are obligated to follow -- which "
                            "is why disregarding it is notable ('yet'). 'Flexible' is the opposite. Pro tip: "
                            "let the surrounding logic, not a familiar synonym, fix the meaning."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Critics praised the documentary for refusing to ______ a complex issue, instead "
                     "presenting its many contradictions honestly.\"\n\n"
                     "Which choice completes the text with the most logical and precise word?"),
            "difficulty": 3,
            "choices": [("oversimplify", True), ("investigate", False), ("finance", False), ("film", False)],
            "explanation": ("'Instead presenting its many contradictions' is the opposite of smoothing an "
                            "issue over, so the film refused to 'oversimplify.' 'Investigate' is something a "
                            "documentary would do, not refuse. Pro tip: 'refusing to ___, instead …' means "
                            "the blank is the opposite of what follows 'instead.'"),
        },
        # ---- Craft & Structure: Text Structure & Purpose ----
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Most people assume bats are blind. In fact, nearly all bat species can see, and "
                     "some have excellent vision. The myth likely persists because bats rely so heavily on "
                     "echolocation at night.\"\n\n"
                     "Which choice best describes the function of the second sentence in the text overall?"),
            "difficulty": 2,
            "choices": [("It corrects the misconception stated in the first sentence.", True),
                        ("It gives an example that supports the first sentence.", False),
                        ("It introduces a topic unrelated to the first sentence.", False),
                        ("It simply restates the first sentence in new words.", False)],
            "explanation": ("'In fact, nearly all bat species can see' directly overturns the opening "
                            "assumption that bats are blind -- a correction. It doesn't support or restate "
                            "that claim. Pro tip: 'In fact' often signals a correction of what came before."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The new bridge was celebrated as an engineering triumph when it opened. Within "
                     "five years, however, cracks appeared in its supports, and engineers admitted the "
                     "original design had underestimated traffic loads.\"\n\n"
                     "Which choice best describes the overall structure of the text?"),
            "difficulty": 2,
            "choices": [("It presents an initial success followed by later problems.", True),
                        ("It compares two competing bridge designs.", False),
                        ("It lists the steps involved in building a bridge.", False),
                        ("It defines a technical engineering term.", False)],
            "explanation": ("The text opens with the bridge's celebrated success and then ('however') turns "
                            "to the cracks and design flaw -- success, then problems. Pro tip: 'however' marks "
                            "the turn that organizes the whole passage."),
        },
        # ---- Craft & Structure: Cross-Text Connections ----
        {
            "text": ("Read the two texts, then answer.\n\n"
                     "Text 1: \"Zoos play a vital role in conservation, breeding endangered species and "
                     "educating millions of visitors every year.\"\n\n"
                     "Text 2: \"While zoos do support some breeding programs, critics note that many "
                     "animals live in enclosures far too small to meet their natural needs.\"\n\n"
                     "Based on the texts, how would the author of Text 2 most likely respond to the claim "
                     "in Text 1?"),
            "difficulty": 3,
            "choices": [("By acknowledging the breeding programs but raising a concern about animal welfare", True),
                        ("By denying that zoos run any breeding programs at all", False),
                        ("By fully agreeing that zoos have no real drawbacks", False),
                        ("By arguing that zoos should focus only on educating visitors", False)],
            "explanation": ("Text 2 concedes the breeding point ('While zoos do support some breeding "
                            "programs') but adds a welfare concern about small enclosures. It doesn't deny "
                            "breeding or agree there are no drawbacks. Pro tip: 'While …' marks a partial "
                            "agreement plus a counterpoint."),
        },
        # ---- Information & Ideas: Central Ideas & Details ----
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Long dismissed as simple pests, crows are now recognized as remarkably "
                     "intelligent. They craft tools from twigs, recognize individual human faces, and even "
                     "gather around their dead in what look like funerals.\"\n\n"
                     "Which choice best states the main idea of the text?"),
            "difficulty": 2,
            "choices": [("Crows are far more intelligent than people once assumed.", True),
                        ("Crows are a common pest in many cities.", False),
                        ("Crows can recognize individual human faces.", False),
                        ("Crows build their nests out of twigs.", False)],
            "explanation": ("Every detail -- tools, face recognition, funeral-like gatherings -- supports the "
                            "single point that crows are surprisingly intelligent. Face recognition is just "
                            "one detail (too narrow). Pro tip: the main idea must cover all the details, not "
                            "one."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"Long dismissed as simple pests, crows are now recognized as remarkably "
                     "intelligent. They craft tools from twigs, recognize individual human faces, and even "
                     "gather around their dead in what look like funerals.\"\n\n"
                     "According to the text, which behavior is offered as evidence of crows' intelligence?"),
            "difficulty": 1,
            "choices": [("Crafting tools from twigs", True),
                        ("Migrating across long distances", False),
                        ("Building unusually large nests", False),
                        ("Singing complex songs", False)],
            "explanation": ("The text directly lists crafting tools from twigs as one sign of intelligence. "
                            "Migration, large nests, and songs are never mentioned. Pro tip: for a detail "
                            "question, point to the exact words in the passage."),
        },
        # ---- Information & Ideas: Command of Evidence (textual) ----
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"A biologist hypothesizes that planting native wildflowers along roadsides "
                     "increases the local bee population.\"\n\n"
                     "Which finding, if true, would most directly support this hypothesis?"),
            "difficulty": 2,
            "choices": [("Roadsides planted with native wildflowers had more bees than nearby unplanted roadsides.", True),
                        ("Native wildflowers are relatively inexpensive to plant.", False),
                        ("Many people find roadside wildflowers attractive.", False),
                        ("Bees are important pollinators all over the world.", False)],
            "explanation": ("The hypothesis links wildflower planting to more bees, so a comparison of "
                            "planted versus unplanted roadsides is directly on point. Cost, beauty, and "
                            "general bee importance are true-but-irrelevant. Pro tip: the best evidence speaks "
                            "to THIS claim."),
        },
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"A historian argues that the spread of the printing press caused literacy rates in "
                     "Europe to rise.\"\n\n"
                     "Which finding, if true, would most strongly support this argument?"),
            "difficulty": 3,
            "choices": [("Literacy rates climbed steadily in regions soon after printing presses were established there.", True),
                        ("Early printing presses were expensive to build and operate.", False),
                        ("Many of the first printed books were religious texts.", False),
                        ("Some regions were slow to adopt the printing press.", False)],
            "explanation": ("A causal claim is best supported by literacy rising right after presses arrived, "
                            "region by region. The other facts are about cost or content, not the press-to-"
                            "literacy link. Pro tip: to support a cause, look for the effect appearing after "
                            "the cause."),
        },
        # ---- Information & Ideas: Command of Evidence (quantitative, with chart) ----
        {
            "text": ("Read the text and bar graph, then answer.\n\n"
                     "A waste-management report claims that, among the four materials shown, paper and "
                     "glass together are recycled at a far higher combined rate than metal and plastic "
                     "together.\n\n"
                     "[[figure:bar_recycling|Recycling rate by material (%)]]\n\n"
                     "Which choice best uses data from the graph to support this claim?"),
            "difficulty": 3,
            "choices": [("Paper and glass total 99%, while metal and plastic total only 37%.", True),
                        ("Paper alone is recycled at 68%, the highest rate shown.", False),
                        ("Plastic is recycled at just 9%, the lowest rate shown.", False),
                        ("Glass and metal are recycled at similar rates.", False)],
            "explanation": ("The claim compares two pairs, so the support must add each pair: paper (68) + "
                            "glass (31) = 99, versus metal (28) + plastic (9) = 37. The other choices cite "
                            "single bars and never make the comparison. Pro tip: a claim about combined "
                            "totals needs the totals."),
        },
        # ---- Information & Ideas: Inferences ----
        {
            "text": ("Read the text, then answer.\n\n"
                     "\"The museum kept its rarest manuscript in a sealed, climate-controlled case, away "
                     "from any direct light. The curators knew that even brief exposure to humidity or "
                     "sunlight could ______\"\n\n"
                     "Which choice most logically completes the text?"),
            "difficulty": 2,
            "choices": [("cause irreversible damage to the fragile pages.", True),
                        ("make the manuscript far more valuable.", False),
                        ("attract many additional visitors.", False),
                        ("improve the document's readability.", False)],
            "explanation": ("Sealing the manuscript away from light and humidity only makes sense if those "
                            "things would harm it, so 'irreversible damage' follows. The other options "
                            "contradict the careful protection described. Pro tip: the inference must explain "
                            "why the people acted as they did."),
        },
        # ---- Standard English Conventions: Boundaries ----
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The hikers reached the summit just before noon ______ the view stretched for miles "
                     "in every direction.\""),
            "difficulty": 2,
            "choices": [("noon; the", True), ("noon, the", False), ("noon the", False), ("noon the,", False)],
            "explanation": ("Both sides are complete sentences, so a semicolon joins them correctly. A comma "
                            "alone is a comma splice, and no punctuation is a run-on. Pro tip: two full "
                            "sentences need a period, a semicolon, or a comma + FANBOYS."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The chef relied on three local ______ ripe tomatoes, fresh basil, and creamy "
                     "mozzarella.\""),
            "difficulty": 2,
            "choices": [("ingredients:", True), ("ingredients,", False), ("ingredients;", False), ("ingredients", False)],
            "explanation": ("'The chef relied on three local ingredients' is a complete sentence, and a list "
                            "follows, so a colon is correct. A semicolon needs a full sentence after it. Pro "
                            "tip: complete sentence + a list = colon."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"Amelia ______ disappeared over the Pacific in 1937, remains one of aviation's most "
                     "famous figures.\""),
            "difficulty": 3,
            "choices": [("Earhart, who", True), ("Earhart who", False), ("Earhart. Who", False), ("Earhart; who", False)],
            "explanation": ("'who disappeared over the Pacific in 1937' is nonessential information and must "
                            "be set off with a comma (paired with the comma after 1937). Starting a new "
                            "sentence with 'Who' makes a fragment. Pro tip: nonessential descriptions take "
                            "commas on both sides."),
        },
        # ---- Standard English Conventions: Form, Structure & Sense ----
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"The bouquet of bright spring flowers ______ a gift from her younger brother.\""),
            "difficulty": 2,
            "choices": [("is", True), ("are", False), ("were", False), ("have been", False)],
            "explanation": ("The subject is 'bouquet' (singular), not 'flowers,' so the singular verb 'is' "
                            "agrees. The plural-sounding 'flowers' is just part of an 'of' phrase. Pro tip: "
                            "cross out the 'of …' phrase to find the real subject."),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"By the time the train pulled into the station, the passengers ______ been waiting "
                     "on the platform for over an hour.\""),
            "difficulty": 2,
            "choices": [("had", True), ("have", False), ("has", False), ("will have", False)],
            "explanation": ("The waiting happened before the train arrived (also past), so the past perfect "
                            "'had been waiting' shows the earlier action. 'Have/has' are present perfect; "
                            "'will have' is future. Pro tip: for the earlier of two past events, use 'had.'"),
        },
        {
            "text": ("Which choice completes the text so that it conforms to the conventions of Standard "
                     "English?\n\n"
                     "\"Exhausted after the long overnight flight, ______\""),
            "difficulty": 3,
            "choices": [("Marcus collapsed onto the hotel bed without even unpacking.", True),
                        ("the hotel bed looked very inviting to Marcus.", False),
                        ("the luggage was left by the door by Marcus.", False),
                        ("it was difficult for Marcus to stay awake.", False)],
            "explanation": ("The opening phrase describes someone exhausted, so the noun right after the "
                            "comma must be that person -- Marcus. The other versions make 'the bed,' 'the "
                            "luggage,' or 'it' exhausted, a dangling modifier. Pro tip: name the doer right "
                            "after an opening descriptive phrase."),
        },
        # ---- Expression of Ideas: Transitions ----
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"The medication relieved her symptoms almost immediately. ______ it caused side "
                     "effects that some patients found difficult to tolerate.\""),
            "difficulty": 2,
            "choices": [("However,", True), ("Therefore,", False), ("For example,", False), ("Similarly,", False)],
            "explanation": ("The relief is a benefit; the side effects are a drawback -- a contrast, so "
                            "'However' fits. 'Therefore' would wrongly make the relief cause the side "
                            "effects. Pro tip: a benefit-then-drawback turn calls for a contrast word."),
        },
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"Heavy rains had saturated the hillside for weeks. ______ the slope finally gave "
                     "way in a sudden landslide.\""),
            "difficulty": 2,
            "choices": [("As a result,", True), ("Nevertheless,", False), ("In contrast,", False), ("For instance,", False)],
            "explanation": ("The weeks of rain are the cause; the landslide is the effect, so a cause-effect "
                            "transition ('As a result') fits. 'Nevertheless' and 'In contrast' wrongly signal "
                            "opposition. Pro tip: cause then expected result = 'as a result/therefore.'"),
        },
        {
            "text": ("Which choice completes the text with the most logical transition?\n\n"
                     "\"Many everyday products were invented by accident. ______ the microwave oven was "
                     "discovered when an engineer noticed a candy bar melting near radar equipment.\""),
            "difficulty": 1,
            "choices": [("For example,", True), ("However,", False), ("Therefore,", False), ("In conclusion,", False)],
            "explanation": ("The microwave is a specific instance of the general claim about accidental "
                            "inventions, so 'For example' fits. 'However' signals contrast and 'In conclusion' "
                            "signals an ending. Pro tip: a specific case after a general claim = 'for "
                            "example.'"),
        },
        # ---- Expression of Ideas: Rhetorical Synthesis ----
        {
            "text": ("While researching, a student took the following notes:\n\n"
                     "- The Voyager 1 probe was launched in 1977.\n"
                     "- It was designed to study the outer planets.\n"
                     "- In 2012, it became the first human-made object to reach interstellar space.\n"
                     "- It still sends data back to Earth from billions of miles away.\n\n"
                     "The student wants to emphasize Voyager 1's historic achievement. Which choice most "
                     "effectively uses relevant information from the notes to accomplish this goal?"),
            "difficulty": 2,
            "choices": [("In 2012, Voyager 1 became the first human-made object to reach interstellar space.", True),
                        ("Voyager 1 was launched back in 1977.", False),
                        ("Voyager 1 was designed to study the outer planets.", False),
                        ("Voyager 1 still sends data back to Earth.", False)],
            "explanation": ("'The first human-made object to reach interstellar space' is the clear historic "
                            "milestone. The other notes give the launch date, purpose, or status -- true, but "
                            "not the achievement. Pro tip: match the choice to the stated GOAL."),
        },
        {
            "text": ("While researching, a student took the following notes:\n\n"
                     "- The Great Pacific Garbage Patch is an area of floating plastic debris.\n"
                     "- It lies in the ocean between California and Hawaii.\n"
                     "- Estimates suggest it covers an area roughly three times the size of France.\n"
                     "- Much of the debris consists of tiny pieces called microplastics.\n\n"
                     "The student wants to emphasize the enormous size of the patch. Which choice most "
                     "effectively uses relevant information from the notes to accomplish this goal?"),
            "difficulty": 2,
            "choices": [("The Great Pacific Garbage Patch covers an area roughly three times the size of France.", True),
                        ("The patch lies between California and Hawaii.", False),
                        ("The patch is made largely of tiny microplastics.", False),
                        ("The patch is an area of floating plastic debris.", False)],
            "explanation": ("'Roughly three times the size of France' directly conveys enormous size. The "
                            "other notes give location, composition, or a vague description. Pro tip: to "
                            "stress size, choose the option with the size comparison."),
        },
        # =====================================================================
        # ==================== MATH (~45% of the test) ========================
        # =====================================================================
        # ---- Algebra ----
        {
            "text": r"Solve for \(x\): \(5x - 4 = 26\).",
            "difficulty": 1,
            "choices": [(r"\(x = 6\)", True), (r"\(x = 30\)", False), (r"\(x = 4.4\)", False), (r"\(x = \tfrac{22}{5}\)", False)],
            "explanation": r"Add 4: \(5x = 30\). Divide by 5: \(x = 6\). The trap 30 forgets to divide. Pro tip: undo the \(-4\) first, then the \(\times 5\).",
        },
        {
            "text": r"What is the slope of the line through \((-1, 4)\) and \((2, 13)\)?",
            "difficulty": 2,
            "choices": [(r"\(3\)", True), (r"\(\tfrac{1}{3}\)", False), (r"\(9\)", False), (r"\(-3\)", False)],
            "explanation": r"Slope is rise over run: \(\dfrac{13-4}{2-(-1)} = \dfrac{9}{3} = 3\). The trap 9 forgets to divide by the run; \(\tfrac{1}{3}\) flips the formula. Pro tip: subtract in the same order on top and bottom.",
        },
        {
            "text": r"Solve the system \(2x + y = 12\) and \(x - y = 3\). What is \(x\)?",
            "difficulty": 2,
            "choices": [(r"\(5\)", True), (r"\(2\)", False), (r"\(15\)", False), (r"\(7\)", False)],
            "explanation": r"Add the equations to eliminate \(y\): \(3x = 15\), so \(x = 5\) (and \(y = 2\)). The trap 2 is the value of \(y\); 15 forgets to divide by 3. Pro tip: matching \(+y\) and \(-y\) lets you add to cancel \(y\).",
        },
        {
            "text": r"Solve the inequality \(-3x + 2 < 11\).",
            "difficulty": 2,
            "choices": [(r"\(x > -3\)", True), (r"\(x < -3\)", False), (r"\(x > 3\)", False), (r"\(x < 3\)", False)],
            "explanation": r"Subtract 2: \(-3x < 9\). Divide by \(-3\) and FLIP the sign: \(x > -3\). The trap \(x < -3\) forgets to flip. Pro tip: dividing by a negative reverses the inequality.",
        },
        {
            "text": r"Which values satisfy \(|x + 1| = 4\)?",
            "difficulty": 2,
            "choices": [(r"\(x = 3\) or \(x = -5\)", True), (r"\(x = 3\) only", False),
                        (r"\(x = 4\) or \(x = -4\)", False), (r"\(x = 5\) or \(x = -3\)", False)],
            "explanation": r"Set the inside to \(+4\) and \(-4\): \(x + 1 = 4 \Rightarrow x = 3\); \(x + 1 = -4 \Rightarrow x = -5\). The trap '3 only' misses the negative case. Pro tip: absolute-value equations usually give two answers.",
        },
        {
            "text": (r"A taxi charges a \$3 base fare plus \$2 for each mile. Which equation gives the "
                     r"total cost \(c\) for a ride of \(m\) miles?"),
            "difficulty": 2,
            "choices": [(r"\(c = 2m + 3\)", True), (r"\(c = 3m + 2\)", False), (r"\(c = 2m - 3\)", False), (r"\(c = 5m\)", False)],
            "explanation": r"The per-mile cost \(2m\) is added to the flat \$3 base: \(c = 2m + 3\). The trap \(3m + 2\) swaps the rate and the base fare. Pro tip: the 'per' quantity multiplies the variable; the one-time fee is the constant.",
        },
        {
            "text": r"A line is perpendicular to the line \(y = \tfrac{1}{3}x + 2\). What is its slope?",
            "difficulty": 3,
            "choices": [(r"\(-3\)", True), (r"\(\tfrac{1}{3}\)", False), (r"\(3\)", False), (r"\(-\tfrac{1}{3}\)", False)],
            "explanation": r"Perpendicular slopes are negative reciprocals: flip \(\tfrac{1}{3}\) to \(3\) and negate to \(-3\). The trap \(\tfrac{1}{3}\) is parallel; \(-\tfrac{1}{3}\) only negates. Pro tip: negative reciprocal = flip AND change the sign.",
        },
        # ---- Advanced Math ----
        {
            "text": r"If \(g(x) = 3x - 5\), what is \(g(6)\)?",
            "difficulty": 1,
            "choices": [(r"\(13\)", True), (r"\(18\)", False), (r"\(3\)", False), (r"\(1\)", False)],
            "explanation": r"Substitute 6 for \(x\): \(3(6) - 5 = 18 - 5 = 13\). The trap 18 forgets the \(-5\). Pro tip: \(g(6)\) means 'plug in 6,' not 'g times 6.'",
        },
        {
            "text": r"If \(f(x) = x^2 - 2\), what is \(f(-4)\)?",
            "difficulty": 2,
            "choices": [(r"\(14\)", True), (r"\(-14\)", False), (r"\(6\)", False), (r"\(18\)", False)],
            "explanation": r"Square first: \((-4)^2 = 16\), then \(16 - 2 = 14\). The trap \(-14\) wrongly treats \((-4)^2\) as \(-16\); a negative squared is positive. Pro tip: square the whole value, including its sign.",
        },
        {
            "text": r"Solve \(x^2 + 2x - 8 = 0\).",
            "difficulty": 2,
            "choices": [(r"\(x = -4\) or \(x = 2\)", True), (r"\(x = 4\) or \(x = -2\)", False),
                        (r"\(x = -4\) or \(x = -2\)", False), (r"\(x = 8\) or \(x = 1\)", False)],
            "explanation": r"Factor into \((x+4)(x-2) = 0\), so \(x = -4\) or \(x = 2\) (they multiply to \(-8\) and add to \(+2\)). The trap flips both signs. Pro tip: find two numbers that multiply to \(c\) and add to \(b\).",
        },
        {
            "text": r"Where does the graph of \(y = x^2 - 9\) cross the x-axis?",
            "difficulty": 2,
            "choices": [(r"\(x = -3\) and \(x = 3\)", True), (r"\(x = -9\) and \(x = 9\)", False),
                        (r"\(x = 3\) only", False), (r"\(x = 0\) only", False)],
            "explanation": r"Set \(y = 0\): \(x^2 - 9 = 0 \Rightarrow x^2 = 9 \Rightarrow x = \pm 3\). The trap \(\pm 9\) forgets the square root. Pro tip: x-intercepts are where \(y = 0\); take the square root and keep both signs.",
        },
        {
            "text": r"Simplify \(3^2 \cdot 3^3\).",
            "difficulty": 1,
            "choices": [(r"\(243\)", True), (r"\(729\)", False), (r"\(81\)", False), (r"\(3^6\)", False)],
            "explanation": r"Same base, so add exponents: \(3^{2+3} = 3^5 = 243\). The traps \(729\) and \(3^6\) multiply the exponents instead. Pro tip: multiplying like bases means ADD the exponents.",
        },
        {
            "text": r"Simplify \((2x^4)^3\).",
            "difficulty": 3,
            "choices": [(r"\(8x^{12}\)", True), (r"\(6x^{12}\)", False), (r"\(8x^{7}\)", False), (r"\(2x^{12}\)", False)],
            "explanation": r"Raise each factor to the 3rd power: \(2^3 = 8\) and \((x^4)^3 = x^{12}\), giving \(8x^{12}\). The trap \(6x^{12}\) does \(2\times3\) instead of \(2^3\); \(8x^7\) adds the exponents. Pro tip: a power outside the parentheses hits every factor inside.",
        },
        {
            "text": (r"A bacteria culture is modeled by \(N = 50 \cdot 3^{t}\), where \(t\) is in hours. "
                     r"How many bacteria are there after \(t = 2\) hours?"),
            "difficulty": 3,
            "choices": [(r"\(450\)", True), (r"\(300\)", False), (r"\(150\)", False), (r"\(900\)", False)],
            "explanation": r"\(N = 50 \cdot 3^2 = 50 \cdot 9 = 450\). The trap 300 treats \(3^2\) as \(3 \times 2 = 6\). Pro tip: exponential growth multiplies -- \(3^2 = 3\times3 = 9\), not \(3 \times 2\).",
        },
        # ---- Problem-Solving & Data Analysis ----
        {
            "text": r"A jacket originally priced at \$80 is discounted by 30%. What is the sale price?",
            "difficulty": 2,
            "choices": [(r"\$56", True), (r"\$24", False), (r"\$50", False), (r"\$110", False)],
            "explanation": r"The discount is \(0.30 \times 80 = \$24\), so the price is \(80 - 24 = \$56\). The trap \$24 gives only the discount. Pro tip: 30% off means you pay 70%: \(0.70 \times 80 = 56\).",
        },
        {
            "text": (r"A printer produces 8 pages every 20 seconds. At that rate, how many pages does it "
                     r"produce in 5 minutes?"),
            "difficulty": 3,
            "choices": [(r"\(120\)", True), (r"\(40\)", False), (r"\(96\)", False), (r"\(24\)", False)],
            "explanation": r"The rate is \(8 \div 20 = 0.4\) pages per second, and 5 minutes is 300 seconds: \(0.4 \times 300 = 120\). The trap 40 just multiplies \(8 \times 5\). Pro tip: convert minutes to seconds before using a per-second rate.",
        },
        {
            "text": (r"The mean of five numbers is 12. Four of the numbers are 10, 14, 8, and 16. What is "
                     r"the fifth number?"),
            "difficulty": 3,
            "choices": [(r"\(12\)", True), (r"\(13\)", False), (r"\(48\)", False), (r"\(60\)", False)],
            "explanation": r"The five numbers total \(5 \times 12 = 60\). The four given add to 48, so the fifth is \(60 - 48 = 12\). The trap 60 is the full total. Pro tip: mean times count gives the total -- then subtract what you know.",
        },
        # ---- Geometry & Trigonometry ----
        {
            "text": r"A right triangle has legs of length 5 and 12. What is the length of the hypotenuse?",
            "difficulty": 1,
            "choices": [(r"\(13\)", True), (r"\(17\)", False), (r"\(119\)", False), (r"\(169\)", False)],
            "explanation": r"\(c = \sqrt{5^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13\). The trap 17 adds the legs; 169 forgets the square root. Pro tip: 5-12-13 is a triple worth memorizing.",
        },
        {
            "text": r"What is the circumference of a circle with radius 4? (Use \(\pi \approx 3.14\).)",
            "difficulty": 2,
            "choices": [(r"\(25.12\)", True), (r"\(50.24\)", False), (r"\(12.56\)", False), (r"\(16\)", False)],
            "explanation": r"\(C = 2\pi r = 2 \times 3.14 \times 4 = 25.12\). The trap 50.24 is the area (\(\pi r^2\)); 16 forgets \(\pi\) entirely. Pro tip: circumference uses \(2\pi r\) -- don't drop the 2.",
        },
        {
            "text": (r"In a right triangle, the side adjacent to angle \(A\) is 8 and the hypotenuse is 17. "
                     r"What is \(\cos A\)?"),
            "difficulty": 2,
            "choices": [(r"\(\tfrac{8}{17}\)", True), (r"\(\tfrac{17}{8}\)", False), (r"\(\tfrac{15}{17}\)", False), (r"\(\tfrac{8}{15}\)", False)],
            "explanation": r"CAH: \(\cos = \dfrac{\text{adjacent}}{\text{hypotenuse}} = \dfrac{8}{17}\). The trap \(\tfrac{15}{17}\) is \(\sin A\) (opposite over hyp); \(\tfrac{17}{8}\) flips the ratio. Pro tip: SOH-CAH-TOA -- cosine is adjacent over hypotenuse.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the capstone full-length SAT practice-test course (Reading, Writing & Math; MCQ only)."

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
            Lesson.objects.create(course=course, title=title, content=content.strip(), order=i)

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
