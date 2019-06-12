# Напишите программу, которая выводит сумму введенных пользователем чисел. Числа вводятся одной строкой

if __name__=='__main__':

    print('Enter list of numbers (through ", "):')
    list_of_word = str(input())
    l=list_of_word.split(",")
    Sum = 0
    for i in l:
        Sum =Sum+int(i)
    print('Sum: ',Sum)



