from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from practice.models import Attempt, Question


class McqOnlyPracticeTests(TestCase):
    def setUp(self):
        call_command("seed_ged_basic_math_fractions", verbosity=0)
        self.user = User.objects.create_user(username="student", password="pass12345")
        self.client.force_login(self.user)

    def test_practice_set_renders_and_grades_mcq_only(self):
        question = Question.objects.filter(
            course__slug="ged-basic-math-fractions-mastery",
            qtype="mcq",
        ).prefetch_related("choices").first()
        correct = question.correct_choice

        url = reverse("practice:practice_set", args=["ged-basic-math-fractions-mastery"])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'type="radio"')
        self.assertNotContains(response, "<textarea")
        self.assertNotContains(response, "AI Score")

        response = self.client.post(url, {f"q{question.id}": str(correct.id)})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1 / 32")
        self.assertEqual(Attempt.objects.filter(student=self.user).count(), 1)
        self.assertTrue(Attempt.objects.get(student=self.user).is_correct)
