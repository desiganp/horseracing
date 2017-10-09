# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:30:27 2017

@author: PADD
"""


import sqlite3 as sql
import pandas as pd
from train_horse import train_horse
from sklearn.externals import joblib

con = sql.connect("racedata.db")

df = pd.read_sql_query('select race_track, race_stakes, race_dist, horse_jockey, horse_trainer, horse_kg, horse_draw, horse_time from results_v1_all where horse_name = "RUN FOR YOUR LIFE"',con)

d_names = pd.read_sql_query('select distinct horse_name from results_v1_all ',con)

l_names = list(d_names['horse_name'])
l_samples = []
l_abserror = []
l_mserror = []
l_model = []
l_filename = []

dirname = 'linearmodels/'
for name in l_names:
    print(name)
    #do query + train model
    lm,df,nsamples,abs_error, ms_error = train_horse(name)
    #save model + metadata
    filename = str.replace(name,' ','_')
    joblib.dump([name,lm,nsamples,df,abs_error,ms_error], dirname + filename)
    #extract result data to list
    l_samples.append(nsamples)
    l_filename.append(filename)
    l_abserror.append(abs_error)
    l_mserror.append(ms_error)
   
    if (lm == -1):
        #model not created due to insufficient data            
        l_model.append(False)
    else:
        l_model.append(True)
    
columns = ['horse',
           'no_of_samples', 
           'abs_error', 
           'ms_error', 
           'model_created',
           'filename']

results_df = pd.DataFrame(columns=columns);  
results_df['horse'] = l_names
results_df['no_of_samples'] = l_samples
results_df['abs_error'] = l_abserror
results_df['ms_error'] = l_mserror
results_df['model_created'] = l_model
results_df['filename'] = l_filename          

results_df.to_excel(dirname + 'training_results.xls',index=False)          
                         
#%% http://scikit-learn.org/stable/modules/model_persistence.html
from sklearn.externals import joblib
dirname = 'linearmodels/'
filename = 'filename.pkl'
joblib.dump([name,lm,nsamples,df,abs_error,ms_error], dirname + filename)
name,lm,nsamples,df,abs_error,ms_error = joblib.load('filename.pkl')
