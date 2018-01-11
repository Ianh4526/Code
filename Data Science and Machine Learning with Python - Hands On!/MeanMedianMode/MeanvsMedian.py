import numpy as np



incomes = np.random.normal(27000,15000,10000)
#centered around 27000
#normal distribution and standard deviation 15000
#elements 10000
print "The Mean is: "
print(np.mean(incomes))
#np.mean to calculate the mean of an array

import matplotlib.pyplot as plt
plt.hist(incomes,50)
#50 buckets division for the data
plt.show()

print "\nThe Median is: "
print(np.median(incomes))

print "\nAdding an Outlier"
incomes = np.append(incomes, [100000000])

print "The Mean is: "
print(np.mean(incomes))

print "\nThe Median is: "
print(np.median(incomes))

import matplotlib.pyplot as plt
plt.hist(incomes,50)
plt.show()
