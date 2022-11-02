print("This is line one.  ", end="")
print("This is line two.")

word = "Commitment"
for letter in word:
    letter = letter.lower()
    if letter == "m":  letter = letter.upper()
    print(letter)

print()

cap = input("what letter do you wish to capitalize? ").lower()
for letter in word:
    letter = letter.lower()
    if letter == cap:  letter = letter.upper()
    print(letter, end="")

print("\n")

cap = input("what letter do you wish to hide? ").lower()
for letter in word:
    letter = letter.lower()
    if letter == cap:  letter = "_"
    print(letter, end="")

print("\n")

first_name = "Brigham"
for i, letter in enumerate(first_name):  print(f"The letter {letter} is at position {i}.")

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

frequency = int(input("Please enter a number: "))

for i, letter in enumerate(quote.lower()):
    if i % frequency == 0:  letter = letter.upper()
    print(letter, end="")

print("\n")

again = "yes"
while not(again in ["no", "n", ""]):
    frequency = int(input("Please enter a number: "))
    for i, letter in enumerate(quote.lower()):
        if i % frequency == 0:  letter = letter.upper()
        print(letter, end="")
    print("\n")
    again = input("again[((y)es/(n)o]? ")
