# Напишите программу, которая переводит температуру в Кельвинах в Цельсии

if __name__=='__main__':

    print('Enter temperature values in Kelvin:')
    kelvin = float(input())
    if kelvin < 0:
        print('It is not correct')
    else:
        celsius = kelvin-273.15
        print(round(celsius),' C')
