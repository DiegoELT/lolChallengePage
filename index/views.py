from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
  return HttpResponse('Hello World~ Welcome to the LoL Challenge Bot')

# Create your views here.
