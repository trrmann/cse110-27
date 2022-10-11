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
    version 1.2:
        date:  9/23/2022
            1)  Compute and display the sales tax.
            2)  Compute and display the total.
            3)  Ask the user for the payment amount and store the value properly as a floating point number.
            4)  Compute and display the change.
            5)  Include a dollar sign ($) before each displayed value.
            6)  Display each value to two decimals.
            7)  Double check that the calculations are correct.
            8)  Show creativity and exceed the core requirements by adding additional features.
            9)  Use good style in your program, including variable names and whitespace.
            input update:
                none.
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
                  discount({discount_percent}*100%):  ${discount_amount}
                Subtotal:  ${subtotal-discount_amount}
                Sales Tax({tax_rate}%):  ${sales_tax}
                Total:  ${total}
                Tip:  ${tip}
                Grand Total:  ${grand_total}
                [if nothing was entered for amount paid]Paid:  ${amount_paid}
                Change: ${change}
    version 1.3:
        date:  9/23/2022
            1)  Align the decimal point on the dollar values
            2)  Display negative change with ()'s instead of - symbol
            input update:
                none.
            Process:
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
                Subtotal:  ${subtotal-discount_amount}
                Sales Tax({tax_rate}%):  ${sales_tax}
                Total:  ${total}
                Tip:  ${tip}
                Grand Total:  ${grand_total}
                [if nothing was entered for amount paid]Paid:  ${amount_paid}
                Change: ${change}
            ref:  https://www.w3schools.com/python/ref_func_max.asp for python max use
                  https://www.w3schools.com/python/ref_func_abs.asp for python abs use

    submission comment:  I believe this submission has earned a Made it my own.  I have met every requirement in the ruberic.  I have also not only added more items in the menu such as beverages, appitizers and deserts, but also verified entries are not empty.  In the event that an entry is empty the program will populate a default value for the response.  I have also added the ability to apply a discount and a tip by either percent or by dollar amount.  When a discount is applied and the tip is given as a percent then there is the option to apply the tip to the discounted value or to the value prior to discount, adjusting the final display of tip percent to the value prior to discount.  Also the dollor amounts in the resulting output are all aligned on the decimal point with total and subtotal lines separating sections.
