#Binomial Probability Mass Function

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n, p = 10, 0.5
x = np.arange(0, 10, 0.001)
plt.plot(x,binom.pmf(x, n, p))
plt.show()
