from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Leaderboard, LeaderboardKey, Player

def index(request):
  num_users = User.objects.all().count()
  num_leaderboards = Leaderboard.objects.all().count()
  num_players = Player.objects.all().count()

  return render(request, 'home.html', context = {'num_users': num_users, 'num_leaderboards': num_leaderboards, 'num_players': num_players})

# Create your views here.
