
#Exponential pdf
#Power Law
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

x = np.arange(0, 10, 0.001)
#creating a range of values
#range from 0 to 10
#incrementing 0.001
plt.plot(x, expon.pdf(x))
plt.show()
