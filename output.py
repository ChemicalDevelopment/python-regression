import matplotlib.pyplot as plt
import rlib
import numpy as np

# prints out the model, and the best fit coefficients
def print_info(model, res):
    pa, pb, pc, pd = res[:4]
    print ("Now printing the best line of fit, using model %s" % model)
    print ("if you did not use a parameter, the value will be 1.1")
    print ("a ~ %f" % pa)
    print ("b ~ %f" % pb)
    print ("c ~ %f" % pc)
    print ("d ~ %f" % pd)
    print ("Full array:")
    print res

# formats a string with average, stddev, median, and r^2 value
def fmt_str(y, fx):
	data = y - fx
	return "$\mu$=%.2f $\widetilde{x}$=%.2f $\sigma$=%.2f $R^2$=%.2f" % (np.average(data), np.median(data), np.std(data), rlib.r2(y, fx))

# prints technical details
def print_details(x, y, result):
	fx = rlib.function(result, x)
	data = y - fx
	print "\n\nFit\n~~~~"
	print "R^2: %.2f" % rlib.r2(y, fx)
	print "\n\nResiduals\n~~~~"
	print "Mean Residual: %.2f" % np.average(data)
	print "Median Residual: %.2f" % np.median(data)
	print "Standard Deviation Residual: %.2f" % np.std(data)
	print "\n\n"

# generates revelant plots
def plot(x, y, result, dfmt):
	print_details(x, y, result)
	fx = rlib.function(result, x)
	if dfmt == "":
		x_t = x
	else:
		x_t = x + 1970
	yr = y - fx
	fig1 = plt.figure("Data")
	plt.suptitle('Data vs Model', fontsize=20)
	
	frame1=fig1.add_axes((.1,.3,.8,.6))
	plt.plot(x_t, y)
	plt.plot(x_t, fx, '-r')
	plt.grid()
	frame2=fig1.add_axes((.1,.1,.8,.2)) 
	plt.plot(x_t, yr, 'r.')
	plt.plot(x_t, x * 0, 'black')
	plt.grid()
	plt.figure("Residuals")

	plt.suptitle(fmt_str(y, fx), fontsize=20)
	binwidth = 1
	plt.hist(yr, bins=range(int(min(yr)), int(max(yr) + binwidth + 1), binwidth))

	plt.show()