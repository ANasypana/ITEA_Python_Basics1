#Без использования методов словарей(кроме items), напишите  функцию remove по ключу и remove по значению


def remove_by_key(dictionary, key):
    if key in dictionary:
        value = dictionary[key]
        del dictionary[key]
    else:
        raise KeyError
    return value


def remove_by_value(dictionary, meaning):
    list_of_keys = []
    for key, value in dictionary.items():
        if value == meaning:
            meaning_key = key
            list_of_keys.append(meaning_key)

    length = len(list_of_keys)
    if length > 0:
        for key in list_of_keys:
            del dictionary[key]
        return list_of_keys
    else:
        raise ValueError


if __name__ == '__main__':
    glossary = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four'
    }

    set_key = 1
    set_value = 'uuu'

    try:
        print(remove_by_key(glossary, set_key))
    except KeyError:
        print("This key doesn't exist.")

    try:
        print(remove_by_value(glossary, set_value))
    except ValueError:
        print("This value doesn't exist.")
