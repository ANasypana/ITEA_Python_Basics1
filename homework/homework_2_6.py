# Нарисовать равнобедренный треугольник

if __name__ == '__main__':
    data = input('Enter height of the triangle:\n')
    data = str(data)
    while not data.isdigit():
        data = input('Error! Try again. You must enter only number:\n')
        data = str(data)
    height = int(data)

    for i in range(height):
        print(' ' * (height - i), '^' * (1 + 2 * i))
