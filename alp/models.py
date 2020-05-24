from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Upper

class Sport(models.Model):
    sport_name = models.CharField(max_length=100, default='Football', unique=True)
    description = models.TextField(default="", null=True)

    class Meta:
        ordering = ['sport_name']

    def __str__(self):
        return self.sport_name

class League(models.Model):
    league_name = models.CharField(max_length=100, unique=True)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, default='Football')

    class Meta:
        ordering = ['league_name']

    def __str__(self):
        return self.league_name

class Team(models.Model):
    league = models.ManyToManyField(League, related_name='team_league_name')
    team_name = models.CharField(max_length=100, unique=True)
    team_short = models.CharField(max_length=20, unique=True)
    place = models.CharField(max_length=50, null=True)
    comments = models.TextField(default="", null=True, blank=True)

    class Meta:
        ordering = [Upper('team_name')]

    def __str__(self):
        return self.team_name

class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='league')
    host_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='host_team')
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest_team')
    host_team_goals = models.PositiveSmallIntegerField(default=0)
    guest_team_goals = models.PositiveSmallIntegerField(default=0)
    round_game = models.PositiveSmallIntegerField(default=1)
    game_date = models.DateTimeField(default=timezone.now)
    place = models.CharField(max_length=50, null=True)
    comments = models.TextField(default="", null=True, blank=True)

    class Meta:
        ordering = ['round_game','game_date']

    def __str__(self):
        return self.host_team.__str__() + '-' + self.guest_team.__str__() + ' ' + self.host_team_goals.__str__() + ':' + self.guest_team_goals.__str__()

class Note(models.Model):
    publish_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=50)
    note = models.TextField(max_length=500, default="", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title