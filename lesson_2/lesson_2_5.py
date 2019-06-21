# Напишите программу, которая выводит сумму введенных пользователем чисел. Числа вводятся одной строкой

if __name__ == '__main__':
    list_of_words = input('Enter list of numbers (through ","):\n')
    list_of_words = str(list_of_words)
    check = list_of_words.replace(',', '')
    check = check.replace(' ', '')

    while not check.isdigit():
        list_of_words = input('Error! Enter list of numbers (through ","):\n')
        list_of_words = str(list_of_words)
        check = list_of_words.replace(',', '')
        check = check.replace(' ', '')

    array = list_of_words.split(",")

    element_sum = 0
    for i in array:
        element_sum += int(i)

    print('Sum: ', element_sum)
