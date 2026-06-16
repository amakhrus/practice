from django.core.management import call_command
from django.test import TestCase

from courses.models import Course
from courses.templatetags.richtext import exam_marks, richtext


REGISTERED = "\N{REGISTERED SIGN}"
TRADEMARK = "\N{TRADE MARK SIGN}"


class HomePageCopyTests(TestCase):
    def test_homepage_displays_scope_and_trademark_disclaimer(self):
        response = self.client.get("/")

        self.assertContains(response, "Independent Test Prep LMS")
        self.assertContains(response, f"GED{REGISTERED}")
        self.assertContains(response, f"SAT{REGISTERED}")
        self.assertContains(response, 'href="/about/"')
        self.assertContains(response, 'href="/privacy/"')
        self.assertContains(response, 'href="/terms/"')
        self.assertContains(response, 'href="/copyright-trademark/"')
        self.assertContains(response, 'href="/parents-minors/"')
        self.assertContains(response, "math, science, social studies, reading, and writing")
        self.assertContains(response, "not official GED")
        self.assertContains(response, "This site is independent and is not affiliated")

    def test_exam_mark_filter_marks_display_text_only(self):
        self.assertEqual(exam_marks("GED and SAT prep"), f"GED{REGISTERED} and SAT{REGISTERED} prep")
        self.assertEqual(exam_marks(f"GED{REGISTERED} and SAT{REGISTERED} prep"), f"GED{REGISTERED} and SAT{REGISTERED} prep")
        self.assertEqual(exam_marks(f"GED{TRADEMARK} Right Triangles"), f"GED{REGISTERED} Right Triangles")


class HomePageMathGroupingTests(TestCase):
    def test_ged_math_courses_are_grouped_by_topic_family(self):
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-geometry-volume-mastery",
            title="GED Geometry: Volume & Surface Area Mastery",
            description="Practice volume and surface area.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-geometry-area-mastery",
            title="GED Geometry: Area Mastery",
            description="Practice area formulas.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-algebra-equations-mastery",
            title="GED Algebra: Equations Mastery",
            description="Practice equations.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-algebra-functions-graphs",
            title="GED Algebra: Functions & Graphs Mastery",
            description="Practice functions and graphs.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-algebra-systems-linear-modeling",
            title="GED Algebra: Systems of Equations & Linear Modeling Mastery",
            description="Practice systems and linear models.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-algebra-expressions-polynomials",
            title="GED Algebra: Expressions & Polynomials Mastery",
            description="Practice expressions and polynomials.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-basic-math-fractions-mastery",
            title="GED Basic Math: Fractions Mastery",
            description="Practice fractions.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-number-sense-measurement",
            title="GED Math Foundations: Number Sense & Measurement Mastery",
            description="Practice number sense and measurement.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-integer-rational-operations",
            title="GED Math Foundations: Integer & Rational Number Operations Mastery",
            description="Practice signed and rational number operations.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-order-operations-formula-skills",
            title="GED Math Foundations: Order of Operations, Calculator & Formula Skills Mastery",
            description="Practice order of operations and formula skills.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-ratios-proportions-scale",
            title="GED Math Foundations: Ratios, Proportions & Scale Factors Mastery",
            description="Practice ratios, proportions, and scale.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-basic-math-rates-mastery",
            title="GED Basic Math: Rates & Unit Rates Mastery",
            description="Practice rates.",
        )
        Course.objects.create(
            program="GED",
            subject="math",
            slug="ged-data-stats-probability",
            title="GED Math: Data, Statistics & Probability",
            description="Practice data and probability.",
        )

        response = self.client.get("/?program=GED")
        html = response.content.decode()

        self.assertContains(response, 'href="#ged-math-foundations"')
        self.assertContains(response, 'href="#ged-math-algebra"')
        self.assertContains(response, 'href="#ged-math-geometry"')
        self.assertContains(response, 'href="#ged-math-data"')
        self.assertContains(response, "Foundations")
        self.assertContains(response, "Algebra")
        self.assertContains(response, "Geometry")
        self.assertContains(response, "Data &amp; Probability")

        self.assertLess(html.index('id="ged-math-foundations"'), html.index('id="ged-math-algebra"'))
        self.assertLess(html.index('id="ged-math-algebra"'), html.index('id="ged-math-geometry"'))
        self.assertLess(
            html.index('href="/course/ged-algebra-expressions-polynomials/"'),
            html.index('href="/course/ged-algebra-equations-mastery/"'),
        )
        self.assertLess(
            html.index('href="/course/ged-algebra-functions-graphs/"'),
            html.index('href="/course/ged-algebra-systems-linear-modeling/"'),
        )
        self.assertLess(
            html.index('href="/course/ged-number-sense-measurement/"'),
            html.index('href="/course/ged-integer-rational-operations/"'),
        )
        self.assertLess(
            html.index('href="/course/ged-integer-rational-operations/"'),
            html.index('href="/course/ged-order-operations-formula-skills/"'),
        )
        self.assertLess(
            html.index('href="/course/ged-order-operations-formula-skills/"'),
            html.index('href="/course/ged-basic-math-fractions-mastery/"'),
        )
        self.assertLess(
            html.index('href="/course/ged-ratios-proportions-scale/"'),
            html.index('href="/course/ged-basic-math-rates-mastery/"'),
        )
        self.assertLess(
            html.index('href="/course/ged-geometry-area-mastery/"'),
            html.index('href="/course/ged-geometry-volume-mastery/"'),
        )


