#Напишите функцию, которая сортирует массив рекурсивно


def recursive_sorting(variety):
    length = len(variety)
    mid = length // 2
    if length <= 1:
        return variety
    else:
        pilot = variety[mid]
        lesser_list = []
        greater_list = []
        p_list = []
        for n in variety:
            if n < pilot:
                lesser_list.append(n)
            elif n > pilot:
                greater_list.append(n)
            else:
                p_list.append(n)
        return recursive_sorting(lesser_list) + p_list + recursive_sorting(greater_list)


if __name__ == '__main__':
    array = [1, 59, 3, 6, 78, 90, 4]
    print(recursive_sorting(array))  