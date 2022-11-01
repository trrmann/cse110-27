import random
import os

empty = ""
underscore = "_"
default_list = ["dog", "cat", "pig", "cow", "ape", "sow", "sheep", "sleep", "house", "horse", "apple"]

def clear_screen():
    print("\n" * 5)
    os.system("cls")

def main():
    game = Wordle()
    while not game.get_exit(): game.play_game()

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
    __data__ = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.__data__ = {}
        self.init_game()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(className={self.className}, testName={self.testName}, numberOfFunctionsInDictionary={len(self.functionDictionary)}, numberOfTestCases={len(self.testCases)})"

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
        if secret_word == None: secret_word = self.get_random().choice(self.get_word_list())
        self.__data__[self.__secret_word_key__] = str(secret_word)
        return self

    def get_secret_word(self, secret_word :str = None):
        if self.__secret_word_key__ in self.__data__.keys(): return str(self.__data__[self.__secret_word_key__])
        elif secret_word != None: return self.set_secret_word(str(secret_word)).get_secret_word()
        else: return self.set_secret_word().get_secret_word()

    def set_word_list(self, word_list :list = []):
        self.__data__[self.__word_list_key__] = list(word_list)
        return self

    def get_word_list(self, word_list :list = None):
        if self.__word_list_key__ in self.__data__.keys(): return list(self.__data__[self.__word_list_key__])
        elif word_list != None: return self.set_word_list(list(word_list)).get_word_list()
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
        self.set_word_list(default_list)

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
            while (value < 0 or (value > self.get_max_turns())) and (tries < max_tries):
                try:
                    if self.get_max_turns() > 0:
                        value = int(input("How many super hints, including the last hit, do you want as a minimum? ")) + 1
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
                if self.get_max_turns() > 0:
                    if value == self.get_max_turns(): super_hints = 1
                    elif value > 0: super_hints = int(self.get_max_turns() / super_hints)
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
            elif (self.get_max_turns() >= 1) and (self.get_turn_number() < (self.get_max_turns())): print(f"{self.get_max_turns()-self.get_turn_number()} turns remaining!")
            print(f"Your hint is {self.get_hint()}.")
            if (self.get_max_turns() >= 1) and (self.get_max_turns()-self.get_turn_number() == 1): print(f"Your last hint is {self.get_last_hint()[self.__puzzle_key__]}with \"{self.get_last_hint()[self.__letters_key__]}\" letters")
            elif ((self.get_turn_number() + 1) > 0) and (self.get_super_hint_frequency() >= 1):
                if (((self.get_turn_number() + 1) % self.get_super_hint_frequency()) == 0): print(f"Your super hint is {self.get_last_hint()[self.__puzzle_key__]}with \"{self.get_last_hint()[self.__letters_key__]}\" letters")
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
