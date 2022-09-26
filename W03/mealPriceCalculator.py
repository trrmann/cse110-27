"""
    filname:  mealPriceCalculator.py
    inputs:  a floating point decimal to represent the price of a child's meal from the user to the question "What is the price of a child's meal? "
    inputs:  a floating point decimal to represent the price of a adult's meal from the user to the question "What is the price of a adult's meal? "
    inputs:  an integer to represent the number of children from the user to the question "How many children? "
    inputs:  an integer to represent the number of adults from the user to the question "How many adults? "
    inputs:  a floating point decimal to represent the sales tax rate from the user to the question "What is the sales tax rate percent? "
    inputs:  a floating point decimal to represent the payment amount from the user to the question "What is the payment amount? "
    Process:  Compute the subtotal.
        children_subtotal = children_quantity * children_price
        adult_subtotal = adult_quantity * adults_price
        subtotal = children_subtotal + adult_subtotal
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax
        change = payment_amount - total
    output:  Display the subtotal and display the total price of the meal by adding the subtotal and the sales tax. (don't worry about rounding to two decimals at this point):
        Subtotal:  ${subtotal}
        Sales Tax({tax_rate}%):  {sales_tax}
        Total:  ${total}
        Change: ${change}
    author:  Tracy Mann
    version:  1.0
    date:  9/22/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
    version 1.1:
        date:  9/23/2022
            1)  For this assignment, you could add anything else to the meal, such as drinks, appetizers, or a tip percentage, or anything else you can think of.
                Play around with different ideas and see what you can learn!
            2)  Add the ability to order beverages, appitizers and deserts.
            3)  Add the ability to apply a discount (either by % or by dollar amount).
            4)  Display the tip calculations based off of full order value for 10%, 15% and 20% for recomendations
            5)  Add the ability to add a tip (either by % or by dollar amount).
            6)  If tip is % allow to base tip on discounted or full order value if applicable.
            7)  Display the itemized breakdown of the order.
                (tip display percent will be on full order value)
                (if the value of an order item is 0 then do not display that line)
                (if the quantity is singular use singular description otherwise use pural)
            8)  Add default values for inputs as follows:
                price of adults = 9.00
                price of children = half the price of the adult
                price of beverages = 2.50
                price of appitizers = 4.00
                price of deserts = 6.00
                number of children = 0
                number of adults = 1
                number of beverages = number of children + number of adults 
                number of appitizers = half the number of children(trimmed down) + number of adults 
                number of deserts = number of children + half the number of adults(trimmed down)
                sales tax rate = 6%
                discount = 0%
                tip = 10%
                payment amount = total amount due
            input update:
                inputs:  a floating point decimal to represent the price of a child's meal from the user to the question "What is the price of a child's meal? "
                inputs:  a floating point decimal to represent the price of a adult's meal from the user to the question "What is the price of a adult's meal? "
                new input:  a floating point decimal to represent the price of a beverage from the user to the question "What is the price of a beverage? "
                new input:  a floating point decimal to represent the price of an appitizer from the user to the question "What is the price of a appitizer? "
                new input:  a floating point decimal to represent the price of a desert from the user to the question "What is the price of a desert? "
                inputs:  an integer to represent the number of children from the user to the question "How many children? "
                inputs:  an integer to represent the number of adults from the user to the question "How many adults? "
                new input:  an integer to represent the number of beverages from the user to the question "How many beverages? "
                new input:  an integer to represent the number of appitizers from the user to the question "How many appitizers? "
                new input:  an integer to represent the number of deserts from the user to the question "How many deserts? "
                new input:  a string to represent the discount from the user to the question "How much of a discount? "
                inputs:  a floating point decimal to represent the sales tax rate from the user to the question "What is the sales tax rate percent? "
                new input:  a string to represent the tip from the user to the question "How much for a tip? "
                optional input:  a string to represent the tip option from the user to the question "Do you wish to apply the tip percent on the discounted value, if not it will be applied to the full order value(Y/N)? "
                inputs:  a floating point decimal to represent the payment amount from the user to the question "What is the payment amount? "
            Process:  Compute the subtotal.
                children_subtotal = children_quantity * children_price
                adult_subtotal = adult_quantity * adults_price
                beverage_subtotal = beverage_quantity * beverage_price
                appitizer_subtotal = appitizer_quantity * appitizer_price
                desert_subtotal = desert_quantity * desert_price
                subtotal = children_subtotal + adult_subtotal + beverage_subtotal + appitizer_subtotal + desert_subtotal
                if discount string ends in % then discount = subtotal * discount_rate {discount string value /100} else floating point cast of discount string
                if tip string ends in % and option tip input = yes then tip base = subtotal - discount else tip base = subtotal
                if tip string ends in % then tip = tip base * tip_rate {tip string value /100} else floating point cast of tip string
                sales_tax = (subtotal-discount) * tax_rate
                total = subtotal - discount + sales_tax
                grand total = total + tip
                change = payment_amount - grand total
            output update:
                [prior to input for tip]${subtotal*.1} = 10%; ${subtotal*.15} = 15%; $(subtotal*.2) = 20%
                [if has singular children_quantity]  {children_quantity} children's meal at ${children_price}:  {children_subtotal}
                [if has plural children_quantity]  {children_quantity} children's meals at ${children_price}:  {children_subtotal}
                [if has singular adult_quantity]  {adult_quantity} adult's meal at ${adults_price}:  {adult_subtotal}
                [if has plural adult_quantity]  {adult_quantity} adult's meals at ${adults_price}:  {adult_subtotal}
                [if has singular beverage_quantity]  {beverage_quantity} beverage at ${beverage_price}:  {beverage_subtotal}
                [if has plural beverage_quantity]  {beverage_quantity} beverages at ${beverage_price}:  {beverage_subtotal}
                [if has singular appitizer_quantity]  {appitizer_quantity} appitizer at ${appitizer_price}:  {appitizer_subtotal}
                [if has plural appitizer_quantity]  {appitizer_quantity} appitizers at ${appitizer_price}:  {appitizer_subtotal}
                [if has singular desert_quantity]  {desert_quantity} desert at ${desert_price}:  {desert_subtotal}
                [if has plural desert_quantity]  {desert_quantity} deserts at ${desert_price}:  {desert_subtotal}
                  discount({discount_percent}*100%):  {discount_amount}
                Subtotal:  {subtotal-discount_amount}
                Sales Tax({tax_rate}%):  {sales_tax}
                Total:  {total}
                Tip:  {tip}
                Grand Total:  {grand_total}
                [if nothing was entered for amount paid]Paid:  {amount_paid}
                Change:  {change}
"""

