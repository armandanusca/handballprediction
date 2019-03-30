from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("asdasdasd")

def search(request, searchString):
    return HttpResponse("The player string is %s" % searchString)

def player(request, playerId):
    return HttpResponse("You have reached the player %s" % playerId)

def anotherPage(requset):
    return HttpResponse("adasdasd")

def details(request, qid):
    response = "You have typed " + str(qid)
    return HttpResponse(response)


# Create your views here.
