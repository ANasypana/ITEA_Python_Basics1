# Напишите программу “угадай число”

import random


if __name__=='__main__':
    imagined_number = random.randint(0, 10)
    x = -1

    while x != imagined_number:
        x = int(input('Enter number from o to 10: \n'))
        if x == imagined_number:
            print('Success!')
        elif x < imagined_number:
            print('The number is larger')

        else:
            print('The number is less')