# Без использования методов списков, напишите реализацию таких методов списков: insert, remove.


def insert_method(variety, index, value):    # into the list
    result_method = []
    length = len(variety)

    if index < 0:
        index = length + index
    if (index < length) and (index > 0):
        for i in range(index):
            result_method[i:i] = [variety[i]]
        result_method[index:index] = [value]
        for i in range(index+1, length+1):
            result_method[i:i] = [variety[i-1]]
    elif index <= 0:
        result_method[0:0] = [value]
        for i in range(1, length +1):
            result_method[i:i] = [variety[i-1]]
    else:
        result_method = variety
        result_method[length:length] = [value]

    return result_method


def remove_method(variety, value):   # remove from the list
    result_method = []
    length = len(variety)
    index = -1

    for i in range(length):
        if variety[i] == value:
            index = i
            break

    if (index > 0) and (index < length):
        for i in range(index):
            result_method[i:i] = [variety[i]]
        for i in range(index+1, length):
            result_method[i-1:i-1] = [variety[i]]
    elif index == 0:
        for i in range(1, length):
            result_method[i-1:i-1] = [variety[i]]
    elif index == length:
        for i in range(length-1):
            result_method[i:i] = [variety[i]]
    else:
        return None

    return result_method


if __name__=='__main__':
    array = [0, 1, 2, 3, 4, 5, 6]

    print(insert_method(array, 1, 'rrr'))
    print(remove_method(array, 4))
    print(remove_method(array, 'tt'))  
