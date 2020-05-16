from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('matches/<str:league_name>/', views.league_match_list, name='league_match_list'),
]
