from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from data import players
from difflib import SequenceMatcher as match
import re


def searchView(request):
    try:
        searchString = request.POST['search-input']
    except:
        return render(request, 'search.html', {"res":[]})

    res = []
    print(searchString.split())
    for i,x in enumerate(players):
        for name in re.split('\W+',searchString):
            for xname in re.split('\W+',x['name,position']):
                if match(None, name.upper(), xname.upper()).ratio() > 0.8:
                    res.append((x['name,position'],i))

    context = {'res':res}

    return render(request, 'search.html', context)