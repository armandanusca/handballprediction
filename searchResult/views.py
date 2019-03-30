from django.shortcuts import render
from django.http import HttpResponse

def searchView(request):
    return HttpResponse('This is what you searched for')