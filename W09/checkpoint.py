#! python
friends = []
friend = ""
while friend != "end":
    friend = input("Type the name of a friend:  ").lower()
    if friend != "end": friends.append(friend.capitalize())
print("Your friends are:")
for friend in friends:
    print(friend)
