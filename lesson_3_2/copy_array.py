import copy

def copy_array(l):
    result_copy = copy.copy(l)
    return result_copy


if __name__=='__main__':

    array = [w*2 for w in 'python']
    dictionary = {a:a**2 for a in range(1, 6)}

    print(copy_array(array))
    print(copy_array(dictionary))

    dictionary[7] = 7**2
    array.append('java')

    print(copy_array(array))
    print(copy_array(dictionary)) 