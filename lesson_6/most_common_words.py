"""Створити файл test1.txt., добавити текст;
   Знайти і вивести 5 найпопулярніших слів в цьому тексті;
   Результат потрібно  записати в файл test1_result.txt."""

import re


def find_by_value(dictionary, meaning):
    list_of_keys = []
    for key, value in dictionary.items():
        if value == meaning:
            meaning_key = key
            list_of_keys.append(meaning_key)
    length = len(list_of_keys)
    if length > 0:
        return list_of_keys
    else:
        raise ValueError


def set_list_of_words(text):
    text = re.sub('_', ' ', text)
    array = re.findall(r'\b[^ \d, \s]\w+', text)
    return array


def set_most_common_words(array):
    glossary = {}
    glossary_num = {}
    for word in array:
        glossary[word.lower()] = glossary.get(word.lower(), 0) + 1
    array_of_values = list(glossary.values())
    for number in array_of_values:
        glossary_num[number] = find_by_value(glossary, number)
    return glossary_num


def make_string(array):
    string = ", ".join(a for a in array)
    return string


if __name__ == '__main__':

    with open('test1.txt', 'r') as working_text:
        text = working_text.read()
        array = set_list_of_words(text)
        working_text.close()
    glossary = set_most_common_words(array)
    citations = list(glossary.keys())
    citations.sort(reverse=True)
    length = len(citations)

    with open('test1_result.txt', 'w') as result_text:
        if length >= 5:
            info = "\n".join(f'{citations[i]} citations - {make_string(glossary[citations[i]])}' for i in range(5))
            print(info)
            result_text.write(info)
        else:
            info = "\n".join(f'{citations[i]} citations - {make_string(glossary[citations[i]])}' for i in citations)
            print(info)
            result_text.write(info)
        result_text.close()
