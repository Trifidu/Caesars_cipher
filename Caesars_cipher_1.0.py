# ввод данных
print('Выберите необходимое действие: ')
action = input('1 - шифровать, 2 - дешифровать  ')
while action != '1' and action != '2':
    print('Неверно введенные данные')
    action = input('Пожалуйста, введите: 1 - шифровать или 2 - дешифровать  ')
action = int(action)
print('Выберите нужный словарь: ')
alphabet = input('1 - Русский, 2 - English  ')
while alphabet != '1' and alphabet != '2':
    print('Неверно введенные данные')
    alphabet = ('Пожалуйста, введите: 1 - Русский или 2 - English   ')
alphabet = int(alphabet)
print('Введите на сколько символов необходимо сдвинуть буквы: ')
shift = input('Сдвиг:   ')
while shift.isdigit() != True:
    print('Неверно введенные данные')
    shift = input('Пожалуйста, введите корректный сдвиг ')
shift = int(shift)
print('Какой текст необходимо преобразовать?')
text = input()
while text.isspace() == True:
    print('Неверно введенные данные')
    text = input('Пожалуйста, введите текст')

# шифратор/дешифратор


def caeser_cipher(direction, lang, step, text):
    # словари
    upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    for i in range(len(text)):
        if lang == 1:  # rus
            alpha = 32
            low_alpha = lower_rus_alphabet
            upp_alpha = upper_rus_alphabet
        if lang == 2:  # eng
            alpha = 26
            low_alpha = lower_eng_alphabet
            upp_alpha = upper_eng_alphabet

        if text[i].isalpha():
            if text[i] == text[i].lower():
                place = low_alpha.index(text[i])
            if text[i] == text[i].upper():
                place = upp_alpha.index(text[i])
            # дешифратор
            if direction == 1:
                index = (place - step) % alpha

            # шифратор
            if direction == 2:
                index = (place + step) % alpha

            if text[i] == text[i].lower():
                print(low_alpha[index], end='')
            if text[i] == text[i].upper():
                print(upp_alpha[index], end='')
        else:
            print(text[i], end='')


caeser_cipher(action, alphabet, shift, text)
