"""
Seed a complete GED Math mastery course for data, statistics, and probability.

Run:
    python manage.py seed_ged_data_stats_probability
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
    "title": "GED Math: Data, Statistics & Probability Mastery",
    "slug": "ged-data-stats-probability",
    "program": "GED",
    "subject": "math",
    "description": (
        "A complete GED Mathematical Reasoning course for data, statistics, and probability. "
        "Students learn how to read tables and graphs, describe distributions, compute and "
        "interpret measures of center and spread, analyze scatterplots, calculate simple and "
        "compound probabilities, and write careful data-based conclusions. Lessons use an "
        "academic tone, visual displays, worked examples, common-misconception notes, and "
        "exam-style practice with step-by-step explanations."
    ),
    "lessons": [
        (
            "1. Statistical Questions and the Data Cycle",
            r"""
Statistics begins with a **question about variation**. A non-statistical question has one fixed answer: "How many lessons are in this course?" A statistical question expects different values: "How many minutes do students study each day?"

Academic data work follows a cycle:
- **Ask** a clear question.
- **Collect** relevant data from a population or a sample.
- **Organize** the data in a table, graph, or distribution.
- **Analyze** patterns, center, spread, and unusual values.
- **Conclude** with a statement supported by evidence.

A **population** is the entire group of interest. A **sample** is the smaller group actually studied. A good sample should represent the population. If a school surveys only students who already attend tutoring, the result may overstate how many students like tutoring.

Variables can be **categorical** or **quantitative**. Eye color, program choice, and phone type are categorical because they name groups. Age, score, time, distance, and cost are quantitative because they are measured with numbers.

Common misconception: any list of numbers is automatically useful. Data become useful only when the question, units, source, and method are clear.

Academic habit: before calculating, identify the question, the population, the sample, the variable, and the unit of measurement.

[[check:Is "How many siblings do students in this class have?" a statistical question?|yes|Different students can give different numerical answers.]]
            """,
        ),
        (
            "2. Tables, Units, and Two-Way Data",
            r"""
A table is often the most precise form of data display because it gives exact values. Read the **title**, then the **row labels**, **column labels**, and **units**. A number without a unit is incomplete; 18 could mean 18 students, 18 percent, 18 dollars, or 18 minutes.

[[figure:two_way_table|A two-way table classifies the same students by two categories: study-plan completion and quiz result.]]

A **two-way table** organizes two categorical variables at the same time. In the figure, one variable is whether the study plan was completed; the other is whether the quiz was passed.

Important totals:
- A **row total** summarizes one row.
- A **column total** summarizes one column.
- The **grand total** is the total number of observations.

The denominator changes the meaning of a percent. From the table, \(18/40=45\%\) means 45% of all students both completed the plan and passed. But \(18/24=75\%\) means 75% of students who completed the plan passed.

Common misconception: using the grand total for every percent. Conditional questions such as "among students who completed the plan" require the row total or column total as the denominator.

Academic habit: circle the group named after words like **of**, **among**, **given**, or **out of**. That group is usually the denominator.
            """,
        ),
        (
            "3. Bar Graphs, Circle Graphs, Line Graphs, and Scales",
            r"""
Different graphs answer different questions.

**Bar graphs** compare categories. Each bar represents a separate group, so the bars usually have spaces between them.

[[figure:bar_toppings|A bar graph compares separate topping categories.]]

**Circle graphs** show parts of one whole. The full circle represents 100%, so the slices must add to the whole.

**Line graphs** show change over time or another ordered variable. A rising line indicates an increase; a falling line indicates a decrease.

[[figure:line_sales|A line graph is useful when the order of the x-values matters, such as months.]]

Graph scales deserve careful attention. A graph can visually exaggerate a small difference if the vertical axis does not begin at 0 or if grid lines represent large intervals.

[[figure:misleading_scale|The axis starts at 90, so a 3-point difference looks much larger than it is.]]

Common misconception: judging a graph only by visual height. Academic interpretation requires reading the actual scale and labels.

Academic habit: before answering any graph question, read the title, axes, units, interval size, and whether the axis starts at 0.
            """,
        ),
        (
            "4. Frequency Tables and Dot Plots",
            r"""
A **frequency** is a count. A frequency table tells how many times each value or category occurs. A dot plot shows the same idea visually: each dot represents one observation.

[[figure:dot_plot_scores|A dot plot keeps individual values visible, so repeated values and clusters are easy to see.]]

The dot plot in the figure shows ten quiz scores:
\[
70,\ 75,\ 75,\ 80,\ 80,\ 80,\ 85,\ 90,\ 90,\ 95.
\]
The score 80 appears most often, so it is the mode. The values cluster mostly between 75 and 90.

