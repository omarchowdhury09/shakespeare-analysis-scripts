# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 22:07:54 2017

@author: Omar
"""


import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

rootURL = 'https://www.opensourceshakespeare.org/views/plays/plays_alpha.php'
playURL = 'https://www.opensourceshakespeare.org/views/plays/play_view.php?WorkID=%s&Scope=entire&pleasewait=1&msg=pl'
rootPage = urllib2.urlopen(rootURL)

# parse the html using beautiful soap and store in variable `shakesSoup`
rootSoup = BeautifulSoup(rootPage, "html.parser")

itms = rootSoup.find_all("li",{"class":"playtext"})

suffixes = []
for itm in itms:
    indivSuffix = itm.a["href"][20:]
    print indivSuffix
    suffixes.append(indivSuffix)
    
playURLs = [playURL % (suffix,) for suffix in suffixes]

lineList = []

for playURL in playURLs:
    print playURL
    playPage = urllib2.urlopen(playURL)
    playSoup = BeautifulSoup(playPage,"html.parser")
    
    playTitle = re.findall("^.*\(complete text\)",playSoup.title.string.strip())[0][:-16]
    playLines = playSoup.find_all('li')
    
    for playLine in playLines:
        playLineSplit = re.split("\.",playLine.text,1)
        playLineCharacter = playLineSplit[0]
        cleanedPlayLine = re.sub("\n ([0-9]+)"," ",playLineSplit[1]).replace("\n"," ").strip()
        lineList.append((playTitle,playLineCharacter,cleanedPlayLine))

playsFrame = pd.DataFrame(lineList, columns = ("Play","Character","Speech"))
    
## playsFrame.to_csv("shakespearePlaysBySpeech.csv")

playsFrame["Speech"] = playsFrame.Speech.str.replace("[^a-zA-Z0-9 ]+","").str.lower()
# another option
# playsFrame["Speech"] = playsFrame.Speech.str.replace("[^a-zA-Z0-9]+"," ").str.lower()

(playsFrame.groupby("Play").apply(lambda x: np.mean(x.Speech.str.len()))/np.mean(playsFrame.Speech.str.len())).plot(kind = 'bar')

(playsFrame.groupby("Play").apply(lambda x: np.sum(x.Speech.str.len()))/playsFrame.groupby("Play").apply(lambda x: np.sum(x.Speech.str.len())).mean()).plot(kind = 'bar')

(playsFrame.groupby("Play").apply(lambda x: np.std(x.Speech.str.len()))/playsFrame.groupby("Play").apply(lambda x: np.std(x.Speech.str.len())).mean()).plot(kind = 'bar')

