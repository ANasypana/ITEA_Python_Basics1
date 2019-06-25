# Ввод цифр с клавиатуры до 0
# Показать: количество чисел, которые были Введены; их общую сумму; среднее арифметическое


def check_number(n):
    str_number = str(n)
    size = len(n)
    return str_number.isdigit() and size == 1


if __name__ == '__main__':
    sum_elements = 0
    quantity = 0
    number = input('Enter number from 0 to 9:\n')
    check = 1

    while check == 1:

        if check_number(number):                        #validation  enter
            number = int(number)
            if number == 0:
                print('Your number is null')
                check = 0

            else:
                while number != 0:
                    quantity += 1
                    sum_elements += number
                    number = input('Enter number from 0 to 9:\n')
                    while not check_number(number):
                        number = input('Error! Enter number from 0 to 9:\n')
                    number = int(number)

                print(f'Sum: \n {sum_elements}')
                print(f'Quantity: \n {quantity}')
                print(f'Mean: \n {sum_elements / quantity}')
                check = 0

        else:
            number = input('Error! Enter number from 0 to 9:\n')
