# Напишите программу используя цикл с предусловием while для вывода каждого четного положительного числа от 0 до 20

if __name__ == '__main__':
    i = 2

    while i <= 20:
        if i % 2 == 0:
            print(i, end=' ')
        i += 1
