# РАБОТАЙ через создание функций def, разделяя каждое действие!!!!
# Консольная игра "Виселица"


import random


def nouns():
    """Логика окрытия словаря"""
    with open('russian_nouns.txt') as noun:
        text = [line.strip() for line in noun]
    return text


def prog_start():
    """Логика старта программы"""
    start = input('Do you want to play? (press y or n) ')
    for i in start:
        if i == 'y':
            print('PC choose a random word. If you guess it, you won!')
        else:
            print('Exit')
            exit()
    return start


def random_word():
    """Логика выбора случайного слова"""
    word = random.choice(nouns())
    # print(word)
    return word


def human_letter():
    """Логика ввода пользователем буквы"""
    insert = input('Enter one letter: ')
    return insert


def is_part_in_word():
    """Логика сравнения введенной буквы и загаданного слова"""
    for w in random_word():
        if w.lower() in human_letter:
            return True
    return False


def add_letter(is_part_in_word):
    """Логика добавления правильной буквы к списку"""
    human_list = []
    while is_part_in_word is True:
        human_list.append(human_letter())
        return human_list
    else:
        exit()


def picture():
    """Логика отрисовки виселицы"""
    pass


prog_start()
random_word()
print(random_word())
# print(human_letter())
# is_part_in_word(human_letter(), random_word())
add_letter(is_part_in_word())
