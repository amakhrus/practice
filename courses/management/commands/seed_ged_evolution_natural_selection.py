"""
Seed data: 'GED Science: Evolution & Natural Selection (Deep Dive)'.

A focused EXPANSION of Lesson 4 ("Evolution & Natural Selection") from the broader
'GED Science: Life Science' course, brought up to the full deep-dive standard
(6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. Evolution -- how populations change over time.
  2. Natural selection -- the four-step logic.
  3. Selection in action -- microbes and moths.
  4. Evidence for evolution (fossils, homologous structures, DNA).
  5. Cladograms -- reading evolutionary trees.
  6. Adaptation, speciation & reading evolution data.

This course uses ALL-NEW diagrams (variation in a population, the natural-selection
cycle, antibiotic resistance, homologous structures, a cladogram, and speciation).

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Biology* and *Concepts of Biology* (evolution, natural selection).
  - Campbell & Reece, *Biology*; Darwin, *On the Origin of Species* (1859).
  - University of California Museum of Paleontology, "Understanding Evolution."
  - National Institutes of Health (antibiotic resistance).
Note: evolution acts on POPULATIONS over generations; natural selection acts on
existing inherited variation (it does not create traits "on demand"). Homologous
structures (e.g., the human arm, whale flipper, and bat wing) share bone
arrangement, evidence of common ancestry.

Run:
    python manage.py seed_ged_evolution_natural_selection
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Evolution & Natural Selection (Deep Dive)",
    "slug": "ged-evolution-natural-selection",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into how life changes over time, expanding the single 'Evolution & Natural "
        "Selection' lesson from the GED Life Science course into a full mini-course. You'll learn what "
        "evolution really means (populations change, not individuals), the four-step logic of natural "
        "selection, real cases you can watch (antibiotic resistance and the peppered moth), the "
        "independent lines of evidence for evolution, how to read a cladogram, and how new species form. "
        "Plain language, all-new labeled diagrams, common-misconception warnings, and GED-style practice "
        "with full explanations throughout."
    ),
    "lessons": [
        (
            "1. Evolution: How Populations Change",
            r"**Evolution** is the change in the inherited traits of a **population** over many generations. The key word is **population** — a single organism does **not** evolve during its lifetime. Instead, individuals with different inherited traits survive and reproduce at different rates, so the makeup of the whole population shifts over time." "\n\n"
            r"[[figure:variation_in_population|A population's individuals vary. Some of that variation is inherited — and that's what evolution acts on.]]" "\n\n"
            r"Evolution depends on **variation**: individuals in a population are not identical. New variation ultimately arises from **mutations** (changes in DNA), and it gets reshuffled through reproduction. If every individual were genetically identical, there would be no differences for the environment to favor — and no evolution." "\n\n"
            r"Evolution can be small or large. A population of insects becoming resistant to a pesticide over a few years is evolution. Over much longer spans, repeated change can produce entirely new species (Lesson 6)." "\n\n"
            r"⚠️ Common misconception: organisms don't evolve because they 'want' or 'need' to. No individual chooses to evolve. **Populations** change when inherited traits affect survival and reproduction across generations." "\n\n"
            r"💡 Tip: **individuals survive or die; populations evolve.** No variation means no evolution.",
        ),
        (
            "2. Natural Selection: The Four-Step Logic",
            r"The main engine of evolution is **natural selection**, an idea from **Charles Darwin**. It follows a clear four-step logic — remember it as **V-I-S-T**." "\n\n"
            r"[[figure:natural_selection_cycle|Variation, Inheritance, Selection, then Time: helpful inherited traits become more common over generations.]]" "\n\n"
            r"- **Variation** — individuals in a population differ." "\n"
            r"- **Inheritance** — some of those differences are passed to offspring." "\n"
            r"- **Selection** — more offspring are produced than can survive, so there is competition; individuals with **helpful** inherited traits tend to survive and reproduce more." "\n"
            r"- **Time** — over many generations, the helpful traits become **more common** in the population." "\n\n"
            r"Crucially, the **environment** decides which traits are 'helpful.' A trait that helps in one place (thick fur in the cold) may be unhelpful in another (the same fur in a hot desert). Selection has no goal — it simply favors whatever works **right now**, in **this** environment." "\n\n"
            r"⚠️ Common misconception: traits do **not** appear because an organism needs them. Natural selection acts on variation that **already exists**; it doesn't create new traits on demand." "\n\n"
            r"💡 Tip: **V-I-S-T — Variation, Inheritance, Selection, Time.** The environment is the 'judge.'",
        ),
        (
            "3. Selection in Action: Microbes & Moths",
            r"Natural selection isn't only ancient history — we can **watch** it happen. Two classic cases make the logic concrete." "\n\n"
            r"[[figure:antibiotic_resistance|An antibiotic kills the non-resistant bacteria; the few resistant ones survive and multiply into a resistant population.]]" "\n\n"
            r"**Antibiotic resistance.** In a population of bacteria, a few individuals happen to carry a gene (often from a **mutation**) that resists a drug — that's **variation**. When an antibiotic is used, the non-resistant bacteria die, but the resistant ones **survive and reproduce**. After many generations, most of the population is resistant. This is why misusing antibiotics is dangerous." "\n\n"
            r"**The peppered moth.** These moths come in **light** and **dark** forms. When tree bark was light, light moths were camouflaged from birds and were common. As pollution **darkened** the bark, **dark** moths became better hidden, survived more, and became common instead. When pollution was later reduced, the light form recovered." "\n\n"
            r"⚠️ Common misconception: an antibiotic does **not** 'teach' bacteria to become resistant. It **selects** bacteria that were already resistant (or that became resistant by a chance mutation)." "\n\n"
            r"💡 Tip: selection **favors traits already present** in the population — it doesn't create the trait because it's needed.",
        ),
        (
            "4. The Evidence for Evolution",
            r"Scientists support evolution with several **independent lines of evidence** that all point the same way." "\n\n"
            r"[[figure:homologous_structures|The same bones — upper arm, forearm, fingers — appear in a human arm, a whale flipper, and a bat wing.]]" "\n\n"
            r"- **Fossils** — preserved remains show what lived in the past and reveal patterns of change over time, including transitional forms." "\n"
            r"- **Homologous structures** — body parts with the **same underlying structure** but different uses, like the **human arm, whale flipper, and bat wing**, which all share the same bone arrangement. This points to inheritance from a **common ancestor**." "\n"
            r"- **DNA similarities** — the more **DNA** two species share, the more closely related they are." "\n"
            r"- **Embryology** and **vestigial structures** add still more clues." "\n\n"
            r"The power comes from **agreement**: when fossils, anatomy, and DNA all support the same family tree, the conclusion is strong. Note that common ancestry does **not** mean one living species 'turned into' another — related species share ancestors in the **past**." "\n\n"
            r"⚠️ Common misconception: evolution is **not** a ladder from 'lower' to 'higher' organisms. It describes a **branching** tree of relationships and change over time." "\n\n"
            r"💡 Tip: **shared structures + shared DNA + fossils = evidence of relatedness.** Multiple lines agreeing make the case strong.",
        ),
        (
            "5. Cladograms: Reading Evolutionary Trees",
            r"A **cladogram** is a branching diagram that shows **hypotheses about how species are related**. Each **branch point (node)** represents a **common ancestor**, and marks along the branches show where a new shared trait likely appeared." "\n\n"
            r"[[figure:cladogram|Branch points are common ancestors; shared traits appear at the nodes. Species sharing a more recent node are more closely related.]]" "\n\n"
            r"The single most important rule: species that share a **more recent common branch point** are **more closely related**. Do **not** judge relatedness by how high or low a name is printed, or by the left-to-right order of the tips — only the **branching pattern** matters. To compare two species, trace each branch backward until they meet; the more recent the meeting point, the closer the relationship." "\n\n"
            r"GED items may ask which two organisms are most closely related, where a trait first appeared, or which group shares a feature. Trace the branches and read the **nodes**." "\n\n"
            r"⚠️ Common misconception: the order of names at the tips is **not** the point. Two species printed next to each other may be distantly related; relatedness comes from the **shared branch points**." "\n\n"
            r"💡 Tip: **closest relatives share the most recent common node.** Read branch points, not positions.",
        ),
        (
            "6. Adaptation, Speciation & Reading Evolution Data",
            r"An **adaptation** is an **inherited** trait that improves survival or reproduction in a particular environment — camouflage, a thick coat, a drought-tolerant root. A **selection pressure** is the environmental factor that makes a trait helpful or not: predators, climate, disease, food supply, or competition." "\n\n"
            r"[[figure:speciation|When a barrier splits a population, the two groups stop interbreeding and can diverge into separate species over time.]]" "\n\n"
            r"Over long periods, populations can change enough to become **separate species** — a process called **speciation**. It often begins when a population is **separated** (by a river, mountain range, or behavior), which reduces **gene flow** between the groups. Different environments then select different traits, and the groups gradually **diverge** until they can no longer interbreed." "\n\n"
            r"**Artificial selection** uses the same logic, but guided by **humans**: people breed dogs, crops, and livestock for traits they want. The difference is who does the 'choosing' — the **environment** (natural selection) versus **people** (artificial selection)." "\n\n"
            r"**Reading evolution data (a GED skill).** Items may show trait frequencies over time or a data table. Read the **title, axes, and units**, find the **trend**, and use only what the data shows. And remember: **correlation is not causation** — to claim cause and effect, look for a **controlled experiment**." "\n\n"
            r"⚠️ Common misconception: an individual doesn't 'adapt' by choosing to change. **Adaptations spread** when inherited traits help individuals leave more offspring over generations." "\n\n"
            r"💡 Tip: **selection pressure = the environmental challenge; adaptation = the inherited trait that meets it.** Isolation can lead to new species." "\n\n"
            r"📚 Sources: OpenStax *Biology* / *Concepts of Biology*; Campbell & Reece, *Biology*; Darwin (1859); UC Museum of Paleontology, *Understanding Evolution*; NIH.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: evolution ---
        {
            "text": r"Evolution is best described as:",
            "difficulty": 1,
            "choices": [("A change in the inherited traits of a population over generations", True),
                        ("A single organism changing because it wants to", False),
                        ("All individuals in a species becoming identical", False),
                        ("Photosynthesis in plants", False)],
            "explanation": r"Evolution happens in populations across generations, as the frequency of inherited traits shifts over time.",
        },
        {
            "text": r"Which actually evolves over time?",
            "difficulty": 2,
            "choices": [("A population, across generations", True),
                        ("A single individual, during its life", False),
                        ("Only non-living things", False),
                        ("Only the largest organism", False)],
            "explanation": r"Individuals survive or die, but it is the population whose trait frequencies change over generations — that is evolution.",
        },
        {
            "text": r"Where does NEW variation in a population ultimately come from?",
            "difficulty": 2,
            "choices": [("Mutations (changes in DNA)", True),
                        ("Animals choosing new traits", False),
                        ("Photosynthesis", False),
                        ("The phases of the Moon", False)],
            "explanation": r"Mutations are the original source of new genetic variation; reproduction then reshuffles it.",
        },
        {
            "text": r"If every individual in a population were genetically identical, natural selection could:",
            "difficulty": 2,
            "choices": [("Not occur, because there would be no differences to favor", True),
                        ("Work faster than ever", False),
                        ("Still change the population easily", False),
                        ("Create new species instantly", False)],
            "explanation": r"Selection needs inherited differences to act on. With no variation, there is nothing for the environment to favor.",
        },
        {
            "text": ("Use the population diagram.\n\n"
                     "[[figure:variation_in_population|A population of beetles in many shades]]\n\n"
                     "The range of colors among the beetles best illustrates:"),
            "difficulty": 1,
            "choices": [("Variation within a population", True),
                        ("That all individuals are identical", False),
                        ("Photosynthesis", False),
                        ("The water cycle", False)],
            "explanation": r"The diagram shows individuals differing from one another — variation, the raw material of natural selection. Pro tip: no variation, no selection.",
        },
        # --- Lesson 2: natural selection ---
        {
            "text": r"Who is credited with developing the idea of natural selection?",
            "difficulty": 1,
            "choices": [("Charles Darwin", True), ("Isaac Newton", False),
                        ("Gregor Mendel", False), ("Marie Curie", False)],
            "explanation": r"Charles Darwin described natural selection as the main mechanism of evolution.",
        },
        {
            "text": r"For natural selection to act, which must be true FIRST?",
            "difficulty": 2,
            "choices": [("Individuals must vary in inherited traits", True),
                        ("All individuals must be identical", False),
                        ("The population must stop reproducing", False),
                        ("The environment must never change", False)],
            "explanation": r"Selection works on existing inherited variation, so differences among individuals must exist before selection can favor some of them.",
        },
        {
            "text": r"In natural selection, individuals with helpful inherited traits tend to:",
            "difficulty": 2,
            "choices": [("Survive and reproduce more than others", True),
                        ("Disappear from the population", False),
                        ("Stop passing on their genes", False),
                        ("Become a different species overnight", False)],
            "explanation": r"Those better suited to the environment leave more offspring, so their traits become more common over generations.",
        },
        {
            "text": ("Use the natural-selection diagram.\n\n"
                     "[[figure:natural_selection_cycle|The four steps of natural selection]]\n\n"
                     "According to the diagram, helpful traits become more common because:"),
            "difficulty": 2,
            "choices": [("Individuals with them survive and reproduce more over time", True),
                        ("Organisms decide to grow them", False),
                        ("The traits are stronger by nature", False),
                        ("The Sun adds them to offspring", False)],
            "explanation": r"The cycle shows variation that is inherited, then selected by the environment, becoming more common over time. Pro tip: remember V-I-S-T.",
        },
        {
            "text": r"A trait that helps an organism survive in one environment:",
            "difficulty": 3,
            "choices": [("May not be helpful in a different environment", True),
                        ("Is always helpful everywhere", False),
                        ("Cannot be inherited", False),
                        ("Stops the population from evolving", False)],
            "explanation": r"Selection depends on the environment. The same trait can be an advantage in one setting and a disadvantage in another.",
        },
        # --- Lesson 3: selection in action ---
        {
            "text": r"A few bacteria survive an antibiotic and then multiply. The best explanation is that they:",
            "difficulty": 2,
            "choices": [("Already had resistance, so the antibiotic selected them", True),
                        ("Each chose to become resistant", False),
                        ("Were created by the antibiotic", False),
                        ("Turned into viruses", False)],
            "explanation": r"Resistance was present in a few individuals (often from mutation). The antibiotic killed the rest, leaving the resistant ones to reproduce.",
        },
        {
            "text": r"Antibiotics cause resistance to spread in a population mainly by:",
            "difficulty": 2,
            "choices": [("Killing non-resistant bacteria, leaving resistant ones to reproduce", True),
                        ("Teaching every bacterium how to resist", False),
                        ("Adding resistance genes to all cells", False),
                        ("Stopping all reproduction", False)],
            "explanation": r"The antibiotic is a selection pressure: it removes susceptible bacteria, so the survivors (resistant ones) dominate the next generations.",
        },
        {
            "text": r"When pollution darkened tree bark, dark peppered moths became more common because they:",
            "difficulty": 2,
            "choices": [("Were better camouflaged and survived predators more often", True),
                        ("Decided to change color", False),
                        ("Ate the light-colored moths", False),
                        ("Were unaffected by birds either way", False)],
            "explanation": r"On dark bark, dark moths were harder for birds to see, so more survived and reproduced, increasing the dark form.",
        },
        {
            "text": r"Does an antibiotic 'teach' bacteria how to become resistant?",
            "difficulty": 3,
            "choices": [("No — it selects bacteria that are already resistant or become so by mutation", True),
                        ("Yes — it trains each bacterium to resist", False),
                        ("Yes — it adds new genes to every cell", False),
                        ("No — resistance is impossible", False)],
            "explanation": r"The antibiotic does not create resistance. It simply selects for resistance that already exists in the population.",
        },
        {
            "text": ("Use the antibiotic-resistance diagram.\n\n"
                     "[[figure:antibiotic_resistance|Before, during, and after antibiotic use]]\n\n"
                     "After the antibiotic is applied, the surviving bacteria are mostly:"),
            "difficulty": 2,
            "choices": [("The resistant type", True),
                        ("The non-resistant type", False),
                        ("Completely dead", False),
                        ("Turned into plants", False)],
            "explanation": r"The diagram shows non-resistant bacteria dying and resistant ones surviving and multiplying. Pro tip: the antibiotic selects, it does not create, resistance.",
        },
        # --- Lesson 4: evidence ---
        {
            "text": r"Fossils provide evidence for evolution because they:",
            "difficulty": 1,
            "choices": [("Show organisms that lived in the past and how life changed over time", True),
                        ("Prove that species never change", False),
                        ("Are found only in living animals", False),
                        ("Show the future of a species", False)],
            "explanation": r"The fossil record preserves past life and reveals patterns of change, including transitional forms.",
        },
        {
            "text": r"The human arm, whale flipper, and bat wing share the same underlying bone arrangement. These are called:",
            "difficulty": 2,
            "choices": [("Homologous structures", True), ("Mutations", False),
                        ("Fossils", False), ("Adaptations to the same job", False)],
            "explanation": r"Homologous structures share structure (from a common ancestor) even though they are used for different jobs.",
        },
        {
            "text": r"Two species are found to share very similar DNA. This suggests that they:",
            "difficulty": 2,
            "choices": [("Are closely related (share a recent common ancestor)", True),
                        ("Live in the exact same place", False),
                        ("Have the same diet", False),
                        ("Cannot be related at all", False)],
            "explanation": r"The more DNA two species share, the more closely related they are likely to be.",
        },
        {
            "text": ("Use the limb diagram.\n\n"
                     "[[figure:homologous_structures|Matching bones in different animals' limbs]]\n\n"
                     "The matching bone pattern in these different limbs is best explained by:"),
            "difficulty": 2,
            "choices": [("Inheritance of the structure from a common ancestor", True),
                        ("Pure coincidence with no meaning", False),
                        ("The animals all living underwater", False),
                        ("The animals choosing the same bones", False)],
            "explanation": r"The shared bone arrangement, despite different uses, points to a common ancestor that had that limb structure. Pro tip: same structure, different jobs = homologous.",
        },
        {
            "text": r"Which situation provides the STRONGEST support for two species sharing a common ancestor?",
            "difficulty": 3,
            "choices": [("Fossils, body structures, and DNA all point to the same relationship", True),
                        ("They happen to be the same color", False),
                        ("They live on the same continent", False),
                        ("They are both large animals", False)],
            "explanation": r"Independent lines of evidence agreeing makes the conclusion far stronger than any single clue alone.",
        },
        # --- Lesson 5: cladograms ---
        {
            "text": r"A cladogram is a diagram that shows:",
            "difficulty": 1,
            "choices": [("How species are related (evolutionary relationships)", True),
                        ("The weather over a week", False),
                        ("How energy flows in a food chain", False),
                        ("A cell's organelles", False)],
            "explanation": r"A cladogram is a branching tree of hypothesized relationships among species.",
        },
        {
            "text": r"On a cladogram, two species are MOST closely related when they:",
            "difficulty": 2,
            "choices": [("Share the most recent common branch point", True),
                        ("Are printed closest together at the tips", False),
                        ("Have the longest names", False),
                        ("Live in the same habitat", False)],
            "explanation": r"Relatedness is shown by the branching pattern: the more recent the shared node, the closer the relationship.",
        },
        {
            "text": r"What does a branch point (node) on a cladogram represent?",
            "difficulty": 2,
            "choices": [("A common ancestor", True), ("A predator", False),
                        ("A fossil's exact age", False), ("A type of cell", False)],
            "explanation": r"Each node marks a common ancestor from which the branching lineages descend.",
        },
        {
            "text": ("Use the cladogram.\n\n"
                     "[[figure:cladogram|A branching evolutionary tree with shared traits]]\n\n"
                     "In the diagram, the dots placed at branch points are used to show:"),
            "difficulty": 2,
            "choices": [("Where a shared trait likely arose in a common ancestor", True),
                        ("Which species is the biggest", False),
                        ("The exact year each species appeared", False),
                        ("Which species is the strongest", False)],
            "explanation": r"Marks at nodes show where a new shared trait appeared, inherited by all branches above it. Pro tip: read nodes, not tip positions.",
        },
        # --- Lesson 6: adaptation, speciation, data ---
        {
            "text": r"An adaptation is:",
            "difficulty": 1,
            "choices": [("An inherited trait that improves survival or reproduction in an environment", True),
                        ("A scar from an injury", False),
                        ("A skill learned in one lifetime", False),
                        ("A temporary choice to hide", False)],
            "explanation": r"Adaptations are inherited (heritable) traits that help organisms survive and reproduce in their environment.",
        },
        {
            "text": r"A selection pressure is:",
            "difficulty": 2,
            "choices": [("An environmental factor that affects survival or reproduction", True),
                        ("A molecule that stores genetic code", False),
                        ("A type of cell organelle", False),
                        ("A food-chain arrow", False)],
            "explanation": r"Predators, climate, disease, food supply, and competition are all selection pressures that shape which traits are favored.",
        },
        {
            "text": r"Speciation (the forming of new species) can occur when populations:",
            "difficulty": 2,
            "choices": [("Become separated and accumulate different inherited changes over time", True),
                        ("Stop having DNA", False),
                        ("Become genetically identical", False),
                        ("Decide to become a new species in one generation", False)],
            "explanation": r"When gene flow is reduced (often by a barrier) and different environments select different traits, populations can diverge into separate species.",
        },
        {
            "text": r"Artificial selection differs from natural selection because artificial selection is guided by:",
            "difficulty": 2,
            "choices": [("Human choice", True), ("Gravity", False),
                        ("Random weather only", False), ("The absence of inheritance", False)],
            "explanation": r"In artificial selection, humans choose which organisms breed (dogs, crops, livestock). In natural selection, the environment does the 'selecting.'",
        },
        {
            "text": ("Use the speciation diagram.\n\n"
                     "[[figure:speciation|A barrier splits a population into two groups]]\n\n"
                     "According to the diagram, what often STARTS the process of speciation?"),
            "difficulty": 3,
            "choices": [("A barrier separates the population, reducing gene flow between the groups", True),
                        ("The whole population suddenly becomes identical", False),
                        ("The organisms stop reproducing forever", False),
                        ("The Sun changes the organisms directly", False)],
            "explanation": r"The diagram shows a barrier (like a river) splitting the population; the isolated groups then diverge as different environments select different traits. Pro tip: isolation reduces gene flow.",
        },
        {
            "text": r"A graph shows two traits changing together over time. Before concluding that one CAUSES the other, you should:",
            "difficulty": 3,
            "choices": [("Look for a controlled experiment, because correlation is not causation", True),
                        ("Assume the first trait causes the second", False),
                        ("Assume the data must be wrong", False),
                        ("Ignore the axis labels", False)],
            "explanation": r"Two variables moving together is a correlation. Showing cause and effect requires a controlled experiment that changes one factor while holding others constant.",
        },
    ],
    "essays": [
        {
            "text": (
                "A population of bacteria is treated with an antibiotic. At first the drug works, but over time it "
                "stops working and most of the bacteria are resistant. Use the four steps of natural selection "
                "(variation, inheritance, selection, time) to explain how the population became resistant, and "
                "explain why it is wrong to say the antibiotic 'taught' the bacteria to resist."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for applying all four steps: (1) variation -- a few bacteria already carried resistance "
                "(often from a mutation); (2) inheritance -- resistance is passed to offspring; (3) selection -- the "
                "antibiotic kills non-resistant bacteria, so resistant ones survive and reproduce; (4) time -- over "
                "generations the resistant trait becomes common. Plus: the antibiotic selects pre-existing resistance "
                "rather than creating it. Deduct for implying individual bacteria chose to become resistant."
            ),
        },
        {
            "text": (
                "Scientists use several independent lines of evidence to conclude that different species share common "
                "ancestors. Describe at least three lines of evidence (such as fossils, homologous structures, and "
                "DNA), and explain why having multiple lines of evidence that agree makes the conclusion stronger "
                "than any single line alone."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) fossils -- show past organisms and change over time; (2) homologous structures "
                "-- same underlying anatomy (e.g., human arm, whale flipper, bat wing) suggesting a common ancestor; "
                "(3) DNA similarities -- more shared DNA means closer relationship; (4) explaining that independent "
                "lines agreeing strengthens the conclusion because each could be questioned alone, but together they "
                "converge on the same family tree. Deduct for treating evolution as a single-file ladder rather than "
                "a branching tree."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Evolution & Natural Selection (Deep Dive)' course."

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

        # Phase 1 is MCQ-only: the written-response prompts above are not seeded.

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
