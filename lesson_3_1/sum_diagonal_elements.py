import random

def sum_diagonal_elements(l):
    sum = 0
    column = len(l)
    row = len(l[0])
    min_value = min(column, row)

    for i in range(min_value):
        sum += l[i][i]
    return sum


def set_array (n, m, a = 0, b = 100):
    l=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            l[i][j] = random.randint(a, b)
    return l


if __name__=='__main__':

    n = 4
    m = 5

    array = set_array(n, m)

    print(array)
    print('Sum of diagonal items: ', sum_diagonal_elements(array))