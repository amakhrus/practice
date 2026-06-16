"""
Seed data: 'GED Social Studies: Economics' -- a focused deep dive into the
economics content area of the GED Social Studies test.

Covers all seven key topics: basic economic concepts (scarcity, opportunity
cost, factors of production), supply and demand, market structures, personal
finance, the role of government in the economy, macroeconomics, and reading
economic data and graphs. Lessons use intuition and real-world hooks, include
diagrams where available, misconception warnings, and tips. Practice mirrors
GED style with full explanations.

Run:
    python manage.py seed_ged_economics
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Economics",
    "slug": "ged-economics",
    "program": "GED",
    "subject": "social",
    "description": (
        "Economics is one of the four content areas on the GED Social Studies test. This course "
        "covers everything you need: scarcity and opportunity cost, how supply and demand set "
        "prices, market structures from competition to monopoly, personal finance skills like "
        "budgeting and credit, the government's role in the economy, macroeconomic indicators "
        "like GDP and inflation, and how to read economic graphs and data. Every lesson uses "
        "real-world examples, key-term definitions, misconception warnings, and tips."
    ),
    "lessons": [
        (
            "1. Basic Economic Concepts",
            "Economics begins with one unavoidable reality: resources are **scarce**, but human "
            "wants are unlimited. **Scarcity** means there is never enough of everything for "
            "everyone, so individuals, businesses, and governments must make **choices**.\n\n"
            "Every choice has a trade-off. The value of the best option you give up when you "
            "make a decision is the **opportunity cost**. If you spend Saturday studying for the "
            "GED instead of working a shift, the opportunity cost is the wages you did not earn. "
            "Opportunity cost is not just money -- it includes time, effort, and anything else "
            "you sacrifice.\n\n"
            "To produce goods and services, an economy uses **factors of production** -- the "
            "basic inputs:\n\n"
            "- **Land** -- natural resources: farmland, forests, minerals, water.\n"
            "- **Labor** -- the work people do: physical effort, skills, time.\n"
            "- **Capital** -- tools, machines, buildings, and technology used in production "
            "(sometimes called physical capital, to distinguish it from financial capital -- money).\n"
            "- **Entrepreneurship** -- the willingness to take risks and combine the other three "
            "factors to create a new business or product.\n\n"
            "A useful thinking tool is the **production possibilities curve (PPC)**, which shows "
            "the maximum combinations of two goods an economy can produce when all resources are "
            "fully used. A point inside the curve means resources are wasted; a point on the curve "
            "is efficient; a point outside is currently impossible.\n\n"
            "**Economic systems** differ in who answers the three basic questions: WHAT to produce, "
            "HOW to produce it, and FOR WHOM:\n\n"
            "- **Market (capitalist) economy** -- private individuals and businesses decide, guided "
            "by prices and profit.\n"
            "- **Command (planned) economy** -- the government decides.\n"
            "- **Mixed economy** -- most real countries, including the U.S., combine both.\n\n"
            "⚠️ Common misconception: opportunity cost is not the total cost of all options you "
            "rejected -- it is only the value of the single BEST alternative you gave up.\n\n"
            "💡 Tip: when a GED question asks for the opportunity cost, identify the best "
            "alternative that was NOT chosen, and state its value -- that is your answer.",
        ),
        (
            "2. Supply and Demand",
            "In a market economy, prices are not set by any single person. They emerge from the "
            "interaction of two forces: **supply** and **demand**.\n\n"
            "**Demand** describes how much of a good buyers are willing and able to purchase at "
            "each possible price. The **law of demand** states: when price rises, quantity "
            "demanded falls; when price falls, quantity demanded rises -- all else equal. This "
            "gives demand its downward-sloping curve on a graph.\n\n"
            "**Supply** describes how much of a good sellers are willing and able to offer at each "
            "possible price. The **law of supply** states: when price rises, quantity supplied "
            "rises; when price falls, quantity supplied falls -- higher prices reward producers. "
            "This gives supply its upward-sloping curve.\n\n"
            "[[figure:supply_demand|Where the supply and demand curves cross is the equilibrium -- "
            "the price at which the amount offered exactly equals the amount wanted.]]\n\n"
            "The point where the two curves intersect is the **equilibrium price** (also called the "
            "market-clearing price). At this price, there is no surplus (excess supply) and no "
            "shortage (excess demand).\n\n"
            "Curves can **shift** -- not just move along -- when conditions change:\n\n"
            "- **Demand shifts right (increases)** when incomes rise, the product becomes popular, "
            "a substitute becomes more expensive, or consumers expect future price increases.\n"
            "- **Supply shifts right (increases)** when production costs fall, technology improves, "
            "or more producers enter the market.\n"
            "- **Supply shifts left (decreases)** when raw materials become scarce, costs rise, or "
            "a natural disaster disrupts production (e.g., a frost destroying the orange crop).\n\n"
            "**Price elasticity of demand** measures how sensitive quantity demanded is to a price "
            "change. Necessities (insulin, electricity) tend to be **inelastic** -- demand changes "
            "little even when price rises sharply. Luxuries or items with many substitutes tend to "
            "be **elastic**.\n\n"
            "⚠️ Common misconception: 'supply' and 'demand' are not single numbers -- they are "
            "entire relationships between price and quantity, shown as curves. A change in price "
            "moves you ALONG the curve; only a change in an outside factor SHIFTS the curve.\n\n"
            "💡 Tip: scarcity + high demand = higher price; abundance + low demand = lower price. "
            "This simple rule answers most GED supply-and-demand questions.",
        ),
        (
            "3. Market Structures",
            "Not all markets work the same way. **Market structure** describes how many sellers "
            "compete, whether their products are similar, and how much control any single seller "
            "has over price.\n\n"
            "**Perfect competition** is the most competitive extreme:\n\n"
            "- Many small sellers, each selling an identical product (wheat, for example).\n"
            "- No single seller can influence the market price -- each is a **price taker**.\n"
            "- Easy for new firms to enter or exit.\n\n"
            "**Monopolistic competition** is common in everyday life (restaurants, clothing brands):\n\n"
            "- Many sellers, but each sells a slightly differentiated product.\n"
            "- Sellers have some control over price, but competition limits it.\n"
            "- **Advertising** and branding matter because firms try to make their product seem unique.\n\n"
            "**Oligopoly** -- a few large firms dominate the market (airlines, auto manufacturers, "
            "smartphone makers):\n\n"
            "- Each firm is aware of its rivals and reacts to their decisions.\n"
            "- High barriers to entry (huge start-up costs, patents, brand loyalty).\n"
            "- Firms may compete fiercely on price -- or they may **collude** (secretly agree to "
            "set prices), which is illegal in the U.S.\n\n"
            "**Monopoly** -- one seller controls the entire market for a product with no close "
            "substitutes:\n\n"
            "- The firm is a **price maker** -- it can set price above what a competitive market "
            "would charge.\n"
            "- Monopolies can result from patents, control of a key resource, government franchise, "
            "or network effects.\n"
            "- **Natural monopoly**: in some industries (water, electricity distribution), one large "
            "provider is more efficient than many small ones, so government often regulates them.\n\n"
            "**Antitrust laws** (like the Sherman Antitrust Act) exist to prevent monopolistic "
            "behavior and keep markets competitive, protecting consumers from artificially high "
            "prices.\n\n"
            "⚠️ Common misconception: a monopoly does not mean the company is the only business "
            "in the world -- it means no close SUBSTITUTE exists in that specific market. A single "
            "cable provider in a town is a local monopoly.\n\n"
            "💡 Tip: on the GED, the key contrast is between **competitive markets** (many sellers, "
            "price determined by supply and demand) and **monopolies** (one seller, price set above "
            "competitive level, consumers have no choice).",
        ),
        (
            "4. Personal Finance",
            "Personal finance is the application of economic thinking to your own money. The GED "
            "tests real-world financial literacy -- skills every adult needs.\n\n"
            "**Budgeting** is the foundation. A budget lists your **income** (money coming in) and "
            "**expenses** (money going out) over a period. A good budget follows a plan such as "
            "50/30/20: about 50% of take-home pay on needs (rent, food, utilities), 30% on wants, "
            "and 20% on savings and debt repayment. The goal is to spend less than you earn.\n\n"
            "**Saving and compound interest:**\n\n"
            "- Putting money in a savings account earns **interest** -- the bank pays you to use "
            "your money.\n"
            "- **Compound interest** means you earn interest on both your original deposit and the "
            "interest already earned. Over time, this 'interest on interest' makes savings grow "
            "much faster. Starting early matters enormously.\n\n"
            "**Credit and debt:**\n\n"
            "- **Credit** allows you to borrow now and repay later, but lenders charge "
            "**interest** for this. The **APR (annual percentage rate)** is the true yearly cost of "
            "borrowing.\n"
            "- A **credit score** (range 300--850) summarizes your credit history. Higher scores "
            "earn lower interest rates on loans and credit cards.\n"
            "- **Good debt** (a student loan, a mortgage at a reasonable rate) can build wealth or "
            "earning power. **Bad debt** (high-interest credit-card balances for everyday spending) "
            "erodes wealth.\n\n"
            "**Investing** means putting money to work to grow over time:\n\n"
            "- **Stocks** -- ownership shares in a company. Stocks offer higher potential returns "
            "but carry more risk.\n"
            "- **Bonds** -- loans you make to a company or government; generally safer but lower "
            "return.\n"
            "- **Diversification** (spreading investments across many assets) reduces risk: if one "
            "investment loses value, others may not.\n\n"
            "**Insurance** transfers risk: you pay a regular **premium** so that if something bad "
            "happens (car accident, illness), the insurance company covers the large cost.\n\n"
            "⚠️ Common misconception: paying the minimum on a credit card is NOT the same as "
            "staying out of debt. Minimum payments mostly cover interest -- the principal balance "
            "barely shrinks and the total paid can far exceed the original purchase price.\n\n"
            "💡 Tip: compound interest works for you when you SAVE and against you when you BORROW. "
            "Remember: the earlier you start saving, the more powerful compounding becomes.",
        ),
        (
            "5. The Role of Government in the Economy",
            "Even in a mostly market economy like the United States, the government plays a "
            "significant role -- setting rules, providing services markets will not, and trying "
            "to keep the economy stable.\n\n"
            "**Taxation** is how governments raise money. Common types:\n\n"
            "- **Income tax** -- a percentage of what individuals and businesses earn. The U.S. "
            "federal income tax is **progressive**: higher earners pay a higher percentage.\n"
            "- **Sales tax** -- a percentage added to the price of goods. Critics call it "
            "**regressive** because lower-income people pay a higher share of their income.\n"
            "- **Property tax** -- based on the value of owned property; funds local services.\n\n"
            "**Government spending** funds public goods and services:\n\n"
            "- **Public goods** are non-excludable (you can't easily stop people from using them) "
            "and non-rival (one person's use doesn't reduce availability for others). Examples: "
            "national defense, lighthouses, public parks. Because everyone benefits and no one can "
            "be excluded, private markets tend to underprovide them -- so government steps in.\n"
            "- **Transfer payments** redistribute income: Social Security, Medicare, unemployment "
            "insurance, and food assistance.\n\n"
            "**Regulation** sets rules for how businesses can operate:\n\n"
            "- Environmental regulations limit pollution.\n"
            "- Workplace safety rules protect workers.\n"
            "- Antitrust enforcement prevents monopolies.\n"
            "- Financial regulations protect consumers and keep banks stable.\n\n"
            "**Externalities** are costs or benefits that fall on people not involved in a "
            "transaction. A factory that pollutes a river creates a **negative externality**; a "
            "homeowner who plants a beautiful garden creates a **positive externality**. Governments "
            "often tax negative externalities (to reduce them) or subsidize positive ones "
            "(to encourage more of them).\n\n"
            "The **Federal Reserve (the Fed)** is the U.S. central bank. It controls the money "
            "supply and sets key interest rates to keep inflation low and employment high "
            "(**monetary policy**).\n\n"
            "**Fiscal policy** is the government's use of taxing and spending to influence the "
            "economy. In a recession, Congress might cut taxes or increase spending "
            "(**expansionary** policy); during inflation it might do the opposite "
            "(**contractionary** policy).\n\n"
            "⚠️ Common misconception: public goods are NOT simply goods provided by the government "
            "-- they have the specific properties of being non-excludable and non-rival. Not "
            "everything the government provides is a public good in the economic sense.\n\n"
            "💡 Tip: on the GED, look for whether a question is about FISCAL policy (Congress, "
            "taxes, spending) or MONETARY policy (the Federal Reserve, interest rates). They are "
            "separate tools.",
        ),
        (
            "6. Macroeconomics",
            "**Macroeconomics** looks at the economy as a whole -- national output, employment, "
            "price levels, and growth -- rather than individual markets.\n\n"
            "**Gross Domestic Product (GDP)** is the total dollar value of all final goods and "
            "services produced within a country in one year. It is the most widely used measure "
            "of an economy's size:\n\n"
            "- **Real GDP** adjusts for inflation, allowing fair comparisons across years.\n"
            "- **GDP per capita** (GDP divided by population) measures the average output per "
            "person and is used to compare living standards across countries.\n\n"
            "**Inflation** is a general rise in price levels over time, which means each dollar "
            "buys less (**purchasing power** falls). Causes include too much money chasing too few "
            "goods, rising production costs, or strong consumer demand. The U.S. measures "
            "inflation mainly with the **Consumer Price Index (CPI)**, which tracks the cost of a "
            "typical 'basket' of goods and services.\n\n"
            "**Unemployment** measures the share of the labor force that is actively seeking work "
            "but cannot find it. Types:\n\n"
            "- **Frictional unemployment** -- workers between jobs or entering the workforce for "
            "the first time. Normal and even healthy.\n"
            "- **Structural unemployment** -- jobs disappear because technology or industry shifts "
            "make certain skills obsolete (e.g., factory automation).\n"
            "- **Cyclical unemployment** -- caused by a downturn in the business cycle; it rises "
            "in recessions and falls during expansions.\n\n"
            "The **business cycle** describes the recurring pattern of economic expansion "
            "(growth) and contraction (recession):\n\n"
            "- **Expansion / Recovery** -- output rises, unemployment falls, consumer spending "
            "increases.\n"
            "- **Peak** -- the high point before a downturn.\n"
            "- **Recession** -- GDP falls for two or more consecutive quarters; unemployment rises.\n"
            "- **Trough** -- the low point before recovery begins.\n\n"
            "**The relationship between inflation and unemployment** is often inverse in the short "
            "run: when unemployment is very low and the economy is booming, inflation tends to rise "
            "because workers earn more and spend more. The Fed tries to balance both goals.\n\n"
            "⚠️ Common misconception: 0% unemployment is NOT the goal of a healthy economy. Some "
            "frictional unemployment is always present and is considered normal. Economists aim "
            "for the **natural rate of unemployment** (roughly 4--5% in the U.S.).\n\n"
            "💡 Tip: in a recession -- GDP falls, unemployment rises, and inflation often slows. "
            "In a boom -- GDP rises, unemployment falls, and inflation may speed up. Knowing this "
            "pattern answers many GED macro questions.",
        ),
        (
            "7. Reading Economic Data and Graphs",
            "The GED Social Studies test regularly presents **graphs, tables, and charts** about "
            "economic topics. Learning to read them accurately is a tested skill in its own right.\n\n"
            "**Before reading any graph:**\n\n"
            "- Read the **title** to know what is being shown.\n"
            "- Read the **axis labels** and **units** (dollars, percentages, millions of workers).\n"
            "- Check the **time period** or **categories** on the horizontal axis.\n"
            "- Note the **scale**: an axis that starts at 90 instead of 0 can make a small change "
            "look dramatic (a **truncated axis** or **misleading graph**).\n\n"
            "**Common graph types in economics:**\n\n"
            "- **Line graph** -- shows change over time. Ideal for GDP growth, inflation rates, or "
            "unemployment rates across years.\n"
            "- **Bar graph** -- compares categories or groups. Used to compare income levels, "
            "spending by sector, or trade balances between countries.\n"
            "- **Pie chart** -- shows parts of a whole. Common for showing budget breakdowns or "
            "how GDP is divided among consumption, investment, government spending, and net "
            "exports.\n"
            "- **Scatter plot** -- shows the relationship between two variables (e.g., education "
            "level vs. income). A positive correlation slopes up; a negative correlation slopes "
            "down.\n\n"
            "**Key analysis skills:**\n\n"
            "- Identify the **trend**: is the value rising, falling, or staying flat?\n"
            "- Identify the **turning point**: when did the trend change direction?\n"
            "- Use **only the data shown** -- do not assume information not in the graph.\n"
            "- Remember: **correlation does not equal causation**. Two things moving together does "
            "not mean one causes the other.\n\n"
            "**Interpreting economic tables**: look at column headers carefully. A table showing "
            "GDP in 'billions of chained 2012 dollars' is inflation-adjusted real GDP -- very "
            "different from a table in 'current dollars'.\n\n"
            "⚠️ Common misconception: a line going up on a graph is not automatically 'good news'. "
            "Rising unemployment or rising inflation is shown with an upward line too -- always "
            "check what the graph measures before drawing a conclusion.\n\n"
            "💡 Tip: treat every economic graph question like a math data question: title, labels, "
            "units, scale -- THEN read the question and find the answer in the graph itself.",
        ),
    ],
    "mcqs": [
        # Lesson 1 -- Basic Economic Concepts
        {
            "text": "Because resources are limited and wants are unlimited, people must make choices. This condition is called:",
            "difficulty": 1,
            "choices": [
                ("Scarcity", True),
                ("Inflation", False),
                ("Surplus", False),
                ("Productivity", False),
            ],
            "explanation": "Scarcity is the fundamental economic problem: resources (time, money, materials) are limited but human wants are unlimited, forcing choices.",
        },
        {
            "text": "A student decides to spend Saturday studying for the GED instead of working a part-time shift that would have paid $60. The opportunity cost of studying is:",
            "difficulty": 2,
            "choices": [
                ("$60 in lost wages", True),
                ("The cost of textbooks", False),
                ("Zero, because studying is free", False),
                ("The tuition fee for the GED test", False),
            ],
            "explanation": "Opportunity cost is the value of the best alternative given up. The student gave up a $60 shift, so that is the opportunity cost -- not money spent, but money not earned.",
        },
        {
            "text": "Which of the following is an example of CAPITAL as a factor of production?",
            "difficulty": 2,
            "choices": [
                ("A printing press used to produce newspapers", True),
                ("A forest of timber trees", False),
                ("A carpenter's daily labor", False),
                ("A business owner's willingness to take risks", False),
            ],
            "explanation": "Capital refers to human-made tools and equipment used in production. The printing press is a machine -- capital. A forest is land; labor is the carpenter's work; risk-taking describes entrepreneurship.",
        },
        {
            "text": "In a COMMAND economy, who decides what goods are produced and at what prices they are sold?",
            "difficulty": 2,
            "choices": [
                ("The government", True),
                ("Private businesses competing for profit", False),
                ("Supply and demand in free markets", False),
                ("Individual consumers", False),
            ],
            "explanation": "In a command (planned) economy, the government makes central production and pricing decisions. In a market economy, those decisions are decentralized among businesses and consumers.",
        },
        {
            "text": "A production possibilities curve shows an economy operating at a point INSIDE the curve. This means the economy is:",
            "difficulty": 3,
            "choices": [
                ("Not using all of its resources efficiently", True),
                ("Producing more than is possible", False),
                ("At its maximum possible output", False),
                ("Experiencing high inflation", False),
            ],
            "explanation": "A point inside the PPC means resources are unemployed or inefficiently used. A point ON the curve is fully efficient; a point outside is currently unachievable.",
        },
        # Lesson 2 -- Supply and Demand
        {
            "text": "According to the law of demand, when the price of a product rises, all else equal, what happens to the quantity demanded?",
            "difficulty": 1,
            "choices": [
                ("It decreases", True),
                ("It increases", False),
                ("It stays the same", False),
                ("It first rises and then falls", False),
            ],
            "explanation": "The law of demand: higher prices make buyers purchase less; lower prices make buyers purchase more. This inverse relationship gives the demand curve its downward slope.",
        },
        {
            "text": "A drought severely reduces wheat harvests. Using supply and demand, what is the most likely effect on the price of bread?",
            "difficulty": 2,
            "choices": [
                ("Bread prices rise because supply has decreased", True),
                ("Bread prices fall because people eat less", False),
                ("Bread prices are unaffected because demand has not changed", False),
                ("Bread prices fall because producers lower prices to attract buyers", False),
            ],
            "explanation": "A drought reduces wheat supply, which shifts the supply curve left. With demand unchanged, the equilibrium price rises -- bread becomes more expensive.",
        },
        {
            "text": "The price at which the quantity of a good supplied exactly equals the quantity demanded is called the:",
            "difficulty": 1,
            "choices": [
                ("Equilibrium price", True),
                ("Opportunity cost", False),
                ("Price ceiling", False),
                ("Marginal cost", False),
            ],
            "explanation": "The equilibrium (market-clearing) price is where the supply and demand curves intersect -- no surplus and no shortage exist at this price.",
        },
        {
            "text": "Insulin is a life-saving medication for diabetics. If the price of insulin doubles, the quantity demanded is likely to fall only slightly. This means demand for insulin is:",
            "difficulty": 3,
            "choices": [
                ("Inelastic, because buyers need it regardless of price", True),
                ("Elastic, because buyers will quickly switch to substitutes", False),
                ("Perfectly elastic, because price cannot change demand", False),
                ("Perfectly inelastic only if the government regulates it", False),
            ],
            "explanation": "Inelastic demand means quantity demanded is not very sensitive to price changes. Necessities with few or no substitutes, like insulin, tend to be inelastic -- patients must buy it.",
        },
        # Lesson 3 -- Market Structures
        {
            "text": "In a perfectly competitive market, individual sellers are called 'price takers.' This means they:",
            "difficulty": 2,
            "choices": [
                ("Must accept the market price because no single seller can influence it", True),
                ("Can set any price they want because they produce a unique product", False),
                ("Negotiate prices directly with each buyer", False),
                ("Receive subsidies from the government to set prices", False),
            ],
            "explanation": "In perfect competition, many sellers offer identical products. No single seller is large enough to affect the market price, so each must 'take' the price the market sets.",
        },
        {
            "text": "A city has only one electric utility company, and customers cannot easily switch to another provider. This is best described as a:",
            "difficulty": 2,
            "choices": [
                ("Monopoly", True),
                ("Perfectly competitive market", False),
                ("Monopolistic competition", False),
                ("Oligopoly", False),
            ],
            "explanation": "A monopoly exists when one seller controls the market and buyers have no close substitutes. A single local utility with no competition is a classic example of a natural monopoly.",
        },
        {
            "text": "The U.S. airline industry is dominated by a small number of large carriers. This market structure is called:",
            "difficulty": 2,
            "choices": [
                ("Oligopoly", True),
                ("Perfect competition", False),
                ("Pure monopoly", False),
                ("Monopolistic competition", False),
            ],
            "explanation": "An oligopoly has a few large firms dominating the market. Airlines feature high barriers to entry, a small number of major players, and strategic interdependence among competitors.",
        },
        {
            "text": "Antitrust laws, such as the Sherman Antitrust Act, are designed primarily to:",
            "difficulty": 3,
            "choices": [
                ("Prevent monopolies and promote competition to protect consumers", True),
                ("Set minimum wages for workers in competitive industries", False),
                ("Allow large companies to merge without government oversight", False),
                ("Guarantee profits for small businesses", False),
            ],
            "explanation": "Antitrust laws break up or prevent monopolies and block collusion so that markets remain competitive -- keeping prices lower and quality higher for consumers.",
        },
        # Lesson 4 -- Personal Finance
        {
            "text": "Maria earns $2,500 per month. After paying $1,200 in rent and $400 in other necessities, she has $900 left. She spends $700 on wants and saves $200. Which budget adjustment would MOST improve her long-term financial health?",
            "difficulty": 2,
            "choices": [
                ("Reduce spending on wants and increase savings", True),
                ("Take out a high-interest loan to increase monthly spending", False),
                ("Stop paying rent to save more money", False),
                ("Invest all $900 in a single high-risk stock", False),
            ],
            "explanation": "Financial health improves by saving more and spending less on nonessential wants. Reducing the $700 in wants gives more to save or invest. Loans add debt; skipping rent is not realistic; putting everything in one risky stock is poor diversification.",
        },
        {
            "text": "You borrow $1,000 on a credit card with a 24% APR. If you make only minimum payments, you will end up paying far more than $1,000. This is because of:",
            "difficulty": 2,
            "choices": [
                ("Compound interest accumulating on the unpaid balance", True),
                ("The government charging extra taxes on credit card purchases", False),
                ("Inflation reducing the value of your payments", False),
                ("Banks randomly increasing the principal amount owed", False),
            ],
            "explanation": "When you carry a balance, interest is charged on the remaining balance each month. Because you're charged interest on interest (compounding), small minimum payments barely reduce principal, and the total paid grows far beyond the original amount borrowed.",
        },
        {
            "text": "Diversification is a strategy used by investors to:",
            "difficulty": 2,
            "choices": [
                ("Spread investments across different assets to reduce risk", True),
                ("Invest all savings in the single highest-returning stock", False),
                ("Avoid paying taxes on investment gains", False),
                ("Guarantee a fixed return regardless of market conditions", False),
            ],
            "explanation": "Diversification reduces risk by not putting all your eggs in one basket. If one investment loses value, others in the portfolio may hold steady or gain, cushioning the loss.",
        },
        {
            "text": "A 25-year-old and a 45-year-old each start saving $200 per month in an account earning 6% annual interest. Who will likely have more money at age 65, and why?",
            "difficulty": 3,
            "choices": [
                ("The 25-year-old, because compound interest has 40 years to grow", True),
                ("The 45-year-old, because older savers understand investing better", False),
                ("Both will have exactly the same amount", False),
                ("The 45-year-old, because interest rates increase with age", False),
            ],
            "explanation": "Compound interest rewards time above all else. The 25-year-old invests for 40 years and gains interest on a growing balance. The 45-year-old only has 20 years. The difference in final balances is dramatic even though monthly contributions are identical.",
        },
        # Lesson 5 -- Role of Government in the Economy
        {
            "text": "A progressive income tax means that:",
            "difficulty": 2,
            "choices": [
                ("People with higher incomes pay a higher percentage of their income in taxes", True),
                ("Everyone pays the same flat dollar amount in taxes", False),
                ("Lower-income earners pay a higher share of their income in taxes", False),
                ("Only businesses pay income taxes, not individuals", False),
            ],
            "explanation": "A progressive tax increases the tax rate as income rises -- higher earners pay a larger percentage. This contrasts with a flat tax (same rate for everyone) and a regressive tax (lower earners pay a higher share).",
        },
        {
            "text": "National defense is considered a PUBLIC GOOD because it is:",
            "difficulty": 2,
            "choices": [
                ("Non-excludable and non-rival -- everyone benefits and one person's protection does not reduce another's", True),
                ("Provided only to taxpayers who pay for it directly", False),
                ("Available only during wartime", False),
                ("Produced by private companies competing for contracts", False),
            ],
            "explanation": "Public goods have two key properties: non-excludable (you can't stop someone from benefiting) and non-rival (one person's use doesn't reduce availability for others). National defense fits perfectly.",
        },
        {
            "text": "A factory dumps chemicals into a nearby river, harming local fishers who had no part in the factory's production. This is an example of a:",
            "difficulty": 3,
            "choices": [
                ("Negative externality", True),
                ("Positive externality", False),
                ("Public good", False),
                ("Price ceiling", False),
            ],
            "explanation": "A negative externality is a cost imposed on uninvolved third parties. The fishers bear the cost of the pollution they did not create -- a classic market failure that often justifies government regulation.",
        },
        {
            "text": "During a recession, the government increases spending on infrastructure and cuts taxes to stimulate the economy. This is an example of:",
            "difficulty": 3,
            "choices": [
                ("Expansionary fiscal policy", True),
                ("Contractionary monetary policy", False),
                ("Regressive taxation", False),
                ("Supply-side regulation", False),
            ],
            "explanation": "Fiscal policy uses government taxing and spending to influence the economy. Increasing spending and cutting taxes during a recession is expansionary fiscal policy -- designed to boost demand and reduce unemployment.",
        },
        # Lesson 6 -- Macroeconomics
        {
            "text": "Gross Domestic Product (GDP) measures:",
            "difficulty": 1,
            "choices": [
                ("The total value of all final goods and services produced in a country in one year", True),
                ("The total amount of money printed by the government each year", False),
                ("The combined savings of all households in the country", False),
                ("The average wage earned by workers nationwide", False),
            ],
            "explanation": "GDP is the broadest measure of an economy's output: the dollar value of all final goods and services produced within the country's borders in a year.",
        },
        {
            "text": "The Consumer Price Index (CPI) is used to measure:",
            "difficulty": 2,
            "choices": [
                ("The rate of inflation by tracking changes in the price of a typical basket of goods", True),
                ("The total number of goods produced by consumers each year", False),
                ("The amount of goods imported from other countries", False),
                ("The growth rate of the stock market", False),
            ],
            "explanation": "The CPI tracks the cost of a standard market basket of goods and services over time. When the CPI rises, it means the average price level has increased -- inflation has occurred.",
        },
        {
            "text": "A worker loses her job at an automobile plant because robots now perform her task. This is an example of:",
            "difficulty": 3,
            "choices": [
                ("Structural unemployment", True),
                ("Frictional unemployment", False),
                ("Cyclical unemployment", False),
                ("Voluntary unemployment", False),
            ],
            "explanation": "Structural unemployment occurs when a worker's skills no longer match available jobs due to technological change or shifts in industry. Automation replacing a factory worker is a textbook example.",
        },
        {
            "text": "During a recession, which of the following changes would you MOST expect to see?",
            "difficulty": 2,
            "choices": [
                ("GDP falls and unemployment rises", True),
                ("GDP rises and unemployment falls", False),
                ("Inflation accelerates and unemployment falls", False),
                ("GDP rises while consumer spending drops", False),
            ],
            "explanation": "A recession is defined as a period of falling GDP (at least two consecutive quarters of decline). As businesses cut production, they lay off workers, so unemployment rises during recessions.",
        },
        {
            "text": "Which stage of the business cycle immediately follows a recession's lowest point (the trough)?",
            "difficulty": 2,
            "choices": [
                ("Recovery (expansion), when output begins rising again", True),
                ("A second, deeper recession", False),
                ("Hyperinflation caused by falling production", False),
                ("A peak, which always comes before the trough", False),
            ],
            "explanation": "The business cycle moves: expansion → peak → recession/contraction → trough → recovery (expansion again). After hitting the trough (the lowest point), the economy enters recovery -- GDP starts rising and unemployment begins to fall.",
        },
        # Lesson 7 -- Reading Economic Data and Graphs
        {
            "text": "A graph showing U.S. GDP from 2000 to 2020 has a vertical axis that begins at $14 trillion instead of $0. What is the risk of this presentation?",
            "difficulty": 3,
            "choices": [
                ("The truncated axis makes small changes look much larger than they really are", True),
                ("Starting at $14 trillion proves GDP has never been lower", False),
                ("The graph cannot be read accurately no matter what", False),
                ("The graph shows inflation-adjusted data, which is always misleading", False),
            ],
            "explanation": "A truncated axis (one that does not start at zero) exaggerates differences by cutting off the bottom of the scale. This is a common way graphs can mislead -- small changes appear dramatic.",
        },
        {
            "text": "A line graph shows that in every year from 2010 to 2020, countries with higher average education levels also had higher average incomes. A student concludes that 'education causes higher income.' What is wrong with this conclusion?",
            "difficulty": 3,
            "choices": [
                ("Correlation does not prove causation -- other factors may explain both", True),
                ("Nothing is wrong; a clear trend on a graph always shows causation", False),
                ("Line graphs cannot show relationships between two variables", False),
                ("The conclusion is wrong because education never affects income", False),
            ],
            "explanation": "Two variables moving together (correlation) does not prove one causes the other. Other factors (economic development, government investment) may cause both higher education and higher income. This is a foundational data-literacy principle.",
        },
        {
            "text": "A pie chart shows that 68% of the federal budget is spent on mandatory programs (Social Security, Medicare, Medicaid), 15% on defense, and the remaining 17% on all other discretionary spending. A politician proposes balancing the budget only by cutting the 'other' category. Based on the data, what is the most accurate observation?",
            "difficulty": 3,
            "choices": [
                ("Cuts to only the 17% category cannot fully close a large budget deficit because most spending is in mandatory programs", True),
                ("The 17% category is clearly the main cause of any deficit", False),
                ("The data shows defense spending is greater than mandatory spending", False),
                ("Pie charts cannot be used to analyze budget data", False),
            ],
            "explanation": "The data shows that 68% of spending is mandatory -- far larger than the 17% discretionary 'other' category. Cutting only that small slice cannot fully address a large deficit. Reading the proportions accurately leads to this conclusion.",
        },
        {
            "text": "When reading an economic data table, the column header reads 'GDP in billions of chained 2012 dollars.' The phrase 'chained 2012 dollars' tells you the data has been:",
            "difficulty": 3,
            "choices": [
                ("Adjusted for inflation, allowing fair comparisons across years", True),
                ("Converted from foreign currencies to U.S. dollars", False),
                ("Rounded to the nearest $2,012", False),
                ("Calculated only for the year 2012", False),
            ],
            "explanation": "'Chained dollars' with a base year (2012) means the data is expressed in real (inflation-adjusted) terms. This allows GDP in 2005 and 2020 to be compared as if prices had stayed constant at 2012 levels.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the 'GED Social Studies: Economics' deep-dive course."

    def handle(self, *args, **options):
        Course.objects.filter(slug=COURSE["slug"]).delete()  # idempotent
        course = Course.objects.create(
            title=COURSE["title"],
            slug=COURSE["slug"],
            program=COURSE["program"],
            subject=COURSE["subject"],
            description=COURSE["description"],
        )
        for i, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=i)
        for q in COURSE["mcqs"]:
            question = Question.objects.create(
                course=course, qtype="mcq", text=q["text"],
                difficulty=q["difficulty"], explanation=q["explanation"],
            )
            for text, correct in q["choices"]:
                Choice.objects.create(question=question, text=text, is_correct=correct)
        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' -- "
            f"{course.lessons.count()} lessons, {course.questions.count()} questions."
        ))
