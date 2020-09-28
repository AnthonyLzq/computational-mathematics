import sympy as sp


def question_1_d(x: float, y: float):
    sp.init_printing(use_unicode=True)
    x1, x2, a = sp.symbols('x1 x2 a', real=True)

    def evaluate(func, x):
        return func.evalf(subs={x1: x[0], x2: x[1]})

    f = (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
    gradient = sp.Matrix([f]).jacobian((x1, x2)).T
    hessian = sp.hessian(f, (x1, x2))

    tolerance = 1e-13

    sigma = 0.1
    beta = 0.1
    s = 1

    j = 0
    x = sp.Matrix([[x], [y]])
    fx = evaluate(f, x)
    grad = evaluate(gradient, x)

    while (grad.norm() > tolerance):

        # direction searching
        d = -grad

        # line searching
        rhs = -(sigma*s*d.T*grad)[0]  # right hand side
        alpha = s
        while fx - evaluate(f, x + alpha*d) < rhs:
            alpha *= beta
            rhs *= beta

        print(f'Iteration {j}')
        print(f'x\t\t: {x}')
        print(f'f(x)\t\t: {fx}')
        print(f'direction\t: {d}')
        print(f'alpha\t\t: {alpha}\n')
        print()

        # Updating
        x = x + alpha*d
        j += 1
        fx = evaluate(f, x)
        grad = evaluate(gradient, x)

    print(f'x\t: {x}')
    print(f'f(x)\t: {fx}')
