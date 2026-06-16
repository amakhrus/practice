"""
Seed a GED Algebra mastery course for expressions and polynomials.

Run:
    python manage.py seed_ged_algebra_expressions_polynomials
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


def item(text, answer, distractors, steps, trap, difficulty=2):
    return {
        "text": text,
        "difficulty": difficulty,
        "choices": [(answer, True)] + [(choice, False) for choice in distractors],
        "explanation": " ".join(
            [f"Step {index}: {step}" for index, step in enumerate(steps, start=1)]
            + [f"Common trap: {trap}"]
        ),
    }


COURSE = {
    "title": "GED Algebra: Expressions & Polynomials Mastery",
    "slug": "ged-algebra-expressions-polynomials",
    "program": "GED",
    "subject": "math",
    "description": (
        "A GED Mathematical Reasoning bridge course for algebraic expressions, "
        "properties, substitution, equivalent forms, exponent rules, polynomials, "
        "factoring, and rational expressions. Students build the symbolic fluency "
        "needed before equations, inequalities, functions, and advanced algebra."
    ),
    "lessons": [
        (
            "1. Variables, Terms, Coefficients, and Constants",
            r"""
Algebra begins with expressions. An **expression** is a mathematical phrase without an equals sign, such as:
\[
3x^2-5x+7.
\]
An expression can be simplified or evaluated, but it is not "solved" because there is no equals sign.

[[figure:expression_anatomy|The parts of an expression have names: term, coefficient, variable, exponent, and constant.]]

A **term** is a piece separated by addition or subtraction. In \(3x^2-5x+7\), the terms are \(3x^2\), \(-5x\), and \(7\). Notice that the negative sign stays attached to \(-5x\).

A **coefficient** is the number multiplying a variable. In \(-5x\), the coefficient is \(-5\). In \(x\), the coefficient is 1 because \(x=1x\). In \(-x\), the coefficient is \(-1\).

A **constant** is a term with no variable, such as 7. A **variable** is a symbol for a number that can change or be unknown.

The **degree** of a term is the exponent on the variable. For \(3x^2\), the degree is 2. For \(5x\), the degree is 1. For a nonzero constant, the degree is 0.

Common misconception: a term's sign is not separate decoration. The term after subtraction is negative, so \(3x-5\) contains \(3x\) and \(-5\).

Academic habit: when you read an expression, mark the terms first. Most algebra mistakes begin with terms being grouped incorrectly.

[[check:In \(4x-9\), what is the coefficient of \(x\)?|4|The coefficient is the number multiplying the variable.]]
            """,
        ),
        (
            "2. Translating Words and Contexts into Expressions",
            r"""
The GED often asks you to turn a situation into an algebraic expression. Translation is not about memorizing one keyword; it is about preserving meaning and order.

Common patterns:
- "a number increased by 8" becomes \(x+8\)
- "8 less than a number" becomes \(x-8\)
- "8 less a number" becomes \(8-x\)
- "twice a number" becomes \(2x\)
- "a number divided by 5" becomes \(\frac{x}{5}\)

Order matters with subtraction and division. "Seven less than twice a number" means start with \(2x\), then subtract 7:
\[
2x-7.
\]
It is not \(7-2x\).

Context can create more complex expressions. If notebooks cost \(\$3\) each and a student buys \(n\) notebooks plus one \(\$5\) folder, the total cost is:
\[
3n+5.
\]
If a rectangle has length \(x+4\) and width \(x\), its perimeter is:
\[
2(x+4)+2x.
\]
This can later be simplified, but the expression first comes from the structure of the shape.

Common misconception: trusting a single keyword without reading the order. The phrase "less than" often reverses the order from how the words appear.

Academic habit: define the variable in words before writing the expression. For example, "Let \(n\) be the number of notebooks."
            """,
        ),
        (
            "3. Evaluating Expressions by Substitution",
            r"""
To **evaluate** an expression, replace the variable with a specific number and simplify. Substitution must be careful, especially for negative numbers.

Example:
\[
4x-7\quad\text{when }x=3.
\]
Replace \(x\) with 3:
\[
4(3)-7=12-7=5.
\]

For a negative input, use parentheses:
\[
x^2+3x\quad\text{when }x=-2.
\]
Substitute:
\[
(-2)^2+3(-2)=4-6=-2.
\]

Expressions with two variables work the same way. If \(a=5\) and \(b=-3\), then:
\[
2a-b=2(5)-(-3)=10+3=13.
\]

If an expression contains a fraction, substitute first and then simplify:
\[
\frac{3x+6}{2}\quad\text{when }x=4
\]
\[
\frac{3(4)+6}{2}=\frac{18}{2}=9.
\]

