from django.db import models
from django.utils import timezone

class Team(models.Model):
    team = models.CharField(max_length=100)
    team_short = models.CharField(max_length=10)

class Match(models.Model):
    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    team_1_goals = models.IntegerField(default=0)
    team_2_goals = models.IntegerField(default=0)
    round_game = models.IntegerField(default=0)
    game_date = models.DateField(
            default=timezone.now)
    comments = models.TextField()
    place = models.CharField(max_length=100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


