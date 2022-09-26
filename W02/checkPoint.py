"""
    filname:  checkPoint.py
    inputs:  a string to represent the first name from the user to the question "What is your first name?"
    inputs:  a string to represent the last name from the user to the question "What is your last name?"
    output:  a statement that of what the user responded as a full name in the form of Last Name comma First Name then Last Name again.
    author:  Tracy Mann
    version:  1.0
    date:  9/15/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
"""

first_name = input("What is your first name?")
last_name = input("What is your last name?")
message = f"\nYour name is {last_name.capitalize()}, {first_name.capitalize()} {last_name.capitalize()}"
print(message)