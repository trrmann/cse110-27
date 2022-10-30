import random
import os

r = random.Random()
r.seed()

empty = ""
underscore = "_"
exit_key = "exit"
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
turn_key = "turn"
track_key = "track"

data = {}
data[exit_key] = False
while not data[exit_key]:
    print("\n" * 5)
    os.system("cls")
    data[number_of_players_key] = int(input("How many players? "))
    data[max_turns_key] = int(input("How many guesses do you want? "))
    data[super_hint_frequency_key] = 3
    data[players_key] = {}
    for index in range(1,data[number_of_players_key] + 1): data[players_key][index] = {}
    data[player_number_key] = 1
    #Store a secret word
    data[secret_word_key] = r.choice(["dog", "cat", "pig", "cow", "ape", "sow", "sheep", "sleep", "house", "horse", "apple"])
    for index in range(1,data[number_of_players_key] + 1): data[players_key][index][hint_key] = f"{underscore} " * len(data[secret_word_key])
    for index in range(1,data[number_of_players_key] + 1): data[players_key][index][last_hint_key] = { puzzle_key : f"{underscore} " * len(data[secret_word_key]), letters_key : ""}
    #Create a variable to store the user's guess
    data[guess_key] = empty
    #Create a variable to count the number of guesses
    data[turn_key] = 0
    data[multiplayer_init_key] = False
    #Continue looping as long as the guess is not correct
    while (data[secret_word_key] != data[guess_key]) and ((data[max_turns_key] < 1) or ((data[max_turns_key] >= 1) and (data[turn_key] < data[max_turns_key]))):
        if data[number_of_players_key] > 1:
            if data[multiplayer_init_key]:
                input("Press enter to continue.")
            data[multiplayer_init_key] = True
            print("\n" * 5)
            os.system("cls")
            print(f"Player {data[player_number_key]} Turn {data[turn_key] + 1}")
            input("Press enter to continue.")
        else:
            print(f"Turn {data[turn_key] + 1}")
        if (data[max_turns_key] >= 1) and (data[max_turns_key]-data[turn_key] == 1):
            print("last chance!")
        elif (data[max_turns_key] >= 1) and (data[turn_key] < (data[max_turns_key])):
            print(f"{data[max_turns_key]-data[turn_key]} turns remaining!")
        print(f"Your hint is {data[players_key][data[player_number_key]][hint_key]}.")
        if (data[max_turns_key] >= 1) and (data[max_turns_key]-data[turn_key] == 1): print(f"Your last hint is {data[players_key][data[player_number_key]][last_hint_key][puzzle_key]}with \"{data[players_key][data[player_number_key]][last_hint_key][letters_key]}\" letters")
        elif (data[turn_key] > 1) and (((data[turn_key] + 1) % data[super_hint_frequency_key]) == 0): print(f"Your super hint is {data[players_key][data[player_number_key]][last_hint_key][puzzle_key]}with \"{data[players_key][data[player_number_key]][last_hint_key][letters_key]}\" letters")
        #have the user make a guess
        data[guess_key] = input("what is your guess? ")
        #Check to see if the guess is the same length as the secret word
        if len(data[secret_word_key]) != len(data[guess_key]):
            #print a message when they're not the same
            print("Your guess must have the same number of letters as the secrete word!\n")
            data[players_key][data[player_number_key]][hint_key] = f"{underscore} " * len(data[secret_word_key])        
        #Otherwise figure out the hint
        else:
            data[track_key] = []
            for index in range(len(data[guess_key])):
                data[track_key].append(data[secret_word_key][index])
                if data[guess_key][index] == data[secret_word_key][index]:
                    data[track_key].pop()
                    data[track_key].append(underscore)
            data[players_key][data[player_number_key]][hint_key] = empty
            #for each letter in the guess
            for index in range(len(data[guess_key])):
                #check if the letter at this location in the guess is the same as this same location in the secret word
                if data[guess_key][index] == data[secret_word_key][index]:
                    #print out the letter capitalized
                    data[players_key][data[player_number_key]][hint_key] = f"{data[players_key][data[player_number_key]][hint_key]}{data[guess_key][index].upper()} "
                #check if the letter is in the secret word but is in the wrong place\
                elif data[guess_key][index] in data[track_key]:
                    tIndex = data[track_key].index(data[guess_key][index])
                    data[track_key].pop(tIndex)
                    data[track_key].insert(tIndex, underscore)
                    #print out the letter in lower case
                    data[players_key][data[player_number_key]][hint_key] = f"{data[players_key][data[player_number_key]][hint_key]}{data[guess_key][index].lower()} "
                #otherwise, the letter isn't in the word at all
                else:
                    #so print out an underscore
                    data[players_key][data[player_number_key]][hint_key] = f"{data[players_key][data[player_number_key]][hint_key]}{underscore} "            
            new_puzzle = ""
            new_letters = str(data[players_key][data[player_number_key]][last_hint_key][letters_key])
            for index in range(len(data[secret_word_key])):
                if (data[players_key][data[player_number_key]][hint_key][index * 2] != underscore) and (data[players_key][data[player_number_key]][last_hint_key][puzzle_key][index * 2] == underscore):
                    if (data[players_key][data[player_number_key]][hint_key][index * 2].upper() == data[players_key][data[player_number_key]][hint_key][index * 2]):
                        #add new if upper
                        new_puzzle = f"{new_puzzle}{data[players_key][data[player_number_key]][hint_key][index * 2]} "
                        if data[players_key][data[player_number_key]][hint_key][index * 2].lower() in new_letters:
                            #remove from letters is present
                            new_letters = new_letters.replace(data[players_key][data[player_number_key]][hint_key][index * 2].lower(), underscore, 1)
                    else:
                        #keep old
                        new_puzzle = f"{new_puzzle}{data[players_key][data[player_number_key]][last_hint_key][puzzle_key][index * 2]} "
                elif (data[players_key][data[player_number_key]][hint_key][index * 2] != underscore):
                    #keep old
                    new_puzzle = f"{new_puzzle}{data[players_key][data[player_number_key]][last_hint_key][puzzle_key][index * 2]} "
                else:
                    #keep old
                    new_puzzle = f"{new_puzzle}{data[players_key][data[player_number_key]][last_hint_key][puzzle_key][index * 2]} "
                #add new unknown location letter to letters
                new_letters = f"{new_letters}{data[players_key][data[player_number_key]][hint_key][index * 2]}"
            data[players_key][data[player_number_key]][last_hint_key][puzzle_key] = new_puzzle
            # rebuild letters based on available to be found and which instance the old letters was (removing extra old letters over teh available to be found)
            data[players_key][data[player_number_key]][last_hint_key][letters_key] = ""
            for index in range(len(new_letters)):
                if ((data[secret_word_key].count(new_letters[index]) - new_puzzle.count(new_letters[index].upper())) > 0) and (new_letters[0:index+1].count(new_letters[index]) <= (data[secret_word_key].count(new_letters[index]) - new_puzzle.count(new_letters[index].upper()))): data[players_key][data[player_number_key]][last_hint_key][letters_key] = f"{data[players_key][data[player_number_key]][last_hint_key][letters_key]}{new_letters[index]}"
        #make sure to increment the guess counter
        if data[secret_word_key] != data[guess_key]:
            data[player_number_key] += 1
            if data[player_number_key] > data[number_of_players_key]:
                data[player_number_key] = 1
                data[turn_key] += 1
    #when you get out here, that means they got the secret word. print out a message to say how many guesses it took
    if(data[secret_word_key] == data[guess_key]):
        if data[number_of_players_key] > 1:
            print(f"Congratulations Player {data[player_number_key]}, you guessed the word!")
        else:
            print("Congratulations, you guessed the word!")
        print(f"You did it in {data[turn_key] + 1} guesses.")
    else:
        print("Better luck next time!")
    if not (input("play again [(y)es/(n)o]?").lower() in ["y", "yes"]):
        data[exit_key] = True
