import urllib.request as req
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

for x in tqdm(range(100000)):
    try:
        s=BeautifulSoup(req.urlopen("http://www.scoresway.com/?sport=handball&page=player&id=" + str(x+1)).read(),"html.parser")
        if(x%30 == 0): 
            time.sleep(10)
        if(s.title.text==" - Handball - Scoresway - Results, fixtures, tables and statistics"):
            continue
        print(x)
    except:
        x=x-1
        