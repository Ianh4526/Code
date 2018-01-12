
#Probability density Function
#Normal / Gaussian
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.arange(-3,3,0.001)
#creating a range of values
#range from -3 to 3
#incrementing 0.001
plt.plot(x, norm.pdf(x))
#probability density function PDF
plt.show()

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)
plt.hist(values,50)
plt.show()
