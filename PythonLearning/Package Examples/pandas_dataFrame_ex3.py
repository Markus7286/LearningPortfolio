# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:00:54 2023

@author: marku
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), index=list('abcdef'), columns=list('ABCD'))
print(df)

print(df.loc[lambda df: df.A > 0, :])
print(df.loc[:, lambda df: ['A', 'B']])
print(df.iloc[:, lambda df: [0, 1]])

df2 = pd.read_csv('201711_F3_1_8_2330.csv', encoding='big5', error_bad_lines=False, header=None, names=[
    "日期", "成交股數", "成交金額", "開盤價", "最高價", "最低價", "收盤價", "漲跌價差", "成交筆數"])
print(df2)
df2 = pd.DataFrame(df2)
print(df2.iloc[:, 5])

print(df2.shape)
print(df2.info())