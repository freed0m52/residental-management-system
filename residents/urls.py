from django.urls import path
from . import views

app_name = "residents" 

urlpatterns = [
    path("", views.residents, name="list"), 
    path("<int:resident_id>/", views.resident_detail, name="detail"),
]
