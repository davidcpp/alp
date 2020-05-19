from django.shortcuts import get_list_or_404, render
from django.db.models import Q
from .models import Match, League, Team, Note
from .table import Row_Table

def league_match_list(request, league_name):
    matches = get_list_or_404(Match, league__league_name = league_name)
    leagues = get_list_or_404(League)
    return render(request, 'alp/matches_results.html', {'matches' : matches, 'league_name': league_name, 'leagues': leagues})

def league_team_match_list(request, team_name):
    matches = get_list_or_404(Match, Q(host_team__team_name=team_name) | Q(guest_team__team_name=team_name))
    leagues = get_list_or_404(League)
    return render(request, 'alp/matches_team_results.html', {'matches' : matches, 'leagues': leagues, 'team_name': team_name})


def home(request):
    leagues = get_list_or_404(League)
    notes = get_list_or_404(Note.objects.order_by('-publish_date'))
    return render(request, 'alp/home.html', {'leagues': leagues, 'notes': notes})

def league_table(request, league_name):
    leagues = get_list_or_404(League)
    teams = get_list_or_404(Team, league__league_name=league_name)
    table = []
    for team in teams:
        # matches as host
        matches = get_list_or_404(Match, Q(league__league_name=league_name) & Q(host_team__team_name=team.team_name))
        for match in matches:
            add_result_to_table(team.team_name, table, match.host_team_goals, match.guest_team_goals)
        # matches as guest
        matches = get_list_or_404(Match, Q(league__league_name=league_name) & Q(guest_team__team_name=team.team_name))
        for match in matches:
            add_result_to_table(team.team_name, table, match.guest_team_goals, match.host_team_goals)
    team_ranking = sort_table(table)
    return render(request, 'alp/league_table.html', {'team_ranking': team_ranking, 'league_name': league_name, 'leagues': leagues})

def calculate_point(win, drow):
    return 3 * win + drow

def sort_table(table):
    for row in table:
        row.calculate_points()
        row.calculate_matches()
        row.calculate_goal_balance()
        print(row.print())
    ranking = sorted(table, key=lambda row: (row.points, row.goal_balance, row.goals_scored), reverse=True)
    rank = 1
    for row in ranking:
        row.set_ranking(rank)
        rank += 1
        print(row.print())
    return ranking

def add_result_to_table(team_name, table, goals_scored, goals_lost):
    next_match = False
    for row in table:
        # next match of team
        if (team_name == row.team_name):
            # win
            row.goals_scored += goals_scored
            row.goals_lost += goals_lost
            row.result(goals_scored, goals_lost)
            print(row.team_name)
            next_match = True
    # first match of team
    if (next_match == False):
        row = Row_Table(team_name, 0, 0, 0, goals_scored, goals_lost)
        row.result(goals_scored, goals_lost)
        table.append(row)
        print(row.print())

