# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:23:02 2017

@author: PADD
"""

import sqlite3 as sql
import pandas as pd

con = sql.connect("racedata.db")

df = pd.read_sql_query('select max(substr(race_date, 7, 4) || "/" || substr(race_date, 4, 2) || "/" || substr(race_date, 1, 2)) as "MaxDate" from results_v1_all',con)
last_date_reversed = str(df['MaxDate'][0])
last_date = last_date_reversed.split('/')[2] + '/' + last_date_reversed.split('/')[1] + '/' + last_date_reversed.split('/')[0]

df = pd.read_sql_query('select * from results_v1_all where race_date == "'+last_date+'"',con);
