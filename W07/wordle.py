import random
import os

empty = ""
underscore = "_"
default_list = ["dog", "cat", "pig", "cow", "ape", "sow", "sheep", "sleep", "house", "horse", "apple"]
random_key = "random"
exit_key = "exit"
word_list_key = "wordList"
secret_word_key = "secretWord"
number_of_players_key = "numberOfPlayers"
player_number_key = "playerNumber"
max_turns_key = "maxTurns"
super_hint_frequency_key = "superHintFrequency"
players_key = "players"
multiplayer_init_key = "multiplayerInit"
hint_key = "hint"
last_hint_key = "lastHint"
puzzle_key = "puzzle"
letters_key = "letters"
guess_key = "guess"
turn_number_key = "turn"
track_key = "track"

def set_random(random_data :dict = {}, random = random.Random()):
    random_data = dict(random_data)
    random_data[random_key] = random
    random_data[random_key].seed()
    return random_data

def get_random(random_data :dict = {}):
    random_data = dict(random_data)
    if random_key in random_data.keys(): return random_data[random_key]
    else: return random.Random()

def set_exit(exit_data :dict = {}, exit :bool = False):
    exit_data = dict(exit_data)
    exit_data[exit_key] = bool(exit)
    return exit_data

def get_exit(exit_data :dict = {}, exit :bool = False):
    exit_data = dict(exit_data)
    if exit_key in exit_data.keys(): return bool(exit_data[exit_key])
    else: return bool(exit)

def clear_screen():
    print("\n" * 5)
    os.system("cls")

def set_player_number(player_number_data :dict = {}, player_number :int = 1):
    player_number_data = dict(player_number_data)
    player_number_data[player_number_key] = int(player_number)
    return player_number_data

def get_player_number(player_number_data :dict = {}, player_number :int = 1):
    player_number_data = dict(player_number_data)
    if player_number_key in player_number_data.keys(): return int(player_number_data[player_number_key])
    else: return int(player_number)

def set_turn_number(turn_number_data :dict = {}, turn_number :int = 0):
    turn_number_data = dict(turn_number_data)
    turn_number_data[turn_number_key] = int(turn_number)
    return turn_number_data

def get_turn_number(turn_number_data :dict = {}, turn_number :int = 0):
    turn_number_data = dict(turn_number_data)
    if turn_number_key in turn_number_data.keys(): return int(turn_number_data[turn_number_key])
    else: return int(turn_number)

def set_secret_word(secret_word_data :dict = {}, secret_word :str = None):
    secret_word_data = dict(secret_word_data)
    if secret_word == None: secret_word = get_random(secret_word_data).choice(get_word_list(secret_word_data))
    secret_word_data[secret_word_key] = str(secret_word)
    return secret_word_data

def get_secret_word(secret_word_data :dict = {}, secret_word :str = None):
    secret_word_data = dict(secret_word_data)
    if secret_word_key in secret_word_data.keys(): return str(secret_word_data[secret_word_key])
    else: return str(secret_word)

def set_word_list(word_list_data :dict = {}, word_list :list = []):
    word_list_data = dict(word_list_data)
    word_list_data[word_list_key] = list(word_list)
    return word_list_data

def get_word_list(word_list_data :dict = {}, word_list :list = []):
    word_list_data = dict(word_list_data)
    if word_list_key in word_list_data.keys(): return list(word_list_data[word_list_key])
    else: return list(word_list)

def set_hint(hint_data :dict = {}, index :int = None, hint :str = empty):
    hint_data = dict(hint_data)
    if index == None: index = get_player_number(hint_data)
    player = get_player(hint_data, index)
    player[hint_key] = str(hint)
    hint_data = set_player(hint_data, index, player)
    return hint_data

def get_hint(hint_data :dict = {}, index :int = None, hint :str = empty):
    hint_data = dict(hint_data)
    if index == None: index = get_player_number(hint_data)
    if hint_key in get_player(hint_data, index).keys(): return str(get_player(hint_data, index)[hint_key])
    else: return str(hint)

def set_last_hint(last_hint_data :dict = {}, index :int = None, last_hint :dict = None):
    last_hint_data = dict(last_hint_data)
    if index == None: index = get_player_number(last_hint_data)
    if last_hint == None:
        last_hint = {}
        last_hint[puzzle_key] = f"{underscore} " * len(get_secret_word(last_hint_data))
        last_hint[letters_key] = empty
    player = get_player(last_hint_data, int(index))
    player[last_hint_key] = dict(last_hint)
    last_hint_data = set_player(last_hint_data, index, player)
    return last_hint_data

