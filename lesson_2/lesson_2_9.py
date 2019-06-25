# Вывести n чисел фибоначчи

if __name__ == '__main__':
    number = input('Enter n:\n')
    number = str(number)
    while not number.isdigit():
        number = input('Error! Try again. You must enter only number n:\n')
        number = str(number)
    number = int(number)

    series = [1, 1]

    for i in range(2, number):
        series.append(series[i - 2] + series[i - 1])

    print(f'Fibonacci numbers:\n {series}')
