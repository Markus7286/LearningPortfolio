# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 11:38:55 2023

@author: marku
"""

import numpy as np
import matplotlib.pyplot as plt
a = np.arange(25)
a = a.reshape((5, 5))
b = np.arange(25)
b = a.reshape((5, 5))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b)
print(a > b)
print(a.dot(b))

x = np.arange(0, 3 * np.pi, 0.001)
y = np.sin(x)

plt.plot(x, y)
plt.show()

c = np.zeros((10, 3))
print(c)
print('--------------------')
d = c.T
print(d)
print('--------------------')
e = np.reshape(d, (5, 6))
print(e)

#ravel->二維轉為一維
f = np.arange(10)
print(f)
print('--------------------')
f = f.reshape((2, 5))
print(f)
print('--------------------')
print(np.ravel(f))