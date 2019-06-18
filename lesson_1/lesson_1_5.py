# Напишите программу, которая считает сумму последних цифр двух введенных пользователем чисел

if __name__=='__main__':
    first_number = input('Enter first number:\n')
    second_number = input('Enter second number:\n')

    first_digit = first_number[-1]
    second_digit = second_number[-1]
    result = int(first_digit)+int(second_digit)
    print('Sum of the last digits: ', result)