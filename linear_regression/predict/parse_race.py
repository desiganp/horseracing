#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:46:44 2017

@author: Desigan
"""
def parse_race(race_url,offline=False):
    import urllib
    from bs4 import BeautifulSoup
    
    
    use_proxy = True
    
    if(offline):
        h = open(race_url,"r")
        soup = BeautifulSoup(h,"lxml")
        
    else:
        if(use_proxy):
            # set up authentication info
            authinfo = urllib.request.HTTPBasicAuthHandler()
            proxy_support = urllib.request.ProxyHandler({"http" : "http://padd:Moonbeam76@proxy.kentron.co.za:80"})
            # build a new opener that adds authentication and caching FTP handlers
            opener = urllib.request.build_opener(proxy_support, authinfo,
                                         urllib.request.CacheFTPHandler)
    
            # install it
            urllib.request.install_opener(opener) 
            page = urllib.request.urlopen(race_url)
            soup = BeautifulSoup(page,"lxml")
    
    #url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=VAAL@31.01.2017.xml'
    #h = open(race_url,"r")
    #page = 'race.html'
    #page = urllib.request.urlopen(url)
    
    #soup = BeautifulSoup(h,"lxml")
    horses = soup.find_all("div", class_="horseHeader")
    weights = soup.find_all("div", style="color: #643A90; font-weight: bold; text-align: center; font-size: 1.7em; margin-top: 30px")
    draws = soup.find_all("div",style="width: 90%; color: #643A90; font-size: 1.1em; border-bottom: 1px solid #ccc; margin: auto;")
    jockeys = soup.find_all("div",style="color: #643A90; font-weight: bold; text-align: center; font-size: 1.4em; margin-top: 23px;")    
    trainers = soup.find_all("div",style="color: #643A90; font-weight: bold; text-align: center; font-size: 1.4em; margin-top: 23px")
    
    distances = soup.find_all("div",style="color: #6B389E; font-size: 1.7em; z-index: 1; font-weight: bold")
    tracks = soup.find_all("div",style="color: #643A90; font-size: 3.5em; z-index: 1; font-weight: bold")   
    stakes = soup.find_all("div",style="font-weight: bold; font-size: 1.4em;")   
     
    
        
    l_horses = []
    l_weights = []
    l_draws = []
    l_jockeys = []
    l_trainers = []
    
    #print('horses')
    for horse in horses:
    #    print(horse.get_text())
        l_horses.append(horse.get_text().strip())
    #print('weights')
    for weight in weights:
        #print(weight.get_text().split('kg')[0].split('            ')[1])
        #l_weights.append(int(weight.get_text().split('kg')[0].split('            ')[1]))
        l_weights.append(int(weight.get_text().split('kg')[0].strip()))
    #print('draws')    
    for draw in draws:
        #print(draw.get_text())
        l_draws.append(int(draw.get_text()))
        
    #print('jockeys')    
    for jockey in jockeys:
        #print(jockey.get_text().split('            ')[1])
        #l_jockeys.append(jockey.get_text().split('            ')[1].split(' ')[0])    
        l_jockeys.append(jockey.get_text().strip().split(' ')[0])    

    #print('trainers')
    for trainer in trainers:
        #print(trainer.get_text().split('            ')[1])
        #l_trainers.append(trainer.get_text().split('            ')[1].split(' ')[0])
        l_trainers.append(trainer.get_text().strip().split(' ')[0])
    
    for distance in distances:
        race_dist = distance.get_text().split(' - ')[2]
        race_dist = race_dist.split('M')[0]
        race_dist = int(race_dist)
        #print(race_dist)
        
    for track in tracks:
        race_track = track.get_text() 
        race_track = race_track.upper()
        #print(race_track)
        
        
    for stake in stakes:
        race_stake = stake.get_text()
        race_stake = race_stake.replace(' ','')
        race_stake = race_stake.replace(u'\xa0', u'')
        race_stake = race_stake.split('R')[1].split('.')[0]
        race_stake = int(race_stake)
        #print(race_stake)
    
    #b = predict_horse(horse_name,race_stakes,race_dist,horse_kg,horse_draw,race_track,horse_jockey,horse_trainer)
    # create dataframe that can be used for the predictions
    import pandas as pd
    
    
    columns = ['horse_name',
               'race_stakes',
               'race_dist',
               'horse_kg',
               'horse_draw',
               'race_track',
               'horse_jockey',
               'horse_trainer']
    
    df = pd.DataFrame(columns=columns);#%%       
    
    #print(r_stakes)
    #nnn
        
    df['horse_name'] = l_horses  
    df['horse_jockey'] = l_jockeys
    df['horse_trainer'] = l_trainers
    df['horse_kg'] = l_weights
    df['horse_draw'] = l_draws
    
    df['race_track'] = race_track
    df['race_stakes'] = race_stake 
    df['race_dist'] = race_dist 
    return df  
