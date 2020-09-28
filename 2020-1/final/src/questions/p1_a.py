import matplotlib.pyplot as plt
import numpy as np
import importlib
importlib.import_module('mpl_toolkits.mplot3d').__path__


def f(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2


def question_1_a():
    x = np.linspace(-5, 5, 30)
    y = np.linspace(-5, 5, 30)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    fig.canvas.set_window_title('Final exam')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Question 1 - item a')
    plt.show()
