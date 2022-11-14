#! python
print("Enter the names and balances of bank accounts (type: quit when done)")
account_names = []
account_balances = []
total = 0.0
name = ""
pad = 10
npad = 0
while name != "Quit":
    name = input("What is the name of this account? ").lower().capitalize()
    if name != "Quit":
        try:
            amount = float(input("What is the balance? $"))
            account_names.append(name)
            account_balances.append(amount)
            if len(name) > pad: pad = len(name)
            if len(f"{amount}:.2f") - 3 > npad: npad = len(f"{amount}:.2f") - 3
            total += amount
        except ValueError:
            pass
average = total / len(account_balances)
if len(f"{total}:.2f") - 3 > npad: npad = len(f"{total}:.2f") - 3
if len(f"{average}:.2f") - 3 > npad: npad = len(f"{average}:.2f") - 3
print("\nAccount Information:\n")
for index, name in enumerate(account_names):
    print(f"{f'{name} - ':<{pad}}"+f"${account_balances[index]:>{npad}.2f}")
print(" " *pad+"="*(npad+1))
print(f"{'Total:  ':>{pad}}"+f"${total:>{npad}.2f}")
print(" " *pad+"-"*(npad+1))
print(f"{'Average:  ':>{pad}}"+f"${average:>{npad}.2f}")