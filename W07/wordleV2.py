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

def date_to_dict(date_time: datetime = datetime.datetime.now()):
    return {"type":"datetime",
    "year" : date_time.year,
    "month" : date_time.month,
    "day" : date_time.day,
    "hour" : date_time.hour,
    "minute" : date_time.minute,
    "second" : date_time.second,
    "microsecond" : date_time.microsecond}

def delta_to_dict(delta: datetime.timedelta = datetime.timedelta(0,0,0)):
    return {"type":"delta",
    "days" : delta.days,
    "seconds" : delta.seconds,
    "microseconds" : delta.microseconds}

def dict_to_date(dictionary: dict = date_to_dict()):
    match dictionary["type"]:
        case "datetime":
            return datetime.datetime(dictionary["year"], dictionary["month"], dictionary["day"], dictionary["hour"], dictionary["minute"], dictionary["second"], dictionary["microsecond"])
        case "delta":
            return dict_to_delta(dictionary)
        case _:
            return None

def dict_to_delta(dictionary: dict = delta_to_dict()):
    match dictionary["type"]:
        case "delta":
            return datetime.timedelta(dictionary["days"], dictionary["seconds"], dictionary["microseconds"])
        case "datetime":
            return dict_to_date(dictionary)
        case _:
            return None

def date_diff_dict(first_date: datetime = datetime.datetime.now(), second_date: datetime = datetime.datetime.now()):
    return delta_to_dict(second_date - first_date)

def date_dict_to_delta_dict(dictionary: dict = date_to_dict()):
    now = datetime.datetime.now()
    if dictionary["year"] < datetime.MINYEAR:
        year_mod = int(datetime.MINYEAR - dictionary["year"])
    elif dictionary["year"] > datetime.MAXYEAR:
        year_mod = int(dictionary["year"] - datetime.MAXYEAR)
    else:
        year_mod = 0
    if dictionary["month"] < 1:
        month_mod = int(1 - dictionary["month"])
    elif dictionary["month"] > 12:
        month_mod = int(dictionary["month"] - 12)
    else:
        month_mod = 0
    if dictionary["day"] < 1:
        day_mod = int(1 - dictionary["day"])
    elif dictionary["day"] > 31:
        day_mod = int(dictionary["day"] - 31)
    else:
        day_mod = 0
    dictionary["year"] += year_mod
    dictionary["month"] += month_mod
    dictionary["day"] += day_mod
    dictionary = date_to_dict(dict_to_date(dictionary))
    dictionary["year"] -= year_mod
    dictionary["month"] -= month_mod
    dictionary["day"] -= day_mod
    minute_to_seconds_factor = 60
    hour_to_seconds_factor = minute_to_seconds_factor * 60
    month_to_days_factor = ((datetime.datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond) - datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/(12*16))
    year_to_days_factor = ((datetime.datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond) - datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/16)
    return delta_to_dict(datetime.timedelta(int(dictionary["day"] + dictionary["month"] * month_to_days_factor + dictionary["year"] * year_to_days_factor), int(dictionary["second"] + dictionary["minute"] * minute_to_seconds_factor + dictionary["hour"] * hour_to_seconds_factor), dictionary["microsecond"]))

def delta_dict_to_date_dict(dictionary: dict = delta_to_dict()):
    now = datetime.datetime.now()
    dictionary = delta_to_dict(dict_to_delta(dictionary))
    minute_to_seconds_factor = 60
    hour_to_seconds_factor = minute_to_seconds_factor * 60
    month_to_days_factor = ((datetime.datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)\
        - datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/(12*16))
    year_to_days_factor = ((datetime.datetime(now.year + 16, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)\
        - datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)).days/16)
    microseconds = dictionary["microseconds"]
    seconds = dictionary["seconds"]
    days = dictionary["days"]
    microsecond = microseconds
    hour = divmod(seconds, hour_to_seconds_factor)[0]
    seconds = seconds - (hour * hour_to_seconds_factor)
    minute = divmod(seconds, minute_to_seconds_factor)[0]
    second = seconds - (minute * minute_to_seconds_factor)
    year = divmod(days, year_to_days_factor)[0]
    days = days - (year * year_to_days_factor)
    month = divmod(days, month_to_days_factor)[0]
    day = days - (month * month_to_days_factor)
    if year < datetime.MINYEAR:
        year_mod = int(datetime.MINYEAR - year)
    elif year > datetime.MAXYEAR:
        year_mod = int(year - datetime.MAXYEAR)
    else:
        year_mod = 0
    if month < 1:
        month_mod = int(1 - month)
    elif month > 12:
        month_mod = int(month - 12)
    else:
        month_mod = 0
    if day < 1:
        day_mod = int(1 - day)
    elif day > 31:
        day_mod = int(day - 31)
    else:
        day_mod = 0
    date_dict = date_to_dict(datetime.datetime(int(year) + year_mod, int(month) + month_mod, int(day) + day_mod, int(hour), int(minute), int(second), int(microsecond)))
    date_dict["year"] = date_dict["year"] - year_mod
    date_dict["month"] = date_dict["month"] - month_mod
    date_dict["day"] = date_dict["day"] - day_mod
    return date_dict

def main():
    file_name = "data.dat"
    if not file_exists(file_name):
        print("no file... create")
        file = open(file_name, "xt")
        file.close()
    file = open(file_name, "rt")
    file_data = ast.literal_eval(file.read())
    file.close()
    print(file_data)
    if file_data == "":  file_data = {}
    if "x" in file_data.keys(): print(f"x = {file_data['x']}")
    if "y" in file_data.keys(): print(f"y = {file_data['y']}")
    file_data["x"] = 1
    file_data["y"] = 2
    file = open(file_name, "wt")
    file.write(str(file_data))
    file.close()

    created = datetime.datetime.fromtimestamp(os.path.getctime(file_name))
    modified = datetime.datetime.fromtimestamp(os.path.getmtime(file_name))
    accessed = datetime.datetime.fromtimestamp(os.path.getatime(file_name))

    create_age = delta_dict_to_date_dict(date_diff_dict(created))
    modified_age = delta_dict_to_date_dict(date_diff_dict(modified))
    accessed_age = delta_dict_to_date_dict(date_diff_dict(accessed))

    print(f"created:  {created}")
    print(f"last modified:  {modified}")
    print(f"last accessed:  {accessed}")
    print(f"now {datetime.datetime.now()}")

    print(f"create age:  {create_age['year']} years {create_age['month']} months {create_age['day']} days {create_age['hour']} hours {create_age['minute']} minutes {create_age['second']} seconds")
    print(f"modified age:  {modified_age['year']} years {modified_age['month']} months {modified_age['day']} days {modified_age['hour']} hours {modified_age['minute']} minutes {modified_age['second']} seconds")
    print(f"last accessed age:  {accessed_age['year']} years {accessed_age['month']} months {accessed_age['day']} days {accessed_age['hour']} hours {accessed_age['minute']} minutes {accessed_age['second']} seconds")

    raise Exception()
    play_data = {}
    play_data[random_key] = Random()
    play_data[random_key].seed()
    play_data[word_list_key] = ["apple", "cat", "dog", "pig", "cow", "sheep", "house"]
    exit = False
    while not exit: exit = play(play_data)

main()