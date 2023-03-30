# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:25:33 2023

@author: marku
"""

#set沒有重複元素
#set裡面的element不可複製，也沒有順序
#可以用{}建立set
st1 = set()
st2 = set([1, 2, 3, 4, 5])
print(st2)
st3 = {'a', 'b', 'c', 'd', 'e'}
print('-----------------------')
st3.add('f')
print(st3)
st3.remove('d')
print(st3)
print('-----------------------')
print(st3.union(st2))
st5 = {'a', 'b', 'c', 'd', 'e'}
print(st3.intersection(st5))
print(st3.difference(st5))
