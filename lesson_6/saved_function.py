"""Написати програму, яка буде зберігати функцію,
   що рахує суми квадратів всіх елементів списку,
   який йому передається в файл test2.py"""

import pickle


def sum_square_of_numbers(array):
    sum_square = sum([int(number) ** 2 for number in array])
    return sum_square


if __name__ == '__main__':

    with open('test2.txt', 'wb') as saved_function:
        pickle.dump(sum_square_of_numbers, saved_function)
