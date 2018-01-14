from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.001)

plt.plot(x, norm.pdf(x))
plt.plot(x, norm.pdf(x, 1.0, 0.5))
plt.savefig('/home/ian/Code/Data Science and Machine Learning with Python - Hands On!/Matplotlib/MyPlot.png', format='png')
