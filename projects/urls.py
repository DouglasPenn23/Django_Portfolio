from django.urls import path
from . import views

urlpatterns = [
    # View for index (Set up to make this Root URL)
    path("", views.homepage, name="homepage"),

    # View for project details (Set up for PK to form URL String)
    path("<int:pk>/", views.project_detail, name="project_detail"),

    # View for Education and Work Page
    path("education_and_work/", views.education_and_work, name="education_and_work"),

    # View for my contact Page
    path("contact/", views.contact, name="contact"),

    # View for my about me Page
    path("about_me/", views.about_me, name="about_me"),

    # View for my Projects Page
    path("projects_page/", views.project_page, name="projects_page")
]