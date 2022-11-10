#! python
print("Enter a list of numbers, type 0 when finished.")
sum = 0
max = 0
min_over_zero = 0
numbers = []
number = -1
while number != 0:
    try:
        number = int(input("Enter number: "))
        sum += number
        if number > max: max = number
        if(number > 0) and (min_over_zero == 0): min_over_zero = number
        elif (number > 0) and (number < min_over_zero): min_over_zero = number
        if number != 0: numbers.append(number)
    except ValueError:
        print("Please enter a number.")
print(f"The sum is: {sum}")
if len(numbers) == 0: print(f"The average is: 0")
else: print(f"The average is: {sum/len(numbers)}")
print(f"The largest number is: {max}")
if min_over_zero != 0: print(f"The smallest positive number over zero is: {min_over_zero}")
numbers.sort()
print("The sorted list is:")
for number in numbers:
    print(number)


