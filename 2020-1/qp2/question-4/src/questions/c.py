import matplotlib.pyplot as plt
from .utils.points import pc0 as p0
from .utils.points import pc1 as p1
from .utils.points import pc2 as p2
from .utils.points import pc3 as p3

LIMIT = 4.01
START = 2
STEP = 0.01


def function(t, axis):
    if(t < 3):
        if axis == 'x':
            return 0.5*t**2 - 3
        else:
            return 5.5*t**2 - 27*t + 30.5
    else:
        if axis == 'x':
            return -0.5*t**2 + 6*t - 12
        else:
            return -4*t**2 + 30*t - 55


def custom_range(start, stop=None, step=None):
    if stop == None:
        stop = start + 0.0
        start = 0.0

    if step == None:
        step = 1.0

    while True:
        if step > 0 and start >= stop:
            break
        elif step < 0 and start <= stop:
            break
        yield start
        start = start + step


def b_spline():
    x_array = []
    y_array = []

    for i in custom_range(START, LIMIT, STEP):
        x_array.append(function(i, 'x'))
    for i in custom_range(START, LIMIT, STEP):
        y_array.append(function(i, 'y'))

    plt.plot(x_array, y_array, label='B-Spline')
    plt.scatter(p0['x'], p0['y'], label='P0', s=10, color='blue')
    plt.scatter(p1['x'], p1['y'], label='P1', s=10, color='blue')
    plt.scatter(p2['x'], p2['y'], label='P2', s=10, color='blue')
    plt.scatter(p3['x'], p3['y'], label='P3', s=10, color='blue')