"""
class Error(Exception):
    """Base class for other exceptions"""
    pass

class UnknownItem(Error):
    """Raised when the item is unknown"""
    pass

class NotAPercent(Error):
    """Raised when the item is not a percent"""
    pass

def price_default(price_item, price_dictionary):
    if price_item == adult_key:
        price_dictionary[price_item] = 9.00
    elif price_item == child_key:
        price_dictionary[price_item] = price_dictionary[adult_key] * .5
    elif price_item == beverage_key:
        price_dictionary[price_item] = 2.50
    elif price_item == appitizer_key:
        price_dictionary[price_item] = 4.00
    elif price_item == desert_key:
        price_dictionary[price_item] = 6.00
    else:
        raise UnknownItem(f"Unknown Item {price_item}!")
    return price_dictionary

def request_price(price_item, names_dictionary, prices_dictionary):
    prices_dictionary[price_item] = -0.001
    while prices_dictionary[price_item] <= 0.0:
        prices_dictionary[price_item] = float(input(f"What is the price of {names_dictionary[price_item][0]} {names_dictionary[price_item][1]}? "))
    return prices_dictionary

def price(price_item, names_dictionary, prices_dictionary):
    try:
        prices_dictionary = request_price(price_item, names_dictionary, prices_dictionary)
    except ValueError:
        prices_dictionary = price_default(price_item, prices_dictionary)
    finally:
        return prices_dictionary

def get_all_prices(names, prices):
    for item in names.keys():
        prices = price(item, names, prices)
    return prices

def quantity_default(quantity_item, quantity_dictionary):
    if quantity_item == adult_key:
        quantity_dictionary[quantity_item] = 1
    elif quantity_item == child_key:
        quantity_dictionary[quantity_item] = 0
    elif quantity_item == beverage_key:
        quantity_dictionary[quantity_item] = quantity_dictionary[child_key] + quantity_dictionary[adult_key]
    elif quantity_item == appitizer_key:
        quantity_dictionary[quantity_item] = int(0.5 * quantity_dictionary[child_key]) + quantity_dictionary[adult_key]
    elif quantity_item == desert_key:
        quantity_dictionary[quantity_item] = quantity_dictionary[child_key] + int(0.5 * quantity_dictionary[adult_key])
    else:
        raise UnknownItem(f"Unknown Item {quantity_item}!")
    return quantity_dictionary

def request_quantity(quantity_item, names_dictionary, quantity_dictionary):
    quantity_dictionary[quantity_item] = -1
    while quantity_dictionary[quantity_item] < 0:
        quantity_dictionary[quantity_item] = int(input(f"How many {names_dictionary[quantity_item][3]}? "))
    return quantity_dictionary

def quantity(quantity_item, names_dictionary, quantity_dictionary):
    try:
        quantity_dictionary = request_quantity(quantity_item, names_dictionary, quantity_dictionary)
    except ValueError:
        quantity_dictionary = quantity_default(quantity_item, quantity_dictionary)
    finally:
        return quantity_dictionary

def get_all_quantities(names, quantities):
    for item in names.keys():
        quantities = quantity(item, names, quantities)
    return quantities

def item_itemize(values, itemize_item, quantity_dictionary, prices_dictionary, names_dictionary):
    values[order_quantity_key] = values[order_quantity_key] + quantity_dictionary[itemize_item]
    values[item_subtotal_key][itemize_item] = quantity_dictionary[itemize_item] * prices_dictionary[itemize_item]
    values[subtotal_key] = values[subtotal_key] + values[item_subtotal_key][itemize_item]
    values[itemize_key][itemize_item] = {}
    if quantity_dictionary[itemize_item] == 1:
        values[itemize_key][itemize_item][base_key] = f"  {quantity_dictionary[itemize_item]} {names_dictionary[itemize_item][1]} at ${prices_dictionary[itemize_item]:.2f} each:"
    else:
        values[itemize_key][itemize_item][base_key] = f"  {quantity_dictionary[itemize_item]} {names_dictionary[itemize_item][2]} at ${prices_dictionary[itemize_item]:.2f} each:"
    values[itemize_key][itemize_item][baseLen_key] = len(values[itemize_key][itemize_item][base_key])
    out = values[item_subtotal_key][itemize_item]
    values[itemize_key][itemize_item][subtotal_key] = f"${out:.2f}"
    values[itemize_key][itemize_item][subtotalLen_key] = len(values[itemize_key][itemize_item][subtotal_key])
    if values[maxBaseLen_key] < values[itemize_key][itemize_item][baseLen_key]:
        values[maxBaseLen_key] = values[itemize_key][itemize_item][baseLen_key]
    if values[maxSubtotalLen_key] < values[itemize_key][itemize_item][subtotalLen_key]:
        values[maxSubtotalLen_key] = values[itemize_key][itemize_item][subtotalLen_key]
    return values

def get_all_items(values, names, prices, quantities):
    for item in names.keys():
        values = item_itemize(values, item, quantities, prices, names)
    return values

def line_itemize(values, itemize_item):
    values[itemize_key][itemize_item] = {}
    if itemize_item == discount_key:
        values[itemize_key][itemize_item][base_key] = f"  discount({(values[discount_percent_key]*100):.1f}%)"
        values[itemize_key][itemize_item][subtotal_key] = f"(${values[discount_amount_key]:.2f})"
    elif itemize_item == discount_subtotal_key:
        values[itemize_key][itemize_item][base_key] = "Subtotal:"
        values[itemize_key][itemize_item][subtotal_key] = f"${values[discounted_subtotal_key]:.2f}"
    elif itemize_item == sales_tax_key:
        values[itemize_key][itemize_item][base_key] = f"Sales Tax({(values[tax_rate_key] * 100):.1f}%):"
        values[itemize_key][itemize_item][subtotal_key] = f"${values[sales_tax_key]:.2f}"
    elif itemize_item == total_key:
        values[itemize_key][itemize_item][base_key] = "Total:"
        values[itemize_key][itemize_item][subtotal_key] = f"${values[total_key]:.2f}"
    elif itemize_item == tip_key:
        values[itemize_key][itemize_item][base_key] = f"Tip({(values[tip_percent_key] * 100.0):.1f}% of ${values[subtotal_key]:.2f}):"
        values[itemize_key][itemize_item][subtotal_key] = f"${values[tip_amount_key]:.2f}"
    elif itemize_item == grand_total_key:
        values[itemize_key][itemize_item][base_key] = "Grand Total:"
        values[itemize_key][itemize_item][subtotal_key] = f"${values[grand_total_key]:.2f}"
    values[itemize_key][itemize_item][baseLen_key] = len(values[itemize_key][itemize_item][base_key])
    values[itemize_key][itemize_item][subtotalLen_key] = len(values[itemize_key][itemize_item][subtotal_key])
    if itemize_item == discount_key:
        values[itemize_key][itemize_item][subtotalLen_key] = values[itemize_key][itemize_item][subtotalLen_key] - 1
    if values[maxBaseLen_key] < values[itemize_key][itemize_item][baseLen_key]:
        values[maxBaseLen_key] = values[itemize_key][itemize_item][baseLen_key]
    if values[maxSubtotalLen_key] < values[itemize_key][itemize_item][subtotalLen_key]:
        values[maxSubtotalLen_key] = values[itemize_key][itemize_item][subtotalLen_key]
    return values

def get_all_lines(values):
    for item in [discount_key, discount_subtotal_key, sales_tax_key, total_key, tip_key, grand_total_key]:
        values = line_itemize(values, item)
    return values

def isPercent(response):
    # response[len(response) - 1] get the last character of the string
    if type(response) == type(""):
        return response[len(response) - 1] == "%"
    else:
        return False

def percent(response):
    if isPercent(response):
        # response[ : len(response) - 1] gets all the characters except the last of the string
        return float(response[ : len(response) - 1])
    else:
        raise NotAPercent(f"{response} is not a %")

def percent_rate(response):
    return float(percent(response))/100.0

def discount_default(response):
    if response == "":
        return "5%"
    else:
        return response

def request_discount(values):
    values[discount_amount_key] = -0.001
    while values[discount_amount_key] <= 0.0:
        discount_string = discount_default(input(f"How much of a discount? "))
        try:
            values[discount_percent_key] = percent_rate(discount_string)
            values[discount_amount_key] = values[subtotal_key] * values[discount_percent_key]
        except NotAPercent:
            ...
            values[discount_amount_key] = float(discount_string)
            values[discount_percent_key] = values[discount_amount_key] / values[subtotal_key]
    return values

def discount(values):
    discount_string = input(f"Do you have a coupon or discount(Y/N)? ")
    if discount_string.lower() in ["y", "yes"]:
        values = request_discount(values)
    else:
        values[discount_amount_key] = 0.0
        values[discount_percent_key] = 0.0
    values[discounted_subtotal_key] = values[subtotal_key] - values[discount_amount_key]
    return values

def tax_rate(values):
    values[tax_rate_key] = 0.0
    while values[tax_rate_key] <= 0.0:
        try:
            temp = input("What is the sales tax rate percent? ")
            if temp[len(temp)-1] == "%": temp=temp[:len(temp)-1]
            values[tax_rate_key] = float(temp) / 100
        except  ValueError:
            values[tax_rate_key] = 0.06
    values[sales_tax_key] = values[discounted_subtotal_key] * values[tax_rate_key]
    values[total_key] = values[discounted_subtotal_key] + values[sales_tax_key]
    return values

def tip_default(response):
    if response == "":
        return "10%"
    else:
        return response

def request_tip(values):
    print(f"${(values[subtotal_key] * .1):.2f} = 10%; ${(values[subtotal_key] * .15):.2f} = 15%; ${(values[subtotal_key] * .2):.2f} = 20%")
    values[tip_amount_key] = -0.001
    while values[tip_amount_key] <= 0.0:
        tip_string = tip_default(input(f"How much of a tip? "))
        try:
            tip_base_string = input("Do you wish to apply the tip percent on the discounted value, if not it will be applied to the full order value(Y/N)? ")
            if tip_base_string.lower() in ["y", "yes"]:
                values[tip_amount_key] = values[discounted_subtotal_key] * percent_rate(tip_string)
                values[tip_percent_key] = values[tip_amount_key] / values[subtotal_key]
            else:
                values[tip_percent_key] = percent_rate(tip_string)
                values[tip_amount_key] = values[subtotal_key] * values[tip_percent_key]
        except NotAPercent:
            values[tip_amount_key] = float(tip_string)
            values[tip_percent_key] = values[tip_amount_key] / values[subtotal_key]
    return values

def tip(values):
    tip_string = input(f"Do you wish to leave a tip(Y/N)? ")
    if tip_string.lower() in ["y", "yes"]:
        values = request_tip(values)
    else:
        values[tip_amount_key] = 0.0
        values[tip_percent_key] = 0.0
    values[grand_total_key] = values[total_key] + values[tip_amount_key]
    return values

def invoice(values, names, quantities, invoice_out):
    empty = ""
    values[maxBaseLen_key] = values[maxBaseLen_key] + 4
    values[invoice_key] = invoice_out
    for item in values[itemize_key].keys():
        values[itemize_key][item][col2mod_key] = values[maxSubtotalLen_key] - values[itemize_key][item][subtotalLen_key]
        values[itemize_key][item][pad_key] = values[maxBaseLen_key] - values[itemize_key][item][baseLen_key]
        values[base_key] = values[itemize_key][item][base_key]
        values[pad_count_key] = values[itemize_key][item][pad_key] + values[itemize_key][item][col2mod_key]
        values[sub_key] = values[itemize_key][item][subtotal_key]
        values[itemize_key][item][line_key] = f"{values[base_key]}{empty:<{values[pad_count_key]}s}{values[sub_key]}\n"
        if (item == discount_key and values[discount_amount_key] == 0.0) or (item in names.keys() and quantities[item] == 0):
            values[itemize_key][item][line_key] = ""
        if ((item in [grand_total_key]) and (values[order_quantity_key] > 0)):
            values[invoice_key] = values[invoice_key] + f"{empty:<{values[maxBaseLen_key]}s}{empty:=<{values[maxSubtotalLen_key]+1}}\n"
        if ((item in [discount_subtotal_key, total_key]) and (values[order_quantity_key] > 0)):
            values[invoice_key] = values[invoice_key] + f"{empty:<{values[maxBaseLen_key]}s}{empty:-<{values[maxSubtotalLen_key]+1}}\n"
        values[invoice_key] = values[invoice_key] + values[itemize_key][item][line_key]
    return values

def main(names, prices, quantities, values):
    empty = ""
    prices = get_all_prices(names, prices)
    quantities = get_all_quantities(names, quantities)
    values = invoice(get_all_lines(tip(tax_rate(discount(get_all_items(values, names, prices, quantities))))), names, quantities, "\n")
    print(values[invoice_key])
    try:
        payment_amount = float(input("What is the payment amount? "))
    except  ValueError:
        payment_amount = values[grand_total_key]
    print(f"Paid:{empty:<{values[maxBaseLen_key] - len('Paid:') + values[maxSubtotalLen_key] - len(f'${values[grand_total_key]:.2f}') }s}${values[grand_total_key]:.2f}\n")
    change = payment_amount - values[grand_total_key]
    if(change < 0.0) :
        change_mod = values[maxSubtotalLen_key] - len(f"${change:.2f}")
        print(f"Change:{empty:<{values[maxBaseLen_key] - len('Change:') + change_mod }s}(${abs(change):.2f})")
    else :
        change_mod = values[maxSubtotalLen_key] - len(f"${change:.2f}")
        print(f"Change:{empty:<{values[maxBaseLen_key] - len('Change:') + change_mod }s}${change:.2f}")

adult_key = "adult"
child_key = "child"
beverage_key = "beverage"
appitizer_key = "appitizer"
desert_key = "desert"
order_quantity_key = "order_quantity"
item_subtotal_key = "item_subtotal"
subtotal_key = "subtotal"
itemize_key = "itemize"
maxBaseLen_key = "maxBaseLen"
maxSubtotalLen_key = "maxSubtotalLen"
base_key = "base"
baseLen_key = "baseLen"
subtotalLen_key = "subtotalLen"
discount_amount_key = "discount_amount"
discount_percent_key = "discount_percent"
discounted_subtotal_key = "discounted_subtotal"
tax_rate_key = "tax_rate"
sales_tax_key = "sales_tax"
total_key = "total"
tip_amount_key = "tip_amount"
tip_percent_key = "tip_percent"
grand_total_key = "grand_total"
discount_key = "discount"
discount_subtotal_key = "discount_subtotal"
tip_key = "tip"
col2mod_key = "col2mod"
pad_key = "pad"
line_key = "line"
pad_count_key = "pad_count"
sub_key = "sub"
invoice_key = "invoice"
main(
    {
        adult_key : ["an", "adult's meal", "adult's meals", "adults"],
        child_key : ["a", "child's meal", "child's meals", "children"],
        beverage_key : ["a", "beverage", "beverages", "beverages"],
        appitizer_key : ["an", "appitizer", "appitizers", "appitizers"],
        desert_key : ["a", "desert", "deserts", "deserts"]
    }, {}, {},
    {
        order_quantity_key : 0,
        item_subtotal_key : {},
        subtotal_key : 0.0,
        itemize_key : {},
        maxBaseLen_key : 0,
        maxSubtotalLen_key : 0
    }
)
