# Найти факториал числа

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)


if __name__ == '__main__':
    n = input('Enter number: \n')
    n = str(n)
    while not n.isdigit():
        n = input('Error! Try again. You must enter only number:\n')
        n = str(n)
    n = int(n)

    print(f'{n}! = {factorial(n)}')
