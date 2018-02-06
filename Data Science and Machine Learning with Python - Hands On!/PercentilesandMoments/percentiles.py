#Percentiles
#the point where X% of the values are less than the value


import numpy as np
import matplotlib.pyplot as plt

vals = np.random.normal(0, 0.5, 10000)

plt.hist(vals, 50)
plt.show()

print "the 50 th percentile"
print(np.percentile(vals, 50))
#the 50 perecential for the Vals.

print "the 90 th percentile"
print(np.percentile(vals, 90))


print "the 20 th percentile"
print(np.percentile(vals, 20))
