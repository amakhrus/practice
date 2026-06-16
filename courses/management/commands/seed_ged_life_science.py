"""
Seed data: 'GED Science: Life Science' -- the first content domain of the GED
Science test, built comprehensively and visually.

Covers cells, cellular energy, genetics, evolution, ecosystems, the human body,
and homeostasis -- plus the science-reasoning skill of reading data. Each lesson
leads with intuition and a real-world hook, includes labeled diagrams, a
common-misconception warning, and a quick tip. Practice questions mirror the
GED style, including diagram- and data-based items.

Run:
    python manage.py seed_ged_life_science
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Life Science",
    "slug": "ged-life-science",
    "program": "GED",
    "subject": "science",
    "description": (
        "Life Science is the largest part of the GED Science test. This course takes you "
        "from the tiny cell all the way up to whole ecosystems: how cells work and make "
        "energy, how traits are inherited, how species evolve, how energy flows through "
        "food chains, and how the human body keeps itself in balance. Every topic uses "
        "plain language, labeled diagrams, and GED-style practice with full explanations."
    ),
    "lessons": [
        (
            "1. The Cell: Life's Basic Unit",
            r"Every living thing — a bacterium, an oak tree, you — is built from **cells**. The **cell theory** sums up three big ideas:" "\n\n"
            r"- All living things are made of one or more cells." "\n"
            r"- The cell is the basic unit of structure and function in life." "\n"
            r"- All cells come from existing cells." "\n\n"
            r"There are two broad types. **Prokaryotic** cells (bacteria) are small and have **no nucleus** — their DNA floats freely. **Eukaryotic** cells (plants, animals, fungi) are larger and keep their DNA inside a **nucleus**, along with other specialized parts called **organelles**." "\n\n"
            r"[[figure:cell_animal|An animal cell. Each organelle has a specific job, like rooms in a tiny factory.]]" "\n\n"
            r"Key organelles and what they do:" "\n"
            r"- **Nucleus** — the control center; holds DNA, the cell's instructions." "\n"
            r"- **Mitochondria** — the 'powerhouse'; release energy (ATP) from food." "\n"
            r"- **Cell membrane** — the gatekeeper; controls what enters and leaves." "\n"
            r"- **Cytoplasm** — the jelly-like fluid where everything sits and reactions happen." "\n"
            r"- **Ribosomes** — build proteins." "\n\n"
            r"**Plant cells** add two parts animal cells don't have: a rigid **cell wall** for support, and **chloroplasts** that capture sunlight to make food." "\n\n"
            r"⚠️ Common misconception: bacteria are not 'simple animals'. They are prokaryotes — a completely separate, nucleus-free kind of cell." "\n\n"
            r"💡 Tip: remember 'mitochondria = powerhouse' and 'nucleus = control center'. Those two come up constantly.",
        ),
        (
            "2. Cellular Energy: Photosynthesis & Respiration",
            r"Life runs on energy, and that energy originally comes from the **Sun**. Two linked processes move it through living things." "\n\n"
            r"**Photosynthesis** happens in plants (in **chloroplasts**). Plants capture light and use it to turn simple ingredients into sugar:" "\n"
            r"\[ 6\,CO_2 + 6\,H_2O \;\overset{\text{light}}{\longrightarrow}\; C_6H_{12}O_6 + 6\,O_2. \]" "\n"
            r"In words: carbon dioxide + water + light → glucose (sugar) + oxygen." "\n\n"
            r"**Cellular respiration** happens in nearly all cells (in **mitochondria**). It does the reverse — it breaks sugar back down to release usable energy (ATP):" "\n"
            r"\[ C_6H_{12}O_6 + 6\,O_2 \;\to\; 6\,CO_2 + 6\,H_2O + \text{energy (ATP)}. \]" "\n\n"
            r"[[figure:energy_cycle|The two processes form a cycle: the products of one are the ingredients of the other.]]" "\n\n"
            r"Notice how they fit together: photosynthesis makes the glucose and oxygen that respiration uses, and respiration makes the carbon dioxide and water that photosynthesis uses." "\n\n"
            r"⚠️ Common misconception: plants do NOT only photosynthesize. Plants also do cellular respiration around the clock to use their stored energy." "\n\n"
            r"💡 Tip: photosynthesis **stores** energy in sugar; respiration **releases** it. One builds up, the other breaks down.",
        ),
        (
            "3. Genetics & Heredity",
            r"Why do you resemble your parents? The answer is **DNA** — a molecule shaped like a twisted ladder (a 'double helix') that stores instructions in a four-letter code (the bases A, T, C, G). A segment of DNA that codes for a trait is a **gene**." "\n\n"
            r"Key vocabulary:" "\n"
            r"- **Allele** — a version of a gene (for example, a 'brown eye' allele vs a 'blue eye' allele)." "\n"
            r"- **Dominant** (written capital, e.g. **B**) — shows up even if only one copy is present." "\n"
            r"- **Recessive** (lowercase, **b**) — only shows when BOTH copies are recessive." "\n"
            r"- **Genotype** — the actual alleles (BB, Bb, or bb). **Phenotype** — the visible trait." "\n\n"
            r"A **Punnett square** predicts offspring. Crossing two **Bb** parents:" "\n\n"
            r"[[figure:punnett_square|Each box is an equally likely combination. Three of four show the dominant trait.]]" "\n\n"
            r"The result is a **3 : 1** ratio — about 3 offspring show the dominant trait for every 1 that shows the recessive trait. Notice this is exactly the probability skill from math: each box is one equally likely outcome." "\n\n"
            r"⚠️ Common misconception: 'dominant' does not mean 'more common' or 'stronger'. It only means it needs just one copy to appear." "\n\n"
            r"💡 Tip: an organism showing a recessive trait must be **bb** — two recessive copies, no other way.",
        ),
        (
            "4. Evolution & Natural Selection",
            r"**Evolution** is the change in the inherited traits of a population over many generations. Its main engine is **natural selection**, an idea from Charles Darwin. The logic has four steps:" "\n\n"
            r"- **Variation** — individuals in a population differ (some beetles are darker, some lighter)." "\n"
            r"- **Inheritance** — many of those differences are passed to offspring." "\n"
            r"- **Selection** — the environment favors some traits; individuals with helpful traits survive and reproduce more." "\n"
            r"- **Time** — over generations, the helpful traits become more common." "\n\n"
            r"A classic example: **antibiotic resistance**. In a population of bacteria, a few happen to carry a gene that resists a drug. When antibiotics are used, the non-resistant bacteria die, but the resistant ones survive and multiply. Soon most of the population is resistant — evolution we can watch in real time." "\n\n"
            r"An **adaptation** is an inherited trait that improves survival or reproduction in a particular environment (a thick coat in the cold, camouflage from predators)." "\n\n"
            r"⚠️ Common misconception: individuals do not 'choose' to evolve, and a single organism does not evolve in its lifetime. **Populations** change across **generations**." "\n\n"
            r"💡 Tip: fossils, shared anatomy, and DNA similarities are all separate lines of evidence that point to evolution.",
        ),
        (
            "5. Ecosystems & Energy Flow",
            r"An **ecosystem** is all the living things in an area plus their non-living surroundings (water, soil, air, sunlight). Energy enters almost every ecosystem as **sunlight** and flows from one organism to the next." "\n\n"
            r"Organisms are grouped by how they get energy:" "\n"
            r"- **Producers** (plants) make their own food by photosynthesis." "\n"
            r"- **Consumers** eat other organisms (herbivores, carnivores, omnivores)." "\n"
            r"- **Decomposers** (fungi, bacteria) break down dead material and recycle nutrients." "\n\n"
            r"A **food chain** shows one path of energy; a **food web** is many chains linked together." "\n\n"
            r"[[figure:food_chain|Arrows point in the direction energy flows — from the food to the eater.]]" "\n\n"
            r"Energy is lost (mostly as heat) at each step, so only about **10%** passes to the next level. That's why there are many grass plants but few hawks — and why food chains rarely have more than four or five links." "\n\n"
            r"[[figure:energy_pyramid|Each level up has far less available energy, so it supports fewer organisms.]]" "\n\n"
            r"⚠️ Common misconception: the arrows in a food chain show the flow of **energy**, pointing toward the consumer — not 'who eats whom' in the opposite direction." "\n\n"
            r"💡 Tip: producers are always at the base of the energy pyramid because they capture energy first.",
        ),
        (
            "6. The Human Body Systems",
            r"The human body is a team of **organ systems** that each handle a job and work together to keep you alive. The major players:" "\n\n"
            r"- **Circulatory** — the heart pumps blood to carry oxygen, nutrients, and wastes. " "\n"
            r"- **Respiratory** — the lungs take in oxygen and release carbon dioxide (gas exchange)." "\n"
            r"- **Digestive** — breaks food into nutrients the body can absorb." "\n"
            r"- **Nervous** — the brain and nerves sense the environment and send fast signals." "\n"
            r"- **Skeletal** and **Muscular** — provide support, protection, and movement." "\n"
            r"- **Immune** — defends against germs." "\n\n"
            r"These systems are deeply connected. For example, the **respiratory** system brings in oxygen, the **circulatory** system delivers it to cells, and the cells use it for **cellular respiration** (from Lesson 2) to release energy. A problem in one system affects the others." "\n\n"
            r"⚠️ Common misconception: the lungs do not 'clean' the blood of all waste — they handle carbon dioxide. The kidneys filter other wastes from the blood." "\n\n"
            r"💡 Tip: when a question links two systems, look for what they exchange — usually oxygen, nutrients, or a signal.",
        ),
        (
            "7. Homeostasis & Reading Science Data",
            r"**Homeostasis** is the body's ability to keep a stable internal environment even as the outside changes — steady temperature, blood sugar, and water balance." "\n\n"
            r"It works through **feedback**: a sensor detects a change, and the body responds to push conditions back toward normal. When you get hot, you **sweat** to cool down; when you get cold, you **shiver** to warm up. Both responses fight the change — that's **negative feedback**." "\n\n"
            r"The GED Science test is as much about **reasoning with data** as memorizing facts. For any graph or table:" "\n"
            r"- Read the **title**, the **axis labels**, and the **units** first." "\n"
            r"- Find the **trend** — is the line rising, falling, or steady?" "\n"
            r"- Use only what the data **shows**; don't assume causes that aren't supported." "\n\n"
            r"For example, if a graph shows body temperature staying near 37 °C while the room temperature swings from 10 °C to 35 °C, the data is evidence of homeostasis at work." "\n\n"
            r"⚠️ Common misconception: **correlation is not causation**. Two things rising together does not prove one caused the other." "\n\n"
            r"💡 Tip: on data questions, point to the specific row, bar, or part of the line that supports your answer.",
        ),
    ],
    "mcqs": [
        {
            "text": r"Which organelle is known as the 'powerhouse of the cell' because it releases energy from food?",
            "difficulty": 1,
            "choices": [("Mitochondrion", True), ("Nucleus", False), ("Cell membrane", False), ("Ribosome", False)],
            "explanation": r"Mitochondria carry out cellular respiration, releasing energy (ATP) from glucose — hence 'powerhouse'. The nucleus is the control center.",
        },
        {
            "text": r"What is the main difference between a prokaryotic and a eukaryotic cell?",
            "difficulty": 2,
            "choices": [("Eukaryotic cells have a nucleus; prokaryotic cells do not", True),
                        ("Prokaryotic cells are always larger", False),
                        ("Only eukaryotic cells contain DNA", False),
                        ("Prokaryotic cells photosynthesize; eukaryotic cells do not", False)],
            "explanation": r"The defining difference is the nucleus: eukaryotes keep their DNA inside a nucleus, while prokaryotes (bacteria) have no nucleus. Both types contain DNA.",
        },
        {
            "text": r"Which structures are found in plant cells but NOT in animal cells?",
            "difficulty": 2,
            "choices": [("Cell wall and chloroplasts", True), ("Nucleus and ribosomes", False),
                        ("Mitochondria and cytoplasm", False), ("Cell membrane and nucleus", False)],
            "explanation": r"Plant cells add a rigid cell wall (support) and chloroplasts (photosynthesis). Both cell types share the nucleus, ribosomes, mitochondria, cytoplasm, and membrane.",
        },
        {
            "text": r"In photosynthesis, which two ingredients does a plant combine using light energy?",
            "difficulty": 2,
            "choices": [("Carbon dioxide and water", True), ("Oxygen and glucose", False),
                        ("Glucose and water", False), ("Oxygen and carbon dioxide", False)],
            "explanation": r"Photosynthesis uses carbon dioxide + water + light to produce glucose and oxygen. Oxygen and glucose are the products, not the ingredients.",
        },
        {
            "text": r"Cellular respiration takes place mainly in which organelle?",
            "difficulty": 1,
            "choices": [("Mitochondria", True), ("Chloroplasts", False), ("Nucleus", False), ("Cell wall", False)],
            "explanation": r"Respiration releases energy from glucose in the mitochondria. (Photosynthesis is the one that happens in chloroplasts.)",
        },
        {
            "text": r"Two parents are each Bb for a trait where B (brown) is dominant over b (blue). What fraction of their offspring is expected to show the blue (recessive) trait?",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{3}{4}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(0\)", False)],
            "explanation": r"A Bb × Bb cross gives BB, Bb, Bb, bb. Only bb (1 of the 4 boxes) shows the recessive trait, so \(\frac{1}{4}\).",
        },
        {
            "text": r"An organism shows a recessive trait. What must its genotype be?",
            "difficulty": 2,
            "choices": [("bb (two recessive alleles)", True), ("BB", False), ("Bb", False), ("Either BB or Bb", False)],
            "explanation": r"A recessive trait only appears when both alleles are recessive, so the genotype must be bb. Even one dominant allele (Bb) would show the dominant trait.",
        },
        {
            "text": r"A population of bacteria is treated with an antibiotic. A few survive and multiply. This is an example of:",
            "difficulty": 2,
            "choices": [("Natural selection", True), ("Photosynthesis", False),
                        ("Homeostasis", False), ("A single bacterium choosing to adapt", False)],
            "explanation": r"The resistant individuals survive and reproduce while others die, so resistance spreads — natural selection. No individual 'chooses' to adapt.",
        },
        {
            "text": r"Which best describes evolution by natural selection?",
            "difficulty": 3,
            "choices": [("Inherited traits in a population change over many generations", True),
                        ("An individual changes its traits during its lifetime", False),
                        ("Organisms gain traits because they need them", False),
                        ("Traits change randomly with no effect on survival", False)],
            "explanation": r"Evolution acts on populations across generations, favoring inherited traits that improve survival and reproduction — not on individuals within one lifetime.",
        },
        {
            "text": r"In a food chain, what do the arrows represent?",
            "difficulty": 1,
            "choices": [("The flow of energy from food to consumer", True),
                        ("The direction predators run", False),
                        ("Which organism is largest", False),
                        ("The flow of energy from consumer to food", False)],
            "explanation": r"Arrows point from the organism being eaten toward the one eating it, showing the direction energy flows.",
        },
        {
            "text": r"About how much of the energy at one level of an energy pyramid is passed to the next level up?",
            "difficulty": 2,
            "choices": [("About 10%", True), ("About 50%", False), ("About 90%", False), ("100%", False)],
            "explanation": r"Roughly 10% of energy transfers to the next level; the rest is lost mostly as heat. This is why higher levels support far fewer organisms.",
        },
        {
            "text": r"Which pair of body systems works together to take in oxygen and deliver it to the body's cells?",
            "difficulty": 2,
            "choices": [("Respiratory and circulatory", True), ("Digestive and nervous", False),
                        ("Skeletal and muscular", False), ("Immune and digestive", False)],
            "explanation": r"The respiratory system brings oxygen into the lungs; the circulatory system carries it in the blood to all cells.",
        },
        {
            "text": r"When you get too hot, your body sweats to cool down. This is an example of:",
            "difficulty": 1,
            "choices": [("Homeostasis", True), ("Natural selection", False),
                        ("Photosynthesis", False), ("Inheritance", False)],
            "explanation": r"Sweating to return body temperature toward normal is homeostasis — maintaining a stable internal environment through feedback.",
        },
        {
            "text": r"A graph shows that as ice cream sales rise, sunburns also rise. What is the best conclusion?",
            "difficulty": 3,
            "choices": [("Both may be caused by a third factor, like hot, sunny weather", True),
                        ("Eating ice cream causes sunburn", False),
                        ("Sunburns make people buy ice cream", False),
                        ("The data must be wrong", False)],
            "explanation": r"This is correlation, not causation. Two things rising together doesn't mean one causes the other; a third factor (hot weather) likely drives both.",
        },
        {
            "text": ("Use the food chain shown.\n\n"
                     "[[figure:food_chain|A food chain from grass to a hawk]]\n\n"
                     "In this food chain, which organism is the producer?"),
            "difficulty": 1,
            "choices": [("Grass", True), ("Grasshopper", False), ("Frog", False), ("Hawk", False)],
            "explanation": r"Producers make their own food by photosynthesis, so the grass at the base of the chain is the producer. The grasshopper, frog, and hawk are all consumers. Pro tip: the producer is where the chain starts, right after the Sun.",
        },
        {
            "text": ("Use the energy pyramid shown.\n\n"
                     "[[figure:energy_pyramid|Energy available at each feeding level]]\n\n"
                     "According to the pyramid, about how much energy is available to the secondary (2nd-level) consumers?"),
            "difficulty": 2,
            "choices": [("About 10 kcal", True), ("About 100 kcal", False), ("About 1000 kcal", False), ("About 1 kcal", False)],
            "explanation": r"Each level keeps only about 10% of the energy below it: 1000 (producers) to 100 (primary consumers) to 10 kcal (secondary consumers). Pro tip: energy drops by roughly 90% at each step up the pyramid.",
        },
        {
            "text": ("Use the Punnett square shown for a Bb x Bb cross.\n\n"
                     "[[figure:punnett_square|A Bb by Bb cross]]\n\n"
                     "Based on the square, what is the ratio of dominant to recessive phenotypes among the offspring?"),
            "difficulty": 2,
            "choices": [("3 : 1", True), ("1 : 1", False), ("1 : 3", False), ("4 : 0", False)],
            "explanation": r"Three boxes (BB, Bb, Bb) show the dominant trait and one (bb) shows the recessive trait, a 3 : 1 ratio. Pro tip: only the bb box gives the recessive phenotype.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain how photosynthesis and cellular respiration are connected. In your answer, name where "
                "each process happens, list the main inputs and outputs of each, and describe how the two "
                "processes form a cycle that keeps carbon and oxygen moving through living things."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) photosynthesis occurs in chloroplasts, using CO2 + water + light to make "
                "glucose + oxygen; (2) respiration occurs in mitochondria, using glucose + oxygen to release "
                "CO2 + water + energy (ATP); (3) explaining that the outputs of one are the inputs of the other, "
                "forming a cycle. Deduct for missing locations, reversed inputs/outputs, or no cycle explanation."
            ),
        },
        {
            "text": (
                "A type of moth comes in light and dark colors. After a forest's tree bark becomes darker from "
                "pollution, the dark moths become far more common over several generations. Use the four steps "
                "of natural selection (variation, inheritance, selection, time) to explain why this happened."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for applying all four steps: (1) variation — both light and dark moths exist; "
                "(2) inheritance — color is passed to offspring; (3) selection — on dark bark, dark moths are "
                "better camouflaged from predators and survive/reproduce more; (4) time — over generations the "
                "dark trait becomes more common. Deduct for any missing step or for implying individual moths changed color."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'GED Science: Life Science' course."

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
