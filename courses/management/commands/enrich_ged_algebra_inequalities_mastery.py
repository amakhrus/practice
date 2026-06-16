from django.core.management.base import BaseCommand
from courses.models import Lesson

LESSONS = [
    (1, """What an Inequality Means

An inequality is a mathematical statement that compares two expressions using one of four symbols: less than (<), greater than (>), less than or equal to (<=), or greater than or equal to (>=). Unlike an equation, which has exactly one solution, an inequality usually has infinitely many solutions — an entire range of values that make the statement true.

Think of it this way: if an equation is a door with one key, an inequality is a door that opens for dozens of keys. For example, the inequality x > 3 means "x can be any number greater than 3." That includes 4, 5, 3.1, 100, and even 3.0001 — any value as long as it is strictly more than 3.

Understanding Inequality Symbols

The four symbols and their meanings:
- < means "is less than" (the open end points to the smaller number)
- > means "is greater than" (the open end points to the smaller number)
- <= means "is less than or equal to"
- >= means "is greater than or equal to"

A helpful trick: the symbol always "eats" the bigger number. The wide, open mouth faces the larger value. So 7 > 3 is read "7 is greater than 3," and the wide side faces 7.

Worked Example

Problem: Is x = 5 a solution to the inequality 2x - 1 < 12?

Step 1: Substitute x = 5 into the left side.
2(5) - 1 = 10 - 1 = 9

Step 2: Compare to the right side.
9 < 12

Step 3: Is this true? Yes, 9 is less than 12.

Therefore, x = 5 is a solution to 2x - 1 < 12.

Now check x = 7:
2(7) - 1 = 14 - 1 = 13
13 < 12? No — 13 is not less than 12, so x = 7 is NOT a solution.

This shows that some values work and some do not — which is the nature of inequalities.

Real-World Connection

Inequalities appear constantly in everyday life. Speed limits, age requirements, budget constraints, and weight limits are all expressed as inequalities. "You must be at least 18 years old" means age >= 18. "The speed limit is 65 mph" means speed <= 65. Understanding this language prepares you not just for the GED but for reading and interpreting everyday information.

Common Mistake to Avoid

A very common error is treating an inequality like an equation and finding only one answer. Remember: most inequalities have a whole range of solutions, not just one number. If someone asks you to solve x + 3 > 7 and you write only "x = 4," that is incorrect. The answer is x > 4 — every number greater than 4 is a valid solution.

GED Test Tip

On the GED, inequality questions often ask you to identify which value from a list is a solution, or to match an inequality to a real-world situation. Practice substituting given values into an inequality to check whether they satisfy it. This plug-and-check strategy works every time and does not require you to solve the inequality from scratch.
"""),

    (2, """Graphing Inequalities on a Number Line

Once you understand what an inequality means, the next step is representing its solution visually on a number line. Graphing gives you a clear picture of all the values that make the inequality true — which can be extremely helpful when checking your work or interpreting results.

The Two Key Symbols on a Number Line Graph

When you graph an inequality on a number line, you use two types of circles (also called dots or endpoints):

1. Open circle (hollow dot): Used when the endpoint is NOT included. This corresponds to strict inequalities using < or >. The boundary value itself is not a solution.

2. Closed circle (filled dot): Used when the endpoint IS included. This corresponds to <= or >=. The boundary value is part of the solution set.

After marking the circle, you draw an arrow (or shade) in the direction of all values that satisfy the inequality. If x > 3, you shade everything to the right of 3 (greater values). If x < 5, you shade everything to the left of 5 (smaller values).

Worked Example

Problem: Graph x <= -2 on a number line.

Step 1: Identify the boundary value. It is -2.

Step 2: Determine the circle type. The symbol is <=, which includes the endpoint. Use a closed (filled) circle at -2.

Step 3: Determine the direction. We want values less than or equal to -2, so shade to the left of -2 (toward -3, -4, -5, and so on).

Step 4: Draw an arrow pointing left from -2 to show the solution continues without bound.

Result: A filled dot at -2 with a leftward arrow covering all numbers to the left.

Now try: Graph x > 1.
- Boundary value: 1
- Circle type: Open circle (strict >, does not include 1)
- Direction: Right (values greater than 1)
- Arrow pointing right from 1

Reading Graphs: Going the Other Direction

You will also be asked to read a graph and write the inequality it represents. Look at whether the circle is open or closed, and whether the arrow goes left (less than) or right (greater than). If the arrow goes right from a closed circle at 4, the inequality is x >= 4.

Negative Numbers and Direction

Be careful with negative numbers. On a number line, -1 is to the right of -5, because -1 is greater. This confuses many students who think "a bigger negative number is larger." Remember: the further right you go on a number line, the larger the value, regardless of sign.

Common Mistake to Avoid

Students frequently mix up open and closed circles. A simple way to remember: if the inequality symbol has a line under it (<= or >=), that means "or equal to" — so the endpoint is included and you use a closed circle. If there is no line under it (< or >), the endpoint is excluded and you use an open circle.

GED Test Tip

GED questions often show a number line graph and ask you to identify the correct inequality, or they give you an inequality and ask which graph matches it. Always check two things: (1) open vs. closed circle, and (2) the direction of shading. Getting both right will lock in the correct answer. Also note that some GED items show a number line with a segment shaded between two points — this represents a compound inequality, which you will study in a later lesson.
"""),

    (3, """One-Step Inequalities

One-step inequalities are the simplest type of inequality to solve. Just like one-step equations, they require only a single operation — addition, subtraction, multiplication, or division — to isolate the variable. The process is almost identical to solving equations, with one crucial difference that you will explore shortly (and study in depth in the next lesson).

The Golden Rule of Inequalities

The most important thing to remember when solving inequalities is this: whatever you do to one side, you must do to the other side — just like equations. Add 5 to the left? Add 5 to the right. Divide by 3 on the left? Divide by 3 on the right. Keeping both sides balanced is the foundation of all algebraic problem-solving.

Solving by Addition or Subtraction

When adding or subtracting a number to solve an inequality, the direction of the inequality symbol does not change.

Worked Example 1

Problem: Solve x - 4 > 9.

Step 1: Add 4 to both sides to isolate x.
x - 4 + 4 > 9 + 4
x > 13

Step 2: Write the solution. x > 13

Check: Try x = 15: 15 - 4 = 11 > 9. True.
Try x = 10: 10 - 4 = 6 > 9. False. Good — 10 is not greater than 13.

Solving by Multiplication or Division (Positive Numbers)

When multiplying or dividing both sides by a positive number, the inequality direction stays the same.

Worked Example 2

Problem: Solve 3x <= 18.

Step 1: Divide both sides by 3.
3x / 3 <= 18 / 3
x <= 6

Step 2: Write the solution. x <= 6

Check: Try x = 4: 3(4) = 12 <= 18. True.
Try x = 7: 3(7) = 21 <= 18. False. Correct — 7 is not in our solution set.

Solving by Multiplication or Division (Negative Numbers — Preview)

If you divide or multiply by a negative number, the inequality sign FLIPS. This will be covered fully in the next lesson, but be aware: x / (-2) < 5 does not follow the same rules as x / 2 < 5. For now, focus on positive multipliers and divisors.

Writing and Interpreting Solutions

After solving, you can express your answer in three ways:
1. Inequality notation: x > 13
2. Number line graph: open circle at 13, arrow pointing right
3. In words: "all real numbers greater than 13"

GED questions may ask for any of these forms, so practice converting between them.

Common Mistake to Avoid

One common error is performing the correct operation but forgetting to carry it through to both sides. For example, in x + 6 < 10, a student might subtract 6 from the left to get x but forget to subtract 6 from 10 on the right. Always apply the operation to both sides simultaneously.

GED Test Tip

One-step inequalities are frequently tested on the GED in the context of word problems. A clue phrase like "no more than" means <= ; "at least" means >=; "fewer than" means <; "more than" means >. When you see these phrases, translate them directly into inequality symbols before solving. This translation skill alone can earn you several points on the GED Mathematical Reasoning test.
"""),

    (4, """The Sign-Flip Rule

One of the most unique and important rules in algebra is the sign-flip rule for inequalities: whenever you multiply or divide both sides of an inequality by a negative number, you must reverse (flip) the direction of the inequality symbol. This rule has no equivalent in equation-solving, which is why it trips up so many students.

Why Does the Sign Flip?

Let's use a simple example to see why this rule must exist.

Start with a true statement: 4 > 2 (four is greater than two — obviously true).

Now multiply both sides by -1:
-4 and -2

Is -4 > -2? No! On the number line, -4 is to the LEFT of -2, which means -4 is LESS than -2.

To keep the statement true, we must flip the symbol:
-4 < -2 ✓

This is why the rule exists. Multiplying or dividing by a negative number reverses the order of numbers on the number line.

Worked Example 1

Problem: Solve -3x < 15.

Step 1: Divide both sides by -3. Because we are dividing by a negative number, flip the inequality.
x > 15 / (-3)
x > -5

Step 2: Write the solution. x > -5

Check: Try x = 0: -3(0) = 0 < 15. True. And 0 > -5. ✓
Try x = -6: -3(-6) = 18 < 15. False. And -6 is not > -5. ✓

Worked Example 2

Problem: Solve -x/4 >= 3.

Step 1: Multiply both sides by -4. Flip the inequality.
x <= 3 x (-4)
x <= -12

Step 2: Write the solution. x <= -12

Check: Try x = -16: -(-16)/4 = 16/4 = 4 >= 3. True. And -16 <= -12. ✓
Try x = -8: -(-8)/4 = 8/4 = 2 >= 3. False. And -8 is not <= -12. ✓

When Does the Sign NOT Flip?

The sign flips ONLY when you multiply or divide by a negative. Adding or subtracting a negative number does NOT cause a flip. For example:
x + (-3) > 5 → add 3 to both sides → x > 8. No flip needed.

Only the act of multiplying or dividing by a negative triggers the flip.

Common Mistake to Avoid

The most frequent error is flipping the sign when adding or subtracting a negative number — or, conversely, forgetting to flip when dividing by a negative. A helpful habit: before you perform a multiplication or division step, ask yourself, "Is the number I'm multiplying or dividing by negative?" If yes, flip the sign as you write the next line.

GED Test Tip

On the GED, the sign-flip rule is often tested indirectly. You may be given a solved inequality with an error and asked to identify the mistake. Or you may see a multiple-choice question where three of the four answers forget to flip the sign. If you master this rule, you will immediately spot the correct answer. Always double-check your solution by plugging in a test value — if the result is false, check whether you missed a sign flip.
"""),

    (5, """Two-Step Inequalities

Two-step inequalities require exactly two operations to isolate the variable, just like two-step equations. The approach is systematic: undo addition or subtraction first, then undo multiplication or division. The only additional consideration is watching for the sign-flip rule when dividing or multiplying by a negative number.

The Two-Step Strategy

Follow these steps every time:
1. Identify the variable and what operations are applied to it.
2. Undo addition or subtraction first (add or subtract the constant from both sides).
3. Undo multiplication or division second (multiply or divide both sides, flipping the sign if the number is negative).
4. Write the solution and check with a test value.

Worked Example 1

Problem: Solve 2x + 5 > 13.

Step 1: Subtract 5 from both sides.
2x + 5 - 5 > 13 - 5
2x > 8

Step 2: Divide both sides by 2 (positive — no flip).
x > 4

Check: Try x = 6: 2(6) + 5 = 17 > 13. True. ✓
Try x = 3: 2(3) + 5 = 11 > 13. False. ✓ (3 is not > 4)

Worked Example 2

Problem: Solve -4x - 3 <= 9.

Step 1: Add 3 to both sides.
-4x - 3 + 3 <= 9 + 3
-4x <= 12

Step 2: Divide both sides by -4. Negative divisor — FLIP the sign.
x >= 12 / (-4)
x >= -3

Check: Try x = 0: -4(0) - 3 = -3 <= 9. True. And 0 >= -3. ✓
Try x = -5: -4(-5) - 3 = 20 - 3 = 17 <= 9. False. And -5 is not >= -3. ✓

Connecting to Real Life

Two-step inequalities show up in budgeting and shopping scenarios. For example: "A store charges $8 per item plus a $3 delivery fee. You can spend at most $35. How many items can you buy?" This translates to 8x + 3 <= 35, a two-step inequality. Solving it:
Step 1: Subtract 3: 8x <= 32
Step 2: Divide by 8: x <= 4
You can buy at most 4 items.

Common Mistake to Avoid

Students sometimes reverse the order of steps: they divide first before dealing with the constant. While this can technically work, it often leads to fraction arithmetic that creates errors. Always remove the constant term first (addition/subtraction), then handle the coefficient (multiplication/division). This order mirrors the standard equation-solving approach and minimizes errors.

Another error: forgetting to apply the operation to the entire right side. In 2x + 5 > 13, when subtracting 5, make sure you write 13 - 5 = 8 — not just 13 on its own.

GED Test Tip

Two-step inequalities are one of the most commonly tested topics on the GED Mathematical Reasoning section. When working on these problems, write out every step clearly — do not try to skip steps in your head. The GED rewards careful, organized work, and writing each step also makes it easier to catch errors before they lead to a wrong answer. Practice at least 10 two-step inequality problems so the process becomes automatic.
"""),

    (6, """Multi-Step Inequalities

Multi-step inequalities involve three or more operations to solve. They often include parentheses that must be expanded, like terms that must be combined, or both. The good news is that the process is a direct extension of what you already know — clear parentheses first, combine like terms, then isolate the variable using the same two-step strategy.

The Multi-Step Strategy

1. Distribute: Use the distributive property to eliminate parentheses.
2. Combine like terms: On each side of the inequality, combine any like terms.
3. Move variable terms: Get all variable terms on one side by adding or subtracting.
4. Move constant terms: Get all constants on the other side.
5. Divide or multiply: Isolate the variable, watching for sign flips.
6. Check your solution.

Worked Example 1

Problem: Solve 3(x - 2) + 4 >= 19.

Step 1: Distribute 3.
3x - 6 + 4 >= 19

Step 2: Combine like terms on the left.
3x - 2 >= 19

Step 3: Add 2 to both sides.
3x >= 21

Step 4: Divide by 3 (positive — no flip).
x >= 7

Check: Try x = 8: 3(8 - 2) + 4 = 3(6) + 4 = 22 >= 19. True. ✓

Worked Example 2

Problem: Solve 5 - 2(x + 3) < 1.

Step 1: Distribute -2.
5 - 2x - 6 < 1

Step 2: Combine like terms on the left.
-2x - 1 < 1

Step 3: Add 1 to both sides.
-2x < 2

Step 4: Divide by -2. Negative divisor — FLIP the sign.
x > -1

Check: Try x = 0: 5 - 2(0 + 3) = 5 - 6 = -1 < 1. True. And 0 > -1. ✓
Try x = -2: 5 - 2(-2 + 3) = 5 - 2(1) = 3 < 1. False. And -2 is not > -1. ✓

Special Cases

Occasionally, solving a multi-step inequality leads to a statement that is always true (like 0 < 5) or always false (like 0 > 5).
- Always true: the solution is all real numbers (every value of x works).
- Always false: there is no solution (no value of x works).

These results are rare on the GED but are worth recognizing.

Common Mistake to Avoid

The most common error in multi-step inequalities is incorrect distribution, especially with negative signs. In the expression -2(x + 3), both the x and the 3 must be multiplied by -2, giving -2x - 6, not -2x + 3. Write out every term of the distribution explicitly rather than trying to do it mentally.

GED Test Tip

When you encounter a multi-step inequality on the GED, take a moment to plan your sequence of steps before you start solving. Rushing leads to skipped steps and sign errors. Also, if the answer choices are given as inequalities (like x > 3 or x <= -1), you can sometimes use process of elimination by checking one of the simpler answer choices against the original inequality to see if it is consistent.
"""),

    (7, """Variables on Both Sides

Some inequalities have variable terms on both sides of the inequality symbol, such as 3x + 1 > x + 9. To solve these, you must collect all variable terms on one side and all constant terms on the other — a technique you may recognize from solving equations with variables on both sides.

The Strategy for Variables on Both Sides

1. Move all variable terms to one side by adding or subtracting.
2. Move all constant terms to the other side.
3. Isolate the variable by dividing or multiplying.
4. Watch for the sign-flip rule.
5. Check your answer.

Worked Example 1

Problem: Solve 3x + 1 > x + 9.

Step 1: Subtract x from both sides to gather variable terms on the left.
3x - x + 1 > 9
2x + 1 > 9

Step 2: Subtract 1 from both sides.
2x > 8

Step 3: Divide by 2 (positive — no flip).
x > 4

Check: Try x = 6: 3(6) + 1 = 19 and 6 + 9 = 15. Is 19 > 15? Yes. ✓
Try x = 2: 3(2) + 1 = 7 and 2 + 9 = 11. Is 7 > 11? No. And 2 is not > 4. ✓

Worked Example 2

Problem: Solve 5x - 3 <= 8x + 9.

Step 1: Subtract 5x from both sides (moving variables to the right, or subtract 8x from both sides to move them left — either works).

Option: Subtract 5x from both sides.
-3 <= 3x + 9

Step 2: Subtract 9 from both sides.
-12 <= 3x

Step 3: Divide by 3 (positive — no flip).
-4 <= x, which is the same as x >= -4.

Check: Try x = 0: 5(0) - 3 = -3 and 8(0) + 9 = 9. Is -3 <= 9? Yes. And 0 >= -4. ✓

Choosing Which Side to Move Variables To

You can move variable terms to either side. However, a smart strategy is to move them to the side where the coefficient will end up positive. This avoids the need to divide by a negative and reduces the chance of forgetting to flip the sign. For example, if you have 2x > 5x - 6, subtracting 2x gives 0 > 3x - 6, but subtracting 5x gives -3x > -6 (requires dividing by a negative). Moving to the side with the larger coefficient keeps the coefficient positive.

Common Mistake to Avoid

Students sometimes move variables to one side but forget to carry the sign. When you subtract x from 3x + 1, you get 2x + 1, not 2x + 1 + x. Rewrite each step completely to avoid dropping terms.

GED Test Tip

Variables-on-both-sides inequalities are common on the GED because they test whether students truly understand algebraic manipulation. If you see an inequality with x on both sides, do not panic — just pick one side to collect the variable terms and systematically work through the steps. A consistent process beats intuition every time.
"""),

    (8, """Fraction and Decimal Inequalities

Fractions and decimals in inequalities can look intimidating, but they are solved using the same principles as whole-number inequalities. The main strategies are: clear fractions by multiplying by the least common denominator (LCD), or clear decimals by multiplying by a power of 10. Once the fractions or decimals are eliminated, the problem reduces to a standard multi-step inequality.

Clearing Fractions

To eliminate fractions from an inequality, multiply every term on both sides by the LCD of all the fractions. This converts the problem into a whole-number inequality.

Worked Example 1

Problem: Solve (x/3) + (1/2) > (5/6).

Step 1: Find the LCD of 3, 2, and 6. The LCD is 6.

Step 2: Multiply every term by 6.
6 * (x/3) + 6 * (1/2) > 6 * (5/6)
2x + 3 > 5

Step 3: Subtract 3 from both sides.
2x > 2

Step 4: Divide by 2.
x > 1

Check: Try x = 2: (2/3) + (1/2) = 4/6 + 3/6 = 7/6 > 5/6. True. ✓

Clearing Decimals

To eliminate decimals, multiply every term by the smallest power of 10 that makes all decimals into whole numbers. If decimals go to the tenths place, multiply by 10. Hundredths? Multiply by 100.

Worked Example 2

Problem: Solve 0.4x - 0.1 <= 0.7.

Step 1: Multiply every term by 10 to clear the tenths-place decimals.
4x - 1 <= 7

Step 2: Add 1 to both sides.
4x <= 8

Step 3: Divide by 4.
x <= 2

Check: Try x = 1: 0.4(1) - 0.1 = 0.3 <= 0.7. True. ✓
Try x = 3: 0.4(3) - 0.1 = 1.1 <= 0.7. False. ✓

Working with Fractions Directly (Without Clearing)

If you prefer, you can also solve fraction inequalities by performing fraction arithmetic at each step. This works but tends to produce more errors. Clearing the LCD first is generally faster and more reliable.

Common Mistake to Avoid

When multiplying both sides of an inequality by the LCD to clear fractions, students sometimes forget to multiply every term. In (x/3) + (1/2) > (5/6), multiplying only the x-term by 6 and not the constant gives wrong results. Write out 6 times each individual term separately before simplifying.

Also remember: if the LCD or the power of 10 you multiply by is negative, you must flip the inequality. In practice, LCD values and powers of 10 are always positive, so this rarely applies — but be aware.

GED Test Tip

The GED Mathematical Reasoning test frequently presents fraction and decimal inequalities because they reflect real-life contexts like budgeting with decimals or splitting costs with fractions. When you see fractions or decimals in an inequality, immediately plan to clear them before doing anything else. This one step converts a messy problem into a clean whole-number inequality that is much faster to solve.
"""),

    (9, """Compound Inequalities

A compound inequality combines two separate inequalities into one statement. There are two types: "and" inequalities (also called conjunctions) and "or" inequalities (also called disjunctions). Each type has a different solution set and a different appearance on a number line.

"And" Inequalities

An "and" inequality means both conditions must be true simultaneously. It is often written as a three-part (or "sandwich") inequality, like -3 < x <= 5. This means x is greater than -3 AND less than or equal to 5. The solution is all values of x between -3 and 5, including 5 but not including -3.

On a number line, this looks like a segment: an open circle at -3, a closed circle at 5, and shading between them.

Worked Example 1

Problem: Solve -1 <= 2x + 3 < 9.

Step 1: Subtract 3 from all three parts.
-1 - 3 <= 2x < 9 - 3
-4 <= 2x < 6

Step 2: Divide all three parts by 2.
-2 <= x < 3

Solution: x is between -2 and 3, including -2 but not including 3.

Check: Try x = 0: -1 <= 2(0) + 3 = 3 < 9. True. ✓
Try x = 3: -1 <= 2(3) + 3 = 9 < 9. False — 9 is not strictly less than 9. ✓

"Or" Inequalities

An "or" inequality means at least one of the conditions must be true. The solution includes all values that satisfy either inequality. These are typically written as two separate statements joined by "or."

Worked Example 2

Problem: Solve x - 1 < -3 or 2x >= 8.

Inequality 1: x - 1 < -3
Add 1: x < -2

Inequality 2: 2x >= 8
Divide by 2: x >= 4

Solution: x < -2 or x >= 4. These are two separate rays pointing away from each other on the number line: a leftward arrow from an open circle at -2, and a rightward arrow from a closed circle at 4.

Graphing Compound Inequalities

- "And" (conjunction): Shading between two points — a bounded segment.
- "Or" (disjunction): Shading in two opposite directions — two separate rays.

Common Mistake to Avoid

In "and" inequalities written as three-part expressions, students sometimes apply an operation to only two of the three parts. Always perform the same operation on all three parts simultaneously. Forgetting to apply it to the middle section (the variable) or leaving out one of the outer constants is a common error.

GED Test Tip

GED compound inequality questions often appear in the form of a number line graph and ask you to write the matching inequality, or vice versa. Remember: if the shading is between two points, it is an "and" compound inequality. If the shading points outward in two directions, it is an "or" compound inequality. Recognizing this pattern instantly narrows your choices on multiple-choice questions.
"""),

    (10, """Absolute Value Inequalities

Absolute value measures the distance a number is from zero on the number line, regardless of direction. The absolute value of 5 is 5, and the absolute value of -5 is also 5, because both are 5 units from zero. When absolute value appears in inequalities, the solution involves two cases that reflect this two-sided nature.

Two Types of Absolute Value Inequalities

Type 1 — Less than (|expression| < k):
The solution is a bounded "and" inequality: -k < expression < k.
Think of it as: the expression must be within k units of zero.

Type 2 — Greater than (|expression| > k):
The solution is an "or" inequality: expression < -k or expression > k.
Think of it as: the expression must be more than k units from zero.

The same rules apply with <= and >= (just use <= or >= instead of < or >).

Worked Example 1

Problem: Solve |x - 3| < 5.

This is a "less than" type, so write a three-part inequality:
-5 < x - 3 < 5

Add 3 to all three parts:
-5 + 3 < x < 5 + 3
-2 < x < 8

Solution: -2 < x < 8

Check: Try x = 0: |0 - 3| = |-3| = 3 < 5. True. And -2 < 0 < 8. ✓
Try x = 10: |10 - 3| = 7 < 5. False. And 10 is not < 8. ✓

Worked Example 2

Problem: Solve |2x + 1| >= 7.

This is a "greater than or equal to" type, so write two separate inequalities:
2x + 1 <= -7 or 2x + 1 >= 7

Case 1: 2x + 1 <= -7
Subtract 1: 2x <= -8
Divide by 2: x <= -4

Case 2: 2x + 1 >= 7
Subtract 1: 2x >= 6
Divide by 2: x >= 3

Solution: x <= -4 or x >= 3

Check: Try x = -5: |2(-5) + 1| = |-9| = 9 >= 7. True. And -5 <= -4. ✓
Try x = 4: |2(4) + 1| = 9 >= 7. True. And 4 >= 3. ✓
Try x = 0: |2(0) + 1| = 1 >= 7. False. And 0 is not in our solution. ✓

When Is There No Solution or All Real Numbers?

If the right side is negative (e.g., |x| < -3), there is no solution — absolute value is always >= 0 and can never be less than a negative number. If the inequality is |x| > -3, the solution is all real numbers because every absolute value is greater than -3.

Common Mistake to Avoid

Students sometimes write the "greater than" case as a single three-part inequality: -7 <= 2x + 1 <= 7. This is the setup for the "less than" case, not the "greater than" case. For |expression| > k, you must write two separate inequalities with "or" between them.

GED Test Tip

Absolute value inequality questions on the GED most often appear in multiple-choice format. A fast approach: after you solve and get two cases, check each answer choice against both cases. The correct answer satisfies one of the two conditions. Also memorize the two rules (< gives "and," > gives "or") — knowing these by heart saves significant time during the exam.
"""),

    (11, """Word Problems with Inequalities

Translating real-world situations into inequalities and then solving them is a critical skill on the GED. Word problems test not just your algebra but your ability to read carefully, identify key information, and convert plain language into mathematical symbols.

Key Phrases and Their Inequality Translations

Learn these common translations:
- "at least" → >=
- "no less than" → >=
- "at most" → <=
- "no more than" → <=
- "fewer than" → <
- "less than" → <
- "more than" → >
- "greater than" → >
- "between" (inclusive) → <=, <=
- "exceeds" → >

A Step-by-Step Translation Process

1. Identify what the variable represents (define it clearly).
2. Find the key phrase that indicates the type of inequality.
3. Write the inequality.
4. Solve.
5. Interpret the answer in context — make sure it makes sense for the real-world situation.

Worked Example 1

Problem: Maria earns $12 per hour at her job. She wants to earn at least $180 this week. How many hours must she work?

Step 1: Let h = number of hours worked.
Step 2: "At least $180" means >= 180.
Step 3: Write the inequality: 12h >= 180.
Step 4: Divide both sides by 12: h >= 15.
Step 5: Interpret. Maria must work at least 15 hours.

Worked Example 2

Problem: A moving truck can carry no more than 4,500 pounds. The furniture already loaded weighs 3,200 pounds. How many additional pounds of boxes, each weighing 30 pounds, can be added?

Step 1: Let b = number of boxes.
Step 2: "No more than 4,500 pounds" means <= 4,500.
Step 3: Write the inequality: 3,200 + 30b <= 4,500.
Step 4: Subtract 3,200: 30b <= 1,300.
Divide by 30: b <= 43.33...
Step 5: Interpret. Since b must be a whole number of boxes, at most 43 boxes can be added. (You cannot add 0.33 of a box.)

The Importance of Context in the Answer

Not all algebraic solutions make sense in context. If you get x >= 4.7 and x represents the number of people, you must round up to 5 (because you cannot have a fraction of a person). If x represents a weight, a decimal may be perfectly acceptable. Always re-read the problem after solving to make sure your answer is reasonable.

Common Mistake to Avoid

A common error is setting up the inequality in the wrong direction. For example, "Maria needs to earn at least $180" means her earnings must be >= 180, so you write 12h >= 180. Writing 12h <= 180 gives the wrong answer (saying she must work at most 15 hours, not at least 15). Underline the key inequality phrase in the problem before writing your inequality to avoid this mistake.

GED Test Tip

Word problems with inequalities make up a significant portion of the GED algebra section. On the test, after solving, always re-read the question to confirm you are answering what was asked. The question might ask for the minimum hours, the maximum number of items, or whether a specific value satisfies the constraint — all slightly different questions that require you to interpret your solution carefully.
"""),

    (12, """Linear Inequalities in Two Variables

A linear inequality in two variables, such as y > 2x - 3 or 3x + 2y <= 12, has a solution set that is not just a range of numbers but an entire region of the coordinate plane. Graphing these inequalities produces a half-plane — half of the coordinate grid — representing all ordered pairs (x, y) that satisfy the inequality.

How to Graph a Linear Inequality in Two Variables

Step 1: Replace the inequality symbol with an equal sign and graph the boundary line. This is the line you already know how to graph using slope-intercept form (y = mx + b).

Step 2: Determine whether the boundary line is solid or dashed.
- Solid line: Use when the symbol is <= or >=. The line itself is part of the solution.
- Dashed line: Use when the symbol is < or >. The line is NOT part of the solution.

Step 3: Choose a test point not on the line — the origin (0, 0) is usually the easiest.

Step 4: Substitute the test point into the original inequality.
- If it makes the inequality TRUE, shade the side containing the test point.
- If it makes the inequality FALSE, shade the opposite side.

Worked Example 1

Problem: Graph y < x + 2.

Step 1: Graph the boundary line y = x + 2.
Slope = 1, y-intercept = 2. Plot (0, 2) and (1, 3), draw the line.

Step 2: The symbol is < (strict), so draw a dashed line.

Step 3: Test the point (0, 0).
Substitute: 0 < 0 + 2 → 0 < 2. True.

Step 4: Since (0, 0) satisfies the inequality, shade the region containing (0, 0) — which is below the line.

Result: The solution is the entire region below the dashed line y = x + 2.

Worked Example 2

Problem: Is the point (1, 4) a solution to 3x + 2y <= 12?

Substitute x = 1, y = 4:
3(1) + 2(4) = 3 + 8 = 11
Is 11 <= 12? Yes.

So (1, 4) is a solution. It lies in the shaded region.

Check (5, 5): 3(5) + 2(5) = 15 + 10 = 25. Is 25 <= 12? No. So (5, 5) is not a solution.

Reading Shaded Regions

When a graph is given and you must identify the inequality, follow these steps:
1. Find the equation of the boundary line.
2. Check whether the line is solid (includes =) or dashed (no =).
3. Pick a point in the shaded region and test it to determine whether the inequality uses < or >.

Systems of Inequalities (Preview)

When two or more linear inequalities are graphed on the same coordinate plane, the solution is the overlapping shaded region — where all inequalities are satisfied simultaneously. This concept extends directly to systems of inequalities, which appear on higher-level GED algebra questions.

Common Mistake to Avoid

Students often shade the wrong side of the boundary line. The test-point method is foolproof: always verify which side to shade by substituting a point (preferably the origin, unless it is on the boundary line) before committing to a shading direction. Never guess based on the direction of the inequality alone, because the position of variables in the inequality can reverse the expected side.

GED Test Tip

On the GED, linear inequality graphs often appear as multiple-choice questions showing four graphs and asking you to identify which one represents the given inequality. Quickly check two things: (1) is the boundary line solid or dashed? and (2) is the origin in the shaded region? Substituting (0, 0) into the given inequality tells you immediately whether the shaded region should include the origin. This two-step check eliminates wrong answers rapidly and is one of the most efficient strategies for this type of GED question.
"""),
]

class Command(BaseCommand):
    help = "Enrich lesson content for GED Algebra Inequalities Mastery"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(course__slug="ged-algebra-inequalities-mastery", order=order).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(self.style.SUCCESS("Done."))