Common misconception: writing \(3(-2)^2\) when the expression is \(3x^2\) and thinking the 3 is squared too. Only the variable part is squared unless parentheses say otherwise.

Academic habit: put every substituted negative number in parentheses. This prevents sign and exponent mistakes.

[[check:Evaluate \(x^2+3x\) when \(x=-2\).|-2|\((-2)^2=4\) and \(3(-2)=-6\), so the value is \(-2\).]]
            """,
        ),
        (
            "4. Combining Like Terms",
            r"""
Like terms have exactly the same variable part. You may combine their coefficients because they count the same kind of object.

Examples:
\[
3x+5x=8x,\qquad 7y-2y=5y.
\]

But \(3x+5\) cannot become \(8x\), because \(3x\) is a variable term and 5 is a constant. Also, \(x^2\) and \(x\) are not like terms because their exponents are different.

Simplify:
\[
4x+7-2x+9.
\]
Group like terms:
\[
(4x-2x)+(7+9)=2x+16.
\]

Signs stay with terms. In \(8a-3b+5a-2b\), the like terms are \(8a\) and \(5a\), and \(-3b\) and \(-2b\):
\[
13a-5b.
\]

Combining like terms does not change the value of the expression. It rewrites the expression in a more useful equivalent form.

Common misconception: combining unlike terms just because they are next to each other. \(2x+3y\) cannot be simplified unless more information is given.

Academic habit: underline matching variable parts before adding coefficients. This makes \(x^2\), \(x\), and constants visibly separate.
            """,
        ),
        (
            "5. The Distributive Property and Negative Groups",
            r"""
The distributive property says:
\[
a(b+c)=ab+ac.
\]
A number or expression outside parentheses multiplies every term inside.

[[figure:distributive_area_model|The area model shows why \(4(x+3)\) becomes \(4x+12\).]]

Examples:
\[
3(x+5)=3x+15,
\]
\[
-2(4x-7)=-8x+14.
\]
The second example shows that the \(-2\) multiplies both \(4x\) and \(-7\).

A minus sign before parentheses is the same as multiplying by \(-1\):
\[
-(x-6)=-x+6.
\]
This is one of the most common GED algebra traps.

Distribute before combining like terms:
\[
2(x+4)+3x=2x+8+3x=5x+8.
\]

Sometimes you can factor after distributing mentally, but for GED work it is usually safer to write the distribution step first.

Common misconception: distributing to only the first term. \(5(x+2)\) is \(5x+10\), not \(5x+2\).

Academic habit: draw arrows from the outside factor to every term inside the parentheses.
            """,
        ),
        (
            "6. Algebraic Properties and Equivalent Expressions",
            r"""
Two expressions are **equivalent** if they have the same value for every allowed value of the variable. For example:
\[
3(x+2)\quad\text{and}\quad 3x+6
\]
are equivalent.

The algebraic properties explain why equivalent forms are valid:
- **Commutative property:** \(a+b=b+a\), \(ab=ba\)
- **Associative property:** \((a+b)+c=a+(b+c)\)
- **Distributive property:** \(a(b+c)=ab+ac\)
- **Identity property:** \(a+0=a\), \(a\cdot1=a\)
- **Inverse property:** \(a+(-a)=0\), \(a\cdot\frac{1}{a}=1\) for \(a\ne0\)

Equivalent expressions are useful because different forms reveal different information. The form \(5x+20\) makes the coefficient and constant clear. The form \(5(x+4)\) makes a common factor visible.

To test whether expressions might be equivalent, simplify both sides. For example:
\[
2(x+3)+x=3x+6.
\]
Since both sides simplify to \(3x+6\), they are equivalent.

Testing a single number can show expressions are not equivalent, but it cannot prove they are equivalent for every number. Algebraic simplification gives stronger evidence.

Common misconception: thinking expressions are different because they look different. Appearance is not enough; equivalent expressions can have very different forms.

Academic habit: when multiple-choice answers ask for an equivalent expression, simplify the original before comparing choices.
            """,
        ),
        (
            "7. Factoring Out the Greatest Common Factor",
            r"""
Factoring rewrites an expression as multiplication. It is the reverse of distributing.

The first factoring move is usually to pull out the **greatest common factor** (GCF). For:
\[
12x+18,
\]
the GCF of 12 and 18 is 6, so:
\[
12x+18=6(2x+3).
\]

For expressions with variables, include common variable factors:
\[
8x^2+12x=4x(2x+3).
\]
The coefficient GCF is 4, and both terms contain at least one \(x\).

