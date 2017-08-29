# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:50:13 2017

@author: PADD
"""

import urllib
url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=VAAL@31.01.2017.xml'
file = urllib.request.urlopen(url)
data = file.read()
file.close()
data = str(data)

#%%
import xml.etree.ElementTree as ET

tree = ET.parse('tab.xml')
root = tree.getroot()

#%% http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html

from bs4 import BeautifulSoup

url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=VAAL@31.01.2017.xml'
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page,"lxml")
races = soup.find_all("td", class_="TABLEHEADER")
winners = soup.find_all("td", class_="TableHeadWinner")

for race in races:
    print(race.get_text())
    
for winner in winners:
    print(winner.get_text())