
def add_to_dictionary(d):
    name = input('Please, enter name:\n')

    if d.get(name) is None:
        phone_number = input('Enter phone number:\n')
        d[name] = phone_number
        print('Subscriber added')
    else:
        answer = input('This subscriber exists, number - {}. '
                       'Would you like to change number (Y/N)\n'.format(d[name])).upper()
        if answer == 'Y':
            phone_number = input('Enter phone number:\n')
            d[name] = phone_number
            print('Phone number was changed')


def remove_from_dictionary(d):
    name = input('Enter name to remove:\n')

    if d.get(name) is None:
        print('This subscriber does not exist')
    else:
        d.pop(name)
        print('Subscriber deleted.')


def edit_dictionary(d):
    element_dictionary = input('Enter name or phone number:\n')

    if element_dictionary in d.keys():
        temporary_key = element_dictionary
        temporary_values = d[temporary_key]
        status_enter = 1
    elif element_dictionary in d.values():
        temporary_values = element_dictionary
        status_enter = 1
        for key, value in d.items():
            if value == temporary_values:
                temporary_key = key
    else:
        status_enter = 0
        print('This subscriber does not exist')

    if  status_enter == 1:
        answer = input('Would you like to change:\n'
                       '1 - name and phone number\n'
                       '2 - phone number\n'
                       '3 - name\n')
        if  str(answer).isdigit() is False:
            answer = input('Error! Try again. Your must choose one of: 1, 2 or 3\n')

        elif int(answer) > 3 or int(answer) < 1:
            answer = input('Error! Try again. Your must choose one of: 1, 2 or 3\n')

        else:
            if int(answer) == 1:
                new_name = input('Enter new name:\n')
                new_number = input('Enter new number:\n')
                d.update([(new_name, new_number)])
                d.pop(temporary_key)
                print('Name and phone number were changed')
            elif int(answer) == 2:
                new_number = input('Enter new  phone number:\n')
                d[temporary_key] = new_number
                print('Phone number was changed')
            elif int(answer) == 3:
                new_name = input('Enter new name:\n')
                d.update([(new_name, temporary_values)])
                d.pop(temporary_key)
                print('Name was changed')


def select_elements(d):
    answer = input('Would you like to search out:\n'
                   '1 - name by phone number\n'
                   '2 - phone number by name\n')

    if str(answer).isdigit() is False:
        answer = input('Error! Try again. Your must choose one of: 1 or 2\n')

    elif  int(answer) == 1:
        phone_number = input('Enter phone number\n')
        if phone_number in d.values():
            for key, value in d.items():
                if value == phone_number:
                    name = key
            print('{} has this number'.format(name))
        else:
            print('This subscriber does not exist')

    elif int(answer) == 2:
        name = input('Enter name\n')
        if name in d.keys():
            print('{} has phone number:'.format(name), d[name])
        else:
            print('This subscriber does not exist')

    else:
        print('Error! Try again. Your must choose one of: 1 or 2')


def count_digits(d):
    array = list(d.values())
    result = []
    temporary_list = []

    for phone in array:
        tem_phone = phone.replace(" ", "")
        n = len(tem_phone)

        for i in range(2, n):
            if tem_phone[i] == tem_phone[i-1] and tem_phone[i-1] == tem_phone[i-2] and str(tem_phone[1]).isdigit():
                temp = phone
                for key, value in d.items():
                    if value == temp:
                        temporary_key = key
                temporary_list.append(temporary_key)

    for i in temporary_list:
        if i not in result:
            result.append(i)

    return result             ##list of keys (values - %digitdigitdigit%)


if __name__=='__main__':
    phone_book = dict([('Anna', '+067 780 33 33'),
                       ('James', '+050 235 09 67'),
                       ('John', '+095 106 89 53'),
                       ('Oliver', '+097 123 33 34'),
                       ('Dylan', '+067 890 33 67')])

    result_of_select = 0

    while result_of_select != -1:
        print('Please, select what you want to do:\n',
              '1 - add name and phone to phone book\n',
              '2 - remove person from the phone book\n',
              '3 - redact name and phone\n',
              '4 - select phone by name or name by phone\n'
              ' 5 - exit\n')
        result_of_select = input()

        if not str(result_of_select).isdigit():
            print('Error! Try again. Your must choose one of: 1, 2, 3, 4 or 5')
            result_of_select = input(' ')

        if int(result_of_select) == 1:
            add_to_dictionary(phone_book)

        elif int(result_of_select) == 2:
            remove_from_dictionary(phone_book)

        elif int(result_of_select) == 3:
            edit_dictionary(phone_book)

        elif int(result_of_select) == 4:
            select_elements(phone_book)

        elif int(result_of_select) == 5:
            result_of_select = -1

        else:
            print('Error! Try again. Your must choose one of: 1, 2, 3, 4 or 5')

    print('Thank you!\n')

    amount_phone = len(count_digits(phone_book))
    tem_array = count_digits(phone_book)
    print('There is/are {} phone number with 3 or more identical digits'.format(amount_phone))

    for name in tem_array:
        print(name, '- ', phone_book[name])