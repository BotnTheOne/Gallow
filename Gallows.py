# РАБОТАЙ через создание функций def, разделяя каждое действие!!!!
# Консольная игра "Виселица"


import random
import re


def start_menu():
    start_input = input('Do you want to play? (press y or n) ')
    if start_input == 'y':
        print('PC choose a random word. If you guess it, you won!')
        main_game_logic()
    elif start_input == 'n':
        print('Exit')
        exit()
    else:
        start_menu()


def create_words_list():
    words_list = ['абажур', 'баклан', 'гонка']
    return words_list


def get_random_from_words_list():
    random_word = random.choice(create_words_list())
    return random_word


def main_game_logic():
    words_list = create_words_list()
    random_word_list = get_random_from_words_list()
    hidden_word = word_to_simbols(random_word_list)
    return words_list, random_word_list, hidden_word


def word_to_simbols(random_word_list):
    random_word = random_word_list.lower()
    symbols = re.sub(r'[а-я]', '_', random_word)
    print(symbols)
    print(random_word) #принт на время тестирования для визуализации загаданного слова
    return symbols


start_menu()
