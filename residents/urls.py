from django.urls import path

from . import views

urlpatterns = [
    path("", views.residents, name="residents"),
    path("<int:resident_id>/", views.resident_detail, name="resident_detail"),
]
