#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 16:19:46 2020

@author: angiecampo
"""


import pandas as pd
# Part 1: read data into data frame
df =  pd.read_csv("mmc3.csv",engine = 'python')

# Part 2: remove data from 1976 and after 1993
#df = df[ df.completed_visit_status != WITHDREW CONSENT ]
data = df.iloc[:,[0,1,29,30,31]]

# Part 3: make a histogram
#df.hist("Natural",bins=100)