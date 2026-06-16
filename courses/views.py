from django.contrib.auth import login
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import Course


MATH_TOPIC_GROUPS = [
    {
        "value": "foundations",
        "label": "Foundations",
        "description": (
            "Number sense, signed and rational operations, formula skills, fractions, "
            "percents, ratios, rates, and unit thinking."
        ),
        "slugs": {
            "ged-math-dasar",
            "ged-number-sense-measurement",
            "ged-integer-rational-operations",
            "ged-order-operations-formula-skills",
            "ged-basic-math-fractions-mastery",
            "ged-basic-math-percents-mastery",
            "ged-ratios-proportions-scale",
            "ged-basic-math-rates-mastery",
            "ged-fractions-decimals-percents",
        },
    },
    {
        "value": "algebra",
        "label": "Algebra",
        "description": "Expressions, polynomials, equations, inequalities, functions, systems, and applications.",
        "slugs": {
            "sat-ged-algebra-essentials",
            "ged-algebra-in-depth",
            "ged-algebra-expressions-polynomials",
            "ged-algebra-equations-mastery",
            "ged-algebra-inequalities-mastery",
            "ged-algebra-functions-graphs",
            "ged-algebra-systems-linear-modeling",
            "ged-algebra-advanced-equations",
            "ged-algebra-advanced-inequalities",
            "sat-math-algebra",
        },
    },
    {
        "value": "advanced-math",
        "label": "Advanced Math",
        "description": "Quadratics, polynomials, radicals, rational expressions, exponential functions, and function transformations.",
        "slugs": {
            "sat-math-advanced-math",
        },
    },
    {
        "value": "geometry",
        "label": "Geometry",
        "description": "Area, perimeter, volume, angles, triangles, coordinate geometry, and trigonometric ratios.",
        "slugs": {
            "ged-geometry-measurement",
            "ged-geometry-area-mastery",
            "ged-geometry-perimeter-mastery",
            "ged-geometry-volume-mastery",
            "ged-geometry-angles-triangles",
            "ged-geometry-right-triangles",
            "ged-geometry-pythagorean-coordinate",
            "ged-geometry-mixed-review",
            "sat-math-geometry-trig",
        },
    },
    {
        "value": "data",
        "label": "Data & Probability",
        "description": "Statistics, probability, graphs, tables, data interpretation, and quantitative reasoning.",
        "slugs": {
            "ged-data-stats-probability",
            "ged-data-analysis-probability-mastery",
            "sat-math-problem-solving",
        },
    },
    {
        "value": "complete-review",
        "label": "Complete Review",
        "description": "Full-course review and mixed test-prep paths.",
        "slugs": {
            "ged-math-complete-course",
            "sat-math-complete-course",
        },
    },
    {
        "value": "practice-exams",
        "label": "Full-Length Practice Exams",
        "description": (
            "Timed, test-day-style GED Mathematical Reasoning exams — 46 questions each, with the real "
            "no-calculator and calculator sections — in five difficulty tiers, from foundational (Level 1) "
            "to elite (Level 5)."
        ),
        "slugs": {
            "ged-math-reasoning-exam",
            "ged-math-reasoning-exam-level2",
            "ged-math-reasoning-exam-level3",
            "ged-math-reasoning-exam-level4",
            "ged-math-reasoning-exam-level5",
        },
    },
]

MATH_FALLBACK_GROUP = {
    "value": "more-math",
    "label": "More Math",
    "description": "Additional math courses and mixed review topics.",
    "slugs": set(),
}

