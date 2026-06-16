from django.core.management.base import BaseCommand
from courses.models import Lesson

LESSONS = [
    (1, """Number Operations & Order of Operations (PEMDAS)

CONCEPT EXPLANATION

When a math problem contains more than one operation — addition, subtraction, multiplication, division, exponents, or parentheses — you cannot simply work from left to right. Mathematicians long ago agreed on a fixed sequence called the Order of Operations so that every person who solves the same expression arrives at the same answer. In the United States this sequence is remembered with the acronym PEMDAS:

  P — Parentheses (and all other grouping symbols such as brackets and braces)
  E — Exponents (powers and roots)
  M — Multiplication
  D — Division
  A — Addition
  S — Subtraction

A critical point that trips up many students: Multiplication and Division are actually equal in priority. You perform whichever one comes first as you read left to right. The same rule applies to Addition and Subtraction — they share equal priority and are handled left to right. Think of PEMDAS as four levels, not six separate steps:
  Level 1: Parentheses
  Level 2: Exponents
  Level 3: Multiplication and Division (left to right)
  Level 4: Addition and Subtraction (left to right)

Every arithmetic problem you encounter on the GED, no matter how complicated it looks, becomes manageable once you apply these four levels in order.

WORKED EXAMPLE

Simplify: 3 + 6 x (4 - 1)^2 / 9

Step 1 — Parentheses first.
  (4 - 1) = 3
  Expression becomes: 3 + 6 x 3^2 / 9

Step 2 — Exponents next.
  3^2 = 9
  Expression becomes: 3 + 6 x 9 / 9

Step 3 — Multiplication and Division, left to right.
  6 x 9 = 54    →    3 + 54 / 9
  54 / 9 = 6    →    3 + 6

Step 4 — Addition and Subtraction, left to right.
  3 + 6 = 9

The answer is 9.

COMMON TRAP

The most frequent mistake is treating PEMDAS as a strict left-to-right list where multiplication always comes before division, and addition always comes before subtraction. Many students look at 12 / 4 x 3 and divide last because they think multiplication outranks division. Working left to right: 12 / 4 = 3, then 3 x 3 = 9. If you mistakenly multiplied first you would get 12 / 12 = 1 — a completely different answer. Always remember: M and D are partners at the same level, handled left to right. So are A and S.

PRACTICAL GED TIP

The GED Mathematical Reasoning test supplies an on-screen calculator (the TI-30XS) for most questions. However, if you type a multi-operation expression carelessly, the calculator will still apply order of operations — and it will give the wrong answer if you enter the numbers in the wrong order. Before pressing any key, write out the expression on your scratch paper, identify each PEMDAS level, and simplify one level at a time. This thirty-second habit eliminates the majority of careless errors and is well worth the time investment on test day."""),

    (2, """Percentages

CONCEPT EXPLANATION

A percentage is a ratio that compares a number to 100. The word itself comes from the Latin "per centum," meaning "out of one hundred." Whenever you see 35%, it simply means 35 out of every 100 — or the fraction 35/100, which simplifies to 7/20, or the decimal 0.35. Being comfortable moving between these three forms (percent, fraction, decimal) is the foundation of all percentage work on the GED.

Three core percentage problems appear repeatedly on the GED:

1. Finding a percent of a number (the "part"):
   Part = Percent x Whole
   Convert the percent to a decimal first, then multiply.

2. Finding what percent one number is of another (the "rate"):
   Percent = (Part / Whole) x 100

3. Finding the original whole when you know the part and the percent (the "base"):
   Whole = Part / Percent   (where percent is in decimal form)

A fourth skill the GED tests heavily is percent change:
   Percent Change = ((New Value - Original Value) / Original Value) x 100
   A positive result is an increase; a negative result is a decrease.

WORKED EXAMPLE

A jacket originally costs $80. It is on sale for 25% off. After the discount, a 10% sales tax is applied. What is the final price?

Step 1 — Find the discount amount.
  25% of $80 = 0.25 x 80 = $20

Step 2 — Subtract the discount from the original price.
  $80 - $20 = $60   (sale price)

Step 3 — Calculate the sales tax on the sale price.
  10% of $60 = 0.10 x 60 = $6

Step 4 — Add the tax to the sale price.
  $60 + $6 = $66

The final price is $66.

COMMON TRAP

Students often confuse "percent of" with "percent off." A price that is 25% off is NOT the same as a price that is 25% of the original. If you pay 25% OF $80 you pay $20 — that is not a discounted price, that is an absurdly cheap price. You pay 25% OFF $80 by subtracting the 20-dollar discount, leaving $60. Read the problem language carefully every time.

A second trap involves stacking discounts. A 20% discount followed by another 10% discount is NOT the same as a 30% discount. Each percentage applies to a different base, so the combined effect is always slightly less than the sum of the two percentages.

PRACTICAL GED TIP

Memorize these benchmark conversions cold — they let you estimate quickly without a calculator and catch obviously wrong answer choices:
  50% = 1/2 = 0.5
  25% = 1/4 = 0.25
  75% = 3/4 = 0.75
  10% = 1/10 = 0.1
  20% = 1/5 = 0.2
  33.3% ≈ 1/3
  66.7% ≈ 2/3
  1% = 0.01

To find 10% of any number, simply move the decimal point one place to the left. To find 5%, take half of 10%. These mental shortcuts can save you 30-60 seconds per problem on the GED."""),

    (3, """Linear Equations in One Variable

CONCEPT EXPLANATION

An equation is a statement that two expressions are equal. A linear equation in one variable contains only one unknown — typically called x — and that variable is raised to the first power only (no x^2, no square roots of x). Examples: 2x + 5 = 13, or 3(x - 4) = x + 2.

The goal is always to isolate the variable: get x alone on one side of the equals sign. You accomplish this by performing the same operation on both sides of the equation, maintaining balance the way a scale stays level only if you add or remove the same weight from both sides.

The general strategy follows this sequence:
  1. Distribute (eliminate parentheses using the distributive property).
  2. Combine like terms on each side separately.
  3. Move variable terms to one side using addition or subtraction.
  4. Move constant terms to the other side using addition or subtraction.
  5. Isolate the variable by multiplying or dividing.
  6. Check your answer by substituting it back into the original equation.

Step 6 takes only ten seconds and will save you from submitting a wrong answer you could have caught yourself.

WORKED EXAMPLE

Solve for x: 3(2x - 4) = 2x + 8

Step 1 — Distribute the 3 on the left side.
  3 x 2x - 3 x 4 = 2x + 8
  6x - 12 = 2x + 8

Step 2 — Move variable terms to the left. Subtract 2x from both sides.
  6x - 2x - 12 = 8
  4x - 12 = 8

Step 3 — Move constants to the right. Add 12 to both sides.
  4x = 8 + 12
  4x = 20

Step 4 — Divide both sides by 4.
  x = 5

Step 5 — Check: substitute x = 5 into the original equation.
  Left side:  3(2(5) - 4) = 3(10 - 4) = 3(6) = 18
  Right side: 2(5) + 8 = 10 + 8 = 18  ✓

The solution is x = 5.

COMMON TRAP

The distributive property causes many errors when a negative sign precedes the parentheses. Consider -(x - 3). Students frequently write -x - 3, forgetting that the negative distributes to BOTH terms, making it -x + 3. Every term inside the parentheses gets multiplied by the factor outside — including its sign. A safe habit: rewrite -(x - 3) as -1(x - 3) to remind yourself to distribute the -1.

Another trap is performing an operation on only one term in an expression rather than the entire side. When you add 12 to the left side, it must be added to everything on the right side as well — not just to one term on the right.

PRACTICAL GED TIP

The GED often presents equations embedded inside word problems. Your first job is to translate the words into an equation. Memorize these translation phrases:
  "is" or "equals" → =
  "sum of" → +
  "difference of" → -
  "product of" → x
  "quotient of" → /
  "twice a number" → 2x
  "five more than a number" → x + 5
  "a number decreased by 3" → x - 3

Once you have the equation written, the solving steps are mechanical. Most GED algebra questions come down to correctly setting up the equation — the arithmetic itself is straightforward."""),

    (4, """Basic Geometry: Perimeter & Area

CONCEPT EXPLANATION

Geometry problems on the GED test your ability to measure and calculate properties of flat (two-dimensional) shapes. Two of the most fundamental measurements are perimeter and area.

PERIMETER is the total distance around the outside of a shape — the length of its boundary. You calculate it by adding up the lengths of all the sides. Perimeter is measured in linear units: inches, feet, centimeters, meters, etc.

AREA is the amount of surface a shape covers — the space inside its boundary. Area is measured in square units: square inches (in^2), square feet (ft^2), square meters (m^2), etc. The "squared" unit is not optional or decorative — it is the correct way to express area and the GED expects it.

Key formulas to memorize:

Rectangle:
  Perimeter = 2l + 2w   (where l = length, w = width)
  Area = l x w

Square (a rectangle where all sides are equal, side = s):
  Perimeter = 4s
  Area = s^2

Triangle (base = b, height = h, sides = a, b, c):
  Perimeter = a + b + c   (sum of all three sides)
  Area = (1/2) x b x h

Parallelogram:
  Area = b x h   (the height must be perpendicular to the base, NOT the slanted side)

Circle (radius = r, diameter = d = 2r):
  Circumference (perimeter) = 2 x pi x r   or   pi x d
  Area = pi x r^2
  Use pi ≈ 3.14 unless the problem says otherwise, or use the pi button on the TI-30XS.

WORKED EXAMPLE

A rectangular garden has a length of 12 feet and a width of 7 feet. A gardener wants to (a) fence the entire perimeter and (b) lay sod over the entire surface. How many feet of fencing and how many square feet of sod are needed?

Part (a) — Perimeter (fencing):
  P = 2l + 2w
  P = 2(12) + 2(7)
  P = 24 + 14
  P = 38 feet of fencing

Part (b) — Area (sod):
  A = l x w
  A = 12 x 7
  A = 84 square feet of sod

Notice that fencing is measured in feet (linear) while sod is measured in square feet (area). These are different units and cannot be added together or compared directly.

COMMON TRAP

The most common geometry mistake on the GED is confusing height with slant side in triangles and parallelograms. The height (also called the altitude) is always the perpendicular distance from the base to the opposite vertex or side — it forms a right angle with the base. If a triangle shows a slanted side of 10 and a perpendicular height of 8, the area formula uses 8, not 10. Using the slanted side instead of the true height is guaranteed to give a wrong answer.

A second trap: when a problem gives the diameter of a circle and asks you to compute the area, many students plug the diameter directly into A = pi x r^2. The formula requires the radius. Always halve the diameter before squaring: r = d / 2.

PRACTICAL GED TIP

The GED Mathematical Reasoning test provides a formula sheet on screen during the exam. You do NOT need to memorize every formula — but you do need to know what each variable in the formula means, and you need to recognize which formula applies to which shape. Spend your study time understanding the formulas rather than just memorizing them by rote. Practice identifying which measurement is the height versus the slant side, and make sure you always include the correct units (feet vs. square feet) in your answer, because some GED questions are designed to catch students who compute the right number but assign the wrong unit."""),
]

class Command(BaseCommand):
    help = "Enrich lesson content for GED Math Fundamentals"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(course__slug="ged-math-dasar", order=order).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(self.style.SUCCESS("Done."))
