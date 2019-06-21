# Написать функцию, которая вычисляет среднее арифметическое элементов массива


def mean_array(l):
    elements_sum = 0
    size = len(l)
    for i in l:
        if str(i).isdigit():
            elements_sum += int(i)
        else:
            return None
    return float(elements_sum / size)


if __name__ == '__main__':
    array = [22, 56, 89, 234, 7, 89]

    print(array)
    print('Result of mean_array:\n', round(mean_array(array), 2))
