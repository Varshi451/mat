# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:48:10 2022

@author: SPTINT-08
"""

import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/Public/python/athlete_events.csv')
plt.scatter(data['Height'],data['Weight'])
plt.title("Scatter plot")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
