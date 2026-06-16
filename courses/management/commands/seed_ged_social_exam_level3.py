"""
Seed a THIRD full-length 'GED Social Studies' practice exam -- Level 3, the
expert tier. Same test-day structure (35 questions; 70 minutes; scored 100-200,
145 to pass), but the items reach the top of the GED's range: landmark Supreme
Court cases, the Federalist debate, reserved vs. enumerated powers, fiscal and
monetary policy, primary-source analysis, and cause-and-effect chains across
U.S. history.

Run:
    python manage.py seed_ged_social_exam_level3
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Full-Length Practice Exam (Level 3 - Expert)",
    "slug": "ged-social-exam-level3",
    "program": "GED",
    "subject": "social",
    "description": (
        "The hardest of the early-tier GED Social Studies practice exams, for students who have cleared "
        "Levels 1 and 2. Same test-day format -- 35 questions weighted toward Civics, with History, "
        "Economics, and Geography, 70 minutes, scored 100-200 (145 to pass) -- but the items sit at the "
        "top of the range: landmark Supreme Court cases, the Federalist debate, reserved vs. enumerated "
        "powers, fiscal and monetary policy, primary-source analysis, and cause-and-effect chains across "
        "U.S. history. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 3: The Expert Social Studies Test",
            r"""
This is the **expert** GED Social Studies practice exam. The format is unchanged:

- **35 questions** in **70 minutes**, weighted toward **Civics**, with **History**, **Economics**, and **Geography**; scored **100-200**, **145 to pass**.

**What makes Level 3 harder:** the questions demand that you **apply principles**, analyze **primary sources**, and trace **cause-and-effect chains**. You'll meet landmark cases (like the one that established judicial review), the Federalist vs. Anti-Federalist debate, fiscal and monetary policy, and document interpretation.

