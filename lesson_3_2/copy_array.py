# передать копию списка или словаря в функцию

import copy


def copy_function(l):
    result_copy = copy.copy(l)
    return len(result_copy)


if __name__ == '__main__':
    array = [w * 2 for w in 'python']
    dictionary = {a: a ** 2 for a in range(1, 6)}

    dictionary[7] = 7 ** 2
    array.append('java')

    print(copy_function(array))
    print(copy_function(dictionary))
