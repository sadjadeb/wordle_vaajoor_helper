from finder import word_finder


def run_terminal():
    game_mode = input('Enter game mode: 1 for vaajoor, 2 for wordle: ')
    if game_mode == '1':
        game_mode = 'vaajoor'
    elif game_mode == '2':
        game_mode = 'wordle'

    number_of_input = int(input('Enter number of exact input: '))
    print('Enter each index and character in separate lines with space: ')
    exact_dict = {}
    for i in range(number_of_input):
        input_data = input().split()
        exact_dict[int(input_data[0]) - 1] = input_data[1]

        if int(input_data[0]) < 1 or int(input_data[0]) > 5:
            print('Error: index must be between 1 and 5')
            exit()

    number_of_input = int(input('Enter number of contains input: '))
    print('Enter each character in separate line: ')
    contains_list = []
    for i in range(number_of_input):
        contains_list.append(input())

    number_of_input = int(input('Enter number of not contains input: '))
    print('Enter each character in separate line: ')
    not_contains_list = []
    for i in range(number_of_input):
        not_contains_list.append(input())

    print(word_finder(game_mode, exact_dict, contains_list, not_contains_list))