Factoring is correct if redistributing returns the original expression:
\[
4x(2x+3)=8x^2+12x.
\]

Factoring can also reveal structure in word problems. If a club spends \(6n+24\) dollars, the expression \(6(n+4)\) shows a common cost of 6 applied to a group count of \(n+4\).

Common misconception: factoring out a common factor from only one term. Every term inside the original expression must be divided by the factor you pull out.

Academic habit: after factoring, multiply back mentally or on paper. This quick check catches most factoring errors.
            """,
        ),
        (
            "8. Exponent Rules for Algebra",
            r"""
Exponent rules are shortcuts for repeated multiplication. They work only when the bases are handled correctly.

Product rule:
\[
x^3\cdot x^2=x^{3+2}=x^5.
\]
You add exponents because the repeated factors combine.

Quotient rule:
\[
\frac{x^7}{x^3}=x^{7-3}=x^4,\qquad x\ne0.
\]

Power rule:
\[
(x^2)^3=x^{2\cdot3}=x^6.
\]

Power of a product:
\[
(3x)^2=9x^2.
\]
Both the coefficient and the variable are squared.

Zero exponent:
\[
x^0=1,\qquad x\ne0.
\]

Negative exponent:
\[
x^{-2}=\frac{1}{x^2},\qquad x\ne0.
\]
A negative exponent does not make the expression negative; it means reciprocal.

Common misconception: adding exponents when adding terms. \(x^3+x^2\) cannot become \(x^5\). The product rule applies to multiplication, not addition.

Academic habit: identify the operation first. Multiplication, division, and power each use a different exponent rule.
            """,
        ),
        (
            "9. Polynomial Degree and Standard Form",
            r"""
A **polynomial** is a sum or difference of terms with whole-number exponents on variables:
\[
2x^3-4x^2+x-9.
\]

[[figure:polynomial_degree|The degree of a polynomial is the highest exponent among its terms.]]

Standard form writes terms from highest degree to lowest degree:
\[
5-3x^2+7x
\]
becomes:
\[
-3x^2+7x+5.
\]

Polynomials are named by number of terms:
- **monomial:** one term, such as \(7x^2\)
- **binomial:** two terms, such as \(x+4\)
- **trinomial:** three terms, such as \(x^2+5x+6\)

The leading coefficient is the coefficient of the highest-degree term in standard form. In \(-3x^2+7x+5\), the leading coefficient is \(-3\).

A constant polynomial such as 8 has degree 0, as long as it is not the zero polynomial.

Common misconception: choosing the largest coefficient instead of the highest exponent. Degree is about exponent, not coefficient size.

Academic habit: rewrite in standard form before identifying degree or leading coefficient.
            """,
        ),
        (
            "10. Adding, Subtracting, and Multiplying Polynomials",
            r"""
Adding and subtracting polynomials is combining like terms.

Example:
\[
(2x^2+3x-5)+(x^2-7x+4).
\]
Combine like terms:
\[
3x^2-4x-1.
\]

Subtraction requires distributing the negative sign:
\[
(4x^2-2x+1)-(x^2+5x-6).
\]
Rewrite:
\[
4x^2-2x+1-x^2-5x+6.
\]
Then combine:
\[
3x^2-7x+7.
\]

To multiply a monomial by a polynomial, distribute:
\[
3x(2x^2-x+4)=6x^3-3x^2+12x.
\]

To multiply binomials, multiply every term in the first binomial by every term in the second:
\[
(x+2)(x+5)=x^2+5x+2x+10=x^2+7x+10.
\]

Common misconception: multiplying only first terms and last terms. Every term must multiply every term.

Academic habit: after multiplying binomials, check for a middle term made by combining the outer and inner products.
            """,
        ),
        (
            "11. Factoring Trinomials and Special Products",
            r"""
Factoring a trinomial reverses binomial multiplication.

[[figure:factoring_trinomial|For \(x^2+5x+6\), find two numbers that multiply to 6 and add to 5.]]

For:
\[
x^2+5x+6,
\]
find two numbers that multiply to 6 and add to 5. The numbers are 2 and 3, so:
\[
x^2+5x+6=(x+2)(x+3).
\]

If the constant is positive and the middle term is negative, both factors are negative:
\[
x^2-7x+12=(x-3)(x-4).
\]

If the constant is negative, one factor is positive and one is negative:
\[
x^2+x-12=(x+4)(x-3).
\]

Special product patterns are worth recognizing:
\[
x^2-9=(x-3)(x+3)
\]
because it is a difference of squares.

Not every trinomial factors nicely with integers. If no pair of integer factors fits, say it is not factorable over the integers.

