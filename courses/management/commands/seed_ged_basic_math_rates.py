"""
Seed a dedicated GED Basic Math rates and unit rates mastery course.

Run:
    python manage.py seed_ged_basic_math_rates
"""
from django.core.management.base import BaseCommand

from courses.models import Course, Lesson
from practice.models import Choice, Question


COURSE = {
    "title": "GED Basic Math: Rates & Unit Rates Mastery",
    "slug": "ged-basic-math-rates-mastery",
    "program": "GED",
    "subject": "math",
    "description": (
        "A deep Basic Math course focused only on rates and unit rates. Students learn "
        "how to read 'per' language, find unit rates, compare unit prices, solve speed "
        "problems, use wages and work rates, interpret rate tables and graphs, and handle "
        "GED-style case studies from shopping, travel, paychecks, fuel, typing, and recipes."
    ),
    "lessons": [
        (
            "1. What a Rate Means: Two Units at Once",
            r"""
A **rate** compares two quantities with different units. The keyword is usually **per**, which means "for each 1."

Examples:
- 60 miles **per** hour
- 12 dollars **per** hour
- 25 cents **per** ounce
- 150 words **per** minute

A rate always has two jobs: the number and the units. Writing "60" is incomplete. Writing "60 miles per hour" tells what is being measured.

[[figure:rate_double_number_line|A double number line shows miles and hours growing together at a constant rate.]]

Worked example: A car travels 180 miles in 3 hours.
\[
\text{rate}=\frac{180\text{ miles}}{3\text{ hours}}=60\text{ miles per hour}.
\]

Why this matters: GED word problems often hide division inside everyday language. If you see "in," "for," "per," or "each," ask whether a rate is being described.

Case study - reading plan: A student reads 45 pages in 5 days. The reading rate is
\[
\frac{45\text{ pages}}{5\text{ days}}=9\text{ pages per day}.
\]

Common mistake: dropping the unit. "9" is not the full answer; "9 pages per day" is the meaningful answer.

[[check:A student reads 45 pages in 5 days. What is the unit rate?|9 pages per day;;9|Divide pages by days: \(45/5\).]]
            """,
        ),
        (
            "2. Unit Rates: Per 1",
            r"""
A **unit rate** is a rate with 1 in the denominator: per 1 hour, per 1 pound, per 1 page, per 1 gallon.

To find a unit rate, divide:
\[
\text{unit rate}=\frac{\text{amount}}{\text{number of units}}.
\]

Example: 24 pencils cost 6 dollars.
\[
\frac{6\text{ dollars}}{24\text{ pencils}}=0.25\text{ dollars per pencil}.
\]
Each pencil costs 25 cents.

Example: 300 miles on 10 gallons.
\[
\frac{300\text{ miles}}{10\text{ gallons}}=30\text{ miles per gallon}.
\]

Case study - online course progress: A student completes 18 lessons in 6 days. The unit rate is 3 lessons per day. At that pace, 30 lessons would take 10 days.

Two directions are possible:
- **Output per input:** miles per gallon, pages per minute, dollars per hour.
- **Input per output:** dollars per ounce, hours per lesson, gallons per mile.

Choose the direction that answers the question.

Common mistake: dividing in the wrong order. For unit price, use dollars divided by items. For speed, use distance divided by time.

[[check:A pack of 24 pencils costs 6 dollars. What is the cost per pencil?|0.25;;25 cents;;$0.25|Divide dollars by pencils: \(6/24\).]]
            """,
        ),
        (
            "3. Unit Price and Best Buy Problems",
            r"""
Unit price tells the cost for one unit. It is one of the most practical GED skills because stores often sell different sizes.

\[
\text{unit price}=\frac{\text{total price}}{\text{number of units}}.
\]

[[figure:unit_price_comparison|The lower cost per ounce is the better buy.]]

Worked example:
- Bag A: 12 ounces for 3 dollars. Unit price \(=3/12=0.25\) dollars per ounce.
- Bag B: 20 ounces for 4 dollars. Unit price \(=4/20=0.20\) dollars per ounce.

Bag B is the better buy because 20 cents per ounce is less than 25 cents per ounce.

Case study - grocery shelf: Cereal comes in 18 ounces for 4.50 dollars or 30 ounces for 6.90 dollars.
\[
4.50/18=0.25,\qquad 6.90/30=0.23.
\]
The 30-ounce box is cheaper per ounce.

When best-buy answers feel close, keep enough decimals. Rounding too early can change the decision.

Common mistake: choosing the larger package automatically. Larger packages are often cheaper per unit, but not always. Compute the unit price.

[[check:Which is cheaper per ounce: 12 oz for 3 dollars or 20 oz for 4 dollars?|20 oz for 4 dollars;;bag b;;20 oz|Compare \(3/12=0.25\) and \(4/20=0.20\).]]
            """,
        ),
        (
            "4. Speed, Distance, and Time",
            r"""
Speed is a rate: distance per time.

\[
\text{rate}=\frac{\text{distance}}{\text{time}},\qquad
\text{distance}=\text{rate}\times\text{time},\qquad
\text{time}=\frac{\text{distance}}{\text{rate}}.
\]

[[figure:rate_distance_triangle|The same three quantities can be rearranged depending on what is missing.]]

Example 1: A car travels 220 miles in 4 hours.
\[
\text{rate}=220/4=55\text{ miles per hour}.
\]

Example 2: A car travels 60 miles per hour for 3.5 hours.
\[
\text{distance}=60(3.5)=210\text{ miles}.
\]

Example 3: A bus travels 180 miles at 45 miles per hour.
\[
\text{time}=180/45=4\text{ hours}.
\]

Case study - GED test day travel: If a testing center is 24 miles away and the bus averages 30 miles per hour, travel time is
\[
24/30=0.8\text{ hour}=48\text{ minutes}.
\]

Common mistake: mixing hours and minutes. If time is in minutes and speed is miles per hour, convert minutes to hours or convert the rate to miles per minute.

[[check:A car travels 180 miles in 3 hours. What is its speed?|60 mph;;60 miles per hour;;60|Divide distance by time: \(180/3\).]]
            """,
        ),
        (
            "5. Rates With Time Conversions",
            r"""
Many rate mistakes happen because the units do not match. Before solving, check whether time is measured in seconds, minutes, hours, days, or weeks.

Useful conversions:
- 60 seconds = 1 minute
- 60 minutes = 1 hour
- 24 hours = 1 day
- 7 days = 1 week

Example: A student walks 2.5 miles in 30 minutes. Find miles per hour.

30 minutes is \(0.5\) hour, so:
\[
\frac{2.5\text{ miles}}{0.5\text{ hour}}=5\text{ miles per hour}.
\]

Example: A machine prints 180 pages in 9 minutes. Pages per minute:
\[
180/9=20\text{ pages per minute}.
\]
Pages per hour:
\[
20(60)=1200\text{ pages per hour}.
\]

Case study - typing speed: A student types 750 words in 5 minutes.
\[
750/5=150\text{ words per minute}.
\]

Common mistake: treating 30 minutes as 30 hours. In speed problems, 30 minutes is \(\frac{1}{2}\) hour.

[[check:A student walks 2.5 miles in 30 minutes. What is the speed in miles per hour?|5 mph;;5 miles per hour;;5|Convert 30 minutes to 0.5 hour, then divide \(2.5/0.5\).]]
            """,
        ),
        (
            "6. Wages, Pay, Commission, and Work Rates",
            r"""
Money rates often use dollars per hour, dollars per item, or percent commission. For hourly wages:
\[
\text{total pay}=\text{hourly rate}\times\text{hours}.
\]

Example: A worker earns 14 dollars per hour for 22 hours.
\[
14(22)=308\text{ dollars}.
\]

If total pay and hours are known, divide to find hourly rate:
\[
\frac{96\text{ dollars}}{8\text{ hours}}=12\text{ dollars per hour}.
\]

Work rate measures output per time: pages per hour, forms per day, lawns per week.

[[figure:work_rate_bars|Work rates compare output per time, not just total output.]]

Case study - two workers: Ava types 8 pages per hour. Ben types 5 pages per hour. Together, if they can work independently on different pages, their combined rate is
\[
8+5=13\text{ pages per hour}.
\]
In 3 hours, they type \(13(3)=39\) pages.

Common mistake: comparing total output without time. Typing 24 pages sounds better than 20 pages, but 24 pages in 6 hours is slower than 20 pages in 2 hours.

[[check:A worker earns 96 dollars for 8 hours. What is the hourly rate?|12 dollars per hour;;12|Divide pay by hours: \(96/8\).]]
            """,
        ),
        (
            "7. Fuel Efficiency, Consumption, and Other Everyday Rates",
            r"""
Fuel efficiency is a rate: miles per gallon.

\[
\text{miles per gallon}=\frac{\text{miles driven}}{\text{gallons used}}.
\]

Example: A car travels 240 miles using 8 gallons.
\[
240/8=30\text{ miles per gallon}.
\]

If you know miles per gallon and distance, divide to find gallons:
\[
\text{gallons}=\frac{\text{miles}}{\text{miles per gallon}}.
\]
For 300 miles at 25 miles per gallon:
\[
300/25=12\text{ gallons}.
\]

Other everyday rates:
- price per pound
- milligrams per serving
- calories per meal
- gallons per minute
- points per game

Case study - water flow: A faucet fills 18 gallons in 6 minutes. Rate:
\[
18/6=3\text{ gallons per minute}.
\]
At that rate, 10 minutes fills \(3(10)=30\) gallons.

Common mistake: confusing miles per gallon with gallons per mile. \(30\) miles per gallon means the car goes far on one gallon. \(\frac{1}{30}\) gallon per mile means fuel used for one mile.

[[check:A car travels 240 miles using 8 gallons. What is the fuel efficiency?|30 mpg;;30 miles per gallon;;30|Divide miles by gallons: \(240/8\).]]
            """,
        ),
        (
            "8. Rate Tables, Proportions, and Missing Values",
            r"""
When a rate is constant, the relationship is proportional. That means multiplying one quantity by the same factor gives the other.

Example: A car travels 60 miles each hour.

\[
\begin{array}{c|c}
\text{hours} & \text{miles}\\
1 & 60\\
2 & 120\\
3 & 180\\
4 & 240
\end{array}
\]

To find a missing value, use the unit rate or set up a proportion.

Example: 5 pounds of apples cost 8 dollars. How much do 12 pounds cost?
\[
\text{unit price}=8/5=1.60\text{ dollars per pound}.
\]
\[
12(1.60)=19.20\text{ dollars}.
\]

Proportion method:
\[
\frac{8}{5}=\frac{x}{12}.
\]
Cross multiply:
\[
5x=96,\qquad x=19.20.
\]

Case study - recipe: 3 cups of flour make 2 loaves. Cups per loaf:
\[
3/2=1.5.
\]
For 5 loaves:
\[
1.5(5)=7.5\text{ cups}.
\]

Common mistake: adding instead of multiplying. If 2 loaves need 3 cups, 5 loaves is not simply 6 cups; use cups per loaf.

[[check:If 3 cups of flour make 2 loaves, how many cups are needed for 5 loaves?|7.5;;7 1/2|Find cups per loaf: \(3/2=1.5\), then multiply by 5.]]
            """,
        ),
        (
            "9. Rates on Graphs",
            r"""
A rate can appear as the slope of a graph. On a distance-time graph, slope is speed:
\[
\text{slope}=\frac{\text{change in distance}}{\text{change in time}}.
\]

[[figure:rate_graph|The line rises 60 miles for every 1 hour, so the rate is 60 miles per hour.]]

Example: A graph passes through \((2,100)\) and \((5,250)\), where x is hours and y is miles.
\[
\text{slope}=\frac{250-100}{5-2}=\frac{150}{3}=50.
\]
The speed is 50 miles per hour.

If the graph is a straight line through the origin, the rate is constant. If the line is steeper, the rate is larger. If the line is flat, the rate is zero.

Case study - saving money: A graph shows dollars saved over weeks. If it goes from \((2,40)\) to \((6,120)\):
\[
\frac{120-40}{6-2}=\frac{80}{4}=20.
\]
The saving rate is 20 dollars per week.

Common mistake: reading only one point. A rate on a graph needs change in y divided by change in x.

[[check:A distance graph goes through \((2,100)\) and \((5,250)\). What is the rate?|50 mph;;50 miles per hour;;50|Compute slope: \((250-100)/(5-2)\).]]
            """,
        ),
        (
            "10. GED Rate Strategy: Units First, Arithmetic Second",
            r"""
Rate problems become manageable when the units lead the work.

Use this checklist:
- What two units are being compared?
- Which unit should be "per 1"?
- Should I divide, multiply, or set up a proportion?
- Do the time units match?
- Does the answer's unit make sense?

Decision map:
- **Find unit rate:** divide total by number of units.
- **Find total:** multiply unit rate by number of units.
- **Find time or quantity:** divide total by unit rate.
- **Compare choices:** compute the same unit rate for each choice.
- **Read a graph:** rate is slope, or change in y over change in x.

Error analysis: A student says 300 miles at 25 miles per gallon uses 7,500 gallons because \(300\times25=7500\). The mistake is using multiplication when the unit tells us to divide:
\[
\frac{300\text{ miles}}{25\text{ miles per gallon}}=12\text{ gallons}.
\]

Case study - test stamina: A student completes 18 practice questions in 24 minutes.
\[
18/24=0.75\text{ questions per minute}.
\]
The same rate can also be written as:
\[
24/18=1.33\text{ minutes per question}.
\]
Both are useful, depending on the question.

Final habit: write the unit before the number. If you need "dollars per pound," set up dollars divided by pounds before touching the calculator.

[[check:A student completes 18 questions in 24 minutes. About how many minutes per question is that?|1.33;;1.3;;4/3|Minutes per question means \(24/18\).]]
            """,
        ),
    ],
    "mcqs": [
        {
            "text": r"A car travels \(180\) miles in \(3\) hours. What is its speed?",
            "difficulty": 1,
            "choices": [("60 miles per hour", True), ("54 miles per hour", False), ("180 miles per hour", False), ("3 miles per hour", False)],
            "explanation": r"Speed is distance divided by time: \(180/3=60\) miles per hour.",
        },
        {
            "text": r"A student reads \(45\) pages in \(5\) days. What is the unit rate?",
            "difficulty": 1,
            "choices": [("9 pages per day", True), ("5 pages per day", False), ("40 pages per day", False), ("225 pages per day", False)],
            "explanation": r"Divide pages by days: \(45/5=9\) pages per day.",
        },
        {
            "text": r"A pack of \(24\) pencils costs \(6\) dollars. What is the cost per pencil?",
            "difficulty": 1,
            "choices": [("0.25 dollars per pencil", True), ("4 dollars per pencil", False), ("6 dollars per pencil", False), ("24 dollars per pencil", False)],
            "explanation": r"Unit price \(=6/24=0.25\) dollars per pencil.",
        },
        {
            "text": r"Which is cheaper per ounce: \(12\) oz for \(3\) dollars or \(20\) oz for \(4\) dollars?",
            "difficulty": 2,
            "choices": [("20 oz for 4 dollars", True), ("12 oz for 3 dollars", False), ("They are the same", False), ("Cannot be determined", False)],
            "explanation": r"\(3/12=0.25\) dollars per oz. \(4/20=0.20\) dollars per oz. The 20 oz option is cheaper per ounce.",
        },
        {
            "text": r"A car travels \(55\) miles per hour for \(4\) hours. How far does it travel?",
            "difficulty": 1,
            "choices": [("220 miles", True), ("59 miles", False), ("13.75 miles", False), ("180 miles", False)],
            "explanation": r"Distance \(=\text{rate}\times\text{time}=55(4)=220\) miles.",
        },
        {
            "text": r"A bus travels \(180\) miles at \(60\) miles per hour. How long does the trip take?",
            "difficulty": 1,
            "choices": [("3 hours", True), ("120 hours", False), ("240 hours", False), ("60 hours", False)],
            "explanation": r"Time \(=\text{distance}/\text{rate}=180/60=3\) hours.",
        },
        {
            "text": r"A train travels \(150\) miles in \(2.5\) hours. What is its average speed?",
            "difficulty": 2,
            "choices": [("60 miles per hour", True), ("50 miles per hour", False), ("375 miles per hour", False), ("37.5 miles per hour", False)],
            "explanation": r"Speed \(=150/2.5=60\) miles per hour.",
        },
        {
            "text": r"A student walks \(2.5\) miles in \(30\) minutes. What is the speed in miles per hour?",
            "difficulty": 2,
            "choices": [("5 miles per hour", True), ("2.5 miles per hour", False), ("30 miles per hour", False), ("75 miles per hour", False)],
            "explanation": r"30 minutes is 0.5 hour. Speed \(=2.5/0.5=5\) miles per hour.",
        },
        {
            "text": r"A machine prints \(180\) pages in \(9\) minutes. What is the rate in pages per minute?",
            "difficulty": 1,
            "choices": [("20 pages per minute", True), ("9 pages per minute", False), ("180 pages per minute", False), ("1,620 pages per minute", False)],
            "explanation": r"Pages per minute \(=180/9=20\).",
        },
        {
            "text": r"A student types \(750\) words in \(5\) minutes. What is the typing rate?",
            "difficulty": 1,
            "choices": [("150 words per minute", True), ("155 words per minute", False), ("75 words per minute", False), ("3,750 words per minute", False)],
            "explanation": r"Words per minute \(=750/5=150\).",
        },
        {
            "text": r"A car travels \(240\) miles using \(8\) gallons. What is the fuel efficiency?",
            "difficulty": 1,
            "choices": [("30 miles per gallon", True), ("32 miles per gallon", False), ("8 miles per gallon", False), ("1,920 miles per gallon", False)],
            "explanation": r"Miles per gallon \(=240/8=30\).",
        },
        {
            "text": r"A car gets \(25\) miles per gallon. How many gallons are needed for \(300\) miles?",
            "difficulty": 2,
            "choices": [("12 gallons", True), ("25 gallons", False), ("7,500 gallons", False), ("10 gallons", False)],
            "explanation": r"Gallons \(=300/25=12\).",
        },
        {
            "text": r"A worker earns \(96\) dollars for \(8\) hours. What is the hourly rate?",
            "difficulty": 1,
            "choices": [("12 dollars per hour", True), ("8 dollars per hour", False), ("96 dollars per hour", False), ("104 dollars per hour", False)],
            "explanation": r"Hourly rate \(=96/8=12\) dollars per hour.",
        },
        {
            "text": r"A worker earns \(14\) dollars per hour for \(22\) hours. What is the total pay?",
            "difficulty": 1,
            "choices": [("308 dollars", True), ("36 dollars", False), ("154 dollars", False), ("286 dollars", False)],
            "explanation": r"Total pay \(=14(22)=308\) dollars.",
        },
        {
            "text": r"A faucet fills \(18\) gallons in \(6\) minutes. What is the flow rate?",
            "difficulty": 1,
            "choices": [("3 gallons per minute", True), ("6 gallons per minute", False), ("18 gallons per minute", False), ("108 gallons per minute", False)],
            "explanation": r"Flow rate \(=18/6=3\) gallons per minute.",
        },
        {
            "text": r"A faucet flows at \(3\) gallons per minute. How many gallons flow in \(10\) minutes?",
            "difficulty": 1,
            "choices": [("30 gallons", True), ("13 gallons", False), ("3 gallons", False), ("0.3 gallon", False)],
            "explanation": r"Total gallons \(=3(10)=30\).",
        },
        {
            "text": r"Three cups of flour make \(2\) loaves. How many cups are needed for \(5\) loaves?",
            "difficulty": 2,
            "choices": [("7.5 cups", True), ("5 cups", False), ("6 cups", False), ("10 cups", False)],
            "explanation": r"Cups per loaf \(=3/2=1.5\). For 5 loaves: \(1.5(5)=7.5\) cups.",
        },
        {
            "text": r"Five pounds of apples cost \(8\) dollars. How much do \(12\) pounds cost at the same rate?",
            "difficulty": 2,
            "choices": [("19.20 dollars", True), ("17 dollars", False), ("20 dollars", False), ("96 dollars", False)],
            "explanation": r"Unit price \(=8/5=1.60\) dollars per pound. Cost for 12 pounds \(=1.60(12)=19.20\).",
        },
        {
            "text": r"A graph goes through \((2,100)\) and \((5,250)\), where x is hours and y is miles. What is the rate?",
            "difficulty": 3,
            "choices": [("50 miles per hour", True), ("30 miles per hour", False), ("150 miles per hour", False), ("350 miles per hour", False)],
            "explanation": r"Rate is slope: \((250-100)/(5-2)=150/3=50\) miles per hour.",
        },
        {
            "text": r"A savings graph goes from \((2,40)\) to \((6,120)\), where x is weeks and y is dollars. What is the saving rate?",
            "difficulty": 2,
            "choices": [("20 dollars per week", True), ("80 dollars per week", False), ("30 dollars per week", False), ("160 dollars per week", False)],
            "explanation": r"Slope \(=(120-40)/(6-2)=80/4=20\) dollars per week.",
        },
        {
            "text": r"Ava types \(8\) pages per hour and Ben types \(5\) pages per hour. If they work together on different pages, what is their combined rate?",
            "difficulty": 2,
            "choices": [("13 pages per hour", True), ("8 pages per hour", False), ("40 pages per hour", False), ("3 pages per hour", False)],
            "explanation": r"Combined independent work rate \(=8+5=13\) pages per hour.",
        },
        {
            "text": r"Ava and Ben type together at \(13\) pages per hour. How many pages can they type in \(3\) hours?",
            "difficulty": 1,
            "choices": [("39 pages", True), ("16 pages", False), ("13 pages", False), ("43 pages", False)],
            "explanation": r"Output \(=\text{rate}\times\text{time}=13(3)=39\) pages.",
        },
        {
            "text": r"A worker completes \(18\) practice questions in \(24\) minutes. About how many minutes per question is that?",
            "difficulty": 2,
            "choices": [("1.33 minutes per question", True), ("0.75 minutes per question", False), ("18 minutes per question", False), ("24 minutes per question", False)],
            "explanation": r"Minutes per question \(=24/18=1.33\) minutes per question.",
        },
        {
            "text": r"A worker completes \(18\) practice questions in \(24\) minutes. How many questions per minute is that?",
            "difficulty": 2,
            "choices": [("0.75 question per minute", True), ("1.33 questions per minute", False), ("6 questions per minute", False), ("42 questions per minute", False)],
            "explanation": r"Questions per minute \(=18/24=0.75\).",
        },
        {
            "text": r"Which expression finds dollars per pound if \(5\) pounds cost \(8\) dollars?",
            "difficulty": 1,
            "choices": [(r"\(8\div5\)", True), (r"\(5\div8\)", False), (r"\(8\times5\)", False), (r"\(8+5\)", False)],
            "explanation": r"Dollars per pound means dollars divided by pounds: \(8/5\).",
        },
        {
            "text": r"Which unit best describes speed?",
            "difficulty": 1,
            "choices": [("miles per hour", True), ("hours per dollar", False), ("dollars per pound", False), ("pages per dollar", False)],
            "explanation": r"Speed compares distance to time, such as miles per hour.",
        },
        {
            "text": r"At a constant speed of \(45\) miles per hour, how far does a car travel in \(2.5\) hours?",
            "difficulty": 2,
            "choices": [("112.5 miles", True), ("18 miles", False), ("47.5 miles", False), ("180 miles", False)],
            "explanation": r"Distance \(=45(2.5)=112.5\) miles.",
        },
        {
            "text": r"A bus travels \(24\) miles at \(30\) miles per hour. How many minutes does the trip take?",
            "difficulty": 3,
            "choices": [("48 minutes", True), ("0.8 minute", False), ("54 minutes", False), ("72 minutes", False)],
            "explanation": r"Time \(=24/30=0.8\) hour. Convert to minutes: \(0.8(60)=48\) minutes.",
        },
        {
            "text": r"A store sells \(3\) pounds of rice for \(4.50\) dollars. What is the unit price?",
            "difficulty": 1,
            "choices": [("1.50 dollars per pound", True), ("4.50 dollars per pound", False), ("13.50 dollars per pound", False), ("0.67 dollar per pound", False)],
            "explanation": r"Unit price \(=4.50/3=1.50\) dollars per pound.",
        },
        {
            "text": r"A recipe uses \(15\) grams of protein for \(3\) servings. How many grams per serving?",
            "difficulty": 1,
            "choices": [("5 grams per serving", True), ("12 grams per serving", False), ("18 grams per serving", False), ("45 grams per serving", False)],
            "explanation": r"Grams per serving \(=15/3=5\).",
        },
        {
            "text": r"A rate table shows \(1\) hour = \(60\) miles. What should \(4\) hours equal?",
            "difficulty": 1,
            "choices": [("240 miles", True), ("64 miles", False), ("15 miles", False), ("180 miles", False)],
            "explanation": r"At 60 miles per hour, \(4(60)=240\) miles.",
        },
        {
            "text": r"A student says a 300-mile trip at 25 miles per gallon needs \(7{,}500\) gallons. What mistake was made?",
            "difficulty": 2,
            "choices": [("They multiplied instead of dividing by miles per gallon.", True), ("They converted minutes to hours incorrectly.", False), ("They found dollars per pound.", False), ("They used a graph slope.", False)],
            "explanation": r"Gallons needed \(=300/25=12\). Multiplying gives an unreasonable answer.",
        },
        {
            "text": r"If a line on a distance-time graph is steeper, what does that usually mean?",
            "difficulty": 2,
            "choices": [("The speed is greater.", True), ("The speed is lower.", False), ("The time is zero.", False), ("The distance is always zero.", False)],
            "explanation": r"On a distance-time graph, slope represents speed. A steeper line has a larger slope.",
        },
    ],
    "essays": [
        {
            "text": (
                r"A car travels \(240\) miles using \(8\) gallons of gas. Find the miles per gallon. "
                r"Then use that rate to find how many gallons are needed for a \(360\)-mile trip."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: computes \(240/8=30\) miles per gallon, then \(360/30=12\) gallons. "
                "The response should include units and explain why the second step uses division."
            ),
        },
        {
            "text": (
                r"Two cereal boxes are sold: 18 ounces for \(4.50\) dollars and 30 ounces for \(6.90\) dollars. "
                r"Find each unit price and decide which is the better buy."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: \(4.50/18=0.25\) dollars per ounce and \(6.90/30=0.23\) dollars per ounce, "
                "so the 30-ounce box is the better buy. Deduct for choosing by package size only."
            ),
        },
        {
            "text": (
                r"A bus averages \(30\) miles per hour. The testing center is \(24\) miles away. "
                r"How many minutes will the trip take? Show the hour-to-minute conversion."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: computes \(24/30=0.8\) hour and converts \(0.8(60)=48\) minutes. "
                "Deduct for leaving the answer as 0.8 minutes."
            ),
        },
        {
            "text": (
                r"Ava types \(24\) pages in \(3\) hours. Ben types \(20\) pages in \(4\) hours. "
                r"Find each typing rate and explain who types faster."
            ),
            "difficulty": 2,
            "rubric": (
                r"Full credit: Ava \(24/3=8\) pages per hour, Ben \(20/4=5\) pages per hour, so Ava is faster. "
                "Explanation should compare unit rates, not only total pages."
            ),
        },
        {
            "text": (
                r"A recipe uses \(3\) cups of flour for \(2\) loaves. How many cups are needed for \(7\) loaves? "
                r"Show either a unit-rate method or a proportion."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: unit rate \(3/2=1.5\) cups per loaf, then \(1.5(7)=10.5\) cups; "
                r"or proportion \(\frac{3}{2}=\frac{x}{7}\), \(x=10.5\)."
            ),
        },
        {
            "text": (
                r"A graph of savings over time passes through \((2,40)\) and \((6,120)\). "
                r"Find the saving rate and explain what the slope means in this situation."
            ),
            "difficulty": 3,
            "rubric": (
                r"Full credit: slope \(=(120-40)/(6-2)=80/4=20\), so the saving rate is "
                r"20 dollars per week. Explanation should identify x as weeks and y as dollars."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Create the dedicated GED Basic Math rates and unit rates mastery course."

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

        # Phase 1 is MCQ-only: written-response prompts are not seeded.

        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with "
                f"{course.lessons.count()} lessons and {course.questions.count()} questions."
            )
        )
