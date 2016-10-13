import csv
import numpy as np
from datetime import datetime

# Jan 1 1970 in datetime
epoch = datetime.utcfromtimestamp(0)

# gets x array
def get_x_array(xdata, fdata, xcol, dfmt):
	try:
		xcol_i = int(xcol)
	except:
		xcol_i = np.where(fdata[0] == xcol)[0][0]
	arr = []
	if (xdata != None):
		arr = xdata
	if (fdata != None):
		arr = arr + [fdata[i][xcol_i] for i in range(1, len(fdata))]
	#Cast to float
	if (dfmt == ""):
		return [float(eval(arr[i])) for i in range (0, len(arr))]
	else:
		return [(datetime.strptime(arr[i], dfmt) - epoch).total_seconds() / (60 * 60 * 24 * 30 * 12) for i in range(0, len(arr))]

# gets y array
def get_y_array(ydata, fdata, ycol):
	try:
		ycol_i = int(ycol)
	except:
		ycol_i = np.where(fdata[0] == ycol)[0][0]
	arr = []
	if (ydata != None):
		arr = ydata
	if (fdata != None):
		arr = arr + [fdata[i][ycol_i] for i in range(1, len(fdata))]
	#Cast to float
	return [float(eval(arr[i])) for i in range (0, len(arr))]

def get_file_data(file, dfmt, xdata, xcol, ydata, ycol):
	if (file != ""):
		csvfile = open(file, 'rb')
		rdr = csv.reader(csvfile, delimiter=',', quotechar="|")
		csv_data = []
		for row in rdr:
			csv_data.append(row)
		csv_data = np.array(csv_data)
	else:
		csv_data = None
	x = get_x_array(xdata, csv_data, xcol, dfmt)
	y = get_y_array(ydata, csv_data, ycol)
	return (x, y)

# gets data in tuple (x, y)
def get_data(file, dfmt, xcol, ycol, xdata, ydata):
	xx, yy = get_file_data(file, dfmt, xdata, xcol, ydata, ycol)
	return (np.array(xx), np.array(yy))