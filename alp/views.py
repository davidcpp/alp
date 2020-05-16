from django.shortcuts import get_list_or_404, render
from .models import Match, League

def league_match_list(request, league_name):
    matches = get_list_or_404(Match, league__league_name = league_name)
    leagues = get_list_or_404(League)
    return render(request, 'alp/matches_results.html', {'matches' : matches, 'league_name': league_name, 'leagues': leagues})

def league_list(request):
    leagues = get_list_or_404(League)
    return render(request, 'alp/home.html', {'leagues': leagues})
