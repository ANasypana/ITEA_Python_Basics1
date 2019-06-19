# Вывести n чисел фибоначчи

if __name__=='__main__':
    number = int(input('Enter n:\n'))
    series = [1, 1]

    for i in range(2, number):
        series.append(series[i-2] + series[i-1])

    print('Fibonacci numbers: ', series)