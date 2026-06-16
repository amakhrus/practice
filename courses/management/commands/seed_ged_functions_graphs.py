"""
Seed a complete GED Math mastery course for functions and graphs.

Run:
    python manage.py seed_ged_functions_graphs
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
    "title": "GED Algebra: Functions & Graphs Mastery",
    "slug": "ged-algebra-functions-graphs",
    "program": "GED",
    "subject": "math",
    "description": (
        "A focused GED Mathematical Reasoning course on functions, graphs, slope, "
        "linear equations, coordinate interpretation, and graph-based reasoning. "
        "Students learn how to move between tables, rules, equations, and graphs; "
        "evaluate function notation; interpret slope as rate of change; graph lines "
        "and inequalities; compare functions; and recognize nonlinear patterns. "
        "Lessons use an academic style with clear definitions, worked examples, "
        "visual figures, common-misconception notes, and GED-style practice."
    ),
    "lessons": [
        (
            "1. The Coordinate Plane as a Data Map",
            r"""
The coordinate plane is a precise map for numerical relationships. The horizontal axis is the **x-axis**, the vertical axis is the **y-axis**, and their crossing point is the **origin**, \((0,0)\).

Every point is written as an ordered pair:
\[
(x,y).
\]
The first number tells how far to move left or right. The second number tells how far to move up or down.

[[figure:coordinate_quadrants|The coordinate plane uses signs to locate a point in a quadrant.]]

Quadrant signs are predictable:
- Quadrant I: \(x>0,\ y>0\)
- Quadrant II: \(x<0,\ y>0\)
- Quadrant III: \(x<0,\ y<0\)
- Quadrant IV: \(x>0,\ y<0\)

Points on an axis are not inside any quadrant. A point with \(x=0\) lies on the y-axis, and a point with \(y=0\) lies on the x-axis.

Common misconception: reversing the order. The point \((3,-2)\) means 3 right and 2 down, not 3 up and 2 right.

Academic habit: read coordinates aloud as "across, then up or down." This prevents most coordinate-order mistakes.

[[check:Which coordinate comes first in an ordered pair?|x;;the x-coordinate|The first coordinate is horizontal, along the x-axis.]]
            """,
        ),
        (
            "2. From Tables to Graphs",
            r"""
A table gives ordered pairs. Each row becomes one point on a graph. When the same rule is used for every row, the graph shows the pattern visually.

[[figure:function_table_line|Each row of the table becomes a point on the graph of \(y=2x+1\).]]

For the rule \(y=2x+1\):
- If \(x=-1\), then \(y=2(-1)+1=-1\), so the point is \((-1,-1)\).
- If \(x=0\), then \(y=1\), so the point is \((0,1)\).
- If \(x=1\), then \(y=3\), so the point is \((1,3)\).
- If \(x=2\), then \(y=5\), so the point is \((2,5)\).

When the output changes by the same amount each time \(x\) increases by 1, the relationship is **linear**. Linear relationships graph as straight lines.

Common misconception: treating a table as two separate lists. Each row is a pair, so \(x=1\) must stay attached to its matching \(y\)-value.

Academic habit: when making a graph from a table, write each row as an ordered pair before plotting.
            """,
        ),
        (
            "3. What Makes a Relation a Function",
            r"""
A **relation** is any set of input-output pairs. A **function** is a special relation where each input has exactly one output.

[[figure:function_machine|A function is like a rule machine: one input enters, exactly one output leaves.]]

The rule \(f(x)=2x+1\) is a function because every input gives one output. For example, input 3 gives output 7.

The set \((1,4),(2,5),(3,6)\) is a function because no input is repeated with a different output. The set \((1,4),(1,9),(2,5)\) is not a function because input 1 has two outputs.

On a graph, the **vertical line test** checks whether a graph is a function. If any vertical line touches the graph more than once, one \(x\)-value has more than one \(y\)-value, so the graph is not a function.

Common misconception: repeated outputs are not a problem. Inputs must be unique; outputs may repeat. The pairs \((1,5),(2,5),(3,5)\) still form a function.

Academic habit: always inspect the inputs first. A relation fails to be a function only when the same input points to different outputs.
            """,
        ),
        (
            "4. Function Notation, Domain, and Range",
            r"""
