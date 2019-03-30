from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def searchView(request):
    return render(request, 'searchResults.html')