import matplotlib.pyplot as plt
import numpy as np
import importlib
importlib.import_module('mpl_toolkits.mplot3d').__path__


def f(x, y):
    return 14*np.sqrt((x - 7)**2 + (y - 2)**2) + 20*np.sqrt((x - 5)**2 + (y + 3)**2) + 30*np.sqrt((x + 6)**2 + (y - 4)**2)


def question_1():
    x = np.linspace(-7, 7, 30)
    y = np.linspace(-7, 7, 30)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    fig.canvas.set_window_title('Qualified 5')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Question 1')
    plt.show()