def get_last_hint(last_hint_data :dict = {}, index :int = None, last_hint :dict = None):
    last_hint_data = dict(last_hint_data)
    if index == None: index = get_player_number(last_hint_data)
    if last_hint == None:
        last_hint = {}
        last_hint[puzzle_key] = f"{underscore} " * len(get_secret_word(last_hint_data))
        last_hint[letters_key] = empty
    if puzzle_key in dict(last_hint).keys():
        if last_hint[puzzle_key] == None:
            last_hint[puzzle_key] = f"{underscore} " * len(get_secret_word(last_hint_data))
    if last_hint_key in get_player(last_hint_data, int(index)).keys():
        return dict(get_player(last_hint_data, index)[last_hint_key])
    else:
        return dict(last_hint)

def set_guess(guess_data :dict = {}, guess :str = empty):
    guess_data = dict(guess_data)
    guess_data[guess_key] = str(guess)
    return guess_data

def get_guess(guess_data :dict = {}, guess :str = empty):
    guess_data = dict(guess_data)
    if guess_key in guess_data.keys():
        return str(guess_data[guess_key])
    else:
        return str(guess)

def set_player(player_data :dict = {}, index :int = None, player :dict = {}):
    player_data = dict(player_data)
    if index == None: index = get_player_number(player_data)
    players = get_players(player_data)
    players[int(index)] = dict(player)
    player_data = set_players(player_data, players)
    return player_data

def get_player(player_data :dict = {}, index :int = None, player :dict = {}):
    player_data = dict(player_data)
    if index == None: index = get_player_number(player_data)
    if players_key in player_data.keys():
        return dict(get_players(player_data)[int(index)])
    else:
        return dict(player)

def set_number_of_players(number_of_players_data :dict = {}, number_of_players :int = 1):
    number_of_players_data = dict(number_of_players_data)
    number_of_players_data[number_of_players_key] = int(number_of_players)
    for index in range(1, number_of_players + 1): number_of_players_data = set_player(number_of_players_data, index)
    number_of_players_data = set_player_number(number_of_players_data)
    return number_of_players_data

def get_number_of_players(number_of_players_data :dict = {}, number_of_players :int = 1):
    number_of_players_data = dict(number_of_players_data)
    if number_of_players_key in number_of_players_data.keys():
        return int(number_of_players_data[number_of_players_key])
    else:
        return int(number_of_players)

def set_max_turns(max_turns_data :dict = {}, max_turns :int = 0):
    max_turns_data = dict(max_turns_data)
    max_turns_data[max_turns_key] = int(max_turns)
    return max_turns_data

def get_max_turns(max_turns_data :dict = {}, max_turns :int = 0):
    max_turns_data = dict(max_turns_data)
    if max_turns_key in max_turns_data.keys():
        return int(max_turns_data[max_turns_key])
    else:
        return int(max_turns)

def set_super_hint_frequency(super_hint_frequency_data :dict = {}, super_hint_frequency :int = 0):
    super_hint_frequency_data = dict(super_hint_frequency_data)
    super_hint_frequency_data[super_hint_frequency_key] = int(super_hint_frequency)
    return super_hint_frequency_data

def get_super_hint_frequency(super_hint_frequency_data :dict = {}, super_hint_frequency :int = 0):
    super_hint_frequency_data = dict(super_hint_frequency_data)
    if super_hint_frequency_key in super_hint_frequency_data.keys():
        return int(super_hint_frequency_data[super_hint_frequency_key])
    else:
        return int(super_hint_frequency)

def set_players(players_data :dict = {}, players :dict = {}):
    players_data = dict(players_data)
    players_data[players_key] = dict(players)
    return players_data

def get_players(players_data :dict = {}, players :dict = {}):
    players_data = dict(players_data)
    if players_key in players_data.keys():
        return dict(players_data[players_key])
    else:
        return dict(players)

def set_multiplayer_init(multiplayer_init_data :dict = {}, multiplayer_init :bool = False):
    multiplayer_init_data = dict(multiplayer_init_data)
    multiplayer_init_data[multiplayer_init_key] = bool(multiplayer_init)
    return multiplayer_init_data

def get_multiplayer_init(multiplayer_init_data :dict = {}, multiplayer_init :bool = False):
    multiplayer_init_data = dict(multiplayer_init_data)
    if multiplayer_init_key in multiplayer_init_data.keys():
        return bool(multiplayer_init_data[multiplayer_init_key])
    else:
        return bool(multiplayer_init)

def set_track(track_data :dict = {}, track :list = []):
    track_data = dict(track_data)
    track_data[track_key] = list(track)
    return track_data

def get_track(track_data :dict = {}, track :list = []):
    track_data = dict(track_data)
    if track_key in track_data.keys():
        return list(track_data[track_key])
    else:
        return list(track)

