from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index),
  path('leaderboards/', views.tabla),
  path('', include('django.contrib.auth.urls'))
]