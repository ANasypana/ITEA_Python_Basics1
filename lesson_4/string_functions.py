# Без использования методов строк, напишите реализацию таких методов строк: replace, split, find.
# Напишите функцию remove по индексу и по подстроке.


def string_replace(s, new, old, count=-1):
    length_string = len(s)
    length_old = len(old)
    s_result = ''
    i = 0

    if count < 0:
        count = length_string

    while i < length_string:
        if (s[i:i + length_old] == old) and count > 0:
            s_result += new
            i += length_old
            count -= 1
        else:
            s_result += s[i]
            i += 1
    return s_result


def string_split(s, separator=' ',  count=-1):
    length_string = len(s)
    length_sep = len(separator)
    array = []
    i = 0

    if count < 0:
        count = length_string

    while (length_string > length_sep) and count > 0:
        if s[i:i + length_sep] == separator:
            array.append(s[0:i])
            s = s[i + length_sep:]
            length_string = len(s)
            count -= 1
            i = 0
        else:
            i += 1
    if count == 0:
        array.append(s)
    elif count > 0:
        if s[0:length_sep] == separator:
            array.append('')
            array.append(s[length_sep:])
        else:
            array.append(s)
    return array


def string_find(s, sub, start=0, end=-1):
    length_string = len(s)
    length_sub = len(sub)

    if end < 0:
        end = length_string + end
    elif abs(end) > length_string:
        return -1

    if abs(start) > length_string:
        return -1
    elif start < 0:
        start += length_string

    if start > end:
        return -1

    i = start
    find_index = -1

    while i <= end:
        if s[i:i + length_sub] == sub:
            find_index = i
            i = end + 1
        else:
            i += 1

    return find_index


def remove_by_index(s, index):
    length = len(s)
    s_result = ''

    if abs(index) > length:
        return s
    elif index < 0:
        index += length
        for i in range(length):
            if i != index:
                s_result += s[i]
    elif index >= 0:
        for i in range(length):
            if i != index:
                s_result += s[i]

    return s_result


def remove_by_substring(s, sub, start=0, end=-1):
    length_string = len(s)
    length_sub = len(sub)

    if end < 0:
        end = length_string + end
    elif abs(end) > length_string:
        return s

    if abs(start) > length_string:
        return s
    elif start < 0:
        start = length_string + start

    if start > end:
        return None

    i = start
    find_index = -1

    while i <= end:
        if s[i:i + length_sub] == sub:
            find_index = i
            i = end + 1
        else:
            i += 1
    if find_index > 0:
        s_result = s[0:find_index] + s[find_index+length_sub:]
    elif find_index == 0:
        s_result = s[length_sub:]
    else:
        s_result = s

    return s_result


if __name__ == '__main__':
    string = 'laaasaaaahjaanu'
    print(string_replace(string, 'ccc', 'aaa'))
    print(string_split(string, 'aa'))
    print(string_find(string, 'an'))
    print(remove_by_index(string, 13))
    print(remove_by_substring(string, 'la'))  
