# Zach Quinn
# DSC 550 
# 21 June 2020
# Program Function: Plots volume of hypersphere vs. dimension.
# Program Description: Uses matplotlib package to plot the volume vs. dimension of a sphere in high dimensional space.
import numpy as np
import sys

import math

import matplotlib.pyplot as plt

x = []
y = []
for dimension in range(50):
    n = float(dimension)
    volume = math.pi**(n/2)/math.gamma(n/2 + 1)
    x.append(n)
    y.append(volume)
plt.title('Volume vs. Dimension of a Hypersphere')
plt.xlabel('Dimension (d)')
plt.ylabel('Volume')
plt.plot(x, y)
plt.show()
