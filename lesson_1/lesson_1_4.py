# Напишите программу, которая сортирует заданный список из чисел


if __name__ == '__main__':
    array = [3453, 6, 89, 999, 7]

    length_array = len(array)

    for i in range(length_array):
        index_min = i
        for j in range(i + 1, length_array):
            if array[j] < array[index_min]:
                index_min = j
        tmp = array[index_min]
        array[index_min] = array[i]
        array[i] = tmp

    print(array)
