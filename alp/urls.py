from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams_list', views.teams_list, name='teams_list'),
    path('matches/<str:league_name>/', views.league_match_list, name='league_match_list'),
    path('tables/<str:league_name>/', views.league_table, name='league_table'),
    path('teams/<str:team_name>/', views.league_team_match_list, name='league_team_match_list'),
    path('match/<int:match_id>/', views.match_details, name='match_details'),
    path('note/new', views.note_form, name='note_form'),
    path('league/new', views.league_form, name='league_form'),
    path('team/new', views.team_form, name='team_form'),
    path('match/new', views.match_form, name='match_form'),
]
