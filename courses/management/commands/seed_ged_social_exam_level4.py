"""
Seed a FOURTH full-length 'GED Social Studies' practice exam -- Level 4, the
mastery tier. Same test-day structure (35 questions; 70 minutes; scored 100-200,
145 to pass), but EVERY item is a hard, multi-layered problem: implied powers and
incorporation, the constitutional compromises, externalities and the business
cycle, document evaluation, and historical interpretation.

Run:
    python manage.py seed_ged_social_exam_level4
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Full-Length Practice Exam (Level 4 - Mastery)",
    "slug": "ged-social-exam-level4",
    "program": "GED",
    "subject": "social",
    "description": (
        "The fourth and second-hardest full-length GED Social Studies practice exam, for students aiming "
        "at a top score after clearing Levels 1-3. Same test-day format -- 35 questions weighted toward "
        "Civics, with History, Economics, and Geography, 70 minutes, scored 100-200 (145 to pass) -- but "
        "every item is a hard, multi-layered problem: implied powers and incorporation, the "
        "constitutional compromises, externalities and the business cycle, document evaluation, and "
        "historical interpretation. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 4: The Mastery Social Studies Test",
            r"""
This is the **mastery** GED Social Studies practice exam -- harder than Levels 1-3. The format is unchanged:

- **35 questions** in **70 minutes**, weighted toward **Civics**, with **History**, **Economics**, and **Geography**; scored **100-200**, **145 to pass**.

**What makes Level 4 the hardest yet:** **every** question is a hard, layered item. You will apply **implied powers** and **incorporation**, weigh the **constitutional compromises**, analyze **externalities** and the **business cycle**, and **evaluate documents** for bias and reliability.

[[check:Powers the federal government has because they are 'necessary and proper' to carry out its listed powers are called what?|implied powers;;implied|Implied powers come from the Necessary and Proper Clause.]]
            """,
        ),
        (
            "2. Applying Principles and Weighing Evidence",
            r"""
Mastery Social Studies is about applying ideas and judging sources.

- **Implied powers.** The Necessary and Proper Clause lets Congress act beyond its strictly listed powers.
- **Incorporation.** The 14th Amendment extends most Bill of Rights protections to the states.
- **Compromise.** The Constitution was built on bargains, like the Great Compromise balancing big and small states.
- **Externalities.** Some costs or benefits (like pollution) fall on third parties, a kind of market failure.
- **Evaluate documents.** Weigh a source's author, purpose, date, and reliability before trusting its claims.

