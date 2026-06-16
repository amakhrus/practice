"""
Seed a comprehensive GED course on Data Analysis and Probability.

This course covers reading data from tables and charts, calculating statistics
(mean, median, mode, range), interpreting distributions, and understanding
probability concepts including single and compound events.

Run:
    python manage.py seed_ged_data_probability_mastery
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Data Analysis & Probability",
    "slug": "ged-data-analysis-probability-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A comprehensive course on data analysis and probability for the GED. Students learn to read and "
        "interpret tables, bar graphs, line graphs, and pie charts; calculate measures of center (mean, median, mode) "
        "and spread (range, standard deviation); understand probability of single and compound events; and apply "
        "statistical reasoning to real-world problems. Includes many worked examples and practice questions."
    ),
    "lessons": [
        (
            "1. Reading Data: Tables, Bar Graphs, and Line Graphs",
            r"""
**Data visualization** displays information in a format that is quick to understand. The GED tests your ability to extract information from common displays.

**Tables:**
A table organizes data into rows and columns. Always read the header row and column labels carefully.

Example table:
\[
\begin{array}{c|c|c|c}
\text{Month} & \text{Sales} & \text{Profit} & \text{Units Sold} \\
\hline
\text{January} & \$12,000 & \$3,200 & 240 \\
\text{February} & \$15,000 & \$4,100 & 300 \\
\text{March} & \$13,500 & \$3,700 & 270 \\
\end{array}
\]

From this table, you can quickly see that February had the highest sales (\$15,000) and the highest profit (\$4,100).

**Bar Graphs:**
Bar graphs compare categories using rectangular bars. The height (or length) of each bar represents the value.

[[figure:bar_graph_sales|Monthly sales comparison for four products.]]

Key reading skills:
- Read the title to understand what is displayed.
- Check the axis labels (x-axis and y-axis).
- Use the scale to determine approximate values.
- Compare bar heights to identify trends.

**Line Graphs:**
Line graphs show change over time. Each point represents a value at a specific time, and connecting lines show the trend.

[[figure:line_graph_temperature|Temperature trend throughout the week.]]

Advantages of line graphs:
- Show trends clearly.
- Make it easy to spot increases, decreases, and patterns.
- Can display multiple data series on the same graph.

Example interpretation: If a line graph shows temperature rising from Monday to Wednesday, then dropping Thursday to Friday, you can say temperature "increased early in the week, then decreased late in the week."

**Real-world context:** A store manager reviews weekly sales data from a table to identify which day sells the most. A nurse reads a patient's temperature graph to monitor fever trends.

Common mistake: misreading the scale. Always check if each grid line represents 1, 10, 100, or another unit.

💡 Tip: Before answering a question, spend 10 seconds identifying the title, labels, and scale. This prevents careless errors.

[[check:From a table showing monthly sales, how do you find the highest-selling month?|find the largest number in the sales column|Compare the values in the relevant column.]]
            """,
        ),
        (
            "2. Pie Charts and Percentages",
            r"""
**Pie charts** divide a whole into slices, where each slice represents a part of the total. The whole circle always represents 100%.

[[figure:pie_chart_budget|Family budget breakdown by category.]]

Reading a pie chart:
1. Identify the title and what each slice represents.
2. Read the percentages (or angles) for each slice.
3. Interpret the relative sizes: a larger slice means a larger percentage.
4. Add percentages to verify: they should sum to 100%.

**Converting pie chart percentages to angles:**
Since a full circle has 360°, multiply the percentage by 360° to find the angle.

Example: If a slice represents 25% of the budget:
\[
\text{Angle} = 0.25 \times 360° = 90°
\]

**Finding amounts from percentages:**
If a pie chart shows 40% of a $2,000 budget spent on rent:
\[
\text{Rent} = 0.40 \times 2,000 = 800 \text{ dollars}
\]

**Real-world context:** A company pie chart shows that 35% of employees work in sales, 25% in operations, and 40% in support. If there are 200 employees total:
- Sales: \(0.35 \times 200 = 70\) employees
- Operations: \(0.25 \times 200 = 50\) employees
- Support: \(0.40 \times 200 = 80\) employees

Common mistake: forgetting that percentages must sum to 100%. If a chart shows 30%, 40%, and 25%, something is missing (5%).

💡 Tip: Draw a mental line from the center to see angles. A quarter of a circle is 90° (25%), a half is 180° (50%), and a three-quarter is 270° (75%).

