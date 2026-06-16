"""
Seed a GED Algebra course for systems of equations and linear modeling.

Run:
    python manage.py seed_ged_algebra_systems_linear_modeling
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
    "title": "GED Algebra: Systems of Equations & Linear Modeling Mastery",
    "slug": "ged-algebra-systems-linear-modeling",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Mathematical Reasoning algebra course on systems of equations, "
        "graphical intersections, checking ordered-pair solutions, substitution, "
        "elimination, no-solution and infinitely-many-solution cases, and real-world "
        "linear modeling. Students learn to compare plans, write break-even equations, "
        "translate ticket and number problems, and choose a reliable solving strategy."
    ),
    "lessons": [
        (
            "1. What a System of Equations Means",
            r"""
A **system of equations** is a set of equations that must be true at the same time. In algebra, a system usually asks for the ordered pair \((x,y)\) that satisfies both equations.

For example:
\[
y=x+1,\qquad y=-x+5.
\]
The solution is not just a value of \(x\) or a value of \(y\). It is the point where both equations agree.

[[figure:system_graph|The solution of a system is the point where both line graphs meet.]]

In real life, a system can compare two plans, two prices, two quantities, or two conditions. If Plan A and Plan B cost the same at a certain number of months, that number is a system solution.

Common misconception: thinking each equation has its own separate answer. A system answer must work in every equation at the same time.

Academic habit: write the answer as an ordered pair unless the context asks for only one quantity.

[[check:If two line graphs intersect at \((4,7)\), what is the solution of the system?|(4,7);;\(4,7\)|The intersection point is the ordered pair that satisfies both equations.]]
            """,
        ),
        (
            "2. Reading Intersections from Graphs",
            r"""
Graphically, each line shows all ordered pairs that make its equation true. The intersection point lies on both lines, so it satisfies both equations.

If two lines cross once, the system has exactly one solution. If two different lines are parallel, they never cross, so there is no solution. If the two equations describe the same line, every point on the line works, so there are infinitely many solutions.

When reading a graph:
1. Locate the crossing point.
2. Read the \(x\)-coordinate first.
3. Read the \(y\)-coordinate second.
4. Write the answer as \((x,y)\).

GED graphs may use scales larger than 1. Always read the axis labels and tick marks before deciding the coordinates.

Common misconception: reporting the crossing as \((y,x)\). Ordered pairs always use horizontal coordinate first, vertical coordinate second.

Academic habit: say "over, then up or down" when reading an intersection.
            """,
        ),
        (
            "3. Checking an Ordered-Pair Solution",
            r"""
An ordered pair solves a system only if it makes **both** equations true.

Example: Check whether \((2,3)\) solves:
\[
y=x+1,\qquad y=-x+5.
\]
First equation:
\[
3=2+1
\]
is true. Second equation:
\[
3=-2+5
\]
is also true. Therefore \((2,3)\) solves the system.

If a point works in one equation but not the other, it is not a system solution.

Checking is especially useful after solving by substitution or elimination. It catches arithmetic mistakes and reversed coordinate errors.

Common misconception: substituting only into one equation. A system has more than one condition, so one check is not enough.

Academic habit: after finding a solution, substitute it into both original equations.
            """,
        ),
        (
            "4. Solving by Substitution",
            r"""
Substitution is often best when one equation already has a variable isolated, such as \(y=x+1\) or \(x=2y\).

[[figure:systems_substitution_flow|Substitution replaces one variable with an equivalent expression from another equation.]]

Example:
\[
y=x+1,\qquad y=-x+5.
\]
Because both expressions equal \(y\), set them equal:
\[
x+1=-x+5.
\]
Solve:
\[
2x=4,\qquad x=2.
\]
Substitute \(x=2\) into \(y=x+1\):
\[
y=2+1=3.
\]
The solution is \((2,3)\).

Substitution turns two-variable work into a one-variable equation.

Common misconception: stopping after finding \(x\). The system solution needs both coordinates.

