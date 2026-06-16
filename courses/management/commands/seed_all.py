"""
Run every content seeder (and enricher) in one command.

This discovers all management commands whose names start with ``seed_`` or
``enrich_`` and runs them in order: seeders first (which create courses), then
enrichers (which add to existing courses). It's the easiest way to build the
full catalog on a fresh server.

Run:
    python manage.py seed_all

Options:
    --list   Show what would run, without running anything.
"""
from django.core.management import call_command, get_commands
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run all seed_* and enrich_* commands to build the full course catalog."

    def add_arguments(self, parser):
        parser.add_argument(
            "--list", action="store_true",
            help="List the commands that would run, without running them.",
        )

    def handle(self, *args, **options):
        names = sorted(get_commands().keys())
        seeders = [n for n in names if n.startswith("seed_") and n != "seed_all"]
        enrichers = [n for n in names if n.startswith("enrich_")]
        ordered = seeders + enrichers

        if options["list"]:
            self.stdout.write(self.style.NOTICE(f"{len(ordered)} commands would run:"))
            for n in ordered:
                self.stdout.write(f"  {n}")
            return

        total = len(ordered)
        ok, failed = 0, []
        for i, name in enumerate(ordered, start=1):
            self.stdout.write(self.style.MIGRATE_HEADING(f"[{i}/{total}] {name}"))
            try:
                call_command(name)
                ok += 1
            except Exception as exc:  # keep going so one bad seeder doesn't stop the rest
                failed.append(name)
                self.stderr.write(self.style.ERROR(f"    FAILED: {exc}"))

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"Done: {ok}/{total} succeeded."))
        if failed:
            self.stdout.write(self.style.WARNING("Failed: " + ", ".join(failed)))
