#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:09:03 2017

@author: Desigan
"""

import urllib
from bs4 import BeautifulSoup

print('Upcoming Meetings:')
print('------------------')

page = urllib.request.urlopen('http://beta.winningform.co.za/Home')
soup = BeautifulSoup(page,"lxml")

dates = soup.find_all("div", style="font-size: 1.4em; color: #6c1b98; padding-top: 4px;")
tracks = soup.find_all("div", style="font-size: 1.7em; font-weight: bold; color: #6c1b98")
races = soup.find_all("div", style="font-size: 1.4em; color: #6c1b98; padding-top: 4px;")

l_dates = []
l_tracks = []
l_races = []
    
for date in dates:
        if 'Races: ' in date.get_text().strip(): l_races.append(date.get_text().strip())
        else: l_dates.append(date.get_text().strip())
        
for track in tracks:
        l_tracks.append(track.get_text().strip())
        
for i in range(len(l_dates)):
    print(i+1,l_dates[i],l_tracks[i],l_races[i])
   