import sympy as sp


def question_1_c():
    sp.init_printing(use_unicode=True)
    x1, x2 = sp.symbols('x1 x2', real=True)
    x = sp.Matrix([[0], [0]])

    def evaluate(function, x):
        return function.evalf(subs={x1: x[0], x2: x[1]})

    f = (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
    hessian = sp.hessian(f, (x1, x2))

    is_positive_definite = evaluate(hessian, x).is_positive_definite
    print('\nThe hessian of the function is:')
    print(hessian)
    print('\nSo, if we want to show whether the function is convex or not, to do that we are going to use determinate whether is definite positive or not.')
    print('To do that we are going to fix x = (x1, x2) = (0, 0), so the value of the hessian in that point is:')
    print(evaluate(hessian, x))
    print('\nSince the value is a matrix, we call the property "is_positive_definite" of a sympy matrix, and it will return us the following value:')
    print(is_positive_definite)
    print('So, we can affirm that this function is not convex.')
