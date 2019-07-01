# Напишите программу, которая выводит сумму введенных пользователем чисел. Числа вводятся одной строкой

from mydoc.subsidiary_functions import (enter_list_of_numbers, )


if __name__ == '__main__':
    list_of_data = enter_list_of_numbers('list of numbers (through ",")')

    sum_elements = 0
    for i in list_of_data:
        sum_elements += int(i)

    print(f'Sum: {sum_elements}')
