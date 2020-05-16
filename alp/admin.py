from django.contrib import admin

from .models import Sport
from .models import League
from .models import Match
from .models import Team

admin.site.register(Sport)
admin.site.register(League)
admin.site.register(Match)
admin.site.register(Team)