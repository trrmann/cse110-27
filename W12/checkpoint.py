#! python
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest = 1000
youngest_name = ""
for index, element in enumerate(people):
    #print(element)
    elements = element.split(" ")
    print(f"Name:  {elements[0]:<15}Age:  {elements[1]}")
    if int(elements[1]) < youngest:
        youngest = int(elements[1])
        youngest_name = elements[0]
print(f"\nThe youngest is {youngest_name} at {youngest} years old.")