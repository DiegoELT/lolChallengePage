from django.contrib import admin
from .models import User, Leaderboard, LeaderboardKey, Player

# Register your models here.
admin.site.register(User)
admin.site.register(Leaderboard)
admin.site.register(LeaderboardKey)
admin.site.register(Player)

