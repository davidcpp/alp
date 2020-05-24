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
    def clean(self):
        super(Match_Form, self).clean()
        host_team = self.cleaned_data['host_team']
        guest_team = self.cleaned_data['guest_team']
        guest_team_goals = self.cleaned_data['guest_team_goals']
        host_team_goals = self.cleaned_data['host_team_goals']
        round_game = self.cleaned_data['round_game']
        league = self.cleaned_data['league']
        if host_team == guest_team:
            self._errors['host_team'] = self.error_class(['Jako drużynę gospodarzy i gości wybrano tą samą drużynę'])
        if guest_team_goals > 150:
            self._errors['guest_team_goals'] = self.error_class(['Zbyt duża liczba bramek strzelonych przez drużynę gości, maksymalna wartość 150'])
        if host_team_goals > 150:
            self._errors['host_team_goals'] = self.error_class(['Zbyt duża liczba bramek strzelonych przez drużynę gospodarzy, maksymalna wartość 150'])
        if round_game < 1:
            self._errors['host_team_goals'] = self.error_class(['Błędny nr kolejki'])
        teams = Team.objects.all().filter(league__league_name=str(league))
        league_teams_name = [team.team_name for team in teams]
        print(league_teams_name)
        print(host_team)
        if str(host_team) not in league_teams_name:
            self._errors['host_team'] = self.error_class(['Drużyna gospodarzy nie jest przypisana do wybranej ligi'])
        if str(guest_team) not in league_teams_name:
            self._errors['guest_team'] = self.error_class(['Drużyna gości nie jest przypisana do wybranej ligi'])
        return self.cleaned_data

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
