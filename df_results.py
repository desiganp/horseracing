#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:55:02 2017

@author: Desigan
"""

from parse_xml import parse_xml

url = 'http://news.tabonline.co.za/Full-Results/2017-Full-Results?fname=TURFFONTEIN%20STANDSIDE@07.09.2017.xml'

df_result = parse_xml(url)

#todo
#1. check if result is available on page
#2. collect the urls for all the result pages and store in db (sql lite)