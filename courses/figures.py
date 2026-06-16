"""
Reusable, self-contained SVG charts for lesson content.

These are referenced from lesson text with a token like:

    [[figure:bar_toppings]]
    [[figure:bar_toppings|An optional caption]]

The richtext template filter looks the name up here and injects the SVG
verbatim (the SVG is trusted, author-controlled content, not user input).
SVG is used instead of image files so the charts are crisp at any size,
need no external hosting, and work offline.
"""

_FONT = "font-family:system-ui,-apple-system,Segoe UI,sans-serif"
_BLUE = "#2563eb"
_GRID = "#e5e7eb"
_AXIS = "#9ca3af"
_INK = "#1a1a1a"
_RED = "#dc2626"


# --- Bar graph: comparing separate categories ------------------------------
_BAR_TOPPINGS = f'''
<svg viewBox="0 0 340 240" role="img" aria-label="Bar graph of pizza toppings chosen by 20 students" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="175" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Pizza Toppings Chosen (20 students)</text>
  <line x1="50" y1="20" x2="50" y2="200" stroke="{_AXIS}"/>
  <line x1="50" y1="200" x2="320" y2="200" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="50" y1="164" x2="320" y2="164" stroke="{_GRID}"/><text x="44" y="167">2</text>
    <line x1="50" y1="128" x2="320" y2="128" stroke="{_GRID}"/><text x="44" y="131">4</text>
    <line x1="50" y1="92"  x2="320" y2="92"  stroke="{_GRID}"/><text x="44" y="95">6</text>
    <line x1="50" y1="56"  x2="320" y2="56"  stroke="{_GRID}"/><text x="44" y="59">8</text>
    <line x1="50" y1="20"  x2="320" y2="20"  stroke="{_GRID}"/><text x="44" y="23">10</text>
    <text x="44" y="204">0</text>
  </g>
  <g fill="{_BLUE}">
    <rect x="66"  y="56"  width="38" height="144"/>
    <rect x="131" y="92"  width="38" height="108"/>
    <rect x="196" y="128" width="38" height="72"/>
    <rect x="261" y="164" width="38" height="36"/>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle" font-weight="700">
    <text x="85" y="50">8</text><text x="150" y="86">6</text><text x="215" y="122">4</text><text x="280" y="158">2</text>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="85" y="216">Cheese</text><text x="150" y="216">Pepp.</text><text x="215" y="216">Veggie</text><text x="280" y="216">Other</text>
  </g>
</svg>'''


# --- Line graph: change over time ------------------------------------------
_LINE_SALES = f'''
<svg viewBox="0 0 340 240" role="img" aria-label="Line graph of monthly sales rising over time" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="175" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Monthly Sales ($)</text>
  <line x1="50" y1="20" x2="50" y2="200" stroke="{_AXIS}"/>
  <line x1="50" y1="200" x2="320" y2="200" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="50" y1="164" x2="320" y2="164" stroke="{_GRID}"/><text x="44" y="167">100</text>
    <line x1="50" y1="128" x2="320" y2="128" stroke="{_GRID}"/><text x="44" y="131">200</text>
    <line x1="50" y1="92"  x2="320" y2="92"  stroke="{_GRID}"/><text x="44" y="95">300</text>
    <line x1="50" y1="56"  x2="320" y2="56"  stroke="{_GRID}"/><text x="44" y="59">400</text>
    <line x1="50" y1="20"  x2="320" y2="20"  stroke="{_GRID}"/><text x="44" y="23">500</text>
    <text x="44" y="204">0</text>
  </g>
  <polyline points="70,128 130,74 190,92 250,56 310,38" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <g fill="{_BLUE}">
    <circle cx="70" cy="128" r="4"/><circle cx="130" cy="74" r="4"/><circle cx="190" cy="92" r="4"/>
    <circle cx="250" cy="56" r="4"/><circle cx="310" cy="38" r="4"/>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="70" y="216">Jan</text><text x="130" y="216">Feb</text><text x="190" y="216">Mar</text>
    <text x="250" y="216">Apr</text><text x="310" y="216">May</text>
  </g>
</svg>'''


# --- Bar chart of a small data set, with the mean marked -------------------
_MEAN_BARS = f'''
<svg viewBox="0 0 340 230" role="img" aria-label="Bar chart of the values 4, 8, 6, 2 with the mean of 5 marked" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="175" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Data set: 4, 8, 6, 2  (mean = 5)</text>
  <line x1="50" y1="30" x2="50" y2="190" stroke="{_AXIS}"/>
  <line x1="50" y1="190" x2="320" y2="190" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="50" y1="150" x2="320" y2="150" stroke="{_GRID}"/><text x="44" y="153">2</text>
    <line x1="50" y1="110" x2="320" y2="110" stroke="{_GRID}"/><text x="44" y="113">4</text>
    <line x1="50" y1="70"  x2="320" y2="70"  stroke="{_GRID}"/><text x="44" y="73">6</text>
    <line x1="50" y1="30"  x2="320" y2="30"  stroke="{_GRID}"/><text x="44" y="33">8</text>
    <text x="44" y="194">0</text>
  </g>
  <g fill="{_BLUE}">
    <rect x="66"  y="110" width="38" height="80"/>
    <rect x="131" y="30"  width="38" height="160"/>
    <rect x="196" y="70"  width="38" height="120"/>
    <rect x="261" y="150" width="38" height="40"/>
  </g>
  <line x1="50" y1="90" x2="320" y2="90" stroke="{_RED}" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="318" y="84" text-anchor="end" font-size="11" font-weight="700" fill="{_RED}">mean = 5</text>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="85" y="205">4</text><text x="150" y="205">8</text><text x="215" y="205">6</text><text x="280" y="205">2</text>
  </g>
</svg>'''


# --- Probability scale from 0 to 1 -----------------------------------------
_PROB_SCALE = f'''
<svg viewBox="0 0 340 130" role="img" aria-label="Probability scale from 0 impossible to 1 certain" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="170" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Probability Scale</text>
  <line x1="30" y1="70" x2="310" y2="70" stroke="{_AXIS}" stroke-width="2"/>
  <g stroke="{_AXIS}">
    <line x1="30"  y1="62" x2="30"  y2="78"/>
    <line x1="100" y1="65" x2="100" y2="75"/>
    <line x1="170" y1="62" x2="170" y2="78"/>
    <line x1="240" y1="65" x2="240" y2="75"/>
    <line x1="310" y1="62" x2="310" y2="78"/>
  </g>
  <circle cx="170" cy="70" r="6" fill="{_BLUE}"/>
  <text x="170" y="44" text-anchor="middle" font-size="11" font-weight="700" fill="{_BLUE}">P(even) = ½</text>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="30"  y="94" font-weight="700">0</text><text x="170" y="94" font-weight="700">½</text><text x="310" y="94" font-weight="700">1</text>
  </g>
  <g font-size="10" fill="#6b7280" text-anchor="middle">
    <text x="30"  y="108">Impossible</text><text x="170" y="108">Even chance</text><text x="310" y="108">Certain</text>
  </g>
</svg>'''


# --- Tree diagram: two coin flips ------------------------------------------
_COIN_TREE = f'''
<svg viewBox="0 0 340 240" role="img" aria-label="Tree diagram of two coin flips with four equally likely outcomes" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="170" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Two Coin Flips</text>
  <g stroke="{_AXIS}" stroke-width="1.5">
    <line x1="40" y1="120" x2="135" y2="75"/>
    <line x1="40" y1="120" x2="135" y2="175"/>
    <line x1="160" y1="75"  x2="255" y2="48"/>
    <line x1="160" y1="75"  x2="255" y2="105"/>
    <line x1="160" y1="175" x2="255" y2="150"/>
    <line x1="160" y1="175" x2="255" y2="207"/>
  </g>
  <g font-size="10" fill="#6b7280">
    <text x="78" y="90">½</text><text x="78" y="158">½</text>
    <text x="200" y="55">½</text><text x="200" y="98">½</text><text x="200" y="148">½</text><text x="200" y="200">½</text>
  </g>
  <g fill="{_BLUE}">
    <circle cx="40" cy="120" r="5"/>
    <circle cx="147" cy="75" r="13"/><circle cx="147" cy="175" r="13"/>
  </g>
  <g font-size="12" fill="#ffffff" text-anchor="middle" font-weight="700">
    <text x="147" y="79">H</text><text x="147" y="179">T</text>
  </g>
  <g font-size="11" fill="{_INK}" font-weight="700">
    <text x="268" y="52">HH = ¼</text><text x="268" y="109">HT = ¼</text>
    <text x="268" y="154">TH = ¼</text><text x="268" y="211">TT = ¼</text>
  </g>
  <text x="40" y="108" text-anchor="middle" font-size="10" fill="#6b7280">start</text>
</svg>'''


# --- Dot plot: quiz scores -------------------------------------------------
_DOT_PLOT_SCORES = f'''
<svg viewBox="0 0 420 210" role="img" aria-label="Dot plot of quiz scores from 60 to 100" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="18" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Quiz Scores Dot Plot</text>
  <line x1="50" y1="160" x2="370" y2="160" stroke="{_AXIS}" stroke-width="1.5"/>
  <g stroke="{_AXIS}">
    <line x1="50" y1="154" x2="50" y2="166"/><line x1="90" y1="154" x2="90" y2="166"/>
    <line x1="130" y1="154" x2="130" y2="166"/><line x1="170" y1="154" x2="170" y2="166"/>
    <line x1="210" y1="154" x2="210" y2="166"/><line x1="250" y1="154" x2="250" y2="166"/>
    <line x1="290" y1="154" x2="290" y2="166"/><line x1="330" y1="154" x2="330" y2="166"/>
    <line x1="370" y1="154" x2="370" y2="166"/>
  </g>
  <g font-size="10.5" fill="{_INK}" text-anchor="middle">
    <text x="50" y="184">60</text><text x="90" y="184">65</text><text x="130" y="184">70</text><text x="170" y="184">75</text>
    <text x="210" y="184">80</text><text x="250" y="184">85</text><text x="290" y="184">90</text><text x="330" y="184">95</text><text x="370" y="184">100</text>
  </g>
  <g fill="{_BLUE}">
    <circle cx="130" cy="145" r="5"/><circle cx="170" cy="145" r="5"/><circle cx="170" cy="132" r="5"/>
    <circle cx="210" cy="145" r="5"/><circle cx="210" cy="132" r="5"/><circle cx="210" cy="119" r="5"/>
    <circle cx="250" cy="145" r="5"/><circle cx="290" cy="145" r="5"/><circle cx="290" cy="132" r="5"/>
    <circle cx="330" cy="145" r="5"/>
  </g>
  <text x="210" y="202" text-anchor="middle" font-size="10.5" fill="#6b7280">Each dot is one student; stacked dots show repeated values.</text>
</svg>'''


# --- Histogram: commute times ---------------------------------------------
_HISTOGRAM_COMMUTE = f'''
<svg viewBox="0 0 420 250" role="img" aria-label="Histogram of commute times grouped into intervals" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="18" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Commute Times Histogram</text>
  <line x1="55" y1="30" x2="55" y2="200" stroke="{_AXIS}"/>
  <line x1="55" y1="200" x2="385" y2="200" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="55" y1="166" x2="385" y2="166" stroke="{_GRID}"/><text x="48" y="169">2</text>
    <line x1="55" y1="132" x2="385" y2="132" stroke="{_GRID}"/><text x="48" y="135">4</text>
    <line x1="55" y1="98" x2="385" y2="98" stroke="{_GRID}"/><text x="48" y="101">6</text>
    <line x1="55" y1="64" x2="385" y2="64" stroke="{_GRID}"/><text x="48" y="67">8</text>
    <line x1="55" y1="30" x2="385" y2="30" stroke="{_GRID}"/><text x="48" y="33">10</text>
    <text x="48" y="204">0</text>
  </g>
  <g fill="{_BLUE}" stroke="#1d4ed8">
    <rect x="70" y="149" width="58" height="51"/>
    <rect x="128" y="81" width="58" height="119"/>
    <rect x="186" y="47" width="58" height="153"/>
    <rect x="244" y="115" width="58" height="85"/>
    <rect x="302" y="166" width="58" height="34"/>
  </g>
  <g font-size="10.5" fill="{_INK}" text-anchor="middle">
    <text x="99" y="219">0-9</text><text x="157" y="219">10-19</text><text x="215" y="219">20-29</text>
    <text x="273" y="219">30-39</text><text x="331" y="219">40-49</text>
  </g>
  <text x="210" y="240" text-anchor="middle" font-size="10.5" fill="#6b7280">Bars touch because the intervals are continuous ranges of time.</text>
</svg>'''


# --- Two-way table: study plan and quiz result -----------------------------
_TWO_WAY_TABLE = f'''
<svg viewBox="0 0 440 230" role="img" aria-label="Two-way table comparing study plan completion and quiz result" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="20" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Two-Way Table: Study Plan and Quiz Result</text>
  <rect x="50" y="45" width="340" height="135" fill="#ffffff" stroke="{_AXIS}"/>
  <g stroke="{_AXIS}">
    <line x1="150" y1="45" x2="150" y2="180"/>
    <line x1="230" y1="45" x2="230" y2="180"/>
    <line x1="310" y1="45" x2="310" y2="180"/>
    <line x1="50" y1="85" x2="390" y2="85"/>
    <line x1="50" y1="125" x2="390" y2="125"/>
    <line x1="50" y1="165" x2="390" y2="165"/>
  </g>
  <rect x="50" y="45" width="340" height="40" fill="#eff6ff"/>
  <rect x="50" y="45" width="100" height="135" fill="#f8fafc" opacity="0.8"/>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="190" y="69" font-weight="700">Passed</text><text x="270" y="69" font-weight="700">Not Passed</text><text x="350" y="69" font-weight="700">Total</text>
    <text x="100" y="109" font-weight="700">Plan done</text><text x="100" y="149" font-weight="700">Plan not done</text><text x="100" y="174" font-weight="700">Total</text>
    <text x="190" y="109">18</text><text x="270" y="109">6</text><text x="350" y="109">24</text>
    <text x="190" y="149">7</text><text x="270" y="149">9</text><text x="350" y="149">16</text>
    <text x="190" y="174">25</text><text x="270" y="174">15</text><text x="350" y="174">40</text>
  </g>
  <text x="220" y="208" text-anchor="middle" font-size="10.5" fill="#6b7280">Rows and columns organize two categories at the same time.</text>
</svg>'''


# --- Misleading graph scale ------------------------------------------------
_MISLEADING_SCALE = f'''
<svg viewBox="0 0 420 230" role="img" aria-label="Bar graph with a truncated y axis showing how scale can exaggerate differences" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="18" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Same Data, Truncated Scale</text>
  <line x1="75" y1="35" x2="75" y2="180" stroke="{_AXIS}"/>
  <line x1="75" y1="180" x2="350" y2="180" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="75" y1="180" x2="350" y2="180" stroke="{_GRID}"/><text x="68" y="183">90</text>
    <line x1="75" y1="130" x2="350" y2="130" stroke="{_GRID}"/><text x="68" y="133">95</text>
    <line x1="75" y1="80" x2="350" y2="80" stroke="{_GRID}"/><text x="68" y="83">100</text>
  </g>
  <g fill="{_BLUE}">
    <rect x="125" y="120" width="70" height="60"/>
    <rect x="235" y="90" width="70" height="90"/>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="160" y="112" font-weight="700">96</text><text x="270" y="82" font-weight="700">99</text>
    <text x="160" y="202">Class A</text><text x="270" y="202">Class B</text>
  </g>
  <text x="210" y="222" text-anchor="middle" font-size="10.5" fill="#6b7280">The axis starts at 90, so a 3-point difference looks visually large.</text>
</svg>'''


# --- Number line: solution of an inequality (x > 2) ------------------------
_NUMBER_LINE_INEQ = f'''
<svg viewBox="0 0 340 90" role="img" aria-label="Number line showing the solution x greater than 2" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="170" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Solution of  x &gt; 2</text>
  <line x1="20" y1="48" x2="320" y2="48" stroke="{_AXIS}" stroke-width="1.5"/>
  <polygon points="320,48 312,44 312,52" fill="{_AXIS}"/>
  <polygon points="20,48 28,44 28,52" fill="{_AXIS}"/>
  <line x1="170" y1="48" x2="316" y2="48" stroke="{_BLUE}" stroke-width="4"/>
  <polygon points="320,48 310,42 310,54" fill="{_BLUE}"/>
  <circle cx="170" cy="48" r="6" fill="#fff" stroke="{_BLUE}" stroke-width="2.5"/>
  <g stroke="{_AXIS}">
    <line x1="30" y1="44" x2="30" y2="52"/><line x1="65" y1="44" x2="65" y2="52"/>
    <line x1="100" y1="44" x2="100" y2="52"/><line x1="135" y1="44" x2="135" y2="52"/>
    <line x1="170" y1="44" x2="170" y2="52"/><line x1="205" y1="44" x2="205" y2="52"/>
    <line x1="240" y1="44" x2="240" y2="52"/><line x1="275" y1="44" x2="275" y2="52"/>
    <line x1="310" y1="44" x2="310" y2="52"/>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="30" y="70">-2</text><text x="65" y="70">-1</text><text x="100" y="70">0</text>
    <text x="135" y="70">1</text><text x="170" y="70">2</text><text x="205" y="70">3</text>
    <text x="240" y="70">4</text><text x="275" y="70">5</text><text x="310" y="70">6</text>
  </g>
  <text x="170" y="36" text-anchor="middle" font-size="9" fill="#6b7280">open circle = 2 not included</text>
</svg>'''


# --- Coordinate plane with the line y = 2x + 1 -----------------------------
_COORD_LINE = f'''
<svg viewBox="0 0 280 290" role="img" aria-label="Coordinate plane graphing the line y = 2x + 1" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Line:  y = 2x + 1</text>
  <g stroke="{_GRID}">
    <line x1="20" y1="30" x2="20" y2="270"/><line x1="44" y1="30" x2="44" y2="270"/><line x1="68" y1="30" x2="68" y2="270"/>
    <line x1="92" y1="30" x2="92" y2="270"/><line x1="116" y1="30" x2="116" y2="270"/><line x1="164" y1="30" x2="164" y2="270"/>
    <line x1="188" y1="30" x2="188" y2="270"/><line x1="212" y1="30" x2="212" y2="270"/><line x1="236" y1="30" x2="236" y2="270"/><line x1="260" y1="30" x2="260" y2="270"/>
    <line x1="20" y1="30" x2="260" y2="30"/><line x1="20" y1="54" x2="260" y2="54"/><line x1="20" y1="78" x2="260" y2="78"/>
    <line x1="20" y1="102" x2="260" y2="102"/><line x1="20" y1="126" x2="260" y2="126"/><line x1="20" y1="174" x2="260" y2="174"/>
    <line x1="20" y1="198" x2="260" y2="198"/><line x1="20" y1="222" x2="260" y2="222"/><line x1="20" y1="246" x2="260" y2="246"/><line x1="20" y1="270" x2="260" y2="270"/>
  </g>
  <line x1="20" y1="150" x2="260" y2="150" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="140" y1="30" x2="140" y2="270" stroke="{_AXIS}" stroke-width="1.5"/>
  <text x="255" y="145" font-size="10" fill="#6b7280">x</text>
  <text x="146" y="40" font-size="10" fill="#6b7280">y</text>
  <line x1="92" y1="222" x2="188" y2="30" stroke="{_BLUE}" stroke-width="2.5"/>
  <g stroke="{_RED}" stroke-width="1.5" stroke-dasharray="4 3">
    <line x1="140" y1="126" x2="164" y2="126"/>
    <line x1="164" y1="126" x2="164" y2="78"/>
  </g>
  <text x="150" y="140" font-size="9" fill="{_RED}">run 1</text>
  <text x="168" y="106" font-size="9" fill="{_RED}">rise 2</text>
  <circle cx="140" cy="126" r="4" fill="{_BLUE}"/>
  <text x="146" y="120" font-size="10" font-weight="700" fill="{_BLUE}">(0, 1)</text>
  <text x="120" y="288" font-size="9" fill="#6b7280" text-anchor="middle">y-intercept b = 1, slope m = 2</text>
</svg>'''


# --- Parabola: y = x^2 - 4, showing its two roots --------------------------
_PARABOLA = f'''
<svg viewBox="0 0 280 290" role="img" aria-label="Parabola y = x squared minus 4 with roots at x = -2 and x = 2" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Parabola:  y = x² − 4</text>
  <line x1="40" y1="190" x2="245" y2="190" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="140" y1="95" x2="140" y2="275" stroke="{_AXIS}" stroke-width="1.5"/>
  <text x="240" y="185" font-size="10" fill="#6b7280">x</text>
  <text x="146" y="103" font-size="10" fill="#6b7280">y</text>
  <polyline points="50,100 65,149.5 80,190 95,221.5 110,244 125,257.5 140,262 155,257.5 170,244 185,221.5 200,190 215,149.5 230,100" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <g fill="{_RED}">
    <circle cx="80" cy="190" r="4.5"/><circle cx="200" cy="190" r="4.5"/>
  </g>
  <text x="80" y="178" text-anchor="middle" font-size="10" font-weight="700" fill="{_RED}">x = −2</text>
  <text x="200" y="178" text-anchor="middle" font-size="10" font-weight="700" fill="{_RED}">x = 2</text>
  <circle cx="140" cy="262" r="4" fill="{_BLUE}"/>
  <text x="140" y="278" text-anchor="middle" font-size="10" fill="{_BLUE}">vertex (0, −4)</text>
  <text x="140" y="290" text-anchor="middle" font-size="9" fill="#6b7280">roots = where the curve crosses the x-axis</text>
</svg>'''


# --- Expression anatomy ----------------------------------------------------
_EXPRESSION_ANATOMY = f'''
<svg viewBox="0 0 540 210" role="img" aria-label="Expression anatomy for 3x squared minus 5x plus 7" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Anatomy of an Algebraic Expression</text>
  <text x="270" y="84" text-anchor="middle" font-size="32" font-weight="700" fill="{_INK}">3x² - 5x + 7</text>
  <g stroke="{_AXIS}" stroke-width="1.3" fill="none">
    <path d="M170,96 L138,128"/><path d="M270,96 L270,128"/><path d="M368,96 L402,128"/>
  </g>
  <g font-size="11" fill="{_INK}">
    <rect x="55" y="132" width="165" height="44" rx="7" fill="#eff6ff" stroke="#bfdbfe"/>
    <text x="138" y="151" text-anchor="middle" font-weight="700" fill="{_BLUE}">term: 3x²</text>
    <text x="138" y="167" text-anchor="middle">coefficient 3, variable x, exponent 2</text>
    <rect x="220" y="132" width="100" height="44" rx="7" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="270" y="151" text-anchor="middle" font-weight="700">term: -5x</text>
    <text x="270" y="167" text-anchor="middle">coefficient -5</text>
    <rect x="336" y="132" width="150" height="44" rx="7" fill="#f0fdf4" stroke="#bbf7d0"/>
    <text x="411" y="151" text-anchor="middle" font-weight="700" fill="#15803d">constant: 7</text>
    <text x="411" y="167" text-anchor="middle">number without a variable</text>
  </g>
  <text x="270" y="198" text-anchor="middle" font-size="10.5" fill="#6b7280">Terms are separated by plus or minus signs; signs stay attached to their terms.</text>
</svg>'''


# --- Distributive property area model --------------------------------------
_DISTRIBUTIVE_AREA_MODEL = f'''
<svg viewBox="0 0 540 250" role="img" aria-label="Area model for 4 times x plus 3 equals 4x plus 12" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Distributive Property as Area</text>
  <rect x="85" y="74" width="210" height="88" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="295" y="74" width="84" height="88" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <line x1="295" y1="68" x2="295" y2="168" stroke="{_AXIS}" stroke-width="1.3"/>
  <g font-size="13" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="190" y="123">4x</text>
    <text x="337" y="123">12</text>
    <text x="232" y="60">x</text>
    <text x="337" y="60">3</text>
    <text x="68" y="122">4</text>
  </g>
  <text x="270" y="195" text-anchor="middle" font-size="16" font-weight="700" fill="{_INK}">4(x + 3) = 4x + 12</text>
  <text x="270" y="222" text-anchor="middle" font-size="10.5" fill="#6b7280">The 4 multiplies every part inside the parentheses, not just the first term.</text>
</svg>'''


# --- Polynomial degree and terms -------------------------------------------
_POLYNOMIAL_DEGREE = f'''
<svg viewBox="0 0 540 220" role="img" aria-label="Polynomial terms arranged by degree" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Degree Tells the Highest Power</text>
  <text x="270" y="66" text-anchor="middle" font-size="24" font-weight="700" fill="{_INK}">2x³ - 4x² + x - 9</text>
  <g>
    <rect x="45" y="102" width="108" height="58" rx="7" fill="#eff6ff" stroke="#bfdbfe"/>
    <rect x="165" y="102" width="108" height="58" rx="7" fill="#f8fafc" stroke="#cbd5e1"/>
    <rect x="285" y="102" width="108" height="58" rx="7" fill="#f0fdf4" stroke="#bbf7d0"/>
    <rect x="405" y="102" width="90" height="58" rx="7" fill="#fff7ed" stroke="#fed7aa"/>
  </g>
  <g font-size="12" fill="{_INK}" text-anchor="middle">
    <text x="99" y="126" font-weight="700" fill="{_BLUE}">2x³</text><text x="99" y="145">degree 3</text>
    <text x="219" y="126" font-weight="700">-4x²</text><text x="219" y="145">degree 2</text>
    <text x="339" y="126" font-weight="700" fill="#15803d">x</text><text x="339" y="145">degree 1</text>
    <text x="450" y="126" font-weight="700" fill="#c2410c">-9</text><text x="450" y="145">degree 0</text>
  </g>
  <text x="270" y="195" text-anchor="middle" font-size="10.5" fill="#6b7280">The polynomial's degree is 3 because the highest exponent is 3.</text>
</svg>'''


# --- Factoring trinomial pattern -------------------------------------------
_FACTORING_TRINOMIAL = f'''
<svg viewBox="0 0 540 245" role="img" aria-label="Factoring x squared plus 5x plus 6 as x plus 2 times x plus 3" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Factoring a Trinomial</text>
  <text x="270" y="62" text-anchor="middle" font-size="22" font-weight="700" fill="{_INK}">x² + 5x + 6</text>
  <g stroke="{_AXIS}" stroke-width="1.5" fill="none">
    <path d="M210,78 C178,102 158,124 144,152"/>
    <path d="M330,78 C362,102 382,124 396,152"/>
  </g>
  <rect x="72" y="150" width="150" height="52" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>
  <rect x="318" y="150" width="150" height="52" rx="8" fill="#f0fdf4" stroke="#bbf7d0"/>
  <g font-size="12" fill="{_INK}" text-anchor="middle">
    <text x="147" y="172" font-weight="700" fill="{_BLUE}">2 and 3</text>
    <text x="147" y="190">multiply to 6</text>
    <text x="393" y="172" font-weight="700" fill="#15803d">2 + 3 = 5</text>
    <text x="393" y="190">add to middle coefficient</text>
  </g>
  <text x="270" y="226" text-anchor="middle" font-size="17" font-weight="700" fill="{_INK}">x² + 5x + 6 = (x + 2)(x + 3)</text>
</svg>'''


# --- Rational expression restrictions --------------------------------------
_RATIONAL_EXPRESSION_RESTRICTION = f'''
<svg viewBox="0 0 540 225" role="img" aria-label="Rational expression restriction showing denominator x minus 4 cannot equal zero" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Rational Expressions: Watch the Denominator</text>
  <text x="270" y="82" text-anchor="middle" font-size="30" font-weight="700" fill="{_INK}">(x² - 16) / (x - 4)</text>
  <rect x="110" y="118" width="320" height="48" rx="8" fill="#fff7ed" stroke="#fed7aa"/>
  <text x="270" y="148" text-anchor="middle" font-size="15" font-weight="700" fill="#c2410c">Restriction: x - 4 cannot equal 0, so x cannot equal 4</text>
  <text x="270" y="194" text-anchor="middle" font-size="10.5" fill="#6b7280">Even if factors cancel later, the original denominator still cannot be zero.</text>
</svg>'''


# --- Function table to graph ----------------------------------------------
_FUNCTION_TABLE_LINE = f'''
<svg viewBox="0 0 520 290" role="img" aria-label="Function table for y equals 2x plus 1 connected to its line graph" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="260" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Table, Rule, and Graph: y = 2x + 1</text>
  <rect x="35" y="45" width="155" height="176" rx="4" fill="#ffffff" stroke="{_AXIS}"/>
  <rect x="35" y="45" width="155" height="36" fill="#eff6ff"/>
  <g stroke="{_AXIS}">
    <line x1="112" y1="45" x2="112" y2="221"/>
    <line x1="35" y1="81" x2="190" y2="81"/><line x1="35" y1="116" x2="190" y2="116"/>
    <line x1="35" y1="151" x2="190" y2="151"/><line x1="35" y1="186" x2="190" y2="186"/>
  </g>
  <g text-anchor="middle" font-size="12" fill="{_INK}">
    <text x="74" y="68" font-weight="700">x</text><text x="151" y="68" font-weight="700">y</text>
    <text x="74" y="104">-1</text><text x="151" y="104">-1</text>
    <text x="74" y="139">0</text><text x="151" y="139">1</text>
    <text x="74" y="174">1</text><text x="151" y="174">3</text>
    <text x="74" y="209">2</text><text x="151" y="209">5</text>
  </g>
  <g stroke="{_GRID}">
    <line x1="260" y1="45" x2="260" y2="245"/><line x1="300" y1="45" x2="300" y2="245"/><line x1="340" y1="45" x2="340" y2="245"/><line x1="380" y1="45" x2="380" y2="245"/><line x1="420" y1="45" x2="420" y2="245"/><line x1="460" y1="45" x2="460" y2="245"/>
    <line x1="240" y1="225" x2="480" y2="225"/><line x1="240" y1="185" x2="480" y2="185"/><line x1="240" y1="145" x2="480" y2="145"/><line x1="240" y1="105" x2="480" y2="105"/><line x1="240" y1="65" x2="480" y2="65"/>
  </g>
  <line x1="240" y1="145" x2="480" y2="145" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="340" y1="45" x2="340" y2="245" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="300" y1="185" x2="420" y2="65" stroke="{_BLUE}" stroke-width="2.5"/>
  <g fill="{_BLUE}">
    <circle cx="300" cy="185" r="4"/><circle cx="340" cy="125" r="4"/><circle cx="380" cy="105" r="4"/><circle cx="420" cy="65" r="4"/>
  </g>
  <text x="360" y="274" text-anchor="middle" font-size="10.5" fill="#6b7280">Each table row becomes a point; the constant slope makes the points line up.</text>
</svg>'''


# --- Slope types -----------------------------------------------------------
_SLOPE_TYPES = f'''
<svg viewBox="0 0 500 190" role="img" aria-label="Four mini graphs showing positive, negative, zero, and undefined slope" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="250" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Four Slope Types</text>
  <g transform="translate(24,42)">
    <rect width="95" height="95" fill="#fff" stroke="{_GRID}"/><line x1="12" y1="78" x2="84" y2="22" stroke="{_BLUE}" stroke-width="3"/>
    <text x="47" y="120" text-anchor="middle" font-size="10.5" font-weight="700" fill="{_INK}">positive</text>
  </g>
  <g transform="translate(143,42)">
    <rect width="95" height="95" fill="#fff" stroke="{_GRID}"/><line x1="12" y1="22" x2="84" y2="78" stroke="{_RED}" stroke-width="3"/>
    <text x="47" y="120" text-anchor="middle" font-size="10.5" font-weight="700" fill="{_INK}">negative</text>
  </g>
  <g transform="translate(262,42)">
    <rect width="95" height="95" fill="#fff" stroke="{_GRID}"/><line x1="12" y1="50" x2="84" y2="50" stroke="#16a34a" stroke-width="3"/>
    <text x="47" y="120" text-anchor="middle" font-size="10.5" font-weight="700" fill="{_INK}">zero</text>
  </g>
  <g transform="translate(381,42)">
    <rect width="95" height="95" fill="#fff" stroke="{_GRID}"/><line x1="47" y1="14" x2="47" y2="84" stroke="#7c3aed" stroke-width="3"/>
    <text x="47" y="120" text-anchor="middle" font-size="10.5" font-weight="700" fill="{_INK}">undefined</text>
  </g>
  <text x="250" y="178" text-anchor="middle" font-size="10.5" fill="#6b7280">Positive rises, negative falls, horizontal has slope 0, and vertical has no defined slope.</text>
</svg>'''


# --- Linear inequality on the coordinate plane -----------------------------
_LINEAR_INEQUALITY_SHADE = f'''
<svg viewBox="0 0 360 300" role="img" aria-label="Coordinate graph of the dashed boundary y equals x plus 1 with the region above shaded" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="180" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Graph of y &gt; x + 1</text>
  <g stroke="{_GRID}">
    <line x1="60" y1="45" x2="60" y2="245"/><line x1="100" y1="45" x2="100" y2="245"/><line x1="140" y1="45" x2="140" y2="245"/><line x1="180" y1="45" x2="180" y2="245"/><line x1="220" y1="45" x2="220" y2="245"/><line x1="260" y1="45" x2="260" y2="245"/><line x1="300" y1="45" x2="300" y2="245"/>
    <line x1="60" y1="45" x2="300" y2="45"/><line x1="60" y1="85" x2="300" y2="85"/><line x1="60" y1="125" x2="300" y2="125"/><line x1="60" y1="165" x2="300" y2="165"/><line x1="60" y1="205" x2="300" y2="205"/><line x1="60" y1="245" x2="300" y2="245"/>
  </g>
  <polygon points="60,45 300,45 300,85 100,245 60,245" fill="#dbeafe" opacity="0.7"/>
  <line x1="100" y1="245" x2="300" y2="85" stroke="{_BLUE}" stroke-width="2.5" stroke-dasharray="7 5"/>
  <line x1="60" y1="165" x2="300" y2="165" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="180" y1="45" x2="180" y2="245" stroke="{_AXIS}" stroke-width="1.5"/>
  <circle cx="180" cy="125" r="4" fill="{_BLUE}"/>
  <text x="190" y="118" font-size="10.5" font-weight="700" fill="{_BLUE}">(0, 1)</text>
  <text x="238" y="62" font-size="10" fill="#1e40af">shade above</text>
  <text x="180" y="276" text-anchor="middle" font-size="10.5" fill="#6b7280">Dashed boundary because points on y = x + 1 are not included.</text>
</svg>'''


_GREEN = "#16a34a"


# --- Animal cell with labeled organelles -----------------------------------
_CELL_ANIMAL = f'''
<svg viewBox="0 0 380 280" role="img" aria-label="Diagram of an animal cell with labeled nucleus, mitochondria, cytoplasm and cell membrane" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Animal Cell</text>
  <ellipse cx="175" cy="155" rx="120" ry="92" fill="#eef2ff" stroke="{_BLUE}" stroke-width="2.5"/>
  <circle cx="150" cy="155" r="38" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5"/>
  <circle cx="158" cy="160" r="11" fill="#4f46e5"/>
  <ellipse cx="232" cy="115" rx="24" ry="12" fill="#fecaca" stroke="{_RED}" stroke-width="1.5"/>
  <ellipse cx="120" cy="212" rx="20" ry="10" fill="#fecaca" stroke="{_RED}" stroke-width="1.5"/>
  <g fill="#64748b">
    <circle cx="210" cy="178" r="2.5"/><circle cx="196" cy="200" r="2.5"/><circle cx="240" cy="165" r="2.5"/><circle cx="172" cy="205" r="2.5"/>
  </g>
  <g stroke="#9ca3af" stroke-width="1">
    <line x1="262" y1="95" x2="300" y2="72"/>
    <line x1="254" y1="113" x2="300" y2="120"/>
    <line x1="114" y1="148" x2="66" y2="124"/>
    <line x1="120" y1="212" x2="70" y2="232"/>
  </g>
  <g font-size="11" fill="{_INK}">
    <text x="302" y="75" text-anchor="start">Cell membrane</text>
    <text x="302" y="123" text-anchor="start">Mitochondrion</text>
    <text x="62" y="120" text-anchor="end">Nucleus</text>
    <text x="66" y="236" text-anchor="end">Cytoplasm</text>
  </g>
</svg>'''


# --- Photosynthesis <-> respiration energy cycle ---------------------------
_ENERGY_CYCLE = f'''
<svg viewBox="0 0 380 235" role="img" aria-label="Cycle linking photosynthesis and cellular respiration" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Photosynthesis and Respiration</text>
  <circle cx="40" cy="52" r="14" fill="#facc15" stroke="#eab308"/>
  <g stroke="#eab308" stroke-width="1.5">
    <line x1="40" y1="30" x2="40" y2="22"/><line x1="22" y1="52" x2="14" y2="52"/><line x1="26" y1="38" x2="20" y2="32"/><line x1="54" y1="38" x2="60" y2="32"/>
  </g>
  <text x="40" y="80" text-anchor="middle" font-size="9" fill="#a16207">sunlight</text>
  <rect x="28" y="92" width="150" height="86" rx="10" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="103" y="112" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Photosynthesis</text>
  <text x="103" y="132" text-anchor="middle" font-size="9.5" fill="{_INK}">in: CO₂ + H₂O + light</text>
  <text x="103" y="148" text-anchor="middle" font-size="9.5" fill="{_INK}">out: glucose + O₂</text>
  <text x="103" y="168" text-anchor="middle" font-size="9" fill="#6b7280">(in chloroplasts)</text>
  <rect x="202" y="92" width="150" height="86" rx="10" fill="#fee2e2" stroke="{_RED}" stroke-width="1.5"/>
  <text x="277" y="112" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c">Respiration</text>
  <text x="277" y="132" text-anchor="middle" font-size="9.5" fill="{_INK}">in: glucose + O₂</text>
  <text x="277" y="148" text-anchor="middle" font-size="9.5" fill="{_INK}">out: CO₂ + H₂O + ATP</text>
  <text x="277" y="168" text-anchor="middle" font-size="9" fill="#6b7280">(in mitochondria)</text>
  <path d="M150,92 C150,58 230,58 230,92" fill="none" stroke="{_GREEN}" stroke-width="2"/>
  <polygon points="230,94 224,82 236,82" fill="{_GREEN}"/>
  <text x="190" y="56" text-anchor="middle" font-size="9.5" fill="#15803d">glucose + O₂</text>
  <path d="M230,178 C230,212 150,212 150,178" fill="none" stroke="{_RED}" stroke-width="2"/>
  <polygon points="150,176 144,188 156,188" fill="{_RED}"/>
  <text x="190" y="222" text-anchor="middle" font-size="9.5" fill="#b91c1c">CO₂ + H₂O</text>
</svg>'''


# --- Punnett square: Bb x Bb -----------------------------------------------
_PUNNETT = f'''
<svg viewBox="0 0 240 250" role="img" aria-label="Punnett square for the cross B b by B b" xmlns="http://www.w3.org/2000/svg" style="max-width:300px;width:100%;height:auto;{_FONT}">
  <text x="120" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Cross:  Bb × Bb</text>
  <g font-size="15" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="90" y="52">B</text><text x="150" y="52">b</text>
    <text x="48" y="100">B</text><text x="48" y="160">b</text>
  </g>
  <g stroke="{_INK}" stroke-width="1.5">
    <rect x="60" y="60" width="60" height="60" fill="#c7d2fe"/>
    <rect x="120" y="60" width="60" height="60" fill="#c7d2fe"/>
    <rect x="60" y="120" width="60" height="60" fill="#c7d2fe"/>
    <rect x="120" y="120" width="60" height="60" fill="#fde68a"/>
  </g>
  <g font-size="15" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="90" y="96">BB</text><text x="150" y="96">Bb</text>
    <text x="90" y="156">Bb</text><text x="150" y="156">bb</text>
  </g>
  <text x="120" y="208" text-anchor="middle" font-size="10.5" fill="{_INK}">Genotype 1 BB : 2 Bb : 1 bb</text>
  <text x="120" y="226" text-anchor="middle" font-size="10.5" fill="{_INK}">Phenotype 3 dominant : 1 recessive</text>
</svg>'''


# --- Food chain ------------------------------------------------------------
_FOOD_CHAIN = f'''
<svg viewBox="0 0 380 135" role="img" aria-label="A food chain from sun to grass to grasshopper to frog to hawk" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">A Food Chain (energy flows →)</text>
  <circle cx="28" cy="60" r="14" fill="#facc15" stroke="#eab308"/>
  <text x="28" y="64" text-anchor="middle" font-size="9" fill="#a16207">Sun</text>
  <g font-size="10.5" text-anchor="middle">
    <rect x="56" y="44" width="58" height="32" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="85" y="64" fill="{_INK}">Grass</text>
    <rect x="142" y="44" width="74" height="32" rx="6" fill="#fef9c3" stroke="#ca8a04"/><text x="179" y="64" fill="{_INK}">Grasshopper</text>
    <rect x="244" y="44" width="54" height="32" rx="6" fill="#ffedd5" stroke="#ea580c"/><text x="271" y="64" fill="{_INK}">Frog</text>
    <rect x="318" y="44" width="54" height="32" rx="6" fill="#fee2e2" stroke="{_RED}"/><text x="345" y="64" fill="{_INK}">Hawk</text>
  </g>
  <g stroke="#6b7280" stroke-width="1.5" fill="#6b7280">
    <line x1="44" y1="60" x2="54" y2="60"/><polygon points="56,60 50,57 50,63"/>
    <line x1="116" y1="60" x2="140" y2="60"/><polygon points="142,60 136,57 136,63"/>
    <line x1="218" y1="60" x2="242" y2="60"/><polygon points="244,60 238,57 238,63"/>
    <line x1="300" y1="60" x2="316" y2="60"/><polygon points="318,60 312,57 312,63"/>
  </g>
  <g font-size="9" fill="#6b7280" text-anchor="middle">
    <text x="85" y="94">Producer</text><text x="179" y="94">1° consumer</text><text x="271" y="94">2° consumer</text><text x="345" y="94">3° consumer</text>
  </g>
</svg>'''


# --- Energy pyramid (the 10% rule) -----------------------------------------
_ENERGY_PYRAMID = f'''
<svg viewBox="0 0 340 250" role="img" aria-label="Energy pyramid showing energy decreasing at each higher level" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="170" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Energy Pyramid</text>
  <polygon points="40,212 300,212 268,168 72,168" fill="{_GREEN}"/>
  <polygon points="72,168 268,168 236,124 104,124" fill="#65a30d"/>
  <polygon points="104,124 236,124 204,80 136,80" fill="#ea580c"/>
  <polygon points="136,80 204,80 184,42 156,42" fill="{_RED}"/>
  <g fill="#ffffff" text-anchor="middle" font-weight="700">
    <text x="170" y="196" font-size="11">Producers — 1000 kcal</text>
    <text x="170" y="152" font-size="10.5">1° consumers — 100 kcal</text>
    <text x="170" y="108" font-size="10">2° consumers — 10 kcal</text>
    <text x="170" y="62" font-size="9">3° — 1 kcal</text>
  </g>
  <line x1="318" y1="212" x2="318" y2="48" stroke="#6b7280" stroke-width="1.5"/>
  <polygon points="318,44 314,54 322,54" fill="#6b7280"/>
  <text x="332" y="130" font-size="10" fill="#6b7280" transform="rotate(90 332 130)" text-anchor="middle">energy decreases</text>
</svg>'''


_AMBER = "#d97706"


# --- Argument structure: Claim -> Evidence -> Reasoning --------------------
_ARGUMENT = f'''
<svg viewBox="0 0 360 250" role="img" aria-label="Diagram of an argument: claim supported by evidence explained by reasoning" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="180" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Building an Argument</text>
  <rect x="70" y="32" width="220" height="46" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="180" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#1e3a8a">CLAIM</text>
  <text x="180" y="68" text-anchor="middle" font-size="10" fill="{_INK}">the point you are arguing</text>
  <line x1="180" y1="78" x2="180" y2="100" stroke="#6b7280" stroke-width="1.5"/>
  <polygon points="180,102 175,92 185,92" fill="#6b7280"/>
  <text x="196" y="94" font-size="9" fill="#6b7280">supported by</text>
  <rect x="70" y="102" width="220" height="46" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="180" y="122" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">EVIDENCE</text>
  <text x="180" y="138" text-anchor="middle" font-size="10" fill="{_INK}">facts, details, examples from the text</text>
  <line x1="180" y1="148" x2="180" y2="170" stroke="#6b7280" stroke-width="1.5"/>
  <polygon points="180,172 175,162 185,162" fill="#6b7280"/>
  <text x="196" y="164" font-size="9" fill="#6b7280">explained by</text>
  <rect x="70" y="172" width="220" height="46" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="180" y="192" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">REASONING</text>
  <text x="180" y="208" text-anchor="middle" font-size="10" fill="{_INK}">how the evidence proves the claim</text>
</svg>'''


# --- Essay structure: intro, body paragraphs, conclusion -------------------
_ESSAY_STRUCTURE = f'''
<svg viewBox="0 0 360 296" role="img" aria-label="Structure of a GED&reg; extended response essay" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="180" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Structure of the GED&reg; Essay</text>
  <rect x="40" y="32" width="280" height="44" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="180" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#1e3a8a">Introduction</text>
  <text x="180" y="68" text-anchor="middle" font-size="9.5" fill="{_INK}">hook + your thesis (the claim you will defend)</text>
  <rect x="40" y="84" width="280" height="40" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="180" y="101" text-anchor="middle" font-size="11.5" font-weight="700" fill="#15803d">Body Paragraph 1</text>
  <text x="180" y="116" text-anchor="middle" font-size="9.5" fill="{_INK}">point + evidence from the passage</text>
  <rect x="40" y="132" width="280" height="40" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="180" y="149" text-anchor="middle" font-size="11.5" font-weight="700" fill="#15803d">Body Paragraph 2</text>
  <text x="180" y="164" text-anchor="middle" font-size="9.5" fill="{_INK}">point + evidence from the passage</text>
  <rect x="40" y="180" width="280" height="40" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="180" y="197" text-anchor="middle" font-size="11.5" font-weight="700" fill="#15803d">Body Paragraph 3</text>
  <text x="180" y="212" text-anchor="middle" font-size="9.5" fill="{_INK}">address the weaker argument</text>
  <rect x="40" y="228" width="280" height="44" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="180" y="248" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">Conclusion</text>
  <text x="180" y="264" text-anchor="middle" font-size="9.5" fill="{_INK}">restate your thesis + wrap up</text>
</svg>'''


# --- Three branches of government ------------------------------------------
_THREE_BRANCHES = f'''
<svg viewBox="0 0 380 250" role="img" aria-label="The three branches of U.S. government and checks and balances" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">The Three Branches of Government</text>
  <g stroke="#9ca3af" stroke-width="1.5">
    <line x1="190" y1="94" x2="95" y2="156"/>
    <line x1="190" y1="94" x2="285" y2="156"/>
    <line x1="168" y1="190" x2="212" y2="190"/>
  </g>
  <text x="190" y="132" text-anchor="middle" font-size="11" font-weight="700" fill="#6b7280">Checks &amp; Balances</text>
  <text x="190" y="146" text-anchor="middle" font-size="9" fill="#9ca3af">each branch limits the others</text>
  <rect x="130" y="34" width="120" height="60" rx="8" fill="#fee2e2" stroke="{_RED}" stroke-width="1.5"/>
  <text x="190" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c">Executive</text>
  <text x="190" y="68" text-anchor="middle" font-size="9.5" fill="{_INK}">President</text>
  <text x="190" y="82" text-anchor="middle" font-size="9.5" fill="{_INK}">enforces the laws</text>
  <rect x="20" y="158" width="150" height="64" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="95" y="178" text-anchor="middle" font-size="12" font-weight="700" fill="#1e3a8a">Legislative</text>
  <text x="95" y="194" text-anchor="middle" font-size="9.5" fill="{_INK}">Congress (House + Senate)</text>
  <text x="95" y="208" text-anchor="middle" font-size="9.5" fill="{_INK}">makes the laws</text>
  <rect x="210" y="158" width="150" height="64" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="285" y="178" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Judicial</text>
  <text x="285" y="194" text-anchor="middle" font-size="9.5" fill="{_INK}">the Courts</text>
  <text x="285" y="208" text-anchor="middle" font-size="9.5" fill="{_INK}">interpret the laws</text>
</svg>'''


# --- Supply and demand graph -----------------------------------------------
_SUPPLY_DEMAND = f'''
<svg viewBox="0 0 320 260" role="img" aria-label="Supply and demand curves crossing at equilibrium" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="165" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Supply and Demand</text>
  <line x1="50" y1="30" x2="50" y2="210" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="50" y1="210" x2="295" y2="210" stroke="{_AXIS}" stroke-width="1.5"/>
  <text x="30" y="125" font-size="10" fill="#6b7280" transform="rotate(-90 30 125)" text-anchor="middle">Price</text>
  <text x="170" y="232" font-size="10" fill="#6b7280" text-anchor="middle">Quantity</text>
  <line x1="50" y1="40" x2="270" y2="200" stroke="{_RED}" stroke-width="2.5"/>
  <line x1="50" y1="200" x2="270" y2="40" stroke="{_BLUE}" stroke-width="2.5"/>
  <g stroke="#9ca3af" stroke-width="1" stroke-dasharray="4 3">
    <line x1="160" y1="120" x2="160" y2="210"/>
    <line x1="50" y1="120" x2="160" y2="120"/>
  </g>
  <circle cx="160" cy="120" r="4.5" fill="{_INK}"/>
  <text x="166" y="113" font-size="10" font-weight="700" fill="{_INK}">Equilibrium</text>
  <text x="250" y="195" font-size="11" font-weight="700" fill="{_RED}" text-anchor="end">Demand</text>
  <text x="250" y="52" font-size="11" font-weight="700" fill="{_BLUE}" text-anchor="end">Supply</text>
</svg>'''


# --- How a bill becomes a law ----------------------------------------------
_BILL_TO_LAW = f'''
<svg viewBox="0 0 380 320" role="img" aria-label="Flowchart of how a bill becomes a law" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="145" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">How a Bill Becomes a Law</text>
  <g stroke="#9ca3af" stroke-width="1.5" fill="#9ca3af">
    <line x1="145" y1="74" x2="145" y2="90"/><polygon points="145,92 140,82 150,82"/>
    <line x1="145" y1="132" x2="145" y2="148"/><polygon points="145,150 140,140 150,140"/>
    <line x1="145" y1="190" x2="145" y2="206"/><polygon points="145,208 140,198 150,198"/>
    <line x1="145" y1="248" x2="145" y2="264"/><polygon points="145,266 140,256 150,256"/>
  </g>
  <g text-anchor="middle">
    <rect x="20" y="34" width="250" height="40" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <text x="145" y="58" font-size="11" fill="{_INK}">1. A bill is introduced in Congress</text>
    <rect x="20" y="92" width="250" height="40" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <text x="145" y="116" font-size="11" fill="{_INK}">2. A committee studies and revises it</text>
    <rect x="20" y="150" width="250" height="40" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <text x="145" y="174" font-size="11" fill="{_INK}">3. The House and Senate both vote yes</text>
    <rect x="20" y="208" width="250" height="40" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
    <text x="145" y="232" font-size="11" fill="{_INK}">4. The President signs it</text>
    <rect x="20" y="266" width="250" height="40" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
    <text x="145" y="290" font-size="11.5" font-weight="700" fill="#15803d">5. It becomes a law</text>
  </g>
  <line x1="270" y1="228" x2="285" y2="228" stroke="#9ca3af" stroke-width="1" stroke-dasharray="3 2"/>
  <g font-size="8.5" fill="#6b7280">
    <text x="288" y="218">If vetoed,</text>
    <text x="288" y="230">Congress can</text>
    <text x="288" y="242">override with a</text>
    <text x="288" y="254">2/3 vote.</text>
  </g>
</svg>'''


# --- Timeline of key moments in U.S. history -------------------------------
_US_TIMELINE = f'''
<svg viewBox="0 0 380 150" role="img" aria-label="Timeline of key moments in United States history" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Key Moments in U.S. History</text>
  <line x1="20" y1="75" x2="360" y2="75" stroke="{_AXIS}" stroke-width="2"/>
  <polygon points="364,75 354,70 354,80" fill="{_AXIS}"/>
  <g stroke="{_BLUE}" stroke-width="1.5">
    <line x1="40" y1="68" x2="40" y2="82"/><line x1="100" y1="68" x2="100" y2="82"/><line x1="160" y1="68" x2="160" y2="82"/>
    <line x1="220" y1="68" x2="220" y2="82"/><line x1="280" y1="68" x2="280" y2="82"/><line x1="340" y1="68" x2="340" y2="82"/>
  </g>
  <g fill="{_BLUE}">
    <circle cx="40" cy="75" r="3.5"/><circle cx="100" cy="75" r="3.5"/><circle cx="160" cy="75" r="3.5"/>
    <circle cx="220" cy="75" r="3.5"/><circle cx="280" cy="75" r="3.5"/><circle cx="340" cy="75" r="3.5"/>
  </g>
  <g font-size="10" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="40" y="58">1607</text><text x="100" y="58">1776</text><text x="160" y="58">1787</text>
    <text x="220" y="58">1861</text><text x="280" y="58">1929</text><text x="340" y="58">1964</text>
  </g>
  <g font-size="8.5" fill="#6b7280" text-anchor="middle">
    <text x="40" y="98">Jamestown</text><text x="100" y="98">Declaration</text><text x="160" y="98">Constitution</text>
    <text x="220" y="98">Civil War</text><text x="280" y="98">Great</text><text x="280" y="109">Depression</text><text x="340" y="98">Civil Rights</text><text x="340" y="109">Act</text>
  </g>
</svg>'''


# --- GED math roadmap ------------------------------------------------------
_GED_MATH_ROADMAP = f'''
<svg viewBox="0 0 420 230" role="img" aria-label="Roadmap of GED&reg; math areas: basic math, geometry, algebra, graphs and functions" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">GED&reg; Math Roadmap</text>
  <g text-anchor="middle">
    <rect x="20" y="45" width="85" height="115" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <rect x="120" y="45" width="85" height="115" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
    <rect x="220" y="45" width="85" height="115" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
    <rect x="320" y="45" width="85" height="115" rx="8" fill="#fee2e2" stroke="{_RED}" stroke-width="1.5"/>
    <text x="62" y="68" font-size="12" font-weight="700" fill="#1e3a8a">Basic</text>
    <text x="62" y="84" font-size="12" font-weight="700" fill="#1e3a8a">Math</text>
    <text x="162" y="76" font-size="12" font-weight="700" fill="#15803d">Geometry</text>
    <text x="262" y="76" font-size="12" font-weight="700" fill="#b45309">Algebra</text>
    <text x="362" y="68" font-size="12" font-weight="700" fill="#b91c1c">Graphs &amp;</text>
    <text x="362" y="84" font-size="12" font-weight="700" fill="#b91c1c">Functions</text>
  </g>
  <g font-size="9.5" fill="{_INK}" text-anchor="middle">
    <text x="62" y="108">fractions</text><text x="62" y="124">percents</text><text x="62" y="140">rates</text>
    <text x="162" y="108">area</text><text x="162" y="124">volume</text><text x="162" y="140">right triangles</text>
    <text x="262" y="108">equations</text><text x="262" y="124">inequalities</text><text x="262" y="140">quadratics</text>
    <text x="362" y="108">slope</text><text x="362" y="124">tables</text><text x="362" y="140">data</text>
  </g>
  <path d="M60,180 C115,206 305,206 360,180" fill="none" stroke="{_AXIS}" stroke-width="1.5"/>
  <polygon points="360,180 349,177 354,188" fill="{_AXIS}"/>
  <text x="210" y="210" text-anchor="middle" font-size="10.5" fill="#6b7280">The test rewards choosing the right model, then doing careful arithmetic.</text>
</svg>'''


# --- Place value ladder ----------------------------------------------------
_PLACE_VALUE_LADDER = f'''
<svg viewBox="0 0 390 150" role="img" aria-label="Place value ladder showing hundreds, tens, ones, tenths, hundredths and thousandths" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Place Value Ladder</text>
  <g text-anchor="middle" font-size="10.5" fill="{_INK}">
    <rect x="20" y="45" width="55" height="58" rx="6" fill="#dbeafe" stroke="{_BLUE}"/><text x="47" y="68" font-weight="700">Hundreds</text><text x="47" y="87">100</text>
    <rect x="80" y="45" width="55" height="58" rx="6" fill="#dbeafe" stroke="{_BLUE}"/><text x="107" y="68" font-weight="700">Tens</text><text x="107" y="87">10</text>
    <rect x="140" y="45" width="55" height="58" rx="6" fill="#dbeafe" stroke="{_BLUE}"/><text x="167" y="68" font-weight="700">Ones</text><text x="167" y="87">1</text>
    <text x="205" y="79" font-size="22" font-weight="700" fill="{_INK}">.</text>
    <rect x="220" y="45" width="55" height="58" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="247" y="68" font-weight="700">Tenths</text><text x="247" y="87">0.1</text>
    <rect x="280" y="45" width="55" height="58" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="307" y="68" font-weight="700">Hundredths</text><text x="307" y="87">0.01</text>
    <rect x="340" y="45" width="45" height="58" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="362" y="65" font-weight="700">Thou-</text><text x="362" y="78" font-weight="700">sandths</text><text x="362" y="94">0.001</text>
  </g>
  <text x="195" y="128" text-anchor="middle" font-size="10.5" fill="#6b7280">Moving right divides by 10; moving left multiplies by 10.</text>
</svg>'''


# --- Fraction, decimal and percent bar -------------------------------------
_FRACTION_PERCENT_BAR = f'''
<svg viewBox="0 0 390 150" role="img" aria-label="A bar showing one fourth equals 25 percent equals 0.25" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">One Part, Three Names</text>
  <rect x="45" y="52" width="300" height="34" fill="#ffffff" stroke="{_INK}" stroke-width="1.2"/>
  <rect x="45" y="52" width="75" height="34" fill="#bfdbfe"/>
  <g stroke="{_INK}" stroke-width="1">
    <line x1="120" y1="52" x2="120" y2="86"/><line x1="195" y1="52" x2="195" y2="86"/><line x1="270" y1="52" x2="270" y2="86"/>
  </g>
  <text x="82" y="74" text-anchor="middle" font-size="12" font-weight="700" fill="#1e3a8a">shaded</text>
  <g text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">
    <text x="95" y="115">1/4</text><text x="195" y="115">0.25</text><text x="295" y="115">25%</text>
  </g>
  <text x="195" y="138" text-anchor="middle" font-size="10.5" fill="#6b7280">Fraction, decimal, and percent can describe the same amount.</text>
</svg>'''


# --- Fraction circle: numerator and denominator ----------------------------
_FRACTION_CIRCLE = f'''
<svg viewBox="0 0 390 230" role="img" aria-label="Circle divided into eight equal parts with three shaded" xmlns="http://www.w3.org/2000/svg" style="max-width:500px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Fraction Meaning: 3/8</text>
  <g transform="translate(118 42)">
    <circle cx="75" cy="75" r="72" fill="#ffffff" stroke="{_INK}" stroke-width="1.5"/>
    <path d="M75,75 L75,3 A72,72 0 0,1 125.9,24.1 Z" fill="#bfdbfe" stroke="{_INK}" stroke-width="1"/>
    <path d="M75,75 L125.9,24.1 A72,72 0 0,1 147,75 Z" fill="#bfdbfe" stroke="{_INK}" stroke-width="1"/>
    <path d="M75,75 L147,75 A72,72 0 0,1 125.9,125.9 Z" fill="#bfdbfe" stroke="{_INK}" stroke-width="1"/>
    <line x1="75" y1="75" x2="75" y2="3" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="125.9" y2="24.1" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="147" y2="75" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="125.9" y2="125.9" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="75" y2="147" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="24.1" y2="125.9" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="3" y2="75" stroke="{_INK}"/>
    <line x1="75" y1="75" x2="24.1" y2="24.1" stroke="{_INK}"/>
  </g>
  <g font-size="12" fill="{_INK}">
    <text x="260" y="78" font-weight="700" fill="#1e3a8a">Numerator = 3</text>
    <text x="260" y="96">shaded parts</text>
    <text x="260" y="134" font-weight="700">Denominator = 8</text>
    <text x="260" y="152">equal total parts</text>
  </g>
  <text x="195" y="210" text-anchor="middle" font-size="10.5" fill="#6b7280">A fraction only works when the parts are equal size.</text>
</svg>'''


# --- Equivalent fraction strips -------------------------------------------
_EQUIVALENT_FRACTION_STRIPS = f'''
<svg viewBox="0 0 410 220" role="img" aria-label="Fraction strips showing one half equals two fourths equals four eighths" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="205" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Equivalent Fractions</text>
  <g stroke="{_INK}" stroke-width="1">
    <rect x="80" y="44" width="240" height="32" fill="#ffffff"/>
    <rect x="80" y="44" width="120" height="32" fill="#bfdbfe"/>
    <line x1="200" y1="44" x2="200" y2="76"/>
    <rect x="80" y="96" width="240" height="32" fill="#ffffff"/>
    <rect x="80" y="96" width="120" height="32" fill="#bfdbfe"/>
    <line x1="140" y1="96" x2="140" y2="128"/><line x1="200" y1="96" x2="200" y2="128"/><line x1="260" y1="96" x2="260" y2="128"/>
    <rect x="80" y="148" width="240" height="32" fill="#ffffff"/>
    <rect x="80" y="148" width="120" height="32" fill="#bfdbfe"/>
    <line x1="110" y1="148" x2="110" y2="180"/><line x1="140" y1="148" x2="140" y2="180"/><line x1="170" y1="148" x2="170" y2="180"/><line x1="200" y1="148" x2="200" y2="180"/>
    <line x1="230" y1="148" x2="230" y2="180"/><line x1="260" y1="148" x2="260" y2="180"/><line x1="290" y1="148" x2="290" y2="180"/>
  </g>
  <g font-size="12" font-weight="700" fill="{_INK}" text-anchor="end">
    <text x="68" y="65">1/2</text>
    <text x="68" y="117">2/4</text>
    <text x="68" y="169">4/8</text>
  </g>
  <text x="205" y="206" text-anchor="middle" font-size="10.5" fill="#6b7280">The shaded amount is unchanged; only the number of cuts changes.</text>
</svg>'''


# --- Common denominator bars ----------------------------------------------
_COMMON_DENOMINATOR_BARS = f'''
<svg viewBox="0 0 420 220" role="img" aria-label="Bars showing one half plus one third rewritten as three sixths plus two sixths" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Common Denominator: 1/2 + 1/3</text>
  <g stroke="{_INK}" stroke-width="1">
    <rect x="38" y="50" width="150" height="34" fill="#ffffff"/><rect x="38" y="50" width="75" height="34" fill="#bfdbfe"/><line x1="113" y1="50" x2="113" y2="84"/>
    <rect x="232" y="50" width="150" height="34" fill="#ffffff"/><rect x="232" y="50" width="50" height="34" fill="#bbf7d0"/><line x1="282" y1="50" x2="282" y2="84"/><line x1="332" y1="50" x2="332" y2="84"/>
    <rect x="38" y="128" width="150" height="34" fill="#ffffff"/><rect x="38" y="128" width="75" height="34" fill="#bfdbfe"/>
    <line x1="63" y1="128" x2="63" y2="162"/><line x1="88" y1="128" x2="88" y2="162"/><line x1="113" y1="128" x2="113" y2="162"/><line x1="138" y1="128" x2="138" y2="162"/><line x1="163" y1="128" x2="163" y2="162"/>
    <rect x="232" y="128" width="150" height="34" fill="#ffffff"/><rect x="232" y="128" width="50" height="34" fill="#bbf7d0"/>
    <line x1="257" y1="128" x2="257" y2="162"/><line x1="282" y1="128" x2="282" y2="162"/><line x1="307" y1="128" x2="307" y2="162"/><line x1="332" y1="128" x2="332" y2="162"/><line x1="357" y1="128" x2="357" y2="162"/>
  </g>
  <g font-size="12" fill="{_INK}" text-anchor="middle">
    <text x="113" y="104">1/2</text><text x="307" y="104">1/3</text>
    <text x="113" y="184">3/6</text><text x="307" y="184">2/6</text>
    <text x="210" y="119" font-weight="700" fill="#6b7280">rewrite both as sixths</text>
  </g>
</svg>'''


# --- Fraction operation map ------------------------------------------------
_FRACTION_OPERATION_MAP = f'''
<svg viewBox="0 0 430 230" role="img" aria-label="Map of fraction operations showing common denominator for addition and reciprocal for division" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="215" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Which Fraction Move?</text>
  <g text-anchor="middle">
    <rect x="25" y="48" width="170" height="62" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <text x="110" y="72" font-size="12" font-weight="700" fill="#1e3a8a">Add or Subtract</text>
    <text x="110" y="92" font-size="10.5" fill="{_INK}">same-size pieces first</text>
    <rect x="235" y="48" width="170" height="62" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
    <text x="320" y="72" font-size="12" font-weight="700" fill="#15803d">Multiply</text>
    <text x="320" y="92" font-size="10.5" fill="{_INK}">multiply straight across</text>
    <rect x="25" y="140" width="170" height="62" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
    <text x="110" y="164" font-size="12" font-weight="700" fill="#b45309">Divide</text>
    <text x="110" y="184" font-size="10.5" fill="{_INK}">keep, change, flip</text>
    <rect x="235" y="140" width="170" height="62" rx="8" fill="#fee2e2" stroke="{_RED}" stroke-width="1.5"/>
    <text x="320" y="164" font-size="12" font-weight="700" fill="#b91c1c">Word Problems</text>
    <text x="320" y="184" font-size="10.5" fill="{_INK}">draw, label, then compute</text>
  </g>
  <text x="215" y="224" text-anchor="middle" font-size="10.5" fill="#6b7280">Most mistakes come from choosing the wrong move before the arithmetic starts.</text>
</svg>'''


# --- Percent grid ----------------------------------------------------------
_PERCENT_GRID = f'''
<svg viewBox="0 0 360 260" role="img" aria-label="Hundred grid with 37 of 100 squares shaded" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="180" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Percent Means Per Hundred</text>
  <g transform="translate(70 42)" stroke="#ffffff" stroke-width="1">
    <rect x="0" y="0" width="200" height="200" fill="#ffffff" stroke="{_INK}" stroke-width="1.5"/>
    <g fill="#bfdbfe">
      <rect x="0" y="0" width="20" height="20"/><rect x="20" y="0" width="20" height="20"/><rect x="40" y="0" width="20" height="20"/><rect x="60" y="0" width="20" height="20"/><rect x="80" y="0" width="20" height="20"/><rect x="100" y="0" width="20" height="20"/><rect x="120" y="0" width="20" height="20"/><rect x="140" y="0" width="20" height="20"/><rect x="160" y="0" width="20" height="20"/><rect x="180" y="0" width="20" height="20"/>
      <rect x="0" y="20" width="20" height="20"/><rect x="20" y="20" width="20" height="20"/><rect x="40" y="20" width="20" height="20"/><rect x="60" y="20" width="20" height="20"/><rect x="80" y="20" width="20" height="20"/><rect x="100" y="20" width="20" height="20"/><rect x="120" y="20" width="20" height="20"/><rect x="140" y="20" width="20" height="20"/><rect x="160" y="20" width="20" height="20"/><rect x="180" y="20" width="20" height="20"/>
      <rect x="0" y="40" width="20" height="20"/><rect x="20" y="40" width="20" height="20"/><rect x="40" y="40" width="20" height="20"/><rect x="60" y="40" width="20" height="20"/><rect x="80" y="40" width="20" height="20"/><rect x="100" y="40" width="20" height="20"/><rect x="120" y="40" width="20" height="20"/><rect x="140" y="40" width="20" height="20"/><rect x="160" y="40" width="20" height="20"/><rect x="180" y="40" width="20" height="20"/>
      <rect x="0" y="60" width="20" height="20"/><rect x="20" y="60" width="20" height="20"/><rect x="40" y="60" width="20" height="20"/><rect x="60" y="60" width="20" height="20"/><rect x="80" y="60" width="20" height="20"/><rect x="100" y="60" width="20" height="20"/><rect x="120" y="60" width="20" height="20"/>
    </g>
    <g fill="none" stroke="#e5e7eb">
      <path d="M20,0 V200 M40,0 V200 M60,0 V200 M80,0 V200 M100,0 V200 M120,0 V200 M140,0 V200 M160,0 V200 M180,0 V200"/>
      <path d="M0,20 H200 M0,40 H200 M0,60 H200 M0,80 H200 M0,100 H200 M0,120 H200 M0,140 H200 M0,160 H200 M0,180 H200"/>
    </g>
  </g>
  <text x="180" y="252" text-anchor="middle" font-size="11" fill="#6b7280">37 shaded squares out of 100 = 37%</text>
</svg>'''


# --- Percent conversion bridge --------------------------------------------
_PERCENT_CONVERSION = f'''
<svg viewBox="0 0 410 170" role="img" aria-label="Conversion bridge showing 25 percent equals 25 over 100 equals one fourth equals 0.25" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="205" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Percent, Fraction, Decimal</text>
  <g text-anchor="middle">
    <rect x="20" y="56" width="80" height="48" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <text x="60" y="85" font-size="14" font-weight="700" fill="#1e3a8a">25%</text>
    <rect x="120" y="56" width="80" height="48" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
    <text x="160" y="78" font-size="12" font-weight="700" fill="#15803d">25/100</text>
    <text x="160" y="94" font-size="10" fill="{_INK}">per hundred</text>
    <rect x="220" y="56" width="80" height="48" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
    <text x="260" y="85" font-size="14" font-weight="700" fill="#b45309">1/4</text>
    <rect x="320" y="56" width="70" height="48" rx="8" fill="#fee2e2" stroke="{_RED}" stroke-width="1.5"/>
    <text x="355" y="85" font-size="14" font-weight="700" fill="#b91c1c">0.25</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="1.5" fill="{_AXIS}">
    <line x1="100" y1="80" x2="118" y2="80"/><polygon points="120,80 111,75 111,85"/>
    <line x1="200" y1="80" x2="218" y2="80"/><polygon points="220,80 211,75 211,85"/>
    <line x1="300" y1="80" x2="318" y2="80"/><polygon points="320,80 311,75 311,85"/>
  </g>
  <text x="205" y="140" text-anchor="middle" font-size="10.5" fill="#6b7280">Move between forms to choose the easiest calculation.</text>
</svg>'''


# --- Discount percent bar --------------------------------------------------
_PERCENT_DISCOUNT_BAR = f'''
<svg viewBox="0 0 410 190" role="img" aria-label="Bar showing 25 percent discount and 75 percent paid" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="205" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Discount: 25% Off</text>
  <rect x="50" y="58" width="300" height="42" fill="#ffffff" stroke="{_INK}" stroke-width="1.2"/>
  <rect x="50" y="58" width="75" height="42" fill="#fecaca"/>
  <rect x="125" y="58" width="225" height="42" fill="#bbf7d0"/>
  <line x1="125" y1="58" x2="125" y2="100" stroke="{_INK}" stroke-width="1"/>
  <text x="88" y="83" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c">25% off</text>
  <text x="238" y="83" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">75% paid</text>
  <text x="205" y="132" text-anchor="middle" font-size="12" fill="{_INK}">Final price = original price x 0.75</text>
  <text x="205" y="158" text-anchor="middle" font-size="10.5" fill="#6b7280">For an 80 dollar item: 0.75 x 80 = 60 dollars.</text>
</svg>'''


# --- Percent change arrow --------------------------------------------------
_PERCENT_CHANGE_ARROW = f'''
<svg viewBox="0 0 420 180" role="img" aria-label="Arrow showing percent increase from old value 50 to new value 65" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Percent Change</text>
  <rect x="45" y="60" width="90" height="46" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="90" y="80" text-anchor="middle" font-size="11" fill="{_INK}">old value</text>
  <text x="90" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#1e3a8a">50</text>
  <rect x="285" y="60" width="90" height="46" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="330" y="80" text-anchor="middle" font-size="11" fill="{_INK}">new value</text>
  <text x="330" y="98" text-anchor="middle" font-size="14" font-weight="700" fill="#15803d">65</text>
  <line x1="138" y1="83" x2="282" y2="83" stroke="{_AXIS}" stroke-width="2"/>
  <polygon points="284,83 273,77 273,89" fill="{_AXIS}"/>
  <text x="210" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309">change = 15</text>
  <text x="210" y="136" text-anchor="middle" font-size="12" fill="{_INK}">percent change = change / old value</text>
  <text x="210" y="156" text-anchor="middle" font-size="10.5" fill="#6b7280">15 / 50 = 0.30 = 30% increase</text>
</svg>'''


# --- Percent equation triangle --------------------------------------------
_PERCENT_EQUATION_TRIANGLE = f'''
<svg viewBox="0 0 360 230" role="img" aria-label="Triangle showing part equals percent times whole" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="180" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Percent Equation</text>
  <polygon points="180,46 70,190 290,190" fill="#f8fafc" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="125" y1="118" x2="235" y2="118" stroke="{_INK}" stroke-width="1"/>
  <line x1="180" y1="118" x2="180" y2="190" stroke="{_INK}" stroke-width="1"/>
  <g text-anchor="middle" font-weight="700">
    <text x="180" y="91" font-size="17" fill="#1e3a8a">Part</text>
    <text x="126" y="158" font-size="15" fill="#15803d">Percent</text>
    <text x="234" y="158" font-size="15" fill="#b45309">Whole</text>
  </g>
  <text x="180" y="215" text-anchor="middle" font-size="10.5" fill="#6b7280">Part = percent decimal x whole</text>
</svg>'''


# --- Rate double number line ----------------------------------------------
_RATE_DOUBLE_NUMBER_LINE = f'''
<svg viewBox="0 0 430 210" role="img" aria-label="Double number line showing 180 miles in 3 hours and 60 miles in 1 hour" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="215" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Rate: Two Quantities Move Together</text>
  <line x1="60" y1="76" x2="360" y2="76" stroke="{_BLUE}" stroke-width="2"/>
  <line x1="60" y1="142" x2="360" y2="142" stroke="{_GREEN}" stroke-width="2"/>
  <g stroke="{_AXIS}" stroke-width="1.5">
    <line x1="60" y1="68" x2="60" y2="150"/><line x1="160" y1="68" x2="160" y2="150"/><line x1="260" y1="68" x2="260" y2="150"/><line x1="360" y1="68" x2="360" y2="150"/>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="34" y="80" text-anchor="end" font-weight="700" fill="#1e3a8a">miles</text>
    <text x="34" y="146" text-anchor="end" font-weight="700" fill="#15803d">hours</text>
    <text x="60" y="57">0</text><text x="160" y="57">60</text><text x="260" y="57">120</text><text x="360" y="57">180</text>
    <text x="60" y="170">0</text><text x="160" y="170">1</text><text x="260" y="170">2</text><text x="360" y="170">3</text>
  </g>
  <text x="215" y="198" text-anchor="middle" font-size="10.5" fill="#6b7280">180 miles in 3 hours means 60 miles per 1 hour.</text>
</svg>'''


# --- Unit price comparison -------------------------------------------------
_UNIT_PRICE_COMPARISON = f'''
<svg viewBox="0 0 430 220" role="img" aria-label="Unit price comparison between twelve ounces for three dollars and twenty ounces for four dollars" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="215" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Best Buy: Compare Unit Prices</text>
  <g text-anchor="middle">
    <rect x="48" y="54" width="150" height="104" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
    <text x="123" y="80" font-size="12" font-weight="700" fill="#1e3a8a">Bag A</text>
    <text x="123" y="104" font-size="12" fill="{_INK}">12 oz for 3 dollars</text>
    <text x="123" y="132" font-size="13" font-weight="700" fill="{_INK}">3 / 12 = 0.25</text>
    <text x="123" y="150" font-size="10.5" fill="#6b7280">25 cents per oz</text>
    <rect x="232" y="54" width="150" height="104" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
    <text x="307" y="80" font-size="12" font-weight="700" fill="#15803d">Bag B</text>
    <text x="307" y="104" font-size="12" fill="{_INK}">20 oz for 4 dollars</text>
    <text x="307" y="132" font-size="13" font-weight="700" fill="{_INK}">4 / 20 = 0.20</text>
    <text x="307" y="150" font-size="10.5" fill="#6b7280">20 cents per oz</text>
  </g>
  <text x="215" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Lower unit price wins: Bag B is the better buy.</text>
</svg>'''


# --- Distance rate time triangle ------------------------------------------
_RATE_DISTANCE_TRIANGLE = f'''
<svg viewBox="0 0 360 230" role="img" aria-label="Triangle showing distance equals rate times time" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="180" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Distance, Rate, Time</text>
  <polygon points="180,46 70,190 290,190" fill="#f8fafc" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="125" y1="118" x2="235" y2="118" stroke="{_INK}" stroke-width="1"/>
  <line x1="180" y1="118" x2="180" y2="190" stroke="{_INK}" stroke-width="1"/>
  <g text-anchor="middle" font-weight="700">
    <text x="180" y="91" font-size="17" fill="#1e3a8a">Distance</text>
    <text x="126" y="158" font-size="16" fill="#15803d">Rate</text>
    <text x="234" y="158" font-size="16" fill="#b45309">Time</text>
  </g>
  <text x="180" y="215" text-anchor="middle" font-size="10.5" fill="#6b7280">Distance = rate x time; rate = distance / time.</text>
</svg>'''


# --- Rate graph ------------------------------------------------------------
_RATE_GRAPH = f'''
<svg viewBox="0 0 360 260" role="img" aria-label="Line graph of distance over time with slope 60 miles per hour" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="180" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Rate on a Graph</text>
  <line x1="55" y1="35" x2="55" y2="210" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="55" y1="210" x2="320" y2="210" stroke="{_AXIS}" stroke-width="1.5"/>
  <g stroke="{_GRID}">
    <line x1="55" y1="165" x2="320" y2="165"/><line x1="55" y1="120" x2="320" y2="120"/><line x1="55" y1="75" x2="320" y2="75"/>
    <line x1="122" y1="35" x2="122" y2="210"/><line x1="189" y1="35" x2="189" y2="210"/><line x1="256" y1="35" x2="256" y2="210"/>
  </g>
  <line x1="55" y1="210" x2="256" y2="75" stroke="{_BLUE}" stroke-width="2.5"/>
  <circle cx="122" cy="165" r="4" fill="{_BLUE}"/><circle cx="189" cy="120" r="4" fill="{_BLUE}"/><circle cx="256" cy="75" r="4" fill="{_BLUE}"/>
  <g font-size="10" fill="{_INK}" text-anchor="middle">
    <text x="122" y="229">1 hr</text><text x="189" y="229">2 hr</text><text x="256" y="229">3 hr</text>
    <text x="44" y="168" text-anchor="end">60</text><text x="44" y="123" text-anchor="end">120</text><text x="44" y="78" text-anchor="end">180</text>
  </g>
  <text x="185" y="58" font-size="11" font-weight="700" fill="#1e3a8a">slope = 60 miles/hour</text>
  <text x="181" y="252" text-anchor="middle" font-size="10.5" fill="#6b7280">On a distance-time graph, slope is speed.</text>
</svg>'''


# --- Work rate bars --------------------------------------------------------
_WORK_RATE_BARS = f'''
<svg viewBox="0 0 430 210" role="img" aria-label="Work rate bars showing pages typed per hour by two people" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="215" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Work Rate: Output per Time</text>
  <g font-size="11" fill="{_INK}">
    <text x="52" y="80" text-anchor="end" font-weight="700">Ava</text>
    <text x="52" y="132" text-anchor="end" font-weight="700">Ben</text>
  </g>
  <rect x="70" y="58" width="240" height="30" fill="#bfdbfe" stroke="{_BLUE}"/>
  <rect x="70" y="110" width="160" height="30" fill="#bbf7d0" stroke="{_GREEN}"/>
  <g font-size="11" fill="{_INK}">
    <text x="320" y="79">24 pages in 3 hr = 8 pages/hr</text>
    <text x="240" y="131">20 pages in 4 hr = 5 pages/hr</text>
  </g>
  <text x="215" y="182" text-anchor="middle" font-size="10.5" fill="#6b7280">Divide output by time to compare fairly.</text>
</svg>'''


# --- Ratio tape diagram ----------------------------------------------------
_RATIO_TAPE = f'''
<svg viewBox="0 0 390 170" role="img" aria-label="Tape diagram showing a ratio of 3 to 2" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Ratio Tape: 3 to 2</text>
  <text x="48" y="62" text-anchor="end" font-size="11" fill="{_INK}">Blue</text>
  <text x="48" y="114" text-anchor="end" font-size="11" fill="{_INK}">Green</text>
  <g stroke="{_INK}" stroke-width="1">
    <rect x="60" y="42" width="60" height="34" fill="#bfdbfe"/><rect x="120" y="42" width="60" height="34" fill="#bfdbfe"/><rect x="180" y="42" width="60" height="34" fill="#bfdbfe"/>
    <rect x="60" y="94" width="60" height="34" fill="#bbf7d0"/><rect x="120" y="94" width="60" height="34" fill="#bbf7d0"/>
  </g>
  <g font-size="10" fill="{_INK}" text-anchor="middle">
    <text x="90" y="63">1 part</text><text x="150" y="63">1 part</text><text x="210" y="63">1 part</text>
    <text x="90" y="115">1 part</text><text x="150" y="115">1 part</text>
  </g>
  <text x="275" y="82" font-size="11" fill="#6b7280">total parts = 5</text>
  <text x="195" y="154" text-anchor="middle" font-size="10.5" fill="#6b7280">If 5 parts are 40 students, each part is 8 students.</text>
</svg>'''


# --- Proportion cross products --------------------------------------------
_PROPORTION_CROSS_PRODUCTS = f'''
<svg viewBox="0 0 500 220" role="img" aria-label="Cross products for the proportion 3 over 4 equals x over 20" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="250" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Solving a Proportion</text>
  <text x="250" y="88" text-anchor="middle" font-size="28" font-weight="700" fill="{_INK}">3 / 4 = x / 20</text>
  <path d="M193,58 C232,40 292,40 335,58" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <path d="M183,118 C229,146 292,146 347,118" fill="none" stroke="{_RED}" stroke-width="2.5"/>
  <text x="250" y="156" text-anchor="middle" font-size="15" font-weight="700" fill="{_INK}">3 x 20 = 4 x x</text>
  <text x="250" y="184" text-anchor="middle" font-size="13" fill="#6b7280">60 = 4x, so x = 15</text>
  <text x="250" y="207" text-anchor="middle" font-size="10.5" fill="#6b7280">Cross products must use opposite corners of the proportion.</text>
</svg>'''


# --- Map scale --------------------------------------------------------------
_MAP_SCALE_DISTANCE = f'''
<svg viewBox="0 0 540 230" role="img" aria-label="Map scale showing one inch represents eight miles" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Map Scale: 1 inch = 8 miles</text>
  <rect x="60" y="52" width="420" height="112" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>
  <circle cx="130" cy="108" r="8" fill="{_BLUE}"/><text x="130" y="86" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Town A</text>
  <circle cx="370" cy="108" r="8" fill="{_RED}"/><text x="370" y="86" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Town B</text>
  <line x1="130" y1="108" x2="370" y2="108" stroke="{_INK}" stroke-width="2" stroke-dasharray="7 5"/>
  <text x="250" y="100" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">3 inches on map</text>
  <rect x="155" y="176" width="230" height="28" rx="4" fill="#ffffff" stroke="{_AXIS}"/>
  <text x="270" y="195" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">3 x 8 = 24 miles in real life</text>
</svg>'''


# --- Similar rectangles scale factor ---------------------------------------
_SIMILAR_RECTANGLES_SCALE = f'''
<svg viewBox="0 0 540 250" role="img" aria-label="Similar rectangles with side lengths scaled by a factor of three" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Similar Figures and Scale Factor</text>
  <rect x="78" y="80" width="96" height="64" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.8"/>
  <rect x="300" y="48" width="144" height="96" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.8"/>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="126" y="70">4 cm</text><text x="64" y="116" transform="rotate(-90 64 116)">3 cm</text>
    <text x="372" y="38">12 cm</text><text x="286" y="98" transform="rotate(-90 286 98)">9 cm</text>
  </g>
  <path d="M195,112 H270" stroke="{_AXIS}" stroke-width="2" fill="none"/>
  <polygon points="276,112 265,106 265,118" fill="{_AXIS}"/>
  <text x="236" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">x3</text>
  <text x="270" y="188" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Scale factor = 12 / 4 = 9 / 3 = 3</text>
  <text x="270" y="216" text-anchor="middle" font-size="10.5" fill="#6b7280">Similar figures keep the same shape; every corresponding length uses the same multiplier.</text>
</svg>'''


# --- Equation balance ------------------------------------------------------
_EQUATION_BALANCE = f'''
<svg viewBox="0 0 390 220" role="img" aria-label="Balance scale representing the equation 2x plus 5 equals 13" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Equation Balance: 2x + 5 = 13</text>
  <line x1="195" y1="70" x2="195" y2="175" stroke="{_INK}" stroke-width="2"/>
  <line x1="95" y1="75" x2="295" y2="75" stroke="{_INK}" stroke-width="2"/>
  <polygon points="195,60 185,78 205,78" fill="{_INK}"/>
  <g stroke="{_AXIS}" stroke-width="1.5" fill="none">
    <line x1="105" y1="75" x2="70" y2="125"/><line x1="105" y1="75" x2="140" y2="125"/>
    <line x1="285" y1="75" x2="250" y2="125"/><line x1="285" y1="75" x2="320" y2="125"/>
  </g>
  <ellipse cx="105" cy="130" rx="48" ry="12" fill="#dbeafe" stroke="{_BLUE}"/>
  <ellipse cx="285" cy="130" rx="48" ry="12" fill="#fee2e2" stroke="{_RED}"/>
  <g text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">
    <text x="105" y="128">x + x + 5</text>
    <text x="285" y="128">13</text>
  </g>
  <rect x="153" y="175" width="84" height="14" fill="{_AXIS}"/>
  <text x="195" y="206" text-anchor="middle" font-size="10.5" fill="#6b7280">Subtract 5 from both sides, then divide both sides by 2.</text>
</svg>'''


# --- Composite area split --------------------------------------------------
_COMPOSITE_AREA = f'''
<svg viewBox="0 0 390 260" role="img" aria-label="Composite L shaped figure split into two rectangles" xmlns="http://www.w3.org/2000/svg" style="max-width:500px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Split a Composite Shape</text>
  <path d="M85,55 H285 V115 H205 V205 H85 Z" fill="#dbeafe" stroke="{_INK}" stroke-width="1.5"/>
  <rect x="85" y="55" width="200" height="60" fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="85" y="115" width="120" height="90" fill="#bbf7d0" stroke="{_GREEN}" stroke-width="1.5"/>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="185" y="88" font-weight="700">Rectangle A</text>
    <text x="145" y="164" font-weight="700">Rectangle B</text>
    <text x="185" y="45">10 ft</text>
    <text x="302" y="88">3 ft</text>
    <text x="66" y="164">6 ft</text>
    <text x="145" y="224">6 ft</text>
  </g>
  <text x="195" y="246" text-anchor="middle" font-size="10.5" fill="#6b7280">Find each rectangle's area, then add: total area = A + B.</text>
</svg>'''


# --- Cylinder with radius and height ---------------------------------------
_CYLINDER_VOLUME = f'''
<svg viewBox="0 0 310 250" role="img" aria-label="Cylinder with radius and height labels for volume" xmlns="http://www.w3.org/2000/svg" style="max-width:390px;width:100%;height:auto;{_FONT}">
  <text x="155" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Cylinder Volume</text>
  <ellipse cx="155" cy="62" rx="72" ry="24" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <path d="M83,62 V174 C83,187 227,187 227,174 V62" fill="#eff6ff" stroke="{_BLUE}" stroke-width="1.5"/>
  <ellipse cx="155" cy="174" rx="72" ry="24" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="155" y1="62" x2="225" y2="62" stroke="{_RED}" stroke-width="2"/>
  <text x="191" y="54" text-anchor="middle" font-size="11" font-weight="700" fill="{_RED}">r</text>
  <line x1="245" y1="62" x2="245" y2="174" stroke="{_GREEN}" stroke-width="2"/>
  <g fill="{_GREEN}">
    <polygon points="245,58 240,68 250,68"/><polygon points="245,178 240,168 250,168"/>
  </g>
  <text x="260" y="121" font-size="11" font-weight="700" fill="{_GREEN}">h</text>
  <text x="155" y="222" text-anchor="middle" font-size="12" fill="{_INK}">V = pi r^2 h</text>
  <text x="155" y="238" text-anchor="middle" font-size="10" fill="#6b7280">base area times height</text>
</svg>'''


# --- Box plot --------------------------------------------------------------
_BOX_PLOT = f'''
<svg viewBox="0 0 390 150" role="img" aria-label="Box plot showing minimum, quartiles, median and maximum" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Box Plot Anatomy</text>
  <line x1="45" y1="92" x2="345" y2="92" stroke="{_AXIS}" stroke-width="1.5"/>
  <g stroke="{_AXIS}">
    <line x1="45" y1="86" x2="45" y2="98"/><line x1="105" y1="86" x2="105" y2="98"/><line x1="165" y1="86" x2="165" y2="98"/><line x1="225" y1="86" x2="225" y2="98"/><line x1="285" y1="86" x2="285" y2="98"/><line x1="345" y1="86" x2="345" y2="98"/>
  </g>
  <line x1="80" y1="72" x2="115" y2="72" stroke="{_BLUE}" stroke-width="2"/>
  <rect x="115" y="55" width="145" height="34" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="180" y1="55" x2="180" y2="89" stroke="{_RED}" stroke-width="2"/>
  <line x1="260" y1="72" x2="320" y2="72" stroke="{_BLUE}" stroke-width="2"/>
  <line x1="80" y1="61" x2="80" y2="83" stroke="{_BLUE}" stroke-width="2"/>
  <line x1="320" y1="61" x2="320" y2="83" stroke="{_BLUE}" stroke-width="2"/>
  <g font-size="9.5" fill="{_INK}" text-anchor="middle">
    <text x="80" y="43">min</text><text x="115" y="43">Q1</text><text x="180" y="43">median</text><text x="260" y="43">Q3</text><text x="320" y="43">max</text>
    <text x="45" y="116">0</text><text x="105" y="116">10</text><text x="165" y="116">20</text><text x="225" y="116">30</text><text x="285" y="116">40</text><text x="345" y="116">50</text>
  </g>
</svg>'''


# --- Scatter plot with trend line -----------------------------------------
_SCATTER_TREND = f'''
<svg viewBox="0 0 350 250" role="img" aria-label="Scatter plot with a positive trend line" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="175" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Positive Association</text>
  <line x1="48" y1="30" x2="48" y2="205" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="48" y1="205" x2="320" y2="205" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="62" y1="184" x2="298" y2="60" stroke="{_RED}" stroke-width="2" stroke-dasharray="6 4"/>
  <g fill="{_BLUE}">
    <circle cx="70" cy="174" r="4"/><circle cx="95" cy="160" r="4"/><circle cx="122" cy="150" r="4"/><circle cx="148" cy="130" r="4"/>
    <circle cx="172" cy="126" r="4"/><circle cx="200" cy="108" r="4"/><circle cx="228" cy="91" r="4"/><circle cx="262" cy="77" r="4"/><circle cx="288" cy="63" r="4"/>
  </g>
  <text x="184" y="232" text-anchor="middle" font-size="10" fill="#6b7280">As x increases, y tends to increase.</text>
</svg>'''


# --- Function machine ------------------------------------------------------
_FUNCTION_MACHINE = f'''
<svg viewBox="0 0 390 170" role="img" aria-label="Function machine where input x goes through rule 2x plus 3 to output y" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="195" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Function Machine</text>
  <rect x="140" y="52" width="110" height="62" rx="10" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="195" y="77" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309">Rule</text>
  <text x="195" y="96" text-anchor="middle" font-size="12" fill="{_INK}">multiply by 2</text>
  <text x="195" y="110" text-anchor="middle" font-size="12" fill="{_INK}">then add 3</text>
  <rect x="35" y="64" width="70" height="38" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="285" y="64" width="70" height="38" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="70" y="87" text-anchor="middle" font-size="13" font-weight="700" fill="#1e3a8a">x = 4</text>
  <text x="320" y="87" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">y = 11</text>
  <line x1="105" y1="83" x2="138" y2="83" stroke="{_AXIS}" stroke-width="1.5"/>
  <polygon points="140,83 130,78 130,88" fill="{_AXIS}"/>
  <line x1="250" y1="83" x2="283" y2="83" stroke="{_AXIS}" stroke-width="1.5"/>
  <polygon points="285,83 275,78 275,88" fill="{_AXIS}"/>
  <text x="195" y="145" text-anchor="middle" font-size="10.5" fill="#6b7280">One input must give exactly one output.</text>
</svg>'''


# --- Area: counting unit squares -------------------------------------------
_AREA_UNIT_GRID = f'''
<svg viewBox="0 0 320 230" role="img" aria-label="A 5 by 3 rectangle divided into 15 unit squares" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="160" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Area = Counting Unit Squares</text>
  <rect x="55" y="45" width="200" height="120" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <g stroke="{_BLUE}" stroke-width="1" opacity="0.6">
    <line x1="95" y1="45" x2="95" y2="165"/><line x1="135" y1="45" x2="135" y2="165"/>
    <line x1="175" y1="45" x2="175" y2="165"/><line x1="215" y1="45" x2="215" y2="165"/>
    <line x1="55" y1="85" x2="255" y2="85"/><line x1="55" y1="125" x2="255" y2="125"/>
  </g>
  <text x="155" y="38" text-anchor="middle" font-size="11" fill="{_INK}">5 units</text>
  <text x="46" y="105" text-anchor="middle" font-size="11" fill="{_INK}" transform="rotate(-90 46 105)">3 units</text>
  <text x="160" y="200" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">Area = 5 × 3 = 15 square units</text>
</svg>'''


# --- Area of a rectangle ---------------------------------------------------
_AREA_RECTANGLE = f'''
<svg viewBox="0 0 320 210" role="img" aria-label="Rectangle 8 cm by 5 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Area of a Rectangle</text>
  <rect x="65" y="52" width="190" height="95" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="160" y="44" text-anchor="middle" font-size="11.5" fill="{_INK}">length = 8 cm</text>
  <text x="52" y="100" text-anchor="middle" font-size="11.5" fill="{_INK}" transform="rotate(-90 52 100)">width = 5 cm</text>
  <text x="160" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">A = l × w = 8 × 5 = 40 cm²</text>
</svg>'''


# --- Area of a triangle ----------------------------------------------------
_AREA_TRIANGLE = f'''
<svg viewBox="0 0 320 235" role="img" aria-label="Triangle with base 10 cm and height 6 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Area of a Triangle</text>
  <polygon points="60,175 260,175 150,62" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="150" y1="62" x2="150" y2="175" stroke="{_RED}" stroke-width="1.5" stroke-dasharray="5 3"/>
  <rect x="150" y="165" width="10" height="10" fill="none" stroke="{_RED}" stroke-width="1"/>
  <text x="160" y="192" text-anchor="middle" font-size="11.5" fill="{_INK}">base = 10 cm</text>
  <text x="160" y="120" text-anchor="start" font-size="11.5" fill="{_RED}">height = 6 cm</text>
  <text x="160" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">A = ½ × b × h = ½ × 10 × 6 = 30 cm²</text>
</svg>'''


# --- Area of a parallelogram -----------------------------------------------
_AREA_PARALLELOGRAM = f'''
<svg viewBox="0 0 340 215" role="img" aria-label="Parallelogram with base 9 cm and height 4 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="170" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Area of a Parallelogram</text>
  <polygon points="70,165 250,165 290,70 110,70" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="110" y1="70" x2="110" y2="165" stroke="{_RED}" stroke-width="1.5" stroke-dasharray="5 3"/>
  <rect x="110" y="155" width="10" height="10" fill="none" stroke="{_RED}" stroke-width="1"/>
  <text x="170" y="183" text-anchor="middle" font-size="11.5" fill="{_INK}">base = 9 cm</text>
  <text x="100" y="122" text-anchor="end" font-size="11.5" fill="{_RED}">height = 4 cm</text>
  <text x="170" y="205" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">A = b × h = 9 × 4 = 36 cm²</text>
</svg>'''


# --- Area of a trapezoid ---------------------------------------------------
_AREA_TRAPEZOID = f'''
<svg viewBox="0 0 340 235" role="img" aria-label="Trapezoid with parallel sides 6 cm and 10 cm and height 4 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="170" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Area of a Trapezoid</text>
  <polygon points="55,170 285,170 230,72 110,72" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="170" y="64" text-anchor="middle" font-size="11.5" fill="{_INK}">b₁ = 6 cm</text>
  <text x="170" y="188" text-anchor="middle" font-size="11.5" fill="{_INK}">b₂ = 10 cm</text>
  <line x1="110" y1="72" x2="110" y2="170" stroke="{_RED}" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="100" y="126" text-anchor="end" font-size="11.5" fill="{_RED}">h = 4 cm</text>
  <text x="170" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">A = ½(b₁ + b₂) × h = ½(16)(4) = 32 cm²</text>
</svg>'''


# --- Area of a circle ------------------------------------------------------
_AREA_CIRCLE = f'''
<svg viewBox="0 0 280 240" role="img" aria-label="Circle with radius 7 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Area of a Circle</text>
  <circle cx="140" cy="120" r="78" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <circle cx="140" cy="120" r="3.5" fill="{_INK}"/>
  <line x1="140" y1="120" x2="218" y2="120" stroke="{_RED}" stroke-width="2"/>
  <text x="178" y="113" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_RED}">r = 7 cm</text>
  <text x="140" y="230" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">A = π r² ≈ 3.14 × 7² ≈ 153.9 cm²</text>
</svg>'''


# --- Perimeter of a rectangle ----------------------------------------------
_PERIMETER_RECTANGLE = f'''
<svg viewBox="0 0 320 210" role="img" aria-label="Rectangle 8 cm by 5 cm with all four sides labeled" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Perimeter of a Rectangle</text>
  <rect x="70" y="52" width="180" height="95" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="160" y="44" text-anchor="middle" font-size="11.5" fill="{_INK}">8 cm</text>
  <text x="160" y="162" text-anchor="middle" font-size="11.5" fill="{_INK}">8 cm</text>
  <text x="58" y="103" text-anchor="middle" font-size="11.5" fill="{_INK}" transform="rotate(-90 58 103)">5 cm</text>
  <text x="262" y="103" text-anchor="middle" font-size="11.5" fill="{_INK}" transform="rotate(90 262 103)">5 cm</text>
  <text x="160" y="190" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">P = 2(8 + 5) = 26 cm</text>
</svg>'''


# --- Perimeter of a triangle -----------------------------------------------
_PERIMETER_TRIANGLE = f'''
<svg viewBox="0 0 320 225" role="img" aria-label="Triangle with sides 13 cm, 13 cm, and 10 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Perimeter of a Triangle</text>
  <polygon points="70,180 250,180 160,58" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="103" y="118" text-anchor="end" font-size="11.5" fill="{_INK}">13 cm</text>
  <text x="217" y="118" text-anchor="start" font-size="11.5" fill="{_INK}">13 cm</text>
  <text x="160" y="197" text-anchor="middle" font-size="11.5" fill="{_INK}">10 cm</text>
  <text x="160" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">P = 13 + 13 + 10 = 36 cm</text>
</svg>'''


# --- Perimeter of a regular polygon (hexagon) ------------------------------
_PERIMETER_POLYGON = f'''
<svg viewBox="0 0 280 240" role="img" aria-label="Regular hexagon with each side 5 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Regular Hexagon</text>
  <polygon points="215,120 177.5,55 102.5,55 65,120 102.5,185 177.5,185" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="140" y="48" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_RED}">s = 5 cm</text>
  <text x="140" y="125" text-anchor="middle" font-size="10.5" fill="#6b7280">6 equal sides</text>
  <text x="140" y="222" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">P = 6 × 5 = 30 cm</text>
</svg>'''


# --- Circumference of a circle ---------------------------------------------
_CIRCLE_CIRCUMFERENCE = f'''
<svg viewBox="0 0 280 240" role="img" aria-label="Circle with diameter 10 cm" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Circumference of a Circle</text>
  <circle cx="140" cy="120" r="78" fill="#dbeafe" stroke="{_BLUE}" stroke-width="2.5"/>
  <line x1="62" y1="120" x2="218" y2="120" stroke="{_RED}" stroke-width="2"/>
  <circle cx="140" cy="120" r="3" fill="{_INK}"/>
  <text x="140" y="113" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_RED}">d = 10 cm</text>
  <text x="140" y="230" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">C = π d ≈ 3.14 × 10 = 31.4 cm</text>
</svg>'''


# --- Perimeter of a composite (L-shaped) figure ----------------------------
_PERIMETER_COMPOSITE = f'''
<svg viewBox="0 0 320 240" role="img" aria-label="L-shaped figure with all sides labeled" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Perimeter of an L-Shape</text>
  <path d="M60,50 H260 V125 H135 V200 H60 Z" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="160" y="43">8 ft</text>
    <text x="274" y="90">3 ft</text>
    <text x="197" y="142">5 ft</text>
    <text x="148" y="167">3 ft</text>
    <text x="97" y="216">3 ft</text>
    <text x="48" y="128">6 ft</text>
  </g>
  <text x="160" y="232" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_INK}">P = 8+3+5+3+3+6 = 28 ft</text>
</svg>'''


# --- Volume of a rectangular prism (box) -----------------------------------
_VOLUME_BOX = f'''
<svg viewBox="0 0 320 240" role="img" aria-label="Rectangular prism 5 by 4 by 3" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Rectangular Prism (Box)</text>
  <polygon points="70,95 200,95 240,60 110,60" fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.5"/>
  <polygon points="200,95 240,60 240,155 200,190" fill="#93c5fd" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="70" y="95" width="130" height="95" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="135" y="208" text-anchor="middle" font-size="11.5" fill="{_INK}">length = 5</text>
  <text x="60" y="145" text-anchor="middle" font-size="11.5" fill="{_INK}" transform="rotate(-90 60 145)">height = 3</text>
  <text x="228" y="80" text-anchor="start" font-size="11.5" fill="{_INK}">width = 4</text>
  <text x="160" y="228" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">V = l × w × h = 5 × 4 × 3 = 60</text>
</svg>'''


# --- Volume of a cube ------------------------------------------------------
_VOLUME_CUBE = f'''
<svg viewBox="0 0 300 240" role="img" aria-label="Cube with side 4" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="150" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Cube</text>
  <polygon points="80,85 190,85 228,52 118,52" fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.5"/>
  <polygon points="190,85 228,52 228,162 190,195" fill="#93c5fd" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="80" y="85" width="110" height="110" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="135" y="212" text-anchor="middle" font-size="11.5" fill="{_INK}">s = 4</text>
  <text x="150" y="228" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">V = s³ = 4³ = 64</text>
</svg>'''


# --- Volume of a cone ------------------------------------------------------
_VOLUME_CONE = f'''
<svg viewBox="0 0 280 250" role="img" aria-label="Cone with radius 3 and height 4" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Cone</text>
  <ellipse cx="140" cy="180" rx="72" ry="22" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <path d="M68,180 L140,52 L212,180" fill="#eff6ff" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="140" y1="52" x2="140" y2="180" stroke="#16a34a" stroke-width="1.5" stroke-dasharray="5 3"/>
  <text x="150" y="120" text-anchor="start" font-size="11.5" font-weight="700" fill="#16a34a">h = 4</text>
  <line x1="140" y1="180" x2="212" y2="180" stroke="{_RED}" stroke-width="2"/>
  <text x="178" y="173" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_RED}">r = 3</text>
  <text x="140" y="232" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">V = (1/3) × π × r² × h</text>
</svg>'''


# --- Volume of a sphere ----------------------------------------------------
_VOLUME_SPHERE = f'''
<svg viewBox="0 0 260 250" role="img" aria-label="Sphere with radius 3" xmlns="http://www.w3.org/2000/svg" style="max-width:340px;width:100%;height:auto;{_FONT}">
  <text x="130" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Sphere</text>
  <circle cx="130" cy="128" r="85" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <ellipse cx="130" cy="128" rx="85" ry="24" fill="none" stroke="{_BLUE}" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="130" y1="128" x2="215" y2="128" stroke="{_RED}" stroke-width="2"/>
  <circle cx="130" cy="128" r="3" fill="{_INK}"/>
  <text x="172" y="121" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_RED}">r = 3</text>
  <text x="130" y="236" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">V = (4/3) × π × r³</text>
</svg>'''


# --- Net of a box (surface area) -------------------------------------------
_SURFACE_NET = f'''
<svg viewBox="0 0 340 260" role="img" aria-label="Net of a box showing six faces" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="170" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Net of a Box: 6 Faces</text>
  <g stroke="{_BLUE}" stroke-width="1.5" font-size="10.5" text-anchor="middle">
    <rect x="90" y="40" width="70" height="55" fill="#bfdbfe"/><text x="125" y="72" fill="{_INK}">Top</text>
    <rect x="20" y="95" width="70" height="70" fill="#dbeafe"/><text x="55" y="134" fill="{_INK}">Side</text>
    <rect x="90" y="95" width="70" height="70" fill="#93c5fd"/><text x="125" y="134" fill="{_INK}">Front</text>
    <rect x="160" y="95" width="70" height="70" fill="#dbeafe"/><text x="195" y="134" fill="{_INK}">Side</text>
    <rect x="230" y="95" width="70" height="70" fill="#bfdbfe"/><text x="265" y="134" fill="{_INK}">Back</text>
    <rect x="90" y="165" width="70" height="55" fill="#bfdbfe"/><text x="125" y="197" fill="{_INK}">Bottom</text>
  </g>
  <text x="170" y="245" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_INK}">Surface area = add the areas of all 6 faces</text>
</svg>'''


# --- Cylinder surface as a net ---------------------------------------------
_SURFACE_CYLINDER = f'''
<svg viewBox="0 0 340 200" role="img" aria-label="Cylinder surface as two circles plus a rectangle" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="170" y="20" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Cylinder Surface = 2 Circles + a Rectangle</text>
  <circle cx="65" cy="70" r="30" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="65" y="73" text-anchor="middle" font-size="9.5" fill="{_INK}">top</text>
  <circle cx="65" cy="140" r="30" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="65" y="143" text-anchor="middle" font-size="9.5" fill="{_INK}">bottom</text>
  <rect x="120" y="55" width="190" height="100" fill="#eff6ff" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="215" y="100" text-anchor="middle" font-size="11" fill="{_INK}">the wrap-around</text>
  <text x="215" y="116" text-anchor="middle" font-size="10" fill="#6b7280">width = circumference (2πr), height = h</text>
  <text x="170" y="186" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">SA = 2πr² + 2πrh</text>
</svg>'''


# --- Pythagorean theorem: labeled right triangle ---------------------------
_PYTHAGOREAN_TRIANGLE = f'''
<svg viewBox="0 0 320 240" role="img" aria-label="Right triangle with legs a and b and hypotenuse c" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Pythagorean Theorem</text>
  <polygon points="80,65 80,175 250,175" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <polygon points="80,175 80,160 95,160 95,175" fill="none" stroke="{_RED}" stroke-width="1.2"/>
  <text x="70" y="122" text-anchor="end" font-size="12" font-weight="700" fill="{_INK}">a</text>
  <text x="165" y="193" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">b</text>
  <text x="173" y="112" text-anchor="start" font-size="12" font-weight="700" fill="{_RED}">c</text>
  <text x="120" y="205" text-anchor="middle" font-size="9.5" fill="#6b7280">legs a, b · hypotenuse c (opposite the right angle)</text>
  <text x="160" y="226" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">a² + b² = c²</text>
</svg>'''


# --- The 3-4-5 triangle with squares on the legs ---------------------------
_RIGHT_TRIANGLE_345 = f'''
<svg viewBox="0 0 260 320" role="img" aria-label="A 3-4-5 right triangle with squares of area 9 and 16 on the legs" xmlns="http://www.w3.org/2000/svg" style="max-width:340px;width:100%;height:auto;{_FONT}">
  <text x="130" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The 3-4-5 Triangle</text>
  <rect x="20" y="80" width="90" height="90" fill="#fee2e2" stroke="{_RED}" stroke-width="1.2"/>
  <text x="65" y="130" text-anchor="middle" font-size="13" font-weight="700" fill="{_RED}">9</text>
  <rect x="110" y="170" width="120" height="120" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
  <text x="170" y="236" text-anchor="middle" font-size="13" font-weight="700" fill="#16a34a">16</text>
  <polygon points="110,80 110,170 230,170" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="122" y="128" text-anchor="start" font-size="11.5" font-weight="700" fill="{_INK}">3</text>
  <text x="170" y="162" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_INK}">4</text>
  <text x="178" y="118" text-anchor="start" font-size="11.5" font-weight="700" fill="{_BLUE}">5</text>
  <text x="130" y="312" text-anchor="middle" font-size="12.5" font-weight="700" fill="{_INK}">3² + 4² = 5²  →  9 + 16 = 25</text>
</svg>'''


# --- Coordinate plane with four quadrants ----------------------------------
_COORDINATE_QUADRANTS = f'''
<svg viewBox="0 0 260 260" role="img" aria-label="Coordinate plane with four labeled quadrants and the point (3, 2)" xmlns="http://www.w3.org/2000/svg" style="max-width:340px;width:100%;height:auto;{_FONT}">
  <text x="130" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">The Coordinate Plane</text>
  <g stroke="{_GRID}">
    <line x1="50" y1="50" x2="50" y2="230"/><line x1="90" y1="50" x2="90" y2="230"/><line x1="170" y1="50" x2="170" y2="230"/><line x1="210" y1="50" x2="210" y2="230"/>
    <line x1="50" y1="50" x2="210" y2="50"/><line x1="50" y1="90" x2="210" y2="90"/><line x1="50" y1="170" x2="210" y2="170"/><line x1="50" y1="210" x2="210" y2="210"/>
  </g>
  <line x1="50" y1="130" x2="210" y2="130" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="130" y1="50" x2="130" y2="230" stroke="{_AXIS}" stroke-width="1.5"/>
  <text x="214" y="126" font-size="10" fill="#6b7280">x</text>
  <text x="135" y="58" font-size="10" fill="#6b7280">y</text>
  <g font-size="11" font-weight="700" fill="#9ca3af" text-anchor="middle">
    <text x="180" y="80">I</text><text x="80" y="80">II</text><text x="80" y="190">III</text><text x="180" y="190">IV</text>
  </g>
  <circle cx="190" cy="90" r="4" fill="{_BLUE}"/>
  <text x="196" y="84" font-size="10.5" font-weight="700" fill="{_BLUE}">(3, 2)</text>
</svg>'''


# --- Distance between two points as a right triangle on the grid ------------
_DISTANCE_ON_GRID = f'''
<svg viewBox="0 0 280 250" role="img" aria-label="Distance from (1,1) to (5,4) found with a right triangle of legs 4 and 3" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Distance = Pythagoras on the Grid</text>
  <g stroke="{_GRID}">
    <line x1="40" y1="50" x2="40" y2="210"/><line x1="72" y1="50" x2="72" y2="210"/><line x1="104" y1="50" x2="104" y2="210"/><line x1="136" y1="50" x2="136" y2="210"/><line x1="168" y1="50" x2="168" y2="210"/><line x1="200" y1="50" x2="200" y2="210"/>
    <line x1="40" y1="50" x2="200" y2="50"/><line x1="40" y1="82" x2="200" y2="82"/><line x1="40" y1="114" x2="200" y2="114"/><line x1="40" y1="146" x2="200" y2="146"/><line x1="40" y1="178" x2="200" y2="178"/>
  </g>
  <line x1="72" y1="178" x2="200" y2="178" stroke="{_RED}" stroke-width="2"/>
  <line x1="200" y1="178" x2="200" y2="82" stroke="#16a34a" stroke-width="2"/>
  <line x1="72" y1="178" x2="200" y2="82" stroke="{_BLUE}" stroke-width="2.5"/>
  <circle cx="72" cy="178" r="4" fill="{_INK}"/><circle cx="200" cy="82" r="4" fill="{_INK}"/>
  <text x="60" y="195" font-size="10" font-weight="700" fill="{_INK}">A(1,1)</text>
  <text x="206" y="80" font-size="10" font-weight="700" fill="{_INK}">B(5,4)</text>
  <text x="136" y="194" text-anchor="middle" font-size="11" font-weight="700" fill="{_RED}">4</text>
  <text x="208" y="134" font-size="11" font-weight="700" fill="#16a34a">3</text>
  <text x="118" y="124" font-size="11" font-weight="700" fill="{_BLUE}">5</text>
  <text x="140" y="232" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_INK}">d = √(4² + 3²) = √25 = 5</text>
</svg>'''


# --- Midpoint of a segment -------------------------------------------------
_MIDPOINT_GRID = f'''
<svg viewBox="0 0 280 250" role="img" aria-label="Midpoint of the segment from (2,1) to (8,5) is (5,3)" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Midpoint = Average the Coordinates</text>
  <g stroke="{_GRID}">
    <line x1="35" y1="45" x2="35" y2="215"/><line x1="87" y1="45" x2="87" y2="215"/><line x1="139" y1="45" x2="139" y2="215"/><line x1="191" y1="45" x2="191" y2="215"/><line x1="243" y1="45" x2="243" y2="215"/>
    <line x1="35" y1="45" x2="243" y2="45"/><line x1="35" y1="93" x2="243" y2="93"/><line x1="35" y1="137" x2="243" y2="137"/><line x1="35" y1="189" x2="243" y2="189"/>
  </g>
  <line x1="87" y1="189" x2="243" y2="85" stroke="{_BLUE}" stroke-width="2"/>
  <circle cx="87" cy="189" r="4" fill="{_INK}"/><circle cx="243" cy="85" r="4" fill="{_INK}"/>
  <circle cx="165" cy="137" r="5" fill="{_RED}"/>
  <text x="75" y="205" font-size="10" font-weight="700" fill="{_INK}">A(2,1)</text>
  <text x="222" y="80" font-size="10" font-weight="700" fill="{_INK}">B(8,5)</text>
  <text x="172" y="132" font-size="10.5" font-weight="700" fill="{_RED}">M(5,3)</text>
  <text x="140" y="234" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">M = ((2+8)/2, (1+5)/2) = (5, 3)</text>
</svg>'''


# --- Types of angles -------------------------------------------------------
_ANGLE_TYPES = f'''
<svg viewBox="0 0 460 150" role="img" aria-label="Acute, right, obtuse, and straight angles" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Types of Angles</text>
  <g stroke="{_BLUE}" stroke-width="2" fill="none">
    <path d="M95,115 L35,115 L75,64"/>
    <path d="M210,115 L150,115 L150,55"/>
    <path d="M335,115 L270,115 L225,72"/>
    <path d="M365,115 L440,115"/>
  </g>
  <rect x="150" y="100" width="15" height="15" fill="none" stroke="{_RED}" stroke-width="1.2"/>
  <circle cx="402" cy="115" r="3" fill="{_INK}"/>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="60" y="140">Acute &lt; 90°</text>
    <text x="177" y="140">Right = 90°</text>
    <text x="295" y="140">Obtuse 90°–180°</text>
    <text x="402" y="140">Straight = 180°</text>
  </g>
</svg>'''


# --- Complementary and supplementary angles --------------------------------
_COMP_SUPP = f'''
<svg viewBox="0 0 460 195" role="img" aria-label="Complementary angles summing to 90 and supplementary angles summing to 180" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Complementary &amp; Supplementary</text>
  <g stroke="{_BLUE}" stroke-width="2" fill="none">
    <path d="M190,150 L70,150 L70,45"/>
    <line x1="70" y1="150" x2="165" y2="72"/>
  </g>
  <rect x="70" y="135" width="15" height="15" fill="none" stroke="{_RED}" stroke-width="1.2"/>
  <text x="150" y="140" font-size="11" fill="{_INK}">35°</text>
  <text x="92" y="95" font-size="11" fill="{_INK}">55°</text>
  <text x="125" y="180" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">35° + 55° = 90°</text>
  <g stroke="{_BLUE}" stroke-width="2" fill="none">
    <line x1="245" y1="150" x2="435" y2="150"/>
    <line x1="340" y1="150" x2="375" y2="68"/>
  </g>
  <text x="305" y="140" font-size="11" fill="{_INK}">110°</text>
  <text x="392" y="142" font-size="11" fill="{_INK}">70°</text>
  <text x="340" y="180" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">110° + 70° = 180°</text>
</svg>'''


# --- Vertical angles -------------------------------------------------------
_VERTICAL_ANGLES = f'''
<svg viewBox="0 0 300 230" role="img" aria-label="Two intersecting lines forming equal vertical angles" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="150" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Vertical Angles</text>
  <line x1="40" y1="60" x2="260" y2="180" stroke="{_BLUE}" stroke-width="2"/>
  <line x1="40" y1="180" x2="260" y2="60" stroke="{_BLUE}" stroke-width="2"/>
  <g font-size="12" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="150" y="95">70°</text>
    <text x="150" y="160">70°</text>
    <text x="95" y="128">110°</text>
    <text x="205" y="128">110°</text>
  </g>
  <text x="150" y="215" text-anchor="middle" font-size="10.5" fill="#6b7280">Vertical angles are equal; a straight pair adds to 180°.</text>
</svg>'''


# --- Parallel lines cut by a transversal -----------------------------------
_PARALLEL_TRANSVERSAL = f'''
<svg viewBox="0 0 320 235" role="img" aria-label="Two parallel lines cut by a transversal" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="18" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Parallel Lines &amp; a Transversal</text>
  <line x1="30" y1="80" x2="290" y2="80" stroke="{_BLUE}" stroke-width="2"/>
  <line x1="30" y1="170" x2="290" y2="170" stroke="{_BLUE}" stroke-width="2"/>
  <line x1="90" y1="40" x2="230" y2="210" stroke="{_AXIS}" stroke-width="2"/>
  <polyline points="150,74 156,80 150,86" fill="none" stroke="{_BLUE}" stroke-width="1.3"/>
  <polyline points="150,164 156,170 150,176" fill="none" stroke="{_BLUE}" stroke-width="1.3"/>
  <circle cx="123" cy="80" r="3" fill="{_INK}"/><circle cx="197" cy="170" r="3" fill="{_INK}"/>
  <text x="138" y="72" font-size="11" font-weight="700" fill="{_RED}">110°</text>
  <text x="212" y="162" font-size="11" font-weight="700" fill="{_RED}">110°</text>
  <text x="160" y="227" text-anchor="middle" font-size="10" fill="#6b7280">Corresponding angles are equal; co-interior angles add to 180°.</text>
</svg>'''


# --- Triangles by sides ----------------------------------------------------
_TRIANGLE_TYPES_SIDES = f'''
<svg viewBox="0 0 420 170" role="img" aria-label="Equilateral, isosceles, and scalene triangles" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Triangles by Sides</text>
  <polygon points="35,130 115,130 75,55" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <g stroke="{_RED}" stroke-width="1.5">
    <line x1="73" y1="130" x2="77" y2="130"/><line x1="51" y1="90" x2="57" y2="94"/><line x1="93" y1="94" x2="99" y2="90"/>
  </g>
  <text x="75" y="150" text-anchor="middle" font-size="10.5" fill="{_INK}">Equilateral</text>
  <text x="75" y="163" text-anchor="middle" font-size="9" fill="#6b7280">all sides equal</text>
  <polygon points="170,130 250,130 210,55" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <g stroke="{_RED}" stroke-width="1.5">
    <line x1="186" y1="90" x2="192" y2="94"/><line x1="228" y1="94" x2="234" y2="90"/>
  </g>
  <text x="210" y="150" text-anchor="middle" font-size="10.5" fill="{_INK}">Isosceles</text>
  <text x="210" y="163" text-anchor="middle" font-size="9" fill="#6b7280">two sides equal</text>
  <polygon points="300,130 400,130 330,55" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="350" y="150" text-anchor="middle" font-size="10.5" fill="{_INK}">Scalene</text>
  <text x="350" y="163" text-anchor="middle" font-size="9" fill="#6b7280">no sides equal</text>
</svg>'''


# --- Triangle angle sum ----------------------------------------------------
_TRIANGLE_ANGLE_SUM = f'''
<svg viewBox="0 0 300 220" role="img" aria-label="A triangle with interior angles 50, 60, and 70 degrees" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="150" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Triangle Angle Sum</text>
  <polygon points="40,175 250,175 150,50" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="62" y="168" font-size="12" font-weight="700" fill="{_INK}">50°</text>
  <text x="222" y="168" font-size="12" font-weight="700" fill="{_INK}">60°</text>
  <text x="150" y="78" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">70°</text>
  <text x="150" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">50° + 60° + 70° = 180°</text>
</svg>'''


# --- Exterior angle of a triangle ------------------------------------------
_EXTERIOR_ANGLE = f'''
<svg viewBox="0 0 320 210" role="img" aria-label="A triangle with an exterior angle equal to the sum of the two remote interior angles" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;width:100%;height:auto;{_FONT}">
  <text x="160" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Exterior Angle of a Triangle</text>
  <line x1="40" y1="160" x2="300" y2="160" stroke="{_AXIS}" stroke-width="1.5"/>
  <polygon points="40,160 220,160 110,55" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="62" y="153" font-size="11.5" font-weight="700" fill="{_INK}">70°</text>
  <text x="110" y="82" text-anchor="middle" font-size="11.5" font-weight="700" fill="{_INK}">60°</text>
  <path d="M245,160 A 26 26 0 0 0 232,138" fill="none" stroke="{_RED}" stroke-width="1.5"/>
  <text x="250" y="150" font-size="11.5" font-weight="700" fill="{_RED}">130°</text>
  <text x="160" y="197" text-anchor="middle" font-size="10" fill="#6b7280">Exterior angle = sum of the two remote interior angles: 70 + 60 = 130.</text>
</svg>'''


# --- Physical Science: states of matter ------------------------------------
_STATES_OF_MATTER = f'''
<svg viewBox="0 0 460 192" role="img" aria-label="Particle arrangement in solids, liquids, and gases" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">States of Matter</text>
  <g stroke="{_AXIS}" stroke-width="1.5" fill="none">
    <rect x="30" y="40" width="110" height="108" rx="4"/>
    <rect x="175" y="40" width="110" height="108" rx="4"/>
    <rect x="320" y="40" width="110" height="108" rx="4"/>
  </g>
  <g fill="{_BLUE}">
    <circle cx="52" cy="62" r="8"/><circle cx="78" cy="62" r="8"/><circle cx="104" cy="62" r="8"/><circle cx="130" cy="62" r="8"/>
    <circle cx="52" cy="86" r="8"/><circle cx="78" cy="86" r="8"/><circle cx="104" cy="86" r="8"/><circle cx="130" cy="86" r="8"/>
    <circle cx="52" cy="110" r="8"/><circle cx="78" cy="110" r="8"/><circle cx="104" cy="110" r="8"/><circle cx="130" cy="110" r="8"/>
    <circle cx="52" cy="134" r="8"/><circle cx="78" cy="134" r="8"/><circle cx="104" cy="134" r="8"/><circle cx="130" cy="134" r="8"/>
  </g>
  <g fill="{_BLUE}">
    <circle cx="193" cy="138" r="8"/><circle cx="215" cy="141" r="8"/><circle cx="237" cy="137" r="8"/><circle cx="259" cy="141" r="8"/><circle cx="280" cy="135" r="8"/>
    <circle cx="202" cy="118" r="8"/><circle cx="226" cy="121" r="8"/><circle cx="250" cy="116" r="8"/><circle cx="273" cy="120" r="8"/>
    <circle cx="212" cy="99" r="8"/><circle cx="248" cy="98" r="8"/>
  </g>
  <g fill="{_BLUE}">
    <circle cx="338" cy="70" r="8"/><circle cx="402" cy="62" r="8"/><circle cx="360" cy="108" r="8"/>
    <circle cx="416" cy="120" r="8"/><circle cx="333" cy="134" r="8"/><circle cx="392" cy="138" r="8"/>
  </g>
  <g text-anchor="middle">
    <text x="85" y="166" font-size="12" font-weight="700" fill="{_INK}">Solid</text>
    <text x="230" y="166" font-size="12" font-weight="700" fill="{_INK}">Liquid</text>
    <text x="375" y="166" font-size="12" font-weight="700" fill="{_INK}">Gas</text>
    <text x="85" y="182" font-size="9.5" fill="#6b7280">packed, fixed shape</text>
    <text x="230" y="182" font-size="9.5" fill="#6b7280">close, flows to fit</text>
    <text x="375" y="182" font-size="9.5" fill="#6b7280">far apart, fills space</text>
  </g>
</svg>'''


# --- Physical Science: atom structure --------------------------------------
_ATOM_STRUCTURE = f'''
<svg viewBox="0 0 360 268" role="img" aria-label="An atom with a nucleus of protons and neutrons surrounded by electrons on two shells" xmlns="http://www.w3.org/2000/svg" style="max-width:420px;width:100%;height:auto;{_FONT}">
  <text x="180" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Structure of an Atom</text>
  <g fill="none" stroke="{_AXIS}" stroke-width="1.2">
    <circle cx="180" cy="142" r="58"/>
    <circle cx="180" cy="142" r="98"/>
  </g>
  <g fill="#dc2626">
    <circle cx="174" cy="138" r="8"/><circle cx="189" cy="136" r="8"/><circle cx="181" cy="151" r="8"/>
  </g>
  <g fill="#94a3b8">
    <circle cx="171" cy="151" r="8"/><circle cx="191" cy="150" r="8"/><circle cx="183" cy="125" r="8"/>
  </g>
  <g fill="{_BLUE}" stroke="#1e3a8a" stroke-width="1">
    <circle cx="180" cy="84" r="7"/><circle cx="180" cy="200" r="7"/>
    <circle cx="278" cy="142" r="7"/><circle cx="106" cy="98" r="7"/>
  </g>
  <g font-size="11">
    <circle cx="44" cy="232" r="7" fill="#dc2626"/><text x="56" y="236" fill="{_INK}">Proton (+)</text>
    <circle cx="146" cy="232" r="7" fill="#94a3b8"/><text x="158" y="236" fill="{_INK}">Neutron</text>
    <circle cx="252" cy="232" r="7" fill="{_BLUE}"/><text x="264" y="236" fill="{_INK}">Electron (&#8722;)</text>
  </g>
  <text x="180" y="258" text-anchor="middle" font-size="9.5" fill="#6b7280">Protons + neutrons sit in the nucleus; electrons orbit in shells.</text>
</svg>'''


# --- Physical Science: periodic table guide --------------------------------
_PERIODIC_TABLE_GUIDE = f'''
<svg viewBox="0 0 560 338" role="img" aria-label="Simplified periodic table guide showing groups, periods, metals, nonmetals, metalloids, and how to read an element box" xmlns="http://www.w3.org/2000/svg" style="max-width:680px;width:100%;height:auto;{_FONT}">
  <text x="280" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How to Use the Periodic Table</text>

  <g font-size="8.5" fill="#6b7280" text-anchor="middle">
    <text x="70" y="47">1</text><text x="95" y="47">2</text><text x="145" y="47">3-12</text>
    <text x="270" y="47">13</text><text x="295" y="47">14</text><text x="320" y="47">15</text><text x="345" y="47">16</text><text x="370" y="47">17</text><text x="395" y="47">18</text>
    <text x="31" y="71">1</text><text x="31" y="96">2</text><text x="31" y="121">3</text><text x="31" y="146">4</text><text x="31" y="171">5</text><text x="31" y="196">6</text>
  </g>

  <g stroke="{_AXIS}" stroke-width="1">
    <rect x="58" y="54" width="24" height="24" fill="#fee2e2"/><rect x="383" y="54" width="24" height="24" fill="#dcfce7"/>
    <rect x="58" y="79" width="24" height="24" fill="#dbeafe"/><rect x="83" y="79" width="24" height="24" fill="#dbeafe"/>
    <rect x="258" y="79" width="24" height="24" fill="#e0f2fe"/><rect x="283" y="79" width="24" height="24" fill="#dcfce7"/><rect x="308" y="79" width="24" height="24" fill="#dcfce7"/><rect x="333" y="79" width="24" height="24" fill="#dcfce7"/><rect x="358" y="79" width="24" height="24" fill="#dcfce7"/><rect x="383" y="79" width="24" height="24" fill="#dcfce7"/>
    <rect x="58" y="104" width="24" height="24" fill="#dbeafe"/><rect x="83" y="104" width="24" height="24" fill="#dbeafe"/>
    <rect x="108" y="104" width="149" height="24" fill="#dbeafe"/><rect x="258" y="104" width="24" height="24" fill="#dbeafe"/><rect x="283" y="104" width="24" height="24" fill="#e0f2fe"/><rect x="308" y="104" width="24" height="24" fill="#dcfce7"/><rect x="333" y="104" width="24" height="24" fill="#dcfce7"/><rect x="358" y="104" width="24" height="24" fill="#dcfce7"/><rect x="383" y="104" width="24" height="24" fill="#dcfce7"/>
    <rect x="58" y="129" width="24" height="24" fill="#dbeafe"/><rect x="83" y="129" width="24" height="24" fill="#dbeafe"/>
    <rect x="108" y="129" width="149" height="24" fill="#dbeafe"/><rect x="258" y="129" width="24" height="24" fill="#dbeafe"/><rect x="283" y="129" width="24" height="24" fill="#dbeafe"/><rect x="308" y="129" width="24" height="24" fill="#e0f2fe"/><rect x="333" y="129" width="24" height="24" fill="#dcfce7"/><rect x="358" y="129" width="24" height="24" fill="#dcfce7"/><rect x="383" y="129" width="24" height="24" fill="#dcfce7"/>
    <rect x="58" y="154" width="24" height="24" fill="#dbeafe"/><rect x="83" y="154" width="24" height="24" fill="#dbeafe"/>
    <rect x="108" y="154" width="149" height="24" fill="#dbeafe"/><rect x="258" y="154" width="24" height="24" fill="#dbeafe"/><rect x="283" y="154" width="24" height="24" fill="#dbeafe"/><rect x="308" y="154" width="24" height="24" fill="#dbeafe"/><rect x="333" y="154" width="24" height="24" fill="#e0f2fe"/><rect x="358" y="154" width="24" height="24" fill="#dcfce7"/><rect x="383" y="154" width="24" height="24" fill="#dcfce7"/>
    <rect x="58" y="179" width="24" height="24" fill="#dbeafe"/><rect x="83" y="179" width="24" height="24" fill="#dbeafe"/>
    <rect x="108" y="179" width="149" height="24" fill="#dbeafe"/><rect x="258" y="179" width="24" height="24" fill="#dbeafe"/><rect x="283" y="179" width="24" height="24" fill="#dbeafe"/><rect x="308" y="179" width="24" height="24" fill="#dbeafe"/><rect x="333" y="179" width="24" height="24" fill="#e0f2fe"/><rect x="358" y="179" width="24" height="24" fill="#dcfce7"/><rect x="383" y="179" width="24" height="24" fill="#dcfce7"/>
  </g>

  <g font-size="8" text-anchor="middle" font-weight="700" fill="{_INK}">
    <text x="70" y="69">H</text><text x="395" y="69">He</text>
    <text x="70" y="94">Li</text><text x="95" y="94">Be</text><text x="270" y="94">B</text><text x="295" y="94">C</text><text x="320" y="94">N</text><text x="345" y="94">O</text><text x="370" y="94">F</text><text x="395" y="94">Ne</text>
    <text x="70" y="119">Na</text><text x="95" y="119">Mg</text><text x="182" y="119">transition metals</text><text x="270" y="119">Al</text><text x="295" y="119">Si</text><text x="320" y="119">P</text><text x="345" y="119">S</text><text x="370" y="119">Cl</text><text x="395" y="119">Ar</text>
    <text x="70" y="144">K</text><text x="95" y="144">Ca</text><text x="270" y="144">Ga</text><text x="295" y="144">Ge</text><text x="320" y="144">As</text><text x="345" y="144">Se</text><text x="370" y="144">Br</text><text x="395" y="144">Kr</text>
    <text x="70" y="169">Rb</text><text x="95" y="169">Sr</text><text x="270" y="169">In</text><text x="295" y="169">Sn</text><text x="320" y="169">Sb</text><text x="345" y="169">Te</text><text x="370" y="169">I</text><text x="395" y="169">Xe</text>
    <text x="70" y="194">Cs</text><text x="95" y="194">Ba</text><text x="270" y="194">Tl</text><text x="295" y="194">Pb</text><text x="320" y="194">Bi</text><text x="345" y="194">Po</text><text x="370" y="194">At</text><text x="395" y="194">Rn</text>
  </g>

  <g stroke="{_RED}" stroke-width="1.5" fill="none">
    <rect x="333" y="79" width="24" height="24"/>
    <path d="M345,103 C365,132 410,154 438,176"/>
  </g>

  <g>
    <rect x="440" y="58" width="82" height="98" rx="4" fill="#ffffff" stroke="{_RED}" stroke-width="1.6"/>
    <text x="449" y="76" font-size="11" font-weight="700" fill="{_RED}">8</text>
    <text x="481" y="105" text-anchor="middle" font-size="30" font-weight="800" fill="{_INK}">O</text>
    <text x="481" y="124" text-anchor="middle" font-size="10.5" fill="{_INK}">Oxygen</text>
    <text x="481" y="143" text-anchor="middle" font-size="11" font-weight="700" fill="{_RED}">16.00</text>
    <g font-size="9" fill="#6b7280">
      <line x1="449" y1="73" x2="420" y2="73" stroke="{_AXIS}"/><text x="306" y="76">atomic number = protons</text>
      <line x1="481" y1="143" x2="420" y2="174" stroke="{_AXIS}"/><text x="308" y="177">atomic mass: round for mass number</text>
    </g>
  </g>

  <g font-size="10" fill="{_INK}">
    <text x="58" y="225" font-weight="700">Groups</text><text x="106" y="225" fill="#6b7280">columns; elements in a group often behave similarly</text>
    <text x="58" y="244" font-weight="700">Periods</text><text x="106" y="244" fill="#6b7280">rows; atomic number increases as you move left to right</text>
    <rect x="58" y="260" width="12" height="12" fill="#dbeafe" stroke="{_AXIS}"/><text x="76" y="270" fill="#6b7280">metals</text>
    <rect x="128" y="260" width="12" height="12" fill="#e0f2fe" stroke="{_AXIS}"/><text x="146" y="270" fill="#6b7280">metalloids</text>
    <rect x="223" y="260" width="12" height="12" fill="#dcfce7" stroke="{_AXIS}"/><text x="241" y="270" fill="#6b7280">nonmetals</text>
    <text x="58" y="300" font-weight="700">GED shortcut:</text>
    <text x="145" y="300" fill="#6b7280">neutral atom: protons = electrons; neutrons ~= rounded mass - protons.</text>
  </g>
</svg>'''


# --- Physical Science: conservation of mass --------------------------------
_CONSERVATION_MASS = f'''
<svg viewBox="0 0 400 222" role="img" aria-label="A balanced scale showing the same atoms before and after a reaction" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="200" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Conservation of Mass</text>
  <line x1="200" y1="78" x2="200" y2="185" stroke="{_INK}" stroke-width="2"/>
  <line x1="160" y1="185" x2="240" y2="185" stroke="{_INK}" stroke-width="2"/>
  <line x1="80" y1="78" x2="320" y2="78" stroke="{_INK}" stroke-width="2"/>
  <polygon points="200,66 191,84 209,84" fill="{_INK}"/>
  <g stroke="{_AXIS}" stroke-width="1.4" fill="none">
    <line x1="110" y1="78" x2="74" y2="122"/><line x1="110" y1="78" x2="146" y2="122"/>
    <line x1="290" y1="78" x2="254" y2="122"/><line x1="290" y1="78" x2="326" y2="122"/>
  </g>
  <ellipse cx="110" cy="126" rx="46" ry="11" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <ellipse cx="290" cy="126" rx="46" ry="11" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <g text-anchor="middle">
    <text x="110" y="104" font-size="11" font-weight="700" fill="{_BLUE}">Reactants</text>
    <text x="110" y="123" font-size="12" font-weight="700" fill="{_INK}">2 H&#8322; + O&#8322;</text>
    <text x="290" y="104" font-size="11" font-weight="700" fill="#16a34a">Products</text>
    <text x="290" y="123" font-size="12" font-weight="700" fill="{_INK}">2 H&#8322;O</text>
    <text x="200" y="208" font-size="10.5" fill="#6b7280">4 H and 2 O before  =  4 H and 2 O after</text>
  </g>
</svg>'''


# --- Physical Science: energy transformations ------------------------------
_ENERGY_FORMS = f'''
<svg viewBox="0 0 470 168" role="img" aria-label="A flashlight changing chemical energy to electrical energy to light and heat" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Energy Transformations</text>
  <g stroke-width="1.5">
    <rect x="20" y="46" width="120" height="58" rx="8" fill="#fef9c3" stroke="#ca8a04"/>
    <rect x="178" y="46" width="120" height="58" rx="8" fill="#dbeafe" stroke="{_BLUE}"/>
    <rect x="336" y="46" width="120" height="58" rx="8" fill="#fee2e2" stroke="{_RED}"/>
  </g>
  <g text-anchor="middle" fill="{_INK}">
    <text x="80" y="71" font-size="12" font-weight="700">Chemical</text>
    <text x="80" y="89" font-size="9.5" fill="#6b7280">battery</text>
    <text x="238" y="71" font-size="12" font-weight="700">Electrical</text>
    <text x="238" y="89" font-size="9.5" fill="#6b7280">current in wire</text>
    <text x="396" y="68" font-size="12" font-weight="700">Light</text>
    <text x="396" y="85" font-size="10.5" font-weight="700">+ Heat</text>
    <text x="396" y="99" font-size="9.5" fill="#6b7280">bulb</text>
  </g>
  <g stroke="{_INK}" stroke-width="2" fill="{_INK}">
    <line x1="142" y1="75" x2="172" y2="75"/><polygon points="172,70 182,75 172,80"/>
    <line x1="300" y1="75" x2="330" y2="75"/><polygon points="330,70 340,75 330,80"/>
  </g>
  <text x="235" y="142" text-anchor="middle" font-size="10" fill="#6b7280">Energy is never created or destroyed &#8212; it only changes form.</text>
</svg>'''


# --- Physical Science: Newton's second law ---------------------------------
_NEWTON_SECOND_LAW = f'''
<svg viewBox="0 0 420 200" role="img" aria-label="A force pushing a block produces acceleration, illustrating F equals m a" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Newton&#8217;s Second Law:  F = m &#215; a</text>
  <line x1="30" y1="150" x2="390" y2="150" stroke="{_AXIS}" stroke-width="2"/>
  <rect x="130" y="100" width="72" height="50" rx="4" fill="#dbeafe" stroke="{_BLUE}" stroke-width="2"/>
  <text x="166" y="131" text-anchor="middle" font-size="16" font-weight="700" fill="{_INK}">m</text>
  <g stroke="{_RED}" stroke-width="3" fill="{_RED}">
    <line x1="60" y1="125" x2="124" y2="125"/><polygon points="124,118 136,125 124,132"/>
  </g>
  <text x="88" y="115" text-anchor="middle" font-size="13" font-weight="700" fill="{_RED}">F</text>
  <g stroke="#16a34a" stroke-width="3" fill="#16a34a">
    <line x1="214" y1="125" x2="320" y2="125"/><polygon points="320,118 332,125 320,132"/>
  </g>
  <text x="272" y="115" text-anchor="middle" font-size="13" font-weight="700" fill="#16a34a">a</text>
  <text x="210" y="180" text-anchor="middle" font-size="10.5" fill="#6b7280">Same push on a heavier mass gives less acceleration.</text>
</svg>'''


# --- Physical Science: lever (simple machine) ------------------------------
_LEVER_MACHINE = f'''
<svg viewBox="0 0 420 200" role="img" aria-label="A lever balanced on a fulcrum lifting a load with effort" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Lever: a Simple Machine</text>
  <rect x="60" y="116" width="300" height="9" rx="3" fill="#cbd5e1" stroke="{_AXIS}" stroke-width="1"/>
  <polygon points="210,118 188,162 232,162" fill="#94a3b8" stroke="{_AXIS}" stroke-width="1"/>
  <rect x="78" y="84" width="44" height="32" rx="3" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="100" y="105" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Load</text>
  <g stroke="{_RED}" stroke-width="3" fill="{_RED}">
    <line x1="320" y1="74" x2="320" y2="110"/><polygon points="313,110 327,110 320,120"/>
  </g>
  <text x="320" y="66" text-anchor="middle" font-size="11" font-weight="700" fill="{_RED}">Effort</text>
  <text x="210" y="182" text-anchor="middle" font-size="11" fill="#6b7280">Fulcrum (pivot) &#8212; a small effort on the long arm lifts a big load.</text>
</svg>'''


# --- Physical Science: parts of a wave -------------------------------------
_WAVE_ANATOMY = f'''
<svg viewBox="0 0 440 206" role="img" aria-label="A wave labeled with crest, trough, wavelength, and amplitude" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Parts of a Wave</text>
  <line x1="40" y1="120" x2="400" y2="120" stroke="{_AXIS}" stroke-width="1" stroke-dasharray="4 4"/>
  <text x="406" y="124" font-size="9" fill="#9ca3af">rest</text>
  <path d="M40,120 C53,80 77,80 90,120 C103,160 127,160 140,120 C153,80 177,80 190,120 C203,160 227,160 240,120 C253,80 277,80 290,120 C303,160 327,160 340,120 C353,80 377,80 390,120" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <g stroke="{_INK}" stroke-width="1.3" fill="{_INK}">
    <line x1="165" y1="62" x2="265" y2="62"/>
    <polygon points="165,62 173,58 173,66"/><polygon points="265,62 257,58 257,66"/>
  </g>
  <text x="215" y="55" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Wavelength</text>
  <g stroke="{_RED}" stroke-width="1.3" fill="{_RED}">
    <line x1="315" y1="120" x2="315" y2="84"/>
    <polygon points="315,84 311,92 319,92"/><polygon points="315,120 311,112 319,112"/>
  </g>
  <text x="322" y="106" font-size="11" font-weight="700" fill="{_RED}">Amplitude</text>
  <text x="65" y="74" text-anchor="middle" font-size="10.5" fill="#16a34a" font-weight="700">Crest</text>
  <text x="115" y="178" text-anchor="middle" font-size="10.5" fill="#7c3aed" font-weight="700">Trough</text>
</svg>'''


# --- Earth & Space: Earth's layers -----------------------------------------
_EARTH_LAYERS = f'''
<svg viewBox="0 0 400 300" role="img" aria-label="Cross-section of Earth showing crust, mantle, outer core, and inner core" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="200" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Earth&#8217;s Layers</text>
  <circle cx="135" cy="165" r="110" fill="#a16207" stroke="#7c3a06" stroke-width="1.5"/>
  <circle cx="135" cy="165" r="100" fill="#ea580c"/>
  <circle cx="135" cy="165" r="60" fill="#f97316"/>
  <circle cx="135" cy="165" r="28" fill="#fcd34d"/>
  <g stroke="{_INK}" stroke-width="1">
    <line x1="135" y1="56" x2="300" y2="60"/>
    <line x1="155" y1="100" x2="300" y2="110"/>
    <line x1="160" y1="135" x2="300" y2="160"/>
    <line x1="148" y1="170" x2="300" y2="210"/>
  </g>
  <g font-size="11" fill="{_INK}">
    <text x="305" y="63">Crust (thin, solid rock)</text>
    <text x="305" y="113">Mantle (hot, slow-flowing rock)</text>
    <text x="305" y="163">Outer core (liquid metal)</text>
    <text x="305" y="213">Inner core (solid metal)</text>
  </g>
  <text x="135" y="292" text-anchor="middle" font-size="9.5" fill="#6b7280">Hottest at the center; the liquid outer core creates Earth&#8217;s magnetic field.</text>
</svg>'''


# --- Earth & Space: plate boundaries ---------------------------------------
_TECTONIC_BOUNDARIES = f'''
<svg viewBox="0 0 470 180" role="img" aria-label="Convergent, divergent, and transform plate boundaries" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Plate Boundaries</text>
  <g fill="#d6d3d1" stroke="{_AXIS}" stroke-width="1.2">
    <rect x="18" y="78" width="58" height="30"/><rect x="80" y="78" width="58" height="30"/>
    <rect x="170" y="78" width="46" height="30"/><rect x="240" y="78" width="46" height="30"/>
    <rect x="320" y="78" width="60" height="30"/><rect x="384" y="78" width="60" height="30"/>
  </g>
  <polygon points="78,78 68,60 88,60" fill="#92400e"/>
  <g stroke="{_RED}" stroke-width="2.5" fill="{_RED}">
    <line x1="40" y1="122" x2="62" y2="122"/><polygon points="62,117 72,122 62,127"/>
    <line x1="116" y1="122" x2="94" y2="122"/><polygon points="94,117 84,122 94,127"/>
    <line x1="200" y1="122" x2="178" y2="122"/><polygon points="178,117 168,122 178,127"/>
    <line x1="256" y1="122" x2="278" y2="122"/><polygon points="278,117 288,122 278,127"/>
    <line x1="338" y1="70" x2="360" y2="70"/><polygon points="360,65 370,70 360,75"/>
    <line x1="426" y1="116" x2="404" y2="116"/><polygon points="404,111 394,116 404,121"/>
  </g>
  <g font-size="11" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="78" y="150">Convergent</text><text x="228" y="150">Divergent</text><text x="382" y="150">Transform</text>
  </g>
  <g font-size="9" fill="#6b7280" text-anchor="middle">
    <text x="78" y="166">collide &#8594; mountains</text><text x="228" y="166">apart &#8594; new crust</text><text x="382" y="166">slide &#8594; earthquakes</text>
  </g>
</svg>'''


# --- Earth & Space: the rock cycle -----------------------------------------
_ROCK_CYCLE = f'''
<svg viewBox="0 0 420 270" role="img" aria-label="The rock cycle linking igneous, sedimentary, and metamorphic rock" xmlns="http://www.w3.org/2000/svg" style="max-width:500px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Rock Cycle</text>
  <g stroke-width="1.5">
    <rect x="148" y="38" width="124" height="44" rx="8" fill="#fee2e2" stroke="{_RED}"/>
    <rect x="300" y="170" width="110" height="44" rx="8" fill="#dbeafe" stroke="{_BLUE}"/>
    <rect x="10" y="170" width="120" height="44" rx="8" fill="#ede9fe" stroke="#7c3aed"/>
  </g>
  <g text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">
    <text x="210" y="65">Igneous</text>
    <text x="355" y="196">Sedimentary</text>
    <text x="70" y="196">Metamorphic</text>
  </g>
  <g fill="none" stroke="{_INK}" stroke-width="1.6">
    <path d="M272,72 C330,95 350,130 352,166"/><polygon points="348,166 356,168 357,159" fill="{_INK}"/>
    <path d="M300,200 C220,224 150,224 132,202"/><polygon points="136,206 128,200 134,194" fill="{_INK}"/>
    <path d="M68,168 C50,120 90,90 146,72"/><polygon points="142,68 150,71 147,79" fill="{_INK}"/>
  </g>
  <g font-size="9" fill="#6b7280" text-anchor="middle">
    <text x="338" y="112">weathering</text><text x="338" y="123">&amp; erosion</text>
    <text x="210" y="244">heat &amp; pressure</text>
    <text x="74" y="112">melting,</text><text x="74" y="123">then cooling</text>
  </g>
</svg>'''


# --- Earth & Space: the water cycle ----------------------------------------
_WATER_CYCLE = f'''
<svg viewBox="0 0 440 250" role="img" aria-label="The water cycle: evaporation, condensation, precipitation, and collection" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Water Cycle</text>
  <circle cx="44" cy="50" r="16" fill="#facc15" stroke="#eab308"/>
  <g stroke="#eab308" stroke-width="1.5"><line x1="44" y1="26" x2="44" y2="18"/><line x1="22" y1="50" x2="14" y2="50"/><line x1="27" y1="33" x2="21" y2="27"/></g>
  <path d="M150,70 q-22,-2 -24,18 q-26,0 -22,22 l108,0 q14,-22 -10,-28 q-6,-18 -28,-12 q-10,-8 -24,0 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.2"/>
  <path d="M300,80 q-20,-2 -22,16 q-24,0 -20,20 l96,0 q12,-20 -10,-26 q-6,-14 -26,-10 Z" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.2"/>
  <rect x="0" y="200" width="440" height="42" fill="#bae6fd"/>
  <path d="M260,200 q30,-40 80,-40 l100,0 0,40 Z" fill="#86efac" stroke="#4ade80"/>
  <g stroke="{_BLUE}" stroke-width="2.5" fill="{_BLUE}">
    <line x1="70" y1="198" x2="70" y2="120"/><polygon points="64,124 70,112 76,124"/>
    <line x1="200" y1="150" x2="200" y2="196"/><polygon points="194,192 200,202 206,192"/>
    <line x1="225" y1="150" x2="225" y2="196"/><polygon points="219,192 225,202 231,192"/>
  </g>
  <g font-size="10" fill="{_INK}">
    <text x="74" y="160">Evaporation</text>
    <text x="150" y="58" font-weight="700">Condensation</text>
    <text x="186" y="182">Precipitation</text>
    <text x="350" y="226">Collection &amp; runoff</text>
  </g>
</svg>'''


# --- Earth & Space: atmosphere layers --------------------------------------
_ATMOSPHERE_LAYERS = f'''
<svg viewBox="0 0 400 300" role="img" aria-label="The layers of Earth's atmosphere from troposphere to thermosphere" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="200" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Layers of the Atmosphere</text>
  <g stroke="#ffffff" stroke-width="1">
    <rect x="30" y="40" width="250" height="52" fill="#1e3a8a"/>
    <rect x="30" y="92" width="250" height="52" fill="#3b82f6"/>
    <rect x="30" y="144" width="250" height="52" fill="#60a5fa"/>
    <rect x="30" y="196" width="250" height="58" fill="#bfdbfe"/>
  </g>
  <rect x="30" y="254" width="250" height="14" fill="#65a30d"/>
  <circle cx="70" cy="66" r="9" fill="#e5e7eb"/><circle cx="200" cy="78" r="6" fill="#e5e7eb"/>
  <ellipse cx="95" cy="230" rx="20" ry="9" fill="#ffffff"/><ellipse cx="180" cy="222" rx="16" ry="8" fill="#ffffff"/>
  <polygon points="150,232 165,229 162,236" fill="#1a1a1a"/>
  <g font-size="11" font-weight="700" fill="{_INK}">
    <text x="288" y="70">Thermosphere</text>
    <text x="288" y="122">Mesosphere</text>
    <text x="288" y="174">Stratosphere</text>
    <text x="288" y="228">Troposphere</text>
  </g>
  <g font-size="8.5" fill="#6b7280">
    <text x="288" y="84">auroras, ISS orbit</text>
    <text x="288" y="136">meteors burn up</text>
    <text x="288" y="188">ozone layer; jets</text>
    <text x="288" y="242">weather &amp; clouds</text>
  </g>
</svg>'''


# --- Earth & Space: the solar system ---------------------------------------
_SOLAR_SYSTEM = f'''
<svg viewBox="0 0 500 180" role="img" aria-label="The Sun and the eight planets in order from Mercury to Neptune" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="250" y="18" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Solar System (not to scale)</text>
  <circle cx="6" cy="90" r="40" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="26" y="94" font-size="10" font-weight="700" fill="#a16207">Sun</text>
  <g fill="none" stroke="{_GRID}"><line x1="62" y1="90" x2="480" y2="90"/></g>
  <circle cx="80" cy="90" r="4" fill="#9ca3af"/>
  <circle cx="112" cy="90" r="6" fill="#d97706"/>
  <circle cx="146" cy="90" r="6" fill="{_BLUE}"/>
  <circle cx="178" cy="90" r="5" fill="#dc2626"/>
  <circle cx="240" cy="90" r="17" fill="#d6a06a"/>
  <g><circle cx="320" cy="90" r="14" fill="#e3c69a"/><ellipse cx="320" cy="90" rx="24" ry="6" fill="none" stroke="#a8895f" stroke-width="2"/></g>
  <circle cx="396" cy="90" r="10" fill="#7dd3fc"/>
  <circle cx="450" cy="90" r="10" fill="#3b82f6"/>
  <g font-size="8" fill="{_INK}" text-anchor="middle">
    <text x="80" y="118">Mercury</text><text x="112" y="118">Venus</text><text x="146" y="118">Earth</text><text x="178" y="118">Mars</text>
    <text x="240" y="120">Jupiter</text><text x="320" y="124">Saturn</text><text x="396" y="116">Uranus</text><text x="450" y="116">Neptune</text>
  </g>
  <g font-size="9" fill="#6b7280" text-anchor="middle">
    <text x="129" y="150">Inner, rocky planets</text><text x="370" y="150">Outer gas giants</text>
  </g>
  <g stroke="#9ca3af" stroke-width="1"><line x1="72" y1="138" x2="186" y2="138"/><line x1="222" y1="138" x2="462" y2="138"/></g>
</svg>'''


# --- Earth & Space: phases of the Moon -------------------------------------
_MOON_PHASES = f'''
<svg viewBox="0 0 490 132" role="img" aria-label="The eight phases of the Moon from new to waning crescent" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <defs>
    <clipPath id="mp-wc"><circle cx="105" cy="62" r="17"/></clipPath>
    <clipPath id="mp-wg"><circle cx="215" cy="62" r="17"/></clipPath>
    <clipPath id="mp-ng"><circle cx="325" cy="62" r="17"/></clipPath>
    <clipPath id="mp-nc"><circle cx="435" cy="62" r="17"/></clipPath>
  </defs>
  <text x="245" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Phases of the Moon</text>
  <circle cx="50" cy="62" r="17" fill="#1e293b" stroke="#475569"/>
  <circle cx="105" cy="62" r="17" fill="#fde68a"/><circle cx="99" cy="62" r="17" fill="#1e293b" clip-path="url(#mp-wc)"/><circle cx="105" cy="62" r="17" fill="none" stroke="#475569"/>
  <circle cx="160" cy="62" r="17" fill="#fde68a" stroke="#475569"/><path d="M160,45 A17 17 0 0 0 160,79 Z" fill="#1e293b"/>
  <circle cx="215" cy="62" r="17" fill="#fde68a"/><circle cx="187" cy="62" r="17" fill="#1e293b" clip-path="url(#mp-wg)"/><circle cx="215" cy="62" r="17" fill="none" stroke="#475569"/>
  <circle cx="270" cy="62" r="17" fill="#fde68a" stroke="#475569"/>
  <circle cx="325" cy="62" r="17" fill="#fde68a"/><circle cx="353" cy="62" r="17" fill="#1e293b" clip-path="url(#mp-ng)"/><circle cx="325" cy="62" r="17" fill="none" stroke="#475569"/>
  <circle cx="380" cy="62" r="17" fill="#fde68a" stroke="#475569"/><path d="M380,45 A17 17 0 0 1 380,79 Z" fill="#1e293b"/>
  <circle cx="435" cy="62" r="17" fill="#fde68a"/><circle cx="441" cy="62" r="17" fill="#1e293b" clip-path="url(#mp-nc)"/><circle cx="435" cy="62" r="17" fill="none" stroke="#475569"/>
  <g font-size="8.5" fill="{_INK}" text-anchor="middle">
    <text x="50" y="104">New</text><text x="105" y="104">Wax. cres.</text><text x="160" y="104">First qtr</text><text x="215" y="104">Wax. gib.</text>
    <text x="270" y="104">Full</text><text x="325" y="104">Wan. gib.</text><text x="380" y="104">Last qtr</text><text x="435" y="104">Wan. cres.</text>
  </g>
  <text x="245" y="124" text-anchor="middle" font-size="9" fill="#6b7280">The lit fraction grows (waxing) then shrinks (waning) over about 29.5 days.</text>
</svg>'''


# --- Earth & Space: the reason for seasons ---------------------------------
_SEASONS = f'''
<svg viewBox="0 0 440 210" role="img" aria-label="Earth's tilt causes the seasons as it orbits the Sun" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Why We Have Seasons: Earth&#8217;s Tilt</text>
  <ellipse cx="220" cy="110" rx="175" ry="64" fill="none" stroke="{_GRID}" stroke-dasharray="4 4"/>
  <circle cx="220" cy="110" r="24" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="220" y="114" text-anchor="middle" font-size="9" font-weight="700" fill="#a16207">Sun</text>
  <circle cx="55" cy="110" r="20" fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="63" y1="91" x2="47" y2="129" stroke="{_INK}" stroke-width="1.6"/>
  <circle cx="63" cy="91" r="2.6" fill="{_RED}"/>
  <circle cx="385" cy="110" r="20" fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.5"/>
  <line x1="393" y1="91" x2="377" y2="129" stroke="{_INK}" stroke-width="1.6"/>
  <circle cx="393" cy="91" r="2.6" fill="{_RED}"/>
  <g font-size="10" fill="{_INK}" text-anchor="middle">
    <text x="55" y="156" font-weight="700">Summer (North)</text>
    <text x="385" y="156" font-weight="700">Winter (North)</text>
    <text x="55" y="170" font-size="8.5" fill="#6b7280">N pole tilted toward Sun</text>
    <text x="385" y="170" font-size="8.5" fill="#6b7280">N pole tilted away</text>
  </g>
  <text x="220" y="196" text-anchor="middle" font-size="9" fill="#6b7280">The axis always points the same way (red dot = North pole) &#8212; tilt, not distance, makes seasons.</text>
</svg>'''


# --- SAT Math: system of two linear equations ------------------------------
_SYSTEM_GRAPH = f'''
<svg viewBox="0 0 280 290" role="img" aria-label="Two lines crossing at the point (2, 3), the solution of a system" xmlns="http://www.w3.org/2000/svg" style="max-width:360px;width:100%;height:auto;{_FONT}">
  <text x="140" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">A System: the lines cross at the solution</text>
  <g stroke="{_GRID}">
    <line x1="20" y1="30" x2="20" y2="270"/><line x1="44" y1="30" x2="44" y2="270"/><line x1="68" y1="30" x2="68" y2="270"/>
    <line x1="92" y1="30" x2="92" y2="270"/><line x1="116" y1="30" x2="116" y2="270"/><line x1="164" y1="30" x2="164" y2="270"/>
    <line x1="188" y1="30" x2="188" y2="270"/><line x1="212" y1="30" x2="212" y2="270"/><line x1="236" y1="30" x2="236" y2="270"/><line x1="260" y1="30" x2="260" y2="270"/>
    <line x1="20" y1="30" x2="260" y2="30"/><line x1="20" y1="54" x2="260" y2="54"/><line x1="20" y1="78" x2="260" y2="78"/>
    <line x1="20" y1="102" x2="260" y2="102"/><line x1="20" y1="126" x2="260" y2="126"/><line x1="20" y1="174" x2="260" y2="174"/>
    <line x1="20" y1="198" x2="260" y2="198"/><line x1="20" y1="222" x2="260" y2="222"/><line x1="20" y1="246" x2="260" y2="246"/><line x1="20" y1="270" x2="260" y2="270"/>
  </g>
  <line x1="20" y1="150" x2="260" y2="150" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="140" y1="30" x2="140" y2="270" stroke="{_AXIS}" stroke-width="1.5"/>
  <text x="255" y="145" font-size="10" fill="#6b7280">x</text>
  <text x="146" y="40" font-size="10" fill="#6b7280">y</text>
  <line x1="68" y1="198" x2="236" y2="30" stroke="{_BLUE}" stroke-width="2.5"/>
  <text x="74" y="212" font-size="9" fill="{_BLUE}">y = x + 1</text>
  <line x1="164" y1="30" x2="236" y2="174" stroke="#16a34a" stroke-width="2.5"/>
  <text x="198" y="183" font-size="9" fill="#16a34a">y = -2x + 7</text>
  <circle cx="188" cy="78" r="4.5" fill="{_RED}"/>
  <text x="194" y="74" font-size="10" font-weight="700" fill="{_RED}">(2, 3)</text>
  <text x="140" y="288" font-size="9" fill="#6b7280" text-anchor="middle">The solution is the point that satisfies both equations.</text>
</svg>'''


# --- Algebra: substitution method flow -------------------------------------
_SYSTEMS_SUBSTITUTION_FLOW = f'''
<svg viewBox="0 0 560 210" role="img" aria-label="Substitution method for a system of equations" xmlns="http://www.w3.org/2000/svg" style="max-width:680px;width:100%;height:auto;{_FONT}">
  <text x="280" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Solving a System by Substitution</text>
  <g font-size="11" text-anchor="middle" font-weight="700">
    <rect x="32" y="56" width="126" height="62" rx="8" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="95" y="81" fill="{_BLUE}">1. One equation</text><text x="95" y="99" fill="{_BLUE}">already says y = ...</text>
    <rect x="182" y="56" width="126" height="62" rx="8" fill="#fef3c7" stroke="#fbbf24"/>
    <text x="245" y="81" fill="#92400e">2. Substitute</text><text x="245" y="99" fill="#92400e">that expression</text>
    <rect x="332" y="56" width="126" height="62" rx="8" fill="#dcfce7" stroke="#86efac"/>
    <text x="395" y="81" fill="#166534">3. Solve for x</text><text x="395" y="99" fill="#166534">then find y</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="1.5" fill="none">
    <path d="M158,87 H180"/><path d="M308,87 H330"/>
  </g>
  <g font-size="12" fill="{_INK}" text-anchor="middle">
    <text x="280" y="150">y = x + 1 and y = -x + 5</text>
    <text x="280" y="176" font-weight="700">x + 1 = -x + 5 -> x = 2, then y = 3</text>
  </g>
</svg>'''


# --- Algebra: elimination method balance -----------------------------------
_SYSTEMS_ELIMINATION_BALANCE = f'''
<svg viewBox="0 0 560 230" role="img" aria-label="Elimination method adding equations to cancel one variable" xmlns="http://www.w3.org/2000/svg" style="max-width:680px;width:100%;height:auto;{_FONT}">
  <text x="280" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Solving a System by Elimination</text>
  <rect x="55" y="48" width="450" height="118" rx="10" fill="#f8fafc" stroke="#cbd5e1"/>
  <g font-size="14" fill="{_INK}" text-anchor="middle">
    <text x="190" y="82">2x + y = 11</text>
    <text x="190" y="114">x - y = 4</text>
    <line x1="105" y1="130" x2="275" y2="130" stroke="{_AXIS}" stroke-width="1.5"/>
    <text x="190" y="154" font-weight="700" fill="{_BLUE}">3x = 15</text>
    <text x="392" y="100" font-size="11" fill="#6b7280">+y and -y cancel</text>
    <path d="M340,92 C370,74 410,74 438,92" fill="none" stroke="{_RED}" stroke-width="2"/>
    <path d="M438,92 l-8,-1 l4,-7" fill="none" stroke="{_RED}" stroke-width="2"/>
  </g>
  <text x="280" y="198" text-anchor="middle" font-size="10.5" fill="#6b7280">Add or subtract equations to remove one variable, then solve the simpler equation.</text>
</svg>'''


# --- Algebra: break-even linear model graph --------------------------------
_BREAK_EVEN_MODEL_GRAPH = f'''
<svg viewBox="0 0 380 270" role="img" aria-label="Break-even graph comparing two linear cost models that intersect" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="190" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Break-Even Point</text>
  <line x1="48" y1="220" x2="340" y2="220" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="48" y1="220" x2="48" y2="42" stroke="{_AXIS}" stroke-width="1.5"/>
  <g stroke="{_GRID}" stroke-width="1">
    <line x1="98" y1="42" x2="98" y2="220"/><line x1="148" y1="42" x2="148" y2="220"/><line x1="198" y1="42" x2="198" y2="220"/><line x1="248" y1="42" x2="248" y2="220"/><line x1="298" y1="42" x2="298" y2="220"/>
    <line x1="48" y1="180" x2="340" y2="180"/><line x1="48" y1="140" x2="340" y2="140"/><line x1="48" y1="100" x2="340" y2="100"/><line x1="48" y1="60" x2="340" y2="60"/>
  </g>
  <path d="M48,190 L318,55" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <path d="M48,145 L318,92" fill="none" stroke="{_GREEN}" stroke-width="2.5"/>
  <circle cx="198" cy="115" r="5" fill="{_RED}"/>
  <text x="206" y="110" font-size="10" font-weight="700" fill="{_RED}">same cost</text>
  <text x="260" y="68" font-size="9" fill="{_BLUE}">Plan A</text>
  <text x="260" y="105" font-size="9" fill="{_GREEN}">Plan B</text>
  <text x="192" y="248" text-anchor="middle" font-size="10" fill="#6b7280">x = number of units</text>
  <text x="18" y="134" text-anchor="middle" font-size="10" fill="#6b7280" transform="rotate(-90 18 134)">total cost</text>
</svg>'''


# --- SAT Math: exponential growth ------------------------------------------
_EXPONENTIAL_GROWTH = f'''
<svg viewBox="0 0 290 240" role="img" aria-label="An exponential growth curve y equals 2 to the x, doubling at each step" xmlns="http://www.w3.org/2000/svg" style="max-width:380px;width:100%;height:auto;{_FONT}">
  <text x="145" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Exponential Growth: y = 2&#739;</text>
  <line x1="40" y1="205" x2="265" y2="205" stroke="{_AXIS}" stroke-width="1.5"/>
  <line x1="40" y1="205" x2="40" y2="28" stroke="{_AXIS}" stroke-width="1.5"/>
  <text x="262" y="222" font-size="10" fill="#6b7280">x</text>
  <text x="26" y="34" font-size="10" fill="#6b7280">y</text>
  <path d="M40,195 L82,185 L124,165 L166,125 L208,45" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <g fill="{_BLUE}">
    <circle cx="40" cy="195" r="3.5"/><circle cx="82" cy="185" r="3.5"/><circle cx="124" cy="165" r="3.5"/><circle cx="166" cy="125" r="3.5"/><circle cx="208" cy="45" r="3.5"/>
  </g>
  <g font-size="9" fill="{_INK}">
    <text x="34" y="190" text-anchor="end">1</text><text x="88" y="184">2</text><text x="130" y="164">4</text><text x="172" y="124">8</text><text x="214" y="46">16</text>
  </g>
  <g font-size="9" fill="#6b7280" text-anchor="middle">
    <text x="40" y="218">0</text><text x="82" y="218">1</text><text x="124" y="218">2</text><text x="166" y="218">3</text><text x="208" y="218">4</text>
  </g>
  <text x="145" y="236" text-anchor="middle" font-size="9" fill="#6b7280">Each step right, y is multiplied by 2 (it doubles), so the curve climbs ever faster.</text>
</svg>'''


# --- Science practices: the scientific method as a repeating cycle ---------
_SCIENTIFIC_METHOD = f'''
<svg viewBox="0 0 380 340" role="img" aria-label="The scientific method as a repeating cycle of five steps" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="180" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">The Scientific Method</text>
  <rect x="60" y="30" width="240" height="44" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="180" y="48" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1e3a8a">1. Observe &amp; Ask a Question</text>
  <text x="180" y="64" text-anchor="middle" font-size="9.5" fill="{_INK}">notice something; ask why it happens</text>
  <rect x="60" y="92" width="240" height="44" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="180" y="110" text-anchor="middle" font-size="11.5" font-weight="700" fill="#15803d">2. Form a Hypothesis</text>
  <text x="180" y="126" text-anchor="middle" font-size="9.5" fill="{_INK}">a testable, falsifiable prediction</text>
  <rect x="60" y="154" width="240" height="44" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="180" y="172" text-anchor="middle" font-size="11.5" font-weight="700" fill="#b45309">3. Test with an Experiment</text>
  <text x="180" y="188" text-anchor="middle" font-size="9.5" fill="{_INK}">change one variable; control the rest</text>
  <rect x="60" y="216" width="240" height="44" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="180" y="234" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1e3a8a">4. Collect &amp; Analyze Data</text>
  <text x="180" y="250" text-anchor="middle" font-size="9.5" fill="{_INK}">organize results; look for the trend</text>
  <rect x="60" y="278" width="240" height="44" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="180" y="296" text-anchor="middle" font-size="11.5" font-weight="700" fill="#15803d">5. Draw a Conclusion</text>
  <text x="180" y="312" text-anchor="middle" font-size="9.5" fill="{_INK}">does the data support the hypothesis?</text>
  <g stroke="#6b7280" stroke-width="1.5" fill="#6b7280">
    <line x1="180" y1="74" x2="180" y2="88"/><polygon points="180,90 175,80 185,80"/>
    <line x1="180" y1="136" x2="180" y2="150"/><polygon points="180,152 175,142 185,142"/>
    <line x1="180" y1="198" x2="180" y2="212"/><polygon points="180,214 175,204 185,204"/>
    <line x1="180" y1="260" x2="180" y2="274"/><polygon points="180,276 175,266 185,266"/>
  </g>
  <path d="M300,300 C352,300 352,52 306,52" fill="none" stroke="#6b7280" stroke-width="1.5" stroke-dasharray="4 3"/>
  <polygon points="306,52 316,47 316,57" fill="#6b7280"/>
  <text x="368" y="176" text-anchor="middle" font-size="9" fill="#6b7280" transform="rotate(90 368 176)">revise &amp; repeat</text>
</svg>'''


# --- Science practices: independent / dependent / controlled variables ------
_CONTROLLED_EXPERIMENT = f'''
<svg viewBox="0 0 380 240" role="img" aria-label="A fair test: independent, dependent, and controlled variables" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">A Fair Test: The Three Kinds of Variables</text>
  <rect x="20" y="40" width="150" height="74" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="95" y="60" text-anchor="middle" font-size="11.5" font-weight="700" fill="#1e3a8a">Independent</text>
  <text x="95" y="78" text-anchor="middle" font-size="9.5" fill="{_INK}">what YOU change</text>
  <text x="95" y="98" text-anchor="middle" font-size="9" fill="#6b7280">(the cause)</text>
  <rect x="210" y="40" width="150" height="74" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="285" y="60" text-anchor="middle" font-size="11.5" font-weight="700" fill="#15803d">Dependent</text>
  <text x="285" y="78" text-anchor="middle" font-size="9.5" fill="{_INK}">what you MEASURE</text>
  <text x="285" y="98" text-anchor="middle" font-size="9" fill="#6b7280">(the result)</text>
  <line x1="170" y1="77" x2="206" y2="77" stroke="#6b7280" stroke-width="1.5"/>
  <polygon points="208,77 198,72 198,82" fill="#6b7280"/>
  <text x="190" y="71" text-anchor="middle" font-size="9" fill="#6b7280">affects</text>
  <rect x="70" y="150" width="240" height="64" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="190" y="172" text-anchor="middle" font-size="11.5" font-weight="700" fill="#b45309">Controlled Variables</text>
  <text x="190" y="190" text-anchor="middle" font-size="9.5" fill="{_INK}">everything else kept exactly the SAME</text>
  <text x="190" y="205" text-anchor="middle" font-size="9" fill="#6b7280">so the change is a fair comparison</text>
</svg>'''


# --- SAT R&W: the four question domains and their share --------------------
_SAT_RW_ROADMAP = f'''
<svg viewBox="0 0 380 300" role="img" aria-label="The four question domains of the SAT Reading and Writing section" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">SAT Reading &amp; Writing: 4 Question Domains</text>
  <rect x="20" y="32" width="340" height="56" rx="8" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="30" y="52" font-size="11.5" font-weight="700" fill="#1e3a8a">Craft &amp; Structure  (~28%)</text>
  <text x="30" y="68" font-size="9.5" fill="{_INK}">Words in Context, Text Structure &amp; Purpose,</text>
  <text x="30" y="81" font-size="9.5" fill="{_INK}">Cross-Text Connections</text>
  <rect x="20" y="96" width="340" height="56" rx="8" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="30" y="116" font-size="11.5" font-weight="700" fill="#15803d">Information &amp; Ideas  (~26%)</text>
  <text x="30" y="132" font-size="9.5" fill="{_INK}">Central Ideas &amp; Details, Command of Evidence,</text>
  <text x="30" y="145" font-size="9.5" fill="{_INK}">Inferences</text>
  <rect x="20" y="160" width="340" height="56" rx="8" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="30" y="180" font-size="11.5" font-weight="700" fill="#b45309">Standard English Conventions  (~26%)</text>
  <text x="30" y="196" font-size="9.5" fill="{_INK}">Boundaries (punctuation),</text>
  <text x="30" y="209" font-size="9.5" fill="{_INK}">Form, Structure &amp; Sense (grammar)</text>
  <rect x="20" y="224" width="340" height="56" rx="8" fill="#fee2e2" stroke="{_RED}" stroke-width="1.5"/>
  <text x="30" y="244" font-size="11.5" font-weight="700" fill="#b91c1c">Expression of Ideas  (~20%)</text>
  <text x="30" y="260" font-size="9.5" fill="{_INK}">Transitions,</text>
  <text x="30" y="273" font-size="9.5" fill="{_INK}">Rhetorical Synthesis</text>
</svg>'''


# --- SAT R&W: transition words grouped by the logic they signal ------------
_TRANSITION_WORDS = f'''
<svg viewBox="0 0 380 290" role="img" aria-label="Common transition words grouped by the logical relationship they signal" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;{_FONT}">
  <text x="190" y="18" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Transitions: Match the Logic</text>
  <g font-size="10">
    <rect x="20" y="30" width="120" height="38" rx="6" fill="#dbeafe" stroke="{_BLUE}"/>
    <text x="30" y="53" font-weight="700" fill="#1e3a8a">Add / continue</text>
    <text x="150" y="53" fill="{_INK}">also, furthermore, in addition</text>
    <rect x="20" y="72" width="120" height="38" rx="6" fill="#fee2e2" stroke="{_RED}"/>
    <text x="30" y="95" font-weight="700" fill="#b91c1c">Contrast</text>
    <text x="150" y="95" fill="{_INK}">however, but, nevertheless</text>
    <rect x="20" y="114" width="120" height="38" rx="6" fill="#dcfce7" stroke="{_GREEN}"/>
    <text x="30" y="137" font-weight="700" fill="#15803d">Cause &amp; effect</text>
    <text x="150" y="137" fill="{_INK}">therefore, thus, consequently</text>
    <rect x="20" y="156" width="120" height="38" rx="6" fill="#fef3c7" stroke="{_AMBER}"/>
    <text x="30" y="179" font-weight="700" fill="#b45309">Example</text>
    <text x="150" y="179" fill="{_INK}">for example, for instance</text>
    <rect x="20" y="198" width="120" height="38" rx="6" fill="#dbeafe" stroke="{_BLUE}"/>
    <text x="30" y="221" font-weight="700" fill="#1e3a8a">Sequence / time</text>
    <text x="150" y="221" fill="{_INK}">first, then, next, finally</text>
    <rect x="20" y="240" width="120" height="38" rx="6" fill="#dcfce7" stroke="{_GREEN}"/>
    <text x="30" y="263" font-weight="700" fill="#15803d">Emphasis</text>
    <text x="150" y="263" fill="{_INK}">in fact, indeed, of course</text>
  </g>
</svg>'''


# --- SAT R&W: bar graph for a quantitative-evidence question ---------------
_BAR_RECYCLING = f'''
<svg viewBox="0 0 340 250" role="img" aria-label="Bar graph of recycling rate by material: paper 68 percent, glass 31, metal 28, plastic 9" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="175" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Recycling Rate by Material (%)</text>
  <line x1="50" y1="20" x2="50" y2="200" stroke="{_AXIS}"/>
  <line x1="50" y1="200" x2="320" y2="200" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="50" y1="155" x2="320" y2="155" stroke="{_GRID}"/><text x="44" y="158">20</text>
    <line x1="50" y1="110" x2="320" y2="110" stroke="{_GRID}"/><text x="44" y="113">40</text>
    <line x1="50" y1="65"  x2="320" y2="65"  stroke="{_GRID}"/><text x="44" y="68">60</text>
    <line x1="50" y1="20"  x2="320" y2="20"  stroke="{_GRID}"/><text x="44" y="23">80</text>
    <text x="44" y="204">0</text>
  </g>
  <g fill="{_BLUE}">
    <rect x="66"  y="47"  width="38" height="153"/>
    <rect x="131" y="130" width="38" height="70"/>
    <rect x="196" y="137" width="38" height="63"/>
    <rect x="261" y="180" width="38" height="20"/>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle" font-weight="700">
    <text x="85" y="42">68</text><text x="150" y="125">31</text><text x="215" y="132">28</text><text x="280" y="175">9</text>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="85" y="216">Paper</text><text x="150" y="216">Glass</text><text x="215" y="216">Metal</text><text x="280" y="216">Plastic</text>
  </g>
</svg>'''


# --- SAT R&W: line graph for a quantitative-evidence question ---------------
_LINE_SOLAR = f'''
<svg viewBox="0 0 340 250" role="img" aria-label="Line graph of global solar capacity in gigawatts rising from about 70 in 2011 to about 850 in 2021" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="175" y="16" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Global Solar Capacity (gigawatts)</text>
  <line x1="50" y1="20" x2="50" y2="200" stroke="{_AXIS}"/>
  <line x1="50" y1="200" x2="320" y2="200" stroke="{_AXIS}"/>
  <g font-size="10" fill="#6b7280" text-anchor="end">
    <line x1="50" y1="140" x2="320" y2="140" stroke="{_GRID}"/><text x="44" y="143">300</text>
    <line x1="50" y1="80"  x2="320" y2="80"  stroke="{_GRID}"/><text x="44" y="83">600</text>
    <line x1="50" y1="20"  x2="320" y2="20"  stroke="{_GRID}"/><text x="44" y="23">900</text>
    <text x="44" y="204">0</text>
  </g>
  <polyline points="60,186 112,172 164,154 216,120 268,80 316,30" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <g fill="{_BLUE}">
    <circle cx="60" cy="186" r="3.5"/><circle cx="112" cy="172" r="3.5"/><circle cx="164" cy="154" r="3.5"/>
    <circle cx="216" cy="120" r="3.5"/><circle cx="268" cy="80" r="3.5"/><circle cx="316" cy="30" r="3.5"/>
  </g>
  <g font-size="8.5" fill="#6b7280" text-anchor="middle">
    <text x="60" y="216">2011</text><text x="112" y="216">2013</text><text x="164" y="216">2015</text>
    <text x="216" y="216">2017</text><text x="268" y="216">2019</text><text x="316" y="216">2021</text>
  </g>
  <g font-size="9" fill="{_INK}" text-anchor="middle" font-weight="700">
    <text x="60" y="180">70</text><text x="316" y="24">850</text>
  </g>
</svg>'''


# --- Earth's interior: depth, temperature and physical state ----------------
_EARTH_INTERIOR_SCALE = f'''
<svg viewBox="0 0 480 330" role="img" aria-label="Depth, temperature and physical state of Earth's four main layers" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="240" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Inside Earth: Depth, Heat &amp; State</text>
  <g stroke="{_INK}" stroke-width="1">
    <rect x="40" y="40" width="110" height="12" fill="#a16207"/>
    <rect x="40" y="52" width="110" height="113" fill="#ea580c"/>
    <rect x="40" y="165" width="110" height="89" fill="#f97316"/>
    <rect x="40" y="254" width="110" height="48" fill="#fcd34d"/>
  </g>
  <g stroke="{_AXIS}" stroke-width="1">
    <line x1="150" y1="46" x2="170" y2="46"/>
    <line x1="150" y1="108" x2="170" y2="108"/>
    <line x1="150" y1="210" x2="170" y2="210"/>
    <line x1="150" y1="278" x2="170" y2="278"/>
  </g>
  <g font-size="11" font-weight="700" fill="{_INK}">
    <text x="174" y="44">Crust &#8212; solid rock</text>
    <text x="174" y="104">Mantle &#8212; solid rock that flows slowly</text>
    <text x="174" y="206">Outer core &#8212; LIQUID iron &amp; nickel</text>
    <text x="174" y="274">Inner core &#8212; SOLID iron &amp; nickel</text>
  </g>
  <g font-size="9" fill="#6b7280">
    <text x="174" y="56">0 &#8211; ~35 km &#183; up to ~1,000&#176;C</text>
    <text x="174" y="116">~35 &#8211; 2,890 km &#183; ~1,000&#8211;3,700&#176;C &#183; biggest layer</text>
    <text x="174" y="218">2,890 &#8211; 5,150 km &#183; ~4,000&#8211;5,000&#176;C &#183; makes the magnetic field</text>
    <text x="174" y="286">5,150 &#8211; 6,371 km &#183; ~5,200&#176;C &#183; hottest, yet solid (pressure)</text>
  </g>
  <text x="40" y="320" font-size="9" fill="#6b7280">Drawn roughly to scale (crust exaggerated). Center of Earth &#8776; 6,371 km deep.</text>
</svg>'''


# --- Earth's interior: seismic-wave evidence (P, S, shadow zone) ------------
_SEISMIC_WAVES = f'''
<svg viewBox="0 0 380 372" role="img" aria-label="Seismic P-waves and S-waves through Earth, with the S-wave shadow zone" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="190" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How We Know: Seismic Waves</text>
  <circle cx="170" cy="185" r="125" fill="#fdebd0" stroke="#b45309" stroke-width="1.5"/>
  <circle cx="170" cy="185" r="56" fill="#bae6fd" stroke="{_BLUE}" stroke-width="1.2"/>
  <circle cx="170" cy="185" r="23" fill="#fcd34d" stroke="#b45309" stroke-width="1"/>
  <g stroke="{_BLUE}" stroke-width="1.4" opacity="0.9">
    <line x1="170" y1="60" x2="45" y2="185"/>
    <line x1="170" y1="60" x2="62" y2="247"/>
    <line x1="170" y1="60" x2="105" y2="293"/>
    <line x1="170" y1="60" x2="170" y2="310"/>
    <line x1="170" y1="60" x2="235" y2="293"/>
    <line x1="170" y1="60" x2="278" y2="247"/>
    <line x1="170" y1="60" x2="295" y2="185"/>
  </g>
  <g stroke="{_RED}" stroke-width="2.2">
    <line x1="170" y1="60" x2="62" y2="123"/>
    <line x1="170" y1="60" x2="45" y2="185"/>
    <line x1="170" y1="60" x2="278" y2="123"/>
    <line x1="170" y1="60" x2="295" y2="185"/>
    <line x1="170" y1="60" x2="170" y2="129"/>
  </g>
  <line x1="170" y1="129" x2="170" y2="241" stroke="{_RED}" stroke-width="1.4" stroke-dasharray="4 4" opacity="0.5"/>
  <g stroke="{_RED}" stroke-width="2"><line x1="164" y1="133" x2="176" y2="145"/><line x1="176" y1="133" x2="164" y2="145"/></g>
  <circle cx="170" cy="60" r="4.5" fill="{_INK}"/>
  <text x="170" y="44" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">earthquake</text>
  <text x="206" y="150" font-size="9" fill="{_RED}">S-waves stop</text>
  <text x="206" y="161" font-size="9" fill="{_RED}">at liquid core</text>
  <text x="170" y="300" text-anchor="middle" font-size="9" font-weight="700" fill="#374151">S-wave shadow zone</text>
  <g font-size="10">
    <line x1="40" y1="338" x2="64" y2="338" stroke="{_BLUE}" stroke-width="2"/>
    <text x="70" y="341" fill="{_INK}">P-waves &#8212; through solid &amp; liquid</text>
    <line x1="40" y1="356" x2="64" y2="356" stroke="{_RED}" stroke-width="2"/>
    <text x="70" y="359" fill="{_INK}">S-waves &#8212; solids only (blocked by liquid core)</text>
  </g>
</svg>'''


# --- Earth's interior: composition vs. mechanical layering ------------------
_LITHOSPHERE_ASTHENOSPHERE = f'''
<svg viewBox="0 0 470 290" role="img" aria-label="Two ways to divide Earth's outer layers: by composition and by mechanical behavior" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Two Ways to Slice the Outer Earth</text>
  <g font-size="9" fill="#6b7280" text-anchor="end">
    <text x="78" y="44">0 km</text>
    <text x="78" y="94">100 km</text>
    <text x="78" y="222">350 km</text>
    <text x="78" y="253">410 km</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="0.8"><line x1="82" y1="40" x2="200" y2="40"/><line x1="82" y1="91" x2="200" y2="91"/><line x1="82" y1="219" x2="200" y2="219"/><line x1="82" y1="250" x2="200" y2="250"/></g>
  <g stroke="{_INK}" stroke-width="0.8">
    <rect x="90" y="40" width="110" height="18" fill="#a16207"/>
    <rect x="90" y="58" width="110" height="33" fill="#ea580c"/>
    <rect x="90" y="91" width="110" height="128" fill="#fdba74"/>
    <rect x="90" y="219" width="110" height="31" fill="#ea580c"/>
  </g>
  <g stroke="#ffffff" stroke-width="1.4"><line x1="128" y1="40" x2="124" y2="91"/><line x1="168" y1="40" x2="172" y2="91"/></g>
  <g stroke="#7c2d12" stroke-width="1.2" fill="#7c2d12">
    <path d="M110,150 q18,-12 36,0" fill="none"/><polygon points="146,150 139,146 140,154"/>
    <path d="M150,178 q18,12 36,0" fill="none"/><polygon points="186,178 179,182 180,174"/>
  </g>
  <g stroke="{_BLUE}" stroke-width="1.4" fill="none">
    <path d="M86,42 h-8 v14 h8"/>
    <path d="M86,60 h-8 v188 h8"/>
  </g>
  <text x="20" y="51" font-size="10" font-weight="700" fill="{_BLUE}">Crust</text>
  <text x="40" y="156" font-size="10" font-weight="700" fill="{_BLUE}" transform="rotate(-90 40 156)" text-anchor="middle">Mantle</text>
  <text x="60" y="278" font-size="9" fill="{_BLUE}" text-anchor="middle">BY COMPOSITION</text>
  <g stroke="{_GREEN}" stroke-width="1.4" fill="none">
    <path d="M204,42 h8 v47 h-8"/>
    <path d="M204,93 h8 v124 h-8"/>
    <path d="M204,221 h8 v27 h-8"/>
  </g>
  <g font-size="10" font-weight="700" fill="#15803d">
    <text x="218" y="62">Lithosphere</text>
    <text x="218" y="150">Asthenosphere</text>
    <text x="218" y="236">Lower mantle</text>
  </g>
  <g font-size="8.5" fill="#6b7280">
    <text x="218" y="74">rigid &#8212; broken into plates</text>
    <text x="218" y="162">soft, hot &#8212; flows slowly</text>
    <text x="218" y="248">rigid again (high pressure)</text>
  </g>
  <text x="360" y="278" font-size="9" fill="{_GREEN}" text-anchor="middle">BY HOW IT BEHAVES</text>
</svg>'''


# --- Earth's interior: the geodynamo and magnetic field --------------------
_GEOMAGNETIC_FIELD = f'''
<svg viewBox="0 0 440 300" role="img" aria-label="Earth's magnetic field generated by churning liquid iron in the outer core" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Earth&#8217;s Magnetic Field: the Geodynamo</text>
  <g stroke="{_BLUE}" stroke-width="1.4" fill="none" opacity="0.8">
    <path d="M220,108 C150,70 70,120 70,170 C70,220 150,270 220,232"/>
    <path d="M220,108 C290,70 370,120 370,170 C370,220 290,270 220,232"/>
    <path d="M220,98 C120,50 30,120 30,170 C30,220 120,290 220,242"/>
    <path d="M220,98 C320,50 410,120 410,170 C410,220 320,290 220,242"/>
  </g>
  <g fill="{_BLUE}">
    <polygon points="70,170 64,160 76,160"/>
    <polygon points="30,170 24,160 36,160"/>
    <polygon points="370,170 364,180 376,180"/>
    <polygon points="410,170 404,180 416,180"/>
  </g>
  <circle cx="220" cy="170" r="62" fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.2"/>
  <circle cx="220" cy="170" r="34" fill="#f97316" stroke="#b45309" stroke-width="1"/>
  <circle cx="220" cy="170" r="13" fill="#fcd34d" stroke="#b45309" stroke-width="0.8"/>
  <g stroke="#7c2d12" stroke-width="1.3" fill="none">
    <path d="M200,150 a14,14 0 1 1 -2,18"/><polygon points="198,168 192,160 204,162" fill="#7c2d12"/>
    <path d="M240,190 a14,14 0 1 1 2,-18"/><polygon points="242,172 248,180 236,178" fill="#7c2d12"/>
  </g>
  <line x1="220" y1="98" x2="220" y2="242" stroke="{_INK}" stroke-width="1" stroke-dasharray="3 3"/>
  <text x="220" y="94" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">magnetic N</text>
  <text x="220" y="256" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">magnetic S</text>
  <g stroke="{_RED}" stroke-width="1.4" fill="{_RED}">
    <line x1="8" y1="60" x2="36" y2="60"/><polygon points="36,60 28,56 28,64"/>
    <line x1="8" y1="78" x2="30" y2="78"/><polygon points="30,78 22,74 22,82"/>
  </g>
  <text x="8" y="50" font-size="9" fill="{_RED}">solar wind</text>
  <text x="220" y="288" text-anchor="middle" font-size="9.5" fill="#6b7280">Churning liquid iron + Earth&#8217;s spin generate the field that deflects the solar wind.</text>
</svg>'''


# --- Plate tectonics: continental drift evidence ---------------------------
_CONTINENTAL_DRIFT = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="Pangaea splitting into today's continents, with matching fossil, rock, and mountain evidence" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Continental Drift: One Supercontinent Split Apart</text>
  <text x="115" y="44" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">~250 million years ago: Pangaea</text>
  <polygon points="70,70 150,58 185,90 175,135 190,180 140,210 85,200 58,160 62,110" fill="#d6b483" stroke="#8a6230" stroke-width="1.5"/>
  <polyline points="68,120 188,150" fill="none" stroke="{_RED}" stroke-width="2.5" stroke-dasharray="5 3"/>
  <polyline points="95,72 120,205" fill="none" stroke="{_GREEN}" stroke-width="2.5"/>
  <line x1="205" y1="135" x2="245" y2="135" stroke="{_AXIS}" stroke-width="2"/>
  <polygon points="245,135 236,130 236,140" fill="{_AXIS}"/>
  <text x="225" y="128" text-anchor="middle" font-size="8.5" fill="#6b7280">drift</text>
  <text x="360" y="44" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Today: separate continents</text>
  <polygon points="270,72 320,62 338,92 330,135 300,150 272,140 262,108" fill="#d6b483" stroke="#8a6230" stroke-width="1.5"/>
  <polygon points="360,95 410,85 440,118 448,170 405,205 360,190 352,150" fill="#d6b483" stroke="#8a6230" stroke-width="1.5"/>
  <polyline points="268,118 332,128" fill="none" stroke="{_RED}" stroke-width="2.5" stroke-dasharray="5 3"/>
  <polyline points="356,140 446,150" fill="none" stroke="{_RED}" stroke-width="2.5" stroke-dasharray="5 3"/>
  <polyline points="300,64 312,148" fill="none" stroke="{_GREEN}" stroke-width="2.5"/>
  <polyline points="372,92 392,202" fill="none" stroke="{_GREEN}" stroke-width="2.5"/>
  <g font-size="9" fill="{_INK}">
    <line x1="60" y1="232" x2="84" y2="232" stroke="{_RED}" stroke-width="2.5" stroke-dasharray="5 3"/><text x="90" y="235">matching fossils</text>
    <line x1="205" y1="232" x2="229" y2="232" stroke="{_GREEN}" stroke-width="2.5"/><text x="235" y="235">matching mountain belts &amp; rock layers</text>
  </g>
</svg>'''


# --- Plate tectonics: mantle convection (the engine) -----------------------
_MANTLE_CONVECTION = f'''
<svg viewBox="0 0 470 270" role="img" aria-label="Mantle convection cells driving tectonic plates, with rising material at a ridge and a sinking slab at a trench" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">What Drives the Plates: Mantle Convection</text>
  <rect x="20" y="60" width="430" height="180" fill="#fdba74"/>
  <rect x="20" y="52" width="430" height="10" fill="#7dd3fc"/>
  <rect x="20" y="58" width="200" height="9" fill="#8a6230"/>
  <rect x="250" y="58" width="200" height="9" fill="#8a6230"/>
  <polygon points="225,52 235,52 245,40 215,40" fill="#7dd3fc"/>
  <text x="230" y="36" text-anchor="middle" font-size="8.5" fill="{_INK}">ridge</text>
  <polygon points="445,58 455,58 451,74" fill="#1e3a8a"/>
  <text x="428" y="50" text-anchor="middle" font-size="8.5" fill="{_INK}">trench</text>
  <polygon points="445,67 451,67 470,150 462,150" fill="#8a6230" opacity="0.8"/>
  <g stroke="{_RED}" stroke-width="2" fill="none">
    <path d="M230,72 C140,72 60,110 60,160 C60,205 150,225 225,210"/>
    <path d="M240,72 C330,72 420,110 430,150"/>
  </g>
  <g fill="{_RED}">
    <polygon points="225,210 233,204 233,216"/>
  </g>
  <line x1="230" y1="150" x2="230" y2="80" stroke="{_RED}" stroke-width="2.5"/>
  <polygon points="230,74 224,86 236,86" fill="{_RED}"/>
  <text x="120" y="150" font-size="9.5" fill="#7c2d12">hot rock rises &amp; spreads</text>
  <text x="300" y="120" font-size="9.5" fill="#7c2d12">cooler rock sinks</text>
  <text x="235" y="258" text-anchor="middle" font-size="9.5" fill="#6b7280">Heat from the core drives slow loops in the solid mantle; the plates ride along (ridge push + slab pull).</text>
</svg>'''


# --- Plate tectonics: seafloor spreading & magnetic stripes ----------------
_SEAFLOOR_SPREADING = f'''
<svg viewBox="0 0 470 230" role="img" aria-label="Seafloor spreading at a mid-ocean ridge with symmetric magnetic stripes and ages increasing away from the ridge" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Seafloor Spreading: New Crust at the Ridge</text>
  <rect x="20" y="34" width="430" height="40" fill="#7dd3fc"/>
  <polygon points="215,74 235,74 245,52 225,40 205,52" fill="#8a6230" stroke="#5c3a18"/>
  <g stroke="{_INK}" stroke-width="0.5">
    <rect x="205" y="80" width="40" height="44" fill="#1f2937"/>
    <rect x="165" y="80" width="40" height="44" fill="#d1d5db"/><rect x="245" y="80" width="40" height="44" fill="#d1d5db"/>
    <rect x="125" y="80" width="40" height="44" fill="#1f2937"/><rect x="285" y="80" width="40" height="44" fill="#1f2937"/>
    <rect x="85" y="80" width="40" height="44" fill="#d1d5db"/><rect x="325" y="80" width="40" height="44" fill="#d1d5db"/>
    <rect x="45" y="80" width="40" height="44" fill="#1f2937"/><rect x="365" y="80" width="40" height="44" fill="#1f2937"/>
  </g>
  <line x1="210" y1="150" x2="120" y2="150" stroke="{_RED}" stroke-width="2.5"/><polygon points="114,150 126,144 126,156" fill="{_RED}"/>
  <line x1="240" y1="150" x2="330" y2="150" stroke="{_RED}" stroke-width="2.5"/><polygon points="336,150 324,144 324,156" fill="{_RED}"/>
  <line x1="225" y1="124" x2="225" y2="100" stroke="{_RED}" stroke-width="2.5"/><polygon points="225,94 219,106 231,106" fill="{_RED}"/>
  <g font-size="9" fill="{_INK}" text-anchor="middle">
    <text x="225" y="172">0 (youngest)</text>
    <text x="105" y="172">older</text><text x="345" y="172">older</text>
    <text x="55" y="172">oldest</text><text x="395" y="172">oldest</text>
  </g>
  <text x="235" y="194" text-anchor="middle" font-size="9.5" fill="#6b7280">Magma rises, hardens, and pushes apart. The magnetic stripes are a mirror image on each side &#8212;</text>
  <text x="235" y="208" text-anchor="middle" font-size="9.5" fill="#6b7280">strong proof that new seafloor forms at the ridge and spreads outward.</text>
</svg>'''


# --- Plate tectonics: convergent boundary (subduction) ---------------------
_CONVERGENT_BOUNDARY = f'''
<svg viewBox="0 0 470 260" role="img" aria-label="An ocean-continent convergent boundary: the dense oceanic plate subducts, forming a trench and volcanoes" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Convergent Boundary: Subduction</text>
  <rect x="20" y="40" width="220" height="34" fill="#7dd3fc"/>
  <rect x="20" y="74" width="430" height="160" fill="#fdba74"/>
  <polygon points="250,74 450,74 450,150 250,120" fill="#c89a5b" stroke="#8a6230"/>
  <polygon points="20,68 248,108 250,124 235,128 20,82" fill="#6b4423"/>
  <polygon points="235,128 250,124 320,210 300,214" fill="#6b4423"/>
  <polygon points="238,74 252,74 245,92" fill="#1e3a8a"/>
  <text x="232" y="36" text-anchor="middle" font-size="9" fill="{_INK}">trench</text>
  <polygon points="330,74 352,74 345,46 337,46" fill="#7c2d12"/>
  <polygon points="338,48 344,48 341,38" fill="{_RED}"/>
  <text x="341" y="32" text-anchor="middle" font-size="9" fill="{_INK}">volcano</text>
  <g fill="{_RED}"><ellipse cx="320" cy="150" rx="10" ry="6"/><circle cx="330" cy="120" r="4"/><circle cx="338" cy="95" r="3"/></g>
  <line x1="270" y1="150" x2="298" y2="193" stroke="{_INK}" stroke-width="2"/><polygon points="303,200 292,194 300,186" fill="{_INK}"/>
  <text x="215" y="138" font-size="9" fill="#7c2d12">dense ocean plate dives down</text>
  <text x="235" y="252" text-anchor="middle" font-size="9.5" fill="#6b7280">The denser oceanic plate sinks beneath the continent &#8594; deep trench, melting, and a chain of volcanoes.</text>
</svg>'''


# --- Plate tectonics: transform boundary -----------------------------------
_TRANSFORM_BOUNDARY = f'''
<svg viewBox="0 0 420 230" role="img" aria-label="A transform boundary where two plates slide past each other along a fault, offsetting a road" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="210" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Transform Boundary: Plates Slide Past</text>
  <polygon points="30,40 205,40 195,110 215,180 30,180" fill="#d6b483" stroke="#8a6230"/>
  <polygon points="205,40 390,40 390,180 215,180 195,110" fill="#c89a5b" stroke="#8a6230"/>
  <polyline points="205,40 195,110 215,180" fill="none" stroke="{_RED}" stroke-width="2.5"/>
  <line x1="40" y1="92" x2="198" y2="100" stroke="{_INK}" stroke-width="3"/>
  <line x1="210" y1="135" x2="380" y2="143" stroke="{_INK}" stroke-width="3"/>
  <text x="110" y="86" font-size="8.5" fill="#374151">road</text>
  <text x="300" y="158" font-size="8.5" fill="#374151">same road, offset</text>
  <line x1="110" y1="60" x2="110" y2="30" stroke="{_BLUE}" stroke-width="2.5"/><polygon points="110,24 104,36 116,36" fill="{_BLUE}"/>
  <line x1="300" y1="160" x2="300" y2="190" stroke="{_BLUE}" stroke-width="2.5"/><polygon points="300,196 294,184 306,184" fill="{_BLUE}"/>
  <polygon points="205,108 210,118 221,118 212,125 216,136 205,129 194,136 198,125 189,118 200,118" fill="{_AMBER}" stroke="#b45309" stroke-width="0.8"/>
  <text x="236" y="112" font-size="9" font-weight="700" fill="#b45309">earthquake</text>
  <text x="210" y="212" text-anchor="middle" font-size="9" fill="#6b7280">Plates grind and catch, then slip suddenly &#8212; earthquakes (e.g., California&#8217;s San Andreas Fault). No crust made or destroyed.</text>
</svg>'''


# --- Plate tectonics: the Pacific Ring of Fire -----------------------------
_RING_OF_FIRE = f'''
<svg viewBox="0 0 360 300" role="img" aria-label="The Pacific Ring of Fire: volcanoes and earthquakes around the rim of the Pacific Ocean" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="180" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Pacific &#8220;Ring of Fire&#8221;</text>
  <ellipse cx="180" cy="158" rx="120" ry="112" fill="#bae6fd" stroke="#7dd3fc"/>
  <text x="180" y="150" text-anchor="middle" font-size="12" fill="#0369a1">Pacific Ocean</text>
  <text x="180" y="170" text-anchor="middle" font-size="8.5" fill="#0369a1">(subduction zones around the rim)</text>
  <g fill="{_RED}">
    <polygon points="180,42 188,58 172,58"/>
    <polygon points="250,64 258,80 242,80"/>
    <polygon points="296,126 304,142 288,142"/>
    <polygon points="296,192 304,208 288,208"/>
    <polygon points="244,250 252,266 236,266"/>
    <polygon points="116,250 124,266 108,266"/>
    <polygon points="64,192 72,208 56,208"/>
    <polygon points="64,122 72,138 56,138"/>
    <polygon points="110,64 118,80 102,80"/>
  </g>
  <g fill="{_AMBER}">
    <circle cx="215" cy="50" r="3"/><circle cx="280" cy="96" r="3"/><circle cx="305" cy="160" r="3"/>
    <circle cx="278" cy="224" r="3"/><circle cx="180" cy="272" r="3"/><circle cx="84" cy="224" r="3"/>
    <circle cx="55" cy="160" r="3"/><circle cx="84" cy="96" r="3"/>
  </g>
  <g font-size="9" fill="{_INK}">
    <polygon points="40,290 48,290 44,280" fill="{_RED}"/><text x="54" y="290">volcano</text>
    <circle cx="150" cy="287" r="3" fill="{_AMBER}"/><text x="158" y="290">earthquake</text>
  </g>
</svg>'''


# --- Plate tectonics: hotspot island chain ---------------------------------
_HOTSPOT = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="A mantle hotspot creating a chain of volcanic islands as the plate moves over it" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Hotspots: A Chain of Islands (e.g., Hawaii)</text>
  <rect x="20" y="60" width="430" height="40" fill="#7dd3fc"/>
  <rect x="20" y="96" width="430" height="14" fill="#8a6230"/>
  <line x1="120" y1="50" x2="200" y2="50" stroke="{_INK}" stroke-width="2"/><polygon points="206,50 194,44 194,56" fill="{_INK}"/>
  <text x="160" y="44" text-anchor="middle" font-size="9" fill="{_INK}">plate moves &#8594;</text>
  <polygon points="70,60 84,60 77,52" fill="#9ca3af"/>
  <polygon points="150,60 168,60 159,48" fill="#78716c"/>
  <polygon points="235,60 257,60 246,40" fill="#7c2d12"/>
  <polygon points="243,42 249,42 246,34" fill="{_RED}"/>
  <rect x="20" y="110" width="430" height="120" fill="#fdba74"/>
  <path d="M246,225 C235,180 256,150 246,112" fill="none" stroke="{_RED}" stroke-width="6" opacity="0.85"/>
  <ellipse cx="246" cy="225" rx="26" ry="10" fill="{_RED}" opacity="0.6"/>
  <text x="298" y="200" font-size="9.5" fill="#7c2d12">hotspot (plume) stays in one place</text>
  <g font-size="8.5" fill="{_INK}" text-anchor="middle">
    <text x="77" y="78">oldest, extinct</text>
    <text x="159" y="78">older</text>
    <text x="246" y="80">active</text>
  </g>
  <text x="235" y="246" text-anchor="middle" font-size="9.5" fill="#6b7280">The plate slides over a fixed hotspot, so islands get older with distance from the active volcano.</text>
</svg>'''


# --- Rock cycle: Mohs hardness scale ---------------------------------------
_MOHS_HARDNESS = f'''
<svg viewBox="0 0 480 172" role="img" aria-label="Mohs hardness scale from talc (1) to diamond (10) with common testing objects" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="240" y="20" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">Mohs Hardness Scale (1 = softest, 10 = hardest)</text>
  <g stroke="{_INK}" stroke-width="0.6">
    <rect x="40" y="70" width="40" height="26" fill="#eff6ff"/>
    <rect x="80" y="70" width="40" height="26" fill="#dbeafe"/>
    <rect x="120" y="70" width="40" height="26" fill="#bfdbfe"/>
    <rect x="160" y="70" width="40" height="26" fill="#93c5fd"/>
    <rect x="200" y="70" width="40" height="26" fill="#60a5fa"/>
    <rect x="240" y="70" width="40" height="26" fill="#3b82f6"/>
    <rect x="280" y="70" width="40" height="26" fill="#2563eb"/>
    <rect x="320" y="70" width="40" height="26" fill="#1d4ed8"/>
    <rect x="360" y="70" width="40" height="26" fill="#1e40af"/>
    <rect x="400" y="70" width="40" height="26" fill="#172554"/>
  </g>
  <g font-size="12" font-weight="700" text-anchor="middle">
    <text x="60" y="88" fill="#1e3a8a">1</text><text x="100" y="88" fill="#1e3a8a">2</text>
    <text x="140" y="88" fill="#1e3a8a">3</text><text x="180" y="88" fill="#1e3a8a">4</text>
    <text x="220" y="88" fill="#ffffff">5</text><text x="260" y="88" fill="#ffffff">6</text>
    <text x="300" y="88" fill="#ffffff">7</text><text x="340" y="88" fill="#ffffff">8</text>
    <text x="380" y="88" fill="#ffffff">9</text><text x="420" y="88" fill="#ffffff">10</text>
  </g>
  <g font-size="8" fill="{_INK}" text-anchor="middle">
    <text x="60" y="110">Talc</text><text x="100" y="110">Gypsum</text><text x="140" y="110">Calcite</text>
    <text x="180" y="110">Fluorite</text><text x="220" y="110">Apatite</text><text x="260" y="110">Feldspar</text>
    <text x="300" y="110">Quartz</text><text x="340" y="110">Topaz</text><text x="380" y="110">Corundum</text>
    <text x="420" y="110">Diamond</text>
  </g>
  <g stroke="{_RED}" stroke-width="1" fill="{_RED}" font-size="8" text-anchor="middle">
    <line x1="120" y1="58" x2="120" y2="70"/><text x="120" y="52">fingernail (2.5)</text>
    <line x1="160" y1="58" x2="160" y2="70"/><text x="160" y="42">penny (3.5)</text>
    <line x1="240" y1="58" x2="240" y2="70"/><text x="240" y="52">steel knife (5.5)</text>
  </g>
  <text x="240" y="134" text-anchor="middle" font-size="9.5" fill="#6b7280">A mineral scratches anything softer than itself, so hardness helps identify minerals.</text>
  <text x="240" y="150" text-anchor="middle" font-size="9" fill="#6b7280">A fingernail (2.5) scratches talc &amp; gypsum; quartz (7) scratches glass and steel.</text>
</svg>'''


# --- Rock cycle: igneous textures (intrusive vs extrusive) -----------------
_IGNEOUS_TEXTURES = f'''
<svg viewBox="0 0 460 235" role="img" aria-label="Intrusive igneous rock with large crystals versus extrusive igneous rock with tiny crystals" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Igneous Rocks: Cooling Rate Sets Crystal Size</text>
  <rect x="40" y="40" width="160" height="100" rx="10" fill="#f3e8d8" stroke="#8a6230" stroke-width="1.5"/>
  <g stroke="#8a6230" stroke-width="0.8">
    <polygon points="55,55 95,50 100,90 60,100" fill="#e7c8a0"/>
    <polygon points="100,52 150,58 160,95 105,92" fill="#d9b38c"/>
    <polygon points="60,102 110,95 130,130 70,132" fill="#cbb9a0"/>
    <polygon points="132,98 185,95 188,132 135,132" fill="#e0cbb0"/>
    <polygon points="150,55 188,52 186,92 152,92" fill="#cdab84"/>
  </g>
  <text x="120" y="158" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Intrusive (e.g., granite)</text>
  <text x="120" y="174" text-anchor="middle" font-size="9" fill="#6b7280">cooled SLOWLY deep underground</text>
  <text x="120" y="187" text-anchor="middle" font-size="9" fill="#6b7280">&#8594; LARGE crystals you can see</text>
  <rect x="260" y="40" width="160" height="100" rx="10" fill="#3f3f46" stroke="#1f2937" stroke-width="1.5"/>
  <g fill="#a1a1aa">
    <circle cx="280" cy="60" r="2"/><circle cx="300" cy="75" r="2"/><circle cx="330" cy="62" r="2"/>
    <circle cx="360" cy="80" r="2"/><circle cx="390" cy="65" r="2"/><circle cx="285" cy="100" r="2"/>
    <circle cx="315" cy="110" r="2"/><circle cx="345" cy="98" r="2"/><circle cx="375" cy="115" r="2"/>
    <circle cx="400" cy="100" r="2"/><circle cx="355" cy="55" r="2"/><circle cx="270" cy="85" r="2"/>
  </g>
  <text x="340" y="158" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Extrusive (e.g., basalt)</text>
  <text x="340" y="174" text-anchor="middle" font-size="9" fill="#6b7280">cooled FAST at the surface</text>
  <text x="340" y="187" text-anchor="middle" font-size="9" fill="#6b7280">&#8594; tiny or no visible crystals</text>
  <text x="230" y="214" text-anchor="middle" font-size="9.5" fill="#6b7280">Slow cooling gives atoms time to build big crystals; fast cooling freezes them tiny (or glassy, like obsidian).</text>
</svg>'''


# --- Rock cycle: sedimentary layering & lithification ----------------------
_SEDIMENTARY_LAYERS = f'''
<svg viewBox="0 0 470 252" role="img" aria-label="How sedimentary rock forms: weathering, erosion, deposition, and compaction into layers" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Sedimentary Rocks: Layers Build Up Over Time</text>
  <g font-size="9" text-anchor="middle">
    <rect x="20" y="34" width="96" height="26" rx="6" fill="#dbeafe" stroke="{_BLUE}"/><text x="68" y="51" fill="{_INK}">1. Weathering</text>
    <rect x="128" y="34" width="96" height="26" rx="6" fill="#dbeafe" stroke="{_BLUE}"/><text x="176" y="51" fill="{_INK}">2. Erosion</text>
    <rect x="236" y="34" width="96" height="26" rx="6" fill="#dbeafe" stroke="{_BLUE}"/><text x="284" y="51" fill="{_INK}">3. Deposition</text>
    <rect x="344" y="34" width="108" height="26" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="398" y="47" fill="{_INK}">4. Compaction</text><text x="398" y="57" fill="{_INK}">&amp; cementation</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="1.2" fill="{_AXIS}">
    <line x1="116" y1="47" x2="126" y2="47"/><polygon points="128,47 120,43 120,51"/>
    <line x1="224" y1="47" x2="234" y2="47"/><polygon points="236,47 228,43 228,51"/>
    <line x1="332" y1="47" x2="342" y2="47"/><polygon points="344,47 336,43 336,51"/>
  </g>
  <g stroke="{_INK}" stroke-width="0.8">
    <rect x="120" y="86" width="240" height="22" fill="#e7d3a1"/>
    <rect x="120" y="108" width="240" height="22" fill="#d8b98a"/>
    <rect x="120" y="130" width="240" height="22" fill="#c8a06a"/>
    <rect x="120" y="152" width="240" height="22" fill="#b58a55"/>
    <rect x="120" y="174" width="240" height="22" fill="#9c7647"/>
  </g>
  <g transform="translate(250 141)" stroke="#4b2e12" stroke-width="1.2" fill="none">
    <path d="M0,0 a6,6 0 1 1 -3,-5"/>
  </g>
  <text x="268" y="145" font-size="8" fill="#4b2e12">fossil</text>
  <g stroke="{_RED}" stroke-width="1.2" fill="{_RED}">
    <line x1="372" y1="97" x2="372" y2="183"/>
    <polygon points="372,186 368,177 376,177"/>
  </g>
  <text x="380" y="97" font-size="9" fill="{_RED}">youngest (top)</text>
  <text x="380" y="190" font-size="9" fill="{_RED}">oldest (bottom)</text>
  <text x="235" y="220" text-anchor="middle" font-size="9.5" fill="#6b7280">Bits of rock settle in flat layers, then are pressed and cemented into rock. Lower layers are older (superposition);</text>
  <text x="235" y="234" text-anchor="middle" font-size="9.5" fill="#6b7280">buried remains can become fossils &#8212; which is why fossils are found mostly in sedimentary rock.</text>
</svg>'''


# --- Rock cycle: metamorphism (heat & pressure, foliation) -----------------
_METAMORPHIC_CHANGE = f'''
<svg viewBox="0 0 470 232" role="img" aria-label="Metamorphic rock forms when heat and pressure realign minerals in a parent rock into bands" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Metamorphic Rocks: Changed by Heat &amp; Pressure</text>
  <rect x="40" y="64" width="110" height="70" rx="6" fill="#cbd5e1" stroke="{_INK}" stroke-width="1"/>
  <g stroke="#94a3b8" stroke-width="1"><line x1="50" y1="82" x2="140" y2="82"/><line x1="50" y1="99" x2="140" y2="99"/><line x1="50" y1="116" x2="140" y2="116"/></g>
  <text x="95" y="152" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Parent rock</text>
  <text x="95" y="166" text-anchor="middle" font-size="8.5" fill="#6b7280">(e.g., shale)</text>
  <g stroke="{_RED}" stroke-width="2" fill="{_RED}">
    <line x1="170" y1="84" x2="200" y2="84"/><polygon points="206,84 196,78 196,90"/>
    <line x1="200" y1="114" x2="170" y2="114"/><polygon points="164,114 174,108 174,120"/>
  </g>
  <text x="187" y="72" text-anchor="middle" font-size="8.5" fill="{_RED}">pressure</text>
  <text x="187" y="134" text-anchor="middle" font-size="9" font-weight="700" fill="{_AMBER}">heat</text>
  <rect x="240" y="64" width="120" height="70" rx="6" fill="#a8a29e" stroke="{_INK}" stroke-width="1"/>
  <g stroke="#57534e" stroke-width="2.2" fill="none"><path d="M250,76 q60,-8 100,0"/><path d="M250,93 q60,-8 100,0"/><path d="M250,110 q60,-8 100,0"/><path d="M250,127 q60,-8 100,0"/></g>
  <text x="300" y="152" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Metamorphic rock</text>
  <text x="300" y="166" text-anchor="middle" font-size="8.5" fill="#6b7280">minerals line up into bands (foliation)</text>
  <text x="235" y="196" text-anchor="middle" font-size="9.5" fill="#6b7280">Heat &amp; pressure change a rock in the SOLID state (no melting). Increasing grade: shale &#8594; slate &#8594; schist &#8594; gneiss.</text>
  <text x="235" y="212" text-anchor="middle" font-size="9.5" fill="#6b7280">Non-foliated (no bands): limestone &#8594; marble, sandstone &#8594; quartzite.</text>
</svg>'''


# --- Rock cycle: detailed wheel with named processes -----------------------
_ROCK_CYCLE_DETAILED = f'''
<svg viewBox="0 0 470 330" role="img" aria-label="The rock cycle linking magma, igneous, sedimentary, and metamorphic rock through named processes" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Rock Cycle (no beginning, no end)</text>
  <g stroke-width="1.5">
    <rect x="190" y="40" width="90" height="42" rx="10" fill="#fee2e2" stroke="{_RED}"/>
    <rect x="370" y="150" width="90" height="42" rx="10" fill="#fde68a" stroke="{_AMBER}"/>
    <rect x="190" y="262" width="90" height="42" rx="10" fill="#dbeafe" stroke="{_BLUE}"/>
    <rect x="12" y="150" width="92" height="42" rx="10" fill="#ede9fe" stroke="#7c3aed"/>
  </g>
  <g text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">
    <text x="235" y="66">Magma / Lava</text>
    <text x="415" y="176">Igneous</text>
    <text x="235" y="288">Sedimentary</text>
    <text x="58" y="176">Metamorphic</text>
  </g>
  <g fill="none" stroke="{_INK}" stroke-width="1.8">
    <path d="M282,58 C340,72 372,110 388,146"/><polygon points="388,150 382,140 392,138" fill="{_INK}"/>
    <path d="M410,194 C398,236 330,266 284,278"/><polygon points="284,278 295,275 290,285" fill="{_INK}"/>
    <path d="M188,282 C130,268 96,238 82,196"/><polygon points="82,192 88,202 78,204" fill="{_INK}"/>
    <path d="M62,148 C78,110 140,74 188,62"/><polygon points="188,58 178,62 184,71" fill="{_INK}"/>
  </g>
  <g font-size="9" fill="{_INK}" text-anchor="middle">
    <text x="356" y="92">cools &amp;</text><text x="356" y="103">crystallizes</text>
    <text x="374" y="246">weathers, erodes,</text><text x="374" y="257">compacts &amp; cements</text>
    <text x="96" y="250">heat &amp;</text><text x="96" y="261">pressure</text>
    <text x="112" y="96">melts</text>
  </g>
  <g fill="none" stroke="{_AXIS}" stroke-width="1.4" stroke-dasharray="5 4">
    <line x1="368" y1="171" x2="110" y2="171"/>
    <polygon points="106,171 116,167 116,175" fill="{_AXIS}"/>
    <polygon points="372,171 362,167 362,175" fill="{_AXIS}"/>
  </g>
  <text x="240" y="165" text-anchor="middle" font-size="8.5" fill="#6b7280">rocks can also melt or be re-cooked directly (shortcuts)</text>
  <text x="235" y="322" text-anchor="middle" font-size="9" fill="#6b7280">Any rock can take a shortcut: any rock can melt, be weathered into sediment, or be cooked &amp; squeezed.</text>
</svg>'''


# --- Rock cycle: three rock families at a glance ---------------------------
_ROCK_CLASSES = f'''
<svg viewBox="0 0 470 230" role="img" aria-label="Comparison of how igneous, sedimentary, and metamorphic rocks form and how to identify them" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Three Rock Families at a Glance</text>
  <g stroke="{_INK}" stroke-width="0.8">
    <rect x="110" y="32" width="118" height="30" fill="#fde68a"/>
    <rect x="228" y="32" width="118" height="30" fill="#dbeafe"/>
    <rect x="346" y="32" width="118" height="30" fill="#d6d3d1"/>
  </g>
  <g text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">
    <text x="169" y="52">Igneous</text><text x="287" y="52">Sedimentary</text><text x="405" y="52">Metamorphic</text>
  </g>
  <g font-size="9.5" font-weight="700" fill="{_INK}">
    <text x="12" y="86">How it</text><text x="12" y="98">forms</text>
    <text x="12" y="140">Clue to</text><text x="12" y="152">spot it</text>
    <text x="12" y="194">Examples</text>
  </g>
  <g stroke="{_GRID}" stroke-width="1">
    <line x1="110" y1="62" x2="464" y2="62"/><line x1="110" y1="116" x2="464" y2="116"/><line x1="110" y1="170" x2="464" y2="170"/><line x1="110" y1="214" x2="464" y2="214"/>
    <line x1="110" y1="32" x2="110" y2="214"/><line x1="228" y1="32" x2="228" y2="214"/><line x1="346" y1="32" x2="346" y2="214"/><line x1="464" y1="32" x2="464" y2="214"/>
  </g>
  <g font-size="8.5" fill="{_INK}" text-anchor="middle">
    <text x="169" y="84">magma/lava</text><text x="169" y="96">cools &amp;</text><text x="169" y="108">hardens</text>
    <text x="287" y="84">sediment is</text><text x="287" y="96">pressed &amp;</text><text x="287" y="108">cemented</text>
    <text x="405" y="84">heat &amp; pressure</text><text x="405" y="96">change an</text><text x="405" y="108">existing rock</text>
    <text x="169" y="140">interlocking</text><text x="169" y="152">crystals</text>
    <text x="287" y="140">flat layers,</text><text x="287" y="152">often fossils</text>
    <text x="405" y="140">bands / aligned,</text><text x="405" y="152">shiny minerals</text>
    <text x="169" y="194">granite, basalt</text>
    <text x="287" y="188">sandstone,</text><text x="287" y="200">limestone</text>
    <text x="405" y="194">marble, slate</text>
  </g>
</svg>'''


# --- Water cycle: distribution of Earth's water ----------------------------
_WATER_DISTRIBUTION = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="Distribution of Earth's water: mostly salt water, with little fresh water, most of it frozen" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Where Is Earth&#8217;s Water?</text>
  <text x="40" y="48" font-size="10" font-weight="700" fill="{_INK}">All water</text>
  <g stroke="{_INK}" stroke-width="0.6">
    <rect x="40" y="54" width="378" height="34" fill="#2563eb"/>
    <rect x="418" y="54" width="12" height="34" fill="#bfdbfe"/>
  </g>
  <text x="229" y="76" text-anchor="middle" font-size="11" font-weight="700" fill="#ffffff">Salt water (oceans) ~97%</text>
  <text x="424" y="102" text-anchor="middle" font-size="9" fill="{_INK}">fresh ~3%</text>
  <line x1="418" y1="88" x2="120" y2="120" stroke="{_AXIS}" stroke-width="0.8" stroke-dasharray="3 3"/>
  <line x1="430" y1="88" x2="430" y2="120" stroke="{_AXIS}" stroke-width="0.8" stroke-dasharray="3 3"/>
  <text x="40" y="138" font-size="10" font-weight="700" fill="{_INK}">That 3% fresh water</text>
  <g stroke="{_INK}" stroke-width="0.6">
    <rect x="40" y="144" width="269" height="34" fill="#e0f2fe"/>
    <rect x="309" y="144" width="117" height="34" fill="#3b82f6"/>
    <rect x="426" y="144" width="4" height="34" fill="#16a34a"/>
  </g>
  <g font-size="10" font-weight="700" text-anchor="middle">
    <text x="174" y="166" fill="#0369a1">Ice caps &amp; glaciers ~69%</text>
    <text x="367" y="166" fill="#ffffff">Groundwater ~30%</text>
  </g>
  <line x1="428" y1="178" x2="428" y2="196" stroke="{_AXIS}" stroke-width="0.8"/>
  <text x="428" y="208" text-anchor="middle" font-size="8.5" fill="#16a34a">lakes &amp; rivers ~1%</text>
  <text x="235" y="230" text-anchor="middle" font-size="9.5" fill="#6b7280">Most water is salty; most fresh water is frozen. The lakes and rivers we use are a tiny sliver of the total.</text>
</svg>'''


# --- Water cycle: the full loop --------------------------------------------
_WATER_CYCLE_DETAILED = f'''
<svg viewBox="0 0 480 300" role="img" aria-label="The water cycle: evaporation, transpiration, condensation, precipitation, runoff, and infiltration into groundwater" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="240" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Water Cycle</text>
  <rect x="0" y="26" width="480" height="200" fill="#eaf6ff"/>
  <circle cx="44" cy="56" r="18" fill="#facc15" stroke="#eab308"/>
  <g stroke="#eab308" stroke-width="1.5"><line x1="44" y1="30" x2="44" y2="22"/><line x1="18" y1="56" x2="10" y2="56"/><line x1="26" y1="38" x2="20" y2="32"/></g>
  <g fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.2">
    <path d="M170,70 q-24,-2 -26,20 q-28,0 -24,24 l120,0 q16,-24 -10,-30 q-6,-20 -30,-14 q-12,-9 -30,0 Z"/>
  </g>
  <text x="206" y="100" text-anchor="middle" font-size="9" fill="#475569">condensation &#8594; cloud</text>
  <rect x="0" y="210" width="300" height="90" fill="#86efac"/>
  <rect x="300" y="210" width="180" height="90" fill="#7dd3fc"/>
  <polygon points="20,210 90,120 160,210" fill="#9ca3af"/>
  <polygon points="70,150 90,120 110,150 98,160 82,150" fill="#ffffff"/>
  <path d="M92,160 C120,200 200,205 300,225" fill="none" stroke="{_BLUE}" stroke-width="4"/>
  <g><rect x="196" y="196" width="4" height="14" fill="#7c4a12"/><circle cx="198" cy="192" r="9" fill="#16a34a"/></g>
  <g><rect x="236" y="198" width="4" height="12" fill="#7c4a12"/><circle cx="238" cy="194" r="8" fill="#16a34a"/></g>
  <g stroke="{_BLUE}" stroke-width="2.2" fill="{_BLUE}">
    <line x1="360" y1="206" x2="360" y2="120"/><polygon points="360,114 354,126 366,126"/>
    <line x1="410" y1="206" x2="410" y2="140"/><polygon points="410,134 404,146 416,146"/>
  </g>
  <text x="400" y="180" font-size="9" fill="{_BLUE}">evaporation</text>
  <g stroke="#15803d" stroke-width="2" fill="#15803d">
    <line x1="216" y1="186" x2="216" y2="142"/><polygon points="216,136 210,148 222,148"/>
  </g>
  <text x="216" y="130" text-anchor="middle" font-size="8.5" fill="#15803d">transpiration</text>
  <g stroke="{_BLUE}" stroke-width="2">
    <line x1="160" y1="120" x2="156" y2="138"/><line x1="180" y1="122" x2="176" y2="140"/>
    <line x1="200" y1="120" x2="196" y2="138"/><line x1="220" y1="122" x2="216" y2="140"/>
    <line x1="240" y1="120" x2="236" y2="138"/>
  </g>
  <text x="132" y="116" text-anchor="middle" font-size="9" fill="{_BLUE}">precipitation</text>
  <g stroke="#0369a1" stroke-width="2" fill="#0369a1">
    <line x1="120" y1="216" x2="120" y2="250"/><polygon points="120,256 114,244 126,244"/>
  </g>
  <text x="120" y="272" text-anchor="middle" font-size="8.5" fill="#0369a1">infiltration</text>
  <rect x="0" y="262" width="300" height="38" fill="#5b6b73" opacity="0.35"/>
  <text x="62" y="286" font-size="8.5" fill="#1f2937">groundwater flows to the sea</text>
  <line x1="190" y1="290" x2="298" y2="290" stroke="#0369a1" stroke-width="2"/><polygon points="300,290 290,286 290,294" fill="#0369a1"/>
  <text x="362" y="252" text-anchor="middle" font-size="9" fill="{_INK}">Ocean</text>
</svg>'''


# --- Water cycle: states of water & energy ---------------------------------
_WATER_PHASE_CHANGES = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="The three states of water and the energy absorbed or released between them" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Water Changes State (and Energy)</text>
  <g stroke="{_INK}" stroke-width="1.2">
    <rect x="30" y="90" width="110" height="60" rx="8" fill="#e0f2fe"/>
    <rect x="180" y="90" width="110" height="60" rx="8" fill="#bae6fd"/>
    <rect x="330" y="90" width="110" height="60" rx="8" fill="#7dd3fc"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="{_INK}">
    <text x="85" y="116" font-size="12">SOLID</text><text x="85" y="134" font-size="9">ice</text>
    <text x="235" y="116" font-size="12">LIQUID</text><text x="235" y="134" font-size="9">water</text>
    <text x="385" y="116" font-size="12">GAS</text><text x="385" y="134" font-size="9">water vapor</text>
  </g>
  <line x1="140" y1="108" x2="180" y2="108" stroke="{_RED}" stroke-width="2"/><polygon points="180,108 170,103 170,113" fill="{_RED}"/>
  <line x1="180" y1="132" x2="140" y2="132" stroke="{_BLUE}" stroke-width="2"/><polygon points="140,132 150,127 150,137" fill="{_BLUE}"/>
  <text x="160" y="80" text-anchor="middle" font-size="8.5" fill="{_RED}">melting</text>
  <text x="160" y="152" text-anchor="middle" font-size="8.5" fill="{_BLUE}">freezing</text>
  <line x1="290" y1="108" x2="330" y2="108" stroke="{_RED}" stroke-width="2"/><polygon points="330,108 320,103 320,113" fill="{_RED}"/>
  <line x1="330" y1="132" x2="290" y2="132" stroke="{_BLUE}" stroke-width="2"/><polygon points="290,132 300,127 300,137" fill="{_BLUE}"/>
  <text x="310" y="80" text-anchor="middle" font-size="8.5" fill="{_RED}">evaporation</text>
  <text x="310" y="152" text-anchor="middle" font-size="8.5" fill="{_BLUE}">condensation</text>
  <text x="235" y="178" text-anchor="middle" font-size="9.5" fill="#6b7280">The Sun&#8217;s energy drives evaporation; condensation releases that heat &#8212; the engine behind clouds and storms.</text>
  <g font-size="9">
    <line x1="120" y1="200" x2="150" y2="200" stroke="{_RED}" stroke-width="2"/><polygon points="150,200 142,196 142,204" fill="{_RED}"/>
    <text x="156" y="203" fill="{_INK}">adds energy (absorbs heat)</text>
    <line x1="120" y1="218" x2="150" y2="218" stroke="{_BLUE}" stroke-width="2"/><polygon points="120,218 128,214 128,222" fill="{_BLUE}"/>
    <text x="156" y="221" fill="{_INK}">releases energy (gives off heat)</text>
  </g>
</svg>'''


# --- Water cycle: cloud formation ------------------------------------------
_CLOUD_FORMATION = f'''
<svg viewBox="0 0 440 270" role="img" aria-label="Cloud formation: warm moist air rises, cools to its dew point, and water vapor condenses into a cloud" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How a Cloud Forms</text>
  <rect x="0" y="26" width="440" height="210" fill="#eaf6ff"/>
  <rect x="0" y="226" width="440" height="44" fill="#86efac"/>
  <circle cx="40" cy="52" r="16" fill="#facc15" stroke="#eab308"/>
  <g fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.2">
    <path d="M250,58 q-24,-2 -26,20 q-28,0 -24,24 l120,0 q16,-24 -10,-30 q-6,-20 -30,-14 q-12,-9 -30,0 Z"/>
  </g>
  <line x1="150" y1="222" x2="150" y2="96" stroke="{_RED}" stroke-width="2.5"/><polygon points="150,90 144,102 156,102" fill="{_RED}"/>
  <text x="118" y="170" font-size="9" fill="{_RED}" transform="rotate(-90 118 170)" text-anchor="middle">warm moist air rises</text>
  <line x1="60" y1="104" x2="380" y2="104" stroke="{_AXIS}" stroke-width="1" stroke-dasharray="5 4"/>
  <text x="66" y="98" font-size="8.5" fill="#6b7280">condensation level (dew point reached)</text>
  <text x="320" y="150" text-anchor="middle" font-size="9" fill="{_BLUE}">higher up = cooler air</text>
  <text x="330" y="206" text-anchor="middle" font-size="9" fill="{_INK}">Sun warms the ground</text>
  <text x="220" y="256" text-anchor="middle" font-size="9.3" fill="#6b7280">Rising air expands and cools. At the dew point, vapor condenses on tiny particles into cloud droplets.</text>
</svg>'''


# --- Water cycle: groundwater, water table & aquifer -----------------------
_GROUNDWATER_AQUIFER = f'''
<svg viewBox="0 0 470 260" role="img" aria-label="Groundwater cross-section showing infiltration, the water table, an aquifer, and a well" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Groundwater, the Water Table &amp; Aquifers</text>
  <rect x="20" y="28" width="430" height="40" fill="#eaf6ff"/>
  <rect x="20" y="68" width="430" height="60" fill="#d9c7a3"/>
  <rect x="20" y="128" width="430" height="80" fill="#9ec7e8"/>
  <rect x="20" y="208" width="430" height="34" fill="#6b7280"/>
  <line x1="20" y1="128" x2="450" y2="128" stroke="{_BLUE}" stroke-width="2"/>
  <text x="352" y="123" font-size="9" font-weight="700" fill="#1e3a8a">water table</text>
  <g stroke="#0369a1" stroke-width="1.8" fill="#0369a1">
    <line x1="80" y1="70" x2="80" y2="120"/><polygon points="80,126 74,114 86,114"/>
    <line x1="120" y1="70" x2="120" y2="120"/><polygon points="120,126 114,114 126,114"/>
  </g>
  <text x="100" y="62" text-anchor="middle" font-size="8.5" fill="#0369a1">rain soaks in (infiltration)</text>
  <rect x="300" y="40" width="10" height="150" fill="#44403c"/>
  <rect x="296" y="36" width="18" height="10" fill="#1f2937"/>
  <text x="305" y="32" text-anchor="middle" font-size="8.5" fill="{_INK}">well</text>
  <text x="240" y="102" text-anchor="middle" font-size="9.3" fill="#7c5a1e">unsaturated zone (air + water in gaps)</text>
  <text x="195" y="172" text-anchor="middle" font-size="10" font-weight="700" fill="#1e3a8a">AQUIFER (saturated rock/sediment)</text>
  <text x="235" y="229" text-anchor="middle" font-size="9.3" fill="#ffffff">impermeable bedrock</text>
  <text x="235" y="256" text-anchor="middle" font-size="9" fill="#6b7280">Water fills the spaces between grains below the water table; a well must reach below it to pump water.</text>
</svg>'''


# --- Weather: composition of the atmosphere --------------------------------
_ATMOSPHERE_COMPOSITION = f'''
<svg viewBox="0 0 470 212" role="img" aria-label="Composition of Earth's dry atmosphere: about 78 percent nitrogen, 21 percent oxygen, and 1 percent other gases" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">What&#8217;s in the Air? (dry air)</text>
  <g stroke="{_INK}" stroke-width="0.6">
    <rect x="40" y="44" width="304" height="40" fill="#2563eb"/>
    <rect x="344" y="44" width="82" height="40" fill="#16a34a"/>
    <rect x="426" y="44" width="4" height="40" fill="{_AMBER}"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="#ffffff">
    <text x="192" y="69" font-size="12">Nitrogen ~78%</text>
    <text x="385" y="69" font-size="9.5">Oxygen ~21%</text>
  </g>
  <text x="430" y="100" text-anchor="middle" font-size="8.5" fill="#b45309">other ~1%</text>
  <line x1="428" y1="84" x2="250" y2="120" stroke="{_AXIS}" stroke-width="0.7" stroke-dasharray="3 3"/>
  <line x1="430" y1="84" x2="430" y2="120" stroke="{_AXIS}" stroke-width="0.7" stroke-dasharray="3 3"/>
  <text x="40" y="136" font-size="10" font-weight="700" fill="{_INK}">That ~1% &#8220;other&#8221;</text>
  <g stroke="{_INK}" stroke-width="0.6">
    <rect x="40" y="142" width="360" height="30" fill="#fde68a"/>
    <rect x="400" y="142" width="16" height="30" fill="#ef4444"/>
    <rect x="416" y="142" width="14" height="30" fill="#a78bfa"/>
  </g>
  <text x="220" y="161" text-anchor="middle" font-size="9.5" font-weight="700" fill="{_INK}">Argon ~0.93%</text>
  <text x="408" y="136" text-anchor="middle" font-size="8" fill="#b91c1c">CO&#8322; ~0.04%</text>
  <text x="235" y="190" text-anchor="middle" font-size="9" fill="#6b7280">Tiny amounts of carbon dioxide, neon, and others make up the rest. Water vapor (0&#8211;4%) varies and is left out of &#8220;dry air.&#8221;</text>
  <text x="235" y="204" text-anchor="middle" font-size="9" fill="#6b7280">Though CO&#8322; is small, it is a key greenhouse gas.</text>
</svg>'''


# --- Weather: atmosphere layers with temperature profile -------------------
_ATMOSPHERE_LAYERS_DETAILED = f'''
<svg viewBox="0 0 480 320" role="img" aria-label="Layers of the atmosphere with altitude and a temperature profile that rises and falls" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="240" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Layers of the Atmosphere</text>
  <g stroke="#ffffff" stroke-width="1">
    <rect x="60" y="50" width="270" height="70" fill="#1e3a8a"/>
    <rect x="60" y="120" width="270" height="70" fill="#3b82f6"/>
    <rect x="60" y="190" width="270" height="60" fill="#60a5fa"/>
    <rect x="60" y="250" width="270" height="40" fill="#bfdbfe"/>
  </g>
  <rect x="60" y="290" width="270" height="12" fill="#65a30d"/>
  <g font-size="11" font-weight="700" fill="#ffffff">
    <text x="120" y="90">Thermosphere</text>
    <text x="120" y="160">Mesosphere</text>
  </g>
  <g font-size="11" font-weight="700" fill="{_INK}">
    <text x="120" y="224">Stratosphere</text>
    <text x="120" y="274">Troposphere</text>
  </g>
  <g font-size="8" fill="#e5e7eb">
    <text x="200" y="104">auroras, ISS orbit</text>
    <text x="200" y="174">meteors burn up</text>
  </g>
  <g font-size="8" fill="{_INK}">
    <text x="205" y="236">ozone layer; jets cruise</text>
    <text x="205" y="286">weather &amp; clouds</text>
  </g>
  <g font-size="8.5" fill="#6b7280" text-anchor="end">
    <text x="56" y="53">600 km</text>
    <text x="56" y="123">85 km</text>
    <text x="56" y="193">50 km</text>
    <text x="56" y="253">12 km</text>
    <text x="56" y="300">0 km</text>
  </g>
  <polyline points="430,290 360,250 435,190 352,120 458,55" fill="none" stroke="{_RED}" stroke-width="2"/>
  <g fill="{_RED}"><circle cx="430" cy="290" r="2.5"/><circle cx="360" cy="250" r="2.5"/><circle cx="435" cy="190" r="2.5"/><circle cx="352" cy="120" r="2.5"/><circle cx="458" cy="55" r="2.5"/></g>
  <text x="405" y="312" text-anchor="middle" font-size="8.5" fill="{_RED}">&#8592; colder    temperature    warmer &#8594;</text>
  <text x="463" y="44" text-anchor="end" font-size="8" fill="{_RED}">temp profile</text>
</svg>'''


# --- Weather: three ways heat moves ----------------------------------------
_HEAT_TRANSFER = f'''
<svg viewBox="0 0 470 200" role="img" aria-label="Three ways heat moves: radiation, conduction, and convection" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Three Ways Heat Moves</text>
  <g stroke="{_GRID}" stroke-width="1"><line x1="158" y1="34" x2="158" y2="180"/><line x1="314" y1="34" x2="314" y2="180"/></g>
  <!-- Radiation -->
  <circle cx="44" cy="60" r="15" fill="#facc15" stroke="#eab308"/>
  <g stroke="{_RED}" stroke-width="1.6">
    <line x1="58" y1="72" x2="92" y2="120"/><line x1="74" y1="64" x2="104" y2="118"/><line x1="40" y1="78" x2="70" y2="124"/>
  </g>
  <polygon points="92,120 82,116 88,110" fill="{_RED}"/><polygon points="104,118 95,114 100,108" fill="{_RED}"/>
  <rect x="30" y="124" width="110" height="12" fill="#65a30d"/>
  <text x="79" y="158" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Radiation</text>
  <text x="79" y="172" text-anchor="middle" font-size="8" fill="#6b7280">through empty space (Sun &#8594; Earth)</text>
  <!-- Conduction -->
  <rect x="178" y="92" width="118" height="16" fill="#f59e0b"/>
  <rect x="178" y="92" width="26" height="16" fill="#dc2626"/>
  <g stroke="#7c2d12" stroke-width="1.4" fill="#7c2d12">
    <line x1="210" y1="100" x2="232" y2="100"/><polygon points="236,100 228,96 228,104"/>
    <line x1="246" y1="100" x2="268" y2="100"/><polygon points="272,100 264,96 264,104"/>
  </g>
  <text x="191" y="86" text-anchor="middle" font-size="8" fill="#dc2626">flame</text>
  <text x="236" y="158" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Conduction</text>
  <text x="236" y="172" text-anchor="middle" font-size="8" fill="#6b7280">through direct contact (a hot spoon)</text>
  <!-- Convection -->
  <rect x="350" y="84" width="84" height="46" fill="#bae6fd" stroke="{_BLUE}" stroke-width="1"/>
  <polygon points="384,134 400,134 392,146" fill="#dc2626"/>
  <g stroke="{_RED}" stroke-width="1.6" fill="none">
    <path d="M392,126 C372,120 372,96 388,92"/><path d="M392,126 C412,120 412,96 396,92"/>
  </g>
  <polygon points="388,92 380,98 390,100" fill="{_RED}"/><polygon points="396,92 394,100 404,98" fill="{_RED}"/>
  <text x="392" y="158" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Convection</text>
  <text x="392" y="172" text-anchor="middle" font-size="8" fill="#6b7280">by a moving fluid (air or water loop)</text>
</svg>'''


# --- Weather: pressure & wind (the sea breeze) -----------------------------
_PRESSURE_WIND = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="A daytime sea breeze: warm air rises over land creating low pressure, cool air sinks over the sea, and surface wind blows from sea to land" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Pressure &amp; Wind: the Daytime Sea Breeze</text>
  <rect x="0" y="26" width="470" height="158" fill="#eaf6ff"/>
  <circle cx="44" cy="54" r="16" fill="#facc15" stroke="#eab308"/>
  <rect x="0" y="184" width="235" height="66" fill="#d9b483"/>
  <rect x="235" y="184" width="235" height="66" fill="#7dd3fc"/>
  <text x="118" y="222" text-anchor="middle" font-size="10" font-weight="700" fill="#7c4a12">warm land</text>
  <text x="352" y="222" text-anchor="middle" font-size="10" font-weight="700" fill="#0369a1">cooler sea</text>
  <!-- rising warm air over land (low) -->
  <line x1="118" y1="180" x2="118" y2="70" stroke="{_RED}" stroke-width="2.5"/><polygon points="118,64 112,76 124,76" fill="{_RED}"/>
  <circle cx="118" cy="150" r="13" fill="#fee2e2" stroke="{_RED}"/><text x="118" y="154" text-anchor="middle" font-size="12" font-weight="700" fill="{_RED}">L</text>
  <text x="150" y="110" font-size="8.5" fill="{_RED}">warm air rises</text>
  <!-- sinking cool air over sea (high) -->
  <line x1="360" y1="70" x2="360" y2="180" stroke="{_BLUE}" stroke-width="2.5"/><polygon points="360,184 354,172 366,172" fill="{_BLUE}"/>
  <circle cx="360" cy="150" r="13" fill="#dbeafe" stroke="{_BLUE}"/><text x="360" y="154" text-anchor="middle" font-size="12" font-weight="700" fill="{_BLUE}">H</text>
  <text x="392" y="110" text-anchor="middle" font-size="8.5" fill="{_BLUE}">cool air sinks</text>
  <!-- surface sea breeze (sea -> land) -->
  <line x1="346" y1="176" x2="138" y2="176" stroke="{_INK}" stroke-width="2.5"/><polygon points="132,176 144,170 144,182" fill="{_INK}"/>
  <text x="240" y="170" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">sea breeze (surface wind)</text>
  <!-- return flow aloft (land -> sea) -->
  <line x1="132" y1="74" x2="346" y2="74" stroke="{_AXIS}" stroke-width="2" stroke-dasharray="5 4"/><polygon points="352,74 340,68 340,80" fill="{_AXIS}"/>
  <text x="240" y="68" text-anchor="middle" font-size="8.5" fill="#6b7280">return flow aloft</text>
  <text x="235" y="242" text-anchor="middle" font-size="9.5" fill="#6b7280">The Sun heats land faster than water, so air flows from high pressure (cool sea) to low pressure (warm land).</text>
</svg>'''


# --- Weather: cold front vs. warm front ------------------------------------
_WEATHER_FRONTS = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="A cold front with cold air wedging under warm air, and a warm front with warm air gliding over cold air" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Cold Front vs. Warm Front</text>
  <!-- COLD FRONT (left) -->
  <rect x="14" y="32" width="216" height="158" fill="#eaf6ff"/>
  <rect x="14" y="190" width="216" height="14" fill="#65a30d"/>
  <path d="M14,190 L120,190 C150,190 150,80 175,60 L175,190 Z" fill="#bfdbfe" opacity="0.8"/>
  <text x="60" y="180" font-size="9" font-weight="700" fill="#1e3a8a">cold air</text>
  <text x="190" y="120" font-size="9" font-weight="700" fill="#b91c1c">warm air</text>
  <g fill="#374151"><ellipse cx="150" cy="60" rx="30" ry="20"/><ellipse cx="150" cy="44" rx="18" ry="14"/></g>
  <g stroke="{_BLUE}" stroke-width="2"><line x1="150" y1="84" x2="146" y2="110"/><line x1="162" y1="84" x2="158" y2="110"/><line x1="138" y1="84" x2="134" y2="110"/></g>
  <line x1="14" y1="204" x2="230" y2="204" stroke="{_BLUE}" stroke-width="2"/>
  <g fill="{_BLUE}"><polygon points="60,204 66,196 72,204"/><polygon points="110,204 116,196 122,204"/><polygon points="160,204 166,196 172,204"/></g>
  <text x="122" y="226" text-anchor="middle" font-size="8.5" fill="#6b7280">cold air shoves warm air up fast &#8594; tall clouds, brief heavy storms</text>
  <!-- WARM FRONT (right) -->
  <rect x="240" y="32" width="216" height="158" fill="#eaf6ff"/>
  <rect x="240" y="190" width="216" height="14" fill="#65a30d"/>
  <path d="M240,190 L240,150 C300,120 380,100 440,96 L440,190 Z" fill="#bfdbfe" opacity="0.8"/>
  <text x="270" y="178" font-size="9" font-weight="700" fill="#1e3a8a">cold air</text>
  <text x="400" y="80" font-size="9" font-weight="700" fill="#b91c1c">warm air</text>
  <g fill="#9ca3af"><ellipse cx="320" cy="110" rx="26" ry="9"/><ellipse cx="370" cy="100" rx="30" ry="9"/><ellipse cx="415" cy="92" rx="24" ry="8"/></g>
  <g stroke="{_BLUE}" stroke-width="1.5"><line x1="320" y1="120" x2="318" y2="150"/><line x1="345" y1="116" x2="343" y2="150"/><line x1="370" y1="112" x2="368" y2="150"/></g>
  <line x1="240" y1="204" x2="456" y2="204" stroke="{_RED}" stroke-width="2"/>
  <g fill="{_RED}"><path d="M300,204 a6,6 0 0 1 12,0 Z"/><path d="M350,204 a6,6 0 0 1 12,0 Z"/><path d="M400,204 a6,6 0 0 1 12,0 Z"/></g>
  <text x="348" y="226" text-anchor="middle" font-size="8.5" fill="#6b7280">warm air glides up slowly &#8594; wide layered clouds, steady light rain</text>
</svg>'''


# --- Weather: the greenhouse effect ----------------------------------------
_GREENHOUSE_EFFECT = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="The greenhouse effect: sunlight warms Earth, which radiates heat, and greenhouse gases send some heat back down" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Greenhouse Effect</text>
  <rect x="0" y="26" width="470" height="180" fill="#eaf6ff"/>
  <rect x="0" y="206" width="470" height="44" fill="#65a30d"/>
  <circle cx="42" cy="54" r="18" fill="#facc15" stroke="#eab308"/>
  <!-- greenhouse gas layer -->
  <rect x="20" y="96" width="430" height="26" fill="#d1d5db" opacity="0.55"/>
  <text x="235" y="113" text-anchor="middle" font-size="9" font-weight="700" fill="#374151">greenhouse gases (CO&#8322;, water vapor, methane)</text>
  <!-- incoming sunlight -->
  <line x1="64" y1="70" x2="150" y2="204" stroke="{_AMBER}" stroke-width="2.5"/><polygon points="150,204 140,198 148,192" fill="{_AMBER}"/>
  <text x="78" y="150" font-size="8.5" fill="#b45309" transform="rotate(58 78 150)">sunlight passes through</text>
  <!-- outgoing infrared from surface -->
  <line x1="250" y1="204" x2="250" y2="124" stroke="{_RED}" stroke-width="2.5"/><polygon points="250,118 244,130 256,130" fill="{_RED}"/>
  <line x1="330" y1="204" x2="330" y2="124" stroke="{_RED}" stroke-width="2.5"/><polygon points="330,118 324,130 336,130" fill="{_RED}"/>
  <text x="345" y="170" font-size="8.5" fill="#b91c1c">Earth radiates heat</text>
  <!-- re-radiated back down -->
  <line x1="290" y1="122" x2="290" y2="200" stroke="{_RED}" stroke-width="2" stroke-dasharray="5 4"/><polygon points="290,204 284,192 296,192" fill="{_RED}"/>
  <line x1="200" y1="122" x2="200" y2="200" stroke="{_RED}" stroke-width="2" stroke-dasharray="5 4"/><polygon points="200,204 194,192 206,192" fill="{_RED}"/>
  <text x="120" y="200" font-size="8.5" fill="#b91c1c">some heat sent back</text>
  <text x="235" y="232" text-anchor="middle" font-size="9.3" fill="#ffffff">Greenhouse gases trap some heat, keeping Earth warm. Adding more of them traps more heat (climate change).</text>
</svg>'''


# --- Solar system: the Sun's structure -------------------------------------
_SUN_ANATOMY = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="The Sun's structure: a fusion core, a hot surface with sunspots, and energy radiating outward" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Sun: Our Star</text>
  <circle cx="150" cy="135" r="108" fill="#fde68a" opacity="0.35"/>
  <circle cx="150" cy="135" r="92" fill="#fb923c" stroke="#ea580c" stroke-width="1.5"/>
  <circle cx="150" cy="135" r="60" fill="#f59e0b"/>
  <circle cx="150" cy="135" r="30" fill="#fde047" stroke="#eab308"/>
  <text x="150" y="132" text-anchor="middle" font-size="8" font-weight="700" fill="#7c2d12">CORE</text>
  <text x="150" y="144" text-anchor="middle" font-size="7" fill="#7c2d12">fusion</text>
  <ellipse cx="120" cy="100" rx="9" ry="6" fill="#9a3412"/>
  <ellipse cx="186" cy="160" rx="7" ry="5" fill="#9a3412"/>
  <g stroke="#f59e0b" stroke-width="2">
    <line x1="150" y1="35" x2="150" y2="20"/><line x1="258" y1="135" x2="274" y2="135"/>
    <line x1="74" y1="59" x2="63" y2="48"/><line x1="226" y1="59" x2="237" y2="48"/>
    <line x1="74" y1="211" x2="63" y2="222"/><line x1="226" y1="211" x2="237" y2="222"/>
  </g>
  <g stroke="#9ca3af" stroke-width="1">
    <line x1="180" y1="135" x2="320" y2="92"/>
    <line x1="205" y1="105" x2="320" y2="146"/>
    <line x1="129" y1="100" x2="300" y2="198"/>
  </g>
  <g font-size="10" fill="{_INK}">
    <text x="324" y="90">Core: hydrogen fuses into helium,</text>
    <text x="324" y="102" font-size="9" fill="#6b7280">releasing huge energy (nuclear fusion)</text>
    <text x="324" y="146">Surface (~5,500&#176;C) gives off</text>
    <text x="324" y="158" font-size="9" fill="#6b7280">light and heat</text>
    <text x="304" y="202">Sunspots: cooler, darker patches</text>
  </g>
  <text x="150" y="244" text-anchor="middle" font-size="9" fill="#6b7280">The Sun is a star holding about 99% of the solar system&#8217;s mass &#8212; its gravity keeps the planets in orbit.</text>
</svg>'''


# --- Solar system: layout & the two families of planets --------------------
_SOLAR_SYSTEM_LAYOUT = f'''
<svg viewBox="0 0 500 210" role="img" aria-label="The Sun and eight planets in order, the asteroid belt between Mars and Jupiter, split into inner rocky planets and outer giants" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="250" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Solar System (not to scale)</text>
  <circle cx="6" cy="105" r="42" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="24" y="109" font-size="10" font-weight="700" fill="#a16207">Sun</text>
  <line x1="56" y1="105" x2="498" y2="105" stroke="{_GRID}"/>
  <circle cx="80" cy="105" r="4" fill="#9ca3af"/>
  <circle cx="112" cy="105" r="6" fill="#d97706"/>
  <circle cx="146" cy="105" r="6" fill="{_BLUE}"/>
  <circle cx="178" cy="105" r="5" fill="#dc2626"/>
  <g fill="#9ca3af"><circle cx="205" cy="96" r="1.5"/><circle cx="212" cy="112" r="1.5"/><circle cx="219" cy="100" r="1.5"/><circle cx="226" cy="114" r="1.5"/><circle cx="233" cy="98" r="1.5"/><circle cx="240" cy="110" r="1.5"/></g>
  <circle cx="285" cy="105" r="18" fill="#d6a06a"/>
  <g><circle cx="360" cy="105" r="15" fill="#e3c69a"/><ellipse cx="360" cy="105" rx="26" ry="6" fill="none" stroke="#a8895f" stroke-width="2"/></g>
  <circle cx="425" cy="105" r="11" fill="#7dd3fc"/>
  <circle cx="475" cy="105" r="11" fill="#3b82f6"/>
  <g font-size="8" fill="{_INK}" text-anchor="middle">
    <text x="80" y="128">Mercury</text><text x="112" y="128">Venus</text><text x="146" y="128">Earth</text><text x="178" y="128">Mars</text>
    <text x="222" y="134">asteroid belt</text>
    <text x="285" y="138">Jupiter</text><text x="360" y="140">Saturn</text><text x="425" y="130">Uranus</text><text x="475" y="130">Neptune</text>
  </g>
  <g stroke="#9ca3af" stroke-width="1"><line x1="70" y1="160" x2="190" y2="160"/><line x1="262" y1="160" x2="492" y2="160"/></g>
  <g font-size="9.5" font-weight="700" fill="#6b7280" text-anchor="middle">
    <text x="130" y="176">Inner: small, rocky</text><text x="377" y="176">Outer: giant planets</text>
  </g>
  <text x="250" y="200" text-anchor="middle" font-size="8.5" fill="#6b7280">Order from the Sun: Mercury, Venus, Earth, Mars, (asteroid belt), Jupiter, Saturn, Uranus, Neptune.</text>
</svg>'''


# --- Solar system: orbits & gravity ----------------------------------------
_ORBIT_GRAVITY = f'''
<svg viewBox="0 0 440 270" role="img" aria-label="A planet's elliptical orbit around the Sun, balancing forward motion and the inward pull of gravity" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Why Planets Stay in Orbit</text>
  <ellipse cx="220" cy="140" rx="180" ry="95" fill="none" stroke="{_AXIS}" stroke-width="1.5" stroke-dasharray="4 4"/>
  <circle cx="170" cy="140" r="22" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="170" y="144" text-anchor="middle" font-size="9" font-weight="700" fill="#a16207">Sun</text>
  <circle cx="220" cy="45" r="9" fill="{_BLUE}" stroke="#1e40af"/>
  <line x1="220" y1="53" x2="180" y2="128" stroke="{_RED}" stroke-width="2.5"/><polygon points="177,135 178,122 186,128" fill="{_RED}"/>
  <text x="236" y="96" font-size="9" fill="{_RED}">gravity pulls inward</text>
  <line x1="220" y1="45" x2="300" y2="53" stroke="{_GREEN}" stroke-width="2.5"/><polygon points="306,54 294,49 295,59" fill="{_GREEN}"/>
  <text x="270" y="36" font-size="9" fill="#15803d">forward motion</text>
  <circle cx="40" cy="140" r="7" fill="{_BLUE}"/>
  <text x="40" y="164" text-anchor="middle" font-size="8" fill="{_INK}">faster when</text><text x="40" y="174" text-anchor="middle" font-size="8" fill="{_INK}">closer</text>
  <circle cx="400" cy="140" r="7" fill="{_BLUE}"/>
  <text x="400" y="164" text-anchor="middle" font-size="8" fill="{_INK}">slower when</text><text x="400" y="174" text-anchor="middle" font-size="8" fill="{_INK}">farther</text>
  <text x="220" y="226" text-anchor="middle" font-size="9.3" fill="#6b7280">An orbit balances two things: the planet&#8217;s forward motion and the Sun&#8217;s inward gravity.</text>
  <text x="220" y="244" text-anchor="middle" font-size="9.3" fill="#6b7280">Without gravity it would fly off straight; without motion it would fall into the Sun. One trip = one year.</text>
</svg>'''


# --- Solar system: the inner rocky planets ---------------------------------
_TERRESTRIAL_PLANETS = f'''
<svg viewBox="0 0 470 210" role="img" aria-label="The four inner rocky planets: Mercury, Venus, Earth, and Mars, with key features" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Inner, Rocky Planets</text>
  <circle cx="70" cy="68" r="16" fill="#9ca3af" stroke="#6b7280"/>
  <g fill="#6b7280"><circle cx="64" cy="64" r="2.5"/><circle cx="74" cy="72" r="2"/></g>
  <text x="70" y="100" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Mercury</text>
  <ellipse cx="180" cy="68" rx="26" ry="26" fill="#fde68a" opacity="0.25"/>
  <circle cx="180" cy="68" r="22" fill="#e0b070" stroke="#b45309"/>
  <text x="180" y="106" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Venus</text>
  <circle cx="295" cy="68" r="23" fill="{_BLUE}" stroke="#1e40af"/>
  <path d="M283,60 q10,-4 18,3 q-6,8 -16,6 Z" fill="#16a34a"/><path d="M298,76 q8,-2 12,4 q-7,4 -13,0 Z" fill="#16a34a"/>
  <text x="295" y="106" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Earth</text>
  <circle cx="405" cy="68" r="18" fill="#c1440e" stroke="#7c2d12"/>
  <circle cx="405" cy="54" r="4" fill="#ffffff" opacity="0.8"/>
  <text x="405" y="102" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Mars</text>
  <g font-size="8" fill="#6b7280" text-anchor="middle">
    <text x="70" y="120">no air;</text><text x="70" y="130">cratered</text>
    <text x="180" y="124">thick CO&#8322;;</text><text x="180" y="134">hottest planet</text>
    <text x="295" y="124">liquid water;</text><text x="295" y="134">life</text>
    <text x="405" y="120">red (rust);</text><text x="405" y="130">thin air, ice caps</text>
  </g>
  <text x="235" y="162" text-anchor="middle" font-size="9.3" fill="{_INK}">Small, dense, and made of rock and metal &#8212; with solid surfaces you could stand on.</text>
  <text x="235" y="182" text-anchor="middle" font-size="9" fill="#6b7280">Venus is hottest (not Mercury) because its thick carbon-dioxide air traps heat &#8212; a runaway greenhouse effect.</text>
</svg>'''


# --- Solar system: the outer giant planets ---------------------------------
_OUTER_PLANETS = f'''
<svg viewBox="0 0 470 210" role="img" aria-label="The four outer giant planets: Jupiter, Saturn, Uranus, and Neptune" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Outer, Giant Planets</text>
  <circle cx="80" cy="78" r="42" fill="#d6a06a" stroke="#9a6a34"/>
  <g stroke="#b07b42" stroke-width="3"><line x1="44" y1="66" x2="116" y2="66"/><line x1="40" y1="82" x2="120" y2="82"/><line x1="46" y1="96" x2="114" y2="96"/></g>
  <ellipse cx="92" cy="88" rx="7" ry="4" fill="#b91c1c"/>
  <text x="80" y="134" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Jupiter</text>
  <circle cx="210" cy="80" r="30" fill="#e3c69a" stroke="#a8895f"/>
  <ellipse cx="210" cy="80" rx="52" ry="12" fill="none" stroke="#a8895f" stroke-width="3"/>
  <text x="210" y="134" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Saturn</text>
  <circle cx="330" cy="82" r="22" fill="#7dd3fc" stroke="#0ea5e9"/>
  <ellipse cx="330" cy="82" rx="22" ry="34" fill="none" stroke="#0ea5e9" stroke-width="1.5" opacity="0.5"/>
  <text x="330" y="134" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Uranus</text>
  <circle cx="425" cy="82" r="21" fill="#3b82f6" stroke="#1e40af"/>
  <text x="425" y="134" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Neptune</text>
  <g font-size="8" fill="#6b7280" text-anchor="middle">
    <text x="80" y="148">largest; Great Red Spot</text>
    <text x="210" y="148">bright rings</text>
    <text x="330" y="148">tilted; icy</text>
    <text x="425" y="148">windy; icy</text>
  </g>
  <line x1="20" y1="162" x2="250" y2="162" stroke="{_GRID}"/><line x1="290" y1="162" x2="460" y2="162" stroke="{_GRID}"/>
  <g font-size="9" font-weight="700" fill="#6b7280" text-anchor="middle">
    <text x="135" y="178">Gas giants (Jupiter, Saturn)</text>
    <text x="375" y="178">Ice giants (Uranus, Neptune)</text>
  </g>
  <text x="235" y="200" text-anchor="middle" font-size="9" fill="#6b7280">Huge, cold balls of gas and ice with no solid surface &#8212; and many moons.</text>
</svg>'''


# --- Solar system: comet anatomy & small bodies ----------------------------
_COMET_ANATOMY = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="A comet with nucleus, coma, and a tail that always points away from the Sun" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="13.5" font-weight="700" fill="{_INK}">A Comet&#8217;s Tail Always Points Away from the Sun</text>
  <circle cx="58" cy="118" r="30" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="58" y="122" text-anchor="middle" font-size="9" font-weight="700" fill="#a16207">Sun</text>
  <path d="M108,118 C200,42 320,42 410,118" fill="none" stroke="{_GRID}" stroke-width="1.5" stroke-dasharray="5 4"/>
  <polygon points="305,58 360,30 372,40 308,66" fill="#a5b4fc" opacity="0.8"/>
  <polygon points="305,64 366,52 372,62 308,70" fill="#93c5fd" opacity="0.7"/>
  <circle cx="300" cy="62" r="12" fill="#bae6fd" opacity="0.6"/>
  <circle cx="300" cy="62" r="5" fill="#e5e7eb" stroke="#9ca3af"/>
  <g stroke="#9ca3af" stroke-width="1">
    <line x1="300" y1="64" x2="262" y2="108"/>
    <line x1="306" y1="58" x2="300" y2="108"/>
    <line x1="350" y1="38" x2="360" y2="98"/>
  </g>
  <g font-size="9" fill="{_INK}" text-anchor="middle">
    <text x="258" y="120">nucleus</text><text x="258" y="131" font-size="8" fill="#6b7280">icy center</text>
    <text x="305" y="120">coma</text><text x="305" y="131" font-size="8" fill="#6b7280">glowing gas/dust</text>
    <text x="362" y="110">tail</text><text x="362" y="121" font-size="8" fill="#6b7280">away from Sun</text>
  </g>
  <text x="235" y="160" text-anchor="middle" font-size="9.3" fill="#6b7280">The Sun&#8217;s heat and solar wind push the comet&#8217;s gas and dust outward, so the tail points away from the Sun.</text>
  <g font-size="8.5" fill="{_INK}">
    <text x="26" y="188" font-weight="700">Small bodies:</text>
    <text x="26" y="204">&#8226; Asteroid = rocky (mostly between Mars &amp; Jupiter)    &#8226; Comet = icy, grows a tail near the Sun</text>
    <text x="26" y="220">&#8226; Meteor = a streak of light (&#8220;shooting star&#8221;)    &#8226; Meteorite = a space rock that lands on the ground</text>
  </g>
</svg>'''


# --- Solar system: the scale of space --------------------------------------
_COSMIC_SCALE = f'''
<svg viewBox="0 0 480 215" role="img" aria-label="The scale of space measured in astronomical units and light travel time" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="240" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How Far Is Space? Measuring Huge Distances</text>
  <line x1="30" y1="80" x2="450" y2="80" stroke="{_AXIS}" stroke-width="2"/>
  <polygon points="456,80 444,75 444,85" fill="{_AXIS}"/>
  <g stroke="{_AXIS}" stroke-width="1.5">
    <line x1="50" y1="72" x2="50" y2="88"/><line x1="140" y1="72" x2="140" y2="88"/><line x1="300" y1="72" x2="300" y2="88"/><line x1="420" y1="72" x2="420" y2="88"/>
  </g>
  <g font-size="9" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="50" y="64">Earth&#8211;Moon</text><text x="140" y="64">Earth&#8211;Sun</text><text x="300" y="64">Neptune</text><text x="420" y="64">nearest star</text>
  </g>
  <g font-size="8.5" fill="#6b7280" text-anchor="middle">
    <text x="50" y="104">1.3 light-seconds</text>
    <text x="140" y="104">1 AU</text><text x="140" y="115">light: ~8 minutes</text>
    <text x="300" y="104">~30 AU</text><text x="300" y="115">light: ~4 hours</text>
    <text x="420" y="104">~4.2 light-years</text>
  </g>
  <g font-size="9" fill="{_INK}">
    <text x="30" y="148" font-weight="700">Two space rulers:</text>
    <text x="40" y="164">&#8226; AU (astronomical unit) = the average Earth&#8211;Sun distance (~150 million km).</text>
    <text x="40" y="180">&#8226; Light-year = how far light travels in one year (~9.5 trillion km).</text>
  </g>
  <text x="240" y="204" text-anchor="middle" font-size="9" fill="#6b7280">Distances are so vast that astronomers measure them by how long light takes to cross them.</text>
</svg>'''


# --- Moon & seasons: Earth's rotation and revolution -----------------------
_EARTH_ROTATION_REVOLUTION = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="Earth's two motions: rotation on its axis makes day and night; revolution around the Sun makes a year" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Earth&#8217;s Two Motions</text>
  <ellipse cx="180" cy="140" rx="150" ry="78" fill="none" stroke="{_AXIS}" stroke-width="1.4" stroke-dasharray="4 4"/>
  <circle cx="180" cy="140" r="26" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="180" y="144" text-anchor="middle" font-size="9" font-weight="700" fill="#a16207">Sun</text>
  <g transform="translate(330 140)">
    <circle r="30" fill="#1e293b"/>
    <path d="M0,-30 A30,30 0 0,1 0,30 Z" fill="#3b82f6"/>
    <line x1="0" y1="-40" x2="0" y2="40" stroke="{_INK}" stroke-width="1.4" stroke-dasharray="3 2"/>
    <text x="-15" y="4" text-anchor="middle" font-size="7" fill="#cbd5e1">night</text>
    <text x="16" y="4" text-anchor="middle" font-size="7" fill="#ffffff">day</text>
  </g>
  <path d="M348,101 a16,10 0 1 1 -12,-5" fill="none" stroke="{_GREEN}" stroke-width="2"/><polygon points="336,96 345,91 346,101" fill="{_GREEN}"/>
  <text x="330" y="86" text-anchor="middle" font-size="9" fill="#15803d">rotation = 1 day</text>
  <path d="M140,72 Q180,50 222,68" fill="none" stroke="{_RED}" stroke-width="2"/><polygon points="222,68 211,63 213,73" fill="{_RED}"/>
  <text x="180" y="44" text-anchor="middle" font-size="9" fill="{_RED}">revolution = 1 year</text>
  <text x="235" y="228" text-anchor="middle" font-size="9.3" fill="#6b7280">Rotation on its tilted axis gives day and night; revolution around the Sun gives the year.</text>
</svg>'''


# --- Moon & seasons: the Earth-Moon system ---------------------------------
_MOON_OVERVIEW = f'''
<svg viewBox="0 0 470 224" role="img" aria-label="The Moon orbits Earth, reflects sunlight, and always shows the same face to Earth" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Moon: Earth&#8217;s Companion</text>
  <g stroke="{_AMBER}" stroke-width="2"><line x1="14" y1="78" x2="58" y2="78"/><line x1="14" y1="116" x2="58" y2="116"/><line x1="14" y1="154" x2="58" y2="154"/></g>
  <polygon points="58,78 48,73 48,83" fill="{_AMBER}"/><polygon points="58,116 48,111 48,121" fill="{_AMBER}"/><polygon points="58,154 48,149 48,159" fill="{_AMBER}"/>
  <text x="30" y="60" font-size="9" fill="#b45309">sunlight</text>
  <ellipse cx="170" cy="116" rx="160" ry="66" fill="none" stroke="{_GRID}" stroke-dasharray="4 4"/>
  <circle cx="170" cy="116" r="34" fill="{_BLUE}" stroke="#1e40af"/>
  <path d="M170,82 A34,34 0 0,1 170,150 Z" fill="#1e293b" opacity="0.45"/>
  <text x="170" y="164" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Earth</text>
  <g transform="translate(360 116)">
    <circle r="20" fill="#1e293b"/>
    <path d="M0,-20 A20,20 0 0,1 0,20 Z" fill="#d1d5db"/>
    <circle cx="-6" cy="-6" r="2.5" fill="#9ca3af"/><circle cx="-3" cy="7" r="2" fill="#9ca3af"/>
  </g>
  <text x="360" y="150" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Moon</text>
  <g font-size="8.5" fill="#6b7280" text-anchor="middle">
    <text x="235" y="194">The Moon makes no light of its own &#8212; it reflects sunlight, so the lit half always faces the Sun.</text>
    <text x="235" y="208">It orbits Earth about every 27 days and keeps the same near side toward us; it is cratered with almost no air.</text>
  </g>
</svg>'''


# --- Moon & seasons: why the Moon has phases -------------------------------
_MOON_PHASES_DETAILED = f'''
<svg viewBox="0 0 470 332" role="img" aria-label="The Moon's phases: sunlight lights one half of the Moon as it orbits Earth, so we see different amounts lit" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Why the Moon Has Phases</text>
  <g stroke="{_AMBER}" stroke-width="2">
    <line x1="10" y1="100" x2="46" y2="100"/><line x1="10" y1="170" x2="46" y2="170"/><line x1="10" y1="240" x2="46" y2="240"/>
  </g>
  <polygon points="46,100 36,95 36,105" fill="{_AMBER}"/><polygon points="46,170 36,165 36,175" fill="{_AMBER}"/><polygon points="46,240 36,235 36,245" fill="{_AMBER}"/>
  <text x="28" y="84" font-size="9" fill="#b45309">sunlight</text>
  <ellipse cx="235" cy="170" rx="120" ry="110" fill="none" stroke="{_GRID}" stroke-dasharray="4 4"/>
  <circle cx="235" cy="170" r="24" fill="{_BLUE}" stroke="#1e40af"/>
  <text x="235" y="174" text-anchor="middle" font-size="8" font-weight="700" fill="#ffffff">Earth</text>
  <g stroke="#475569" stroke-width="0.6">
    <g><circle cx="115" cy="170" r="15" fill="#1e293b"/><path d="M115,155 A15,15 0 0,0 115,185 Z" fill="#f1f5f9"/></g>
    <g><circle cx="150" cy="93" r="15" fill="#1e293b"/><path d="M150,78 A15,15 0 0,0 150,108 Z" fill="#f1f5f9"/></g>
    <g><circle cx="235" cy="60" r="15" fill="#1e293b"/><path d="M235,45 A15,15 0 0,0 235,75 Z" fill="#f1f5f9"/></g>
    <g><circle cx="320" cy="93" r="15" fill="#1e293b"/><path d="M320,78 A15,15 0 0,0 320,108 Z" fill="#f1f5f9"/></g>
    <g><circle cx="355" cy="170" r="15" fill="#1e293b"/><path d="M355,155 A15,15 0 0,0 355,185 Z" fill="#f1f5f9"/></g>
    <g><circle cx="320" cy="247" r="15" fill="#1e293b"/><path d="M320,232 A15,15 0 0,0 320,262 Z" fill="#f1f5f9"/></g>
    <g><circle cx="235" cy="280" r="15" fill="#1e293b"/><path d="M235,265 A15,15 0 0,0 235,295 Z" fill="#f1f5f9"/></g>
    <g><circle cx="150" cy="247" r="15" fill="#1e293b"/><path d="M150,232 A15,15 0 0,0 150,262 Z" fill="#f1f5f9"/></g>
  </g>
  <g font-size="8.5" fill="{_INK}" text-anchor="middle">
    <text x="86" y="173">New</text>
    <text x="150" y="70">Wax. crescent</text>
    <text x="235" y="40">First quarter</text>
    <text x="320" y="70">Wax. gibbous</text>
    <text x="384" y="173">Full</text>
    <text x="320" y="276">Wan. gibbous</text>
    <text x="235" y="306">Last quarter</text>
    <text x="150" y="276">Wan. crescent</text>
  </g>
  <text x="235" y="324" text-anchor="middle" font-size="8.8" fill="#6b7280">The lit half always faces the Sun; from Earth we see it grow (waxing) then shrink (waning) over ~29.5 days.</text>
</svg>'''


# --- Moon & seasons: solar and lunar eclipses ------------------------------
_ECLIPSES = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="A solar eclipse has the Moon between Sun and Earth; a lunar eclipse has Earth between Sun and Moon" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Two Kinds of Eclipse</text>
  <!-- SOLAR (top) -->
  <circle cx="44" cy="74" r="20" fill="#facc15" stroke="#eab308"/>
  <text x="44" y="48" text-anchor="middle" font-size="8" fill="#a16207">Sun</text>
  <circle cx="230" cy="74" r="7" fill="#9ca3af"/>
  <circle cx="320" cy="74" r="22" fill="{_BLUE}" stroke="#1e40af"/>
  <polygon points="230,67 230,81 312,80 312,68" fill="#374151" opacity="0.4"/>
  <g stroke="{_AMBER}" stroke-width="1.2"><line x1="66" y1="68" x2="222" y2="70"/><line x1="66" y1="80" x2="222" y2="78"/></g>
  <text x="230" y="100" text-anchor="middle" font-size="8" fill="{_INK}">Moon</text>
  <text x="320" y="106" text-anchor="middle" font-size="8" fill="{_INK}">Earth</text>
  <text x="358" y="62" font-size="9.5" font-weight="700" fill="{_INK}">Solar eclipse</text>
  <text x="358" y="76" font-size="8" fill="#6b7280">Moon blocks the Sun</text>
  <text x="358" y="88" font-size="8" fill="#6b7280">(happens at new moon)</text>
  <line x1="14" y1="124" x2="456" y2="124" stroke="{_GRID}"/>
  <!-- LUNAR (bottom) -->
  <circle cx="44" cy="186" r="20" fill="#facc15" stroke="#eab308"/>
  <text x="44" y="160" text-anchor="middle" font-size="8" fill="#a16207">Sun</text>
  <circle cx="230" cy="186" r="22" fill="{_BLUE}" stroke="#1e40af"/>
  <circle cx="340" cy="186" r="9" fill="#6b7280"/>
  <polygon points="252,178 252,194 348,198 348,174" fill="#374151" opacity="0.45"/>
  <g stroke="{_AMBER}" stroke-width="1.2"><line x1="66" y1="180" x2="206" y2="182"/><line x1="66" y1="192" x2="206" y2="190"/></g>
  <text x="230" y="220" text-anchor="middle" font-size="8" fill="{_INK}">Earth</text>
  <text x="340" y="210" text-anchor="middle" font-size="8" fill="{_INK}">Moon</text>
  <text x="372" y="176" font-size="9.5" font-weight="700" fill="{_INK}">Lunar eclipse</text>
  <text x="372" y="190" font-size="8" fill="#6b7280">Earth&#8217;s shadow</text>
  <text x="372" y="202" font-size="8" fill="#6b7280">falls on the Moon</text>
  <text x="372" y="214" font-size="8" fill="#6b7280">(at full moon)</text>
</svg>'''


# --- Moon & seasons: the reason for the seasons ----------------------------
_SEASONS_DETAILED = f'''
<svg viewBox="0 0 470 268" role="img" aria-label="Earth's seasons come from its tilted axis: each hemisphere takes turns leaning toward the Sun" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Seasons: Earth&#8217;s Tilt (not distance)</text>
  <ellipse cx="235" cy="138" rx="175" ry="92" fill="none" stroke="{_GRID}" stroke-dasharray="4 4"/>
  <circle cx="235" cy="138" r="24" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
  <text x="235" y="142" text-anchor="middle" font-size="9" font-weight="700" fill="#a16207">Sun</text>
  <g>
    <circle cx="60" cy="138" r="20" fill="#3b82f6" stroke="#1e40af"/>
    <line x1="67" y1="124" x2="53" y2="152" stroke="{_INK}" stroke-width="1.5"/><circle cx="67" cy="124" r="2.6" fill="{_RED}"/>
  </g>
  <g>
    <circle cx="410" cy="138" r="20" fill="#3b82f6" stroke="#1e40af"/>
    <line x1="417" y1="124" x2="403" y2="152" stroke="{_INK}" stroke-width="1.5"/><circle cx="417" cy="124" r="2.6" fill="{_RED}"/>
  </g>
  <g>
    <circle cx="235" cy="50" r="18" fill="#3b82f6" stroke="#1e40af"/>
    <line x1="242" y1="37" x2="228" y2="63" stroke="{_INK}" stroke-width="1.5"/><circle cx="242" cy="37" r="2.4" fill="{_RED}"/>
  </g>
  <g>
    <circle cx="235" cy="226" r="18" fill="#3b82f6" stroke="#1e40af"/>
    <line x1="242" y1="213" x2="228" y2="239" stroke="{_INK}" stroke-width="1.5"/><circle cx="242" cy="213" r="2.4" fill="{_RED}"/>
  </g>
  <g font-size="9" fill="{_INK}" text-anchor="middle">
    <text x="60" y="180" font-weight="700">June</text><text x="60" y="192" font-size="8" fill="#6b7280">N. summer</text>
    <text x="410" y="180" font-weight="700">December</text><text x="410" y="192" font-size="8" fill="#6b7280">N. winter</text>
    <text x="235" y="28">equinox (spring/fall)</text>
    <text x="235" y="258">equinox (spring/fall)</text>
  </g>
  <text x="118" y="120" font-size="7.5" fill="#6b7280">N pole tilts</text><text x="118" y="129" font-size="7.5" fill="#6b7280">toward Sun</text>
  <text x="352" y="120" font-size="7.5" fill="#6b7280">N pole tilts</text><text x="352" y="129" font-size="7.5" fill="#6b7280">away from Sun</text>
</svg>'''


# --- Moon & seasons: tides -------------------------------------------------
_TIDES = f'''
<svg viewBox="0 0 470 226" role="img" aria-label="The Moon's gravity pulls Earth's oceans into bulges, creating high and low tides" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="200" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Tides: the Moon&#8217;s Gravity Pulls the Ocean</text>
  <ellipse cx="200" cy="118" rx="78" ry="52" fill="#7dd3fc" stroke="{_BLUE}" stroke-width="1"/>
  <circle cx="200" cy="118" r="50" fill="#86efac" stroke="#15803d"/>
  <text x="200" y="122" text-anchor="middle" font-size="10" font-weight="700" fill="#166534">Earth</text>
  <circle cx="420" cy="118" r="16" fill="#d1d5db" stroke="#9ca3af"/>
  <text x="420" y="122" text-anchor="middle" font-size="8" font-weight="700" fill="#6b7280">Moon</text>
  <line x1="288" y1="118" x2="398" y2="118" stroke="{_RED}" stroke-width="1.5" stroke-dasharray="4 3"/>
  <polygon points="288,118 298,113 298,123" fill="{_RED}"/>
  <text x="338" y="110" text-anchor="middle" font-size="8" fill="{_RED}">Moon&#8217;s pull</text>
  <g font-size="8.5" fill="{_INK}" text-anchor="middle">
    <text x="120" y="118" font-weight="700">high</text><text x="278" y="118" font-weight="700">high</text>
    <text x="200" y="60" font-weight="700">low</text><text x="200" y="184" font-weight="700">low</text>
  </g>
  <text x="235" y="206" text-anchor="middle" font-size="9" fill="#6b7280">High tides bulge on the sides facing toward and away from the Moon; low tides fall in between. The Sun adds to this, making stronger &#8220;spring&#8221; and weaker &#8220;neap&#8221; tides.</text>
</svg>'''


# --- Cell biology: timeline of discovering the cell ------------------------
_CELL_DISCOVERY_TIMELINE = f'''
<svg viewBox="0 0 480 165" role="img" aria-label="Timeline of key discoveries that led to the cell theory" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="240" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Discovering the Cell</text>
  <line x1="40" y1="78" x2="450" y2="78" stroke="{_AXIS}" stroke-width="2"/>
  <polygon points="456,78 444,73 444,83" fill="{_AXIS}"/>
  <g stroke="{_BLUE}" stroke-width="1.5"><line x1="70" y1="70" x2="70" y2="86"/><line x1="180" y1="70" x2="180" y2="86"/><line x1="300" y1="70" x2="300" y2="86"/><line x1="420" y1="70" x2="420" y2="86"/></g>
  <g fill="{_BLUE}"><circle cx="70" cy="78" r="4"/><circle cx="180" cy="78" r="4"/><circle cx="300" cy="78" r="4"/><circle cx="420" cy="78" r="4"/></g>
  <g font-size="10" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="70" y="60">1665</text><text x="180" y="60">1670s</text><text x="300" y="60">1838&#8211;39</text><text x="420" y="60">1855</text>
  </g>
  <g font-size="8" fill="#6b7280" text-anchor="middle">
    <text x="70" y="100">Hooke</text><text x="70" y="111">names &#8220;cells&#8221;</text><text x="70" y="122">(in cork)</text>
    <text x="180" y="100">Leeuwenhoek</text><text x="180" y="111">sees living</text><text x="180" y="122">microbes</text>
    <text x="300" y="100">Schleiden &amp;</text><text x="300" y="111">Schwann: all life</text><text x="300" y="122">is made of cells</text>
    <text x="420" y="100">Virchow:</text><text x="420" y="111">cells come</text><text x="420" y="122">from cells</text>
  </g>
  <text x="240" y="150" text-anchor="middle" font-size="9" fill="#6b7280">Better microscopes turned scattered observations into the three-part cell theory.</text>
</svg>'''


# --- Cell biology: prokaryotic vs eukaryotic cells -------------------------
_PROKARYOTE_EUKARYOTE = f'''
<svg viewBox="0 0 470 228" role="img" aria-label="A small prokaryotic cell without a nucleus next to a larger eukaryotic cell with a nucleus and organelles" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Two Kinds of Cell</text>
  <ellipse cx="115" cy="116" rx="80" ry="48" fill="#dcfce7" stroke="#15803d" stroke-width="3"/>
  <ellipse cx="115" cy="116" rx="74" ry="42" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
  <ellipse cx="110" cy="116" rx="22" ry="12" fill="none" stroke="{_BLUE}" stroke-width="2" transform="rotate(-18 110 116)"/>
  <text x="110" y="119" text-anchor="middle" font-size="6.5" fill="{_BLUE}">DNA</text>
  <g fill="#9ca3af"><circle cx="150" cy="104" r="2"/><circle cx="152" cy="128" r="2"/><circle cx="80" cy="132" r="2"/><circle cx="138" cy="142" r="2"/></g>
  <path d="M35,118 q-9,-8 -17,0 q-8,8 -16,0" fill="none" stroke="#15803d" stroke-width="1.5"/>
  <text x="115" y="184" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Prokaryote</text>
  <text x="115" y="197" text-anchor="middle" font-size="8" fill="#6b7280">bacteria &#8212; NO nucleus, small</text>
  <text x="115" y="208" text-anchor="middle" font-size="8" fill="#6b7280">DNA loops free in the cytoplasm</text>
  <ellipse cx="352" cy="114" rx="98" ry="66" fill="#eef2ff" stroke="{_BLUE}" stroke-width="2.5"/>
  <circle cx="345" cy="110" r="30" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5"/>
  <circle cx="352" cy="116" r="9" fill="#4f46e5"/>
  <ellipse cx="402" cy="86" rx="16" ry="8" fill="#fecaca" stroke="{_RED}"/>
  <path d="M300,148 q18,-10 34,2" fill="none" stroke="#7c3aed" stroke-width="2"/>
  <text x="352" y="196" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Eukaryote</text>
  <text x="352" y="209" text-anchor="middle" font-size="8" fill="#6b7280">plants, animals, fungi &#8212; HAS a nucleus &amp; organelles, larger</text>
</svg>'''


# --- Cell biology: detailed eukaryotic (animal) cell -----------------------
_EUKARYOTIC_CELL_DETAILED = f'''
<svg viewBox="0 0 470 300" role="img" aria-label="A detailed eukaryotic animal cell with labeled organelles" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Inside a Eukaryotic (Animal) Cell</text>
  <ellipse cx="210" cy="165" rx="150" ry="110" fill="#eef2ff" stroke="{_BLUE}" stroke-width="3"/>
  <circle cx="180" cy="150" r="46" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5"/>
  <circle cx="190" cy="158" r="13" fill="#4f46e5"/>
  <g stroke="#7c3aed" stroke-width="1.5" fill="none"><path d="M150,196 q30,14 64,4"/><path d="M150,206 q30,14 64,4"/></g>
  <g fill="#7c3aed"><circle cx="156" cy="199" r="1.6"/><circle cx="172" cy="205" r="1.6"/><circle cx="190" cy="207" r="1.6"/><circle cx="206" cy="204" r="1.6"/></g>
  <path d="M236,128 q26,-6 40,10 q-14,16 -40,8" fill="none" stroke="#a78bfa" stroke-width="1.5"/>
  <g stroke="#d97706" stroke-width="2" fill="none"><path d="M250,205 q26,-10 52,0"/><path d="M252,214 q24,-9 48,0"/><path d="M254,223 q22,-8 44,0"/></g>
  <ellipse cx="120" cy="110" rx="22" ry="11" fill="#fecaca" stroke="{_RED}" stroke-width="1.5"/>
  <path d="M104,110 q8,-7 16,0 q8,7 16,0" fill="none" stroke="{_RED}" stroke-width="1"/>
  <ellipse cx="300" cy="120" rx="20" ry="10" fill="#fecaca" stroke="{_RED}" stroke-width="1.5"/>
  <circle cx="150" cy="245" r="11" fill="#fed7aa" stroke="#ea580c"/>
  <g fill="#64748b"><circle cx="250" cy="150" r="2.5"/><circle cx="270" cy="170" r="2.5"/><circle cx="240" cy="240" r="2.5"/></g>
  <g stroke="#9ca3af" stroke-width="0.8">
    <line x1="190" y1="156" x2="60" y2="80"/><line x1="120" y1="110" x2="40" y2="120"/>
    <line x1="182" y1="201" x2="120" y2="240"/><line x1="276" y1="214" x2="360" y2="245"/>
    <line x1="300" y1="120" x2="400" y2="100"/><line x1="276" y1="138" x2="380" y2="140"/>
    <line x1="161" y1="245" x2="86" y2="262"/><line x1="270" y1="170" x2="360" y2="185"/>
  </g>
  <g font-size="9" fill="{_INK}">
    <text x="62" y="80" text-anchor="end">Nucleus (DNA, control)</text>
    <text x="38" y="123" text-anchor="end">Mitochondrion (energy)</text>
    <text x="118" y="244" text-anchor="end">Rough ER (+ ribosomes)</text>
    <text x="362" y="248" text-anchor="start">Golgi (packaging)</text>
    <text x="402" y="100" text-anchor="start">Mitochondrion</text>
    <text x="382" y="140" text-anchor="start">Smooth ER (lipids)</text>
    <text x="84" y="266" text-anchor="end">Lysosome (recycling)</text>
    <text x="362" y="188" text-anchor="start">Ribosomes (proteins)</text>
  </g>
  <text x="235" y="294" text-anchor="middle" font-size="8.5" fill="#6b7280">Like a factory: each organelle has a job, and the cell membrane is the outer gate.</text>
</svg>'''


# --- Cell biology: plant vs animal cell ------------------------------------
_PLANT_VS_ANIMAL_CELL = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="An animal cell next to a plant cell, highlighting the cell wall, chloroplasts, and large vacuole" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Animal Cell vs. Plant Cell</text>
  <ellipse cx="120" cy="120" rx="95" ry="78" fill="#eef2ff" stroke="{_BLUE}" stroke-width="2.5"/>
  <circle cx="110" cy="110" r="28" fill="#c7d2fe" stroke="#4f46e5"/><circle cx="116" cy="116" r="8" fill="#4f46e5"/>
  <ellipse cx="160" cy="142" rx="16" ry="8" fill="#fecaca" stroke="{_RED}"/>
  <text x="120" y="212" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Animal cell</text>
  <text x="120" y="226" text-anchor="middle" font-size="8" fill="#6b7280">round; membrane only</text>
  <rect x="262" y="48" width="176" height="150" rx="6" fill="#dcfce7" stroke="#15803d" stroke-width="4"/>
  <rect x="270" y="56" width="160" height="134" rx="4" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
  <rect x="300" y="80" width="100" height="86" rx="8" fill="#bae6fd" stroke="#38bdf8"/>
  <text x="350" y="126" text-anchor="middle" font-size="8" fill="#0369a1">large vacuole</text>
  <circle cx="300" cy="120" r="22" fill="#c7d2fe" stroke="#4f46e5"/><circle cx="306" cy="126" r="7" fill="#4f46e5"/>
  <g fill="#16a34a" stroke="#15803d"><ellipse cx="408" cy="78" rx="12" ry="6"/><ellipse cx="290" cy="178" rx="12" ry="6"/></g>
  <text x="350" y="212" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Plant cell</text>
  <text x="350" y="226" text-anchor="middle" font-size="8" fill="#6b7280">rectangular; wall + chloroplasts + big vacuole</text>
  <g stroke="#9ca3af" stroke-width="0.8">
    <line x1="262" y1="52" x2="240" y2="40"/><line x1="408" y1="78" x2="448" y2="64"/>
  </g>
  <g font-size="8" fill="{_INK}">
    <text x="238" y="40" text-anchor="end">cell wall</text>
    <text x="450" y="64" text-anchor="start">chloroplast</text>
  </g>
</svg>'''


# --- Cell biology: membrane transport --------------------------------------
_MEMBRANE_TRANSPORT = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="The cell membrane with passive transport down a gradient and active transport using energy against a gradient" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Crossing the Cell Membrane</text>
  <text x="40" y="52" font-size="8" fill="#6b7280">outside the cell</text>
  <text x="40" y="172" font-size="8" fill="#6b7280">inside the cell</text>
  <rect x="30" y="96" width="410" height="40" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
  <line x1="30" y1="116" x2="440" y2="116" stroke="#d97706" stroke-width="0.6" stroke-dasharray="3 3"/>
  <text x="35" y="113" font-size="7.5" fill="#b45309">phospholipid bilayer</text>
  <g fill="{_GREEN}"><circle cx="100" cy="66" r="3"/><circle cx="118" cy="74" r="3"/><circle cx="134" cy="62" r="3"/><circle cx="112" cy="58" r="3"/><circle cx="128" cy="80" r="3"/></g>
  <circle cx="118" cy="168" r="3" fill="{_GREEN}"/>
  <line x1="118" y1="84" x2="118" y2="150" stroke="{_INK}" stroke-width="2"/><polygon points="118,156 112,144 124,144" fill="{_INK}"/>
  <text x="118" y="192" text-anchor="middle" font-size="8.5" font-weight="700" fill="{_INK}">Diffusion</text>
  <text x="118" y="203" text-anchor="middle" font-size="7.5" fill="#6b7280">passive: high &#8594; low</text>
  <rect x="222" y="92" width="6" height="48" fill="#60a5fa"/><rect x="246" y="92" width="6" height="48" fill="#60a5fa"/>
  <circle cx="237" cy="82" r="3.4" fill="{_BLUE}"/><line x1="237" y1="92" x2="237" y2="150" stroke="{_BLUE}" stroke-width="1.5" stroke-dasharray="3 2"/><circle cx="237" cy="156" r="3.4" fill="{_BLUE}"/>
  <text x="237" y="192" text-anchor="middle" font-size="8.5" font-weight="700" fill="{_INK}">Facilitated</text>
  <text x="237" y="203" text-anchor="middle" font-size="7.5" fill="#6b7280">passive: via a protein</text>
  <rect x="350" y="90" width="26" height="52" rx="6" fill="#fecaca" stroke="{_RED}"/>
  <circle cx="363" cy="160" r="3.4" fill="{_RED}"/><line x1="363" y1="150" x2="363" y2="92" stroke="{_RED}" stroke-width="2"/><polygon points="363,86 357,98 369,98" fill="{_RED}"/>
  <text x="398" y="118" font-size="8" font-weight="700" fill="{_AMBER}">ATP</text>
  <text x="363" y="192" text-anchor="middle" font-size="8.5" font-weight="700" fill="{_INK}">Active transport</text>
  <text x="363" y="203" text-anchor="middle" font-size="7.5" fill="#6b7280">needs energy: low &#8594; high</text>
  <text x="235" y="228" text-anchor="middle" font-size="9" fill="#6b7280">Passive transport moves WITH the gradient (no energy); active transport pumps AGAINST it using ATP.</text>
</svg>'''


# --- Cell biology: the cell cycle ------------------------------------------
_CELL_CYCLE = f'''
<svg viewBox="0 0 440 270" role="img" aria-label="The cell cycle: a long interphase, then mitosis and cytokinesis, producing two identical cells" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Cell Cycle</text>
  <circle cx="150" cy="150" r="84" fill="none" stroke="{_GRID}" stroke-width="16"/>
  <path d="M150,66 A84,84 0 1 1 66,150" fill="none" stroke="{_BLUE}" stroke-width="16"/>
  <path d="M66,150 A84,84 0 0 1 150,66" fill="none" stroke="{_RED}" stroke-width="16"/>
  <text x="186" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#1e40af">Interphase</text>
  <text x="150" y="166" text-anchor="middle" font-size="8" fill="#1e40af">G1 &#183; S &#183; G2</text>
  <text x="150" y="178" text-anchor="middle" font-size="7.5" fill="#6b7280">grow &amp; copy DNA</text>
  <text x="92" y="104" text-anchor="middle" font-size="9" font-weight="700" fill="#b91c1c">Mitosis</text>
  <line x1="240" y1="150" x2="286" y2="150" stroke="{_AXIS}" stroke-width="1.5"/><polygon points="292,150 280,145 280,155" fill="{_AXIS}"/>
  <circle cx="330" cy="118" r="22" fill="#eef2ff" stroke="{_BLUE}"/><circle cx="330" cy="118" r="8" fill="#c7d2fe" stroke="#4f46e5"/>
  <circle cx="330" cy="186" r="22" fill="#eef2ff" stroke="{_BLUE}"/><circle cx="330" cy="186" r="8" fill="#c7d2fe" stroke="#4f46e5"/>
  <text x="385" y="150" text-anchor="middle" font-size="8.5" fill="{_INK}">two identical</text><text x="385" y="161" text-anchor="middle" font-size="8.5" fill="{_INK}">daughter cells</text>
  <text x="220" y="256" text-anchor="middle" font-size="9" fill="#6b7280">A cell spends most of its life in interphase; mitosis then splits it into two identical cells for growth &amp; repair.</text>
</svg>'''


# --- Cellular energy: the ATP-ADP cycle ------------------------------------
_ATP_ADP_CYCLE = f'''
<svg viewBox="0 0 440 240" role="img" aria-label="The ATP-ADP cycle: energy charges ADP into ATP, and ATP releases energy to do cell work" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="220" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">ATP: the Cell&#8217;s Energy Currency</text>
  <rect x="36" y="92" width="118" height="56" rx="10" fill="#e5e7eb" stroke="#9ca3af" stroke-width="1.5"/>
  <text x="95" y="116" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">ADP + P</text>
  <text x="95" y="134" text-anchor="middle" font-size="8" fill="#6b7280">low energy</text>
  <rect x="286" y="92" width="118" height="56" rx="10" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="345" y="116" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">ATP</text>
  <text x="345" y="134" text-anchor="middle" font-size="8" fill="#6b7280">charged battery</text>
  <path d="M150,96 C210,60 230,60 290,96" fill="none" stroke="{_RED}" stroke-width="2.5"/>
  <polygon points="290,96 278,90 282,100" fill="{_RED}"/>
  <text x="220" y="58" text-anchor="middle" font-size="9" fill="{_RED}">energy stored (from food / respiration)</text>
  <path d="M290,144 C230,180 210,180 150,144" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <polygon points="150,144 162,150 158,140" fill="{_BLUE}"/>
  <text x="220" y="196" text-anchor="middle" font-size="9" fill="{_BLUE}">energy released (powers cell work)</text>
  <text x="220" y="222" text-anchor="middle" font-size="8.5" fill="#6b7280">Adding a phosphate stores energy; removing it releases energy &#8212; like charging and using a battery.</text>
</svg>'''


# --- Cellular energy: photosynthesis overview ------------------------------
_PHOTOSYNTHESIS_OVERVIEW = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="Photosynthesis in a chloroplast: carbon dioxide, water, and light become glucose and oxygen" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Photosynthesis (in the chloroplast)</text>
  <circle cx="44" cy="60" r="16" fill="#facc15" stroke="#eab308"/>
  <g stroke="#eab308" stroke-width="1.5"><line x1="44" y1="38" x2="44" y2="30"/><line x1="22" y1="60" x2="14" y2="60"/></g>
  <ellipse cx="235" cy="135" rx="92" ry="56" fill="#dcfce7" stroke="#15803d" stroke-width="2.5"/>
  <g stroke="#16a34a" stroke-width="1.2" fill="none"><ellipse cx="210" cy="125" rx="20" ry="9"/><ellipse cx="255" cy="150" rx="20" ry="9"/><ellipse cx="245" cy="118" rx="16" ry="7"/></g>
  <text x="235" y="190" text-anchor="middle" font-size="9" fill="#15803d">chloroplast (has chlorophyll)</text>
  <g font-size="10" fill="{_INK}" text-anchor="end">
    <text x="120" y="110">CO&#8322;</text><text x="120" y="139">H&#8322;O</text><text x="120" y="166">light</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="1.8">
    <line x1="124" y1="106" x2="148" y2="116"/><line x1="124" y1="135" x2="148" y2="135"/><line x1="124" y1="162" x2="148" y2="152"/>
  </g>
  <g fill="{_AXIS}">
    <polygon points="150,117 140,112 142,121"/><polygon points="150,135 140,130 140,140"/><polygon points="150,151 140,147 142,156"/>
  </g>
  <g stroke="{_GREEN}" stroke-width="1.8">
    <line x1="322" y1="118" x2="346" y2="108"/><line x1="322" y1="152" x2="346" y2="162"/>
  </g>
  <g fill="{_GREEN}">
    <polygon points="350,106 340,107 344,115"/><polygon points="350,164 340,156 344,163"/>
  </g>
  <g font-size="10" font-weight="700" fill="{_INK}" text-anchor="start">
    <text x="352" y="106">glucose (sugar)</text><text x="352" y="166">oxygen (O&#8322;)</text>
  </g>
  <text x="235" y="224" text-anchor="middle" font-size="9" fill="#6b7280">6 CO&#8322; + 6 H&#8322;O + light &#8594; glucose + 6 O&#8322;</text>
  <text x="235" y="240" text-anchor="middle" font-size="8.5" fill="#6b7280">Light energy is stored as chemical energy in sugar.</text>
</svg>'''


# --- Cellular energy: cellular respiration overview ------------------------
_RESPIRATION_OVERVIEW = f'''
<svg viewBox="0 0 470 248" role="img" aria-label="Cellular respiration in a mitochondrion: glucose and oxygen become carbon dioxide, water, and ATP" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Cellular Respiration (in the mitochondrion)</text>
  <ellipse cx="235" cy="135" rx="100" ry="52" fill="#fee2e2" stroke="{_RED}" stroke-width="2.5"/>
  <path d="M150,135 q20,-22 44,0 q22,22 44,0 q22,-22 44,0" fill="none" stroke="#b91c1c" stroke-width="1.6"/>
  <text x="235" y="184" text-anchor="middle" font-size="9" fill="#b91c1c">mitochondrion (folded inner membrane)</text>
  <g font-size="10" fill="{_INK}" text-anchor="end"><text x="120" y="120">glucose</text><text x="120" y="150">O&#8322;</text></g>
  <g stroke="{_AXIS}" stroke-width="1.8"><line x1="124" y1="118" x2="150" y2="125"/><line x1="124" y1="148" x2="150" y2="142"/></g>
  <g fill="{_AXIS}"><polygon points="154,126 144,121 145,131"/><polygon points="154,141 144,137 145,147"/></g>
  <g stroke="{_GREEN}" stroke-width="1.8"><line x1="322" y1="110" x2="348" y2="103"/></g>
  <g fill="{_GREEN}"><polygon points="352,101 342,103 346,111"/></g>
  <g stroke="{_AXIS}" stroke-width="1.8"><line x1="322" y1="130" x2="348" y2="128"/><line x1="322" y1="150" x2="348" y2="156"/></g>
  <g fill="{_AXIS}"><polygon points="352,128 342,124 343,133"/><polygon points="352,157 342,153 343,162"/></g>
  <g font-size="10" font-weight="700" fill="{_INK}" text-anchor="start"><text x="352" y="106">ATP (energy!)</text><text x="352" y="132">CO&#8322;</text><text x="352" y="158">H&#8322;O</text></g>
  <text x="235" y="216" text-anchor="middle" font-size="9" fill="#6b7280">glucose + 6 O&#8322; &#8594; 6 CO&#8322; + 6 H&#8322;O + ATP</text>
  <text x="235" y="232" text-anchor="middle" font-size="8.5" fill="#6b7280">Energy stored in sugar is released as usable ATP.</text>
</svg>'''


# --- Cellular energy: photosynthesis & respiration linked ------------------
_PHOTO_RESP_LINK = f'''
<svg viewBox="0 0 470 244" role="img" aria-label="Photosynthesis and cellular respiration are linked: the outputs of one are the inputs of the other" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Two Halves of an Energy Cycle</text>
  <rect x="30" y="80" width="150" height="90" rx="12" fill="#dcfce7" stroke="{_GREEN}" stroke-width="2"/>
  <text x="105" y="108" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Photosynthesis</text>
  <text x="105" y="128" text-anchor="middle" font-size="8.5" fill="{_INK}">in chloroplasts</text>
  <text x="105" y="144" text-anchor="middle" font-size="8.5" fill="{_INK}">stores energy in sugar</text>
  <rect x="290" y="80" width="150" height="90" rx="12" fill="#fee2e2" stroke="{_RED}" stroke-width="2"/>
  <text x="365" y="108" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c">Respiration</text>
  <text x="365" y="128" text-anchor="middle" font-size="8.5" fill="{_INK}">in mitochondria</text>
  <text x="365" y="144" text-anchor="middle" font-size="8.5" fill="{_INK}">releases energy (ATP)</text>
  <path d="M180,98 C230,70 240,70 290,98" fill="none" stroke="{_GREEN}" stroke-width="2.5"/><polygon points="290,98 278,92 282,102" fill="{_GREEN}"/>
  <text x="235" y="66" text-anchor="middle" font-size="9" fill="#15803d">glucose + oxygen &#8594;</text>
  <path d="M290,152 C240,180 230,180 180,152" fill="none" stroke="{_RED}" stroke-width="2.5"/><polygon points="180,152 192,158 188,148" fill="{_RED}"/>
  <text x="235" y="196" text-anchor="middle" font-size="9" fill="#b91c1c">&#8592; carbon dioxide + water</text>
  <circle cx="44" cy="58" r="14" fill="#facc15" stroke="#eab308"/><line x1="58" y1="66" x2="84" y2="84" stroke="#eab308" stroke-width="2"/>
  <text x="235" y="222" text-anchor="middle" font-size="8.5" fill="#6b7280">The products of each process are the raw materials of the other &#8212; carbon and oxygen keep cycling.</text>
</svg>'''


# --- Cellular energy: fermentation pathways --------------------------------
_FERMENTATION_PATHS = f'''
<svg viewBox="0 0 470 280" role="img" aria-label="Glucose breakdown: with oxygen aerobic respiration makes much ATP; without oxygen fermentation makes little ATP" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">With Oxygen vs. Without Oxygen</text>
  <rect x="180" y="36" width="110" height="34" rx="8" fill="#fef3c7" stroke="{_AMBER}"/>
  <text x="235" y="58" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309">Glucose</text>
  <line x1="235" y1="70" x2="235" y2="92" stroke="{_AXIS}" stroke-width="1.5"/><polygon points="235,96 230,86 240,86" fill="{_AXIS}"/>
  <text x="316" y="86" font-size="8" fill="#6b7280">glycolysis (a little ATP)</text>
  <line x1="235" y1="100" x2="120" y2="130" stroke="{_AXIS}" stroke-width="1.5"/><polygon points="116,131 128,129 123,138" fill="{_AXIS}"/>
  <line x1="235" y1="100" x2="350" y2="130" stroke="{_AXIS}" stroke-width="1.5"/><polygon points="354,131 342,129 347,138" fill="{_AXIS}"/>
  <text x="150" y="118" font-size="8.5" font-weight="700" fill="#15803d">oxygen present</text>
  <text x="322" y="118" font-size="8.5" font-weight="700" fill="#b91c1c">no oxygen</text>
  <rect x="40" y="138" width="160" height="64" rx="10" fill="#dcfce7" stroke="{_GREEN}"/>
  <text x="120" y="160" text-anchor="middle" font-size="10.5" font-weight="700" fill="#15803d">Aerobic respiration</text>
  <text x="120" y="176" text-anchor="middle" font-size="8.5" fill="{_INK}">in mitochondria</text>
  <text x="120" y="192" text-anchor="middle" font-size="8.5" font-weight="700" fill="{_INK}">LOTS of ATP (~36)</text>
  <rect x="270" y="138" width="160" height="64" rx="10" fill="#fee2e2" stroke="{_RED}"/>
  <text x="350" y="160" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b91c1c">Fermentation</text>
  <text x="350" y="176" text-anchor="middle" font-size="8.5" fill="{_INK}">no oxygen needed</text>
  <text x="350" y="192" text-anchor="middle" font-size="8.5" font-weight="700" fill="{_INK}">little ATP (~2)</text>
  <line x1="310" y1="202" x2="300" y2="226" stroke="{_AXIS}" stroke-width="1.2"/><polygon points="299,230 305,221 308,231" fill="{_AXIS}"/>
  <line x1="390" y1="202" x2="400" y2="226" stroke="{_AXIS}" stroke-width="1.2"/><polygon points="401,230 392,221 395,231" fill="{_AXIS}"/>
  <text x="290" y="246" text-anchor="middle" font-size="8.5" fill="{_INK}">Lactic acid</text>
  <text x="290" y="257" text-anchor="middle" font-size="7.5" fill="#6b7280">(muscles, yogurt)</text>
  <text x="410" y="246" text-anchor="middle" font-size="8.5" fill="{_INK}">Alcohol + CO&#8322;</text>
  <text x="410" y="257" text-anchor="middle" font-size="7.5" fill="#6b7280">(yeast, bread)</text>
  <text x="235" y="274" text-anchor="middle" font-size="8.5" fill="#6b7280">Both start with glycolysis; oxygen lets cells extract far more energy from glucose.</text>
</svg>'''


# --- Cellular energy: photosynthesis rate vs light -------------------------
_PHOTOSYNTHESIS_RATE_GRAPH = f'''
<svg viewBox="0 0 360 238" role="img" aria-label="A graph of photosynthesis rate rising with light intensity then leveling off" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="180" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Photosynthesis Rate vs. Light Intensity</text>
  <line x1="50" y1="34" x2="50" y2="195" stroke="{_AXIS}"/>
  <line x1="50" y1="195" x2="330" y2="195" stroke="{_AXIS}"/>
  <text x="22" y="115" font-size="10" fill="#6b7280" transform="rotate(-90 22 115)" text-anchor="middle">O&#8322; produced (rate)</text>
  <text x="190" y="222" font-size="10" fill="#6b7280" text-anchor="middle">Light intensity</text>
  <path d="M50,180 C110,150 150,80 210,68 C260,60 300,60 320,60" fill="none" stroke="{_GREEN}" stroke-width="2.5"/>
  <line x1="210" y1="68" x2="320" y2="68" stroke="{_AXIS}" stroke-width="0.8" stroke-dasharray="4 3"/>
  <text x="262" y="56" font-size="8.5" fill="#6b7280" text-anchor="middle">levels off (another factor limits)</text>
  <text x="108" y="118" font-size="8.5" fill="#15803d">more light &#8594; faster</text>
</svg>'''


# --- Genetics: DNA double helix --------------------------------------------
_DNA_DOUBLE_HELIX = f'''
<svg viewBox="0 0 440 272" role="img" aria-label="DNA as a double helix: two backbones joined by base pairs A-T and G-C" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="220" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">DNA: the Molecule of Heredity</text>
  <rect x="146" y="50" width="8" height="184" rx="4" fill="#6b7280"/>
  <rect x="286" y="50" width="8" height="184" rx="4" fill="#6b7280"/>
  <g font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">
    <rect x="154" y="55" width="64" height="18" fill="#ef4444"/><rect x="222" y="55" width="64" height="18" fill="#f59e0b"/><text x="186" y="68">A</text><text x="254" y="68">T</text>
    <rect x="154" y="81" width="64" height="18" fill="#3b82f6"/><rect x="222" y="81" width="64" height="18" fill="#22c55e"/><text x="186" y="94">C</text><text x="254" y="94">G</text>
    <rect x="154" y="107" width="64" height="18" fill="#f59e0b"/><rect x="222" y="107" width="64" height="18" fill="#ef4444"/><text x="186" y="120">T</text><text x="254" y="120">A</text>
    <rect x="154" y="133" width="64" height="18" fill="#22c55e"/><rect x="222" y="133" width="64" height="18" fill="#3b82f6"/><text x="186" y="146">G</text><text x="254" y="146">C</text>
    <rect x="154" y="159" width="64" height="18" fill="#ef4444"/><rect x="222" y="159" width="64" height="18" fill="#f59e0b"/><text x="186" y="172">A</text><text x="254" y="172">T</text>
    <rect x="154" y="185" width="64" height="18" fill="#f59e0b"/><rect x="222" y="185" width="64" height="18" fill="#ef4444"/><text x="186" y="198">T</text><text x="254" y="198">A</text>
    <rect x="154" y="211" width="64" height="18" fill="#3b82f6"/><rect x="222" y="211" width="64" height="18" fill="#22c55e"/><text x="186" y="224">C</text><text x="254" y="224">G</text>
  </g>
  <line x1="150" y1="52" x2="112" y2="46" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="108" y="48" text-anchor="end" font-size="8.5" fill="{_INK}">sugar-phosphate backbone</text>
  <text x="220" y="258" text-anchor="middle" font-size="9" fill="#6b7280">The ladder twists into a double helix. Bases always pair the same way: A with T, G with C.</text>
</svg>'''


# --- Genetics: chromosome to DNA to gene -----------------------------------
_DNA_GENE_CHROMOSOME = f'''
<svg viewBox="0 0 460 222" role="img" aria-label="From chromosome to DNA to gene: a chromosome is packed DNA and a gene is a segment of it" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Chromosome &#8594; DNA &#8594; Gene</text>
  <g stroke="#7c3aed" stroke-width="10" stroke-linecap="round">
    <line x1="70" y1="70" x2="100" y2="120"/><line x1="100" y1="70" x2="70" y2="120"/>
    <line x1="70" y1="120" x2="100" y2="170"/><line x1="100" y1="120" x2="70" y2="170"/>
  </g>
  <text x="85" y="192" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Chromosome</text>
  <text x="85" y="205" text-anchor="middle" font-size="8" fill="#6b7280">tightly packed DNA</text>
  <line x1="118" y1="120" x2="158" y2="120" stroke="{_AXIS}" stroke-width="1.8"/><polygon points="164,120 152,114 152,126" fill="{_AXIS}"/>
  <g stroke="#6b7280" stroke-width="4" fill="none">
    <path d="M186,70 q24,25 0,50 q-24,25 0,50"/>
    <path d="M226,70 q-24,25 0,50 q24,25 0,50"/>
  </g>
  <g stroke="#9ca3af" stroke-width="2"><line x1="190" y1="84" x2="222" y2="84"/><line x1="186" y1="104" x2="226" y2="104"/><line x1="190" y1="124" x2="222" y2="124"/><line x1="186" y1="146" x2="226" y2="146"/><line x1="190" y1="166" x2="222" y2="166"/></g>
  <text x="206" y="192" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">DNA</text>
  <text x="206" y="205" text-anchor="middle" font-size="8" fill="#6b7280">double helix</text>
  <line x1="248" y1="120" x2="288" y2="120" stroke="{_AXIS}" stroke-width="1.8"/><polygon points="294,120 282,114 282,126" fill="{_AXIS}"/>
  <g stroke="#6b7280" stroke-width="4" fill="none">
    <path d="M326,70 q24,25 0,50 q-24,25 0,50"/>
    <path d="M366,70 q-24,25 0,50 q24,25 0,50"/>
  </g>
  <rect x="318" y="96" width="56" height="48" rx="6" fill="none" stroke="{_RED}" stroke-width="2.5"/>
  <text x="346" y="192" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Gene</text>
  <text x="346" y="205" text-anchor="middle" font-size="8" fill="#6b7280">a segment of DNA</text>
  <text x="406" y="116" font-size="8" fill="{_RED}">one</text><text x="406" y="127" font-size="8" fill="{_RED}">gene</text>
</svg>'''


# --- Genetics: dominant & recessive genotypes ------------------------------
_DOMINANT_RECESSIVE = f'''
<svg viewBox="0 0 460 224" role="img" aria-label="Genotypes TT, Tt, and tt and the tall or short phenotype each produces" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">One Gene, Two Alleles (T = tall, t = short)</text>
  <line x1="30" y1="150" x2="430" y2="150" stroke="#a8a29e" stroke-width="2"/>
  <line x1="90" y1="150" x2="90" y2="64" stroke="#15803d" stroke-width="3"/>
  <ellipse cx="80" cy="100" rx="10" ry="5" fill="#16a34a"/><ellipse cx="100" cy="118" rx="10" ry="5" fill="#16a34a"/><circle cx="90" cy="60" r="7" fill="#f59e0b"/>
  <line x1="230" y1="150" x2="230" y2="64" stroke="#15803d" stroke-width="3"/>
  <ellipse cx="220" cy="100" rx="10" ry="5" fill="#16a34a"/><ellipse cx="240" cy="118" rx="10" ry="5" fill="#16a34a"/><circle cx="230" cy="60" r="7" fill="#f59e0b"/>
  <line x1="370" y1="150" x2="370" y2="112" stroke="#15803d" stroke-width="3"/>
  <ellipse cx="360" cy="130" rx="9" ry="5" fill="#16a34a"/><circle cx="370" cy="108" r="7" fill="#f59e0b"/>
  <g text-anchor="middle">
    <text x="90" y="170" font-size="13" font-weight="700" fill="{_INK}">TT</text>
    <text x="230" y="170" font-size="13" font-weight="700" fill="{_INK}">Tt</text>
    <text x="370" y="170" font-size="13" font-weight="700" fill="{_INK}">tt</text>
    <text x="90" y="186" font-size="9" font-weight="700" fill="#15803d">Tall</text>
    <text x="230" y="186" font-size="9" font-weight="700" fill="#15803d">Tall</text>
    <text x="370" y="186" font-size="9" font-weight="700" fill="#b45309">Short</text>
    <text x="90" y="200" font-size="7.5" fill="#6b7280">homozygous dominant</text>
    <text x="230" y="200" font-size="7.5" fill="#6b7280">heterozygous</text>
    <text x="370" y="200" font-size="7.5" fill="#6b7280">homozygous recessive</text>
  </g>
  <text x="230" y="218" text-anchor="middle" font-size="8.5" fill="#6b7280">One dominant T makes the plant tall; only tt (two recessive alleles) is short.</text>
</svg>'''


# --- Genetics: worked Punnett square ---------------------------------------
_PUNNETT_SQUARE_WORKED = f'''
<svg viewBox="0 0 440 262" role="img" aria-label="A Tt by Tt Punnett square giving a three to one tall-to-short ratio" xmlns="http://www.w3.org/2000/svg" style="max-width:520px;width:100%;height:auto;{_FONT}">
  <text x="220" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Punnett Square: Tt &#215; Tt</text>
  <text x="150" y="58" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">T</text>
  <text x="210" y="58" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">t</text>
  <text x="96" y="104" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">T</text>
  <text x="96" y="164" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">t</text>
  <g stroke="{_INK}" stroke-width="1.5">
    <rect x="120" y="68" width="60" height="60" fill="#dcfce7"/>
    <rect x="180" y="68" width="60" height="60" fill="#dcfce7"/>
    <rect x="120" y="128" width="60" height="60" fill="#dcfce7"/>
    <rect x="180" y="128" width="60" height="60" fill="#fde68a"/>
  </g>
  <g font-size="15" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="150" y="104">TT</text><text x="210" y="104">Tt</text>
    <text x="150" y="164">Tt</text><text x="210" y="164">tt</text>
  </g>
  <text x="330" y="80" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Results</text>
  <text x="262" y="104" font-size="9.5" font-weight="700" fill="{_INK}">Genotype</text>
  <text x="262" y="118" font-size="9" fill="#6b7280">1 TT : 2 Tt : 1 tt</text>
  <text x="262" y="142" font-size="9.5" font-weight="700" fill="{_INK}">Phenotype</text>
  <text x="262" y="156" font-size="9" fill="#15803d">3 tall : 1 short</text>
  <rect x="262" y="168" width="108" height="16" fill="#dcfce7" stroke="{_INK}" stroke-width="0.6"/>
  <rect x="343" y="168" width="27" height="16" fill="#fde68a" stroke="{_INK}" stroke-width="0.6"/>
  <text x="306" y="180" text-anchor="middle" font-size="8" fill="#15803d">tall (3/4)</text>
  <text x="356" y="180" text-anchor="middle" font-size="7.5" fill="#b45309">short</text>
  <text x="220" y="222" text-anchor="middle" font-size="9" fill="#6b7280">Each of the 4 boxes is equally likely. Three show tall (TT, Tt, Tt) and one shows short (tt).</text>
  <text x="220" y="240" text-anchor="middle" font-size="9" fill="#6b7280">So P(short) = 1/4 = 25%, and P(tall) = 3/4 = 75%.</text>
</svg>'''


# --- Genetics: mitosis vs meiosis ------------------------------------------
_MITOSIS_VS_MEIOSIS = f'''
<svg viewBox="0 0 470 264" role="img" aria-label="Mitosis makes two identical cells; meiosis makes four cells with half the chromosomes" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Mitosis vs. Meiosis</text>
  <text x="40" y="60" font-size="11" font-weight="700" fill="#1e40af">Mitosis</text>
  <circle cx="70" cy="92" r="20" fill="#dbeafe" stroke="{_BLUE}"/>
  <g stroke="#1e40af" stroke-width="2.5"><line x1="63" y1="88" x2="63" y2="98"/><line x1="70" y1="86" x2="70" y2="100"/><line x1="77" y1="88" x2="77" y2="98"/></g>
  <line x1="94" y1="92" x2="150" y2="92" stroke="{_AXIS}" stroke-width="1.5"/><polygon points="156,92 144,86 144,98" fill="{_AXIS}"/>
  <text x="124" y="84" text-anchor="middle" font-size="8" fill="#6b7280">1 division</text>
  <circle cx="186" cy="70" r="16" fill="#dbeafe" stroke="{_BLUE}"/><g stroke="#1e40af" stroke-width="2"><line x1="181" y1="67" x2="181" y2="75"/><line x1="186" y1="65" x2="186" y2="77"/><line x1="191" y1="67" x2="191" y2="75"/></g>
  <circle cx="186" cy="116" r="16" fill="#dbeafe" stroke="{_BLUE}"/><g stroke="#1e40af" stroke-width="2"><line x1="181" y1="113" x2="181" y2="121"/><line x1="186" y1="111" x2="186" y2="123"/><line x1="191" y1="113" x2="191" y2="121"/></g>
  <text x="248" y="84" font-size="9" fill="{_INK}">2 identical cells</text>
  <text x="248" y="98" font-size="8" fill="#6b7280">same chromosome number</text>
  <text x="248" y="112" font-size="8" fill="#6b7280">for growth &amp; repair</text>
  <line x1="20" y1="142" x2="450" y2="142" stroke="{_GRID}"/>
  <text x="40" y="166" font-size="11" font-weight="700" fill="#b91c1c">Meiosis</text>
  <circle cx="70" cy="200" r="20" fill="#fee2e2" stroke="{_RED}"/>
  <g stroke="#b91c1c" stroke-width="2.5"><line x1="63" y1="196" x2="63" y2="206"/><line x1="70" y1="194" x2="70" y2="208"/><line x1="77" y1="196" x2="77" y2="206"/></g>
  <line x1="94" y1="200" x2="150" y2="200" stroke="{_AXIS}" stroke-width="1.5"/><polygon points="156,200 144,194 144,206" fill="{_AXIS}"/>
  <text x="124" y="192" text-anchor="middle" font-size="8" fill="#6b7280">2 divisions</text>
  <g fill="#fee2e2" stroke="{_RED}">
    <circle cx="184" cy="172" r="13"/><circle cx="184" cy="200" r="13"/><circle cx="184" cy="228" r="13"/><circle cx="216" cy="186" r="13"/>
  </g>
  <g stroke="#b91c1c" stroke-width="1.6"><line x1="184" y1="170" x2="184" y2="176"/><line x1="184" y1="198" x2="184" y2="204"/><line x1="184" y1="226" x2="184" y2="232"/><line x1="216" y1="184" x2="216" y2="190"/></g>
  <text x="262" y="186" font-size="9" fill="{_INK}">4 different cells</text>
  <text x="262" y="200" font-size="8" fill="#6b7280">HALF the chromosome number</text>
  <text x="262" y="214" font-size="8" fill="#6b7280">sex cells (egg &amp; sperm); variation</text>
  <text x="235" y="256" text-anchor="middle" font-size="8.5" fill="#6b7280">Mitosis copies a body cell; meiosis makes varied sex cells with half the chromosomes.</text>
</svg>'''


# --- Genetics: pedigree chart ----------------------------------------------
_PEDIGREE_CHART = f'''
<svg viewBox="0 0 460 232" role="img" aria-label="A family pedigree using squares for males, circles for females, and shading for an affected trait" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Reading a Pedigree</text>
  <rect x="150" y="50" width="28" height="28" fill="#ffffff" stroke="{_INK}" stroke-width="1.8"/>
  <circle cx="250" cy="64" r="15" fill="#ffffff" stroke="{_INK}" stroke-width="1.8"/>
  <line x1="178" y1="64" x2="235" y2="64" stroke="{_INK}" stroke-width="1.5"/>
  <text x="118" y="68" text-anchor="end" font-size="9" font-weight="700" fill="#6b7280">I</text>
  <line x1="206" y1="64" x2="206" y2="100" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="120" y1="100" x2="320" y2="100" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="120" y1="100" x2="120" y2="122" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="190" y1="100" x2="190" y2="122" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="250" y1="100" x2="250" y2="122" stroke="{_INK}" stroke-width="1.5"/>
  <line x1="320" y1="100" x2="320" y2="122" stroke="{_INK}" stroke-width="1.5"/>
  <circle cx="120" cy="138" r="15" fill="#ffffff" stroke="{_INK}" stroke-width="1.8"/>
  <rect x="176" y="124" width="28" height="28" fill="{_INK}" stroke="{_INK}" stroke-width="1.8"/>
  <circle cx="250" cy="138" r="15" fill="#ffffff" stroke="{_INK}" stroke-width="1.8"/>
  <rect x="306" y="124" width="28" height="28" fill="#ffffff" stroke="{_INK}" stroke-width="1.8"/>
  <text x="94" y="142" text-anchor="end" font-size="9" font-weight="700" fill="#6b7280">II</text>
  <text x="230" y="176" text-anchor="middle" font-size="8.5" fill="#6b7280">Two unaffected parents have an affected child &#8212; so the trait is most likely recessive.</text>
  <g font-size="9" fill="{_INK}">
    <rect x="58" y="198" width="16" height="16" fill="#ffffff" stroke="{_INK}" stroke-width="1.5"/><text x="80" y="210">male</text>
    <circle cx="134" cy="206" r="8" fill="#ffffff" stroke="{_INK}" stroke-width="1.5"/><text x="148" y="210">female</text>
    <rect x="214" y="198" width="16" height="16" fill="{_INK}"/><text x="236" y="210">shaded = has the trait</text>
  </g>
</svg>'''


# --- Evolution: variation within a population ------------------------------
_VARIATION_IN_POPULATION = f'''
<svg viewBox="0 0 460 196" role="img" aria-label="A population of beetles in many shades, showing inherited variation" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Variation: Individuals in a Population Differ</text>
  <g stroke="#1f2937" stroke-width="0.6">
    <ellipse cx="50" cy="70" rx="16" ry="11" fill="#e5e7eb"/><ellipse cx="110" cy="70" rx="16" ry="11" fill="#c7cdd4"/><ellipse cx="170" cy="70" rx="16" ry="11" fill="#9aa3ad"/><ellipse cx="230" cy="70" rx="16" ry="11" fill="#6b7280"/><ellipse cx="290" cy="70" rx="16" ry="11" fill="#4b5563"/><ellipse cx="350" cy="70" rx="16" ry="11" fill="#374151"/><ellipse cx="410" cy="70" rx="16" ry="11" fill="#1f2937"/>
    <ellipse cx="80" cy="118" rx="16" ry="11" fill="#d1d5db"/><ellipse cx="140" cy="118" rx="16" ry="11" fill="#aeb5bd"/><ellipse cx="200" cy="118" rx="16" ry="11" fill="#838b95"/><ellipse cx="260" cy="118" rx="16" ry="11" fill="#5b6573"/><ellipse cx="320" cy="118" rx="16" ry="11" fill="#42505e"/><ellipse cx="380" cy="118" rx="16" ry="11" fill="#2b3543"/>
  </g>
  <g stroke="#1f2937" stroke-width="0.6">
    <line x1="50" y1="59" x2="50" y2="81"/><line x1="110" y1="59" x2="110" y2="81"/><line x1="170" y1="59" x2="170" y2="81"/><line x1="230" y1="59" x2="230" y2="81"/><line x1="290" y1="59" x2="290" y2="81"/><line x1="350" y1="59" x2="350" y2="81"/><line x1="410" y1="59" x2="410" y2="81"/>
  </g>
  <text x="230" y="166" text-anchor="middle" font-size="9.5" fill="#6b7280">Some of this variation is inherited. Without differences, natural selection would have nothing to act on.</text>
</svg>'''


# --- Evolution: the four-step logic of natural selection -------------------
_NATURAL_SELECTION_CYCLE = f'''
<svg viewBox="0 0 470 262" role="img" aria-label="The four steps of natural selection: variation, inheritance, selection, and time" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Natural Selection: Four Steps</text>
  <g stroke-width="1.5">
    <rect x="150" y="38" width="170" height="44" rx="10" fill="#dbeafe" stroke="{_BLUE}"/>
    <rect x="318" y="108" width="144" height="44" rx="10" fill="#dcfce7" stroke="{_GREEN}"/>
    <rect x="150" y="178" width="170" height="44" rx="10" fill="#fef3c7" stroke="{_AMBER}"/>
    <rect x="8" y="108" width="144" height="44" rx="10" fill="#ede9fe" stroke="#7c3aed"/>
  </g>
  <g text-anchor="middle" fill="{_INK}">
    <text x="235" y="58" font-size="11" font-weight="700">1. Variation</text>
    <text x="235" y="73" font-size="8" fill="#6b7280">individuals differ</text>
    <text x="390" y="128" font-size="11" font-weight="700">2. Inheritance</text>
    <text x="390" y="143" font-size="8" fill="#6b7280">traits passed on</text>
    <text x="235" y="198" font-size="11" font-weight="700">3. Selection</text>
    <text x="235" y="213" font-size="8" fill="#6b7280">helpful traits survive &amp; reproduce more</text>
    <text x="80" y="128" font-size="11" font-weight="700">4. Time</text>
    <text x="80" y="143" font-size="8" fill="#6b7280">trait becomes common</text>
  </g>
  <g fill="none" stroke="{_AXIS}" stroke-width="1.8">
    <path d="M320,66 C372,74 392,90 398,106"/><polygon points="398,108 392,98 404,98" fill="{_AXIS}"/>
    <path d="M388,152 C380,182 330,194 322,196"/><polygon points="322,198 333,194 328,204" fill="{_AXIS}"/>
    <path d="M150,196 C98,194 80,178 76,154"/><polygon points="76,152 70,162 82,162" fill="{_AXIS}"/>
    <path d="M82,108 C90,90 132,74 150,66"/><polygon points="150,64 139,66 145,75" fill="{_AXIS}"/>
  </g>
  <text x="235" y="252" text-anchor="middle" font-size="8.5" fill="#6b7280">Remember V-I-S-T. The environment decides which inherited traits are 'helpful.'</text>
</svg>'''


# --- Evolution: antibiotic resistance (selection in action) ----------------
_ANTIBIOTIC_RESISTANCE = f'''
<svg viewBox="0 0 470 222" role="img" aria-label="Antibiotic resistance: an antibiotic kills non-resistant bacteria, and the resistant ones survive and multiply" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Evolution We Can Watch: Antibiotic Resistance</text>
  <g stroke="{_GRID}" stroke-width="1"><line x1="157" y1="36" x2="157" y2="176"/><line x1="313" y1="36" x2="313" y2="176"/></g>
  <text x="80" y="50" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">1. Before</text>
  <g fill="#60a5fa" stroke="#1e40af" stroke-width="0.6"><circle cx="50" cy="80" r="7"/><circle cx="78" cy="96" r="7"/><circle cx="108" cy="78" r="7"/><circle cx="62" cy="120" r="7"/><circle cx="100" cy="120" r="7"/><circle cx="120" cy="104" r="7"/></g>
  <g fill="#ef4444" stroke="#991b1b" stroke-width="0.6"><circle cx="86" cy="80" r="7"/></g>
  <text x="85" y="158" text-anchor="middle" font-size="8" fill="#6b7280">mostly normal; a few resistant (red)</text>
  <text x="235" y="50" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">2. Antibiotic</text>
  <g fill="#dbeafe" stroke="#9ca3af" stroke-width="0.8"><circle cx="205" cy="80" r="7"/><circle cx="233" cy="96" r="7"/><circle cx="263" cy="78" r="7"/><circle cx="217" cy="120" r="7"/><circle cx="255" cy="120" r="7"/><circle cx="275" cy="104" r="7"/></g>
  <g stroke="#b91c1c" stroke-width="1.4"><line x1="200" y1="75" x2="210" y2="85"/><line x1="210" y1="75" x2="200" y2="85"/><line x1="228" y1="91" x2="238" y2="101"/><line x1="238" y1="91" x2="228" y2="101"/><line x1="258" y1="73" x2="268" y2="83"/><line x1="268" y1="73" x2="258" y2="83"/></g>
  <g fill="#ef4444" stroke="#991b1b" stroke-width="0.6"><circle cx="241" cy="80" r="7"/></g>
  <text x="235" y="158" text-anchor="middle" font-size="8" fill="#6b7280">normal bacteria die; resistant survive</text>
  <text x="392" y="50" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">3. After</text>
  <g fill="#ef4444" stroke="#991b1b" stroke-width="0.6"><circle cx="360" cy="80" r="7"/><circle cx="388" cy="96" r="7"/><circle cx="418" cy="78" r="7"/><circle cx="372" cy="120" r="7"/><circle cx="410" cy="120" r="7"/><circle cx="430" cy="104" r="7"/></g>
  <text x="392" y="158" text-anchor="middle" font-size="8" fill="#6b7280">resistant ones multiply &#8594; resistant population</text>
  <text x="235" y="200" text-anchor="middle" font-size="8.5" fill="#6b7280">The antibiotic does not create resistance &#8212; it selects bacteria that were already resistant.</text>
</svg>'''


# --- Evolution: homologous structures --------------------------------------
_HOMOLOGOUS_STRUCTURES = f'''
<svg viewBox="0 0 470 222" role="img" aria-label="Homologous limb bones in a human arm, a whale flipper, and a bat wing share the same arrangement" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Homologous Structures: Same Bones, Different Jobs</text>
  <g stroke="#1f2937" stroke-width="0.6">
    <rect x="58" y="44" width="20" height="40" rx="6" fill="#3b82f6"/>
    <rect x="52" y="86" width="12" height="34" rx="5" fill="#22c55e"/><rect x="68" y="86" width="12" height="34" rx="5" fill="#22c55e"/>
    <g fill="#f59e0b"><rect x="48" y="122" width="6" height="30" rx="3"/><rect x="58" y="122" width="6" height="34" rx="3"/><rect x="68" y="122" width="6" height="32" rx="3"/><rect x="78" y="122" width="6" height="26" rx="3"/></g>
    <rect x="208" y="44" width="26" height="40" rx="8" fill="#3b82f6"/>
    <rect x="202" y="86" width="14" height="28" rx="5" fill="#22c55e"/><rect x="220" y="86" width="14" height="28" rx="5" fill="#22c55e"/>
    <g fill="#f59e0b"><rect x="198" y="116" width="9" height="46" rx="4"/><rect x="210" y="116" width="9" height="50" rx="4"/><rect x="222" y="116" width="9" height="46" rx="4"/><rect x="234" y="116" width="9" height="40" rx="4"/></g>
    <rect x="360" y="44" width="18" height="40" rx="6" fill="#3b82f6"/>
    <rect x="354" y="86" width="10" height="30" rx="4" fill="#22c55e"/><rect x="368" y="86" width="10" height="30" rx="4" fill="#22c55e"/>
    <g fill="#f59e0b"><rect x="346" y="118" width="5" height="58" rx="2.5"/><rect x="357" y="118" width="5" height="62" rx="2.5"/><rect x="368" y="118" width="5" height="60" rx="2.5"/><rect x="379" y="118" width="5" height="54" rx="2.5"/></g>
  </g>
  <g font-size="9.5" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="66" y="172">Human arm</text><text x="222" y="182">Whale flipper</text><text x="368" y="194">Bat wing</text>
  </g>
  <g font-size="8.5" text-anchor="start">
    <rect x="120" y="196" width="12" height="9" fill="#3b82f6"/><text x="136" y="204" fill="{_INK}">upper-arm bone</text>
    <rect x="232" y="196" width="12" height="9" fill="#22c55e"/><text x="248" y="204" fill="{_INK}">forearm bones</text>
    <rect x="332" y="196" width="12" height="9" fill="#f59e0b"/><text x="348" y="204" fill="{_INK}">finger bones</text>
  </g>
</svg>'''


# --- Evolution: a cladogram ------------------------------------------------
_CLADOGRAM = f'''
<svg viewBox="0 0 470 244" role="img" aria-label="A cladogram branching from a common ancestor, with shared traits marked at branch points" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Reading a Cladogram</text>
  <g stroke="{_INK}" stroke-width="2" fill="none">
    <path d="M30,200 L80,200"/>
    <path d="M80,200 L120,60"/>
    <path d="M80,200 L120,200"/>
    <path d="M120,160 L170,80"/><path d="M120,160 L170,160"/>
    <path d="M170,120 L220,100"/><path d="M170,120 L220,120"/>
  </g>
  <g stroke="{_INK}" stroke-width="2"><line x1="120" y1="60" x2="430" y2="60"/><line x1="170" y1="80" x2="430" y2="80"/><line x1="220" y1="100" x2="430" y2="100"/><line x1="220" y1="120" x2="430" y2="120"/><line x1="120" y1="200" x2="430" y2="200"/></g>
  <g font-size="10" font-weight="700" fill="{_INK}" text-anchor="start">
    <text x="436" y="64">Mouse</text><text x="436" y="84">Lizard</text><text x="436" y="104">Frog</text><text x="436" y="124">Salamander</text><text x="436" y="204">Fish</text>
  </g>
  <g fill="{_GREEN}"><circle cx="80" cy="200" r="5"/><circle cx="120" cy="160" r="5"/><circle cx="170" cy="120" r="5"/></g>
  <g font-size="7.5" fill="#15803d" text-anchor="middle">
    <text x="80" y="216">backbone</text><text x="120" y="176">legs</text><text x="170" y="136">amniotic egg</text>
  </g>
  <text x="235" y="236" text-anchor="middle" font-size="8.5" fill="#6b7280">Each dot is a shared trait at a common ancestor. Closer branch points mean more closely related.</text>
</svg>'''


# --- Evolution: speciation by isolation ------------------------------------
_SPECIATION = f'''
<svg viewBox="0 0 470 224" role="img" aria-label="Speciation: a barrier splits a population, and the two groups change until they become separate species" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How New Species Can Form (Speciation)</text>
  <g stroke="{_GRID}" stroke-width="1"><line x1="157" y1="36" x2="157" y2="170"/><line x1="313" y1="36" x2="313" y2="170"/></g>
  <text x="80" y="50" text-anchor="middle" font-size="9.5" font-weight="700" fill="{_INK}">1. One population</text>
  <g fill="#16a34a" stroke="#15803d" stroke-width="0.6"><circle cx="55" cy="90" r="7"/><circle cx="80" cy="104" r="7"/><circle cx="105" cy="88" r="7"/><circle cx="68" cy="124" r="7"/><circle cx="95" cy="120" r="7"/></g>
  <text x="235" y="50" text-anchor="middle" font-size="9.5" font-weight="700" fill="{_INK}">2. A barrier splits it</text>
  <g fill="#16a34a" stroke="#15803d" stroke-width="0.6"><circle cx="190" cy="96" r="7"/><circle cx="212" cy="120" r="7"/><circle cx="270" cy="92" r="7"/><circle cx="288" cy="118" r="7"/></g>
  <path d="M240,70 q-8,30 0,60 q8,30 0,40" fill="none" stroke="#60a5fa" stroke-width="6"/>
  <text x="240" y="160" text-anchor="middle" font-size="7.5" fill="#0369a1">river / mountain</text>
  <text x="392" y="50" text-anchor="middle" font-size="9.5" font-weight="700" fill="{_INK}">3. Two species</text>
  <g fill="#16a34a" stroke="#15803d" stroke-width="0.6"><circle cx="345" cy="92" r="7"/><circle cx="367" cy="116" r="6"/></g>
  <g fill="#7c3aed" stroke="#5b21b6" stroke-width="0.6"><circle cx="415" cy="92" r="8"/><circle cx="435" cy="116" r="8"/></g>
  <text x="392" y="158" text-anchor="middle" font-size="8" fill="#6b7280">each adapts differently</text>
  <text x="235" y="202" text-anchor="middle" font-size="8.5" fill="#6b7280">Separation reduces gene flow; over many generations different environments select different traits.</text>
</svg>'''


# --- Ecosystems: levels of organization ------------------------------------
_ECOSYSTEM_LEVELS = f'''
<svg viewBox="0 0 470 196" role="img" aria-label="Levels of ecological organization from organism to biosphere" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Levels of Organization</text>
  <g stroke="{_AXIS}" stroke-width="1.6" fill="{_AXIS}">
    <line x1="86" y1="90" x2="104" y2="90"/><polygon points="108,90 100,86 100,94"/>
    <line x1="180" y1="90" x2="198" y2="90"/><polygon points="202,90 194,86 194,94"/>
    <line x1="274" y1="90" x2="292" y2="90"/><polygon points="296,90 288,86 288,94"/>
    <line x1="368" y1="90" x2="386" y2="90"/><polygon points="390,90 382,86 382,94"/>
  </g>
  <circle cx="50" cy="90" r="26" fill="#f0fdf4" stroke="#15803d"/><circle cx="50" cy="90" r="6" fill="#16a34a"/>
  <circle cx="144" cy="90" r="26" fill="#f0fdf4" stroke="#15803d"/><g fill="#16a34a"><circle cx="136" cy="84" r="5"/><circle cx="152" cy="86" r="5"/><circle cx="144" cy="98" r="5"/></g>
  <circle cx="238" cy="90" r="26" fill="#f0fdf4" stroke="#15803d"/><g fill="#16a34a"><circle cx="230" cy="84" r="5"/><circle cx="244" cy="88" r="5"/></g><g fill="#b45309"><circle cx="236" cy="98" r="5"/><circle cx="248" cy="98" r="4"/></g>
  <circle cx="332" cy="90" r="26" fill="#eaf6ff" stroke="{_BLUE}"/><circle cx="324" cy="82" r="5" fill="#16a34a"/><circle cx="338" cy="84" r="4" fill="#b45309"/><circle cx="322" cy="98" r="6" fill="#7dd3fc"/><circle cx="344" cy="98" r="4" fill="#facc15"/>
  <circle cx="426" cy="90" r="26" fill="#7dd3fc" stroke="{_BLUE}"/><path d="M410,90 q8,-10 18,-2 q10,6 16,-2" fill="none" stroke="#16a34a" stroke-width="4"/>
  <g font-size="9" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="50" y="138">Organism</text><text x="144" y="138">Population</text><text x="238" y="138">Community</text><text x="332" y="138">Ecosystem</text><text x="426" y="138">Biosphere</text>
  </g>
  <g font-size="7.5" fill="#6b7280" text-anchor="middle">
    <text x="50" y="150">one individual</text><text x="144" y="150">same species</text><text x="238" y="150">all species</text><text x="332" y="150">+ nonliving</text><text x="426" y="150">all of Earth</text>
  </g>
  <text x="235" y="178" text-anchor="middle" font-size="8.5" fill="#6b7280">An ecosystem is a community of living things plus the nonliving things (sun, water, soil) they interact with.</text>
</svg>'''


# --- Ecosystems: a food web ------------------------------------------------
_FOOD_WEB = f'''
<svg viewBox="0 0 470 282" role="img" aria-label="A food web with several linked feeding paths; arrows point from food to the eater" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">A Food Web (arrows = energy flow)</text>
  <g stroke="#9ca3af" stroke-width="1.6" fill="#9ca3af">
    <line x1="70" y1="230" x2="150" y2="216"/><polygon points="156,215 145,213 148,222"/>
    <line x1="84" y1="226" x2="276" y2="234"/><polygon points="282,234 271,230 272,239"/>
    <line x1="184" y1="197" x2="188" y2="156"/><polygon points="189,150 183,160 194,159"/>
    <line x1="208" y1="206" x2="298" y2="164"/><polygon points="304,161 293,162 298,171"/>
    <line x1="300" y1="222" x2="246" y2="94"/><polygon points="244,88 242,99 252,95"/>
    <line x1="318" y1="223" x2="372" y2="86"/><polygon points="374,80 366,89 376,91"/>
    <line x1="198" y1="126" x2="220" y2="94"/><polygon points="224,89 213,93 221,101"/>
    <line x1="334" y1="138" x2="372" y2="86"/><polygon points="376,82 366,87 374,93"/>
    <line x1="260" y1="74" x2="356" y2="70"/><polygon points="362,70 351,66 352,75"/>
  </g>
  <g font-size="9" text-anchor="middle">
    <ellipse cx="56" cy="230" rx="30" ry="15" fill="#dcfce7" stroke="{_GREEN}"/><text x="56" y="233" fill="{_INK}">Grass</text>
    <ellipse cx="180" cy="212" rx="36" ry="15" fill="#fef9c3" stroke="#ca8a04"/><text x="180" y="215" fill="{_INK}">Grasshopper</text>
    <ellipse cx="304" cy="236" rx="28" ry="15" fill="#fef9c3" stroke="#ca8a04"/><text x="304" y="239" fill="{_INK}">Mouse</text>
    <ellipse cx="184" cy="138" rx="26" ry="15" fill="#ffedd5" stroke="#ea580c"/><text x="184" y="141" fill="{_INK}">Frog</text>
    <ellipse cx="322" cy="150" rx="30" ry="15" fill="#ffedd5" stroke="#ea580c"/><text x="322" y="153" fill="{_INK}">Sparrow</text>
    <ellipse cx="232" cy="78" rx="28" ry="15" fill="#fee2e2" stroke="{_RED}"/><text x="232" y="81" fill="{_INK}">Snake</text>
    <ellipse cx="384" cy="70" rx="28" ry="15" fill="#fee2e2" stroke="{_RED}"/><text x="384" y="73" fill="{_INK}">Hawk</text>
  </g>
  <text x="235" y="270" text-anchor="middle" font-size="8.5" fill="#6b7280">Most organisms have several food sources, so chains link into a web. Decomposers recycle them all.</text>
</svg>'''


# --- Ecosystems: energy pyramid (10% rule) ---------------------------------
_ENERGY_PYRAMID_DETAILED = f'''
<svg viewBox="0 0 460 268" role="img" aria-label="An energy pyramid showing about 10 percent of energy passing to each higher level" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="230" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Energy Pyramid: the 10% Rule</text>
  <polygon points="40,210 300,210 268,166 72,166" fill="{_GREEN}"/>
  <polygon points="72,166 268,166 236,122 104,122" fill="#65a30d"/>
  <polygon points="104,122 236,122 204,78 136,78" fill="#ea580c"/>
  <polygon points="136,78 204,78 184,40 156,40" fill="{_RED}"/>
  <g fill="#ffffff" text-anchor="middle" font-weight="700">
    <text x="170" y="194" font-size="11">Producers &#8212; 10,000 kcal</text>
    <text x="170" y="150" font-size="10.5">1&#176; consumers &#8212; 1,000 kcal</text>
    <text x="170" y="106" font-size="10">2&#176; consumers &#8212; 100 kcal</text>
    <text x="170" y="62" font-size="9">3&#176; &#8212; 10 kcal</text>
  </g>
  <g stroke="#b45309" stroke-width="1.4" fill="#b45309">
    <line x1="308" y1="188" x2="332" y2="188"/><polygon points="338,188 328,184 328,192"/>
    <line x1="276" y1="144" x2="332" y2="144"/><polygon points="338,144 328,140 328,148"/>
    <line x1="244" y1="100" x2="332" y2="100"/><polygon points="338,100 328,96 328,104"/>
  </g>
  <text x="392" y="148" text-anchor="middle" font-size="8.5" fill="#b45309" transform="rotate(90 392 148)">~90% lost as heat each step</text>
  <text x="230" y="240" text-anchor="middle" font-size="9" fill="#6b7280">Only about 10% of the energy at one level passes up, so higher levels support far fewer organisms.</text>
  <text x="230" y="256" text-anchor="middle" font-size="8.5" fill="#6b7280">Decomposers feed at every level, returning nutrients to the ecosystem.</text>
</svg>'''


# --- Ecosystems: the carbon cycle ------------------------------------------
_CARBON_CYCLE = f'''
<svg viewBox="0 0 470 262" role="img" aria-label="The carbon cycle: photosynthesis removes carbon dioxide; respiration, decomposition, and burning fuels release it" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Carbon Cycle</text>
  <rect x="150" y="36" width="170" height="34" rx="10" fill="#e0f2fe" stroke="{_BLUE}"/>
  <text x="235" y="58" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">CO&#8322; in the atmosphere</text>
  <line x1="80" y1="206" x2="80" y2="150" stroke="#15803d" stroke-width="3"/><ellipse cx="70" cy="172" rx="10" ry="5" fill="#16a34a"/><ellipse cx="90" cy="160" rx="10" ry="5" fill="#16a34a"/>
  <text x="80" y="222" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Plants</text>
  <ellipse cx="240" cy="182" rx="26" ry="16" fill="#fde68a" stroke="#ca8a04"/><text x="240" y="186" text-anchor="middle" font-size="9" fill="{_INK}">Animals</text>
  <rect x="350" y="170" width="96" height="30" rx="8" fill="#e5e7eb" stroke="#6b7280"/><text x="398" y="183" text-anchor="middle" font-size="8.5" fill="{_INK}">decomposers &amp;</text><text x="398" y="194" text-anchor="middle" font-size="8.5" fill="{_INK}">burning fuels</text>
  <g stroke="{_GREEN}" stroke-width="2" fill="{_GREEN}"><line x1="182" y1="72" x2="94" y2="148"/><polygon points="90,151 93,139 101,147"/></g>
  <text x="116" y="108" font-size="8" fill="#15803d">photosynthesis</text>
  <g stroke="{_RED}" stroke-width="2" fill="{_RED}">
    <line x1="248" y1="166" x2="252" y2="74"/><polygon points="252,70 247,82 257,80"/>
    <line x1="398" y1="168" x2="302" y2="74"/><polygon points="300,70 302,82 309,75"/>
    <line x1="102" y1="172" x2="214" y2="182"/><polygon points="220,183 209,178 209,187"/>
  </g>
  <text x="272" y="120" font-size="8" fill="#b91c1c">respiration</text>
  <text x="332" y="116" font-size="8" fill="#b91c1c">release CO&#8322;</text>
  <text x="150" y="166" font-size="8" fill="#6b7280">eaten</text>
  <text x="235" y="240" text-anchor="middle" font-size="9" fill="#6b7280">Photosynthesis pulls carbon out of the air; respiration, decomposition, and burning fuels put it back.</text>
</svg>'''


# --- Ecosystems: carrying capacity -----------------------------------------
_CARRYING_CAPACITY_GRAPH = f'''
<svg viewBox="0 0 380 236" role="img" aria-label="A population graph rising and leveling off at the carrying capacity" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="190" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Population Growth &amp; Carrying Capacity</text>
  <line x1="50" y1="34" x2="50" y2="196" stroke="{_AXIS}"/>
  <line x1="50" y1="196" x2="350" y2="196" stroke="{_AXIS}"/>
  <text x="22" y="115" font-size="10" fill="#6b7280" transform="rotate(-90 22 115)" text-anchor="middle">Population size</text>
  <text x="200" y="222" font-size="10" fill="#6b7280" text-anchor="middle">Time</text>
  <line x1="50" y1="64" x2="350" y2="64" stroke="{_RED}" stroke-width="1.4" stroke-dasharray="5 4"/>
  <text x="346" y="58" text-anchor="end" font-size="9" font-weight="700" fill="{_RED}">carrying capacity (K)</text>
  <path d="M50,188 C120,184 150,150 175,110 C200,72 250,66 350,66" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <text x="118" y="150" font-size="8.5" fill="#1e40af">rapid growth</text>
  <text x="268" y="84" font-size="8.5" fill="#1e40af">levels off at the limit</text>
</svg>'''


# --- Ecosystems: types of symbiosis ----------------------------------------
_SYMBIOSIS_TYPES = f'''
<svg viewBox="0 0 470 196" role="img" aria-label="Three types of symbiosis: mutualism (both benefit), commensalism (one benefits), and parasitism (one harmed)" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Three Kinds of Symbiosis</text>
  <g stroke="{_GRID}" stroke-width="1"><line x1="157" y1="36" x2="157" y2="156"/><line x1="313" y1="36" x2="313" y2="156"/></g>
  <text x="80" y="52" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Mutualism</text>
  <circle cx="55" cy="92" r="16" fill="#fde68a" stroke="#ca8a04"/><circle cx="105" cy="92" r="16" fill="#dcfce7" stroke="{_GREEN}"/>
  <text x="55" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">+</text><text x="105" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">+</text>
  <text x="80" y="140" text-anchor="middle" font-size="8" fill="#6b7280">both benefit (bee &amp; flower)</text>
  <text x="235" y="52" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Commensalism</text>
  <circle cx="210" cy="92" r="16" fill="#fde68a" stroke="#ca8a04"/><circle cx="260" cy="92" r="16" fill="#e5e7eb" stroke="#6b7280"/>
  <text x="210" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">+</text><text x="260" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#6b7280">0</text>
  <text x="235" y="140" text-anchor="middle" font-size="8" fill="#6b7280">one benefits, other unaffected</text>
  <text x="392" y="52" text-anchor="middle" font-size="11" font-weight="700" fill="#b91c1c">Parasitism</text>
  <circle cx="367" cy="92" r="16" fill="#fde68a" stroke="#ca8a04"/><circle cx="417" cy="92" r="16" fill="#fee2e2" stroke="{_RED}"/>
  <text x="367" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#15803d">+</text><text x="417" y="120" text-anchor="middle" font-size="13" font-weight="700" fill="#b91c1c">&#8722;</text>
  <text x="392" y="140" text-anchor="middle" font-size="8" fill="#6b7280">one benefits, other harmed (tick &amp; dog)</text>
  <text x="235" y="174" text-anchor="middle" font-size="8.5" fill="#6b7280">Read the signs: + benefits, 0 unaffected, &#8722; harmed.</text>
</svg>'''


# --- Ecosystems: predator-prey populations ---------------------------------
_PREDATOR_PREY_GRAPH = f'''
<svg viewBox="0 0 380 236" role="img" aria-label="A predator-prey graph: prey and predator populations rise and fall, with the predator lagging the prey" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="190" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Predator and Prey Populations</text>
  <line x1="50" y1="34" x2="50" y2="190" stroke="{_AXIS}"/>
  <line x1="50" y1="190" x2="350" y2="190" stroke="{_AXIS}"/>
  <text x="22" y="112" font-size="10" fill="#6b7280" transform="rotate(-90 22 112)" text-anchor="middle">Population</text>
  <text x="200" y="216" font-size="10" fill="#6b7280" text-anchor="middle">Time</text>
  <path d="M50,150 C90,70 130,70 170,150 C210,70 250,70 290,150 C310,110 330,110 350,150" fill="none" stroke="{_GREEN}" stroke-width="2.2"/>
  <path d="M50,170 C100,150 130,110 180,120 C220,128 250,110 300,120 C320,124 335,140 350,150" fill="none" stroke="{_RED}" stroke-width="2.2"/>
  <g font-size="9"><line x1="238" y1="58" x2="262" y2="58" stroke="{_GREEN}" stroke-width="2.2"/><text x="266" y="61" fill="{_INK}">prey</text>
  <line x1="238" y1="74" x2="262" y2="74" stroke="{_RED}" stroke-width="2.2"/><text x="266" y="77" fill="{_INK}">predator</text></g>
  <text x="190" y="230" font-size="8.5" fill="#6b7280" text-anchor="middle">When prey rise, predators rise soon after; then prey fall, and predators follow.</text>
</svg>'''


# --- Number sense: signed number line --------------------------------------
_INTEGER_NUMBER_LINE = f'''
<svg viewBox="0 0 500 170" role="img" aria-label="Integer number line from negative 6 to positive 6 showing opposites and absolute value as distance" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="250" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Integers, Opposites, and Absolute Value</text>
  <line x1="40" y1="88" x2="460" y2="88" stroke="{_AXIS}" stroke-width="2"/>
  <g stroke="{_AXIS}" font-size="10" fill="{_INK}" text-anchor="middle">
    <line x1="40" y1="80" x2="40" y2="96"/><text x="40" y="116">-6</text>
    <line x1="75" y1="82" x2="75" y2="94"/><text x="75" y="116">-5</text>
    <line x1="110" y1="80" x2="110" y2="96"/><text x="110" y="116">-4</text>
    <line x1="145" y1="82" x2="145" y2="94"/><text x="145" y="116">-3</text>
    <line x1="180" y1="80" x2="180" y2="96"/><text x="180" y="116">-2</text>
    <line x1="215" y1="82" x2="215" y2="94"/><text x="215" y="116">-1</text>
    <line x1="250" y1="76" x2="250" y2="100"/><text x="250" y="118" font-weight="700">0</text>
    <line x1="285" y1="82" x2="285" y2="94"/><text x="285" y="116">1</text>
    <line x1="320" y1="80" x2="320" y2="96"/><text x="320" y="116">2</text>
    <line x1="355" y1="82" x2="355" y2="94"/><text x="355" y="116">3</text>
    <line x1="390" y1="80" x2="390" y2="96"/><text x="390" y="116">4</text>
    <line x1="425" y1="82" x2="425" y2="94"/><text x="425" y="116">5</text>
    <line x1="460" y1="80" x2="460" y2="96"/><text x="460" y="116">6</text>
  </g>
  <circle cx="145" cy="88" r="7" fill="{_BLUE}"/><circle cx="355" cy="88" r="7" fill="{_RED}"/>
  <path d="M145,64 C185,38 315,38 355,64" fill="none" stroke="#7c3aed" stroke-width="2"/>
  <path d="M145,65 l8,-3 l-3,-8" fill="none" stroke="#7c3aed" stroke-width="2"/>
  <path d="M355,65 l-8,-3 l3,-8" fill="none" stroke="#7c3aed" stroke-width="2"/>
  <text x="250" y="48" text-anchor="middle" font-size="11" fill="#7c3aed" font-weight="700">-3 and 3 are opposites</text>
  <text x="250" y="147" text-anchor="middle" font-size="10.5" fill="#6b7280">Absolute value is distance from zero: |-3| = 3 and |3| = 3.</text>
</svg>'''


# --- Number sense: signed operation rules ----------------------------------
_SIGNED_OPERATION_RULES = f'''
<svg viewBox="0 0 500 220" role="img" aria-label="Rules for signed-number operations" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="250" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Signed-Number Operations</text>
  <rect x="34" y="45" width="198" height="130" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>
  <rect x="268" y="45" width="198" height="130" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
  <text x="133" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="{_BLUE}">Adding/Subtracting</text>
  <text x="367" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">Multiplying/Dividing</text>
  <g font-size="11" fill="{_INK}">
    <text x="54" y="96">Same signs: add sizes, keep sign</text>
    <text x="54" y="122">Different signs: subtract sizes</text>
    <text x="54" y="148">Subtracting means add the opposite</text>
    <text x="288" y="96">Same signs -> positive</text>
    <text x="288" y="122">Different signs -> negative</text>
    <text x="288" y="148">Zero divided by nonzero = 0</text>
  </g>
  <g font-size="11" fill="#6b7280">
    <text x="54" y="192">Example: -9 + 4 = -5</text>
    <text x="288" y="192">Example: (-6)(-3) = 18</text>
  </g>
</svg>'''


# --- Number sense: absolute-value distance model ---------------------------
_ABSOLUTE_VALUE_DISTANCE_MODEL = f'''
<svg viewBox="0 0 520 190" role="img" aria-label="Absolute value as distance between two points on a number line" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;{_FONT}">
  <text x="260" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Absolute Value Measures Distance</text>
  <line x1="54" y1="98" x2="466" y2="98" stroke="{_AXIS}" stroke-width="2"/>
  <g stroke="{_AXIS}" font-size="10" fill="{_INK}" text-anchor="middle">
    <line x1="54" y1="89" x2="54" y2="107"/><text x="54" y="128">-6</text>
    <line x1="123" y1="91" x2="123" y2="105"/><text x="123" y="128">-4</text>
    <line x1="192" y1="91" x2="192" y2="105"/><text x="192" y="128">-2</text>
    <line x1="260" y1="86" x2="260" y2="110"/><text x="260" y="130" font-weight="700">0</text>
    <line x1="329" y1="91" x2="329" y2="105"/><text x="329" y="128">2</text>
    <line x1="398" y1="91" x2="398" y2="105"/><text x="398" y="128">4</text>
    <line x1="466" y1="89" x2="466" y2="107"/><text x="466" y="128">6</text>
  </g>
  <circle cx="123" cy="98" r="7" fill="{_BLUE}"/><circle cx="363" cy="98" r="7" fill="{_RED}"/>
  <path d="M123,70 C180,40 306,40 363,70" fill="none" stroke="#7c3aed" stroke-width="2.2"/>
  <path d="M123,70 l8,-3 l-4,-8" fill="none" stroke="#7c3aed" stroke-width="2.2"/>
  <path d="M363,70 l-8,-3 l4,-8" fill="none" stroke="#7c3aed" stroke-width="2.2"/>
  <text x="243" y="54" text-anchor="middle" font-size="11" font-weight="700" fill="#7c3aed">distance from -4 to 3 is 7</text>
  <text x="260" y="160" text-anchor="middle" font-size="10.5" fill="#6b7280">Use |a - b| for distance: |3 - (-4)| = |7| = 7.</text>
</svg>'''


# --- Operations: order of operations stack ---------------------------------
_ORDER_OPERATIONS_STACK = f'''
<svg viewBox="0 0 520 245" role="img" aria-label="Order of operations stack showing grouping, exponents, multiply/divide, add/subtract" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;{_FONT}">
  <text x="260" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Order Comes from Structure</text>
  <g font-size="11" font-weight="700" text-anchor="middle">
    <rect x="155" y="45" width="210" height="35" rx="8" fill="#dbeafe" stroke="#93c5fd"/>
    <text x="260" y="67" fill="{_BLUE}">1. Grouping symbols</text>
    <rect x="155" y="88" width="210" height="35" rx="8" fill="#fef3c7" stroke="#fbbf24"/>
    <text x="260" y="110" fill="#92400e">2. Exponents and roots</text>
    <rect x="155" y="131" width="210" height="35" rx="8" fill="#dcfce7" stroke="#86efac"/>
    <text x="260" y="153" fill="#166534">3. Multiply or divide left to right</text>
    <rect x="155" y="174" width="210" height="35" rx="8" fill="#fee2e2" stroke="#fca5a5"/>
    <text x="260" y="196" fill="#991b1b">4. Add or subtract left to right</text>
  </g>
  <text x="260" y="228" text-anchor="middle" font-size="10.5" fill="#6b7280">Example: 6 + 2(5)^2 means square 5, multiply by 2, then add 6.</text>
</svg>'''


# --- Formula skills: substitution workflow ---------------------------------
_FORMULA_SUBSTITUTION_FLOW = f'''
<svg viewBox="0 0 560 210" role="img" aria-label="Formula substitution workflow from identify variables to substitute, simplify, and attach units" xmlns="http://www.w3.org/2000/svg" style="max-width:680px;width:100%;height:auto;{_FONT}">
  <text x="280" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Formula Skill: Name, Substitute, Simplify</text>
  <g font-size="10.5" text-anchor="middle" font-weight="700">
    <rect x="28" y="58" width="114" height="62" rx="8" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="85" y="83" fill="{_BLUE}">1. Choose</text><text x="85" y="100" fill="{_BLUE}">the formula</text>
    <rect x="162" y="58" width="114" height="62" rx="8" fill="#f8fafc" stroke="#cbd5e1"/>
    <text x="219" y="83" fill="{_INK}">2. Label</text><text x="219" y="100" fill="{_INK}">given values</text>
    <rect x="296" y="58" width="114" height="62" rx="8" fill="#fef3c7" stroke="#fbbf24"/>
    <text x="353" y="83" fill="#92400e">3. Substitute</text><text x="353" y="100" fill="#92400e">with parentheses</text>
    <rect x="430" y="58" width="104" height="62" rx="8" fill="#dcfce7" stroke="#86efac"/>
    <text x="482" y="83" fill="#166534">4. Simplify</text><text x="482" y="100" fill="#166534">and units</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="1.6" fill="none">
    <path d="M142,89 H160"/><path d="M276,89 H294"/><path d="M410,89 H428"/>
  </g>
  <g font-size="12" fill="{_INK}" text-anchor="middle">
    <text x="280" y="155">A = lw, l = 8, w = 5</text>
    <text x="280" y="178" font-weight="700">A = (8)(5) = 40 square units</text>
  </g>
</svg>'''


# --- Number sense: GCF and LCM from factors --------------------------------
_GCF_LCM_FACTOR_MAP = f'''
<svg viewBox="0 0 520 250" role="img" aria-label="Prime-factor map showing the GCF and LCM of 18 and 30" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;{_FONT}">
  <text x="260" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">GCF and LCM from Prime Factors</text>
  <text x="145" y="55" text-anchor="middle" font-size="12" font-weight="700" fill="{_BLUE}">18 = 2 x 3 x 3</text>
  <text x="375" y="55" text-anchor="middle" font-size="12" font-weight="700" fill="{_GREEN}">30 = 2 x 3 x 5</text>
  <circle cx="210" cy="135" r="80" fill="#dbeafe" opacity="0.72" stroke="#93c5fd"/>
  <circle cx="310" cy="135" r="80" fill="#dcfce7" opacity="0.72" stroke="#86efac"/>
  <g font-size="18" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="175" y="132">3</text>
    <text x="260" y="122">2</text>
    <text x="260" y="152">3</text>
    <text x="345" y="132">5</text>
  </g>
  <rect x="184" y="192" width="152" height="32" rx="6" fill="#ffffff" stroke="{_AXIS}"/>
  <text x="260" y="213" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">GCF = 2 x 3 = 6</text>
  <text x="260" y="238" text-anchor="middle" font-size="10.5" fill="#6b7280">LCM uses all needed factors: 2 x 3 x 3 x 5 = 90.</text>
</svg>'''


# --- Number sense: scientific notation ladder ------------------------------
_SCIENTIFIC_NOTATION_LADDER = f'''
<svg viewBox="0 0 520 230" role="img" aria-label="Scientific notation ladder showing powers of ten and decimal movement" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;{_FONT}">
  <text x="260" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Scientific Notation and Powers of 10</text>
  <line x1="70" y1="112" x2="450" y2="112" stroke="{_AXIS}" stroke-width="2"/>
  <g stroke="{_AXIS}" fill="{_INK}" font-size="10" text-anchor="middle">
    <line x1="70" y1="100" x2="70" y2="124"/><text x="70" y="146">10^-3</text>
    <line x1="146" y1="100" x2="146" y2="124"/><text x="146" y="146">10^-2</text>
    <line x1="222" y1="100" x2="222" y2="124"/><text x="222" y="146">10^-1</text>
    <line x1="298" y1="96" x2="298" y2="128"/><text x="298" y="148" font-weight="700">10^0</text>
    <line x1="374" y1="100" x2="374" y2="124"/><text x="374" y="146">10^1</text>
    <line x1="450" y1="100" x2="450" y2="124"/><text x="450" y="146">10^2</text>
  </g>
  <path d="M210,70 C240,48 356,48 386,70" fill="none" stroke="{_BLUE}" stroke-width="2"/>
  <path d="M386,70 l-9,-2 l4,-8" fill="none" stroke="{_BLUE}" stroke-width="2"/>
  <text x="298" y="62" text-anchor="middle" font-size="11" font-weight="700" fill="{_BLUE}">multiply by 10, decimal moves right</text>
  <path d="M386,172 C356,194 240,194 210,172" fill="none" stroke="{_RED}" stroke-width="2"/>
  <path d="M210,172 l9,2 l-4,8" fill="none" stroke="{_RED}" stroke-width="2"/>
  <text x="298" y="203" text-anchor="middle" font-size="11" font-weight="700" fill="{_RED}">divide by 10, decimal moves left</text>
  <text x="260" y="92" text-anchor="middle" font-size="11" fill="#6b7280">Example: 5.2 x 10^4 = 52,000</text>
</svg>'''


# --- Measurement: unit conversion bridge -----------------------------------
_UNIT_CONVERSION_BRIDGE = f'''
<svg viewBox="0 0 540 240" role="img" aria-label="Dimensional-analysis bridge for converting units" xmlns="http://www.w3.org/2000/svg" style="max-width:660px;width:100%;height:auto;{_FONT}">
  <text x="270" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Unit Conversion Bridge</text>
  <rect x="35" y="62" width="120" height="60" rx="8" fill="#eff6ff" stroke="#bfdbfe"/>
  <rect x="210" y="62" width="120" height="60" rx="8" fill="#ffffff" stroke="{_AXIS}"/>
  <rect x="385" y="62" width="120" height="60" rx="8" fill="#dcfce7" stroke="#86efac"/>
  <text x="95" y="97" text-anchor="middle" font-size="13" font-weight="700" fill="{_BLUE}">3.5 ft</text>
  <text x="270" y="86" text-anchor="middle" font-size="12" fill="{_INK}">12 in</text>
  <line x1="230" y1="94" x2="310" y2="94" stroke="{_AXIS}"/>
  <text x="270" y="112" text-anchor="middle" font-size="12" fill="{_INK}">1 ft</text>
  <text x="445" y="97" text-anchor="middle" font-size="13" font-weight="700" fill="{_GREEN}">42 in</text>
  <g stroke="{_AXIS}" stroke-width="2" fill="none">
    <path d="M155,92 H210"/>
    <path d="M330,92 H385"/>
  </g>
  <text x="270" y="154" text-anchor="middle" font-size="11" fill="#6b7280">Use a conversion factor that cancels the starting unit.</text>
  <text x="270" y="182" text-anchor="middle" font-size="12" fill="{_INK}">3.5 ft x (12 in / 1 ft) = 42 in</text>
  <text x="270" y="212" text-anchor="middle" font-size="10.5" fill="#6b7280">The number changes, but the measured length stays the same.</text>
</svg>'''


# --- Human body: levels of organization ------------------------------------
_BODY_ORGANIZATION = f'''
<svg viewBox="0 0 470 196" role="img" aria-label="Levels of body organization from cell to tissue to organ to organ system to organism" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">From Cells to Body Systems</text>
  <g stroke="{_AXIS}" stroke-width="1.6" fill="{_AXIS}">
    <line x1="86" y1="86" x2="104" y2="86"/><polygon points="108,86 100,82 100,90"/>
    <line x1="180" y1="86" x2="198" y2="86"/><polygon points="202,86 194,82 194,90"/>
    <line x1="274" y1="86" x2="292" y2="86"/><polygon points="296,86 288,82 288,90"/>
    <line x1="368" y1="86" x2="386" y2="86"/><polygon points="390,86 382,82 382,90"/>
  </g>
  <circle cx="50" cy="86" r="26" fill="#fee2e2" stroke="{_RED}"/><circle cx="50" cy="86" r="8" fill="#fca5a5"/><circle cx="52" cy="88" r="3" fill="#b91c1c"/>
  <circle cx="144" cy="86" r="26" fill="#fee2e2" stroke="{_RED}"/><g fill="#fca5a5" stroke="#b91c1c" stroke-width="0.5"><circle cx="136" cy="80" r="6"/><circle cx="150" cy="82" r="6"/><circle cx="140" cy="94" r="6"/><circle cx="153" cy="93" r="6"/></g>
  <circle cx="238" cy="86" r="26" fill="#ffffff" stroke="{_RED}"/><path d="M238,98 C224,84 228,72 238,80 C248,72 252,84 238,98 Z" fill="{_RED}"/>
  <circle cx="332" cy="86" r="26" fill="#ffffff" stroke="{_RED}"/><path d="M332,96 C322,84 325,75 332,81 C339,75 342,84 332,96 Z" fill="{_RED}"/><g stroke="{_RED}" stroke-width="1.5"><line x1="332" y1="96" x2="332" y2="108"/><line x1="320" y1="74" x2="326" y2="80"/><line x1="344" y1="74" x2="338" y2="80"/></g>
  <circle cx="426" cy="86" r="26" fill="#dbeafe" stroke="{_BLUE}"/><circle cx="426" cy="74" r="6" fill="#1e40af"/><rect x="418" y="82" width="16" height="22" rx="6" fill="#1e40af"/>
  <g font-size="9" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="50" y="134">Cell</text><text x="144" y="134">Tissue</text><text x="238" y="134">Organ</text><text x="332" y="134">Organ system</text><text x="426" y="134">Organism</text>
  </g>
  <g font-size="7.5" fill="#6b7280" text-anchor="middle">
    <text x="50" y="146">muscle cell</text><text x="144" y="146">muscle tissue</text><text x="238" y="146">heart</text><text x="332" y="146">circulatory</text><text x="426" y="146">the body</text>
  </g>
  <text x="235" y="176" text-anchor="middle" font-size="8.5" fill="#6b7280">Similar cells form tissues, tissues form organs, organs form systems, and systems make up the organism.</text>
</svg>'''


# --- Human body: major organ systems ---------------------------------------
_ORGAN_SYSTEMS = f'''
<svg viewBox="0 0 470 252" role="img" aria-label="Six major organ systems and what each one does" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Major Organ Systems</text>
  <g stroke-width="1.4">
    <rect x="16" y="36" width="140" height="88" rx="8" fill="#fef2f2" stroke="{_RED}"/>
    <rect x="166" y="36" width="140" height="88" rx="8" fill="#eff6ff" stroke="{_BLUE}"/>
    <rect x="316" y="36" width="140" height="88" rx="8" fill="#f0fdf4" stroke="{_GREEN}"/>
    <rect x="16" y="134" width="140" height="88" rx="8" fill="#fefce8" stroke="#ca8a04"/>
    <rect x="166" y="134" width="140" height="88" rx="8" fill="#f5f3ff" stroke="#7c3aed"/>
    <rect x="316" y="134" width="140" height="88" rx="8" fill="#fff7ed" stroke="#ea580c"/>
  </g>
  <g text-anchor="middle">
    <circle cx="86" cy="64" r="10" fill="{_RED}"/><text x="86" y="96" font-size="11" font-weight="700" fill="{_INK}">Circulatory</text><text x="86" y="112" font-size="8" fill="#6b7280">heart moves blood</text>
    <ellipse cx="236" cy="64" rx="12" ry="9" fill="{_BLUE}"/><text x="236" y="96" font-size="11" font-weight="700" fill="{_INK}">Respiratory</text><text x="236" y="112" font-size="8" fill="#6b7280">lungs: gas exchange</text>
    <ellipse cx="386" cy="64" rx="11" ry="10" fill="{_GREEN}"/><text x="386" y="96" font-size="11" font-weight="700" fill="{_INK}">Digestive</text><text x="386" y="112" font-size="8" fill="#6b7280">breaks food to nutrients</text>
    <circle cx="86" cy="162" r="10" fill="#ca8a04"/><text x="86" y="194" font-size="11" font-weight="700" fill="{_INK}">Nervous</text><text x="86" y="210" font-size="8" fill="#6b7280">fast signals; control</text>
    <rect x="228" y="153" width="16" height="16" rx="3" fill="#7c3aed"/><text x="236" y="194" font-size="10.5" font-weight="700" fill="{_INK}">Skeletal &amp; Muscular</text><text x="236" y="210" font-size="8" fill="#6b7280">support &amp; movement</text>
    <path d="M386,152 l10,4 v8 q0,8 -10,10 q-10,-2 -10,-10 v-8 Z" fill="#ea580c"/><text x="386" y="194" font-size="11" font-weight="700" fill="{_INK}">Immune</text><text x="386" y="210" font-size="8" fill="#6b7280">defends against germs</text>
  </g>
  <text x="235" y="242" text-anchor="middle" font-size="8.5" fill="#6b7280">Each system has a job, and the systems work together to keep the body alive.</text>
</svg>'''


# --- Human body: oxygen & nutrient delivery --------------------------------
_OXYGEN_DELIVERY = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="How the respiratory, circulatory, and digestive systems deliver oxygen and glucose to a body cell" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Getting Oxygen &amp; Fuel to Your Cells</text>
  <g fill="#bfdbfe" stroke="{_BLUE}" stroke-width="1.5"><path d="M70,70 q-22,4 -18,46 q2,20 20,16 l0,-62 Z"/><path d="M96,70 q22,4 18,46 q-2,20 -20,16 l0,-62 Z"/></g>
  <line x1="83" y1="46" x2="83" y2="70" stroke="{_INK}" stroke-width="1.5"/>
  <text x="83" y="150" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Lungs</text>
  <text x="40" y="44" font-size="8" fill="{_GREEN}">O&#8322; in</text><text x="100" y="44" font-size="8" fill="#b45309">CO&#8322; out</text>
  <ellipse cx="200" cy="120" rx="24" ry="20" fill="#fecaca" stroke="{_RED}"/><path d="M200,132 C190,120 193,112 200,117 C207,112 210,120 200,132 Z" fill="{_RED}"/>
  <text x="200" y="160" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Heart / blood</text>
  <rect x="320" y="80" width="120" height="86" rx="16" fill="#eef2ff" stroke="{_BLUE}" stroke-width="2"/>
  <ellipse cx="380" cy="123" rx="20" ry="11" fill="#fecaca" stroke="{_RED}"/><text x="380" y="126" text-anchor="middle" font-size="7" fill="#b91c1c">mitochondria</text>
  <text x="380" y="158" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Body cell</text>
  <g stroke="{_GREEN}" stroke-width="2" fill="{_GREEN}"><line x1="112" y1="108" x2="176" y2="116"/><polygon points="182,117 171,112 171,121"/><line x1="224" y1="112" x2="316" y2="108"/><polygon points="322,107 311,108 313,117"/></g>
  <text x="150" y="100" font-size="8" fill="#15803d">O&#8322;</text><text x="270" y="100" font-size="8" fill="#15803d">O&#8322; + glucose</text>
  <g stroke="#b45309" stroke-width="1.6" fill="#b45309" stroke-dasharray="4 3"><line x1="316" y1="140" x2="224" y2="140"/><line x1="176" y1="136" x2="112" y2="128"/></g>
  <g fill="#b45309"><polygon points="218,140 229,135 229,145"/><polygon points="106,127 117,124 116,133"/></g>
  <text x="265" y="156" font-size="8" fill="#b45309">CO&#8322; back to lungs</text>
  <text x="235" y="206" text-anchor="middle" font-size="9" fill="#6b7280">Lungs take in oxygen; the digestive system supplies glucose; blood delivers both; cells make ATP and</text>
  <text x="235" y="220" text-anchor="middle" font-size="9" fill="#6b7280">give off carbon dioxide, which the blood carries back to the lungs to be exhaled.</text>
</svg>'''


# --- Human body: the reflex arc --------------------------------------------
_NEURON_REFLEX = f'''
<svg viewBox="0 0 470 230" role="img" aria-label="A reflex arc: a stimulus signals the spinal cord through a sensory neuron, and a motor neuron triggers the muscle" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">A Reflex Arc (fast, automatic)</text>
  <polygon points="60,150 70,120 80,150 75,150 78,134 62,134 65,150" fill="#f59e0b"/>
  <ellipse cx="70" cy="166" rx="26" ry="12" fill="#fde68a" stroke="#ca8a04"/>
  <text x="70" y="192" text-anchor="middle" font-size="8.5" fill="{_INK}">1. hot stove (stimulus)</text>
  <rect x="222" y="60" width="26" height="120" rx="10" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="235" y="50" text-anchor="middle" font-size="9" font-weight="700" fill="#6b21a8">spinal cord</text>
  <g stroke="{_GREEN}" stroke-width="2.5" fill="{_GREEN}"><line x1="92" y1="158" x2="216" y2="120"/><polygon points="222,118 210,116 213,126"/></g>
  <text x="120" y="128" font-size="8.5" fill="#15803d">2. sensory neuron (signal in)</text>
  <g stroke="{_RED}" stroke-width="2.5" fill="{_RED}"><line x1="250" y1="130" x2="372" y2="158"/><polygon points="378,160 366,156 367,166"/></g>
  <text x="300" y="128" font-size="8.5" fill="#b91c1c">3. motor neuron (signal out)</text>
  <ellipse cx="404" cy="166" rx="28" ry="14" fill="#fecaca" stroke="{_RED}"/>
  <text x="404" y="170" text-anchor="middle" font-size="8" fill="#b91c1c">muscle</text>
  <text x="404" y="194" text-anchor="middle" font-size="8.5" fill="{_INK}">4. hand pulls away (response)</text>
  <text x="235" y="216" text-anchor="middle" font-size="8.5" fill="#6b7280">The spinal cord triggers the response without waiting for the brain &#8212; that's why reflexes are so fast.</text>
</svg>'''


# --- Human body: nutrients -------------------------------------------------
_NUTRITION_CHART = f'''
<svg viewBox="0 0 470 244" role="img" aria-label="A chart of nutrient groups, their main jobs, and example foods" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Nutrients and What They Do</text>
  <g stroke="{_INK}" stroke-width="0.8">
    <rect x="20" y="34" width="150" height="26" fill="#dbeafe"/>
    <rect x="170" y="34" width="170" height="26" fill="#dbeafe"/>
    <rect x="340" y="34" width="110" height="26" fill="#dbeafe"/>
  </g>
  <g font-size="10" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="95" y="52">Nutrient</text><text x="255" y="52">Main job</text><text x="395" y="52">Example</text>
  </g>
  <g stroke="{_GRID}" stroke-width="1">
    <line x1="20" y1="60" x2="450" y2="60"/><line x1="20" y1="90" x2="450" y2="90"/><line x1="20" y1="120" x2="450" y2="120"/><line x1="20" y1="150" x2="450" y2="150"/><line x1="20" y1="180" x2="450" y2="180"/><line x1="20" y1="210" x2="450" y2="210"/>
    <line x1="20" y1="34" x2="20" y2="210"/><line x1="170" y1="34" x2="170" y2="210"/><line x1="340" y1="34" x2="340" y2="210"/><line x1="450" y1="34" x2="450" y2="210"/>
  </g>
  <g font-size="9" fill="{_INK}">
    <text x="30" y="79">Carbohydrates</text><text x="180" y="79" fill="#6b7280">quick energy</text><text x="350" y="79" fill="#6b7280">bread, rice</text>
    <text x="30" y="109">Fats</text><text x="180" y="109" fill="#6b7280">stored energy</text><text x="350" y="109" fill="#6b7280">oils, nuts</text>
    <text x="30" y="139">Proteins</text><text x="180" y="139" fill="#6b7280">build &amp; repair tissues</text><text x="350" y="139" fill="#6b7280">meat, beans</text>
    <text x="30" y="169">Vitamins</text><text x="180" y="169" fill="#6b7280">help body processes</text><text x="350" y="169" fill="#6b7280">fruits, vegetables</text>
    <text x="30" y="199">Minerals</text><text x="180" y="199" fill="#6b7280">calcium: bones; iron: blood</text><text x="350" y="199" fill="#6b7280">milk, spinach</text>
  </g>
  <text x="235" y="230" text-anchor="middle" font-size="8.5" fill="#6b7280">Calories measure energy. Carbs and fats supply energy; proteins build; vitamins and minerals help processes.</text>
</svg>'''


# --- Human body: disease transmission & prevention -------------------------
_DISEASE_TRANSMISSION = f'''
<svg viewBox="0 0 470 244" role="img" aria-label="Four ways disease spreads and a prevention method matched to each route" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How Disease Spreads &#8212; and Prevention</text>
  <g stroke-width="1.4">
    <rect x="18" y="36" width="210" height="78" rx="8" fill="#eff6ff" stroke="{_BLUE}"/>
    <rect x="242" y="36" width="210" height="78" rx="8" fill="#f0fdf4" stroke="{_GREEN}"/>
    <rect x="18" y="124" width="210" height="78" rx="8" fill="#fefce8" stroke="#ca8a04"/>
    <rect x="242" y="124" width="210" height="78" rx="8" fill="#fff7ed" stroke="#ea580c"/>
  </g>
  <g font-size="10.5" font-weight="700" fill="{_INK}">
    <text x="34" y="60">Airborne (droplets)</text>
    <text x="258" y="60">Water / food</text>
    <text x="34" y="148">Contact / blood</text>
    <text x="258" y="148">Vector (insects)</text>
  </g>
  <g font-size="8.5" fill="#6b7280">
    <text x="34" y="80">coughs, sneezes spread germs</text>
    <text x="258" y="80">contaminated water or food</text>
    <text x="34" y="168">touching, body fluids</text>
    <text x="258" y="168">e.g., mosquito bites</text>
  </g>
  <g font-size="8.5" font-weight="700" fill="#15803d">
    <text x="34" y="102">Prevent: cover coughs, ventilate</text>
    <text x="258" y="102">Prevent: clean water, sanitation</text>
    <text x="34" y="190">Prevent: handwashing</text>
    <text x="258" y="190">Prevent: nets, insect control</text>
  </g>
  <text x="235" y="228" text-anchor="middle" font-size="8.5" fill="#6b7280">The immune system fights pathogens; vaccines train it in advance. Match prevention to how the disease spreads.</text>
</svg>'''


# --- Homeostasis: a negative-feedback loop ---------------------------------
_FEEDBACK_LOOP = f'''
<svg viewBox="0 0 470 256" role="img" aria-label="A negative-feedback loop that returns a condition to its normal range" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Negative Feedback Keeps You Balanced</text>
  <g stroke-width="1.5">
    <rect x="150" y="40" width="170" height="42" rx="10" fill="#fee2e2" stroke="{_RED}"/>
    <rect x="320" y="112" width="142" height="42" rx="10" fill="#dbeafe" stroke="{_BLUE}"/>
    <rect x="150" y="184" width="170" height="42" rx="10" fill="#dcfce7" stroke="{_GREEN}"/>
    <rect x="8" y="112" width="142" height="42" rx="10" fill="#fef3c7" stroke="{_AMBER}"/>
  </g>
  <g text-anchor="middle" fill="{_INK}">
    <text x="235" y="60" font-size="10.5" font-weight="700">1. Condition leaves normal</text>
    <text x="235" y="74" font-size="8" fill="#6b7280">(e.g., body gets too hot)</text>
    <text x="391" y="131" font-size="10.5" font-weight="700">2. Sensor detects it</text>
    <text x="391" y="145" font-size="8" fill="#6b7280">sends to control center</text>
    <text x="235" y="204" font-size="10.5" font-weight="700">3. Effector responds</text>
    <text x="235" y="218" font-size="8" fill="#6b7280">(e.g., you sweat)</text>
    <text x="79" y="131" font-size="10.5" font-weight="700">4. Back to normal</text>
    <text x="79" y="145" font-size="8" fill="#6b7280">change is reversed</text>
  </g>
  <g fill="none" stroke="{_AXIS}" stroke-width="1.8">
    <path d="M320,60 C372,68 392,86 398,110"/><polygon points="398,112 392,102 404,102" fill="{_AXIS}"/>
    <path d="M390,156 C382,186 332,200 322,202"/><polygon points="322,204 333,200 328,210" fill="{_AXIS}"/>
    <path d="M150,202 C98,200 80,186 76,158"/><polygon points="76,156 70,166 82,166" fill="{_AXIS}"/>
    <path d="M80,110 C88,86 132,68 150,60"/><polygon points="150,58 139,60 145,69" fill="{_AXIS}"/>
  </g>
  <text x="235" y="246" text-anchor="middle" font-size="8.5" fill="#6b7280">'Negative' feedback means the response REVERSES the change, pushing the body back toward its set point.</text>
</svg>'''


# --- Homeostasis: thermoregulation -----------------------------------------
_THERMOREGULATION = f'''
<svg viewBox="0 0 470 234" role="img" aria-label="The body responds to being too hot or too cold to return to normal temperature" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Body Temperature: a Negative-Feedback Balance</text>
  <ellipse cx="235" cy="117" rx="66" ry="32" fill="#dcfce7" stroke="{_GREEN}" stroke-width="2"/>
  <text x="235" y="113" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Normal</text>
  <text x="235" y="128" text-anchor="middle" font-size="9" fill="#15803d">~37&#176;C</text>
  <rect x="14" y="44" width="156" height="60" rx="8" fill="#fee2e2" stroke="{_RED}"/>
  <text x="92" y="62" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b91c1c">TOO HOT</text>
  <text x="92" y="78" text-anchor="middle" font-size="8.5" fill="{_INK}">sweat; skin vessels widen</text>
  <text x="92" y="92" text-anchor="middle" font-size="8.5" fill="{_INK}">&#8594; release heat</text>
  <rect x="300" y="130" width="156" height="60" rx="8" fill="#dbeafe" stroke="{_BLUE}"/>
  <text x="378" y="148" text-anchor="middle" font-size="10.5" font-weight="700" fill="#1e40af">TOO COLD</text>
  <text x="378" y="164" text-anchor="middle" font-size="8.5" fill="{_INK}">shiver; skin vessels narrow</text>
  <text x="378" y="178" text-anchor="middle" font-size="8.5" fill="{_INK}">&#8594; keep heat</text>
  <g fill="none" stroke="{_RED}" stroke-width="2"><path d="M150,104 C180,118 188,116 196,112"/></g>
  <polygon points="200,110 189,109 193,118" fill="{_RED}"/>
  <text x="150" y="128" font-size="8" fill="#b91c1c">cools down</text>
  <g fill="none" stroke="{_BLUE}" stroke-width="2"><path d="M320,130 C290,116 282,118 274,122"/></g>
  <polygon points="270,124 281,125 277,116" fill="{_BLUE}"/>
  <text x="316" y="116" font-size="8" fill="#1e40af">warms up</text>
  <text x="235" y="220" text-anchor="middle" font-size="8.5" fill="#6b7280">Whether you get too hot or too cold, the body responds to push your temperature back toward normal.</text>
</svg>'''


# --- Homeostasis: plant stomata --------------------------------------------
_STOMATA = f'''
<svg viewBox="0 0 460 200" role="img" aria-label="Plant stomata open for gas exchange and close to conserve water during drought" xmlns="http://www.w3.org/2000/svg" style="max-width:540px;width:100%;height:auto;{_FONT}">
  <text x="230" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">A Plant Balances Water: Stomata</text>
  <g fill="#86efac" stroke="#15803d" stroke-width="1.6">
    <path d="M120,60 C96,72 96,128 120,140 C132,128 132,72 120,60 Z"/>
    <path d="M160,60 C184,72 184,128 160,140 C148,128 148,72 160,60 Z"/>
  </g>
  <ellipse cx="140" cy="100" rx="9" ry="26" fill="#ffffff" stroke="#9ca3af" stroke-width="0.8"/>
  <text x="140" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">OPEN</text>
  <text x="140" y="176" text-anchor="middle" font-size="8" fill="#6b7280">gas exchange; water escapes</text>
  <g fill="#65a30d" stroke="#15803d" stroke-width="1.6">
    <path d="M320,60 C300,72 300,128 320,140 C336,128 336,72 320,60 Z"/>
    <path d="M340,60 C360,72 360,128 340,140 C324,128 324,72 340,60 Z"/>
  </g>
  <text x="330" y="160" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">CLOSED</text>
  <text x="330" y="176" text-anchor="middle" font-size="8" fill="#6b7280">conserves water (drought)</text>
  <text x="230" y="194" text-anchor="middle" font-size="8.5" fill="#6b7280">Guard cells open and close the pore &#8212; a plant keeping its internal water in balance (homeostasis).</text>
</svg>'''


# --- Homeostasis: blood glucose after a meal -------------------------------
_BLOOD_GLUCOSE_GRAPH = f'''
<svg viewBox="0 0 380 236" role="img" aria-label="A graph of blood glucose rising after a meal and returning to normal" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;{_FONT}">
  <text x="190" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">Blood Glucose After a Meal</text>
  <line x1="50" y1="34" x2="50" y2="190" stroke="{_AXIS}"/>
  <line x1="50" y1="190" x2="350" y2="190" stroke="{_AXIS}"/>
  <text x="22" y="112" font-size="10" fill="#6b7280" transform="rotate(-90 22 112)" text-anchor="middle">Blood glucose</text>
  <text x="200" y="216" font-size="10" fill="#6b7280" text-anchor="middle">Time</text>
  <line x1="50" y1="150" x2="350" y2="150" stroke="{_GREEN}" stroke-width="1.4" stroke-dasharray="5 4"/>
  <text x="346" y="144" text-anchor="end" font-size="8.5" fill="#15803d">normal range</text>
  <path d="M50,152 L96,150 C120,150 130,70 165,68 C210,66 250,140 350,150" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <line x1="96" y1="190" x2="96" y2="62" stroke="{_AXIS}" stroke-width="0.8" stroke-dasharray="3 3"/>
  <text x="96" y="206" text-anchor="middle" font-size="8.5" fill="{_INK}">meal</text>
  <text x="150" y="56" font-size="8.5" fill="#1e40af">rises after eating</text>
  <text x="270" y="130" font-size="8.5" fill="#15803d">returns to normal</text>
</svg>'''


# --- Homeostasis / data: parts of an experiment ----------------------------
_EXPERIMENT_VARIABLES = f'''
<svg viewBox="0 0 470 226" role="img" aria-label="The parts of a fair experiment: independent variable, dependent variable, and controlled variables" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Parts of a Fair Experiment</text>
  <rect x="20" y="44" width="180" height="58" rx="10" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <text x="110" y="66" text-anchor="middle" font-size="11" font-weight="700" fill="#1e3a8a">Independent variable</text>
  <text x="110" y="82" text-anchor="middle" font-size="8.5" fill="{_INK}">what you CHANGE</text>
  <text x="110" y="95" text-anchor="middle" font-size="8" fill="#6b7280">(amount of fertilizer)</text>
  <rect x="270" y="44" width="180" height="58" rx="10" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="360" y="66" text-anchor="middle" font-size="11" font-weight="700" fill="#15803d">Dependent variable</text>
  <text x="360" y="82" text-anchor="middle" font-size="8.5" fill="{_INK}">what you MEASURE</text>
  <text x="360" y="95" text-anchor="middle" font-size="8" fill="#6b7280">(plant height)</text>
  <line x1="200" y1="73" x2="266" y2="73" stroke="{_AXIS}" stroke-width="1.8"/><polygon points="272,73 260,68 260,78" fill="{_AXIS}"/>
  <text x="236" y="66" text-anchor="middle" font-size="8" fill="#6b7280">affects?</text>
  <rect x="90" y="128" width="290" height="56" rx="10" fill="#fef3c7" stroke="{_AMBER}" stroke-width="1.5"/>
  <text x="235" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309">Controlled variables</text>
  <text x="235" y="166" text-anchor="middle" font-size="8.5" fill="{_INK}">kept the SAME for a fair test</text>
  <text x="235" y="178" text-anchor="middle" font-size="8" fill="#6b7280">(water, light, soil, pot size)</text>
  <text x="235" y="208" text-anchor="middle" font-size="8.5" fill="#6b7280">Change ONE thing, measure the result, and keep everything else the same. Repeat trials for reliability.</text>
</svg>'''


# --- Homeostasis / data: correlation vs causation --------------------------
_CORRELATION_CAUSATION = f'''
<svg viewBox="0 0 470 224" role="img" aria-label="Two correlated variables, ice cream sales and sunburns, both caused by a third factor: hot sunny weather" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Correlation Is Not Causation</text>
  <rect x="30" y="40" width="150" height="40" rx="8" fill="#eff6ff" stroke="{_BLUE}"/>
  <text x="105" y="64" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Ice cream sales &#8593;</text>
  <rect x="290" y="40" width="150" height="40" rx="8" fill="#fff7ed" stroke="#ea580c"/>
  <text x="365" y="64" text-anchor="middle" font-size="10" font-weight="700" fill="{_INK}">Sunburns &#8593;</text>
  <line x1="180" y1="60" x2="290" y2="60" stroke="{_AXIS}" stroke-width="1.4" stroke-dasharray="5 4"/>
  <text x="235" y="52" text-anchor="middle" font-size="8" fill="#6b7280">rise together (correlated)</text>
  <g stroke="{_RED}" stroke-width="2"><line x1="205" y1="74" x2="265" y2="74"/><line x1="226" y1="64" x2="244" y2="84"/><line x1="244" y1="64" x2="226" y2="84"/></g>
  <text x="235" y="98" text-anchor="middle" font-size="8" fill="#b91c1c">one does NOT cause the other</text>
  <rect x="150" y="150" width="170" height="44" rx="10" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="235" y="170" text-anchor="middle" font-size="10.5" font-weight="700" fill="#b45309">Hot, sunny weather</text>
  <text x="235" y="184" text-anchor="middle" font-size="8" fill="#6b7280">the real cause of both</text>
  <g fill="none" stroke="{_GREEN}" stroke-width="2"><path d="M180,150 C150,130 120,100 105,84"/><path d="M290,150 C320,130 350,100 365,84"/></g>
  <polygon points="103,80 110,90 114,80" fill="{_GREEN}"/><polygon points="367,80 356,82 360,92" fill="{_GREEN}"/>
  <text x="235" y="214" text-anchor="middle" font-size="8.5" fill="#6b7280">A third factor can make two things rise together. To show cause, you need a controlled experiment.</text>
</svg>'''


# --- Matter: the particle model of the three states -----------------------
_PARTICLE_MODEL = f'''
<svg viewBox="0 0 470 220" role="img" aria-label="Particle arrangement in solids, liquids, and gases, with their shape and volume properties" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">The Particle Model of Matter</text>
  <g stroke="{_INK}" stroke-width="1.2" fill="none">
    <rect x="20" y="36" width="130" height="110" rx="6"/>
    <rect x="170" y="36" width="130" height="110" rx="6"/>
    <rect x="320" y="36" width="130" height="110" rx="6"/>
  </g>
  <g fill="{_BLUE}">
    <circle cx="42" cy="58" r="7"/><circle cx="64" cy="58" r="7"/><circle cx="86" cy="58" r="7"/><circle cx="108" cy="58" r="7"/><circle cx="130" cy="58" r="7"/>
    <circle cx="42" cy="80" r="7"/><circle cx="64" cy="80" r="7"/><circle cx="86" cy="80" r="7"/><circle cx="108" cy="80" r="7"/><circle cx="130" cy="80" r="7"/>
    <circle cx="42" cy="102" r="7"/><circle cx="64" cy="102" r="7"/><circle cx="86" cy="102" r="7"/><circle cx="108" cy="102" r="7"/><circle cx="130" cy="102" r="7"/>
    <circle cx="42" cy="124" r="7"/><circle cx="64" cy="124" r="7"/><circle cx="86" cy="124" r="7"/><circle cx="108" cy="124" r="7"/><circle cx="130" cy="124" r="7"/>
  </g>
  <g fill="#16a34a">
    <circle cx="190" cy="62" r="7"/><circle cx="212" cy="70" r="7"/><circle cx="236" cy="60" r="7"/><circle cx="262" cy="72" r="7"/><circle cx="285" cy="64" r="7"/>
    <circle cx="198" cy="90" r="7"/><circle cx="224" cy="96" r="7"/><circle cx="250" cy="88" r="7"/><circle cx="278" cy="98" r="7"/>
    <circle cx="186" cy="118" r="7"/><circle cx="212" cy="122" r="7"/><circle cx="240" cy="116" r="7"/><circle cx="268" cy="124" r="7"/><circle cx="290" cy="116" r="7"/>
  </g>
  <g fill="{_RED}">
    <circle cx="345" cy="60" r="7"/><circle cx="410" cy="72" r="7"/><circle cx="380" cy="100" r="7"/><circle cx="430" cy="118" r="7"/><circle cx="350" cy="126" r="7"/><circle cx="412" cy="48" r="7"/>
  </g>
  <g stroke="{_RED}" stroke-width="1" fill="none"><path d="M360,58 l8,-4"/><path d="M396,104 l-8,5"/><path d="M425,112 l7,-5"/></g>
  <g font-size="11" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="85" y="166">Solid</text><text x="235" y="166">Liquid</text><text x="385" y="166">Gas</text>
  </g>
  <g font-size="8" fill="#6b7280" text-anchor="middle">
    <text x="85" y="180">packed, fixed; vibrate</text><text x="235" y="180">close, slide past</text><text x="385" y="180">far apart, fast</text>
    <text x="85" y="194">fixed shape &amp; volume</text><text x="235" y="194">fixed volume only</text><text x="385" y="194">fills its container</text>
  </g>
  <text x="235" y="212" text-anchor="middle" font-size="8.5" fill="#6b7280">Same particles, different spacing and energy &#8212; that's what makes a solid, liquid, or gas.</text>
</svg>'''


# --- Matter: changes of state ----------------------------------------------
_PHASE_CHANGE_DIAGRAM = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="Changes of state between solid, liquid, and gas, including sublimation and deposition" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Changes of State</text>
  <g stroke="{_INK}" stroke-width="1.2">
    <rect x="20" y="100" width="110" height="56" rx="10" fill="#e0f2fe"/>
    <rect x="180" y="100" width="110" height="56" rx="10" fill="#bae6fd"/>
    <rect x="340" y="100" width="110" height="56" rx="10" fill="#7dd3fc"/>
  </g>
  <g text-anchor="middle" font-weight="700" fill="{_INK}">
    <text x="75" y="126" font-size="12">SOLID</text><text x="75" y="142" font-size="8">ice</text>
    <text x="235" y="126" font-size="12">LIQUID</text><text x="235" y="142" font-size="8">water</text>
    <text x="395" y="126" font-size="12">GAS</text><text x="395" y="142" font-size="8">water vapor</text>
  </g>
  <line x1="130" y1="116" x2="180" y2="116" stroke="{_RED}" stroke-width="2"/><polygon points="180,116 170,111 170,121" fill="{_RED}"/>
  <line x1="180" y1="140" x2="130" y2="140" stroke="{_BLUE}" stroke-width="2"/><polygon points="130,140 140,135 140,145" fill="{_BLUE}"/>
  <text x="155" y="94" text-anchor="middle" font-size="8" fill="{_RED}">melting</text>
  <text x="155" y="156" text-anchor="middle" font-size="8" fill="{_BLUE}">freezing</text>
  <line x1="290" y1="116" x2="340" y2="116" stroke="{_RED}" stroke-width="2"/><polygon points="340,116 330,111 330,121" fill="{_RED}"/>
  <line x1="340" y1="140" x2="290" y2="140" stroke="{_BLUE}" stroke-width="2"/><polygon points="290,140 300,135 300,145" fill="{_BLUE}"/>
  <text x="315" y="94" text-anchor="middle" font-size="8" fill="{_RED}">evaporation</text>
  <text x="315" y="156" text-anchor="middle" font-size="8" fill="{_BLUE}">condensation</text>
  <path d="M70,100 C90,50 380,50 400,100" fill="none" stroke="{_RED}" stroke-width="1.6" stroke-dasharray="5 3"/><polygon points="400,100 390,92 398,88" fill="{_RED}"/>
  <text x="235" y="58" text-anchor="middle" font-size="8" fill="{_RED}">sublimation (solid &#8594; gas)</text>
  <path d="M400,168 C380,206 90,206 70,168" fill="none" stroke="{_BLUE}" stroke-width="1.6" stroke-dasharray="5 3"/><polygon points="70,168 80,176 72,180" fill="{_BLUE}"/>
  <text x="235" y="206" text-anchor="middle" font-size="8" fill="{_BLUE}">deposition (gas &#8594; solid)</text>
  <text x="235" y="228" text-anchor="middle" font-size="8.5" fill="#6b7280">Adding energy moves matter toward gas; removing energy moves it toward solid. The substance stays the same.</text>
</svg>'''


# --- Matter: a heating curve -----------------------------------------------
_HEATING_CURVE = f'''
<svg viewBox="0 0 400 244" role="img" aria-label="A heating curve: temperature rises, then stays flat during melting and boiling" xmlns="http://www.w3.org/2000/svg" style="max-width:460px;width:100%;height:auto;{_FONT}">
  <text x="200" y="20" text-anchor="middle" font-size="13" font-weight="700" fill="{_INK}">A Heating Curve</text>
  <line x1="50" y1="32" x2="50" y2="196" stroke="{_AXIS}"/>
  <line x1="50" y1="196" x2="376" y2="196" stroke="{_AXIS}"/>
  <text x="22" y="114" font-size="10" fill="#6b7280" transform="rotate(-90 22 114)" text-anchor="middle">Temperature</text>
  <text x="210" y="222" font-size="10" fill="#6b7280" text-anchor="middle">Heat added (time)</text>
  <polyline points="50,180 100,140 160,140 210,90 300,90 360,50" fill="none" stroke="{_RED}" stroke-width="2.5"/>
  <line x1="100" y1="140" x2="100" y2="196" stroke="{_GRID}" stroke-dasharray="3 3"/>
  <line x1="210" y1="90" x2="210" y2="196" stroke="{_GRID}" stroke-dasharray="3 3"/>
  <text x="130" y="132" text-anchor="middle" font-size="8" fill="{_INK}">melting</text>
  <text x="255" y="82" text-anchor="middle" font-size="8" fill="{_INK}">boiling</text>
  <g font-size="8" fill="#6b7280" text-anchor="middle">
    <text x="74" y="172">solid</text><text x="185" y="118">liquid</text><text x="345" y="44">gas</text>
  </g>
  <text x="200" y="238" text-anchor="middle" font-size="8.5" fill="#6b7280">The flat parts are changes of state: added heat breaks bonds instead of raising the temperature.</text>
</svg>'''


# --- Matter: density & floating --------------------------------------------
_DENSITY_COMPARE = f'''
<svg viewBox="0 0 470 230" role="img" aria-label="Density compares mass in the same volume; less dense objects float and denser ones sink" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Density = Mass &#247; Volume</text>
  <rect x="30" y="46" width="80" height="80" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <g fill="{_BLUE}"><circle cx="50" cy="66" r="5"/><circle cx="90" cy="70" r="5"/><circle cx="62" cy="100" r="5"/><circle cx="95" cy="106" r="5"/></g>
  <text x="70" y="142" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">less dense</text>
  <text x="70" y="155" text-anchor="middle" font-size="8" fill="#6b7280">fewer particles &#8594; floats</text>
  <rect x="140" y="46" width="80" height="80" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.5"/>
  <g fill="{_BLUE}"><circle cx="156" cy="60" r="5"/><circle cx="176" cy="60" r="5"/><circle cx="196" cy="60" r="5"/><circle cx="156" cy="82" r="5"/><circle cx="176" cy="82" r="5"/><circle cx="196" cy="82" r="5"/><circle cx="156" cy="104" r="5"/><circle cx="176" cy="104" r="5"/><circle cx="196" cy="104" r="5"/></g>
  <text x="180" y="142" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">more dense</text>
  <text x="180" y="155" text-anchor="middle" font-size="8" fill="#6b7280">same size, more mass &#8594; sinks</text>
  <rect x="290" y="44" width="150" height="150" rx="4" fill="#eaf6ff" stroke="{_BLUE}"/>
  <rect x="290" y="86" width="150" height="108" fill="#bae6fd" opacity="0.7"/>
  <rect x="320" y="60" width="34" height="22" rx="3" fill="#facc15" stroke="#ca8a04"/>
  <text x="337" y="56" text-anchor="middle" font-size="7.5" fill="#b45309">floats</text>
  <rect x="380" y="160" width="30" height="22" rx="3" fill="#6b7280" stroke="#374151"/>
  <text x="395" y="156" text-anchor="middle" font-size="7.5" fill="#374151">sinks</text>
  <text x="365" y="210" text-anchor="middle" font-size="8.5" fill="#6b7280">Less dense than water floats; denser than water sinks.</text>
</svg>'''


# --- Matter: physical vs chemical changes ----------------------------------
_PHYSICAL_VS_CHEMICAL = f'''
<svg viewBox="0 0 470 226" role="img" aria-label="Physical changes keep the same substance; chemical changes form a new substance" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Physical vs. Chemical Change</text>
  <rect x="18" y="36" width="210" height="160" rx="10" fill="#eff6ff" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="242" y="36" width="210" height="160" rx="10" fill="#fef2f2" stroke="{_RED}" stroke-width="1.5"/>
  <text x="123" y="58" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">Physical change</text>
  <text x="123" y="74" text-anchor="middle" font-size="8.5" fill="#6b7280">same substance, new form</text>
  <text x="347" y="58" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c">Chemical change</text>
  <text x="347" y="74" text-anchor="middle" font-size="8.5" fill="#6b7280">a NEW substance forms</text>
  <g font-size="9" fill="{_INK}">
    <text x="36" y="98">&#8226; ice melting</text>
    <text x="36" y="118">&#8226; cutting or tearing paper</text>
    <text x="36" y="138">&#8226; dissolving sugar in water</text>
    <text x="36" y="158">&#8226; bending a wire</text>
    <text x="260" y="98">&#8226; burning wood</text>
    <text x="260" y="118">&#8226; iron rusting</text>
    <text x="260" y="138">&#8226; baking a cake</text>
    <text x="260" y="158">&#8226; digesting food</text>
  </g>
  <text x="123" y="184" text-anchor="middle" font-size="8" fill="#6b7280">usually easy to reverse</text>
  <text x="347" y="180" text-anchor="middle" font-size="8" fill="#6b7280">signs: color change, gas/bubbles,</text>
  <text x="347" y="190" text-anchor="middle" font-size="8" fill="#6b7280">light/heat, hard to reverse</text>
  <text x="235" y="216" text-anchor="middle" font-size="8.5" fill="#6b7280">Ask: did a NEW substance form? If yes, it's a chemical change.</text>
</svg>'''


# --- Matter: mixtures, solutions & separation ------------------------------
_MIXTURES_SOLUTIONS = f'''
<svg viewBox="0 0 470 228" role="img" aria-label="A heterogeneous mixture, a solution, and ways to separate mixtures" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Mixtures, Solutions &amp; Separating Them</text>
  <path d="M40,52 h70 v76 a35,14 0 0 1 -70,0 Z" fill="#eaf6ff" stroke="{_BLUE}" stroke-width="1.2"/>
  <g fill="#ca8a04"><circle cx="56" cy="80" r="5"/><circle cx="90" cy="92" r="5"/><circle cx="70" cy="108" r="5"/></g>
  <g fill="#16a34a"><circle cx="80" cy="76" r="4"/><circle cx="60" cy="100" r="4"/><circle cx="96" cy="110" r="4"/></g>
  <text x="75" y="150" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Heterogeneous</text>
  <text x="75" y="163" text-anchor="middle" font-size="7.5" fill="#6b7280">parts are visible</text>
  <path d="M180,52 h70 v76 a35,14 0 0 1 -70,0 Z" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.2"/>
  <g fill="#2563eb" opacity="0.55"><circle cx="196" cy="78" r="3"/><circle cx="214" cy="86" r="3"/><circle cx="232" cy="76" r="3"/><circle cx="204" cy="100" r="3"/><circle cx="226" cy="104" r="3"/><circle cx="240" cy="92" r="3"/><circle cx="190" cy="112" r="3"/><circle cx="220" cy="118" r="3"/></g>
  <text x="215" y="150" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Solution</text>
  <text x="215" y="163" text-anchor="middle" font-size="7.5" fill="#6b7280">uniform; dissolved</text>
  <g stroke="{_INK}" stroke-width="1.2" fill="none">
    <path d="M330,56 l40,0 l-14,22 l0,30 l-12,0 l0,-30 Z" fill="#ffffff"/>
  </g>
  <g fill="#ca8a04"><circle cx="346" cy="66" r="3"/><circle cx="356" cy="70" r="3"/></g>
  <line x1="350" y1="118" x2="350" y2="138" stroke="{_BLUE}" stroke-width="2"/><polygon points="350,142 345,132 355,132" fill="{_BLUE}"/>
  <ellipse cx="350" cy="152" rx="22" ry="7" fill="#dbeafe" stroke="{_BLUE}"/>
  <text x="408" y="80" font-size="8.5" font-weight="700" fill="{_INK}">Filtration</text>
  <text x="408" y="92" font-size="7.5" fill="#6b7280">traps solids</text>
  <text x="408" y="150" font-size="8.5" font-weight="700" fill="{_INK}">Evaporation</text>
  <text x="408" y="162" font-size="7.5" fill="#6b7280">leaves dissolved solid</text>
  <text x="235" y="204" text-anchor="middle" font-size="8.5" fill="#6b7280">Mixtures are physically combined and can be separated by physical means.</text>
  <text x="235" y="218" text-anchor="middle" font-size="8.5" fill="#6b7280">A solution is a uniform (homogeneous) mixture; its parts keep their properties.</text>
</svg>'''


# --- Atoms: anatomy of an atom ---------------------------------------------
_ATOM_ANATOMY = f'''
<svg viewBox="0 0 470 250" role="img" aria-label="An atom with protons and neutrons in the nucleus and electrons in shells" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Inside an Atom</text>
  <circle cx="170" cy="132" r="46" fill="none" stroke="{_GRID}" stroke-width="1.2"/>
  <circle cx="170" cy="132" r="82" fill="none" stroke="{_GRID}" stroke-width="1.2"/>
  <g stroke="{_INK}" stroke-width="0.5">
    <circle cx="162" cy="124" r="9" fill="{_RED}"/><circle cx="180" cy="124" r="9" fill="#9ca3af"/><circle cx="170" cy="140" r="9" fill="{_RED}"/>
    <circle cx="158" cy="140" r="9" fill="#9ca3af"/><circle cx="182" cy="140" r="9" fill="{_RED}"/><circle cx="172" cy="122" r="9" fill="#9ca3af"/>
  </g>
  <g fill="{_BLUE}" stroke="#1e40af" stroke-width="0.5">
    <circle cx="170" cy="86" r="6"/><circle cx="170" cy="178" r="6"/>
    <circle cx="88" cy="132" r="6"/><circle cx="252" cy="132" r="6"/><circle cx="124" cy="74" r="6"/><circle cx="216" cy="190" r="6"/>
  </g>
  <g stroke="#9ca3af" stroke-width="0.8">
    <line x1="186" y1="124" x2="300" y2="70"/><line x1="252" y1="132" x2="300" y2="120"/>
    <line x1="182" y1="140" x2="300" y2="170"/><line x1="170" y1="178" x2="300" y2="210"/>
  </g>
  <g font-size="10" fill="{_INK}">
    <text x="304" y="64">Nucleus</text><text x="304" y="76" font-size="8" fill="#6b7280">(protons + neutrons)</text>
    <text x="304" y="118">Proton (+)</text>
    <text x="304" y="168">Neutron (0)</text>
    <text x="304" y="208">Electron (&#8722;)</text>
  </g>
  <circle cx="293" cy="114" r="5" fill="{_RED}"/><circle cx="294" cy="164" r="5" fill="#9ca3af"/><circle cx="294" cy="204" r="5" fill="{_BLUE}"/>
  <text x="170" y="240" text-anchor="middle" font-size="8.5" fill="#6b7280">In a neutral atom, the number of protons (+) equals the number of electrons (&#8722;).</text>
</svg>'''


# --- Atoms: reading an element box -----------------------------------------
_ATOMIC_NUMBER_MASS = f'''
<svg viewBox="0 0 470 238" role="img" aria-label="An element box for carbon and how to find protons, neutrons, and electrons" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Reading an Element Box</text>
  <rect x="34" y="48" width="150" height="150" rx="6" fill="#eff6ff" stroke="{_BLUE}" stroke-width="2"/>
  <text x="48" y="76" font-size="20" font-weight="700" fill="{_INK}">6</text>
  <text x="48" y="88" font-size="8" fill="#6b7280">atomic number</text>
  <text x="109" y="138" text-anchor="middle" font-size="44" font-weight="700" fill="#1e3a8a">C</text>
  <text x="109" y="166" text-anchor="middle" font-size="11" fill="{_INK}">Carbon</text>
  <text x="109" y="188" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">12.01</text>
  <text x="109" y="198" text-anchor="middle" font-size="7.5" fill="#6b7280">atomic mass</text>
  <g font-size="10.5" fill="{_INK}">
    <text x="214" y="82">Protons = atomic number = 6</text>
    <text x="214" y="116">Electrons = protons = 6</text>
    <text x="214" y="124" font-size="8" fill="#6b7280">(in a neutral atom)</text>
    <text x="214" y="158">Neutrons = mass &#8722; atomic number</text>
    <text x="214" y="174" font-weight="700">&#8776; 12 &#8722; 6 = 6</text>
  </g>
  <text x="235" y="222" text-anchor="middle" font-size="8.5" fill="#6b7280">The atomic number (protons) identifies the element; the atomic mass is about protons + neutrons.</text>
</svg>'''


# --- Atoms: Bohr models ----------------------------------------------------
_BOHR_MODELS = f'''
<svg viewBox="0 0 470 216" role="img" aria-label="Bohr models of hydrogen, helium, carbon, and oxygen showing electrons filling shells" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Bohr Models: Electrons Fill Shells</text>
  <g>
    <circle cx="70" cy="100" r="32" fill="none" stroke="{_GRID}"/>
    <circle cx="70" cy="100" r="13" fill="#fee2e2" stroke="{_RED}"/><text x="70" y="104" text-anchor="middle" font-size="9" font-weight="700" fill="#b91c1c">H</text>
    <circle cx="70" cy="68" r="5" fill="{_BLUE}"/>
    <text x="70" y="168" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Hydrogen</text>
    <text x="70" y="180" text-anchor="middle" font-size="8" fill="#6b7280">1 electron</text>
  </g>
  <g>
    <circle cx="185" cy="100" r="32" fill="none" stroke="{_GRID}"/>
    <circle cx="185" cy="100" r="13" fill="#fee2e2" stroke="{_RED}"/><text x="185" y="104" text-anchor="middle" font-size="9" font-weight="700" fill="#b91c1c">He</text>
    <circle cx="185" cy="68" r="5" fill="{_BLUE}"/><circle cx="185" cy="132" r="5" fill="{_BLUE}"/>
    <text x="185" y="168" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Helium</text>
    <text x="185" y="180" text-anchor="middle" font-size="8" fill="#6b7280">2 (full shell)</text>
  </g>
  <g>
    <circle cx="300" cy="100" r="22" fill="none" stroke="{_GRID}"/><circle cx="300" cy="100" r="40" fill="none" stroke="{_GRID}"/>
    <circle cx="300" cy="100" r="13" fill="#fee2e2" stroke="{_RED}"/><text x="300" y="104" text-anchor="middle" font-size="9" font-weight="700" fill="#b91c1c">C</text>
    <circle cx="300" cy="78" r="5" fill="{_BLUE}"/><circle cx="300" cy="122" r="5" fill="{_BLUE}"/>
    <circle cx="260" cy="100" r="5" fill="{_BLUE}"/><circle cx="340" cy="100" r="5" fill="{_BLUE}"/><circle cx="272" cy="72" r="5" fill="{_BLUE}"/><circle cx="328" cy="128" r="5" fill="{_BLUE}"/>
    <text x="300" y="168" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Carbon</text>
    <text x="300" y="180" text-anchor="middle" font-size="8" fill="#6b7280">2 inner, 4 outer</text>
  </g>
  <g>
    <circle cx="415" cy="100" r="22" fill="none" stroke="{_GRID}"/><circle cx="415" cy="100" r="40" fill="none" stroke="{_GRID}"/>
    <circle cx="415" cy="100" r="13" fill="#fee2e2" stroke="{_RED}"/><text x="415" y="104" text-anchor="middle" font-size="9" font-weight="700" fill="#b91c1c">O</text>
    <circle cx="415" cy="78" r="5" fill="{_BLUE}"/><circle cx="415" cy="122" r="5" fill="{_BLUE}"/>
    <circle cx="375" cy="100" r="5" fill="{_BLUE}"/><circle cx="455" cy="100" r="5" fill="{_BLUE}"/><circle cx="387" cy="72" r="5" fill="{_BLUE}"/><circle cx="443" cy="72" r="5" fill="{_BLUE}"/><circle cx="387" cy="128" r="5" fill="{_BLUE}"/><circle cx="443" cy="128" r="5" fill="{_BLUE}"/>
    <text x="415" y="168" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Oxygen</text>
    <text x="415" y="180" text-anchor="middle" font-size="8" fill="#6b7280">2 inner, 6 outer</text>
  </g>
  <text x="235" y="206" text-anchor="middle" font-size="8.5" fill="#6b7280">The first shell holds up to 2 electrons; the next holds up to 8. Outer (valence) electrons drive chemistry.</text>
</svg>'''


# --- Atoms: how the periodic table is organized ----------------------------
_PERIODIC_TABLE_MAP = f'''
<svg viewBox="0 0 470 262" role="img" aria-label="A simplified periodic table showing metals, nonmetals, metalloids, periods, and groups" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">How the Periodic Table Is Organized</text>
  <rect x="70" y="56" width="360" height="150" rx="4" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.2"/>
  <polygon points="270,56 430,56 430,150 330,150 330,120 300,120 300,90 270,90" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <polygon points="270,90 300,90 300,120 330,120 330,150 300,150 300,128 270,128" fill="#fef3c7" stroke="#ca8a04" stroke-width="1"/>
  <rect x="412" y="56" width="18" height="150" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <rect x="70" y="56" width="18" height="150" fill="#fee2e2" stroke="{_RED}" stroke-width="1"/>
  <g font-size="9" font-weight="700" fill="{_INK}">
    <text x="150" y="120">Metals</text>
    <text x="350" y="84" fill="#15803d">Nonmetals</text>
  </g>
  <text x="79" y="226" font-size="7.5" fill="#b91c1c" text-anchor="middle" transform="rotate(90 79 130)">alkali metals</text>
  <text x="421" y="226" font-size="7.5" fill="#6b21a8" text-anchor="middle" transform="rotate(90 421 130)">noble gases</text>
  <line x1="70" y1="44" x2="430" y2="44" stroke="{_AXIS}" stroke-width="1.4"/><polygon points="430,44 420,40 420,48" fill="{_AXIS}"/>
  <text x="250" y="38" text-anchor="middle" font-size="8.5" fill="#6b7280">Groups (columns): similar properties &#8594;</text>
  <line x1="58" y1="56" x2="58" y2="206" stroke="{_AXIS}" stroke-width="1.4"/><polygon points="58,206 54,196 62,196" fill="{_AXIS}"/>
  <text x="40" y="131" text-anchor="middle" font-size="8.5" fill="#6b7280" transform="rotate(-90 40 131)">Periods (rows)</text>
  <g font-size="8" fill="{_INK}">
    <rect x="92" y="222" width="11" height="9" fill="#dbeafe" stroke="{_BLUE}"/><text x="108" y="230">metals</text>
    <rect x="168" y="222" width="11" height="9" fill="#dcfce7" stroke="#16a34a"/><text x="184" y="230">nonmetals</text>
    <rect x="258" y="222" width="11" height="9" fill="#fef3c7" stroke="#ca8a04"/><text x="274" y="230">metalloids</text>
  </g>
  <text x="235" y="250" text-anchor="middle" font-size="8.5" fill="#6b7280">Elements are arranged by increasing atomic number; each column (group) shares similar properties.</text>
</svg>'''


# --- Atoms: elements vs compounds ------------------------------------------
_ELEMENT_VS_COMPOUND = f'''
<svg viewBox="0 0 470 218" role="img" aria-label="An element is one kind of atom; a compound is different atoms chemically bonded" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Elements vs. Compounds</text>
  <rect x="18" y="36" width="210" height="130" rx="10" fill="#eff6ff" stroke="{_BLUE}" stroke-width="1.5"/>
  <rect x="242" y="36" width="210" height="130" rx="10" fill="#f0fdf4" stroke="{_GREEN}" stroke-width="1.5"/>
  <text x="123" y="58" text-anchor="middle" font-size="12" font-weight="700" fill="#1e40af">Element</text>
  <text x="123" y="72" text-anchor="middle" font-size="8.5" fill="#6b7280">one kind of atom</text>
  <g fill="{_BLUE}" stroke="#1e40af" stroke-width="0.6">
    <circle cx="70" cy="110" r="13"/><circle cx="100" cy="110" r="13"/>
    <circle cx="150" cy="128" r="13"/><circle cx="180" cy="128" r="13"/>
  </g>
  <line x1="83" y1="110" x2="87" y2="110" stroke="#1e40af" stroke-width="3"/>
  <line x1="163" y1="128" x2="167" y2="128" stroke="#1e40af" stroke-width="3"/>
  <text x="123" y="156" text-anchor="middle" font-size="8" fill="#6b7280">e.g., oxygen gas (O&#8322;)</text>
  <text x="347" y="58" text-anchor="middle" font-size="12" font-weight="700" fill="#15803d">Compound</text>
  <text x="347" y="72" text-anchor="middle" font-size="8.5" fill="#6b7280">different atoms bonded</text>
  <g>
    <circle cx="320" cy="112" r="15" fill="{_RED}" stroke="#991b1b" stroke-width="0.6"/><text x="320" y="116" text-anchor="middle" font-size="9" fill="#fff">O</text>
    <circle cx="300" cy="96" r="9" fill="#e5e7eb" stroke="#9ca3af"/><text x="300" y="99" text-anchor="middle" font-size="7" fill="{_INK}">H</text>
    <circle cx="340" cy="96" r="9" fill="#e5e7eb" stroke="#9ca3af"/><text x="340" y="99" text-anchor="middle" font-size="7" fill="{_INK}">H</text>
    <line x1="309" y1="103" x2="312" y2="106" stroke="{_INK}" stroke-width="2"/><line x1="331" y1="103" x2="328" y2="106" stroke="{_INK}" stroke-width="2"/>
  </g>
  <text x="385" y="120" font-size="11" font-weight="700" fill="{_INK}">H&#8322;O</text>
  <text x="347" y="156" text-anchor="middle" font-size="8" fill="#6b7280">e.g., water (2 H + 1 O)</text>
  <text x="235" y="196" text-anchor="middle" font-size="8.5" fill="#6b7280">A compound has new properties: hydrogen and oxygen are gases, but together they make liquid water.</text>
  <text x="235" y="210" text-anchor="middle" font-size="8.5" fill="#6b7280">A molecule is two or more atoms bonded &#8212; of one element (O&#8322;) or of a compound (H&#8322;O).</text>
</svg>'''


# --- Atoms: ions and isotopes ----------------------------------------------
_IONS_ISOTOPES = f'''
<svg viewBox="0 0 470 230" role="img" aria-label="Ions form by gaining or losing electrons; isotopes differ in number of neutrons" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Ions and Isotopes</text>
  <g stroke="{_GRID}" stroke-width="1"><line x1="235" y1="36" x2="235" y2="200"/></g>
  <text x="118" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Ion: change in electrons</text>
  <circle cx="90" cy="104" r="30" fill="none" stroke="{_GRID}"/>
  <circle cx="90" cy="104" r="12" fill="#fee2e2" stroke="{_RED}"/>
  <circle cx="90" cy="74" r="5" fill="{_BLUE}"/><circle cx="60" cy="104" r="5" fill="{_BLUE}"/><circle cx="120" cy="104" r="5" fill="{_BLUE}"/>
  <line x1="124" y1="98" x2="158" y2="86" stroke="{_INK}" stroke-width="1.5"/><polygon points="162,84 151,85 155,93" fill="{_INK}"/>
  <circle cx="166" cy="80" r="5" fill="{_BLUE}"/>
  <text x="150" y="118" font-size="20" font-weight="700" fill="{_RED}">+</text>
  <text x="118" y="158" text-anchor="middle" font-size="8.5" fill="#6b7280">lose an electron &#8594; positive ion</text>
  <text x="118" y="170" text-anchor="middle" font-size="8.5" fill="#6b7280">gain an electron &#8594; negative ion</text>
  <text x="352" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">Isotope: change in neutrons</text>
  <g stroke="{_INK}" stroke-width="0.5">
    <circle cx="296" cy="100" r="8" fill="{_RED}"/><circle cx="312" cy="100" r="8" fill="#9ca3af"/><circle cx="304" cy="112" r="8" fill="{_RED}"/><circle cx="304" cy="88" r="8" fill="#9ca3af"/><circle cx="288" cy="112" r="8" fill="{_RED}"/><circle cx="320" cy="112" r="8" fill="#9ca3af"/>
  </g>
  <text x="304" y="142" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Carbon-12</text>
  <text x="304" y="153" text-anchor="middle" font-size="7.5" fill="#6b7280">6 protons, 6 neutrons</text>
  <g stroke="{_INK}" stroke-width="0.5">
    <circle cx="396" cy="98" r="8" fill="{_RED}"/><circle cx="412" cy="98" r="8" fill="#9ca3af"/><circle cx="404" cy="110" r="8" fill="{_RED}"/><circle cx="404" cy="86" r="8" fill="#9ca3af"/><circle cx="388" cy="110" r="8" fill="{_RED}"/><circle cx="420" cy="110" r="8" fill="#9ca3af"/><circle cx="420" cy="86" r="8" fill="#9ca3af"/><circle cx="388" cy="86" r="8" fill="#9ca3af"/>
  </g>
  <text x="404" y="142" text-anchor="middle" font-size="9" font-weight="700" fill="{_INK}">Carbon-14</text>
  <text x="404" y="153" text-anchor="middle" font-size="7.5" fill="#6b7280">6 protons, 8 neutrons</text>
  <text x="235" y="186" text-anchor="middle" font-size="8.5" fill="#6b7280">Electrons set the charge (ion); neutrons set the mass (isotope); protons set the element's identity.</text>
</svg>'''


# --- Reactions: reactants to products --------------------------------------
_REACTANTS_PRODUCTS = f'''
<svg viewBox="0 0 470 214" role="img" aria-label="A chemical reaction where reactant molecules rearrange into product molecules" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">A Chemical Reaction: Reactants &#8594; Products</text>
  <g stroke="{_INK}" stroke-width="2">
    <line x1="44" y1="80" x2="64" y2="80"/><line x1="44" y1="130" x2="64" y2="130"/>
  </g>
  <g stroke="#9ca3af" stroke-width="0.6">
    <circle cx="40" cy="80" r="11" fill="#e5e7eb"/><circle cx="68" cy="80" r="11" fill="#e5e7eb"/>
    <circle cx="40" cy="130" r="12" fill="#86efac"/><circle cx="68" cy="130" r="12" fill="#86efac"/>
  </g>
  <text x="54" y="83" text-anchor="middle" font-size="8" fill="{_INK}">H</text><text x="54" y="84" text-anchor="middle" font-size="0"> </text>
  <text x="115" y="110" text-anchor="middle" font-size="22" font-weight="700" fill="{_INK}">+</text>
  <line x1="180" y1="105" x2="240" y2="105" stroke="{_INK}" stroke-width="2"/><polygon points="246,105 234,99 234,111" fill="{_INK}"/>
  <text x="210" y="98" text-anchor="middle" font-size="8.5" fill="#6b7280">yields</text>
  <g stroke="{_INK}" stroke-width="2"><line x1="300" y1="80" x2="320" y2="80"/><line x1="300" y1="130" x2="320" y2="130"/></g>
  <g stroke="#9ca3af" stroke-width="0.6">
    <circle cx="296" cy="80" r="11" fill="#e5e7eb"/><circle cx="324" cy="80" r="12" fill="#86efac"/>
    <circle cx="296" cy="130" r="11" fill="#e5e7eb"/><circle cx="324" cy="130" r="12" fill="#86efac"/>
  </g>
  <g font-size="11" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="55" y="168">Reactants</text><text x="345" y="168">Products</text>
  </g>
  <text x="235" y="194" text-anchor="middle" font-size="8.5" fill="#6b7280">Bonds break and re-form: the same atoms rearrange into new substances. Signs of a reaction include</text>
  <text x="235" y="207" text-anchor="middle" font-size="8.5" fill="#6b7280">a color change, bubbles/gas, a temperature change, light, or a solid (precipitate) forming.</text>
</svg>'''


# --- Reactions: conservation of mass (balance) -----------------------------
_CONSERVATION_MASS_BALANCE = f'''
<svg viewBox="0 0 470 226" role="img" aria-label="A balance showing the mass of reactants equals the mass of products" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Conservation of Mass</text>
  <line x1="100" y1="92" x2="370" y2="92" stroke="{_INK}" stroke-width="3"/>
  <polygon points="235,92 222,138 248,138" fill="#9ca3af" stroke="{_INK}" stroke-width="1"/>
  <line x1="235" y1="92" x2="235" y2="78" stroke="{_INK}" stroke-width="2"/>
  <g stroke="{_INK}" stroke-width="1"><line x1="120" y1="92" x2="120" y2="120"/><line x1="350" y1="92" x2="350" y2="120"/></g>
  <path d="M92,120 a28,12 0 0 0 56,0 Z" fill="#dbeafe" stroke="{_BLUE}" stroke-width="1.2"/>
  <path d="M322,120 a28,12 0 0 0 56,0 Z" fill="#dcfce7" stroke="{_GREEN}" stroke-width="1.2"/>
  <text x="120" y="116" text-anchor="middle" font-size="9" font-weight="700" fill="#1e40af">Reactants</text>
  <text x="120" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">10 g</text>
  <text x="350" y="116" text-anchor="middle" font-size="9" font-weight="700" fill="#15803d">Products</text>
  <text x="350" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="{_INK}">10 g</text>
  <text x="235" y="118" text-anchor="middle" font-size="16" font-weight="700" fill="{_INK}">=</text>
  <text x="235" y="194" text-anchor="middle" font-size="8.5" fill="#6b7280">Atoms are only rearranged, so the total mass before a reaction equals the total mass after</text>
  <text x="235" y="207" text-anchor="middle" font-size="8.5" fill="#6b7280">(in a closed system, where escaping gases are also counted).</text>
</svg>'''


# --- Reactions: balancing an equation --------------------------------------
_BALANCING_EQUATION = f'''
<svg viewBox="0 0 470 224" role="img" aria-label="The balanced equation 2 H2 plus O2 yields 2 H2O with equal atom counts on both sides" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="24" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Balancing an Equation</text>
  <text x="235" y="64" text-anchor="middle" font-size="20" font-weight="700" fill="{_INK}">2 H&#8322; + O&#8322; &#8594; 2 H&#8322;O</text>
  <g stroke="{_INK}" stroke-width="0.8">
    <rect x="120" y="92" width="230" height="92" fill="#ffffff"/>
    <line x1="120" y1="120" x2="350" y2="120"/><line x1="120" y1="152" x2="350" y2="152"/>
    <line x1="196" y1="92" x2="196" y2="184"/><line x1="273" y1="92" x2="273" y2="184"/>
  </g>
  <g font-size="11" font-weight="700" fill="{_INK}" text-anchor="middle">
    <text x="158" y="112">Atom</text><text x="234" y="112">Left</text><text x="311" y="112">Right</text>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="middle">
    <text x="158" y="142">H</text><text x="234" y="142">4</text><text x="311" y="142">4</text>
    <text x="158" y="174">O</text><text x="234" y="174">2</text><text x="311" y="174">2</text>
  </g>
  <text x="235" y="208" text-anchor="middle" font-size="8.5" fill="#6b7280">The same number of each atom appears on both sides. Balance with coefficients &#8212; never change subscripts.</text>
</svg>'''


# --- Reactions: common reaction types --------------------------------------
_REACTION_TYPES = f'''
<svg viewBox="0 0 470 220" role="img" aria-label="Three reaction types: synthesis, decomposition, and combustion" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Common Reaction Types</text>
  <g stroke-width="1.3">
    <rect x="20" y="36" width="430" height="50" rx="8" fill="#eff6ff" stroke="{_BLUE}"/>
    <rect x="20" y="92" width="430" height="50" rx="8" fill="#f0fdf4" stroke="{_GREEN}"/>
    <rect x="20" y="148" width="430" height="50" rx="8" fill="#fff7ed" stroke="#ea580c"/>
  </g>
  <text x="36" y="58" font-size="11" font-weight="700" fill="#1e40af">Synthesis</text>
  <text x="36" y="74" font-size="8" fill="#6b7280">two combine into one</text>
  <text x="250" y="68" font-size="13" font-weight="700" fill="{_INK}">A + B &#8594; AB</text>
  <text x="36" y="114" font-size="11" font-weight="700" fill="#15803d">Decomposition</text>
  <text x="36" y="130" font-size="8" fill="#6b7280">one breaks into two</text>
  <text x="250" y="124" font-size="13" font-weight="700" fill="{_INK}">AB &#8594; A + B</text>
  <text x="36" y="170" font-size="11" font-weight="700" fill="#b45309">Combustion</text>
  <text x="36" y="186" font-size="8" fill="#6b7280">a fuel burns in oxygen</text>
  <text x="270" y="180" font-size="12" font-weight="700" fill="{_INK}">fuel + O&#8322; &#8594; CO&#8322; + H&#8322;O</text>
  <text x="235" y="214" text-anchor="middle" font-size="8.5" fill="#6b7280">Synthesis builds up; decomposition breaks down; combustion burns a fuel with oxygen, releasing energy.</text>
</svg>'''


# --- Reactions: exothermic vs endothermic ----------------------------------
_EXOTHERMIC_ENDOTHERMIC = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="Energy diagrams for an exothermic reaction releasing energy and an endothermic reaction absorbing energy" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Energy in Reactions</text>
  <line x1="40" y1="44" x2="40" y2="180" stroke="{_AXIS}"/>
  <line x1="40" y1="180" x2="220" y2="180" stroke="{_AXIS}"/>
  <text x="20" y="112" font-size="9" fill="#6b7280" transform="rotate(-90 20 112)" text-anchor="middle">Energy</text>
  <path d="M55,90 C90,90 95,56 115,56 C140,56 150,140 200,140" fill="none" stroke="{_RED}" stroke-width="2.5"/>
  <line x1="55" y1="90" x2="200" y2="90" stroke="{_GRID}" stroke-dasharray="3 3"/>
  <line x1="205" y1="90" x2="205" y2="140" stroke="{_GREEN}" stroke-width="1.5"/><polygon points="205,142 201,132 209,132" fill="{_GREEN}"/>
  <text x="130" y="200" text-anchor="middle" font-size="10" font-weight="700" fill="#b91c1c">Exothermic</text>
  <text x="130" y="214" text-anchor="middle" font-size="8" fill="#6b7280">releases energy; products LOWER</text>
  <line x1="260" y1="44" x2="260" y2="180" stroke="{_AXIS}"/>
  <line x1="260" y1="180" x2="440" y2="180" stroke="{_AXIS}"/>
  <path d="M275,140 C310,140 318,52 340,52 C362,52 370,92 420,92" fill="none" stroke="{_BLUE}" stroke-width="2.5"/>
  <line x1="275" y1="140" x2="420" y2="140" stroke="{_GRID}" stroke-dasharray="3 3"/>
  <line x1="425" y1="140" x2="425" y2="92" stroke="{_GREEN}" stroke-width="1.5"/><polygon points="425,90 421,100 429,100" fill="{_GREEN}"/>
  <text x="350" y="200" text-anchor="middle" font-size="10" font-weight="700" fill="#1e40af">Endothermic</text>
  <text x="350" y="214" text-anchor="middle" font-size="8" fill="#6b7280">absorbs energy; products HIGHER</text>
  <text x="235" y="234" text-anchor="middle" font-size="8" fill="#6b7280">The hump is the activation energy &#8212; the push needed to start the reaction.</text>
</svg>'''


# --- Reactions: factors that change reaction rate --------------------------
_REACTION_RATE_FACTORS = f'''
<svg viewBox="0 0 470 220" role="img" aria-label="Four factors that speed up a reaction: temperature, concentration, surface area, and a catalyst" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">What Speeds Up a Reaction?</text>
  <g stroke-width="1.3">
    <rect x="18" y="36" width="210" height="70" rx="8" fill="#fef2f2" stroke="{_RED}"/>
    <rect x="242" y="36" width="210" height="70" rx="8" fill="#eff6ff" stroke="{_BLUE}"/>
    <rect x="18" y="116" width="210" height="70" rx="8" fill="#fefce8" stroke="#ca8a04"/>
    <rect x="242" y="116" width="210" height="70" rx="8" fill="#f0fdf4" stroke="{_GREEN}"/>
  </g>
  <g font-size="11" font-weight="700" fill="{_INK}">
    <text x="34" y="62">Higher temperature</text>
    <text x="258" y="62">Higher concentration</text>
    <text x="34" y="142">More surface area</text>
    <text x="258" y="142">A catalyst</text>
  </g>
  <g font-size="8.5" fill="#6b7280">
    <text x="34" y="82">particles move &amp; collide faster</text>
    <text x="258" y="82">more particles to collide</text>
    <text x="34" y="162">smaller pieces expose more</text>
    <text x="258" y="162">lowers the activation energy</text>
  </g>
  <g font-size="8.5" font-weight="700" fill="#15803d">
    <text x="34" y="96">&#8594; faster</text><text x="258" y="96">&#8594; faster</text>
    <text x="34" y="176">&#8594; faster</text><text x="258" y="176">&#8594; faster (and is not used up)</text>
  </g>
  <text x="235" y="210" text-anchor="middle" font-size="8.5" fill="#6b7280">Anything that makes particles collide more often, or more easily, speeds up the reaction.</text>
</svg>'''


# --- Energy: kinetic vs potential ------------------------------------------
_KINETIC_POTENTIAL = f'''
<svg viewBox="0 0 470 226" role="img" aria-label="A ball on a hill has potential energy at the top and kinetic energy at the bottom" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Kinetic &amp; Potential Energy</text>
  <path d="M50,70 C150,70 210,170 420,176" fill="none" stroke="#8a6230" stroke-width="3"/>
  <path d="M50,70 C150,70 210,170 420,176 L420,200 L50,200 Z" fill="#f3e8d8" opacity="0.6"/>
  <circle cx="58" cy="60" r="12" fill="{_BLUE}" stroke="#1e40af"/>
  <circle cx="418" cy="164" r="12" fill="{_RED}" stroke="#991b1b"/>
  <line x1="430" y1="164" x2="452" y2="164" stroke="{_RED}" stroke-width="2"/><polygon points="456,164 446,159 446,169" fill="{_RED}"/>
  <text x="58" y="40" text-anchor="middle" font-size="9" font-weight="700" fill="#1e40af">High PE</text>
  <text x="58" y="92" text-anchor="middle" font-size="8" fill="#6b7280">stored; not moving fast</text>
  <text x="412" y="138" text-anchor="middle" font-size="9" font-weight="700" fill="#b91c1c">High KE</text>
  <text x="410" y="196" text-anchor="middle" font-size="8" fill="#6b7280">moving fast</text>
  <g font-size="9" fill="{_INK}">
    <text x="150" y="120">Potential energy (PE) = stored energy</text>
    <text x="150" y="134" font-size="8" fill="#6b7280">(here, due to height)</text>
  </g>
  <text x="235" y="218" text-anchor="middle" font-size="8.5" fill="#6b7280">As the ball rolls down, stored potential energy is converted into kinetic energy (the energy of motion).</text>
</svg>'''


# --- Energy: forms of energy chart -----------------------------------------
_ENERGY_FORMS_CHART = f'''
<svg viewBox="0 0 470 240" role="img" aria-label="Eight forms of energy with an example of each" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Forms of Energy</text>
  <g stroke="{_INK}" stroke-width="0.8">
    <rect x="12" y="34" width="108" height="84" rx="8" fill="#eff6ff"/>
    <rect x="128" y="34" width="108" height="84" rx="8" fill="#fef2f2"/>
    <rect x="244" y="34" width="108" height="84" rx="8" fill="#f0fdf4"/>
    <rect x="360" y="34" width="98" height="84" rx="8" fill="#fefce8"/>
    <rect x="12" y="128" width="108" height="84" rx="8" fill="#f5f3ff"/>
    <rect x="128" y="128" width="108" height="84" rx="8" fill="#fff7ed"/>
    <rect x="244" y="128" width="108" height="84" rx="8" fill="#ecfeff"/>
    <rect x="360" y="128" width="98" height="84" rx="8" fill="#fdf2f8"/>
  </g>
  <g text-anchor="middle">
    <text x="66" y="66" font-size="11" font-weight="700" fill="#1e40af">Mechanical</text><text x="66" y="86" font-size="8" fill="#6b7280">a moving car</text><text x="66" y="100" font-size="8" fill="#6b7280">(motion + position)</text>
    <text x="182" y="66" font-size="11" font-weight="700" fill="#b91c1c">Thermal</text><text x="182" y="86" font-size="8" fill="#6b7280">heat from a fire</text><text x="182" y="100" font-size="8" fill="#6b7280">(particle motion)</text>
    <text x="298" y="66" font-size="11" font-weight="700" fill="#15803d">Chemical</text><text x="298" y="86" font-size="8" fill="#6b7280">food, fuel,</text><text x="298" y="100" font-size="8" fill="#6b7280">batteries</text>
    <text x="409" y="66" font-size="11" font-weight="700" fill="#b45309">Electrical</text><text x="409" y="86" font-size="8" fill="#6b7280">moving</text><text x="409" y="100" font-size="8" fill="#6b7280">charges</text>
    <text x="66" y="160" font-size="11" font-weight="700" fill="#6b21a8">Light</text><text x="66" y="180" font-size="8" fill="#6b7280">sunlight,</text><text x="66" y="194" font-size="8" fill="#6b7280">a lamp (radiant)</text>
    <text x="182" y="160" font-size="11" font-weight="700" fill="#ea580c">Sound</text><text x="182" y="180" font-size="8" fill="#6b7280">music,</text><text x="182" y="194" font-size="8" fill="#6b7280">a voice</text>
    <text x="298" y="160" font-size="11" font-weight="700" fill="#0891b2">Nuclear</text><text x="298" y="180" font-size="8" fill="#6b7280">the Sun;</text><text x="298" y="194" font-size="8" fill="#6b7280">power plants</text>
    <text x="409" y="160" font-size="11" font-weight="700" fill="#be185d">Elastic</text><text x="409" y="180" font-size="8" fill="#6b7280">a stretched</text><text x="409" y="194" font-size="8" fill="#6b7280">spring</text>
  </g>
  <text x="235" y="230" text-anchor="middle" font-size="8.5" fill="#6b7280">Energy comes in many forms &#8212; and one form can be changed into another.</text>
</svg>'''


# --- Energy: transformations -----------------------------------------------
_ENERGY_TRANSFORMATION = f'''
<svg viewBox="0 0 470 218" role="img" aria-label="Energy transformation chains in a flashlight, a car, and a toaster" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Energy Transformations</text>
  <text x="30" y="58" font-size="10" font-weight="700" fill="{_INK}">Flashlight</text>
  <g font-size="9.5" font-weight="700" text-anchor="middle">
    <rect x="120" y="44" width="78" height="24" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="159" y="60" fill="#15803d">Chemical</text>
    <rect x="232" y="44" width="78" height="24" rx="6" fill="#fefce8" stroke="#ca8a04"/><text x="271" y="60" fill="#b45309">Electrical</text>
    <rect x="344" y="44" width="78" height="24" rx="6" fill="#f5f3ff" stroke="#7c3aed"/><text x="383" y="60" fill="#6b21a8">Light</text>
  </g>
  <text x="62" y="98" font-size="10" font-weight="700" fill="{_INK}">Car engine</text>
  <g font-size="9.5" font-weight="700" text-anchor="middle">
    <rect x="120" y="84" width="78" height="24" rx="6" fill="#dcfce7" stroke="{_GREEN}"/><text x="159" y="100" fill="#15803d">Chemical</text>
    <rect x="232" y="84" width="120" height="24" rx="6" fill="#eff6ff" stroke="{_BLUE}"/><text x="292" y="100" fill="#1e40af">Kinetic (motion)</text>
  </g>
  <text x="58" y="138" font-size="10" font-weight="700" fill="{_INK}">Toaster</text>
  <g font-size="9.5" font-weight="700" text-anchor="middle">
    <rect x="120" y="124" width="78" height="24" rx="6" fill="#fefce8" stroke="#ca8a04"/><text x="159" y="140" fill="#b45309">Electrical</text>
    <rect x="232" y="124" width="120" height="24" rx="6" fill="#fef2f2" stroke="{_RED}"/><text x="292" y="140" fill="#b91c1c">Thermal (heat)</text>
  </g>
  <g stroke="{_AXIS}" stroke-width="1.6" fill="{_AXIS}">
    <line x1="198" y1="56" x2="230" y2="56"/><polygon points="234,56 224,51 224,61"/>
    <line x1="310" y1="56" x2="342" y2="56"/><polygon points="346,56 336,51 336,61"/>
    <line x1="198" y1="96" x2="230" y2="96"/><polygon points="234,96 224,91 224,101"/>
    <line x1="198" y1="136" x2="230" y2="136"/><polygon points="234,136 224,131 224,141"/>
  </g>
  <text x="235" y="186" text-anchor="middle" font-size="8.5" fill="#6b7280">Energy changes form along each chain. Some energy always escapes as 'waste' heat at each step.</text>
  <text x="235" y="200" text-anchor="middle" font-size="8.5" fill="#6b7280">(A solar panel runs it backward: light energy &#8594; electrical energy.)</text>
</svg>'''


# --- Energy: conservation of energy ----------------------------------------
_CONSERVATION_OF_ENERGY = f'''
<svg viewBox="0 0 470 232" role="img" aria-label="On a roller coaster, potential energy converts to kinetic energy while the total stays the same" xmlns="http://www.w3.org/2000/svg" style="max-width:580px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Conservation of Energy</text>
  <path d="M40,60 C120,60 150,170 235,170 C320,170 350,110 430,110" fill="none" stroke="#8a6230" stroke-width="3"/>
  <circle cx="44" cy="52" r="8" fill="#1f2937"/><circle cx="235" cy="162" r="8" fill="#1f2937"/><circle cx="426" cy="102" r="8" fill="#1f2937"/>
  <g stroke="{_INK}" stroke-width="0.5">
    <rect x="30" y="78" width="22" height="60" fill="{_BLUE}"/>
    <rect x="222" y="100" width="22" height="6" fill="{_BLUE}"/><rect x="222" y="106" width="22" height="54" fill="{_RED}"/>
    <rect x="414" y="100" width="22" height="36" fill="{_BLUE}"/><rect x="414" y="136" width="22" height="24" fill="{_RED}"/>
  </g>
  <g font-size="8" fill="{_INK}" text-anchor="middle">
    <text x="41" y="150">top</text><text x="233" y="174">bottom</text><text x="425" y="150">middle</text>
  </g>
  <g font-size="8.5">
    <rect x="120" y="196" width="12" height="9" fill="{_BLUE}"/><text x="138" y="204" fill="{_INK}">potential energy (PE)</text>
    <rect x="270" y="196" width="12" height="9" fill="{_RED}"/><text x="288" y="204" fill="{_INK}">kinetic energy (KE)</text>
  </g>
  <text x="235" y="224" text-anchor="middle" font-size="8.5" fill="#6b7280">PE turns into KE and back, but the TOTAL energy (each bar's height) stays the same.</text>
</svg>'''


# --- Energy: efficiency (energy flow) --------------------------------------
_ENERGY_EFFICIENCY = f'''
<svg viewBox="0 0 470 220" role="img" aria-label="An energy flow diagram: input energy splits into a small useful output and a large amount of wasted heat" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="235" y="22" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Energy Efficiency: a Light Bulb</text>
  <rect x="30" y="80" width="120" height="80" fill="#fefce8" stroke="#ca8a04" stroke-width="1.5"/>
  <text x="90" y="116" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309">Input</text>
  <text x="90" y="134" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">100 J</text>
  <text x="90" y="148" text-anchor="middle" font-size="8" fill="#6b7280">electrical</text>
  <polygon points="150,90 250,96 250,108 150,104" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1"/>
  <text x="300" y="100" text-anchor="middle" font-size="10" font-weight="700" fill="#6b21a8">10 J useful (light)</text>
  <polygon points="150,110 250,124 250,176 150,152" fill="#fee2e2" stroke="{_RED}" stroke-width="1"/>
  <text x="300" y="156" text-anchor="middle" font-size="10" font-weight="700" fill="#b91c1c">90 J wasted (heat)</text>
  <text x="235" y="196" text-anchor="middle" font-size="9" fill="#6b7280">Efficiency = useful out &#247; total in = 10 &#247; 100 = 10%. The 'wasted' energy isn't destroyed &#8212; it spreads as heat.</text>
</svg>'''


# --- Data & Probability: Bar graph sales ----------------------------------------
_BAR_GRAPH_SALES = f'''
<svg viewBox="0 0 480 300" role="img" aria-label="Horizontal bar graph of monthly sales data for four products" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="240" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Monthly Sales by Product</text>
  <line x1="100" y1="50" x2="100" y2="280" stroke="{_AXIS}" stroke-width="2"/>
  <line x1="100" y1="280" x2="460" y2="280" stroke="{_AXIS}" stroke-width="2"/>
  <g font-size="10" fill="#6b7280">
    <line x1="100" y1="276" x2="100" y2="284"/><text x="95" y="295" text-anchor="end">$0k</text>
    <line x1="155" y1="276" x2="155" y2="284"/><text x="150" y="295" text-anchor="end">$5k</text>
    <line x1="210" y1="276" x2="210" y2="284"/><text x="205" y="295" text-anchor="end">$10k</text>
    <line x1="265" y1="276" x2="265" y2="284"/><text x="260" y="295" text-anchor="end">$15k</text>
    <line x1="320" y1="276" x2="320" y2="284"/><text x="315" y="295" text-anchor="end">$20k</text>
    <line x1="375" y1="276" x2="375" y2="284"/><text x="370" y="295" text-anchor="end">$25k</text>
    <line x1="430" y1="276" x2="430" y2="284"/><text x="425" y="295" text-anchor="end">$30k</text>
  </g>
  <g stroke="{_GRID}" stroke-width="1" stroke-dasharray="2,2">
    <line x1="155" y1="50" x2="155" y2="280"/><line x1="210" y1="50" x2="210" y2="280"/>
    <line x1="265" y1="50" x2="265" y2="280"/><line x1="320" y1="50" x2="320" y2="280"/>
    <line x1="375" y1="50" x2="375" y2="280"/><line x1="430" y1="50" x2="430" y2="280"/>
  </g>
  <g fill="{_BLUE}">
    <rect x="100" y="70" width="310" height="35" rx="3"/>
    <rect x="100" y="120" width="235" height="35" rx="3"/>
    <rect x="100" y="170" width="280" height="35" rx="3"/>
    <rect x="100" y="220" width="190" height="35" rx="3"/>
  </g>
  <g font-size="11" fill="{_INK}" font-weight="700">
    <text x="315" y="93">$31k</text><text x="240" y="143">$24k</text>
    <text x="285" y="193">$28k</text><text x="195" y="243">$19k</text>
  </g>
  <g font-size="11" fill="{_INK}" text-anchor="end">
    <text x="95" y="93">Product A</text><text x="95" y="143">Product B</text>
    <text x="95" y="193">Product C</text><text x="95" y="243">Product D</text>
  </g>
</svg>'''

# --- Data & Probability: Line graph temperature --------------------------------
_LINE_GRAPH_TEMPERATURE = f'''
<svg viewBox="0 0 480 300" role="img" aria-label="Line graph of daily temperature throughout the week" xmlns="http://www.w3.org/2000/svg" style="max-width:560px;width:100%;height:auto;{_FONT}">
  <text x="240" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Daily Temperature This Week</text>
  <line x1="60" y1="40" x2="60" y2="250" stroke="{_AXIS}" stroke-width="2"/>
  <line x1="60" y1="250" x2="450" y2="250" stroke="{_AXIS}" stroke-width="2"/>
  <g font-size="10" fill="#6b7280">
    <line x1="55" y1="248" x2="65" y2="248"/><text x="50" y="252" text-anchor="end" font-size="9">50°</text>
    <line x1="55" y1="200" x2="65" y2="200"/><text x="50" y="204" text-anchor="end" font-size="9">60°</text>
    <line x1="55" y1="152" x2="65" y2="152"/><text x="50" y="156" text-anchor="end" font-size="9">70°</text>
    <line x1="55" y1="104" x2="65" y2="104"/><text x="50" y="108" text-anchor="end" font-size="9">80°</text>
    <line x1="55" y1="56" x2="65" y2="56"/><text x="50" y="60" text-anchor="end" font-size="9">90°</text>
  </g>
  <polyline points="90,134 155,112 220,90 285,102 350,128 415,156 450,188" stroke="{_BLUE}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <g fill="{_BLUE}" r="4">
    <circle cx="90" cy="134" r="4"/><circle cx="155" cy="112" r="4"/><circle cx="220" cy="90" r="4"/>
    <circle cx="285" cy="102" r="4"/><circle cx="350" cy="128" r="4"/><circle cx="415" cy="156" r="4"/><circle cx="450" cy="188" r="4"/>
  </g>
  <g font-size="10" fill="{_INK}" text-anchor="middle">
    <text x="90" y="270">Mon</text><text x="155" y="270">Tue</text><text x="220" y="270">Wed</text>
    <text x="285" y="270">Thu</text><text x="350" y="270">Fri</text><text x="415" y="270">Sat</text><text x="450" y="270">Sun</text>
  </g>
</svg>'''

# --- Data & Probability: Pie chart budget ----------------------------------------
_PIE_CHART_BUDGET = f'''
<svg viewBox="0 0 560 340" role="img" aria-label="Pie chart showing monthly budget breakdown by category" xmlns="http://www.w3.org/2000/svg" style="max-width:640px;width:100%;height:auto;{_FONT}">
  <text x="280" y="22" text-anchor="middle" font-size="15" font-weight="700" fill="{_INK}">Monthly Budget Breakdown ($2,000)</text>

  <!-- Pie Chart centered at (180,160) r=100. Angles clockwise from 12 o'clock.
       Endpoint formula: x=r·sin(θ), y=-r·cos(θ)
       0°→(0,-100)  126°→(80.9,58.78)  216°→(-58.78,80.9)
       280.8°→(-98.23,-18.74)  324°→(-58.78,-80.9) -->
  <g transform="translate(180, 160)">
    <!-- Housing 35% (0° → 126°) -->
    <path d="M 0,-100 A 100,100 0 0,1 80.9,58.78 L 0,0 Z" fill="#2563eb" stroke="white" stroke-width="2"/>
    <!-- Food 25% (126° → 216°) -->
    <path d="M 80.9,58.78 A 100,100 0 0,1 -58.78,80.9 L 0,0 Z" fill="#059669" stroke="white" stroke-width="2"/>
    <!-- Transportation 18% (216° → 280.8°) -->
    <path d="M -58.78,80.9 A 100,100 0 0,1 -98.23,-18.74 L 0,0 Z" fill="#f59e0b" stroke="white" stroke-width="2"/>
    <!-- Utilities 12% (280.8° → 324°) -->
    <path d="M -98.23,-18.74 A 100,100 0 0,1 -58.78,-80.9 L 0,0 Z" fill="#dc2626" stroke="white" stroke-width="2"/>
    <!-- Entertainment 10% (324° → 360°) -->
    <path d="M -58.78,-80.9 A 100,100 0 0,1 0,-100 L 0,0 Z" fill="#8b5cf6" stroke="white" stroke-width="2"/>
  </g>

  <!-- Labels at 65% radius, at midpoint angle of each slice.
       SVG coords = center(180,160) + (65·sin(mid), -65·cos(mid)) -->
  <g font-size="12" font-weight="700" text-anchor="middle" fill="white">
    <!-- Housing mid 63°:  (238, 131) -->
    <text x="238" y="135">35%</text>
    <!-- Food mid 171°:    (190, 224) -->
    <text x="190" y="224">25%</text>
    <!-- Transportation mid 248.4°: (120, 184) -->
    <text x="120" y="184">18%</text>
    <!-- Utilities mid 302.4°: (125, 125) -->
    <text x="125" y="125">12%</text>
    <!-- Entertainment mid 342°: (160, 98) -->
    <text x="160" y="98">10%</text>
  </g>

  <!-- Legend -->
  <g font-size="12" fill="{_INK}">
    <rect x="340" y="110" width="16" height="16" fill="#2563eb" rx="2"/>
    <text x="365" y="123" font-weight="600">Housing (35% = $700)</text>
    <rect x="340" y="138" width="16" height="16" fill="#059669" rx="2"/>
    <text x="365" y="151" font-weight="600">Food (25% = $500)</text>
    <rect x="340" y="166" width="16" height="16" fill="#f59e0b" rx="2"/>
    <text x="365" y="179" font-weight="600">Transportation (18% = $360)</text>
    <rect x="340" y="194" width="16" height="16" fill="#dc2626" rx="2"/>
    <text x="365" y="207" font-weight="600">Utilities (12% = $240)</text>
    <rect x="340" y="222" width="16" height="16" fill="#8b5cf6" rx="2"/>
    <text x="365" y="235" font-weight="600">Entertainment (10% = $200)</text>
  </g>

  <text x="280" y="320" text-anchor="middle" font-size="11" fill="#6b7280">Total: 100% = $2,000</text>
</svg>'''

# --- Data & Probability: Normal distribution -----------------------------------
_NORMAL_DISTRIBUTION = f'''
<svg viewBox="0 0 500 280" role="img" aria-label="Bell curve showing normal distribution" xmlns="http://www.w3.org/2000/svg" style="max-width:600px;width:100%;height:auto;{_FONT}">
  <text x="250" y="20" text-anchor="middle" font-size="14" font-weight="700" fill="{_INK}">Normal Distribution (Bell Curve)</text>
  <line x1="50" y1="220" x2="450" y2="220" stroke="{_AXIS}" stroke-width="2"/>
  <g font-size="10" fill="#6b7280" text-anchor="middle">
    <line x1="50" y1="216" x2="50" y2="224"/><text x="50" y="240">-3σ</text>
    <line x1="100" y1="216" x2="100" y2="224"/><text x="100" y="240">-2σ</text>
    <line x1="150" y1="216" x2="150" y2="224"/><text x="150" y="240">-1σ</text>
    <line x1="250" y1="216" x2="250" y2="224"/><text x="250" y="240">μ</text>
    <line x1="350" y1="216" x2="350" y2="224"/><text x="350" y="240">+1σ</text>
    <line x1="400" y1="216" x2="400" y2="224"/><text x="400" y="240">+2σ</text>
    <line x1="450" y1="216" x2="450" y2="224"/><text x="450" y="240">+3σ</text>
  </g>
  <path d="M 50 220 Q 100 150 150 80 Q 200 20 250 15 Q 300 20 350 80 Q 400 150 450 220" stroke="{_BLUE}" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M 150 220 L 150 80 M 350 220 L 350 80" stroke="{_BLUE}" stroke-width="1" stroke-dasharray="2,2" opacity="0.5"/>
  <text x="250" y="60" text-anchor="middle" font-size="10" fill="{_BLUE}" font-weight="700">68% within 1σ</text>
</svg>'''

# --- Data & Probability: Skewed distributions ---------------------------------
_SKEWED_DISTRIBUTIONS = f'''
<svg viewBox="0 0 520 280" role="img" aria-label="Two histograms showing right-skewed and left-skewed distributions" xmlns="http://www.w3.org/2000/svg" style="max-width:620px;width:100%;height:auto;{_FONT}">
  <text x="130" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">Right-Skewed</text>
  <text x="390" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="{_INK}">Left-Skewed</text>
  <g fill="{_BLUE}" opacity="0.8">
    <rect x="25" y="140" width="20" height="90"/><rect x="48" y="110" width="20" height="120"/>
    <rect x="71" y="90" width="20" height="140"/><rect x="94" y="80" width="20" height="150"/>
    <rect x="117" y="100" width="20" height="130"/><rect x="140" y="130" width="20" height="100"/>
    <rect x="163" y="160" width="20" height="70"/>
    <rect x="285" y="160" width="20" height="70"/><rect x="308" y="130" width="20" height="100"/>
    <rect x="331" y="100" width="20" height="130"/><rect x="354" y="80" width="20" height="150"/>
    <rect x="377" y="90" width="20" height="140"/><rect x="400" y="110" width="20" height="120"/>
    <rect x="423" y="140" width="20" height="90"/>
  </g>
  <line x1="20" y1="230" x2="190" y2="230" stroke="{_AXIS}" stroke-width="2"/>
  <line x1="280" y1="230" x2="450" y2="230" stroke="{_AXIS}" stroke-width="2"/>
  <text x="130" y="260" text-anchor="middle" font-size="9" fill="#6b7280" font-weight="700">Mean > Median</text>
  <text x="365" y="260" text-anchor="middle" font-size="9" fill="#6b7280" font-weight="700">Mean < Median</text>
</svg>'''


FIGURES = {
    "sat_rw_roadmap": _SAT_RW_ROADMAP,
    "transition_words": _TRANSITION_WORDS,
    "bar_recycling": _BAR_RECYCLING,
    "line_solar": _LINE_SOLAR,
    "scientific_method": _SCIENTIFIC_METHOD,
    "controlled_experiment": _CONTROLLED_EXPERIMENT,
    "argument": _ARGUMENT,
    "essay_structure": _ESSAY_STRUCTURE,
    "three_branches": _THREE_BRANCHES,
    "supply_demand": _SUPPLY_DEMAND,
    "bill_to_law": _BILL_TO_LAW,
    "us_timeline": _US_TIMELINE,
    "bar_toppings": _BAR_TOPPINGS,
    "line_sales": _LINE_SALES,
    "mean_bars": _MEAN_BARS,
    "prob_scale": _PROB_SCALE,
    "coin_tree": _COIN_TREE,
    "dot_plot_scores": _DOT_PLOT_SCORES,
    "histogram_commute": _HISTOGRAM_COMMUTE,
    "two_way_table": _TWO_WAY_TABLE,
    "misleading_scale": _MISLEADING_SCALE,
    "number_line_ineq": _NUMBER_LINE_INEQ,
    "coord_line": _COORD_LINE,
    "parabola": _PARABOLA,
    "expression_anatomy": _EXPRESSION_ANATOMY,
    "distributive_area_model": _DISTRIBUTIVE_AREA_MODEL,
    "polynomial_degree": _POLYNOMIAL_DEGREE,
    "factoring_trinomial": _FACTORING_TRINOMIAL,
    "rational_expression_restriction": _RATIONAL_EXPRESSION_RESTRICTION,
    "function_table_line": _FUNCTION_TABLE_LINE,
    "slope_types": _SLOPE_TYPES,
    "linear_inequality_shade": _LINEAR_INEQUALITY_SHADE,
    "cell_animal": _CELL_ANIMAL,
    "energy_cycle": _ENERGY_CYCLE,
    "punnett_square": _PUNNETT,
    "food_chain": _FOOD_CHAIN,
    "energy_pyramid": _ENERGY_PYRAMID,
    "ged_math_roadmap": _GED_MATH_ROADMAP,
    "place_value_ladder": _PLACE_VALUE_LADDER,
    "integer_number_line": _INTEGER_NUMBER_LINE,
    "signed_operation_rules": _SIGNED_OPERATION_RULES,
    "absolute_value_distance_model": _ABSOLUTE_VALUE_DISTANCE_MODEL,
    "order_operations_stack": _ORDER_OPERATIONS_STACK,
    "formula_substitution_flow": _FORMULA_SUBSTITUTION_FLOW,
    "gcf_lcm_factor_map": _GCF_LCM_FACTOR_MAP,
    "scientific_notation_ladder": _SCIENTIFIC_NOTATION_LADDER,
    "unit_conversion_bridge": _UNIT_CONVERSION_BRIDGE,
    "fraction_percent_bar": _FRACTION_PERCENT_BAR,
    "fraction_circle": _FRACTION_CIRCLE,
    "equivalent_fraction_strips": _EQUIVALENT_FRACTION_STRIPS,
    "common_denominator_bars": _COMMON_DENOMINATOR_BARS,
    "fraction_operation_map": _FRACTION_OPERATION_MAP,
    "percent_grid": _PERCENT_GRID,
    "percent_conversion": _PERCENT_CONVERSION,
    "percent_discount_bar": _PERCENT_DISCOUNT_BAR,
    "percent_change_arrow": _PERCENT_CHANGE_ARROW,
    "percent_equation_triangle": _PERCENT_EQUATION_TRIANGLE,
    "rate_double_number_line": _RATE_DOUBLE_NUMBER_LINE,
    "unit_price_comparison": _UNIT_PRICE_COMPARISON,
    "rate_distance_triangle": _RATE_DISTANCE_TRIANGLE,
    "rate_graph": _RATE_GRAPH,
    "work_rate_bars": _WORK_RATE_BARS,
    "ratio_tape": _RATIO_TAPE,
    "proportion_cross_products": _PROPORTION_CROSS_PRODUCTS,
    "map_scale_distance": _MAP_SCALE_DISTANCE,
    "similar_rectangles_scale": _SIMILAR_RECTANGLES_SCALE,
    "equation_balance": _EQUATION_BALANCE,
    "composite_area": _COMPOSITE_AREA,
    "cylinder_volume": _CYLINDER_VOLUME,
    "area_unit_grid": _AREA_UNIT_GRID,
    "area_rectangle": _AREA_RECTANGLE,
    "area_triangle": _AREA_TRIANGLE,
    "area_parallelogram": _AREA_PARALLELOGRAM,
    "area_trapezoid": _AREA_TRAPEZOID,
    "area_circle": _AREA_CIRCLE,
    "perimeter_rectangle": _PERIMETER_RECTANGLE,
    "perimeter_triangle": _PERIMETER_TRIANGLE,
    "perimeter_polygon": _PERIMETER_POLYGON,
    "circle_circumference": _CIRCLE_CIRCUMFERENCE,
    "perimeter_composite": _PERIMETER_COMPOSITE,
    "volume_box": _VOLUME_BOX,
    "volume_cube": _VOLUME_CUBE,
    "volume_cone": _VOLUME_CONE,
    "volume_sphere": _VOLUME_SPHERE,
    "surface_net": _SURFACE_NET,
    "surface_cylinder": _SURFACE_CYLINDER,
    "angle_types": _ANGLE_TYPES,
    "comp_supp": _COMP_SUPP,
    "vertical_angles": _VERTICAL_ANGLES,
    "parallel_transversal": _PARALLEL_TRANSVERSAL,
    "triangle_types_sides": _TRIANGLE_TYPES_SIDES,
    "triangle_angle_sum": _TRIANGLE_ANGLE_SUM,
    "exterior_angle": _EXTERIOR_ANGLE,
    "pythagorean_triangle": _PYTHAGOREAN_TRIANGLE,
    "right_triangle_345": _RIGHT_TRIANGLE_345,
    "coordinate_quadrants": _COORDINATE_QUADRANTS,
    "distance_on_grid": _DISTANCE_ON_GRID,
    "midpoint_grid": _MIDPOINT_GRID,
    "box_plot": _BOX_PLOT,
    "scatter_trend": _SCATTER_TREND,
    "function_machine": _FUNCTION_MACHINE,
    "states_of_matter": _STATES_OF_MATTER,
    "atom_structure": _ATOM_STRUCTURE,
    "periodic_table_guide": _PERIODIC_TABLE_GUIDE,
    "conservation_mass": _CONSERVATION_MASS,
    "energy_forms": _ENERGY_FORMS,
    "newton_second_law": _NEWTON_SECOND_LAW,
    "lever_machine": _LEVER_MACHINE,
    "wave_anatomy": _WAVE_ANATOMY,
    "earth_layers": _EARTH_LAYERS,
    "earth_interior_scale": _EARTH_INTERIOR_SCALE,
    "seismic_waves": _SEISMIC_WAVES,
    "lithosphere_asthenosphere": _LITHOSPHERE_ASTHENOSPHERE,
    "geomagnetic_field": _GEOMAGNETIC_FIELD,
    "continental_drift": _CONTINENTAL_DRIFT,
    "mantle_convection": _MANTLE_CONVECTION,
    "seafloor_spreading": _SEAFLOOR_SPREADING,
    "convergent_boundary": _CONVERGENT_BOUNDARY,
    "transform_boundary": _TRANSFORM_BOUNDARY,
    "ring_of_fire": _RING_OF_FIRE,
    "hotspot": _HOTSPOT,
    "mohs_hardness": _MOHS_HARDNESS,
    "igneous_textures": _IGNEOUS_TEXTURES,
    "sedimentary_layers": _SEDIMENTARY_LAYERS,
    "metamorphic_change": _METAMORPHIC_CHANGE,
    "rock_cycle_detailed": _ROCK_CYCLE_DETAILED,
    "rock_classes": _ROCK_CLASSES,
    "water_distribution": _WATER_DISTRIBUTION,
    "water_cycle_detailed": _WATER_CYCLE_DETAILED,
    "water_phase_changes": _WATER_PHASE_CHANGES,
    "cloud_formation": _CLOUD_FORMATION,
    "groundwater_aquifer": _GROUNDWATER_AQUIFER,
    "atmosphere_composition": _ATMOSPHERE_COMPOSITION,
    "atmosphere_layers_detailed": _ATMOSPHERE_LAYERS_DETAILED,
    "heat_transfer": _HEAT_TRANSFER,
    "pressure_wind": _PRESSURE_WIND,
    "weather_fronts": _WEATHER_FRONTS,
    "greenhouse_effect": _GREENHOUSE_EFFECT,
    "sun_anatomy": _SUN_ANATOMY,
    "solar_system_layout": _SOLAR_SYSTEM_LAYOUT,
    "orbit_gravity": _ORBIT_GRAVITY,
    "terrestrial_planets": _TERRESTRIAL_PLANETS,
    "outer_planets": _OUTER_PLANETS,
    "comet_anatomy": _COMET_ANATOMY,
    "cosmic_scale": _COSMIC_SCALE,
    "earth_rotation_revolution": _EARTH_ROTATION_REVOLUTION,
    "moon_overview": _MOON_OVERVIEW,
    "moon_phases_detailed": _MOON_PHASES_DETAILED,
    "eclipses": _ECLIPSES,
    "seasons_detailed": _SEASONS_DETAILED,
    "tides": _TIDES,
    "cell_discovery_timeline": _CELL_DISCOVERY_TIMELINE,
    "prokaryote_eukaryote": _PROKARYOTE_EUKARYOTE,
    "eukaryotic_cell_detailed": _EUKARYOTIC_CELL_DETAILED,
    "plant_vs_animal_cell": _PLANT_VS_ANIMAL_CELL,
    "membrane_transport": _MEMBRANE_TRANSPORT,
    "cell_cycle": _CELL_CYCLE,
    "atp_adp_cycle": _ATP_ADP_CYCLE,
    "photosynthesis_overview": _PHOTOSYNTHESIS_OVERVIEW,
    "respiration_overview": _RESPIRATION_OVERVIEW,
    "photo_resp_link": _PHOTO_RESP_LINK,
    "fermentation_paths": _FERMENTATION_PATHS,
    "photosynthesis_rate_graph": _PHOTOSYNTHESIS_RATE_GRAPH,
    "dna_double_helix": _DNA_DOUBLE_HELIX,
    "dna_gene_chromosome": _DNA_GENE_CHROMOSOME,
    "dominant_recessive": _DOMINANT_RECESSIVE,
    "punnett_square_worked": _PUNNETT_SQUARE_WORKED,
    "mitosis_vs_meiosis": _MITOSIS_VS_MEIOSIS,
    "pedigree_chart": _PEDIGREE_CHART,
    "variation_in_population": _VARIATION_IN_POPULATION,
    "natural_selection_cycle": _NATURAL_SELECTION_CYCLE,
    "antibiotic_resistance": _ANTIBIOTIC_RESISTANCE,
    "homologous_structures": _HOMOLOGOUS_STRUCTURES,
    "cladogram": _CLADOGRAM,
    "speciation": _SPECIATION,
    "ecosystem_levels": _ECOSYSTEM_LEVELS,
    "food_web": _FOOD_WEB,
    "energy_pyramid_detailed": _ENERGY_PYRAMID_DETAILED,
    "carbon_cycle": _CARBON_CYCLE,
    "carrying_capacity_graph": _CARRYING_CAPACITY_GRAPH,
    "symbiosis_types": _SYMBIOSIS_TYPES,
    "predator_prey_graph": _PREDATOR_PREY_GRAPH,
    "body_organization": _BODY_ORGANIZATION,
    "organ_systems": _ORGAN_SYSTEMS,
    "oxygen_delivery": _OXYGEN_DELIVERY,
    "neuron_reflex": _NEURON_REFLEX,
    "nutrition_chart": _NUTRITION_CHART,
    "disease_transmission": _DISEASE_TRANSMISSION,
    "feedback_loop": _FEEDBACK_LOOP,
    "thermoregulation": _THERMOREGULATION,
    "stomata": _STOMATA,
    "blood_glucose_graph": _BLOOD_GLUCOSE_GRAPH,
    "experiment_variables": _EXPERIMENT_VARIABLES,
    "correlation_causation": _CORRELATION_CAUSATION,
    "particle_model": _PARTICLE_MODEL,
    "phase_change_diagram": _PHASE_CHANGE_DIAGRAM,
    "heating_curve": _HEATING_CURVE,
    "density_compare": _DENSITY_COMPARE,
    "physical_vs_chemical": _PHYSICAL_VS_CHEMICAL,
    "mixtures_solutions": _MIXTURES_SOLUTIONS,
    "atom_anatomy": _ATOM_ANATOMY,
    "atomic_number_mass": _ATOMIC_NUMBER_MASS,
    "bohr_models": _BOHR_MODELS,
    "periodic_table_map": _PERIODIC_TABLE_MAP,
    "element_vs_compound": _ELEMENT_VS_COMPOUND,
    "ions_isotopes": _IONS_ISOTOPES,
    "reactants_products": _REACTANTS_PRODUCTS,
    "conservation_mass_balance": _CONSERVATION_MASS_BALANCE,
    "balancing_equation": _BALANCING_EQUATION,
    "reaction_types": _REACTION_TYPES,
    "exothermic_endothermic": _EXOTHERMIC_ENDOTHERMIC,
    "reaction_rate_factors": _REACTION_RATE_FACTORS,
    "tectonic_boundaries": _TECTONIC_BOUNDARIES,
    "rock_cycle": _ROCK_CYCLE,
    "water_cycle": _WATER_CYCLE,
    "atmosphere_layers": _ATMOSPHERE_LAYERS,
    "solar_system": _SOLAR_SYSTEM,
    "moon_phases": _MOON_PHASES,
    "seasons": _SEASONS,
    "system_graph": _SYSTEM_GRAPH,
    "systems_substitution_flow": _SYSTEMS_SUBSTITUTION_FLOW,
    "systems_elimination_balance": _SYSTEMS_ELIMINATION_BALANCE,
    "break_even_model_graph": _BREAK_EVEN_MODEL_GRAPH,
    "exponential_growth": _EXPONENTIAL_GROWTH,
    "bar_graph_sales": _BAR_GRAPH_SALES,
    "line_graph_temperature": _LINE_GRAPH_TEMPERATURE,
    "pie_chart_budget": _PIE_CHART_BUDGET,
    "normal_distribution": _NORMAL_DISTRIBUTION,
    "skewed_distributions": _SKEWED_DISTRIBUTIONS,
}