[[check:If a pie chart slice represents 20% of the total, what is the angle of that slice?|72°;;72 degrees|Multiply: \(0.20 \times 360° = 72°\).]]
            """,
        ),
        (
            "3. Mean, Median, Mode, and Range",
            r"""
These four **measures** describe a dataset in different ways.

**Mean (Average):**
The mean is the sum of all values divided by the number of values.

\[
\text{Mean} = \frac{\text{Sum of all values}}{\text{Number of values}}
\]

Example: Find the mean of 3, 7, 5, 9, and 6.
\[
\text{Mean} = \frac{3 + 7 + 5 + 9 + 6}{5} = \frac{30}{5} = 6
\]

**Median:**
The median is the middle value when data is arranged in order. It divides the dataset in half.

Example: For 3, 5, 6, 7, 9 (already sorted), the median is 6 (the middle value).
Example: For 3, 5, 6, 7, 9, 12 (six values), the median is the average of the two middle values: \(\frac{6+7}{2} = 6.5\).

**Mode:**
The mode is the value that appears most frequently.

Example: In the dataset 2, 3, 3, 3, 5, 7, 7, the mode is 3 (appears three times).
A dataset can have no mode (all values appear once), one mode (unimodal), or multiple modes (bimodal, multimodal).

**Range:**
The range measures spread. It is the difference between the largest and smallest values.

\[
\text{Range} = \text{Largest value} - \text{Smallest value}
\]

Example: For 3, 5, 6, 7, 9:
\[
\text{Range} = 9 - 3 = 6
\]

**When to use each:**
- **Mean:** Most common. Use when you want a single representative value. Affected by outliers (very large or small values).
- **Median:** Use when data has outliers. It is more "resistant" to extreme values.
- **Mode:** Use for categorical data or to identify the most popular value.
- **Range:** Use to understand spread and variability.

**Real-world context:** A manager reviews employee salaries: \$30k, \$35k, \$40k, \$45k, \$500k. The mean is \(\frac{30+35+40+45+500}{5} = \$130k\), but the median is \$40k. The median better represents "typical" salary because the CEO's \$500k salary is an outlier.

Common mistake: calculating mean wrong. Always add all values first, then divide by the count.

💡 Tip: Remember the order: "Mean is the average, Median is the middle, Mode is the most frequent, Range is the difference."

[[check:Find the median of 2, 8, 5, 3, 9, 1, 7.|5|Sort first: 1, 2, 3, 5, 7, 8, 9. The middle value is 5.]]
            """,
        ),
        (
            "5. Probability Basics: Single Events",
            r"""
**Probability** measures the likelihood of an event occurring, from 0 (impossible) to 1 (certain).

\[
\text{Probability} = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
\]

**Basic Example:**
A standard die has six faces numbered 1 to 6. The probability of rolling a 4 is:
\[
P(\text{rolling a 4}) = \frac{1}{6} \approx 0.167 \text{ or } 16.7\%
\]

The probability of rolling an even number (2, 4, or 6) is:
\[
P(\text{rolling an even}) = \frac{3}{6} = \frac{1}{2} = 0.5 \text{ or } 50\%
\]

**Key Probability Concepts:**

- **Probability of 0:** Event is impossible. Example: rolling a 7 on a standard die.
- **Probability of 1:** Event is certain. Example: rolling a number 1–6 on a standard die.
- **Probability between 0 and 1:** Event is possible but not certain.

**Complementary Events:**
The complement of an event is "not this event." The sum of an event's probability and its complement's probability is always 1.

\[
P(\text{event}) + P(\text{not event}) = 1
\]

Example: If the probability of rain tomorrow is 0.3 (30%), then the probability of no rain is \(1 - 0.3 = 0.7\) (70%).

**Theoretical vs. Experimental Probability:**
- **Theoretical:** Calculated based on the structure. Probability of heads on a fair coin is exactly 0.5.
- **Experimental:** Observed from actual trials. Flip a coin 100 times and record heads/tails.

**Real-world context:** A quality control manager tests 1,000 lightbulbs and finds 15 are defective. The experimental probability of a defective bulb is \(\frac{15}{1,000} = 0.015\) or 1.5%.

Common mistake: confusing "number of favorable outcomes" with "number of trials." Always use the formula carefully.

