# Вывести прямоугольник со сторонами a,b

if __name__ == '__main__':
    height_rectangle = 10
    length_rectangle = 30
    sign = '*'
    first_pattern = sign * length_rectangle
    second_pattern = sign + ' ' * (length_rectangle - 2) + sign

    for i in range(height_rectangle):
        if i == 0 or i == (height_rectangle - 1):
            print(first_pattern)
        else:
            print(second_pattern)
