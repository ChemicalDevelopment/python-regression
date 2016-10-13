"""
ChemicalDevelopment 2016

License: GPLv3

Python regression and graphing from csv

"""

# parsing
import argparse

# our other 3 files
import input
import output
import rlib

parser = argparse.ArgumentParser(description='ChemicalDevelopment python regression.')
# commandline args
parser.add_argument("--file", type=str, default="data.csv", help="use a file for input data")
parser.add_argument("--dateformat", type=str, default="", help="use special date format")
parser.add_argument("--xcolumn", type=str, default="0",help="x column for fitting. Use int for index, or string for name of column")
parser.add_argument("--ycolumn", type=str, default="1",help="y column for fitting. Use int for index, or string for name of column")
parser.add_argument("--model", type=str, default="a*x+b", help="model for fitting. Use a, b, c, d then use p[i]. Set this number below")
parser.add_argument("--parameters", type=int, default=4, help="number of parameters")

args = parser.parse_args()

# create refs
file = args.file; model = args.model; xcol = args.xcolumn; ycol = args.ycolumn; dfmt = args.dateformat; parameters = args.parameters

# minimum of 4 parameters
if parameters < 4:
	parameters = 4

# log info
print("Running python regression now using file %s and model y~%s" % (file, model))

# unpack data from file
x, y = input.get_data(file, dfmt, xcol, ycol)

# perfrom regression
result = rlib.regress_data(parameters, x, y, model)[0]

# print all our info
output.print_info(model, result)

# plot diagrams
output.plot(x, y, result, dfmt)