class AboutPageTests(TestCase):
    def test_about_page_renders_professional_site_overview(self):
        response = self.client.get("/about/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Independent Test Prep LMS")
        self.assertContains(response, "Clear, independent test prep")
        self.assertContains(response, "Why this site exists")
        self.assertContains(response, "What learners can do here")
        self.assertContains(response, "How the content is created")
        self.assertContains(response, "Who it is for")
        self.assertContains(response, "GED&reg;", html=False)
        self.assertContains(response, "SAT&reg;", html=False)
        self.assertContains(response, "not affiliated with, endorsed by, sponsored by")
        self.assertContains(response, 'href="/#courses"')
        self.assertContains(response, 'href="/practice/diagnostic/"')


class PrivacyPolicyTests(TestCase):
    def test_privacy_policy_page_renders(self):
        response = self.client.get("/privacy/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Privacy Policy")
        self.assertContains(response, "Last updated:</strong> June 7, 2026", html=False)
        self.assertContains(response, "multiple-choice only")
        self.assertContains(response, "We do not sell learner personal information")
        self.assertContains(response, "If a learner is under 13")
        self.assertContains(response, "Parents and Minors")


class TermsOfUseTests(TestCase):
    def test_terms_of_use_page_renders(self):
        response = self.client.get("/terms/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Terms of Use")
        self.assertContains(response, "Last updated:</strong> June 7, 2026", html=False)
        self.assertContains(response, "Original Study Content")
        self.assertContains(response, "not official GED")
        self.assertContains(response, "No Guarantees")
        self.assertContains(response, "Governing Law and Disputes")


class CopyrightTrademarkDisclaimerTests(TestCase):
    def test_copyright_trademark_page_renders(self):
        response = self.client.get("/copyright-trademark/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Copyright and Trademark Disclaimer")
        self.assertContains(response, "Original Content Statement")
        self.assertContains(response, "No Official Materials")
        self.assertContains(response, "Trademark Ownership")
        self.assertContains(response, "not affiliated with, endorsed by, sponsored by")
        self.assertContains(response, "not official GED")


class ParentsMinorsTests(TestCase):
    def test_parents_minors_page_renders(self):
        response = self.client.get("/parents-minors/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Parents and Minors")
        self.assertContains(response, "Learners under 13 should use this site only with parent, guardian, or school consent")
        self.assertContains(response, "Learners ages 13 to 17 should use this site with permission")
        self.assertContains(response, "Parent and Guardian Requests")
        self.assertContains(response, "does not send student answers to an external AI API")

    def test_login_page_displays_minor_notice(self):
        response = self.client.get("/accounts/login/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learners under 13 should use this site only with parent, guardian, or school consent")
        self.assertContains(response, 'href="/parents-minors/"')