Dot plots are especially useful for small to medium data sets because the original values are still visible. You can often find the median by counting inward from both ends.

Frequency tables are more compact. For example, the same data could be listed as: 70 occurs 1 time, 75 occurs 2 times, 80 occurs 3 times, 85 occurs 1 time, 90 occurs 2 times, and 95 occurs 1 time.

Common misconception: counting each distinct value once. In statistics, repeated values matter. Three dots at 80 mean three students scored 80.

Academic habit: when values repeat, use frequency to avoid rewriting long lists while preserving the total count.
            """,
        ),
        (
            "5. Histograms and Distribution Shape",
            r"""
A **histogram** groups quantitative data into intervals called **bins**. Unlike bar graphs, histogram bars touch because the intervals are continuous ranges.

[[figure:histogram_commute|A histogram groups commute times into intervals such as 10-19 minutes and 20-29 minutes.]]

Histograms help describe the **shape** of a distribution:
- **Symmetric:** values spread about evenly on both sides of the center.
- **Skewed right:** most values are low or moderate, with a long tail to the right.
- **Skewed left:** most values are high or moderate, with a long tail to the left.
- **Cluster:** many values appear in one region.
- **Gap:** an interval has few or no values.

In the commute-time histogram, the largest bin is 20-29 minutes. Most commutes are under 30 minutes, but a few longer commutes create a right-side tail.

Common misconception: treating histogram bins as single exact values. The bin 20-29 minutes means every value from 20 through 29 minutes, not exactly 20.

Academic habit: describe a distribution with **center**, **spread**, **shape**, and **unusual values** rather than one number alone.
            """,
        ),
        (
            "6. Mean, Median, Mode, and Range",
            r"""
Statistics summarizes a data set without listing every value.

**Mean** is the arithmetic average:
\[
\text{mean}=\frac{\text{sum of values}}{\text{number of values}}.
\]
For \(4,8,6,2\), the mean is \((4+8+6+2)/4=20/4=5\).

[[figure:mean_bars|The mean acts like a balance point for the data.]]

**Median** is the middle value after ordering the data. If there are two middle values, average them.

**Mode** is the value that appears most often. A data set may have one mode, more than one mode, or no mode.

**Range** is the maximum minus the minimum. It gives a quick measure of spread, but it uses only the two extreme values.

Mean and median answer different questions. The mean uses every value, so it is sensitive to outliers. The median uses position, so it is more resistant to one extremely high or low value.

Common misconception: finding the median before ordering the data. The median is the middle of the **ordered** list, not the middle of the list as written.

Academic habit: report the measure and the context: "The mean score is 82 points," not just "82."
            """,
        ),
        (
            "7. Weighted Averages and Missing Values",
            r"""
A regular mean treats every value equally. A **weighted average** gives some values more influence because they count more often or carry more weight.

The weighted-average formula is:
\[
\text{weighted mean}=\frac{\text{sum of value times weight}}{\text{sum of weights}}.
\]

Example: A course grade uses tests with weight 3 and a project with weight 1. If the test average is 80 and the project score is 90, then:
\[
\frac{3(80)+1(90)}{3+1}=\frac{330}{4}=82.5.
\]
The result is closer to 80 because the test category has more weight.

Frequency tables are weighted averages in disguise. If two students score 70, three students score 80, and one student scores 90, the mean is:
\[
\frac{2(70)+3(80)+1(90)}{2+3+1}=\frac{470}{6}\approx78.3.
\]

Missing-value problems use the target total. If five scores have mean 82, their sum must be \(5(82)=410\). Subtract the known scores to find the missing value.

Common misconception: averaging percentages or scores without checking weights. A 90 on a small assignment may not offset an 80 on a heavily weighted test.

Academic habit: write the numerator as value times weight before dividing.
            """,
        ),
        (
            "8. Spread, Quartiles, IQR, and Box Plots",
            r"""
Measures of center tell what is typical. Measures of **spread** tell how far apart the data values are.

The **five-number summary** is:
- minimum
- first quartile, \(Q1\)
- median
- third quartile, \(Q3\)
- maximum

[[figure:box_plot|A box plot shows the five-number summary and makes spread visible.]]

The **interquartile range** is:
\[
IQR=Q3-Q1.
\]
The IQR measures the spread of the middle half of the data. It is useful because it is less affected by outliers than the full range.

Example: for \(2,4,6,8,10,12,14\), the median is 8. The lower half is \(2,4,6\), so \(Q1=4\). The upper half is \(10,12,14\), so \(Q3=12\). Therefore \(IQR=12-4=8\).

