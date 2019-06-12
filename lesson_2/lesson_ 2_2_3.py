# Посчитайте значение выражения: cos(x)*sin(x)
def composition_sin_cos(x):
    return math.sin(x)* math.cos(x)

import math

if __name__=='__main__':

    print('Enter a function argument:')
    x=float(input())
    print('Function values:', composition_sin_cos(x))