class RichtextTests(TestCase):
    def test_self_check_token_renders_interactive_markup(self):
        rendered = str(richtext(r"[[check:What is \(2+2\)?|4|Add two and two.]]"))

        self.assertIn('class="self-check"', rendered)
        self.assertIn('data-answer="4"', rendered)
        self.assertIn(r"\(2+2\)", rendered)
        self.assertIn("Add two and two.", rendered)

    def test_richtext_adds_exam_marks_to_visible_lesson_content(self):
        rendered = str(richtext("GED and SAT practice"))

        self.assertIn(f"GED{REGISTERED}", rendered)
        self.assertIn(f"SAT{REGISTERED}", rendered)


class SeedGedMathCompleteTests(TestCase):
    def test_seed_command_creates_complete_course(self):
        call_command("seed_ged_math_complete", verbosity=0)

        course = Course.objects.get(slug="ged-math-complete-course")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 40)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 40)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)


class SeedGedBasicMathFractionsTests(TestCase):
    def test_seed_command_creates_fraction_mastery_course(self):
        call_command("seed_ged_basic_math_fractions", verbosity=0)

        course = Course.objects.get(slug="ged-basic-math-fractions-mastery")
        self.assertEqual(course.lessons.count(), 10)
        self.assertEqual(course.questions.count(), 32)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 32)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("fractions", course.description.lower())


class SeedGedBasicMathPercentsTests(TestCase):
    def test_seed_command_creates_percents_mastery_course(self):
        call_command("seed_ged_basic_math_percents", verbosity=0)

        course = Course.objects.get(slug="ged-basic-math-percents-mastery")
        self.assertEqual(course.lessons.count(), 10)
        self.assertEqual(course.questions.count(), 33)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 33)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("percents", course.description.lower())


class SeedGedBasicMathRatesTests(TestCase):
    def test_seed_command_creates_rates_mastery_course(self):
        call_command("seed_ged_basic_math_rates", verbosity=0)

        course = Course.objects.get(slug="ged-basic-math-rates-mastery")
        self.assertEqual(course.lessons.count(), 10)
        self.assertEqual(course.questions.count(), 33)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 33)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("rates", course.description.lower())


