#! python
import os

os.system("cls")
print("Enter the names and balances of bank accounts (type: quit when done)")
account_names = []
account_balances = []
total = 0.0
highest = 0
highest_index = -1
name = ""
pad = 0
npad = 0
counter = 0
while name != "Quit":
    name = input("What is the name of this account? ").lower().capitalize()
    if name != "Quit":
        try:
            amount = float(input("What is the balance? $"))
            account_names.append(name)
            account_balances.append(amount)
            if len(f'{counter}. {name} - ') > pad: pad = len(f'{counter}. {name} - ')
            if len(f"{amount}:.2f") - 3 > npad: npad = len(f"{amount}:.2f") - 3
            if highest_index == -1: highest_index = len(account_names) - 1
            if amount > highest:
                highest = amount
                highest_index = len(account_names) - 1

            total += amount
            counter += 1
        except ValueError:
            pass
reply = "y"
while reply in ["yes","y"]:
    average = total / len(account_balances)
    if len(f"Highest Balance:  {account_names[highest_index]} - ") > pad: pad = len(f"Highest Balance:  {account_names[highest_index]} - ")
    if len(f"{total}:.2f") - 3 > npad: npad = len(f"{total}:.2f") - 3
    if len(f"{average}:.2f") - 3 > npad: npad = len(f"{average}:.2f") - 3
    if len(f"{highest}:.2f") - 3 > npad: npad = len(f"{highest}:.2f") - 3
    os.system("cls")
    print("\nAccount Information:\n")
    for index, name in enumerate(account_names):
        print(f"{f'{index}. {name} - ':<{pad}}"+f"${account_balances[index]:>{npad}.2f}")
    print(" " *pad+"="*(npad+1))
    print(f"{'Total:  ':>{pad}}"+f"${total:>{npad}.2f}")
    print(" " *pad+"-"*(npad+1))
    print(f"{'Average:  ':>{pad}}"+f"${average:>{npad}.2f}")
    print(f"{f'Highest Balance:  {account_names[highest_index]} - ':>{pad}}"+f"${highest:>{npad}.2f}")
    reply=input("\nDo you want to update an account?").lower()
    if reply in ["yes","y"]:
        index = -1
        while (index < 0) or (index > (len(account_names) - 1)):
            try:
                index = int(input("What account index do you want to update? "))
            except ValueError:
                pass
        total -= account_balances[index]
        amount = -0.001
        while amount < 0.0:
            try:
                amount = float(input("What is the new amount? "))
            except ValueError:
                pass
        total += amount
        account_balances[index] = amount
        if len(f"{amount}:.2f") - 3 > npad: npad = len(f"{amount}:.2f") - 3
        highest = -0.001
        for index, amount in enumerate(account_balances):
            if amount > highest:
                highest = amount
                highest_index = index