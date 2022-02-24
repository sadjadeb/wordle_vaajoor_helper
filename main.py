from webserver import run_webserver
from finder import word_finder


def run_shell():
    game_mode = input('Enter game mode(vaajoor, wordle): ')
    number_of_exact_input = int(input('Enter number of exact input: '))
    print('Enter each index and character in separate lines with space: ')
    exact_dict = {}
    for i in range(number_of_exact_input):
        input_data = input().split()
        exact_dict[input_data[1]] = int(input_data[0]) - 1

        if exact_dict[input_data[1]] < 0 or exact_dict[input_data[1]] > 4:
            print('Error: index must be between 1 and 5')
            exit()

    number_of_exact_input = int(input('Enter number of contain input: '))
    print('Enter each character in separate line: ')
    contains_list = []
    for i in range(number_of_exact_input):
        contains_list.append(input())

    print(word_finder(game_mode, exact_dict, contains_list))


if __name__ == '__main__':
    run_mode = int(input('Enter run mode: 1 for shell, 2 for webserver: '))
    if run_mode == 1:
        run_shell()
    elif run_mode == 2:
        run_webserver()
    else:
        print('Error: run mode not acceptable')
        exit()
