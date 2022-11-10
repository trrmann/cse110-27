#! python
print("Enter a list of numbers, type 0 when finished.")
sum = 0
max = 0
numbers = []
number = -1
while number != 0:
    try:
        number = int(input("Enter number: "))
        sum += number
        if number > max: max = number
        if number != 0: numbers.append(number)
    except ValueError:
        print("Please enter a number.")
print(f"The sum is: {sum}")
if len(numbers) == 0: print(f"The average is: 0")
else: print(f"The average is: {sum/len(numbers)}")
print(f"The largest number is: {max}")