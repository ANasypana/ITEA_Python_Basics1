# Найти факториал числа
def factorial(a):
    if a == 0:
        return 1
    else:
        return a*factorial(a-1)

    
if __name__ == '__main__':

    print('Enter number: ')
    n = int(input())
    print('{}!: '.format(n), factorial(n)) 
