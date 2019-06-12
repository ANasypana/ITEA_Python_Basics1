# заполние массива случайными числами в диапазоне, указанном пользователем

import random

def set_array(a, b, m = 8):
    result = []
    if a > b:
        for j in range(m):
            result.append(random.randint(b, a))
    else:
        for j in range(m):
            result.append(random.randint(a, b))
    print(result)
    return #result


if __name__=='__main__':

    a = 2
    b = 8
    set_array(a,b)





