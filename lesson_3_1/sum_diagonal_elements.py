# Найти сумму диагональных элементов матрицы


import random


def sum_diagonal_elements(l):
    sum_elements = 0
    row = len(l)
    column = len(l[0])
    min_value = min(column, row)

    for i in range(min_value):
        sum_elements += l[i][i]
    return sum_elements


def set_array(number_row, number_col, a=0, b=100):
    l = []
    for i in range(number_row):
        l.append([random.randint(a, b) for j in range(number_col)])
    return l


if __name__ == '__main__':
    n = 4
    m = 5
    array = set_array(n, m)

    print(array)
    print(f'Sum of diagonal items: {sum_diagonal_elements(array)}')
