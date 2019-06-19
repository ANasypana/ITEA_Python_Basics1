# Найти сумму чисел числа 2 способами

if __name__=='__main__':
    number = input('Enter number:\n')
    sum_of_first_method = 0
    sum_of_second_method = 0

    for i in number:
        sum_of_first_method += int(i)

    length = len(number)
    for i in range(length):
        sum_of_second_method += int(number)%(10**(i+1))//(10**i)

    print('Sum of first method: \n', sum_of_first_method)
    print('Sum of second method: \n', sum_of_second_method)