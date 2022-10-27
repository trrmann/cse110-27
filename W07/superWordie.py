#pip install requests
#pip install certifi
from random import *
import requests
import certifi
import os

exit_key = "exit"
number_of_players_key = "number_of_players"
bible_string_key = "bible_strings"
online_key = "online"
letters_key = "letters"
non_case_words_key = "non_case_words"
full_words_key = "full_words_key"
words_key = "words"
word_key = "word"
count_key = "count"
percent_key = "percent"
rank_key = "rank"
puzzle_key = "puzzle"
question_count_key = "question_count"
fail_count_key = "fail_count"
invalid_count_key = "invalid_count"
lost_key = "lost"
points_key = "points"
guesses_key = "guesses"
offline_list = ["testing", "developing", "implementing", "patching", "upgrading"]

def isAlpha(string):
    s = string
    return (len(s) == 1) and (s.lower() >= "a" and s.lower() <= "z")

def purify_alpha(string, min_len = 2):
    if len(string) < min_len:
        return string
    else:
        if isAlpha(string[0]) and isAlpha(string[len(string)-1]):
            return string
        elif isAlpha(string[0]):
            return purify_alpha(string[0:len(string)-1], min_len)
        elif isAlpha(string[len(string)-1]):
            return purify_alpha(string[1:len(string)], min_len)
        else:
            return purify_alpha(string[0:len(string)-1], min_len)

def test_connection_to_github():
    try:
        print('Checking connection to Github...')
        test = requests.get('https://api.github.com')
        print('Connection to Github OK.')
        return True
    except requests.exceptions.SSLError as err:
        print('SSL Error. Adding custom certs to Certifi store...')
        cafile = certifi.where()
        with open('certicate.pem', 'rb') as infile:
            customca = infile.read()
        with open(cafile, 'ab') as outfile:
            outfile.write(customca)
        print('That might have worked.')
        return False

def has_letters(string):
    if string == None:
        return False
    else:
        count=0
        for letter in string:
            if isAlpha(letter): count = count + 1
        return count > 0

def only_letters(string):
    if string == None:
        return string
    else:
        return all(isAlpha(letter) for letter in string)

