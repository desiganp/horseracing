#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:46:44 2017

@author: Desigan
"""

from bs4 import BeautifulSoup

#url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=VAAL@31.01.2017.xml'
h = open('race.html',"r")
#page = 'race.html'
#page = urllib.request.urlopen(url)

soup = BeautifulSoup(h,"lxml")
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

print('horses')
for horse in horses:
    print(horse.get_text())
    l_horses.append(horse.get_text())
print('weights')
for weight in weights:
    print(weight.get_text().split('kg')[0].split('            ')[1])
    l_weights.append(weight.get_text().split('kg')[0].split('            ')[1])
print('draws')    
for draw in draws:
    print(draw.get_text())
    l_draws.append(draw.get_text())
    
print('jockeys')    
for jockey in jockeys:
    print(jockey.get_text().split('            ')[1])
    l_jockeys.append(jockey.get_text().split('            ')[1])    

print('trainers')
for trainer in trainers:
    print(trainer.get_text().split('            ')[1])
    l_trainers.append(trainer.get_text().split('            ')[1])
    

for distance in distances:
    print(distance.get_text().split(' - ')[2])
for track in tracks:
    print(track.get_text())
for stake in stakes:
    print(stake.get_text().replace(' ',''))

#for winner in winners:
#    print(winner.get_text())#