# сортировку массива по возрастанию суммы цифр чисел

def sum_array_digit (l):
    size = len(l)
    res_array = []
    for i in range(size):
        s = 0
        for j in str(l[i]):
            s = s + int(j)
        res_array.append(s)
    return res_array

def sort_array(l):
        t = []
        def sum_digit (a):
            s = 0
            for i in a:
                s = s+int(i)
            return s

        size = len(l)
        for i in range(size):
            index_min = i
            for j in range(i+1,size):
                if sum_digit(str(l[j])) < sum_digit(str(l[index_min])):
                    index_min = j
            tmp = l[index_min]
            l[index_min] = l[i]
            l[i] = tmp
        return l

if __name__=='__main__':
    l=[106,77,8,90]

    print('List: ', l)
    print('List of sum of numbers: ', sum_array_digit(l))
    print('Sorted mass: ', sort_array(l))
