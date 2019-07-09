# Пользователь задает случайное число n. Сгенерировать список этой длины и заполнить его 0 и 1 случайным образом.
# Найти самую длинную цепочку из подряд идущих 0 или 1.
# Вывести эту длину.
# Для какого максимального значения n, ваш алгоритм будет работать меньше чем 1 секунда?

import random
import time
from mydoc.subsidiary_functions import enter_positive_number


if __name__ == '__main__':
    number = enter_positive_number('positive number')
    start_time = time.perf_counter()
    delta = 0
    array = []
    current_length = 1
    temporary_max = 1

    for i in range(number):
        array.append((random.randint(0, 1)))
        if i > 0 and array[i - 1] == array[i]:
            current_length += 1
        else:
            if temporary_max < current_length:
                temporary_max = current_length
                current_length = 1
    max_length = max(current_length, temporary_max)
    time_stop = time.perf_counter()

    delta = time_stop - start_time

    print(f'The max length of chain of series 0 or 1 - {max_length}')
    print(f'Time of working program - {round(delta, 3)} sec.\nNumber - {number}')
    """Max N ~ 170000"""
