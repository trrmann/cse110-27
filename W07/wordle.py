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
players_key = "players"
max_guesses_key = "max_guesses"

def request_guess(player_number :int, play_data :dict):
    if remaining_tries(int(player_number), dict(play_data)) == 1: tries = f"{remaining_tries(int(player_number), dict(play_data))} tries remaining"
    else: tries = "last chance"
    try:
        return str(input(f"Your guess is ({tries})? ").lower())
    except KeyboardInterrupt:
        print()
        return str(get_hint(int(player_number), dict(play_data)))

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
            return int(0)
        if players < 1:
            print("Please provide a number of players greater than 1!")
        tries += 1
    if (players < 1):
        players = 1
    return int(players)

def wait_for_enter(exit :bool = False):
    try: input(f"Press Enter to continue.")
    except KeyboardInterrupt: exit = True
    return bool(exit)

def play_again(exit :bool = False):
    if not bool(exit):
        try:
            again = str(input("Do you wish to play again [(Y)es/(N)o]? "))
        except KeyboardInterrupt:
            print()
            again = "no"
        if again.lower() in ["n", "no"]:
            exit = True
        elif again.lower() in ["y", "yes", ""]:
            exit = False
        else:
            exit = False
    return bool(exit)

def clear_screen():
    print("\n" * 6)
    os.system("cls")

def is_guess_size_incorrect(player_number :int, play_data :dict):
    return bool(len(get_guess(int(player_number), dict(play_data))) != len(get_secret_word(int(player_number), dict(play_data))))

def is_guess_incorrect(player_number :int, play_data :dict):
    return bool(get_guess(int(player_number), dict(play_data)).lower() != get_secret_word(int(player_number), dict(play_data)).lower())

def is_match(player_number :int, index :int, play_data :dict):
    if int(index) >= 0 and int(index) < len(get_guess(int(player_number), dict(play_data))) and int(index) < len(get_secret_word(int(player_number), dict(play_data))): return bool(get_guess(int(player_number), dict(play_data))[int(index)] == get_secret_word(int(player_number), dict(play_data))[int(index)])
    return False

def is_in(player_number :int, index :int, play_data :dict):
    if int(index) >= 0 and int(index) < len(get_guess(int(player_number), dict(play_data))): return bool(get_guess(int(player_number), dict(play_data))[int(index)] in get_secret_word(int(player_number), dict(play_data)))
    return False

def is_single_player(play_data :dict):
    return bool(get_number_of_players(dict(play_data)) == 1)

def is_multi_player(play_data :dict):
    return bool(get_number_of_players(dict(play_data)) > 1)

def get_number_of_players(play_data :dict):
    return int(dict(play_data)[number_of_players_key])

def set_number_of_players(number_of_players :int, play_data :dict):
    dict(play_data)[number_of_players_key] = int(number_of_players)

def get_player(player_number :int, play_data :dict):
    return dict(play_data)[players_key][int(player_number)]

def add_player(player_number :int, play_data :dict):
    dict(play_data)[players_key][int(player_number)] = {}

def get_guess(player_number :int, play_data :dict):
    return str(get_player(int(player_number), dict(play_data))[guess_key])

def set_guess(player_number :int, guess :str, play_data :dict):
    get_player(int(player_number), dict(play_data))[guess_key] = str(guess)

def get_secret_word(player_number :int, play_data :dict):
    return str(get_player(int(player_number), dict(play_data))[secret_word_key])

def set_secret_word(player_number :int, secret_word :str, play_data :dict):
    get_player(int(player_number), dict(play_data))[secret_word_key] = str(secret_word)

def get_last_hint(player_number :int, play_data :dict):
    return str(get_player(int(player_number), dict(play_data))[last_hint_key])

def set_last_hint(player_number :int, last_hint :str, play_data :dict):
    get_player(int(player_number), dict(play_data))[last_hint_key] = str(last_hint)

def build_last_hint(player_number :int, hint :str, play_data :dict):
    last_hint = get_last_hint(int(player_number), dict(play_data))
    print("merge hint to last hint")
    last_hint = f"{last_hint} {hint}"
    return str(last_hint)

def get_hint(player_number :int, play_data :dict):
    return str(get_player(int(player_number), dict(play_data))[hint_key])

def set_hint(player_number :int, hint :str, play_data :dict):
    get_player(int(player_number), dict(play_data))[hint_key] = str(hint)

def process_incorrect_guess_size(player_number :int, play_data :dict):
    print("Sorry, the guess must have the same number of letters as the secret word.\n")
    set_hint(int(player_number), "_ " * len(get_secret_word(int(player_number), dict(play_data))), dict(play_data))
    set_last_hint(build_last_hint(int(player_number), get_hint(int(player_number), dict(play_data)), dict(play_data)))
    if is_multi_player(play_data): wait_for_enter(exit)
    return play_data

if

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