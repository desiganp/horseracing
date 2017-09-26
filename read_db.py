# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 12:53:25 2017

@author: PADD
"""

import sqlite3 as sql
import pandas as pd

con = sql.connect("racedata.db")

df = pd.read_sql_query('select race_track, race_stakes, race_dist, horse_jockey, horse_trainer, horse_kg, horse_draw, horse_time from results_v1_all where horse_name = "RUN FOR YOUR LIFE"',con)
