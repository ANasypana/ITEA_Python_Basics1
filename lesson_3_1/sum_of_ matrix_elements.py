# Найти сумму элементов матрицы

if __name__ == '__main__':
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    row = len(array)
    elements_sum = 0

    for i in range(row):
        elements_sum += sum(array[i])

    print(f'Sum of elements of matrix  - {elements_sum}')