class SeedGedNumberSenseMeasurementTests(TestCase):
    def test_seed_command_creates_number_sense_measurement_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_number_sense_measurement", verbosity=0)

        course = Course.objects.get(slug="ged-number-sense-measurement")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Math Foundations: Number Sense & Measurement Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 57)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 57)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("number sense", course.description.lower())
        self.assertIn("measurement", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("absolute value", lesson_text.lower())
        self.assertIn("scientific notation", lesson_text.lower())
        self.assertIn("unit conversion", lesson_text.lower())
        self.assertIn("greatest common factor", lesson_text.lower())
        self.assertIn("least common multiple", lesson_text.lower())
        self.assertIn("[[figure:integer_number_line", lesson_text)
        self.assertIn("[[figure:signed_operation_rules", lesson_text)
        self.assertIn("[[figure:gcf_lcm_factor_map", lesson_text)
        self.assertIn("[[figure:scientific_notation_ladder", lesson_text)
        self.assertIn("[[figure:unit_conversion_bridge", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-number-sense-measurement/")
        self.assertContains(response, f"GED{REGISTERED} Math Foundations: Number Sense &amp; Measurement Mastery")
        self.assertContains(response, "Start Practice (57 questions)")


class SeedGedIntegerRationalOperationsTests(TestCase):
    def test_seed_command_creates_integer_rational_operations_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_integer_rational_operations", verbosity=0)

        course = Course.objects.get(slug="ged-integer-rational-operations")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Math Foundations: Integer & Rational Number Operations Mastery")
        self.assertEqual(course.lessons.count(), 10)
        self.assertEqual(course.questions.count(), 40)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 40)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("integers", course.description.lower())
        self.assertIn("rational-number", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("absolute value", lesson_text.lower())
        self.assertIn("signed fractions", lesson_text.lower())
        self.assertIn("real-world positive and negative", lesson_text.lower())
        self.assertIn("multi-step signed expressions", lesson_text.lower())
        self.assertIn("[[figure:integer_number_line", lesson_text)
        self.assertIn("[[figure:absolute_value_distance_model", lesson_text)
        self.assertIn("[[figure:signed_operation_rules", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-integer-rational-operations/")
        self.assertContains(response, f"GED{REGISTERED} Math Foundations: Integer &amp; Rational Number Operations Mastery")
        self.assertContains(response, "Start Practice (40 questions)")


class SeedGedOrderOperationsFormulaSkillsTests(TestCase):
    def test_seed_command_creates_order_operations_formula_skills_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_order_operations_formula_skills", verbosity=0)

        course = Course.objects.get(slug="ged-order-operations-formula-skills")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Math Foundations: Order of Operations, Calculator & Formula Skills Mastery")
        self.assertEqual(course.lessons.count(), 10)
        self.assertEqual(course.questions.count(), 40)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 40)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("order of operations", course.description.lower())
        self.assertIn("formula", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("scientific calculator", lesson_text.lower())
        self.assertIn("formula sheet", lesson_text.lower())
        self.assertIn("rearranging", lesson_text.lower())
        self.assertIn("rounding", lesson_text.lower())
        self.assertIn("[[figure:expression_anatomy", lesson_text)
        self.assertIn("[[figure:order_operations_stack", lesson_text)
        self.assertIn("[[figure:formula_substitution_flow", lesson_text)
        self.assertIn("[[figure:unit_conversion_bridge", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-order-operations-formula-skills/")
        self.assertContains(response, f"GED{REGISTERED} Math Foundations: Order of Operations, Calculator &amp; Formula Skills Mastery")
        self.assertContains(response, "Start Practice (40 questions)")


class SeedGedRatiosProportionsScaleTests(TestCase):
    def test_seed_command_creates_ratios_proportions_scale_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_ratios_proportions_scale", verbosity=0)

        course = Course.objects.get(slug="ged-ratios-proportions-scale")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Math Foundations: Ratios, Proportions & Scale Factors Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 52)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 52)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("ratios", course.description.lower())
        self.assertIn("proportions", course.description.lower())
        self.assertIn("scale", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("part-to-whole", lesson_text.lower())
        self.assertIn("cross products", lesson_text.lower())
        self.assertIn("scale factor", lesson_text.lower())
        self.assertIn("direct variation", lesson_text.lower())
        self.assertIn("[[figure:ratio_tape", lesson_text)
        self.assertIn("[[figure:proportion_cross_products", lesson_text)
        self.assertIn("[[figure:map_scale_distance", lesson_text)
        self.assertIn("[[figure:similar_rectangles_scale", lesson_text)
        self.assertIn("[[figure:rate_graph", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-ratios-proportions-scale/")
        self.assertContains(response, f"GED{REGISTERED} Math Foundations: Ratios, Proportions &amp; Scale Factors Mastery")
        self.assertContains(response, "Start Practice (52 questions)")


class SeedGedDataStatsProbabilityTests(TestCase):
    def test_seed_command_creates_complete_data_stats_probability_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_data_stats_probability", verbosity=0)

        course = Course.objects.get(slug="ged-data-stats-probability")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Math: Data, Statistics & Probability Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 50)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 50)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("statistics", course.description.lower())
        self.assertIn("probability", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("weighted average", lesson_text.lower())
        self.assertIn("histogram", lesson_text.lower())
        self.assertIn("conditional", lesson_text.lower())
        self.assertIn("[[figure:dot_plot_scores", lesson_text)
        self.assertIn("[[figure:histogram_commute", lesson_text)
        self.assertIn("[[figure:two_way_table", lesson_text)
        self.assertIn("[[figure:misleading_scale", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-data-stats-probability/")
        self.assertContains(response, f"GED{REGISTERED} Math: Data, Statistics &amp; Probability Mastery")
        self.assertContains(response, "Start Practice (50 questions)")


class SeedGedAlgebraExpressionsPolynomialsTests(TestCase):
    def test_seed_command_creates_expressions_polynomials_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_algebra_expressions_polynomials", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-expressions-polynomials")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Expressions & Polynomials Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 52)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 52)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("expressions", course.description.lower())
        self.assertIn("polynomials", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("equivalent", lesson_text.lower())
        self.assertIn("distributive property", lesson_text.lower())
        self.assertIn("rational expression", lesson_text.lower())
        self.assertIn("factoring", lesson_text.lower())
        self.assertIn("[[figure:expression_anatomy", lesson_text)
        self.assertIn("[[figure:distributive_area_model", lesson_text)
        self.assertIn("[[figure:polynomial_degree", lesson_text)
        self.assertIn("[[figure:factoring_trinomial", lesson_text)
        self.assertIn("[[figure:rational_expression_restriction", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-expressions-polynomials/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Expressions &amp; Polynomials Mastery")
        self.assertContains(response, "Start Practice (52 questions)")


class SeedGedFunctionsGraphsTests(TestCase):
    def test_seed_command_creates_functions_graphs_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_functions_graphs", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-functions-graphs")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Functions & Graphs Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 52)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 52)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("functions", course.description.lower())
        self.assertIn("graphs", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("domain", lesson_text.lower())
        self.assertIn("range", lesson_text.lower())
        self.assertIn("linear inequality", lesson_text.lower())
        self.assertIn("[[figure:function_table_line", lesson_text)
        self.assertIn("[[figure:slope_types", lesson_text)
        self.assertIn("[[figure:linear_inequality_shade", lesson_text)
        self.assertIn("[[figure:system_graph", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-functions-graphs/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Functions &amp; Graphs Mastery")
        self.assertContains(response, "Start Practice (52 questions)")


class SeedGedAlgebraSystemsLinearModelingTests(TestCase):
    def test_seed_command_creates_systems_linear_modeling_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_algebra_systems_linear_modeling", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-systems-linear-modeling")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Systems of Equations & Linear Modeling Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 50)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 50)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)
        self.assertIn("systems", course.description.lower())
        self.assertIn("linear modeling", course.description.lower())

        lesson_text = "\n".join(course.lessons.values_list("content", flat=True))
        self.assertIn("substitution", lesson_text.lower())
        self.assertIn("elimination", lesson_text.lower())
        self.assertIn("break-even", lesson_text.lower())
        self.assertIn("infinitely many solutions", lesson_text.lower())
        self.assertIn("[[figure:system_graph", lesson_text)
        self.assertIn("[[figure:systems_substitution_flow", lesson_text)
        self.assertIn("[[figure:systems_elimination_balance", lesson_text)
        self.assertIn("[[figure:break_even_model_graph", lesson_text)
        self.assertIn("[[figure:function_table_line", lesson_text)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", question.text):
                self.assertIn(name, FIGURES)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-systems-linear-modeling/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Systems of Equations &amp; Linear Modeling Mastery")
        self.assertContains(response, "Start Practice (50 questions)")


