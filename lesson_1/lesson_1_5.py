# Напишите программу, которая считает сумму последних цифр двух введенных пользователем чисел

if __name__=='__main__':

    print('Enter number 1:')
    first_number = str(input())

    print('Enter number 2:')
    second_number = str(input())

    first_number = first_number[-1]
    second_number = second_number[-1]
    result = int(first_number)+int(second_number)
    print('Sum of the last digits: ', result)