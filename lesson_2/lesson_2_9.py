# Вывести n чисел фибоначчи

from mydoc.subsidiary_functions import enter_positive_number


if __name__ == '__main__':
    number = enter_positive_number('positive number')
    series = [1, 1]

    if number >= 2:
        for i in range(2, number):
            series.append(series[i - 2] + series[i - 1])
        print(f'Fibonacci numbers:\n {series}')
    else:
        print(f'Fibonacci numbers:\n {series[0]}')
