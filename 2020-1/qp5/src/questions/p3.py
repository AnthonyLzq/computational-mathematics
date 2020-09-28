import sympy as sp


def question_3():
    tolerance = 0.001
    x_0 = [0, 0]
    # Math notation
    sp.init_printing(use_unicode=True)
    x, y, alpha = sp.symbols('x y alpha', real=True)
    # Function
    f = 14 * ((x - 7)**2 + (y - 2)**2)**0.5 + \
        20 * ((x - 5)**2 + (y + 3)**2)**0.5 + \
        30 * ((x + 6)**2 + (y - 4)**2)**0.5
    gradient = [f.diff(x), f.diff(y)]
    # Hessian matrix
    hessian = [
        [
            f.diff(x).diff(x).evalf(subs={x: x_0[0], y: x_0[1]}),
            f.diff(y).diff(x).evalf(subs={x: x_0[0], y: x_0[1]})
        ],
        [
            f.diff(x).diff(y).evalf(subs={x: x_0[0], y: x_0[1]}),
            f.diff(y).diff(y).evalf(subs={x: x_0[0], y: x_0[1]})
        ]
    ]
    M = sp.Matrix(hessian)
    M_inv = M.inv()
    # d_0
    d = -1*M_inv*sp.Matrix(
        [
            gradient[0].evalf(subs={x: x_0[0], y:x_0[1]}),
            gradient[1].evalf(subs={x: x_0[0], y:x_0[1]})
        ]
    )
    # Armijo constants
    sigma = 0.1
    beta = 0.5
    s = 1
    exit_condition = sp.Matrix(
        [
            gradient[0].evalf(subs={x: x_0[0], y: x_0[1]}),
            gradient[1].evalf(subs={x: x_0[0], y: x_0[1]})
        ]
    ).norm()
    x_current = x_0
    i = 0  # Iterator

    print('\nNewton method with Armijo rule\n')
    print(f'f(x, y) = {f}\n')
    print(f'∇f = {gradient}\n')
    print(f'H(f(x_0)) = {M}\n')
    print(f'H⁻¹(f(x_0)) = {M_inv}\n')
    print(f'd_0 = −∇²f⁻¹(x_0) * ∇f(x_0) = {d}\n')
    print(f'Current value: {x_current}\n')

    while(exit_condition > tolerance):
        # Hessian matrix
        hessian = [
            [
                f.diff(x).diff(x).evalf(
                    subs={x: x_current[0], y: x_current[1]}
                ),
                f.diff(y).diff(x).evalf(
                    subs={x: x_current[0], y: x_current[1]}
                )
            ],
            [
                f.diff(x).diff(y).evalf(
                    subs={x: x_current[0], y: x_current[1]}
                ),
                f.diff(y).diff(y).evalf(
                    subs={x: x_current[0], y: x_current[1]}
                )
            ]
        ]
        M = sp.Matrix(hessian)
        M_inv = M.inv()

        d = -1*M_inv*sp.Matrix(
            [
                gradient[0].evalf(subs={x: x_current[0], y: x_current[1]}),
                gradient[1].evalf(subs={x: x_current[0], y: x_current[1]})
            ]
        )

        m = 0
        # f(x_k) - f(x_k + beta^m*s*d^k)
        right_armijo = f.evalf(subs={x: x_current[0], y: x_current[1]}) - \
            f.evalf(subs={
                x: x_current[0] + s*d[0],
                y: x_current[1] + s*d[1]
            })
        left_armijo = -sigma*s*(d.transpose()*sp.Matrix([
            gradient[0].evalf(subs={x: x_current[0], y: x_current[1]}),
            gradient[1].evalf(subs={x: x_current[0], y: x_current[1]})
        ]))[0]

        while(right_armijo < left_armijo):
            m += 1
            right_armijo = f.evalf(subs={x: x_current[0], y: x_current[1]}) - \
                f.evalf(subs={
                    x: x_current[0] + (beta**m)*s*d[0],
                    y: x_current[1] + (beta**m)*s*d[1]
                })
            left_armijo = -sigma*(beta**m)*s*(d.transpose()*sp.Matrix([
                gradient[0].evalf(subs={x: x_current[0], y: x_current[1]}),
                gradient[1].evalf(subs={x: x_current[0], y: x_current[1]})
            ]))[0]

        alpha = (beta**m)*s

        x_current = [x_current[0] + alpha*d[0], x_current[1] + alpha*d[1]]

        exit_condition = sp.Matrix(
            [
                gradient[0].evalf(subs={x: x_current[0], y: x_current[1]}),
                gradient[1].evalf(subs={x: x_current[0], y: x_current[1]})
            ]
        ).norm()

        i += 1

    print(f'\nIteration {i}\n')
    print(f'f(x^{i}) - f(x^{i} + ({beta}^{m})*{s}*{d}^{i}) = {right_armijo}')
    print(f'{sigma}*({beta}**{m})*{d}^{i}T*∇f(x^{i}) = {left_armijo}')
    print(f'm = {m}')
    print(f'α = {alpha}')
    print(f'x = {x_current}')
    print(f'd = {d}')
