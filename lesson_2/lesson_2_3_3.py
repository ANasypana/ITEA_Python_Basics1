# заполние массива случайными числами в диапазоне, указанном пользователем

import random


def set_array(a, b, m=8):
    result = []
    if a == b:
        return None
    else:
        start = min(a, b)
        end = max(a, b)
        for j in range(m):
            result.append(random.randint(start, end))
    return result


if __name__ == '__main__':
    a = 2
    b = 8
    print(set_array(a, b))
