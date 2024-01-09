from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.boardPage),         # <int:pk> ::: pk가 정수형임을 명시
    path('', views.boardList),                             # blog 앱에서의 기본(메인) 페이지

]

