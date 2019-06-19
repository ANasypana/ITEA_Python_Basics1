# Написать рекурсивную функцию, которая возвращает сумму цифр числа

def sum_digits(n):
    if n < 10:
        return n
    else:
        sum = n - (n // 10) * 10
        a = n // 10
        return sum + sum_digits(a)


if __name__=='__main__':
    number = 123
    print(sum_digits(number))