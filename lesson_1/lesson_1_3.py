# Напишите программу, которая считает сколько букв ‘o’ в заданной строке

if __name__ == '__main__':
    word = input('Enter word: \n')
    word = word.upper()
    quantity = word.count('O')

    print(f'Number of "o" - {quantity}')
