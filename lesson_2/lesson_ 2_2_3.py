# Посчитайте значение выражения: cos(x)*sin(x)

import math


def composition_sin_cos(x):
    return math.sin(x)* math.cos(x)


if __name__=='__main__':
    x = input('Enter a function argument:\n')
    x = float(x)

    print('Function values:', composition_sin_cos(x))