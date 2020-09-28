from questions.p1 import question_1
from questions.p2 import question_2
from questions.p3 import question_3

options = [
    'Plot',
    'Steepest descent search',
    'Newton\'s method',
    'Exit'
]

if __name__ == '__main__':
    option = ''
    print('Calificated practice 5:')
    while option != 'd':
        print(
            f'\na. {options[0]}\nb. {options[1]}\nc. {options[2]}\nd. {options[3]}'
        )
        option = input('\nType an option: ').lower()

        while option != 'a' and option != 'b' and option != 'c' and option != 'd':
            print('That is not a valid option.')
            option = input('Type an option: ')

        if option == 'a':
            question_1()
        elif option == 'b':
            question_2()
        elif option == 'c':
            question_3()
        elif option == 'd':
            print('\nThanks for coming!')
            break
