"""Створити функцію, яка буде генерувати 5 випадкових чисел в діапазоні від 0 до 10(1 рядок через пробіл)
   100 раз записати результат данної функції в файл test3_result.txt."""

import random


def set_random_numbers(n=5):
    string = " ".join(str(random.randint(0, 10)) for i in range(n))
    return string


if __name__ == '__main__':
    with open('test3_result.txt', 'w') as input_file:
        pass
    input_file.close()

    for i in range(100):
        with open('test3_result.txt', 'ab') as input_file:
            if i < 99:
                input_file.write(bytes(f'{set_random_numbers()}\n', 'utf8'))
            else:
                input_file.write(bytes(f'{set_random_numbers()}', 'utf8'))
    input_file.close()
