from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

from .models import Leaderboard, LeaderboardKey, Player

def index(request):
  num_leaderboards = Leaderboard.objects.all().count()
  num_players = Player.objects.all().count()

  num_visits = request.session.get('num_visits', 0)
  request.session['num_visits'] = num_visits + 1

  return render(request, 'home.html', context = {'num_leaderboards': num_leaderboards, 'num_players': num_players, 'num_visits': num_visits})

def tabla(request):
  return render(request, 'leaderboard.html')


# Create your views here.
