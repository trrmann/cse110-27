import os
from random import *

exit_key = "exit"
lost_key = "lost"
random_key = "random"
word_list_key = "wordList"
secret_word_key = "secretWord"
count_key = "count"
guess_key = "guess"
hint_key = "hint"
last_hint_key = "lastHint"
number_of_players_key = "numberOfPlayers"
max_guesses_key = "max_guesses"

def request_guess(play_data, hint):
    try:
        if remaining_tries(play_data) == 0: return input(f"Your guess is (last chance)? ").lower()
        else: return input(f"Your guess is ({remaining_tries(play_data) + 1} tries remaining)? ").lower()
    except KeyboardInterrupt:
        print()
        return hint

def request_number_of_players():
    players = -1
    max_tries = 3
    tries = 0
    while (players < 1) and (tries < max_tries):
        try:
            players = int(input("How many players? "))
        except ValueError:
            players = 0
        except KeyboardInterrupt:
            print()
            return 0
        if players < 1:
            print("Please provide a number of players greater than 1!")
        tries += 1
    if (players < 1):
        players = 1
    return players

def wait_for_enter(exit):
    try: input(f"Press Enter to continue.")
    except KeyboardInterrupt: exit = True
    return exit

def play_again(exit: bool = False):
    if not exit:
        try:
            again = input("Do you wish to play again [(Y)es/(N)o]? ")
        except KeyboardInterrupt:
            print()
            again = "no"
        if again.lower() in ["n", "no"]:
            exit = True
        elif again.lower() in ["y", "yes", ""]:
            exit = False
        else:
            exit = False
    return exit

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

def main_hint_index(player_no, turn_no, play_data):
    if turn_no == 0: return -1
    else: return ((((turn_no-1) * play_data[number_of_players_key])+player_no)) - 1

def last_hint(play_data):
    for index in range(turn_number(play_data) + 1):
        print(f"main index {main_hint_index(player_number(play_data), index, play_data)} \
player {player_number(play_data)} turn {index} \
guess {play_data[main_hint_index(player_number(play_data), index, play_data)][guess_key]} \
hint to guess {play_data[main_hint_index(player_number(play_data), index, play_data)][hint_key]} \
current turn {turn_number(play_data)} \
number of players {play_data[number_of_players_key]} \
number of main indexes {play_data[count_key]}")
    play_data[play_data[count_key]][last_hint_key] = "last hint"
    input("")
    return play_data

def process_incorrect_guess_size(play_data):
    print("Sorry, the guess must have the same number of letters as the secret word.\n")
    play_data[play_data[count_key]][hint_key] = ""
    play_data[play_data[count_key]][hint_key] = "_ " * len(play_data[secret_word_key])
    if remaining_tries(play_data)==1:  play_data = last_hint(play_data)
    if is_multi_player(play_data): wait_for_enter(exit)
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
    if remaining_tries(play_data)==1: play_data = last_hint(play_data)
    return play_data

def process_multiplayer_win(play_data):
    print(f"Congratulations Player {player_number(play_data)}, you guessed it!")
    if turn_number(play_data) > 1: print(f"It took you {turn_number(play_data)} guesses.")
    else: print(f"It took you {turn_number(play_data)} guess.")

def process_single_win(play_data):
    print("Congratulations! You guessed it!")
    if turn_number(play_data) > 1: print(f"It took you {turn_number(play_data)} guesses.")
    else: print(f"It took you {turn_number(play_data)} guess.")

def process_multiplayer_turn_display(play_data):
    print(f"Player {player_number(play_data)} turn {turn_number(play_data)}")

def process_single_turn_display(play_data):
    print(f"turn {turn_number(play_data)}")

def current_player_last_guess_index(play_data):
    if is_multi_player(play_data): return main_hint_index(player_number(play_data),turn_number(play_data)-1,play_data)
    else: return main_hint_index(player_number(play_data),turn_number(play_data),play_data)
    #if play_data[count_key] < (play_data[number_of_players_key] - 1): return -1
    #else: return play_data[count_key] - (play_data[number_of_players_key] - 1)

def last_player_in_turn(play_data):
    return play_data[number_of_players_key] == player_number(play_data)

def remaining_tries(play_data):
    return play_data[max_guesses_key] - turn_number(play_data)

def last_chance(play_data):
    return last_player_in_turn(play_data) and (remaining_tries(play_data) == 0)

def turn(play_data):
    previous_turn_index = current_player_last_guess_index(play_data)
    if is_multi_player(play_data): clear_screen()
    hint = play_data[previous_turn_index][hint_key]
    print(f"{remaining_tries(play_data)} {previous_turn_index} {play_data[count_key]}")
    if remaining_tries(play_data) == 1 and last_hint_key in play_data[previous_turn_index].keys():
        last_hint = play_data[previous_turn_index][last_hint_key]
    else: last_hint = None
    play_data[count_key] += 1
    play_data[play_data[count_key]] = {}
    if is_multi_player(play_data): process_multiplayer_turn_display(play_data)
    else: process_single_turn_display(play_data)
    if is_multi_player(play_data) and (play_data[count_key] >= 0): play_data[exit_key] = wait_for_enter(play_data[exit_key])
    print(f"Your hint is {hint}")
    if last_hint != None: print(f"Your last hint is {last_hint}")
    play_data[play_data[count_key]][guess_key] = request_guess(play_data, hint)
    if play_data[play_data[count_key]][guess_key] == hint:  play_data[exit_key] = True
    elif is_guess_size_incorrect(play_data): play_data = process_incorrect_guess_size(play_data)
    elif is_guess_incorrect(play_data): play_data = process_incorrect_guess(play_data)
    if last_chance(play_data):  play_data[lost_key] = True
    return play_data

def play(play_data, exit = False):
    play_data[exit_key] = exit
    clear_screen()
    play_data[secret_word_key] = play_data[random_key].choice(play_data[word_list_key])
    play_data[count_key] = -1
    play_data[play_data[count_key]] = {}
    play_data[number_of_players_key] = request_number_of_players()
    if play_data[number_of_players_key] == 0: play_data[exit_key] = True
    play_data[play_data[count_key]][guess_key] = ""
    #play_data[current_player_last_guess_index(play_data)][hint_key] = ""
    play_data[play_data[count_key]][hint_key] = "_ " * len(play_data[secret_word_key])
    play_data[max_guesses_key] = 5
    play_data[lost_key] = False
    while not play_data[exit_key] and not play_data[lost_key] and (play_data[play_data[count_key]][guess_key] != play_data[secret_word_key]): play_data = turn(play_data)
    if not play_data[exit_key] and not play_data[lost_key] and is_multi_player(play_data): process_multiplayer_win(play_data)
    elif not play_data[exit_key] and not play_data[lost_key] : process_single_win(play_data)
    elif play_data[lost_key] : print("Better luck next time!")
    return play_again(play_data[exit_key])

def main():
    play_data = {}
    play_data[random_key] = Random()
    play_data[random_key].seed()
    play_data[word_list_key] = ["apple", "cat", "dog", "pig", "cow", "sheep", "house"]
    exit = False
    while not exit: exit = play(play_data)
    print("Have a great day!")

main()