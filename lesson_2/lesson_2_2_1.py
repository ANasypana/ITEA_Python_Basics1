# Выведите случайные числа в заданном пользователем диапазоне

import random
from mydoc.subsidiary_functions import enter_diapason


if __name__ == '__main__':
    entered_data = enter_diapason('diapason (through ",")')
    if not entered_data:
        print('Incorrect diapason')
    else:
        print(random.randint(entered_data[0], entered_data[1]))
