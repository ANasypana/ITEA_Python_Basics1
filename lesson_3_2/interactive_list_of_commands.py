'''Реализовать интерактивное меню с опциями выбора:
    добавление в справочник
    вывод номера телефона по имени
    вывод имени по номеру телефона
    удаления человека из справочника
    редактирования номера\имени
Посчитать количество номеров телефонов в предыдущем примере, в которых есть 3 или более одинаковых цифр подряд'''

from mydoc.dic_functions import (add_to_dictionary,
                              select_by_name,
                              select_by_phone,
                              remove_from_dictionary,
                              edit_contact,
                              count_digits, )

from mydoc.checking import (is_phone_number,
                            is_name, )


if __name__ == '__main__':

    phone_book = dict([('Anna', '+067 780 33 33'),
                       ('James', '+050 235 09 67'),
                       ('John', '+095 106 89 53'),
                       ('Oliver', '+097 123 33 34'),
                       ('Dylan', '+067 890 33 67')])

    function_dictionary = {
        1: add_to_dictionary,
        2: select_by_name,
        3: select_by_phone,
        4: remove_from_dictionary,
        5: edit_contact,
        6: -1
    }

    result_of_select = 0

    while result_of_select != -1:
        result_of_select = input('Please, select what you want to do:\n'
                                 '1 - add name and phone to phone book\n'
                                 '2 - select phone by name\n'
                                 '3 - select name by phone number\n'
                                 '4 - remove person from the phone book\n'
                                 '5 - redact contact (phone number) \n'
                                 '6 - exit\n')

        if str(result_of_select).isdigit() and (int(result_of_select) in function_dictionary.keys()):
            result_of_select = int(result_of_select)
            if result_of_select in [1, 5]:
                name = input('Enter name:\n')
                while not is_name(name):
                    name = str(input('Error input. Enter only name:\n'))

                phone_number = input('Enter phone number:\n')
                while not is_phone_number(phone_number):
                    phone_number = str(input('Error input. Enter only  phone number:\n'))

                option = function_dictionary[result_of_select]
                print(option(phone_book, name, phone_number))

            elif result_of_select in [2, 4]:
                name = input('Enter name:\n')
                while not is_name(name):
                    name = input('Error input. Enter only name:\n')

                option = function_dictionary[result_of_select]
                print(option(phone_book, name))

            elif result_of_select == 3:
                phone_number = input('Enter phone number:\n')
                while not is_phone_number(phone_number):
                    phone_number = input('Error input. Enter only  phone number:\n')

                option = function_dictionary[result_of_select]
                print(option(phone_book, phone_number))

            else:
                result_of_select = -1
                print('Thank you:)\n')

        else:
            answer = input('Error!  Your must choose one of: 1, 2, 3, 4, 5 or 6\n'
                           'Would you like to continue? (Y/N)\n')
            answer = str(answer).upper()
            if answer == 'Y':
                result_of_select = 0
            else:
                result_of_select = -1
                print('Thank you:)\n')

    quantity = len(count_digits(phone_book))
    name_array = count_digits(phone_book)
    print(f'There is/are {quantity} phone number with 3 or more identical digits')

    for name in name_array:
        print(f'{name}: {phone_book[name]}')
