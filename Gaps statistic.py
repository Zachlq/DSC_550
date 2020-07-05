# Zach Quinn
# DSC 550
# File Name: Gaps statistic.py
# Program Function: Computes and plots gap statistic vs. k clusters.
# Program Description: Plots the gap statistic of the iris data set.  

from sklearn.datasets import load_iris
import pandas as pd
import scipy
import scipy.cluster.vq
import scipy.spatial.distance
import math
import numpy as np
from numpy.lib import scimath
import matplotlib.pyplot as plt

# Load iris data set from sklearn library.
iris = load_iris()
# Convert iris data set into data frame. 
df = pd.DataFrame(iris.data)
# Create four dimensional array for iris values.
data = df[[0,1,2,3]].values
# Import scipy's euclidean distance function. 
dst = scipy.spatial.distance.euclidean

# Gap function takes data (iris), nrefs and k = 10 clusters. 
def gap(data, refs=None, nrefs=20, ks=range(1,11)):
    # Shapes data.
    shape = data.shape
    if refs==None:
        tops = data.max(axis=0)
        bots = data.min(axis=0)
        dists = scipy.matrix(np.diag(tops-bots))
        rands = scipy.random.random_sample(size=(shape[0],shape[1],nrefs))
        for i in range(nrefs):
            rands[:,:,i] = rands[:,:,i]*dists+bots
    else:
        rands = refs
    # Calculates zeroes.
    gaps = np.zeros((len(ks),))
    # Calculates errors. 
    errors = np.zeros((len(ks),))
    # Adds labels to keyed dictionary. 
    labels = dict((el,[]) for el in ks)
    for (i,k) in enumerate(ks):
        (kmc,kml) = scipy.cluster.vq.kmeans2(data, k)
        disp = sum([dst(data[m,:],kmc[kml[m],:]) for m in range(shape[0])])
        labels[k] = kml

        refdisps = np.zeros((rands.shape[2],))
        for j in range(rands.shape[2]):
            (kmc,kml) = scipy.cluster.vq.kmeans2(rands[:,:,j], k)
            refdisps[j] = sum([dst(rands[m,:,j],kmc[kml[m],:]) for m in range(shape[0])])
        #Computes gaps using scipi log functions. 
        gaps[i] = scimath.log(np.mean(refdisps))-scimath.log(disp)
        #Computes errors using scipi square root, log, and numpy mean functions. 
        errors[i] = scimath.sqrt(sum(((scimath.log(refdisp)-np.mean(scimath.log(refdisps)))**2) \
                                for refdisp in refdisps)/float(nrefs)) * scimath.sqrt(1+1/nrefs)
    # Returns gaps, labels and errors. 
    return gaps, labels, errors

# Creates function to plot gap statistic. 
def gap_stat_plt(gaps, errors):
    xval = range(1, len(gaps)+1)
    yval = gaps
    plt.errorbar(xval, yval, xerr= None, yerr = errors)
    plt.xlabel('Clusters K')
    plt.ylabel('Gap')
    plt.title('Gap Statistics: Gap vs. Clusters K')
    plt.show()
    
gaps, labels, errors = gap(data, refs = None, nrefs = 20, ks= range(1,11))

gap_stat_plt(gaps, errors)

# Generates second gap statistic plot. 
gaps, labels, errors = gap(data, refs = None, nrefs = 30, ks= range(1,11))

gap_stat_plt(gaps, errors)

# Answers to Excercise Three:

# Number 1:
# The value of k between the elbow points was estimated to be k = 2. This is evident in the output of the first plot.
# The gap statistic calculation estimated k = 3 to be the optimal value for k. 

# Number 2: 
# The estimates of the values of k derived from figures 1 and 2 are nearly identical to that conveyed by the iris data set.
# Specifically, the graphs suggest the optimal point of k to be three, and there are three species of flower in iris.

# Number 3: 
# In my opinion, the k means test seemed to be more reliable because there is a clear elbow point and apex so, visually, it is easier to designate a value for k. 

# References

# Tibshrani, R. Walther, G. Hastie, T. (2001). Estimating the number of clusters in a data set via the gap statistic. Royal Statistical Society. 63, 2, pp. 411 - 423.
# The Glowing Python. (2019). A Visual Introduction to the Gap Statistics. Glowing Python.
# The Data Science Lab. (2013). Finding the K in K-Means Clustering. Data Science Lab.
# Vejdemo-Johansson, M. (2013). Implementing Gap Stat. Github. 