💡 Tip: If probability is 0.25, that means 1 in 4, or 25%. Probability is always between 0 and 1 (or 0% and 100%).

[[check:A bag has 3 red, 2 blue, and 5 white marbles. What is the probability of drawing a red marble?|3/10;;0.3;;30%|Total marbles: 10. Red marbles: 3. Probability: 3/10.]]
            """,
        ),
        (
            "6. Compound Probability: AND and OR",
            r"""
**Compound events** involve multiple outcomes.

**AND Events (Intersection):**
Both events must happen. Use multiplication.

\[
P(\text{A AND B}) = P(\text{A}) \times P(\text{B})
\]

(Assuming events are independent—one doesn't affect the other.)

Example: Probability of rolling a 3 on the first roll AND a 5 on the second roll of a die:
\[
P(\text{3 then 5}) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}
\]

Example: Probability of drawing a red marble from bag A AND a blue marble from bag B:
\[
P(\text{red AND blue}) = P(\text{red in A}) \times P(\text{blue in B})
\]

**OR Events (Union):**
At least one event happens. Use addition (and subtract overlap if needed).

\[
P(\text{A OR B}) = P(\text{A}) + P(\text{B}) - P(\text{A AND B})
\]

Example: Probability of rolling a 3 OR a 5 on a single die roll:
\[
P(\text{3 or 5}) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}
\]

(Note: There's no overlap—a single roll cannot be both 3 and 5, so we don't subtract.)

**Dependent Events:**
When one event affects another, use conditional probability.

Example: Drawing two cards from a deck without replacement. After drawing the first card, the deck has 51 cards left, not 52.

\[
P(\text{two aces}) = \frac{4}{52} \times \frac{3}{51}
\]

(First ace is 4 out of 52. Second ace is 3 out of 51.)

**Real-world context:** A student has a 70% chance of passing Math and an 80% chance of passing English. Assuming these are independent:
- Probability of passing both: \(0.70 \times 0.80 = 0.56\) or 56%.
- Probability of passing at least one: \(0.70 + 0.80 - (0.70 \times 0.80) = 0.94\) or 94%.

Common mistake: confusing AND (multiply) with OR (add). Remember: AND is more restrictive (lower probability), OR is less restrictive (higher probability).

💡 Tip: Draw a tree diagram or use a probability grid to visualize compound events.

[[check:A coin is flipped twice. What is the probability of getting heads on both flips?|1/4;;0.25||25%|P(HH) = P(H on 1st) * P(H on 2nd) = 0.5 * 0.5 = 0.25.]]
            """,
        ),
        (
            "7. Distributions and Outliers",
            r"""
A **distribution** describes how data is spread across a range.

**Normal Distribution (Bell Curve):**
Many real-world datasets follow a bell-shaped curve: most values cluster near the center (mean), with fewer values at the extremes.

[[figure:normal_distribution|Bell curve showing normal distribution and standard deviations.]]

Properties:
- Symmetric around the mean.
- About 68% of data falls within 1 standard deviation of the mean.
- About 95% falls within 2 standard deviations.
- About 99.7% falls within 3 standard deviations.

Example: Adult heights approximately follow a normal distribution with mean 70 inches and standard deviation 3 inches.
- 68% of adults are between 67 and 73 inches tall.
- 95% are between 64 and 76 inches.

**Skewed Distributions:**
Data that is not symmetric is "skewed."

- **Right skew (positive skew):** Tail extends to the right. Mean > Median. Example: income distribution (most earn moderate amounts, few earn very high).
- **Left skew (negative skew):** Tail extends to the left. Mean < Median. Example: test scores where most students score high, few score very low.

[[figure:skewed_distributions|Right-skewed and left-skewed distributions compared.]]

**Outliers:**
Values far from the rest of the data. They can significantly affect the mean but not the median.

Identifying outliers:
- **IQR method:** Outliers are below \(Q_1 - 1.5 \times \text{IQR}\) or above \(Q_3 + 1.5 \times \text{IQR}\).
- **Visual inspection:** Points far from others on a scatter plot or well separated on a number line.

Example: Dataset 2, 3, 4, 5, 6, 100. The value 100 is an outlier. It raises the mean from 4 (without 100) to 20 (with 100) but barely affects the median.

**Real-world context:** Test scores in a class: 75, 78, 80, 82, 85, 88, 92, 95, 98. The distribution is roughly symmetric. One student scores 35—an outlier. This dramatically lowers the class mean but not the median.

