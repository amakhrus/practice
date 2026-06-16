"""
Seed data: 'GED Science: Genetics & Heredity (Deep Dive)'.

A focused EXPANSION of Lesson 3 ("Genetics & Heredity") from the broader
'GED Science: Life Science' course, brought up to the full deep-dive standard
(6 lessons, ~30 MCQs, 2 extended prompts, all-new diagrams):

  1. DNA -- the molecule of heredity (structure and base pairing).
  2. Genes, chromosomes & proteins (from DNA to traits).
  3. Alleles, genotype & phenotype (dominant and recessive).
  4. Punnett squares & probability.
  5. Meiosis, sex cells & variation.
  6. Mutations, pedigrees & reading genetic data.

This course uses ALL-NEW diagrams (a DNA double helix, a chromosome-to-gene zoom,
dominant/recessive genotypes, a worked Tt x Tt Punnett square, mitosis vs.
meiosis, and a pedigree chart) rather than reusing the parent course's single
'punnett_square' figure.

Each lesson keeps the parent course's style: a plain-language hook, a labeled
diagram, a "common misconception" warning, and a quick tip. Practice questions
mirror GED Science item types, including diagram- and data-based items.

GED note: the GED Science test is multiple-choice / technology-enhanced; the
Science Short Answer items were removed in 2017. The two extended prompts below
are kept as study material only and, like the parent course, are NOT seeded by
this command (Phase 1 is MCQ-only).

Scientific accuracy & sources:
  - OpenStax, *Biology* and *Concepts of Biology* (DNA, inheritance, meiosis).
  - Campbell & Reece, *Biology*; Mendel's laws of inheritance.
  - National Human Genome Research Institute (NHGRI) / NIH; MedlinePlus Genetics.
Note: human body cells have 46 chromosomes (23 pairs); DNA bases pair A-T and G-C;
a monohybrid Tt x Tt cross gives a 1:2:1 genotype ratio and a 3:1 phenotype ratio.

Run:
    python manage.py seed_ged_genetics_heredity
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Genetics & Heredity (Deep Dive)",
    "slug": "ged-genetics-heredity",
    "program": "GED",
    "subject": "science",
    "description": (
        "A deep dive into how traits are passed from parents to offspring, expanding the single "
        "'Genetics & Heredity' lesson from the GED Life Science course into a full mini-course. You'll "
        "explore DNA and its base-pairing code, how genes and chromosomes carry instructions to build "
        "proteins, the difference between genotype and phenotype, how to use Punnett squares to predict "
        "offspring, how meiosis creates variation, and how mutations and pedigrees reveal inheritance "
        "patterns. Plain language, all-new labeled diagrams, common-misconception warnings, and "
        "GED-style practice with full explanations throughout."
    ),
    "lessons": [
        (
            "1. DNA: The Molecule of Heredity",
            r"Why do you resemble your parents? The answer is **DNA** — the molecule that stores the inherited instructions for building and running a living thing. Every one of your cells carries a copy." "\n\n"
            r"[[figure:dna_double_helix|DNA is a twisted ladder. Its rungs are base pairs, and the bases always pair A with T and G with C.]]" "\n\n"
            r"DNA is shaped like a twisted ladder called a **double helix**. The two sides (the 'rails') are a **sugar-phosphate backbone**. The 'rungs' are pairs of chemical **bases**, and there are only four: **A, T, G, and C**. The bases follow a strict **pairing rule**:" "\n"
            r"- **A** always pairs with **T**." "\n"
            r"- **G** always pairs with **C**." "\n\n"
            r"That pairing rule is powerful: because each base has exactly one partner, a strand of DNA can be **copied** precisely. Before a cell divides, the ladder 'unzips' and each side serves as a template to build a matching new strand — so every new cell gets a complete set of instructions." "\n\n"
            r"⚠️ Common misconception: DNA is not found only in a special 'master' cell. The **same** DNA is packed into nearly **every** cell of your body." "\n\n"
            r"💡 Tip: remember the base pairs — **A–T and G–C.** They never pair any other way.",
        ),
        (
            "2. Genes, Chromosomes & Proteins",
            r"DNA is a very long molecule, so cells keep it organized. Understanding three nested terms unlocks most genetics questions." "\n\n"
            r"[[figure:dna_gene_chromosome|A chromosome is tightly packed DNA; a gene is a specific segment of that DNA.]]" "\n\n"
            r"- A **chromosome** is a long, organized **package** of DNA. Human **body cells** have **46 chromosomes** — 23 pairs, with one of each pair inherited from each biological parent." "\n"
            r"- A **gene** is a **segment** of DNA that carries the instructions for a particular trait or product." "\n"
            r"- Those instructions are mostly directions to build **proteins**, the molecules that do the cell's work and shape its traits." "\n\n"
            r"So the chain of information runs: **DNA → genes → proteins → traits.** A gene's code is read and used to assemble a protein; the proteins a cell makes help determine features like eye color, blood type, or how an enzyme works." "\n\n"
            r"⚠️ Common misconception: a gene and a chromosome are **not** the same size. A gene is **one section** of DNA; a chromosome is a **large package** containing **many** genes." "\n\n"
            r"💡 Tip: **gene = one instruction; chromosome = a bundle of many instructions.** Genes code for proteins, and proteins build traits.",
        ),
        (
            "3. Alleles, Genotype & Phenotype",
            r"Most genes come in different **versions**, called **alleles** — for example, an allele for a tall plant and an allele for a short plant. Since you inherit one allele from each parent, you carry **two** alleles for each gene." "\n\n"
            r"[[figure:dominant_recessive|With one dominant allele (T), the plant is tall; only two recessive alleles (tt) make it short.]]" "\n\n"
            r"Some key vocabulary, using **T** (tall) and **t** (short):" "\n"
            r"- A **dominant** allele (capital, **T**) shows up even if only **one** copy is present." "\n"
            r"- A **recessive** allele (lowercase, **t**) shows only when **both** copies are recessive." "\n"
            r"- **Genotype** is the pair of alleles you have (**TT**, **Tt**, or **tt**); **phenotype** is the visible trait (tall or short)." "\n"
            r"- **Homozygous** means two of the same allele (**TT** or **tt**); **heterozygous** means two different (**Tt**)." "\n\n"
            r"So **TT** and **Tt** both look **tall**, because one dominant T is enough. Only **tt** is short." "\n\n"
            r"⚠️ Common misconception: 'dominant' does **not** mean 'stronger,' 'better,' or 'more common.' It only means **one copy is enough** for the trait to appear." "\n\n"
            r"💡 Tip: if an organism **shows a recessive trait**, its genotype **must** be two recessive alleles (**tt**) — there's no other way.",
        ),
        (
            "4. Punnett Squares & Probability",
            r"A **Punnett square** is a simple grid that predicts the **probability** of an offspring's genotypes and phenotypes. Each parent's two alleles go along the top and side, and each box combines one allele from each parent." "\n\n"
            r"[[figure:punnett_square_worked|A Tt x Tt cross gives a 1:2:1 genotype ratio and a 3:1 tall-to-short phenotype ratio.]]" "\n\n"
            r"Cross two heterozygous tall plants, **Tt × Tt**. The four equally likely boxes are **TT, Tt, Tt, tt**:" "\n"
            r"- **Genotype ratio:** 1 TT : 2 Tt : 1 tt." "\n"
            r"- **Phenotype ratio:** 3 tall : 1 short (because TT, Tt, and Tt are all tall; only tt is short)." "\n\n"
            r"This is exactly the **probability** skill from math: each box is one equally likely outcome. So the chance of a short (tt) plant is **1 out of 4 = 1/4 = 25%**, and the chance of a tall plant is **3/4 = 75%**. A GED question may ask for a fraction, a percent, or a ratio — so be ready to convert between them." "\n\n"
            r"⚠️ Common misconception: a Punnett square predicts **probabilities**, not a guarantee. A 3:1 ratio doesn't mean a family of four children must have exactly three tall and one short." "\n\n"
            r"💡 Tip: **count the boxes**, then convert to the form the question asks — 1 of 4 is 1/4 or 25%; 2 of 4 is 1/2 or 50%.",
        ),
        (
            "5. Meiosis, Sex Cells & Variation",
            r"If each parent passed on **all** of their chromosomes, offspring would have double the normal number. The body avoids this with a special kind of cell division called **meiosis**, which makes **sex cells** (eggs and sperm)." "\n\n"
            r"[[figure:mitosis_vs_meiosis|Mitosis makes two identical body cells; meiosis makes four varied sex cells with half the chromosomes.]]" "\n\n"
            r"Compare the two kinds of division:" "\n"
            r"- **Mitosis** makes **two genetically identical** body cells with the **full** chromosome number — for **growth and repair**." "\n"
            r"- **Meiosis** makes **four** sex cells, each with **half** the chromosome number. When a sperm and egg join at **fertilization**, the full number is restored." "\n\n"
            r"Meiosis is also the main source of **variation**, which is why siblings (other than identical twins) look different. The chromosome pairs are shuffled into different combinations, sections can swap during **crossing over**, and any sperm can combine with any egg. This variation is the raw material that **natural selection** acts on." "\n\n"
            r"⚠️ Common misconception: meiosis and mitosis are **not** interchangeable. Mitosis = identical body cells; meiosis = varied sex cells with **half** the chromosomes." "\n\n"
            r"💡 Tip: **mitosis = copy (2 identical); meiosis = sex cells (4 different, half the chromosomes).**",
        ),
        (
            "6. Mutations, Pedigrees & Reading Genetic Data",
            r"A **mutation** is a change in the DNA sequence. Its effect depends on where it happens: some mutations are **neutral** (no real effect), some are **harmful**, and a few are **helpful** in a particular environment. A mutation in a **sex cell** can be passed to offspring; a mutation in an ordinary **body cell** usually affects only that individual." "\n\n"
            r"[[figure:pedigree_chart|In a pedigree, squares are males, circles are females, and shaded symbols show individuals with the trait.]]" "\n\n"
            r"A **pedigree chart** tracks a trait through a family. **Squares** are males, **circles** are females, and **shaded** symbols mark individuals who **have** the trait. A classic clue: if **two unaffected parents** have a child **who is affected**, the trait is most likely **recessive** (both parents were carriers)." "\n\n"
            r"Traits aren't always set by genes alone — **environment** matters too. Nutrition, temperature, and sunlight can all influence a phenotype, so genes and environment often work together." "\n\n"
            r"**Reading genetic data (a GED skill).** Items may give a Punnett square, a ratio, or a pedigree and ask what it shows. Track exactly **who is affected**, use the **legend**, and conclude only what the data supports. And remember: **correlation is not causation**." "\n\n"
            r"⚠️ Common misconception: not every mutation is harmful. A mutation is simply a **DNA change** — its effect can be neutral, harmful, or helpful." "\n\n"
            r"💡 Tip: for a pedigree, find **who has the trait**, then ask which **genotypes** are possible — two unaffected parents with an affected child points to a **recessive** trait." "\n\n"
            r"📚 Sources: OpenStax *Biology* / *Concepts of Biology*; Campbell & Reece, *Biology*; NHGRI / NIH; MedlinePlus Genetics; Mendel's laws.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: DNA ---
        {
            "text": r"Which molecule stores the inherited instructions in living things?",
            "difficulty": 1,
            "choices": [("DNA", True), ("ATP", False),
                        ("Glucose", False), ("Water", False)],
            "explanation": r"DNA carries the genetic instructions that are passed from parents to offspring and used to build and run cells.",
        },
        {
            "text": r"The overall shape of a DNA molecule is described as a:",
            "difficulty": 1,
            "choices": [("Double helix (twisted ladder)", True),
                        ("Flat square", False),
                        ("Single straight line", False),
                        ("Solid ball", False)],
            "explanation": r"DNA's two strands wind around each other in a double helix, like a twisted ladder.",
        },
        {
            "text": r"In DNA, the base A (adenine) always pairs with:",
            "difficulty": 2,
            "choices": [("T", True), ("G", False), ("C", False), ("A", False)],
            "explanation": r"The base-pairing rule is A with T and G with C. These pairs never change.",
        },
        {
            "text": r"In DNA, the base G (guanine) always pairs with:",
            "difficulty": 2,
            "choices": [("C", True), ("A", False), ("T", False), ("G", False)],
            "explanation": r"G always pairs with C, just as A always pairs with T.",
        },
        {
            "text": ("Use the DNA diagram.\n\n"
                     "[[figure:dna_double_helix|The structure of DNA]]\n\n"
                     "According to the diagram, the 'rungs' of the DNA ladder are made of:"),
            "difficulty": 2,
            "choices": [("Base pairs (A-T and G-C)", True),
                        ("Sugar and phosphate", False),
                        ("Whole proteins", False),
                        ("Water molecules", False)],
            "explanation": r"The rungs are base pairs; the rails (sides) are the sugar-phosphate backbone. Pro tip: backbone = sides, base pairs = rungs.",
        },
        # --- Lesson 2: genes, chromosomes, proteins ---
        {
            "text": r"A segment of DNA that carries instructions for a trait is called a:",
            "difficulty": 1,
            "choices": [("Gene", True), ("Chromosome", False),
                        ("Cell", False), ("Protein", False)],
            "explanation": r"A gene is a section of DNA that codes for a trait or a functional product such as a protein.",
        },
        {
            "text": r"A long, organized package of DNA that contains many genes is a:",
            "difficulty": 1,
            "choices": [("Chromosome", True), ("Gene", False),
                        ("Ribosome", False), ("Vacuole", False)],
            "explanation": r"Chromosomes are tightly packed DNA. Each chromosome holds many genes.",
        },
        {
            "text": r"How many chromosomes are in a typical human body cell?",
            "difficulty": 2,
            "choices": [("46 (23 pairs)", True), ("2", False),
                        ("23 (no pairs)", False), ("100", False)],
            "explanation": r"Human body cells have 46 chromosomes arranged in 23 pairs, with one of each pair from each parent.",
        },
        {
            "text": r"Genes mainly carry instructions to build which molecules that shape an organism's traits?",
            "difficulty": 2,
            "choices": [("Proteins", True), ("Rocks", False),
                        ("Vitamins", False), ("Sugars only", False)],
            "explanation": r"Genes code for proteins. Proteins do much of the cell's work and help determine traits.",
        },
        {
            "text": r"Which statement about genes and chromosomes is correct?",
            "difficulty": 3,
            "choices": [("A gene is a section of DNA; a chromosome is a much larger package of DNA", True),
                        ("A gene is larger than a chromosome", False),
                        ("They are exactly the same thing", False),
                        ("A chromosome is a single base pair", False)],
            "explanation": r"A chromosome is a large DNA package made of many genes, so a gene (one section) is far smaller than a chromosome.",
        },
        # --- Lesson 3: alleles, genotype, phenotype ---
        {
            "text": r"Different versions of the same gene are called:",
            "difficulty": 1,
            "choices": [("Alleles", True), ("Proteins", False),
                        ("Cells", False), ("Ribosomes", False)],
            "explanation": r"An allele is one version of a gene, such as a tall allele versus a short allele.",
        },
        {
            "text": r"The visible trait an organism shows is its:",
            "difficulty": 1,
            "choices": [("Phenotype", True), ("Genotype", False),
                        ("Allele only", False), ("Chromosome number", False)],
            "explanation": r"Phenotype is the observable trait. Genotype is the underlying pair of alleles.",
        },
        {
            "text": r"If T (tall) is dominant over t (short), which genotype produces a SHORT plant?",
            "difficulty": 2,
            "choices": [("tt", True), ("TT", False),
                        ("Tt", False), ("T", False)],
            "explanation": r"A recessive trait appears only with two recessive alleles, so a short plant must be tt. Both TT and Tt are tall.",
        },
        {
            "text": r"An organism with two identical alleles (such as TT or tt) is said to be:",
            "difficulty": 2,
            "choices": [("Homozygous", True), ("Heterozygous", False),
                        ("Recessive only", False), ("Mutated", False)],
            "explanation": r"Homozygous means two of the same allele. Heterozygous (Tt) means two different alleles.",
        },
        {
            "text": ("Use the genotype diagram.\n\n"
                     "[[figure:dominant_recessive|TT, Tt, and tt and their phenotypes]]\n\n"
                     "According to the diagram, why do both TT and Tt plants look tall?"),
            "difficulty": 3,
            "choices": [("One dominant allele (T) is enough to show the dominant (tall) trait", True),
                        ("They both have two short alleles", False),
                        ("Tall is recessive", False),
                        ("They have no alleles at all", False)],
            "explanation": r"A single dominant T produces the tall phenotype, so TT and Tt both look tall. Only tt (two recessive) is short. Pro tip: one dominant copy is enough.",
        },
        # --- Lesson 4: Punnett squares ---
        {
            "text": r"A Punnett square is mainly used to:",
            "difficulty": 1,
            "choices": [("Predict the probability of offspring genotypes and phenotypes", True),
                        ("Measure a cell's energy", False),
                        ("Show the order of the planets", False),
                        ("Balance a chemical equation", False)],
            "explanation": r"A Punnett square combines the parents' alleles to predict the likely genotypes and phenotypes of their offspring.",
        },
        {
            "text": r"In a Tt x Tt cross, what fraction of offspring is expected to be short (tt)?",
            "difficulty": 2,
            "choices": [("1/4", True), ("3/4", False),
                        ("1/2", False), ("1", False)],
            "explanation": r"The four boxes are TT, Tt, Tt, and tt, so one of four (1/4) is tt (short).",
        },
        {
            "text": r"In a Tt x Tt cross with complete dominance, the phenotype ratio is:",
            "difficulty": 2,
            "choices": [("3 tall : 1 short", True), ("1 tall : 3 short", False),
                        ("2 tall : 2 short", False), ("4 short : 0 tall", False)],
            "explanation": r"TT, Tt, and Tt are tall; only tt is short, giving a 3:1 tall-to-short ratio.",
        },
        {
            "text": ("Use the Punnett square.\n\n"
                     "[[figure:punnett_square_worked|A Tt x Tt cross and its results]]\n\n"
                     "Based on the square, what is the probability that an offspring is TALL?"),
            "difficulty": 2,
            "choices": [("3/4 (75%)", True), ("1/4 (25%)", False),
                        ("1/2 (50%)", False), ("0", False)],
            "explanation": r"Three of the four boxes (TT, Tt, Tt) are tall, so P(tall) = 3/4 = 75%. Pro tip: count the boxes, then convert.",
        },
        {
            "text": r"In a Tt x Tt cross, two of the four boxes are Tt. As a percent, that is:",
            "difficulty": 3,
            "choices": [("50%", True), ("25%", False),
                        ("75%", False), ("100%", False)],
            "explanation": r"Two of four boxes is 2/4 = 1/2 = 50% of offspring expected to be heterozygous (Tt).",
        },
        # --- Lesson 5: meiosis & variation ---
        {
            "text": r"Which process produces sex cells (eggs and sperm)?",
            "difficulty": 1,
            "choices": [("Meiosis", True), ("Mitosis", False),
                        ("Photosynthesis", False), ("Digestion", False)],
            "explanation": r"Meiosis makes sex cells with half the chromosome number. Mitosis makes identical body cells.",
        },
        {
            "text": r"Compared with a normal body cell, a sex cell made by meiosis has:",
            "difficulty": 2,
            "choices": [("Half the number of chromosomes", True),
                        ("Twice the number of chromosomes", False),
                        ("No chromosomes", False),
                        ("Exactly the same number", False)],
            "explanation": r"Meiosis halves the chromosome number so that fertilization restores the full number in the offspring.",
        },
        {
            "text": r"Which process makes two genetically identical cells for growth and repair?",
            "difficulty": 1,
            "choices": [("Mitosis", True), ("Meiosis", False),
                        ("Fermentation", False), ("Natural selection", False)],
            "explanation": r"Mitosis produces two identical daughter cells with the full chromosome number, used for growth and repair.",
        },
        {
            "text": ("Use the cell-division diagram.\n\n"
                     "[[figure:mitosis_vs_meiosis|Mitosis compared with meiosis]]\n\n"
                     "According to the diagram, meiosis produces:"),
            "difficulty": 2,
            "choices": [("Four cells, each with half the chromosome number", True),
                        ("Two identical cells with the full chromosome number", False),
                        ("One giant cell", False),
                        ("No new cells", False)],
            "explanation": r"The diagram shows meiosis making four varied cells with half the chromosomes, while mitosis makes two identical cells. Pro tip: meiosis = 4 different, half; mitosis = 2 identical, full.",
        },
        {
            "text": r"Why do most siblings (other than identical twins) look different from each other?",
            "difficulty": 2,
            "choices": [("Meiosis and fertilization shuffle genes, creating variation", True),
                        ("Each child has completely different DNA from any human", False),
                        ("Siblings share no genes at all", False),
                        ("Mitosis randomly changes their traits", False)],
            "explanation": r"Meiosis mixes the chromosome combinations (and crossing over swaps sections), and any sperm can fertilize any egg, so offspring vary.",
        },
        # --- Lesson 6: mutations, pedigrees, data ---
        {
            "text": r"A change in the DNA sequence is called a:",
            "difficulty": 1,
            "choices": [("Mutation", True), ("Phenotype", False),
                        ("Genotype", False), ("Ratio", False)],
            "explanation": r"A mutation is any change in DNA. Its effect can be neutral, harmful, or helpful.",
        },
        {
            "text": r"Are all mutations harmful?",
            "difficulty": 2,
            "choices": [("No — some are neutral, and a few are even helpful", True),
                        ("Yes — every mutation causes disease", False),
                        ("Yes — mutations always kill the cell", False),
                        ("No — mutations never affect anything", False)],
            "explanation": r"A mutation is just a DNA change. Depending on where it occurs and the environment, it may have no effect, be harmful, or be beneficial.",
        },
        {
            "text": ("Use the pedigree chart.\n\n"
                     "[[figure:pedigree_chart|A family pedigree]]\n\n"
                     "In the pedigree, a shaded SQUARE represents:"),
            "difficulty": 2,
            "choices": [("A male who has the trait", True),
                        ("A female who has the trait", False),
                        ("A male without the trait", False),
                        ("A chromosome", False)],
            "explanation": r"Squares are males and circles are females; shading means the individual has the trait. So a shaded square is an affected male. Pro tip: square = male, circle = female, shaded = affected.",
        },
        {
            "text": r"Two parents who do NOT show a trait have a child who DOES. The trait is most likely:",
            "difficulty": 3,
            "choices": [("Recessive (both parents were carriers)", True),
                        ("Dominant", False),
                        ("Caused only by the environment", False),
                        ("Impossible to inherit", False)],
            "explanation": r"If neither parent shows the trait but a child does, each parent likely carried a hidden recessive allele (they were Tt), and the child inherited tt.",
        },
    ],
    "essays": [
        {
            "text": (
                "Explain how DNA, genes, chromosomes, and traits are related. In your answer, describe the basic "
                "structure of DNA (including base pairing), explain the difference between a gene and a chromosome, "
                "and describe how the information in DNA leads to an organism's traits."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) DNA is a double helix with a sugar-phosphate backbone and base pairs that pair "
                "A-T and G-C; (2) a gene is a segment of DNA, while a chromosome is a large package of DNA containing "
                "many genes; (3) genes carry instructions to build proteins, and proteins help determine traits "
                "(DNA -> genes -> proteins -> traits). Deduct for equating a gene with a chromosome or reversing the "
                "base-pairing rule."
            ),
        },
        {
            "text": (
                "Two heterozygous tall pea plants (Tt) are crossed, where T (tall) is dominant over t (short). "
                "Describe the Punnett square for this cross, give the genotype and phenotype ratios, and find the "
                "probability that an offspring is short. Then explain what 'dominant' really means and why a dominant "
                "trait is not necessarily the most common one in a population."
            ),
            "difficulty": 3,
            "rubric": (
                "Full marks for: (1) the cross gives boxes TT, Tt, Tt, tt; (2) genotype ratio 1 TT : 2 Tt : 1 tt; "
                "(3) phenotype ratio 3 tall : 1 short; (4) probability of a short (tt) offspring is 1/4 (25%); "
                "(5) 'dominant' means one copy is enough to show the trait, NOT that it is stronger or more common -- "
                "frequency depends on how common the alleles are. Deduct for wrong ratios or claiming dominant always "
                "means more common."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the in-depth 'GED Science: Genetics & Heredity (Deep Dive)' course."

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