[[figure:three_branches|Each branch's powers -- enumerated and implied -- are balanced against the others.]]

[[check:When a factory's pollution harms nearby residents who are not part of the sale, economists call that cost a(n) what?|externality;;negative externality|A cost imposed on third parties is a (negative) externality.]]
            """,
        ),
        (
            "3. Strategy for Mastery Items",
            r"""
- **Apply the principle to the scenario.** Decide which idea (implied powers, incorporation, externality) a situation shows.
- **Judge the source.** Ask who wrote a document, when, for whom, and with what bias before accepting it.
- **Distinguish cause, effect, and consequence.** Separate what triggered an event from its long-term results.
- **Read data for the relationship.** Compare trends across a chart or table, not just single values.
- **Never leave a blank.** Eliminate what you can, then choose.

[[check:Two sources describe the same event very differently. What should you consider to judge which is more reliable?|the author and purpose;;bias;;who wrote it and why;;the point of view|Weigh each author's perspective, purpose, and possible bias.]]
            """,
        ),
    ],
    "mcqs": [
        # ====================== CIVICS & GOVERNMENT ==========================
        {
            "text": ("**Civics.** Congress creates a national bank, arguing it is 'necessary and proper' for "
                     "managing the country's money even though the Constitution never lists a bank. This "
                     "relies on Congress's:"),
            "difficulty": 3,
            "choices": [("Implied powers", True), ("Reserved powers", False),
                        ("Veto power", False), ("Judicial power", False)],
            "explanation": r"The Necessary and Proper Clause gives Congress implied powers beyond those listed. The trap, reserved powers, belong to the states. Pro tip: implied powers (upheld in McCulloch v. Maryland) flow from the 'necessary and proper' clause.",
        },
        {
            "text": ("**Civics.** Through 'incorporation,' most protections in the Bill of Rights now also "
                     "limit STATE governments. This was accomplished mainly through the:"),
            "difficulty": 3,
            "choices": [("14th Amendment", True), ("3rd Amendment", False),
                        ("Articles of Confederation", False), ("Preamble", False)],
            "explanation": r"The 14th Amendment's due-process clause has been used to apply most Bill of Rights protections to the states. The trap, the Articles, predate the Constitution. Pro tip: incorporation works through the 14th Amendment.",
        },
        {
            "text": ("**Civics.** At the Constitutional Convention, the 'Great Compromise' settled a dispute "
                     "between large and small states by creating:"),
            "difficulty": 3,
            "choices": [("A two-house Congress: one by population, one with equal state representation", True),
                        ("A single national king", False),
                        ("A Congress with no states represented", False),
                        ("Three Presidents at once", False)],
            "explanation": r"The Great Compromise gave the House seats by population and the Senate two seats per state. The trap, a king, is the opposite of the Founders' aim. Pro tip: the Great Compromise balanced big and small states in a bicameral Congress.",
        },
        {
            "text": ("**Civics.** Both the federal and state governments can collect taxes. Powers that BOTH "
                     "levels of government share are called:"),
            "difficulty": 3,
            "choices": [("Concurrent powers", True), ("Enumerated powers", False),
                        ("Veto powers", False), ("Reserved powers", False)],
            "explanation": r"Concurrent powers, like taxation, are exercised by both federal and state governments. The trap, reserved powers, belong only to the states. Pro tip: concurrent = shared by both levels (e.g., taxing, building roads).",
        },
        {
            "text": ("**Civics.** 'Civil liberties' protect individuals FROM government action (like free speech), "
                     "while 'civil rights' protect individuals from:"),
            "difficulty": 3,
            "choices": [("Discrimination, ensuring equal treatment", True),
                        ("Paying any taxes", False),
                        ("Voting in elections", False),
                        ("Reading the news", False)],
            "explanation": r"Civil rights guarantee equal treatment and protection against discrimination. The trap 'paying any taxes' is unrelated. Pro tip: liberties limit government; rights guarantee equality.",
        },
        {
            "text": ("**Civics.** A President nominates a Supreme Court justice, but the nominee cannot take the "
                     "seat unless approved by the Senate. This requirement is a check that gives the Senate "
                     "the power of:"),
            "difficulty": 3,
            "choices": [("Confirmation (advice and consent)", True),
                        ("Judicial review", False),
                        ("The pocket veto", False),
                        ("Impeachment of itself", False)],
            "explanation": r"The Senate must confirm judicial and many executive appointments -- 'advice and consent.' The trap, judicial review, is a court power. Pro tip: Senate confirmation checks the President's appointment power.",
        },
        {
            "text": ("**Civics.** A judge who believes the Constitution should be interpreted strictly, based "
                     "closely on its original text, takes a view often described as:"),
            "difficulty": 3,
            "choices": [("Strict (narrow) constructionism", True),
                        ("Loose construction of unlimited powers", False),
                        ("Rejecting the Constitution entirely", False),
                        ("Monarchy", False)],
            "explanation": r"Strict constructionists read the Constitution narrowly and closely to its text. The trap, rejecting the Constitution, is not interpretation at all. Pro tip: strict construction reads the text narrowly; loose construction reads it broadly.",
        },
        {
            "text": ("**Civics.** A law funds chaplains of one specific religion in public schools. A court would "
                     "most likely find this violates the First Amendment's protection against:"),
            "difficulty": 3,
            "choices": [("Government establishment of religion", True),
                        ("Freedom of the press", False),
                        ("The right to bear arms", False),
                        ("Interstate commerce", False)],
            "explanation": r"The Establishment Clause bars government from favoring or establishing a religion. The trap, freedom of the press, is a different protection. Pro tip: the First Amendment both bars establishing religion and protects its free exercise.",
        },
        {
            "text": ("**Civics.** Some critics argue the Electoral College can let a candidate win the presidency "
                     "without winning the most individual votes nationwide. This is a criticism of how the "
                     "Electoral College can produce:"),
            "difficulty": 3,
            "choices": [("A winner who lost the national popular vote", True),
                        ("A tie in every single election", False),
                        ("A President chosen by the Supreme Court", False),
                        ("No President at all, ever", False)],
            "explanation": r"Because it counts state-by-state electors, the Electoral College can elect someone who lost the popular vote. The trap 'a tie in every election' is not the criticism. Pro tip: the gap between electoral and popular votes drives debate over the system.",
        },
        {
            "text": ("**Civics.** The amendment process is deliberately difficult (two-thirds of Congress, "
                     "three-fourths of states) mainly to:"),
            "difficulty": 3,
            "choices": [("Ensure broad, lasting agreement before the Constitution changes", True),
                        ("Make sure no amendment is ever added", False),
                        ("Let the President change it alone", False),
                        ("Speed up frequent changes", False)],
            "explanation": r"The high bar ensures only changes with wide, durable support are added. The trap 'no amendment ever' is false -- 27 have passed. Pro tip: the difficulty protects the Constitution from hasty, narrow changes.",
        },
        {
            "text": ("**Civics.** A country where leaders can jail critics without a trial, ignoring its own "
                     "written laws, most clearly lacks:"),
            "difficulty": 3,
            "choices": [("The rule of law", True), ("Natural resources", False),
                        ("A national flag", False), ("Any geography", False)],
            "explanation": r"Ignoring the law to punish critics violates the rule of law. The trap, natural resources, is unrelated to legal fairness. Pro tip: the rule of law means even leaders must follow the law.",
        },
        {
            "text": ("**Civics.** 'Due process' concerns FAIR PROCEDURES, while 'equal protection' concerns "
                     "TREATING people EQUALLY. A law that gives unfair trials violates due process; a law "
                     "that treats one group worse than another violates:"),
            "difficulty": 3,
            "choices": [("Equal protection", True), ("Free trade", False),
                        ("The Necessary and Proper Clause", False), ("A tariff", False)],
            "explanation": r"Treating groups unequally under the law violates equal protection. The trap, free trade, is economic. Pro tip: due process = fair procedures; equal protection = no unfair discrimination.",
        },
        {
            "text": ("**Civics.** To decide whether a 1790s pamphlet gives a reliable account of an event, a "
                     "historian should FIRST consider:"),
            "difficulty": 3,
            "choices": [("Who wrote it, when, and for what purpose", True),
                        ("How many pages it has", False),
                        ("The color of the ink", False),
                        ("Whether it is heavy", False)],
            "explanation": r"Sourcing -- author, date, and purpose -- reveals possible bias and reliability. The traps (length, ink, weight) say nothing about reliability. Pro tip: always source a document before trusting its claims.",
        },
        {
            "text": ("**Civics.** A government that may only do what its constitution specifically permits, and no "
                     "more, is an example of:"),
            "difficulty": 3,
            "choices": [("Limited government", True), ("Unlimited monarchy", False),
                        ("A command economy", False), ("Direct democracy", False)],
            "explanation": r"Limited government is bound by its constitution and cannot exceed its granted powers. The trap, unlimited monarchy, is the opposite. Pro tip: limited government is a core principle protecting individual liberty.",
        },
        {
            "text": ("**Civics.** Politicians often watch public opinion polls closely before taking a position. "
                     "This shows that, in a democracy, public opinion can:"),
            "difficulty": 3,
            "choices": [("Influence the decisions of elected officials", True),
                        ("Replace the Constitution", False),
                        ("Set the speed of light", False),
                        ("Command the army directly", False)],
            "explanation": r"Because officials must face voters, public opinion shapes their choices. The trap 'replace the Constitution' overstates its power. Pro tip: in a democracy, leaders are responsive to the public that elects them.",
        },
        {
            "text": ("**Civics.** A state and the federal government both claim authority over the same issue, and "
                     "the dispute is taken to court. The branch that will ultimately interpret the "
                     "Constitution to resolve it is the:"),
            "difficulty": 3,
            "choices": [("Judicial branch", True), ("Legislative branch", False),
                        ("Executive branch", False), ("Military", False)],
            "explanation": r"Courts interpret the Constitution and settle such disputes. The trap, the legislative branch, makes laws rather than interpreting them. Pro tip: when the meaning of the Constitution is in question, the judiciary decides.",
        },
        {
            "text": ("**Civics.** In a parliamentary system, unlike the U.S. system, the chief executive (prime "
                     "minister) is usually:"),
            "difficulty": 3,
            "choices": [("Chosen by the legislature, not separately elected", True),
                        ("A hereditary king with absolute power", False),
                        ("Appointed by a foreign nation", False),
                        ("Selected by the Supreme Court", False)],
            "explanation": r"In parliamentary systems, the legislature selects the prime minister, blending the branches. The trap, a hereditary king, is a different system. Pro tip: the U.S. separates the executive and legislature; parliamentary systems fuse them.",
        },
        {
            "text": ("**Civics.** A citizen sues, claiming a new law violates her constitutional rights, and asks "
                     "a court to strike it down. She is relying on the courts' power of:"),
            "difficulty": 3,
            "choices": [("Judicial review", True), ("Taxation", False),
                        ("Coining money", False), ("Declaring war", False)],
            "explanation": r"Asking a court to invalidate a law invokes judicial review. The traps (taxation, coining money, declaring war) are powers of Congress. Pro tip: judicial review is how individuals challenge unconstitutional laws.",
        },
        # =========================== U.S. HISTORY ============================
        {
            "text": ("**U.S. History.** The 16th and 17th Amendments, passed during the Progressive Era, "
                     "respectively created the federal income tax and provided for the:"),
            "difficulty": 3,
            "choices": [("Direct election of U.S. senators by voters", True),
                        ("Abolition of Congress", False),
                        ("Return of British rule", False),
                        ("End of all taxes", False)],
            "explanation": r"The 17th Amendment let voters directly elect senators (previously chosen by state legislatures). The trap 'end of all taxes' contradicts the 16th Amendment's income tax. Pro tip: 16th = income tax; 17th = direct election of senators.",
        },
        {
            "text": ("**U.S. History.** Historians often note that the Civil War's deepest cause was slavery, "
                     "though Southern leaders also framed it as a matter of 'states' rights.' This shows "
                     "that a single event can be:"),
            "difficulty": 3,
            "choices": [("Explained through more than one perspective", True),
                        ("Caused by nothing at all", False),
                        ("Completely unrelated to slavery", False),
                        ("Impossible for historians to study", False)],
            "explanation": r"Major events have layered causes and competing interpretations -- here, slavery and states' rights. The trap 'unrelated to slavery' ignores the central cause. Pro tip: history often involves weighing multiple perspectives on the same event.",
        },
        {
            "text": ("**U.S. History.** The failure of Reconstruction to secure lasting equality contributed "
                     "directly to:"),
            "difficulty": 3,
            "choices": [("Decades of segregation that the Civil Rights Movement later fought", True),
                        ("The American Revolution", False),
                        ("The invention of the printing press", False),
                        ("The end of all U.S. history", False)],
            "explanation": r"When Reconstruction collapsed, segregation took hold, setting the stage for the Civil Rights Movement. The trap, the American Revolution, came earlier. Pro tip: cause and effect chain -- Reconstruction's failure led toward later civil rights struggles.",
        },
        {
            "text": ("**U.S. History.** During World War II, the American 'home front' saw women enter factory "
                     "jobs in large numbers, which:"),
            "difficulty": 3,
            "choices": [("Expanded women's role in the workforce", True),
                        ("Ended all manufacturing", False),
                        ("Started the Revolutionary War", False),
                        ("Removed women from public life", False)],
            "explanation": r"Wartime labor needs drew many women into factories, broadening their economic roles. The trap 'removed women from public life' is the opposite. Pro tip: WWII reshaped the workforce, with lasting social effects.",
        },
        {
            "text": ("**U.S. History.** The 1962 Cuban Missile Crisis, a tense standoff over Soviet missiles near "
                     "the U.S., is best understood as part of the:"),
            "difficulty": 3,
            "choices": [("Cold War rivalry between the U.S. and the Soviet Union", True),
                        ("American Revolution", False),
                        ("Civil War", False),
                        ("Industrial Revolution", False)],
            "explanation": r"The Cuban Missile Crisis was a dangerous flashpoint of the Cold War. The trap, the Civil War, is the wrong century. Pro tip: place an event in its era -- the Cold War ran roughly from the late 1940s to 1991.",
        },
        {
            "text": ("**U.S. History.** Two newspaper accounts of the same protest describe it very differently -- "
                     "one as 'a riot,' the other as 'a peaceful march.' A careful reader should:"),
            "difficulty": 3,
            "choices": [("Consider each source's bias and seek more evidence", True),
                        ("Assume the first one read is always correct", False),
                        ("Believe whichever is longer", False),
                        ("Ignore both sources completely", False)],
            "explanation": r"Conflicting accounts call for weighing bias and gathering more evidence. The trap 'the first one is always correct' ignores point of view. Pro tip: corroborate across sources and account for each author's perspective.",
        },
        {
            "text": ("**U.S. History.** The Declaration of Independence lists grievances against the king "
                     "BEFORE declaring independence. This structure was meant to:"),
            "difficulty": 3,
            "choices": [("Justify the break by showing it was a reasoned response to abuses", True),
                        ("Praise the king's good rule", False),
                        ("Establish a new monarchy", False),
                        ("Set tax rates for the colonies", False)],
            "explanation": r"Listing abuses first builds the case that independence was justified, not rash. The trap 'praise the king' is the opposite. Pro tip: the Declaration argues its case with evidence before stating its conclusion.",
        },
        # ============================ ECONOMICS ==============================
        {
            "text": ("**Economics.** A factory pollutes a river, harming downstream residents who had no part in "
                     "the factory's business. Economists call this spillover cost a:"),
            "difficulty": 3,
            "choices": [("Negative externality", True), ("Tariff", False),
                        ("Subsidy", False), ("Surplus", False)],
            "explanation": r"A cost imposed on uninvolved third parties is a negative externality, a kind of market failure. The trap, a tariff, is an import tax. Pro tip: externalities are costs (or benefits) that fall on people outside the transaction.",
        },
        {
            "text": ("**Economics.** An economy moves through expansion, a peak, a recession, and a recovery, then "
                     "repeats. This repeating pattern is called the:"),
            "difficulty": 3,
            "choices": [("Business cycle", True), ("Electoral College", False),
                        ("Water cycle", False), ("Rock cycle", False)],
            "explanation": r"The business cycle is the recurring rise and fall of economic activity. The trap, the water cycle, is an Earth-science process. Pro tip: expansion -> peak -> recession -> trough -> recovery is the business cycle.",
        },
        {
            "text": ("**Economics.** When the demand for a product rises sharply while its supply stays the same, "
                     "the equilibrium price will most likely:"),
            "difficulty": 3,
            "choices": [("Increase", True), ("Decrease", False),
                        ("Fall to zero", False), ("Stay exactly the same", False)],
            "explanation": r"Higher demand against fixed supply pushes the price up. The trap 'decrease' would follow a rise in SUPPLY, not demand. Pro tip: more demand with the same supply raises the equilibrium price.",
        },
        {
            "text": ("**Economics.** Governments sometimes provide goods like national defense and public roads "
                     "because private markets tend to UNDER-supply them. Such goods are called:"),
            "difficulty": 3,
            "choices": [("Public goods", True), ("Luxury goods", False),
                        ("Imported goods", False), ("Illegal goods", False)],
            "explanation": r"Public goods (defense, roads) benefit everyone and are hard to sell individually, so government provides them. The trap, luxury goods, are sold normally in markets. Pro tip: public goods are shared and non-excludable, so markets under-provide them.",
        },
        {
            "text": ("**Economics.** A table shows unemployment falling from 9% to 4% over five years while GDP "
                     "rises each year. Together, these data most likely indicate an economy that is:"),
            "difficulty": 3,
            "choices": [("Growing and improving", True),
                        ("Entering a deep depression", False),
                        ("Completely unchanged", False),
                        ("Shrinking rapidly", False)],
            "explanation": r"Rising GDP with falling unemployment signals economic growth. The trap 'deep depression' contradicts both trends. Pro tip: read multiple indicators together -- here, both point to expansion.",
        },
        # ====================== GEOGRAPHY & THE WORLD ========================
        {
            "text": ("**Geography.** A country's population is shown with many young people at the bottom and few "
                     "elderly at the top of its age chart. This 'population pyramid' suggests the country has:"),
            "difficulty": 3,
            "choices": [("A young, rapidly growing population", True),
                        ("Mostly elderly residents", False),
                        ("No people under age 50", False),
                        ("An equal number at every age forever", False)],
            "explanation": r"A wide base of young people indicates high birth rates and rapid growth. The trap 'mostly elderly' describes the opposite shape. Pro tip: a wide-bottomed pyramid means a youthful, fast-growing population.",
        },
        {
            "text": ("**Geography.** Historically, many great cities grew along rivers and coastlines mainly "
                     "because these locations offered:"),
            "difficulty": 3,
            "choices": [("Water, food, and routes for trade and transport", True),
                        ("Protection from all weather", False),
                        ("Lower latitude only", False),
                        ("Freedom from any government", False)],
            "explanation": r"Rivers and coasts provided water, food, and transport, encouraging settlement and trade. The trap 'protection from all weather' is false -- coasts face storms. Pro tip: geography shapes where people settle; water access is a powerful draw.",
        },
        {
            "text": ("**Geography.** A government must decide whether to allow mining that brings jobs but damages "
                     "a forest. This decision involves a:"),
            "difficulty": 3,
            "choices": [("Trade-off between economic gain and environmental cost", True),
                        ("Change to the law of gravity", False),
                        ("Constitutional amendment", False),
                        ("New line of longitude", False)],
            "explanation": r"Weighing jobs against environmental harm is a classic trade-off. The trap 'change to gravity' is nonsensical. Pro tip: many policy choices balance economic benefits against environmental costs.",
        },
        {
            "text": ("**Geography.** When food, music, language, or technology spreads from one culture to another, "
                     "geographers call this process:"),
            "difficulty": 3,
            "choices": [("Cultural diffusion", True), ("Photosynthesis", False),
                        ("Judicial review", False), ("Erosion", False)],
            "explanation": r"Cultural diffusion is the spread of ideas and practices between cultures. The trap, photosynthesis, is a biological process. Pro tip: trade, migration, and media all drive cultural diffusion.",
        },
        {
            "text": ("**Geography.** A landlocked country with no seacoast may face higher costs to trade overseas "
                     "because it must:"),
            "difficulty": 3,
            "choices": [("Move goods through neighboring countries to reach a port", True),
                        ("Stop trading with everyone", False),
                        ("Change its time zone", False),
                        ("Rewrite its constitution", False)],
            "explanation": r"Without a coast, a country depends on neighbors' routes and ports, raising trade costs. The trap 'stop trading with everyone' overstates the problem. Pro tip: geography (like being landlocked) shapes a nation's trade and economy.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the mastery (Level 4) full-length GED Social Studies practice exam (35 questions; MCQ only)."

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
            f"{course.questions.count()} questions (all hard)."
        ))