Common mistake: assuming all data follows a normal distribution. Always visualize your data.

💡 Tip: Understand that outliers are not always errors—they may be real, valuable data points. Investigate before removing.

[[check:If a distribution is right-skewed, which is true: Mean > Median or Mean < Median?|Mean > Median|Right skew pulls the mean toward the long tail (right).]]
            """,
        ),
        (
            "8. Data Analysis: Test-Taking Strategies",
            r"""
Master these strategies for the GED data and probability questions.

**Strategy 1 - Always read the graph carefully.**
Spend 15 seconds identifying:
- Title: What is the graph showing?
- Axes: What do x and y represent? What are the scales?
- Legend: Are there multiple data series?
- Units: Dollars? Percentages? Thousands?

One misread label ruins your answer.

**Strategy 2 - Estimate before calculating.**
If a pie chart shows slices that look like quarters and thirds, estimate 25%, 25%, and 50% before reading exact percentages. If your calculated answer is wildly different, recheck.

**Strategy 3 - For probability, simplify fractions.**
\(\frac{3}{6}\) simplifies to \(\frac{1}{2}\), which is easier to understand. Know common fractions:
- 1/2 = 0.5 = 50%
- 1/3 ≈ 0.33 = 33.3%
- 1/4 = 0.25 = 25%
- 1/5 = 0.2 = 20%

**Strategy 4 - For AND/OR problems, write out the formula.**
Don't try to do it mentally. Write:
\[
P(\text{A AND B}) = P(\text{A}) \times P(\text{B})
\]
Then substitute and calculate.

**Strategy 5 - Identify outliers visually.**
If a scatter plot has one point far from others, or a line graph has one sharp spike, note it. Questions often ask about outliers.

**Strategy 6 - Compare measures strategically.**
If you see both mean and median in a problem:
- If they're very different, there are outliers.
- If they're similar, data is roughly symmetric.
- Use this to interpret what "typical" looks like.

**Strategy 7 - Use context to eliminate answers.**
A probability can never be negative or greater than 1. A percentage on a pie chart can't be more than 100%. A median can never be larger than all values or smaller than all values.

**Common pitfalls to avoid:**
- Misreading the scale (treating 100 as 10, or vice versa).
- Forgetting units (mixing dollars and thousands).
- Confusing mean with median.
- Forgetting the "total" when calculating from a pie chart.
- Multiplying probabilities for OR events (should add).

**Quick double-check routine:**
1. Reread the question—what exactly is it asking?
2. Check your formula or method—is it correct?
3. Verify your arithmetic—did you add/multiply correctly?
4. Sanity test—does the answer make sense in context?

