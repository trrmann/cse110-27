#
# favoriteColor.py
#   inputs:  a string to represent a response from the user to the question "What is your Favorite Color?"
#   conditional input:  if the original response from the user is a string that does not match a known color string
#       a prompt requesting to validate by yes or no entry that this is a color.
#   outputs:  a statement that of what the user responded as a favorite color or a statement that the favorite color
#       is not known.
#   inputs:  a string to represent a response from the user to the question "What is your Favorite Color?"
#   process:  will validate the input is a known color, if it is not then request validation from the user.  if it
#       is not a valid color then retry to get the favorite color up to 3 times.  once the color is determine valid
#       or retries exceeded report either the favorite color or that it is unknown.
#   author:  Tracy Mann
#   version:  1.0
#   date:  9/12/2022
#   class:  CSE110
#   teacher:  Brother Wilson
#   section:  27
#   ref:  https://www.w3schools.com/python/default.asp for language operations and available functions.
#
hasAnswer = False
attempt = 0
while (not hasAnswer):
    knownColor = False
    attempt = attempt + 1
    favoriteColor = input("What is your favorite color?  ")
    if favoriteColor.lower() in ["red", "green", "blue", "yellow", "orange", "purple", "black", "white", "pink", "tan", "brown"]:
        knownColor = True
        hasAnswer = True
    #end if favoriteColor
    if knownColor in [False]:
        reply = input("Are you sure that " + favoriteColor + " is a color(Yes/No)?  ")
        if reply in ["Yes", "yes", "y", "Y"]:
            knownColor = True
            hasAnswer = True
        else:
            knownColor = False
            hasAnswer = False
            if (attempt > 2):
                hasAnswer = True
            #end if (attempt > 2)
        #end if reply
    #end if knownColor
#end While not hasAnswer
if knownColor in [True]:
    print("Your favorite color is " + favoriteColor + "!")
else:
    print("I do not know your favorite color!")
#end if knownColor