# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:48:14 2022

@author: SPTINT-08
"""

import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/Public/python/athlete_events.csv')
plt.bar(data[data['Year'] ==2000]['Medal'].value_counts())
plt.title("Bar chart")
plt.xlabel("Medal")
plt.ylabel("Year")
plt.show()
