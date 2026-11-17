from django.urls import path
from . import views

app_name = "residents"

urlpatterns = [
    path("", views.residents, name="list"),
    path("create/", views.resident_create, name="create"), # <-- Добавили
    path("<int:resident_id>/", views.resident_detail, name="detail"),
    path("requests/", views.request_list, name="requests"),
    path("statistics/", views.statistics, name="statistics"),
    path("requests/create/", views.request_create, name="request_create"),
]
