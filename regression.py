import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

import random

# the model we try to fit
def func(X, P):
    return X * X * P[0] + X * P[1] + P[2]

# the residue. Minimize this squared
def resid(P, Y, T):
	return Y - func(T, P)

# some artificially noisy data to fit
x = np.array(range(0, 10))
y = np.array([2 * x[i] * x[i] - 5 + random.uniform(-2, 2) for i in range(0, len(x))])

# init guesses
x0 = np.array([0, 0, 0])

# Returns the coefs that fit the data best
res = leastsq(resid, x0, args=(y, x))
print res
# plot real and line of best fit
plt.plot(x, y)
plt.plot(x, func(x, res[0]))
plt.show()