 # Выводить буквы строки, до первой заглавной

if __name__=='__main__':

    s = 'tttpImmP'

    for i in s:
        if i.isupper():
            break
        print(i, end='')        
