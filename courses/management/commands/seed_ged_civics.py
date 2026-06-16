"""
Seed data: 'GED Social Studies: Civics & Government' -- a deep dive into the
largest content area on the GED Social Studies test (about half of it).

Goes well beyond the survey course: the foundations of American democracy, the
three branches in detail, the Constitution and federalism, the levels of
government, how a bill becomes a law, and elections and citizenship. Lessons use
intuition, diagrams, common-misconception warnings, and tips.

Run:
    python manage.py seed_ged_civics
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Civics & Government",
    "slug": "ged-civics-government",
    "program": "GED",
    "subject": "social",
    "description": (
        "Civics and Government is the largest part of the GED Social Studies test -- about half "
        "of the questions. This deep-dive course explains how American democracy is designed and "
        "why: its founding principles, the three branches, the Constitution and federalism, the "
        "levels of government, how laws are actually made, and how citizens take part."
    ),
    "lessons": [
        (
            "1. Foundations of American Democracy",
            "Before the rules, come the ideas. American government rests on a few big principles, "
            "many borrowed from Enlightenment thinkers, about where power should come from.\n\n"
            "- **Popular sovereignty** — government's power comes from the people. The people are the "
            "ultimate source of authority.\n"
            "- **Social contract** — people agree to give up some freedoms in exchange for "
            "government's protection of their rights. If government fails, the people may change it.\n"
            "- **Consent of the governed** — leaders rule only with the people's agreement, usually "
            "expressed through elections.\n"
            "- **Rule of law** — everyone, including leaders, must obey the law. No one is above it.\n"
            "- **Limited government** — government's power is restricted by law (the Constitution) to "
            "protect individual rights.\n\n"
            "The **Declaration of Independence (1776)** put these ideas into famous words: that people "
            "have rights to 'life, liberty, and the pursuit of happiness', and that governments get "
            "their 'just powers from the consent of the governed'.\n\n"
            "⚠️ Common misconception: a democracy does not mean the people vote on every decision. The "
            "U.S. is a **representative democracy** (a republic) — citizens elect officials to make "
            "decisions for them.\n\n"
            "💡 Tip: when you see 'power comes from the people', think **popular sovereignty**; when "
            "you see 'no one is above the law', think **rule of law**.",
        ),
        (
            "2. The Three Branches in Depth",
            "To stop any one person or group from gaining too much power, the Constitution splits the "
            "federal government into three branches — **separation of powers** — and lets each one "
            "limit the others through **checks and balances**.\n\n"
            "[[figure:three_branches|Each branch has a distinct job and can check the power of the "
            "other two.]]\n\n"
            "- **Legislative (Congress)** makes laws. It has two houses: the **House of "
            "Representatives** (seats based on each state's population) and the **Senate** (two per "
            "state). It also controls government spending and can declare war.\n"
            "- **Executive (the President)** carries out laws, commands the military, and conducts "
            "foreign policy. It includes the Cabinet and federal agencies.\n"
            "- **Judicial (the courts)** interprets laws and the Constitution. The **Supreme Court** "
            "is the highest court and can declare laws or actions **unconstitutional**.\n\n"
            "Examples of checks and balances:\n\n"
            "- The President can **veto** a bill; Congress can **override** a veto with a two-thirds "
            "vote.\n"
            "- The Senate must **approve** the President's treaties and major appointments.\n"
            "- The courts can strike down a law as **unconstitutional**.\n\n"
            "⚠️ Common misconception: the Supreme Court does not write laws. It judges whether laws "
            "follow the Constitution.\n\n"
            "💡 Tip: 'makes / enforces / interprets' = Legislative / Executive / Judicial. Lock that "
            "trio in.",
        ),
        (
            "3. The Constitution, Federalism & Rights",
            "The **Constitution (1787)** is the supreme law of the land. It opens with the "
            "**Preamble** ('We the People...'), sets up the three branches, and explains how power is "
            "divided and limited.\n\n"
            "A central design is **federalism** — power shared between the **national** government and "
            "the **states**:\n\n"
            "- **Federal powers**: print money, declare war, regulate trade between states, run the "
            "postal service.\n"
            "- **State powers**: run schools, hold elections, issue licenses, set up local "
            "governments.\n"
            "- **Shared powers**: collect taxes, build roads, make and enforce laws.\n\n"
            "The Constitution can be **amended** (changed). The first ten amendments are the **Bill of "
            "Rights**, protecting freedoms such as speech, religion, and the press (1st), the right to "
            "a fair trial, and protection from unreasonable searches (4th). Later amendments expanded "
            "rights — ending slavery (13th) and protecting voting rights (15th, 19th, 26th).\n\n"
            "⚠️ Common misconception: amending the Constitution is hard on purpose. It takes a "
            "two-thirds vote of Congress and approval by three-fourths of the states.\n\n"
            "💡 Tip: 'Bill of Rights = first 10 amendments' and 'federalism = shared national/state "
            "power' are two of the most tested facts.",
        ),
        (
            "4. Levels of Government: Federal, State & Local",
            "Government in the U.S. operates on **three levels**, each handling different parts of "
            "daily life. Many share a similar three-branch shape.\n\n"
            "- **Federal (national)** — based in Washington, D.C. Handles things that affect the whole "
            "country: national defense, foreign policy, money, and trade between states. Led by the "
            "President and Congress.\n"
            "- **State** — each state has its own constitution, governor, legislature, and courts. "
            "Handles education, state highways, driver's licenses, and elections.\n"
            "- **Local** — counties, cities, and towns. Handles police and fire departments, public "
            "schools, garbage collection, parks, and zoning. Led by mayors, city councils, and "
            "school boards.\n\n"
            "When a state law and a federal law conflict, federal law generally wins (the "
            "Constitution is the 'supreme law of the land'). But states keep broad power over local "
            "matters.\n\n"
            "⚠️ Common misconception: the President does not run your local schools or police. Those "
            "are handled by state and local governments.\n\n"
            "💡 Tip: match the problem to the level — a pothole is local, a driver's license is state, "
            "and a war is federal.",
        ),
        (
            "5. How a Bill Becomes a Law",
            "Most laws follow a clear path through Congress. Understanding it shows checks and "
            "balances in action.\n\n"
            "[[figure:bill_to_law|A bill must pass both houses of Congress and be signed by the "
            "President before it becomes law.]]\n\n"
            "The basic steps:\n\n"
            "- A member of Congress **introduces** a bill.\n"
            "- A **committee** studies, debates, and often revises it. Many bills die here.\n"
            "- **Both the House and the Senate** debate and vote. The bill must pass both.\n"
            "- The **President** signs it into law — or **vetoes** it.\n"
            "- If vetoed, Congress can still **override** the veto with a two-thirds vote in both "
            "houses, and the bill becomes law anyway.\n\n"
            "This process is deliberately slow and full of checkpoints. That makes new laws hard to "
            "pass — which the founders saw as a feature, not a bug, because it forces compromise.\n\n"
            "⚠️ Common misconception: the President cannot pass a law alone. Only Congress can pass "
            "legislation; the President signs or vetoes it.\n\n"
            "💡 Tip: remember the two musts — a bill must pass **both houses** and get the President's "
            "signature (or a veto override).",
        ),
        (
            "6. Elections, Parties & the Citizen's Role",
            "In a representative democracy, citizens shape government mainly by **choosing leaders** "
            "in elections — and by staying involved between them.\n\n"
            "**Political parties** are groups that share goals and run candidates for office. The U.S. "
            "mostly has two major parties, but anyone can form or join others. **Interest groups** "
            "also organize people around specific causes and try to influence policy.\n\n"
            "A few election ideas the GED tests:\n\n"
            "- Most U.S. elections are decided by **majority or plurality** vote.\n"
            "- The President is chosen through the **Electoral College**, not a direct national "
            "popular vote.\n"
            "- Citizens 18 and older have the **right to vote**; many amendments expanded who can.\n\n"
            "Beyond voting, citizens participate by contacting officials, joining peaceful protests, "
            "signing petitions, volunteering, serving on juries, and running for office. A healthy "
            "democracy depends on an **informed, active citizenry**.\n\n"
            "⚠️ Common misconception: the President is not chosen purely by the national popular vote — "
            "the Electoral College determines the winner.\n\n"
            "💡 Tip: if a question asks how citizens influence government, favor **active** answers "
            "(voting, petitioning, contacting officials) over passive ones.",
        ),
    ],
    "mcqs": [
        {
            "text": "The principle that government's power comes from the people is called:",
            "difficulty": 2,
            "choices": [("Popular sovereignty", True), ("Federalism", False),
                        ("Judicial review", False), ("Separation of powers", False)],
            "explanation": "Popular sovereignty means the people are the ultimate source of the government's authority, usually expressed through elections.",
        },
        {
            "text": "Which document declared that governments get their 'just powers from the consent of the governed'?",
            "difficulty": 2,
            "choices": [("The Declaration of Independence", True), ("The Bill of Rights", False),
                        ("The Articles of Confederation", False), ("The Emancipation Proclamation", False)],
            "explanation": "The Declaration of Independence (1776) stated this core idea of self-government.",
        },
        {
            "text": "The United States is best described as a:",
            "difficulty": 2,
            "choices": [("Representative democracy (republic)", True), ("Direct democracy", False),
                        ("Monarchy", False), ("Dictatorship", False)],
            "explanation": "Citizens elect representatives to make decisions for them, which makes the U.S. a representative democracy, not a direct one where everyone votes on every issue.",
        },
        {
            "text": "Which branch of government can declare a law unconstitutional?",
            "difficulty": 2,
            "choices": [("The judicial branch", True), ("The legislative branch", False),
                        ("The executive branch", False), ("The state governors", False)],
            "explanation": "The judicial branch — especially the Supreme Court — interprets the Constitution and can strike down laws that violate it.",
        },
        {
            "text": "How can Congress respond when the President vetoes a bill?",
            "difficulty": 3,
            "choices": [("Override the veto with a two-thirds vote in both houses", True),
                        ("Ask the Supreme Court to sign the bill", False),
                        ("Hold a national popular vote", False),
                        ("Nothing; a veto is always final", False)],
            "explanation": "Congress can override a presidential veto with a two-thirds vote in both the House and Senate — a key check on executive power.",
        },
        {
            "text": "Two houses make up the U.S. Congress. They are the:",
            "difficulty": 1,
            "choices": [("House of Representatives and the Senate", True),
                        ("Supreme Court and the Cabinet", False),
                        ("House and the Electoral College", False),
                        ("Senate and the Presidency", False)],
            "explanation": "Congress is bicameral: the House of Representatives (based on population) and the Senate (two per state).",
        },
        {
            "text": "The sharing of power between the national government and the states is called:",
            "difficulty": 2,
            "choices": [("Federalism", True), ("Popular sovereignty", False),
                        ("Checks and balances", False), ("Impeachment", False)],
            "explanation": "Federalism divides power between the federal (national) government and the state governments.",
        },
        {
            "text": "Which of these is mainly a responsibility of LOCAL government?",
            "difficulty": 2,
            "choices": [("Running public schools and police departments", True),
                        ("Declaring war", False),
                        ("Printing the nation's money", False),
                        ("Making treaties with other countries", False)],
            "explanation": "Local governments handle day-to-day services like schools, police, fire, and garbage collection. War, money, and treaties are federal powers.",
        },
        {
            "text": "Before a bill can become a federal law, it must:",
            "difficulty": 2,
            "choices": [("Pass both the House and the Senate", True),
                        ("Be approved by the Supreme Court", False),
                        ("Win a national popular vote", False),
                        ("Be signed by all 50 governors", False)],
            "explanation": "A bill must pass both houses of Congress and then be signed by the President (or have a veto overridden) to become law.",
        },
        {
            "text": "Which is one of the first ten amendments to the Constitution?",
            "difficulty": 2,
            "choices": [("Freedom of speech (1st Amendment)", True),
                        ("The creation of the Electoral College", False),
                        ("The two-term limit on presidents", False),
                        ("The income tax", False)],
            "explanation": "Freedom of speech is in the 1st Amendment, part of the Bill of Rights (the first ten amendments).",
        },
        {
            "text": "The President of the United States is officially chosen by the:",
            "difficulty": 3,
            "choices": [("Electoral College", True), ("national popular vote alone", False),
                        ("Supreme Court", False), ("Senate", False)],
            "explanation": "Although citizens vote, the Electoral College officially elects the President, which is why the popular-vote winner does not always win.",
        },
        {
            "text": "Which of the following is the MOST active way for a citizen to influence who governs?",
            "difficulty": 1,
            "choices": [("Voting in elections", True), ("Paying taxes", False),
                        ("Obeying laws", False), ("Watching the news", False)],
            "explanation": "Voting directly determines who holds office. The others are duties or activities but do not directly choose leaders.",
        },
    ],
    "essays": [
        {
            "text": ("Explain the principle of 'separation of powers' and how 'checks and balances' "
                     "protects against the abuse of power. Name the three branches and their main "
                     "jobs, and give at least two specific examples of one branch checking another."),
            "difficulty": 3,
            "rubric": ("Full marks for: (1) defining separation of powers as dividing government into "
                       "three branches; (2) naming legislative (makes laws), executive (enforces laws), "
                       "and judicial (interprets laws); (3) explaining checks and balances lets each "
                       "branch limit the others; (4) at least two correct examples (veto, veto "
                       "override, Senate approval of appointments/treaties, courts ruling laws "
                       "unconstitutional, impeachment). Deduct for a missing branch, wrong job, or "
                       "fewer than two valid examples."),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the 'GED Social Studies: Civics & Government' deep-dive course."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent
        course = Course.objects.create(
            title=COURSE["title"], slug=COURSE["slug"], program=COURSE["program"],
            subject=COURSE["subject"], description=COURSE["description"],
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
