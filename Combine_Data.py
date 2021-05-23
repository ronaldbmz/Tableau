# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:25:41 2021

@author: rohti
"""

import pandas as pd

df_202011 = pd.read_csv('202011-citibike-tripdata.csv')

df_202012 = pd.read_csv('202012-citibike-tripdata.csv')

df_202101 = pd.read_csv('202101-citibike-tripdata.csv')

df_202102 = pd.read_csv('202102-citibike-tripdata.csv')

df_202103 = pd.read_csv('202103-citibike-tripdata.csv')

df_202104 = pd.read_csv('202104-citibike-tripdata.csv')


df_final = df_202011.append(df_202012)

df_final = df_final.append(df_202101)
df_final = df_final.append(df_202102)
df_final = df_final.append(df_202103)
df_final = df_final.append(df_202104)