An **outlier** is a value unusually far from the rest. GED-style questions often ask how an outlier affects the mean, median, or range.

Common misconception: reading the width of the box as the total range. The box is the IQR; the whiskers extend toward the minimum and maximum.

Academic habit: use resistant measures, such as median and IQR, when the data include outliers.
            """,
        ),
        (
            "9. Scatterplots, Association, and Lines of Best Fit",
            r"""
A **scatterplot** displays paired quantitative data. Each point represents two values for the same observation, such as study hours and quiz score.

[[figure:scatter_trend|The upward trend shows a positive association between x and y.]]

Association describes how two variables move together:
- **Positive association:** as \(x\) increases, \(y\) tends to increase.
- **Negative association:** as \(x\) increases, \(y\) tends to decrease.
- **No clear association:** the points show no consistent direction.

A **line of best fit** summarizes the trend. It can be used to make approximate predictions, especially within the range of the data. Predicting inside the observed range is called interpolation. Predicting far outside the observed range is extrapolation and is less reliable.

Correlation does not prove causation. If students who study more tend to score higher, the scatterplot shows association. To prove cause, the study design would need much stronger evidence.

Common misconception: every upward trend proves one variable caused the other. A scatterplot alone can show a relationship, but it cannot prove cause.

Academic habit: write cautious conclusions: "The data suggest a positive association," not "x definitely causes y."
            """,
        ),
        (
            "10. Probability Models, Complements, and Expected Frequency",
            r"""
Probability measures how likely an event is. It always falls between 0 and 1:
\[
0 \le P(\text{event}) \le 1.
\]

[[figure:prob_scale|A probability of 0 is impossible, 1 is certain, and 1/2 is an even chance.]]

When outcomes are equally likely:
\[
P(\text{event})=\frac{\text{favorable outcomes}}{\text{total outcomes}}.
\]
Rolling an even number on a fair die has three favorable outcomes, \(2,4,6\), out of six possible outcomes, so \(P=3/6=1/2\).

The **complement** is the event not happening:
\[
P(\text{not A})=1-P(A).
\]
If the chance of rain is 70%, the chance of no rain is 30%.

Probability can be used for expected frequency. If an event has probability 0.20 and the experiment is repeated 50 times, the expected number of successes is \(0.20(50)=10\). This is not a guarantee; it is a long-run expectation.

Common misconception: a probability predicts the exact next result. Probability describes long-run patterns, not certainty for a single trial.

Academic habit: convert fractions, decimals, and percents carefully; \(\frac{1}{4}=0.25=25\%\).
            """,
        ),
        (
            "11. Compound Probability, Tables, and Counting",
            r"""
Compound probability involves more than one event.

For independent events, one event does not change the probability of the other. Flipping two fair coins is independent:
\[
P(H\text{ and }H)=\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}.
\]

[[figure:coin_tree|A tree diagram lists all outcomes of two coin flips.]]

For dependent events, the first event changes the second probability. If a bag has 3 red and 2 blue marbles, the probability of drawing two red marbles without replacement is:
\[
\frac{3}{5}\cdot\frac{2}{4}=\frac{6}{20}=\frac{3}{10}.
\]
The second denominator is 4 because one marble has already been removed.

For "A or B" questions, add probabilities only when the outcomes cannot happen at the same time. Rolling a 1 or 2 on one die gives \(1/6+1/6=2/6=1/3\).

The **counting principle** says that if one choice has \(m\) options and another has \(n\) options, the total number of ordered combinations is \(mn\).

Common misconception: multiplying for every compound problem. "And" often suggests multiplication; "or" often suggests addition, but the event structure must be checked.

Academic habit: decide whether events are independent or dependent before calculating.
            """,
        ),
        (
            "12. Integrated GED Data Analysis and Academic Conclusions",
            r"""
GED data questions often combine several skills: reading a graph, choosing a denominator, computing a statistic, and interpreting the result in context.

A strong academic response has three parts:
- **Evidence:** quote the relevant number, graph feature, or table entry.
- **Computation:** show the formula or arithmetic.
- **Interpretation:** explain what the answer means in the situation.

Example: In a class of 40 students, 18 completed the study plan and passed the quiz. The statement "45% of all students completed the plan and passed" is supported because \(18/40=0.45=45\%\). The statement "75% of plan completers passed" is also supported because \(18/24=0.75=75\%\). Both statements are true, but they answer different questions.

When evaluating a claim, ask:
- What group is being described?
- Which denominator matches that group?
- Is the statistic affected by an outlier?
- Does the graph scale exaggerate the difference?
- Is the conclusion about association or causation?

