from typing import List, Dict

persian_words: List[str] = []

# read words from file
with open('persian_words.txt', 'r', encoding='utf-8') as f:
    for line in f:
        persian_words.append(line.strip())

print(len(persian_words))


def word_finder(exact_dict: Dict, contain_list: List):
    if len(contain_list) == 0 and len(exact_dict.keys()) == 0:
        return {'message': 'No condition', 'result': [], 'result_count': 0}

    condition = ''
    if len(exact_dict.keys()) > 0:
        condition = ' and '.join([f'word[{exact_dict[key]}] == "{key}"' for key in exact_dict])
    if len(contain_list) > 0 and len(exact_dict.keys()) > 0:
        condition += ' and '
    if len(contain_list) > 0:
        condition += ' and '.join([f'"{character}" in word' for character in contain_list])

    all_acceptable_words = []
    for word in persian_words:
        if len(word) == 5:
            if eval(condition):
                all_acceptable_words.append(word)
                print(word)

    return {'message': 'Success', 'result': all_acceptable_words, 'result_count': len(all_acceptable_words)}


if __name__ == '__main__':
    number_of_exact_input = int(input('Enter number of exact input: '))
    print('Enter each index and character in seprate lines with space: ')
    exact_dict = {}
    for i in range(number_of_exact_input):
        input_data = input().split()
        exact_dict[input_data[1]] = int(input_data[0]) - 1

        if exact_dict[input_data[1]] < 0 or exact_dict[input_data[1]] > 4:
            print('Error: index must be between 1 and 5')
            exit()

    number_of_exact_input = int(input('Enter number of contain input: '))
    print('Enter each character in seprate line: ')
    contain_list = []
    for i in range(number_of_exact_input):
        contain_list.append(input())

    print(word_finder(exact_dict, contain_list))
