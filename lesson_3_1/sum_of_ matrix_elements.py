
def sum_elements(l):

    sum = 0

    for row in l:
        for elem in row:
            sum += int(elem)
    return sum


if __name__=='__main__':

    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sum_elements(array))
