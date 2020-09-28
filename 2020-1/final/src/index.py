from questions.p1_a import question_1_a
from questions.p1_b import question_1_b
from questions.p1_c import question_1_c
from questions.p1_d import question_1_d
from questions.p2_b import question_2_b

options = [
    'Question 1 - Item a',
    'Question 1 - Item b',
    'Question 1 - Item c',
    'Question 1 - Item d',
    'Question 1 - Item e',
    'Question 2 - Item b',
    'Exit'
]

options_values = list(range(1, len(options) + 1))

if __name__ == '__main__':
    option = ''
    print('Final exam:')
    while option != 'd':
        print(
            f'\n1. {options[0]}\n2. {options[1]}\n3. {options[2]}\n4. {options[3]}\n5. {options[4]}\n6. {options[5]}\n7. {options[6]}'
        )
        option = int(input('\nType an option: '))

        while option not in options_values:
            print('That is not a valid option.')
            option = input('Type an option: ')

        if option == 1:
            question_1_a()
        elif option == 2:
            question_1_b()
        elif option == 3:
            question_1_c()
        elif option == 4:
            x1 = float(input('Enter a float value for x1: '))
            x2 = float(input('Enter a float value for x2: '))
            question_1_d(x1, x2)
        elif option == 5:
            print('\nStarting point (-4, -4):\n')
            question_1_d(-4, -4)
            print('\nStarting point (-4, 4):\n')
            question_1_d(-4, 4)
            print('\nStarting point (0, 0):\n')
            question_1_d(0, 0)
            print('\nStarting point (4, 0):\n')
            question_1_d(4, 0)
        elif option == 6:
            question_2_b()
        elif option == 7:
            print('\nThanks for coming!')
            break
