# Нарисовать равнобедренный треугольник

if __name__=='__main__':

    print('Enter number:')
    a = int(input())
    for i in range(a):
        print(' '*(a-i),'^'*(1+2*i))