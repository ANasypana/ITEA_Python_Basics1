# сортировку массива по возрастанию суммы цифр чисел

def array_of_sum_digits(l):
    size = len(l)
    res_array = []

    for i in range(size):
        s = 0
        for j in str(l[i]):
            s = s + int(j)
        res_array.append(s)

    return res_array


def sorted_array(l):
        def sum_digits(a):
            s = 0
            for i in a:
                s = s+int(i)
            return s

        size = len(l)

        for i in range(size):
            index_min = i

            for j in range(i+1, size):
                if sum_digits(str(l[j])) < sum_digits(str(l[index_min])):
                    index_min = j
            temporary = l[index_min]
            l[index_min] = l[i]
            l[i] = temporary

        return l


if __name__=='__main__':
    array = [106, 77, 8, 90]

    print('List: \n', array)
    print('List of sum of numbers: \n', array_of_sum_digits(array))
    print('Sorted array: \n', sorted_array(array))