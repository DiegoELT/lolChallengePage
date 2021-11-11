from django.contrib import admin
from .models import Leaderboard, LeaderboardKey, Player

# Register your models here.
admin.site.register(Leaderboard)
admin.site.register(LeaderboardKey)
admin.site.register(Player)

