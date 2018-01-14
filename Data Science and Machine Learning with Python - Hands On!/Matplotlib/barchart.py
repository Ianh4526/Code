from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

values = [12, 55, 4, 32, 14]
colors = ['r', 'g', 'b', 'c' , 'm']
labels = ['India', 'United States', 'Russia', 'China', 'Europe']
plt.bar(range(0,5), values, color=colors, label=labels)
plt.title('Student Location')
plt.show()
