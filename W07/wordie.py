import os

exit_key = "exit"
number_of_players_key = "number_of_players"
words_key = "words"
word_key = "word"
question_count_key = "question_count"
fail_count_key = "fail_count"
invalid_count_key = "invalid_count"
lost_key = "lost"
points_key = "points"
guesses_key = "guesses"

def invalid_number_of_players(number_of_players: int, min_number_of_players: int = 1, max_number_of_players: int = 2):
    return (int(number_of_players) < int(min_number_of_players)) or (int(number_of_players) > int(max_number_of_players))

def valid_number_of_players(number_of_players: int, min_number_of_players: int = 1, max_number_of_players: int = 2):
    return not invalid_number_of_players(int(number_of_players), int(min_number_of_players), int(max_number_of_players))

def request_number_of_players(invalid_count: int = 0, min_number_of_players: int = 1, max_number_of_players: int = 2, max_invalid_count: int = 3):
    number_of_players = int(min_number_of_players) - 1
    try:
        number_of_players = int(input("How many players?  "))
    except ValueError:
        number_of_players = int(min_number_of_players) - 1
    except KeyboardInterrupt:
        print("\nQuitting!")
        return int(min_number_of_players) - 2
    if invalid_number_of_players(int(number_of_players), int(min_number_of_players), int(max_number_of_players)):
        if (int(invalid_count) + 1) > int(max_invalid_count):
            number_of_players = int(min_number_of_players)
        else:
            print(f"Please enter a number from {int(min_number_of_players)} to {int(max_number_of_players)}.")
    return int(number_of_players)

def request_valid_number_of_players(min_number_of_players: int = 1, max_number_of_players: int = 2, max_invalid_count: int = 3):
    os.system("cls")
    invalid_count = 0
    number_of_players = int(min_number_of_players) - 1
    while invalid_number_of_players(number_of_players, int(min_number_of_players), int(max_number_of_players)):
        number_of_players = request_number_of_players(invalid_count, int(min_number_of_players), int(max_number_of_players), int(max_invalid_count))
        if(number_of_players == int(min_number_of_players) - 2): return int(number_of_players)
        invalid_count = int(invalid_count) + 1
    return int(number_of_players)

def initialize_data(number_of_players: int = 1):
    data = {}
    if(int(number_of_players) == int(min_number_of_players) - 2):
        data[exit_key] = True
    else:
        data[exit_key] = False
        data[number_of_players_key] = int(number_of_players)
        data[words_key] = ["abcde", "vwxyz", "lmnop"]
        data[word_key] = "abcde"
        data[question_count_key] = 0
        for player in range(data[number_of_players_key]):
            data[player + 1] = {}
            data[player + 1][lost_key] = False
            data[player + 1][fail_count_key] = 0
            data[player + 1][invalid_count_key] = 0
            data[player + 1][points_key] = 0
            data[player + 1][guesses_key] = []
    return data

def exit(data):
    return bool(data[exit_key])

def question_count(data):
    return int(data[question_count_key])

def number_of_players(data):
    return int(data[number_of_players_key])

def current_player_has_lost(data):
    return bool(data[player_number(data)][lost_key])

def guess_retry(data, guess):
    return bool(guess in data[player_number(data)][guesses_key])

def invalid_count(data):
    return int(data[player_number(data)][invalid_count_key])

def not_exit(data):
    return bool(not exit(data))

def player_number(data):
    return int(question_count(data) % number_of_players(data)) + 1

def turn_number(data):
    return int(question_count(data) / number_of_players(data)) + 1

def current_player_has_not_lost(data):
    return bool(not current_player_has_lost(data))

def has_players(data, single:bool = True):
    if single:
        return bool(number_of_players(data) >= 1)
    else:
        return bool(number_of_players(data) > 1)

def invalid_guess(data, guess):
    return bool(len(guess) < 1)

def valid_guess(data, guess):
    return bool(not invalid_guess(data, guess))

def is_single_player(data):
    return number_of_players(data) == 1

def is_multi_player(data):
    return not is_single_player(data)

def is_playing(data):
    return bool(has_players(data, is_single_player(data)) and current_player_has_not_lost(data))

def has_only_one_player_playing(data):
    return bool(number_of_players_playing(data) == 1)

def has_at_least_two_players_playing(data):
    return bool(number_of_players_playing(data) > 2)

def is_last_player_playing(data):
    return bool(has_only_one_player_playing(data) and current_player_has_not_lost(data))

def number_of_players_playing(data):
    number_of_players_playing = 0
    for lost_player in range(number_of_players(data)):
        if not data[lost_player + 1][lost_key]: number_of_players_playing = number_of_players_playing + 1
    return int(number_of_players_playing)

def request_quit():
    try:
        quit_option = input(f"You have pressed ctrl-c again, do you wish to quit [(Y)es/(N)o]!")
    except KeyboardInterrupt:
        print()
        quit_option = "YES"
    return str(quit_option)

def request_forfeit(data):
    try:
        quit_option = input(f"You have pressed ctrl-c, do you wish to forfeit [(Y)es/(N)o]!")
    except KeyboardInterrupt:
        print()
        if has_at_least_two_players_playing(data):
            quit_option = request_quit()
            if quit_option.upper() in ["Y", "YES", ""]:
                print("Quitting!")
                data[player_number(data)][lost_key] = True
                data[exit_key] = True
            else:
                quit_option = "YES"
        else:
            quit_option = "YES"
    return str(quit_option)

