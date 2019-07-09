# checking functions

import re

def transfer_phone(number):
    number = str(number)
    if number.startswith('+'):
        transfer_number = number[1:].replace(' ', '')
    else:
        transfer_number = number.replace(' ', '')
    return transfer_number


def is_phone_number(number):
    str_number = str(transfer_phone(number))
    if str_number.isdigit():
        return True
    else:
        return False


def is_name(name):
    str_name = str(name)
    check_name = str_name.replace(' ', '')
    if check_name.isalpha():
        return True
    else:
        return False


def enter_name(query):
    name = input(f'Enter {query}:\n')
    while not is_name(name):
        name = input(f'Error input. Enter only {query}:\n')
    return name


def enter_number(query):
    number = input(f'Enter {query}:\n')
    while not is_phone_number(number):
        number = input(f'Error input. Enter only {query}:\n')
    return number
