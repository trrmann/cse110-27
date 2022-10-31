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
player_number_key = "playerNumber"
turn_number_key = "turnNumber"
max_turns_key = "maxTurns"

def request_guess(play_data :dict):
    play_data = dict(play_data)
    if get_remaining_turns(play_data) == 1: tries = f"{get_remaining_turns(play_data)} tries remaining"
    else: tries = "last chance"
    try:
        return str(input(f"Your guess is ({tries})? ").lower())
    except KeyboardInterrupt:
        print()
        return str(get_hint(play_data))

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

def is_guess_size_incorrect(play_data :dict):
    play_data = dict(play_data)
    return bool(len(get_guess(play_data)) != len(get_secret_word(play_data)))

def is_guess_incorrect(play_data :dict):
    play_data = dict(play_data)
    return bool(get_guess(play_data).lower() != get_secret_word(play_data).lower())

def is_match(index :int, play_data :dict):
    play_data = dict(play_data)
    if int(index) >= 0 and int(index) < len(get_guess(play_data)) and int(index) < len(get_secret_word(play_data)): return bool(get_guess(play_data)[int(index)] == get_secret_word(play_data)[int(index)])
    return False

def is_in(index :int, play_data :dict):
    play_data = dict(play_data)
    if int(index) >= 0 and int(index) < len(get_guess(play_data)): return bool(get_guess(play_data)[int(index)] in get_secret_word(play_data))
    return False

def is_in_with_quantity_match(index :int, play_data :dict):
    play_data = dict(play_data)
    return bool(is_in(int(index), play_data))

def is_single_player(play_data :dict):
    play_data = dict(play_data)
    return bool(get_number_of_players(play_data) == 1)

def is_multi_player(play_data :dict):
    play_data = dict(play_data)
    return bool(get_number_of_players(play_data) > 1)

def is_last_player_in_turn(play_data :dict):
    play_data = dict(play_data)
    return bool(get_number_of_players(play_data) == get_player_number(play_data))

def is_last_turn(play_data :dict):
    play_data = dict(play_data)
    return bool(get_remaining_turns(play_data) == 1)

def is_last_game_turn(play_data :dict):
    play_data = dict(play_data)
    return bool(is_last_turn(play_data) and is_last_player_in_turn(play_data))

def is_exit(play_data :dict):
    play_data = dict(play_data)
    return bool(play_data[exit_key])

def has_player_lost(play_data :dict):
    play_data = dict(play_data)
    return bool(get_player(play_data)[lost_key])

def set_player_lost(player_lost :bool, play_data :dict):
    play_data = dict(play_data)
    get_player(play_data)[lost_key] = bool(player_lost)
    return play_data

def set_exit(exit :bool = False, play_data :dict = None):
    if play_data == None:  play_data = set_word_list(["test"])
    play_data = dict(play_data)
    play_data[exit_key] = bool(exit)
    return play_data

def get_random(play_data :dict):
    play_data = dict(play_data)
    return play_data[random_key]

def set_random(play_data :dict = {}):
    play_data = dict(play_data)
    play_data[random_key] = Random()
    get_random(play_data).seed()
    return play_data

def get_word_list(play_data :dict):
    play_data = dict(play_data)
    return list(play_data[word_list_key])

def set_word_list(word_list :list, play_data :dict = None):
    if play_data == None:  play_data = set_random()
    play_data = dict(play_data)
    play_data[word_list_key] = list(word_list)
    return play_data

def get_player_number(play_data :dict):
    play_data = dict(play_data)
    return int(play_data[player_number_key])

def set_player_number(player_number :int, play_data :dict):
    play_data = dict(play_data)
    play_data[player_number_key] = int(player_number)
    return play_data

def get_player(play_data :dict):
    play_data = dict(play_data)
    return play_data[players_key][get_player_number(play_data)]

def add_player(play_data :dict):
    play_data = dict(play_data)
    play_data[players_key][get_player_number(play_data)] = {}
    return play_data

def get_number_of_players(play_data :dict):
    play_data = dict(play_data)
    return int(play_data[number_of_players_key])

