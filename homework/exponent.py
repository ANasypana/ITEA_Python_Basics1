# Возвести число в степень с помощью цикла

def degree_of_number(a, n):
    s = 1
    for i in range(n):
        s = s * a
    return s


if __name__=='__main__':

    a = 2
    n = 3
    
    print(degree_of_number(a,n))  
