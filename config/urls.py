from django.contrib import admin
from django.urls import path, include

from courses import views as courses_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", courses_views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),  # login/logout bawaan
    path("practice/", include("practice.urls")),
    path("", include("courses.urls")),
]
