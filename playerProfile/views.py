from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from data import players

def viewPlayer(request):
    try:
        name = request.POST['buttonValue']
        print(name)
    except:
        return render(request, 'playerProfile.html')

    data = [x for x in players if x['name'] == name]
    position = data[0]['position']
    playerStats = [{'season': x['season'], 
                    'predictedGoals': x['predictedGoals'],
                    'actualGoals': x['actualGoals']} for x in data]
    contents={'playerName':name, 'position': position, 'stats': playerStats}
    return render(request, 'playerProfile.html', contents)
