from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy_policy, name="privacy_policy"),
    path("terms/", views.terms_of_use, name="terms_of_use"),
    path("copyright-trademark/", views.copyright_trademark_disclaimer, name="copyright_trademark_disclaimer"),
    path("parents-minors/", views.parents_minors, name="parents_minors"),
    path("course/<slug:slug>/", views.course_detail, name="course_detail"),
]
