from django.urls import path
from . import views

urlpatterns = [
    path("pets/", views.PetsView.as_view()),
    path("pets/<int:pet_id>/", views.PetsDetailView.as_view()),
]