Academic habit: when you find one variable, immediately return to an original equation to find the other variable.
            """,
        ),
        (
            "5. Solving by Elimination",
            r"""
Elimination is often best when adding or subtracting the equations can cancel one variable.

[[figure:systems_elimination_balance|Elimination adds or subtracts equations so one variable disappears.]]

Example:
\[
2x+y=10,\qquad x-y=2.
\]
Add the equations:
\[
(2x+y)+(x-y)=10+2.
\]
The \(+y\) and \(-y\) cancel:
\[
3x=12,\qquad x=4.
\]
Substitute into \(x-y=2\):
\[
4-y=2,\qquad y=2.
\]
The solution is \((4,2)\).

Sometimes you must multiply one or both equations before eliminating. The goal is to create opposite coefficients, such as \(+2y\) and \(-2y\).

Common misconception: adding equations but forgetting to add both sides. Whatever operation you do to the left side must also happen to the right side.

Academic habit: line up like terms vertically before adding or subtracting equations.
            """,
        ),
        (
            "6. No Solution and Infinitely Many Solutions",
            r"""
Some systems do not have exactly one intersection.

If two lines have the same slope but different y-intercepts, they are parallel:
\[
y=2x+1,\qquad y=2x-3.
\]
They never meet, so the system has **no solution**.

If two equations describe the same line, every point on that line satisfies both equations. The system has **infinitely many solutions**:
\[
y=3x+2,\qquad 2y=6x+4.
\]
The second equation becomes \(y=3x+2\) after dividing by 2.

If two lines have different slopes, they cross once and have exactly one solution.

Common misconception: assuming every system must have one ordered-pair solution. Parallel lines and identical lines are special cases.

Academic habit: compare slopes and intercepts after rewriting equations into slope-intercept form.
            """,
        ),
        (
            "7. Writing Systems from Word Problems",
            r"""
A word problem becomes a system when two conditions must be true at the same time.

Example: Adult tickets cost 12 dollars, child tickets cost 8 dollars. A family buys 10 tickets for 96 dollars. Let \(a\) be adult tickets and \(c\) be child tickets.

The total number of tickets gives:
\[
a+c=10.
\]
The total cost gives:
\[
12a+8c=96.
\]
Together, these equations form a system.

The variables must be defined clearly. If \(a\) means adult tickets in one equation, it must mean adult tickets in the other equation too.

Common misconception: writing only the money equation or only the count equation. A system needs both relationships.

Academic habit: underline the two totals in a word problem. They often become the two equations.
            """,
        ),
        (
            "8. Linear Models: Slope and Starting Value",
            r"""
A linear model often has the form:
\[
y=mx+b.
\]
Here \(m\) is the rate of change and \(b\) is the starting value.

Example: A rental company charges a 30 dollar setup fee plus 12 dollars per hour. If \(h\) is hours and \(C\) is cost, the model is:
\[
C=12h+30.
\]
The slope is 12 dollars per hour. The starting value is 30 dollars.

[[figure:slope_types|Slope describes direction and rate of change in a linear model.]]

Linear models can be compared. If two plans have different starting values and different rates, a system can find when they are equal.

Common misconception: switching the fixed fee and the rate. The fixed fee is the y-intercept; the repeated charge is the slope.

Academic habit: identify "starts at" and "per" language before writing the equation.
            """,
        ),
        (
            "9. Break-Even and Comparison Problems",
            r"""
A break-even point is where two costs, earnings, or quantities are equal.

[[figure:break_even_model_graph|The break-even point is where the two linear models have the same value.]]

Example: Plan A costs \(20+5m\). Plan B costs \(50+2m\), where \(m\) is months. To find when they cost the same:
\[
20+5m=50+2m.
\]
Subtract \(2m\):
\[
20+3m=50.
\]
Subtract 20:
\[
3m=30,\qquad m=10.
\]
At 10 months, the plans cost the same.

Before 10 months, one plan may be cheaper. After 10 months, the plan with the smaller rate may become cheaper.

