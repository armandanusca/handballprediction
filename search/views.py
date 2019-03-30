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

    res = set()
    print(searchString.split())
    for i,x in enumerate(players):
        percent = 0
        for name in re.split('\W+',searchString):
            for xname in re.split('\W+',x['name']):
                matchRatio = match(None, name.upper(), xname.upper()).ratio()
                if matchRatio > 0.8:
                    res.add((x['name'],matchRatio))

    res = list(res)
    res.sort(reverse = True, key = lambda x: x[1])
    res = [x[0] for x in res]

    context = {'res':res}

    return render(request, 'search.html', context)