#changed in version 1.1
#children_price = float(input("What is the price of a child's meal? "))
children_price_string = input("What is the price of a child's meal? ")
#changed in version 1.1
#adults_price = float(input("What is the price of a adult's meal? "))
adults_price_string = input("What is the price of a adult's meal? ") 
if(adults_price_string==""): adults_price_string = "9.00"
adults_price = float(adults_price_string)
if(children_price_string==""): children_price_string = str(adults_price * .5)
children_price = float(children_price_string)
#added in version 1.1
beverage_price_string = input("What is the price of a beverage? ") 
#added in version 1.1
if(beverage_price_string==""): beverage_price_string = "2.50"
#added in version 1.1
beverage_price = float(beverage_price_string)
#added in version 1.1
appitizer_price_string = input("What is the price of an appitizer? ") 
#added in version 1.1
if(appitizer_price_string==""): appitizer_price_string = "4.00"
#added in version 1.1
appitizer_price = float(appitizer_price_string)
#added in version 1.1
desert_price_string = input("What is the price of a desert? ") 
#added in version 1.1
if(desert_price_string==""): desert_price_string = "6.00"
#added in version 1.1
desert_price = float(desert_price_string)
#changed in version 1.1
#children_quantity = int(input("How many children? "))
children_quantity_string = input("How many children? ")
#added in version 1.1
if(children_quantity_string==""): children_quantity_string = "0"
#added in version 1.1
children_quantity = int(children_quantity_string)
#changed in version 1.1
#adult_quantity = int(input("How many adults? "))
adult_quantity_string = input("How many adults? ")
#added in version 1.1
if(adult_quantity_string==""): adult_quantity_string = "1"
#added in version 1.1
adult_quantity = int(adult_quantity_string)
#added in version 1.1
beverage_quantity_string = input("How many beverages? ")
#added in version 1.1
if(beverage_quantity_string==""): beverage_quantity_string = str(children_quantity + adult_quantity)
#added in version 1.1
beverage_quantity = int(beverage_quantity_string)
#added in version 1.1
appitizer_quantity_string = input("How many appitizers? ")
#added in version 1.1
if(appitizer_quantity_string==""): appitizer_quantity_string = str(int(0.5 * children_quantity) + adult_quantity)
#added in version 1.1
appitizer_quantity = int(appitizer_quantity_string)
#added in version 1.1
desert_quantity_string = input("How many deserts? ")
#added in version 1.1
if(desert_quantity_string==""): desert_quantity_string = str(children_quantity + int(0.5 * adult_quantity))
#added in version 1.1
desert_quantity = int(desert_quantity_string)
children_subtotal = children_quantity * children_price
adult_subtotal = adult_quantity * adults_price
#added in version 1.1
beverage_subtotal = beverage_quantity * beverage_price
#added in version 1.1
appitizer_subtotal = appitizer_quantity * appitizer_price
#added in version 1.1
desert_subtotal = desert_quantity * desert_price
#changed in version 1.1
subtotal = children_subtotal + adult_subtotal + beverage_subtotal + appitizer_subtotal + desert_subtotal
#added in version 1.1
discount_string = input(f"How much of a discount? ")
#added in version 1.1
if (discount_string == ""): discount_string = "0%"
#added in version 1.1
# discount_string[:len(discount_string)-1] get the last character of the string
if (discount_string[len(discount_string)-1]=="%"):
    # discount_string[:len(discount_string)-1] gets all the characters except the last of the string
    discount_percent = float(discount_string[:len(discount_string)-1])/100
    discount_amount = subtotal * discount_percent