def set_number_of_players(number_of_players :int, play_data :dict):
    play_data = dict(play_data)
    play_data[number_of_players_key] = int(number_of_players)
    play_data[players_key] = {}
    if get_number_of_players(play_data) > 0:
        for index in range(1, get_number_of_players(play_data) + 1):
            play_data = set_player_number(index, play_data)
            play_data = add_player(play_data)
    return play_data

def get_turn_number(play_data :dict):
    play_data = dict(play_data)
    return int(play_data[turn_number_key])

def set_turn_number(turn_number :int, play_data :dict):
    play_data = dict(play_data)
    play_data[turn_number_key] = int(turn_number)
    return play_data

def get_guess(play_data :dict):
    play_data = dict(play_data)
    return str(get_player(play_data)[guess_key])

def set_guess(guess :str, play_data :dict):
    play_data = dict(play_data)
    get_player(play_data)[guess_key] = str(guess)
    return play_data

def get_secret_word(play_data :dict):
    play_data = dict(play_data)
    return str(get_player(play_data)[secret_word_key])

def set_secret_word(secret_word :str, play_data :dict):
    play_data = dict(play_data)
    get_player(play_data)[secret_word_key] = str(secret_word)
    return play_data

def get_last_hint(play_data :dict):
    play_data = dict(play_data)
    return str(get_player(play_data)[last_hint_key])

def set_last_hint(last_hint :str, play_data :dict):
    play_data = dict(play_data)
    get_player(play_data)[last_hint_key] = str(last_hint)
    return play_data

def get_hint(play_data :dict):
    play_data = dict(play_data)
    return str(get_player(play_data)[hint_key])

def set_hint(hint :str, play_data :dict):
    play_data = dict(play_data)
    get_player(play_data)[hint_key] = str(hint)
    return play_data

def get_max_turns(play_data :dict):
    play_data = dict(play_data)
    return int(play_data[max_turns_key])

def set_max_turns(max_turns :int, play_data :dict):
    play_data = dict(play_data)
    play_data[max_turns_key] = int(max_turns)
    return play_data

def get_remaining_turns(play_data :dict):
    play_data = dict(play_data)
    return get_max_turns(play_data) - get_turn_number(play_data)

def build_last_hint(hint :str, play_data :dict):
    play_data = dict(play_data)
    last_hint = get_last_hint(play_data)
    print("merge hint to last hint")
    last_hint = f"{last_hint} {hint}"
    return str(last_hint)

def process_incorrect_guess_size(play_data :dict):
    play_data = dict(play_data)
    print("Sorry, the guess must have the same number of letters as the secret word.\n")
    set_hint("_ " * len(get_secret_word(play_data)), play_data)
    set_last_hint(build_last_hint(get_hint(play_data), play_data), play_data)
    if is_multi_player(play_data): wait_for_enter(exit)
    return play_data

def process_match(index :int, play_data :dict):
    play_data = dict(play_data)
    set_hint(f"{get_hint(play_data)}{get_guess(play_data)[int(index)].upper()} ", play_data)
    return play_data

def process_in(index :int, play_data :dict):
    play_data = dict(play_data)
    set_hint(f"{get_hint(play_data)}{get_guess(play_data)[int(index)].lower()} ", play_data)
    return play_data

def process_no_match(play_data :dict):
    play_data = dict(play_data)
    set_hint(f"{get_hint(play_data)}_ ", play_data)
    return play_data

def process_hint_index(index :int, play_data :dict):
    play_data = dict(play_data)
    if is_match(int(index), play_data): play_data = process_match(int(index), play_data)
    elif is_in(int(index), play_data, ): play_data = process_in(int(index), play_data)
    else: process_no_match(play_data)
    return play_data

def process_incorrect_guess(play_data :dict):
    play_data = dict(play_data)
    play_data = set_hint("", play_data)
    for index in range(len(get_guess(play_data))): play_data = process_hint_index(index, play_data)
    play_data = set_last_hint(build_last_hint(get_hint(play_data), play_data), play_data)
    return play_data

