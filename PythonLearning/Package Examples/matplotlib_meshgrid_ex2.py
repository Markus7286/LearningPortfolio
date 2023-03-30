# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:29:58 2023

@author: marku
"""

import numpy as np
import matplotlib.pyplot as plt

nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
print(x)
y = np.linspace(0, 1, ny)
print(y)
print('-----------------------')
xv, yv = np.meshgrid(x, y)
print(xv)
print(yv)