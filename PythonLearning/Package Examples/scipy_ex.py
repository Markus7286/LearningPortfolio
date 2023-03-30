# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:29:58 2023

@author: marku
"""

import numpy as np
from scipy import linalg
A = np.array([[1, 3, 5], [2, 5, 1], [2, 3, 8]])
print(A)
print(linalg.inv(A))
print(A.dot(linalg.inv(A)))
print('---------------------')

B = np.array([[1, 2], [3, 4]])
print(B)
print(linalg.det(B))
print('---------------------')

C = np.array([[1, 5, 2], [2, 4, 1], [3, 6, 2]])
lna, v = linalg.eig(C)
l1, l2, l3 = lna
#Eigenvalue
print(l1, l2, l3)
print('---------------------')
#Eigenvector
print(v)
print('---------------------')
print(v[:, 0])
print(v[:, 1])
print(v[:, 2])
v1 = np.array(v[:, 0]).T
print('---------------------')
print(v1)
print(linalg.norm(A.dot(v1) - l1 * v1))