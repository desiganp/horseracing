#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:09:03 2017

@author: Desigan
"""

import urllib
from bs4 import BeautifulSoup
import sys
from predict_race import predict_race

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
meeting_url = l_meetings[int(event_id)-1]
page = urllib.request.urlopen(meeting_url)
soup = BeautifulSoup(page,"lxml")

#race, time, distance

l_race_nos = []
l_race_times = []
l_race_dists = []
l_race_links = []

race_nos = soup.find_all("div",style="font-size: 2.1em; color: #480d83;text-align:center;line-height:2.2em;z-index:2;")
race_times = soup.find_all("div",style="font-size: 1.2em;color:#6B389E;font-weight:400;position:absolute; top:0;right:0;padding:7px;")
race_dists = soup.find_all("div",style="font-size: 1.2em;color:#6B389E;font-weight:400;position:absolute; top:0;left:0;padding:7px;")
race_links = soup.find_all("a", class_="col-sm-6 raceDiv clickable")

for race_link in race_links:
        l_race_links.append(raceform_url + race_link.get('href'))
    
for race_no in race_nos:
    l_race_nos.append(race_no.get_text())
    
for race_time in race_times:
    l_race_times.append(race_time.get_text())
    
for race_dist in race_dists:
    l_race_dists.append(race_dist.get_text())
    
for i in range(len(l_race_nos)):
    print(i+1,l_race_nos[i],l_race_times[i],l_race_dists[i])
    
race_id = input('Please select a race from (1-'+str(i+1)+') : ')
try: 
    race_id = int(race_id)
except: 
    print('invalid selection')
    sys.exit()
    

while (race_id < 1 or race_id > i+1):
    race_id = input('Please select a meeting from (1-'+str(i+1)+') : ')
    try: 
        race_id = int(race_id)
    except: 
        print('invalid selection')
        sys.exit()
        
print(l_race_links[int(race_id)-1])

race_url = l_race_links[int(race_id)-1]
print('--------------')
print('Field...')
print('Number - Horse - Jockey - Trainer - Kg - Draw')
results = predict_race(race_url)
print('--------------')
print('Predictions...')
print(results.sort_values('horse_time'))
