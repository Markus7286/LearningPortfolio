# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:30:18 2023

@author: marku
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx ** 2 + yy ** 2) / (xx ** 2 + yy ** 2)
h = plt.contour(x, y, z)