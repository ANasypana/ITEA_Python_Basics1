# Написать функцию, которая вычисляет среднее арифметическое элементов массива

def mean_array(l):
    sum = 0
    size = len(l)
    for i in l:

        if str(i).isdigit():
            sum = sum + int(i)
        else:
            return None

    return float(sum/size)


if __name__=='__main__':
    series = input('Enter the list of numbers (through ","):\n')
    series = str(series)
    array = series.split(",")

    print(array)
    print('Result of mean_array:', mean_array(array))