# Вывести все символы заглавные буквы в строке

if __name__ == '__main__':
    word = input('Enter word:\n')

    for i in word:
        if i.isupper():
            print(i, end=' ')
