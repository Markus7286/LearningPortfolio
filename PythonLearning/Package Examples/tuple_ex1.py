# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:17:23 2023

@author: marku
"""

tp1 = ()
print(tp1)
tp2 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tp2)
print(sum(tp2))
print('--------------------------')
print(tp2[2:5])
print(tp2[-1])
tp3 = tuple([2*x for x in range(1, 8)])
print(tp3)
print('--------------------------')
tp4 = tuple('Ivy Lin')
print(tp4)
tp5 = ("John", "Mary", "Lex")
print(tp5)
print(len(tp5))
print(tp4 + tp5)
print('--------------------------')
tp6 = tuple([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(tp6)
print(max(tp6))
print(min(tp6))