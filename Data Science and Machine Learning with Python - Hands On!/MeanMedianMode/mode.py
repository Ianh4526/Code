import numpy as np


ages = np.random.randint(18, high=90, size=500)

print ages

from scipy import stats
print stats.mode(ages)
