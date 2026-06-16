# Generated for Phase 1 MCQ-only practice.

from django.db import migrations


def remove_essay_questions(apps, schema_editor):
    Question = apps.get_model("practice", "Question")
    Question.objects.filter(qtype="essay").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("practice", "0003_alter_question_qtype_alter_question_rubric"),
    ]

    operations = [
        migrations.RunPython(remove_essay_questions, migrations.RunPython.noop),
    ]
