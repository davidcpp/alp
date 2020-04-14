from django.contrib import admin

from .models import Match
from .models import Team

admin.site.register(Match)
admin.site.register(Team)