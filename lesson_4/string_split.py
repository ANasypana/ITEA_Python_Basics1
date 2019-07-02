# Разбить строку "data" на группы по 3 числа и посчитать суммы каждого первого, второго и третьего


def sum_of_column_elements(column_number, l):
    row = len(l)
    column = len(l[0])
    sum_elements = 0
    if column_number <= column:
        for i in range(row):
            sum_elements += l[i][column_number]
        return sum_elements
    else:
        return None


if __name__ == '__main__':

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
    n = len(temporary_str) // 3

    for i in range(n):
       array.append([float(temporary_str[3 * i + j]) for j in range(3)])

    print(f'Created array:\n{array}')
    for i in range(3):
        print(f'Sum of elements of {i + 1} column - {sum_of_column_elements(i, array)}')
