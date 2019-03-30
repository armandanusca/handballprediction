from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from data import players

def viewPlayer(request):
    return render(request, 'playerProfile.html')
