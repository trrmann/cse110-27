import os
import ast
import datetime
from random import *
from pathlib import Path

random_key = "random"
word_list_key = "wordList"
secret_word_key = "secretWord"
count_key = "count"
guess_key = "guess"
hint_key = "hint"
number_of_players_key = "numberOfPlayers"

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

def request_valid_bool(question: str, msg_invalid: str = None, true_list: list = None, false_list: list = None,
        default: bool = None, max_retries: int = None, keyboard_interupt_handler_function = None):
    if msg_invalid == None: has_msg_invalid = False
    else: has_msg_invalid = True
    if true_list == None: has_true_list = False
    else: has_true_list = True
    if false_list == None: has_false_list = False
    else: has_false_list = True
    if default == None: has_default = False
    else: has_default = True
    if max_retries == None: has_max_retries = False
    else: has_max_retries = True
    valid_bool = None
    counter = 1
    while valid_bool == None:
        try:
            valid_bool = input(question)
            # fix this
            if (has_true_list and not (valid_bool in list(true_list)))\
                or (has_false_list and not (valid_bool in list(false_list))):
                if has_msg_invalid:  print(msg_invalid)
                valid_bool = None
            else:
                valid_bool = valid_bool in list(true_list)
        except ValueError as err:
            if has_true_list or has_false_list:
                if has_max_retries and counter >= int(max_retries):
                    if has_default: valid_bool = bool(default)
                    else:
                        if has_msg_invalid:  print(msg_invalid)
                        print("Retries exceeded and no default defined!")
                        raise err
                elif has_max_retries:
                    pass                    
                elif has_default:
                    valid_bool = bool(default)
            elif has_max_retries and counter >= int(max_retries):
                if has_default: valid_bool = bool(default)
                else:
                    if has_msg_invalid:  print(msg_invalid)
                    print("Retries exceeded and no default defined!")
                    raise err
            elif has_default:
                valid_bool = bool(default)
            else:
                if has_msg_invalid:  print(msg_invalid)
        except KeyboardInterrupt as err:
            if keyboard_interupt_handler_function != None:
                return keyboard_interupt_handler_function
            else:
                raise err
        finally:
            counter += 1
    return valid_bool

def request_valid_int(question: str, msg_invalid: str = None, min: int = None, max: int = None,
        default: int = None, max_retries: int = None, min_is_a_limit: bool = False, max_is_a_limit: bool = False,
        keyboard_interupt_handler_function = request_valid_bool("you pressed ctr-c.  quit(y/n)?", true_list = ["y", "yes", ""], false_list = ["n", "no"],
        default = True, max_retries = 3)):
    if msg_invalid == None: has_msg_invalid = False
    else: has_msg_invalid = True
    if min == None: has_min = False
    else: has_min = True
    if max == None: has_max = False
    else: has_max = True
    if default == None: has_default = False
    else: has_default = True
    if max_retries == None: has_max_retries = False
    else: has_max_retries = True
    valid_int = None
    counter = 1
    while valid_int == None:
        try:
            valid_int = int(input(question))
            if (has_min and (valid_int < int(min)) and not min_is_a_limit)\
                or (has_min and (valid_int <= int(min)) and min_is_a_limit)\
                or (has_max and (valid_int >= int(max)) and max_is_a_limit)\
                or (has_max and (valid_int > int(max)) and not max_is_a_limit):
                if has_msg_invalid:  print(msg_invalid)
                valid_int = None
        except ValueError as err:
            if has_min or has_max:
                if has_max_retries and counter >= int(max_retries):
                    if has_default: valid_int = int(default)
                    else:
                        if has_msg_invalid:  print(msg_invalid)
                        print("Retries exceeded and no default defined!")
                        raise err
                elif has_max_retries:
                    pass                    
                elif has_default:
                    valid_int = int(default)
            elif has_max_retries and counter >= int(max_retries):
                if has_default: valid_int = int(default)
                else:
                    if has_msg_invalid:  print(msg_invalid)
                    print("Retries exceeded and no default defined!")
                    raise err
            elif has_default:
                valid_int = int(default)
            else:
                if has_msg_invalid:  print(msg_invalid)
        except KeyboardInterrupt as err:
            if keyboard_interupt_handler_function != None:
                return keyboard_interupt_handler_function
            else:
                raise err
        finally:
            counter += 1
    return valid_int

def request_valid_float(question: str, msg_invalid: str = None, min: float = None, max: float = None,
        default: float = None, max_retries: int = None, min_is_a_limit: bool = False, max_is_a_limit: bool = False,
        keyboard_interupt_handler_function = None):
    if msg_invalid == None: has_msg_invalid = False
    else: has_msg_invalid = True
    if min == None: has_min = False
    else: has_min = True
    if max == None: has_max = False
    else: has_max = True
    if default == None: has_default = False
    else: has_default = True
    if max_retries == None: has_max_retries = False
    else: has_max_retries = True
    valid_float = None
    counter = 1
    while valid_float == None:
        try:
            valid_float = float(input(question))
            if (has_min and (valid_float < float(min)) and not min_is_a_limit)\
                or (has_min and (valid_float <= float(min)) and min_is_a_limit)\
                or (has_max and (valid_float >= float(max)) and max_is_a_limit)\
                or (has_max and (valid_float > float(max)) and not max_is_a_limit):
                if has_msg_invalid:  print(msg_invalid)
                valid_float = None
        except ValueError as err:
            if has_min or has_max:
                if has_max_retries and counter >= int(max_retries):
                    if has_default: valid_float = float(default)
                    else:
                        if has_msg_invalid:  print(msg_invalid)
                        print("Retries exceeded and no default defined!")
                        raise err
                elif has_max_retries:
                    pass                    
                elif has_default:
                    valid_float = float(default)
            elif has_max_retries and counter >= int(max_retries):
                if has_default: valid_float = float(default)
                else:
                    if has_msg_invalid:  print(msg_invalid)
                    print("Retries exceeded and no default defined!")
                    raise err
            elif has_default:
                valid_float = float(default)
            else:
                if has_msg_invalid:  print(msg_invalid)
        except KeyboardInterrupt as err:
            if keyboard_interupt_handler_function != None:
                return keyboard_interupt_handler_function
            else:
                raise err
        finally:
            counter += 1
    return valid_float

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
    play_data = {}
    play_data[random_key] = Random()
    play_data[random_key].seed()
    play_data[word_list_key] = ["apple", "cat", "dog", "pig", "cow", "sheep", "house"]
    exit = False
    while not exit: exit = play(play_data)

main()