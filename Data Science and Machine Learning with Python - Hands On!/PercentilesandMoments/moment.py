#Moment
#1st Mean
#2nd Variance
#3rd Skew lopside of the graf left negative right positive
#4th Kurtosis the more up it goes the mor kurtosis it is

import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

print "First Moment Mean"
print(np.mean(vals))

print "2nd Moment Variance"
print(np.var(vals))

import scipy.stats as sp
print "3rd Moment Skew"
print(sp.skew(vals))

print "4th Moment Kurtosis"
print(sp.kurtosis(vals))
