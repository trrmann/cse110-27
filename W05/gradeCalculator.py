"""
    filname:  gradeCalculator.py
        Requirements:
        1)  Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade.
            (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)
        2)  Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out. Add a separate
            if statement to determine if the user passed the course, and if so display a message to congratulate them. If not, display a
            different message to encourage them for next time.
        3)  Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block,
            instead create a new variable called letter and then in each block, set this variable to the appropriate value. Finally, after the
            whole series of if-elif-else statements, have a single print statement that prints the letter grade once.
        4)  The grade distribution is as follows:
            A >= 90
            B >= 80
            C >= 70
            D >= 60
            F < 60
    author:  Tracy Mann
    version:  1.0
    date:  10/8/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
        inputs:  a floating point decinal to represent the grade percentage from the user to the question "What did you recieve for your grade as a percentage? "
        process:  if-elif-else statements to determine the correct grade as in Req.#4 and directly output the letter grade.
        output:  "You received a(an) {A,B,C,D,F} for a letter grade."
        output:  if the grade is passing as per Req.#2 report, "Congratulations, you passed!" otherwise, report "Even though you did not pass this time, you will do better next time."
    version 1.1:
    date:  10/8/2022
        process:  if-elif-else statements to determine the correct grade as in Req.#4 and store into a variable, as well as storing if it is a passing grade or not into a variable.
        output:  use a single print statement to perfrom the same output as in version 1.0
    Challenge:
        Requirements:
        1)  Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, you'll know it is a "+" if the last digit is >= 7. You'll
            know it is a minus if the last digit is < 3 and otherwise it has no sign.
        2)  After your logic to determine the grade letter, add another section to determine the sign. Save this sign into a variable. Then, display both the grade letter and the sign
            in one print statement.
            Hint: To get the last digit, you could divide the number by 10, and get the remainder. You might refer back to the preparation material for Lesson 03 to see the operators
                and find the one that does division and gives you the remainder.
            At this point, don't worry about the exceptional cases of A+, F+, or F-.
        3)  Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.
        4)  Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.
    version 1.2:
    date:  10/8/2022
        process:  changes to process are to add modulus for the letter grade modifier.
        output:  add the letter grade modifier to the letter grade in the output.
    version 1.3:
    date:  10/8/2022
        process:  changes to process are to remove the letter grade modifier by using stronger if elif statements.    
"""

grade = -1.0
while (grade<0.0)or(grade>100.0):
    try:
        grade = float(input("What did you recieve for your grade as a percentage? "))
    except ValueError:
        print("Please enter a valid percentage grade between 0 and 100.")
if grade >= 90.0:
#changed in version 1.1
#    print("You received an A for a letter grade.")
#added in version 1.1
    article = "an"
#added in version 1.1
    letter = "A"
#added in version 1.1
    passing = True
elif grade >= 80.0:
#changed in version 1.1
#    print("You received a B for a letter grade.")
#added in version 1.1
    article = "a"
#added in version 1.1
    letter = "B"
#added in version 1.1
    passing = True
elif grade >= 70.0:
#changed in version 1.1
#    print("You received a C for a letter grade.")
#added in version 1.1
    article = "a"
#added in version 1.1
    letter = "C"
#added in version 1.1
    passing = True
elif grade >= 60.0:
#changed in version 1.1
#    print("You received a D for a letter grade.")
#added in version 1.1
    article = "a"
#added in version 1.1
    letter = "D"
#added in version 1.1
    passing = False
else:
#changed in version 1.1
#    print("You received an F for a letter grade.")
#added in version 1.1
    article = "an"
#added in version 1.1
    letter = "F"
#added in version 1.1
    passing = False
#changed in version 1.1
#added in version 1.2
grade_mod = grade % 10
#added in version 1.2
#changed in version 1.3
#if grade_mod >= 7.0:
if (grade_mod >= 7.0) and (letter not in ["A","F"]):
#added in version 1.2
    letter = f"{letter}+"
#added in version 1.2
#changed in version 1.3
#elif grade_mod <= 3.0:
elif (grade_mod <= 3.0) and (letter not in ["F"]) and grade != 100.0:
#added in version 1.2
    letter = f"{letter}-"
#if grade >= 70.0:
#    print("Congratulations, you passed!")
#else:
#    print("Even though you did not pass this time, you will do better next time.")
if passing:
    msg="Congratulations, you passed!"
else:
    msg="Even though you did not pass this time, you will do better next time."
print(f"You received {article} {letter} for a letter grade.\n{msg}")