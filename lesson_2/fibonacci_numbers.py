# Вывести n чисел фибоначчи

if __name__=='__main__':

    print('Enter n:')
    number = int(input())
    
    list = [1, 1]
    
    for i in range(2, number):
        list.append(list[i-2]+list[i-1])

    print('Fibonacci numbers: ', list) 
