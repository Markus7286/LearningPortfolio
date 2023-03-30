# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:16:41 2023

@author: marku
"""

import numpy as np
import matplotlib.pyplot as plt

data = {
        "a": np.arange(50),
        "c": np.random.randint(0, 50, 50),
        "d": np.random.randn(50)
        }
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

#scatter(xInput, yInput, c for mark color, s for mark size, data)
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()