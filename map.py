# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 18:38:08 2018

@author: Roshan
"""
import pandas as pd
df = pd.read_csv('Census.csv')
'''
dff = df.groupby('STNAME')['CTYNAME'].nunique()
max_count= dff.argmax()
dff = df.groupby(['STNAME','CTYNAME']).sum().reset_index()
'''
dff = df.copy()
dff.set_index('CTYNAME',inplace=True)
population = dff.iloc[:,1:6]
population_t = population.transpose()
abs_value = population_t.max() - population_t.min()
print(abs_value.argmax())