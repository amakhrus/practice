"""
Seed a FIFTH and FINAL full-length 'GED Social Studies' practice exam -- Level 5,
the elite tier, the hardest of the set. Same test-day structure (35 questions; 70
minutes; scored 100-200, 145 to pass). Every item is a hard, multi-layered
problem at the ceiling of the GED's range: social-contract theory and the
Federalist reasoning, comparing and evaluating primary sources, judicial
activism vs. restraint, comparative advantage and policy trade-offs, and the
tragedy of the commons.

Run:
    python manage.py seed_ged_social_exam_level5
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Full-Length Practice Exam (Level 5 - Elite)",
    "slug": "ged-social-exam-level5",
    "program": "GED",
    "subject": "social",
    "description": (
        "The fifth and hardest full-length GED Social Studies practice exam -- the elite tier, for "
        "students who have cleared Levels 1-4 and want the toughest possible rehearsal. Same test-day "
        "format -- 35 questions weighted toward Civics, with History, Economics, and Geography, 70 "
        "minutes, scored 100-200 (145 to pass) -- but every item sits at the ceiling of the range: "
        "social-contract theory and the Federalist reasoning, comparing and evaluating primary sources, "
        "judicial activism vs. restraint, comparative advantage and policy trade-offs, and the tragedy "
        "of the commons. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 5: The Elite Social Studies Test",
            r"""
This is the **elite** GED Social Studies practice exam -- the toughest of all five. The format never changes:

- **35 questions** in **70 minutes**, weighted toward **Civics**, with **History**, **Economics**, and **Geography**; scored **100-200**, **145 to pass**.

**What makes Level 5 the hardest of all:** there is not a single routine question. You will reason about **political philosophy** (the social contract), **compare and evaluate primary sources**, weigh **judicial activism vs. restraint**, analyze **comparative advantage and policy trade-offs**, and apply the **tragedy of the commons**. If you can score well here, the real GED Social Studies test will feel comfortable.

