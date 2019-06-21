# Извлекать квадратный корень из введенного пользователем числа до тех пор, пока значение больше 10

import math


if __name__ == '__main__':
    number = input('Enter number:\n')
    number = str(number)
    while not number.isdigit():
        number = input('Error! Try again. You must enter only number:\n')
        number = str(number)
    number = int(number)

    while math.sqrt(number) > 10:
        number = input('Enter number:\n')
        number = str(number)
        while not number.isdigit():
            number = input('Error! Try again. You must enter only number:\n')
            number = str(number)
        number = int(number)

    print('Square root of number <10')
