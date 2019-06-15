
if __name__=='__main__':
    
    side_rectangle_1 = 10
    side_rectangle_2 = 20

    for i in range(side_rectangle_1):
        if i == 0 or i == side_rectangle_1-1:
            for j in range(side_rectangle_2):
                print('*', end='')
        else:
            print('*', end='')
            for j in range(1, side_rectangle_2-1):
                print(' ', end='')
            print('*', end='')
        print()