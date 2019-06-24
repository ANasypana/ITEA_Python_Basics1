# Напишите программу, которая выводит сумму введенных пользователем чисел. Числа вводятся одной строкой

if __name__ == '__main__':
    list_of_dates = input('Enter list of numbers (through ","):\n')
    list_of_dates = str(list_of_dates)
    check = list_of_dates.replace(',', '')
    check = check.replace(' ', '')

    while not check.isdigit():
        list_of_dates = input('Error! Enter list of numbers (through ","):\n')
        list_of_dates = str(list_of_dates)
        check = list_of_dates.replace(',', '')
        check = check.replace(' ', '')

    array = list_of_dates.split(",")

    sum_elements = 0
    for i in array:
        sum_elements += int(i)

    print(f'Sum: {sum_elements}')