Common misconception: choosing the plan with the lower starting cost without considering the monthly rate.

Academic habit: for comparison problems, write one expression for each option, then set them equal only when the question asks when they match.
            """,
        ),
        (
            "10. Ticket, Number, and Total-Value Systems",
            r"""
Many GED systems use a total count and a total value.

Ticket example:
\[
a+c=10,\qquad 12a+8c=96.
\]
The first equation counts tickets. The second equation counts dollars.

Number example: Two numbers have a sum of 18 and a difference of 4. Let \(x\) be the larger number and \(y\) be the smaller number:
\[
x+y=18,\qquad x-y=4.
\]
Add the equations:
\[
2x=22,\qquad x=11.
\]
Then \(y=7\).

In total-value problems, keep units consistent. You cannot add tickets and dollars in the same equation.

Common misconception: mixing count and value terms in one equation without coefficients.

Academic habit: name what each equation measures: count, cost, distance, or value.
            """,
        ),
        (
            "11. Systems from Tables and Graphs",
            r"""
A system may appear as a table, graph, or verbal description rather than two equations.

From a table, create a linear model by finding the starting value and rate of change. For points:
\[
(0,10),(1,15),(2,20),
\]
the starting value is 10 and the rate of change is 5, so the model is:
\[
y=5x+10.
\]

If another model is \(y=25\), the intersection solves:
\[
5x+10=25.
\]
Then \(5x=15\), so \(x=3\), and \(y=25\).

[[figure:function_table_line|A table can become a line model when the rate of change is constant.]]

Graphs show the solution visually. Tables show it numerically. Equations show it symbolically. All three forms can describe the same system.

Common misconception: thinking a system must be written as two equations at the start. GED problems often require you to build the equations first.

Academic habit: translate every representation into "starting value plus rate times input" when the relationship is linear.
            """,
        ),
        (
            "12. Choosing a Method and Checking Reasonableness",
            r"""
Choose the method that matches the structure.

Use graphing when the intersection is easy to read and exact enough. Use substitution when a variable is already isolated. Use elimination when coefficients are lined up or can be made opposites.

A final answer should pass three checks:
1. It works in both equations.
2. It answers the question being asked.
3. It makes sense in context.

For example, a system about tickets should not produce a negative number of tickets. A break-even month should not be reported as a cost unless the question asks for total cost.

If a solution is \((4,2)\), read it in context. It might mean 4 adult tickets and 2 child tickets, or 4 months and 2 dollars, depending on variable definitions.

Common misconception: solving correctly but answering the wrong quantity. The pair is useful only when interpreted with labels.

