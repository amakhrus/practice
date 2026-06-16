from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice

COURSE = {
    "title": "SAT Math: Algebra",
    "slug": "sat-math-algebra",
    "program": "SAT",
    "subject": "math",
    "description": "A focused deep-dive into the SAT Algebra domain. Master linear equations, functions, systems, inequalities, and word problems — the skills that appear most frequently on the SAT Math section. Each lesson pairs clear explanations with SAT-style worked examples so you can build both understanding and test-taking confidence.",
    "lessons": [
        (
            "Linear Equations in One Variable",
            "An equation is a statement that two expressions are equal. In a **linear equation in one variable**, the variable appears to the first power only — no exponents, no square roots.\n\n**Solving strategies by step count**\n\n- **One-step:** Undo a single operation. Example: x + 9 = 15 → subtract 9 from both sides → x = 6.\n- **Two-step:** Undo addition/subtraction first, then multiplication/division. Example: 2x - 4 = 10 → add 4 → 2x = 14 → divide by 2 → x = 7.\n- **Multi-step:** Distribute, combine **like terms**, then isolate the variable. Example: 3(x - 2) + x = 14 → 3x - 6 + x = 14 → 4x = 20 → x = 5.\n\n**Special solution types**\n\n- **No solution:** The variable cancels and you get a false statement (e.g., 5 = 3). The lines are parallel.\n- **Infinite solutions:** The variable cancels and you get a true statement (e.g., 4 = 4). The equations are identical.\n\n**SAT Example:** If 3x - 7 = 14, find x.\nAdd 7: 3x = 21. Divide by 3: x = 7.\n\n⚠️ Common mistake: Forgetting to distribute the negative sign — for example, -(x - 3) becomes -x + 3, not -x - 3.\n\n💡 Tip: After solving, substitute your answer back into the original equation to verify it is correct before moving on."
        ),
        (
            "Linear Functions and Slope",
            "A **linear function** produces a straight-line graph. The most useful form is **slope-intercept form**: y = mx + b, where **m** is the slope and **b** is the y-intercept.\n\n**Slope** measures steepness and direction: m = (y₂ - y₁) / (x₂ - x₁). It tells you how much y changes for each 1-unit increase in x.\n\n[[figure:slope_types|Types of slopes: positive, negative, zero, undefined]]\n\n- **Positive slope:** Line rises left to right.\n- **Negative slope:** Line falls left to right.\n- **Zero slope:** Horizontal line (y = constant).\n- **Undefined slope:** Vertical line (x = constant).\n\n**Point-slope form** is handy when you know one point (x₁, y₁) and the slope: y - y₁ = m(x - x₁).\n\n**Parallel and perpendicular lines**\n\n- **Parallel lines** share the same slope: m₁ = m₂.\n- **Perpendicular lines** have slopes that are **negative reciprocals**: m₁ × m₂ = -1.\n\n**Real-world context:** In y = 0.15x + 25, the slope 0.15 means cost increases $0.15 per mile, and the y-intercept 25 is the flat base fee.\n\n⚠️ Common mistake: Mixing up x and y in the slope formula — always subtract y-values in the numerator and x-values in the denominator.\n\n💡 Tip: Rewrite any linear equation in slope-intercept form first; the slope and intercept are then immediately visible."
        ),
        (
            "Systems of Linear Equations",
            "A **system of linear equations** is two or more equations considered simultaneously. The solution is the point (x, y) that satisfies all equations at once.\n\n**Substitution method**\n1. Isolate one variable in one equation.\n2. Substitute that expression into the other equation.\n3. Solve the resulting single-variable equation, then back-substitute.\n\n**Elimination (addition) method**\n1. Multiply one or both equations so a variable has equal and opposite coefficients.\n2. Add the equations to eliminate that variable.\n3. Solve for the remaining variable.\n\n**Graphical interpretation**\n\n- **One solution:** Lines intersect at exactly one point.\n- **No solution:** Lines are parallel (same slope, different y-intercept).\n- **Infinitely many solutions:** Lines are identical (same slope, same y-intercept).\n\n**Word problem example:** A store sells pens at $2 and notebooks at $5. A customer buys 8 items for $25. How many of each? Set up: p + n = 8 and 2p + 5n = 25. Solve to get p = 5, n = 3.\n\n⚠️ Common mistake: After using elimination, students sometimes forget to solve for the second variable — always find both x and y.\n\n💡 Tip: On the SAT, if a system question asks only for x + y (not individual values), look for a shortcut by adding or subtracting the two equations directly."
        ),
        (
            "Linear Inequalities",
            "A **linear inequality** is like an equation but uses <, >, ≤, or ≥ instead of =. Solving techniques mirror equation-solving with one critical difference.\n\n**Solving steps**\n1. Simplify each side (distribute, combine like terms).\n2. Isolate the variable using inverse operations.\n3. **Flip the inequality sign** whenever you multiply or divide both sides by a **negative number**.\n\n[[figure:linear_inequality_shade|Number line showing x > 3]]\n\n**Compound inequalities**\n\n- **AND (conjunction):** Both conditions must hold. Example: -2 < x ≤ 5. On a number line, shade the overlap.\n- **OR (disjunction):** At least one condition holds. Example: x < -1 or x > 4. Shade the union.\n\n**Interval notation**\n\n- Parenthesis ( ) for strict inequalities (< or >); bracket [ ] for inclusive (≤ or ≥).\n- Example: x > 3 → (3, ∞).\n\n**SAT-style example:** Which value satisfies 2x + 3 > 11?\n2x > 8 → x > 4. Only values greater than 4 work — check answer choices.\n\n**Graphing on the coordinate plane:** Shade the half-plane on the correct side of the boundary line; use a dashed line for strict inequalities.\n\n⚠️ Common mistake: Forgetting to flip the inequality sign when dividing by a negative — this is the most tested inequality rule on the SAT.\n\n💡 Tip: After solving an inequality, pick a test value from your solution set and plug it into the original inequality to confirm your answer."
        ),
        (
            "Word Problems with Linear Models",
            "Many SAT algebra questions describe real situations that you must translate into equations. The key skill is identifying the **variable**, the **rate**, and the **starting value**.\n\n**Translation guide**\n\n- \"is,\" \"equals,\" \"is the same as\" → =\n- \"more than,\" \"increased by\" → +\n- \"less than,\" \"decreased by\" → -\n- \"times,\" \"of,\" \"per\" → ×\n\n**Common linear model types**\n\n- **Rate × time = distance:** d = rt. If a train travels at 60 mph for t hours, d = 60t.\n- **Fixed cost + variable cost:** Total = base fee + (rate × quantity). A plumber charges $75 flat plus $50 per hour: C = 75 + 50h.\n- **Break-even analysis:** Set revenue equal to cost and solve. If Revenue = 20x and Cost = 8x + 360, then 20x = 8x + 360 → x = 30 units.\n\n**Step-by-step approach**\n1. Define the variable (let x = ...).\n2. Write the equation.\n3. Solve.\n4. Check that the answer makes sense in context (negative time is not realistic).\n\n⚠️ Common mistake: Translating \"5 less than x\" as 5 - x instead of x - 5. Order matters!\n\n💡 Tip: Underline the quantity each variable represents as you read; this prevents mixing up what x stands for midway through the problem."
        ),
        (
            "Interpreting Linear Expressions",
            "The SAT frequently asks what a specific **coefficient** or **constant** represents in a real-world equation, rather than asking you to solve for a variable.\n\n**Framework for interpretation**\n\nFor a linear model y = mx + b:\n- **m (slope / coefficient)** is the **rate of change** — how much y changes per one-unit increase in x.\n- **b (y-intercept / constant)** is the **initial value** — the value of y when x = 0.\n\n**SAT-style example:** In the equation C = 50 + 12n, what does 12 represent?\n- C is total cost, n is the number of items.\n- 12 is the coefficient of n → cost increases by $12 for each additional item.\n- 50 is the constant → $50 is the fixed starting cost regardless of quantity.\n\n**Units help you interpret:** If n is in hours and C is in dollars, then 12 has units of dollars per hour.\n\n**Common SAT variations**\n\n- \"What is the meaning of the number 50 in this context?\" → It is the value when n = 0 (initial cost, base fee, etc.).\n- \"By how much does C increase for each additional item?\" → The coefficient 12.\n- \"At what value of n does C equal zero?\" → Solve 50 + 12n = 0 (not always meaningful in context).\n\n⚠️ Common mistake: Confusing the coefficient (rate) with the constant (initial value) — always ask yourself which part changes and which part stays fixed.\n\n💡 Tip: Substitute x = 0 to find what the constant means, and substitute x = 1 vs x = 0 to find what the coefficient means as a change."
        ),
        (
            "SAT Algebra Strategy",
            "Knowing algebra is necessary but not sufficient — you also need smart **test-taking strategies** to maximize your score under time pressure.\n\n**Plugging in numbers**\nWhen a question has variables in the answer choices, assign a simple value to the variable (avoid 0 and 1), compute the target expression, then check which answer choice matches. This turns an abstract algebra problem into arithmetic.\n\n**Backsolving (working from answer choices)**\nWhen answer choices are numbers, plug each one back into the original equation or inequality. Start with B or C (middle values) to eliminate as many choices as possible fastest.\n\n**Process of elimination**\nEven partial knowledge helps. If you know x must be positive, eliminate all negative answer choices. If the answer must be an integer, eliminate fractions.\n\n**Time management tips**\n\n- **Easy questions first:** Skip any question that feels stuck after 60 seconds; return later.\n- **Mark and move:** Use the test's flagging feature to revisit skipped questions.\n- **Calculator vs. no-calculator:** On the no-calculator section, choose numbers that make arithmetic clean.\n\n**Common SAT algebra traps**\n\n- **Trap 1:** Solving for x when the question asks for 2x or x + 1.\n- **Trap 2:** Assuming a system has one solution when it might have none or infinitely many.\n- **Trap 3:** Forgetting that an absolute value equation can produce two solutions.\n- **Trap 4:** Misreading \"no solution\" as x = 0.\n\n⚠️ Common mistake: Rushing through setup and solving for the wrong quantity — read the final question carefully before calculating.\n\n💡 Tip: After you circle your answer, re-read the question one more time to confirm you answered what was actually asked."
        ),
    ],
    "mcqs": [
        # Lesson 1 — Linear Equations in One Variable (difficulty 1–5)
        {
            "text": "If 3x - 7 = 14, what is the value of x?",
            "difficulty": 1,
            "choices": [
                ("3", False),
                ("7", True),
                ("9", False),
                ("21", False),
            ],
            "explanation": "Add 7 to both sides: 3x = 21. Divide both sides by 3: x = 7.",
        },
        {
            "text": "Solve for x: 5x + 3 = 3x + 11",
            "difficulty": 2,
            "choices": [
                ("2", False),
                ("4", True),
                ("7", False),
                ("14", False),
            ],
            "explanation": "Subtract 3x from both sides: 2x + 3 = 11. Subtract 3: 2x = 8. Divide by 2: x = 4.",
        },
        {
            "text": "Which value of x makes the equation 4(x - 2) + 2 = 3x + 4 true?",
            "difficulty": 2,
            "choices": [
                ("4", False),
                ("6", False),
                ("8", False),
                ("10", True),
            ],
            "explanation": "Distribute: 4x - 8 + 2 = 3x + 4 → 4x - 6 = 3x + 4. Subtract 3x: x - 6 = 4. Add 6: x = 10. Verify: 4(10 - 2) + 2 = 32 + 2 = 34 and 3(10) + 4 = 34. Confirmed.",
        },
        {
            "text": "The equation 2(x + 5) = 2x + 10 has how many solutions?",
            "difficulty": 3,
            "choices": [
                ("No solution", False),
                ("Exactly one solution", False),
                ("Infinitely many solutions", True),
                ("Exactly two solutions", False),
            ],
            "explanation": "Distribute: 2x + 10 = 2x + 10. The variable terms cancel, leaving 10 = 10, which is always true. Therefore every real number is a solution — infinitely many solutions.",
        },
        # Lesson 2 — Linear Functions and Slope (difficulty cycling)
        {
            "text": "What is the slope of the line passing through the points (2, 5) and (6, 13)?",
            "difficulty": 1,
            "choices": [
                ("1", False),
                ("2", True),
                ("3", False),
                ("4", False),
            ],
            "explanation": "Slope = (13 - 5) / (6 - 2) = 8 / 4 = 2.",
        },
        {
            "text": "The equation of a line is y = -3x + 7. Which of the following lines is parallel to it?",
            "difficulty": 2,
            "choices": [
                ("y = 3x + 7", False),
                ("y = -3x - 4", True),
                ("y = (1/3)x + 7", False),
                ("y = -x + 7", False),
            ],
            "explanation": "Parallel lines have equal slopes. The given slope is -3. The line y = -3x - 4 also has slope -3, so it is parallel.",
        },
        {
            "text": "A line is perpendicular to y = 4x - 1. What is the slope of the perpendicular line?",
            "difficulty": 2,
            "choices": [
                ("4", False),
                ("-4", False),
                ("-1/4", True),
                ("1/4", False),
            ],
            "explanation": "Perpendicular slopes are negative reciprocals. The original slope is 4, so the perpendicular slope is -1/4.",
        },
        {
            "text": "In the function y = 2x + 6, what is the y-intercept?",
            "difficulty": 1,
            "choices": [
                ("2", False),
                ("3", False),
                ("6", True),
                ("12", False),
            ],
            "explanation": "In slope-intercept form y = mx + b, b is the y-intercept. Here b = 6.",
        },
        # Lesson 3 — Systems of Linear Equations
        {
            "text": "What is the solution to the system: x + y = 10 and x - y = 4?",
            "difficulty": 1,
            "choices": [
                ("x = 3, y = 7", False),
                ("x = 7, y = 3", True),
                ("x = 6, y = 4", False),
                ("x = 8, y = 2", False),
            ],
            "explanation": "Add the two equations: 2x = 14, so x = 7. Substitute back: 7 + y = 10, so y = 3.",
        },
        {
            "text": "The system 2x + 3y = 12 and 4x + 6y = 18 has how many solutions?",
            "difficulty": 3,
            "choices": [
                ("Infinitely many", False),
                ("Exactly one", False),
                ("No solution", True),
                ("Exactly two", False),
            ],
            "explanation": "Multiply the first equation by 2: 4x + 6y = 24. But the second equation says 4x + 6y = 18. Since 24 ≠ 18, there is no solution — the lines are parallel.",
        },
        {
            "text": "Using substitution, solve: y = 2x - 1 and 3x + y = 14. What is x?",
            "difficulty": 2,
            "choices": [
                ("2", False),
                ("3", True),
                ("4", False),
                ("5", False),
            ],
            "explanation": "Substitute y = 2x - 1 into 3x + y = 14: 3x + (2x - 1) = 14 → 5x - 1 = 14 → 5x = 15 → x = 3.",
        },
        {
            "text": "A cashier has 25 coins (nickels and dimes) totaling $1.90. How many dimes are there?",
            "difficulty": 4,
            "choices": [
                ("10", False),
                ("13", True),
                ("15", False),
                ("18", False),
            ],
            "explanation": "Let d = dimes, n = nickels. System: d + n = 25 and 10d + 5n = 190. From first equation, n = 25 - d. Substitute: 10d + 5(25 - d) = 190 → 10d + 125 - 5d = 190 → 5d = 65 → d = 13.",
        },
        # Lesson 4 — Linear Inequalities
        {
            "text": "Which value of x satisfies 2x + 3 > 11?",
            "difficulty": 1,
            "choices": [
                ("3", False),
                ("4", False),
                ("5", True),
                ("2", False),
            ],
            "explanation": "Solve: 2x + 3 > 11 → 2x > 8 → x > 4. Only x = 5 is greater than 4.",
        },
        {
            "text": "Solve the inequality: -3x + 6 ≤ 18. Which of the following is the solution set?",
            "difficulty": 2,
            "choices": [
                ("x ≤ -4", False),
                ("x ≥ -4", True),
                ("x ≤ 4", False),
                ("x ≥ 4", False),
            ],
            "explanation": "Subtract 6 from both sides: -3x ≤ 12. Divide both sides by -3 and flip the inequality sign: x ≥ -4.",
        },
        {
            "text": "Which compound inequality is equivalent to -1 < 3x - 4 < 11?",
            "difficulty": 3,
            "choices": [
                ("1 < x < 5", True),
                ("1 ≤ x ≤ 5", False),
                ("-5 < x < 1", False),
                ("x > 1", False),
            ],
            "explanation": "Add 4 to all parts: 3 < 3x < 15. Divide all parts by 3: 1 < x < 5.",
        },
        {
            "text": "In interval notation, what is the solution to 5 - 2x < 1?",
            "difficulty": 2,
            "choices": [
                ("(-∞, 2)", False),
                ("(2, ∞)", True),
                ("(-2, ∞)", False),
                ("(-∞, -2)", False),
            ],
            "explanation": "5 - 2x < 1 → -2x < -4 → divide by -2 and flip: x > 2. In interval notation: (2, ∞).",
        },
        # Lesson 5 — Word Problems with Linear Models
        {
            "text": "A plumber charges a flat fee of $75 plus $50 per hour. Which equation gives the total charge C for h hours of work?",
            "difficulty": 1,
            "choices": [
                ("C = 50h", False),
                ("C = 75h + 50", False),
                ("C = 75 + 50h", True),
                ("C = 125h", False),
            ],
            "explanation": "The flat fee is a constant (75), and the hourly rate (50) multiplies the hours (h). Total charge: C = 75 + 50h.",
        },
        {
            "text": "Two trains leave the same station traveling in opposite directions. One travels at 55 mph and the other at 45 mph. After how many hours will they be 300 miles apart?",
            "difficulty": 3,
            "choices": [
                ("2.5", False),
                ("3", True),
                ("3.5", False),
                ("4", False),
            ],
            "explanation": "Combined speed = 55 + 45 = 100 mph. Distance = rate × time: 300 = 100t → t = 3 hours.",
        },
        {
            "text": "A company sells widgets for $20 each. Their fixed costs are $360 and variable cost is $8 per widget. How many widgets must they sell to break even?",
            "difficulty": 3,
            "choices": [
                ("18", False),
                ("25", False),
                ("30", True),
                ("45", False),
            ],
            "explanation": "Break-even: Revenue = Cost → 20x = 8x + 360 → 12x = 360 → x = 30 widgets.",
        },
        {
            "text": "Maria is 5 years older than twice her brother's age. If her brother is b years old, which expression represents Maria's age?",
            "difficulty": 1,
            "choices": [
                ("2b - 5", False),
                ("5b + 2", False),
                ("2b + 5", True),
                ("b + 5", False),
            ],
            "explanation": "\"Twice her brother's age\" is 2b. \"5 years older\" means add 5. Maria's age = 2b + 5.",
        },
        {
            "text": "A car rental costs $30 per day plus $0.20 per mile. If Jenna's total bill was $78 for one day, how many miles did she drive?",
            "difficulty": 2,
            "choices": [
                ("180", False),
                ("200", False),
                ("240", True),
                ("390", False),
            ],
            "explanation": "78 = 30 + 0.20m → 48 = 0.20m → m = 240 miles.",
        },
        # Lesson 6 — Interpreting Linear Expressions
        {
            "text": "In the equation C = 50 + 12n, where C is total cost in dollars and n is the number of items purchased, what does 12 represent?",
            "difficulty": 1,
            "choices": [
                ("The total cost when no items are purchased", False),
                ("The cost per item", True),
                ("The number of items at break-even", False),
                ("The maximum number of items available", False),
            ],
            "explanation": "12 is the coefficient of n — it is the rate of change of cost. For each additional item purchased, the cost increases by $12.",
        },
        {
            "text": "The equation P = 1500 - 25t models the population P of a town t years after 2000. What does 1500 represent?",
            "difficulty": 1,
            "choices": [
                ("The rate at which the population decreases each year", False),
                ("The population in the year 2000", True),
                ("The year when the population reaches zero", False),
                ("The total population decrease over 25 years", False),
            ],
            "explanation": "When t = 0 (the year 2000), P = 1500. The constant 1500 is the initial population in year 2000.",
        },
        {
            "text": "In the equation d = 60t, which represents distance in miles and t time in hours, what are the units of 60?",
            "difficulty": 2,
            "choices": [
                ("Miles", False),
                ("Hours", False),
                ("Miles per hour", True),
                ("Hours per mile", False),
            ],
            "explanation": "Since d is in miles and t is in hours, 60 must have units of miles/hour so that miles = (miles/hour) × hours.",
        },
        {
            "text": "A phone plan charges a monthly fee plus a per-minute rate modeled by C = 15 + 0.05m. By how much does the cost increase for each additional 20 minutes of calls?",
            "difficulty": 2,
            "choices": [
                ("$0.05", False),
                ("$0.20", False),
                ("$1.00", True),
                ("$15.00", False),
            ],
            "explanation": "The per-minute rate is $0.05. For 20 minutes: 0.05 × 20 = $1.00 increase.",
        },
        {
            "text": "The equation T = 32 + 1.8C converts Celsius (C) to Fahrenheit (T). What does the coefficient 1.8 represent in this context?",
            "difficulty": 3,
            "choices": [
                ("The freezing point of water in Fahrenheit", False),
                ("The number of Fahrenheit degrees per 1 degree Celsius", True),
                ("The boiling point of water in Celsius", False),
                ("The difference between Fahrenheit and Celsius at 0 degrees", False),
            ],
            "explanation": "1.8 is the slope — the rate of change. For every 1-degree increase in Celsius, the Fahrenheit temperature increases by 1.8 degrees.",
        },
        # Lesson 7 — SAT Algebra Strategy
        {
            "text": "On the SAT, if 3x + 6 = 21, what is the value of x + 2?",
            "difficulty": 1,
            "choices": [
                ("3", False),
                ("5", False),
                ("7", True),
                ("9", False),
            ],
            "explanation": "Notice that 3x + 6 = 3(x + 2). So 3(x + 2) = 21, meaning x + 2 = 7. The common trap is solving for x first (x = 5) and stopping there — but the question asks for x + 2, not x.",
        },
        {
            "text": "The SAT asks: if 5y - 10 = 0, what is 2y? Which strategy is fastest here?",
            "difficulty": 2,
            "choices": [
                ("Graph both sides", False),
                ("Use a system of equations", False),
                ("Solve for y, then multiply by 2", True),
                ("Plug in answer choices", False),
            ],
            "explanation": "Solve directly: 5y = 10 → y = 2. Then 2y = 4. This direct algebraic approach is fastest for a simple linear equation.",
        },
        {
            "text": "Using backsolving: which answer satisfies 3x - 4 = 2x + 1?",
            "difficulty": 1,
            "choices": [
                ("3", False),
                ("4", False),
                ("5", True),
                ("6", False),
            ],
            "explanation": "Test x = 5: 3(5) - 4 = 11 and 2(5) + 1 = 11. Both sides equal 11, so x = 5 is correct. Backsolving confirmed the answer efficiently.",
        },
        {
            "text": "A student solves 2x + 4 = 18 and gets x = 7. The SAT question asks for the value of 4x + 8. What is the correct answer?",
            "difficulty": 2,
            "choices": [
                ("18", False),
                ("28", False),
                ("36", True),
                ("46", False),
            ],
            "explanation": "Notice 4x + 8 = 2(2x + 4) = 2(18) = 36. The shortcut is to recognize the expression as a multiple of the original equation, avoiding the need to find x separately.",
        },
    ],
}


class Command(BaseCommand):
    help = "Seed SAT Math: Algebra"

    def handle(self, *args, **options):
        course, _ = Course.objects.update_or_create(
            slug=COURSE["slug"],
            defaults={
                "title": COURSE["title"],
                "program": COURSE["program"],
                "subject": COURSE["subject"],
                "description": COURSE["description"],
            },
        )
        course.lessons.all().delete()
        for order, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=order)
        course.questions.all().delete()
        for item in COURSE["mcqs"]:
            q = Question.objects.create(
                course=course,
                text=item["text"],
                qtype="mcq",
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=q, text=text, is_correct=is_correct)
        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with {len(COURSE['lessons'])} lessons and {len(COURSE['mcqs'])} questions."
            )
        )
