from django.core.management.base import BaseCommand
from courses.models import Lesson

LESSONS = [
    (1, """**Ratios, Rates, and Proportions**

A **ratio** compares two quantities and can be written as a:b or as the fraction a/b. Before working with any ratio, always simplify by dividing both parts by their greatest common factor. For example, the ratio 18:24 simplifies to 3:4 because both 18 and 24 share a GCF of 6.

There are two types of ratios to keep straight. A **part-to-part ratio** compares one group to another group (for example, boys to girls in a class). A **part-to-whole ratio** compares one group to the entire group (for example, boys to all students). The SAT frequently switches between these types in a single problem, so identify which type you need before you calculate.

A **unit rate** expresses a quantity relative to exactly one unit of something else. To find the unit rate, divide the total quantity by the number of units. If 5 pounds of apples cost $8.75, the cost per pound (unit rate) is $8.75 ÷ 5 = $1.75 per pound. Unit rates let you compare options directly. Unit rate applications include speed (miles per hour), density (grams per milliliter), and fuel efficiency (miles per gallon).

A **proportion** is a statement that two ratios are equal: a/b = c/d. To solve for an unknown, use **cross multiplication**: multiply the numerator of each fraction by the denominator of the other, then solve the resulting linear equation. If 3/5 = x/20, then 3 × 20 = 5 × x, so 60 = 5x, giving x = 12.

**Scale problems** are proportions in disguise. A map scale of 1 inch : 50 miles means you can set up 1/50 = measured inches/actual miles and solve. Model dimensions and architectural blueprints work the same way.

**Example 1.** A recipe calls for 3 cups of flour for every 2 cups of sugar. If a baker uses 9 cups of flour, how many cups of sugar are needed?

Set up the proportion: 3/2 = 9/x. Cross multiply: 3x = 18, so x = 6. The baker needs **6 cups of sugar**.

**Example 2.** Car A travels 150 miles on 6 gallons of gas. Car B travels 200 miles on 9 gallons. Which car gets better fuel efficiency?

Car A: 150 ÷ 6 = 25 mpg. Car B: 200 ÷ 9 ≈ 22.2 mpg. **Car A has better fuel efficiency.**

**Example 3.** On a map, 1 cm represents 40 km. Two cities are 7.5 cm apart on the map. What is the actual distance between them?

1/40 = 7.5/x → x = 7.5 × 40 = **300 km**.

**Common traps:**
- Mixing up part-to-part and part-to-whole. If the ratio of cats to dogs is 2:3, then cats are 2/5 of all pets, not 2/3.
- Forgetting to simplify before setting up proportions, which leads to messier arithmetic.
- Using inconsistent units on the two sides of a proportion (mixing miles and kilometers, for instance).

**Tip:** When a problem gives you a ratio and a total, find the total number of "parts" first. A ratio of 3:5 means 3 + 5 = 8 parts. Divide the total by 8 to find the value of one part, then multiply to find each group's share."""),

    (2, """**Percentages and Percent Change**

A **percent** means "per hundred." To find a percent of a number, convert the percent to a decimal by dividing by 100, then multiply. 35% of 80 = 0.35 × 80 = 28. You can also move the decimal point two places to the left: 35% → 0.35.

The **percent increase formula** is: (new value - old value) / old value × 100%. If a price rises from $40 to $52, the percent increase is (52 - 40)/40 × 100% = 12/40 × 100% = 30%. If the new value is smaller than the old value, the result is negative, representing a **percent decrease**.

To find the **original value** when you know a percent result, work backward by dividing. If a jacket costs $68 after a 15% discount, the sale price is 85% of the original (100% - 15% = 85%). So the original price = $68 ÷ 0.85 = $80.

**Successive percent changes** do not simply add together. A 20% increase followed by a 10% decrease multiplies the original by 1.20 and then by 0.90. The combined multiplier is 1.20 × 0.90 = 1.08, which is only an 8% net increase, not 10%.

Real-world applications follow directly from these ideas:
- **Tax:** final price = original × (1 + tax rate)
- **Discount:** sale price = original × (1 - discount rate)
- **Tip:** total bill = original × (1 + tip rate)
- **Markup:** selling price = cost × (1 + markup rate)

**Example 1.** A store raises the price of a TV from $500 to $575. What is the percent increase?

(575 - 500)/500 × 100% = 75/500 × 100% = **15% increase**.

**Example 2.** A shirt is on sale for $34 after a 20% discount. What was the original price?

$34 = original × (1 - 0.20) = original × 0.80. Original = $34 ÷ 0.80 = **$42.50**.

**Example 3.** A stock rises 30% one month and then falls 25% the next. What is the net percent change from the original price?

Multiplier: 1.30 × 0.75 = 0.975. Net change: (0.975 - 1) × 100% = **-2.5%**, a net decrease of 2.5%.

**Common traps:**
- Adding successive percent changes instead of multiplying the multipliers.
- Forgetting that finding the original from a percent result requires dividing, not multiplying.
- Confusing "25% more than" (multiply by 1.25) with "25% of" (multiply by 0.25).

**Tip:** Convert every percent to a decimal multiplier immediately. Then you can chain any number of changes by multiplication without ever writing a percent formula."""),

    (3, """**Unit Conversion and Measurement**

**Dimensional analysis** (also called the factor-label method) is the safest way to convert units. You multiply the given quantity by one or more **conversion fractions** — fractions equal to 1 — chosen so that unwanted units cancel and the desired units remain. Always write units next to every number and cancel them explicitly before calculating.

For example, to convert 180 minutes to hours, multiply by the conversion fraction (1 hour / 60 minutes): 180 min × (1 hr / 60 min) = 3 hr. The "min" unit appears in both numerator and denominator, so it cancels cleanly.

**Metric prefixes** attach to base units (meter, gram, liter) and multiply them by a power of 10:
- **kilo- (k):** × 1,000 (1 km = 1,000 m)
- **centi- (c):** × 0.01 (1 cm = 0.01 m, or 100 cm = 1 m)
- **milli- (m):** × 0.001 (1 mm = 0.001 m, or 1,000 mm = 1 m)

When the SAT provides a **table of conversion rates**, read it carefully. Identify the row and column that match your starting unit, read off the conversion factor, and set up your fraction so the old unit cancels. Always re-read the table instead of relying on memory.

**Two-step conversions** require chaining two conversion fractions. To convert miles per hour to feet per second:

Step 1 — convert miles to feet: 1 mile = 5,280 feet, so use (5,280 ft / 1 mi).
Step 2 — convert hours to seconds: 1 hour = 3,600 seconds, so use (1 hr / 3,600 s).

60 mph × (5,280 ft/1 mi) × (1 hr/3,600 s) = 60 × 5,280/3,600 ft/s = **88 ft/s**.

**Example 1.** A car travels at 90 km/h. How fast is this in meters per second?

90 km/h × (1,000 m/1 km) × (1 h/3,600 s) = 90,000/3,600 = **25 m/s**.

**Example 2.** A recipe requires 2.5 liters of broth. How many milliliters is that?

2.5 L × (1,000 mL/1 L) = **2,500 mL**.

**Example 3.** A fence runs 0.45 km. The owner wants to post signs every 15 meters. How many intervals are there (not counting the starting post)?

Convert 0.45 km to meters: 0.45 × 1,000 = 450 m. Number of intervals = 450 ÷ 15 = **30 intervals** (31 posts total, but the question asks for intervals).

**Common traps:**
- Flipping the conversion fraction so units don't cancel properly.
- Doing only one step of a two-step conversion and stopping early.
- Confusing "centi" and "milli" — students often remember one but forget the other. Memorize: 100 cm = 1 m and 1,000 mm = 1 m.

**Tip:** Before calculating, write out all units and draw slash-marks through the ones that cancel. If the units that remain match what the question asks for, your setup is correct. If not, flip one of your conversion fractions."""),

    (4, """**Statistics: Mean, Median, Mode, and Range**

The **mean** (arithmetic average) equals the sum of all values divided by the count of values. If you add a new value to a data set, the new mean is (old sum + new value) / (old count + 1). If you remove a value, recalculate with the reduced sum and count. The mean is sensitive to **outliers** — one extremely large or small value can pull it significantly.

The **median** is the middle value when data is arranged in order. For an odd number of values, the median is the single middle term. For an even number of values, the median is the average of the two middle terms. The median is **resistant to outliers**: adding one very large value shifts the median by at most one position, whereas it can shift the mean dramatically.

The **mode** is the value that appears most frequently. A data set can have:
- **No mode** — if all values appear equally often.
- **One mode** — the most common case.
- **Multiple modes** — if two or more values tie for most frequent (bimodal, trimodal, etc.).

The **range** = maximum value - minimum value. It measures total spread but is heavily influenced by outliers. The **interquartile range (IQR)** = Q3 - Q1, where Q1 is the median of the lower half and Q3 is the median of the upper half. IQR captures the spread of the middle 50% of data and is resistant to outliers.

**Standard deviation (SD)** measures how spread out data values are from the mean. A larger SD means values are more dispersed; a smaller SD means they cluster tightly around the mean. The SAT does not ask you to calculate SD from scratch, but you must understand what it represents conceptually.

**Effect of transforming data:**
- Adding a constant c to every value shifts the mean and median up by c but leaves the range, IQR, and SD unchanged.
- Multiplying every value by a constant k multiplies the mean, median, range, IQR, and SD all by k.

**Example 1.** The mean of five test scores is 82. A sixth score of 94 is added. What is the new mean?

Original sum = 82 × 5 = 410. New sum = 410 + 94 = 504. New mean = 504 ÷ 6 = **84**.

**Example 2.** Data set: 3, 7, 7, 9, 12, 15, 20. Find the median and IQR.

Ordered (already): median is the 4th value = **9**. Lower half: 3, 7, 7 → Q1 = 7. Upper half: 12, 15, 20 → Q3 = 15. IQR = 15 - 7 = **8**.

**Example 3.** If 5 is added to every value in a data set that has a mean of 20 and a standard deviation of 3, what are the new mean and SD?

New mean = 20 + 5 = **25**. New SD = **3** (unchanged, because all values shift equally so the spread stays the same).

**Common traps:**
- Forgetting to re-order data before finding the median.
- Assuming the mode is always the middle value or the mean.
- Thinking that adding a constant changes the standard deviation — it does not.

**Tip:** On the SAT, if a question asks which measure is "most affected" by an outlier, the answer is almost always the **mean**. If it asks which is "least affected," choose the **median** or **IQR**."""),

    (5, """**Data Interpretation: Tables and Bar Graphs**

A **two-way table** organizes data about two categorical variables into rows and columns. The numbers inside the table are **joint frequencies** (counts for a specific combination). The numbers in the last row and column are **marginal totals** (totals for one variable regardless of the other). The bottom-right cell is the **grand total**.

**Conditional frequencies** tell you what proportion of one group falls into a specific category. To find the conditional frequency of A given B, divide the cell value (A and B) by the row or column total for B. For example, if 30 out of 80 male respondents prefer option X, the conditional frequency of preferring X given male is 30/80 = 37.5%.

**Probability from a two-way table:**
- **Joint probability** P(A and B) = cell count / grand total.
- **Conditional probability** P(A | B) = cell count / total for B (row or column total, not grand total).

**Bar graphs** display categorical data as rectangular bars whose heights represent values. Read bar heights carefully by tracing a horizontal line to the y-axis scale. To compare categories, identify which bar is tallest or shortest, and calculate differences by subtracting the appropriate bar heights.

Watch for **misleading graphs**: a y-axis that does not start at zero makes small differences look enormous. Always check the y-axis scale before drawing conclusions about relative sizes.

**Example 1.** A two-way table shows survey responses:

|  | Likes Coffee | Dislikes Coffee | Total |
|---|---|---|---|
| Adults | 45 | 15 | 60 |
| Teens | 20 | 20 | 40 |
| Total | 65 | 35 | 100 |

What is P(Teen | Dislikes Coffee)?

P(Teen | Dislikes Coffee) = teens who dislike coffee / all who dislike coffee = 20/35 = **4/7 ≈ 57.1%**.

**Example 2.** Using the same table, what is the probability that a randomly selected person both likes coffee and is an adult?

P(Adult and Likes Coffee) = 45/100 = **0.45**.

**Example 3.** A bar graph shows monthly sales (in thousands): Jan = 12, Feb = 15, Mar = 10, Apr = 18. The y-axis starts at 8 instead of 0. A student claims February's sales were 50% higher than March's. Is this correct?

Actual values: 15 vs. 10 → (15 - 10)/10 × 100% = 50%. Yes, this specific claim is **correct**, but the graph makes it look like February's bar is roughly three times March's bar, which is visually misleading.

**Common traps:**
- Dividing by the grand total instead of the row/column total when computing conditional probability.
- Reading the wrong row or column in a two-way table — always label which variable is in rows vs. columns.
- Being misled by a truncated y-axis into misjudging how different two values are.

**Tip:** For conditional probability questions, ask yourself "given what?" That phrase tells you which row or column total to use as the denominator."""),

    (6, """**Scatterplots and Lines of Best Fit**

A **scatterplot** displays two numerical variables by plotting each data pair (x, y) as a point. The overall pattern of the points reveals the **correlation** between the variables:
- **Positive correlation:** as x increases, y tends to increase; points slope upward from left to right.
- **Negative correlation:** as x increases, y tends to decrease; points slope downward from left to right.
- **No correlation:** points appear scattered randomly with no clear direction.

The **line of best fit** (also called the least-squares regression line) is the straight line that best summarizes the relationship by minimizing the sum of squared vertical distances from each point to the line. The SAT provides the equation of this line; you do not need to derive it.

**Interpreting the equation y = mx + b in context:**
- The **slope m** represents the rate of change — how much y changes for each one-unit increase in x. Always attach units: "For each additional year, the population increases by approximately 250 people."
- The **y-intercept b** is the predicted value of y when x = 0. It only has a meaningful real-world interpretation if x = 0 is sensible in context (for example, if x is years since 2000, then b is the predicted value in the year 2000).

**Making predictions:** Substitute an x-value into the line equation to predict y. Be cautious of **extrapolation** — predicting far outside the range of the original data is unreliable because the linear trend may not continue.

**Correlation does not imply causation.** Two variables may be correlated because of a third hidden factor (a **confounding variable**), not because one directly causes the other.

A **residual** = actual y value - predicted y value. If a point is **above** the line, its residual is positive. If a point is **below** the line, its residual is negative. A residual of zero means the point lies exactly on the line.

**Example 1.** A line of best fit for hours studied (x) vs. exam score (y) has the equation y = 4.5x + 55. Predict the score for a student who studies 8 hours.

y = 4.5(8) + 55 = 36 + 55 = **91**.

**Example 2.** Using the same equation, a student studies 6 hours and scores 82. What is the residual?

Predicted: 4.5(6) + 55 = 27 + 55 = 82. Residual = 82 - 82 = **0**. The point lies exactly on the line.

**Example 3.** A scatterplot shows a strong negative correlation between daily screen time (hours) and GPA. A researcher concludes that screen time causes lower GPAs. What is wrong with this conclusion?

Correlation does not establish causation. A **confounding variable** — such as study habits or family environment — could cause both more screen time and lower grades. The data cannot prove a causal link.

**Common traps:**
- Confusing slope with the y-intercept when interpreting an equation in context. Always ask: "Which one changes when x changes by 1?" That is slope.
- Extrapolating wildly beyond the data range and treating the prediction as reliable.
- Concluding causation from a scatterplot. The SAT frequently presents correlation-causation questions; always choose the answer that merely describes an association.

**Tip:** When asked to interpret the slope, use the template: "For each one-unit increase in [x variable], [y variable] increases/decreases by [|slope|] [units of y]." This phrasing earns full credit and prevents mixing up slope and intercept."""),

    (7, """**Probability and Sampling**

**Basic probability** is defined as: P(event) = (number of favorable outcomes) / (total number of equally likely outcomes). Probability values always fall between 0 and 1 inclusive — P = 0 means impossible, P = 1 means certain. Any answer outside this range signals a setup error.

The **complement rule** states that P(not A) = 1 - P(A). If the probability it rains tomorrow is 0.3, then the probability it does not rain is 0.7. Use this rule whenever it is easier to count what you do not want.

**Independent events** are events where the outcome of one does not affect the other. For two independent events A and B: P(A and B) = P(A) × P(B). For example, flipping a coin and rolling a die are independent, so P(heads and a 4) = 1/2 × 1/6 = 1/12.

**Mutually exclusive events** cannot both occur at the same time. For mutually exclusive events A and B: P(A or B) = P(A) + P(B). Drawing a king and drawing a queen from one draw are mutually exclusive; P(king or queen) = 4/52 + 4/52 = 8/52 = 2/13.

**Representative sampling** is essential for drawing valid conclusions about a population. A **random sample** gives every member of the population an equal chance of being selected. A sample is **biased** if it systematically over- or under-represents certain groups:
- **Voluntary response bias:** people who respond to optional surveys tend to have stronger opinions than the average person.
- **Convenience sampling bias:** surveying only the people easiest to reach (for example, only students in one class) excludes most of the population.

The **margin of error** describes the uncertainty around a sample estimate. Larger samples produce smaller margins of error because they are more representative of the population. The SAT expects you to know this direction of the relationship, not to calculate margin of error from a formula.

**Example 1.** A bag contains 4 red, 6 blue, and 2 green marbles. One marble is drawn at random. What is the probability that it is not red?

Total = 12. P(red) = 4/12 = 1/3. P(not red) = 1 - 1/3 = **2/3**.

**Example 2.** A fair coin is flipped three times. What is the probability of getting heads all three times?

Each flip is independent. P(H and H and H) = 1/2 × 1/2 × 1/2 = **1/8**.

**Example 3 (sampling bias).** A school wants to know the average number of hours students sleep per night. A researcher posts an online survey on the school's social media page and collects 150 responses. Is this a representative sample?

No. This is **voluntary response bias** — only students who see the post and choose to respond participate. Students who are very sleep-deprived (or very well-rested) may be more motivated to respond, skewing the results. A better approach would be to randomly select students from the full enrollment list.

**Common traps:**
- Adding probabilities for independent events instead of multiplying. P(A and B) = P(A) × P(B), not P(A) + P(B).
- Forgetting that "or" for mutually exclusive events means add, but "or" for non-mutually exclusive events requires the addition rule: P(A or B) = P(A) + P(B) - P(A and B).
- Assuming a large sample eliminates bias. A large biased sample is still biased — sample size reduces random error, not systematic bias.

**Tip:** When the SAT asks you to evaluate a sampling method, look for whether every member of the target population had an equal chance of being included. If not, name the specific bias. The answer choice that says "the sample may not be representative because not all students had an equal chance of being selected" is almost always correct."""),
]


class Command(BaseCommand):
    help = "Enrich lesson content for SAT Math: Problem Solving & Data Analysis"

    def handle(self, *args, **options):
        for order, content in LESSONS:
            rows = Lesson.objects.filter(
                course__slug="sat-math-problem-solving", order=order
            ).update(content=content)
            self.stdout.write(f"  Lesson {order}: {rows} row(s) updated")
        self.stdout.write(
            self.style.SUCCESS(
                "Done enriching SAT Math: Problem Solving & Data Analysis lessons."
            )
        )
