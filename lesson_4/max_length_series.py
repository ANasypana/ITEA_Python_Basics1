# Пользователь задает случайное число n. Сгенерировать список этой длины и заполнить его 0 и 1 случайным образом.
# Найти самую длинную цепочку из подряд идущих 0 или 1.
# Вывести эту длину.
# Для какого максимального значения n, ваш алгоритм будет работать меньше чем 1 секунда?


import random
import time


if __name__ == '__main__':
     n = 70000
     delta = 0

     while delta < 1:
         start_time = time.perf_counter()
         array = []
         current_length = 1
         temporary_max = 0

         for i in range(n):
             array.append((random.randint(0, 1)))

         for i in range(1, n):
             if array[i-1] == array[i]:
                 current_length += 1
             else:
                 if temporary_max < current_length:
                     temporary_max = current_length
                 current_length = 1

         max_length = max(current_length, temporary_max)

         time_stop = time.perf_counter()
         delta = time_stop-start_time                        # max n ~ [70 000 - 70 200]
         n += 1

     print('The max length of chain of series 0 or 1 - ', max_length)
     print('Max n - ', n)  
