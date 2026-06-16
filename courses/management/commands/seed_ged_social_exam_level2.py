"""
Seed a SECOND full-length 'GED Social Studies' practice exam -- Level 2, a harder
companion to ``seed_ged_social_exam``.

Same test-day structure (35 questions weighted toward Civics, with History,
Economics, and Geography; 70 minutes; scored 100-200, 145 to pass), but the items
are tougher: judicial review and the amendment process, the Reconstruction
amendments, cause-and-effect in U.S. history, inflation and opportunity cost, and
map and document reasoning. No 'easy' items.

Run:
    python manage.py seed_ged_social_exam_level2
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Full-Length Practice Exam (Level 2 - Advanced)",
    "slug": "ged-social-exam-level2",
    "program": "GED",
    "subject": "social",
    "description": (
        "A tougher, second full-length GED Social Studies practice exam for students who have cleared "
        "Level 1. Same test-day format -- 35 questions weighted toward Civics & Government, with U.S. "
        "History, Economics, and Geography, 70 minutes, scored 100-200 (145 to pass) -- but every item is "
        "medium or hard. It pushes into judicial review and the amendment process, the Reconstruction "
        "amendments, cause-and-effect in U.S. history, inflation and opportunity cost, and reading maps "
        "and documents. Every question includes a worked explanation and a pro tip."
    ),
    "lessons": [
        (
            "1. Level 2: What's Harder",
            r"""
This is the **advanced** GED Social Studies practice exam. The format matches the real test and Level 1:

- **35 questions** in **70 minutes**, weighted toward **Civics & Government**, with **U.S. History**, **Economics**, and **Geography**.
- Scored **100-200**, with **145 to pass**.

**What's harder here than Level 1:** the questions move past single facts to **how government works** (judicial review, the amendment process, federalism in action), **why historical events happened** (cause and effect), and **economic reasoning** (inflation, opportunity cost, shifting supply and demand). You will also read documents and maps more closely.

[[check:When the Supreme Court declares a law unconstitutional, it is using which power?|judicial review|Judicial review lets the courts strike down laws that violate the Constitution.]]
            """,
        ),
        (
            "2. How Government and History Connect",
            r"""
Advanced Social Studies rewards reasoning about systems and causes.

- **Checks in action.** Congress makes laws, the President can veto, and the courts can rule a law unconstitutional (judicial review).
- **Amending the Constitution** is deliberately hard: proposed by two-thirds of Congress and ratified by three-fourths of the states.
- **Cause and effect.** Ask what led to an event (a cause) and what followed from it (an effect).
- **Point of view.** A document or cartoon argues a position -- identify the author's purpose and bias.

[[figure:bill_to_law|A bill must clear both houses of Congress and the President before it becomes law.]]

[[check:How many of the states must ratify an amendment for it to be added to the Constitution -- one-half, two-thirds, or three-fourths?|three-fourths;;3/4;;three fourths|Three-fourths of the states must ratify an amendment.]]
            """,
        ),
        (
            "3. Strategy for Harder Items",
            r"""
- **Read the source first.** A chart, map, or quotation usually contains the answer; check its title, labels, and date.
- **Trace cause to effect.** Distinguish what caused an event from what merely came before it.
- **Watch the point of view.** Persuasive documents take a side -- name it before judging the content.
- **Apply, don't just recall.** Many questions give a scenario and ask which principle it shows.
- **Never leave a blank.** Eliminate what you can, then choose.

