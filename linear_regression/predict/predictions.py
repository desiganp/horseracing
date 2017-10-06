# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:30:03 2017

@author: PADD
"""
from predict_race import predict_race

race_url = 'http://beta.winningform.co.za/Race/RaceDetails?raceDate=10%2F06%2F2017%2000%3A00%3A00&raceCourse=P&raceNo=1&raceCount=8'

results = predict_race(race_url)

print(results.sort_values('horse_time'))
