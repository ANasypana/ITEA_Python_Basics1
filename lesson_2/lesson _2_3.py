# Извлекать квадратный корень из введенного пользователем числа до тех пор, пока значение больше 10

import math

if __name__=='__main__':

    print('Enter number:')
    number = int(input())

    if math.sqrt(number) > 10:
        while math.sqrt(number) > 10:
            print(math.sqrt(number))
            print('Enter number:')
            number = int(input())
        print('Square root of number <10')
    else:
        print('Square root of number <10')