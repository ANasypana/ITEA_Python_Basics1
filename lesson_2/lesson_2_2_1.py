# Выведите случайные числа в заданном пользователем диапазоне

import random


if __name__ == '__main__':
    entered_dates = input('Set the range (through ","):\n')
    entered_dates = entered_dates.replace(' ', '')
    diapason = entered_dates.split(",")
    length = len(diapason)

    if length > 1 and diapason[0].isdigit() and diapason[1].isdigit():

        border_1 = int(diapason[0])
        border_2 = int(diapason[1])

        if border_1 > border_2:
            print(random.randint(border_2, border_1))
        else:
            print(random.randint(border_1, border_2))

    else:
        print('Incorrect diapason')
