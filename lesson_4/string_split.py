# Разбить строку "data" на группы по 3 числа и посчитать суммы каждого первого, второго и третьего


def sum_of_column_elements(n, l):
    row = len(l)
    column = len(l[0])
    sum_elements = 0
    if n <= column:
        for i in range(row):
            sum_elements += l[i][n]
        return sum_elements
    else:
        return None


if __name__=='__main__':

    data = """
    0.00002640
    23174.4902
    0.61180654
    0.00002599
    8434.0130
    0.21919999
    0.00002000
    52622.1944
    1.05244388
    0.00001599
    13708.5678
    0.21919999
    0.00001500
    100232.3673
    1.50348550
    """
    temporary_str = data.split("\n    ")
    temporary_str = temporary_str[1:-1]
    array = []

    for i in range(5):
       array.append([float(temporary_str[3*i+j]) for j in range(3)])
    array = list(array)

    print('Created array:\n', array)
    for i in range(3):
        print('Sum of elements of {} column - '.format(i+1), sum_of_column_elements(i, array))