# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:40:46 2023

@author: marku
"""

import pandas as pd
names = ['Jack', 'John', 'Mary', 'Ben'];
myArray = pd.Series(names)
print(myArray)

print('---------------------')

salartDic = {
    "John": '50000',
    'Jack': '20000',
    'Mary': '45000',
    'Ben': '55000'
    }

myDic = pd.Series(salartDic, index = salartDic.keys())
print(myDic[0])
print(myDic['John'])
print(myDic[[0, 1, 3]])
print(myDic[['John', 'Jack', 'Ben']])