Common misconception: assuming one correct number answers every interpretation question. Data analysis depends on the question being asked.

Academic habit: end with a precise sentence: "Among students who completed the plan, 75% passed, so the data suggest a positive association between plan completion and passing."
            """,
        ),
    ],
    "mcqs": [
        item(
            "Which question is statistical?",
            "How many minutes do students in this class study each night?",
            ["What is 8 plus 7?", "How many sides does a triangle have?", "What is the formula for area of a rectangle?"],
            ["A statistical question expects variation in the answers.", "Different students may study different numbers of minutes.", "Therefore the study-time question is statistical."],
            "choosing a question just because it contains a number; the key is whether the answers vary.",
            1,
        ),
        item(
            "A researcher wants to know the average commute time of all adult learners in a city, but surveys 200 learners. What is the 200-learner group called?",
            "A sample",
            ["A population", "A variable", "A histogram"],
            ["The population is the entire group of interest: all adult learners in the city.", "The 200 surveyed learners are the smaller group actually measured.", "A measured subgroup is a sample."],
            "calling the sample the population because it is the group actually seen.",
            1,
        ),
        item(
            "Which variable is categorical?",
            "Preferred study location",
            ["Minutes studied", "Quiz score", "Distance traveled"],
            ["Categorical variables name groups or labels.", "Preferred study location might be library, home, school, or cafe.", "The other choices are numerical measurements."],
            "assuming every survey answer is numerical; categories are data too.",
            1,
        ),
        item(
            "A school asks only students in an advanced math club whether math tutoring is helpful. What is the main concern?",
            "The sample may be biased.",
            ["The population is too small to define.", "The data must be quantitative.", "The survey has no variable."],
            ["The goal is likely to learn about students more broadly.", "Advanced math club students may not represent all students.", "A non-representative sample can create bias."],
            "thinking a larger-sounding group is automatically fair; representation matters more than convenience.",
            2,
        ),
        item(
            "Use the two-way table.\n\n[[figure:two_way_table|Study plan completion and quiz result]]\n\nHow many students passed the quiz?",
            r"\(25\)",
            [r"\(18\)", r"\(40\)", r"\(24\)"],
            ["Look at the Passed column.", "The column total at the bottom is 25.", "That total includes students who did and did not complete the plan."],
            "using only the 18 students who both completed the plan and passed.",
            1,
        ),
        item(
            "Use the two-way table.\n\n[[figure:two_way_table|Study plan completion and quiz result]]\n\nAmong students who completed the plan, what fraction passed?",
            r"\(\frac{18}{24}=\frac{3}{4}\)",
            [r"\(\frac{18}{40}\)", r"\(\frac{24}{40}\)", r"\(\frac{25}{40}\)"],
            ["The phrase 'among students who completed the plan' names the row group.", "That row total is 24.", "Of those 24 students, 18 passed, so the fraction is \(18/24=3/4\)."],
            "using the grand total 40 even though the question restricts the group to plan completers.",
            2,
        ),
        item(
            "Use the two-way table.\n\n[[figure:two_way_table|Study plan completion and quiz result]]\n\nWhat percent of all students both completed the plan and passed?",
            r"\(45\%\)",
            [r"\(75\%\)", r"\(60\%\)", r"\(25\%\)"],
            ["The question says 'all students,' so use the grand total 40.", "The count that both completed and passed is 18.", "\(18/40=0.45=45\%\)."],
            "using \(18/24=75\%\), which answers a different conditional question.",
            2,
        ),
        item(
            "A table shows 12 students prefer online study, 8 prefer in-person study, and 5 prefer hybrid study. How many students are represented?",
            r"\(25\)",
            [r"\(20\)", r"\(12\)", r"\(30\)"],
            ["The categories are parts of one group.", "Add the frequencies: \(12+8+5=25\).", "The table represents 25 students."],
            "choosing the largest category instead of adding all categories.",
            1,
        ),
        item(
            "Use the bar graph.\n\n[[figure:bar_toppings|Pizza toppings chosen by 20 students]]\n\nHow many more students chose cheese than veggie?",
            r"\(4\)",
            [r"\(12\)", r"\(8\)", r"\(2\)"],
            ["Read the cheese bar as 8.", "Read the veggie bar as 4.", "'How many more' means subtract: \(8-4=4\)."],
            "adding the two bars instead of finding the difference.",
            1,
        ),
        item(
            "Use the line graph.\n\n[[figure:line_sales|Monthly sales]]\n\nWhat general trend does the graph show from January to May?",
            "Sales generally increase.",
            ["Sales generally decrease.", "Sales stay exactly the same.", "Sales are impossible to compare."],
            ["A line graph shows change over time.", "The points are mostly higher as the months move from January to May.", "Therefore the general trend is increasing."],
            "expecting every month to rise; a general trend can still include a small dip.",
            1,
        ),
        item(
            "Use the truncated-scale graph.\n\n[[figure:misleading_scale|Class averages with an axis beginning at 90]]\n\nWhich statement is most accurate?",
            "Class B is 3 points higher, but the graph makes the difference look large.",
            ["Class B is twice as high as Class A.", "Class A and Class B are equal.", "The graph proves Class B studied twice as much."],
            ["Read the labels: Class A is 96 and Class B is 99.", "The difference is \(99-96=3\) points.", "Because the axis starts at 90, the visual difference is exaggerated."],
            "judging only by bar height without reading the y-axis scale.",
            2,
        ),
        item(
            "A circle graph shows 40% rent, 25% food, 15% transportation, 10% savings, and 10% other. What should the slices add to?",
            r"\(100\%\)",
            [r"\(50\%\)", r"\(40\%\)", r"\(200\%\)"],
            ["A circle graph represents one whole.", "One whole equals 100%.", "The listed slices should add to 100%."],
            "adding only the largest slices or forgetting that the entire circle is the whole.",
            1,
        ),
        item(
            "Use the dot plot.\n\n[[figure:dot_plot_scores|Quiz scores dot plot]]\n\nWhich score is the mode?",
            r"\(80\)",
            [r"\(75\)", r"\(90\)", r"\(95\)"],
            ["The mode is the value that appears most often.", "The dot plot has three dots above 80.", "No other value appears three times."],
            "choosing the highest score instead of the most frequent score.",
            1,
        ),
        item(
            "Use the dot plot.\n\n[[figure:dot_plot_scores|Quiz scores dot plot]]\n\nHow many students are represented?",
            r"\(10\)",
            [r"\(6\)", r"\(80\)", r"\(95\)"],
            ["Each dot represents one student.", "Count all dots across the plot.", "There are 10 dots, so 10 students are represented."],
            "counting only the number of distinct score values.",
            1,
        ),
        item(
            "Use the dot plot.\n\n[[figure:dot_plot_scores|Quiz scores dot plot]]\n\nWhat is the median score?",
            r"\(80\)",
            [r"\(85\)", r"\(82.5\)", r"\(90\)"],
            ["The ordered scores are \(70,75,75,80,80,80,85,90,90,95\).", "There are 10 values, so average the 5th and 6th values.", "Both middle values are 80, so the median is 80."],
            "averaging 80 and 85 because those are near the visual center, not the exact middle positions.",
            2,
        ),
        item(
            "A frequency table shows: score 70 occurs 1 time, score 80 occurs 3 times, and score 90 occurs 2 times. How many scores are in the data set?",
            r"\(6\)",
            [r"\(3\)", r"\(240\)", r"\(80\)"],
            ["The total count is the sum of frequencies.", "Add \(1+3+2=6\).", "The data set contains 6 scores."],
            "adding the score values instead of the frequencies.",
            1,
        ),
        item(
            "Use the histogram.\n\n[[figure:histogram_commute|Commute time histogram]]\n\nWhich interval has the greatest frequency?",
            "20-29 minutes",
            ["0-9 minutes", "10-19 minutes", "40-49 minutes"],
            ["In a histogram, taller bars have greater frequency.", "The tallest bar is over 20-29 minutes.", "Therefore 20-29 minutes has the greatest frequency."],
            "choosing the largest time interval because its numbers are biggest, not because its bar is tallest.",
            1,
        ),
        item(
            "Use the histogram.\n\n[[figure:histogram_commute|Commute time histogram]]\n\nHow many commutes are at least 30 minutes?",
            r"\(7\)",
            [r"\(5\)", r"\(2\)", r"\(14\)"],
            ["At least 30 minutes includes the 30-39 and 40-49 bins.", "The frequencies are 5 and 2.", "Add \(5+2=7\)."],
            "using only the 30-39 bin and forgetting the 40-49 bin.",
            2,
        ),
        item(
            "Why do bars touch in a histogram?",
            "The bars represent continuous numerical intervals.",
            ["The bars represent unrelated categories.", "The graph must always start at 90.", "The values are all percentages."],
            ["A histogram groups quantitative data into intervals.", "Adjacent intervals connect along a number line.", "Bars touch to show continuous ranges."],
            "confusing histograms with bar graphs; bar graph categories usually have spaces.",
            1,
        ),
        item(
            "A histogram has most values low and a few very high values. What shape is this?",
            "Skewed right",
            ["Skewed left", "Perfectly symmetric", "No distribution"],
            ["A few very high values create a tail on the high-value side.", "High values are on the right side of the number line.", "Therefore the distribution is skewed right."],
            "naming the side where most values sit instead of the side where the tail extends.",
            2,
        ),
        item(
            r"Find the mean of \(4,\ 8,\ 6,\ 2\).",
            r"\(5\)",
            [r"\(6\)", r"\(20\)", r"\(4\)"],
            ["Add the values: \(4+8+6+2=20\).", "There are 4 values.", "Divide: \(20/4=5\)."],
            "stopping at the sum instead of dividing by the number of values.",
            1,
        ),
        item(
            r"Find the median of \(3,\ 9,\ 1,\ 7,\ 5\).",
            r"\(5\)",
            [r"\(7\)", r"\(1\)", r"\(9\)"],
            ["Order the values: \(1,3,5,7,9\).", "There are 5 values, so the 3rd value is the middle.", "The median is 5."],
            "using the middle number as written without ordering first.",
            1,
        ),
        item(
            r"What is the range of \(12,\ 4,\ 20,\ 8\)?",
            r"\(16\)",
            [r"\(20\)", r"\(8\)", r"\(11\)"],
            ["Identify the maximum: 20.", "Identify the minimum: 4.", "Subtract: \(20-4=16\)."],
            "choosing the maximum value instead of maximum minus minimum.",
            1,
        ),
        item(
            r"Which measure is usually affected most by one extremely high outlier?",
            "Mean",
            ["Median", "Mode", "Sample size"],
            ["The mean uses every value in the data set.", "An extremely high value increases the total strongly.", "Therefore the mean is usually affected most."],
            "thinking the median moves as much as the mean; the median depends on position.",
            2,
        ),
        item(
            r"Four scores are \(78,\ 84,\ 90,\ 80\). A fifth score is missing. If the mean of all five scores is \(82\), what is the missing score?",
            r"\(78\)",
            [r"\(82\)", r"\(88\)", r"\(410\)"],
            ["A mean of 82 for 5 scores means the total must be \(5(82)=410\).", "The known scores sum to \(78+84+90+80=332\).", "The missing score is \(410-332=78\)."],
            "using 82 as the missing value without checking the total.",
            3,
        ),
        item(
            r"A test average of \(80\) has weight 3 and a project score of \(90\) has weight 1. What is the weighted average?",
            r"\(82.5\)",
            [r"\(85\)", r"\(170\)", r"\(80\)"],
            ["Multiply each value by its weight: \(3(80)+1(90)=330\).", "Add the weights: \(3+1=4\).", "Divide: \(330/4=82.5\)."],
            "averaging 80 and 90 equally even though the test category has more weight.",
            3,
        ),
        item(
            r"A frequency table shows 70 for 2 students, 80 for 3 students, and 90 for 1 student. What is the mean?",
            r"\(\frac{470}{6}\approx78.3\)",
            [r"\(80\)", r"\(240\)", r"\(\frac{240}{3}=80\)"],
            ["Use value times frequency: \(2(70)+3(80)+1(90)=470\).", "The total number of students is \(2+3+1=6\).", "The mean is \(470/6\approx78.3\)."],
            "averaging the distinct score values and ignoring that 80 occurs three times.",
            3,
        ),
        item(
            r"For \(2,\ 4,\ 6,\ 8,\ 10,\ 12,\ 14\), what is the interquartile range?",
            r"\(8\)",
            [r"\(12\)", r"\(4\)", r"\(14\)"],
            ["The median is 8, so use the lower half \(2,4,6\) and upper half \(10,12,14\).", "The first quartile is \(Q1=4\), and the third quartile is \(Q3=12\).", "The IQR is \(12-4=8\)."],
            "subtracting the minimum from the maximum, which gives the range, not the IQR.",
            3,
        ),
        item(
            "Use the box plot.\n\n[[figure:box_plot|Box plot anatomy]]\n\nWhat does the line inside the box represent?",
            "The median",
            ["The mean", "The maximum", "The range"],
            ["A box plot displays the five-number summary.", "The line inside the box marks the median.", "The box edges mark Q1 and Q3."],
            "assuming the center line is the mean; standard box plots show the median.",
            1,
        ),
        item(
            r"If \(Q1=22\) and \(Q3=38\), what is the IQR?",
            r"\(16\)",
            [r"\(60\)", r"\(30\)", r"\(8\)"],
            ["The IQR is \(Q3-Q1\).", "Substitute: \(38-22\).", "The IQR is 16."],
            "adding the quartiles instead of subtracting.",
            2,
        ),
        item(
            r"A data set is \(4,\ 5,\ 6,\ 7,\ 30\). Which measure better describes the typical value if the outlier matters?",
            "Median",
            ["Mean", "Maximum", "Range"],
            ["The value 30 is far from the others.", "The mean is pulled upward by 30.", "The median is resistant and better represents the central cluster."],
            "choosing mean automatically because it is common; outliers can make the mean misleading.",
            2,
        ),
        item(
            "Use the scatterplot.\n\n[[figure:scatter_trend|Scatterplot with a positive trend]]\n\nWhat association is shown?",
            "Positive association",
            ["Negative association", "No association", "A guaranteed cause"],
            ["The points generally rise from left to right.", "As x increases, y tends to increase.", "That pattern is a positive association."],
            "claiming causation from a scatterplot; association alone does not prove cause.",
            1,
        ),
        item(
            "A scatterplot shows that students who sleep more tend to have higher quiz scores. What conclusion is safest?",
            "There is a positive association between sleep and quiz score.",
            ["Sleep definitely causes every student to score higher.", "Quiz score causes sleep.", "There is no relationship because the data are paired."],
            ["The phrase 'tend to' describes an association.", "Higher sleep values go with higher quiz scores.", "A scatterplot alone does not prove causation."],
            "turning association into a definite cause-and-effect claim.",
            2,
        ),
        item(
            r"A line of best fit is \(y=3x+10\). What is the predicted \(y\)-value when \(x=5\)?",
            r"\(25\)",
            [r"\(18\)", r"\(15\)", r"\(50\)"],
            ["Substitute \(x=5\) into the equation.", "Compute \(3(5)+10=15+10\).", "The predicted value is 25."],
            "multiplying 3 and 10 before substituting x.",
            2,
        ),
        item(
            "A data set uses x-values from 0 to 10. Predicting at x = 6 from a trend line is called:",
            "Interpolation",
            ["Extrapolation", "A two-way table", "A frequency count"],
            ["The prediction uses an x-value inside the observed range.", "Predicting inside the data range is interpolation.", "Predicting beyond the range would be extrapolation."],
            "thinking every prediction from a line is extrapolation.",
            2,
        ),
        item(
            r"A fair six-sided die is rolled. What is the probability of rolling an even number?",
            r"\(\frac{1}{2}\)",
            [r"\(\frac{1}{6}\)", r"\(\frac{1}{3}\)", r"\(\frac{2}{3}\)"],
            ["Even outcomes are 2, 4, and 6.", "There are 3 favorable outcomes out of 6 total outcomes.", "The probability is \(3/6=1/2\)."],
            "counting only one even number instead of all even outcomes.",
            1,
        ),
        item(
            r"The probability of rain is \(70\%\). What is the probability it does not rain?",
            r"\(30\%\)",
            [r"\(70\%\)", r"\(0\%\)", r"\(100\%\)"],
            ["The event 'does not rain' is the complement of rain.", "Complements add to 100%.", "\(100\%-70\%=30\%\)."],
            "forgetting that the complement is what remains out of the whole.",
            1,
        ),
        item(
            r"If the probability of passing a quiz is \(0.20\), about how many passes are expected in \(50\) attempts?",
            r"\(10\)",
            [r"\(5\)", r"\(20\)", r"\(40\)"],
            ["Expected frequency equals probability times number of trials.", "Compute \(0.20(50)=10\).", "About 10 passes are expected."],
            "treating 0.20 as 20 attempts instead of 20 percent of the attempts.",
            2,
        ),
        item(
            r"In 40 trials, an event happened 12 times. What is the relative frequency?",
            r"\(0.30\)",
            [r"\(0.12\)", r"\(3.33\)", r"\(28\)"],
            ["Relative frequency is successes divided by total trials.", "Compute \(12/40=0.30\).", "As a percent, that is 30%."],
            "subtracting from 40 instead of forming the ratio.",
            2,
        ),
        item(
            r"You flip a fair coin twice. What is the probability of heads both times?",
            r"\(\frac{1}{4}\)",
            [r"\(\frac{1}{2}\)", r"\(\frac{2}{1}\)", r"\(1\)"],
            ["Each flip has probability \(1/2\) for heads.", "The flips are independent, so multiply.", "\(1/2\cdot1/2=1/4\)."],
            "adding \(1/2+1/2\) for an 'and' situation.",
            2,
        ),
        item(
            r"A fair die is rolled once. What is the probability of rolling a 1 or a 2?",
            r"\(\frac{1}{3}\)",
            [r"\(\frac{1}{6}\)", r"\(\frac{1}{2}\)", r"\(\frac{2}{12}\)"],
            ["The favorable outcomes are 1 and 2.", "That is 2 outcomes out of 6.", "\(2/6=1/3\)."],
            "leaving the answer unsimplified in a form not offered or counting only one outcome.",
            1,
        ),
        item(
            r"A bag has 3 red and 2 blue marbles. Two marbles are drawn without replacement. What is the probability both are red?",
            r"\(\frac{3}{10}\)",
            [r"\(\frac{9}{25}\)", r"\(\frac{6}{25}\)", r"\(\frac{2}{5}\)"],
            ["The first red probability is \(3/5\).", "Without replacement, one red is removed, so the second red probability is \(2/4\).", "Multiply: \(3/5\cdot2/4=6/20=3/10\)."],
            "using \(3/5\) for both draws even though the first draw changes the bag.",
            3,
        ),
        item(
            r"A student can choose 4 shirts and 3 pairs of pants. How many outfits are possible?",
            r"\(12\)",
            [r"\(7\)", r"\(1\)", r"\(24\)"],
            ["There are 4 choices for the shirt.", "For each shirt, there are 3 choices for pants.", "Use the counting principle: \(4\cdot3=12\)."],
            "adding choices instead of multiplying independent choices.",
            1,
        ),
        item(
            r"How many ways can 2 students be chosen from a group of 5 if order does not matter?",
            r"\(10\)",
            [r"\(20\)", r"\(25\)", r"\(5\)"],
            ["There are \(5\cdot4=20\) ordered ways to pick first and second.", "Each pair is counted twice, such as AB and BA.", "Divide by 2: \(20/2=10\)."],
            "counting AB and BA as different even though order does not matter.",
            3,
        ),
        item(
            "Use the two-way table.\n\n[[figure:two_way_table|Study plan completion and quiz result]]\n\nWhat is the probability a randomly chosen student passed, given that the student completed the plan?",
            r"\(\frac{3}{4}\)",
            [r"\(\frac{18}{40}\)", r"\(\frac{25}{40}\)", r"\(\frac{6}{24}\)"],
            ["The phrase 'given that the student completed the plan' restricts the denominator to 24 plan completers.", "Among those 24, 18 passed.", "\(18/24=3/4\)."],
            "using all 40 students as the denominator for a conditional probability.",
            3,
        ),
        item(
            "A claim says, 'Most plan completers passed.' Which table value is the best denominator to test the claim?",
            "The total number of plan completers",
            ["The grand total", "The total number who failed", "The total number who did not complete the plan"],
            ["The claim is only about plan completers.", "The denominator should match the group being described.", "Therefore use the total number of plan completers."],
            "using the grand total when the claim describes a subgroup.",
            2,
        ),
        item(
            r"A report says the mean income is high, but the median income is much lower. What is the best explanation?",
            "A few very high incomes may be pulling the mean upward.",
            ["The data set must have no outliers.", "The median is always higher than the mean.", "The range must be zero."],
            ["The mean is sensitive to extreme values.", "Very high values increase the total used in the mean.", "The median can remain lower because it depends on position."],
            "assuming mean and median must always be close.",
            2,
        ),
        item(
            r"Which statement is written in the strongest academic style?",
            "The data suggest a positive association between study time and score.",
            ["Study time definitely causes all score increases.", "The graph says studying is always good.", "Scores went up because I can see dots."],
            ["Academic conclusions should be precise and cautious.", "A scatterplot can support association.", "It should not claim definite causation without stronger evidence."],
            "overstating what the data can prove.",
            2,
        ),
        item(
            r"A class has scores \(60,\ 70,\ 80,\ 90,\ 100\). If each score increases by 5 points, what happens to the mean?",
            "It increases by 5 points.",
            ["It stays the same.", "It doubles.", "It decreases by 5 points."],
            ["Adding 5 to every value increases the total by \(5\) times the number of values.", "When that total is divided by the same number of values, the mean rises by 5.", "The new mean is the old mean plus 5."],
            "thinking the spread change is needed; shifting every value shifts the mean by the same amount.",
            3,
        ),
        item(
            "Which display is usually best for comparing separate categories such as favorite study app?",
            "Bar graph",
            ["Histogram", "Box plot", "Scatterplot"],
            ["Favorite study app is categorical data.", "Bar graphs compare counts or percents across categories.", "Therefore a bar graph is the best display."],
            "using a histogram for categories; histograms are for numerical intervals.",
            1,
        ),
    ],
}


class Command(BaseCommand):
    help = "Create the GED Math Data, Statistics & Probability Mastery course (MCQ only)."

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
