# Дано натуральное число N. Выведите все его цифры по одной, в обратном порядке, разделяя их пробелами или новыми строками

def print_digits(n):
    if n < 10:
        print(n)
    else:
        s = n - (n // 10) * 10
        print(s)

        a = n // 10
        return print_digits(a)

if __name__=='__main__':
    n = 246
    print_digits(n)
