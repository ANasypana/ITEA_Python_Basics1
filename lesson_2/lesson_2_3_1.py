# Написать функцию, которая вычисляет среднее арифметическое элементов массива


def mean_array(l):
    sum_elements = 0
    size = len(l)
    for i in l:
        sum_elements += int(i)
    return float(sum_elements / size)


if __name__ == '__main__':
    array = [22, 90, 89, 234, 7, 89]

    checking_string = ''
    for i in array:
        checking_string += str(i)
    if checking_string.isdigit():
        print(array)
        print(f'Result of mean_array: {round(mean_array(array), 2)}')
    else:
        print('Incorrect data in list.')