MATH_COURSE_ORDER = {
    "ged-math-dasar": 10,
    "ged-number-sense-measurement": 20,
    "ged-integer-rational-operations": 25,
    "ged-order-operations-formula-skills": 28,
    "ged-basic-math-fractions-mastery": 30,
    "ged-fractions-decimals-percents": 40,
    "ged-basic-math-percents-mastery": 50,
    "ged-ratios-proportions-scale": 60,
    "ged-basic-math-rates-mastery": 70,
    "sat-ged-algebra-essentials": 110,
    "ged-algebra-expressions-polynomials": 120,
    "ged-algebra-equations-mastery": 130,
    "ged-algebra-inequalities-mastery": 140,
    "ged-algebra-functions-graphs": 150,
    "ged-algebra-systems-linear-modeling": 155,
    "ged-algebra-in-depth": 160,
    "ged-algebra-advanced-equations": 170,
    "ged-algebra-advanced-inequalities": 180,
    "ged-geometry-measurement": 210,
    "ged-geometry-angles-triangles": 220,
    "ged-geometry-area-mastery": 230,
    "ged-geometry-perimeter-mastery": 240,
    "ged-geometry-volume-mastery": 250,
    "ged-geometry-right-triangles": 260,
    "ged-geometry-pythagorean-coordinate": 270,
    "ged-geometry-mixed-review": 280,
    "ged-data-stats-probability": 310,
    "ged-data-analysis-probability-mastery": 320,
    "sat-math-algebra": 116,
    "sat-math-advanced-math": 190,
    "sat-math-geometry-trig": 215,
    "sat-math-problem-solving": 325,
    "ged-math-complete-course": 410,
    "sat-math-complete-course": 420,
    "ged-math-reasoning-exam": 510,
    "ged-math-reasoning-exam-level2": 520,
    "ged-math-reasoning-exam-level3": 530,
    "ged-math-reasoning-exam-level4": 540,
    "ged-math-reasoning-exam-level5": 550,
}


# ---------------------------------------------------------------------------
# Science topic groups
# ---------------------------------------------------------------------------
SCIENCE_TOPIC_GROUPS = [
    {
        "value": "life-science",
        "label": "Life Science",
        "description": "Cells, genetics, evolution, ecosystems, the human body, and homeostasis.",
        "slugs": {
            "ged-life-science",
            "ged-cell-biology",
            "ged-cellular-energy",
            "ged-genetics-heredity",
            "ged-evolution-natural-selection",
            "ged-ecosystems-energy-flow",
            "ged-human-body-health",
            "ged-homeostasis-data",
        },
    },
    {
        "value": "physical-science",
        "label": "Physical Science",
        "description": "Matter, atoms, chemical reactions, energy, forces, motion, machines, and waves.",
        "slugs": {
            "ged-physical-science",
            "ged-matter-states",
            "ged-atoms-periodic-table",
            "ged-chemical-reactions-conservation",
            "ged-energy-forms-transformations",
            "ged-forces-motion",
            "ged-work-power-simple-machines",
            "ged-waves-energy-data",
        },
    },
    {
        "value": "earth-space",
        "label": "Earth & Space Science",
        "description": "Earth's structure, plate tectonics, the rock and water cycles, weather, the solar system, and Earth's cycles.",
        "slugs": {
            "ged-earth-space-science",
            "ged-earth-structure-layers",
            "ged-plate-tectonics",
            "ged-rock-cycle",
            "ged-water-cycle",
            "ged-weather-atmosphere",
            "ged-solar-system",
            "ged-moon-seasons",
        },
    },
    {
        "value": "environmental",
        "label": "Environmental Science",
        "description": "Ecosystems, biodiversity, human impact, climate change, pollution, conservation, and sustainability.",
        "slugs": {
            "ged-environmental-science",
        },
    },
    {
        "value": "science-practices",
        "label": "Scientific Reasoning",
        "description": "The scientific method, experimental design, data analysis, and evidence-based reasoning.",
        "slugs": {
            "ged-science-reasoning-practices",
        },
    },
    {
        "value": "science-complete",
        "label": "Complete Review",
        "description": "Full-length practice and mixed review spanning all three science content areas.",
        "slugs": {
            "ged-science-complete-practice",
        },
    },
    {
        "value": "science-practice-exams",
        "label": "Full-Length Practice Exams",
        "description": (
            "Timed, test-day-style GED Science exams -- 34 questions each, spanning Life, Physical, and "
            "Earth & Space Science -- in five difficulty tiers, from foundational (Level 1) to elite "
            "(Level 5)."
        ),
        "slugs": {
            "ged-science-exam",
            "ged-science-exam-level2",
            "ged-science-exam-level3",
            "ged-science-exam-level4",
            "ged-science-exam-level5",
        },
    },
]

SCIENCE_FALLBACK_GROUP = {
    "value": "more-science",
    "label": "More Science",
    "description": "Additional science courses.",
    "slugs": set(),
}

