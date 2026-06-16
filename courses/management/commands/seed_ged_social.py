"""
Seed data: 'GED Social Studies' -- the fourth GED subject, built comprehensively.

Covers the four content areas the test weights most: Civics & Government (the
largest), U.S. History, Economics, and Geography -- plus the core skill of
reading and judging social-studies sources and data. Lessons lead with intuition
and real-world hooks, include diagrams (the three branches, supply & demand), a
common-misconception warning, and a quick tip. Practice mirrors the GED style,
including source- and data-based questions.

Run:
    python manage.py seed_ged_social
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies",
    "slug": "ged-social-studies",
    "program": "GED",
    "subject": "social",
    "description": (
        "Social Studies on the GED is about how people govern themselves, share a past, run an "
        "economy, and live on the land. This course covers the four tested areas -- Civics & "
        "Government, U.S. History, Economics, and Geography -- and teaches the reasoning skill at "
        "the heart of the test: reading sources, maps, and data, and telling evidence from opinion."
    ),
    "lessons": [
        (
            "1. How the U.S. Government Is Structured",
            "The people who designed the U.S. government feared putting too much power in one "
            "place. Their solution was to split power into **three branches**, each with a different "
            "job, so that no single branch could control everything.\n\n"
            "[[figure:three_branches|Power is divided three ways, and each branch can limit the "
            "other two.]]\n\n"
            "- **Legislative branch (Congress)** — **makes** the laws. It has two houses: the House "
            "of Representatives and the Senate.\n"
            "- **Executive branch (the President)** — **carries out / enforces** the laws.\n"
            "- **Judicial branch (the courts)** — **interprets** the laws and decides what they mean.\n\n"
            "This design is called **separation of powers**. To keep any branch from growing too "
            "strong, each can check the others — a system of **checks and balances**. For example, "
            "Congress passes a bill, but the President can **veto** it; the Supreme Court can rule a "
            "law **unconstitutional**; and Congress can **impeach** officials.\n\n"
            "⚠️ Common misconception: the President does not make laws. The President can propose and "
            "sign or veto them, but only Congress writes and passes laws.\n\n"
            "💡 Tip: remember the verbs — Legislative **makes**, Executive **enforces**, Judicial "
            "**interprets**. Match the verb to the branch.",
        ),
        (
            "2. The Constitution & the Bill of Rights",
            "The **Constitution** is the supreme law of the United States — the rulebook that sets up "
            "the government and limits its power. When it was written in 1787, it replaced the weaker "
            "Articles of Confederation.\n\n"
            "A key idea is **federalism**: power is **shared** between the national (federal) "
            "government and the state governments. Some powers belong to the nation (printing money, "
            "declaring war), some to the states, and some to both.\n\n"
            "The Constitution can be changed through **amendments**. The first ten amendments are the "
            "**Bill of Rights**, which protects individual freedoms, including:\n\n"
            "- **1st Amendment** — freedom of speech, religion, press, assembly, and petition.\n"
            "- **4th Amendment** — protection from unreasonable searches.\n"
            "- **5th Amendment** — rights of the accused (such as not testifying against yourself).\n\n"
            "Later amendments expanded democracy — for example, ending slavery (13th) and protecting "
            "the right to vote regardless of race (15th) or sex (19th).\n\n"
            "⚠️ Common misconception: rights are not unlimited. Free speech, for instance, does not "
            "protect speech that causes serious, direct harm.\n\n"
            "💡 Tip: 'Bill of Rights = first 10 amendments' is one of the most tested facts. Lock it in.",
        ),
        (
            "3. Citizenship & Civic Participation",
            "A **democracy** only works when citizens take part. In the United States, government "
            "power ultimately comes from the people, who express their will mainly through **voting**.\n\n"
            "Citizens have both **rights** and **responsibilities**:\n\n"
            "- **Rights** — to vote, to speak freely, to a fair trial, to equal protection under the law.\n"
            "- **Responsibilities** — to obey laws, pay taxes, serve on juries, and stay informed.\n\n"
            "People also shape government **between** elections — by contacting representatives, "
            "joining peaceful protests, signing petitions, volunteering, and running for office. "
            "**Political parties** and **interest groups** organize people around shared goals.\n\n"
            "Voting matters at every level: national elections choose the President and Congress, but "
            "state and local elections decide schools, police, roads, and taxes that affect daily "
            "life most directly.\n\n"
            "⚠️ Common misconception: local elections are not 'less important'. Local government often "
            "has the most direct effect on your everyday life.\n\n"
            "💡 Tip: if a question asks how citizens can influence government, look for active answers — "
            "voting, petitioning, protesting — not just 'paying taxes'.",
        ),
        (
            "4. Key Themes in U.S. History",
            "You don't need to memorize every date, but you should know the big turning points and "
            "what they changed.\n\n"
            "- **Colonization & Independence (1600s–1776):** thirteen British colonies grew, then "
            "declared independence in the **Declaration of Independence (1776)**, arguing that "
            "government must protect rights and rests on the consent of the governed.\n"
            "- **A New Nation (1780s):** after winning the Revolution, the states wrote the "
            "**Constitution** to build a stronger national government.\n"
            "- **Civil War & Reconstruction (1861–1877):** disputes over slavery and states' rights "
            "split the country. The Union won, slavery ended, and new amendments expanded rights.\n"
            "- **Industrialization & Immigration (late 1800s):** factories, railroads, and waves of "
            "immigrants transformed the economy and cities.\n"
            "- **Civil Rights Movement (1950s–1960s):** Americans organized to end legal segregation "
            "and win equal rights, leading to laws like the Civil Rights Act of 1964.\n\n"
            "A repeating theme: the meaning of 'liberty and equality' has expanded over time to "
            "include more and more people.\n\n"
            "⚠️ Common misconception: the Declaration of Independence (1776) and the Constitution "
            "(1787) are different documents written years apart — don't mix them up.\n\n"
            "💡 Tip: for each era, remember the **cause** and the **effect**. The GED loves "
            "cause-and-effect questions.",
        ),
        (
            "5. Economics Basics",
            "Economics is the study of how people use limited resources to meet unlimited wants. "
            "Because resources are **scarce**, every choice has a trade-off, and the value of what you "
            "give up is the **opportunity cost**.\n\n"
            "In a market economy, prices are set by **supply** and **demand**:\n\n"
            "- **Demand** — how much buyers want at each price. As price rises, demand usually falls "
            "(the downward line).\n"
            "- **Supply** — how much sellers offer at each price. As price rises, supply usually rises "
            "(the upward line).\n\n"
            "[[figure:supply_demand|Where supply and demand cross is the equilibrium — the price at "
            "which the amount offered equals the amount wanted.]]\n\n"
            "Where the two lines cross is the **equilibrium price**. If something becomes scarce (a "
            "frost ruins the orange crop), supply drops and prices rise. If a product becomes popular, "
            "demand rises and prices climb too.\n\n"
            "⚠️ Common misconception: 'supply' and 'demand' are not the same as 'how much exists'. "
            "They describe amounts **at each price**, which is why a graph shows lines, not single dots.\n\n"
            "💡 Tip: scarce + wanted = higher price; plentiful + unwanted = lower price.",
        ),
        (
            "6. Geography & the World",
            "**Geography** studies the Earth's surface and how people interact with it. Two big "
            "branches: **physical geography** (landforms, climate, rivers, oceans) and **human "
            "geography** (where people live, how they move, and how they use the land).\n\n"
            "To read a map, use its tools:\n\n"
            "- The **compass rose** shows direction (North, South, East, West).\n"
            "- The **key (legend)** explains what the symbols and colors mean.\n"
            "- The **scale** shows how map distance relates to real distance.\n\n"
            "Geography shapes history and economics. Rivers and harbors helped cities grow and trade; "
            "mountains and deserts isolated peoples; fertile land supported farming. People also "
            "change the environment — building dams, clearing forests, and creating pollution.\n\n"
            "**Movement** of people (migration) and goods (trade) constantly reshapes the world, "
            "spreading languages, foods, religions, and ideas.\n\n"
            "⚠️ Common misconception: geography is more than memorizing place names. The GED asks how "
            "physical features **affect** how and where people live.\n\n"
            "💡 Tip: on any map question, read the **key** and **scale** first — they usually contain "
            "the answer.",
        ),
        (
            "7. Reading Social Studies Sources & Data",
            "The GED Social Studies test is really a **reasoning** test. You'll read documents, "
            "quotes, maps, cartoons, and graphs, and answer questions about them.\n\n"
            "Know your sources:\n\n"
            "- A **primary source** comes from the time being studied — a letter, a speech, a photo, "
            "a law (for example, the Declaration of Independence itself).\n"
            "- A **secondary source** was made later by someone analyzing events — a textbook or a "
            "historian's article.\n\n"
            "When you read a source, ask **who** made it, **when**, and **why**. Every source has a "
            "point of view, and authors may show **bias** — presenting only one side. Loaded, "
            "emotional language is a clue that a source is trying to persuade, not just inform.\n\n"
            "For graphs and tables, do what you did in math: read the **title**, the **labels**, and "
            "the **units**; find the **trend**; and use only what the data actually shows. Remember "
            "that **correlation is not causation**.\n\n"
            "⚠️ Common misconception: a source being 'official' or old does not make it unbiased. "
            "Always consider the author's purpose.\n\n"
            "💡 Tip: separate **fact** (checkable) from **opinion** (a judgment). The strongest answers "
            "are supported directly by the source.",
        ),
    ],
    "mcqs": [
        {
            "text": "Which branch of the U.S. government is responsible for making laws?",
            "difficulty": 1,
            "choices": [("The legislative branch (Congress)", True),
                        ("The executive branch (the President)", False),
                        ("The judicial branch (the courts)", False),
                        ("The state governments only", False)],
            "explanation": "Congress — the legislative branch — writes and passes laws. The executive enforces them and the judicial branch interprets them.",
        },
        {
            "text": "The President refuses to sign a bill passed by Congress, sending it back. This power is called:",
            "difficulty": 2,
            "choices": [("A veto", True), ("An impeachment", False),
                        ("A filibuster", False), ("An amendment", False)],
            "explanation": "The veto is the President's power to reject a bill. It is a classic example of checks and balances between the executive and legislative branches.",
        },
        {
            "text": "What are the first ten amendments to the Constitution known as?",
            "difficulty": 1,
            "choices": [("The Bill of Rights", True), ("The Declaration of Independence", False),
                        ("The Articles of Confederation", False), ("The Preamble", False)],
            "explanation": "The first ten amendments are the Bill of Rights, which protect individual freedoms such as speech and religion.",
        },
        {
            "text": "Which freedom is protected by the First Amendment?",
            "difficulty": 2,
            "choices": [("Freedom of speech", True), ("The right to a jury trial", False),
                        ("Protection from unreasonable searches", False), ("The right to vote at age 18", False)],
            "explanation": "The First Amendment protects freedom of speech, religion, press, assembly, and petition. The others are covered by different amendments.",
        },
        {
            "text": "The sharing of power between the national government and the state governments is called:",
            "difficulty": 2,
            "choices": [("Federalism", True), ("Separation of powers", False),
                        ("Capitalism", False), ("Democracy", False)],
            "explanation": "Federalism divides power between the federal and state governments. (Separation of powers divides power among the three branches.)",
        },
        {
            "text": "Which of the following is the most direct way for a citizen to influence who holds public office?",
            "difficulty": 1,
            "choices": [("Voting in elections", True), ("Paying sales tax", False),
                        ("Obeying traffic laws", False), ("Reading the news", False)],
            "explanation": "Voting is the most direct way citizens choose their representatives. The others are civic duties or activities but don't directly select officials.",
        },
        {
            "text": ("The Declaration of Independence (1776) argued that governments get their authority "
                     "from the 'consent of the governed.' This idea means that:"),
            "difficulty": 3,
            "choices": [("Government's power comes from the people it governs", True),
                        ("Only a king can rule a country", False),
                        ("Citizens must always obey without question", False),
                        ("States should have no government at all", False)],
            "explanation": "'Consent of the governed' means legitimate government power comes from the people — a foundational idea of American democracy.",
        },
        {
            "text": "Which conflict led to the end of slavery in the United States and the addition of new amendments expanding rights?",
            "difficulty": 2,
            "choices": [("The Civil War", True), ("The Revolutionary War", False),
                        ("World War I", False), ("The War of 1812", False)],
            "explanation": "The Civil War (1861–1865) ended slavery, followed by the 13th, 14th, and 15th Amendments during Reconstruction.",
        },
        {
            "text": "In a market, the price at which the amount supplied equals the amount demanded is called the:",
            "difficulty": 2,
            "choices": [("Equilibrium price", True), ("Opportunity cost", False),
                        ("Surplus", False), ("Tax rate", False)],
            "explanation": "Equilibrium is where the supply and demand curves cross — the quantity offered equals the quantity wanted.",
        },
        {
            "text": "A frost destroys much of the orange crop, so far fewer oranges are available. According to supply and demand, what will most likely happen to the price of oranges?",
            "difficulty": 2,
            "choices": [("It will rise", True), ("It will fall", False),
                        ("It will stay exactly the same", False), ("Oranges will become free", False)],
            "explanation": "When supply drops but people still want oranges, the now-scarce oranges become more expensive — the price rises.",
        },
        {
            "text": "On a map, which feature explains what the symbols and colors mean?",
            "difficulty": 1,
            "choices": [("The key (legend)", True), ("The compass rose", False),
                        ("The title", False), ("The scale", False)],
            "explanation": "The key (or legend) defines the map's symbols and colors. The compass rose shows direction and the scale shows distance.",
        },
        {
            "text": "Which of the following is a PRIMARY source about the American Revolution?",
            "difficulty": 2,
            "choices": [("A letter written by a soldier during the war in 1777", True),
                        ("A textbook chapter written in 2020", False),
                        ("A documentary made last year", False),
                        ("An encyclopedia article about the war", False)],
            "explanation": "A primary source comes from the time being studied — like a soldier's 1777 letter. Textbooks, documentaries, and encyclopedias are secondary sources made later.",
        },
        {
            "text": ("A political pamphlet says: 'Only a fool would support this reckless, dangerous "
                     "policy.' This loaded language is a clue that the source is mainly trying to:"),
            "difficulty": 3,
            "choices": [("Persuade the reader to take a side", True),
                        ("Present neutral, balanced facts", False),
                        ("Report data without opinion", False),
                        ("Teach geography", False)],
            "explanation": "Emotional, loaded words like 'fool', 'reckless', and 'dangerous' signal a persuasive purpose and bias, not neutral information.",
        },
    ],
    "essays": [
        {
            "text": ("Explain how the system of checks and balances limits the power of government. In "
                     "your answer, name the three branches, state the main job of each, and give at "
                     "least two specific examples of one branch checking another."),
            "difficulty": 3,
            "rubric": ("Full marks for: (1) naming the legislative (makes laws), executive (enforces "
                       "laws), and judicial (interprets laws) branches with their jobs; (2) explaining "
                       "that checks and balances let each branch limit the others to prevent too much "
                       "power in one place; (3) at least two correct examples (e.g., the President can "
                       "veto a bill; the Supreme Court can rule a law unconstitutional; Congress can "
                       "impeach officials or override a veto). Deduct for missing a branch, a wrong job, "
                       "or fewer than two valid examples."),
        },
        {
            "text": ("Some people argue that voting in local elections matters just as much as voting "
                     "in national ones. Write a short, well-organized response that states a clear "
                     "position and supports it with specific reasons and examples about how local "
                     "government affects daily life."),
            "difficulty": 3,
            "rubric": ("Score for: (1) a clear thesis taking a position; (2) specific, relevant support "
                       "(e.g., local government decides schools, police, roads, zoning, and local taxes "
                       "that directly affect daily life); (3) organization with an introduction, body, "
                       "and conclusion; and (4) correct grammar and clear writing. Deduct for vague "
                       "support, no clear position, or disorganized structure."),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the comprehensive 'GED Social Studies' course."

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
