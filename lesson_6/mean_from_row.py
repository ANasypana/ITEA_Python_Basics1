"""Реалізувати функцію, що буде імпорnувати метод з файла test2.py і передавати в нього список,
який буде формуватись за наступним алгоритмом: кожен елемент складає з себе
середнє арифметичне кожного рядку файла test3_result.txt. Тобто 100 елементний список"""

import pickle
import re
from saved_function import sum_square_of_numbers


def set_array_from(data):
    result_array = []
    with open(data, 'rb') as sent_array:
        text = sent_array.read()
    text = str(text, 'utf8')
    temporary_array = re.split('\n', text)
    for string in temporary_array:
        list_of_number = re.split(' ', string)
        quantity_numbers = len(list_of_number)
        sum_numbers = sum(int(i) for i in list_of_number)
        result_array.append(sum_numbers / quantity_numbers)
    return result_array


if __name__ == '__main__':
    with open('test2.txt', 'rb') as saved_function:
        new_function = pickle.load(saved_function)

    print(new_function(set_array_from('test3_result.txt')))
    print(set_array_from('test3_result.txt'))