def get_bible_strings():
    data = {}
    data[online_key] = False
    if test_connection_to_github():
        data[online_key] = True
        kjv_scriptures_file = "https://raw.githubusercontent.com/beandog/lds-scriptures/master/text/kjv-scriptures.txt"
        lds_scriptures_file = "https://raw.githubusercontent.com/beandog/lds-scriptures/master/text/lds-scriptures.txt"
        kjv_scriptures = requests.get(url=kjv_scriptures_file, params={"owner":"beandog", "repo":"lds-scriptures", "path":"text/kjv-scriptures.txt", "ref":"master", "accept":"application/text"}, stream = True)
        lds_scriptures = requests.get(url=lds_scriptures_file, params={"owner":"beandog", "repo":"lds-scriptures", "path":"text/lds-scriptures.txt", "ref":"master", "accept":"application/text"}, stream = True)
        scriptures = f"{kjv_scriptures.text}\n{lds_scriptures.text}"
        lines = scriptures.split("\n")
        non_case_words = {}
        words = {}
        letters = {}
        min_len = 1
        word_count = 0
        for line in lines:
            line_words = line.split(" ")
            for word in line_words:
                word = purify_alpha(word, min_len)
                if only_letters(word) and (len(word) >= min_len):
                    if not(word in words.keys()): 
                        words[word] = 0
                        non_case_words[word.lower()] = 0
                    words[word] = words[word] + 1
                    non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                    word_count = word_count + 1
                    for letter in word.lower():
                        if not(letter in letters.keys()):
                            letters[letter] = 0
                        letters[letter] = letters[letter] + 1
                elif has_letters(word) and (len(word) >= (min_len + 2)) and ("'" in word):
                    if only_letters(word[0:len(word)-2]) and (len(word[0:len(word)-2]) >= min_len):
                        if not(word in words.keys()): 
                            words[word] = 0
                            non_case_words[word.lower()] = 0
                        words[word] = words[word] + 1
                        non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                        word_count = word_count + 1
                        for letter in word.lower():
                            if isAlpha(letter):
                                if not(letter in letters.keys()):
                                    letters[letter] = 0
                                letters[letter] = letters[letter] + 1
                        word = word[0:len(word)-2]
                        if not(word in words.keys()): 
                            words[word] = 0
                            non_case_words[word.lower()] = 0
                        words[word] = words[word] + 1
                        non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                    elif only_letters(word[2:len(word)]) and (len(word[1:len(word)]) >= min_len):
                        if not(word in words.keys()): 
                            words[word] = 0
                            non_case_words[word.lower()] = 0
                        words[word] = words[word] + 1
                        non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                        word_count = word_count + 1
                        for letter in word.lower():
                            if isAlpha(letter):
                                if not(letter in letters.keys()):
                                    letters[letter] = 0
                                letters[letter] = letters[letter] + 1
                        word = word[0:len(word)-2]
                        if not(word in words.keys()): 
                            words[word] = 0
                            non_case_words[word.lower()] = 0
                        words[word] = words[word] + 1
                        non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                    elif has_letters(word) and not("--" in word) and ("-" in word) and (len(word) >= (min_len + 1)):
                        if not(word in words.keys()): 
                            words[word] = 0
                            non_case_words[word.lower()] = 0
                        words[word] = words[word] + 1
                        non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                        word_count = word_count + 1
                        for letter in word.lower():
                            if isAlpha(letter):
                                if not(letter in letters.keys()):
                                    letters[letter] = 0
                                letters[letter] = letters[letter] + 1
                    else:
                        print(f"X'X {len(words.keys())} {word}")
                elif has_letters(word) and ("--" in word) and (len(word) >= ((min_len * 2) + 2)):
                    pair = word.split("--")
                    for pair_word in pair:
                        if only_letters(pair_word) and (len(pair_word) >= min_len):
                            if not(pair_word in words.keys()): 
                                words[pair_word] = 0
                                non_case_words[pair_word.lower()] = 0
                            words[pair_word] = words[pair_word] + 1
                            non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                            word_count = word_count + 1
                            for letter in pair_word.lower():
                                if isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                        else:
                            #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                            pass
                elif has_letters(word) and (";" in word) and (len(word) >= ((min_len * 2) + 1)):
                    pair = word.split(";")
                    for pair_word in pair:
                        if only_letters(pair_word) and (len(pair_word) >= min_len):
                            if not(pair_word in words.keys()): 
                                words[pair_word] = 0
                                non_case_words[pair_word.lower()] = 0
                            words[pair_word] = words[pair_word] + 1
                            non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                            word_count = word_count + 1
                            for letter in pair_word.lower():
                                if isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                        else:
                            #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                            pass
                elif has_letters(word) and ("," in word) and (len(word) >= ((min_len * 2) + 1)):
                    pair = word.split(",")
                    for pair_word in pair:
                        if only_letters(pair_word) and (len(pair_word) >= min_len):
                            if not(pair_word in words.keys()): 
                                words[pair_word] = 0
                                non_case_words[pair_word.lower()] = 0
                            words[pair_word] = words[pair_word] + 1
                            non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                            word_count = word_count + 1
                            for letter in pair_word.lower():
                                if isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                        else:
                            #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                            pass
                elif has_letters(word) and ("." in word) and (len(word) >= ((min_len * 2) + 1)):
                    pair = word.split(".")
                    for pair_word in pair:
                        if only_letters(pair_word) and (len(pair_word) >= min_len):
                            if not(pair_word in words.keys()): 
                                words[pair_word] = 0
                                non_case_words[pair_word.lower()] = 0
                            words[pair_word] = words[pair_word] + 1
                            non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                            word_count = word_count + 1
                            for letter in pair_word.lower():
                                if isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                        else:
                            #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                            pass
                elif has_letters(word) and not("--" in word) and ("-" in word) and (len(word) >= (min_len + 1)):
                    if not(word in words.keys()): 
                        words[word] = 0
                        non_case_words[word.lower()] = 0
                    words[word] = words[word] + 1
                    non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                    word_count = word_count + 1
                    for letter in word.lower():
                        if isAlpha(letter):
                            if not(letter in letters.keys()):
                                letters[letter] = 0
                            letters[letter] = letters[letter] + 1
                elif has_letters(word) and (len(word) >= min_len) and not(word in words.keys()):
                    print(f"{len(words.keys())} {word}")
        #            print(word)
        #    print(f"{line_count}  {line}")
        #    line_count = line_count + 1
        #print(words.keys())
        letter_count = 0
        for letter in letters.keys(): letter_count = letter_count + letters[letter]
        by_per = {}
        for letter in letters.keys():
            count = letters[letter]
            letters[letter] = {}
            letters[letter][count_key] = count
            letters[letter][percent_key] = letters[letter][count_key] / letter_count * 100
            by_per[letters[letter][percent_key]] = letter
        pk = [*by_per.keys()]
        pk.sort(reverse=True)
        rnk = {}
        for idx in range(len(pk)):
            rnk[by_per[pk[idx]]] = idx + 1
        for letter in letters.keys():
            letters[letter][rank_key] = rnk[letter]
        word_count = 0
        for word in non_case_words.keys(): word_count = word_count + non_case_words[word]
        by_per = {}
        for word in non_case_words.keys():
            count = non_case_words[word]
            non_case_words[word] = {}
            non_case_words[word][count_key] = count
            non_case_words[word][percent_key] = non_case_words[word][count_key] / word_count * 100
            by_per[non_case_words[word][percent_key]] = word
        pk = [*by_per.keys()]
        pk.sort(reverse=True)
        rnk = {}
        for idx in range(len(pk)):
            rnk[by_per[pk[idx]]] = idx + 1
            if idx <5 or idx >= len(pk)-5:
                pass
            #    print(f"{rnk[by_per[pk[idx]]]} {by_per[pk[idx]]} {non_case_words[by_per[pk[idx]]]}")
        for word in non_case_words.keys():
            if word in rnk.keys(): non_case_words[word][rank_key] = rnk[word]
            else:  non_case_words[word][rank_key] = rnk[by_per[non_case_words[word][percent_key]]]
        for idx in range(len(non_case_words.keys())):
            if idx <5 or idx >= len(non_case_words)-5:
                pass
            #    print(f"{idx} {[*(non_case_words.keys())][idx]} {non_case_words[[*(non_case_words.keys())][idx]]}")
        print(f"words:  {len(words.keys())} - non_case_words:  {len(non_case_words.keys())} - word_count:  {word_count} - letter_count:  {letter_count} - letters:  {len(letters.keys())}")
        data[letters_key] = letters
        data[non_case_words_key] = non_case_words
        data[words_key] = words
    else:
        data[words_key] = offline_list
    return data

