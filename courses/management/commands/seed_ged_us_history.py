"""
Seed data: 'GED Social Studies: U.S. History' -- a deep dive into the U.S. History
content area of the GED Social Studies test (about 20 % of the exam).

Covers the full sweep from Colonial America through the present day in seven lessons,
organised around the eras and skills the GED tests most: causes and effects of key
events, primary-source analysis, and understanding how the meaning of liberty and
equality has expanded over time.

Run:
    python manage.py seed_ged_us_history
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: U.S. History",
    "slug": "ged-us-history",
    "program": "GED",
    "subject": "social",
    "description": (
        "U.S. History makes up roughly one-fifth of the GED Social Studies test. This deep-dive "
        "course walks through seven eras -- from Colonial America and the Revolution, through the "
        "Civil War, Reconstruction, and the Industrial Age, into the World Wars and Civil Rights "
        "movement, and up to the present. Every lesson builds the cause-and-effect reasoning and "
        "primary-source reading skills the GED actually tests."
    ),
    "lessons": [
        (
            "1. Colonial America & the Road to Independence",
            "[[figure:us_timeline|Key dates in American history from colonisation to the present day.]]\n\n"
            "Long before 1776, the land that became the United States was home to diverse "
            "**Native American** peoples with rich cultures, languages, and trade networks. European "
            "exploration began in earnest after Columbus reached the Americas in 1492, and **English "
            "colonisation** of the eastern seaboard started at Jamestown, Virginia in **1607**.\n\n"
            "By the mid-1700s, thirteen British colonies had grown along the Atlantic coast. Colonists "
            "were largely self-governing through elected assemblies, which made them value local "
            "control. That tradition clashed directly with Britain's decision -- after the expensive "
            "**French and Indian War (1754-1763)** -- to tax the colonies to pay its war debts.\n\n"
            "The cry of **'no taxation without representation'** captured the colonial anger. Key "
            "flashpoints included:\n\n"
            "- **Stamp Act (1765)** -- a direct tax on printed materials; colonists boycotted British goods.\n"
            "- **Boston Massacre (1770)** -- British soldiers killed five colonists; used as powerful propaganda.\n"
            "- **Boston Tea Party (1773)** -- colonists dumped British tea into Boston Harbor to protest the Tea Act.\n"
            "- **Intolerable Acts (1774)** -- Britain's harsh response, which united the colonies further.\n\n"
            "Enlightenment ideas also shaped colonial thinking. Thinkers like **John Locke** argued "
            "that people have natural rights -- life, liberty, and property -- and that government "
            "exists only to protect those rights. If it fails, the people may change it. These ideas "
            "flowed directly into the **Declaration of Independence (1776)**.\n\n"
            "⚠️ Common misconception: the colonists did not simply object to paying taxes -- they "
            "objected to being taxed by a parliament in which they had **no elected representatives**. "
            "The distinction between taxation and taxation without representation is a GED favourite.\n\n"
            "💡 Tip: connect each cause to its effect. The French and Indian War -> British debt -> "
            "new taxes -> colonial anger -> Revolution. Knowing the chain beats memorising isolated dates.",
        ),
        (
            "2. American Revolution & the New Nation 1775-1800",
            "Armed conflict began in April **1775** at Lexington and Concord, Massachusetts. The "
            "**Second Continental Congress** quickly formed a continental army and named **George "
            "Washington** its commander. After months of debate, delegates adopted the "
            "**Declaration of Independence on July 4, 1776**, written mainly by **Thomas Jefferson**.\n\n"
            "The Declaration made three bold claims:\n\n"
            "- All people are created equal and have **unalienable rights** -- life, liberty, and the pursuit of happiness.\n"
            "- Governments exist to protect those rights and derive their power from the **consent of the governed**.\n"
            "- When a government violates rights, the people have the right to **alter or abolish** it.\n\n"
            "The war itself was far from certain. The Continental Army endured the brutal winter at "
            "**Valley Forge (1777-1778)**. The turning point was the **Battle of Saratoga (1777)**, "
            "which convinced **France** to enter as an American ally. French money, troops, and naval "
            "power proved decisive. Britain surrendered at **Yorktown in 1781**, and the "
            "**Treaty of Paris (1783)** officially recognised American independence.\n\n"
            "The new nation first governed itself under the **Articles of Confederation**, but the "
            "central government was too weak -- it couldn't tax, couldn't enforce laws, and couldn't "
            "keep order (Shays' Rebellion, 1786, alarmed leaders). Delegates met in Philadelphia in "
            "**1787** and wrote the **Constitution**, which replaced the Articles. After fierce debate, "
            "it was ratified in 1788, and the first ten amendments -- the **Bill of Rights** -- were "
            "added in **1791** to protect individual freedoms.\n\n"
            "⚠️ Common misconception: the Declaration of Independence (1776) and the Constitution (1787) "
            "are entirely different documents written eleven years apart. The Declaration announced "
            "independence; the Constitution created the government's structure.\n\n"
            "💡 Tip: know the three-step sequence -- Declaration (independence) -> Articles (weak "
            "government) -> Constitution (strong framework). The GED loves putting these in order.",
        ),
        (
            "3. Expansion, Conflict & the Civil War Era 1800-1865",
            "After 1800, the young United States grew rapidly westward. The **Louisiana Purchase "
            "(1803)** -- when President **Thomas Jefferson** bought a vast territory from France -- "
            "roughly doubled the nation's size. The idea that the U.S. was destined to stretch from "
            "coast to coast became known as **Manifest Destiny**.\n\n"
            "Expansion, however, raised a question that could not be avoided: would new territories "
            "allow **slavery**? The country was already deeply divided:\n\n"
            "- The **South** relied on enslaved labor for cotton plantations and wanted to extend slavery.\n"
            "- The **North** was industrialising and increasingly opposed to slavery's spread.\n"
            "- A series of compromises -- the **Missouri Compromise (1820)**, the **Compromise of 1850**, "
            "and the **Kansas-Nebraska Act (1854)** -- temporarily patched the divide but settled nothing.\n\n"
            "The **Dred Scott decision (1857)** by the Supreme Court ruled that enslaved people were "
            "property, not citizens -- enraging the North. The election of **Abraham Lincoln** in "
            "**1860**, on a platform opposing slavery's spread, triggered Southern secession. Eleven "
            "southern states formed the **Confederate States of America**, and the **Civil War** began "
            "in April **1861** when Confederate forces fired on Fort Sumter.\n\n"
            "Key Civil War developments:\n\n"
            "- **Emancipation Proclamation (January 1, 1863)** -- Lincoln declared enslaved people in "
            "Confederate states to be free, turning the war into an explicit fight to end slavery.\n"
            "- **Battle of Gettysburg (July 1863)** -- the bloodiest battle of the war; the Union's "
            "victory stopped the Confederate advance into the North.\n"
            "- **Gettysburg Address (November 1863)** -- Lincoln's short, powerful speech redefined the "
            "war as a struggle for equality and democracy.\n"
            "- The Confederacy surrendered in April **1865**; Lincoln was assassinated days later.\n\n"
            "⚠️ Common misconception: the Civil War was caused by **multiple factors** -- slavery, "
            "states' rights, economic differences -- but the GED recognises slavery as the **central "
            "cause**. The Emancipation Proclamation did not immediately free all enslaved people; it "
            "applied only to Confederate states.\n\n"
            "💡 Tip: trace the sequence -- Manifest Destiny -> slavery debate -> failed compromises -> "
            "election of Lincoln -> secession -> war. Understanding WHY something happened earns more "
            "GED points than memorising exact dates.",
        ),
        (
            "4. Reconstruction & the Gilded Age 1865-1900",
            "After the Civil War, the U.S. faced the enormous task of **Reconstruction** -- "
            "rebuilding the South and defining the rights of four million formerly enslaved people.\n\n"
            "Three constitutional amendments were passed during this period:\n\n"
            "- **13th Amendment (1865)** -- abolished slavery throughout the United States.\n"
            "- **14th Amendment (1868)** -- granted citizenship and equal protection under the law to "
            "all persons born or naturalised in the U.S.\n"
            "- **15th Amendment (1870)** -- prohibited denying the vote based on race.\n\n"
            "For a time, African American men voted and held office across the South. However, "
            "Reconstruction ended in **1877** when federal troops were withdrawn. Southern states "
            "quickly passed **Jim Crow laws** -- legal segregation that separated races in schools, "
            "restaurants, transportation, and public life. **Poll taxes**, **literacy tests**, and "
            "**grandfather clauses** were used to strip Black voters of their rights in practice, "
            "despite the 15th Amendment.\n\n"
            "Simultaneously, the U.S. entered the **Gilded Age** (roughly 1870-1900), an era of "
            "explosive **industrialisation**:\n\n"
            "- **Railroads** linked the continent, enabling national markets.\n"
            "- **Steel, oil, and finance** produced enormous fortunes for industrialists like Andrew "
            "Carnegie and John D. Rockefeller -- called **'robber barons'** by critics for their "
            "ruthless business methods.\n"
            "- Millions of **immigrants** arrived from Europe and Asia, providing factory labor.\n"
            "- Workers responded to dangerous conditions and long hours by forming **labor unions** "
            "to demand better wages and safety.\n\n"
            "⚠️ Common misconception: the 13th Amendment ended slavery, but it did NOT guarantee full "
            "equality. Jim Crow laws and disenfranchisement showed that legal freedom and practical "
            "freedom were very different things for decades.\n\n"
            "💡 Tip: the Reconstruction amendments (13th, 14th, 15th) are heavily tested. Know what "
            "each one did and in what order they were ratified.",
        ),
        (
            "5. Progressive Era, WWI & the Great Depression 1900-1940",
            "The **Progressive Era (roughly 1890-1920)** was a response to the Gilded Age's excesses. "
            "Reformers called **'muckrakers'** -- journalists like **Upton Sinclair** (whose book "
            "*The Jungle* exposed meatpacking conditions) -- exposed corruption and inequality.\n\n"
            "Progressive achievements included:\n\n"
            "- **17th Amendment (1913)** -- direct election of U.S. senators by voters (previously "
            "chosen by state legislatures).\n"
            "- **18th Amendment (1919)** -- Prohibition, banning alcohol (later repealed by the 21st).\n"
            "- **19th Amendment (1920)** -- women's **right to vote**, after decades of the "
            "**suffrage movement** led by figures like Susan B. Anthony and Elizabeth Cady Stanton.\n"
            "- Antitrust laws broke up monopolies; food and drug laws protected consumers.\n\n"
            "**World War I (1914-1918)** began in Europe. The U.S. stayed neutral until 1917, when "
            "German submarine attacks on American ships and the **Zimmermann Telegram** (Germany "
            "proposing a military alliance with Mexico against the U.S.) pushed Congress to declare war. "
            "American troops helped tip the balance; Germany surrendered in November **1918**.\n\n"
            "President **Woodrow Wilson** proposed the **Fourteen Points** for a just peace, including "
            "a **League of Nations**. The Treaty of Versailles (1919) harshly punished Germany, "
            "planting seeds for future conflict; the U.S. Senate refused to join the League.\n\n"
            "The **Roaring Twenties** saw economic boom, cultural change, and new technology. The boom "
            "ended with the **stock market crash of October 1929**, triggering the **Great Depression** -- "
            "the worst economic collapse in U.S. history. Unemployment reached 25 %; banks failed; "
            "families lost homes. President **Franklin D. Roosevelt (FDR)** responded with the "
            "**New Deal** -- a series of programs and reforms that put people back to work, regulated "
            "banks, and created a social safety net (including **Social Security**, 1935).\n\n"
            "⚠️ Common misconception: the New Deal did not fully end the Great Depression -- World War II "
            "spending ultimately ended mass unemployment. The New Deal's lasting legacy was its "
            "regulatory and social-insurance programs.\n\n"
            "💡 Tip: for the GED, connect each amendment to its specific right -- 17th = direct Senate "
            "elections, 19th = women's vote. And remember the Depression sequence: crash (1929) -> "
            "Depression -> New Deal.",
        ),
        (
            "6. WWII, the Cold War & Civil Rights 1940-1970",
            "**World War II (1939-1945)** began when Nazi Germany invaded Poland. Again the U.S. "
            "stayed neutral until **Japan attacked Pearl Harbor, Hawaii, on December 7, 1941**, "
            "drawing America into the war on two fronts.\n\n"
            "Key WWII facts the GED tests:\n\n"
            "- The U.S. fought in both **Europe** (against Germany and Italy) and the **Pacific** "
            "(against Japan).\n"
            "- **D-Day (June 6, 1944)** -- the Allied invasion of Normandy, France; the largest "
            "seaborne invasion in history.\n"
            "- The **Holocaust** -- Nazi Germany's systematic murder of six million Jewish people and "
            "millions of others.\n"
            "- The U.S. dropped **atomic bombs** on Hiroshima and Nagasaki (August 1945); Japan "
            "surrendered, ending the war.\n"
            "- At home, women entered the workforce in large numbers (**'Rosie the Riveter'**); "
            "Japanese Americans were unjustly imprisoned in **internment camps**.\n\n"
            "After the war, the **United Nations** was founded (1945) to prevent future conflicts. "
            "The U.S. and Soviet Union -- former allies -- fell into the **Cold War**: a decades-long "
            "ideological struggle between American **capitalism/democracy** and Soviet **communism**. "
            "Neither side directly attacked the other (each had nuclear weapons), but they competed "
            "globally. Key Cold War events include the **Korean War (1950-1953)**, the "
            "**Cuban Missile Crisis (1962)**, and the **Vietnam War (U.S. involvement: 1965-1973)**.\n\n"
            "At home, African Americans and allies waged the **Civil Rights Movement** to dismantle "
            "legal segregation:\n\n"
            "- **Brown v. Board of Education (1954)** -- Supreme Court ruled school segregation unconstitutional.\n"
            "- **Montgomery Bus Boycott (1955-1956)** -- sparked by Rosa Parks; led by Dr. **Martin Luther King Jr.**\n"
            "- **March on Washington (1963)** -- King's 'I Have a Dream' speech.\n"
            "- **Civil Rights Act of 1964** -- banned discrimination in public places and employment.\n"
            "- **Voting Rights Act of 1965** -- prohibited discriminatory voting practices.\n\n"
            "⚠️ Common misconception: the Cold War was not a direct military war between the U.S. and "
            "USSR -- it was fought through proxy wars, espionage, and competition. A 'hot' nuclear war "
            "was what both sides feared and avoided.\n\n"
            "💡 Tip: the GED often pairs a Civil Rights event with its effect on law. Know: Brown v. "
            "Board -> school desegregation; Civil Rights Act -> public accommodations; Voting Rights "
            "Act -> protected access to the ballot.",
        ),
        (
            "7. Modern America 1970-Present & Reading Historical Sources",
            "The last five decades brought sweeping changes to American society, economy, and "
            "world role.\n\n"
            "Key developments since 1970:\n\n"
            "- **Watergate Scandal (1972-1974)** -- President **Richard Nixon**'s administration broke "
            "into Democratic headquarters; the cover-up led to Nixon's resignation -- the first "
            "presidential resignation in U.S. history.\n"
            "- **End of the Cold War** -- the Soviet Union collapsed in **1991**, ending the Cold War "
            "and leaving the U.S. as the world's sole superpower.\n"
            "- **September 11, 2001** -- terrorist attacks killed nearly 3,000 people; the U.S. "
            "launched the **War on Terror** in Afghanistan and later invaded Iraq.\n"
            "- **Great Recession (2007-2009)** -- financial crisis caused by a housing bubble collapse; "
            "the worst economic downturn since the Great Depression.\n"
            "- Technology, globalisation, and shifting demographics continued to reshape the economy "
            "and culture.\n\n"
            "The GED tests not just historical facts but the **skill of reading historical sources**. "
            "Two source types to know:\n\n"
            "- **Primary sources** -- made during the time being studied: speeches, letters, laws, "
            "photographs, diaries. They give a direct window into the period but reflect their "
            "author's perspective.\n"
            "- **Secondary sources** -- made later by people analysing events: textbooks, documentaries, "
            "historians' articles. Useful for context but one step removed.\n\n"
            "When analysing any source, ask:\n\n"
            "- **Who** created it, and what was their purpose?\n"
            "- **When** was it made -- does the timing matter?\n"
            "- What **point of view or bias** does it reflect?\n"
            "- What does it **prove**, and what does it **not** prove?\n\n"
            "Always distinguish **fact** (a statement that can be verified) from **opinion** (a "
            "judgment or interpretation). The GED frequently asks you to identify which claims in a "
            "passage are supported by evidence and which are not.\n\n"
            "⚠️ Common misconception: a source being official, old, or written by a famous person does "
            "not make it objective. Every source reflects the biases and goals of its creator.\n\n"
            "💡 Tip: on GED history passages, read the source header (who wrote it, when, why) before "
            "reading the text -- that context will help you answer every question about it.",
        ),
    ],
    "mcqs": [
        # --- Lesson 1: Colonial America & Road to Independence ---
        {
            "text": "Colonists protested 'taxation without representation' mainly because they:",
            "difficulty": 2,
            "choices": [
                ("Had no elected representatives in the British Parliament that taxed them", True),
                ("Refused to pay any taxes under any circumstances", False),
                ("Wanted to remain part of Britain and avoid war", False),
                ("Objected only to taxes on imported tea", False),
            ],
            "explanation": "The core colonial complaint was political: Parliament was imposing taxes on people who had no voice in that body. The issue was representation, not taxation itself.",
        },
        {
            "text": "Which event directly helped unite the thirteen colonies against British rule by showing Britain's willingness to punish dissent harshly?",
            "difficulty": 2,
            "choices": [
                ("The Intolerable Acts of 1774", True),
                ("The signing of the Mayflower Compact", False),
                ("The French and Indian War", False),
                ("The founding of Jamestown in 1607", False),
            ],
            "explanation": "The Intolerable Acts were Britain's punishing response to the Boston Tea Party. Their harshness alarmed colonists throughout all thirteen colonies, pushing them toward unified resistance.",
        },
        {
            "text": "Enlightenment thinker John Locke argued that if a government fails to protect people's natural rights, the people have the right to:",
            "difficulty": 3,
            "choices": [
                ("Alter or replace that government", True),
                ("Submit peacefully and wait for change", False),
                ("Appeal to the king for more laws", False),
                ("Move to a new country", False),
            ],
            "explanation": "Locke's social-contract theory held that legitimate government rests on consent and exists to protect rights. If it fails this duty, citizens may change it -- an idea the Declaration of Independence borrowed directly.",
        },
        {
            "text": "The French and Indian War (1754-1763) contributed to the American Revolution mainly because it:",
            "difficulty": 3,
            "choices": [
                ("Left Britain deeply in debt and led it to tax the colonies", True),
                ("Gave France control of the thirteen colonies", False),
                ("Proved that colonists could not defend themselves without British help", False),
                ("Created the first colonial representative assemblies", False),
            ],
            "explanation": "Britain's war debt prompted Parliament to tax the colonies -- sparking the 'no taxation without representation' crisis that eventually led to revolution.",
        },
        # --- Lesson 2: American Revolution & the New Nation ---
        {
            "text": "The Declaration of Independence (1776) stated that governments derive their 'just powers from the consent of the governed.' This means:",
            "difficulty": 2,
            "choices": [
                ("Government authority comes from the people it governs", True),
                ("Only wealthy landowners can grant power to a government", False),
                ("The British king had the right to tax the colonies", False),
                ("The military is the source of all governmental power", False),
            ],
            "explanation": "'Consent of the governed' is the principle of popular sovereignty -- legitimate government power flows from the people. It is one of the most tested phrases on the GED Social Studies exam.",
        },
        {
            "text": "Why was the Battle of Saratoga (1777) a turning point in the Revolutionary War?",
            "difficulty": 3,
            "choices": [
                ("It convinced France to enter the war as an American ally", True),
                ("It ended the war immediately with a British surrender", False),
                ("It was the first battle won by the Continental Army", False),
                ("It occurred in Britain, forcing Parliament to negotiate", False),
            ],
            "explanation": "The American victory at Saratoga persuaded France that the colonists could actually win, leading France to provide the crucial military and financial support that helped defeat Britain.",
        },
        {
            "text": "The Articles of Confederation were replaced by the Constitution mainly because the Articles:",
            "difficulty": 2,
            "choices": [
                ("Created a central government too weak to tax, enforce laws, or keep order", True),
                ("Gave the President too much power over the states", False),
                ("Did not mention individual rights or freedoms", False),
                ("Were written by the British and not truly American", False),
            ],
            "explanation": "Under the Articles, the Congress could not tax citizens directly, could not force states to follow federal law, and could not suppress domestic unrest like Shays' Rebellion -- weaknesses that made a stronger Constitution necessary.",
        },
        # --- Lesson 3: Expansion, Civil War ---
        {
            "text": "President Jefferson's Louisiana Purchase (1803) was historically significant mainly because it:",
            "difficulty": 2,
            "choices": [
                ("Roughly doubled the size of the United States by acquiring a vast territory from France", True),
                ("Gave the U.S. control of Florida from Spain", False),
                ("Settled the boundary between the U.S. and Canada permanently", False),
                ("Ended the War of 1812 and secured the Mississippi River", False),
            ],
            "explanation": "The Louisiana Purchase added approximately 828,000 square miles to the U.S. for about $15 million, opening the interior of the continent to American expansion and fueling Manifest Destiny.",
        },
        {
            "text": "The Emancipation Proclamation (January 1, 1863) declared that:",
            "difficulty": 2,
            "choices": [
                ("Enslaved people in Confederate states were free", True),
                ("Slavery was abolished throughout the entire United States immediately", False),
                ("All enslaved people would be freed after the war ended", False),
                ("The Confederate states would be readmitted to the Union if they freed enslaved people", False),
            ],
            "explanation": "The Proclamation applied only to Confederate (rebel) states, not to border states still in the Union. Slavery was fully abolished nationwide by the 13th Amendment in 1865.",
        },
        {
            "text": "Which compromise temporarily resolved the debate over slavery in new territories by drawing a geographic line at latitude 36°30'?",
            "difficulty": 3,
            "choices": [
                ("The Missouri Compromise of 1820", True),
                ("The Compromise of 1850", False),
                ("The Kansas-Nebraska Act of 1854", False),
                ("The Dred Scott decision of 1857", False),
            ],
            "explanation": "The Missouri Compromise (1820) admitted Missouri as a slave state and Maine as a free state, and drew a line across the Louisiana Territory -- slavery was permitted south of 36°30' and prohibited north of it.",
        },
        {
            "text": "The Civil War began in April 1861 when Confederate forces attacked:",
            "difficulty": 1,
            "choices": [
                ("Fort Sumter in South Carolina", True),
                ("Washington, D.C.", False),
                ("Gettysburg, Pennsylvania", False),
                ("Richmond, Virginia", False),
            ],
            "explanation": "Confederate artillery opened fire on the Union-held Fort Sumter on April 12, 1861, starting the Civil War. President Lincoln called it an act of rebellion and called for troops.",
        },
        # --- Lesson 4: Reconstruction & Gilded Age ---
        {
            "text": "The 14th Amendment (1868) was most important because it:",
            "difficulty": 2,
            "choices": [
                ("Granted citizenship and equal protection of the laws to all persons born in the U.S.", True),
                ("Abolished slavery throughout the United States", False),
                ("Gave African American men the right to vote", False),
                ("Ended Reconstruction and withdrew federal troops from the South", False),
            ],
            "explanation": "The 14th Amendment defined citizenship broadly and guaranteed equal protection -- a foundation for civil-rights law ever since. Abolishing slavery was the 13th, and voting rights for Black men were the 15th.",
        },
        {
            "text": "After Reconstruction ended in 1877, Southern states used which methods to prevent Black citizens from exercising their voting rights?",
            "difficulty": 2,
            "choices": [
                ("Poll taxes, literacy tests, and grandfather clauses", True),
                ("Arresting anyone who registered to vote", False),
                ("Repealing the 15th Amendment in Southern states", False),
                ("Requiring voters to own land", False),
            ],
            "explanation": "Although the 15th Amendment prohibited denying the vote based on race, Southern states used technically 'race-neutral' tools -- poll taxes, literacy tests, grandfather clauses, and violence -- to disenfranchise Black voters in practice.",
        },
        {
            "text": "During the Gilded Age (1870-1900), industrialists like John D. Rockefeller and Andrew Carnegie were sometimes called 'robber barons' because:",
            "difficulty": 2,
            "choices": [
                ("They used ruthless business practices to crush competition and accumulate vast wealth", True),
                ("They stole gold and silver from government treasuries", False),
                ("They supported labor unions and higher wages for workers", False),
                ("They were European nobles who owned American factories", False),
            ],
            "explanation": "Critics called these industrialists 'robber barons' because they used monopolistic practices, bribery, and brutal labor conditions to build fortunes, while workers and competitors suffered.",
        },
        # --- Lesson 5: Progressive Era, WWI, Great Depression ---
        {
            "text": "The 19th Amendment (1920) was the direct result of decades of effort by the:",
            "difficulty": 1,
            "choices": [
                ("Women's suffrage movement", True),
                ("Abolitionist movement", False),
                ("Labor union movement", False),
                ("Temperance movement", False),
            ],
            "explanation": "The 19th Amendment gave women the right to vote, the central goal of the women's suffrage movement led by activists such as Susan B. Anthony and Elizabeth Cady Stanton since the 1840s.",
        },
        {
            "text": "The United States entered World War I in 1917 primarily because of:",
            "difficulty": 2,
            "choices": [
                ("German submarine attacks on American ships and the Zimmermann Telegram", True),
                ("A direct military attack on U.S. territory by Germany", False),
                ("A request from Britain to honour a formal military alliance", False),
                ("The assassination of President Wilson", False),
            ],
            "explanation": "Germany's unrestricted submarine warfare sank American ships, and the Zimmermann Telegram revealed a German proposal for Mexico to attack the U.S. These events shifted public opinion and led Congress to declare war.",
        },
        {
            "text": "President Roosevelt's New Deal programs of the 1930s were designed primarily to:",
            "difficulty": 2,
            "choices": [
                ("Provide relief, recovery, and reform during the Great Depression", True),
                ("Prepare the United States for entry into World War II", False),
                ("Break up the industrial monopolies formed during the Gilded Age", False),
                ("Enforce Prohibition and eliminate the alcohol trade", False),
            ],
            "explanation": "The New Deal's three Rs -- Relief (immediate aid), Recovery (economic stimulus), and Reform (lasting regulations like Social Security and banking rules) -- were FDR's response to the Depression's mass unemployment and financial collapse.",
        },
        {
            "text": "What event triggered the Great Depression in the United States?",
            "difficulty": 1,
            "choices": [
                ("The stock market crash of October 1929", True),
                ("The start of World War I in 1914", False),
                ("A severe drought that destroyed American farmland", False),
                ("The assassination of President McKinley in 1901", False),
            ],
            "explanation": "The stock market crash of October 1929 wiped out billions in wealth, triggered bank failures, and set off a cascade of unemployment and economic collapse that became the Great Depression.",
        },
        # --- Lesson 6: WWII, Cold War, Civil Rights ---
        {
            "text": "What event directly caused the United States to enter World War II?",
            "difficulty": 1,
            "choices": [
                ("Japan's attack on Pearl Harbor on December 7, 1941", True),
                ("Germany's invasion of France in 1940", False),
                ("The sinking of the Lusitania in 1915", False),
                ("The signing of the Treaty of Versailles in 1919", False),
            ],
            "explanation": "Japan's surprise attack on the U.S. naval base at Pearl Harbor, Hawaii, killed more than 2,400 Americans. Congress declared war on Japan the next day, and Germany and Italy then declared war on the U.S.",
        },
        {
            "text": "The Cold War (roughly 1947-1991) was a conflict between the United States and the Soviet Union that was best described as:",
            "difficulty": 2,
            "choices": [
                ("An ideological and geopolitical struggle that avoided direct military combat between the two superpowers", True),
                ("A series of direct battles fought mainly in Europe", False),
                ("A trade war that resulted in economic collapse of both nations", False),
                ("A formal military alliance that broke down over nuclear weapons", False),
            ],
            "explanation": "The Cold War was defined by ideological competition, an arms race, and proxy wars -- but the U.S. and USSR never directly attacked each other, in part because both possessed nuclear weapons.",
        },
        {
            "text": "The Supreme Court's Brown v. Board of Education decision (1954) ruled that:",
            "difficulty": 2,
            "choices": [
                ("Racial segregation in public schools was unconstitutional", True),
                ("The Civil Rights Act of 1964 was unconstitutional", False),
                ("States could set their own policies on school integration", False),
                ("Affirmative action in university admissions was required by law", False),
            ],
            "explanation": "In Brown v. Board of Education, the Supreme Court unanimously overturned the 'separate but equal' doctrine established in Plessy v. Ferguson (1896), ruling that segregated schools violated the 14th Amendment's equal-protection clause.",
        },
        {
            "text": "The Civil Rights Act of 1964 most directly addressed discrimination by:",
            "difficulty": 2,
            "choices": [
                ("Banning discrimination based on race in public accommodations and employment", True),
                ("Granting African Americans the right to vote for the first time", False),
                ("Ending school segregation throughout the South", False),
                ("Establishing affirmative action programs in federal hiring", False),
            ],
            "explanation": "The Civil Rights Act of 1964 prohibited discrimination in hotels, restaurants, theatres, and employment on the basis of race, color, religion, sex, or national origin -- a landmark use of federal power.",
        },
        {
            "text": "Dr. Martin Luther King Jr.'s leadership of the Civil Rights Movement was most closely associated with which strategy?",
            "difficulty": 2,
            "choices": [
                ("Nonviolent civil disobedience and peaceful protest", True),
                ("Armed resistance against segregationist violence", False),
                ("Filing lawsuits in federal courts as the only tactic", False),
                ("Encouraging African Americans to emigrate to Africa", False),
            ],
            "explanation": "King drew on the philosophy of Mahatma Gandhi and his Christian faith to lead marches, boycotts, and sit-ins based on nonviolent resistance -- tactics that gained public sympathy and put moral pressure on the government.",
        },
        # --- Lesson 7: Modern America & Historical Sources ---
        {
            "text": "The Watergate scandal (1972-1974) was historically significant mainly because it:",
            "difficulty": 2,
            "choices": [
                ("Led to the first-ever resignation of a U.S. president", True),
                ("Resulted in the only impeachment conviction of a president", False),
                ("Caused the United States to withdraw from the Vietnam War", False),
                ("Exposed Soviet spying inside the White House", False),
            ],
            "explanation": "Facing almost certain impeachment after recordings revealed his role in covering up the Watergate break-in, President Nixon resigned on August 9, 1974 -- the only time a U.S. president has resigned.",
        },
        {
            "text": "A historian studying the Civil War reads a letter written by a Union soldier in 1863 and a textbook published in 2010. Which of these is a PRIMARY source?",
            "difficulty": 1,
            "choices": [
                ("The soldier's 1863 letter", True),
                ("The 2010 textbook", False),
                ("Both are primary sources", False),
                ("Neither is a primary source", False),
            ],
            "explanation": "A primary source is created during the time being studied. The 1863 letter was written by a participant in the war while it was happening. The 2010 textbook is a secondary source -- created later by someone analysing the war.",
        },
        {
            "text": "A political speech uses phrases like 'our cowardly enemies' and 'a glorious, righteous cause.' A careful reader should recognise that this language suggests the source:",
            "difficulty": 2,
            "choices": [
                ("Is intended to persuade and contains clear bias", True),
                ("Is a neutral, factual account of events", False),
                ("Is a primary source and therefore completely reliable", False),
                ("Can be trusted because it was written by a leader", False),
            ],
            "explanation": "Loaded emotional language ('cowardly,' 'glorious,' 'righteous') signals persuasive intent and bias. Even if it is a primary source, that does not make it objective -- it reflects the speaker's point of view.",
        },
        {
            "text": "Which of the following best describes the end of the Cold War?",
            "difficulty": 2,
            "choices": [
                ("The Soviet Union collapsed in 1991, ending the ideological conflict between the superpowers", True),
                ("The United States defeated the USSR in a major military conflict in 1991", False),
                ("A peace treaty signed in 1985 officially ended the Cold War", False),
                ("The Cold War ended when both nations agreed to dismantle all nuclear weapons", False),
            ],
            "explanation": "The Cold War ended not through military defeat or a formal treaty but through the internal collapse and dissolution of the Soviet Union in December 1991.",
        },
        {
            "text": "The September 11, 2001 terrorist attacks led most directly to:",
            "difficulty": 1,
            "choices": [
                ("U.S. military action in Afghanistan and a broad 'War on Terror'", True),
                ("A declaration of war against Iraq approved the same week", False),
                ("The end of the Cold War", False),
                ("The passage of the Civil Rights Act", False),
            ],
            "explanation": "After the 9/11 attacks, the U.S. invaded Afghanistan to destroy al-Qaeda and the Taliban government that sheltered them, beginning what the George W. Bush administration called the 'War on Terror.'",
        },
        {
            "text": "When reading a historical document, which question is MOST important for evaluating its reliability?",
            "difficulty": 2,
            "choices": [
                ("Who created the document, when, and for what purpose?", True),
                ("How long is the document and how many facts does it contain?", False),
                ("Whether the document agrees with your prior knowledge of the topic", False),
                ("Whether the document was published in a textbook", False),
            ],
            "explanation": "Evaluating a source requires understanding its author, time period, and purpose -- these factors reveal potential bias and limit what conclusions the source can support. Length and personal agreement are not indicators of reliability.",
        },
        {
            "text": "The phrase 'correlation is not causation' is most relevant when:",
            "difficulty": 3,
            "choices": [
                ("Two trends appear on a graph at the same time but one may not have caused the other", True),
                ("A primary source contradicts a secondary source on the same topic", False),
                ("A map shows two different countries side by side", False),
                ("A historical figure held both positive and negative views", False),
            ],
            "explanation": "Just because two trends happen at the same time (correlation) does not mean one caused the other (causation). This is a key data-interpretation principle the GED tests on graphs and tables.",
        },
    ],
}


class Command(BaseCommand):
    help = "Create the 'GED Social Studies: U.S. History' deep-dive course."

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
