---
name: seeders-wipe-attempt-history
description: Re-running a course seed command deletes that course's student Attempt history
metadata:
  type: project
---

Every `seed_*` management command starts with `Course.objects.filter(slug=...).delete()` then recreates the course. Because the FK chain `Attempt → Question → Course` cascades on delete, **re-seeding a course also deletes all student `Attempt` rows for it.**

**Why:** This was harmless while attempt data was never shown, but the progress dashboard (`/practice/dashboard/`, `practice.views.dashboard`) now surfaces `Attempt` history, so re-seeding a live course silently resets students' progress for it.

**How to apply:** Don't re-run a course seeder on a course with real user data unless you intend to wipe its history. If history must be preserved, refactor the seeder to update questions in place (match on a stable key) instead of delete-and-recreate. Related: [[richtext-renders-question-text]].
