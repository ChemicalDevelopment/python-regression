"""
ChemicalDevelopment 2016

License: GPLv3

Python regression and graphing from csv

To use a csv, assure that the first row is blank, or has titles. No data should be in the first row

Example:

"
Date, 

"

"""


import argparse
import input
import output
import rlib

parser = argparse.ArgumentParser(description='ChemicalDevelopment python regression.')

parser.add_argument("--file", type=str, default="data.csv", help="use a file for input data")
parser.add_argument("--dateformat", type=str, default="", help="use special date format")
parser.add_argument("--xcolumn", type=str, default="0",help="x column for fitting. Use int for index, or string for name of column")
parser.add_argument("--ycolumn", type=str, default="1",help="y column for fitting. Use int for index, or string for name of column")
parser.add_argument("--model", type=str, default="pa*x+pb", help="model for fitting. Use pa, pb, ..., pf then use p[i]. Set this number below")
parser.add_argument("--parameters", type=int, default=4, help="number of parameters")

args = parser.parse_args()

file = args.file; model = args.model; xcol = args.xcolumn; ycol = args.ycolumn; dfmt = args.dateformat; parameters = args.parameters

if parameters < 4:
	parameters = 4

print("Running python regression now using file %s and model y~%s" % (file, model))

x, y = input.get_data(file, dfmt, xcol, ycol)

result = rlib.regress_data(parameters, x, y, model)[0]

output.print_info(model, result)

output.plot(x, y, result)