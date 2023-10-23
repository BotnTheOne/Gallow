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
    words_list = ['абажур', 'баклан', 'гонка']
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


def player_input():
    players_input = input('Enter your letter here: ')
    player_word = []
    player_mistake = 0
    if players_input in get_random_from_words_list():
        player_word.append(players_input)
        print(player_word) # удалить
    else:
        show_of_draw_hangman(player_mistake)
        player_mistake += 1 # проверь данное выражение(пострайся пройтись циклом while по ошибкам)
    return players_input



# def mistake_counter():
#     for i in picture_of_hangman():
#         print(i)
#     # print(picture_of_hangman())


def show_of_draw_hangman(index):
    print(hangman_picture[index])



start_menu()