SCIENCE_COURSE_ORDER = {
    # Life Science
    "ged-life-science": 10,
    "ged-cell-biology": 11,
    "ged-cellular-energy": 12,
    "ged-genetics-heredity": 13,
    "ged-evolution-natural-selection": 14,
    "ged-ecosystems-energy-flow": 15,
    "ged-human-body-health": 16,
    "ged-homeostasis-data": 17,
    # Physical Science
    "ged-physical-science": 20,
    "ged-matter-states": 21,
    "ged-atoms-periodic-table": 22,
    "ged-chemical-reactions-conservation": 23,
    "ged-energy-forms-transformations": 24,
    "ged-forces-motion": 25,
    "ged-work-power-simple-machines": 26,
    "ged-waves-energy-data": 27,
    # Earth & Space Science
    "ged-earth-space-science": 30,
    "ged-earth-structure-layers": 31,
    "ged-plate-tectonics": 32,
    "ged-rock-cycle": 33,
    "ged-water-cycle": 34,
    "ged-weather-atmosphere": 35,
    "ged-solar-system": 36,
    "ged-moon-seasons": 37,
    # Environmental Science
    "ged-environmental-science": 40,
    # Scientific Reasoning
    "ged-science-reasoning-practices": 50,
    # Complete Review
    "ged-science-complete-practice": 90,
    # Full-Length Practice Exams
    "ged-science-exam": 110,
    "ged-science-exam-level2": 120,
    "ged-science-exam-level3": 130,
    "ged-science-exam-level4": 140,
    "ged-science-exam-level5": 150,
}


def _science_topic_group(course):
    for group in SCIENCE_TOPIC_GROUPS:
        if course.slug in group["slugs"]:
            return group
    return SCIENCE_FALLBACK_GROUP


def _science_topic_groups(courses):
    grouped = {group["value"]: [] for group in SCIENCE_TOPIC_GROUPS}
    grouped[SCIENCE_FALLBACK_GROUP["value"]] = []

    for course in courses:
        grouped[_science_topic_group(course)["value"]].append(course)

    topic_groups = []
    for group in [*SCIENCE_TOPIC_GROUPS, SCIENCE_FALLBACK_GROUP]:
        items = grouped[group["value"]]
        if not items:
            continue
        items.sort(key=lambda c: (SCIENCE_COURSE_ORDER.get(c.slug, 999), c.title))
        topic_groups.append({
            "value": group["value"],
            "label": group["label"],
            "description": group["description"],
            "courses": items,
        })
    return topic_groups


# ---------------------------------------------------------------------------
# RLA (Reading & Language Arts) topic groups
# ---------------------------------------------------------------------------
RLA_TOPIC_GROUPS = [
    {
        "value": "reading",
        "label": "Reading Comprehension",
        "description": "Strategies for understanding informational and literary texts, identifying main ideas, inference, author's purpose, text structure, and comparing two passages.",
        "slugs": {
            "ged-reading-comprehension",
            "sat-rw-information-ideas",
            "sat-rw-craft-structure",
        },
    },
    {
        "value": "writing",
        "label": "Writing & Language",
        "description": "Grammar, sentence structure, punctuation, word choice, and the Extended Response essay — everything the GED and SAT test in the writing strand.",
        "slugs": {
            "ged-grammar-conventions",
            "ged-extended-response",
            "sat-rw-standard-english",
        },
    },
    {
        "value": "rla-complete",
        "label": "Complete Review",
        "description": "Full-course survey covering both reading comprehension and writing skills.",
        "slugs": {
            "ged-language-arts",
            "sat-reading-writing-complete",
        },
    },
    {
        "value": "rla-practice-exams",
        "label": "Full-Length Practice Exams",
        "description": (
            "Timed, test-day-style GED Reasoning Through Language Arts exams -- 46 questions each, with "
            "Reading Comprehension and Language & Editing sections -- in five difficulty tiers, from "
            "foundational (Level 1) to elite (Level 5)."
        ),
        "slugs": {
            "ged-rla-exam",
            "ged-rla-exam-level2",
            "ged-rla-exam-level3",
            "ged-rla-exam-level4",
            "ged-rla-exam-level5",
        },
    },
]

RLA_FALLBACK_GROUP = {
    "value": "more-rla",
    "label": "More Language Arts",
    "description": "Additional reading and writing courses.",
    "slugs": set(),
}

