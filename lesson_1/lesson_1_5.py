# Напишите программу, которая считает сумму последних цифр двух введенных пользователем чисел


def enter_number(number):
    num = input(f'Enter {number}:\n')
    while not num.isdigit():
        num = input('Error! Try again. You must enter only number:\n')
    return num


if __name__ == '__main__':
    first_number = enter_number('first number')
    second_number = enter_number('second number')

    first_digit = first_number[-1]
    second_digit = second_number[-1]

    result = int(first_digit) + int(second_digit)
    print(f'Sum of last digits - {result}')
