import numpy as np
from scipy.optimize import leastsq
from math import *

def function(p, x):
	# unpack the min into special keywords
	a, b, c, d = p[:4]
	v = eval(model)
	return v

def residual(p, y, x):
	return (y - function(p, x)) ** 2

def regress_data(params, x, y, _model):
	x0 = np.array([1.1] * params)
	global model
	model = _model
	return leastsq(residual, x0, args=(y, x))