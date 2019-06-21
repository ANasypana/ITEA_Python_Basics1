# Выведите случайные числа в заданном пользователем диапазоне

import random

if __name__=='__main__':

    print('Set the range (through ","):')
    entered_data =str(input())

    diapason = entered_data.split(",")
    
    border_1 = int(diapason[0])
    border_2 = int(diapason[1])
    
    if border_1 > border_2:
        print(random.randint(border_2, border_1))
    elif border_1 < border_2:
        print(random.randint(border_1, border_2))
    else:
        print('Incorrect range') 
