# Напишите программу, которая сортирует заданный список из чисел

import string

if __name__=='__main__':
    
    temporary = ''
    array = []
    # print('Enter the list of numbers (through ','):')
    # a = str(input())
    a ='3453, 6,89,999,7'
    for i in a:
        if i != ',':
            temporary = temporary+i
        else:
            array.append(int(temporary.strip(' ')))
            temporary = ''
    array.append(int(temporary.strip(' ')))
    print(array)

    sort_array = array
    lenth_array = len(sort_array)

    for i in range(lenth_array):
       index_min = i
    
       for j in range(i+1, lenth_array):
          if sort_array[j] < sort_array[index_min]:
              index_min = j
                
       tmp = sort_array[index_min]
       sort_array[index_min] = sort_array[i]
       sort_array[i] = tmp
    
    print(sort_array) 
