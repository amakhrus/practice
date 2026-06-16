from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    """Short course, e.g. 'GED Math Basics' or 'SAT Reading'."""

    PROGRAM_CHOICES = [
        ("GED", "GED"),
        ("SAT", "SAT"),
    ]
    # Subject area, used to group/filter courses on the home page.
    SUBJECT_CHOICES = [
        ("math", "Mathematics"),
        ("science", "Science"),
        ("social", "Social Studies"),
        ("rla", "Language Arts"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    program = models.CharField(max_length=3, choices=PROGRAM_CHOICES)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default="math")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.program}] {self.title}"

    @property
    def mcq_count(self):
        return self.questions.filter(qtype="mcq").count()

    @property
    def written_count(self):
        return self.questions.filter(qtype="written").count()


class Lesson(models.Model):
    """A single lesson within a course."""

    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(
        help_text=(
            "Lesson content. Supports **bold**, *italic*, `code`, '- ' bullet lists, "
            "blank lines for paragraphs, and LaTeX math: \\(inline\\) or \\[display\\]."
        )
    )
    video_url = models.URLField(
        blank=True,
        help_text="YouTube/Vimeo video link (optional). Paste a normal link, e.g. https://www.youtube.com/watch?v=XXXX",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"

    @property
    def embed_url(self):
        """Convert a normal YouTube/Vimeo link into an embed URL for <iframe>."""
        url = self.video_url.strip()
        if not url:
            return ""
        if "youtube.com/watch" in url and "v=" in url:
            vid = url.split("v=")[1].split("&")[0]
            return f"https://www.youtube.com/embed/{vid}"
        if "youtu.be/" in url:
            vid = url.split("youtu.be/")[1].split("?")[0]
            return f"https://www.youtube.com/embed/{vid}"
        if "vimeo.com/" in url:
            vid = url.split("vimeo.com/")[1].split("?")[0].split("/")[0]
            return f"https://player.vimeo.com/video/{vid}"
        # Already an embed link or other format -> use as-is
        return url


class Enrollment(models.Model):
    """A student's enrollment in a course."""

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.username} -> {self.course.title}"
