# Нарисовать равнобедренный треугольник

if __name__=='__main__':
    a = input('Enter height of the triangle:\n')
    height = int(a)

    for i in range(height):
        print(' '*(height-i), '^'*(1+2*i))