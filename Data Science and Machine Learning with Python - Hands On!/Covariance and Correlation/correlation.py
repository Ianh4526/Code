# Normalize everithyng by their standard deviations, giving you an easier understandingof from -1 to 1

import matplotlib.pyplot as plt
import numpy as np

def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]


def covariance(x,y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y))/ (n-1)

def correlation(x,y):
    stddevx = x.std()
    stddevy = y.std()
    return covariance(x,y) / stddevx / stddevy #check if divided by 0


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

print correlation(pageSpeeds, purchaseAmount)

print "Numpy can do it easier with corrcoef"
print np.corrcoef(pageSpeeds, purchaseAmount)
#array that give the relation betewn the var given

purchaseAmount = 100 - pageSpeeds*3
plt.scatter(pageSpeeds, purchaseAmount)
print correlation(pageSpeeds, purchaseAmount)
plt.show()
