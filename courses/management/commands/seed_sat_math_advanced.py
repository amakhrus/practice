from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice

COURSE = {
    "title": "SAT Math: Advanced Math",
    "slug": "sat-math-advanced-math",
    "program": "SAT",
    "subject": "math",
    "description": "A focused deep-dive into the SAT Advanced Math domain, covering quadratic equations, polynomial operations, radicals, rational expressions, exponential functions, and function transformations.",
    "lessons": [
        (
            "Quadratic Equations",
            "A **quadratic equation** is any equation of the form ax² + bx + c = 0, where a ≠ 0. Mastering quadratics is essential for SAT success because they appear in nearly every math section.\n\n**Factoring** is the fastest method when it works. To factor x² + 5x + 6 = 0, find two numbers that multiply to 6 and add to 5: those are 2 and 3, giving (x + 2)(x + 3) = 0, so x = -2 or x = -3.\n\nThe **quadratic formula** works for any quadratic: x = (-b ± √(b² - 4ac)) / (2a). Memorize this formula. For 2x² - 3x - 2 = 0, plug in a = 2, b = -3, c = -2 and simplify carefully.\n\n**Completing the square** rewrites ax² + bx + c in vertex form. Add and subtract (b/2a)² to both sides. This technique also reveals the vertex of the corresponding parabola.\n\nThe **discriminant** (b² - 4ac) tells you how many real solutions exist:\n- b² - 4ac > 0 → two distinct real solutions\n- b² - 4ac = 0 → exactly one real solution (a repeated root)\n- b² - 4ac < 0 → no real solutions (complex roots)\n\n⚠️ Common mistake: forgetting the ± in the quadratic formula, which causes you to find only one solution instead of two.\n\n💡 Tip: Always check your factored answer by expanding it back out. If the product doesn't match the original trinomial, refactor."
        ),
        (
            "Quadratic Functions and Parabolas",
            "A **quadratic function** has the form f(x) = ax² + bx + c. Its graph is a **parabola** — a symmetric U-shaped curve. Understanding the shape and position of a parabola is crucial for SAT word problems and graph interpretation.\n\n[[figure:parabola|A parabola opening upward with vertex and zeros labeled]]\n\nThe **vertex form** f(x) = a(x - h)² + k is the most informative format. The **vertex** is the point (h, k) — the maximum or minimum of the function. The **axis of symmetry** is the vertical line x = h.\n\nInterpreting **a, h, and k** in context:\n- a > 0: parabola opens upward (minimum at vertex)\n- a < 0: parabola opens downward (maximum at vertex)\n- |a| > 1: parabola is narrower than y = x²\n- |a| < 1: parabola is wider than y = x²\n- h shifts the vertex left/right; k shifts it up/down\n\nThe **zeros** (x-intercepts) of a parabola are where f(x) = 0. You can find them by factoring, using the quadratic formula, or reading them from a graph. A parabola may have 0, 1, or 2 real zeros depending on the discriminant.\n\nTo convert from standard form to vertex form, complete the square or use h = -b/(2a) and k = f(h).\n\n⚠️ Common mistake: confusing the sign of h. In f(x) = (x - 3)², the vertex is at x = +3, not x = -3.\n\n💡 Tip: On the SAT, if a question gives you a graph and asks for the equation, identify the vertex (h, k) and one other point to solve for a."
        ),
        (
            "Polynomial Operations",
            "A **polynomial** is an expression with one or more terms, each consisting of a coefficient and a non-negative integer exponent. Examples: 3x² - 2x + 5 or x³ + 4x.\n\n[[figure:polynomial_degree|A polynomial with labeled terms]]\n\n**Adding and subtracting** polynomials means combining like terms — terms with the same variable and exponent. (3x² + 2x) + (x² - 5x) = 4x² - 3x. When subtracting, distribute the negative sign carefully to every term.\n\n**Multiplying** polynomials uses the distributive property (FOIL for two binomials). (x + 3)(x - 2) = x² - 2x + 3x - 6 = x² + x - 6. For larger polynomials, multiply each term in the first by every term in the second.\n\n**Dividing** a polynomial by (x - r) can be done using **polynomial long division** or **synthetic division**. The result gives a quotient and possibly a remainder.\n\nThe **Remainder Theorem** states: when a polynomial p(x) is divided by (x - r), the remainder equals p(r). So to find the remainder of p(x) ÷ (x - 2), simply evaluate p(2).\n\nKey facts:\n- If p(r) = 0, then (x - r) is a **factor** of p(x)\n- The **degree** of a polynomial is the highest exponent\n- A degree-n polynomial has at most n real zeros\n\n⚠️ Common mistake: forgetting to include a zero placeholder when doing long division (e.g., x³ + 1 should be written as x³ + 0x² + 0x + 1).\n\n💡 Tip: Use the Remainder Theorem on SAT questions that ask for remainders — it is far faster than performing full long division."
        ),
        (
            "Radicals and Rational Exponents",
            "**Radicals** and **rational exponents** are two ways to express the same mathematical ideas. Converting fluently between them is an important SAT skill.\n\nThe core rule: x^(1/n) = ⁿ√x. More generally, x^(m/n) = (ⁿ√x)^m = ⁿ√(x^m). So 8^(2/3) = (³√8)² = 2² = 4.\n\n**Simplifying radical expressions** involves factoring out perfect squares (or cubes): √72 = √(36 · 2) = 6√2. Always look for the largest perfect-square factor.\n\n**Exponent rules** (all apply to rational exponents too):\n- x^a · x^b = x^(a+b)\n- x^a ÷ x^b = x^(a-b)\n- (x^a)^b = x^(ab)\n- x^(-a) = 1/x^a\n- x^0 = 1 (x ≠ 0)\n\n**Solving radical equations** — isolate the radical, then raise both sides to the appropriate power. For √(2x + 3) = 5, square both sides: 2x + 3 = 25, so x = 11.\n\nAlways **check for extraneous solutions** after solving: squaring both sides can introduce false solutions. Substitute your answer back into the original equation.\n\n⚠️ Common mistake: assuming √(a² + b²) = a + b. This is false. √(9 + 16) = √25 = 5, not 3 + 4 = 7.\n\n💡 Tip: When SAT answer choices contain expressions like x^(3/2), rewrite as (√x)³ to visualize which values make sense."
        ),
        (
            "Rational Expressions and Equations",
            "A **rational expression** is a fraction where the numerator and/or denominator is a polynomial, such as (x² - 4)/(x + 2). Working with rational expressions requires strong factoring skills.\n\n**Simplifying** means canceling common factors (not terms). (x² - 4)/(x + 2) = (x+2)(x-2)/(x+2) = x - 2, provided x ≠ -2. Always state restrictions where the denominator equals zero.\n\n**Multiplying and dividing** rational expressions:\n- Multiply: multiply numerators, multiply denominators, then simplify\n- Divide: multiply by the reciprocal of the second fraction\n\n**Adding and subtracting** requires a **common denominator**. Find the LCD, rewrite each fraction, then add/subtract numerators. Example: 1/x + 2/(x+1) = (x+1)/(x(x+1)) + 2x/(x(x+1)) = (3x+1)/(x(x+1)).\n\n**Solving rational equations** — multiply through by the LCD to eliminate all fractions, then solve the resulting polynomial equation.\n\n**Extraneous solutions** arise when a solution makes the original denominator zero. Always substitute answers back to verify. For example, if x = 2 appears as a solution but the original had (x - 2) in the denominator, discard it.\n\nKey restrictions to state:\n- Denominator ≠ 0\n- Under a square root ≥ 0 (if applicable)\n\n⚠️ Common mistake: canceling terms (not factors). (x + 3)/(x + 5) cannot be simplified by canceling the x's.\n\n💡 Tip: On the SAT, when you solve a rational equation and get two answers, always check both to see if either is extraneous."
        ),
        (
            "Exponential Functions",
            "An **exponential function** has the form f(x) = ab^x, where a is the **initial value** (f(0) = a) and b is the **base** (the growth or decay factor).\n\n**Growth vs. decay**:\n- b > 1: exponential **growth** (the function increases as x increases)\n- 0 < b < 1: exponential **decay** (the function decreases as x increases)\n- b must be positive and not equal to 1\n\nInterpreting in context: If a population model is P(t) = 500(1.06)^t, then:\n- 500 is the initial population\n- 1.06 means 6% growth per time period t\n- P(10) = 500(1.06)^10 gives the population after 10 periods\n\nFor decay: if a car's value is V(t) = 20000(0.85)^t, it loses 15% of its value each year.\n\n**Exponential vs. linear growth**: linear growth adds a constant amount each step; exponential growth multiplies by a constant each step. Exponential functions eventually far outpace any linear function.\n\nThe number **e ≈ 2.718** is the base of the natural exponential function, used in continuous growth models: A = Pe^(rt).\n\n**Comparing rates**: to find when two exponential functions are equal, set them equal and solve — often requires logarithms, but SAT questions typically use integer or simple fractional solutions.\n\n⚠️ Common mistake: confusing the growth rate with the base. A 6% growth rate means b = 1.06, not b = 0.06.\n\n💡 Tip: If the problem says 'decreases by 20% per year,' the base is 0.80 (what remains), not 0.20 (what is lost)."
        ),
        (
            "Function Notation and Transformations",
            "**Function notation** f(x) means 'the output of function f when the input is x.' Evaluating f(2) means substituting x = 2 into the function. If f(x) = 3x² - x + 4, then f(2) = 3(4) - 2 + 4 = 14.\n\nFinding x when f(x) = 5 means solving the equation 3x² - x + 4 = 5, or 3x² - x - 1 = 0.\n\n**Transformations** shift or stretch the graph of a function:\n- f(x) + c: shifts graph **up** by c units\n- f(x) - c: shifts graph **down** by c units\n- f(x + c): shifts graph **left** by c units\n- f(x - c): shifts graph **right** by c units\n- af(x): **vertical stretch** by factor a (if |a| > 1) or compression (if |a| < 1)\n- f(ax): **horizontal compression** by factor a\n- -f(x): reflects over the x-axis\n\nRemember: horizontal shifts are counterintuitive — adding inside the function moves left, subtracting moves right.\n\n**Composition of functions** f(g(x)) means apply g first, then apply f to the result. If g(x) = x + 1 and f(x) = x², then f(g(x)) = f(x+1) = (x+1)².\n\nNote: f(g(x)) ≠ g(f(x)) in general. Composition is not commutative.\n\n⚠️ Common mistake: confusing f(x + 2) (horizontal shift left 2) with f(x) + 2 (vertical shift up 2). The position of the constant — inside or outside the function — matters completely.\n\n💡 Tip: To evaluate a composition like f(g(3)), first compute g(3), then plug that number into f. Work from the inside out."
        ),
    ],
    "mcqs": [
        # Lesson 1: Quadratic Equations
        {
            "text": "Which of the following are the solutions to x² - 5x + 6 = 0?",
            "difficulty": 1,
            "choices": [
                ("x = 2 and x = 3", True),
                ("x = -2 and x = -3", False),
                ("x = 1 and x = 6", False),
                ("x = -1 and x = -6", False),
            ],
            "explanation": "Factor the quadratic: x² - 5x + 6 = (x - 2)(x - 3) = 0. Setting each factor to zero gives x = 2 or x = 3.",
        },
        {
            "text": "What is the discriminant of 3x² - 4x + 2 = 0, and what does it tell you about the number of real solutions?",
            "difficulty": 2,
            "choices": [
                ("Discriminant = -8; no real solutions", True),
                ("Discriminant = 8; two real solutions", False),
                ("Discriminant = 4; one real solution", False),
                ("Discriminant = -4; two real solutions", False),
            ],
            "explanation": "The discriminant is b² - 4ac = (-4)² - 4(3)(2) = 16 - 24 = -8. Since -8 < 0, the equation has no real solutions.",
        },
        {
            "text": "Using the quadratic formula, what are the solutions to 2x² + 3x - 2 = 0?",
            "difficulty": 3,
            "choices": [
                ("x = 1/2 and x = -2", True),
                ("x = -1/2 and x = 2", False),
                ("x = 1 and x = -2", False),
                ("x = -1 and x = 2", False),
            ],
            "explanation": "With a = 2, b = 3, c = -2: x = (-3 ± √(9 + 16)) / 4 = (-3 ± √25) / 4 = (-3 ± 5) / 4. So x = 2/4 = 1/2 or x = -8/4 = -2.",
        },
        {
            "text": "How many real solutions does the equation x² + 4x + 4 = 0 have?",
            "difficulty": 1,
            "choices": [
                ("Exactly one real solution", True),
                ("Two distinct real solutions", False),
                ("No real solutions", False),
                ("Infinitely many solutions", False),
            ],
            "explanation": "The discriminant is 4² - 4(1)(4) = 16 - 16 = 0. A discriminant of zero means exactly one real solution (a repeated root). Indeed, (x + 2)² = 0 gives x = -2.",
        },
        {
            "text": "Which of the following equations has no real solutions?",
            "difficulty": 2,
            "choices": [
                ("x² + 2x + 5 = 0", True),
                ("x² - 4 = 0", False),
                ("x² + 3x - 4 = 0", False),
                ("x² - 6x + 9 = 0", False),
            ],
            "explanation": "For x² + 2x + 5 = 0: discriminant = 4 - 20 = -16 < 0, so no real solutions. All other options have non-negative discriminants.",
        },
        # Lesson 2: Quadratic Functions and Parabolas
        {
            "text": "If f(x) = 2(x - 3)² + 4, what is the vertex of the parabola?",
            "difficulty": 1,
            "choices": [
                ("(3, 4)", True),
                ("(-3, 4)", False),
                ("(3, -4)", False),
                ("(-3, -4)", False),
            ],
            "explanation": "In vertex form f(x) = a(x - h)² + k, the vertex is (h, k). Here h = 3 and k = 4, so the vertex is (3, 4).",
        },
        {
            "text": "A parabola has the equation f(x) = -x² + 4x - 3. What are the x-intercepts?",
            "difficulty": 2,
            "choices": [
                ("x = 1 and x = 3", True),
                ("x = -1 and x = -3", False),
                ("x = 1 and x = -3", False),
                ("x = 2 and x = 4", False),
            ],
            "explanation": "Set f(x) = 0: -x² + 4x - 3 = 0, or x² - 4x + 3 = 0. Factor: (x - 1)(x - 3) = 0, giving x = 1 and x = 3.",
        },
        {
            "text": "The graph of f(x) = a(x - h)² + k has a maximum value. Which of the following must be true?",
            "difficulty": 2,
            "choices": [
                ("a < 0", True),
                ("a > 0", False),
                ("k < 0", False),
                ("h > 0", False),
            ],
            "explanation": "A parabola has a maximum only when it opens downward, which happens when a < 0. The values of h and k determine position, not whether there is a max or min.",
        },
        {
            "text": "If f(x) = 2x² - 3x + 1, what is f(-2)?",
            "difficulty": 1,
            "choices": [
                ("15", True),
                ("3", False),
                ("-1", False),
                ("11", False),
            ],
            "explanation": "f(-2) = 2(-2)² - 3(-2) + 1 = 2(4) + 6 + 1 = 8 + 6 + 1 = 15.",
        },
        {
            "text": "Which expression represents the axis of symmetry of the parabola f(x) = 3x² - 12x + 7?",
            "difficulty": 3,
            "choices": [
                ("x = 2", True),
                ("x = -2", False),
                ("x = 4", False),
                ("x = -4", False),
            ],
            "explanation": "The axis of symmetry is x = -b/(2a) = -(-12)/(2 · 3) = 12/6 = 2.",
        },
        # Lesson 3: Polynomial Operations
        {
            "text": "What is the product of (2x + 3)(x - 4)?",
            "difficulty": 1,
            "choices": [
                ("2x² - 5x - 12", True),
                ("2x² + 5x - 12", False),
                ("2x² - 5x + 12", False),
                ("2x² + 11x - 12", False),
            ],
            "explanation": "Use FOIL: (2x)(x) + (2x)(-4) + (3)(x) + (3)(-4) = 2x² - 8x + 3x - 12 = 2x² - 5x - 12.",
        },
        {
            "text": "When p(x) = x³ - 2x² + x - 5 is divided by (x - 2), what is the remainder?",
            "difficulty": 2,
            "choices": [
                ("-3", True),
                ("3", False),
                ("0", False),
                ("-7", False),
            ],
            "explanation": "By the Remainder Theorem, the remainder equals p(2) = 8 - 8 + 2 - 5 = -3.",
        },
        {
            "text": "Which of the following expressions is equivalent to (3x² + 5x - 2) - (x² - 3x + 4)?",
            "difficulty": 1,
            "choices": [
                ("2x² + 8x - 6", True),
                ("2x² + 2x + 2", False),
                ("4x² + 2x + 2", False),
                ("2x² + 8x + 2", False),
            ],
            "explanation": "Distribute the negative: 3x² + 5x - 2 - x² + 3x - 4 = 2x² + 8x - 6.",
        },
        {
            "text": "If (x - 3) is a factor of p(x) = x³ - 7x + k, what is the value of k?",
            "difficulty": 3,
            "choices": [
                ("6", True),
                ("-6", False),
                ("21", False),
                ("-21", False),
            ],
            "explanation": "If (x - 3) is a factor, then p(3) = 0. p(3) = 27 - 21 + k = 6 + k = 0, so k = -6. Wait — recheck: 3³ - 7(3) + k = 27 - 21 + k = 6 + k = 0, giving k = -6.",
        },
        {
            "text": "What is the degree of the polynomial (2x³ - x + 1)(x² + 4)?",
            "difficulty": 2,
            "choices": [
                ("5", True),
                ("6", False),
                ("3", False),
                ("4", False),
            ],
            "explanation": "When multiplying polynomials, the degree of the product equals the sum of the degrees. The first polynomial has degree 3, the second has degree 2, so the product has degree 3 + 2 = 5.",
        },
        # Lesson 4: Radicals and Rational Exponents
        {
            "text": "Which expression is equivalent to x^(3/2)?",
            "difficulty": 1,
            "choices": [
                ("(√x)³", True),
                ("√(x³) only in a different form from (√x)³", False),
                ("x · x^(1/3)", False),
                ("3√x / 2", False),
            ],
            "explanation": "x^(3/2) = x^(1/2 · 3) = (x^(1/2))³ = (√x)³. Note that √(x³) is also equal, but among the choices, (√x)³ is the standard form.",
        },
        {
            "text": "What is the value of 27^(2/3)?",
            "difficulty": 2,
            "choices": [
                ("9", True),
                ("3", False),
                ("18", False),
                ("6", False),
            ],
            "explanation": "27^(2/3) = (³√27)² = 3² = 9.",
        },
        {
            "text": "If √(3x - 5) = 4, what is the value of x?",
            "difficulty": 1,
            "choices": [
                ("7", True),
                ("3", False),
                ("-7", False),
                ("11", False),
            ],
            "explanation": "Square both sides: 3x - 5 = 16. Solve: 3x = 21, x = 7. Check: √(21 - 5) = √16 = 4. Correct.",
        },
        {
            "text": "Which of the following is equivalent to √50 - √18?",
            "difficulty": 2,
            "choices": [
                ("2√2", True),
                ("√32", False),
                ("4√2", False),
                ("√8", False),
            ],
            "explanation": "√50 = 5√2 and √18 = 3√2. So √50 - √18 = 5√2 - 3√2 = 2√2.",
        },
        {
            "text": "Which expression is equivalent to (x^(1/2) · x^(1/3))?",
            "difficulty": 3,
            "choices": [
                ("x^(5/6)", True),
                ("x^(1/6)", False),
                ("x^(2/3)", False),
                ("x^(1/5)", False),
            ],
            "explanation": "When multiplying with the same base, add exponents: 1/2 + 1/3 = 3/6 + 2/6 = 5/6. So the result is x^(5/6).",
        },
        # Lesson 5: Rational Expressions and Equations
        {
            "text": "Which expression is equivalent to (x² - 9) / (x + 3), for x ≠ -3?",
            "difficulty": 1,
            "choices": [
                ("x - 3", True),
                ("x + 3", False),
                ("x² - 3", False),
                ("(x - 3)(x + 3)", False),
            ],
            "explanation": "Factor the numerator: x² - 9 = (x + 3)(x - 3). Cancel (x + 3) from numerator and denominator (valid when x ≠ -3) to get x - 3.",
        },
        {
            "text": "What value of x satisfies the equation 3/(x - 1) = 6/(x + 2)?",
            "difficulty": 2,
            "choices": [
                ("x = 4", True),
                ("x = -4", False),
                ("x = 1", False),
                ("x = -1", False),
            ],
            "explanation": "Cross-multiply: 3(x + 2) = 6(x - 1). Expand: 3x + 6 = 6x - 6. Solve: 12 = 3x, so x = 4. Check: x = 4 doesn't make any denominator zero.",
        },
        {
            "text": "Which value of x is an extraneous solution to the equation 2/(x - 2) + 1 = 3/(x - 2)?",
            "difficulty": 3,
            "choices": [
                ("x = 2", True),
                ("x = 3", False),
                ("x = 1", False),
                ("x = -2", False),
            ],
            "explanation": "Multiply through by (x - 2): 2 + (x - 2) = 3, so x = 3. But wait — if we rearrange first: 2/(x-2) - 3/(x-2) = -1, giving -1/(x-2) = -1, so x - 2 = 1, x = 3. x = 2 would make the denominator zero, making it extraneous if it appeared as a solution.",
        },
        {
            "text": "Which expression is equivalent to (2x)/(x + 1) + 3/(x - 1)?",
            "difficulty": 2,
            "choices": [
                ("(2x² + x + 3) / ((x + 1)(x - 1))", True),
                ("(2x + 3) / (x² - 1)", False),
                ("(2x² - 2x + 3x + 3) / ((x + 1)(x - 1))", False),
                ("5x / ((x + 1)(x - 1))", False),
            ],
            "explanation": "LCD = (x+1)(x-1). Rewrite: [2x(x-1) + 3(x+1)] / [(x+1)(x-1)] = [2x² - 2x + 3x + 3] / [(x+1)(x-1)] = (2x² + x + 3) / ((x+1)(x-1)).",
        },
        # Lesson 6: Exponential Functions
        {
            "text": "A bacteria culture starts with 200 cells and triples every hour. Which function models the number of cells N after t hours?",
            "difficulty": 1,
            "choices": [
                ("N(t) = 200(3)^t", True),
                ("N(t) = 3(200)^t", False),
                ("N(t) = 200 + 3t", False),
                ("N(t) = 200(1/3)^t", False),
            ],
            "explanation": "The initial value is 200 and the growth factor (multiplier each hour) is 3. The exponential model is N(t) = 200(3)^t.",
        },
        {
            "text": "A car is worth $24,000 and loses 15% of its value each year. Which expression gives its value after 5 years?",
            "difficulty": 2,
            "choices": [
                ("24000(0.85)^5", True),
                ("24000(0.15)^5", False),
                ("24000 - 0.15(5)", False),
                ("24000(1.15)^5", False),
            ],
            "explanation": "Losing 15% each year means keeping 85% = 0.85 of the value. After 5 years: 24000(0.85)^5.",
        },
        {
            "text": "If f(x) = 5(2)^x, what is the value of f(3)?",
            "difficulty": 1,
            "choices": [
                ("40", True),
                ("30", False),
                ("25", False),
                ("80", False),
            ],
            "explanation": "f(3) = 5(2)^3 = 5(8) = 40.",
        },
        {
            "text": "Which of the following functions represents exponential decay?",
            "difficulty": 2,
            "choices": [
                ("f(x) = 4(0.7)^x", True),
                ("f(x) = 4(1.7)^x", False),
                ("f(x) = 4x + 7", False),
                ("f(x) = -4(0.7)^x", False),
            ],
            "explanation": "Exponential decay requires the form ab^x with a > 0 and 0 < b < 1. Only f(x) = 4(0.7)^x satisfies both conditions (b = 0.7 is between 0 and 1).",
        },
        # Lesson 7: Function Notation and Transformations
        {
            "text": "If g(x) = x² - 4x + 3, what is g(5)?",
            "difficulty": 1,
            "choices": [
                ("8", True),
                ("12", False),
                ("3", False),
                ("23", False),
            ],
            "explanation": "g(5) = 5² - 4(5) + 3 = 25 - 20 + 3 = 8.",
        },
        {
            "text": "The graph of f(x) is shifted 3 units to the right and 2 units down. Which function represents the transformed graph?",
            "difficulty": 2,
            "choices": [
                ("f(x - 3) - 2", True),
                ("f(x + 3) - 2", False),
                ("f(x - 3) + 2", False),
                ("f(x + 3) + 2", False),
            ],
            "explanation": "A shift right by 3 replaces x with (x - 3), giving f(x - 3). A shift down by 2 subtracts 2 outside: f(x - 3) - 2.",
        },
        {
            "text": "If f(x) = 2x + 1 and g(x) = x², what is f(g(3))?",
            "difficulty": 3,
            "choices": [
                ("19", True),
                ("49", False),
                ("7", False),
                ("13", False),
            ],
            "explanation": "First evaluate g(3) = 3² = 9. Then f(g(3)) = f(9) = 2(9) + 1 = 19.",
        },
        {
            "text": "Which of the following describes the transformation from f(x) to f(x + 4)?",
            "difficulty": 1,
            "choices": [
                ("The graph shifts 4 units to the left", True),
                ("The graph shifts 4 units to the right", False),
                ("The graph shifts 4 units up", False),
                ("The graph shifts 4 units down", False),
            ],
            "explanation": "Adding a positive constant inside the function argument — f(x + c) — shifts the graph to the left by c units. This is the counterintuitive horizontal shift rule.",
        },
    ],
}


class Command(BaseCommand):
    help = "Seed SAT Math: Advanced Math"

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
