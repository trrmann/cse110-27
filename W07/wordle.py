import os
from random import *
from pathlib import Path

random_key = "random"
word_list_key = "wordList"
secret_word_key = "secretWord"
count_key = "count"
guess_key = "guess"
hint_key = "hint"
number_of_players_key = "numberOfPlayers"

def file_exists(file_name):
    return os.path.exists(file_name)

def is_file(file_name):
    if file_exists(file_name): return Path(file_name).is_file
    else: return False

def clear_screen():
    print("\n" * 6)
    os.system("cls")

def is_guess_size_incorrect(play_data):
    return len(play_data[play_data[count_key]][guess_key]) != len(play_data[secret_word_key])

def is_guess_incorrect(play_data):
    return play_data[play_data[count_key]][guess_key].lower() != play_data[secret_word_key].lower()

def is_match(play_data, index):
    return play_data[play_data[count_key]][guess_key][index] == play_data[secret_word_key][index]

def is_in(play_data, index):
    return play_data[play_data[count_key]][guess_key][index] in play_data[secret_word_key]

def is_multi_player(play_data):
    return play_data[number_of_players_key] > 1

def player_number(play_data):
    return (play_data[count_key] % play_data[number_of_players_key]) + 1

def turn_number(play_data):
    return int(play_data[count_key] / play_data[number_of_players_key]) + 1

def process_incorrect_guess_size(play_data):
    print("Sorry, the guess must have the same number of letters as the secret word.\n")
    play_data[play_data[count_key]][hint_key] = "_ " * len(play_data[secret_word_key])
    return play_data

def process_match(play_data, index):
    play_data[play_data[count_key]][hint_key] = f"{play_data[play_data[count_key]][hint_key]}{play_data[play_data[count_key]][guess_key][index].upper()} "
    return play_data

def process_in(play_data, index):
    play_data[play_data[count_key]][hint_key] = f"{play_data[play_data[count_key]][hint_key]}{play_data[play_data[count_key]][guess_key][index].lower()} "
    return play_data

def process_no_match(play_data, index):
    play_data[play_data[count_key]][hint_key] = f"{play_data[play_data[count_key]][hint_key]}_ "
    return play_data

def process_hint_index(play_data, index):
    if is_match(play_data, index): play_data = process_match(play_data, index)
    elif is_in(play_data, index): play_data = process_in(play_data, index)
    else: process_no_match(play_data, index)
    return play_data

def process_incorrect_guess(play_data):
    play_data[play_data[count_key]][hint_key] = ""
    for index in range(len(play_data[play_data[count_key]][guess_key])): play_data = process_hint_index(play_data, index)
    return play_data

def process_multiplayer_win(play_data):
    print(f"Congratulations Player {player_number(play_data)}, you guessed it!")
    print(f"It took you {turn_number(play_data)} guesses.")

def process_single_win(play_data):
    print("Congratulations! You guessed it!")
    print(f"It took you {turn_number(play_data)} guesses.")

def process_multiplayer_turn_display(play_data):
    print(f"Player {player_number(play_data)} turn {turn_number(play_data)}")

def process_single_turn_display(play_data):
    print(f"turn {turn_number(play_data)}")

def turn(play_data):
    if is_multi_player(play_data): clear_screen()
    print(f"Your hint is {play_data[play_data[count_key]][hint_key]}")
    play_data[count_key] += 1
    play_data[play_data[count_key]] = {}
    if is_multi_player(play_data): process_multiplayer_turn_display(play_data)
    else: process_single_turn_display(play_data)
    play_data[play_data[count_key]][guess_key] = input("Your guess is? ")
    if is_guess_size_incorrect(play_data): play_data = process_incorrect_guess_size(play_data)
    elif is_guess_incorrect(play_data): play_data = process_incorrect_guess(play_data)
    return play_data

def play(play_data, exit = False):
    clear_screen()
    play_data[secret_word_key] = play_data[random_key].choice(play_data[word_list_key])
    play_data[count_key] = -1
    play_data[play_data[count_key]] = {}
    play_data[play_data[count_key]][guess_key] = ""
    play_data[play_data[count_key]][hint_key] = "_ " * len(play_data[secret_word_key])
    play_data[number_of_players_key] = int(input("How many players? "))
    while play_data[play_data[count_key]][guess_key] != play_data[secret_word_key]: play_data = turn(play_data)
    if is_multi_player(play_data): process_multiplayer_win(play_data)
    else: process_single_win(play_data)
    again = input("Do you wish to play again [(Y)es/(N)o]? ")
    if again.lower() in ["n", "no", ""]: exit = True
    return exit

def main():
    file_name = "data.dat"
    if file_exists(file_name):
        file = open(file_name, "xt")
        file.close()
    file = open(file_name, "rt")
    file_data = file.read()
    file.close()
    print(file_data)
    raise Exception()
    play_data = {}
    play_data[random_key] = Random()
    play_data[random_key].seed()
    play_data[word_list_key] = ["apple", "cat", "dog", "pig", "cow", "sheep", "house"]
    exit = False
    while not exit: exit = play(play_data)

main()