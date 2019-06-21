# Напишите программу, которая преобразует строку, в которой записаны слова через “,” в список из этих слов

import string

if __name__=='__main__':
    
    temporary = ''
    array = []
    # print('Enter the list of words (through ','):')
    # a = str(input())
    a='ooojuoi, tyiu, ll, , k'

    for i in a:
        if i != ',':
            temporary = temporary+i
        else:
            array.append(temporary.strip(' '))
            temporary = ''
    array.append(temporary.strip(' '))

    print(array) 