def process_multiplayer_win(play_data :dict):
    play_data = dict(play_data)
    print(f"Congratulations Player {get_player_number(play_data)}, you guessed it!")
    if get_turn_number(play_data) > 1: print(f"It took you {get_turn_number(play_data)} guesses.")
    else: print(f"It took you {get_turn_number(play_data)} guess.")

def process_single_win(play_data :dict):
    play_data = dict(play_data)
    print("Congratulations! You guessed it!")
    if get_turn_number(play_data) > 1: print(f"It took you {get_turn_number(play_data)} guesses.")
    else: print(f"It took you {get_turn_number(play_data)} guess.")

def process_multiplayer_turn_display(play_data :dict):
    play_data = dict(play_data)
    print(f"Player {get_turn_number(play_data)} turn {get_turn_number(play_data)}")

def process_single_turn_display(play_data :dict):
    play_data = dict(play_data)
    print(f"turn {get_turn_number(play_data)}")

def next_player(play_data :dict):
    play_data = dict(play_data)
    set_player_number(get_player_number(play_data) + 1, play_data)
    return play_data

def next_turn(play_data :dict):
    play_data = dict(play_data)
    set_turn_number(get_turn_number(play_data) + 1, play_data)
    return play_data

def turn(play_data :dict):
    play_data = dict(play_data)
    if is_multi_player(play_data): clear_screen()
    if is_multi_player(play_data): process_multiplayer_turn_display(play_data)
    else: process_single_turn_display(play_data)
    if is_multi_player(play_data): play_data[exit_key] = wait_for_enter(play_data[exit_key])
    print(f"Your hint is {get_hint(play_data)}")
    if is_last_turn(play_data): print(f"Your last hint is {get_last_hint(play_data)}")
    play_data = set_guess(request_guess(play_data), play_data)
    if get_guess(play_data) == get_hint(play_data): play_data = set_exit(True, play_data)
    elif is_guess_size_incorrect(play_data): play_data = play_data = process_incorrect_guess_size(play_data)
    elif is_guess_incorrect(play_data): play_data = play_data = process_incorrect_guess(play_data)
    if is_last_turn(play_data): play_data = set_player_lost(True, play_data)
    return play_data

def play(play_data :dict, exit :bool = False):
    play_data = dict(play_data)
    play_data = set_exit(bool(exit), play_data)
    play_data = set_turn_number(1, play_data)
    play_data = set_max_turns(5, play_data)
    secret_word = get_random(play_data).choice(get_word_list(play_data))
    clear_screen()
    play_data = set_number_of_players(request_number_of_players(),play_data)
    if get_number_of_players(play_data) == 0: play_data = set_exit(True, play_data)
    else:
        for index in range(1, get_number_of_players(play_data) + 1):
            play_data = set_player_number(index, play_data)
            play_data = set_secret_word(secret_word, play_data)
            play_data = set_guess("", play_data)
            play_data = set_hint("_ " * len(get_secret_word(play_data)), play_data)
            play_data = set_last_hint(get_hint(play_data), play_data)
            play_data = set_player_lost(False, play_data)
        play_data = set_player_number(1, play_data)
        while not is_exit(play_data) and is_guess_incorrect(play_data):
            if not has_player_lost(play_data):
                play_data = turn(play_data)
                if is_last_game_turn(play_data):
                    play_data = set_exit(True, play_data)
            play_data = next_player(play_data)
            if is_last_player_in_turn(play_data): play_data = next_turn(play_data)    
        if not is_exit(play_data) and not has_player_lost(play_data) and is_multi_player(play_data): process_multiplayer_win(play_data)
        elif not is_exit(play_data) and not has_player_lost(play_data) : process_single_win(play_data)
        elif has_player_lost(play_data) : print("Better luck next time!")
    return play_again(play_data[exit_key])

def main():
#    play_data = set_exit(False, set_word_list(["apple", "cat", "dog", "pig", "cow", "sheep", "house"], set_random({})))
    play_data = set_exit(play_data=set_word_list(["dog"]))
    while not is_exit(play_data): set_exit(play(play_data), play_data)
    print("Have a great day!")

main()