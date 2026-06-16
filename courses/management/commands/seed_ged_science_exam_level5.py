"""
Seed a FIFTH and FINAL full-length 'GED Science' practice exam -- Level 5, the
elite tier, the hardest of the set. Same test-day structure (34 questions; 90
minutes; scored 100-200, 145 to pass). Every item is a hard, multi-layered
problem at the ceiling of the GED's range: quantitative synthesis, equilibrium
and momentum, dihybrid and allele-frequency reasoning, evaluating data and
conclusions, and cosmology.

Run:
    python manage.py seed_ged_science_exam_level5
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Science: Full-Length Practice Exam (Level 5 - Elite)",
    "slug": "ged-science-exam-level5",
    "program": "GED",
    "subject": "science",
    "description": (
        "The fifth and hardest full-length GED Science practice exam -- the elite tier, for students who "
        "have cleared Levels 1-4 and want the toughest possible rehearsal. Same test-day format -- 34 "
        "questions across Life, Physical, and Earth & Space Science, 90 minutes, scored 100-200 (145 to "
        "pass) -- but every item sits at the ceiling of the range: quantitative synthesis, equilibrium "
        "and momentum, dihybrid and allele-frequency reasoning, evaluating data against conclusions, and "
        "cosmology. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 5: The Elite Science Test",
            r"""
This is the **elite** GED Science practice exam -- the toughest of all five. The format never changes:

- **34 questions** in **90 minutes**, across **Life**, **Physical**, and **Earth & Space Science**; scored **100-200**, **145 to pass**.

**What makes Level 5 the hardest of all:** there is not a single routine question. You will run **multi-step calculations**, reason about **equilibrium, momentum, and energy**, predict **dihybrid and allele-frequency outcomes**, decide whether **data truly supports a conclusion**, and apply ideas from **cosmology**. If you can score well here, the real GED Science test will feel comfortable.

[[check:If a quantity decays by half every step, what fraction remains after 3 half-lives?|1/8;;one eighth;;0.125|Three halvings: 1/2 of 1/2 of 1/2 = 1/8.]]
            """,
        ),
        (
            "2. Reasoning at the Highest Level",
            r"""
Elite science demands precise quantitative and evaluative thinking.

- **Square and cube relationships.** Kinetic energy depends on the square of speed; doubling speed quadruples energy.
- **Conservation in collisions.** Total momentum is conserved before and after a collision.
- **Inheritance probability.** Dihybrid crosses give a 9:3:3:1 ratio; combine probabilities for specific outcomes.
- **Data vs. conclusion.** Ask whether the evidence actually supports the claim, controls for confounding factors, and rules out chance.
- **Cosmic evidence.** Redshift shows galaxies moving away -- evidence the universe is expanding.

[[figure:cosmic_scale|From atoms to galaxies, the same physical laws scale across the universe.]]

[[check:Galaxies show a redshift that grows with distance. What does this provide evidence for?|the universe is expanding;;an expanding universe;;expansion of the universe|Redshift increasing with distance indicates the universe is expanding.]]
            """,
        ),
        (
            "3. Strategy for Elite Items",
            r"""
- **Set up every calculation fully.** Formula, values, units, answer -- in that order.
- **Watch nonlinear relationships.** Energy with the square of speed; intensity with the inverse square of distance.
- **Combine probabilities.** Multiply independent probabilities; use ratios for offspring outcomes.
- **Attack the conclusion.** Look for confounding variables, missing controls, and overreach beyond the data.
- **Estimate as a safeguard.** A rough check catches a wrong power of ten or a flipped ratio.

