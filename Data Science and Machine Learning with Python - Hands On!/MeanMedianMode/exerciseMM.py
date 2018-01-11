import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)
print incomes

plt.hist(incomes, 50)
plt.show()

print "\nThe Mean is:   "
print np.mean(incomes)

print "\nThe Median is:   "
print np.median(incomes)