def get_random_strings_list(count: int = 1, min_len: int = 5, full_list = offline_list):
    r = Random()
    r.seed()
    list = []
    for counter in range(5):
        word = ""
        while len(word) < int(min_len):
            word = r.choice(full_list)
        list.append(word)
    return list

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
    r = Random()
    r.seed()
    data = {}
    if(int(number_of_players) == int(min_number_of_players) - 2):
        data[exit_key] = True
    else:
        data[exit_key] = False
        data[number_of_players_key] = int(number_of_players)
        data[bible_string_key] = get_bible_strings()
        if data[bible_string_key][online_key]:
            data[full_words_key] = [*data[bible_string_key][words_key].keys()]
        else:
            data[full_words_key] = data[bible_string_key][words_key]
        data[words_key] = get_random_strings_list(5, 5, data[full_words_key])
        data[word_key] = r.choice(data[words_key])
        data[words_key].remove(data[word_key])
        data[puzzle_key] = ""
        size = len(data[word_key])
        for loop in range(size): data[puzzle_key] = f"{data[puzzle_key]}_ "
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
    if data[bible_string_key][online_key]:
        return not(guess.lower() in data[bible_string_key][non_case_words_key].keys())
    else:
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
    hint = ""
    puzzle = ""
    for index in range(len(guess)):
        letter = guess[index]
        if letter in data[word_key]:
            if letter == data[word_key][index]:
                hint = f"{hint} {letter.upper()}"
            else: hint = f"{hint} {letter.lower()}"
        else: hint = f"{hint} _"
    for index in range(len(data[word_key])):
        puzzle_index = (((index + 1) * 2) - 2)
        #if index < len(guess): print(f"{index} {data[word_key]} {puzzle_index} {data[puzzle_key][puzzle_index]} {guess[index]} {data[word_key][index]} {data[puzzle_key]} {guess} {len(guess)}")
        if (data[puzzle_key][puzzle_index] == "_") and (index < len(guess)):
            if guess[index].lower() == data[word_key][index].lower(): puzzle = f"{puzzle}{data[word_key][index]} "
            else: puzzle = f"{puzzle}{data[puzzle_key][puzzle_index]} "
        else: puzzle = f"{puzzle}{data[puzzle_key][puzzle_index]} "
    data[puzzle_key] = puzzle
    print(f"hint:  {hint}")

