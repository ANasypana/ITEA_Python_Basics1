# Вывести сумму всех делителей заданного числа

from mydoc.subsidiary_functions import (enter_number, )


if __name__ == '__main__':
    data = enter_number('positive number')

    sum_divisors = 0
    for i in range(2, data):
        if data % i == 0:
            sum_divisors += i

    print(f'The sum of dividers {data} - {sum_divisors}')
