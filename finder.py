persian_words = []
english_words = []

# read persian words from file
with open('persian_words.txt', 'r', encoding='utf-8') as f:
    for line in f:
        persian_words.append(line.strip())

# read english words from file
with open('english_words.txt', 'r', encoding='utf-8') as f:
    for line in f:
        english_words.append(line.strip())


def word_finder(game_mode: str, exact_dict: dict, contains_list: list):
    if len(contains_list) == 0 and len(exact_dict.keys()) == 0:
        return {'message': 'No condition', 'result': [], 'result_count': 0}

    condition = ''
    if len(exact_dict.keys()) > 0:
        condition = ' and '.join([f'word[{exact_dict[key]}] == "{key}"' for key in exact_dict])
    if len(contains_list) > 0 and len(exact_dict.keys()) > 0:
        condition += ' and '
    if len(contains_list) > 0:
        condition += ' and '.join([f'"{character}" in word' for character in contains_list])

    if game_mode == 'vaajoor':
        words_dictionary = persian_words
    elif game_mode == 'wordle':
        words_dictionary = english_words
    else:
        return {'message': 'Mode not acceptable', 'result': [], 'result_count': 0}

    all_acceptable_words = []
    for word in words_dictionary:
        if len(word) == 5:
            if eval(condition):
                all_acceptable_words.append(word)

    if len(all_acceptable_words) == 0:
        return {'message': 'No words were found', 'result': [], 'result_count': 0}

    return {'message': 'Success', 'result': all_acceptable_words, 'result_count': len(all_acceptable_words)}
