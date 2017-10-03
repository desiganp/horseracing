# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 08:21:28 2017

@author: PADD
"""

def predict_horse(horse_name,race_stakes,race_dist,horse_kg,horse_draw,race_track,horse_jockey,horse_trainer):
    from sklearn.externals import joblib
    #from sklearn.linear_model import LinearRegression
    import pandas as pd
    import numpy as np
    
    
    #horse_name = 'WEATHER WISE'
    
    dirname = 'linearmodels/'
    training_results = pd.read_excel(dirname+'training_results.xls')
    filename = training_results[training_results['horse'] == horse_name]['filename'].to_string()
    filename = filename.split(' ')[-1]
    #filename = filename[0]
    # get the linear model
    try:
        name,lm,nsamples,df,abs_error,ms_error = joblib.load(dirname+filename)
    except:
        print('No prediction available for :',horse_name)   
        return -1
    
    if lm == -1:
        print('No prediction available for :',horse_name)   
        return -1
    
    # build up numpy array by cycling through the columns
    l_pred = []
    for col in df.columns:
        if col == 'race_stakes': l_pred.append(race_stakes) 
        if col == 'race_dist': l_pred.append(race_dist)
        if col == 'horse_kg': l_pred.append(horse_kg)
        if col == 'horse_draw': l_pred.append(horse_draw)
     
     
        if 'track' in str(col):
            if race_track in str(col):
                l_pred.append(1)
            else:
                l_pred.append(0)
                #print('Info: first time at this track')
                
        if 'jockey' in str(col):
            if horse_jockey in str(col):
                l_pred.append(1)
            else:
                l_pred.append(0)
                #print('Info: new jockey')
            
        if 'trainer' in str(col):
            if horse_trainer in str(col):
                l_pred.append(1)
            else:
                l_pred.append(0)
                #print('Info: new trainer')
        
    a = np.array(l_pred)
    a =  a.reshape(1,-1)
    time_pred = lm.predict(a)
    
    return time_pred[0]




