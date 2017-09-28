# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:53:25 2017

@author: PADD
"""
def train_horse(horse_name):
    import sqlite3 as sql
    import pandas as pd
    
    
    con = sql.connect("racedata.db")
    
    df = pd.read_sql_query('select race_track, race_stakes, race_dist, horse_jockey, horse_trainer, horse_kg, horse_draw, horse_time from results_v1_all where horse_name = "' + horse_name +'"',con)

    
    #%% create the feature table
    # if the horse_time = 0.0
    df = df[df.horse_time != '0.00']
    
    if len(df) < 5:
        print('Less than 5 samples - cannot train model')
        return -1,-1,len(df)
    else:
        print('Proceeding to train with ',len(df),'samples')
    
    # use one hot encoding for categorical data
    race_tracks = pd.get_dummies(df['race_track'],prefix = 'track')
    df = df.drop('race_track',axis=1)
    df = df.join(race_tracks)
    
    horse_jockeys = pd.get_dummies(df['horse_jockey'],prefix = 'jockey')
    df = df.drop('horse_jockey',axis=1)
    df = df.join(horse_jockeys)
    
    horse_trainers = pd.get_dummies(df['horse_trainer'],prefix = 'trainer')
    df = df.drop('horse_trainer',axis=1)
    df = df.join(horse_trainers)
    
    
    df['horse_time'] = df['horse_time'].astype(float)
    df['horse_kg'] = df['horse_kg'].astype(float)
    df['horse_draw'] = df['horse_draw'].astype(int)
    
    df['race_dist'] = df['race_dist'].str.replace(' ','')
    df['race_dist'] = df['race_dist'].str.replace('m','')
    df['race_dist'] = df['race_dist'].astype(int)
    
    df['race_stakes'] = df['race_stakes'].str.replace(' ','')
    df['race_stakes'] = df['race_stakes'].str.replace('R','')
    df['race_stakes'] = df['race_stakes'].astype(int)
    
    
    #%%
    
    feature_list = list(df.columns)
    feature_list.remove('horse_time')
    
    X = df[feature_list]
    y = df['horse_time']
    
    #%% train the model
    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
    from sklearn.linear_model import LinearRegression
    lm = LinearRegression()
    lm.fit(X_train,y_train)
    
    #%%
    predictions = lm.predict(X_test)
    
    #%%
    from sklearn import metrics
    abs_error = metrics.mean_absolute_error(y_test,predictions)
    ms_error = metrics.mean_squared_error(y_test,predictions)
    
    print('Mean absolute error = ',abs_error)
    print('Mean squared error = ',ms_error)
    
    return lm, df, len(df), abs_error, ms_error

#%% do a prediction

#import numpy as np
# data obtained from race card sheet - how to automate this?
# http://news.tabonline.co.za/FieldsPDF/SouthAfrican/FAIRVIEW%20POLYTRACK@2017.09.26.pdf
#d = np.array([66000,1200,58,2,0,1,0,0,0,0,1,0,0,0,1,0])
#d =  d.reshape(1,-1)
#time_pred = lm.predict(d)
# array([ 71.93932502])
# real finish time was 72.13

