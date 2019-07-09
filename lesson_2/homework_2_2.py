# Найти факториал числа

from mydoc.subsidiary_functions import enter_positive_number


def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)


if __name__ == '__main__':
    n = enter_positive_number('positive number')
    print(f'{n}! = {factorial(n)}')
