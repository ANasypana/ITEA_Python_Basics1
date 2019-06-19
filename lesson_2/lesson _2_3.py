# Извлекать квадратный корень из введенного пользователем числа до тех пор, пока значение больше 10

import math


if __name__=='__main__':
    number = input('Enter number:\n')
    str_number = str(number)

    if str_number.isdigit():
        number = int(number)

        if math.sqrt(number) > 10:
            while math.sqrt(number) > 10:
                print(math.sqrt(number))
                print('Enter number:')
                number = int(input())
            print('Square root of number <10')
        else:
            print('Square root of number <10')

    else:
        input('Error! Try again. Your must enter only figures: \n')