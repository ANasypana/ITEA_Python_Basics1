import random

def sum_upper_elements (l):
    sum = 0
    column = len(l)
    row = len(l[0])

    for i in range(column):
        for j in range(i+1, row):
            sum += int(l[i][j])
    return sum


def set_array (n, m, a = 0, b = 100):

    l=[[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            l[i][j] = random.randint(a, b)
    return l

if __name__=='__main__':
    n = 5
    m = 6
    array = set_array(n,m)
    print(array)
    print('Sum of upper items: ', sum_upper_elements(array))

