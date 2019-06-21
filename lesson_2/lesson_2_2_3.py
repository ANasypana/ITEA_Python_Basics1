# Посчитайте значение выражения: cos(x)*sin(x)

import math


def composition_sin_cos(x):
    return math.sin(x) *  math.cos(x)


if __name__ == '__main__':
    x = input('Enter a function argument:\n')
    x = str(x)
    x_check = x.replace('.', '')
    while not x_check.isdigit():
        x = input('Error! Try again. Your must enter only number:\n')
        x = str(x)
        x_check = x.replace('.', '')
    x = float(x)

    print(f'sin({x})*cos({x}) - ', composition_sin_cos(x))