[[check:A study finds ice-cream sales and drownings both rise in summer. What third factor most likely explains both?|hot weather;;warm weather;;summer heat;;heat|Hot weather drives both swimming (drownings) and ice-cream sales -- a confounding variable.]]
            """,
        ),
    ],
    "mcqs": [
        # ============================ LIFE SCIENCE ===========================
        {
            "text": r"**Life Science.** In a dihybrid cross of two parents heterozygous for both traits (RrYy × RrYy), the classic ratio of phenotypes among the offspring is:",
            "difficulty": 3,
            "choices": [("9 : 3 : 3 : 1", True), ("3 : 1", False),
                        ("1 : 1 : 1 : 1", False), ("All identical", False)],
            "explanation": r"A dihybrid cross of two double-heterozygotes yields the 9:3:3:1 phenotype ratio. The trap '3:1' is a monohybrid cross. Pro tip: 9:3:3:1 is the signature of a dihybrid cross.",
        },
        {
            "text": r"**Life Science.** Two parents are both carriers (Bb) of a recessive disorder. What is the probability that a given child will be AFFECTED (bb)?",
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{1}{2}\)", False),
                        (r"\(\frac{3}{4}\)", False), (r"0", False)],
            "explanation": r"Bb x Bb gives BB, Bb, Bb, bb, so 1 in 4 children is affected (bb). The trap 1/2 is the carrier-only share among unaffected children. Pro tip: only the double-recessive (bb) shows a recessive disorder -- a 1/4 chance.",
        },
        {
            "text": r"**Life Science.** A food chain's producers capture 50,000 units of energy. Following the 10% rule, the third trophic level (the carnivores that eat the herbivores) receives about:",
            "difficulty": 3,
            "choices": [("500 units", True), ("5,000 units", False),
                        ("50,000 units", False), ("50 units", False)],
            "explanation": r"50,000 -> 5,000 (herbivores) -> 500 (carnivores). The trap 5,000 stops one level too soon. Pro tip: multiply by 0.1 for each step up; two steps means 0.01 of the original.",
        },
        {
            "text": r"**Life Science.** Moving sodium ions OUT of a cell against their concentration gradient requires the cell to use energy (ATP). This is called:",
            "difficulty": 3,
            "choices": [("Active transport", True), ("Passive diffusion", False),
                        ("Osmosis", False), ("Combustion", False)],
            "explanation": r"Pumping a substance against its gradient requires energy -- active transport. The trap, passive diffusion, moves substances WITH the gradient and needs no energy. Pro tip: 'against the gradient' = uphill = active transport needs ATP.",
        },
        {
            "text": r"**Life Science.** The wing of a bird and the wing of an insect perform the same function but evolved independently and share no common winged ancestor. Such ANALOGOUS structures are evidence of:",
            "difficulty": 3,
            "choices": [("Convergent evolution", True),
                        ("Common ancestry", False),
                        ("Identical DNA", False),
                        ("A single species", False)],
            "explanation": r"Independent evolution toward a similar solution is convergent evolution; the structures are analogous, not homologous. The trap 'common ancestry' would describe homologous structures. Pro tip: analogous = same function, different origin (convergent evolution).",
        },
        {
            "text": ("**Life Science.** An enzyme's activity was measured at several pH values, peaking at pH 7 and "
                     "dropping off sharply on both sides. The best conclusion is that the enzyme:"),
            "difficulty": 3,
            "choices": [("Has an optimal pH around 7, where it works best", True),
                        ("Works equally well at every pH", False),
                        ("Stops all reactions permanently", False),
                        ("Is not affected by pH", False)],
            "explanation": r"A peak at pH 7 with falloff on each side shows an optimal pH. The trap 'works equally well at every pH' contradicts the data. Pro tip: enzymes have a best (optimal) pH and temperature; conditions away from it slow them.",
        },
        {
            "text": r"**Life Science.** A small founding population that becomes isolated from a larger one often has LESS genetic diversity. This reduction is an example of:",
            "difficulty": 3,
            "choices": [("A genetic bottleneck / founder effect", True),
                        ("Photosynthesis", False),
                        ("Active transport", False),
                        ("Homeostasis", False)],
            "explanation": r"A few founders carry only a slice of the original gene pool, reducing diversity -- the founder effect. The trap, photosynthesis, is unrelated. Pro tip: small isolated populations lose variation through bottleneck and founder effects.",
        },
        {
            "text": r"**Life Science.** Removing a top predator (like wolves) can cause prey (like deer) to overgraze and crash the plant community. This chain of effects is called a:",
            "difficulty": 3,
            "choices": [("Trophic cascade", True), ("Chemical reaction", False),
                        ("Mutation", False), ("Half-life", False)],
            "explanation": r"A change at the top ripples down through the food web -- a trophic cascade. The trap, mutation, is a DNA change. Pro tip: removing a keystone predator can transform an entire ecosystem from the top down.",
        },
        {
            "text": ("**Life Science.** A study reports that towns with more bookstores have higher average test scores, "
                     "and concludes that bookstores raise scores. The biggest weakness is that:"),
            "difficulty": 3,
            "choices": [("A third factor, such as community wealth, may explain both", True),
                        ("Test scores cannot be measured", False),
                        ("Bookstores never sell books", False),
                        ("Correlation always proves causation", False)],
            "explanation": r"Wealthier areas may have both more bookstores and higher scores, so the link may be coincidental. The trap 'correlation always proves causation' is exactly the error. Pro tip: a confounding variable can create a correlation without any direct cause.",
        },
        {
            "text": r"**Life Science.** In the balanced equation for photosynthesis, 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂, the total number of carbon atoms is the same on both sides because:",
            "difficulty": 3,
            "choices": [("Atoms are conserved -- 6 carbons on each side", True),
                        ("Carbon is created during the reaction", False),
                        ("Carbon disappears into energy", False),
                        ("The equation is not balanced", False)],
            "explanation": r"6CO₂ has 6 carbons and C₆H₁₂O₆ also has 6 -- atoms are rearranged, not created or destroyed. The trap 'carbon is created' violates conservation. Pro tip: a balanced equation conserves every type of atom.",
        },
        {
            "text": r"**Life Science.** Genes can be switched 'on' or 'off' so that a liver cell and a skin cell, which share the SAME DNA, look and function differently. This control of which genes are used is called:",
            "difficulty": 3,
            "choices": [("Gene expression / regulation", True),
                        ("Mitosis", False),
                        ("Fermentation", False),
                        ("Osmosis", False)],
            "explanation": r"Different cell types express different subsets of the same genome -- gene regulation. The trap, mitosis, is cell division. Pro tip: every cell has the full DNA, but each expresses only the genes it needs.",
        },
        {
            "text": r"**Life Science.** If a recessive trait appears in about 1 of every 100 individuals, the recessive allele is relatively:",
            "difficulty": 3,
            "choices": [("Uncommon, but carried unseen by some heterozygotes", True),
                        ("Impossible to inherit", False),
                        ("More common than the dominant allele", False),
                        ("Found only in one family ever", False)],
            "explanation": r"A rare recessive phenotype means the allele is uncommon, yet carriers (heterozygotes) hold it without showing it. The trap 'impossible to inherit' contradicts that it appears at all. Pro tip: recessive alleles can hide in carriers for generations.",
        },
        {
            "text": r"**Life Science.** Which provides the STRONGEST evidence that a newly found fossil organism is a transitional form between fish and amphibians?",
            "difficulty": 3,
            "choices": [("It has features of both groups, in rock of the expected age", True),
                        ("It is the same color as a modern fish", False),
                        ("It was found near a lake today", False),
                        ("It is larger than a modern frog", False)],
            "explanation": r"A mix of fish and amphibian traits, dated to the right time, is powerful transitional evidence. The traps (color, location, size) don't establish lineage. Pro tip: transitional fossils combine traits of older and newer groups at the predicted time.",
        },
        # ========================== PHYSICAL SCIENCE =========================
        {
            "text": r"**Physical Science.** A 1,000 kg car traveling at 10 m/s speeds up to 20 m/s. Because kinetic energy depends on the SQUARE of speed, its kinetic energy becomes:",
            "difficulty": 3,
            "choices": [("Four times as large", True), ("Twice as large", False),
                        ("Half as large", False), ("Unchanged", False)],
            "explanation": r"KE = ½mv²; doubling v multiplies KE by 2² = 4. The trap 'twice' forgets the square. Pro tip: kinetic energy grows with the square of speed, so small speed increases add a lot of energy.",
        },
        {
            "text": r"**Physical Science.** A machine does 100 joules of work in 5 seconds. Its power output is:",
            "difficulty": 3,
            "choices": [("20 watts", True), ("500 watts", False),
                        ("95 watts", False), ("105 watts", False)],
            "explanation": r"Power = work / time = 100 / 5 = 20 watts. The trap 500 multiplies instead of dividing. Pro tip: power is how fast work is done -- joules per second equals watts.",
        },
        {
            "text": r"**Physical Science.** A circuit has a 12-volt battery and a resistance of 4 ohms. Using V = IR, the current is:",
            "difficulty": 3,
            "choices": [("3 amperes", True), ("48 amperes", False),
                        ("16 amperes", False), ("0.33 amperes", False)],
            "explanation": r"I = V / R = 12 / 4 = 3 amperes. The trap 48 multiplies instead of dividing. Pro tip: rearrange V = IR to I = V/R when solving for current.",
        },
        {
            "text": r"**Physical Science.** Two forces act on a box: 10 N to the right and 4 N to the left. The net force is:",
            "difficulty": 3,
            "choices": [("6 N to the right", True), ("14 N to the right", False),
                        ("6 N to the left", False), ("0 N", False)],
            "explanation": r"Opposing forces subtract: 10 - 4 = 6 N in the direction of the larger force (right). The trap 14 N adds them. Pro tip: forces in opposite directions subtract; the net force points the way of the bigger one.",
        },
        {
            "text": r"**Physical Science.** In an isolated collision between two carts, the total momentum after the collision compared with before is:",
            "difficulty": 3,
            "choices": [("The same -- momentum is conserved", True),
                        ("Always greater", False),
                        ("Always zero", False),
                        ("Always doubled", False)],
            "explanation": r"With no outside forces, total momentum is conserved in a collision. The trap 'always greater' would create momentum from nothing. Pro tip: momentum lost by one object is gained by the other; the total stays constant.",
        },
        {
            "text": r"**Physical Science.** In a PARALLEL circuit with two bulbs, if one bulb is unscrewed and removed, the other bulb will:",
            "difficulty": 3,
            "choices": [("Stay lit, because it has its own path to the battery", True),
                        ("Also go out, because the circuit is broken", False),
                        ("Explode immediately", False),
                        ("Become a series circuit", False)],
            "explanation": r"Parallel branches are independent, so removing one bulb leaves the other's path intact. The trap 'also go out' describes a series circuit. Pro tip: parallel = separate paths, so each device works on its own.",
        },
        {
            "text": r"**Physical Science.** A radioactive sample starts with 800 grams. Its half-life is 5 years. After 15 years, the amount remaining is:",
            "difficulty": 3,
            "choices": [("100 grams", True), ("400 grams", False),
                        ("200 grams", False), ("0 grams", False)],
            "explanation": r"15 years is 3 half-lives: 800 -> 400 -> 200 -> 100 grams. The trap 400 counts only one half-life. Pro tip: count the half-lives first, then halve that many times.",
        },
        {
            "text": r"**Physical Science.** Increasing the pressure on a reaction at equilibrium between gases generally shifts the reaction toward the side with:",
            "difficulty": 3,
            "choices": [("Fewer gas molecules", True),
                        ("More gas molecules", False),
                        ("No molecules at all", False),
                        ("A different element", False)],
            "explanation": r"By Le Chatelier's principle, higher pressure favors the side with fewer gas molecules, easing the pressure. The trap 'more gas molecules' would increase pressure further. Pro tip: a system at equilibrium shifts to oppose the change forced on it.",
        },
        {
            "text": r"**Physical Science.** Across the electromagnetic spectrum, as wavelength gets SHORTER, the energy of the wave:",
            "difficulty": 3,
            "choices": [("Increases", True), ("Decreases", False),
                        ("Stays the same", False), ("Drops to zero", False)],
            "explanation": r"Shorter wavelength means higher frequency and more energy. The trap 'decreases' reverses the inverse relationship. Pro tip: wavelength and energy are inverses -- short waves (like gamma) carry the most energy.",
        },
        {
            "text": r"**Physical Science.** A 100 mL salt solution is diluted with water to 200 mL. The concentration of salt in the solution:",
            "difficulty": 3,
            "choices": [("Decreases, because the same salt is in more water", True),
                        ("Increases", False),
                        ("Stays exactly the same", False),
                        ("Becomes a pure element", False)],
            "explanation": r"The amount of salt is unchanged but spread through more water, so concentration falls. The trap 'increases' is backwards. Pro tip: adding solvent dilutes -- same solute, larger volume, lower concentration.",
        },
        {
            "text": r"**Physical Science.** A block of unknown metal has a mass of 90 g and a volume of 10 cm³. Lead has a density near 11 g/cm³ and aluminum near 2.7 g/cm³. This block's density (9 g/cm³) suggests it is:",
            "difficulty": 3,
            "choices": [("Neither pure lead nor pure aluminum", True),
                        ("Definitely pure aluminum", False),
                        ("Definitely pure lead", False),
                        ("Not a metal at all", False)],
            "explanation": r"Density = 90/10 = 9 g/cm³, which matches neither lead (11) nor aluminum (2.7). The trap 'pure aluminum' is far off. Pro tip: density is a fingerprint -- compute it, then compare to known values.",
        },
        {
            "text": r"**Physical Science.** When water freezes into ice, it expands and becomes LESS dense, which is why ice:",
            "difficulty": 3,
            "choices": [("Floats on liquid water", True),
                        ("Sinks to the bottom", False),
                        ("Dissolves instantly", False),
                        ("Conducts electricity", False)],
            "explanation": r"Ice is less dense than liquid water, so it floats -- unusual among substances. The trap 'sinks' would happen if ice were denser. Pro tip: water's expansion on freezing lets lakes freeze top-down, protecting life below.",
        },
        {
            "text": r"**Physical Science.** A ball is dropped and bounces back to a lower height each time. The 'lost' mechanical energy is mainly:",
            "difficulty": 3,
            "choices": [("Transformed into heat and sound", True),
                        ("Destroyed completely", False),
                        ("Turned into new matter", False),
                        ("Stored as nuclear energy", False)],
            "explanation": r"Energy isn't lost but converted to heat and sound at each bounce, so the ball rises less. The trap 'destroyed completely' violates conservation of energy. Pro tip: 'lost' energy has just changed into a less useful form, like heat.",
        },
        # ======================= EARTH & SPACE SCIENCE =======================
        {
            "text": r"**Earth & Space.** A rock contains equal amounts of a radioactive parent isotope and its decay product. If the half-life is 700 million years, the rock is about:",
            "difficulty": 3,
            "choices": [("700 million years old", True),
                        ("350 million years old", False),
                        ("1.4 billion years old", False),
                        ("70 million years old", False)],
            "explanation": r"A 50/50 parent-to-daughter ratio means exactly one half-life has passed: 700 million years. The trap 1.4 billion is two half-lives (25% parent). Pro tip: half the parent remaining = one half-life of age.",
        },
        {
            "text": r"**Earth & Space.** A tectonic plate moves 100 km over 2 million years. Its average speed is about:",
            "difficulty": 3,
            "choices": [("5 cm per year", True), ("50 cm per year", False),
                        ("2 cm per year", False), ("200 cm per year", False)],
            "explanation": r"100 km = 10,000,000 cm; divided by 2,000,000 years = 5 cm/year. The trap 50 misplaces a decimal. Pro tip: convert to the same units first, then divide distance by time.",
        },
        {
            "text": r"**Earth & Space.** Light from distant galaxies is shifted toward the red (longer-wavelength) end of the spectrum, and the shift grows with distance. This is evidence that:",
            "difficulty": 3,
            "choices": [("The universe is expanding", True),
                        ("The galaxies are cooling down", False),
                        ("Earth is the center of the universe", False),
                        ("Light has stopped moving", False)],
            "explanation": r"Redshift increasing with distance shows galaxies receding -- the universe is expanding (Hubble's observation). The trap 'Earth is the center' is the discarded view. Pro tip: more distant galaxies recede faster, which is the signature of expansion.",
        },
        {
            "text": r"**Earth & Space.** A blue-white star is generally MUCH hotter than a red star because a star's color depends on its:",
            "difficulty": 3,
            "choices": [("Surface temperature", True), ("Distance from Earth", False),
                        ("Age in Earth years", False), ("Chemical name", False)],
            "explanation": r"Hotter stars glow blue-white; cooler stars glow red. The trap, distance, doesn't determine color. Pro tip: like a flame, blue is hotter than red -- star color reveals temperature.",
        },
        {
            "text": r"**Earth & Space.** The highest 'spring' tides occur when the Sun, Earth, and Moon are aligned (at full and new moon) because:",
            "difficulty": 3,
            "choices": [("The Sun's and Moon's gravitational pulls combine", True),
                        ("The Moon stops orbiting Earth", False),
                        ("The oceans freeze briefly", False),
                        ("Earth moves closer to the Sun", False)],
            "explanation": r"When aligned, the Sun and Moon pull together, producing the largest tidal range (spring tides). The trap 'Moon stops orbiting' is false. Pro tip: aligned pulls add (spring tides); right-angle pulls partly cancel (neap tides).",
        },
        {
            "text": r"**Earth & Space.** A buried rock layer is tilted and topped by flat horizontal layers, with an eroded surface between them. This gap in the rock record is called:",
            "difficulty": 3,
            "choices": [("An unconformity", True), ("A half-life", False),
                        ("A solstice", False), ("A convection current", False)],
            "explanation": r"An eroded surface separating older tilted rock from younger flat rock is an unconformity -- a gap in the record. The trap, half-life, is a decay concept. Pro tip: an unconformity marks missing time, where rock was eroded or never deposited.",
        },
        {
            "text": r"**Earth & Space.** Rising global temperatures can increase evaporation, putting more water vapor (a greenhouse gas) into the air, which traps still more heat. This best illustrates:",
            "difficulty": 3,
            "choices": [("A positive (amplifying) feedback loop", True),
                        ("A negative (stabilizing) feedback loop", False),
                        ("Conservation of mass", False),
                        ("Radioactive decay", False)],
            "explanation": r"Warming -> more water vapor -> more warming is a self-reinforcing positive feedback. The trap, negative feedback, would dampen the change. Pro tip: positive feedback amplifies an initial change; it does not stabilize.",
        },
        {
            "text": r"**Earth & Space.** Earth's global wind belts (like the trade winds) curve rather than blowing straight because of:",
            "difficulty": 3,
            "choices": [("The Coriolis effect from Earth's rotation", True),
                        ("The pull of the Moon's gravity", False),
                        ("Ocean tides only", False),
                        ("Volcanic eruptions", False)],
            "explanation": r"Earth's rotation deflects moving air, curving the winds -- the Coriolis effect. The trap, the Moon's gravity, drives tides, not wind curvature. Pro tip: the spinning Earth bends large-scale winds and currents.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the elite (Level 5) full-length GED Science practice exam (34 questions; MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()
        course = Course.objects.create(
            title=COURSE["title"], slug=COURSE["slug"], program=COURSE["program"],
            subject=COURSE["subject"], description=COURSE["description"],
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
        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- {course.lessons.count()} lessons, "
            f"{course.questions.count()} questions (elite level)."
        ))
