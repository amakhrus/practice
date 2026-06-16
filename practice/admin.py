from django.contrib import admin
from .models import Question, Choice, Attempt


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "course", "qtype", "difficulty")
    list_filter = ("course", "qtype", "difficulty")
    search_fields = ("text",)
    inlines = [ChoiceInline]


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "is_correct", "ai_score", "created_at")
    list_filter = ("is_correct",)
    readonly_fields = ("ai_feedback", "ai_score")
