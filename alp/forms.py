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
            'team_short': 'Nazwa skrócona',
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
        if self.error_the_same_team(host_team, guest_team):
            self._errors['league'] = self.error_class(self.error_message_the_same_team())
        if self.error_host_goals(host_team_goals):
            self._errors['host_team_goals'] = self.error_class(self.error_message_host_goals())
        if self.error_guset_goals(guest_team_goals):
            self._errors['guest_team_goals'] = self.error_class(self.error_message_guest_goals())
        if self.error_round_game(round_game, league):
            self._errors['round_game'] = self.error_class(self.error_message_round_game())
        if self.error_host_not_in_league(host_team, self.teams_name_list_from_league(league)):
            self._errors['host_team'] = self.error_class(self.error_message_host_not_in_league())
        if self.error_guest_not_in_league(guest_team, self.teams_name_list_from_league(league)):
            self._errors['guest_team'] = self.error_class(self.error_message_guest_not_in_league())
        return self.cleaned_data

    def error_host_not_in_league(self, host, teams_name_list):
        if str(host) not in teams_name_list:
            return True
        else:
            return False

    def error_guest_not_in_league(self, guest, teams_name_list):
        if str(guest) not in teams_name_list:
            return True
        else:
            return False

    def error_message_host_not_in_league(self):
        return ['Drużyna gospodarzy nie jest przypisana do wybranej ligi']

    def error_message_guest_not_in_league(self):
        return ['Drużyna gości nie jest przypisana do wybranej ligi']

    def teams_name_list_from_league(self, league):
        teams = Team.objects.all().filter(league__league_name=str(league))
        league_teams_name = [team.team_name for team in teams]
        return league_teams_name

    def error_the_same_team(self, team_a, team_b):
        if str(team_a) == str(team_b):
            return True
        else:
            return False

    def error_message_the_same_team(self):
        return ['Jako drużynę gospodarzy i gości wybrano tą samą drużynę']

    def error_host_goals(self, host_goals):
        if host_goals > 150:
            return True
        else:
            return False

    def error_message_host_goals(self):
        return ['Zbyt duża liczba bramek strzelonych przez drużynę gospodarzy, maksymalna wartość 150']

    def error_guset_goals(self, guest_goals):
        if guest_goals > 150:
            return True
        else:
            return False

    def error_message_guest_goals(self):
        return ['Zbyt duża liczba bramek strzelonych przez drużynę gości, maksymalna wartość 150']

    def error_round_game(self, round_game, league):
        teams = Team.objects.all().filter(league__league_name=str(league))
        if round_game < 1 or round_game > (len(teams) - 1) * 2:
            return True
        else:
            return False

    def error_message_round_game(self):
        return ['Błędny nr kolejki']

    class Meta:
        model = Match
        fields = ('league', 'host_team', 'guest_team', 'host_team_goals', 'guest_team_goals', 'round_game',
                  'place', 'comments', 'game_date')
        labels = {
            'league': 'Nazwa ligi',
            'host_team': 'Gospodarz',
            'guest_team': 'Gość',
            'host_team_goals': 'Bramki strzelone - gospodarz',
            'guest_team_goals': 'Bramki strzelone - gość',
            'round_game': 'Kolejka',
            'place': 'Miejscowość',
            'comments': 'Komentarz',
            'game_date': 'Data',
        }
