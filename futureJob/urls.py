from django.urls import path
from . import views

urlpatterns = [
    path("", views.futureJob),
    path("futureJobSkill/", views.futureJobSkill),
    path("futureJobMedia/", views.futureJobMedia),
]
