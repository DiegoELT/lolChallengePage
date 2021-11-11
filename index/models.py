from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.urls import reverse
import uuid

# Create your models here.
class Player(models.Model):
  riot_id = models.CharField(max_length=100, primary_key=True)
  summoner_name = models.CharField(max_length=20, help_text='Ingresa el Summoner Name del jugador.')

  REGIONS = (
    ('br1', 'Brasil'),
    ('eun1', 'EUNE'),
    ('euw1', 'EU West'),
    ('jp1', 'Japón'),
    ('kr', 'Korea'),
    ('la1', 'LAN'),
    ('la2', 'LAS'),
    ('na1', 'NA'),
    ('oc1', 'Oceanía'),
    ('tr1', 'Turquía'),
    ('ru', 'Rusia')
  )

  server = models.CharField(max_length=4, choices=REGIONS, default='na1', help_text='Servidor en el que se encuentra el jugador.')

  def __str__(self):
      return self.summoner_name

  def get_absolute_url(self):
    return reverse('player-detail', args=[str(self.riot_id)])

class Leaderboard(models.Model):
  leaderboard_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID correspondiente a la creación de la tabla de jugadores.')
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  is_challenge = models.BooleanField(help_text='La tabla de jugadores es un challenge, y por lo tanto tiene un limite de tiempo.')
  finish_date = models.DateField(null=True, blank=True, help_text='La fecha de final del challenge de la tabla.')
  name = models.CharField(max_length=20, help_text='Ingresa de la Leaderboard que vas a crear.')
  description = models.TextField(null=True, blank=True, help_text='Ingresa una descripción para tu Leaderboard (e.g. Yo y mis amigos).')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('leaderboard-data', args=[str(self.leaderboard_id)])

class LeaderboardKey(models.Model):
  riot_id = models.ForeignKey('Player', on_delete=models.CASCADE)
  leaderboard_id = models.ForeignKey('Leaderboard', on_delete=models.CASCADE)

  def __str__(self):
    return '%s (%s)' % (self.Player.riot_id, self.Leaderboard.leaderboard_id)

  def get_absolute_url(self):
    return reverse('leaderboard-key-detail', args=[str(self.id)])