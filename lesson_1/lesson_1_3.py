# Напишите программу, которая считает сколько букв ‘o’ в заданной строке

if __name__ == '__main__':
    word = input('Enter word: \n')
    word = word.upper()
    j = 0

    for i in word:
        if i == 'O':
            j = j+1

<<<<<<< HEAD
    print('Number of "o": ', j)
=======
    print('Number of "o": ', j) 
>>>>>>> 7f6936377cf62bf4f297893c7b2929436b5d6406
