"""
Seed a full-length 'GED Social Studies' practice exam that mirrors the real test:

  - 35 questions, the real GED Social Studies length, in 70 minutes.
  - Weighted like the real blueprint: Civics & Government (~50%), U.S. History
    (~20%), Economics (~15%), and Geography & the World (~15%), built around
    documents, maps, and charts.
  - Scored 100-200 (145 to pass).
  - A foundational (Level 1) difficulty spread.

Items are fresh and in the capstone style: each explanation names the tempting
wrong answer and ends with a Pro tip. Several questions reuse the diagram library.

Run:
    python manage.py seed_ged_social_exam
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Full-Length Practice Exam (Level 1 - Foundational)",
    "slug": "ged-social-exam",
    "program": "GED",
    "subject": "social",
    "description": (
        "A full-length, test-day-style GED Social Studies practice exam: 35 questions modeled on the real "
        "blueprint, weighted toward Civics & Government (about half the test) with U.S. History, "
        "Economics, and Geography, and built around documents, maps, and charts. It covers the core "
        "tested ideas -- the three branches, the Constitution and Bill of Rights, checks and balances, "
        "key events in U.S. history, supply and demand, and map skills -- at a foundational, easy-to-hard "
        "difficulty spread. Every question includes a worked explanation and a pro tip. Use the lessons "
        "to learn the test format (70 minutes, scored 100-200, 145 to pass) before taking the 35 "
        "questions as one timed rehearsal."
    ),
    "lessons": [
        (
            "1. How the GED Social Studies Test Works",
            r"""
This exam is built to feel like the **real GED Social Studies test**. Here is what you are walking into:

- **About 35 questions** in **70 minutes** -- about 2 minutes each.
- It is one timed section, built around **documents, maps, charts, and political cartoons**. Most questions hand you the source and ask you to read it -- the answer is usually right there.
- The content is weighted toward **Civics & Government** (about **50%**), then **U.S. History** (~20%), **Economics** (~15%), and **Geography & the World** (~15%).

**Scoring:** the test is scored from **100 to 200**, and you need **145 to pass**. There is **no penalty for a wrong answer**, so never leave a question blank.

[[check:About what share of the GED Social Studies test is Civics & Government?|50%;;about 50%;;half;;about half|Civics & Government is roughly half the test.]]
            """,
        ),
        (
            "2. Reading Sources & Civics Basics",
            r"""
Most points come from **reading a source carefully** and knowing a few civics essentials.

- **Use the source.** Read the title, the labels, the dates, and the author of any document, map, or chart before answering.
- **The three branches:** the **legislative** branch (Congress) makes laws, the **executive** branch (the President) enforces them, and the **judicial** branch (the courts) interprets them.
- **Checks and balances** let each branch limit the others, so no one branch grows too powerful.
- **Point of view.** A speech or political cartoon usually has a purpose -- ask what side it is taking.

[[figure:three_branches|The three branches of the U.S. government and their separate powers.]]

[[check:Which branch of government enforces the laws -- legislative, executive, or judicial?|executive|The executive branch (the President) enforces the laws.]]
            """,
        ),
        (
            "3. Test-Day Game Plan",
            r"""
- **Pacing.** About 2 minutes per question. If one stalls you, lock in a best guess, flag it, and move on.
- **Read the last line.** Know exactly what the question asks -- a cause, an effect, a main idea, or a value from a chart.
- **Watch for bias.** Documents and cartoons often argue a point of view; identify it before judging the content.
- **Never leave a blank.** No penalty for wrong answers -- eliminate what you can, then choose.
- **Use what the test gives you:** the documents, maps, and charts in front of you.

