# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:28:09 2017

@author: PADD
"""

from predict_horse import predict_horse

horse_name = "RUN FOR YOUR LIFE"
race_stakes = 66000
race_dist = 1200
horse_kg = 58
horse_draw = 2
race_track = 'FAIRVIEW POLYTRACK'
horse_jockey = 'Zackey'
horse_trainer = 'Spies'

b = predict_horse(horse_name,race_stakes,race_dist,horse_kg,horse_draw,race_track,horse_jockey,horse_trainer)

print(b)
