from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from data import players

def index(request):
    return HttpResponse("asdasdasd")

def search(request, searchString):
    return HttpResponse("The player string is %s" % searchString)

def player(request, playerId):
    return HttpResponse("You have reached the player %s" % players[playerId])

def anotherPage(requset):
    return HttpResponse("adasdasd")

def details(request):
    template = loader.get_template('polls/index.html')
    a=2
    context={'a':a}
    return HttpResponse(template.render(context,request))


# Create your views here.