RLA_COURSE_ORDER = {
    "ged-reading-comprehension": 10,
    "ged-grammar-conventions": 20,
    "ged-extended-response": 30,
    "sat-rw-information-ideas": 40,
    "sat-rw-craft-structure": 50,
    "sat-rw-standard-english": 60,
    "ged-language-arts": 90,
    "sat-reading-writing-complete": 100,
    "ged-rla-exam": 110,
    "ged-rla-exam-level2": 120,
    "ged-rla-exam-level3": 130,
    "ged-rla-exam-level4": 140,
    "ged-rla-exam-level5": 150,
}


def _rla_topic_group(course):
    for group in RLA_TOPIC_GROUPS:
        if course.slug in group["slugs"]:
            return group
    return RLA_FALLBACK_GROUP


def _rla_topic_groups(courses):
    grouped = {group["value"]: [] for group in RLA_TOPIC_GROUPS}
    grouped[RLA_FALLBACK_GROUP["value"]] = []

    for course in courses:
        grouped[_rla_topic_group(course)["value"]].append(course)

    topic_groups = []
    for group in [*RLA_TOPIC_GROUPS, RLA_FALLBACK_GROUP]:
        items = grouped[group["value"]]
        if not items:
            continue
        items.sort(key=lambda c: (RLA_COURSE_ORDER.get(c.slug, 999), c.title))
        topic_groups.append({
            "value": group["value"],
            "label": group["label"],
            "description": group["description"],
            "courses": items,
        })
    return topic_groups


# ---------------------------------------------------------------------------
# Social Studies topic groups
# ---------------------------------------------------------------------------
SOCIAL_TOPIC_GROUPS = [
    {
        "value": "civics",
        "label": "Civics & Government",
        "description": "The largest section of the GED Social Studies test: democracy, the three branches, the Constitution, federalism, elections, and citizenship.",
        "slugs": {
            "ged-civics-government",
        },
    },
    {
        "value": "us-history",
        "label": "U.S. History",
        "description": "Colonial America through modern times: the Revolution, the Civil War, the World Wars, the Cold War, the Civil Rights Movement, and beyond.",
        "slugs": {
            "ged-us-history",
        },
    },
    {
        "value": "economics",
        "label": "Economics",
        "description": "Supply and demand, market structures, personal finance, government fiscal policy, macroeconomics, and reading economic data.",
        "slugs": {
            "ged-economics",
        },
    },
    {
        "value": "geography",
        "label": "Geography & the World",
        "description": "Maps, physical and human geography, world regions, human-environment interaction, globalization, and geographic data skills.",
        "slugs": {
            "ged-geography-world",
        },
    },
    {
        "value": "social-complete",
        "label": "Complete Review",
        "description": "Full-course survey covering all four Social Studies content areas in one place.",
        "slugs": {
            "ged-social-studies",
        },
    },
    {
        "value": "social-practice-exams",
        "label": "Full-Length Practice Exams",
        "description": (
            "Timed, test-day-style GED Social Studies exams -- 35 questions each, spanning Civics, U.S. "
            "History, Economics, and Geography -- in five difficulty tiers, from foundational (Level 1) "
            "to elite (Level 5)."
        ),
        "slugs": {
            "ged-social-exam",
            "ged-social-exam-level2",
            "ged-social-exam-level3",
            "ged-social-exam-level4",
            "ged-social-exam-level5",
        },
    },
]

SOCIAL_FALLBACK_GROUP = {
    "value": "more-social",
    "label": "More Social Studies",
    "description": "Additional Social Studies courses.",
    "slugs": set(),
}

SOCIAL_COURSE_ORDER = {
    "ged-civics-government": 10,
    "ged-us-history": 20,
    "ged-economics": 30,
    "ged-geography-world": 40,
    "ged-social-studies": 90,
    "ged-social-exam": 110,
    "ged-social-exam-level2": 120,
    "ged-social-exam-level3": 130,
    "ged-social-exam-level4": 140,
    "ged-social-exam-level5": 150,
}


def _social_topic_group(course):
    for group in SOCIAL_TOPIC_GROUPS:
        if course.slug in group["slugs"]:
            return group
    return SOCIAL_FALLBACK_GROUP


