from random import choice

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
"Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет", 
"Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')

print('Как Вас зовут?')
user_name = input()
print('Привет', user_name)

flag = False
while flag == False:
    print('Напишите вопрос')
    question = input()
    answer = choice( answers )
    print(answer)
    print('Хотели бы задать еще вопрос? Напишите Да или Нет')
    second_question = input()
    if second_question == 'Да' or second_question == 'да':
        flag = False
    else:
        print('Возвращайся если возникнут вопросы!')
        flag = True