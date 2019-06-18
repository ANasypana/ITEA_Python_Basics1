
if __name__=='__main__':
    
    hight_rectangle = 10
    length_rectangle = 30

    for i in range(hight_rectangle):
        if i == 0 or i == hight_rectangle - 1:
            for j in range(length_rectangle):
                print('*', end='')
        else:
            print('*', end='')
            for j in range(1, length_rectangle - 1):
                print(' ', end='')
            print('*', end='')
        print()