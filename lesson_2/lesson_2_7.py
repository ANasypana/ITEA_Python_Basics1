# Ввод цифр с клавиатуры до 0
# Показать: количество чисел, которые были Введены; их общую сумму; среднее арифметическое

from mydoc.subsidiary_functions import enter_number_up_to


if __name__ == '__main__':
    sum_elements = 0
    quantity = 0
    number = enter_number_up_to('number from 0 to 9', 9)
    if number == 0:
        print('Your number is null')

    else:
        while number != 0:
            quantity += 1
            sum_elements += number
            number = enter_number_up_to('number from 0 to 9', 9)

        print(f'Sum: \n {sum_elements}')
        print(f'Quantity: \n {quantity}')
        print(f'Mean: \n {sum_elements / quantity}')
