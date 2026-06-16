"""
Seed data: 'GED Social Studies: Geography & the World'.

Covers the geography strand of the GED Social Studies test -- roughly 15 percent
of the exam. Seven lessons take students from the basics of map reading through
physical and human geography, world regions, human-environment interaction,
globalization, and GED-specific data-reading strategies.

Run:
    python manage.py seed_ged_geography
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED Social Studies: Geography & the World",
    "slug": "ged-geography-world",
    "program": "GED",
    "subject": "social",
    "description": (
        "Geography explains where things are, why they are there, and how place shapes human life. "
        "This course covers the tools geographers use, the physical and human forces that shape "
        "Earth's surface, the major world regions, the relationship between people and their "
        "environment, globalization, and the map and data-reading skills the GED Social Studies "
        "test specifically measures. No prior geography background required."
    ),
    "lessons": [
        (
            "1. Geographic Tools: Maps, Coordinates, and Scale",
            "Geography is the study of Earth's surface — its physical features, climates, peoples, "
            "and the connections among them. Geographers rely on a set of core tools to record and "
            "communicate this information.\n\n"
            "**Latitude and Longitude**\n\n"
            "Every location on Earth can be identified by two coordinates:\n\n"
            "- **Latitude** measures distance north or south of the **Equator** (0°). Lines of "
            "latitude run east-west and are called **parallels**. Values range from 0° at the "
            "Equator to 90°N (North Pole) or 90°S (South Pole).\n"
            "- **Longitude** measures distance east or west of the **Prime Meridian** (0°), which "
            "runs through Greenwich, England. Lines of longitude run north-south and are called "
            "**meridians**. Values range from 0° to 180°E or 180°W.\n\n"
            "Together a latitude-longitude pair pinpoints any spot on Earth. For example, New York "
            "City is approximately 41°N, 74°W.\n\n"
            "**Types of Maps**\n\n"
            "- **Political maps** show country and state boundaries, capitals, and major cities.\n"
            "- **Physical maps** show natural features: mountains, rivers, plains, and elevation "
            "using color (green for low, brown for high) or **contour lines** (lines connecting "
            "points of equal elevation).\n"
            "- **Thematic maps** highlight one specific topic, such as population density, rainfall, "
            "climate zones, or natural resources.\n"
            "- **Road maps** and **street maps** show transportation networks.\n\n"
            "**Map Scale**\n\n"
            "A **map scale** is the ratio between a distance on the map and the real distance on "
            "Earth. It can be shown as a **bar scale** (a drawn ruler), a **ratio** (1:100,000 "
            "means 1 cm on the map = 100,000 cm in reality), or a **verbal statement** "
            "('1 inch = 50 miles'). A **large-scale map** shows a small area in great detail "
            "(a city). A **small-scale map** shows a large area with less detail (a continent).\n\n"
            "**Map Projections**\n\n"
            "Because Earth is a sphere, any flat map distorts it. Common projections include the "
            "**Mercator** (useful for navigation but distorts size near the poles — making Greenland "
            "look as large as Africa) and the **Robinson** (a compromise that reduces all types of "
            "distortion moderately).\n\n"
            "**The Five Themes of Geography** organize geographic thinking:\n\n"
            "- **Location** (where?), **Place** (what is it like?), **Human-Environment "
            "Interaction** (how do people and environment affect each other?), **Movement** "
            "(how do people, goods, and ideas travel?), **Region** (what areas share "
            "characteristics?).\n\n"
            "⚠️ Common misconception: latitude is the east-west lines. In fact latitude lines run "
            "east-west but measure north-south distance from the Equator. It is easy to mix up "
            "which lines run which direction. Remember: lines of **lat**itude lie **flat** "
            "(horizontal).\n\n"
            "💡 Tip: On the GED, when reading a map always check the title, legend (key), compass "
            "rose, and scale before answering any question. These four elements tell you what the "
            "map shows and how to interpret it.",
        ),
        (
            "2. Physical Geography: Landforms, Climate, and Biomes",
            "**Physical geography** studies the natural features of Earth's surface — its shape, "
            "climate, and ecosystems.\n\n"
            "**Major Landforms**\n\n"
            "- **Mountains** — high, steep landforms formed by tectonic forces or volcanic activity. "
            "They influence climate by forcing air upward (which cools and drops rain on the "
            "windward side, leaving a dry **rain shadow** on the leeward side).\n"
            "- **Plains** — large, flat or gently rolling areas. Often fertile and heavily farmed "
            "(the Great Plains of North America; the North European Plain).\n"
            "- **Plateaus** — elevated flat areas, sometimes called 'tablelands' (the Tibetan "
            "Plateau, the Colorado Plateau).\n"
            "- **Valleys and River Basins** — low areas carved by rivers. Rivers deposit sediment "
            "to form **deltas** at their mouths, creating fertile land.\n"
            "- **Deserts** — areas receiving very little precipitation (less than 250 mm/year). "
            "Can be hot (Sahara) or cold (Gobi).\n\n"
            "**Climate**\n\n"
            "**Climate** is the long-term average of weather conditions (temperature, precipitation, "
            "wind) in a region. Key factors that determine climate:\n\n"
            "- **Latitude** — areas near the Equator receive direct sunlight year-round and are hot; "
            "polar regions receive indirect sunlight and are cold.\n"
            "- **Altitude** — higher elevations are cooler (approximately 6.5°C colder per 1,000 m "
            "gained).\n"
            "- **Proximity to water** — oceans moderate temperatures (coastal areas are neither "
            "very hot in summer nor very cold in winter); interiors have extreme seasonal swings.\n"
            "- **Ocean currents** — warm currents (Gulf Stream) warm nearby coastlines; cold "
            "currents cool them.\n"
            "- **Wind patterns** — global wind belts carry moisture or dry air.\n\n"
            "**Climate Zones** from Equator to poles: **Tropical** (hot, wet or wet-and-dry) → "
            "**Subtropical** (hot, often dry) → **Temperate** (moderate) → **Subarctic** "
            "(cold, short summers) → **Polar** (permanently cold).\n\n"
            "**Biomes**\n\n"
            "A **biome** is a large region defined by its climate, vegetation, and animal life:\n\n"
            "- **Tropical rainforest** — near the Equator; hot and wet year-round; highest "
            "biodiversity on Earth.\n"
            "- **Savanna** — tropical grassland with distinct wet and dry seasons (Africa, "
            "Brazil's cerrado).\n"
            "- **Desert** — hot or cold; very dry; sparse, drought-adapted vegetation.\n"
            "- **Temperate grassland** — moderate rainfall; fertile soils (prairies, steppes, "
            "pampas).\n"
            "- **Temperate deciduous forest** — four seasons; trees shed leaves in autumn "
            "(eastern North America, Europe).\n"
            "- **Boreal forest (Taiga)** — cold, long winters; coniferous trees (Canada, "
            "Russia, Scandinavia).\n"
            "- **Tundra** — very cold; permafrost; no trees; near the poles and on high mountains.\n\n"
            "**Natural Processes That Shape the Land**\n\n"
            "- **Tectonic plates** move slowly, building mountains (collision), creating rift "
            "valleys (spreading), and causing earthquakes and volcanoes.\n"
            "- **Erosion and deposition** by water, wind, and ice continuously reshape the surface.\n\n"
            "⚠️ Common misconception: deserts are always hot and sandy. Many deserts are cold "
            "(Antarctica is technically the world's largest desert — it receives less than 200 mm "
            "of precipitation per year). Desert is defined by low precipitation, not high "
            "temperature.\n\n"
            "💡 Tip: remember the pattern — moving away from the Equator, you generally move from "
            "tropical to temperate to polar, and from wet forest to grassland to desert (depending "
            "on rainfall) along each latitude band.",
        ),
        (
            "3. Human Geography: Population, Migration, and Culture",
            "**Human geography** studies where people live, why they live there, and how they "
            "organize their societies and spaces.\n\n"
            "**Population Patterns**\n\n"
            "The world's population is not spread evenly. **Population density** (people per "
            "square kilometer) is very high in:\n\n"
            "- River valleys and deltas (Nile, Ganges, Yangtze) — fertile soil and water supply.\n"
            "- Coastal and lowland areas — trade access, mild climate.\n"
            "- Industrial regions — job opportunities.\n\n"
            "Population density is very low in deserts, dense rainforests, high mountains, and "
            "polar regions — places that are too dry, too hot, too steep, or too cold to support "
            "large numbers of people.\n\n"
            "**Population Growth**\n\n"
            "The **demographic transition model** describes how countries move through stages as "
            "they develop:\n\n"
            "- **Stage 1** — high birth rates, high death rates → stable, small population.\n"
            "- **Stage 2** — high birth rates, falling death rates (better medicine/sanitation) → "
            "rapid population growth.\n"
            "- **Stage 3** — falling birth rates, low death rates → slower growth.\n"
            "- **Stage 4** — low birth rates, low death rates → stable or slowly growing population.\n\n"
            "**Migration**\n\n"
            "**Migration** is the movement of people from one place to another. Geographers "
            "distinguish:\n\n"
            "- **Push factors** — conditions that drive people away from a place: war, famine, "
            "poverty, persecution, environmental disaster.\n"
            "- **Pull factors** — conditions that attract people to a new place: economic "
            "opportunity, safety, family connections, better climate.\n"
            "- **Voluntary migration** — people choose to move for economic or personal reasons.\n"
            "- **Forced migration** — people are compelled to move (slavery, refugee crises).\n"
            "- **Internal migration** — movement within a country (rural to urban).\n"
            "- **International migration** — movement between countries.\n\n"
            "**Urbanization**\n\n"
            "**Urbanization** is the process by which an increasing share of a population lives "
            "in cities. Since 2007, more than half the world's population has lived in urban "
            "areas — a historic first. Rapid urbanization can strain housing, infrastructure, "
            "water, and sanitation in fast-growing cities, especially in developing nations.\n\n"
            "**Culture Regions**\n\n"
            "A **culture region** is an area whose people share a common language, religion, "
            "customs, or historical experience. Language families (Indo-European, Sino-Tibetan, "
            "Afro-Asiatic) and world religion distributions (Christianity, Islam, Hinduism, "
            "Buddhism) are major ways geographers define cultural regions.\n\n"
            "⚠️ Common misconception: urbanization only happens in wealthy countries. In reality, "
            "the most rapid urbanization today is occurring in Africa and Asia, where megacities "
            "(10+ million people) are growing fastest.\n\n"
            "💡 Tip: when a GED question asks why a particular area has a large population, look "
            "for a combination of physical advantages (fertile soil, river access, mild climate) "
            "and human factors (economic opportunity, historical settlement).",
        ),
        (
            "4. World Regions Overview",
            "The GED Social Studies test expects students to recognize basic facts about the "
            "world's major regions: their locations, physical features, and human characteristics.\n\n"
            "**North America**\n\n"
            "Includes Canada, the United States, and Mexico. Major physical features: Rocky "
            "Mountains (west), Appalachian Mountains (east), Mississippi River system, Great "
            "Plains, Great Lakes. Largely temperate climate. Among the world's wealthiest and "
            "most technologically advanced economies.\n\n"
            "**Latin America**\n\n"
            "Includes Mexico, Central America, the Caribbean, and South America. Major features: "
            "Andes Mountains (world's longest continental mountain range, running down western "
            "South America), Amazon Basin (world's largest tropical rainforest and river basin), "
            "Atacama Desert (one of the driest places on Earth). Predominantly Spanish- and "
            "Portuguese-speaking; largely Catholic. Economies range from emerging (Brazil, "
            "Mexico) to developing.\n\n"
            "**Europe**\n\n"
            "A relatively small continent with enormous historical influence. Features: Alps, "
            "Rhine and Danube river systems, Mediterranean coast (warm and dry), northern plains. "
            "High population density; highly urbanized; diverse languages but many in the "
            "Indo-European family. The **European Union (EU)** is a major political and economic "
            "bloc.\n\n"
            "**Africa**\n\n"
            "The second-largest continent and the one with the highest biodiversity. Major "
            "features: Sahara Desert (world's largest hot desert, covering North Africa), Nile "
            "River (world's longest), Congo Basin (Africa's largest rainforest), Rift Valley "
            "(eastern Africa, site of human evolutionary origins). Enormous linguistic diversity "
            "(over 2,000 languages). Many nations are developing economically but have rich "
            "natural resources.\n\n"
            "**Asia**\n\n"
            "The world's largest and most populous continent. Major features: Himalayas and "
            "Tibetan Plateau (highest in the world), Yangtze and Yellow Rivers (China), Ganges "
            "(India), Siberian Plains (Russia). Home to the two most populous countries: China "
            "and India (together over 2.8 billion people). Includes diverse climates from "
            "tropical (Southeast Asia) to desert (Central Asia) to subarctic (Siberia).\n\n"
            "**The Middle East**\n\n"
            "Generally defined as Southwest Asia and Northeast Africa. Largely arid; major rivers "
            "are the Tigris and Euphrates (Iraq) and the Nile (Egypt). Among the world's largest "
            "reserves of oil and natural gas (Persian Gulf region). Predominantly Arabic-speaking "
            "and Muslim, though Israel is Jewish-majority and Iran is Persian-speaking. "
            "Geopolitically significant due to energy resources and historical-religious sites.\n\n"
            "**Oceania**\n\n"
            "Includes Australia, New Zealand, Papua New Guinea, and the Pacific Island nations. "
            "Australia is the world's largest island and smallest continent; much of its interior "
            "is arid (Outback). The Pacific Islands are coral atolls and volcanic islands in the "
            "Pacific Ocean, many threatened by rising sea levels. English is widely spoken "
            "in Australia and New Zealand.\n\n"
            "⚠️ Common misconception: the Middle East is a continent. It is not — it is a "
            "geopolitical region that spans parts of Asia and Africa. Similarly, 'Latin America' "
            "is a cultural-linguistic region, not a continent.\n\n"
            "💡 Tip: for GED questions about world regions, focus on the most distinctive "
            "feature of each area — the Sahara for North Africa, the Amazon for South America, "
            "the Himalayas for South/Central Asia, and oil for the Middle East.",
        ),
        (
            "5. Human-Environment Interaction",
            "One of the five themes of geography, **human-environment interaction** examines "
            "the two-way relationship between people and the physical world they inhabit. "
            "People both **adapt to** and **modify** their environment, and those modifications "
            "often create new challenges.\n\n"
            "**How Environment Shapes Human Activity**\n\n"
            "- **Agriculture** depends on soil quality, rainfall, temperature, and growing "
            "season. The world's great early civilizations arose in river valleys "
            "(Nile, Tigris-Euphrates, Indus, Huang He) where annual flooding deposited "
            "rich silt.\n"
            "- **Settlement patterns** follow water: coastal cities, river towns, and lake "
            "communities all formed where water provided food, transportation, and drinking "
            "supply.\n"
            "- **Building styles** reflect climate: thick mud-brick walls in hot deserts "
            "retain cool air; steep roofs in snowy regions shed snow; stilted houses in "
            "flood-prone tropical areas stay above floodwaters.\n"
            "- **Trade routes** follow natural corridors: mountain passes, river valleys, "
            "and coastlines. The Silk Road crossed the gaps in the mountains of Central Asia; "
            "Atlantic trade relied on predictable wind patterns.\n\n"
            "**How Humans Modify the Environment**\n\n"
            "- **Deforestation** — clearing forests for agriculture and timber destroys habitat, "
            "increases erosion, and changes regional rainfall patterns.\n"
            "- **Irrigation** — diverting river water to dry farmland transformed deserts into "
            "farmland but can also cause soil salinization over time.\n"
            "- **Dams** — control flooding and generate hydroelectric power but disrupt river "
            "ecosystems and displace human communities upstream.\n"
            "- **Urbanization** — cities replace natural surfaces with concrete and asphalt, "
            "creating **urban heat islands** (cities are several degrees warmer than "
            "surrounding rural areas).\n"
            "- **Land reclamation** — countries like the Netherlands have reclaimed land "
            "from the sea using systems of dikes and pumps.\n"
            "- **Resource extraction** — mining, drilling, and quarrying permanently alter "
            "landscapes and can pollute water tables.\n\n"
            "**Environmental Consequences**\n\n"
            "Human modifications often trigger unintended consequences:\n\n"
            "- Overuse of irrigation in Central Asia helped shrink the Aral Sea from one of "
            "the world's four largest lakes to a fraction of its former size.\n"
            "- Draining wetlands removes natural flood control, making flooding worse "
            "downstream.\n"
            "- Burning fossil fuels that power modern civilization is the primary driver of "
            "climate change, which in turn alters precipitation patterns, raises sea levels, "
            "and intensifies storms.\n\n"
            "⚠️ Common misconception: only developing countries modify their environments "
            "significantly. Wealthy industrial nations have often made the largest-scale "
            "modifications — dams on the Colorado River, draining of the American Midwest's "
            "wetlands, massive highway networks.\n\n"
            "💡 Tip: GED questions on this topic often ask you to identify whether humans are "
            "adapting TO the environment (building with local materials, choosing flood-safe "
            "sites) or modifying IT (building a dam, clearing a forest). Both directions are "
            "tested.",
        ),
        (
            "6. Globalization and Economic Geography",
            "**Economic geography** asks: where are resources, industries, and economic "
            "activities located, and why? **Globalization** describes the increasing "
            "interconnection of the world's economies, cultures, and governments.\n\n"
            "**Natural Resources and Their Distribution**\n\n"
            "Resources are unevenly distributed around the world, which drives trade:\n\n"
            "- **Fossil fuels** (oil, coal, natural gas) are concentrated in the Middle East, "
            "Russia, North America, and parts of Africa.\n"
            "- **Minerals** (iron ore, copper, bauxite, rare earth elements) are concentrated in "
            "specific geologic zones (Sub-Saharan Africa, Australia, South America).\n"
            "- **Freshwater** is abundant in equatorial regions and the Northern Hemisphere but "
            "scarce in the Middle East and much of Africa.\n"
            "- **Fertile agricultural land** is concentrated in temperate zones with reliable "
            "rainfall or irrigation.\n\n"
            "**Trade and Interdependence**\n\n"
            "No nation is self-sufficient in all resources. Countries specialize in what they "
            "produce most efficiently (**comparative advantage**) and trade with others. "
            "Global supply chains mean that a single product — a smartphone, a car — may contain "
            "components manufactured in dozens of countries.\n\n"
            "**Development Levels**\n\n"
            "Geographers classify countries by development level:\n\n"
            "- **More developed (MDCs / 'Global North')** — high income, strong industry and "
            "services, high literacy and life expectancy (USA, Western Europe, Japan, Australia).\n"
            "- **Less developed (LDCs / 'Global South')** — lower average income, agriculture "
            "more dominant, ongoing challenges in education and healthcare (much of Sub-Saharan "
            "Africa, parts of Asia and Latin America).\n"
            "- **Newly industrializing countries (NICs)** — rapidly transitioning from "
            "agriculture to manufacturing and services (China, India, Brazil, Mexico, South Korea).\n\n"
            "**Consequences of Globalization**\n\n"
            "- **Benefits**: lower-cost goods, faster spread of technology and medicine, economic "
            "growth in developing nations, cultural exchange.\n"
            "- **Costs**: exploitation of low-wage workers, environmental degradation, erosion of "
            "local cultures, and vulnerability — when one part of a global supply chain breaks "
            "(pandemic, war), the whole system is disrupted.\n\n"
            "**Economic Sectors**\n\n"
            "- **Primary sector** — raw material extraction: farming, mining, fishing, logging.\n"
            "- **Secondary sector** — manufacturing: turning raw materials into products.\n"
            "- **Tertiary sector** — services: retail, healthcare, education, finance.\n"
            "- **Quaternary sector** — knowledge and information industries: research, technology, "
            "consulting.\n\n"
            "⚠️ Common misconception: free trade always benefits all countries equally. In "
            "practice, wealthier countries with more capital and technology often gain more, "
            "while poorer countries can get locked into exporting low-value raw materials.\n\n"
            "💡 Tip: when the GED shows a map or chart of trade flows, resource distribution, or "
            "GDP by country, look for the pattern of uneven distribution and ask which countries "
            "are buyers vs. sellers, producers vs. consumers.",
        ),
        (
            "7. Reading Maps, Charts, and Geographic Data on the GED",
            "The GED Social Studies test is heavily data-based. Many geography questions give "
            "you a map, bar chart, line graph, table, or infographic and ask you to read, "
            "compare, and draw conclusions from it. This lesson gives you a systematic strategy.\n\n"
            "**Reading a Map on the GED**\n\n"
            "Before answering any question about a map, check these four elements in order:\n\n"
            "- **Title** — what does the map show? (Political boundaries? Population density? "
            "Climate zones? Trade routes?)\n"
            "- **Legend/Key** — what do the colors, symbols, and shading mean? Never assume — "
            "always check.\n"
            "- **Compass rose or directional indicator** — which way is north?\n"
            "- **Scale** — what distance on Earth does an inch or centimeter on the map "
            "represent?\n\n"
            "**Types of GED Map Questions**\n\n"
            "- **Location questions**: identify a country, region, or city using coordinates "
            "or relative position ('north of the equator', 'west of the Andes').\n"
            "- **Comparison questions**: which region has the highest population density? "
            "Which area receives the most rainfall?\n"
            "- **Cause-and-effect questions**: why does this coastal region have a milder "
            "climate than the interior? (Ocean influence.)\n"
            "- **Inference questions**: based on the physical map, which area would most "
            "likely support large-scale agriculture?\n\n"
            "**Reading Charts and Graphs**\n\n"
            "- **Bar charts** compare discrete categories (population of world regions, "
            "CO₂ emissions by country). Read the axis labels and note the unit.\n"
            "- **Line graphs** show change over time (world population growth, temperature "
            "trends). Identify whether the trend is rising, falling, or stable, and note "
            "any sharp changes.\n"
            "- **Pie charts** show parts of a whole (% of world land by continent, % of "
            "energy from each source). Make sure percentages add to 100%.\n"
            "- **Tables** organize data in rows and columns. Read the column headers before "
            "the data.\n\n"
            "**Interpreting Geographic Data**\n\n"
            "- **Identify the trend**: is the value going up, down, or staying flat?\n"
            "- **Compare values**: which group is largest/smallest? By how much?\n"
            "- **Use proportional reasoning**: if the scale says 1 cm = 500 km, and two "
            "cities are 3 cm apart, they are 1,500 km apart.\n"
            "- **Correlation vs. causation**: two trends moving together does not prove "
            "one causes the other. Use your geographic knowledge to judge the relationship.\n\n"
            "**Common GED Question Traps**\n\n"
            "- Reading the wrong axis on a double-axis graph.\n"
            "- Confusing 'north of' with 'east of' when reading relative locations.\n"
            "- Choosing an answer that sounds geographically accurate but is not supported "
            "by the specific data shown.\n\n"
            "⚠️ Common misconception: a map without a scale is still accurate enough to "
            "measure distances by eye. Without a scale, you cannot determine real-world "
            "distances — maps can be drawn at any size or proportion.\n\n"
            "💡 Tip: the GED does not expect you to have memorized every world capital or "
            "border. What it tests is your ability to READ and INTERPRET geographic "
            "information presented to you — so practice working from the data rather "
            "than from memory.",
        ),
    ],
    "mcqs": [
        # ── Lesson 1: Geographic Tools ──────────────────────────────────────────
        {
            "text": "Lines of latitude on a globe run in which direction, and what do they measure?",
            "difficulty": 1,
            "choices": [
                ("They run east-west and measure distance north or south of the Equator.", True),
                ("They run north-south and measure distance east or west of the Prime Meridian.", False),
                ("They run east-west and measure distance east or west of the Prime Meridian.", False),
                ("They run north-south and measure distance north or south of the Equator.", False),
            ],
            "explanation": (
                "Lines of latitude (parallels) run east-west across the globe but measure how far north "
                "or south a location is from the Equator (0°). Lines of longitude (meridians) run "
                "north-south and measure east-west distance from the Prime Meridian."
            ),
        },
        {
            "text": "A thematic map showing population density by country is BEST used to answer which question?",
            "difficulty": 2,
            "choices": [
                ("Which countries have the most people per square kilometer?", True),
                ("What is the elevation of the Himalayan mountain range?", False),
                ("Which roads connect two major cities?", False),
                ("Where are the borders between European nations?", False),
            ],
            "explanation": (
                "Thematic maps highlight one specific topic — in this case, population density. They are "
                "ideal for comparing that variable across locations. Elevation is shown on physical maps, "
                "roads on road maps, and borders on political maps."
            ),
        },
        {
            "text": "A map has a scale of 1 cm = 200 km. If two cities are 4.5 cm apart on the map, what is the actual distance between them?",
            "difficulty": 2,
            "choices": [
                ("900 km", True),
                ("44.5 km", False),
                ("800 km", False),
                ("200 km", False),
            ],
            "explanation": (
                "Multiply the map distance by the scale factor: 4.5 cm × 200 km/cm = 900 km. "
                "This is a direct proportional reasoning problem — exactly the type the GED tests."
            ),
        },
        {
            "text": "The Mercator map projection is criticized in geography education primarily because it:",
            "difficulty": 2,
            "choices": [
                ("Greatly exaggerates the size of landmasses near the poles, making Greenland appear comparable in size to Africa.", True),
                ("Shows the world as a globe instead of a flat map.", False),
                ("Fails to show lines of latitude and longitude.", False),
                ("Is less useful for sea navigation than other projections.", False),
            ],
            "explanation": (
                "The Mercator projection distorts area near the poles. Greenland and Antarctica appear "
                "enormous, while equatorial Africa looks small relative to its true size. Africa is "
                "actually about 14 times larger than Greenland. The projection is excellent for "
                "navigation (straight lines = constant compass bearing) but misleads viewers about "
                "the relative sizes of countries."
            ),
        },
        # ── Lesson 2: Physical Geography ────────────────────────────────────────
        {
            "text": "A mountain range blocks moist air from the ocean. The dry area on the inland side of the mountain is called a:",
            "difficulty": 2,
            "choices": [
                ("Rain shadow", True),
                ("Plateau", False),
                ("Delta", False),
                ("Biome", False),
            ],
            "explanation": (
                "As moist air rises over a mountain range, it cools and drops its moisture as rain or snow "
                "on the windward (ocean-facing) side. The air descends dry on the leeward (inland) side, "
                "creating a rain shadow — an area of much lower precipitation. Many deserts, including the "
                "Atacama and the Great Basin, form in rain shadows."
            ),
        },
        {
            "text": "Which biome is characterized by permanently frozen subsoil, the absence of trees, and an extremely short growing season?",
            "difficulty": 2,
            "choices": [
                ("Tundra", True),
                ("Taiga (boreal forest)", False),
                ("Temperate grassland", False),
                ("Desert", False),
            ],
            "explanation": (
                "Tundra is found at high latitudes (Arctic) and at high elevations. Its defining "
                "features are permafrost (permanently frozen soil below the surface), no trees, and a "
                "very short summer growing season. The taiga has trees (conifers) and a longer summer; "
                "grasslands have moderate rainfall and no permafrost; deserts are defined by low precipitation."
            ),
        },
        {
            "text": "The world's most biodiverse terrestrial biome — home to more plant and animal species than any other — is the:",
            "difficulty": 1,
            "choices": [
                ("Tropical rainforest", True),
                ("Temperate deciduous forest", False),
                ("Coral reef", False),
                ("Savanna", False),
            ],
            "explanation": (
                "Tropical rainforests, concentrated near the Equator (Amazon Basin, Congo Basin, "
                "Southeast Asia), have year-round heat and abundant rainfall that support the highest "
                "species diversity of any land biome. Coral reefs are the marine equivalent but are "
                "aquatic, not terrestrial."
            ),
        },
        {
            "text": "Antarctica receives very little precipitation each year. Based on this information, Antarctica is technically classified as a:",
            "difficulty": 2,
            "choices": [
                ("Desert", True),
                ("Tundra", False),
                ("Polar ice cap with no biome classification", False),
                ("Taiga", False),
            ],
            "explanation": (
                "A desert is defined as any region receiving less than 250 mm (about 10 inches) of "
                "precipitation per year — regardless of temperature. Antarctica averages only about "
                "200 mm/year, making it the world's largest desert. This is a classic GED misconception "
                "trap: deserts are NOT defined by heat."
            ),
        },
        {
            "text": "The primary reason cities in equatorial regions (near 0° latitude) are generally hotter than cities at 60° north latitude is:",
            "difficulty": 2,
            "choices": [
                ("Sunlight strikes equatorial regions at a more direct angle, concentrating solar energy over a smaller area.", True),
                ("Equatorial regions are physically closer to the sun due to Earth's orbit.", False),
                ("Cities near the Equator have no wind to cool them.", False),
                ("Higher latitudes receive more hours of daylight in summer.", False),
            ],
            "explanation": (
                "The sun's rays hit equatorial regions nearly straight on (90°), concentrating energy "
                "over a small surface area. At high latitudes, the same energy spreads over a larger "
                "area at an oblique angle, producing less heat per square meter. The distance to the "
                "sun changes very little between latitudes and is not the cause."
            ),
        },

        # ── Lesson 3: Human Geography ───────────────────────────────────────────
        {
            "text": "A farmer in Bangladesh moves to a city after seasonal flooding regularly destroys crops. This is an example of:",
            "difficulty": 2,
            "choices": [
                ("A push factor causing internal migration from rural to urban areas.", True),
                ("A pull factor attracting migrants to rural areas.", False),
                ("Forced migration resulting from political persecution.", False),
                ("Stage 1 of the demographic transition model.", False),
            ],
            "explanation": (
                "A push factor is something that drives people away from their current location. "
                "Recurrent flooding that destroys livelihoods is a push factor. Moving from a "
                "rural area to a city within the same country is internal migration. "
                "Pull factors attract people to new places; political persecution describes "
                "a different type of forced migration."
            ),
        },
        {
            "text": "In the demographic transition model, which stage produces the FASTEST population growth?",
            "difficulty": 2,
            "choices": [
                ("Stage 2: high birth rates combined with rapidly falling death rates.", True),
                ("Stage 1: both birth rates and death rates are high.", False),
                ("Stage 3: birth rates begin to fall.", False),
                ("Stage 4: both birth rates and death rates are low.", False),
            ],
            "explanation": (
                "Population grows fastest in Stage 2, when improvements in medicine, sanitation, and "
                "food supply sharply reduce death rates while birth rates remain high. The gap between "
                "birth and death rates is at its widest, producing rapid natural increase. In Stages 1 "
                "and 4, both rates are similar, so growth is slow or stable."
            ),
        },
        {
            "text": "Which physical geographic feature most consistently explains why the ancient civilizations of Egypt, Mesopotamia, and China all developed near rivers?",
            "difficulty": 2,
            "choices": [
                ("Rivers provided fertile soil from annual flooding, reliable water for irrigation, and transportation routes.", True),
                ("Rivers marked natural borders that protected civilizations from invasion.", False),
                ("Civilizations avoided coastal areas due to flooding risk and preferred rivers for safety.", False),
                ("Rivers provided a source of stone for building construction.", False),
            ],
            "explanation": (
                "The three factors — fertile alluvial soil, irrigation water, and transportation — "
                "explain why virtually every early civilization emerged in a river valley. These "
                "advantages directly supported surplus agriculture, which freed people to specialize "
                "in crafts, trade, and governance."
            ),
        },
        {
            "text": "Areas with VERY LOW population density are most likely characterized by:",
            "difficulty": 1,
            "choices": [
                ("Extreme environments: deserts, dense rainforests, high mountains, or polar regions.", True),
                ("High industrial output and strong transportation infrastructure.", False),
                ("Proximity to major ocean ports and river systems.", False),
                ("Fertile plains with a long agricultural growing season.", False),
            ],
            "explanation": (
                "Low population density is strongly associated with environments that are hostile to "
                "large-scale human settlement: too dry (deserts), too cold (polar regions), too steep "
                "(mountains), or too dense and disease-prone (some rainforests). The other options all "
                "describe conditions that support high population density."
            ),
        },
        # ── Lesson 4: World Regions ──────────────────────────────────────────────
        {
            "text": "The Amazon Basin, home to the world's largest tropical rainforest, is located in:",
            "difficulty": 1,
            "choices": [
                ("South America", True),
                ("Sub-Saharan Africa", False),
                ("Southeast Asia", False),
                ("Central America", False),
            ],
            "explanation": (
                "The Amazon River and its surrounding rainforest basin are centered in Brazil and "
                "extend into neighboring South American countries (Peru, Colombia, Venezuela). "
                "The Congo Basin contains Africa's largest rainforest; Southeast Asia has extensive "
                "tropical forests but not the Amazon."
            ),
        },
        {
            "text": "The Persian Gulf region of the Middle East is globally significant primarily because of its:",
            "difficulty": 1,
            "choices": [
                ("Enormous reserves of oil and natural gas.", True),
                ("High population density and agricultural output.", False),
                ("Location at the center of global sea trade routes.", False),
                ("Large freshwater lakes and rivers.", False),
            ],
            "explanation": (
                "The Persian Gulf states (Saudi Arabia, UAE, Kuwait, Iraq, Iran) hold among the "
                "world's largest proven reserves of crude oil and natural gas. This resource "
                "wealth makes the region geopolitically critical, though it is one of the world's "
                "most arid regions with limited freshwater and agricultural capacity."
            ),
        },
        {
            "text": "Which of the following CORRECTLY matches a world region with its most famous geographic feature?",
            "difficulty": 2,
            "choices": [
                ("North Africa — the Sahara Desert, the world's largest hot desert.", True),
                ("South America — the Rocky Mountains, stretching along the western coast.", False),
                ("Southeast Asia — the Tibetan Plateau, the world's highest plateau.", False),
                ("Europe — the Andes Mountains, separating the continent's interior.", False),
            ],
            "explanation": (
                "The Sahara covers most of North Africa and is the world's largest hot desert. "
                "South America's western mountain range is the Andes (not the Rockies, which are "
                "in North America). The Tibetan Plateau and Himalayas are in South/Central Asia. "
                "Europe's major mountain range in the south is the Alps."
            ),
        },
        {
            "text": "The Pacific Island nations of Oceania face a unique geographic threat that most other world regions do not. That threat is:",
            "difficulty": 2,
            "choices": [
                ("Rising sea levels from climate change that may permanently submerge low-lying atolls.", True),
                ("Desertification spreading from the Australian Outback toward the Pacific Islands.", False),
                ("Extreme cold and permafrost affecting agricultural potential.", False),
                ("Deforestation of the world's largest temperate rainforests.", False),
            ],
            "explanation": (
                "Many Pacific Island nations (Tuvalu, Kiribati, Marshall Islands) are coral atolls "
                "that barely rise above sea level. Even modest increases in ocean levels from melting "
                "ice and thermal expansion threaten to flood them permanently. This makes them among "
                "the most climate-vulnerable places on Earth."
            ),
        },

        # ── Lesson 5: Human-Environment Interaction ─────────────────────────────
        {
            "text": "Early human civilizations most commonly developed in river valleys rather than on mountain plateaus primarily because river valleys offered:",
            "difficulty": 2,
            "choices": [
                ("Fertile soil from river deposits, reliable water, and flat land suitable for farming.", True),
                ("Natural defense from mountain barriers on all sides.", False),
                ("Easy access to timber and building stone from nearby mountains.", False),
                ("Cooler temperatures that prevented the spread of tropical diseases.", False),
            ],
            "explanation": (
                "Annual river flooding deposits rich alluvial silt, creating highly fertile soil. "
                "Flat valley floors are easy to farm, and the river itself provides irrigation water "
                "and a transportation corridor. These combined advantages made river valleys the "
                "cradles of agriculture and civilization."
            ),
        },
        {
            "text": "The Aral Sea in Central Asia shrank dramatically during the twentieth century. Which human activity was the PRIMARY cause?",
            "difficulty": 2,
            "choices": [
                ("Large-scale irrigation projects diverted the rivers that fed the sea.", True),
                ("Volcanic activity raised the lake bed, reducing its depth.", False),
                ("Global warming evaporated the sea's surface water.", False),
                ("Mining operations drained underground water into the sea floor.", False),
            ],
            "explanation": (
                "Soviet irrigation projects beginning in the 1960s diverted the Amu Darya and Syr Darya "
                "rivers — the Aral Sea's main water sources — to grow cotton in the surrounding desert. "
                "Without inflow, the sea shrank to about 10% of its original volume by the 2000s, "
                "leaving behind salt flats and a collapsed fishing industry."
            ),
        },
        {
            "text": "An urban heat island occurs when:",
            "difficulty": 2,
            "choices": [
                ("Cities are significantly warmer than surrounding rural areas because concrete and asphalt absorb and retain heat.", True),
                ("Factories in cities release greenhouse gases that heat only the surrounding city blocks.", False),
                ("High buildings block wind and trap cold air, making city centers colder than suburbs.", False),
                ("Urban areas are closer to the Equator than rural areas, receiving more direct sunlight.", False),
            ],
            "explanation": (
                "Dark paved surfaces and buildings absorb more solar radiation than vegetation and "
                "soil, and they release this heat slowly at night. Reduced vegetation means less "
                "evaporative cooling. Cities typically run 1-3°C warmer than nearby rural areas, "
                "a phenomenon called the urban heat island effect."
            ),
        },
        {
            "text": "Which pair correctly identifies one way people ADAPT to their environment and one way they MODIFY it?",
            "difficulty": 2,
            "choices": [
                ("Adapt: building steep-roofed homes in snowy regions; Modify: constructing a dam to control river flooding.", True),
                ("Adapt: irrigating desert farmland; Modify: building homes with thick walls in hot climates.", False),
                ("Adapt: drilling for oil; Modify: planting drought-resistant crops.", False),
                ("Adapt: constructing a highway through a mountain; Modify: wearing warm clothing in cold weather.", False),
            ],
            "explanation": (
                "Adaptation means adjusting human behavior or design to suit the environment "
                "(steep roofs shed snow). Modification means changing the environment itself "
                "(building a dam changes the river). Irrigating a desert modifies the land; "
                "wearing warm clothes adapts behavior to cold — not the other way around."
            ),
        },

        # ── Lesson 6: Globalization and Economic Geography ───────────────────────
        {
            "text": "The primary reason countries engage in international trade is that:",
            "difficulty": 1,
            "choices": [
                ("Natural resources and production advantages are unevenly distributed, so countries can benefit by specializing and exchanging goods.", True),
                ("International law requires all countries to trade with their neighbors.", False),
                ("Trade is the only way to obtain freshwater and food.", False),
                ("Countries trade to spread their language and culture to other nations.", False),
            ],
            "explanation": (
                "No country has every resource and production capability equally. Comparative advantage "
                "means countries produce what they are relatively most efficient at making, then trade "
                "for everything else. This specialization raises total output and lowers prices globally."
            ),
        },
        {
            "text": "A country where most workers are employed in agriculture, income levels are low, and literacy rates are improving but still below the global average is BEST classified as:",
            "difficulty": 2,
            "choices": [
                ("A less developed country (LDC).", True),
                ("A more developed country (MDC).", False),
                ("A newly industrializing country (NIC).", False),
                ("A post-industrial economy.", False),
            ],
            "explanation": (
                "Less developed countries (LDCs) are characterized by high dependence on agriculture, "
                "lower per-capita income, and developing education and health systems. MDCs have "
                "service-dominant economies and high incomes. NICs are transitioning rapidly from "
                "agriculture to manufacturing, typically showing faster GDP growth than LDCs."
            ),
        },
        {
            "text": "A factory worker in Vietnam assembles electronics using components shipped from South Korea, Japan, and China, and the finished phones are sold in the United States and Europe. This scenario BEST illustrates:",
            "difficulty": 2,
            "choices": [
                ("A global supply chain and economic interdependence among nations.", True),
                ("A self-sufficient national economy.", False),
                ("The primary economic sector dominating a developing country.", False),
                ("Mercantilism, in which countries avoid importing foreign goods.", False),
            ],
            "explanation": (
                "When production is distributed across multiple countries — with each contributing "
                "components, labor, or markets — this is a global supply chain, a defining feature "
                "of modern globalization and economic interdependence. No single country in this "
                "example is self-sufficient."
            ),
        },
        {
            "text": "Teaching in a university, providing financial advisory services, and conducting scientific research all belong to which economic sector?",
            "difficulty": 2,
            "choices": [
                ("Tertiary and quaternary sectors (services and knowledge industries).", True),
                ("Primary sector (raw material extraction).", False),
                ("Secondary sector (manufacturing).", False),
                ("Agricultural sector (food production).", False),
            ],
            "explanation": (
                "The tertiary sector covers services (education, healthcare, retail, finance), and the "
                "quaternary sector covers knowledge and information industries (research, technology, "
                "consulting). Teaching and research fit the quaternary; financial advising fits the "
                "tertiary. Both are distinct from the primary (extraction) and secondary "
                "(manufacturing) sectors."
            ),
        },
        # ── Lesson 7: Reading Maps, Charts, and Geographic Data ──────────────────
        {
            "text": "When beginning to answer a question about an unfamiliar map on the GED, what should you check FIRST?",
            "difficulty": 1,
            "choices": [
                ("The map title and legend (key) to determine what the map shows and what the symbols mean.", True),
                ("The names of the largest countries on the map.", False),
                ("Whether the map is a physical map or a political map by looking at its colors.", False),
                ("The scale bar to calculate the distance between every labeled city.", False),
            ],
            "explanation": (
                "The title tells you the map's topic; the legend defines every symbol, color, and "
                "shading pattern. Without these, any interpretation is guesswork. Always orient "
                "yourself with the title and legend before reading any specific feature of the map."
            ),
        },
        {
            "text": "A bar chart compares annual CO₂ emissions (in metric tons) for six countries. Country A has a bar reaching 5,000 and Country D has a bar reaching 1,250. Country A's emissions are how many times greater than Country D's?",
            "difficulty": 2,
            "choices": [
                ("4 times greater", True),
                ("3 times greater", False),
                ("3,750 times greater", False),
                ("10 times greater", False),
            ],
            "explanation": (
                "Divide Country A's value by Country D's: 5,000 ÷ 1,250 = 4. Country A emits "
                "exactly four times as much CO₂ as Country D. The difference (3,750) is how much "
                "more, not how many times more — a common mix-up on comparison questions."
            ),
        },
        {
            "text": "A line graph shows world population rising steeply from 1950 to 2000, then continuing to rise but more gradually. The BEST description of the trend is:",
            "difficulty": 2,
            "choices": [
                ("Population is still growing but the rate of growth has slowed.", True),
                ("Population peaked in 2000 and is now declining.", False),
                ("Population growth was slow from 1950 to 2000 and has since accelerated.", False),
                ("Population has remained stable since 2000.", False),
            ],
            "explanation": (
                "A steep slope indicates fast growth; a gentler upward slope after 2000 means "
                "growth continues but at a slower rate — population is still rising, just less "
                "rapidly. A decline would be shown by a downward slope; stability by a flat line."
            ),
        },
        {
            "text": "A map shows shading from light to dark, where darker shading represents higher population density. A student concludes that the darkest region on the map is the most important economic region in the world. This conclusion is:",
            "difficulty": 3,
            "choices": [
                ("Not supported by the map, which shows population density, not economic importance.", True),
                ("Correct because high population density always indicates high economic output.", False),
                ("Supported because the map legend mentions economic zones.", False),
                ("Correct because the GED always uses dark shading to indicate wealth.", False),
            ],
            "explanation": (
                "The map shows population density — the number of people per unit area. High "
                "population density does not necessarily mean high economic output; some of the "
                "world's most densely populated areas are among its poorest. The student's conclusion "
                "goes beyond what the data shows. Always base your answer only on what the "
                "specific source actually presents."
            ),
        },
        {
            "text": "On a GED map question, a city is described as located 'at approximately 35°N, 139°E'. Based on these coordinates alone, the city is:",
            "difficulty": 2,
            "choices": [
                ("North of the Equator and east of the Prime Meridian.", True),
                ("South of the Equator and west of the Prime Meridian.", False),
                ("North of the Equator and west of the Prime Meridian.", False),
                ("South of the Equator and east of the Prime Meridian.", False),
            ],
            "explanation": (
                "The 'N' in 35°N means 35 degrees north of the Equator. The 'E' in 139°E means "
                "139 degrees east of the Prime Meridian. (These coordinates correspond to Tokyo, "
                "Japan.) North latitude = above the Equator; East longitude = right (east) of the "
                "Prime Meridian on a standard map."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed GED Social Studies: Geography & the World course"

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

        lesson_count = len(COURSE["lessons"])
        question_count = len(COURSE["mcqs"])
        self.stdout.write(
            self.style.SUCCESS(
                f"Created '{course.title}' with {lesson_count} lessons and {question_count} questions."
            )
        )
