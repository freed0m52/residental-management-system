from django.urls import path
from . import views

app_name = "premises"

urlpatterns = [
    path("", views.premises, name="list"),
    path("<slug:slug>/", views.premise_detail, name="detail"),  # Теперь ищем по slug
]
