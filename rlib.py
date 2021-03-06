import numpy as np
from scipy.optimize import leastsq
from math import *

# evaluates the function. Requires a global model to be declared
def function(p, x):
	# unpack the min into special keywords
	a, b, c, d = p[:4]
	v = eval(model)
	return v

# returns residual
def residual(p, y, x):
	return (y - function(p, x))

# regresses the data and returns relevant info
def regress_data(params, x, y, _model):
	x0 = np.array([1.1] * params)
	global model
	model = _model
	return leastsq(residual, x0, args=(y, x))

# returns r^2 val
def r2(y, fx):
	s_r = np.sum((y - fx) ** 2)
	s_t = np.sum((y - np.average(y)) ** 2)
	return (1 - s_r / s_t) ** 2
