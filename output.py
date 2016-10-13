import matplotlib.pyplot as plt
import rlib
import numpy as np

def print_info(model, res):
    pa, pb, pc, pd = res[:4]
    print ("Now printing the best line of fit, using model %s" % model)
    print ("if you did not use a parameter, the value will be 1.1")
    print ("pa ~ %f" % pa)
    print ("pb ~ %f" % pb)
    print ("pc ~ %f" % pc)
    print ("pd ~ %f" % pd)
    print ("Full array:")
    print res

def fmt_str(y, fx):
	data = y - fx
	s_tot = np.sum((y - np.average(y)) ** 2)
	s_res = np.sum((data) ** 2)
	return "$\mu$=%.2f $\sigma$=%.2f $\widetilde{x}$=%.2f $R^2$=%.2f" % (np.average(data), np.std(data), np.median(data), (1 - (s_res) / (s_tot)))

def plot(x, y, result):
	fx = rlib.function(result, x)
	x_t = x + 1970
	yr = y - fx

	fig1 = plt.figure("Data")
	plt.suptitle('Data vs Model', fontsize=20)
	
	frame1=fig1.add_axes((.1,.3,.8,.6))
	plt.plot(x, y)
	plt.plot(x, fx, '-r')
	plt.grid()
	frame2=fig1.add_axes((.1,.1,.8,.2)) 
	plt.plot(x, yr, 'r.')
	plt.plot(x, x * 0, 'black')
	plt.grid()
	plt.figure("Residuals")

	plt.suptitle(fmt_str(y, fx), fontsize=20)
	binwidth = 1
	plt.hist(yr, bins=range(int(min(yr)), int(max(yr) + binwidth), binwidth))

	plt.show()