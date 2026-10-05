from django.urls import path

from . import views

urlpatterns = [
    path("", views.premises, name="premises"),
    path("<int:premise_id>/", views.premise_detail, name="premise_detail"),
]