def does_guess_not_equal_secret_word(is_next_turn_data :dict = {}):
    is_next_turn_data = dict(is_next_turn_data)
    return get_secret_word(is_next_turn_data) != get_guess(is_next_turn_data)

def is_next_turn(is_next_turn_data :dict = {}):
    is_next_turn_data = dict(is_next_turn_data)
    return does_guess_not_equal_secret_word(is_next_turn_data) and\
        ((get_max_turns(is_next_turn_data) < 1) or\
        ((get_max_turns(is_next_turn_data) >= 1) and (get_turn_number(is_next_turn_data) < get_max_turns(is_next_turn_data))))

def game_win_message(game_win_message_data :dict = {}):
    game_win_message_data = dict(game_win_message_data)
    if get_number_of_players(game_win_message_data) > 1: print(f"Congratulations Player {get_player_number(game_win_message_data)}, you guessed the word!")
    else: print("Congratulations, you guessed the word!")
    print(f"You did it in {get_turn_number(game_win_message_data) + 1} guesses.")
    return game_win_message_data

def init_game(initialization_data :dict = {}, exit :bool = False):
    initialization_data = dict(initialization_data)
    initialization_data = set_random(initialization_data)
    initialization_data = set_exit(initialization_data, bool(exit))
    initialization_data = set_players(initialization_data)
    initialization_data = set_word_list(initialization_data, default_list)
    return initialization_data

def configure_game(configuration_data :dict = {}):
    configuration_data = dict(configuration_data)
    configuration_data = set_number_of_players(configuration_data, int(input("How many players? ")))
    configuration_data = set_max_turns(configuration_data, int(input("How many guesses do you want? ")))
    if str(input("Do you want super hints [(y)es/(n)o]? ")).lower() in ["y", "yes", empty]:
        if get_max_turns(configuration_data) > 0:
            super_hints = int(input("How many super hints do you want as a minimum? ")) + 1
            if super_hints >= get_max_turns(configuration_data): configuration_data = set_super_hint_frequency(configuration_data,  1)
            elif super_hints > 0: configuration_data = set_super_hint_frequency(configuration_data,  int(get_max_turns(configuration_data) / super_hints))
            else: configuration_data = set_super_hint_frequency(configuration_data,  0)
        else: configuration_data = set_super_hint_frequency(configuration_data,  int(input("How often do you want super hints? ")))
    else: configuration_data = set_super_hint_frequency(configuration_data,  0)
    return configuration_data

