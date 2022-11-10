# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 01:46:04 2022

@author: SPTINT-08
"""

import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/Public/python/athlete_events.csv')
plt.hist(data['Age'])
plt.title("Histogram")
plt.show()
