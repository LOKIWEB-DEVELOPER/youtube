text = input()

flag = False

print('Выберите направление "Шифрование" или "Дешифрование" и напишите')

while flag == False:
    direction = input()
    
    if direction == 'Шифрование' or direction == 'Дешифрование':
    
        flag = True
    
    else:
    
        print('Напишите Шифрование или Дешифрование')

flag = False

print('Укажите язык алфавита a (английский) или р (русский)')

while flag == False:
    
    language_alphabet = input()
    
    if language_alphabet == 'а' or language_alphabet == 'р':
    
        flag = True
    
    else:
    
        print('Укажите язык алфавита а или р')

flag = False

print('Укажите шаг сдвига')

while flag == False:
    
    shift = input()
    
    if (language_alphabet == 'а'):
    
        if shift.isdigit() == True:
    
            shift = int(shift)
    
            if shift >= 0 and shift <= 26:
    
                flag = True
    
            else:
    
                print('Введите целое число от 1 до 26(вкл)')
    
        else:
    
            print('Введите целое число от 1 до 26(вкл)')
    
    elif language_alphabet == 'р':
    
        if shift.isdigit() == True:
    
            shift = int(shift)
    
            if (shift >= 0) and (shift <= 32):
    
                flag = True
    
            else:
    
                print('Введите целое число от 1 до 32(вкл)')
    
        else:
    
            print('Введите целое число от 1 до 32(вкл)')

eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'

eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

if direction == 'Шифрование':

    def data_encryption():

        if language_alphabet == 'р':

            new_text = ''

            for i in range(len(text)):

                if ord(text[i]) >= 1040 and ord(text[i]) <= 1071:

                    intermediate_value = ord(text[i]) + shift

                    if intermediate_value > 1071:

                        intermediate_value = 1039 + (intermediate_value % 1071)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                elif ord(text[i]) >= 1072 and ord(text[i]) <= 1103:

                    intermediate_value = ord(text[i]) + shift

                    if intermediate_value > 1103:

                        intermediate_value = 1071 + (intermediate_value % 1103)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                else:

                    new_text += text[i]

            return new_text

        elif language_alphabet == 'а':

            new_text = ''

            for j in range(len(text)):

                if ord(text[j]) >= 65 and ord(text[j]) <= 90:

                    intermediate_value = ord(text[j]) + shift

                    if intermediate_value > 90:

                        intermediate_value = 64 + (intermediate_value % 90)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                elif ord(text[j]) >= 97 and ord(text[j]) <= 122:

                    intermediate_value = ord(text[j]) + shift

                    if intermediate_value > 122:

                        intermediate_value = 96 + (intermediate_value % 122)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                else:

                    new_text += text[j]

            return new_text

    print(data_encryption())

elif direction == 'Дешифрование':

    def data_decryption():

        if language_alphabet == 'р':

            new_text = ''

            for i in range(len(text)):

                if ord(text[i]) >= 1040 and ord(text[i]) <= 1071:

                    intermediate_value = ord(text[i]) - shift

                    if intermediate_value < 1040:

                        intermediate_value = 1072 - (1040 - intermediate_value)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                elif ord(text[i]) >= 1072 and ord(text[i]) <= 1103:

                    intermediate_value = ord(text[i]) - shift

                    if intermediate_value < 1072:

                        intermediate_value = 1104 - (1072 - intermediate_value)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                else:

                    new_text += text[i]

            return new_text

        elif language_alphabet == 'а':

            new_text = ''

            for j in range(len(text)):

                if ord(text[j]) >= 65 and ord(text[j]) <= 90:
                    
                    intermediate_value = ord(text[j]) - shift
                    
                    if intermediate_value < 65:

                        intermediate_value = 91 - (65 - intermediate_value)

                        new_text += chr(intermediate_value)
                
                elif ord(text[j]) >= 97 and ord(text[j]) <= 122:
                    
                    intermediate_value = ord(text[j]) - shift
                    
                    if intermediate_value < 97:

                        intermediate_value = 123 - (97 - intermediate_value)

                        new_text += chr(intermediate_value)

                    else:

                        new_text += chr(intermediate_value)

                else:

                    new_text += text[j]

            return new_text

    print(data_decryption())


