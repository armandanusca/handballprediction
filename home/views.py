from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, 'home.html')
