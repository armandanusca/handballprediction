import urllib.request
from tqdm import *
from bs4 import BeautifulSoup

def getPlayerStats(player_id):
    #Get page
    text = urllib.request.urlopen("http://www.scoresway.com/?sport=handball&page=player&id=" + str(player_id)).read()
    soup = BeautifulSoup(text,"html.parser")
    #Skip if player doen't exist
    
    if(soup.title.text==" - Handball - Scoresway - Results, fixtures, tables and statistics"):
        return None, None
    
    #Get all details from table and add them to v
    x=soup.find_all("dt")
    y=soup.find_all("dd")
    v={}
    for a,b in zip(x,y):
        v[a.text] = b.text

    #Get all seasons, appearences and goals
    m = {"season":[], "appearences":[], "goals":[]}
    s = soup.find_all("td", {"class":"season"})
    a = soup.find_all("td", {"class":"appearances"})
    g = soup.find_all("td", {"class":"goals_in"})

    #Skip if goals are empty
    if(len(g) == 0):
        return None, None
    
    #Add them to dictionary
    for x,y,z in zip(s,a,g):
        m["season"].append(x.text.replace("\n", ""))
        m["appearences"].append(int(y.text))
        m["goals"].append(int(z.text))
    return v, m

for x in tqdm(range(10000000)):
    try:
        a,b = getPlayerStats(x+1)
        print(x)
    except:
        pass