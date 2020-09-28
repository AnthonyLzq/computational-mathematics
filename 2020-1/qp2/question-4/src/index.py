import matplotlib.pyplot as plt

from questions.a import lagrange_curve
from questions.b import beizer_curve
from questions.c import b_spline

options = [
    'Lagrange interpolation',
    'Beizer curve',
    'B-Spline',
    'Exit'
]

fig = plt.gcf()

if __name__ == '__main__':
    option = ''
    print('Question 4')
    while option != 'd':
        print(
            f'\na. {options[0]}\nb. {options[1]}\nc. {options[2]}\nd. {options[3]}'
        )
        option = input('\nType an option: ').lower()

        while option != 'a' and option != 'b' and option != 'c' and option != 'd':
            print('That is not a valid option.')
            option = input('Type an option: ')

        if option == 'a':
            lagrange_curve()
            plt.title(f'{options[0]}')
        elif option == 'b':
            beizer_curve()
            plt.title(f'{options[1]}')
        elif option == 'c':
            b_spline()
            plt.title(f'{options[2]}')
        elif option == 'd':
            print('\nThanks for coming!')
            break

        fig.canvas.set_window_title('Question 2')
        plt.xlabel('x')
        plt.ylabel('y')
        # plt.legend()
        plt.show()
        plt.gcf().canvas.get_tk_widget().focus_force()
