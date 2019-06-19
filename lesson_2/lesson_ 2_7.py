# Ввод цифр с клавиатуры до 0
#Показать: количество чисел, которые были Введены; их общую сумму; среднее арифметическое

def check_number(n):
    str_number = str(n)
    size = len(n)
    if str_number.isdigit() and size == 1:
        return True
    else:
        return False


if __name__=='__main__':
    sum = 0
    quantity = 0
    number = input('Enter number from 0 to 9:\n')
    check = 1

    while check == 1:

        if check_number(number):
            number = int(number)
            if number == 0:
                print('Your number is null')
                check = 0

            else:
                while number != 0:
                    quantity += 1
                    sum += number
                    number = input('Enter number from 0 to 9:\n')
                    while not check_number(number):
                        number = input('Error! Enter number from 0 to 9:\n')
                    number = int(number)

                print('Sum: \n', sum)
                print('Quantity: \n', quantity)
                print('Mean: \n', sum / quantity)
                check = 0

        else:
            number = input('Error! Enter number from 0 to 9:\n')