# Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае

def power_2(n):
    if n % 1 != 0:
        return 'No'
    elif n == 1:
        return 'Yes'
    else:
        return power_2(n/2)


if __name__=='__main__':
    n = 12
    print(power_2(n))