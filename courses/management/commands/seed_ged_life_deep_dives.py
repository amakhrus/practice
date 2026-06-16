"""
Seed all in-depth Life Science companion courses ("Deep Dive").

The parent 'GED Science: Life Science' course gives seven one-lesson overviews.
This command creates the full companion series by delegating to one dedicated,
full-standard seed command per topic (each: 6 lessons, ~30 MCQs, 2 extended
prompts, all-new diagrams):

  1. The Cell -- Structure & Function    (seed_ged_cell_biology)
  2. Cellular Energy                      (seed_ged_cellular_energy)
  3. Genetics & Heredity                  (seed_ged_genetics_heredity)
  4. Evolution & Natural Selection        (seed_ged_evolution_natural_selection)
  5. Ecosystems & Energy Flow             (seed_ged_ecosystems_energy_flow)
  6. Human Body Systems & Health          (seed_ged_human_body_health)
  7. Homeostasis & Life Science Data      (seed_ged_homeostasis_data)

Run:
    python manage.py seed_ged_life_deep_dives
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand


DEEP_DIVE_COMMANDS = (
    "seed_ged_cell_biology",
    "seed_ged_cellular_energy",
    "seed_ged_genetics_heredity",
    "seed_ged_evolution_natural_selection",
    "seed_ged_ecosystems_energy_flow",
    "seed_ged_human_body_health",
    "seed_ged_homeostasis_data",
)


class Command(BaseCommand):
    help = "Create all in-depth Life Science companion courses (Deep Dive)."

    def handle(self, *args, **options):
        for command_name in DEEP_DIVE_COMMANDS:
            call_command(command_name, verbosity=options.get("verbosity", 1))

        self.stdout.write(self.style.SUCCESS("All Life Science deep dives seeded."))
