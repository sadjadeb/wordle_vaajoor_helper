import json

# load words from json file
with open('words_5_letters.json', 'r', encoding='utf-8') as f:
    words = json.load(f)
    persian_words = words['vaajoor']
    english_words = words['wordle']


def word_finder(game_mode: str, exact_dict: dict, contains_list: list, not_contains_list: list):
    if len(contains_list) == 0 and len(exact_dict.keys()) == 0 and len(not_contains_list) == 0:
        return {'message': 'No condition', 'result': [], 'result_count': 0}

    condition = ''
    if len(exact_dict.keys()) > 0:
        condition = ' and '.join([f'word[{key}] == "{exact_dict[key]}"' for key in exact_dict])
    if len(contains_list) > 0 and len(exact_dict.keys()) > 0:
        condition += ' and '
    if len(contains_list) > 0:
        condition += ' and '.join([f'"{character}" in word' for character in contains_list])
    if len(not_contains_list) > 0 and (len(exact_dict.keys()) > 0 or len(contains_list) > 0):
        condition += ' and '
    if len(not_contains_list) > 0:
        condition += ' and '.join([f'"{character}" not in word' for character in not_contains_list])

    if game_mode == 'vaajoor':
        words_dictionary = persian_words
    elif game_mode == 'wordle':
        words_dictionary = english_words
    else:
        return {'message': 'Mode not acceptable', 'result': [], 'result_count': 0}

    all_acceptable_words = []
    for word in words_dictionary:
        if eval(condition):
            all_acceptable_words.append(word)

    if len(all_acceptable_words) == 0:
        return {'message': 'No words were found', 'result': [], 'result_count': 0}

    return {'message': 'Success', 'result': all_acceptable_words, 'result_count': len(all_acceptable_words)}
