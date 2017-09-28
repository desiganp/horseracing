# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:30:27 2017

@author: PADD
"""


import sqlite3 as sql
import pandas as pd
from train_horse import train_horse

con = sql.connect("racedata.db")

df = pd.read_sql_query('select race_track, race_stakes, race_dist, horse_jockey, horse_trainer, horse_kg, horse_draw, horse_time from results_v1_all where horse_name = "RUN FOR YOUR LIFE"',con)

d_names = pd.read_sql_query('select distinct horse_name from results_v1_all ',con)

l_names = list(d_names['horse_name'])

for name in l_names:
    print(name)
    #do query
    #train model
    lm,df,nsamples,abs_error, ms_error = train_horse(name)
    #save model

#%% http://scikit-learn.org/stable/modules/model_persistence.html
from sklearn.externals import joblib
joblib.dump(lm, 'filename.pkl') 

lm = joblib.load('filename.pkl') 
