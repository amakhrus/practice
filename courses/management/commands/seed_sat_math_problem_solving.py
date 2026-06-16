"""
Seed data: 'SAT Math: Problem Solving & Data Analysis' -- a deep-dive course on the
SAT Problem Solving & Data Analysis domain.

Covers ratios, rates, and proportions; percentages and percent change; unit conversion
and measurement; statistics (mean, median, mode, range); data interpretation from
tables and bar graphs; scatterplots and lines of best fit; and probability and sampling.

Run:
    python manage.py seed_sat_math_problem_solving
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "SAT Math: Problem Solving & Data Analysis",
    "slug": "sat-math-problem-solving",
    "program": "SAT",
    "subject": "math",
    "description": (
        "A focused deep-dive into the SAT's Problem Solving & Data Analysis domain, covering "
        "ratios, rates, proportions, percentages, unit conversion, and the statistics and "
        "probability skills tested on every Digital SAT. "
        "You will learn to read and interpret tables, bar graphs, and scatterplots, calculate "
        "measures of center and spread, evaluate sampling methods, and apply probability rules "
        "to realistic survey and experiment scenarios."
    ),
    "lessons": [
        (
            "1. Ratios, Rates, and Proportions",
            "A **ratio** compares two quantities using division. It can be written as a fraction, "
            "with a colon, or in words: the ratio of 3 red marbles to 5 blue marbles is 3/5, 3:5, "
            "or '3 to 5'. Ratios tell you the relative size of quantities, not necessarily the "
            "actual amounts.\n\n"
            "A **rate** is a special ratio that compares quantities with different units. The most "
            "useful form is the **unit rate** -- the amount per one unit of the denominator. "
            "If a car travels 240 miles on 8 gallons of gas, the unit rate is 240 / 8 = 30 miles "
            "per gallon.\n\n"
            "A **proportion** sets two ratios equal to each other:\n"
            "- If 3 pounds of apples cost $4.50, how much do 7 pounds cost?\n"
            "- Set up: 3/4.50 = 7/x. Cross-multiply: 3x = 31.50, so x = $10.50.\n\n"
            "**Setting up proportions step by step:**\n"
            "- Identify the two quantities being compared (apples and dollars above).\n"
            "- Write the known ratio on one side and the unknown on the other, keeping units "
            "consistent (apples over dollars on both sides).\n"
            "- Cross-multiply to solve.\n\n"
            "**Scale problems** use proportions to convert between a model and the real world. "
            "If a map scale is 1 inch = 50 miles, then 3.5 inches represents 3.5 x 50 = 175 miles.\n\n"
            "**Worked example:** A recipe calls for 2 cups of flour for every 3 cups of oats. "
            "If you want to use 9 cups of oats, how many cups of flour do you need?\n"
            "- Ratio: flour/oats = 2/3.\n"
            "- Set up: 2/3 = x/9. Cross-multiply: 3x = 18, so x = 6 cups of flour.\n\n"
            "- **Part-to-whole ratios:** If the ratio of boys to girls in a class is 3:5, then "
            "boys make up 3/(3+5) = 3/8 of the class.\n"
            "- **Equivalent ratios:** Multiply or divide both parts by the same number to scale "
            "a ratio up or down (just like equivalent fractions).\n\n"
            "⚠️ Common mistake: confusing part-to-part ratios (3:5) with part-to-whole fractions "
            "(3/8). A ratio of 3:5 does NOT mean 3 out of 5 -- it means 3 out of every 8 total.\n\n"
            "💡 Tip: always label units when setting up a proportion. Keeping track of labels "
            "helps you catch errors before they cost you points."
        ),
        (
            "2. Percentages and Percent Change",
            "**Percent** means 'per hundred.' The foundational relationship is:\n\n"
            "part = percent x whole  (where percent is written as a decimal)\n\n"
            "This one formula handles three types of SAT percent questions:\n"
            "- Find the part: 'What is 30% of 80?' --> 0.30 x 80 = 24.\n"
            "- Find the percent: '24 is what percent of 80?' --> 24/80 = 0.30 = 30%.\n"
            "- Find the whole: '24 is 30% of what number?' --> 24/0.30 = 80.\n\n"
            "**Percent increase and percent decrease** are the two most commonly tested "
            "percent applications on the SAT:\n\n"
            "percent change = (new value - original value) / original value x 100\n\n"
            "- A salary rises from $50,000 to $57,500: change = 7,500 / 50,000 = 0.15 = 15% increase.\n"
            "- A price drops from $200 to $170: change = -30 / 200 = -0.15 = 15% decrease.\n\n"
            "**Shortcut multipliers** speed up calculations:\n"
            "- Increase by 20%: multiply by 1.20.\n"
            "- Decrease by 15%: multiply by 0.85.\n"
            "- Apply a 40% markup then a 40% discount: multiply by 1.40 x 0.60 = 0.84 "
            "(an 16% net decrease -- NOT back to the original!).\n\n"
            "**Worked example:** A store buys a jacket for $80 and marks it up 25%. A week later "
            "they put it on a 20% off sale. What is the final sale price?\n"
            "- After markup: $80 x 1.25 = $100.\n"
            "- After discount: $100 x 0.80 = $80.\n"
            "- The final price is $80 -- back to cost, but NOT the original retail.\n\n"
            "- **Successive percent changes** are multiplicative, not additive. A 25% increase "
            "followed by a 25% decrease gives 1.25 x 0.75 = 0.9375, a net loss of 6.25%.\n"
            "- **Percent of a percent:** '20% of 15%' means 0.20 x 0.15 = 0.03 = 3%.\n\n"
            "⚠️ Common mistake: dividing by the NEW value instead of the ORIGINAL when "
            "calculating percent change. Percent change always uses the starting value as "
            "the denominator.\n\n"
            "💡 Tip: convert percent to a decimal multiplier and multiply -- it is faster "
            "and more reliable than the formula, especially on the calculator-active section."
        ),
        (
            "3. Unit Conversion and Measurement",
            "**Unit conversion** means rewriting a measurement in different units without "
            "changing its value. The tool for this is **dimensional analysis** -- multiplying "
            "by a conversion factor written as a fraction equal to 1.\n\n"
            "**Dimensional analysis in three steps:**\n"
            "1. Write the original quantity as a fraction.\n"
            "2. Multiply by a conversion fraction so the unwanted unit cancels.\n"
            "3. Simplify.\n\n"
            "Example: convert 72 miles per hour to feet per second.\n"
            "- 72 miles/1 hr x 5,280 ft/1 mile x 1 hr/3,600 sec\n"
            "- The 'miles' cancel and the 'hr' cancel: 72 x 5,280 / 3,600 = 105.6 ft/sec.\n\n"
            "**Common SAT conversion facts you should know:**\n"
            "- Length: 1 foot = 12 inches; 1 yard = 3 feet; 1 mile = 5,280 feet.\n"
            "- Time: 1 minute = 60 seconds; 1 hour = 60 minutes.\n"
            "- Weight: 1 pound = 16 ounces; 1 ton = 2,000 pounds.\n"
            "- The SAT provides metric conversions in the reference sheet when needed.\n\n"
            "**Reading conversion tables:** The Digital SAT sometimes gives a table of "
            "conversion factors or exchange rates and asks you to convert a given quantity. "
            "Identify which row or column matches the units you are starting with, then "
            "multiply or divide as indicated.\n\n"
            "**Worked example:** A recipe calls for 3.5 cups of milk. A chef has a container "
            "that holds 2 pints. 1 pint = 2 cups. Does the chef have enough?\n"
            "- Convert pints to cups: 2 pints x 2 cups/pint = 4 cups.\n"
            "- 4 cups > 3.5 cups, so yes, the chef has enough.\n\n"
            "- **Multi-step conversions:** chain the fractions so each unwanted unit cancels "
            "before you multiply everything out.\n"
            "- **Rate conversions:** when converting rates (like mph to m/s), convert both "
            "the numerator and denominator units separately.\n\n"
            "⚠️ Common mistake: multiplying when you should divide (or vice versa) during "
            "unit conversion. If the answer seems unreasonably large or small, you probably "
            "used the conversion factor upside-down.\n\n"
            "💡 Tip: write the units in your conversion fraction so they visually cancel "
            "like variables in algebra. If the unwanted unit does not cancel, flip the fraction."
        ),
        (
            "4. Statistics: Mean, Median, Mode, and Range",
            "Statistics questions make up a large portion of the SAT Problem Solving domain. "
            "The four key descriptors the SAT tests are **mean**, **median**, **mode**, "
            "and **range**.\n\n"
            "**Mean (average):** Add all values and divide by the count.\n"
            "- Data: 5, 8, 8, 10, 14. Sum = 45. Count = 5. Mean = 45/5 = 9.\n\n"
            "**Median:** The middle value when data is in order. For an even count, it is "
            "the average of the two middle values.\n"
            "- Odd count: 3, 6, 9, 12, 15 --> median = 9.\n"
            "- Even count: 4, 7, 11, 16 --> median = (7+11)/2 = 9.\n\n"
            "**Mode:** The value(s) that appear most often. A data set can have one mode, "
            "more than one mode, or no mode if all values are equally frequent.\n"
            "- 2, 3, 3, 5, 7 --> mode = 3.\n\n"
            "**Range:** The highest value minus the lowest. Measures how spread out the data is.\n"
            "- 2, 3, 3, 5, 7 --> range = 7 - 2 = 5.\n\n"
            "**Effect of adding or removing a value:**\n"
            "- Adding a value equal to the mean leaves the mean unchanged.\n"
            "- Adding a high outlier raises the mean more than the median.\n"
            "- Removing the highest value always decreases the range.\n\n"
            "**Worked example:** A student's five quiz scores are 72, 85, 90, 90, and 93. "
            "Find mean, median, mode, and range.\n"
            "- Mean: (72 + 85 + 90 + 90 + 93) / 5 = 430 / 5 = 86.\n"
            "- Median: scores in order are 72, 85, 90, 90, 93 --> middle is 90.\n"
            "- Mode: 90 (appears twice).\n"
            "- Range: 93 - 72 = 21.\n\n"
            "- **Outliers** pull the mean toward them but barely affect the median. "
            "When data is skewed, the median better represents 'typical.'\n"
            "- **The SAT may give the mean and ask for a missing value:** if the mean of "
            "5 numbers is 10, their total is 50. Find the missing number by subtraction.\n\n"
            "⚠️ Common mistake: forgetting to put data in order before finding the median. "
            "The median is the middle position, not the middle value as written.\n\n"
            "💡 Tip: for 'find the missing value given the mean' questions, use "
            "total = mean x count and subtract the known values."
        ),
        (
            "5. Data Interpretation: Tables and Bar Graphs",
            "A large portion of SAT data questions present information in a **two-way table** "
            "or a **bar chart** and ask you to read, calculate, and interpret values.\n\n"
            "[[figure:bar_chart_sales|A bar chart comparing values across categories]]\n\n"
            "**Two-way tables** organize data by two categorical variables (like grade level "
            "and preferred subject). Each cell shows a count or frequency.\n\n"
            "| | Math | English | Science | Total |\n"
            "|---|---|---|---|---|\n"
            "| 10th Grade | 45 | 30 | 25 | 100 |\n"
            "| 11th Grade | 35 | 40 | 25 | 100 |\n"
            "| Total | 80 | 70 | 50 | 200 |\n\n"
            "From this table:\n"
            "- The proportion of ALL students who prefer Math = 80/200 = 40%.\n"
            "- The **conditional frequency** of 10th graders preferring Math = 45/100 = 45%.\n"
            "- The **joint frequency** of 11th graders preferring English = 40.\n\n"
            "**Bar charts** display categorical data as rectangular bars. The SAT may ask you "
            "to read exact values, compare categories, or calculate a percent difference.\n\n"
            "**Reading bar charts step by step:**\n"
            "1. Read the title and axis labels carefully.\n"
            "2. Identify the scale (each gridline value).\n"
            "3. Read the height of the relevant bar by comparing to the scale.\n"
            "4. Perform any requested calculation using those values.\n\n"
            "**Worked example:** Use the school preference table above. A researcher claims "
            "that 11th graders prefer English more than 10th graders do. Is this supported?\n"
            "- 10th grade English rate: 30/100 = 30%.\n"
            "- 11th grade English rate: 40/100 = 40%.\n"
            "- Yes, 40% > 30%, so the claim is supported by the data.\n\n"
            "- **Relative frequency:** a cell count divided by the row total, column total, "
            "or grand total -- know which denominator the question asks for.\n"
            "- **Marginal frequency:** the totals in the margins (last row or column).\n\n"
            "⚠️ Common mistake: using the grand total when the question asks for a "
            "conditional frequency (a row or column total is the correct denominator).\n\n"
            "💡 Tip: underline the exact group the question asks about before calculating "
            "-- 'of 10th graders' means use the 10th-grade row total, not the grand total."
        ),
        (
            "6. Scatterplots and Lines of Best Fit",
            "A **scatterplot** displays data as individual points on a coordinate plane, "
            "with one variable on each axis. The pattern of points shows the **association** "
            "between the two variables.\n\n"
            "[[figure:scatter_plot_correlation|A scatterplot with a line of best fit]]\n\n"
            "**Types of association:**\n"
            "- **Positive:** as x increases, y tends to increase (points rise left to right).\n"
            "- **Negative:** as x increases, y tends to decrease (points fall left to right).\n"
            "- **No association:** no clear trend in any direction.\n"
            "- **Strength:** a tight cluster around the trend line is a strong association; "
            "a wide scatter is weak.\n\n"
            "**Line of best fit (trend line):** a straight line drawn through the cloud of "
            "points to minimize the overall distance from each point to the line. It is written "
            "in the form y = mx + b.\n\n"
            "**Interpreting slope and y-intercept in context:**\n"
            "- Slope = the change in y for each one-unit increase in x.\n"
            "  Example: if a line of best fit for (hours studied, test score) has slope 4, "
            "  each additional hour of studying is associated with a 4-point score increase.\n"
            "- y-intercept = the predicted y-value when x = 0.\n"
            "  Example: a y-intercept of 55 means a student who studied 0 hours is predicted "
            "  to score 55 points.\n\n"
            "**Making predictions:** substitute the given x into the line equation.\n"
            "- Line: score = 4(hours) + 55. Predict for 7 hours: 4(7) + 55 = 83.\n\n"
            "**Worked example:** A scatterplot shows hours of exercise per week (x) and "
            "resting heart rate in beats per minute (y). The line of best fit is "
            "y = -2x + 80.\n"
            "- Slope = -2: each additional hour of exercise per week is associated with a "
            "  2 bpm decrease in resting heart rate.\n"
            "- y-intercept = 80: a person who exercises 0 hours per week is predicted to "
            "  have a resting heart rate of 80 bpm.\n"
            "- Predict for 10 hours: y = -2(10) + 80 = 60 bpm.\n\n"
            "- **Correlation vs. causation:** a scatterplot shows association, NOT proof "
            "that one variable causes the other. A confounding variable could explain both.\n"
            "- **Outliers on scatterplots:** a point far from the trend line is an outlier "
            "and can affect the slope and y-intercept of the best-fit line.\n\n"
            "⚠️ Common mistake: interpreting a strong correlation as proof of causation. "
            "The SAT frequently tests whether students understand that 'associated with' is "
            "not the same as 'causes.'\n\n"
            "💡 Tip: to find the value predicted by the line of best fit, plug the given "
            "x into the equation -- do not try to read it off the graph visually unless "
            "the question specifically tells you to."
        ),
        (
            "7. Probability and Sampling",
            "**Probability** measures how likely an event is to occur, expressed as a "
            "number between 0 (impossible) and 1 (certain).\n\n"
            "Basic probability formula:\n"
            "P(event) = (number of favorable outcomes) / (total number of equally likely outcomes)\n\n"
            "- P(rolling a 3 on a fair die) = 1/6.\n"
            "- P(drawing a red card from a standard deck) = 26/52 = 1/2.\n\n"
            "**Complementary events:** P(A does NOT happen) = 1 - P(A happens).\n"
            "- P(not rolling a 3) = 1 - 1/6 = 5/6.\n\n"
            "**Conditional probability:** P(A | B) = the probability of A given that B has "
            "already occurred. Use a restricted sample space.\n"
            "- In a class of 30 students, 12 play sports and 8 play sports AND are in the "
            "  honor society. Given a student plays sports, P(honor society) = 8/12 = 2/3.\n\n"
            "**Worked example:** A survey of 200 voters found 120 support Measure A and "
            "80 do not. Of the 120 supporters, 90 are registered in Party X. What is the "
            "probability that a randomly selected supporter of Measure A is in Party X?\n"
            "- Restrict to the 120 supporters: P = 90/120 = 0.75 = 75%.\n\n"
            "**Sampling methods and representativeness:**\n"
            "- A **representative sample** reflects the population it is drawn from. "
            "  Random selection helps ensure representativeness.\n"
            "- **Biased samples** over- or under-represent certain groups, making "
            "  conclusions unreliable. Surveying only gym members about exercise habits "
            "  is a biased sample.\n"
            "- **Margin of error:** a measure of the uncertainty in a survey estimate. "
            "  A result of '52% +/- 3%' means the true population value is likely between "
            "  49% and 55%. Larger samples generally produce smaller margins of error.\n\n"
            "- **Experimental vs. observational study:** in an experiment, researchers "
            "  randomly assign subjects to conditions, allowing causal conclusions. "
            "  In an observational study, researchers only observe and record, so they "
            "  can conclude association but NOT causation.\n"
            "- **Generalizing results:** conclusions can only be generalized to the "
            "  population that the sample was randomly drawn from.\n\n"
            "⚠️ Common mistake: concluding causation from an observational study or a "
            "survey. The SAT tests this distinction directly -- look for the words "
            "'randomly assigned' to know if a causal claim is valid.\n\n"
            "💡 Tip: for conditional probability, mentally cross out everyone outside "
            "the given condition and recalculate using only the restricted group."
        ),
    ],
    "mcqs": [
        # ── Lesson 1: Ratios, Rates, and Proportions ──────────────────────────
        {
            "text": (
                "A car travels 312 miles in 6 hours at a constant speed. "
                "At this rate, how many miles will it travel in 8 hours?"
            ),
            "difficulty": 1,
            "choices": [
                ("416 miles", True),
                ("234 miles", False),
                ("384 miles", False),
                ("480 miles", False),
            ],
            "explanation": (
                "Unit rate: 312 / 6 = 52 miles per hour.\n"
                "Distance in 8 hours: 52 x 8 = 416 miles.\n"
                "The trap 384 uses 48 mph (312 / 6.5); the trap 234 divides 312 by 8 "
                "instead of finding the rate first.\n"
                "Pro tip: find the unit rate first, then scale to the new quantity."
            ),
        },
        {
            "text": (
                "In a school, the ratio of students who prefer online learning to those "
                "who prefer in-person learning is 3:7. If there are 420 students in total, "
                "how many prefer in-person learning?"
            ),
            "difficulty": 2,
            "choices": [
                ("294", True),
                ("126", False),
                ("210", False),
                ("147", False),
            ],
            "explanation": (
                "The ratio 3:7 means 7 out of every 10 students prefer in-person learning.\n"
                "In-person students: (7/10) x 420 = 294.\n"
                "The trap 126 calculates the online group (3/10 x 420).\n"
                "The trap 210 splits 420 in half.\n"
                "Pro tip: convert the ratio to a fraction of the whole: "
                "in-person share = 7 / (3+7) = 7/10."
            ),
        },
        {
            "text": (
                "A map uses a scale of 1.5 inches = 30 miles. "
                "Two cities are 5 inches apart on the map. "
                "What is the actual distance between the cities?"
            ),
            "difficulty": 2,
            "choices": [
                ("100 miles", True),
                ("45 miles", False),
                ("75 miles", False),
                ("150 miles", False),
            ],
            "explanation": (
                "Unit rate: 30 miles / 1.5 inches = 20 miles per inch.\n"
                "Actual distance: 20 x 5 = 100 miles.\n"
                "The trap 75 uses 15 miles per inch (30 / 2 instead of 30 / 1.5).\n"
                "Pro tip: find miles per inch first, then multiply by the map distance."
            ),
        },
        {
            "text": (
                "A recipe uses a flour-to-sugar ratio of 5:2. "
                "A baker wants to use 14 cups of sugar. "
                "How many cups of flour are needed?"
            ),
            "difficulty": 1,
            "choices": [
                ("35", True),
                ("5.6", False),
                ("28", False),
                ("70", False),
            ],
            "explanation": (
                "Set up proportion: flour/sugar = 5/2 = x/14.\n"
                "Cross-multiply: 2x = 70, so x = 35.\n"
                "The trap 5.6 divides 14 by 2.5; the trap 28 multiplies 14 by 2 instead "
                "of by 5/2.\n"
                "Pro tip: cross-multiply, then divide by the coefficient of x."
            ),
        },
        # ── Lesson 2: Percentages and Percent Change ─────────────────────────
        {
            "text": (
                "A laptop originally priced at $800 is on sale for 15% off. "
                "What is the sale price?"
            ),
            "difficulty": 1,
            "choices": [
                ("$680", True),
                ("$120", False),
                ("$720", False),
                ("$692", False),
            ],
            "explanation": (
                "15% off means you pay 85%: $800 x 0.85 = $680.\n"
                "Alternatively, discount = 0.15 x 800 = $120; price = 800 - 120 = $680.\n"
                "The trap $120 gives only the discount amount.\n"
                "The trap $720 uses 90% instead of 85%.\n"
                "Pro tip: 'percent off' means multiply by (1 - rate). "
                "'15% off' = multiply by 0.85."
            ),
        },
        {
            "text": (
                "A town's population grew from 12,000 to 13,500 over one year. "
                "What was the percent increase in population?"
            ),
            "difficulty": 2,
            "choices": [
                ("12.5%", True),
                ("11.1%", False),
                ("15%", False),
                ("1.5%", False),
            ],
            "explanation": (
                "Percent change = (new - original) / original x 100.\n"
                "= (13,500 - 12,000) / 12,000 x 100 = 1,500 / 12,000 x 100 = 12.5%.\n"
                "The trap 11.1% divides by the new value (1,500 / 13,500).\n"
                "Pro tip: always divide by the ORIGINAL (starting) value."
            ),
        },
        {
            "text": (
                "A store marks up a jacket by 40% and then offers a 25% sale discount. "
                "What is the overall percent change in price from the original?"
            ),
            "difficulty": 3,
            "choices": [
                ("5% increase", True),
                ("15% decrease", False),
                ("65% increase", False),
                ("No change", False),
            ],
            "explanation": (
                "Apply successive multipliers: 1.40 x 0.75 = 1.05.\n"
                "1.05 represents a 5% overall increase.\n"
                "The trap 'No change' wrongly assumes +40% and -25% cancel.\n"
                "The trap 15% decrease subtracts 40 - 25 = 15 instead of multiplying.\n"
                "Pro tip: for successive percent changes, multiply the decimal "
                "multipliers together."
            ),
        },
        {
            "text": (
                "48 is 60% of what number?"
            ),
            "difficulty": 1,
            "choices": [
                ("80", True),
                ("28.8", False),
                ("72", False),
                ("120", False),
            ],
            "explanation": (
                "Use part = percent x whole: 48 = 0.60 x whole.\n"
                "Whole = 48 / 0.60 = 80.\n"
                "The trap 28.8 multiplies 48 by 0.60 instead of dividing.\n"
                "Pro tip: 'is X% of what?' means divide by the decimal percent."
            ),
        },
        # ── Lesson 3: Unit Conversion and Measurement ─────────────────────────
        {
            "text": (
                "A runner completes a 10-kilometer race. "
                "Given that 1 kilometer = 0.621 miles, "
                "approximately how many miles did the runner travel? "
                "Round to the nearest tenth."
            ),
            "difficulty": 1,
            "choices": [
                ("6.2 miles", True),
                ("16.1 miles", False),
                ("10.6 miles", False),
                ("0.62 miles", False),
            ],
            "explanation": (
                "Multiply: 10 km x 0.621 miles/km = 6.21 miles ≈ 6.2 miles.\n"
                "The trap 16.1 adds 10 + 0.621 + ... instead of multiplying.\n"
                "The trap 0.62 divides 0.621 by 10 instead of multiplying 10 by 0.621.\n"
                "Pro tip: km x (miles/km) -- the 'km' units cancel, leaving miles."
            ),
        },
        {
            "text": (
                "A swimming pool holds 15,000 gallons of water. "
                "Water is draining at 250 gallons per minute. "
                "How many hours will it take to drain the pool completely?"
            ),
            "difficulty": 2,
            "choices": [
                ("1 hour", True),
                ("60 hours", False),
                ("0.017 hours", False),
                ("6 hours", False),
            ],
            "explanation": (
                "Time to drain in minutes: 15,000 / 250 = 60 minutes.\n"
                "Convert to hours: 60 minutes / 60 = 1 hour.\n"
                "The trap '60 hours' forgets to convert minutes to hours.\n"
                "Pro tip: find the answer in the convenient unit first, "
                "then convert to the unit the question asks for."
            ),
        },
        {
            "text": (
                "A recipe requires 3 tablespoons of olive oil per serving. "
                "1 cup = 16 tablespoons. "
                "A chef wants to make 20 servings. "
                "How many cups of olive oil are needed?"
            ),
            "difficulty": 2,
            "choices": [
                ("3.75 cups", True),
                ("60 cups", False),
                ("1.25 cups", False),
                ("5.33 cups", False),
            ],
            "explanation": (
                "Total tablespoons: 3 x 20 = 60 tablespoons.\n"
                "Convert to cups: 60 / 16 = 3.75 cups.\n"
                "The trap '60 cups' forgets the conversion step.\n"
                "The trap 1.25 divides 20 by 16 without multiplying by 3.\n"
                "Pro tip: find the total in the given unit first, "
                "then apply the conversion."
            ),
        },
        {
            "text": (
                "A car's fuel efficiency is rated at 35 miles per gallon. "
                "Gas costs $3.80 per gallon. "
                "How much does the gas cost to drive 280 miles? "
                "Round to the nearest cent."
            ),
            "difficulty": 3,
            "choices": [
                ("$30.40", True),
                ("$133.00", False),
                ("$9.21", False),
                ("$38.00", False),
            ],
            "explanation": (
                "Gallons needed: 280 miles / 35 mpg = 8 gallons.\n"
                "Cost: 8 x $3.80 = $30.40.\n"
                "The trap $133 multiplies 280 by $3.80 without dividing by 35 first.\n"
                "Pro tip: dimensional analysis: "
                "280 miles x (1 gal / 35 miles) x ($3.80 / 1 gal) = $30.40."
            ),
        },
        # ── Lesson 4: Statistics ──────────────────────────────────────────────
        {
            "text": (
                "A student's scores on six tests are 72, 85, 78, 90, 88, and 91. "
                "What is the mean score?"
            ),
            "difficulty": 1,
            "choices": [
                ("84", True),
                ("88", False),
                ("86.5", False),
                ("90", False),
            ],
            "explanation": (
                "Sum: 72 + 85 + 78 + 90 + 88 + 91 = 504.\n"
                "Mean: 504 / 6 = 84.\n"
                "The trap 88 is one of the individual scores.\n"
                "The trap 86.5 is the median of the sorted list.\n"
                "Pro tip: mean = total sum divided by the count of values."
            ),
        },
        {
            "text": (
                "The seven daily high temperatures (in degrees Fahrenheit) for a city last "
                "week were: 65, 72, 68, 74, 81, 70, and 74. "
                "What is the median temperature?"
            ),
            "difficulty": 1,
            "choices": [
                ("72", True),
                ("74", False),
                ("72.0", False),
                ("71.9", False),
            ],
            "explanation": (
                "Sort: 65, 68, 70, 72, 74, 74, 81.\n"
                "There are 7 values; the middle (4th) value is 72.\n"
                "The trap 74 is the mode, not the median.\n"
                "Pro tip: always sort the data before identifying the middle value."
            ),
        },
        {
            "text": (
                "The mean of five numbers is 18. "
                "Four of the numbers are 12, 15, 22, and 25. "
                "What is the fifth number?"
            ),
            "difficulty": 2,
            "choices": [
                ("16", True),
                ("18", False),
                ("74", False),
                ("20", False),
            ],
            "explanation": (
                "Total of five numbers: 18 x 5 = 90.\n"
                "Sum of known four: 12 + 15 + 22 + 25 = 74.\n"
                "Fifth number: 90 - 74 = 16.\n"
                "The trap 74 gives the sum of the four known numbers.\n"
                "Pro tip: total = mean x count; missing value = total minus the known sum."
            ),
        },
        {
            "text": (
                "A data set has values: 10, 14, 14, 18, 22, 30. "
                "A new value of 100 is added to the data set. "
                "Which of the following best describes what happens?"
            ),
            "difficulty": 3,
            "choices": [
                ("The mean increases more than the median does.", True),
                ("The median increases more than the mean does.", False),
                ("Both the mean and median increase by the same amount.", False),
                ("Neither the mean nor the median changes.", False),
            ],
            "explanation": (
                "Original mean: (10+14+14+18+22+30)/6 = 108/6 = 18.\n"
                "New mean: (108+100)/7 = 208/7 ≈ 29.7. Mean increased by about 11.7.\n"
                "Original median: (14+18)/2 = 16. New median (7 values): 18. "
                "Median increased by only 2.\n"
                "The extreme outlier 100 pulls the mean up dramatically but barely "
                "shifts the median.\n"
                "Pro tip: outliers affect the mean far more than the median."
            ),
        },
        # ── Lesson 5: Tables and Bar Graphs ───────────────────────────────────
        {
            "text": (
                "A survey of 500 high school students asked whether they prefer "
                "reading print books or e-books. The results are shown below.\n\n"
                "| | Print | E-book | Total |\n"
                "|---|---|---|---|\n"
                "| Freshman | 90 | 60 | 150 |\n"
                "| Senior | 110 | 240 | 350 |\n"
                "| Total | 200 | 300 | 500 |\n\n"
                "What fraction of seniors prefer e-books?"
            ),
            "difficulty": 1,
            "choices": [
                ("240/350", True),
                ("240/500", False),
                ("240/300", False),
                ("110/350", False),
            ],
            "explanation": (
                "The question asks about SENIORS only, so use the senior row total (350) "
                "as the denominator: 240/350 ≈ 68.6%.\n"
                "The trap 240/500 uses the grand total, giving an overall rate, "
                "not the senior rate.\n"
                "The trap 240/300 uses the e-book column total.\n"
                "Pro tip: 'of seniors' means restrict to the senior row; "
                "use the row total as the denominator."
            ),
        },
        {
            "text": (
                "Use the same survey table:\n\n"
                "| | Print | E-book | Total |\n"
                "|---|---|---|---|\n"
                "| Freshman | 90 | 60 | 150 |\n"
                "| Senior | 110 | 240 | 350 |\n"
                "| Total | 200 | 300 | 500 |\n\n"
                "A student is selected at random from those who prefer print books. "
                "What is the probability that the student is a freshman?"
            ),
            "difficulty": 2,
            "choices": [
                ("9/20", True),
                ("9/50", False),
                ("3/5", False),
                ("11/50", False),
            ],
            "explanation": (
                "Restrict to the Print column (total = 200). "
                "Freshmen in the print column = 90.\n"
                "P = 90/200 = 9/20.\n"
                "The trap 9/50 uses 500 as the denominator.\n"
                "The trap 11/50 uses seniors (110) in the numerator.\n"
                "Pro tip: conditional probability -- 'given that they prefer print' "
                "means use 200 as the denominator."
            ),
        },
        {
            "text": (
                "A bar chart shows the number of books sold by a store in four quarters. "
                "The values are Q1: 400, Q2: 550, Q3: 700, Q4: 350. "
                "By what percent did sales increase from Q1 to Q3?"
            ),
            "difficulty": 2,
            "choices": [
                ("75%", True),
                ("43%", False),
                ("300%", False),
                ("57%", False),
            ],
            "explanation": (
                "Percent increase from Q1 to Q3: (700 - 400) / 400 x 100 = 300/400 x 100 = 75%.\n"
                "The trap 43% divides by 700 (the new value) instead of 400.\n"
                "The trap 300% uses the raw change as the percent.\n"
                "Pro tip: percent increase = change / ORIGINAL x 100."
            ),
        },
        {
            "text": (
                "In a two-way table, 180 out of 600 surveyed adults said they exercise "
                "daily, and 90 of those daily exercisers also report sleeping at least "
                "8 hours per night. What percent of daily exercisers sleep at least 8 hours?"
            ),
            "difficulty": 2,
            "choices": [
                ("50%", True),
                ("15%", False),
                ("33%", False),
                ("90%", False),
            ],
            "explanation": (
                "Restrict to daily exercisers (180). 90 of them sleep 8+ hours.\n"
                "P = 90/180 = 0.50 = 50%.\n"
                "The trap 15% divides by the total (90/600).\n"
                "The trap 33% divides by 270 instead of 180.\n"
                "Pro tip: 'of daily exercisers' means use 180 as the denominator."
            ),
        },
        # ── Lesson 6: Scatterplots and Lines of Best Fit ──────────────────────
        {
            "text": (
                "A scatterplot shows the relationship between the number of hours "
                "a student studies (x) and their score on a standardized test (y). "
                "The line of best fit is y = 5x + 50. "
                "What does the slope of 5 represent in this context?"
            ),
            "difficulty": 2,
            "choices": [
                ("Each additional hour of studying is associated with a 5-point score increase.", True),
                ("A student who studies 0 hours scores 5 points.", False),
                ("The maximum possible score is 5.", False),
                ("The test is 5 points long.", False),
            ],
            "explanation": (
                "The slope is the change in y (score) per one-unit increase in x (hours).\n"
                "Slope = 5 means each additional hour of studying predicts a 5-point "
                "increase in the test score.\n"
                "The trap 'A student who studies 0 hours scores 5 points' describes "
                "the y-intercept (50), not the slope.\n"
                "Pro tip: slope = rate of change = change in y per unit of x."
            ),
        },
        {
            "text": (
                "Using the line of best fit y = 5x + 50 from the previous context "
                "(x = hours studied, y = test score), what score does the model predict "
                "for a student who studies 12 hours?"
            ),
            "difficulty": 1,
            "choices": [
                ("110", True),
                ("62", False),
                ("60", False),
                ("610", False),
            ],
            "explanation": (
                "Substitute x = 12: y = 5(12) + 50 = 60 + 50 = 110.\n"
                "The trap 62 adds 12 + 50; the trap 60 computes only 5 x 12.\n"
                "Pro tip: substitute the given x value into the equation and "
                "compute step by step."
            ),
        },
        {
            "text": (
                "A researcher finds a strong positive correlation between ice cream "
                "sales and the number of drowning incidents across different months. "
                "Which of the following is the most appropriate conclusion?"
            ),
            "difficulty": 2,
            "choices": [
                ("Both variables are likely influenced by a third variable, such as hot weather.", True),
                ("Eating ice cream causes drowning incidents.", False),
                ("Drowning incidents cause people to buy ice cream.", False),
                ("The correlation proves ice cream sales and drowning are directly related.", False),
            ],
            "explanation": (
                "Correlation does NOT imply causation. A confounding variable (hot weather) "
                "explains both: people buy ice cream and swim more in hot months.\n"
                "The trap 'ice cream causes drowning' treats correlation as causation.\n"
                "Pro tip: when two variables correlate, always ask whether a third "
                "variable could explain both."
            ),
        },
        {
            "text": (
                "A scatterplot of advertising spending (x, in thousands of dollars) "
                "versus monthly revenue (y, in thousands of dollars) has a line of best fit "
                "with a y-intercept of 30. "
                "What is the best interpretation of this y-intercept?"
            ),
            "difficulty": 3,
            "choices": [
                ("When advertising spending is $0, the model predicts monthly revenue of $30,000.", True),
                ("The company earns $30 per dollar spent on advertising.", False),
                ("The maximum monthly revenue is $30,000.", False),
                ("Advertising spending increases revenue by $30,000 per month.", False),
            ],
            "explanation": (
                "The y-intercept is the predicted value of y when x = 0. "
                "Here x = 0 means $0 in advertising, and y = 30 (thousands) = $30,000 in revenue.\n"
                "The trap '$30 per dollar' describes the slope, not the y-intercept.\n"
                "Pro tip: the y-intercept is always the value of y when x = 0."
            ),
        },
        {
            "text": (
                "A scatterplot shows data for 10 cities: average daily temperature (x) "
                "and heating oil usage (y). As temperature increases, heating oil usage "
                "consistently decreases. This association is best described as:"
            ),
            "difficulty": 1,
            "choices": [
                ("Strong negative", True),
                ("Strong positive", False),
                ("Weak negative", False),
                ("No association", False),
            ],
            "explanation": (
                "As x (temperature) increases, y (oil usage) consistently decreases: "
                "that is a negative association. The word 'consistently' indicates the "
                "association is strong (points cluster tightly around the trend line).\n"
                "Pro tip: 'as x goes up, y goes down' = negative; "
                "'consistent' = strong."
            ),
        },
        # ── Lesson 7: Probability and Sampling ───────────────────────────────
        {
            "text": (
                "A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. "
                "A marble is drawn at random. "
                "What is the probability of drawing a blue marble?"
            ),
            "difficulty": 1,
            "choices": [
                ("3/10", True),
                ("3/5", False),
                ("1/3", False),
                ("7/10", False),
            ],
            "explanation": (
                "Total marbles: 5 + 3 + 2 = 10. Favorable outcomes (blue): 3.\n"
                "P(blue) = 3/10.\n"
                "The trap 3/5 divides by only the non-green total (8).\n"
                "The trap 7/10 is P(not blue).\n"
                "Pro tip: P(event) = favorable / total. Count ALL outcomes in the "
                "denominator, not just certain types."
            ),
        },
        {
            "text": (
                "A survey of 400 randomly selected residents of a city found that "
                "112 residents use public transportation daily. "
                "Based on this sample, which of the following best estimates the "
                "number of daily public transportation users in a city of 250,000 residents?"
            ),
            "difficulty": 2,
            "choices": [
                ("70,000", True),
                ("28,000", False),
                ("112,000", False),
                ("44,800", False),
            ],
            "explanation": (
                "Sample rate: 112 / 400 = 0.28 = 28%.\n"
                "Estimate for city: 0.28 x 250,000 = 70,000.\n"
                "The trap 28,000 multiplies 112 by 250 instead of 0.28 by 250,000.\n"
                "The trap 112,000 applies 112 as a rate per thousand.\n"
                "Pro tip: find the sample proportion, then multiply by the population."
            ),
        },
        {
            "text": (
                "A medical study randomly assigned 200 patients to receive a new drug "
                "and 200 patients to receive a placebo. Patients who received the drug "
                "showed a 30% reduction in symptoms. "
                "Which of the following conclusions is best supported?"
            ),
            "difficulty": 3,
            "choices": [
                ("The drug caused the reduction in symptoms.", True),
                ("The result shows only an association, not causation.", False),
                ("The study is biased because not all patients received the drug.", False),
                ("The result cannot be generalized to any population.", False),
            ],
            "explanation": (
                "Random assignment to drug vs. placebo allows a causal conclusion: "
                "the drug caused the improvement. This is a randomized experiment.\n"
                "The trap 'only an association' applies to observational studies, "
                "not randomized controlled experiments.\n"
                "Pro tip: random assignment is the key phrase that licenses a "
                "causal conclusion."
            ),
        },
        {
            "text": (
                "A polling organization reports that 54% of voters support a ballot "
                "measure, with a margin of error of +/-4%. "
                "Which of the following is the most accurate interpretation?"
            ),
            "difficulty": 2,
            "choices": [
                ("The true level of support is likely between 50% and 58%.", True),
                ("Exactly 54% of all voters support the measure.", False),
                ("The measure will definitely pass because support exceeds 50%.", False),
                ("The margin of error means the poll is unreliable.", False),
            ],
            "explanation": (
                "Margin of error defines an interval: 54% - 4% = 50% to 54% + 4% = 58%. "
                "The true population proportion is likely within this range.\n"
                "The trap 'exactly 54%' ignores sampling variability.\n"
                "The trap 'definitely pass' ignores that 50% is within the margin of error.\n"
                "Pro tip: margin of error creates a range, not an exact value."
            ),
        },
        {
            "text": (
                "A researcher wants to study the eating habits of college students. "
                "She surveys 100 students who are eating in the campus dining hall at noon. "
                "Why might this sample produce biased results?"
            ),
            "difficulty": 2,
            "choices": [
                ("It excludes students who do not eat in the dining hall, who may have different habits.", True),
                ("The sample size of 100 is too small to draw any conclusions.", False),
                ("Dining hall food is different from other foods, so the study is invalid.", False),
                ("The survey was conducted at noon, which is a perfectly representative time.", False),
            ],
            "explanation": (
                "Surveying only dining hall users over-represents students who eat "
                "in communal settings and excludes those who eat off-campus, cook for "
                "themselves, or skip meals -- potentially very different eating habits.\n"
                "The trap 'sample size too small' is not the primary issue here; "
                "bias in selection is the core problem.\n"
                "Pro tip: bias comes from HOW the sample is selected, not just its size."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the 'SAT Math: Problem Solving & Data Analysis' deep-dive course."

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

        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' with "
            f"{len(COURSE['lessons'])} lessons and {len(COURSE['mcqs'])} questions."
        ))
