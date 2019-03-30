from django.shortcuts import render
from django.http import HttpResponse

def mlStats(request):
    return render(request, 'mlstats.html')