class SeedGedRightTrianglesTests(TestCase):
    def test_seed_command_creates_right_triangles_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_right_triangles", verbosity=0)

        course = Course.objects.get(slug="ged-geometry-right-triangles")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Geometry: Right Triangles")
        self.assertEqual(course.lessons.count(), 8)
        self.assertEqual(course.questions.count(), 28)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 28)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-geometry-right-triangles/")
        self.assertContains(response, f"GED{REGISTERED} Geometry: Right Triangles")
        self.assertNotContains(response, f"GED{TRADEMARK}")


class SeedGedAlgebraEquationsTests(TestCase):
    def test_seed_command_creates_equations_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_algebra_equations", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-equations-mastery")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Equations Mastery")
        self.assertEqual(course.lessons.count(), 10)
        self.assertEqual(course.questions.count(), 45)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 45)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-equations-mastery/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Equations Mastery")
        self.assertContains(response, "Start Practice (45 questions)")


class SeedGedAlgebraAdvancedEquationsTests(TestCase):
    def test_seed_command_creates_advanced_equations_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_algebra_advanced_equations", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-advanced-equations")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Advanced Equations & Applications")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 60)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 60)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-advanced-equations/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Advanced Equations &amp; Applications")
        self.assertContains(response, "Start Practice (60 questions)")


