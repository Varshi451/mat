# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:48:07 2022

@author: SPTINT-08
"""

import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/Public/python/athlete_events.csv')
plt.bar(data[data['Sex'] =='M']['Medal'].value_counts())
plt.title("Bar chart")
plt.xlabel("Medal")
plt.ylabel("Male")
plt.show()
