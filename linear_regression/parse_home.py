#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:09:03 2017

@author: Desigan
"""

import urllib
from bs4 import BeautifulSoup
import sys

print('Upcoming Meetings:')
print('------------------')

raceform_url = 'http://beta.winningform.co.za'
page = urllib.request.urlopen(raceform_url)
soup = BeautifulSoup(page,"lxml")

dates = soup.find_all("div", style="font-size: 1.4em; color: #6c1b98; padding-top: 4px;")
tracks = soup.find_all("div", style="font-size: 1.7em; font-weight: bold; color: #6c1b98")
races = soup.find_all("div", style="font-size: 1.4em; color: #6c1b98; padding-top: 4px;")
meetings = soup.find_all("a", class_="btn btn-default")

l_dates = []
l_tracks = []
l_races = []
l_meetings = []

for meeting in meetings:
        l_meetings.append(raceform_url + meeting.get('href'))
    
for date in dates:
        if 'Races: ' in date.get_text().strip(): l_races.append(date.get_text().strip())
        else: l_dates.append(date.get_text().strip())
        
for track in tracks:
        l_tracks.append(track.get_text().strip())
        
for i in range(len(l_dates)):
    print(i+1,l_dates[i],l_tracks[i],l_races[i])
   
event_id = input('Please select a meeting from (1-'+str(i+1)+') : ')
try: 
    event_id = int(event_id)
except: 
    print('invalid selection')
    sys.exit()
    

while (event_id < 1 or event_id > i+1):
    event_id = input('Please select a meeting from (1-'+str(i+1)+') : ')
    try: 
        event_id = int(event_id)
    except: 
        print('invalid selection')
        sys.exit()

#%% move to selected event
print(l_meetings[int(event_id)-1])
