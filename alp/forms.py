from django import forms

from .models import Note, League, Team, Match

class Note_Form(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'note',)
        labels = {
            'title': 'Tytuł',
            'note': 'Treść',
        }

class League_Form(forms.ModelForm):
    class Meta:
        model = League
        fields = ('sport', 'league_name')
        labels = {
            'sport': 'Dyscyplina',
            'league_name': 'Nazwa ligi',
        }

class Team_Form(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('league', 'team_name', 'team_short', 'place', 'comments')
        labels = {
            'league': 'Nazwa ligi',
            'team_name': 'Nazwa drużyny',
            'team_short': 'Skrócona nazwa drużyny',
            'place': 'Miejscowość',
            'comments': 'Uwagi',
        }

class Match_Form(forms.ModelForm):
    class Meta:
        model = Match
        fields = ('league', 'host_team', 'guest_team', 'host_team_goals', 'guest_team_goals', 'round_game',
                  'place', 'comments')
        labels = {
            'league': 'Nazwa ligi',
            'host_team': 'Gospodarz',
            'guest_team': 'Gość',
            'host_team_goals': 'Bramki strzelone - gospodarz',
            'guest_team_goals': 'Bramki strzelone - gość',
            'round_game': 'Kolejka',
            'place': 'Miejscowość',
            'comments': 'Komentarz',
        }