[[check:Is there any penalty for a wrong answer on the GED Social Studies test? Answer yes or no.|no|So always guess rather than leave a blank.]]
            """,
        ),
    ],
    "mcqs": [
        # =====================================================================
        # ====================== CIVICS & GOVERNMENT ==========================
        # =====================================================================
        {
            "text": ("**Civics.** Use the diagram.\n\n"
                     "[[figure:three_branches|The three branches of the U.S. government]]\n\n"
                     "Which branch of government is responsible for ENFORCING the laws?"),
            "difficulty": 1,
            "choices": [("The executive branch (the President)", True),
                        ("The legislative branch (Congress)", False),
                        ("The judicial branch (the courts)", False),
                        ("The state governments only", False)],
            "explanation": r"The executive branch, led by the President, enforces the laws. The trap, the legislative branch, makes the laws instead. Pro tip: executive = enforce; legislative = make; judicial = interpret.",
        },
        {
            "text": r"**Civics.** Which branch of the U.S. government has the power to MAKE laws?",
            "difficulty": 1,
            "choices": [("The legislative branch (Congress)", True),
                        ("The executive branch (the President)", False),
                        ("The judicial branch (the courts)", False),
                        ("The military", False)],
            "explanation": r"Congress, the legislative branch, writes and passes laws. The trap, the President, signs or vetoes them but does not write them. Pro tip: legislators legislate -- they make the laws.",
        },
        {
            "text": r"**Civics.** The branch of government that interprets the laws and decides what they mean is the:",
            "difficulty": 2,
            "choices": [("Judicial branch (the courts)", True),
                        ("Legislative branch", False),
                        ("Executive branch", False),
                        ("Electoral College", False)],
            "explanation": r"The judicial branch, including the Supreme Court, interprets laws and the Constitution. The trap, the legislative branch, makes laws rather than interpreting them. Pro tip: judges in the judicial branch judge what the law means.",
        },
        {
            "text": r"**Civics.** Which document begins with the words 'We the People' and serves as the supreme law of the United States?",
            "difficulty": 2,
            "choices": [("The U.S. Constitution", True),
                        ("The Declaration of Independence", False),
                        ("The Emancipation Proclamation", False),
                        ("The Gettysburg Address", False)],
            "explanation": r"The Constitution's Preamble begins 'We the People' and sets up the government. The trap, the Declaration of Independence (1776), announced separation from Britain. Pro tip: Constitution = rules of government; Declaration = the break from Britain.",
        },
        {
            "text": r"**Civics.** The first ten amendments to the U.S. Constitution are together known as the:",
            "difficulty": 1,
            "choices": [("Bill of Rights", True), ("Preamble", False),
                        ("Articles of Confederation", False), ("Federalist Papers", False)],
            "explanation": r"The first ten amendments are the Bill of Rights, protecting freedoms like speech and religion. The trap, the Federalist Papers, were essays arguing for the Constitution. Pro tip: 'first ten amendments' = Bill of Rights.",
        },
        {
            "text": (r"**Civics.** The President can veto a bill, but Congress can override that veto with a "
                     r"two-thirds vote. This is an example of:"),
            "difficulty": 2,
            "choices": [("Checks and balances", True), ("Federalism", False),
                        ("Free enterprise", False), ("Popular sovereignty", False)],
            "explanation": r"Each branch can limit the others (veto vs. override), which is checks and balances. The trap, federalism, is the split between national and state power. Pro tip: when branches limit each other, that's checks and balances.",
        },
        {
            "text": r"**Civics.** The sharing of power between the national government and the state governments is called:",
            "difficulty": 2,
            "choices": [("Federalism", True), ("Monarchy", False),
                        ("Dictatorship", False), ("Anarchy", False)],
            "explanation": r"Federalism divides power between national and state governments. The trap, monarchy, is rule by a king or queen. Pro tip: federalism = layered government, national and state sharing power.",
        },
        {
            "text": r"**Civics.** In a democracy, the power to govern ultimately comes from:",
            "difficulty": 1,
            "choices": [("The people, through voting", True),
                        ("A single royal family", False),
                        ("The military", False),
                        ("Foreign governments", False)],
            "explanation": r"In a democracy, citizens hold power and express it through voting. The trap, a royal family, describes a monarchy. Pro tip: democracy means 'rule by the people.'",
        },
        {
            "text": r"**Civics.** The freedom to express your opinions without government punishment is protected by the First Amendment as freedom of:",
            "difficulty": 2,
            "choices": [("Speech", True), ("Travel", False),
                        ("Taxation", False), ("Trade", False)],
            "explanation": r"The First Amendment protects freedom of speech, along with religion, press, and assembly. The trap, travel, is not a First Amendment freedom. Pro tip: the First Amendment guards speech, religion, press, assembly, and petition.",
        },
        {
            "text": r"**Civics.** Which of the following is a basic RESPONSIBILITY of citizens in a democracy?",
            "difficulty": 1,
            "choices": [("Voting in elections", True),
                        ("Owning a large house", False),
                        ("Serving as President", False),
                        ("Joining the army by force", False)],
            "explanation": r"Voting is a core civic responsibility that keeps a democracy working. The traps are personal choices or not required of everyone. Pro tip: participation like voting and jury duty keeps self-government running.",
        },
        {
            "text": ("**Civics.** Use the diagram.\n\n"
                     "[[figure:bill_to_law|How a bill becomes a law]]\n\n"
                     "Before a bill can become a federal law, it must first be passed by:"),
            "difficulty": 2,
            "choices": [("Both houses of Congress", True),
                        ("The Supreme Court", False),
                        ("State governors only", False),
                        ("The United Nations", False)],
            "explanation": r"A bill must pass both the House and the Senate, then be signed by the President. The trap, the Supreme Court, does not pass laws. Pro tip: a bill travels through both houses of Congress before reaching the President.",
        },
        {
            "text": r"**Civics.** The U.S. Congress is made up of two houses: the Senate and the:",
            "difficulty": 2,
            "choices": [("House of Representatives", True),
                        ("Supreme Court", False),
                        ("Cabinet", False),
                        ("Electoral College", False)],
            "explanation": r"Congress has two houses -- the Senate and the House of Representatives. The trap, the Supreme Court, is part of the judicial branch. Pro tip: a 'bicameral' legislature has two chambers: Senate and House.",
        },
        {
            "text": r"**Civics.** Dividing the government into separate branches with different jobs is called:",
            "difficulty": 2,
            "choices": [("Separation of powers", True),
                        ("Free trade", False),
                        ("Inflation", False),
                        ("Globalization", False)],
            "explanation": r"Separation of powers splits government into legislative, executive, and judicial branches. The trap, free trade, is an economic idea. Pro tip: separation of powers keeps any one branch from holding all the power.",
        },
        {
            "text": r"**Civics.** The Constitution can be changed over time through a formal process that adds:",
            "difficulty": 2,
            "choices": [("Amendments", True), ("Tariffs", False),
                        ("Vetoes", False), ("Treaties", False)],
            "explanation": r"Changes to the Constitution are added as amendments. The trap, tariffs, are taxes on imports, not constitutional changes. Pro tip: the Constitution is a living document, updated through amendments.",
        },
        {
            "text": r"**Civics.** A person becomes President of the United States by:",
            "difficulty": 1,
            "choices": [("Winning a national election", True),
                        ("Inheriting the office from a parent", False),
                        ("Being appointed by the Supreme Court", False),
                        ("Serving the longest in Congress", False)],
            "explanation": r"The President is chosen through a national election (and the Electoral College). The trap, inheriting the office, describes a monarchy. Pro tip: in the U.S., leaders are elected, not born into power.",
        },
        {
            "text": r"**Civics.** Serving on a jury when called is best described as a citizen's:",
            "difficulty": 2,
            "choices": [("Civic duty", True), ("Optional hobby", False),
                        ("Constitutional amendment", False), ("Economic right", False)],
            "explanation": r"Jury service is a civic duty that supports the justice system. The trap, optional hobby, understates that it is a responsibility. Pro tip: voting and jury duty are duties that keep democracy and justice working.",
        },
        {
            "text": r"**Civics.** The main purpose of holding regular, free elections is to:",
            "difficulty": 2,
            "choices": [("Let citizens choose and replace their leaders", True),
                        ("Raise money for the military", False),
                        ("Decide the price of goods", False),
                        ("Write new scientific laws", False)],
            "explanation": r"Elections let the people choose leaders and remove them peacefully. The trap, deciding prices, is an economic matter. Pro tip: elections give citizens regular control over who governs them.",
        },
        {
            "text": r"**Civics.** A government in which citizens elect representatives to make laws and decisions on their behalf is called a:",
            "difficulty": 2,
            "choices": [("Representative democracy (republic)", True),
                        ("Absolute monarchy", False),
                        ("Military dictatorship", False),
                        ("Theocracy", False)],
            "explanation": r"In a representative democracy, voters elect officials to govern for them. The trap, an absolute monarchy, is rule by a single hereditary ruler. Pro tip: the U.S. is a representative democracy -- citizens elect leaders rather than voting on every law themselves.",
        },
        # =====================================================================
        # =========================== U.S. HISTORY ============================
        # =====================================================================
        {
            "text": r"**U.S. History.** The American Revolution was fought mainly to gain independence from:",
            "difficulty": 1,
            "choices": [("Great Britain", True), ("France", False),
                        ("Mexico", False), ("Canada", False)],
            "explanation": r"The American Revolution won independence from Great Britain. The trap, France, actually helped the colonists against Britain. Pro tip: the colonies broke away from British rule in the Revolution.",
        },
        {
            "text": r"**U.S. History.** The American Civil War (1861-1865) was fought primarily over:",
            "difficulty": 2,
            "choices": [("Slavery and the survival of the Union", True),
                        ("A tax on imported tea", False),
                        ("Independence from Great Britain", False),
                        ("Women's right to vote", False)],
            "explanation": r"The Civil War centered on slavery and whether the Union would hold together. The traps belong to other eras. Pro tip: match the event to its time period to rule out wrong eras.",
        },
        {
            "text": r"**U.S. History.** In what year was the Declaration of Independence adopted?",
            "difficulty": 2,
            "choices": [("1776", True), ("1492", False),
                        ("1865", False), ("1945", False)],
            "explanation": r"The Declaration of Independence was adopted in 1776. The trap, 1492, is when Columbus reached the Americas. Pro tip: 1776 is the birth year of American independence.",
        },
        {
            "text": ("**U.S. History.** Use the timeline.\n\n"
                     "[[figure:us_timeline|A timeline of major U.S. events]]\n\n"
                     "The U.S. Constitution, which set up the current national government, was written in:"),
            "difficulty": 2,
            "choices": [("1787", True), ("1620", False),
                        ("1776", False), ("1929", False)],
            "explanation": r"The Constitution was written in 1787 and took effect in 1789. The trap, 1776, is the Declaration of Independence. Pro tip: Declaration first (1776), Constitution a decade later (1787).",
        },
        {
            "text": r"**U.S. History.** Dr. Martin Luther King Jr. is best known for his nonviolent leadership in the:",
            "difficulty": 1,
            "choices": [("Civil Rights Movement", True),
                        ("American Revolution", False),
                        ("Industrial Revolution", False),
                        ("Space Race", False)],
            "explanation": r"Dr. King led the Civil Rights Movement for racial equality through nonviolent protest. The trap, the American Revolution, came nearly 200 years earlier. Pro tip: King is linked to civil rights and the 1960s.",
        },
        {
            "text": r"**U.S. History.** The right of women to vote in the United States was guaranteed nationwide by an amendment passed in:",
            "difficulty": 2,
            "choices": [("1920", True), ("1776", False),
                        ("1620", False), ("2000", False)],
            "explanation": r"The 19th Amendment (1920) guaranteed women the right to vote. The trap, 1776, predates it by well over a century. Pro tip: women's suffrage came in 1920, long after independence.",
        },
        {
            "text": r"**U.S. History.** Millions of immigrants came to the United States in the late 1800s and early 1900s mainly seeking:",
            "difficulty": 2,
            "choices": [("Economic opportunity and a better life", True),
                        ("To start a war", False),
                        ("To avoid all forms of work", False),
                        ("To return immediately to Europe", False)],
            "explanation": r"Most immigrants came seeking jobs, freedom, and a better life. The trap 'to start a war' misreads their motives. Pro tip: opportunity and escape from hardship drove most immigration.",
        },
        # =====================================================================
        # ============================ ECONOMICS ==============================
        # =====================================================================
        {
            "text": ("**Economics.** Use the graph.\n\n"
                     "[[figure:supply_demand|Supply and demand curves for a good]]\n\n"
                     "According to the law of demand, as the price of a good rises, the quantity that "
                     "consumers want to buy usually:"),
            "difficulty": 2,
            "choices": [("Decreases", True), ("Increases", False),
                        ("Stays exactly the same", False), ("Doubles", False)],
            "explanation": r"The downward-sloping demand curve shows higher prices lead to lower quantity demanded. The trap 'increases' describes supply, not demand. Pro tip: demand slopes down -- as price rises, buyers want less.",
        },
        {
            "text": r"**Economics.** A tax that a government places on goods brought in from other countries is called a:",
            "difficulty": 2,
            "choices": [("Tariff", True), ("Subsidy", False),
                        ("Surplus", False), ("Deficit", False)],
            "explanation": r"A tariff is a tax on imports. The trap, a subsidy, is money the government gives to support a business. Pro tip: tariff = tax at the border on imported goods.",
        },
        {
            "text": r"**Economics.** The basic economic problem that there are unlimited wants but limited resources is called:",
            "difficulty": 2,
            "choices": [("Scarcity", True), ("Surplus", False),
                        ("Inflation", False), ("Democracy", False)],
            "explanation": r"Scarcity is the gap between unlimited wants and limited resources, forcing choices. The trap, surplus, is having more than enough. Pro tip: scarcity is why every economy must decide how to use limited resources.",
        },
        {
            "text": r"**Economics.** A business earns a profit when its total revenue is:",
            "difficulty": 1,
            "choices": [("Greater than its total costs", True),
                        ("Less than its total costs", False),
                        ("Exactly equal to zero", False),
                        ("Equal to the number of workers", False)],
            "explanation": r"Profit is revenue minus costs, so a profit means revenue is greater than costs. The trap 'less than its costs' would be a loss. Pro tip: profit = money in (revenue) minus money out (costs).",
        },
        {
            "text": r"**Economics.** Setting aside part of your income now to use later is called:",
            "difficulty": 1,
            "choices": [("Saving", True), ("Borrowing", False),
                        ("A tariff", False), ("Inflation", False)],
            "explanation": r"Saving is keeping income for future use. The trap, borrowing, is taking money you must repay. Pro tip: saving builds a cushion; borrowing creates debt you owe back.",
        },
        # =====================================================================
        # ====================== GEOGRAPHY & THE WORLD ========================
        # =====================================================================
        {
            "text": r"**Geography.** On a map, the lines that run east-west and measure distance north or south of the equator are called lines of:",
            "difficulty": 2,
            "choices": [("Latitude", True), ("Longitude", False),
                        ("Elevation", False), ("Population", False)],
            "explanation": r"Latitude lines run east-west and measure north-south position. The trap, longitude, runs north-south instead. Pro tip: latitude lines are like the flat rungs of a ladder, going up and down.",
        },
        {
            "text": r"**Geography.** The imaginary line at 0 degrees latitude that circles the middle of the Earth is the:",
            "difficulty": 1,
            "choices": [("Equator", True), ("Prime Meridian", False),
                        ("North Pole", False), ("Tropic of Cancer", False)],
            "explanation": r"The equator is 0 degrees latitude, dividing Earth into Northern and Southern Hemispheres. The trap, the Prime Meridian, is 0 degrees longitude. Pro tip: equator splits north and south; Prime Meridian splits east and west.",
        },
        {
            "text": r"**Geography.** On most maps, a small box that explains what the symbols and colors mean is called the:",
            "difficulty": 1,
            "choices": [("Legend (or key)", True), ("Equator", False),
                        ("Compass", False), ("Border", False)],
            "explanation": r"The legend, or key, explains the map's symbols and colors. The trap, the compass, shows direction (N, S, E, W). Pro tip: always read the legend before interpreting a map.",
        },
        {
            "text": r"**Geography.** A region with very little rainfall, sparse plant life, and sandy or rocky ground is best described as a:",
            "difficulty": 1,
            "choices": [("Desert", True), ("Rainforest", False),
                        ("Ocean", False), ("Glacier", False)],
            "explanation": r"A desert is a dry region with little rain and sparse vegetation. The trap, a rainforest, gets heavy rainfall instead. Pro tip: deserts are defined by low precipitation, not just heat.",
        },
        {
            "text": r"**Geography.** The way people change their surroundings -- such as building dams, clearing forests, or irrigating fields -- is an example of:",
            "difficulty": 2,
            "choices": [("Human-environment interaction", True),
                        ("Plate tectonics", False),
                        ("The water cycle", False),
                        ("A constitutional amendment", False)],
            "explanation": r"People altering their environment to meet their needs is human-environment interaction. The trap, plate tectonics, is a natural geologic process. Pro tip: this geography theme is about how humans and their environment shape each other.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the foundational (Level 1) full-length GED Social Studies practice exam (35 questions; MCQ only)."

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
            f"{course.questions.count()} questions (Civics, History, Economics, Geography)."
        ))
