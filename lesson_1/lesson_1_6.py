# Напишите программу, которая переводит температуру в Кельвинах в Цельсии

if __name__ == '__main__':
    kelvin = float(input('Enter temperature values in Kelvin:\n'))

    if kelvin < 0:
        print('It is not correct')
    else:
        celsius = kelvin-273.15
        print(round(celsius, 2), ' C')