[[check:Which 1803 case established the Supreme Court's power of judicial review?|Marbury v. Madison;;Marbury v Madison;;Marbury|Marbury v. Madison (1803) established judicial review.]]
            """,
        ),
        (
            "2. Analyzing Sources and Tracing Causes",
            r"""
Expert Social Studies is about reasoning, not recall.

- **Apply the principle.** Many questions give a scenario and ask which constitutional idea it illustrates (federalism, due process, checks and balances).
- **Read primary sources.** Identify the author, the date, the audience, and the point of view of a document or quotation.
- **Chains of cause and effect.** Events connect -- the Civil War led to Reconstruction, which gave way to segregation, which sparked the Civil Rights Movement.
- **Two kinds of economic policy.** Fiscal policy is government taxing and spending; monetary policy is the central bank managing money and interest rates.

[[figure:us_timeline|Events connect across time -- each one shaped by what came before and shaping what came after.]]

[[check:Government changing tax rates and spending to steer the economy is which kind of policy -- fiscal or monetary?|fiscal;;fiscal policy|Fiscal policy is taxing and spending; monetary policy is the central bank's job.]]
            """,
        ),
        (
            "3. Strategy for the Hardest Items",
            r"""
- **Match the scenario to the principle.** Decide which idea (federalism, judicial review, due process) a situation shows before reading the choices.
- **Source it.** For a document, ask who wrote it, when, and why -- then read for bias.
- **Follow the chain.** Distinguish a cause from an effect, and an event from its long-term consequence.
- **Read charts for the trend.** Note the axes and units, then describe the pattern.
- **Never leave a blank.** Eliminate what you can, then choose.

[[check:To judge a historical document's reliability, naming its author and purpose is called what?|sourcing;;sourcing the document;;analyzing the source|Sourcing means examining who made a document and why.]]
            """,
        ),
    ],
    "mcqs": [
        # ====================== CIVICS & GOVERNMENT ==========================
        {
            "text": r"**Civics.** The Supreme Court's power to declare laws unconstitutional was established in the landmark case:",
            "difficulty": 3,
            "choices": [("Marbury v. Madison (1803)", True),
                        ("Brown v. Board of Education (1954)", False),
                        ("The Louisiana Purchase", False),
                        ("The Boston Tea Party", False)],
            "explanation": r"Marbury v. Madison established judicial review in 1803. The trap, Brown v. Board, ended school segregation in 1954. Pro tip: Marbury = judicial review; Brown = desegregation.",
        },
        {
            "text": r"**Civics.** Brown v. Board of Education (1954) was a landmark ruling because it declared that:",
            "difficulty": 3,
            "choices": [("Racial segregation in public schools was unconstitutional", True),
                        ("The President could serve three terms", False),
                        ("Congress could not collect taxes", False),
                        ("States could leave the Union", False)],
            "explanation": r"Brown overturned 'separate but equal,' ruling school segregation unconstitutional. The trap about a third term is unrelated. Pro tip: Brown v. Board was a turning point of the Civil Rights Movement.",
        },
        {
            "text": r"**Civics.** During the debate over ratifying the Constitution, the Anti-Federalists most strongly demanded:",
            "difficulty": 3,
            "choices": [("A Bill of Rights to protect individual liberties", True),
                        ("An immediate war with Britain", False),
                        ("The abolition of all states", False),
                        ("A king to rule the nation", False)],
            "explanation": r"Anti-Federalists feared a strong central government and insisted on a Bill of Rights. The trap, a king, is the opposite of their goal. Pro tip: the Anti-Federalists' demand gave us the first ten amendments.",
        },
        {
            "text": r"**Civics.** The 10th Amendment says that powers not given to the federal government are reserved to:",
            "difficulty": 3,
            "choices": [("The states and the people", True),
                        ("The President alone", False),
                        ("Foreign nations", False),
                        ("The Supreme Court only", False)],
            "explanation": r"The 10th Amendment reserves un-delegated powers to the states and the people. The trap, the President, would concentrate power instead. Pro tip: the 10th Amendment is the foundation of states' reserved powers.",
        },
        {
            "text": ("**Civics.** A state passes a law that directly conflicts with a valid federal law. Under the "
                     "Constitution's Supremacy Clause, the result is that:"),
            "difficulty": 3,
            "choices": [("The federal law generally prevails", True),
                        ("The state law automatically wins", False),
                        ("Both laws are thrown out forever", False),
                        ("The President must resign", False)],
            "explanation": r"The Supremacy Clause makes valid federal law supreme over conflicting state law. The trap 'state law automatically wins' reverses this. Pro tip: when state and federal law clash, federal law usually controls.",
        },
        {
            "text": r"**Civics.** Congress can remove a President from office for serious misconduct through the process of:",
            "difficulty": 3,
            "choices": [("Impeachment and conviction", True),
                        ("Judicial review", False),
                        ("A tariff", False),
                        ("A pocket veto", False)],
            "explanation": r"The House impeaches and the Senate convicts to remove an official. The trap, judicial review, is a court power. Pro tip: impeachment is a check Congress holds over the executive and judicial branches.",
        },
        {
            "text": r"**Civics.** Although the First Amendment protects free speech, the courts have ruled that this right is:",
            "difficulty": 3,
            "choices": [("Not absolute -- some speech, like direct threats, can be limited", True),
                        ("Unlimited in every situation", False),
                        ("Only for government officials", False),
                        ("A power of the states alone", False)],
            "explanation": r"Free speech is broad but not unlimited; threats and incitement can be restricted. The trap 'unlimited in every situation' overstates it. Pro tip: rights have limits where they cause direct harm to others.",
        },
        {
            "text": ("**Civics.** A mayor, a governor, and the President each lead an executive branch at a different "
                     "level of government. This layered structure best illustrates:"),
            "difficulty": 3,
            "choices": [("Federalism -- power divided among levels of government", True),
                        ("Judicial review", False),
                        ("Inflation", False),
                        ("Free trade", False)],
            "explanation": r"Power shared among local, state, and national levels is federalism. The trap, judicial review, is a court power. Pro tip: federalism stacks government into levels, each with its own executive.",
        },
        {
            "text": r"**Civics.** The right to vote has expanded over time through amendments. The 26th Amendment specifically:",
            "difficulty": 3,
            "choices": [("Lowered the voting age to 18", True),
                        ("Gave women the right to vote", False),
                        ("Abolished slavery", False),
                        ("Created the income tax", False)],
            "explanation": r"The 26th Amendment (1971) set the voting age at 18. The trap, women's suffrage, was the 19th Amendment. Pro tip: 15th (race), 19th (women), 26th (age 18) mark the expansion of voting rights.",
        },
        {
            "text": ("**Civics.** A federal court strikes down an executive order as exceeding the President's "
                     "authority. This is an example of one branch:"),
            "difficulty": 3,
            "choices": [("Checking the power of another branch", True),
                        ("Making a new law from scratch", False),
                        ("Setting tax rates", False),
                        ("Holding an election", False)],
            "explanation": r"A court limiting the executive is a check between branches. The trap 'making a new law' is the legislature's role, not the court's. Pro tip: when one branch limits another, that's checks and balances.",
        },
        {
            "text": ("**Civics.** A newspaper investigates and exposes corruption by a powerful official. This "
                     "illustrates the role of a free press as a:"),
            "difficulty": 3,
            "choices": [("Watchdog on those in power", True),
                        ("Branch of the military", False),
                        ("Member of the Supreme Court", False),
                        ("Tool of the government to control news", False)],
            "explanation": r"A free press holds the powerful accountable by exposing wrongdoing. The trap 'tool of the government' is the opposite of a free press. Pro tip: a free press acts as a check outside the three branches.",
        },
        {
            "text": ("**Civics.** 'Voting is a right; serving on a jury when summoned is a duty.' This statement "
                     "distinguishes between a:"),
            "difficulty": 3,
            "choices": [("Right (a freedom) and a responsibility (an obligation)", True),
                        ("Tariff and a subsidy", False),
                        ("State and a nation", False),
                        ("Cause and an effect", False)],
            "explanation": r"A right is a protected freedom; a responsibility is something citizens are expected to do. The trap, tariff and subsidy, is economic. Pro tip: rights protect you; responsibilities ask something of you.",
        },
        {
            "text": ("**Civics.** A political cartoon shows the three branches of government tugging on the same "
                     "rope from different sides, none able to pull it away. The cartoon most likely "
                     "comments on:"),
            "difficulty": 3,
            "choices": [("How checks and balances keep power in tension", True),
                        ("A real tug-of-war competition", False),
                        ("The price of rope", False),
                        ("How to sail a ship", False)],
            "explanation": r"The image of branches holding power in tension symbolizes checks and balances. The trap 'a real tug-of-war' reads the cartoon literally. Pro tip: political cartoons use symbols -- look for the idea behind the picture.",
        },
        {
            "text": r"**Civics.** The idea that government's powers should be restricted, often by a written constitution, is called:",
            "difficulty": 3,
            "choices": [("Limited government", True), ("Absolute monarchy", False),
                        ("Inflation", False), ("Globalization", False)],
            "explanation": r"Limited government means the government's power is bounded by law and a constitution. The trap, absolute monarchy, is unlimited rule. Pro tip: limited government protects liberty by capping what the state may do.",
        },
        {
            "text": ("**Civics.** A law guarantees that people accused of crimes receive a fair, public trial with "
                     "a lawyer. This protects their right to:"),
            "difficulty": 3,
            "choices": [("Due process of law", True), ("Free trade", False),
                        ("A tariff exemption", False), ("Manifest destiny", False)],
            "explanation": r"Fair legal procedures before punishment are due process. The trap, free trade, is economic. Pro tip: due process ensures the government follows fair rules before depriving anyone of liberty.",
        },
        {
            "text": r"**Civics.** The powers specifically listed for Congress in the Constitution, such as coining money, are called:",
            "difficulty": 3,
            "choices": [("Enumerated (delegated) powers", True),
                        ("Reserved powers", False),
                        ("Veto powers", False),
                        ("Royal powers", False)],
            "explanation": r"Enumerated powers are those expressly listed for the federal government. The trap, reserved powers, are those left to the states. Pro tip: enumerated = written out for Congress; reserved = left to the states.",
        },
        {
            "text": ("**Civics.** A citizen argues that because the Constitution does not mention the internet, "
                     "online speech is not protected. A court would most likely respond that:"),
            "difficulty": 3,
            "choices": [("Broad principles like free speech can apply to new situations", True),
                        ("The Constitution can never be interpreted", False),
                        ("Only speech on paper is protected", False),
                        ("The President decides what speech is allowed", False)],
            "explanation": r"Courts apply the Constitution's broad principles to new circumstances, like online speech. The trap 'only speech on paper' takes the text too narrowly. Pro tip: enduring principles are interpreted to fit modern life.",
        },
        {
            "text": r"**Civics.** In the U.S. system, the President proposes a budget, but the power to actually approve spending belongs to:",
            "difficulty": 3,
            "choices": [("Congress", True), ("The Supreme Court", False),
                        ("State governors", False), ("The military", False)],
            "explanation": r"Congress holds the 'power of the purse' and must approve spending. The trap, the Supreme Court, interprets law rather than funding government. Pro tip: the President proposes a budget, but Congress controls the money.",
        },
        # =========================== U.S. HISTORY ============================
        {
            "text": r"**U.S. History.** The belief in the 1800s that the United States was destined to expand across the continent to the Pacific was called:",
            "difficulty": 3,
            "choices": [("Manifest Destiny", True), ("Reconstruction", False),
                        ("The Cold War", False), ("The New Deal", False)],
            "explanation": r"Manifest Destiny was the belief that the U.S. should expand westward. The trap, Reconstruction, came after the Civil War. Pro tip: Manifest Destiny drove westward expansion and conflict with Native nations and Mexico.",
        },
        {
            "text": ("**U.S. History.** After Reconstruction ended, many Southern states passed 'Jim Crow' laws "
                     "that:"),
            "difficulty": 3,
            "choices": [("Enforced racial segregation and limited Black Americans' rights", True),
                        ("Guaranteed full equality for all races", False),
                        ("Abolished all state governments", False),
                        ("Ended the use of money", False)],
            "explanation": r"Jim Crow laws enforced segregation and stripped away rights gained in Reconstruction. The trap 'guaranteed full equality' is the opposite. Pro tip: Jim Crow segregation later fueled the Civil Rights Movement.",
        },
        {
            "text": ("**U.S. History.** During the Progressive Era (around 1900), reformers worked mainly to:"),
            "difficulty": 3,
            "choices": [("Address problems caused by rapid industrialization, such as poor working conditions", True),
                        ("Restore a king to power", False),
                        ("End all trade with other nations", False),
                        ("Return the country to hunting and gathering", False)],
            "explanation": r"Progressives fought corruption, unsafe factories, and child labor. The trap 'restore a king' is unrelated. Pro tip: the Progressive Era responded to the downsides of the Industrial Revolution.",
        },
        {
            "text": r"**U.S. History.** Franklin Roosevelt's 'New Deal' was a series of programs created mainly to:",
            "difficulty": 3,
            "choices": [("Provide relief and recovery during the Great Depression", True),
                        ("Win the American Revolution", False),
                        ("Start the Cold War", False),
                        ("Build the first railroads", False)],
            "explanation": r"The New Deal aimed to relieve suffering and revive the economy during the 1930s Depression. The trap, the Revolution, predates it by over 150 years. Pro tip: New Deal = Depression-era jobs, relief, and reforms.",
        },
        {
            "text": ("**U.S. History.** During the Cold War, the U.S. policy of 'containment' was meant to:"),
            "difficulty": 3,
            "choices": [("Stop the spread of communism to other countries", True),
                        ("Expand the British Empire", False),
                        ("End World War I", False),
                        ("Abolish the Constitution", False)],
            "explanation": r"Containment aimed to keep communism from spreading beyond where it already existed. The trap, the British Empire, is unrelated. Pro tip: containment shaped U.S. actions like the Marshall Plan and the Korean War.",
        },
        {
            "text": ("**U.S. History.** Read this excerpt: 'We hold these truths to be self-evident, that all men "
                     "are created equal...' This famous line comes from the:"),
            "difficulty": 3,
            "choices": [("Declaration of Independence", True),
                        ("U.S. Constitution", False),
                        ("Gettysburg Address", False),
                        ("Emancipation Proclamation", False)],
            "explanation": r"This line opens the Declaration of Independence (1776). The trap, the Constitution, begins 'We the People.' Pro tip: 'all men are created equal' = Declaration; 'We the People' = Constitution.",
        },
        {
            "text": ("**U.S. History.** The Civil Rights Movement of the 1950s and 1960s used strategies such as "
                     "boycotts, marches, and sit-ins, which were mainly:"),
            "difficulty": 3,
            "choices": [("Nonviolent forms of protest", True),
                        ("Armed military invasions", False),
                        ("Secret and hidden from the public", False),
                        ("Efforts to leave the country", False)],
            "explanation": r"The movement relied on nonviolent civil disobedience to demand equal rights. The trap 'armed military invasions' misrepresents its methods. Pro tip: nonviolent protest was central to leaders like Dr. King.",
        },
        # ============================ ECONOMICS ==============================
        {
            "text": ("**Economics.** When a government lowers taxes and increases spending to fight a recession, "
                     "it is using:"),
            "difficulty": 3,
            "choices": [("Fiscal policy", True), ("Monetary policy", False),
                        ("Foreign policy", False), ("Judicial review", False)],
            "explanation": r"Fiscal policy is the government's use of taxing and spending to steer the economy. The trap, monetary policy, is the central bank's control of money and interest rates. Pro tip: fiscal = taxes and spending; monetary = money supply and interest rates.",
        },
        {
            "text": ("**Economics.** A nation's central bank lowers interest rates to encourage borrowing and "
                     "spending. This is an example of:"),
            "difficulty": 3,
            "choices": [("Monetary policy", True), ("Fiscal policy", False),
                        ("A tariff", False), ("A constitutional amendment", False)],
            "explanation": r"Adjusting interest rates and the money supply is monetary policy, run by the central bank. The trap, fiscal policy, involves taxes and government spending instead. Pro tip: interest rates and money supply = monetary policy.",
        },
        {
            "text": ("**Economics.** Two countries each specialize in what they produce most efficiently and then "
                     "trade with each other. This idea, which explains why nations trade, is called:"),
            "difficulty": 3,
            "choices": [("Comparative advantage", True), ("Inflation", False),
                        ("Segregation", False), ("Federalism", False)],
            "explanation": r"Comparative advantage holds that nations gain by specializing and trading. The trap, inflation, is rising prices. Pro tip: specialization plus trade can leave both countries better off.",
        },
        {
            "text": ("**Economics.** During a recession, the unemployment rate usually:"),
            "difficulty": 3,
            "choices": [("Rises, as businesses cut jobs", True),
                        ("Falls to zero", False),
                        ("Has no connection to the economy", False),
                        ("Is set by the Supreme Court", False)],
            "explanation": r"In a recession, slowing business leads to layoffs and higher unemployment. The trap 'falls to zero' is the opposite. Pro tip: recessions and unemployment tend to rise together.",
        },
        {
            "text": ("**Economics.** A chart shows prices rising 3% one year, 4% the next, and 5% the year after. "
                     "The chart shows that inflation is:"),
            "difficulty": 3,
            "choices": [("Present and increasing each year", True),
                        ("Falling each year", False),
                        ("Exactly zero", False),
                        ("Turning into deflation", False)],
            "explanation": r"Prices rising by a growing percentage each year means inflation that is increasing. The trap 'falling each year' misreads the rising numbers. Pro tip: read the trend in the data -- here, the inflation rate climbs.",
        },
        # ====================== GEOGRAPHY & THE WORLD ========================
        {
            "text": ("**Geography.** A thematic map uses dark shading for crowded areas and light shading for "
                     "empty ones. This map most likely shows:"),
            "difficulty": 3,
            "choices": [("Population density", True), ("Average rainfall only", False),
                        ("The branches of government", False), ("Stock prices", False)],
            "explanation": r"Darker areas for more people indicate a population-density map. The trap, rainfall, isn't suggested by 'crowded' areas. Pro tip: read the map's legend to learn what the shading represents.",
        },
        {
            "text": ("**Geography.** Around the world, people have increasingly moved from rural areas into "
                     "cities. This process is called:"),
            "difficulty": 3,
            "choices": [("Urbanization", True), ("Glaciation", False),
                        ("Ratification", False), ("Inflation", False)],
            "explanation": r"Urbanization is the growth of cities as people move from the countryside. The trap, glaciation, is the spread of ice sheets. Pro tip: urbanization often follows industrial and economic opportunity in cities.",
        },
        {
            "text": ("**Geography.** Faster communication, global trade, and the spread of ideas across the world "
                     "are all features of:"),
            "difficulty": 3,
            "choices": [("Globalization", True), ("Segregation", False),
                        ("Impeachment", False), ("Photosynthesis", False)],
            "explanation": r"Globalization links the world's economies and cultures more tightly. The trap, segregation, is about separation, not connection. Pro tip: globalization increases connections in trade, technology, and culture.",
        },
        {
            "text": ("**Geography.** Control over a scarce, valuable resource such as fresh water or oil can be a "
                     "source of:"),
            "difficulty": 3,
            "choices": [("Cooperation or conflict between regions", True),
                        ("Changes to the law of gravity", False),
                        ("New lines of latitude", False),
                        ("Constitutional amendments", False)],
            "explanation": r"Scarce resources can lead regions to cooperate or to clash over access. The trap 'changes to gravity' is nonsensical. Pro tip: who controls key resources shapes economics and politics, sometimes sparking conflict.",
        },
        {
            "text": ("**Geography.** A government decides to build levees and flood walls after studying which "
                     "areas flood most often. This best shows how people:"),
            "difficulty": 3,
            "choices": [("Modify their environment to reduce natural hazards", True),
                        ("Change the Earth's orbit", False),
                        ("Write constitutional amendments", False),
                        ("Set interest rates", False)],
            "explanation": r"Building flood defenses is humans modifying the environment to manage risk -- human-environment interaction. The trap 'change the Earth's orbit' is impossible. Pro tip: people adapt to and reshape their environment to meet needs and reduce danger.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the expert (Level 3) full-length GED Social Studies practice exam (35 questions; MCQ only)."

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
            f"{course.questions.count()} questions (expert level)."
        ))
