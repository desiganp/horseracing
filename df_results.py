#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:55:02 2017

@author: Desigan
"""

from parse_xml import parse_xml

url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=TURFFONTEIN%20STANDSIDE@07.09.2017.xml'

df_result = parse_xml(url)

#%%

#todo
#1. check if result is available on page
#2. collect the urls for all the result pages and store in db (sql lite)

url_list = []

#2009
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=01/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=02/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=03/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=04/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=05/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=06/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=07/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=08/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=09/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=10/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=11/2009')
#url_list.append('http://news.tabonline.co.za/Full-Results/2009-Full-Results?racesformonth=12/2009')



#2010
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=01/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=02/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=03/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=04/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=05/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=06/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=07/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=08/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=09/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=10/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=11/2010')
url_list.append('http://news.tabonline.co.za/Full-Results/2010-Full-Results?racesformonth=12/2010')



#2011
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=01/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=02/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=03/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=04/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=05/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=06/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=07/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=08/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=09/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=10/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=11/2011')
url_list.append('http://news.tabonline.co.za/Full-Results/2011-Full-Results?racesformonth=12/2011')


#2012
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=01/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=02/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=03/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=04/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=05/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=06/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=07/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=08/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=09/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=10/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=11/2012')
url_list.append('http://news.tabonline.co.za/Full-Results/2012-Full-Results?racesformonth=12/2012')


#2013
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=01/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=02/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=03/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=04/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=05/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=06/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=07/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=08/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=09/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=10/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=11/2013')
url_list.append('http://news.tabonline.co.za/Full-Results/2013-Full-Results?racesformonth=12/2013')

#2014
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=01/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=02/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=03/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=04/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=05/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=06/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=07/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=08/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=09/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=10/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=11/2014')
url_list.append('http://news.tabonline.co.za/Full-Results/2014-Full-Results?racesformonth=12/2014')

#2015
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=01/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=02/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=03/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=04/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=05/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=06/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=07/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=08/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=09/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=10/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=11/2015')
url_list.append('http://news.tabonline.co.za/Full-Results/2015-Full-Results?racesformonth=12/2015')

#2016
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=01/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=02/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=03/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=04/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=05/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=06/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=07/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=08/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=09/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=10/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=11/2016')
url_list.append('http://news.tabonline.co.za/Full-Results/2016-Full-Results?racesformonth=12/2016')

#2017
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=01/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=02/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=03/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=04/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=05/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=06/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=07/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=08/2017')
url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=09/2017')
#url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=10/2017')
#url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=11/2017')
#url_list.append('http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=12/2017')

#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=03/2017
#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=04/2017
#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=05/2017
#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=06/2017
#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=07/2017
#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=08/2017
#http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=09/2017
#%%
#url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?racesformonth=01/2017'
url = url_list[2]
import urllib
from bs4 import BeautifulSoup
#import time
#import pandas as pd
from parse_xml import parse_xml

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
    meeting_page = urllib.request.urlopen(meeting)
    meeting_soup = BeautifulSoup(meeting_page,"lxml")
    if('Race Information Currently Unavailable' in str(meeting_soup.get_text())):
        print('No race info')
    else:
        #df[i] = pd.DataFrame()
        df.append(parse_xml(meeting))
    #time.sleep(5)

# write month data to database
#%%
import sqlite3 as sql
import pandas as pd

from write_month import write_month_data

df = write_month_data(url_list[len(url_list)-1])

con = sql.connect("racedata.db")
for d in df:
    pd.io.sql.to_sql(d, "results", con, if_exists='append',)