def _social_topic_groups(courses):
    grouped = {group["value"]: [] for group in SOCIAL_TOPIC_GROUPS}
    grouped[SOCIAL_FALLBACK_GROUP["value"]] = []

    for course in courses:
        grouped[_social_topic_group(course)["value"]].append(course)

    topic_groups = []
    for group in [*SOCIAL_TOPIC_GROUPS, SOCIAL_FALLBACK_GROUP]:
        items = grouped[group["value"]]
        if not items:
            continue
        items.sort(key=lambda c: (SOCIAL_COURSE_ORDER.get(c.slug, 999), c.title))
        topic_groups.append({
            "value": group["value"],
            "label": group["label"],
            "description": group["description"],
            "courses": items,
        })
    return topic_groups


def _math_topic_group(course):
    for group in MATH_TOPIC_GROUPS:
        if course.slug in group["slugs"]:
            return group
    if "geometry" in course.slug:
        return next(group for group in MATH_TOPIC_GROUPS if group["value"] == "geometry")
    if "algebra" in course.slug:
        return next(group for group in MATH_TOPIC_GROUPS if group["value"] == "algebra")
    return MATH_FALLBACK_GROUP


def _math_topic_groups(courses):
    grouped = {group["value"]: [] for group in MATH_TOPIC_GROUPS}
    grouped[MATH_FALLBACK_GROUP["value"]] = []

    for course in courses:
        grouped[_math_topic_group(course)["value"]].append(course)

    topic_groups = []
    for group in [*MATH_TOPIC_GROUPS, MATH_FALLBACK_GROUP]:
        items = grouped[group["value"]]
        if not items:
            continue
        items.sort(key=lambda course: (MATH_COURSE_ORDER.get(course.slug, 999), course.title))
        topic_groups.append({
            "value": group["value"],
            "label": group["label"],
            "description": group["description"],
            "courses": items,
        })
    return topic_groups


# ---------------------------------------------------------------------------
# SAT Math topic groups
# ---------------------------------------------------------------------------
SAT_MATH_TOPIC_GROUPS = [
    {
        "value": "sat-algebra",
        "label": "Algebra",
        "description": "Linear equations, linear functions, systems of equations, and linear inequalities — the SAT Algebra domain.",
        "slugs": {"sat-math-algebra", "sat-ged-algebra-essentials"},
    },
    {
        "value": "sat-advanced-math",
        "label": "Advanced Math",
        "description": "Quadratics, polynomials, radicals, rational expressions, exponential functions, and function transformations — the SAT Advanced Math domain.",
        "slugs": {"sat-math-advanced-math"},
    },
    {
        "value": "sat-problem-solving",
        "label": "Problem Solving & Data Analysis",
        "description": "Ratios, percentages, statistics, probability, data interpretation, and scatterplots — the SAT Problem Solving & Data Analysis domain.",
        "slugs": {"sat-math-problem-solving"},
    },
    {
        "value": "sat-geometry-trig",
        "label": "Geometry & Trigonometry",
        "description": "Lines, angles, triangles, circles, coordinate geometry, and trigonometric ratios — the SAT Additional Topics in Math domain.",
        "slugs": {"sat-math-geometry-trig"},
    },
    {
        "value": "sat-math-complete",
        "label": "Complete Review",
        "description": "Full-length SAT Math course covering all four domains with mixed practice.",
        "slugs": {"sat-math-complete-course"},
    },
]

SAT_MATH_FALLBACK_GROUP = {
    "value": "sat-more-math",
    "label": "More SAT Math",
    "description": "Additional SAT Math topics and practice.",
    "slugs": set(),
}

SAT_MATH_COURSE_ORDER = {
    "sat-math-algebra": 10,
    "sat-ged-algebra-essentials": 15,
    "sat-math-advanced-math": 20,
    "sat-math-problem-solving": 30,
    "sat-math-geometry-trig": 40,
    "sat-math-complete-course": 90,
}


def _sat_math_topic_groups(courses):
    grouped = {group["value"]: [] for group in SAT_MATH_TOPIC_GROUPS}
    grouped[SAT_MATH_FALLBACK_GROUP["value"]] = []
    for course in courses:
        assigned = SAT_MATH_FALLBACK_GROUP
        for group in SAT_MATH_TOPIC_GROUPS:
            if course.slug in group["slugs"]:
                assigned = group
                break
        grouped[assigned["value"]].append(course)
    topic_groups = []
    for group in [*SAT_MATH_TOPIC_GROUPS, SAT_MATH_FALLBACK_GROUP]:
        items = grouped[group["value"]]
        if not items:
            continue
        items.sort(key=lambda c: (SAT_MATH_COURSE_ORDER.get(c.slug, 999), c.title))
        topic_groups.append({
            "value": group["value"],
            "label": group["label"],
            "description": group["description"],
            "courses": items,
        })
    return topic_groups


