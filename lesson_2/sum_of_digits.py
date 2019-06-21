# Найти сумму чисел числа 2 способами

if __name__=='__main__':

    print('Enter number:')
    number = str(input())
    
    sum_1 = 0
    sum_2 = 0
    
    for i in number:
        sum_1=sum_1+int(i)
   
    lenth = len(number)
    for i in range(lenth):
        sum_2 = sum_2+(int(number)%(10**(i+1)))//(10**i)

    print(sum_1)
    print(sum_2) 
