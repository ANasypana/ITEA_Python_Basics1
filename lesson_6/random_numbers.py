"""Створити функцію, яка буде генерувати 5 випадкових чисел в діапазоні від 0 до 10(1 рядок через пробіл)
   100 раз записати результат данної функції в файл test3_result.txt."""

import random


def set_random_numbers(n=5):
    string = " ".join(str(random.randint(0, 10)) for i in range(n))
    return string


if __name__ == '__main__':

    with open('test3_result.txt', 'wb') as input_file:
        input_file.write(bytes("\n".join(set_random_numbers() for i in range(100)), 'utf8'))
        input_file.close()
