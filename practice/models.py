from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Question(models.Model):
    """Practice question for the current MCQ-only phase."""

    TYPE_CHOICES = [
        ("mcq", "Multiple Choice"),
        ("written", "Written Response"),
    ]
    DIFFICULTY_CHOICES = [
        (1, "Easy"),
        (2, "Medium"),
        (3, "Hard"),
    ]

    course = models.ForeignKey(Course, related_name="questions", on_delete=models.CASCADE)
    qtype = models.CharField(max_length=10, choices=TYPE_CHOICES, default="mcq")
    text = models.TextField("Question text")
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES, default=2)
    # Reserved for a later written-response phase.
    rubric = models.TextField(blank=True, help_text="Reserved for a later written-response phase.")
    # Official explanation shown after the student submits an answer.
    explanation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_qtype_display()}] {self.text[:50]}"

    @property
    def correct_choice(self):
        return self.choices.filter(is_correct=True).first()


class Choice(models.Model):
    """Answer option for a multiple-choice question."""

    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Attempt(models.Model):
    """A student's answer to a practice question."""

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attempts")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="attempts")
    # MCQ answers use selected_choice. answer_text is reserved for a later phase.
    selected_choice = models.ForeignKey(Choice, null=True, blank=True, on_delete=models.SET_NULL)
    answer_text = models.TextField(blank=True)

    is_correct = models.BooleanField(null=True)
    ai_score = models.FloatField(null=True, blank=True)  # reserved for a later phase
    ai_feedback = models.TextField(blank=True)  # local explanation/feedback
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - Q{self.question_id}"