class SeedGedAlgebraInequalitiesTests(TestCase):
    def test_seed_command_creates_inequalities_mastery_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_algebra_inequalities", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-inequalities-mastery")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Inequalities Mastery")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 62)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 62)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-inequalities-mastery/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Inequalities Mastery")
        self.assertContains(response, "Start Practice (62 questions)")


class SeedGedAlgebraAdvancedInequalitiesTests(TestCase):
    def test_seed_command_creates_advanced_inequalities_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_algebra_advanced_inequalities", verbosity=0)

        course = Course.objects.get(slug="ged-algebra-advanced-inequalities")
        self.assertEqual(course.program, "GED")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.title, "GED Algebra: Advanced Inequalities & Applications")
        self.assertEqual(course.lessons.count(), 12)
        self.assertEqual(course.questions.count(), 64)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 64)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)
            self.assertIn("Step 1", question.explanation)
            self.assertIn("Common trap", question.explanation)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

        response = self.client.get("/course/ged-algebra-advanced-inequalities/")
        self.assertContains(response, f"GED{REGISTERED} Algebra: Advanced Inequalities &amp; Applications")
        self.assertContains(response, "Start Practice (64 questions)")


class SeedGedLifeScienceTests(TestCase):
    def test_seed_command_creates_life_science_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_life_science", verbosity=0)

        course = Course.objects.get(slug="ged-life-science")
        self.assertEqual(course.subject, "science")
        self.assertEqual(course.lessons.count(), 7)
        self.assertEqual(course.questions.count(), 17)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 17)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

    def test_seed_command_creates_life_science_deep_dive_series(self):
        import re

        from courses.figures import FIGURES
        from courses.views import COURSE_SERIES

        call_command("seed_ged_life_science", verbosity=0)
        call_command("seed_ged_life_deep_dives", verbosity=0)

        slugs = COURSE_SERIES["ged-life-science"]
        self.assertEqual(len(slugs), 7)

        for slug in slugs:
            course = Course.objects.get(slug=slug)
            self.assertEqual(course.program, "GED")
            self.assertEqual(course.subject, "science")
            self.assertIn("Deep Dive", course.title)
            self.assertGreaterEqual(course.lessons.count(), 5)
            self.assertGreaterEqual(course.questions.count(), 10)
            self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

            for question in course.questions.all():
                self.assertEqual(question.qtype, "mcq")
                self.assertEqual(question.choices.count(), 4)
                self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

            for lesson in course.lessons.all():
                self.assertIn("Common misconception", lesson.content)
                for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                    self.assertIn(name, FIGURES)

            shortest_lesson = min(len(lesson.content) for lesson in course.lessons.all())
            self.assertGreaterEqual(shortest_lesson, 850)

        response = self.client.get("/course/ged-life-science/")
        self.assertContains(response, "Go deeper: in-depth companion courses")
        self.assertContains(response, f"GED{REGISTERED} Science: The Cell -- Structure &amp; Function (Deep Dive)")
        self.assertContains(response, f"GED{REGISTERED} Science: Homeostasis &amp; Life Science Data (Deep Dive)")

        response = self.client.get("/course/ged-cell-biology/")
        self.assertContains(response, "Part of the")
        self.assertContains(response, f"GED{REGISTERED} Science: Life Science")