Function notation is a compact way to name a rule. If
\[
f(x)=3x-2,
\]
then \(f(4)\) means "the output of the function when the input is 4."

Evaluate by substituting:
\[
f(4)=3(4)-2=12-2=10.
\]
For a negative input:
\[
f(-2)=3(-2)-2=-6-2=-8.
\]

The **domain** is the set of allowed inputs. The **range** is the set of outputs. If a table has points \((0,1),(1,3),(2,5)\), the domain is \(\{0,1,2\}\) and the range is \(\{1,3,5\}\).

In real-world functions, context may restrict the domain. If \(C(t)=15t\) gives cost for \(t\) hours of tutoring, negative hours do not make sense.

Common misconception: reading \(f(4)\) as \(f \times 4\). The notation is not multiplication; it means evaluate the rule at input 4.

Academic habit: replace every \(x\) in the expression with the input value, including parentheses around negative numbers.
            """,
        ),
        (
            "5. Slope as Rate of Change",
            r"""
**Slope** measures how quickly \(y\) changes compared with \(x\). It is the ratio:
\[
\text{slope}=\frac{\text{change in }y}{\text{change in }x}
=\frac{y_2-y_1}{x_2-x_1}.
\]

[[figure:slope_types|Slope direction tells whether a line rises, falls, stays flat, or is vertical.]]

Worked example: find the slope through \((1,2)\) and \((4,8)\).
\[
m=\frac{8-2}{4-1}=\frac{6}{3}=2.
\]
The line rises 2 units for every 1 unit to the right.

In context, slope is often a rate. If a distance-time graph has slope 60, the rate is 60 miles per hour.

[[figure:rate_graph|On a distance-time graph, slope is speed: miles per hour.]]

Common misconception: reporting the rise only. Slope is rise divided by run, so both changes matter.

Academic habit: keep the point order consistent. If you subtract \(y_2-y_1\) on top, subtract \(x_2-x_1\) in the same order on bottom.
            """,
        ),
        (
            "6. Slope-Intercept Form and Graphing Lines",
            r"""
Most GED line questions use **slope-intercept form**:
\[
y=mx+b.
\]
Here \(m\) is the slope and \(b\) is the y-intercept, the point where the line crosses the y-axis.

[[figure:coord_line|For \(y=2x+1\), start at the y-intercept \((0,1)\), then use slope \(2=\frac{2}{1}\).]]

To graph \(y=2x+1\):
- Plot the y-intercept \((0,1)\).
- Use the slope \(2=\frac{2}{1}\): rise 2 and run 1.
- Plot another point, such as \((1,3)\).
- Draw the line through the points.

For \(y=-3x+4\), the slope is \(-3\) and the y-intercept is 4. A negative slope falls from left to right.

Common misconception: identifying the constant as the slope. In \(y=mx+b\), the coefficient of \(x\) is the slope; the constant is the y-intercept.

Academic habit: label slope and intercept before graphing. This separates the two jobs and reduces sign errors.
            """,
        ),
        (
            "7. Writing Linear Equations from Evidence",
            r"""
Graph and table questions often ask for the equation of a line. A linear equation needs two pieces of evidence: slope and one point. The most common form is:
\[
y=mx+b.
\]

If the slope is 3 and the y-intercept is \(-2\), the equation is:
\[
y=3x-2.
\]

From a table, first find slope. Suppose the table includes \((0,5),(1,8),(2,11)\). Each time \(x\) increases by 1, \(y\) increases by 3, so \(m=3\). Since \(x=0\) gives \(y=5\), the y-intercept is 5. The equation is:
\[
y=3x+5.
\]

From a point and a slope, substitute to find \(b\). A line has slope 2 and passes through \((4,11)\):
\[
11=2(4)+b,\quad 11=8+b,\quad b=3.
\]
So the equation is \(y=2x+3\).

Common misconception: using any visible \(y\)-value as \(b\). The y-intercept is the \(y\)-value only when \(x=0\).

Academic habit: write the evidence as "slope = ..., point = ..." before building the equation.
            """,
        ),
        (
            "8. Intercepts, Standard Form, and Graph Interpretation",
            r"""
An **intercept** is where a graph crosses an axis.

