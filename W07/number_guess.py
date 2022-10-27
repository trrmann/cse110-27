import random

exit = False

while not exit:
    #magic_number = int(input("What is the magic number? "))
    magic_number = random.randint(1, 100)
    guess = magic_number - 1
    counter = 1
    while not(guess == magic_number):
        guess = int(input("What is your guess? "))
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        else:
            print(f"You guessed it in {counter} tries!")
            replay_option = input("Do you wish to play again[(Y)es/(N)o]? ")
            if replay_option.lower() in ["n", "no", ""]: exit = True
        counter = counter + 1
