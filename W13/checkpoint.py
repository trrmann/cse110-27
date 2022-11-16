#! python
def display_regular(msg:str):
    print(msg)

def display_uppercase(msg:str):
    print(msg.upper())

def display_lowercase(msg:str):
    print(msg.lower())

message = input("What is your message? ")
display_regular(message)
display_uppercase(message)
display_lowercase(message)