# Вывести квадраты всех чисел от 1 до 10

if __name__=='__main__':

    for i in range(1,11):
        
        if i == 10:
            print(i**2, end='')
        else:
            print(i ** 2, end=', ') 
