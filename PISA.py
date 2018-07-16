# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
import numpy as np

sco={'Score': 'float64'}

math_dataframe = pd.read_csv('Math.csv', dtype=sco)
# math_dataframe = pd.read_csv('Math.csv', header=None)
math_dataframe['Math Rank'] = np.linspace(1, math_dataframe.shape[0], num = math_dataframe.shape[0],
              dtype= 'int64')
print(math_dataframe)


#print(os.listdir(os.curdir))

science_dataframe = pd.read_csv('Science.csv', dtype=sco)
science_dataframe['Science Rank'] = np.linspace(1, science_dataframe.shape[0], num = science_dataframe.shape[0],
              dtype= 'int64')
print(science_dataframe)


reading_dataframe = pd.read_csv('Reading.csv', dtype=sco)
reading_dataframe['Reading Rank'] = np.linspace(1, reading_dataframe.shape[0], num = reading_dataframe.shape[0],
              dtype= 'int64')
print(reading_dataframe)

dfs = [math_dataframe, science_dataframe]
total_dfs = reading_dataframe.merge(dfs[0], on = ['Country'] , how = 'right')
print(total_dfs)
 
total_dfs = total_dfs.merge(dfs[1], on = ['Country'] , how = 'right')
print(total_dfs)

names = {'Score_x': 'Reading Score', 'Score_y': 'Math Score', 'Score': 'Science Score'}

total_dfs.rename(columns = names, inplace = True)
#print(total_dfs.columns)
print(total_dfs)

total_dfs['Total Country Score']= np.round(total_dfs['Math Score'] + total_dfs['Science Score'] + total_dfs['Reading Score'], 0)
print(total_dfs)
total_dfs.sort_values('Total Country Score', inplace=True, ascending=False)
total_dfs.to_csv('PISA_Total_Country_Rank.csv', index = False)








