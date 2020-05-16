from django.shortcuts import get_list_or_404, render
from .models import Match, League

def match_list(request):
    matches = Match.objects.all()
    return render(request, 'alp/match_list2.html', {'matches' : matches})

def league_match_list(request, league_name):
    matches = get_list_or_404(Match, league__league_name = league_name)
    return render(request, 'alp/matches_results.html', {'matches' : matches, 'league_name': league_name})