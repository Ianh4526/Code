#Poisson Probability Mass Function
#gets odd of getting a result
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

mu = 500
x = np.arange(400, 600, 0.5)
plt.plot(x, poisson.pmf(x,mu))
plt.show()
