# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:52:58 2023

@author: marku
"""

import pandas as pd

groups = ["Working", "Dancing", "Cooking", "Movies", "Sports", "Fishing"]
num = [12, 15, 3, 8, 29, 38]
dict = {"groups": groups, "num": num}

mydf = pd.DataFrame(dict)
print(mydf.iloc[:,:]) # All columns and rows
print('--------')
print(mydf.iloc[0, 1]) # The first row and the second column
print('--------')
print(mydf.iloc[0:2,:]) # The first and second row
print('--------')
print(mydf.iloc[:,0]) # All rows and the first column
print('--------')
print(mydf['num']) # All rows['num']
print('--------')
print(mydf.num)

