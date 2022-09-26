"""
    filname:  idBadge.py
    inputs:  a string to represent the first name from the user to the question "What is your first name?"
    inputs:  a string to represent the last name from the user to the question "What is your last name?"
    inputs:  a string to represent the email address from the user to the question "What is your last name?"
    inputs:  a string to represent the phone number from the user to the question "What is your last name?"
    inputs:  a string to represent the job title from the user to the question "What is your last name?"
    inputs:  a string to represent the ID number from the user to the question "What is your last name?"
    output:  a formated display of the Identification Badge for the given input as below:
        ----------------------------------------
        [LAST NAME], [first name]
        [Job title]
        ID: [id number]

        [email address]
        [phone number]
        ----------------------------------------
    additional requirements for output:
        1)  The last name should be converted from whatever the user types to be displayed in ALL CAPS.
        2)  The job title should be displayed so that the first letter is capitalized.
        3)  The email address should be displayed in all lowercase.
    author:  Tracy Mann
    version:  1.0
    date:  9/15/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
    version 1.1:
        date:  9/15/2022
            1)  Add hair color and eye color and put them both on the same line in the display.
            2)  Add a field for the name of the month they started and also a yes/no field for whether they have completed advanced training. Put these both on the same line in the display.
            3)  For the two lines that you just added, make it so that the second columns align, regardless of how many letters are in the responses.
            output layout update:
                The ID Card is:
                ----------------------------------------
                DOE, Jane
                Chief Software Architect
                ID: 83-23821

                janedoe@email.com
                (208) 555-1234

                Hair: Brown           Eyes: Blue
                Month: September      Training: Yes
                ----------------------------------------
            ref:  https://www.w3resource.com/python/python-format.php for padded formatting notes
                  https://www.geeksforgeeks.org/python-string-length-len/ for length of string
                  https://www.w3schools.com/python/python_conditions.asp for python conditions
                  https://www.golinuxcloud.com/python-line-continuation/ line continuation
"""

first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is your e-mail address?")
phone = input("What is your phone number?")
job_title = input("What is your job title?")
id_number = input("What is your id number?")
#added in version 1.1
hair_color = input("What is your hair color?")
#added in version 1.1
eye_color = input("What is your eye color?")
#added in version 1.1
hire_month = input("What month were you hired in?")
#added in version 1.1
advanced_training = input("Did you take the advanced training(Yes/No)?")
separator_line = "----------------------------------------"
#added in version 1.1
if len(hair_color) > len(hire_month)+1:
    pad = len(hair_color)+2 
else:
    pad = len(hire_month)+3
#end if len(hair_color) > len(hire_month):
#changed in version 1.1
#id_card = f"{separator_line}\n{last_name.upper()}, {first_name.capitalize()}\n{job_title.title()}\nID:  {id_number}\n\n{email.lower()}\n{phone}\n{separator_line}\n"
id_card = f"{separator_line}\n\
{last_name.upper()}, {first_name.capitalize()}\n\
{job_title.title()}\n\
ID:  {id_number}\n\n\
{email.lower()}\n\
{phone}\n\n\
Hair:  {hair_color:<{pad+1}s}Eyes:  {eye_color}\n\
Month:  {hire_month:<{pad}s}Training:  {advanced_training}\n\
{separator_line}\n"
message = f"\nThe ID Card is:\n{id_card}"
print(message)
#input("Press enter to continue:  ")