#Напишите функцию, которая сортирует массив рекурсивно
"""Hoare algorithm"""


def recursive_sorting(array):
    length = len(array)
    if length <= 1:
        return array
    else:
        mid = length // 2
        pilot = array[mid]
        lesser_list = []
        greater_list = []
        p_list = []
        for n in array:
            if n < pilot:
                lesser_list.append(n)
            elif n > pilot:
                greater_list.append(n)
            else:
                p_list.append(n)
        return recursive_sorting(lesser_list) + p_list + recursive_sorting(greater_list)


if __name__ == '__main__':
    array = [1, 777, 1, 59, 3, 6, 78, 90, 4]
    print(recursive_sorting(array))   
