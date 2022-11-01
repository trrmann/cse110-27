import ast
from datetime import datetime, timedelta
from pathlib import Path
import random
import os
import shutil
from ssl import CertificateError
import requests

empty = ""
underscore = "_"

def clear_screen():
    print("\n" * 5)
    os.system("cls")

def other(game):
    other_file1 = "test.dat"
    other_file2 = "test.txt"
    other_file3 = "test.tmp"

    shutil.copyfile(other_file1, other_file3)
    if not game.file_exists(other_file1):
        print("no file... create")
        file = open(other_file1, "xt")
        file.close()
    file = open(other_file1, "rt")
    file_raw_data = file.read()
    if file_raw_data != "": file_data = ast.literal_eval(file_raw_data)
    else: file_data = file_raw_data
    file.close()
    print(other_file1)
    print(file_data)
    if file_data == "":  file_data = {}
    if "x" in file_data.keys(): print(f"x = {file_data['x']}")
    if "y" in file_data.keys(): print(f"y = {file_data['y']}")
    file_data["x"] = 1
    file_data["y"] = 2
    file = open(other_file1, "wt")
    file.write(str(file_data))
    file.close()
    os.remove(other_file3)

    now = datetime.now()

    print(f"created:  {other_file2} - {game.file_created_datetime(other_file2)} - {game.file_created_age(other_file2)} - {game.is_data_filename_create_expired(other_file2)}")
    print(f"now {now}")
    game.request_enter_to_continue()

def main():
    game = Wordle()
    print(game.read_data_from_github())
    game.request_enter_to_continue()
    while not game.get_exit(): game.play_game()
    #other(game)
    print(game)

