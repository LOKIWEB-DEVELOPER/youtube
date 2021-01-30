from random import randint
from math import ceil
flag_0 = True
while flag_0 == True:
    print('Добро пожаловать в числовую угадайку')
    print('Укажите число - правую границу промежутка для случайного выбора')
    n_2 = int(input())
    n = randint(0, n_2)
    flag = False
    flag_2 = False
    print('Напишите предполагаемое число')
    n_u = input()
    count = 1
    
    while flag_2 == False:
        
        def is_valid(n_u):
            if n_u.isdigit() == True:
                return True
            else:
                print('А может быть все-таки введем целое число от 1 до 100?')
                return False
        
        flag = is_valid(n_u)
        
        if flag == True:
            n_u = int(n_u)
            if n_u < n:
                flag_2 = False
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n_u > n:
                flag_2 = False
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n_u == n:
                print('Вы угадали, поздравляем!')
                break
        
        count += 1
        n_u = input()
    print('Вам потребовалось', count, 'попыток')
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')