# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:50:13 2017

@author: PADD
"""

#%% http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

from bs4 import BeautifulSoup
offline = True

if(offline):
    h = open('tab.xml',"r")
    soup = BeautifulSoup(h,"lxml")
    
else:
    url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=VAAL@31.01.2017.xml'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    
races = soup.find_all("td", class_="TABLEHEADER")
winners = soup.find_all("td", class_="TableHeadWinner")
test = soup.find_all("td")


#for race in races:
#    print(race.get_text())
    
#for winner in winners:
#    print(winner.get_text())

start_race_info = False
count = 0
# use a dataframe rather?
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

# add race_date, race_track, race_id, race_stakes, race_dist, race_maidens, race_fillies, race_mares


for t in test:
    #print(t.get_text())
    if("- Race " in t.get_text()): 
        print(t.get_text())
    
    if("WINNER: " in t.get_text()): 
        #print(t.get_text())
        start_race_info = False
    
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
            count = 0
            
    if("Prev" in t.get_text()): 
        #print(t.get_text())
        start_race_info = True
        count = 0
        
        


        
#print(Horse)    
