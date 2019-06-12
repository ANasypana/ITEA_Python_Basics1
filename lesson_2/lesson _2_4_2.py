# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае

def power2(n):
    if n % 1 != 0:
        return print('No')
    elif n == 1:
        return print('Yes')
    else:
        return power2(n/2)

if __name__=='__main__':
    n = 16
    power2(n)

