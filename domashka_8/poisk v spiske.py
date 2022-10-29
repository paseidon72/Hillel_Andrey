INPUT_LIST = [
    1, '2', 'cat', 99, 'dog',
    (4, 44, ['red', 'green', ('mather', 'father')]),
    ['one', 'two', '55', {3, 8, 'big', True}, ['milk', 9, 'bred']],
    'End'
]


def find_word(word, INPUT_LIST):
    result = False

    for item in INPUT_LIST:
        if isinstance(item, (str, int)) and item == word:
            result = True
            break
        elif isinstance(item, (list, tuple)):
            result = find_word(word, item)
            if result:
                break
        elif isinstance(item, set):
            if word in item:
                result = True
                break
    return result


def main():
    input_word = input('Введите слово: ')
    if find_word(input_word, INPUT_LIST):
        print('Слово найдено')
    else:
        print('Слово не найдено')


main()