[[check:The idea that government's authority comes from the consent of the governed to protect their rights is called what?|the social contract;;social contract theory;;social contract|Social-contract theory roots government in the consent of the governed.]]
            """,
        ),
        (
            "2. Reasoning at the Highest Level",
            r"""
Elite Social Studies is about evaluating ideas, sources, and trade-offs.

- **Political philosophy.** The Founders drew on social-contract thinkers: government exists by consent to protect rights, and the Federalist Papers argued 'ambition must be made to counteract ambition.'
- **Comparing sources.** Read two documents on one issue, find where they agree and clash, and judge which is better supported.
- **Judicial philosophy.** Activism reads the Constitution broadly to address new problems; restraint defers to elected branches.
- **Policy trade-offs.** Comparative advantage, the inflation-unemployment tension, and shared-resource dilemmas force hard choices.

[[figure:supply_demand|Markets balance competing forces; so do governments, sources, and policies -- weigh both sides.]]

[[check:When many users overuse a shared resource like a common pasture until it is ruined, this dilemma is called what?|the tragedy of the commons;;tragedy of the commons|It is the tragedy of the commons -- shared resources get overused.]]
            """,
        ),
        (
            "3. Strategy for Elite Items",
            r"""
- **Name the principle precisely.** Social contract, judicial review, federalism, externality -- match the exact idea to the scenario.
- **Compare sources head to head.** Identify each author's claim, evidence, and bias; decide which is better supported.
- **Weigh the trade-off.** Most elite economics and policy questions ask what is gained AND what is given up.
- **Synthesize the data.** Draw a conclusion that fits ALL the evidence, not just one figure.
- **Never leave a blank.** Eliminate what you can, then choose.

[[check:To decide which of two conflicting documents is more reliable, you weigh each author's evidence and what else?|bias;;point of view;;purpose and bias;;perspective|Weigh each author's perspective, purpose, and possible bias.]]
            """,
        ),
    ],
    "mcqs": [
        # ====================== CIVICS & GOVERNMENT ==========================
        {
            "text": ("**Civics.** The Declaration of Independence says governments derive 'their just powers from "
                     "the consent of the governed.' This reflects the philosophy that:"),
            "difficulty": 3,
            "choices": [("Government's authority comes from the people it serves", True),
                        ("Kings rule by divine right alone", False),
                        ("Government needs no justification", False),
                        ("Only the wealthy may govern", False)],
            "explanation": r"This is social-contract theory: legitimate power flows from the consent of the governed. The trap, divine right, is the idea the Founders rejected. Pro tip: 'consent of the governed' is the heart of social-contract thinking.",
        },
        {
            "text": ("**Civics.** Federalist No. 51 argues that 'ambition must be made to counteract ambition.' "
                     "This is a justification for:"),
            "difficulty": 3,
            "choices": [("Checks and balances among the branches", True),
                        ("Giving one branch all the power", False),
                        ("Abolishing the government", False),
                        ("Rule by a single ambitious leader", False)],
            "explanation": r"The phrase argues that each branch's self-interest should check the others' -- the logic of checks and balances. The trap 'one branch all the power' is the opposite. Pro tip: Federalist 51 explains WHY power is divided and balanced.",
        },
        {
            "text": ("**Civics.** A judge interprets the Constitution broadly to extend a right to a situation the "
                     "Founders never anticipated. Critics call this approach 'judicial activism'; its "
                     "opposite, deferring to the elected branches, is called:"),
            "difficulty": 3,
            "choices": [("Judicial restraint", True), ("Judicial review", False),
                        ("Impeachment", False), ("Federalism", False)],
            "explanation": r"Judicial restraint defers to the legislature and reads the Constitution narrowly. The trap, judicial review, is the power to strike laws, which both approaches use. Pro tip: activism = broad interpretation; restraint = deference to elected branches.",
        },
        {
            "text": ("**Civics.** A newspaper wants to publish details of an ongoing trial, while the defendant "
                     "argues the coverage will prevent a fair jury. This conflict pits freedom of the press "
                     "against the right to:"),
            "difficulty": 3,
            "choices": [("A fair trial", True), ("Bear arms", False),
                        ("Vote in elections", False), ("Avoid all taxes", False)],
            "explanation": r"This is a clash between two constitutional rights: a free press and a fair trial. The trap, the right to bear arms, isn't involved. Pro tip: rights can conflict, and courts must balance them.",
        },
        {
            "text": ("**Civics.** Two essays from 1788 disagree: one argues a strong national government will "
                     "protect liberty; the other warns it will threaten it. To judge which is more "
                     "persuasive, a reader should evaluate:"),
            "difficulty": 3,
            "choices": [("The evidence and reasoning each essay offers", True),
                        ("Which essay is printed in larger type", False),
                        ("Which author lived longer", False),
                        ("The number of words in each title", False)],
            "explanation": r"Comparing the strength of each argument's evidence and logic is how to judge them. The traps (type size, lifespan, title length) are irrelevant. Pro tip: weigh the quality of reasoning and evidence, not surface features.",
        },
        {
            "text": ("**Civics.** A law passed by a large majority strips a small minority group of a basic right. "
                     "A court that overturns the law is protecting the principle that:"),
            "difficulty": 3,
            "choices": [("Majority rule does not allow violating minority rights", True),
                        ("The majority may do anything it wishes", False),
                        ("Courts must always obey the legislature", False),
                        ("Rights apply only to majorities", False)],
            "explanation": r"Constitutional rights limit what even a majority can do, protecting minorities. The trap 'the majority may do anything' ignores those limits. Pro tip: constitutional democracy balances majority rule with minority rights.",
        },
        {
            "text": ("**Civics.** After the Supreme Court interprets the Constitution in a way many oppose, the "
                     "public's most direct lasting remedy is to:"),
            "difficulty": 3,
            "choices": [("Amend the Constitution", True),
                        ("Ignore the ruling entirely", False),
                        ("Abolish the judicial branch", False),
                        ("Have the President rewrite the decision", False)],
            "explanation": r"A constitutional amendment can override a Court interpretation -- a check by the people and states. The trap 'ignore the ruling' isn't a lawful remedy. Pro tip: amendments have been used to reverse specific Court decisions.",
        },
        {
            "text": ("**Civics.** 'Cooperative federalism' differs from 'dual federalism' in that cooperative "
                     "federalism features:"),
            "difficulty": 3,
            "choices": [("Federal and state governments working together on shared programs", True),
                        ("The federal government abolishing all states", False),
                        ("States ignoring all federal law", False),
                        ("A single national king", False)],
            "explanation": r"Cooperative federalism blends federal and state efforts (shared funding and programs), unlike sharply separated dual federalism. The trap 'abolishing all states' is neither. Pro tip: cooperative = mixed/shared; dual = separate 'layer cake' of powers.",
        },
        {
            "text": ("**Civics.** A person breaks a law they consider unjust, openly and nonviolently, and accepts "
                     "the legal penalty to call attention to the injustice. This is best described as:"),
            "difficulty": 3,
            "choices": [("Civil disobedience", True), ("Judicial review", False),
                        ("A tariff", False), ("Federalism", False)],
            "explanation": r"Openly breaking an unjust law and accepting the consequences to spur change is civil disobedience. The trap, judicial review, is a court power. Pro tip: civil disobedience, used in the Civil Rights Movement, accepts the penalty to highlight injustice.",
        },
        {
            "text": ("**Civics.** The Necessary and Proper (or 'Elastic') Clause is significant because it allows "
                     "the meaning of federal power to:"),
            "difficulty": 3,
            "choices": [("Stretch to meet needs the Founders could not foresee", True),
                        ("Shrink until the government can do nothing", False),
                        ("Be decided only by foreign courts", False),
                        ("Stay frozen and never change", False)],
            "explanation": r"The Elastic Clause lets Congress adapt its powers to new circumstances. The trap 'stay frozen' is the opposite of 'elastic.' Pro tip: the clause has expanded federal power to address modern problems.",
        },
        {
            "text": ("**Civics.** During a crisis, a government expands surveillance to improve security, raising "
                     "fears about privacy. This illustrates a recurring tension between:"),
            "difficulty": 3,
            "choices": [("Security and individual liberty", True),
                        ("Latitude and longitude", False),
                        ("Supply and demand", False),
                        ("Igneous and metamorphic rock", False)],
            "explanation": r"Expanding security can come at the cost of liberty -- a classic trade-off. The trap, supply and demand, is economic. Pro tip: balancing safety against freedom is a recurring constitutional dilemma.",
        },
        {
            "text": ("**Civics.** A 'winner-take-all' election system, where the top vote-getter wins everything "
                     "and runners-up get nothing, tends to:"),
            "difficulty": 3,
            "choices": [("Favor a small number of large parties", True),
                        ("Guarantee dozens of equal parties", False),
                        ("Eliminate all elections", False),
                        ("Make voting illegal", False)],
            "explanation": r"Winner-take-all systems push voters toward a few major parties, since votes for small parties often 'waste.' The trap 'dozens of equal parties' fits proportional systems instead. Pro tip: election rules shape the party system.",
        },
        {
            "text": ("**Civics.** Two government officials describe the same new policy: a supporter calls it 'bold "
                     "reform'; an opponent calls it 'reckless overreach.' These loaded phrases mainly reveal "
                     "the speakers':"),
            "difficulty": 3,
            "choices": [("Differing points of view, or bias", True),
                        ("Agreement on the policy", False),
                        ("The exact cost of the policy", False),
                        ("A scientific measurement", False)],
            "explanation": r"Charged words like 'bold' versus 'reckless' expose each speaker's bias. The trap 'agreement' contradicts the opposite framing. Pro tip: word choice reveals point of view -- read loaded language as a clue to bias.",
        },
        {
            "text": ("**Civics.** A state requires voters to show ID. Supporters say it prevents fraud; critics say "
                     "it burdens eligible voters. A court weighing this law must balance:"),
            "difficulty": 3,
            "choices": [("Election integrity against access to voting", True),
                        ("Inflation against deflation", False),
                        ("Latitude against longitude", False),
                        ("Igneous against sedimentary rock", False)],
            "explanation": r"The court must weigh preventing fraud against keeping voting accessible -- competing goods. The trap, inflation vs. deflation, is economic. Pro tip: many civics questions ask you to identify the two values in tension.",
        },
        {
            "text": ("**Civics.** A core reason the Founders chose a written constitution over relying on tradition "
                     "alone was to:"),
            "difficulty": 3,
            "choices": [("Clearly define and limit government power in a lasting document", True),
                        ("Make the rules impossible to know", False),
                        ("Hand all power to one leader", False),
                        ("Avoid ever changing the law", False)],
            "explanation": r"A written constitution fixes and limits government power so citizens can hold leaders to it. The trap 'all power to one leader' is the opposite. Pro tip: writing it down makes the limits on government clear and enforceable.",
        },
        {
            "text": ("**Civics.** The principle of 'separation of powers' refers to dividing government by "
                     "FUNCTION, while 'federalism' divides government by:"),
            "difficulty": 3,
            "choices": [("Level (national, state, and local)", True),
                        ("Color", False),
                        ("Alphabetical order", False),
                        ("Population only", False)],
            "explanation": r"Separation of powers splits functions (legislative, executive, judicial); federalism splits power across levels of government. The trap 'color' is meaningless here. Pro tip: powers split by job = separation of powers; split by level = federalism.",
        },
        {
            "text": ("**Civics.** A document claims an event occurred but was written 50 years later by someone who "
                     "was not present, while another was written the same week by an eyewitness. The "
                     "eyewitness account is generally considered:"),
            "difficulty": 3,
            "choices": [("A primary source, often more direct evidence", True),
                        ("Automatically false", False),
                        ("Less useful because it is older", False),
                        ("Identical to the later account", False)],
            "explanation": r"A firsthand, same-time account is a primary source, usually stronger direct evidence (though still possibly biased). The trap 'automatically false' overstates the case. Pro tip: primary sources are firsthand; secondary sources interpret later.",
        },
        {
            "text": ("**Civics.** A law is challenged as unconstitutional. A judge practicing judicial RESTRAINT "
                     "would most likely:"),
            "difficulty": 3,
            "choices": [("Uphold the law unless it clearly violates the Constitution", True),
                        ("Strike down any law the judge personally dislikes", False),
                        ("Refuse to ever hear the case", False),
                        ("Rewrite the law as the judge prefers", False)],
            "explanation": r"Judicial restraint defers to the elected legislature, overturning a law only when the violation is clear. The trap 'strike down any law the judge dislikes' describes activism, even overreach. Pro tip: restraint favors leaving policy to elected branches.",
        },
        # =========================== U.S. HISTORY ============================
        {
            "text": ("**U.S. History.** The Founders' ideas about natural rights and government by consent drew "
                     "heavily on thinkers of the:"),
            "difficulty": 3,
            "choices": [("Enlightenment", True), ("Cold War", False),
                        ("Industrial Revolution", False), ("Space Age", False)],
            "explanation": r"Enlightenment thinkers like Locke shaped the ideas of natural rights and consent in the Declaration. The trap, the Cold War, came nearly two centuries later. Pro tip: the Enlightenment inspired the American Revolution's political ideals.",
        },
        {
            "text": ("**U.S. History.** The Civil Rights Act of 1964 was a landmark law because it:"),
            "difficulty": 3,
            "choices": [("Banned discrimination based on race, color, religion, sex, or national origin", True),
                        ("Started the Civil War", False),
                        ("Created the Electoral College", False),
                        ("Ended the American Revolution", False)],
            "explanation": r"The 1964 Act outlawed major forms of discrimination in employment and public places. The trap, starting the Civil War, is a century off. Pro tip: the Civil Rights Act of 1964 was a major legislative victory of the movement.",
        },
        {
            "text": ("**U.S. History.** Both the Progressive Era reforms and the New Deal expanded the "
                     "government's role in the economy. A key DIFFERENCE is that the New Deal responded "
                     "specifically to:"),
            "difficulty": 3,
            "choices": [("The Great Depression's mass unemployment", True),
                        ("The American Revolution", False),
                        ("A British invasion", False),
                        ("The fall of Rome", False)],
            "explanation": r"The New Deal was a direct response to the Great Depression, while Progressivism addressed industrial-era problems earlier. The trap, the Revolution, is unrelated. Pro tip: compare reforms by the crises that prompted them.",
        },
        {
            "text": ("**U.S. History.** The Cold War is often described as an 'ideological' conflict because it was "
                     "rooted in a clash between:"),
            "difficulty": 3,
            "choices": [("Capitalism/democracy and communism", True),
                        ("Two identical economic systems", False),
                        ("Rival sports leagues", False),
                        ("Different time zones", False)],
            "explanation": r"The Cold War pitted democratic capitalism against communism -- a battle of ideologies. The trap 'two identical systems' ignores the core difference. Pro tip: 'ideological' means a clash of competing belief systems.",
        },
        {
            "text": ("**U.S. History.** A historian finds that a wartime government poster urges citizens to "
                     "'buy war bonds to defeat the enemy.' The poster is most useful as evidence of:"),
            "difficulty": 3,
            "choices": [("How the government tried to shape public opinion", True),
                        ("The exact number of soldiers in the war", False),
                        ("The secret plans of the enemy", False),
                        ("Next year's weather", False)],
            "explanation": r"As propaganda, the poster reveals government efforts to influence the public. The trap 'exact number of soldiers' is not what a poster shows. Pro tip: a source is evidence of its maker's purpose, here, persuasion.",
        },
        {
            "text": ("**U.S. History.** The 13th, 14th, and 15th Amendments are together called the "
                     "'Reconstruction Amendments' because they were passed to:"),
            "difficulty": 3,
            "choices": [("Define the rights of formerly enslaved people after the Civil War", True),
                        ("Declare independence from Britain", False),
                        ("Create the federal income tax", False),
                        ("End World War II", False)],
            "explanation": r"These three amendments abolished slavery and established citizenship and voting rights after the Civil War. The trap, the income tax, was the 16th Amendment. Pro tip: 13th, 14th, 15th = the Reconstruction Amendments.",
        },
        {
            "text": ("**U.S. History.** Two textbooks describe westward expansion differently: one emphasizes "
                     "pioneer opportunity, the other emphasizes harm to Native nations. Together they show "
                     "that history can be:"),
            "difficulty": 3,
            "choices": [("Viewed through multiple, sometimes conflicting perspectives", True),
                        ("Known completely from a single book", False),
                        ("Free of any point of view", False),
                        ("Impossible to study at all", False)],
            "explanation": r"Different perspectives highlight different truths about the same events. The trap 'a single book' ignores that sources have viewpoints. Pro tip: strong historical understanding weighs multiple perspectives.",
        },
        # ============================ ECONOMICS ==============================
        {
            "text": ("**Economics.** In the short run, economists often observe a trade-off in which policies that "
                     "lower unemployment can tend to raise:"),
            "difficulty": 3,
            "choices": [("Inflation", True), ("The number of states", False),
                        ("Lines of latitude", False), ("The speed of light", False)],
            "explanation": r"A common short-run trade-off links lower unemployment with higher inflation. The trap 'number of states' is unrelated. Pro tip: policymakers often weigh inflation against unemployment.",
        },
        {
            "text": ("**Economics.** Country A can produce cloth at a lower opportunity cost than Country B. "
                     "Comparative advantage suggests Country A should:"),
            "difficulty": 3,
            "choices": [("Specialize in cloth and trade for other goods", True),
                        ("Stop producing anything", False),
                        ("Produce only goods it makes poorly", False),
                        ("Refuse to trade at all", False)],
            "explanation": r"A nation should specialize where its opportunity cost is lowest, then trade. The trap 'only goods it makes poorly' is the reverse. Pro tip: comparative advantage means producing what you give up the least to make.",
        },
        {
            "text": ("**Economics.** A village shares a common pasture. Each herder adds more animals for personal "
                     "gain until the overgrazed pasture is ruined for everyone. This dilemma is called:"),
            "difficulty": 3,
            "choices": [("The tragedy of the commons", True),
                        ("Comparative advantage", False),
                        ("Judicial review", False),
                        ("Manifest destiny", False)],
            "explanation": r"When individuals overuse a shared resource for private gain, all suffer -- the tragedy of the commons. The trap, comparative advantage, is about trade. Pro tip: shared, unmanaged resources tend to be overused.",
        },
        {
            "text": ("**Economics.** A central bank RAISES interest rates while the government CUTS spending at the "
                     "same time. Both actions are likely intended to:"),
            "difficulty": 3,
            "choices": [("Slow down an overheating economy and curb inflation", True),
                        ("Cause a recession on purpose forever", False),
                        ("Increase inflation rapidly", False),
                        ("Have no effect at all", False)],
            "explanation": r"Higher rates (monetary) and less spending (fiscal) both cool demand, fighting inflation. The trap 'increase inflation' is the opposite effect. Pro tip: tighter money and tighter budgets both slow the economy.",
        },
        {
            "text": ("**Economics.** A data table shows that as a country's spending on education rose over 20 "
                     "years, its average income also rose. The MOST cautious conclusion is that the two are:"),
            "difficulty": 3,
            "choices": [("Correlated, though other factors may be involved", True),
                        ("Proven to have no relationship", False),
                        ("Certainly cause and effect with no other factors", False),
                        ("Identical measurements", False)],
            "explanation": r"A correlation is shown, but other factors could contribute, so causation isn't proven. The trap 'certainly cause and effect' overclaims. Pro tip: correlation suggests a link but does not, by itself, prove causation.",
        },
        # ====================== GEOGRAPHY & THE WORLD ========================
        {
            "text": ("**Geography.** As countries industrialize, birth and death rates tend to fall and "
                     "populations age. This long-term shift in population patterns is called the:"),
            "difficulty": 3,
            "choices": [("Demographic transition", True), ("Tragedy of the commons", False),
                        ("Electoral College", False), ("Rock cycle", False)],
            "explanation": r"The demographic transition describes how birth and death rates change as a society develops. The trap, the tragedy of the commons, is a resource dilemma. Pro tip: developed nations often have low birth rates and aging populations.",
        },
        {
            "text": ("**Geography.** Globalization has lowered the cost of many goods but also moved some factory "
                     "jobs overseas. This illustrates that globalization involves:"),
            "difficulty": 3,
            "choices": [("Trade-offs, with both winners and losers", True),
                        ("Only benefits for everyone", False),
                        ("Only harm for everyone", False),
                        ("No economic effects at all", False)],
            "explanation": r"Globalization brings cheaper goods but can displace workers -- gains and losses together. The traps pick only one side. Pro tip: most major economic changes create both winners and losers.",
        },
        {
            "text": ("**Geography.** Several nations share a single large river for drinking water and farming. "
                     "Managing it fairly most likely requires:"),
            "difficulty": 3,
            "choices": [("International cooperation and agreements", True),
                        ("Each nation ignoring the others", False),
                        ("Changing the river's latitude", False),
                        ("A constitutional amendment in one country", False)],
            "explanation": r"A shared resource crossing borders requires nations to cooperate to avoid conflict and overuse. The trap 'ignoring the others' invites disputes. Pro tip: shared transboundary resources demand cooperation, echoing the commons problem.",
        },
        {
            "text": ("**Geography.** A map shows factories clustered near coal deposits and rail lines in the "
                     "1800s. This pattern best supports the conclusion that industry located where it could:"),
            "difficulty": 3,
            "choices": [("Access energy and transport cheaply", True),
                        ("Avoid all natural resources", False),
                        ("Stay far from any transportation", False),
                        ("Escape the law of gravity", False)],
            "explanation": r"Clustering near coal (energy) and rail (transport) shows industry sought cheap power and shipping. The trap 'avoid all natural resources' contradicts the map. Pro tip: read a map's pattern, then infer the reason behind it.",
        },
        {
            "text": ("**Geography.** A wealthy nation and a developing nation debate limits on carbon emissions. "
                     "The developing nation argues limits would slow its growth. This dispute reflects a "
                     "tension between:"),
            "difficulty": 3,
            "choices": [("Economic development and environmental protection", True),
                        ("Latitude and longitude", False),
                        ("Judicial review and impeachment", False),
                        ("Igneous and sedimentary rock", False)],
            "explanation": r"The clash pits a nation's growth against global environmental goals -- a development-vs-environment trade-off. The trap, latitude vs. longitude, is a mapping concept. Pro tip: global policy often balances growth against sustainability.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the elite (Level 5) full-length GED Social Studies practice exam (35 questions; MCQ only)."

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
