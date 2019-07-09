# Найти сумму верхней диагонали матрицы

import random


def sum_upper_elements(l):
    sum_elements = 0
    len_row = len(l)
    len_column = len(l[0])
    min_value = min(len_row, len_column - 1)
    for i in range(min_value):
        sum_elements += sum(l[i][i + 1:])
    return sum_elements


def set_array(number_row, number_col, a=0, b=100):
    l = []
    for i in range(number_row):
        l.append([random.randint(a, b) for j in range(number_col)])
    return l


if __name__ == '__main__':
    n = 5
    m = 6
    array = set_array(n, m)

    print(array)
    print(f'Sum of upper items - {sum_upper_elements(array)}')
