# Нарисовать равнобедренный треугольник

from mydoc.subsidiary_functions import enter_positive_number


if __name__ == '__main__':
    height = enter_positive_number('positive number (height of the triangle)')

    for i in range(height):
        print(' ' * (height - i), '^' * (1 + 2 * i))