Academic habit: write a short sentence after the ordered pair: "This means ..." That final sentence catches many GED word-problem mistakes.
            """,
        ),
    ],
    "mcqs": [
        item(r"Which ordered pair satisfies both \(y=x+1\) and \(y=-x+5\)?", r"\((2,3)\)", [r"\((3,2)\)", r"\((1,4)\)", r"\((5,0)\)"], ["Test \((2,3)\) in the first equation: \(3=2+1\).", "Test it in the second equation: \(3=-2+5\).", "Because it works in both equations, \((2,3)\) is the solution."], "checking only one equation or reversing the ordered pair.", 2),
        item(r"Does \((2,3)\) solve the system \(y=x+1\) and \(y=-x+5\)?", "Yes, it satisfies both equations.", ["No, it satisfies neither equation.", "It satisfies only the first equation.", "It satisfies only the second equation."], ["Substitute into \(y=x+1\): \(3=2+1\), true.", "Substitute into \(y=-x+5\): \(3=-2+5\), true.", "The point solves the system because both statements are true."], "stopping after only one substitution check.", 1),
        item(r"If two line graphs intersect at \((4,7)\), what is the solution of the system?", r"\((4,7)\)", [r"\((7,4)\)", r"\(4\)", r"\(7\)"], ["A system solution is the intersection point.", "An intersection is written as an ordered pair.", "The solution is \((4,7)\)."], "reporting only one coordinate or reversing the order.", 1),
        item(r"What does the solution of a system of two linear equations represent on a graph?", "The point where the two lines intersect", ["The slope of the steeper line", "The y-intercept of the first line", "Any point on either line"], ["Each line contains points that satisfy one equation.", "The intersection lies on both lines.", "Therefore the intersection is the system solution."], "thinking any point on one line solves the whole system.", 1),
        item("Use the graph.\n\n[[figure:system_graph|Two lines intersecting at a solution point]]\n\nWhat does the red point represent?", "The ordered pair that satisfies both equations", ["Only the x-intercept", "Only the slope", "A point that satisfies neither equation"], ["The red point is where the lines cross.", "A crossing point lies on both lines.", "So it satisfies both equations."], "reading the point as decoration instead of the shared solution.", 1),

        item(r"Solve the system \(y=x+1\) and \(y=-x+5\).", r"\((2,3)\)", [r"\((3,2)\)", r"\((1,2)\)", r"\((4,1)\)"], ["Set the expressions for \(y\) equal: \(x+1=-x+5\).", "Solve \(2x=4\), so \(x=2\).", "Substitute into \(y=x+1\), giving \(y=3\)."], "finding \(x\) but not finding \(y\).", 2),
        item(r"Solve the system \(y=2x+3\) and \(y=x+8\).", r"\((5,13)\)", [r"\((13,5)\)", r"\((3,9)\)", r"\((8,19)\)"], ["Set \(2x+3=x+8\).", "Subtract \(x\) and 3 to get \(x=5\).", "Substitute: \(y=2(5)+3=13\)."], "switching x and y in the final ordered pair.", 2),
        item(r"Solve the system \(x+y=10\) and \(y=2x+1\).", r"\((3,7)\)", [r"\((7,3)\)", r"\((4,6)\)", r"\((2,5)\)"], ["Substitute \(y=2x+1\) into \(x+y=10\).", "Solve \(x+2x+1=10\), so \(3x=9\) and \(x=3\).", "Then \(y=2(3)+1=7\)."], "substituting correctly but reversing the coordinates.", 2),
        item(r"Solve the system \(y=4x-1\) and \(y=11\).", r"\((3,11)\)", [r"\((11,3)\)", r"\((2,7)\)", r"\((4,11)\)"], ["Since \(y=11\), set \(4x-1=11\).", "Solve \(4x=12\), so \(x=3\).", "The ordered pair is \((3,11)\)."], "using \(y=11\) as the x-value.", 2),
        item(r"Solve the system \(y=3x\) and \(x+y=20\).", r"\((5,15)\)", [r"\((15,5)\)", r"\((4,12)\)", r"\((10,10)\)"], ["Substitute \(y=3x\) into \(x+y=20\).", "Solve \(x+3x=20\), so \(4x=20\) and \(x=5\).", "Then \(y=3(5)=15\)."], "stopping at \(x=5\) without finding \(y\).", 2),
        item(r"Solve the system \(x=2y\) and \(x+y=18\).", r"\((12,6)\)", [r"\((6,12)\)", r"\((9,9)\)", r"\((10,8)\)"], ["Substitute \(x=2y\) into \(x+y=18\).", "Solve \(2y+y=18\), so \(3y=18\) and \(y=6\).", "Then \(x=2(6)=12\)."], "writing the variables in the wrong order.", 2),
        item(r"A student solves a system and finds \(x=2\). What should the student do next?", "Substitute \(x=2\) into an original equation to find \(y\).", ["Stop because a system needs only x.", "Change \(x\) to \(y\).", "Graph a new unrelated line."], ["A system solution is an ordered pair.", "Finding \(x\) gives only the first coordinate.", "Substitute back to find the second coordinate."], "treating a partial answer as the full ordered pair.", 1),

        item(r"Solve by elimination: \(x+y=9\) and \(x-y=1\).", r"\((5,4)\)", [r"\((4,5)\)", r"\((9,1)\)", r"\((1,9)\)"], ["Add the equations: \(2x=10\).", "Solve \(x=5\).", "Substitute into \(x+y=9\), so \(y=4\)."], "adding x-values and y-values without canceling.", 2),
        item(r"Solve by elimination: \(2x+y=10\) and \(x-y=2\).", r"\((4,2)\)", [r"\((2,4)\)", r"\((3,4)\)", r"\((5,0)\)"], ["Add the equations so \(y\) cancels.", "Get \(3x=12\), so \(x=4\).", "Substitute into \(x-y=2\): \(4-y=2\), so \(y=2\)."], "forgetting to solve for the second coordinate.", 2),
        item(r"Solve by elimination: \(x+2y=10\) and \(x-2y=2\).", r"\((6,2)\)", [r"\((2,6)\)", r"\((4,3)\)", r"\((8,1)\)"], ["Add the equations: \(2x=12\).", "Solve \(x=6\).", "Substitute: \(6+2y=10\), so \(2y=4\), \(y=2\)."], "canceling x instead of y without a plan.", 2),
        item(r"Solve by elimination: \(3x+2y=18\) and \(3x-2y=6\).", r"\((4,3)\)", [r"\((3,4)\)", r"\((2,6)\)", r"\((6,0)\)"], ["Add the equations: \(6x=24\).", "Solve \(x=4\).", "Substitute into \(3x+2y=18\): \(12+2y=18\), so \(y=3\)."], "forgetting that adding cancels the y-terms.", 3),
        item(r"Solve \(2x+y=13\) and \(x-y=2\).", r"\((5,3)\)", [r"\((3,5)\)", r"\((4,5)\)", r"\((6,1)\)"], ["Add the equations: \(3x=15\).", "Solve \(x=5\).", "Substitute into \(x-y=2\): \(5-y=2\), so \(y=3\)."], "subtracting equations when addition already cancels \(y\).", 2),
        item(r"In the system \(2x+y=11\) and \(x-y=4\), which variable cancels if the equations are added?", r"\(y\)", [r"\(x\)", "Both variables", "No variable"], ["The first equation has \(+y\).", "The second equation has \(-y\).", "Adding gives \(+y-y=0\), so \(y\) cancels."], "looking only at the x-coefficients.", 1),
        item(r"When is elimination usually convenient?", "When one variable has opposite coefficients or can be made opposite", ["Only when both equations are graphed", "Only when both slopes are positive", "Only when there are no constants"], ["Elimination works by canceling one variable.", "Opposite coefficients cancel when equations are added.", "So aligned opposite coefficients make elimination efficient."], "choosing a method based on appearance rather than structure.", 1),

        item(r"How many solutions does \(y=2x+1\) and \(y=2x-3\) have?", "No solution", ["One solution", "Infinitely many solutions", "Two solutions"], ["Both lines have slope 2.", "Their y-intercepts are different.", "They are parallel, so they never intersect."], "assuming every system has one solution.", 2),
        item(r"How many solutions does \(y=3x+2\) and \(2y=6x+4\) have?", "Infinitely many solutions", ["No solution", "One solution", "Exactly two solutions"], ["Divide the second equation by 2.", "It becomes \(y=3x+2\).", "Both equations describe the same line, so every point on that line works."], "thinking different-looking equations must be different lines.", 3),
        item(r"Which pair of lines has exactly one solution?", r"\(y=x+1\) and \(y=-x+5\)", [r"\(y=2x+1\) and \(y=2x-3\)", r"\(y=3x+2\) and \(2y=6x+4\)", r"\(y=-4x+1\) and \(2y=-8x+2\)"], ["Lines with different slopes intersect once.", "The slopes \(1\) and \(-1\) are different.", "Therefore \(y=x+1\) and \(y=-x+5\) have one solution."], "choosing parallel or identical lines.", 2),
        item(r"Two lines have the same slope and different y-intercepts. What kind of system is this?", "No solution", ["One solution", "Infinitely many solutions", "Cannot be determined from slope and intercept"], ["Same slope means the lines are parallel or identical.", "Different y-intercepts mean they are not the same line.", "Parallel distinct lines have no solution."], "thinking same slope means same line automatically.", 2),
        item(r"Which system represents the same line twice?", r"\(y=4x-2\) and \(2y=8x-4\)", [r"\(y=4x-2\) and \(y=4x+3\)", r"\(y=4x-2\) and \(y=-4x-2\)", r"\(y=4x-2\) and \(y=2x-4\)"], ["Divide \(2y=8x-4\) by 2.", "The result is \(y=4x-2\).", "Both equations describe the same line."], "looking only at whether the equations look different.", 3),

        item(r"A taxi charges a \(5\) dollar base fee plus \(2\) dollars per mile. Which equation models cost \(C\) for \(m\) miles?", r"\(C=2m+5\)", [r"\(C=5m+2\)", r"\(C=7m\)", r"\(C=2m-5\)"], ["The per-mile charge is the rate, or slope, 2.", "The base fee is the starting value, 5.", "The model is \(C=2m+5\)."], "switching the fixed fee and the rate.", 1),
        item(r"Plan A costs \(20+5m\). Plan B costs \(50+2m\). At how many months do they cost the same?", r"\(10\)", [r"\(5\)", r"\(15\)", r"\(30\)"], ["Set the costs equal: \(20+5m=50+2m\).", "Subtract \(2m\) and 20 to get \(3m=30\).", "Solve \(m=10\)."], "choosing the lower starting cost without solving.", 2),
        item(r"Plan A costs \(8+4x\). Plan B costs \(20+2x\). At what \(x\)-value are the costs equal?", r"\(6\)", [r"\(4\)", r"\(12\)", r"\(14\)"], ["Set \(8+4x=20+2x\).", "Subtract \(2x\): \(8+2x=20\).", "Subtract 8 and divide by 2: \(x=6\)."], "subtracting constants but not variable terms.", 2),
        item(r"Adult tickets cost \(\$12\), child tickets cost \(\$8\), and 10 tickets cost \(\$96\). Which system matches the situation?", r"\(a+c=10,\ 12a+8c=96\)", [r"\(12+c=10,\ a+8c=96\)", r"\(a+c=96,\ 12a+8c=10\)", r"\(12a+8c=10,\ a+c=96\)"], ["One equation counts tickets: \(a+c=10\).", "The other equation counts dollars: \(12a+8c=96\).", "Together they match both conditions."], "mixing the ticket total and money total.", 2),
        item(r"Solve \(a+c=10\) and \(12a+8c=96\).", r"\(a=4,\ c=6\)", [r"\(a=6,\ c=4\)", r"\(a=8,\ c=2\)", r"\(a=2,\ c=8\)"], ["From \(a+c=10\), \(c=10-a\).", "Substitute: \(12a+8(10-a)=96\), so \(4a+80=96\).", "Solve \(a=4\), then \(c=6\)."], "reversing adult and child counts.", 3),
        item(r"Two numbers have a sum of 18 and a difference of 4. What are the numbers?", r"\(11\) and \(7\)", [r"\(9\) and \(9\)", r"\(14\) and \(4\)", r"\(10\) and \(8\)"], ["Let \(x+y=18\) and \(x-y=4\).", "Add equations: \(2x=22\), so \(x=11\).", "Then \(y=7\)."], "using the difference as one of the numbers.", 2),
        item(r"A setup fee is \(\$30\) plus \(\$12\) per hour. Which model gives total cost \(C\) for \(h\) hours?", r"\(C=12h+30\)", [r"\(C=30h+12\)", r"\(C=42h\)", r"\(C=12h-30\)"], ["The hourly charge is the rate, 12.", "The setup fee is the starting value, 30.", "The model is \(C=12h+30\)."], "switching the fixed fee and per-hour rate.", 1),
        item(r"In a model \(C=15x+40\), what does 40 usually represent?", "The starting cost or fixed fee", ["The rate per unit", "The number of units", "The break-even point"], ["In \(y=mx+b\), \(b\) is the starting value.", "Here \(b=40\).", "So 40 represents the fixed or starting cost."], "choosing the slope instead of the intercept.", 1),
        item("Use the graph.\n\n[[figure:break_even_model_graph|Two linear models crossing at a break-even point]]\n\nWhat does the intersection of the two cost lines mean?", "The two plans have the same total cost there.", ["Both plans have zero cost there.", "One plan has no slope there.", "The units are no longer needed there."], ["The vertical axis shows total cost.", "At an intersection, both models have the same \(x\) and same cost.", "So the plans cost the same at that point."], "thinking the intersection always means zero.", 1),
        item(r"A table has \((0,10),(1,15),(2,20)\). Which linear model fits?", r"\(y=5x+10\)", [r"\(y=10x+5\)", r"\(y=15x+10\)", r"\(y=5x\)"], ["The starting value is 10 because \(x=0\) gives \(y=10\).", "The output increases by 5 for each increase of 1 in \(x\).", "The model is \(y=5x+10\)."], "using the starting value as the slope.", 2),
        item(r"Which situation most clearly calls for a system of equations?", "Two plans are compared to find when their total costs are equal.", ["A single number is doubled.", "A rectangle's area is found from length and width.", "A percent is converted to a decimal."], ["A system uses two relationships at the same time.", "Comparing two plans gives two cost expressions.", "Setting them equal creates a system-like comparison."], "using a system when one equation is enough.", 1),

        item(r"When is substitution usually the best first choice?", "When one equation already has \(x=\) or \(y=\)", ["When both equations have opposite coefficients", "When no variable is isolated", "Only when the graph is provided"], ["Substitution replaces one variable with an expression.", "That is easiest when a variable is already isolated.", "Equations like \(y=2x+3\) are ready for substitution."], "choosing substitution even when elimination is simpler.", 1),
        item(r"When is elimination usually the best first choice?", "When adding or subtracting equations can cancel a variable", ["When one equation is already \(y=\)", "When the answer choices are decimals", "Only when both slopes are positive"], ["Elimination is built around canceling one variable.", "Opposite coefficients cancel by addition.", "So aligned coefficients suggest elimination."], "choosing a method based on the signs of the answers.", 1),
        item(r"How do you check whether \((4,2)\) solves \(2x+y=10\) and \(x-y=2\)?", "Substitute \(x=4,y=2\) into both equations.", ["Substitute only into the first equation.", "Check whether \(4+2=10\).", "Graph a different system."], ["A system solution must satisfy both equations.", "Use \(x=4\) and \(y=2\) in each original equation.", "If both are true, the ordered pair is correct."], "checking only one equation.", 1),
        item(r"Solve \(x+y=12\) and \(x=2y\).", r"\((8,4)\)", [r"\((4,8)\)", r"\((6,6)\)", r"\((10,2)\)"], ["Substitute \(x=2y\) into \(x+y=12\).", "Solve \(2y+y=12\), so \(3y=12\), \(y=4\).", "Then \(x=8\), so the solution is \((8,4)\)."], "writing y first in the ordered pair.", 2),
        item(r"Solve \(y=3x\) and \(y=x+10\).", r"\((5,15)\)", [r"\((15,5)\)", r"\((10,30)\)", r"\((4,12)\)"], ["Set \(3x=x+10\).", "Solve \(2x=10\), so \(x=5\).", "Then \(y=3(5)=15\)."], "setting x-values equal incorrectly or reversing coordinates.", 2),
        item(r"Solve \(4x+y=19\) and \(y=3\).", r"\((4,3)\)", [r"\((3,4)\)", r"\((5,3)\)", r"\((4,19)\)"], ["Substitute \(y=3\) into \(4x+y=19\).", "Solve \(4x+3=19\), so \(4x=16\), \(x=4\).", "The solution is \((4,3)\)."], "using the given y-value as the x-coordinate.", 1),
        item(r"What does a break-even solution usually mean in a cost comparison?", "The two options have the same total cost.", ["The cheaper option is always first.", "The cost is zero.", "The rates are both zero."], ["Break-even means equality between two models.", "In cost problems, equal models mean equal total cost.", "The solution gives where the costs match."], "thinking break-even means no money is spent.", 1),
        item(r"Which system has no solution?", r"\(y=5x+1\) and \(y=5x-4\)", [r"\(y=5x+1\) and \(y=-5x+1\)", r"\(y=5x+1\) and \(2y=10x+2\)", r"\(y=x\) and \(y=2x+1\)"], ["No solution happens for same slope and different intercepts.", "The equations \(y=5x+1\) and \(y=5x-4\) have the same slope 5.", "Their intercepts differ, so the lines are parallel."], "choosing identical lines or lines with different slopes.", 2),
        item(r"Which system has infinitely many solutions?", r"\(y=2x+3\) and \(2y=4x+6\)", [r"\(y=2x+3\) and \(y=2x-3\)", r"\(y=2x+3\) and \(y=-2x+3\)", r"\(y=x+3\) and \(y=2x+3\)"], ["Divide \(2y=4x+6\) by 2.", "It becomes \(y=2x+3\).", "The two equations are the same line."], "thinking same slope alone is enough; the intercept must also match.", 3),
        item(r"The point \((3,2)\) is tested in these equations. Which equation is NOT satisfied?", r"\(y=3x-1\)", [r"\(x+y=5\)", r"\(2x+y=8\)", r"\(x-y=1\)"], ["For \((3,2)\), \(x=3\) and \(y=2\).", "Check \(y=3x-1\): \(2=3(3)-1=8\), which is false.", "The other equations are true."], "substituting the coordinates in reverse order.", 2),
        item(r"Two linear models have the same rate but different starting values. What happens when they are compared?", "They never have the same value.", ["They always intersect once.", "They are the same model.", "They intersect at \(x=0\) only."], ["Same rate means the lines have the same slope.", "Different starting values mean different intercepts.", "The lines are parallel, so they never meet."], "thinking same rate means same total value.", 2),
        item(r"Solve \(x+y=15\) and \(y=x+3\).", r"\((6,9)\)", [r"\((9,6)\)", r"\((5,10)\)", r"\((7,8)\)"], ["Substitute \(y=x+3\) into \(x+y=15\).", "Solve \(x+x+3=15\), so \(2x=12\) and \(x=6\).", "Then \(y=6+3=9\), so the solution is \((6,9)\)."], "finding the two values but reversing x and y.", 2),
        item(r"Plan A costs \(100+20x\). Plan B costs \(40+35x\). At what \(x\)-value do they cost the same?", r"\(4\)", [r"\(6\)", r"\(8\)", r"\(60\)"], ["Set the costs equal: \(100+20x=40+35x\).", "Subtract 20x and 40 to get \(60=15x\).", "Solve \(x=4\)."], "subtracting in the wrong direction and getting a negative or using the cost difference as the answer.", 2),
        item(r"A problem says there are 7 adult and child tickets total. If \(a\) is adult tickets and \(c\) is child tickets, which equation represents the count?", r"\(a+c=7\)", [r"\(7a+c=0\)", r"\(a+c=0\)", r"\(ac=7\)"], ["The total count combines adult tickets and child tickets.", "Adult tickets plus child tickets equals 7.", "The count equation is \(a+c=7\)."], "multiplying the ticket counts instead of adding them.", 1),
        item(r"In an ordered pair \((x,y)\), which coordinate is written first?", "The x-coordinate", ["The y-coordinate", "The slope", "The y-intercept"], ["Ordered pairs are written \((x,y)\).", "The first coordinate is horizontal, or x.", "The second coordinate is vertical, or y."], "writing graph answers as \((y,x)\).", 1),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Systems of Equations & Linear Modeling Mastery course."

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
