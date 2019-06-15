# Напишите программу, которая считает сколько букв ‘o’ в заданной строке

if __name__=='__main__':

    print('Enter word: ')
    
    word = str(input())
    j = 0
    for i in word:
        if i == 'o' or i == 'O':
            j = j+1

    print('Number of "o": ', j) 