[[check:If a probability is 0.75, what percentage is that?|75%;;75|Multiply by 100: 0.75 * 100 = 75%.]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": "From the table below, which month had the highest sales?\n\n| Month | Sales |\n|-------|-------|\n| Jan   | $5,000 |\n| Feb   | $7,200 |\n| Mar   | $6,500 |",
            "difficulty": 1,
            "choices": [("February", True), ("January", False), ("March", False), ("Cannot be determined", False)],
            "explanation": r"Read the Sales column. February has $7,200, which is greater than January ($5,000) and March ($6,500).",
        },
        {
            "text": r"A pie chart shows 30% of a $2,000 budget spent on housing. How much is spent on housing?",
            "difficulty": 1,
            "choices": [("$600", True), ("$1,400", False), ("$300", False), ("$2,000", False)],
            "explanation": r"Multiply: $2,000 × 0.30 = $600.",
        },
        {
            "text": r"Find the mean of: 4, 8, 12, 16, 20.",
            "difficulty": 1,
            "choices": [("12", True), ("16", False), ("8", False), ("20", False)],
            "explanation": r"Mean = (4 + 8 + 12 + 16 + 20) / 5 = 60 / 5 = 12.",
        },
        {
            "text": r"Find the median of: 3, 7, 2, 9, 5.",
            "difficulty": 1,
            "choices": [("5", True), ("9", False), ("3", False), ("7", False)],
            "explanation": r"Sort: 2, 3, 5, 7, 9. The middle value is 5.",
        },
        {
            "text": r"Find the mode of: 2, 3, 3, 3, 5, 7, 7.",
            "difficulty": 1,
            "choices": [("3", True), ("2", False), ("7", False), ("5", False)],
            "explanation": r"The mode is the value that appears most often. 3 appears three times.",
        },
        {
            "text": r"Find the range of: 5, 12, 8, 3, 20.",
            "difficulty": 1,
            "choices": [("17", True), ("12", False), ("8", False), ("15", False)],
            "explanation": r"Range = Largest - Smallest = 20 - 3 = 17.",
        },
        {
            "text": r"A standard die is rolled. What is the probability of rolling a 3?",
            "difficulty": 1,
            "choices": [(r"\(\frac{1}{6}\)", True), (r"\(\frac{1}{3}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(\frac{1}{4}\)", False)],
            "explanation": r"There is 1 favorable outcome (rolling a 3) out of 6 possible outcomes.",
        },
        {
            "text": r"A bag has 5 red, 3 blue, and 2 green marbles. What is the probability of drawing a red marble?",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{2}\)", True), (r"\(\frac{1}{3}\)", False), (r"\(\frac{1}{5}\)", False), (r"\(\frac{2}{5}\)", False)],
            "explanation": r"Total marbles: 5 + 3 + 2 = 10. Red marbles: 5. Probability = 5/10 = 1/2.",
        },
        {
            "text": r"A coin is flipped twice. What is the probability of getting heads on both flips?",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{4}\)", True), (r"\(\frac{1}{2}\)", False), (r"\(\frac{1}{3}\)", False), (r"\(\frac{3}{4}\)", False)],
            "explanation": r"P(HH) = P(H on 1st) × P(H on 2nd) = 1/2 × 1/2 = 1/4.",
        },
        {
            "text": r"What is the probability of rolling a 3 OR a 5 on a single die roll?",
            "difficulty": 2,
            "choices": [(r"\(\frac{1}{3}\)", True), (r"\(\frac{1}{6}\)", False), (r"\(\frac{1}{2}\)", False), (r"\(\frac{2}{3}\)", False)],
            "explanation": r"P(3 or 5) = P(3) + P(5) = 1/6 + 1/6 = 2/6 = 1/3.",
        },
        {
            "text": r"If the probability of an event is 0.25, what is the probability it does NOT occur?",
            "difficulty": 1,
            "choices": [("0.75", True), ("0.25", False), ("1.0", False), ("0.5", False)],
            "explanation": r"P(not event) = 1 - P(event) = 1 - 0.25 = 0.75.",
        },
        {
            "text": r"A dataset has values: 2, 4, 6, 8, 100. Which is true?",
            "difficulty": 2,
            "choices": [("100 is an outlier", True), ("The mean equals the median", False), ("The mode is 6", False), ("The range is 8", False)],
            "explanation": r"The value 100 is far from the other values (2-8), making it an outlier.",
        },
        {
            "text": r"Calculate the mean of: 10, 20, 30, 40.",
            "difficulty": 1,
            "choices": [("25", True), ("30", False), ("20", False), ("35", False)],
            "explanation": r"Mean = (10 + 20 + 30 + 40) / 4 = 100 / 4 = 25.",
        },
        {
            "text": r"From a pie chart: Housing = 35%, Food = 25%, Other = 40%. If monthly budget is $2,000, how much is food?",
            "difficulty": 2,
            "choices": [("$500", True), ("$700", False), ("$800", False), ("$1,000", False)],
            "explanation": r"Food = $2,000 × 0.25 = $500.",
        },
        {
            "text": r"A spinner has 4 equal sections: Red, Blue, Green, Yellow. What is P(Red OR Blue)?",
            "difficulty": 2,
            "choices": [("1/2", True), ("1/4", False), ("1/8", False), ("3/4", False)],
            "explanation": r"P(Red or Blue) = P(Red) + P(Blue) = 1/4 + 1/4 = 1/2.",
        },
        {
            "text": r"Find the median: 15, 22, 18, 30, 25.",
            "difficulty": 1,
            "choices": [("22", True), ("25", False), ("18", False), ("30", False)],
            "explanation": r"Sort: 15, 18, 22, 25, 30. The middle value is 22.",
        },
        {
            "text": r"A probability is expressed as a fraction: 3/8. What is this as a decimal?",
            "difficulty": 1,
            "choices": [("0.375", True), ("0.38", False), ("0.3", False), ("0.8", False)],
            "explanation": r"Divide: 3 ÷ 8 = 0.375.",
        },
        {
            "text": r"A bar graph shows product sales: A=$5k, B=$8k, C=$6k, D=$9k. Which product had the lowest sales?",
            "difficulty": 1,
            "choices": [("A", True), ("B", False), ("C", False), ("D", False)],
            "explanation": r"Product A has the lowest value at $5,000.",
        },
        {
            "text": r"Two cards are drawn from a deck without replacement. What is P(both aces)?",
            "difficulty": 3,
            "choices": [(r"\(\frac{1}{221}\)", True), (r"\(\frac{1}{169}\)", False), (r"\(\frac{1}{52}\)", False), (r"\(\frac{1}{26}\)", False)],
            "explanation": r"P(both aces) = (4/52) × (3/51) = 12/2652 = 1/221.",
        },
        {
            "text": r"A pie chart has sections for Pizza (45%), Burgers (30%), and Salad. What percentage is Salad?",
            "difficulty": 1,
            "choices": [("25%", True), ("45%", False), ("30%", False), ("75%", False)],
            "explanation": r"Total must equal 100%. Salad = 100% - 45% - 30% = 25%.",
        },
        {
            "text": r"Find the range: 12, 5, 23, 8, 19, 30.",
            "difficulty": 1,
            "choices": [("25", True), ("30", False), ("18", False), ("12", False)],
            "explanation": r"Range = 30 - 5 = 25.",
        },
        {
            "text": r"A spinner has sections: 40% Blue, 35% Red, 25% Green. If you spin twice, what is P(Blue both times)?",
            "difficulty": 3,
            "choices": [("0.16 or 16%", True), ("0.80 or 80%", False), ("0.40 or 40%", False), ("0.75 or 75%", False)],
            "explanation": r"P(Blue both times) = 0.40 × 0.40 = 0.16.",
        },
        {
            "text": r"Mean of dataset is 50, median is 48. What can you infer?",
            "difficulty": 2,
            "choices": [("Data is likely right-skewed or has outliers", True), ("Data is perfectly symmetric", False), ("Mode is 50", False), ("No conclusion can be drawn", False)],
            "explanation": r"When mean > median, data is typically right-skewed or has high outliers.",
        },
        {
            "text": r"A line graph shows temperature from Monday to Friday: 65°, 68°, 70°, 69°, 66°. What trend is shown?",
            "difficulty": 2,
            "choices": [("Temperature rose until Wednesday, then fell", True), ("Temperature steadily increased", False), ("Temperature steadily decreased", False), ("Temperature was constant", False)],
            "explanation": r"The line rises from 65 to 70 (Mon-Wed), then falls to 66 (Wed-Fri).",
        },
        {
            "text": r"If P(event) = 0.6, what is P(NOT event) expressed as a fraction?",
            "difficulty": 2,
            "choices": [(r"\(\frac{2}{5}\)", True), (r"\(\frac{3}{5}\)", False), (r"\(\frac{1}{5}\)", False), (r"\(\frac{4}{5}\)", False)],
            "explanation": r"P(NOT event) = 1 - 0.6 = 0.4 = 2/5.",
        },
        {
            "text": r"A bar graph shows monthly revenue: Jan=$12k, Feb=$15k, Mar=$18k, Apr=$20k. Which statement is true?",
            "difficulty": 2,
            "choices": [("Revenue increased every month", True), ("Revenue stayed the same", False), ("Revenue decreased in April", False), ("January had the highest revenue", False)],
            "explanation": r"Each month's revenue is higher than the previous: 12 < 15 < 18 < 20.",
        },
        {
            "text": r"A dataset: 10, 15, 15, 20, 25. What is the mode?",
            "difficulty": 1,
            "choices": [("15", True), ("20", False), ("17.5", False), ("No mode", False)],
            "explanation": r"15 appears twice; all others appear once. Mode is 15.",
        },
        {
            "text": r"P(A) = 0.3, P(B) = 0.5. If A and B are independent, what is P(A AND B)?",
            "difficulty": 2,
            "choices": [("0.15", True), ("0.8", False), ("0.35", False), ("0.6", False)],
            "explanation": r"P(A AND B) = P(A) × P(B) = 0.3 × 0.5 = 0.15.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the GED Data Analysis & Probability Mastery course."

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

        for item in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course,
                qtype="mcq",
                text=item["text"],
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=is_correct)

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
