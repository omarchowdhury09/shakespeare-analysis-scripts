# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

shakesURL = 'http://www.gutenberg.org/cache/epub/100/pg100-images.html'
    
shakesPage = urllib2.urlopen(shakesURL)

# parse the html using beautiful soap and store in variable `shakesSoup`
shakesSoup = BeautifulSoup(shakesPage, "html.parser")

tags = shakesSoup.find_all()

charURL = 'https://www.opensourceshakespeare.org/views/plays/characters/chardisplay.php?sortby=lines&searchterm='

charPage = urllib2.urlopen(charURL)

# parse the html using beautiful soap and store in variable `shakesSoup`
charSoup = BeautifulSoup(charPage, "html.parser")
    
charTable = charSoup.find_all('table')


tbl = charTable[1].find_all('tr')

charFreqList = []
i = 0
for itm in tbl:
    i = i + 1
    print i
    if i > 1:
        row = itm.find_all('td')
        name = row[2].string.strip()
        freq = row[0].string.strip()
        charFreqList.append((name,freq))
    
charFreqDF = pd.DataFrame(charFreqList[1:],columns =charFreqList[0])

charFreqDF.to_csv("shakespeareCharacterFrequencies.csv")





    
        