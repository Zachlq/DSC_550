# Zach Quinn
# DSC 550
# 21 June 2020
# Function: Finds fraction of volume for hyperball incscribed in hypercube 
# Description: Derrives formulas to find fraction of volume of hyperball inscribed in hypercube.
import numpy as np
import scipy.spatial.distance
import pandas as pd
import matplotlib.pyplot as plt
import tqdm
import random

# Defines maximum dimensions 
N_MAX = 100
# Defines 100,000 values.  
M = int(1e+5)
# Defines type.
dims = np.zeros(N_MAX, dtype=np.int32)
# Formula for volume.
volume = np.zeros(N_MAX)
for N in range(1,N_MAX+1):
    y = np.random.uniform(low=-0.5, high=0.5,size=(M,N))
    # Cdist computes distance between 2  matrices y-> (M,N) and [[0..0]]
    # Uses euclidean formula to determine distance between points. 
    dist = scipy.spatial.distance.cdist(y,np.expand_dims(np.zeros(N),0),metric='euclidean')
    p = np.sum(dist < 0.5)/M
    dims[N-1] = N
    volume[N-1] = p
df=pd.DataFrame(data={'dims': dims,'volume': volume})
print(df)

# Plots dimension, volume and displays graph.
plt.plot(df.dims, df.volume,'o-')
plt.title('Fraction of volume of Hyperball inscribed in a Unit Hypercube',size=16)
plt.xlabel('Dimensions',size=12)
plt.ylabel('Volume of inscribed hyperball',size=12)
plt.show()

# Based on the generated graph we can determine:
# That after approximately d < 20 dimensions (approx d = 8 -10), the fraction goes essentially to zero.
# X goes to 100% after approximately 1.3 dimensions (intercept 1.32, 0.99).