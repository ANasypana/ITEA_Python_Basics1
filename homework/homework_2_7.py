# Напишите программу “угадай число”

import random


if __name__ == '__main__':
    imagined_number = random.randint(0, 10)
    x = -1

    while x != imagined_number:
        x = input('Enter number from o to 10: \n')
        while not x.isdigit():
            x = input('Error! Try again. You must enter number from o to 10:\n')
        x = int(x)

        if x == imagined_number:
            print('Success!')
        elif x < imagined_number:
            print('The number is larger')
        else:
            print('The number is less')
