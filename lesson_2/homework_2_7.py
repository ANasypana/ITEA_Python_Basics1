# Напишите программу “угадай число”

import random
from mydoc.subsidiary_functions import (enter_number_up_to, )


if __name__ == '__main__':
    imagined_number = random.randint(0, 10)
    x = -1

    while x != imagined_number:
        x = enter_number_up_to('number from 0 to 10', 10)

        if x == imagined_number:
            print('Success!')
        elif x < imagined_number:
            print('The number is larger')
        else:
            print('The number is less')