The **y-intercept** occurs where \(x=0\). The **x-intercept** occurs where \(y=0\). These points often have real-world meaning.

Example:
\[
2x+y=10.
\]
To find the y-intercept, set \(x=0\):
\[
2(0)+y=10,\quad y=10.
\]
The y-intercept is \((0,10)\).

To find the x-intercept, set \(y=0\):
\[
2x+0=10,\quad x=5.
\]
The x-intercept is \((5,0)\).

Standard form can be rewritten into slope-intercept form. For \(2x+y=10\), subtract \(2x\) from both sides:
\[
y=-2x+10.
\]
The slope is \(-2\) and the y-intercept is 10.

Common misconception: x-intercept and y-intercept are not the same thing. The x-intercept has \(y=0\); the y-intercept has \(x=0\).

Academic habit: when the problem asks for an intercept, immediately set the other variable equal to zero.
            """,
        ),
        (
            "9. Systems of Equations as Intersections",
            r"""
A **system of equations** is two or more equations considered at the same time. On a graph, the solution is the intersection point because that point satisfies both equations.

[[figure:system_graph|The solution to a system of lines is the point where the lines cross.]]

Example:
\[
y=x+1,\qquad y=-x+5.
\]
At the intersection, the two \(y\)-values are equal:
\[
x+1=-x+5.
\]
Add \(x\) to both sides:
\[
2x+1=5.
\]
Subtract 1:
\[
2x=4,\quad x=2.
\]
Then \(y=2+1=3\). The solution is \((2,3)\).

If two lines have the same slope and different y-intercepts, they are parallel and have no solution. If they are the same line, they have infinitely many solutions.

Common misconception: giving only the \(x\)-value. A graphical system solution is an ordered pair \((x,y)\).

Academic habit: after finding the intersection, substitute into both equations to confirm the point works twice.
            """,
        ),
        (
            "10. Graphing Linear Inequalities",
            r"""
A linear inequality in two variables describes a region of the coordinate plane, not just a line.

[[figure:linear_inequality_shade|For \(y>x+1\), the boundary is dashed and the region above the line is shaded.]]

Use this process:
- Graph the boundary line by replacing the inequality symbol with \(=\).
- Use a **solid** line for \(\le\) or \(\ge\) because boundary points are included.
- Use a **dashed** line for \(<\) or \(>\) because boundary points are not included.
- Shade above the line for \(y>\) or \(y\ge\).
- Shade below the line for \(y<\) or \(y\le\).

You can test a point to decide the shading. For \(y<x+2\), test \((0,0)\):
\[
0<0+2
\]
is true, so the side containing \((0,0)\) should be shaded.

Common misconception: always shading above. The direction depends on the inequality and the form of the equation.

Academic habit: when unsure, test \((0,0)\) unless it lies on the boundary line.
            """,
        ),
        (
            "11. Comparing Functions in Different Forms",
            r"""
GED questions often ask students to compare two functions presented in different forms: an equation, a table, a graph, or a verbal description.

To compare functions, look for:
- **Initial value:** the output when \(x=0\), often the y-intercept.
- **Rate of change:** the slope for a linear function.
- **Specific output:** the value of the function at a named input.

Example: Function A is \(A(x)=2x+5\). Function B is shown by the table \((0,3),(1,7),(2,11)\).

Function A has initial value 5 and rate of change 2. Function B has initial value 3. Its output increases by 4 each time \(x\) increases by 1, so its rate of change is 4.

Therefore, Function A starts higher, but Function B grows faster.

[[figure:function_table_line|Tables, equations, and graphs can describe the same kind of relationship.]]

Common misconception: comparing only one output value. A function with the larger value at \(x=0\) may not stay larger if the other function has a greater slope.

Academic habit: compare both starting value and rate of change before writing a conclusion.
            """,
        ),
        (
            "12. Nonlinear Patterns and Final Graph Strategy",
            r"""
Not every relationship is linear. A **linear** function changes by equal differences and graphs as a line. A **quadratic** function has an \(x^2\) term and graphs as a parabola. An **exponential** pattern changes by equal multiplication factors.

[[figure:parabola|A quadratic graph is a parabola. Its roots are where it crosses the x-axis.]]