def show_puzzle(data):
    if data[player_number(data)][points_key] > 0: print(f"score:  {data[player_number(data)][points_key]}")
    print(data[puzzle_key])

def award_points(data, guess):
    points = 0
    if data[bible_string_key][online_key]:
        if data[word_key] == guess:
            points = data[bible_string_key][non_case_words_key][guess][rank_key] * 100
        for index in range(len(data[word_key])):
            letter = data[word_key][index]
            if index < len(guess):
                if letter == guess[index]:
                    points = points + (data[bible_string_key][letters_key][letter][rank_key] * 10)
                elif letter in guess:
                    points = points + data[bible_string_key][letters_key][letter][rank_key]
            elif letter in guess:
                points = points + data[bible_string_key][letters_key][letter][rank_key]
    else:
        if data[word_key] == guess:
            points = 100
        for index in range(len(data[word_key])):
            letter = data[word_key][index]
            if index < len(guess):
                if letter == guess[index]:
                    points = points + 10
                elif letter in guess:
                    points = points + 1
            elif letter in guess:
                points = points + 1
    data[player_number(data)][points_key] = data[player_number(data)][points_key] + points
    print(f"You get {points} points for a score of {data[player_number(data)][points_key]}!")

def next_word(data):
    r = Random()
    r.seed()
    print("next word")
    if len(data[words_key]) < 1: data[words_key] = get_random_strings_list(5, 5, data[full_words_key])
    data[word_key] = r.choice(data[words_key])
    data[words_key].remove(data[word_key])
    data[puzzle_key] = ""
    size = len(data[word_key])
    for loop in range(size): data[puzzle_key] = f"{data[puzzle_key]}_ "
    for player in range(data[number_of_players_key]):
        if not data[player + 1][lost_key]:
            data[player + 1][fail_count_key] = 0
            data[player + 1][invalid_count_key] = 0
            data[player + 1][guesses_key] = []

def eval_win(data):
    current_win_score = 0
    for player in range(data[number_of_players_key]):
        if not data[player + 1][lost_key]:
            if data[player + 1][points_key] > current_win_score:
                current_win_score = data[player + 1][points_key]
                current_win_player = player + 1
    print(f"Player {current_win_player} is winning with a score of {current_win_score}!")



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
        award_points(data, guess)
        data[player_number(data)][fail_count_key] = 0
        data[player_number(data)][invalid_count_key] = 0
        next_word(data)
    elif has_hint(data, guess) and not_exit(data):
        print("You got part of the word!")
        show_hint(data, guess)
        award_points(data, guess)
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
    