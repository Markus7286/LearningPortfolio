# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:57:34 2023

@author: marku
"""

import pandas as pd
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
print(df.tail())

print('-----------------------------')

df = pd.read_csv('MI_INDEX.csv', encoding='big5')
print(df)

print('-----------------------------')

df = pd.DataFrame(df)
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())
print(df.head())
print(df.index)
print(df.columns)
print(df.tail().T)