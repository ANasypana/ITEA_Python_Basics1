# Напишите программу, которая считает сумму последних цифр двух введенных пользователем чисел

if __name__ == '__main__':
    first_number = input('Enter first number:\n')
    first_number = str(first_number)
    while not first_number.isdigit():
        first_number = input('Error! Try again. You must enter only number:\n')
        first_number = str(first_number)

    second_number = input('Enter second number:\n')
    second_number = str(second_number)
    while not second_number.isdigit():
        second_number = input('Error! Try again. You must enter only number:\n')
        second_number = str(first_number)

    first_digit = first_number[-1]
    second_digit = second_number[-1]
    
    result = int(first_digit) + int(second_digit)
    print('Sum of the last digits: ', result)
