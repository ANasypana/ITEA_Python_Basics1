# Найти факториал числа

def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)


if __name__ == '__main__':
    n = int(input('Enter number: \n'))
    print('Factorial {}! - '.format(n), factorial(n))