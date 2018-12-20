# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:37:44 2018

@author: 762309
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt


data_file = pd.read_csv('Position_Salaries.csv')
x = data_file.iloc[:,1:2].values
y = data_file.iloc[:,2].values

from sklearn.tree import DecisionTreeRegressor
dtr = DecisionTreeRegressor()
dtr.fit(x,y)
y_pred = dtr.predict(6.5)

plt.scatter(x,y)
x_grid = np.arange(min(x),max(x),0.1)
x_grid = x_grid.reshape((len(x_grid),1))
plt.plot(x_grid,dtr.predict(x_grid),color='red')
plt.show()