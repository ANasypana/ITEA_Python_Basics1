# сортировку массива по возрастанию суммы цифр чисел


def array_of_sum_digits(l):
    size = len(l)
    res_array = []
    for i in range(size):
        s = 0
        for j in str(l[i]):
            s += int(j)
        res_array.append(s)
    return res_array


def sum_digits(number):
    number = str(number)
    s = 0
    for i in number:
        s += int(i)
    return s


def sorted_array(l):
    size = len(l)

    for i in range(size):
        index_min = i
        for j in range(i + 1, size):
            if sum_digits(l[j]) < sum_digits(l[index_min]):
                index_min = j
            elif sum_digits(l[j]) == sum_digits(l[index_min]):
                if l[j] < l[index_min]:
                    index_min = j

        temporary = l[index_min]
        l[index_min] = l[i]
        l[i] = temporary

    return l


if __name__ == '__main__':
    array = [106, 77, 8, 80, 90]

    checking_string = ''
    for i in array:
        checking_string += str(i)
    if checking_string.isdigit():
        print('List: \n', array)
        print('List of sum of numbers: \n', array_of_sum_digits(array))
        print('Sorted array: \n', sorted_array(array))
    else:
        print('Incorrect data in list.')
