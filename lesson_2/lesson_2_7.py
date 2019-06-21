# Ввод цифр с клавиатуры до 0
#Показать: количество чисел, которые были Введены; их общую сумму; среднее арифметическое

def check_number(n):
    str_number = str(n)
    size = len(n)
    return str_number.isdigit() and size == 1


if __name__ == '__main__':
    elements_sum = 0
    quantity = 0
    number = input('Enter number from 0 to 9:\n')
    check = 1

    while check == 1:

        if check_number(number):  #validation  enter
            number = int(number)
            if number == 0:
                print('Your number is null')
                check = 0

            else:
                while number != 0:
                    quantity += 1
                    elements_sum += number
                    number = input('Enter number from 0 to 9:\n')
                    while not check_number(number):
                        number = input('Error! Enter number from 0 to 9:\n')
                    number = int(number)

                print('Sum: \n', elements_sum)
                print('Quantity: \n', quantity)
                print('Mean: \n', elements_sum / quantity)
                check = 0

        else:
            number = input('Error! Enter number from 0 to 9:\n')
