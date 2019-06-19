# Проверить является ли введенное число простым.

def prime_number(a):
    p = 1
    root = int(a**0.5)
    for i in range(2, (root + 1)):
        p = p * (a % i)

    if p == 0:
        return False
    return True


if __name__=='__main__':
    a = 8
    print(prime_number(a))