[[check:Two events happen in order. Does the earlier one always CAUSE the later one? Answer yes or no.|no|Coming before something is not the same as causing it.]]
            """,
        ),
    ],
    "mcqs": [
        # ====================== CIVICS & GOVERNMENT ==========================
        {
            "text": r"**Civics.** When the Supreme Court rules that a law passed by Congress is unconstitutional, it is exercising the power of:",
            "difficulty": 3,
            "choices": [("Judicial review", True), ("The veto", False),
                        ("Impeachment", False), ("Taxation", False)],
            "explanation": r"Judicial review lets the courts strike down laws that conflict with the Constitution. The trap, the veto, is the President's power. Pro tip: judicial review is the judicial branch's main check on the other two.",
        },
        {
            "text": r"**Civics.** Amending the U.S. Constitution requires a proposal by two-thirds of Congress and ratification by:",
            "difficulty": 3,
            "choices": [("Three-fourths of the states", True),
                        ("A simple majority of one state", False),
                        ("The President alone", False),
                        ("The Supreme Court", False)],
            "explanation": r"An amendment must be ratified by three-fourths of the states. The trap, the President alone, has no role in amending the Constitution. Pro tip: the high bar (2/3 then 3/4) makes the Constitution hard to change on a whim.",
        },
        {
            "text": r"**Civics.** The 13th Amendment to the Constitution is most important because it:",
            "difficulty": 3,
            "choices": [("Abolished slavery in the United States", True),
                        ("Gave women the right to vote", False),
                        ("Created the income tax", False),
                        ("Set presidential term limits", False)],
            "explanation": r"The 13th Amendment (1865) abolished slavery. The trap, women's suffrage, was the 19th Amendment. Pro tip: 13th = end of slavery, 14th = citizenship and equal protection, 15th = voting regardless of race.",
        },
        {
            "text": r"**Civics.** The 14th Amendment guaranteed citizenship and 'equal protection of the laws' to:",
            "difficulty": 3,
            "choices": [("All persons born or naturalized in the United States", True),
                        ("Only members of Congress", False),
                        ("Only property owners", False),
                        ("Only the President's family", False)],
            "explanation": r"The 14th Amendment extended citizenship and equal protection to all born or naturalized in the U.S. The trap, only property owners, describes earlier, narrower rules. Pro tip: the 14th Amendment is the basis of equal-protection cases.",
        },
        {
            "text": r"**Civics.** In the U.S. federal system, running public schools and holding local elections are mainly the responsibility of:",
            "difficulty": 3,
            "choices": [("State and local governments", True),
                        ("The President alone", False),
                        ("The Supreme Court", False),
                        ("Foreign governments", False)],
            "explanation": r"Under federalism, states and localities handle schools and elections. The trap, the President, does not run local schools. Pro tip: federalism leaves many day-to-day powers to the states.",
        },
        {
            "text": r"**Civics.** The main reason the Founders divided the government into three branches was to:",
            "difficulty": 3,
            "choices": [("Prevent any one branch from becoming too powerful", True),
                        ("Make laws as quickly as possible", False),
                        ("Save money on government salaries", False),
                        ("Give the President total control", False)],
            "explanation": r"Separation of powers and checks and balances guard against tyranny by spreading power. The trap, giving the President total control, is the opposite goal. Pro tip: the Founders feared concentrated power, so they split it up.",
        },
        {
            "text": r"**Civics.** The principle that everyone, including government leaders, must obey the law is called:",
            "difficulty": 2,
            "choices": [("The rule of law", True), ("Free enterprise", False),
                        ("Manifest destiny", False), ("Globalization", False)],
            "explanation": r"The rule of law means no one is above the law, not even leaders. The trap, free enterprise, is an economic idea. Pro tip: rule of law protects citizens from arbitrary government.",
        },
        {
            "text": r"**Civics.** A person accused of a crime has the right to a fair trial and proper legal procedures. This protection is known as:",
            "difficulty": 3,
            "choices": [("Due process of law", True), ("A tariff", False),
                        ("Popular sovereignty", False), ("A subsidy", False)],
            "explanation": r"Due process guarantees fair legal procedures before the government can take life, liberty, or property. The trap, a tariff, is an import tax. Pro tip: due process is promised in the 5th and 14th Amendments.",
        },
        {
            "text": r"**Civics.** Which of these is a power of the legislative branch (Congress)?",
            "difficulty": 3,
            "choices": [("Declaring war and collecting taxes", True),
                        ("Interpreting the Constitution", False),
                        ("Commanding the army in the field", False),
                        ("Vetoing its own bills", False)],
            "explanation": r"Congress can declare war, collect taxes, and regulate commerce. The trap, interpreting the Constitution, is the judicial branch's job. Pro tip: 'power of the purse' and the power to declare war belong to Congress.",
        },
        {
            "text": r"**Civics.** Justices of the U.S. Supreme Court are appointed by the President and, once confirmed, generally serve:",
            "difficulty": 3,
            "choices": [("For life (during good behavior)", True),
                        ("For a two-year term", False),
                        ("Only while the President is in office", False),
                        ("Until the next election", False)],
            "explanation": r"Federal judges serve lifetime appointments to keep them independent of politics. The trap, a two-year term, describes House members. Pro tip: lifetime tenure lets judges rule without fear of losing an election.",
        },
        {
            "text": r"**Civics.** The President's role as 'Commander in Chief' means the President:",
            "difficulty": 2,
            "choices": [("Leads the nation's armed forces", True),
                        ("Writes all the laws", False),
                        ("Decides Supreme Court cases", False),
                        ("Sets the price of goods", False)],
            "explanation": r"As Commander in Chief, the President leads the military. The trap, writing all laws, is Congress's role. Pro tip: the executive branch carries out and defends the nation, including commanding the armed forces.",
        },
        {
            "text": ("**Civics.** A pamphlet urges citizens to support a new amendment, listing only its benefits "
                     "and none of its drawbacks. The pamphlet is best described as:"),
            "difficulty": 3,
            "choices": [("Persuasive, showing a clear point of view", True),
                        ("Completely neutral and balanced", False),
                        ("A scientific experiment", False),
                        ("A map of the country", False)],
            "explanation": r"Listing only benefits reveals a one-sided, persuasive purpose. The trap 'completely neutral' ignores the bias. Pro tip: a source that gives only one side is arguing a position, not reporting neutrally.",
        },
        {
            "text": r"**Civics.** Joining a community group, contacting an elected official, or peacefully protesting are all forms of:",
            "difficulty": 2,
            "choices": [("Civic participation", True), ("Judicial review", False),
                        ("Inflation", False), ("Federalism", False)],
            "explanation": r"These are ways citizens take part in public life -- civic participation. The trap, judicial review, is a court power. Pro tip: civic participation goes beyond voting to many forms of involvement.",
        },
        {
            "text": r"**Civics.** The Preamble to the Constitution lists goals such as to 'establish Justice' and 'promote the general Welfare.' The Preamble mainly serves to:",
            "difficulty": 3,
            "choices": [("State the purposes of the government being created", True),
                        ("List every law in detail", False),
                        ("Name the fifty states", False),
                        ("Set tax rates", False)],
            "explanation": r"The Preamble explains WHY the Constitution was written and what the government aims to do. The trap 'list every law' misreads its purpose. Pro tip: the Preamble is the mission statement of the Constitution.",
        },
        {
            "text": r"**Civics.** Political parties play an important role in democracy mainly by:",
            "difficulty": 2,
            "choices": [("Organizing candidates and ideas for voters to choose among", True),
                        ("Writing the Constitution", False),
                        ("Commanding the military", False),
                        ("Setting interest rates", False)],
            "explanation": r"Parties group candidates and platforms so voters have organized choices. The trap, writing the Constitution, is not their role. Pro tip: parties help structure elections and debate, though they are not mentioned in the Constitution.",
        },
        {
            "text": r"**Civics.** In a presidential election, the candidate who wins becomes President after receiving a majority of votes in the:",
            "difficulty": 3,
            "choices": [("Electoral College", True),
                        ("Supreme Court", False),
                        ("United Nations", False),
                        ("House of Lords", False)],
            "explanation": r"The Electoral College formally elects the President based on state outcomes. The trap, the Supreme Court, does not elect Presidents. Pro tip: U.S. presidential elections run through the Electoral College, not a direct national count alone.",
        },
        {
            "text": r"**Civics.** Which scenario best illustrates 'checks and balances' in action?",
            "difficulty": 3,
            "choices": [("Congress overrides the President's veto with a two-thirds vote", True),
                        ("A citizen votes in a local election", False),
                        ("A state builds a new highway", False),
                        ("A business lowers its prices", False)],
            "explanation": r"One branch (Congress) checking another (the President's veto) is the core of checks and balances. The trap, voting, is civic participation, not a check between branches. Pro tip: look for one branch limiting another to spot checks and balances.",
        },
        {
            "text": r"**Civics.** The Bill of Rights protects freedom of the press mainly to ensure that:",
            "difficulty": 3,
            "choices": [("People can share news and criticize the government", True),
                        ("Newspapers can charge any price", False),
                        ("The President controls all news", False),
                        ("Only the government may publish news", False)],
            "explanation": r"Freedom of the press lets people report and criticize without government censorship. The trap 'the President controls all news' is the opposite. Pro tip: a free press is a watchdog on those in power.",
        },
        # =========================== U.S. HISTORY ============================
        {
            "text": r"**U.S. History.** The colonists' protest of 'no taxation without representation' was a complaint that they were taxed by Britain but had:",
            "difficulty": 3,
            "choices": [("No elected representatives in the British Parliament", True),
                        ("Too many representatives in Parliament", False),
                        ("Refused to pay any taxes ever", False),
                        ("Already won their independence", False)],
            "explanation": r"Colonists objected to being taxed by a Parliament in which they had no vote. The trap 'too many representatives' is the opposite of their complaint. Pro tip: the grievance was being taxed without a voice in the decision.",
        },
        {
            "text": r"**U.S. History.** The U.S. Constitution replaced the Articles of Confederation mainly because the Articles created a national government that was:",
            "difficulty": 3,
            "choices": [("Too weak to govern effectively", True),
                        ("Far too powerful and controlling", False),
                        ("Run entirely by a king", False),
                        ("Identical to British rule", False)],
            "explanation": r"The Articles left the national government too weak (it couldn't tax or enforce laws well), so the Constitution strengthened it. The trap 'too powerful' is the reverse problem. Pro tip: the Articles' weakness led to a stronger federal Constitution in 1787.",
        },
        {
            "text": r"**U.S. History.** After the Civil War, the period in which the nation worked to rebuild the South and define the rights of formerly enslaved people was called:",
            "difficulty": 3,
            "choices": [("Reconstruction", True), ("The Revolution", False),
                        ("The Cold War", False), ("The Renaissance", False)],
            "explanation": r"Reconstruction (1865-1877) rebuilt the South and added the 13th, 14th, and 15th Amendments. The trap, the Revolution, came nearly a century earlier. Pro tip: Reconstruction directly followed the Civil War.",
        },
        {
            "text": r"**U.S. History.** The Industrial Revolution in the United States led to major growth in:",
            "difficulty": 3,
            "choices": [("Factories and cities", True),
                        ("The number of kings", False),
                        ("Hunting and gathering", False),
                        ("The size of the dinosaur population", False)],
            "explanation": r"Industrialization brought factories, machines, and rapid urban growth. The trap 'the number of kings' is unrelated. Pro tip: the Industrial Revolution moved people from farms to factory cities.",
        },
        {
            "text": r"**U.S. History.** The Great Depression, the worst economic crisis in U.S. history, began with a stock market crash in:",
            "difficulty": 3,
            "choices": [("1929", True), ("1776", False),
                        ("1861", False), ("2008", False)],
            "explanation": r"The 1929 stock market crash triggered the Great Depression of the 1930s. The trap, 1861, is the start of the Civil War. Pro tip: 1929 crash, 1930s Depression -- mass unemployment and bank failures.",
        },
        {
            "text": r"**U.S. History.** The United States entered World War II after the 1941 attack on:",
            "difficulty": 3,
            "choices": [("Pearl Harbor", True), ("Fort Sumter", False),
                        ("the Alamo", False), ("Gettysburg", False)],
            "explanation": r"Japan's attack on Pearl Harbor in 1941 brought the U.S. into World War II. The trap, Fort Sumter, opened the Civil War in 1861. Pro tip: match each attack to its war -- Pearl Harbor goes with WWII.",
        },
        {
            "text": r"**U.S. History.** The Cold War was a long period of tension, without direct large-scale fighting between the two superpowers, the United States and the:",
            "difficulty": 3,
            "choices": [("Soviet Union", True), ("Roman Empire", False),
                        ("Confederacy", False), ("British colonies", False)],
            "explanation": r"The Cold War was a rivalry between the U.S. and the Soviet Union after WWII. The trap, the Roman Empire, is from ancient history. Pro tip: 'Cold' means rivalry and arms races, not direct war between the two.",
        },
        # ============================ ECONOMICS ==============================
        {
            "text": r"**Economics.** Inflation is best described as a general rise in prices over time, which means each dollar:",
            "difficulty": 3,
            "choices": [("Buys less than it did before", True),
                        ("Buys more than it did before", False),
                        ("Becomes a different currency", False),
                        ("Stops being money", False)],
            "explanation": r"When prices rise, the same dollar buys fewer goods -- its purchasing power falls. The trap 'buys more' is the opposite. Pro tip: inflation erodes the value of money over time.",
        },
        {
            "text": ("**Economics.** Use the graph.\n\n"
                     "[[figure:supply_demand|Supply and demand curves]]\n\n"
                     "If a bumper crop greatly increases the SUPPLY of apples while demand stays the same, "
                     "the price of apples will most likely:"),
            "difficulty": 3,
            "choices": [("Fall", True), ("Rise sharply", False),
                        ("Stay exactly the same", False), ("Disappear", False)],
            "explanation": r"More supply with unchanged demand pushes the price down. The trap 'rise sharply' would happen if supply fell. Pro tip: a surplus (extra supply) puts downward pressure on price.",
        },
        {
            "text": r"**Economics.** Gross Domestic Product (GDP) measures a country's:",
            "difficulty": 3,
            "choices": [("Total value of goods and services produced", True),
                        ("Number of registered voters", False),
                        ("Total land area", False),
                        ("Average daily temperature", False)],
            "explanation": r"GDP is the total value of all goods and services a country produces. The trap, number of voters, is a civics figure, not economic output. Pro tip: GDP is the standard measure of the size of an economy.",
        },
        {
            "text": r"**Economics.** When you choose to spend your time studying instead of working a paid shift, the wages you give up are called the:",
            "difficulty": 3,
            "choices": [("Opportunity cost", True), ("Tariff", False),
                        ("Surplus", False), ("Subsidy", False)],
            "explanation": r"Opportunity cost is the value of the next-best alternative you gave up. The trap, a tariff, is an import tax. Pro tip: every choice has an opportunity cost -- what you didn't choose.",
        },
        {
            "text": r"**Economics.** In a market economy, the prices of most goods are determined mainly by:",
            "difficulty": 3,
            "choices": [("The interaction of supply and demand", True),
                        ("A single government official", False),
                        ("The weather alone", False),
                        ("The alphabet", False)],
            "explanation": r"In a market economy, supply and demand set prices. The trap, a single official, describes a command economy. Pro tip: where supply meets demand is the market price (equilibrium).",
        },
        # ====================== GEOGRAPHY & THE WORLD ========================
        {
            "text": r"**Geography.** The Prime Meridian is the line of 0 degrees longitude. Lines of longitude are used, in part, to help set the world's:",
            "difficulty": 3,
            "choices": [("Time zones", True), ("Ocean tides", False),
                        ("Political parties", False), ("Tax rates", False)],
            "explanation": r"Longitude lines help divide the globe into time zones. The trap, ocean tides, is driven by the Moon's gravity. Pro tip: as you cross longitude lines east or west, the local time changes.",
        },
        {
            "text": ("**Geography.** A map's scale shows that 1 inch represents 100 miles. Two cities that are "
                     "3 inches apart on the map are actually about:"),
            "difficulty": 3,
            "choices": [("300 miles apart", True), ("33 miles apart", False),
                        ("103 miles apart", False), ("3 miles apart", False)],
            "explanation": r"Each inch is 100 miles, so 3 inches = 300 miles. The trap 33 divides instead of multiplying. Pro tip: multiply the map distance by the scale to get the real distance.",
        },
        {
            "text": ("**Geography.** People often leave a region because of war or a lack of jobs, and move to "
                     "places offering safety and work. These reasons are called:"),
            "difficulty": 3,
            "choices": [("Push and pull factors of migration", True),
                        ("Lines of latitude", False),
                        ("Checks and balances", False),
                        ("Supply and demand", False)],
            "explanation": r"Push factors drive people away; pull factors draw them to a new place. The trap, lines of latitude, is a mapping tool. Pro tip: 'push' = problems at home; 'pull' = opportunities elsewhere.",
        },
        {
            "text": r"**Geography.** In general, regions located very close to the equator tend to have climates that are:",
            "difficulty": 3,
            "choices": [("Warm year-round", True), ("Freezing year-round", False),
                        ("Always snowy", False), ("Without any sunlight", False)],
            "explanation": r"Near the equator, sunlight is most direct, so climates are warm all year. The trap 'freezing year-round' describes the poles. Pro tip: latitude shapes climate -- equator is warm, poles are cold.",
        },
        {
            "text": ("**Geography.** A country with large oil reserves often builds much of its economy around "
                     "exporting that oil. This best shows how:"),
            "difficulty": 3,
            "choices": [("Natural resources can shape a region's economy", True),
                        ("Time zones determine wealth", False),
                        ("Maps create oil", False),
                        ("Latitude sets prices", False)],
            "explanation": r"A region's natural resources strongly influence its economy and trade. The trap 'time zones determine wealth' is unrelated. Pro tip: where resources are found shapes what a region produces and sells.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the advanced (Level 2) full-length GED Social Studies practice exam (35 questions; MCQ only)."

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
            f"{course.questions.count()} questions (all medium/hard)."
        ))
