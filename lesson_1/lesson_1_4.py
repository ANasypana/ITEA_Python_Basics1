# Напишите программу, которая сортирует заданный список из чисел

import string


if __name__=='__main__':
    line = '3453, 6,89,999,7'
    temporary = ''
    array = []

    for i in line:
        if i != ',':
            temporary = temporary+i
        else:
            array.append(int(temporary.strip(' ')))
            temporary = ''
    array.append(int(temporary.strip(' ')))
    print(array)

    sorted_array = array
    length_array = len(sorted_array)

    for i in range(length_array):
       index_min = i
       for j in range(i+1, length_array):
          if sorted_array[j] < sorted_array[index_min]:
              index_min = j
       tmp = sorted_array[index_min]
       sorted_array[index_min] = sorted_array[i]
       sorted_array[i] = tmp

    print(sorted_array)  