def request_guess(data):
    guess = ""
    try:
        guess = input("What is your guess?  ")
    except KeyboardInterrupt:
        print()
        quit_option = request_forfeit(data)
        if quit_option.upper() in ["Y", "YES", ""]:
            data[player_number(data)][lost_key] = True
    return str(guess)

def request_valid_guess(data):
    guess = ""
    while not_exit(data) and invalid_guess(data, guess) and is_playing(data):
        guess = request_guess(data)
        if not_exit(data) and invalid_guess(data, guess):
            if guess != "": print(f"{guess} is invalid, please try again!")
            else: print(f"is invalid, please try again!")
            data[player_number(data)][invalid_count_key] = invalid_count(data) + 1
        elif not_exit(data) and guess_retry(data, guess):
            print(f"You have already tried {guess} this game!")
            data[player_number(data)][invalid_count_key] = invalid_count(data) + 1
            guess = ""
        elif not_exit(data):
            data[player_number(data)][guesses_key].append(guess)
            """
            here
            """
        if not_exit(data) and invalid_guess(data, guess) and (int(invalid_count(data) % int(invalid_count_period)) == 0) and (invalid_count(data) > 0):
            try:
                if is_multi_player(data):
                    quit_option = input(f"You have passed {invalid_count(data)} invalid answers, do you wish to forfeit [(Y)es/(N)o]!")
                else:
                    quit_option = input(f"You have passed {invalid_count(data)} invalid answers, do you wish to quit [(Y)es/(N)o]!")
            except KeyboardInterrupt:
                quit_option = "YES"
            if quit_option.upper() in ["Y", "YES"]:
                data[player_number(data)][lost_key] = True
                if is_single_player(data): data[exit_key] = True
    return str(guess)

def has_hint(data, guess):
    has_hint = False
    for letter in guess:
        has_hint = has_hint or letter in data[word_key]
    return has_hint

def show_hint(data, guess):
    print("Show hint!")

def show_puzzle(data):
    print("Show puzzle!")

def award_points(data):
    print("award points!")

def next_word(data):
    print("next word")
    for player in range(data[number_of_players_key]):
        data[player + 1][fail_count_key] = 0
        data[player + 1][invalid_count_key] = 0
        data[player + 1][guesses_key] = []

def eval_win(data):
    print("check for winner!")

min_number_of_players = 1
max_number_of_players = 6
max_invalid_count = 3
invalid_count_period = 3
fail_count_period = 5
data = initialize_data(request_valid_number_of_players(min_number_of_players, max_number_of_players, max_invalid_count))
while not_exit(data):
    if is_multi_player(data): os.system("cls")
    if is_single_player(data):
        if is_playing(data): print(f"turn # {turn_number(data)}.")
    elif (data[number_of_players_key] == number_of_players_playing(data)) and is_multi_player(data):
        if is_playing(data): print(f"Player {player_number(data)} of {data[number_of_players_key]} turn # {turn_number(data)}.")
    elif number_of_players_playing(data) == 1:
        if is_playing(data): print(f"Player {player_number(data)} turn # {turn_number(data)}.")
    else:
        if is_playing(data): print(f"Player {player_number(data)} of {data[number_of_players_key]} ({number_of_players_playing(data)} remaining) turn # {turn_number(data)}.")
    if is_last_player_playing(data) and (data[number_of_players_key] > 1):
        print("You win!")
        data[exit_key] = True;
    else:
        show_puzzle(data)
        guess = request_valid_guess(data)

    if (data[word_key] == guess) and not_exit(data):
        print("You got the word!")
        award_points(data)
        data[player_number(data)][fail_count_key] = 0
        data[player_number(data)][invalid_count_key] = 0
        next_word(data)
    elif has_hint(data, guess) and not_exit(data):
        print("You got part of the word!")
        show_hint(data, guess)
        award_points(data)
        data[player_number(data)][fail_count_key] = 0
        data[player_number(data)][invalid_count_key] = 0
    elif not_exit(data):
        print("Better luck next time!")
        data[player_number(data)][fail_count_key] = data[player_number(data)][fail_count_key] + 1
   
    if not_exit(data) and (int(data[player_number(data)][fail_count_key] % int(fail_count_period)) == 0) and (data[player_number(data)][fail_count_key] > 0):
        try:
            if is_multi_player(data):
                quit_option = input(f"You have passed {data[player_number(data)][fail_count_key]} failing answers in a row, do you wish to forfeit [(Y)es/(N)o]!")
            else:
                quit_option = input(f"You have passed {data[player_number(data)][fail_count_key]} failing answers in a row, do you wish to quit [(Y)es/(N)o]!")
        except KeyboardInterrupt:
            quit_option = "YES"
        if quit_option.upper() in ["Y", "YES"]:
            data[player_number(data)][lost_key] = True
            if is_single_player(data): data[exit_key] = True

    if not_exit(data):  eval_win(data)
    if not_exit(data) and (not data[player_number(data)][lost_key]) and is_multi_player(data): input("Press enter to go on.")
    data[question_count_key] = int(int(data[question_count_key]) + 1)
    