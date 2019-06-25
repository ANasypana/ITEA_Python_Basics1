# Вывести сумму всех делителей заданного числа

if __name__ == '__main__':
    data = input('Enter number: \n')
    data = str(data)
    while not data.isdigit():
        data = input('Error! Try again. You must enter only number:\n')
        data = str(data)
    data = int(data)

    sum_divisors = 0
    for i in range(2, data):
        if data % i == 0:
            sum_divisors += i

    print(f'The sum of dividers {data} - {sum_divisors}')
