from django.urls import path
from . import views

app_name = "premises"  

urlpatterns = [
    path("", views.premises, name="list"),
    path("<int:premise_id>/", views.premise_detail, name="detail"),
]
