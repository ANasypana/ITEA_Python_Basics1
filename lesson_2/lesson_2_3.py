# Извлекать квадратный корень из введенного пользователем числа до тех пор, пока значение больше 10

import math
from mydoc.subsidiary_functions import (enter_positive_number, )


if __name__ == '__main__':
    number = enter_positive_number('positive number')

    while math.sqrt(number) > 10:
        print(math.sqrt(number))
        number = enter_positive_number('positive number')
    print('Square root of number <10')