def play_turn(turn_data :dict = {}):
    if get_number_of_players(turn_data) > 1:
        if get_multiplayer_init(turn_data): input("Press enter to continue.")
        turn_data = set_multiplayer_init(turn_data, True)
        print("\n" * 5)
        os.system("cls")
        print(f"Player {get_player_number(turn_data)} Turn {get_turn_number(turn_data) + 1}")
        input("Press enter to continue.")
    else: print(f"Turn {get_turn_number(turn_data) + 1}")
    if (get_max_turns(turn_data) >= 1) and (get_max_turns(turn_data)-get_turn_number(turn_data) == 1): print("last chance!")
    elif (get_max_turns(turn_data) >= 1) and (get_turn_number(turn_data) < (get_max_turns(turn_data))): print(f"{get_max_turns(turn_data)-get_turn_number(turn_data)} turns remaining!")
    print(f"Your hint is {get_hint(turn_data)}.")
    if (get_max_turns(turn_data) >= 1) and (get_max_turns(turn_data)-get_turn_number(turn_data) == 1): print(f"Your last hint is {get_last_hint(turn_data)[puzzle_key]}with \"{get_last_hint(turn_data)[letters_key]}\" letters")
    elif ((get_turn_number(turn_data) + 1) > 0) and (get_super_hint_frequency(turn_data) >= 1):
        if (((get_turn_number(turn_data) + 1) % get_super_hint_frequency(turn_data)) == 0): print(f"Your super hint is {get_last_hint(turn_data)[puzzle_key]}with \"{get_last_hint(turn_data)[letters_key]}\" letters")
    #have the user make a guess
    turn_data = set_guess(turn_data,  input("what is your guess? "))
    #Check to see if the guess is the same length as the secret word
    if len(get_secret_word(turn_data)) != len(get_guess(turn_data)):
        #print a message when they're not the same
        print("Your guess must have the same number of letters as the secrete word!\n")
        turn_data = set_hint(turn_data, hint = f"{underscore} " * len(get_secret_word(turn_data)))
    #Otherwise figure out the hint
    else:
        turn_data = set_track(turn_data)
        for index in range(len(get_guess(turn_data))):
            track = get_track(turn_data)
            track.append(get_secret_word(turn_data)[index])
            if get_guess(turn_data)[index] == get_secret_word(turn_data)[index]:
                track.pop()
                track.append(underscore)
            turn_data = set_track(turn_data, track)
        turn_data = set_hint(turn_data)
        #for each letter in the guess
        for index in range(len(get_guess(turn_data))):
            #check if the letter at this location in the guess is the same as this same location in the secret word
            if get_guess(turn_data)[index] == get_secret_word(turn_data)[index]:
                #print out the letter capitalized
                turn_data = set_hint(turn_data, hint = f"{get_hint(turn_data)}{get_guess(turn_data)[index].upper()} ")
            #check if the letter is in the secret word but is in the wrong place\
            elif get_guess(turn_data)[index] in get_track(turn_data):
                track = get_track(turn_data)
                tIndex = track.index(get_guess(turn_data)[index])
                track.pop(tIndex)
                track.insert(tIndex, underscore)
                turn_data = set_track(turn_data, track)
                #print out the letter in lower case
                turn_data = set_hint(turn_data, hint = f"{get_hint(turn_data)}{get_guess(turn_data)[index].lower()} ")
            #otherwise, the letter isn't in the word at all
            else:
                #so print out an underscore
                turn_data = set_hint(turn_data, hint = f"{get_hint(turn_data)}{underscore} ")
        last_hint = get_last_hint(turn_data)
        new_puzzle = empty
        new_letters = str(last_hint[letters_key])
        for index in range(len(get_secret_word(turn_data))):
            if (get_hint(turn_data)[index * 2] != underscore) and (last_hint[puzzle_key][index * 2] == underscore):
                if (get_hint(turn_data)[index * 2].upper() == get_hint(turn_data)[index * 2]):
                    #add new if upper
                    new_puzzle = f"{new_puzzle}{get_hint(turn_data)[index * 2]} "
                    if get_hint(turn_data)[index * 2].lower() in new_letters:
                        #remove from letters is present
                        new_letters = new_letters.replace(get_hint(turn_data)[index * 2].lower(), underscore, 1)
                else:
                    #keep old
                    new_puzzle = f"{new_puzzle}{last_hint[puzzle_key][index * 2]} "
            elif (get_hint(turn_data)[index * 2] != underscore):
                #keep old
                new_puzzle = f"{new_puzzle}{last_hint[puzzle_key][index * 2]} "
            else:
                #keep old
                new_puzzle = f"{new_puzzle}{last_hint[puzzle_key][index * 2]} "
            #add new unknown location letter to letters
            new_letters = f"{new_letters}{get_hint(turn_data)[index * 2]}"
        last_hint[puzzle_key] = new_puzzle
        # rebuild letters based on available to be found and which instance the old letters was (removing extra old letters over teh available to be found)
        last_hint[letters_key] = empty
        for index in range(len(new_letters)):
            if ((get_secret_word(turn_data).count(new_letters[index]) - new_puzzle.count(new_letters[index].upper())) > 0) and (new_letters[0:index+1].count(new_letters[index]) <= (get_secret_word(turn_data).count(new_letters[index]) - new_puzzle.count(new_letters[index].upper()))): last_hint[letters_key] = f"{last_hint[letters_key]}{new_letters[index]}"
        turn_data = set_last_hint(turn_data, last_hint = last_hint)
    #make sure to increment the guess counter
    if get_secret_word(turn_data) != get_guess(turn_data):
        turn_data = set_player_number(turn_data, get_player_number(turn_data) + 1)
        if get_player_number(turn_data) > get_number_of_players(turn_data): turn_data = set_turn_number(set_player_number(turn_data), get_turn_number(turn_data) + 1)
    return turn_data

def play_game(game_data :dict = {}):
    game_data = dict(game_data)
    clear_screen()
    game_data = configure_game(game_data)
    #Store a secret word
    game_data = set_secret_word(game_data)
    for index in range(1, get_number_of_players(game_data) + 1):
        game_data = set_hint(game_data, index, f"{underscore} " * len(get_secret_word(game_data)))
        game_data = set_last_hint(game_data, index)
    #Create a variable to store the user's guess
    game_data = set_guess(game_data)
    #Create a variable to count the number of guesses
    game_data = set_multiplayer_init(set_turn_number(game_data))
    #Continue looping as long as the guess is not correct
    while is_next_turn(game_data): game_data = play_turn(game_data)
    #when you get out here, that means they got the secret word. print out a message to say how many guesses it took
    if(get_secret_word(game_data) == get_guess(game_data)): game_data = game_win_message(game_data)
    else: print("Better luck next time!")
    if not (input("play again [(y)es/(n)o]?").lower() in ["y", "yes"]): game_data = set_exit(game_data, True)
    return game_data

def main():
    main_data = init_game()
    while not get_exit(main_data): main_data = play_game(main_data)

main()