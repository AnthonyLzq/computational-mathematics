import sympy as sp


def question_2_b():
    sp.init_printing(use_unicode=True)
    x1, x2 = sp.symbols('x1 x2', real=True)

    def evaluate(function, x):
        return function.evalf(subs={x1: x[0], x2: x[1]})

    h = x1 + x2*2 - 4
    g = -x1

    tolerance = 1e-3
    x0 = sp.Matrix([[-1], [-1]])
    rho = 1  # ρ
    phi = 1  # φ

    f = (x1 + 2)**2 + (x2 - 3)**2
    F = f + rho*h**2 + sp.Max(0, g)**2

    x_current = x0
    gradient = sp.Matrix([F]).jacobian((x1, x2)).T
    grad = evaluate(gradient, x_current)
    FX = evaluate(F, x_current)
    fx = evaluate(f, x_current)

    sigma = 0.1
    beta = 0.1
    s = 1

    j = 0  # iterator

    while grad.norm() > tolerance or sp.Abs(evaluate(h, x_current)) > tolerance or evaluate(g, x_current) > tolerance:
        # direction searching
        d = -grad
        # line searching
        rhs = -(sigma*s*d.T*grad)[0]  # right hand side
        alpha = s
        while FX - evaluate(F, x_current + alpha*d) < rhs:
            alpha *= beta
            rhs *= beta

        print(f'Iteration {j}')
        print(f'x\t\t: {x_current}')
        print(f'f(x)\t\t: {fx}')
        print(f'direction\t: {d}')
        print(f'alpha\t\t: {alpha}\n')

        x_current = x_current + alpha*d
        j += 1
        if sp.Abs(evaluate(h, x_current)) > tolerance:
            rho *= 3
        if evaluate(g, x_current) > tolerance:
            phi *= 3
        F = f + rho*h**2 + phi*sp.Max(0, g)**2
        gradient = sp.Matrix([F]).jacobian((x1, x2)).T
        grad = evaluate(gradient, x_current)
        FX = evaluate(F, x_current)
        fx = evaluate(f, x_current)

    print(f'x\t: {x_current}')
    print(f'f(x)\t: {FX}')
