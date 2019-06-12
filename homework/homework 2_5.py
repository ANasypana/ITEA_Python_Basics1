# Вывести сумму всех делителей заданного числа

if __name__=='__main__':

    print('Enter number: ')
    a = int(input())
    s = 0
    for i in range(2,a):
        if a%i == 0:
            s = s+i
    print(s)