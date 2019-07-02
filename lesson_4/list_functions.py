# Без использования методов списков, напишите реализацию таких методов списков: insert, remove.


def insert_method(variety, index, value):
    length = len(variety)
    if index < 0:
        index += length

    if 0 < index < length:
        result_method = variety[:index] + [value] + variety[index:]
    elif index <= 0:
        result_method = [value] + variety
    else:
        result_method = variety + [value]

    return result_method


def remove_method(variety, value):
    length = len(variety)
    index = -1

    for i in range(length):
        if variety[i] == value:
            index = i
            break

    if 0 < index < length:
        result_method = variety[:index] + variety[index + 1:]
    elif index == 0:
        result_method = variety[1:]
    elif index == length:
        result_method = variety[:length]
    else:
        return None

    return result_method


if __name__ == '__main__':
    array = [0, 1, 2, 3, 4, 5, 6]

    print(insert_method(array, 0, 'rrr'))
    print(remove_method(array, 6))
    print(remove_method(array, 'tt'))  
