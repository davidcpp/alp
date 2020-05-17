from django.urls import path
from . import views

urlpatterns = [
    path('', views.league_list, name='league_list'),
    path('matches/<str:league_name>/', views.league_match_list, name='league_match_list'),
    path('tables/<str:league_name>/', views.league_table, name='league_table'),
]
