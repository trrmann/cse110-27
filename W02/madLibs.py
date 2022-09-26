"""
    filname:  madLibs.py
    inputs:  a string to represent an adjective from the user to the question "Please enter an adjective:  "
    inputs:  a string to represent an animal from the user to the question "Please enter a type of animal:  "
    inputs:  a string to represent a verb from the user to the question "Please enter a verb:  "
    inputs:  a string to represent an exclamation from the user to the question "Please enter an exclamation:  "
    inputs:  a string to represent a second verb from the user to the question "Please enter a second verb:  "
    inputs:  a string to represent a third verb from the user to the question "Please enter a third verb:  "
    output:  a formated display of the Mad Lib for the given input as below:
        The other day, I was really in trouble. It all started when I saw a very
        [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
        I could think to do was to [verb] over and over. Miraculously,
        that caused it to stop, but not before it tried to [verb]
        right in front of my family.
    additional requirements for output:
        1)  Make it so that the "exclamation" word is automatically capitalized, because it starts a new sentence.
        2)  Extra whitespace before or after punctuation is not allowed.
    ref:  https://www.digitalocean.com/community/tutorials/python-trim-string-rstrip-lstrip-strip for trimming the strings.
    author:  Tracy Mann
    version:  1.0
    date:  9/16/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
    version 1.1:
        date:  9/16/2022
            1)  add more to the story, including several more words that will be filled in.
                inputs:  a string to represent a noun from the user to the question "Please enter a noun:  "
                inputs:  a string to represent an adverb from the user to the question "Please enter an adverb:  "
                inputs:  a string to represent a forth verb from the user to the question "Please enter a forth verb:  "
            2)  validate if no string is provided.  in the event that nothing is provided, randomly select a value from a list.
            
            additional requirements for output:
                1)  when a sentence that has an "a" or "an" in front of the word, determine and display the appropiate appropriate article.
            output layout update:
                The other day, I was really in trouble. It all started when I saw a very
                [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
                I could think to do was to [verb] over and over. Miraculously,
                that caused it to stop, but not before it tried to [verb]
                right in front of my family.  Just then, to top the day off, out of the blue,
                [a/an] [noun] [adverb] [verb] us all.
            ref:  https://www.w3schools.com/python/python_conditions.asp for python conditions
                  https://www.golinuxcloud.com/python-line-continuation/ line continuation
                  https://stackoverflow.com/questions/8848294/how-to-get-char-from-string-by-index for additional string manipulation
                  https://www.w3schools.com/python/python_lists.asp for list information
                  https://docs.python.org/3/library/random.html for random selection
    
    submission comment:  I believe this submission has earned a Made it my own.  I have met every requirement in the ruberic including looking up the solution to making sure that white space around and entry is removed.  I have also not only added more words and sentence structure to the output, but also verified entries are not empty.  In the event that an entry is empty the program will randomly select from a list of valid options to allow the output to read better.
"""

#added in version 1.1
from random import seed
#added in version 1.1
from random import choice
adjective = input("Please enter an adjective:  ")
animal = input("Please enter a type of animal:  ")
first_verb = input("Please enter a verb:  ")
exclamation = input("Please enter an exclamation:  ")
second_verb = input("Please enter a second verb:  ")
third_verb = input("Please enter a third verb:  ")
#added in version 1.1
noun = input("Please enter a noun:  ")
#added in version 1.1
adverb = input("Please enter an adverb:  ")
#added in version 1.1
forth_verb = input("Please enter a forth verb:  ")
#added in version 1.1 to seed random numbers
seed()
#added in version 1.1
if adjective == "":adjective = choice(["happy", "tired", "sad", "energetic"])
#added in version 1.1
if animal == "":animal = choice(["zebra", "snail", "dog", "cat"])
#added in version 1.1
if first_verb == "":first_verb = choice(["sneeze", "yell", "sneak", "lumber"])
#added in version 1.1
if exclamation == "":exclamation = choice(["hooray", "oh no", "stop", "hey"])
#added in version 1.1
if second_verb == "":second_verb = choice(["read", "sing", "pray", "yell"])
#added in version 1.1
if third_verb == "":third_verb = choice(["drive", "skip", "bolt", "run"])
#added in version 1.1
if noun == "":noun = choice(["elephant", "alligator", "lion", "tiger"])
#added in version 1.1
if adverb == "":adverb = choice(["angrily", "happily", "aggresively", "valiently"])
#added in version 1.1
if forth_verb == "":forth_verb = choice(["charged", "ate", "challenged", "attacked"])
#added in version 1.1 - to make this Unicode safe
noun.encode('utf-8')
#added in version 1.1
if noun[0].lower() in ["a","e","i","o","u"]:
    article = "an"
else:
    article = "a"
#changed in version 1.1
#madLib = f"The other day, I was really in trouble. It all started when I saw a very\n\
#{adjective.strip()} {animal.strip()} {first_verb.strip()} down the hallway. \"{exclamation.strip().capitalize()}!\" I yelled. But all\n\
#I could think to do was to {second_verb.strip()} over and over. Miraculously,\n\
#that caused it to stop, but not before it tried to {third_verb.strip()}\n\
#right in front of my family.\n"
madLib = f"The other day, I was really in trouble. It all started when I saw a very\n\
{adjective.strip()} {animal.strip()} {first_verb.strip()} down the hallway. \"{exclamation.strip().capitalize()}!\" I yelled. But all\n\
I could think to do was to {second_verb.strip()} over and over. Miraculously,\n\
that caused it to stop, but not before it tried to {third_verb.strip()}\n\
right in front of my family.  Just then, to top the day off, out of the blue,\n\
{article} {noun.strip()} {adverb.strip()} {forth_verb.strip()} us all.\n"
print(f"\nYour story is:\n\n{madLib}\n")