Common misconception: using numbers that multiply correctly but do not add to the middle coefficient. Both conditions must be true.

Academic habit: multiply the binomials back to check. Factoring and multiplication undo each other.
            """,
        ),
        (
            "12. Rational Expressions, Restrictions, and GED Modeling",
            r"""
A **rational expression** is a fraction whose numerator or denominator contains a variable, such as:
\[
\frac{x^2-16}{x-4}.
\]

[[figure:rational_expression_restriction|A rational expression is undefined when its original denominator is zero.]]

Restrictions come from the denominator. Since \(x-4=0\) when \(x=4\), the expression is undefined at \(x=4\). Therefore \(x\ne4\).

You may simplify rational expressions by factoring and canceling common factors:
\[
\frac{x^2-16}{x-4}=\frac{(x-4)(x+4)}{x-4}=x+4,\qquad x\ne4.
\]
The simplified expression \(x+4\) looks defined at \(x=4\), but the original expression was not. The restriction remains.

Rational expressions appear in GED-style formulas and rates. If \(C\) dollars are shared among \(n\) people, the cost per person is:
\[
\frac{C}{n},\qquad n\ne0.
\]
Zero people would make the situation impossible.

Common misconception: canceling terms instead of factors. In \(\frac{x+6}{x}\), the \(x\) in the numerator is not a separate factor, so it cannot cancel with the denominator.

Academic habit: write restrictions before simplifying. That preserves values that are not allowed.

