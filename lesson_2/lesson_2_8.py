# Найти сумму чисел числа 2 способами

from mydoc.subsidiary_functions import enter_positive_number


if __name__ == '__main__':
    number = str(enter_positive_number('positive number'))

    sum_of_first_method = 0
    sum_of_second_method = 0

    for i in number:
        sum_of_first_method += int(i)

    length = len(number)
    for i in range(length):
        sum_of_second_method += int(number) % (10 ** (i + 1)) // (10 ** i)

    print(f'Sum of first method: \n {sum_of_first_method}')
    print(f'Sum of second method: \n {sum_of_second_method}')
