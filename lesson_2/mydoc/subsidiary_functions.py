# subsidiary functions


def enter_positive_number(query):
    number = input(f'Enter {query}:\n')
    while not (number.isdigit() and int(number) > 0):
        number = input(f'Error! Try again. You must enter only {query}:\n')
    return int(number)


def enter_number_up_to(query, up_to):
    number = input(f'Enter {query}:\n')
    diapason = []
    for i in range(up_to + 1):
        diapason.append(i)
    while not (number.isdigit() and int(number) in diapason):
        number = input(f'Error! Try again. You must enter only {query}:\n')
    return int(number)


def enter_diapason(query):
    entered_data = input(f'Set the {query}:\n')
    entered_data = entered_data.replace(' ', '')
    diapason = entered_data.split(",")
    length = len(diapason)
    condition = (length == 2) and (diapason[0] != diapason[1])
    if condition and diapason[0].isdigit() and diapason[1].isdigit():
        border_1 = min(int(diapason[0]), int(diapason[1]))
        border_2 = max(int(diapason[0]), int(diapason[1]))
        return [border_1, border_2]
    else:
        return False


def enter_list_of_numbers(query):
    list_of_data = input(f'Enter {query}:\n')
    check = list_of_data.replace(',', '')
    check = check.replace(' ', '')

    while not check.isdigit():
        list_of_data = input(f'Error! Try again. Enter only {query}):\n')
        check = list_of_data.replace(',', '')
        check = check.replace(' ', '')
    array = list_of_data.split(",")
    return array
