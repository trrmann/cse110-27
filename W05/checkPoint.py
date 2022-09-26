first_number = int(input("What is the first Number? "))
second_number = int(input("What is the second Number? "))
if first_number > second_number:
    print("The first number is greater.")
    print("The numbers are not equal.")
    print("The second number is not greater.\n")
elif first_number == second_number:
    print("The first number is not greater.")
    print("The numbers are equal.")
    print("The second number is not greater.\n")
else:
    print("The first number is not greater.")
    print("The numbers are not equal.")
    print("The second number is greater.\n")
animal = input("What is your favorite animal? ")
if animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")