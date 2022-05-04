import matplotlib.pyplot as mplot
import numpy as np

def draw_function(lower_range, upper_range, function):
    axes = mplot.figure().subplots()
    x = np.linspace(lower_range, upper_range, 100)
    y = []

    if lower_range <= 0 <= upper_range:
        mplot.axvline(x=0, color='black', lw=1)
        mplot.axhline(y=0, color='black', lw=1)

    for i in x:
        y.append(function(i))
    axes.plot(x, y, "r")

    axes.set_xlabel('X')
    axes.set_ylabel('Y')

    mplot.show()

