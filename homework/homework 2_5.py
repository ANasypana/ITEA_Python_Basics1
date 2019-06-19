# Вывести сумму всех делителей заданного числа

if __name__=='__main__':
    a = int(input('Enter number: \n'))
    s = 0

    for i in range(2, a):
        if a%i == 0:
            s = s+i
    print(s)