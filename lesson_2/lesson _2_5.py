# Напишите программу, которая выводит сумму введенных пользователем чисел. Числа вводятся одной строкой

if __name__=='__main__':
    list_of_words = input('Enter list of numbers (through ", "):\n')
    list_of_words = str(list_of_words)
    array = list_of_words.split(",")

    Sum = 0
    for i in array:
        Sum += int(i)

    print('Sum: ', Sum)