# Zach Quinn
# DSC 550 
# 21 June 2020
# Program Function: Plots volume of hypersphere vs. dimension.
# Program Description: Uses matplotlib package to plot the volume vs. dimension of a sphere in high dimensional space.
import numpy as np
import sys

import math

import matplotlib.pyplot as plt

# Defines blank list of random values for x
x = []
# Defines blank list of random values for y
y = []
for dimension in range(50):
# Establishes dimension variable.
    n = float(dimension)
# Defines volume equation.
    volume = math.pi**(n/2)/math.gamma(n/2 + 1)
# Adds n to x axis.
    x.append(n)
# Adds volume to y axis. 
    y.append(volume)
# Creates title. 
plt.title('Volume vs. Dimension of a Hypersphere')
# Labels x axis.
plt.xlabel('Dimension (d)')
# Labels y axis.
plt.ylabel('Volume')
# Plots points.
plt.plot(x, y)
# Displays graph.
plt.show()