In a table:
- Linear pattern: outputs change by the same amount each step, such as \(3,7,11,15\).
- Quadratic pattern: first differences change, but second differences may be constant, such as \(1,4,9,16\).
- Exponential pattern: outputs multiply by the same factor, such as \(2,4,8,16\).

Final GED graph strategy:
- Read the title, axes, labels, scale, and units.
- Identify whether the graph is linear or nonlinear.
- Locate intercepts and key points.
- Interpret slope or change in context.
- Use the graph only for claims it actually supports.

Common misconception: forcing every graph into \(y=mx+b\). Slope-intercept form is for lines; curves require different reasoning.

Academic habit: describe the pattern before calculating. A correct description often reveals the right method.
            """,
        ),
    ],
    "mcqs": [
        item(r"Which point is 3 units right and 2 units down from the origin?", r"\((3,-2)\)", [r"\((-2,3)\)", r"\((2,-3)\)", r"\((-3,2)\)"], ["Right means positive \(x\).", "Down means negative \(y\).", "The ordered pair is \((3,-2)\)."], "reversing the order of the coordinates.", 1),
        item(r"In which quadrant is \((-4,5)\)?", "Quadrant II", ["Quadrant I", "Quadrant III", "Quadrant IV"], ["The \(x\)-coordinate is negative, so the point is left of the y-axis.", "The \(y\)-coordinate is positive, so the point is above the x-axis.", "Left and above is Quadrant II."], "checking only one sign instead of both coordinate signs.", 1),
        item(r"Where is the point \((0,-6)\)?", "On the y-axis", ["On the x-axis", "Quadrant IV", "Quadrant III"], ["A point with \(x=0\) has no left-right movement.", "It sits on the vertical axis.", "Therefore \((0,-6)\) is on the y-axis."], "putting the point in a quadrant even though points on axes are not in quadrants.", 1),
        item(r"For the rule \(y=2x+1\), what is \(y\) when \(x=3\)?", r"\(7\)", [r"\(6\)", r"\(5\)", r"\(9\)"], ["Substitute \(x=3\).", "Compute \(2(3)+1=6+1\).", "The output is 7."], "multiplying 2 and 3 but forgetting the plus 1.", 1),
        item(r"The table has points \((0,4),(1,6),(2,8)\). Which rule matches the table?", r"\(y=2x+4\)", [r"\(y=4x+2\)", r"\(y=x+4\)", r"\(y=2x\)"], ["When \(x=0\), \(y=4\), so the y-intercept is 4.", "The output rises by 2 each time \(x\) rises by 1, so the slope is 2.", "The rule is \(y=2x+4\)."], "using the first output as the slope instead of the intercept.", 2),
        item(r"Which set of ordered pairs is NOT a function?", r"\((1,2),(1,5),(3,6)\)", [r"\((1,2),(2,2),(3,2)\)", r"\((0,4),(1,5),(2,6)\)", r"\((-1,3),(0,3),(1,3)\)"], ["A function cannot give one input two different outputs.", "In \((1,2),(1,5),(3,6)\), input 1 appears twice.", "Because input 1 has outputs 2 and 5, the relation is not a function."], "thinking repeated outputs are the problem; repeated inputs with different outputs are the problem.", 2),
        item(r"What does \(f(4)\) mean?", "The output of function \(f\) when the input is 4", ["\(f\) multiplied by 4", "The slope of the function", "The fourth function in a list"], ["Function notation names a rule.", "The number inside the parentheses is the input.", "\(f(4)\) means evaluate \(f\) at input 4."], "reading function notation as multiplication.", 1),
        item(r"If \(f(x)=3x-2\), what is \(f(4)\)?", r"\(10\)", [r"\(5\)", r"\(14\)", r"\(12\)"], ["Replace \(x\) with 4.", "Compute \(3(4)-2=12-2\).", "So \(f(4)=10\)."], "forgetting to subtract 2 after multiplying.", 1),
        item(r"If \(g(x)=x^2+1\), what is \(g(-3)\)?", r"\(10\)", [r"\(-8\)", r"\(-10\)", r"\(7\)"], ["Replace \(x\) with \(-3\).", "Square the entire input: \((-3)^2=9\).", "Add 1 to get 10."], "squaring 3 and then keeping a negative sign outside.", 2),
        item(r"For the points \((0,1),(2,5),(4,9)\), what is the domain?", r"\(\{0,2,4\}\)", [r"\(\{1,5,9\}\)", r"\(\{0,1,2,4,5,9\}\)", r"\(\{1,2,4\}\)"], ["The domain is the set of inputs.", "Inputs are the \(x\)-values of the ordered pairs.", "The domain is \(\{0,2,4\}\)."], "using the y-values, which are the range.", 1),
        item(r"For the points \((0,1),(2,5),(4,9)\), what is the range?", r"\(\{1,5,9\}\)", [r"\(\{0,2,4\}\)", r"\(\{0,1,2,4,5,9\}\)", r"\(\{1,2,4\}\)"], ["The range is the set of outputs.", "Outputs are the \(y\)-values.", "The range is \(\{1,5,9\}\)."], "confusing range with domain.", 1),
        item(r"A vertical line touches a graph at two points. What does this show?", "The graph is not a function.", ["The graph must be linear.", "The graph has slope 0.", "The graph has no y-intercept."], ["A function gives each input exactly one output.", "A vertical line represents one \(x\)-value.", "If it touches twice, one input has two outputs, so it is not a function."], "thinking every graph is a function if it is drawn on a coordinate plane.", 2),
        item(r"What is the slope through \((1,2)\) and \((4,8)\)?", r"\(2\)", [r"\(6\)", r"\(\frac{1}{2}\)", r"\(3\)"], ["Compute change in \(y\): \(8-2=6\).", "Compute change in \(x\): \(4-1=3\).", "Slope \(=6/3=2\)."], "reporting the rise 6 without dividing by the run.", 2),
        item(r"A line rises from left to right. What kind of slope does it have?", "Positive slope", ["Negative slope", "Zero slope", "Undefined slope"], ["Rising left to right means \(y\) increases as \(x\) increases.", "That makes the change in \(y\) positive for a positive run.", "The slope is positive."], "mixing up rising and falling lines.", 1),
        item(r"What is the slope of a horizontal line?", r"\(0\)", ["Undefined", r"\(1\)", r"\(-1\)"], ["A horizontal line has no vertical change.", "Rise is 0 while run is not 0.", "Slope is \(0/\text{run}=0\)."], "confusing horizontal lines with vertical lines.", 1),
        item(r"What is the slope of a vertical line?", "Undefined", [r"\(0\)", r"\(1\)", r"\(-1\)"], ["A vertical line has no horizontal change.", "The run is 0.", "Division by 0 is undefined, so the slope is undefined."], "saying vertical slope is 0; slope 0 belongs to horizontal lines.", 2),
        item(r"A distance-time graph rises 120 miles over 2 hours. What is the slope?", "60 miles per hour", ["120 miles per hour", "2 miles per hour", "240 miles per hour"], ["Slope is change in distance divided by change in time.", "Compute \(120/2=60\).", "The slope is 60 miles per hour."], "using the total distance as the rate without dividing by time.", 1),
        item(r"What is the slope of \(y=-3x+4\)?", r"\(-3\)", [r"\(4\)", r"\(3\)", r"\(-4\)"], ["Compare with \(y=mx+b\).", "The slope is the coefficient of \(x\).", "Here \(m=-3\)."], "choosing the y-intercept 4 instead of the slope.", 1),
        item(r"What is the y-intercept of \(y=2x-7\)?", r"\(-7\)", [r"\(2\)", r"\(7\)", r"\(-2\)"], ["Compare with \(y=mx+b\).", "The y-intercept is \(b\), the constant term.", "Here \(b=-7\)."], "dropping the negative sign from the intercept.", 1),
        item(r"Which equation has slope \(3\) and y-intercept \(2\)?", r"\(y=3x+2\)", [r"\(y=2x+3\)", r"\(y=3x-2\)", r"\(y=x+5\)"], ["Use slope-intercept form \(y=mx+b\).", "Put \(m=3\) and \(b=2\).", "The equation is \(y=3x+2\)."], "switching slope and intercept.", 1),
        item(r"To graph \(y=2x+1\), which point is the y-intercept?", r"\((0,1)\)", [r"\((1,0)\)", r"\((2,1)\)", r"\((1,2)\)"], ["The y-intercept occurs where \(x=0\).", "In \(y=2x+1\), \(b=1\).", "The y-intercept point is \((0,1)\)."], "writing the intercept as \((1,0)\), which would be an x-intercept form.", 2),
        item(r"A line has slope \(2\) and passes through \((4,11)\). What is its equation?", r"\(y=2x+3\)", [r"\(y=2x+11\)", r"\(y=4x+3\)", r"\(y=3x+2\)"], ["Start with \(y=2x+b\).", "Substitute \((4,11)\): \(11=2(4)+b\).", "Solve \(11=8+b\), so \(b=3\), giving \(y=2x+3\)."], "using the point's y-value as the intercept even though \(x\ne0\).", 3),
        item(r"The table has \((0,5),(1,8),(2,11)\). What is the equation?", r"\(y=3x+5\)", [r"\(y=5x+3\)", r"\(y=3x+8\)", r"\(y=x+5\)"], ["The y-value when \(x=0\) is 5, so \(b=5\).", "The y-values increase by 3 when x increases by 1, so \(m=3\).", "The equation is \(y=3x+5\)."], "using the second row value as the intercept.", 2),
        item(r"Find the x-intercept of \(2x+y=10\).", r"\((5,0)\)", [r"\((0,10)\)", r"\((10,0)\)", r"\((0,5)\)"], ["For an x-intercept, set \(y=0\).", "Solve \(2x+0=10\), so \(x=5\).", "The x-intercept is \((5,0)\)."], "finding the y-intercept instead.", 2),
        item(r"Find the y-intercept of \(2x+y=10\).", r"\((0,10)\)", [r"\((5,0)\)", r"\((10,0)\)", r"\((0,5)\)"], ["For a y-intercept, set \(x=0\).", "Solve \(2(0)+y=10\), so \(y=10\).", "The y-intercept is \((0,10)\)."], "setting the wrong variable to zero.", 2),
        item(r"Rewrite \(2x+y=10\) in slope-intercept form.", r"\(y=-2x+10\)", [r"\(y=2x+10\)", r"\(y=-2x-10\)", r"\(y=10x-2\)"], ["Start with \(2x+y=10\).", "Subtract \(2x\) from both sides.", "The result is \(y=-2x+10\)."], "moving \(2x\) without changing its sign.", 2),
        item(r"What is the solution of the system \(y=x+1\) and \(y=-x+5\)?", r"\((2,3)\)", [r"\((3,2)\)", r"\((2,5)\)", r"\((1,3)\)"], ["Set the two expressions for \(y\) equal: \(x+1=-x+5\).", "Solve: \(2x=4\), so \(x=2\).", "Substitute into \(y=x+1\), giving \(y=3\), so the solution is \((2,3)\)."], "reporting the coordinates in the wrong order.", 3),
        item(r"What does the intersection point of two line graphs represent?", "The ordered pair that satisfies both equations", ["Only the slope of the first line", "Only the y-intercept", "A point that satisfies neither equation"], ["Each line contains points satisfying its own equation.", "The intersection lies on both lines.", "Therefore it satisfies both equations."], "forgetting that a system solution is shared by both equations.", 2),
        item(r"Two lines have the same slope but different y-intercepts. How many solutions does the system have?", "No solution", ["One solution", "Infinitely many solutions", "Two solutions"], ["Lines with the same slope and different intercepts are parallel.", "Parallel distinct lines do not cross.", "A system solution is an intersection, so there is no solution."], "thinking every pair of lines must intersect.", 2),
        item(r"For \(y>2x-1\), should the boundary line be solid or dashed?", "Dashed", ["Solid", "Neither, because there is no boundary", "Solid only above the x-axis"], ["The symbol \(>\) does not include equality.", "Boundary points are not part of the solution.", "Use a dashed boundary line."], "using a solid line for every inequality.", 2),
        item(r"For \(y\le -x+3\), where should the graph be shaded?", "Below the solid boundary line", ["Above the dashed boundary line", "Above the solid boundary line", "Only on the x-axis"], ["The symbol \(\le\) includes the boundary, so the line is solid.", "The inequality is \(y\le\), so shade values below the line.", "The correct description is below the solid boundary line."], "shading above because the graph has a negative slope.", 2),
        item(r"Does the point \((0,0)\) satisfy \(y<x+2\)?", "Yes", ["No", "Only if the line is vertical", "Only if x is positive"], ["Substitute \(x=0\) and \(y=0\).", "The inequality becomes \(0<0+2\), or \(0<2\).", "This is true, so the point satisfies the inequality."], "testing only x or only y instead of substituting both coordinates.", 2),
        item(r"Function A is \(A(x)=2x+5\). What is its initial value?", r"\(5\)", [r"\(2\)", r"\(7\)", r"\(0\)"], ["The initial value is the output when \(x=0\).", "Compute \(A(0)=2(0)+5\).", "The initial value is 5."], "choosing the slope as the initial value.", 1),
        item(r"Function B has table values \((0,3),(1,7),(2,11)\). What is its rate of change?", r"\(4\)", [r"\(3\)", r"\(7\)", r"\(8\)"], ["As \(x\) increases from 0 to 1, \(y\) increases from 3 to 7.", "The change in \(y\) is \(7-3=4\) for a change in \(x\) of 1.", "The rate of change is 4."], "using the first output 3 as the rate.", 2),
        item(r"Function A is \(A(x)=2x+5\). Function B has rate of change 4 and initial value 3. Which grows faster?", "Function B", ["Function A", "They grow at the same rate", "Neither function changes"], ["Growth rate for a linear function is slope.", "Function A has slope 2.", "Function B has rate of change 4, which is larger, so B grows faster."], "choosing the function with the larger initial value instead of the larger rate.", 2),
        item(r"Which function has the greater value at \(x=3\): \(f(x)=2x+1\) or \(g(x)=x+6\)?", r"\(g(x)\)", [r"\(f(x)\)", "They are equal.", "There is not enough information"], ["Evaluate \(f(3)=2(3)+1=7\).", "Evaluate \(g(3)=3+6=9\).", "Since \(9>7\), \(g(x)\) has the greater value at \(x=3\)."], "comparing slopes only without evaluating at the requested input.", 2),
        item(r"Which output sequence is linear?", r"\(3,\ 7,\ 11,\ 15\)", [r"\(1,\ 4,\ 9,\ 16\)", r"\(2,\ 4,\ 8,\ 16\)", r"\(5,\ 5,\ 8,\ 13\)"], ["A linear sequence has constant first differences.", "\(3,7,11,15\) increases by 4 each time.", "Therefore it is linear."], "choosing a pattern just because it increases; linear means equal differences.", 2),
        item(r"Which output sequence is exponential?", r"\(2,\ 4,\ 8,\ 16\)", [r"\(3,\ 7,\ 11,\ 15\)", r"\(1,\ 4,\ 9,\ 16\)", r"\(10,\ 8,\ 6,\ 4\)"], ["An exponential pattern multiplies by the same factor.", "\(2,4,8,16\) doubles each time.", "The constant factor is 2, so the pattern is exponential."], "looking for equal differences instead of equal multiplication factors.", 2),
        item(r"What shape is the graph of a quadratic function?", "A parabola", ["A straight line", "A circle", "A histogram"], ["A quadratic includes an \(x^2\) term.", "Quadratic functions graph as U-shaped curves.", "That curve is called a parabola."], "using line language for every function.", 1),
        item(r"On the graph of a quadratic, what are roots?", "The x-values where the graph crosses the x-axis", ["The y-intercept only", "The slope of the curve", "The highest output in every graph"], ["Roots are solutions to \(f(x)=0\).", "On a graph, \(f(x)=0\) means \(y=0\).", "Those are the x-intercepts."], "confusing roots with the y-intercept.", 2),
        item(r"A graph has a y-intercept of 12 and slope \(-2\). Which real-world interpretation fits?", "It starts at 12 and decreases by 2 per x-unit.", ["It starts at -2 and increases by 12 per x-unit.", "It starts at 2 and decreases by 12 per x-unit.", "It has no starting value."], ["The y-intercept gives the starting value when \(x=0\).", "The slope gives the change per x-unit.", "So the value starts at 12 and decreases by 2 each step."], "switching the roles of slope and intercept.", 2),
        item(r"Which statement is safest from a graph alone?", "The graph shows an association or pattern.", ["The graph always proves cause and effect.", "The graph gives exact values beyond its scale.", "The graph makes units unnecessary."], ["A graph can show patterns and relationships.", "Cause requires stronger evidence than a graph alone.", "Therefore the safe claim is association or pattern."], "overclaiming cause from visual evidence.", 1),
        item(r"If a graph's vertical scale counts by 5s, what value is two grid lines above 10?", r"\(20\)", [r"\(12\)", r"\(15\)", r"\(25\)"], ["Each grid line represents 5 units.", "Two grid lines represent \(2\cdot5=10\) units.", "Starting at 10, the value is \(10+10=20\)."], "counting grid lines as 1 unit each without reading the scale.", 1),
        item(r"Which equation represents a vertical line through \(x=4\)?", r"\(x=4\)", [r"\(y=4\)", r"\(y=4x\)", r"\(x=y+4\)"], ["A vertical line has the same x-value for every point.", "The x-value is fixed at 4.", "The equation is \(x=4\)."], "using \(y=4\), which is a horizontal line.", 2),
        item(r"Which equation represents a horizontal line through \(y=-3\)?", r"\(y=-3\)", [r"\(x=-3\)", r"\(y=-3x\)", r"\(x=y-3\)"], ["A horizontal line has the same y-value for every point.", "The y-value is fixed at -3.", "The equation is \(y=-3\)."], "using \(x=-3\), which is vertical.", 2),
        item(r"A function has rate of change \(0\). What does its graph look like?", "A horizontal line", ["A vertical line", "A parabola", "A line that must rise"], ["Rate of change is slope.", "Slope 0 means no vertical change as x changes.", "The graph is horizontal."], "confusing zero slope with undefined slope.", 2),
        item(r"If \(h(x)=15x\) gives cost for \(x\) tutoring hours, which domain value is not reasonable in context?", r"\(-2\)", [r"\(0\)", r"\(1\)", r"\(3\)"], ["The input \(x\) represents hours.", "Negative hours do not make sense in this context.", "Therefore \(-2\) is not reasonable."], "forgetting that real-world context can restrict the domain.", 1),
        item(r"Which line is steeper: \(y=5x+1\) or \(y=2x+10\)?", r"\(y=5x+1\)", [r"\(y=2x+10\)", "They are equally steep", "Cannot be determined"], ["Steepness for a line is controlled by the absolute value of slope.", "The slopes are 5 and 2.", "Since 5 is larger than 2, \(y=5x+1\) is steeper."], "choosing the line with the larger y-intercept.", 2),
        item(r"Which line has a negative slope?", r"\(y=-4x+6\)", [r"\(y=4x-6\)", r"\(y=6\)", r"\(x=-4\)"], ["In \(y=mx+b\), slope is the coefficient of \(x\).", "For \(y=-4x+6\), the slope is -4.", "A negative coefficient means negative slope."], "choosing an equation with a negative constant instead of a negative slope.", 1),
        item(r"The point \((2,7)\) is on a graph. What does that mean in function language?", "When the input is 2, the output is 7.", ["When the input is 7, the output is 2.", "The slope is 7.", "The y-intercept is 2."], ["The x-coordinate is the input.", "The y-coordinate is the output.", "So input 2 gives output 7."], "reversing input and output.", 1),
        item(r"If a table's x-values increase by 1 and y-values decrease by 3 each time, what is the slope?", r"\(-3\)", [r"\(3\)", r"\(\frac{1}{3}\)", r"\(-\frac{1}{3}\)"], ["Slope is change in y divided by change in x.", "The change in y is -3 and the change in x is 1.", "Slope \(=-3/1=-3\)."], "dropping the negative sign because the size of the change is 3.", 2),
        item(r"Which ordered pair satisfies \(y=2x+1\)?", r"\((3,7)\)", [r"\((3,6)\)", r"\((7,3)\)", r"\((1,2)\)"], ["Test \((3,7)\): \(2(3)+1=7\).", "The y-value matches the rule.", "Therefore \((3,7)\) satisfies the equation."], "testing the coordinates in the wrong positions.", 1),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Algebra: Functions & Graphs Mastery course (MCQ only)."

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
