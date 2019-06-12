# Написать функцию, которая вычисляет среднее арифметическое элементов массива, переданного ей в качестве аргумента

def avrg_array(l):
    sum = 0
    size = len(l)
    for i in l:
        sum = sum + int(i)
    return float(sum/size)

if __name__=='__main__':

    print('Enter the list of numbers (through ","):')
    a=str(input())
    array = a.split(",")
    print(array)
    print('Result of avrg_array:', avrg_array(array))

