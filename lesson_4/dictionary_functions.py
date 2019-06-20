#Без использования методов словарей(кроме items), напишите  функцию remove по ключу и remove по значению


def remove_by_key(dic, key):     #remove from dictionary by key
     if key in dic:
         del dic[key]
     else:
         return 'KeyError'
     return dic


def remove_by_value(dic, meaning):     #remove from dictionary by value
    if meaning in dic.values():
        for key, value in dic.items():
            if value == meaning:
                meaning_key = key
        del dic[meaning_key]
        return dic
    else:
        return 'ValueError'
    return dic


if __name__ == '__main__':
    dictionary = dict(zip([1, 2, 3, 4], ['one', 'two', 'three', 'four']))

    print(remove_by_key(dictionary, 1))
    print(remove_by_value(dictionary, 'two'))  
