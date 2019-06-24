# checking functions


def is_phone_number(number):
    str_number = str(number)
    check_number = str_number.replace(' ', '')
    check_condition = check_number.isdigit() or (check_number[0] == '+' and check_number[1:].isdigit())
    if check_condition:
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
