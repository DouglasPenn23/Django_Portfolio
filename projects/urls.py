from django.urls import path
from . import views

urlpatterns = [
    # View for index (Set up to make this Root URL)
    path("", views.project_index, name="project_index"),
    # View for project details (Set up for PK to form URL String)
    path("<int:pk>/", views.project_detail, name="project_detail"),
]