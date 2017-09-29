#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:03:25 2017

@author: Desigan
"""

def write_month_data(url,year):
    import urllib
    from bs4 import BeautifulSoup
    import time
    #import pandas as pd
    from parse_xml import parse_xml
    import sys
    import os
    
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    
    #meeting = soup.find_all("a",href = True)
    meetings_for_month = []
    import re
    for possible_link in soup.find_all('a', {'href': re.compile(r'fname.*')}):
        #print(url.split('?')[0] + possible_link.attrs['href'])
        meetings_for_month.append(url.split('?')[0] + str(possible_link.attrs['href']).replace(' ','%20'))
    
    
    df = [] 
    for meeting in meetings_for_month:
        #determine if 'Race Information Currently Unavailable'
        print(meeting)
        try:
            meeting_page = urllib.request.urlopen(meeting,timeout=10)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
            print(exc_type, fname, exc_tb.tb_lineno)
        
        meeting_soup = BeautifulSoup(meeting_page,"lxml")
        if('Race Information Currently Unavailable' in str(meeting_soup.get_text())):
            print('No race info')
        else:
            #df[i] = pd.DataFrame()
            d = parse_xml(meeting,year)
            if (len(d) > 0):
                df.append(d)
        time.sleep(2)
    
    # write month data to database
    return df
