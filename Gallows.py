# РАБОТАЙ через создание функций def, разделяя каждое действие!!!!
# Консольная игра "Виселица"


import random
import re


hangman_picture = (
    "+---+\n"
    "|   |\n"
    "|\n"
    "|\n"
    "|\n"
    "|\n"
    "=========\n",
    "+---+\n"
    "|   |\n"
    "|  ( )\n"
    "|   \n"
    "|   \n"
    "|   \n"
    "=========\n",
    "=========\n"
    "+---+\n"
    "|   |\n"
    "|  ( )\n"
    "|   |\n"
    "|   \n"
    "|   \n"
    "=========\n",
    "=========\n"
    "+---+\n"
    "|   |\n"
    "|  ( )\n"
    "|  \|\n"
    "|   \n"
    "|   \n"
    "=========\n",
    "=========\n"
    "+---+\n"
    "|   |\n"
    "|  ( )\n"
    "|  \|/\n"
    "|   \n"
    "|   \n"
    "=========\n",
    "=========\n"
    "+---+\n"
    "|   |\n"
    "|  ( )\n"
    "|  \|/\n"
    "|   |\n"
    "|  / \\\n"
    "|   \n"
    "=========\n",
)


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
    words_list = ['баклажка']
    return words_list


def get_random_from_words_list():
    random_word = random.choice(create_words_list())
    return random_word


def main_game_logic():
    words_list = create_words_list()
    random_word_list = get_random_from_words_list()
    hidden_word = word_to_simbols(random_word_list)
    player_letter_input = player_input()
    return words_list, random_word_list, hidden_word, player_letter_input


def word_to_simbols(random_word_list):
    random_word = random_word_list.lower()
    symbols = re.sub(r'[а-я]', '_', random_word)
    print(symbols)
    print(random_word)  # удалить после тестов
    return symbols


used_letters_list = ''
mistake_count = 0


def player_input():
    inputed_letter = input('Enter your letter here: ')
    global mistake_count
    global used_letters_list
    word = get_random_from_words_list()
    if inputed_letter.lower() in word.lower():
        print(used_letters_list) # удалить
    else:
        if mistake_count == 5:
            print('You loose this game!')
            start_menu()
        used_letters_list = check_inputed_letters(inputed_letter, used_letters_list)
        print(used_letters_list) # удалить
        mistake_count += 1
    show_of_draw_hangman(mistake_count)
    print(f'Count of mistakes: {mistake_count}')
    return player_input()


def show_of_draw_hangman(index):
    print(hangman_picture[index])


def check_inputed_letters(inputed_letter, used_letters_list):
    if inputed_letter not in used_letters_list:
        used_letters_list += inputed_letter
    return used_letters_list


start_menu()
