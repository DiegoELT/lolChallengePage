# Generated by Django 3.2.8 on 2021-11-11 04:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('leaderboard_id', models.UUIDField(default=uuid.uuid4, help_text='ID correspondiente a la creación de la tabla de jugadores.', primary_key=True, serialize=False)),
                ('is_challenge', models.BooleanField(help_text='La tabla de jugadores es un challenge, y por lo tanto tiene un limite de tiempo.')),
                ('finish_date', models.DateField(blank=True, help_text='La fecha de final del challenge de la tabla.', null=True)),
                ('name', models.CharField(help_text='Ingresa de la Leaderboard que vas a crear.', max_length=20)),
                ('description', models.TextField(blank=True, help_text='Ingresa una descripción para tu Leaderboard (e.g. Yo y mis amigos).', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('riot_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('summoner_name', models.CharField(help_text='Ingresa el Summoner Name del jugador.', max_length=20)),
                ('server', models.CharField(choices=[('br1', 'Brasil'), ('eun1', 'EUNE'), ('euw1', 'EU West'), ('jp1', 'Japón'), ('kr', 'Korea'), ('la1', 'LAN'), ('la2', 'LAS'), ('na1', 'NA'), ('oc1', 'Oceanía'), ('tr1', 'Turquía'), ('ru', 'Rusia')], default='na1', help_text='Servidor en el que se encuentra el jugador.', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderboardKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leaderboard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.leaderboard')),
                ('riot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.player')),
            ],
        ),
    ]
