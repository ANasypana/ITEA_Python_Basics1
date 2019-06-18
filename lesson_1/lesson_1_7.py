# Напишите программу, которая преобразует строку, в которой записаны слова через “,” в список из этих слов

import string


if __name__=='__main__':
    line = 'ooojuoi, tyiu, ll, , k'
    temporary = ''
    array = []

    for i in line:
        if i != ',':
            temporary = temporary+i
        else:
            array.append(temporary.strip(' '))
            temporary = ''
    array.append(temporary.strip(' '))

    print(array) 
