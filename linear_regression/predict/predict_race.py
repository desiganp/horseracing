# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:28:09 2017

@author: PADD
"""

from predict_horse import predict_horse
from parse_race import parse_race

race_url = 'http://beta.winningform.co.za/Race/RaceDetails?raceDate=10%2F06%2F2017%2000%3A00%3A00&raceCourse=P&raceNo=1&raceCount=8'
df = parse_race(race_url)
#%% cycle through dataframe rows doing predictions

#use the race url for encoding the race track

race_course = race_url.split('&')[1]
race_course = race_course.split('=')[1]

if   race_course == 'A': race_track = 'ARLINGTON'
elif race_course == 'C': race_track = 'CLAIRWOOD'
elif race_course == 'D': race_track = 'GREYVILLE'
elif race_course == 'E': race_track = 'SCOTTSVILLE'
elif race_course == 'G': race_track = 'GREYVILLE POLYTRACK'
elif race_course == 'H': race_track = 'BORROWDALE'
elif race_course == 'I': race_track = 'RANDJIESFONTEIN'
elif race_course == 'J': race_track = 'TURFFONTEIN INSIDE'
elif race_course == 'K': race_track = 'KENILWORTH'
elif race_course == 'L': race_track = 'DURBANVILLE'
elif race_course == 'L': race_track = 'DURBANVILLE'
elif race_course == 'P': race_track = 'FAIRVIEW POLYTRACK'
elif race_course == 'Q': race_track = 'FLAMINGO PARK'
elif race_course == 'R': race_track = 'VAAL SAND'
elif race_course == 'S': race_track = 'SCOTTSVILLE'
elif race_course == 'T': race_track = 'TURFFONTEIN STANDSIDE'
elif race_course == 'U': race_track = 'MAURITIUS'
elif race_course == 'V': race_track = 'VAAL'
else: race_track = df['race_track'][0]

#race_track = df['race_track'][0]
race_stakes = df['race_stakes'][0]
race_dist = df['race_dist'][0]

for index, row in df.iterrows(): 
    horse_name = df['horse_name'][index]
    horse_trainer = df['horse_trainer'][index]
    horse_jockey = df['horse_jockey'][index]
    horse_kg = df['horse_kg'][index]
    horse_draw = df['horse_draw'][index]
    finish_time = predict_horse(horse_name,race_stakes,race_dist,horse_kg,horse_draw,race_track,horse_jockey,horse_trainer)
    print(horse_name+' : ',finish_time)
