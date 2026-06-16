# GED & SAT LMS

A Learning Management System for GED & SAT preparation, built with **Django**.
Phase 1 focuses on multiple-choice practice with local answer checking and stored explanations.

## Features (MVP)
- Short courses + lessons
- Question bank: multiple choice
- Local answer checking
- Stored explanations after submission
- Student login & built-in Django admin panel to manage courses/questions

## Structure
```
config/      -> main Django settings & URLs
courses/     -> Course, Lesson, Enrollment
practice/    -> Question, Choice, Attempt (practice questions)
ai_engine/   -> reserved for later AI features
templates/   -> HTML views
```

## How to run (Windows / PowerShell)
```powershell
# 1. Activate the virtual environment
.\venv\Scripts\Activate.ps1

# 2. Migrate the database
python manage.py migrate

# 3. Seed the complete GED Math course
python manage.py seed_ged_math_complete
python manage.py seed_ged_number_sense_measurement
python manage.py seed_ged_integer_rational_operations
python manage.py seed_ged_order_operations_formula_skills
python manage.py seed_ged_basic_math_fractions
python manage.py seed_ged_basic_math_percents
python manage.py seed_ged_ratios_proportions_scale
python manage.py seed_ged_basic_math_rates
python manage.py seed_ged_data_stats_probability
python manage.py seed_ged_right_triangles
python manage.py seed_ged_algebra_expressions_polynomials
python manage.py seed_ged_algebra_equations
python manage.py seed_ged_functions_graphs
python manage.py seed_ged_algebra_systems_linear_modeling
python manage.py seed_ged_algebra_advanced_equations
python manage.py seed_ged_algebra_inequalities
python manage.py seed_ged_algebra_advanced_inequalities

# Science courses
python manage.py seed_ged_life_science
python manage.py seed_ged_life_deep_dives       # deep dives: life science topics
python manage.py seed_ged_physical_science
python manage.py seed_ged_physical_deep_dives    # deep dives: physical science topics
python manage.py seed_ged_earth_space_science
python manage.py seed_ged_earth_structure_layers   # deep dive: Earth's interior
python manage.py seed_ged_plate_tectonics          # deep dive: plate tectonics
python manage.py seed_ged_rock_cycle               # deep dive: rock cycle & minerals
python manage.py seed_ged_water_cycle              # deep dive: water cycle
python manage.py seed_ged_weather_atmosphere       # deep dive: weather & atmosphere
python manage.py seed_ged_solar_system             # deep dive: solar system
python manage.py seed_ged_moon_seasons             # deep dive: moon, seasons & tides
python manage.py seed_ged_science_practices        # cross-cutting science reasoning
python manage.py seed_ged_science_complete         # mixed GED Science practice test

# SAT courses
python manage.py seed_sat_math

# 4. Create an admin account
python manage.py createsuperuser

# 5. Run the server
python manage.py runserver
```
Open http://127.0.0.1:8000 (site) and http://127.0.0.1:8000/admin (manage content).

> Campus network note (SSL): if `pip install` fails due to certificates, add
> `--trusted-host pypi.org --trusted-host files.pythonhosted.org`.

## Next roadmap
- Progress tracking & student dashboard
- Adaptive practice (automatic difficulty adjustment / IRT)
- SAT/GED score prediction
- Payments & certificates
- Optional AI explanations and written-response grading in a later phase