class SeedGedPhysicalScienceTests(TestCase):
    def test_seed_command_creates_physical_science_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_physical_science", verbosity=0)

        course = Course.objects.get(slug="ged-physical-science")
        self.assertEqual(course.subject, "science")
        self.assertEqual(course.lessons.count(), 7)
        self.assertEqual(course.questions.count(), 29)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 29)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        # Every MCQ must have exactly four choices and exactly one correct answer.
        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

        # Every figure referenced in a lesson must exist in the registry.
        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

    def test_seed_command_creates_physical_science_deep_dive_series(self):
        import re

        from courses.figures import FIGURES
        from courses.views import COURSE_SERIES

        call_command("seed_ged_physical_science", verbosity=0)
        call_command("seed_ged_physical_deep_dives", verbosity=0)

        slugs = COURSE_SERIES["ged-physical-science"]
        self.assertEqual(len(slugs), 7)

        for slug in slugs:
            course = Course.objects.get(slug=slug)
            self.assertEqual(course.program, "GED")
            self.assertEqual(course.subject, "science")
            self.assertIn("Deep Dive", course.title)
            self.assertGreaterEqual(course.lessons.count(), 5)
            self.assertGreaterEqual(course.questions.count(), 10)
            self.assertEqual(course.questions.filter(qtype="mcq").count(), course.questions.count())
            self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

            for question in course.questions.all():
                self.assertEqual(question.choices.count(), 4)
                self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

            for lesson in course.lessons.all():
                self.assertIn("Common misconception", lesson.content)
                for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                    self.assertIn(name, FIGURES)

            shortest_lesson = min(len(lesson.content) for lesson in course.lessons.all())
            self.assertGreaterEqual(shortest_lesson, 900)

        atoms_course = Course.objects.get(slug="ged-atoms-periodic-table")
        atoms_text = "\n".join(atoms_course.lessons.values_list("content", flat=True)).lower()
        self.assertIn("atomic number", atoms_text)
        self.assertIn("groups", atoms_text)

        response = self.client.get("/course/ged-physical-science/")
        self.assertContains(response, "Go deeper: in-depth companion courses")
        self.assertContains(response, f"GED{REGISTERED} Science: Matter and Its States (Deep Dive)")
        self.assertContains(response, f"GED{REGISTERED} Science: Waves, Energy &amp; Reading Science Data (Deep Dive)")

        response = self.client.get("/course/ged-forces-motion/")
        self.assertContains(response, "Part of the")
        self.assertContains(response, f"GED{REGISTERED} Science: Physical Science")


class SeedGedEarthSpaceScienceTests(TestCase):
    def test_seed_command_creates_earth_space_science_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_ged_earth_space_science", verbosity=0)

        course = Course.objects.get(slug="ged-earth-space-science")
        self.assertEqual(course.subject, "science")
        self.assertEqual(course.lessons.count(), 7)
        self.assertEqual(course.questions.count(), 26)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 26)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        # Every MCQ must have exactly four choices and exactly one correct answer.
        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

        # Every figure referenced in a lesson must exist in the registry.
        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)


class SeedSatMathTests(TestCase):
    def test_seed_command_creates_sat_math_course(self):
        import re

        from courses.figures import FIGURES

        call_command("seed_sat_math", verbosity=0)

        course = Course.objects.get(slug="sat-math-complete-course")
        self.assertEqual(course.program, "SAT")
        self.assertEqual(course.subject, "math")
        self.assertEqual(course.lessons.count(), 9)
        self.assertEqual(course.questions.count(), 35)
        self.assertEqual(course.questions.filter(qtype="mcq").count(), 35)
        self.assertEqual(course.questions.filter(qtype="essay").count(), 0)

        # Every MCQ must have exactly four choices and exactly one correct answer.
        for question in course.questions.all():
            self.assertEqual(question.choices.count(), 4)
            self.assertEqual(question.choices.filter(is_correct=True).count(), 1)

        # Every figure referenced in a lesson must exist in the registry.
        for lesson in course.lessons.all():
            for name in re.findall(r"\[\[figure:([a-zA-Z0-9_]+)", lesson.content):
                self.assertIn(name, FIGURES)

    def test_homepage_shows_sat_section_once_seeded(self):
        call_command("seed_sat_math", verbosity=0)

        response = self.client.get("/?program=SAT")
        self.assertContains(response, f"SAT{REGISTERED} Math: Complete Course &amp; Test Prep")
