import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sympy as sp


def question_2():
    tolerance = 0.001
    x_0 = [0, 0]
    # Math notation
    sp.init_printing(use_unicode=True)
    x, y, alpha = sp.symbols('x y alpha', real=True)
    # Function
    f = 14 * ((x - 7)**2 + (y - 2)**2)**0.5 + \
        20 * ((x - 5)**2 + (y + 3)**2)**0.5 + \
        30 * ((x + 6)**2 + (y - 4)**2)**0.5
    # Gradient
    gradient = [f.diff(x), f.diff(y)]
    # d_0
    d = -1 * sp.Matrix(
        [
            gradient[0].evalf(subs={x: x_0[0], y: x_0[1]}),
            gradient[1].evalf(subs={x: x_0[0], y: x_0[1]})
        ]
    )
    exit_condition = sp.Matrix(
        [
            gradient[0].evalf(subs={x: x_0[0], y: x_0[1]}),
            gradient[1].evalf(subs={x: x_0[0], y: x_0[1]})
        ]
    ).norm()
    i = 0  # Iterator
    x_current = x_0

    print('\nSteepest descent search\n')
    print(f'f(x, y) = {f}\n')
    print(f'∇f = {gradient}\n')
    print(f'd_0 = -∇f(x_0) = {d}\n')

    while(exit_condition > tolerance):
        i = i + 1
        gradient = [f.diff(x), f.diff(y)]
        d = -1 * sp.Matrix(
            [
                gradient[0].evalf(subs={x: x_current[0], y: x_current[1]}),
                gradient[1].evalf(subs={x: x_current[0], y: x_current[1]})
            ]
        )
        # x_(k + 1) = x_k + alpha*d
        f_next = f.subs(
            [(x, x_current[0] + alpha*d[0]), (y, x_current[1] + alpha*d[1])]
        )
        f_next = f_next.diff(alpha)
        alpha_value = sp.nsolve(f_next, alpha, 0)
        x_current = [
            x_current[0] + alpha_value * d[0], x_current[1] + alpha_value*d[1]
        ]
        exit_condition = sp.Matrix(
            [
                gradient[0].evalf(subs={x: x_current[0], y: x_current[1]}),
                gradient[1].evalf(subs={x: x_current[0], y: x_current[1]})
            ]
        ).norm()

        print(f'Iteration {i}:\n')
        print(f'd = {d}')
        print(f'α = {alpha_value}')
        print(f'x = {x_current}\n')
