from django.urls import path
from . import views

app_name = "premises"

urlpatterns = [
    path("", views.premises, name="list"),
    path("create/", views.premise_create, name="create"),      # <-- Создание ДО слага!
    path("<slug:slug>/", views.premise_detail, name="detail"),
]