class Wordle():
    __random_key__ = "random"
    __exit_key__ = "exit"
    __word_list_key__ = "wordList"
    __secret_word_key__ = "secretWord"
    __number_of_players_key__ = "numberOfPlayers"
    __player_number_key__ = "playerNumber"
    __max_turns_key__ = "maxTurns"
    __super_hint_frequency_key__ = "superHintFrequency"
    __players_key__ = "players"
    __multiplayer_init_key__ = "multiplayerInit"
    __hint_key__ = "hint"
    __last_hint_key__ = "lastHint"
    __puzzle_key__ = "puzzle"
    __letters_key__ = "letters"
    __guess_key__ = "guess"
    __turn_number_key__ = "turn"
    __track_key__ = "track"
    __lost_key__ = "lost"
    data_filename_key = "dataFilename"
    data_filename_access_expire_age_days_key = "dataFilenameAccessExpireAgeDays"
    data_filename_modify_expire_age_days_key = "dataFilenameModifyExpireAgeDays"
    data_filename_create_expire_age_days_key = "dataFilenameCreateExpireAgeDays"

    online_key = "online"
    letters_key = "letters"
    non_case_words_key = "non_case_words"
    words_key = "words"
    count_key = "count"
    percent_key = "percent"
    rank_key = "rank"

    __data__ = None
    default_list = ["dog", "cat", "pig", "cow", "ape", "sow", "sheep", "sleep", "house", "horse", "apple"]

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.__data__ = {}
        self.init_game()

    def __repr__(self) -> str:
        string = f"\"{self.__exit_key__}\" : {self.get_exit()}"
        string = f"{string}, \"{self.data_filename_access_expire_age_days_key}\" : {self.get_data_filename_access_expire_age_days()}"
        string = f"{string}, \"{self.data_filename_modify_expire_age_days_key}\" : {self.get_data_filename_modify_expire_age_days()}"
        string = f"{string}, \"{self.data_filename_create_expire_age_days_key}\" : {self.get_data_filename_create_expire_age_days()}"
        string = f"{string}, \"{self.data_filename_key}\" : \"{self.get_data_filename()}\""
        string = f"{string}, \"{self.__word_list_key__}\" : {self.get_word_list()}"
        string = f"{string}, \"{self.__secret_word_key__}\" : \"{self.get_secret_word()}\""
        string = f"{string}, \"{self.__number_of_players_key__}\" : {self.get_number_of_players()}"
        string = f"{string}, \"{self.__player_number_key__}\" : {self.get_player_number()}"
        string = f"{string}, \"{self.__max_turns_key__}\" : {self.get_max_turns()}"
        string = f"{string}, \"{self.__super_hint_frequency_key__}\" : {self.get_super_hint_frequency()}"
        string = f"{string}, \"{self.__players_key__}\" : {self.get_players()}"
        string = f"{string}, \"{self.__multiplayer_init_key__}\" : {self.get_multiplayer_init()}"
        string = f"{string}, \"{self.__guess_key__}\" : \"{self.get_guess()}\""
        string = f"{string}, \"{self.__turn_number_key__}\" : {self.get_turn_number()}"
        string = f"{string}, \"{self.__track_key__}\" : {self.get_track()}"
        string = f"\( {string} \)"
        string = f"\( \"{type(self).__name__}\" : {string} \)"
        string = string.replace("\(", "{")
        string = string.replace("\)", "}")
        return string

    def read_file(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        file = open(filename, "rt")
        file_raw_data = file.read()
        if file_raw_data != "": data = ast.literal_eval(file_raw_data)
        else: data = {}
        file.close()
        return data

    def test_connection_to_github(self):
        try:
            print('Checking connection to Github...')
            test = requests.get('https://api.github.com')
            print('Connection to Github OK.')
            return True
        
        except requests.exceptions.ConnectionError as err:
            ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
            print("connection closed!")
            #raise err
        except requests.exceptions.SSLError as err:
            print('SSL Error. Adding custom certs to Certifi store...')
            cafile = CertificateError.where()
            with open('certicate.pem', 'rb') as infile:
                customca = infile.read()
            with open(cafile, 'ab') as outfile:
                outfile.write(customca)
            print('That might have worked.')
            return False

    def isAlpha(self, string):
        s = string
        return (len(s) == 1) and (s.lower() >= "a" and s.lower() <= "z")

    def purify_alpha(self, string, min_len = 2):
        if len(string) < min_len:
            return string
        else:
            if self.isAlpha(string[0]) and self.isAlpha(string[len(string)-1]):
                return string
            elif self.isAlpha(string[0]):
                return self.self.purify_alpha(string[0:len(string)-1], min_len)
            elif self.isAlpha(string[len(string)-1]):
                return self.self.purify_alpha(string[1:len(string)], min_len)
            else:
                return self.self.purify_alpha(string[0:len(string)-1], min_len)

    def has_letters(self, string):
        if string == None:
            return False
        else:
            count=0
            for letter in string:
                if self.isAlpha(letter): count = count + 1
            return count > 0

    def only_letters(self, string):
        if string == None:
            return string
        else:
            return all(self.isAlpha(letter) for letter in string)

    def get_bible_strings(self):
        data = {}
        data[self.online_key] = False
        if self.test_connection_to_github():
            data[self.online_key] = True
            kjv_scriptures_file = "https://raw.githubusercontent.com/beandog/lds-scriptures/master/text/kjv-scriptures.txt"
            lds_scriptures_file = "https://raw.githubusercontent.com/beandog/lds-scriptures/master/text/lds-scriptures.txt"
            kjv_scriptures = request.Request.get(url=kjv_scriptures_file, params={"owner":"beandog", "repo":"lds-scriptures", "path":"text/kjv-scriptures.txt", "ref":"master", "accept":"application/text"}, stream = True)
            lds_scriptures = request.Request.get(url=lds_scriptures_file, params={"owner":"beandog", "repo":"lds-scriptures", "path":"text/lds-scriptures.txt", "ref":"master", "accept":"application/text"}, stream = True)
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
                    word = self.purify_alpha(word, min_len)
                    if self.only_letters(word) and (len(word) >= min_len):
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
                    elif self.has_letters(word) and (len(word) >= (min_len + 2)) and ("'" in word):
                        if self.only_letters(word[0:len(word)-2]) and (len(word[0:len(word)-2]) >= min_len):
                            if not(word in words.keys()): 
                                words[word] = 0
                                non_case_words[word.lower()] = 0
                            words[word] = words[word] + 1
                            non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                            word_count = word_count + 1
                            for letter in word.lower():
                                if self.isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                            word = word[0:len(word)-2]
                            if not(word in words.keys()): 
                                words[word] = 0
                                non_case_words[word.lower()] = 0
                            words[word] = words[word] + 1
                            non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                        elif self.only_letters(word[2:len(word)]) and (len(word[1:len(word)]) >= min_len):
                            if not(word in words.keys()): 
                                words[word] = 0
                                non_case_words[word.lower()] = 0
                            words[word] = words[word] + 1
                            non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                            word_count = word_count + 1
                            for letter in word.lower():
                                if self.isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                            word = word[0:len(word)-2]
                            if not(word in words.keys()): 
                                words[word] = 0
                                non_case_words[word.lower()] = 0
                            words[word] = words[word] + 1
                            non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                        elif self.has_letters(word) and not("--" in word) and ("-" in word) and (len(word) >= (min_len + 1)):
                            if not(word in words.keys()): 
                                words[word] = 0
                                non_case_words[word.lower()] = 0
                            words[word] = words[word] + 1
                            non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                            word_count = word_count + 1
                            for letter in word.lower():
                                if self.isAlpha(letter):
                                    if not(letter in letters.keys()):
                                        letters[letter] = 0
                                    letters[letter] = letters[letter] + 1
                        else:
                            print(f"X'X {len(words.keys())} {word}")
                    elif self.has_letters(word) and ("--" in word) and (len(word) >= ((min_len * 2) + 2)):
                        pair = word.split("--")
                        for pair_word in pair:
                            if self.only_letters(pair_word) and (len(pair_word) >= min_len):
                                if not(pair_word in words.keys()): 
                                    words[pair_word] = 0
                                    non_case_words[pair_word.lower()] = 0
                                words[pair_word] = words[pair_word] + 1
                                non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                                word_count = word_count + 1
                                for letter in pair_word.lower():
                                    if self.isAlpha(letter):
                                        if not(letter in letters.keys()):
                                            letters[letter] = 0
                                        letters[letter] = letters[letter] + 1
                            else:
                                #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                                pass
                    elif self.has_letters(word) and (";" in word) and (len(word) >= ((min_len * 2) + 1)):
                        pair = word.split(";")
                        for pair_word in pair:
                            if self.only_letters(pair_word) and (len(pair_word) >= min_len):
                                if not(pair_word in words.keys()): 
                                    words[pair_word] = 0
                                    non_case_words[pair_word.lower()] = 0
                                words[pair_word] = words[pair_word] + 1
                                non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                                word_count = word_count + 1
                                for letter in pair_word.lower():
                                    if self.isAlpha(letter):
                                        if not(letter in letters.keys()):
                                            letters[letter] = 0
                                        letters[letter] = letters[letter] + 1
                            else:
                                #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                                pass
                    elif self.has_letters(word) and ("," in word) and (len(word) >= ((min_len * 2) + 1)):
                        pair = word.split(",")
                        for pair_word in pair:
                            if self.only_letters(pair_word) and (len(pair_word) >= min_len):
                                if not(pair_word in words.keys()): 
                                    words[pair_word] = 0
                                    non_case_words[pair_word.lower()] = 0
                                words[pair_word] = words[pair_word] + 1
                                non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                                word_count = word_count + 1
                                for letter in pair_word.lower():
                                    if self.isAlpha(letter):
                                        if not(letter in letters.keys()):
                                            letters[letter] = 0
                                        letters[letter] = letters[letter] + 1
                            else:
                                #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                                pass
                    elif self.has_letters(word) and ("." in word) and (len(word) >= ((min_len * 2) + 1)):
                        pair = word.split(".")
                        for pair_word in pair:
                            if self.only_letters(pair_word) and (len(pair_word) >= min_len):
                                if not(pair_word in words.keys()): 
                                    words[pair_word] = 0
                                    non_case_words[pair_word.lower()] = 0
                                words[pair_word] = words[pair_word] + 1
                                non_case_words[pair_word.lower()] = non_case_words[pair_word.lower()] + 1
                                word_count = word_count + 1
                                for letter in pair_word.lower():
                                    if self.isAlpha(letter):
                                        if not(letter in letters.keys()):
                                            letters[letter] = 0
                                        letters[letter] = letters[letter] + 1
                            else:
                                #print(f"X--X {len(words.keys())} {word} {pair} {pair_word}")
                                pass
                    elif self.has_letters(word) and not("--" in word) and ("-" in word) and (len(word) >= (min_len + 1)):
                        if not(word in words.keys()): 
                            words[word] = 0
                            non_case_words[word.lower()] = 0
                        words[word] = words[word] + 1
                        non_case_words[word.lower()] = non_case_words[word.lower()] + 1
                        word_count = word_count + 1
                        for letter in word.lower():
                            if self.isAlpha(letter):
                                if not(letter in letters.keys()):
                                    letters[letter] = 0
                                letters[letter] = letters[letter] + 1
                    elif self.has_letters(word) and (len(word) >= min_len) and not(word in words.keys()):
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
                letters[letter][self.count_key] = count
                letters[letter][self.percent_key] = letters[letter][self.count_key] / letter_count * 100
                by_per[letters[letter][self.percent_key]] = letter
            pk = [*by_per.keys()]
            pk.sort(reverse=True)
            rnk = {}
            for idx in range(len(pk)):
                rnk[by_per[pk[idx]]] = idx + 1
            for letter in letters.keys():
                letters[letter][self.rank_key] = rnk[letter]
            word_count = 0
            for word in non_case_words.keys(): word_count = word_count + non_case_words[word]
            by_per = {}
            for word in non_case_words.keys():
                count = non_case_words[word]
                non_case_words[word] = {}
                non_case_words[word][self.count_key] = count
                non_case_words[word][self.percent_key] = non_case_words[word][self.count_key] / word_count * 100
                by_per[non_case_words[word][self.percent_key]] = word
            pk = [*by_per.keys()]
            pk.sort(reverse=True)
            rnk = {}
            for idx in range(len(pk)):
                rnk[by_per[pk[idx]]] = idx + 1
                if idx <5 or idx >= len(pk)-5:
                    pass
                #    print(f"{rnk[by_per[pk[idx]]]} {by_per[pk[idx]]} {non_case_words[by_per[pk[idx]]]}")
            for word in non_case_words.keys():
                if word in rnk.keys(): non_case_words[word][self.rank_key] = rnk[word]
                else:  non_case_words[word][self.rank_key] = rnk[by_per[non_case_words[word][self.percent_key]]]
            for idx in range(len(non_case_words.keys())):
                if idx <5 or idx >= len(non_case_words)-5:
                    pass
                #    print(f"{idx} {[*(non_case_words.keys())][idx]} {non_case_words[[*(non_case_words.keys())][idx]]}")
            print(f"words:  {len(words.keys())} - non_case_words:  {len(non_case_words.keys())} - word_count:  {word_count} - letter_count:  {letter_count} - letters:  {len(letters.keys())}")
            data[self.letters_key] = letters
            data[self.non_case_words_key] = non_case_words
            data[self.words_key] = words
        else:
            data[self.words_key] = {}
        return data

    def read_data_from_github(self):
        data = self.get_bible_strings()
        return data

    def get_default_datafile_data(self):
        default_data = {}
        word_list = {}
        for index in range(len(self.default_list)):
            word = self.default_list[index]
            word_list[word] = {}
            word_list[word]["display"] = word
            word_list[word]["count"] = 1
            word_list[word]["points"] = 5
        default_data[self.__word_list_key__] = word_list
        return default_data

    def create_empty_file(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.file_exists(filename): os.remove(filename)
        file = open(filename, "xt")
        file.close()

    def write_data_to_file(self, filename :str = None, data :dict = {}):
        if filename == None: filename = self.get_data_filename()
        file = open(filename, "wt")
        file.write(str(data))
        file.close()

    def build_file(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        github_data = self.read_data_from_github()
        if github_data != {}:
            self.create_empty_file(filename)
            if not(self.__word_list_key__ in github_data.keys()): self.write_data_to_file(filename, self.get_default_datafile_data())
            else: self.write_data_to_file(filename, github_data)
        elif (not self.file_exists(filename)) and (github_data == {}):
            self.create_empty_file(filename)
            self.write_data_to_file(filename, self.get_default_datafile_data())
        else:
            data = self.read_file(filename)
            if self.__word_list_key__ not in data.keys():
                self.create_empty_file(filename)
                self.write_data_to_file(filename, self.get_default_datafile_data())

    def load_word_list(self):
        if (self.is_data_filename_create_expired() == None) or (self.is_data_filename_modify_expired() == None) or (self.is_data_filename_access_expired() == None) or (not self.file_exists()): self.build_file()
        if self.is_data_filename_create_expired() or self.is_data_filename_modify_expired() or self.is_data_filename_access_expired(): self.build_file()
        file_data = self.read_file()
        self.set_word_list(file_data[self.__word_list_key__])

    def is_data_filename_access_expired(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.get_data_filename_access_expire_age_days() < 1: return False
        elif self.file_accessed_age(filename) != None: return (self.file_accessed_age(filename).days >= self.get_data_filename_access_expire_age_days())
        else: return True

    def is_data_filename_modify_expired(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.get_data_filename_modify_expire_age_days() < 1: return False
        elif self.file_modified_age(filename) != None: return (self.file_modified_age(filename).days >= self.get_data_filename_modify_expire_age_days())
        else: return True

    def is_data_filename_create_expired(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.get_data_filename_create_expire_age_days() < 1: return False
        elif self.file_created_age(filename) != None:  return (self.file_created_age(filename).days >= self.get_data_filename_create_expire_age_days())
        else: return True

    def set_data_filename_access_expire_age_days(self, access_expire_age_days :int = 3):
        self.__data__[self.data_filename_access_expire_age_days_key] = int(access_expire_age_days)
        return self

    def get_data_filename_access_expire_age_days(self, access_expire_age_days :int = None):
        if self.data_filename_access_expire_age_days_key in self.__data__.keys(): return self.__data__[self.data_filename_access_expire_age_days_key]
        elif access_expire_age_days != None: return self.set_data_filename_access_expire_age_days(int(access_expire_age_days)).get_data_filename_access_expire_age_days()
        else: return self.set_data_filename_access_expire_age_days().get_data_filename_access_expire_age_days()

    def set_data_filename_modify_expire_age_days(self, modify_expire_age_days :int = 7):
        self.__data__[self.data_filename_modify_expire_age_days_key] = int(modify_expire_age_days)
        return self

    def get_data_filename_modify_expire_age_days(self, modify_expire_age_days :int = None):
        if self.data_filename_modify_expire_age_days_key in self.__data__.keys(): return self.__data__[self.data_filename_modify_expire_age_days_key]
        elif modify_expire_age_days != None: return self.set_data_filename_modify_expire_age_days(int(modify_expire_age_days)).get_data_filename_modify_expire_age_days()
        else: return self.set_data_filename_modify_expire_age_days().get_data_filename_modify_expire_age_days()

    def set_data_filename_create_expire_age_days(self, create_expire_age_days :int = 30):
        self.__data__[self.data_filename_create_expire_age_days_key] = int(create_expire_age_days)
        return self

    def get_data_filename_create_expire_age_days(self, create_expire_age_days :int = None):
        if self.data_filename_create_expire_age_days_key in self.__data__.keys(): return self.__data__[self.data_filename_create_expire_age_days_key]
        elif create_expire_age_days != None: return self.set_data_filename_create_expire_age_days(int(create_expire_age_days)).get_data_filename_create_expire_age_days()
        else: return self.set_data_filename_create_expire_age_days().get_data_filename_create_expire_age_days()

    def file_created_age(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.is_file(filename): return datetime.now() - self.file_created_datetime(filename)
        else: return None

    def file_modified_age(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.is_file(filename): return datetime.now() - self.file_modified_datetime(filename)
        else: return None

    def file_accessed_age(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.is_file(filename): return datetime.now() - self.file_accessed_datetime(filename)
        else: return None

    def file_created_datetime(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.is_file(filename): return datetime.fromtimestamp(os.path.getctime(filename))
        else: return None

    def file_modified_datetime(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.is_file(filename): return datetime.fromtimestamp(os.path.getmtime(filename))
        else: return None

    def file_accessed_datetime(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.is_file(filename): return datetime.fromtimestamp(os.path.getatime(filename))
        else: return None

    def file_exists(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        return os.path.exists(filename)

    def is_file(self, filename :str = None):
        if filename == None: filename = self.get_data_filename()
        if self.file_exists(filename): return Path(filename).is_file
        else: return False

    def set_data_filename(self, data_filename :str = "data.dat"):
        self.__data__[self.data_filename_key] = str(data_filename)
        return self

    def get_data_filename(self, data_filename :str = None):
        if self.data_filename_key in self.__data__.keys(): return self.__data__[self.data_filename_key]
        elif data_filename != None: return self.set_data_filename(str(data_filename)).get_data_filename()
        else: return self.set_data_filename().get_data_filename()

    def set_random(self, random = random.Random()):
        self.__data__[self.__random_key__] = random
        self.__data__[self.__random_key__].seed()
        return self

    def get_random(self):
        if self.__random_key__ in self.__data__.keys(): return self.__data__[self.__random_key__]
        else: return self.set_random().get_random()

    def set_exit(self, exit :bool = False):
        self.__data__[self.__exit_key__] = bool(exit)
        return self

    def get_exit(self, exit :bool = None):
        if self.__exit_key__ in self.__data__.keys(): return bool(self.__data__[self.__exit_key__])
        elif exit != None: return self.set_exit(bool(exit)).get_exit()
        else: return self.set_exit().get_exit()

    def set_player_number(self, player_number :int = 1):
        self.__data__[self.__player_number_key__] = int(player_number)
        return self

    def get_player_number(self, player_number :int = None):
        if self.__player_number_key__ in self.__data__.keys(): return int(self.__data__[self.__player_number_key__])
        elif player_number != None: return self.set_player_number(int(player_number)).get_player_number()
        else: return self.set_player_number().get_player_number()

    def set_turn_number(self, turn_number :int = 0):
        self.__data__[self.__turn_number_key__] = int(turn_number)
        return self

    def get_turn_number(self, turn_number :int = None):
        if self.__turn_number_key__ in self.__data__.keys(): return int(self.__data__[self.__turn_number_key__])
        elif turn_number != None: return self.set_turn_number(int(turn_number)).get_turn_number()
        else: return self.set_turn_number().get_turn_number()

    def set_secret_word(self, secret_word :str = None):
        if secret_word == None: secret_word = self.get_random().choice([self.get_word_list().keys()])
        self.__data__[self.__secret_word_key__] = str(secret_word)
        return self

    def get_secret_word(self, secret_word :str = None):
        if self.__secret_word_key__ in self.__data__.keys(): return str(self.__data__[self.__secret_word_key__])
        elif secret_word != None: return self.set_secret_word(str(secret_word)).get_secret_word()
        else: return self.set_secret_word().get_secret_word()

    def set_word_list(self, word_list :dict = {}):
        self.__data__[self.__word_list_key__] = dict(word_list)
        return self

    def get_word_list(self, word_list :dict = None):
        if self.__word_list_key__ in self.__data__.keys(): return dict(self.__data__[self.__word_list_key__])
        elif word_list != None: return self.set_word_list(dict(word_list)).get_word_list()
        else: return self.set_word_list().get_word_list()

    def set_hint(self, index :int = None, hint :str = empty):
        if index == None: index = self.get_player_number()
        player = self.get_player(int(index))
        player[self.__hint_key__] = str(hint)
        self.set_player(index, player)
        return self

    def get_hint(self, index :int = None, hint :str = None):
        if index == None: index = self.get_player_number()
        if self.__hint_key__ in self.get_player(int(index)).keys(): return str(self.get_player(int(index))[self.__hint_key__])
        elif hint != None: return self.set_hint(index, str(hint)).get_hint()
        else: return self.set_hint(index).get_hint()

    def set_last_hint(self, index :int = None, last_hint :dict = None):
        if index == None: index = self.get_player_number()
        if last_hint == None:
            last_hint = {}
            last_hint[self.__puzzle_key__] = f"{underscore} " * len(self.get_secret_word())
            last_hint[self.__letters_key__] = empty
        player = self.get_player(int(index))
        player[self.__last_hint_key__] = dict(last_hint)
        self.set_player(index, player)
        return self

    def get_last_hint(self, index :int = None, last_hint :dict = None):
        if index == None: index = self.get_player_number()
        if self.__last_hint_key__ in self.get_player(int(index)).keys(): return dict(self.get_player(index)[self.__last_hint_key__])
        elif last_hint != None: return self.set_last_hint(dict(last_hint)).get_last_hint()
        else: return self.set_last_hint().get_last_hint()

    def set_guess(self, guess :str = empty):
        self.__data__[self.__guess_key__] = str(guess)
        return self

    def get_guess(self, guess :str = None):
        if self.__guess_key__ in self.__data__.keys(): return str(self.__data__[self.__guess_key__])
        elif guess != None: return self.set_guess(str(guess)).get_guess()
        else: return self.set_guess().get_guess()

    def set_player(self, index :int = None, player :dict = {}):
        if index == None: index = self.get_player_number()
        if (index < 1) or (index > self.get_number_of_players(noAuto=True)):  raise IndexError(f"index {index} attempted out of {self.get_number_of_players()}!")
        players = self.get_players()
        players[int(index)] = dict(player)
        self.set_players(players)
        return self

    def get_player(self, index :int = None, player :dict = None):
        if index == None: index = self.get_player_number()
        if int(index) in self.get_players().keys(): return dict(self.get_players()[int(index)])
        elif player != None: return self.set_player(index, dict(player)).get_player()
        else: return self.set_player(index).get_player()

    def set_number_of_players(self, number_of_players :int = 1):
        self.__data__[self.__number_of_players_key__] = int(number_of_players)
        for index in range(1, number_of_players + 1): self.set_player(index)
        self.set_player_number()
        return self

    def get_number_of_players(self, number_of_players :int = None, noAuto = False):
        if self.__number_of_players_key__ in self.__data__.keys(): return int(self.__data__[self.__number_of_players_key__])
        elif (number_of_players != None) and noAuto: return int(number_of_players)
        elif number_of_players != None: return self.set_number_of_players(int(number_of_players)).get_number_of_players()
        elif noAuto: return 0
        else: return self.set_number_of_players().get_number_of_players()

    def set_max_turns(self, max_turns :int = 0):
        self.__data__[self.__max_turns_key__] = int(max_turns)
        return self

    def get_max_turns(self, max_turns :int = None):
        if self.__max_turns_key__ in self.__data__.keys(): return int(self.__data__[self.__max_turns_key__])
        elif max_turns != None: return self.set_max_turns(int(max_turns)).get_max_turns()
        else: return self.set_max_turns().get_max_turns()

    def set_super_hint_frequency(self, super_hint_frequency :int = 0):
        self.__data__[self.__super_hint_frequency_key__] = int(super_hint_frequency)
        return self

    def get_super_hint_frequency(self, super_hint_frequency :int = None):
        if self.__super_hint_frequency_key__ in self.__data__.keys(): return int(self.__data__[self.__super_hint_frequency_key__])
        elif super_hint_frequency != None: return self.set_super_hint_frequency(int(super_hint_frequency)).get_super_hint_frequency()
        else: return self.set_super_hint_frequency().get_super_hint_frequency()

    def set_players(self, players :dict = {}):
        self.__data__[self.__players_key__] = dict(players)
        return self

    def get_players(self, players :dict = None):
        if self.__players_key__ in self.__data__.keys(): return dict(self.__data__[self.__players_key__])
        elif players != None:  return self.set_players(dict(players)).get_players()
        else: return self.set_players().get_players()

    def set_multiplayer_init(self, multiplayer_init :bool = False):
        self.__data__[self.__multiplayer_init_key__] = bool(multiplayer_init)
        return self

    def get_multiplayer_init(self, multiplayer_init :bool = None):
        if self.__multiplayer_init_key__ in self.__data__.keys(): return bool(self.__data__[self.__multiplayer_init_key__])
        elif multiplayer_init != None:  return self.set_multiplayer_init(bool(multiplayer_init)).get_multiplayer_init()
        else: return self.set_multiplayer_init().get_multiplayer_init()

    def set_track(self, track :list = []):
        self.__data__[self.__track_key__] = list(track)
        return self

    def get_track(self, track :list = None):
        if self.__track_key__ in self.__data__.keys(): return list(self.__data__[self.__track_key__])
        elif track != None:  return self.set_track(list(track)).get_track()
        else: return self.set_track().get_track()

    def set_lost(self, index :int = None, lost :bool = False):
        if index == None: index = self.get_player_number()
        player = self.get_player(index)
        player[self.__lost_key__] = bool(lost)
        self.set_player(index, player)
        return self

    def get_lost(self, index : int = None, lost :bool = None):
        if index == None: index = self.get_player_number()
        if self.__lost_key__ in self.get_player(index).keys(): return self.get_player(index)[self.__lost_key__]
        elif lost != None: return self.set_lost(index, lost).get_lost(index)
        else: return self.set_lost(index).get_lost(index)

    def does_guess_not_equal_secret_word(self):
        return self.get_secret_word() != self.get_guess()

    def is_next_turn(self):
        return self.does_guess_not_equal_secret_word() and\
            (
                not self.get_exit() and
                (self.get_max_turns() < 1) or\
                (
                    (self.get_max_turns() >= 1) and\
                    (self.get_turn_number() < self.get_max_turns())
                )
            )

    def game_win_message(self):
        if self.get_number_of_players() > 1: print(f"Congratulations Player {self.get_player_number()}, you guessed the word!")
        else: print("Congratulations, you guessed the word!")
        print(f"You did it in {self.get_turn_number() + 1} guesses.")

    def get_number_of_active_players(self):
        count = 0
        for index in range(1, self.get_number_of_players() + 1):
            if not self.get_lost(index): count += 1
        return count

    def init_game(self, exit :bool = False):
        self.set_exit(bool(exit))
        self.load_word_list()

    def request_enter_to_continue(self):
        try:
            input("Press enter to continue.")
        except KeyboardInterrupt:
            print()
            print("if you wish to exit please do so at your turns response!")

    def request_valid_number_of_players(self, max_tries :int = 3, max_tries_default :int = 1, ctrl_c_default :int = 0):
        value = -1
        tries = 0
        while (value < 1) and (tries < max_tries):
            try:
                value = int(input("How many players? "))
            except ValueError:
                value = -1
            except KeyboardInterrupt:
                print()
                return ctrl_c_default
            finally:
                tries += 1
            if (value < 1) and (tries < max_tries): print("Please enter a positive number of players!")
        if (value < 1) and (tries == max_tries):
            print(f"I will set the number of players to {max_tries_default}.")
            value = max_tries_default
        return value

    def request_valid_number_of_turns(self, max_tries :int = 3, max_tries_default :int = 0, ctrl_c_default :int = -1):
        value = -2
        tries = 0
        while (value < 0) and (tries < max_tries):
            try:
                value = int(input("How many guesses do you want (0 is unlimited)? "))
            except ValueError:
                value = -2
            except KeyboardInterrupt:
                print()
                return ctrl_c_default
            finally:
                tries += 1
            if (value < 0) and (tries < max_tries): print("Please enter a number of guesses!")
        if (value < 0) and (tries == max_tries):
            print(f"I will set the number of guesses to {max_tries_default}.")
            value = max_tries_default
        return value

    def request_confirm_option_super_hints(self, tries : int = 0, max_tries :int = 3, max_tries_default :bool = True, ctrl_c_default :bool = False):
        true_set = ["y", "yes", empty]
        false_set = ["n", "no"]
        if self.get_max_turns() != 1:
            while tries < max_tries:
                try:
                    reply = str(input("Do you want super hints [(y)es/(n)o]? ")).lower()
                    if reply in true_set:  return True
                    elif reply in false_set:  return False
                except KeyboardInterrupt:
                    print()
                    return ctrl_c_default
                finally:
                    tries += 1
                if (tries < max_tries): print("Please indicate yes or no!")
            return max_tries_default
        else: return False

    def request_confirm_play_again(self, max_tries :int = 3, max_tries_default :bool = True, ctrl_c_default :bool = False):
        true_set = ["y", "yes", empty]
        false_set = ["n", "no"]
        tries = 0
        while tries < max_tries:
            try:
                reply = str(input("play again [(y)es/(n)o]? ")).lower()
                if reply in true_set:  return True
                elif reply in false_set:  return False
            except KeyboardInterrupt:
                print()
                return ctrl_c_default
            finally:
                tries += 1
            if (tries < max_tries): print("Please indicate yes or no!")
        return max_tries_default

    def request_valid_super_hints(self, max_tries :int = 3, max_tries_default :int = 0, ctrl_c_default :int = -1):
        super_hints = 0
        tries = 0
        if self.request_confirm_option_super_hints(tries, max_tries):
            value = -1
            while (value < 0 or ((self.get_max_turns()>2 and (value >= (self.get_max_turns()-1))))) and (tries < max_tries):
                try:
                    if self.get_max_turns() > 0:
                        value = int(input("How many super hints, including the last hit, do you want as a minimum? "))
                    else:
                        value = int(input("How often do you want super hints? "))
                except ValueError:
                    value = -1
                except KeyboardInterrupt:
                    print()
                    return ctrl_c_default
                finally:
                    tries += 1
                if (value < 0 or (value > self.get_max_turns())) and (tries < max_tries): print("Please enter a number of super hints!")
            if (value < 0 or (value > self.get_max_turns())) and (tries == max_tries):
                print(f"I will set the number of super hints to {max_tries_default}.")
                super_hints = max_tries_default
            else:
                if (self.get_max_turns() > 0) and (value > 0): super_hints = int(self.get_max_turns() / value)
                else: super_hints = value 
        return super_hints

    def request_confirm_quit(self, max_tries :int = 2, max_tries_default :bool = False, ctrl_c_default :bool = True):
        true_set = ["y", "yes", empty]
        false_set = ["n", "no"]
        tries = 0
        while tries < max_tries:
            try:
                reply = str(input("do you wish to quit [(y)es/(n)o]? ")).lower()
                if reply in true_set:  return True
                elif reply in false_set:  return False
            except KeyboardInterrupt:
                print()
                return ctrl_c_default
            finally:
                tries += 1
            if (tries < max_tries): print("Please indicate yes or no!")
        return max_tries_default

    def request_confirm_forfeit(self, max_tries :int = 2, max_tries_default :bool = False, ctrl_c_default :bool = True):
        true_set = ["y", "yes", empty]
        false_set = ["n", "no"]
        tries = 0
        while tries < max_tries:
            try:
                reply = str(input("do you wish to forfiet [(y)es/(n)o]? ")).lower()
                if reply in true_set:  return True
                elif reply in false_set:  return False
            except KeyboardInterrupt:
                print()
                self.set_exit(self.request_confirm_quit())
                return ctrl_c_default
            finally:
                tries += 1
            if (tries < max_tries): print("Please indicate yes or no!")
        return max_tries_default

    def request_valid_guess(self):
        answered = False
        while not answered:
            try:
                return input("what is your guess? ")
            except KeyboardInterrupt:
                print()
                if self.get_number_of_active_players() > 1:
                    self.set_lost(lost = self.request_confirm_forfeit())
                else:
                    self.set_lost(lost = self.request_confirm_quit())
                    self.set_exit(self.get_lost())
                answered = True
        return self.get_hint()

    def configure_game(self):
        self.set_number_of_players(self.request_valid_number_of_players())
        if self.get_number_of_players() > 0:
            self.set_max_turns(self.request_valid_number_of_turns())
            if self.get_max_turns() > -1:
                self.set_super_hint_frequency(self.request_valid_super_hints())

    def play_turn(self):
        if not self.get_lost():
            if self.get_number_of_players() > 1:
                if self.get_multiplayer_init(): self.request_enter_to_continue()
                self.set_multiplayer_init(True)
                print("\n" * 5)
                os.system("cls")
                print(f"Player {self.get_player_number()} Turn {self.get_turn_number() + 1}")
                self.request_enter_to_continue()
            else: print(f"Turn {self.get_turn_number() + 1}")
            if (self.get_max_turns() >= 1) and (self.get_max_turns()-self.get_turn_number() == 1): print("last chance!")
            elif (self.get_max_turns() >= 1) and (self.get_turn_number() < (self.get_max_turns())): print(f"{self.get_max_turns()-self.get_turn_number() - 1} turns remaining after this turn!")
            print(f"Your hint is {self.get_hint()}.")
            if (self.get_max_turns() > 1) and (self.get_max_turns()-self.get_turn_number() == 1): print(f"Your last hint is {self.get_last_hint()[self.__puzzle_key__]}with \"{self.get_last_hint()[self.__letters_key__]}\" letters")
            elif ((self.get_turn_number() + 1) > 0) and (self.get_super_hint_frequency() >= 1):
                if (self.get_turn_number() >= 1) and (((self.get_turn_number() + 1) % self.get_super_hint_frequency()) == 0): print(f"Your super hint is {self.get_last_hint()[self.__puzzle_key__]}with \"{self.get_last_hint()[self.__letters_key__]}\" letters")
            #have the user make a guess
            self.set_guess(self.request_valid_guess())
            if not self.get_lost() and not self.get_exit():
                #Check to see if the guess is the same length as the secret word
                if len(self.get_secret_word()) != len(self.get_guess()):
                    #print a message when they're not the same
                    print("Your guess must have the same number of letters as the secrete word!\n")
                    self.set_hint(hint = f"{underscore} " * len(self.get_secret_word()))
                #Otherwise figure out the hint
                else:
                    self.set_track()
                    for index in range(len(self.get_guess())):
                        track = self.get_track()
                        track.append(self.get_secret_word()[index])
                        if self.get_guess()[index] == self.get_secret_word()[index]:
                            track.pop()
                            track.append(underscore)
                        self.set_track(track)
                    self.set_hint()
                    #for each letter in the guess
                    for index in range(len(self.get_guess())):
                        #check if the letter at this location in the guess is the same as this same location in the secret word
                        if self.get_guess()[index] == self.get_secret_word()[index]:
                            #print out the letter capitalized
                            self.set_hint(hint = f"{self.get_hint()}{self.get_guess()[index].upper()} ")
                        #check if the letter is in the secret word but is in the wrong place\
                        elif self.get_guess()[index] in self.get_track():
                            track = self.get_track()
                            tIndex = track.index(self.get_guess()[index])
                            track.pop(tIndex)
                            track.insert(tIndex, underscore)
                            self.set_track(track)
                            #print out the letter in lower case
                            self.set_hint(hint = f"{self.get_hint()}{self.get_guess()[index].lower()} ")
                        #otherwise, the letter isn't in the word at all
                        else:
                            #so print out an underscore
                            self.set_hint(hint = f"{self.get_hint()}{underscore} ")
                    last_hint = self.get_last_hint()
                    new_puzzle = empty
                    new_letters = str(last_hint[self.__letters_key__])
                    for index in range(len(self.get_secret_word())):
                        if (self.get_hint()[index * 2] != underscore) and (last_hint[self.__puzzle_key__][index * 2] == underscore):
                            if (self.get_hint()[index * 2].upper() == self.get_hint()[index * 2]):
                                #add new if upper
                                new_puzzle = f"{new_puzzle}{self.get_hint()[index * 2]} "
                                if self.get_hint()[index * 2].lower() in new_letters:
                                    #remove from letters is present
                                    new_letters = new_letters.replace(self.get_hint()[index * 2].lower(), underscore, 1)
                            else:
                                #keep old
                                new_puzzle = f"{new_puzzle}{last_hint[self.__puzzle_key__][index * 2]} "
                        elif (self.get_hint()[index * 2] != underscore):
                            #keep old
                            new_puzzle = f"{new_puzzle}{last_hint[self.__puzzle_key__][index * 2]} "
                        else:
                            #keep old
                            new_puzzle = f"{new_puzzle}{last_hint[self.__puzzle_key__][index * 2]} "
                        #add new unknown location letter to letters
                        new_letters = f"{new_letters}{self.get_hint()[index * 2]}"
                    last_hint[self.__puzzle_key__] = new_puzzle
                    # rebuild letters based on available to be found and which instance the old letters was (removing extra old letters over teh available to be found)
                    last_hint[self.__letters_key__] = empty
                    for index in range(len(new_letters)):
                        if ((self.get_secret_word().count(new_letters[index]) - new_puzzle.count(new_letters[index].upper())) > 0) and (new_letters[0:index+1].count(new_letters[index]) <= (self.get_secret_word().count(new_letters[index]) - new_puzzle.count(new_letters[index].upper()))): last_hint[self.__letters_key__] = f"{last_hint[self.__letters_key__]}{new_letters[index]}"
                    self.set_last_hint(last_hint = last_hint)
        #make sure to increment the guess counter
        if self.get_secret_word() != self.get_guess():
            self.set_player_number(self.get_player_number() + 1)
            if self.get_player_number() > self.get_number_of_players():
                self.set_player_number()
                self.set_turn_number(self.get_turn_number() + 1)
        return self

    def play_game(self):
        clear_screen()
        self.configure_game()
        if (self.get_number_of_players() > 0) and (self.get_max_turns() > -1):
            #Store a secret word
            self.set_secret_word()
            for index in range(1, self.get_number_of_players() + 1):
                self.set_hint(index, f"{underscore} " * len(self.get_secret_word()))
                self.set_last_hint(index)
            #Create a variable to store the user's guess
            self.set_guess()
            #Create a variable to count the number of guesses
            self.set_turn_number()
            self.set_multiplayer_init()
            #Continue looping as long as the guess is not correct
            while self.is_next_turn(): self.play_turn()
            #when you get out here, that means they got the secret word. print out a message to say how many guesses it took
            if not self.get_exit() and not self.get_lost() and (self.get_secret_word() == self.get_guess()): self.game_win_message()
            elif not self.get_exit(): print("Better luck next time!")
            if not self.get_exit():
                if not (self.request_confirm_play_again()):
                    self.set_exit(True)
                    print("Goodbye!")
        else: self.set_exit(True)
        return self

main()
