import matplotlib.pyplot as plt
from .utils.points import p0
from .utils.points import p1
from .utils.points import p2
from .utils.points import p3

LIMIT = 1.01
STEP = 0.01


def function(t, axis):
    if axis == 'x':
        return -2*t**3 + 3*t**2 + 6*t - 2
    else:
        return -19*t**3 + 33*t**2 - 15*t + 1


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


def beizer_curve():
    x_array = []
    y_array = []

    for i in custom_range(0, LIMIT, STEP):
        x_array.append(function(i, 'x'))
    for i in custom_range(0, LIMIT, STEP):
        y_array.append(function(i, 'y'))

    plt.plot(x_array, y_array, label='Beizer Curve')
    plt.scatter(p0['x'], p0['y'], label='P0', s=10)
    plt.scatter(p1['x'], p1['y'], label='P1', s=10)
    plt.scatter(p2['x'], p2['y'], label='P2', s=10)
    plt.scatter(p3['x'], p3['y'], label='P3', s=10)
