from django.urls import path
from . import views

app_name = "practice"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("diagnostic/", views.diagnostic_home, name="diagnostic_home"),
    path("diagnostic/<str:program>/", views.diagnostic_quiz, name="diagnostic_quiz"),
    path("course/<slug:slug>/", views.practice_set, name="practice_set"),
    path("interactive/<slug:slug>/", views.practice_interactive, name="practice_interactive"),
    path("results/<slug:slug>/", views.practice_results, name="practice_results"),
    path("written/<slug:slug>/", views.written_set, name="written_set"),
    path("question/<int:pk>/", views.question_detail, name="question_detail"),
]
