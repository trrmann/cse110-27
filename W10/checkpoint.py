#! python
shoppingList = []
item = ""
while item != "quit":
    item = input("Enter an item in the shopping list:  ").lower()
    if item != "quit": shoppingList.append(item.capitalize())
print("Your shopping list is:")
for item in shoppingList:
    print(item)
print()
for index in range(len(shoppingList)):
    print(f"{index} {shoppingList[index]}")
print()
index = len(shoppingList)
while (index<0) or (index>=len(shoppingList)):
    index = int(input("Which item would you like to change? "))
item = input("What is the new item? ").lower().capitalize()

shoppingList.pop(index)
shoppingList.insert(index, item)

for index in range(len(shoppingList)):
    print(f"{index} {shoppingList[index]}")
