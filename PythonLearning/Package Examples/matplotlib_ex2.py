# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:08:13 2023

@author: marku
"""

import numpy as np
import matplotlib.pyplot as plt
#set y, x default
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

#set x, y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16]);
plt.show()

#ro->設定點為紅色圈
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro');
#設定yLabel scale
plt.axis([0, 6, 0, 20])
plt.show()

t = np.arange(0., 5., 0.2)
#r--紅色虛線 bs->blue square g^->green triangle
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()