
#Uniform Distribution
import numpy as np
import matplotlib.pyplot as plt

values = np.random.uniform(-10.0, 10.0, 100000)
#range from -10 to 10
#give me 100000 values
plt.hist(values,50)
#buckets are the columns of the hist
plt.show()
