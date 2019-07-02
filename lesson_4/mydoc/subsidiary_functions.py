# subsidiary functions


def enter_positive_number(query):
    number = input(f'Enter {query}:\n')
    while not (number.isdigit() and int(number) > 0):
        number = input(f'Error! Try again. You must enter only {query}:\n')
    return int(number)
