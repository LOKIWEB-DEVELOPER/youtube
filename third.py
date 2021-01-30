from random import choice
from string import digits, ascii_lowercase, ascii_uppercase, punctuation
digits_1 = digits
lowercase_letters = ascii_lowercase
uppercase_letters = ascii_uppercase
punctuation_1 = punctuation
chars = ''
flag = False
while flag == False:
    print('Количество паролей для генерации')
    quantity_passwords = input()
    while quantity_passwords.isdigit() == False: 
        print('Пожалуйста введите целое число')
        quantity_passwords = input()
    quantity_passwords = int(quantity_passwords)
    print('Длина пароля')
    length = input()
    while length.isdigit() == False: 
        print('Пожалуйста введите целое число')
        length = input()
    length = int(length)
    print('Включать ли цифры 0123456789?  да или нет')
    need_numbers = input()
    while need_numbers != 'да' and need_numbers != 'нет':
        print('Пожалуйста напишите "да" или "нет"')
        need_numbers = input()
    print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?  да или нет')
    need_uppercase = input()
    while need_uppercase != 'да' and need_uppercase != 'нет':
        print('Пожалуйста напишите "да" или "нет"')
        need_uppercase = input()
    print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?  да или нет')
    need_lowercase = input()
    while need_lowercase != 'да' and need_lowercase != 'нет':
        print('Пожалуйста напишите "да" или "нет"')
        need_lowercase = input()
    print('Включать ли символы !#$%&*+-=?@^_?  да или нет')
    need_punctuation = input()
    while need_punctuation != 'да' and need_punctuation != 'нет':
        print('Пожалуйста напишите "да" или "нет"')
        need_punctuation = input()
    print('Исключать ли неоднозначные символы il1Lo0O?  да или нет')
    need_ambiguous_characters = input()
    while need_ambiguous_characters != 'да' and need_ambiguous_characters != 'нет':
        print('Пожалуйста напишите "да" или "нет"')
        need_ambiguous_characters = input()
    ambiguous_characters = 'il1Lo0O'
    if need_numbers == 'да':
        chars += digits_1
    if need_uppercase == 'да':
        chars += uppercase_letters
    if need_lowercase == 'да':
        chars += lowercase_letters
    if need_punctuation == 'да':
        chars += punctuation_1
    if need_ambiguous_characters == 'да':
        for g in range(len(ambiguous_characters)):
            chars.replace('ambiguous_characters[g]', '')
    password = ''
    for q in range(quantity_passwords):
        def generate_password(password):
            for p in range(length):
                password += choice( chars )
            return password
        print(generate_password(password))
        password = ''
    print('Сгенерировать снова? да или нет')
    repeat = input()
    while repeat != 'да' and repeat != 'нет':
        print('Пожалуйста напишите "да" или "нет"')
        repeat = input()
    if repeat == 'да':
        flag == False
    else:
        flag = True