# ---------------------------------------------------------------------------
# SAT Reading & Writing topic groups
# ---------------------------------------------------------------------------
SAT_RLA_TOPIC_GROUPS = [
    {
        "value": "sat-information-ideas",
        "label": "Information & Ideas",
        "description": "Central ideas, command of evidence (textual and quantitative), inferences, and cross-text connections — the SAT Information & Ideas domain.",
        "slugs": {"sat-rw-information-ideas"},
    },
    {
        "value": "sat-craft-structure",
        "label": "Craft & Structure",
        "description": "Words in context, text structure, author's perspective, rhetorical choices, and cross-text comparisons — the SAT Craft & Structure domain.",
        "slugs": {"sat-rw-craft-structure"},
    },
    {
        "value": "sat-standard-english",
        "label": "Standard English Conventions",
        "description": "Sentence boundaries, subject-verb agreement, pronoun case, modifiers, parallel structure, punctuation, and verb tense — the SAT Standard English Conventions domain.",
        "slugs": {"sat-rw-standard-english"},
    },
    {
        "value": "sat-rla-complete",
        "label": "Complete Review",
        "description": "Full-length SAT Reading & Writing course covering all domains with mixed practice.",
        "slugs": {"sat-reading-writing-complete"},
    },
]

SAT_RLA_FALLBACK_GROUP = {
    "value": "sat-more-rla",
    "label": "More SAT Reading & Writing",
    "description": "Additional SAT Reading & Writing topics and practice.",
    "slugs": set(),
}

SAT_RLA_COURSE_ORDER = {
    "sat-rw-information-ideas": 10,
    "sat-rw-craft-structure": 20,
    "sat-rw-standard-english": 30,
    "sat-reading-writing-complete": 90,
}


def _sat_rla_topic_groups(courses):
    grouped = {group["value"]: [] for group in SAT_RLA_TOPIC_GROUPS}
    grouped[SAT_RLA_FALLBACK_GROUP["value"]] = []
    for course in courses:
        assigned = SAT_RLA_FALLBACK_GROUP
        for group in SAT_RLA_TOPIC_GROUPS:
            if course.slug in group["slugs"]:
                assigned = group
                break
        grouped[assigned["value"]].append(course)
    topic_groups = []
    for group in [*SAT_RLA_TOPIC_GROUPS, SAT_RLA_FALLBACK_GROUP]:
        items = grouped[group["value"]]
        if not items:
            continue
        items.sort(key=lambda c: (SAT_RLA_COURSE_ORDER.get(c.slug, 999), c.title))
        topic_groups.append({
            "value": group["value"],
            "label": group["label"],
            "description": group["description"],
            "courses": items,
        })
    return topic_groups


