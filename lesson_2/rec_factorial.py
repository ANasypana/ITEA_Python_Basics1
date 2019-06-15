# Напишите функцию, которая возвращает факториал числа

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

    
if __name__=='__main__':
    
    n = 7
    print(n, '!=', factorial(n))         
