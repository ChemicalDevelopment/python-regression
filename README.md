# Regression

## installation

make sure you have `python` and `pip` installed (not python3)

run `pip install -r requirements.txt`

## info

Tool for regression of csv files.

Run `python main.py --help` for info

With csv, you can get from google sheets, or most websites with large datasets will allow download.

You can see examples in `./data/` directory.

**The first line should not contain data**

It should contain the title of the column. For example `Price`, `Date`, and the like are used

For dates, use `--dateformat` option.

The default model is linear, `a*x+b`, see below for more.

## dates

say we have `data.csv`

```
Date,      Open,  High,   . . . 
2009-07-01,143.50,144.66, . . .
.
.
.
```

To find the relationship between `Date` and `High`, Run

`python main.py --xcolumn Date --ycolumn High --dateformat "%Y-%m-%d" --model "a*x+b"`

The dateformat is exactly what is sounds like.

The `Date` column has the year (`%Y`) then a `-` followed by the month (`%m`), then another `-` and finally the day (`%d`).

If you had `January 2009 01`, use `--dateformat "%B %Y %d"`

If you had `Jan 2009 01`, use `--dateformat "%b %Y %d"`

For more info, check:

https://www.tutorialspoint.com/python/time_strptime.htm


## model

You can use any model you'd like with this.

use `x` for the data in xcolumn. `a`, `b`, `c`, and `d` are all variables you use.

For example, using `a*x+b` will pick `a` and `b` such that the sum of the squares between `a*x+b` and `y` dataset are minimized

For exponential fit, `a*(x**b)`.

This just pulls an `eval` on the code. 

If you need more than 4 parameters, just use `--parameters $n`.

Then, use `p[i]` for the ith parameter (a=p[0], b=p[1], c=p[2], d=p[3])

For example, `--model "a*x+b"` is the same as `--model "p[0]*x+p[1]"`


## plot

A window pops up with two windows.

One is the actual dataset (in blue), and the model (in red). The lower portion also has the residuals plotted in red dots.

The second is a histogram of the residuals, with some info at the top, such as mean, standard deviation, mean, and `R^2` value.

The `a`, `b`, and all parameters which are used are printed in the terminal.

