# Организовать непрерывный ввод цифр с клавиатуры, пока пользователь НЕ введёт 0 После ввода нуля, показать на экран количество чисел, которые были Введены, их общую сумму и среднее арифметическое

if __name__=='__main__':

    print('Enter number:')
    number = int(input())
    sum = 0
    quantity = 0
    if number != 0:
        while number != 0:
            quantity = quantity+1
            sum = number+sum
            print('Enter number:')
            number = int(input())
        print('Sum: ', sum)
        print('Quantity ', quantity)
        print('Mean: ', sum/quantity)
    else:
        print('Your number is null')
