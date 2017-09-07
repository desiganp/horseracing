# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:50:13 2017

@author: PADD
"""



def parse_xml(url):
    import urllib
    from bs4 import BeautifulSoup
    offline = False
    
    if(offline):
        h = open('tab.xml',"r")
        soup = BeautifulSoup(h,"lxml")
        
    else:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page,"lxml")
        
    
    meeting = soup.find_all("span", class_ = "HeaderOfRace")
    result_data = soup.find_all("td")
    a = str(meeting)
    race_track = a.split('>')[1].split('<')[0]
    race_date = a.split('>')[2].split(' ')[1].split('<')[0]
    
    
    start_race_info = False
    count = 0
    No = []
    Horse = []
    Jockey = []
    Trainer = []
    Al_Bl = []
    Kg = []
    Dr = []
    Fin = []
    Dist = []
    Time = []
    OP = []
    SP = []
    Prev = []
    r_id = []
    r_stakes = []
    r_dist = []
    r_maidens = []
    r_fillies = []
    r_mares = []
    track = []
    date = []
    
    
    for t in result_data:
        #print(t.get_text())
        if("- Race " in t.get_text()): 
            print(t.get_text())
            race_details = t.get_text()
            raceid = race_details.split('-')[0]
            stakes = race_details.split('-')[2]
            dist = race_details.split('-')[4]
            race_maidens = 'Maiden' in race_details
            race_fillies = 'Fillies' in race_details
            race_mares = 'Mares' in race_details
            # get the race info
        
        if("WINNER: " in t.get_text()): 
            #print(t.get_text())
            start_race_info = False
        
        if(t.get_text()=='SCRATCHED') : 
            #print(t.get_text())
            del No[len(No)-1]
            del Horse[len(Horse)-1]
            del Jockey[len(Jockey)-1]
            count = 0
    
        else:
        
            if(start_race_info):
                if (count == 0):
                    No.append(t.get_text())
                    count = count + 1
                elif (count == 1):
                    Horse.append(t.get_text())
                    count = count + 1
                elif (count == 2):
                    Jockey.append(t.get_text())
                    count = count + 1
                elif (count == 3):
                    Trainer.append(t.get_text())
                    count = count + 1                   
                elif (count == 4):
                    Al_Bl.append(t.get_text())
                    count = count + 1
                elif (count == 5):
                    Kg.append(t.get_text())
                    count = count + 1  
                elif (count == 6):
                    Dr.append(t.get_text())
                    count = count + 1        
                elif (count == 7):
                    Fin.append(t.get_text())
                    count = count + 1       
                elif (count == 8):
                    Dist.append(t.get_text())
                    count = count + 1      
                elif (count == 9):
                    Time.append(t.get_text())
                    count = count + 1         
                elif (count == 10):
                    OP.append(t.get_text())
                    count = count + 1   
                elif (count == 11):
                    SP.append(t.get_text())
                    count = count + 1  
                elif (count == 12):
                    Prev.append(t.get_text())
                    r_id.append(raceid)
                    r_stakes.append(stakes)
                    r_dist.append(dist)
                    r_maidens.append(race_maidens)
                    r_fillies.append(race_fillies)
                    r_mares.append(race_mares)
                    track.append(race_track)
                    date.append(race_date)
                    count = 0
                    
            if("Prev" in t.get_text()): 
                #print(t.get_text())
                start_race_info = True
                count = 0
    
    import pandas as pd
    
    
    columns = ['race_date',
               'race_track', 
               'race_id', 
               'race_stakes', 
               'race_dist', 
               'race_maidens', 
               'race_fillies', 
               'race_mares',
               'horse_num',
               'horse_name',
               'horse_jockey',
               'horse_trainer',
               'horse_Al_Bl',
               'horse_kg',
               'horse_draw',
               'horse_finish',
               'horse_dist',
               'horse_time',
               'horse_op',
               'horse_sp',
               'horse_prev']
    
    df = pd.DataFrame(columns=columns);#%%        
        
          
    df['horse_num'] = No
    df['horse_name'] = Horse  
    df['horse_jockey'] = Jockey
    df['horse_trainer'] = Trainer
    df['horse_Al_Bl'] = Al_Bl
    df['horse_kg'] = Kg
    df['horse_draw'] = Dr
    df['horse_finish'] = Fin
    df['horse_dist'] = Dist
    df['horse_time'] = Time
    df['horse_op'] = OP
    df['horse_sp'] = SP
    df['horse_prev'] = Prev  
    df['race_date'] = date
    df['race_track'] = track
    df['race_id'] = r_id
    df['race_stakes'] = stakes 
    df['race_dist'] = dist 
    df['race_maidens'] = r_maidens
    df['race_fillies'] = r_fillies
    df['race_mares'] = r_mares
        
    return df
