from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("jobList", views.jobList),
    path("jobInterest", views.jobInterest),
    path("jobExperience", views.jobExperience, name='news_search'),
    path("futureJob", views.futureJob),
    path("futureJobSkill", views.futureJobSkill),
    path("futureJobMedia", views.futureJobMedia),
    path("jobex", views.jobex),
    path("joby", views.joby),
    path("game1", views.game1),
    path("game2", views.game2),
]
