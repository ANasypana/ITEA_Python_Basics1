# Вывести все символы заглавные буквы в строке

if __name__=='__main__':

    print('Enter word:')
    word = str(input())

    for i in word:
        if i.isupper():
            print(i, end=' ')
        continue