def home(request):
    """Courses grouped by program, subject, and topic family where helpful."""
    valid_programs = dict(Course.PROGRAM_CHOICES)
    active = request.GET.get("program", "")
    if active not in valid_programs:
        active = ""

    all_courses = list(
        Course.objects
        .annotate(num_lessons=Count("lessons", distinct=True),
                  num_questions=Count("questions", distinct=True))
        .order_by("title")
    )

    # Which program sections to show (all of them, or just the filtered one).
    show = [active] if active else [p for p, _ in Course.PROGRAM_CHOICES]

    sections = []
    for pval in show:
        subj_groups = []
        for sval, slabel in Course.SUBJECT_CHOICES:
            items = [c for c in all_courses if c.program == pval and c.subject == sval]
            if items:
                if pval == "SAT" and sval == "math":
                    items.sort(key=lambda course: (SAT_MATH_COURSE_ORDER.get(course.slug, 999), course.title))
                    topic_groups = _sat_math_topic_groups(items)
                elif pval == "SAT" and sval == "rla":
                    items.sort(key=lambda course: (SAT_RLA_COURSE_ORDER.get(course.slug, 999), course.title))
                    topic_groups = _sat_rla_topic_groups(items)
                elif sval == "math":
                    items.sort(key=lambda course: (MATH_COURSE_ORDER.get(course.slug, 999), course.title))
                    topic_groups = _math_topic_groups(items)
                elif sval == "science":
                    items.sort(key=lambda course: (SCIENCE_COURSE_ORDER.get(course.slug, 999), course.title))
                    topic_groups = _science_topic_groups(items)
                elif sval == "social":
                    items.sort(key=lambda course: (SOCIAL_COURSE_ORDER.get(course.slug, 999), course.title))
                    topic_groups = _social_topic_groups(items)
                elif sval == "rla":
                    items.sort(key=lambda course: (RLA_COURSE_ORDER.get(course.slug, 999), course.title))
                    topic_groups = _rla_topic_groups(items)
                else:
                    topic_groups = []
                subj_groups.append({
                    "value": sval,
                    "label": slabel,
                    "courses": items,
                    "topic_groups": topic_groups,
                    "course_count": len(items),
                })
        sections.append({
            "value": pval,
            "label": valid_programs[pval],
            "subjects": subj_groups,
        })

    # Honest catalog stats for the landing page (computed from real data).
    stats = {
        "courses": len(all_courses),
        "questions": sum(c.num_questions for c in all_courses),
        "lessons": sum(c.num_lessons for c in all_courses),
        "subjects": len({c.subject for c in all_courses if c.subject != "other"}),
    }

    return render(request, "courses/home.html", {
        "sections": sections,
        "programs": Course.PROGRAM_CHOICES,
        "active": active,
        "stats": stats,
    })


# --- Course series: an overview course and its in-depth companion courses ---
# Each "deep dive" expands one lesson of the overview, listed here in lesson order.
COURSE_SERIES = {
    "ged-life-science": [
        "ged-cell-biology",
        "ged-cellular-energy",
        "ged-genetics-heredity",
        "ged-evolution-natural-selection",
        "ged-ecosystems-energy-flow",
        "ged-human-body-health",
        "ged-homeostasis-data",
    ],
    "ged-earth-space-science": [
        "ged-earth-structure-layers",
        "ged-plate-tectonics",
        "ged-rock-cycle",
        "ged-water-cycle",
        "ged-weather-atmosphere",
        "ged-solar-system",
        "ged-moon-seasons",
    ],
    "ged-physical-science": [
        "ged-matter-states",
        "ged-atoms-periodic-table",
        "ged-chemical-reactions-conservation",
        "ged-energy-forms-transformations",
        "ged-forces-motion",
        "ged-work-power-simple-machines",
        "ged-waves-energy-data",
    ],
}
# Reverse lookup: a deep-dive slug -> its overview slug.
COURSE_SERIES_PARENT = {
    child: parent for parent, children in COURSE_SERIES.items() for child in children
}


def _courses_by_slugs(slugs):
    """Return Course objects for the given slugs, in the given order, with counts."""
    by_slug = {
        c.slug: c
        for c in Course.objects.filter(slug__in=slugs).annotate(
            num_lessons=Count("lessons", distinct=True),
            num_questions=Count("questions", distinct=True),
        )
    }
    return [by_slug[s] for s in slugs if s in by_slug]


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)

    # If this course anchors a series, show its in-depth companion courses.
    deep_dives = _courses_by_slugs(COURSE_SERIES.get(course.slug, []))

    # If this course is a deep dive, link back to its overview course.
    parent_course = None
    parent_slug = COURSE_SERIES_PARENT.get(course.slug)
    if parent_slug:
        parent_course = Course.objects.filter(slug=parent_slug).first()

    return render(request, "courses/course_detail.html", {
        "course": course,
        "deep_dives": deep_dives,
        "parent_course": parent_course,
    })


def signup(request):
    """Create a free account, then sign the new user in and send them home."""
    if request.user.is_authenticated:
        return redirect("courses:home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Send brand-new users straight to the diagnostic to find where to start.
            return redirect("practice:diagnostic_home")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})


def about(request):
    return render(request, "courses/about.html")


def privacy_policy(request):
    return render(request, "courses/privacy_policy.html")


def terms_of_use(request):
    return render(request, "courses/terms_of_use.html")


def copyright_trademark_disclaimer(request):
    return render(request, "courses/copyright_trademark_disclaimer.html")


def parents_minors(request):
    return render(request, "courses/parents_minors.html")