else:
    discount_amount = float(discount_string)
    discount_percent = discount_amount / subtotal
#changed in version 1.1
#tax_rate = float(input("What is the sales tax rate percent? "))/100
tax_rate_string = input("What is the sales tax rate percent? ")
#added in version 1.1
if(tax_rate_string==""): tax_rate_string = "6"
#added in version 1.1
tax_rate = float(tax_rate_string)/100
#changed in version 1.1
#sales_tax = subtotal * tax_rate
sales_tax = (subtotal-discount_amount) * tax_rate
#changed in version 1.1
#total = subtotal + sales_tax
total = subtotal - discount_amount + sales_tax
#added in version 1.1
print(f"${(subtotal*.1)} = 10%; ${(subtotal*.15)} = 15%; ${(subtotal*.2)} = 20%")
#added in version 1.1
tip_string = input(f"How much for a tip? ")
#added in version 1.1
if (tip_string == ""): tip_string = "10%"
#added in version 1.1
# tip_string[len(tip_string)-1] get the last character of the string
if (tip_string[len(tip_string)-1]=="%"):
    # tip_string[:len(tip_string)-1] gets all the characters except the last of the string
    tip_percent = float(tip_string[:len(tip_string)-1])/100
    tip_base_string = input("Do you wish to apply the tip percent on the discounted value, if not it will be applied to the full order value(Y/N)? ")
    if tip_base_string.lower() in ["y","yes"]:
        tip_amount = (subtotal - discount_amount) * tip_percent
        tip_percent = tip_amount / subtotal
    else:
        tip_amount = subtotal * tip_percent
else:
    tip_amount = float(tip_string)
    tip_percent = tip_amount / subtotal
#added in version 1.1
grand_total = total + tip_amount
#added in version 1.1
if(children_quantity==1): child_string = "child's meal"
else: child_string = "children's meals"
#added in version 1.1
if(adult_quantity==1): adult_string = "adult's meal"
else: adult_string = "adult's meals"
#added in version 1.1
if(beverage_quantity==1): beverage_string = "beverage"
else: beverage_string = "beverages"
#added in version 1.1
if(appitizer_quantity==1): appitizer_string = "appitizer"
else: appitizer_string = "appitizers"
#added in version 1.1
if(desert_quantity==1): desert_string = "desert"
else: desert_string = "deserts"
#added in version 1.1
child_line_base = f"  {children_quantity} {child_string} at ${children_price} each:"
#added in version 1.1
adult_line_base = f"  {adult_quantity} {adult_string} at ${adults_price} each:"
#added in version 1.1
beverage_line_base = f"  {beverage_quantity} {beverage_string} at ${beverage_price} each:"
#added in version 1.1
appitizer_line_base = f"  {appitizer_quantity} {appitizer_string} at ${appitizer_price} each:"
#added in version 1.1
desert_line_base = f"  {desert_quantity} {desert_string} at ${desert_price} each:"
#added in version 1.1
child_line = f"{child_line_base} {children_subtotal}\n"
#added in version 1.1
adult_line = f"{adult_line_base} {adult_subtotal}\n"
#added in version 1.1
beverage_line = f"{beverage_line_base} {beverage_subtotal}\n"
#added in version 1.1
appitizer_line = f"{appitizer_line_base} {appitizer_subtotal}\n"
#added in version 1.1
desert_line = f"{desert_line_base} {desert_subtotal}\n"
#added in version 1.1
discount_line = f"  discount({discount_percent*100}%):  {discount_amount}\n"
#added in version 1.1
if(children_quantity==0): child_line=""
#added in version 1.1
if(adult_quantity==0): adult_line=""
#added in version 1.1
if(beverage_quantity==0): beverage_line=""
#added in version 1.1
if(appitizer_quantity==0): appitizer_line=""
#added in version 1.1
if(desert_quantity==0): desert_line=""
#added in version 1.1
if(discount_amount==0): discount_line=""
#changed in version 1.1
#invoice = f"\nSubtotal:  {subtotal}\n\
#Sales Tax({tax_rate}%):  {sales_tax}\n\
#Total:  {total}\n\n"
invoice = f"\n{appitizer_line}{child_line}{adult_line}{desert_line}{beverage_line}{discount_line}\
Subtotal:  {subtotal-discount_amount}\n\
Sales Tax({tax_rate * 100}%):  {sales_tax}\n\
Total:  {total}\n\
Tip({(tip_percent*100.0)}%):  {tip_amount}\n\
Grand Total:  {grand_total}\n"
print(invoice)
#changed in version 1.1
#payment_amount = float(input("What is the payment amount? "))
payment_amount_string = input("What is the payment amount? ")
#added in version 1.1
if(payment_amount_string==""):
    payment_amount_string = str(grand_total)
    print(f"Paid:  {grand_total}\n")
#added in version 1.1
payment_amount = float(payment_amount_string)
#changed in version 1.1
#change = payment_amount - total
change = payment_amount - grand_total
print(f"Change: ${change}\n")