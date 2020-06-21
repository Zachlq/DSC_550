import pandas as pd
import math
import matplotlib.pyplot as plt
# Defines blank list of random x values.
x = []
# Defines blank list of random y values.
y = []
# Creates data frame for dimension and radius.
radius = pd.DataFrame(columns=['Dimension', 'Radius'])
# Iterates for d = 1 - 101. 
for dimension in range(1,101):
        n = float(dimension)
        volume = 1
# Defines radius equation
        radius = math.sqrt(1 / (math.pi * n))
# Adds n to x axis.
        x.append(n)
# Adds radius to y axis. 
        y.append(radius)
for i in range(1,len(x)):
        radius_df = pd.DataFrame({'Dimension': x, 'Radius': y})
print(radius_df)
# Defines labels.
plt.xlabel('Dimension')
plt.ylabel('Volume')
plt.plot(x, y)
# Titles graph.
plt.title('Radius of a Hypersphere')
# Displays graph.
plt.show()