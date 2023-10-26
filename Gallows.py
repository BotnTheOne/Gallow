# РАБОТАЙ через создание функций def, разделяя каждое действие!!!!
# Консольная игра "Виселица"
# Добавить валидацию символов
# Откорректировать внешний вид вывода результатов в соответствии с Википедией
# Допилить запуск программы через __name__ == '__main__':

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
    words_list = ['zara']
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
    symbols = re.sub(r'[a-z]', '_', random_word)
    print(symbols)
    print(random_word)  # удалить после тестов
    return symbols


used_letters_list = ''
simbols = list(word_to_simbols(random_word_list=get_random_from_words_list()))


def player_input():
    global simbols_word, mistake_count
    global used_letters_list
    word = get_random_from_words_list()
    final_word = word[:]
    while simbols != final_word:
        inputed_letter = input('Enter your letter here: ')
        mistake_count = 0
        for ref_indx, let in enumerate(final_word):
            if let == inputed_letter:
                simbols[ref_indx] = inputed_letter
                simbols_word = ''.join(simbols)
        if inputed_letter not in final_word:
            used_letters_list = check_inputed_letters(inputed_letter, used_letters_list)
            mistake_count += len(used_letters_list)
        if mistake_count == 5:
            print('You loose the game!')
            start_menu()
        if simbols_word == final_word:
            print(f'You won! The word was: {simbols_word}')
            start_menu()
        show_of_draw_hangman(mistake_count)
        print(f'Word is: {simbols_word}')
        print(f'Count of mistakes: {mistake_count}')
        print(f'Used letters: {used_letters_list}')

    # else:
    #     if mistake_count == 5:
    #         print('You loose this game!')
    #         start_menu()
    #     used_letters_list = check_inputed_letters(inputed_letter, used_letters_list)
    #     print(used_letters_list)
    #     mistake_count += 1
    # show_of_draw_hangman(mistake_count)
    # print(f'Count of mistakes: {mistake_count}')
    # print(f'Used letters: {used_letters_list}')
    # # return player_input()


def show_of_draw_hangman(index):
    print(hangman_picture[index])


def check_inputed_letters(inputed_letter, used_letters_list):
    if inputed_letter not in used_letters_list:
        used_letters_list += inputed_letter
    return used_letters_list


start_menu()