[[check:What value is not allowed in \(\frac{x^2-16}{x-4}\)?|4|The denominator \(x-4\) cannot equal zero, so \(x\ne4\).]]
            """,
        ),
    ],
    "mcqs": [
        item(r"In the expression \(3x^2-5x+7\), what is the coefficient of \(x^2\)?", r"\(3\)", [r"\(-5\)", r"\(2\)", r"\(7\)"], ["The coefficient is the number multiplying the variable part.", "The term with \(x^2\) is \(3x^2\).", "Therefore the coefficient is 3."], "choosing the exponent 2 instead of the coefficient.", 1),
        item(r"In \(3x^2-5x+7\), which term is the constant?", r"\(7\)", [r"\(3x^2\)", r"\(-5x\)", r"\(x\)"], ["A constant has no variable.", "The only term without a variable is 7.", "So the constant term is 7."], "forgetting that signs and variables define terms.", 1),
        item(r"How many terms are in \(4a-9b+12\)?", r"\(3\)", [r"\(2\)", r"\(4\)", r"\(1\)"], ["Terms are separated by plus or minus signs.", "The terms are \(4a\), \(-9b\), and \(12\).", "There are 3 terms."], "counting variables only instead of terms.", 1),
        item(r"Which is an expression, not an equation?", r"\(5x+2\)", [r"\(5x+2=17\)", r"\(x=3\)", r"\(2x-1=9\)"], ["An expression has no equals sign.", "\(5x+2\) has no equals sign.", "Therefore it is an expression."], "thinking every algebra phrase must be an equation.", 1),

        item(r"Write 'seven less than twice a number \(x\)' as an expression.", r"\(2x-7\)", [r"\(7-2x\)", r"\(2(x-7)\)", r"\(7x-2\)"], ["Twice a number is \(2x\).", "Seven less than that means subtract 7 from \(2x\).", "The expression is \(2x-7\)."], "reversing the subtraction order.", 1),
        item(r"A taxi charges \(\$4\) plus \(\$2\) per mile. Which expression gives the cost for \(m\) miles?", r"\(2m+4\)", [r"\(4m+2\)", r"\(6m\)", r"\(2+m+4\)"], ["The per-mile cost is \(2m\).", "The fixed charge is 4.", "Total cost is \(2m+4\)."], "multiplying the fixed fee by miles.", 1),
        item(r"A rectangle has length \(x+5\) and width \(x\). Which expression represents its perimeter?", r"\(2(x+5)+2x\)", [r"\((x+5)x\)", r"\(x+5+x\)", r"\(2x+5\)"], ["Perimeter adds all side lengths.", "A rectangle has two lengths and two widths.", "So the expression is \(2(x+5)+2x\)."], "writing area or adding only one length and one width.", 2),
        item(r"Which expression means 'a number \(n\) divided by 6, then increased by 4'?", r"\(\frac{n}{6}+4\)", [r"\(\frac{n}{10}\)", r"\(\frac{n+4}{6}\)", r"\(6n+4\)"], ["First divide the number by 6.", "Then increase the result by 4.", "That gives \(\frac{n}{6}+4\)."], "putting the later increase inside the division.", 2),

        item(r"Evaluate \(4x-7\) when \(x=3\).", r"\(5\)", [r"\(9\)", r"\(-5\)", r"\(19\)"], ["Substitute \(x=3\).", "Compute \(4(3)-7=12-7\).", "The value is 5."], "forgetting multiplication between 4 and \(x\).", 1),
        item(r"Evaluate \(x^2+3x\) when \(x=-2\).", r"\(-2\)", [r"\(2\)", r"\(-10\)", r"\(10\)"], ["Substitute with parentheses: \((-2)^2+3(-2)\).", "Compute \(4-6\).", "The value is \(-2\)."], "squaring the input incorrectly or losing the negative in \(3(-2)\).", 2),
        item(r"If \(a=5\) and \(b=-3\), evaluate \(2a-b\).", r"\(13\)", [r"\(7\)", r"\(-13\)", r"\(10\)"], ["Substitute: \(2(5)-(-3)\).", "Subtracting \(-3\) means adding 3.", "The value is \(10+3=13\)."], "treating minus negative as minus positive.", 2),
        item(r"Evaluate \(\frac{3x+6}{2}\) when \(x=4\).", r"\(9\)", [r"\(6\)", r"\(15\)", r"\(7\)"], ["Substitute \(x=4\): \(\frac{3(4)+6}{2}\).", "Compute the numerator: \(12+6=18\).", "Divide: \(18/2=9\)."], "dividing only part of the numerator by 2.", 2),

        item(r"Simplify \(4x+7-2x+9\).", r"\(2x+16\)", [r"\(2x+2\)", r"\(6x+16\)", r"\(18x\)"], ["Combine \(4x-2x=2x\).", "Combine constants \(7+9=16\).", "The simplified expression is \(2x+16\)."], "combining variable terms and constants together.", 1),
        item(r"Simplify \(8a-3b+5a-2b\).", r"\(13a-5b\)", [r"\(13a-b\)", r"\(3a-5b\)", r"\(18ab\)"], ["Combine \(a\)-terms: \(8a+5a=13a\).", "Combine \(b\)-terms: \(-3b-2b=-5b\).", "The result is \(13a-5b\)."], "dropping the negative sign on the \(b\)-terms.", 2),
        item(r"Which terms are like terms?", r"\(6x^2\) and \(-3x^2\)", [r"\(6x^2\) and \(6x\)", r"\(4x\) and \(4y\)", r"\(5\) and \(5x\)"], ["Like terms have the same variable part.", "\(6x^2\) and \(-3x^2\) both have \(x^2\).", "Therefore they are like terms."], "matching coefficients instead of variable parts.", 1),
        item(r"Simplify \(9x^2+4x-3x^2+6\).", r"\(6x^2+4x+6\)", [r"\(10x^2+6\)", r"\(6x^2+10x\)", r"\(16x^2\)"], ["Combine \(x^2\)-terms: \(9x^2-3x^2=6x^2\).", "The \(4x\) term and constant 6 are unlike terms.", "The result is \(6x^2+4x+6\)."], "combining \(x^2\), \(x\), and constants as if they were alike.", 2),

        item(r"Simplify \(3(x+5)\).", r"\(3x+15\)", [r"\(3x+5\)", r"\(x+15\)", r"\(8x\)"], ["The 3 multiplies every term inside parentheses.", "Compute \(3\cdot x=3x\) and \(3\cdot5=15\).", "The result is \(3x+15\)."], "distributing to only the first term.", 1),
        item(r"Simplify \(-2(4x-7)\).", r"\(-8x+14\)", [r"\(-8x-14\)", r"\(-8x+7\)", r"\(8x+14\)"], ["Multiply \(-2\) by \(4x\) to get \(-8x\).", "Multiply \(-2\) by \(-7\) to get \(+14\).", "The result is \(-8x+14\)."], "forgetting that a negative times a negative is positive.", 2),
        item(r"Simplify \(-(x-6)\).", r"\(-x+6\)", [r"\(-x-6\)", r"\(x+6\)", r"\(x-6\)"], ["A leading minus means multiply by \(-1\).", "Multiply both terms by \(-1\).", "The result is \(-x+6\)."], "changing only the first sign.", 2),
        item(r"Simplify \(2(x+4)+3x\).", r"\(5x+8\)", [r"\(2x+11\)", r"\(5x+4\)", r"\(10x+8\)"], ["Distribute: \(2x+8+3x\).", "Combine like terms: \(2x+3x=5x\).", "The result is \(5x+8\)."], "combining before distributing or forgetting to multiply 4 by 2.", 2),

        item(r"Which expression is equivalent to \(5(x-3)\)?", r"\(5x-15\)", [r"\(5x-3\)", r"\(x-15\)", r"\(5x+15\)"], ["Use the distributive property.", "Multiply \(5\) by \(x\) and by \(-3\).", "The equivalent expression is \(5x-15\)."], "not distributing to the constant term.", 1),
        item(r"Which property is shown by \(a+b=b+a\)?", "Commutative property of addition", ["Associative property", "Distributive property", "Identity property"], ["The order of the addends changes.", "Changing order without changing the sum is commutative.", "So this is the commutative property of addition."], "confusing order change with grouping change.", 1),
        item(r"Are \(2(x+3)+x\) and \(3x+6\) equivalent?", "Yes, both simplify to \(3x+6\).", ["No, because they look different.", "No, because one has parentheses.", "Only when \(x=0\)."], ["Distribute \(2(x+3)\) to get \(2x+6\).", "Add \(x\): \(2x+6+x=3x+6\).", "The expressions are equivalent for all \(x\)."], "judging by appearance instead of simplifying.", 2),
        item(r"Which expression is NOT equivalent to \(4x+8\)?", r"\(4(x+8)\)", [r"\(4(x+2)\)", r"\(8+4x\)", r"\(2(2x+4)\)"], ["Simplify each choice.", "\(4(x+8)=4x+32\).", "That is not equivalent to \(4x+8\)."], "choosing a form just because it starts with the same coefficient.", 2),

        item(r"Factor \(12x+18\) using the greatest common factor.", r"\(6(2x+3)\)", [r"\(3(4x+6)\)", r"\(12(x+18)\)", r"\(2(6x+9)\)"], ["The GCF of 12 and 18 is 6.", "Divide each term by 6: \(12x/6=2x\), \(18/6=3\).", "The factored form is \(6(2x+3)\)."], "factoring with a common factor but not the greatest one.", 2),
        item(r"Factor \(8x^2+12x\) completely.", r"\(4x(2x+3)\)", [r"\(4(2x^2+3x)\)", r"\(x(8x+12)\)", r"\(2x(4x+6)\)"], ["The coefficient GCF is 4.", "Both terms also share \(x\).", "Factor out \(4x\) to get \(4x(2x+3)\)."], "factoring out only the numerical GCF or only the variable.", 2),
        item(r"Which expression equals \(7y-21\) after factoring out the GCF?", r"\(7(y-3)\)", [r"\(7(y+3)\)", r"\(y(7-21)\)", r"\(3(7y-7)\)"], ["The GCF is 7.", "Divide \(7y\) by 7 to get \(y\), and \(-21\) by 7 to get \(-3\).", "The factored expression is \(7(y-3)\)."], "losing the negative sign inside parentheses.", 1),
        item(r"Check the factoring: what is \(5x(3x-2)\) after distributing?", r"\(15x^2-10x\)", [r"\(15x-10x\)", r"\(8x^2-10x\)", r"\(15x^2-2\)"], ["Multiply \(5x\cdot3x=15x^2\).", "Multiply \(5x\cdot(-2)=-10x\).", "The result is \(15x^2-10x\)."], "forgetting that \(x\cdot x=x^2\).", 2),

        item(r"Simplify \(x^3\cdot x^2\).", r"\(x^5\)", [r"\(x^6\)", r"\(2x^5\)", r"\(x\)"], ["The bases are the same and the operation is multiplication.", "Add exponents: \(3+2=5\).", "The result is \(x^5\)."], "multiplying exponents instead of adding them.", 1),
        item(r"Simplify \(\frac{x^7}{x^3}\), assuming \(x\ne0\).", r"\(x^4\)", [r"\(x^{10}\)", r"\(x^{21}\)", r"\(x^3\)"], ["The bases are the same and the operation is division.", "Subtract exponents: \(7-3=4\).", "The result is \(x^4\)."], "adding exponents during division.", 1),
        item(r"Simplify \((x^2)^3\).", r"\(x^6\)", [r"\(x^5\)", r"\(x^8\)", r"\(x^9\)"], ["A power raised to a power multiplies exponents.", "Compute \(2\cdot3=6\).", "The result is \(x^6\)."], "adding exponents instead of multiplying them.", 1),
        item(r"Simplify \((3x)^2\).", r"\(9x^2\)", [r"\(3x^2\)", r"\(6x\)", r"\(9x\)"], ["The exponent applies to both 3 and \(x\).", "\(3^2=9\) and \(x^2=x^2\).", "The result is \(9x^2\)."], "squaring only the variable or only the coefficient.", 2),
        item(r"Rewrite \(x^{-2}\) with a positive exponent.", r"\(\frac{1}{x^2}\)", [r"\(-x^2\)", r"\(\frac{1}{2x}\)", r"\(x^2\)"], ["A negative exponent means reciprocal.", "Move \(x^2\) to the denominator.", "So \(x^{-2}=\frac{1}{x^2}\)."], "thinking a negative exponent makes the expression negative.", 2),

        item(r"What is the degree of \(2x^3-4x^2+x-9\)?", r"\(3\)", [r"\(2\)", r"\(4\)", r"\(9\)"], ["Degree is the highest exponent.", "The highest exponent in the polynomial is 3.", "Therefore the degree is 3."], "choosing the largest coefficient or constant.", 1),
        item(r"Write \(5-3x^2+7x\) in standard form.", r"\(-3x^2+7x+5\)", [r"\(7x-3x^2+5\)", r"\(5+7x-3x^2\)", r"\(-3x+7x^2+5\)"], ["Standard form orders terms by descending degree.", "The \(x^2\) term comes first, then the \(x\) term, then the constant.", "Keep signs attached: \(-3x^2+7x+5\)."], "reordering terms while dropping or changing signs.", 2),
        item(r"Which polynomial is a trinomial?", r"\(x^2+5x+6\)", [r"\(7x\)", r"\(x+4\)", r"\(x^3\)"], ["A trinomial has three terms.", "\(x^2+5x+6\) has three terms.", "Therefore it is a trinomial."], "confusing degree with number of terms.", 1),
        item(r"What is the leading coefficient of \(-3x^2+7x+5\)?", r"\(-3\)", [r"\(7\)", r"\(5\)", r"\(2\)"], ["The leading term is the highest-degree term.", "The highest-degree term is \(-3x^2\).", "Its coefficient is \(-3\)."], "choosing the largest positive coefficient.", 1),

        item(r"Add \((2x^2+3x-5)+(x^2-7x+4)\).", r"\(3x^2-4x-1\)", [r"\(3x^2+10x-1\)", r"\(2x^4-4x-1\)", r"\(x^2-4x+9\)"], ["Combine \(x^2\)-terms: \(2x^2+x^2=3x^2\).", "Combine \(x\)-terms: \(3x-7x=-4x\).", "Combine constants: \(-5+4=-1\)."], "adding unlike terms or losing negative signs.", 2),
        item(r"Subtract: \((4x^2-2x+1)-(x^2+5x-6)\).", r"\(3x^2-7x+7\)", [r"\(3x^2+3x-5\)", r"\(5x^2+3x-5\)", r"\(3x^2-7x-5\)"], ["Distribute the subtraction: \(4x^2-2x+1-x^2-5x+6\).", "Combine like terms.", "The result is \(3x^2-7x+7\)."], "not distributing the negative sign to every term in the second polynomial.", 3),
        item(r"Multiply \(3x(2x^2-x+4)\).", r"\(6x^3-3x^2+12x\)", [r"\(6x^2-3x+12\)", r"\(5x^3-3x^2+7x\)", r"\(6x^3-3x+12x\)"], ["Distribute \(3x\) to each term.", "\(3x\cdot2x^2=6x^3\), \(3x\cdot(-x)=-3x^2\), and \(3x\cdot4=12x\).", "The product is \(6x^3-3x^2+12x\)."], "forgetting to add exponents when multiplying variable factors.", 2),
        item(r"Multiply \((x+2)(x+5)\).", r"\(x^2+7x+10\)", [r"\(x^2+10\)", r"\(x^2+3x+10\)", r"\(2x+7\)"], ["Multiply every term by every term.", "The middle products are \(5x\) and \(2x\).", "Combine to get \(x^2+7x+10\)."], "multiplying only first and last terms.", 2),
        item(r"Multiply \((x-3)(x+4)\).", r"\(x^2+x-12\)", [r"\(x^2-7x-12\)", r"\(x^2+x+12\)", r"\(x^2-12\)"], ["Compute first: \(x^2\).", "Compute outer and inner: \(4x-3x=x\).", "Compute last: \(-3)(4)=-12\), so the result is \(x^2+x-12\)."], "dropping the middle term or the negative sign.", 2),

        item(r"Factor \(x^2+5x+6\).", r"\((x+2)(x+3)\)", [r"\((x+1)(x+6)\)", r"\((x-2)(x-3)\)", r"\((x+5)(x+6)\)"], ["Find two numbers that multiply to 6.", "They must also add to 5; 2 and 3 work.", "So the factorization is \((x+2)(x+3)\)."], "using factors that multiply correctly but do not add to the middle coefficient.", 2),
        item(r"Factor \(x^2-7x+12\).", r"\((x-3)(x-4)\)", [r"\((x+3)(x+4)\)", r"\((x-6)(x-2)\)", r"\((x-12)(x+1)\)"], ["Find numbers that multiply to 12 and add to \(-7\).", "The numbers are \(-3\) and \(-4\).", "So the factorization is \((x-3)(x-4)\)."], "getting the signs wrong when the middle term is negative.", 2),
        item(r"Factor \(x^2+x-12\).", r"\((x+4)(x-3)\)", [r"\((x-4)(x+3)\)", r"\((x+6)(x-2)\)", r"\((x-12)(x+1)\)"], ["The factors of \(-12\) must have opposite signs.", "The pair 4 and \(-3\) multiplies to \(-12\) and adds to 1.", "So the factorization is \((x+4)(x-3)\)."], "checking multiplication but not the sum.", 3),
        item(r"Factor \(x^2-9\).", r"\((x-3)(x+3)\)", [r"\((x-9)(x+1)\)", r"\((x-3)^2\)", r"\((x+9)(x-1)\)"], ["Recognize a difference of squares.", "\(x^2-9=x^2-3^2\).", "The factorization is \((x-3)(x+3)\)."], "treating a difference of squares as a repeated binomial.", 2),
        item(r"Which trinomial is not factorable over the integers?", r"\(x^2+x+1\)", [r"\(x^2+5x+6\)", r"\(x^2-9\)", r"\(x^2-7x+12\)"], ["For \(x^2+x+1\), factors of 1 are 1 and 1.", "Their sum is 2, not 1.", "So it does not factor over the integers."], "assuming every trinomial has integer factors.", 3),

        item(r"What value is not allowed in \(\frac{x+2}{x-5}\)?", r"\(5\)", [r"\(-2\)", r"\(0\)", r"\(-5\)"], ["The denominator cannot equal zero.", "Set \(x-5=0\).", "Solve to get \(x=5\), so 5 is not allowed."], "using the numerator to find restrictions.", 1),
        item(r"Simplify \(\frac{x^2-16}{x-4}\), with the restriction \(x\ne4\).", r"\(x+4\)", [r"\(x-4\)", r"\(x^2+4\)", r"\(1\)"], ["Factor the numerator: \(x^2-16=(x-4)(x+4)\).", "Cancel the common factor \(x-4\), keeping the restriction.", "The simplified expression is \(x+4\)."], "forgetting the difference-of-squares factorization.", 2),
        item(r"Why does \(\frac{x^2-16}{x-4}\) still have the restriction \(x\ne4\) after simplifying?", "The original denominator would be zero at \(x=4\).", ["The numerator is always zero.", "All rational expressions forbid \(x=0\).", "The simplified expression has no variables."], ["Restrictions come from the original denominator.", "At \(x=4\), \(x-4=0\).", "So \(x=4\) remains excluded even after cancellation."], "checking only the simplified expression and forgetting the original denominator.", 3),
        item(r"Which cancellation is valid?", r"\(\frac{3x(x+2)}{6x}=\frac{x+2}{2}\), \(x\ne0\)", [r"\(\frac{x+6}{x}=6\)", r"\(\frac{x+2}{2}=x\)", r"\(\frac{x^2+4}{x}=x+4\)"], ["Only common factors may cancel.", "In \(\frac{3x(x+2)}{6x}\), the factor \(3x\) cancels with part of \(6x\).", "The result is \(\frac{x+2}{2}\), with \(x\ne0\)."], "canceling terms that are added instead of factors that are multiplied.", 3),
        item(r"If \(C\) dollars are shared equally among \(n\) people, which expression gives cost per person?", r"\(\frac{C}{n}\)", [r"\(\frac{n}{C}\)", r"\(Cn\)", r"\(C+n\)"], ["Cost per person means total cost divided by number of people.", "The total is \(C\) and the number of people is \(n\).", "The expression is \(\frac{C}{n}\)."], "reversing numerator and denominator in a rate expression.", 1),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Expressions & Polynomials Mastery course (MCQ only)."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()
        course = Course.objects.create(
            title=COURSE["title"],
            slug=COURSE["slug"],
            program=COURSE["program"],
            subject=COURSE["subject"],
            description=COURSE["description"],
        )

        for index, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content.strip(), order=index)

        for question_data in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course,
                qtype="mcq",
                text=question_data["text"],
                difficulty=question_data["difficulty"],
                explanation=question_data["explanation"],
            )
            for text, is_correct in question_data["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=is_correct)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
