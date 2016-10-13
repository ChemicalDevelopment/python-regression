import csv
import numpy as np
from datetime import datetime

epoch = datetime.utcfromtimestamp(0)

def get_x_array(data, xcol, dfmt):
	try:
		xcol_i = int(xcol)
	except:
		xcol_i = np.where(data[0] == xcol)[0][0]
	print xcol_i
	#Years since epoch
	if not (dfmt == ""):
		ret = np.array([float((datetime.strptime(data[i][xcol_i], dfmt)-epoch).total_seconds() / (60 * 60 * 24 * 30 * 12)) for i in range (1, len(data))])
	else:
		ret = np.array([float(data[i][xcol_i]) for i in range (1, len(data))])
	return ret

def get_y_array(data, ycol):
	try:
		ycol_i = int(ycol)
	except:
		ycol_i = np.where(data[0] == ycol)[0][0]
	#Cast to float
	return np.array([float(data[i][ycol_i]) for i in range (1, len(data))])

def get_data(file, dfmt, xcol, ycol):
	csvfile = open(file, 'rb')
	rdr = csv.reader(csvfile, delimiter=',', quotechar="|")
	csv_data = []
	for row in rdr:
		csv_data.append(row)
	csv_data = np.array(csv_data) 
	x = get_x_array(csv_data, xcol, dfmt)
	y = get_y_array(csv_data, ycol)
	return (x, y)