# dictionary functions


def add_to_dictionary(d, name, phone_number):
    if name in d.keys():
        return f'This subscriber {name} exists, number - {d[name]}.\n'
    else:
        d[name] = phone_number
        return 'Subscriber added'


def select_by_name(d, name):
    if name in d.keys():
        return f'{name} has phone number: {d[name]}'
    else:
        return 'This number does not exist'


def select_by_phone(d, phone_number):
    temporary_d = {}
    for key in d.keys():
        temporary_value = d[key]
        temporary_value = str(temporary_value)
        if temporary_value[0] == '+':
            temporary_value = temporary_value[1:]
        temporary_value = temporary_value.replace(' ', '')
        temporary_d[key] = temporary_value

    phone_number = str(phone_number)
    if phone_number[0] == '+':
        phone_number = phone_number[1:]
    phone_number = phone_number.replace(' ', '')

    if phone_number in temporary_d.values():
        list_of_subscribers = []
        for key, value in temporary_d.items():
            if value == phone_number:
                name = key
                list_of_subscribers.append(name)
        for i in list_of_subscribers:
            return f'{i} has the number - {d[i]}'
    else:
        return 'This number does not exist'


def remove_from_dictionary(d, name):
    if name in d.keys():
        d.pop(name)
        return 'Subscriber deleted.'
    else:
        return 'This subscriber does not exist'


def edit_contact(d, name, phone_number):
    if name in d.keys():
        d[name] = phone_number
        return f'The phone number  of {name} was changed'
    else:
        return 'This subscriber does not exist'


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
