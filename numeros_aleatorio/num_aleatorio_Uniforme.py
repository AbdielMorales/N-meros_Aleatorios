import numpy as np
mu, sigma = 0.1, 32000
s = np.random.uniform (mu, sigma, 20000)
print (s)

import matplotlib.pyplot as plt
plt.hist(s, 40)
plt.show()
