# checking functions


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
