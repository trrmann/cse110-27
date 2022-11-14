#! python
#shopping_cart = {}
items = []
prices = []
quantities = []
print("Welcome to the Shopping Cart Program!")
quit = False
while not quit:
    print("Please select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    try:
        action = int(input("Please enter an action: "))
    except ValueError:
        action = 0
    except KeyboardInterrupt:
        action = 5
    finally:
        match action:
            case 1:
                item = input("What item would you like to add? ")
                #shopping_cart[item] = {}
                items.append(item)
                price = float(input(f"What is the price of 1 \'{item}\'? "))
                prices.append(price)
                quantity = int(input(f"How many \'{item}\' do you want to add? "))
                quantities.append(quantity)
                #shopping_cart[item]["price"] = price
                #shopping_cart[item]["quantity"] = quantity
                print(f"\'{item}\' have been added to the cart.\n")
            case 2:
                print("The contents of the shopping cart are: ")
                #for index, item in enumerate(shopping_cart.keys()):
                #    print(f"{index + 1}. {item} - {shopping_cart[item]['quantity']} @ ${shopping_cart[item]['price']:.2f} for ${(shopping_cart[item]['quantity'] * shopping_cart[item]['price']):.2f}")
                for index, item in enumerate(items):
                    print(f"{index + 1}. {item} - {quantities[index]} @ ${prices[index]:.2f} for ${(quantities[index] * prices[index]):.2f}")
                print()
            case 3:
                remove = int(input("Which item would you like to remove? "))
                #if (remove >= 1) and (remove <= len(shopping_cart.keys())):
                #    shopping_cart.pop([*shopping_cart.keys()][(remove - 1)])
                #    print(f"item removed.")
                #else:
                #    print(f"Sorry that is not a valid item number between 1 and {len(shopping_cart.keys())}.")
                if (remove >= 1) and (remove <= len(items)):
                    items.pop(remove - 1)
                    quantities.pop(remove - 1)
                    prices.pop(remove - 1)
                    print(f"item removed.\n")
                else:
                    print(f"Sorry that is not a valid item number between 1 and {len(items)}.")
            case 4:
                total = 0
                #for item in shopping_cart.keys():
                #    total += shopping_cart[item]['quantity'] * shopping_cart[item]['price']
                for index in range(len(items)):
                    total += quantities[index] * prices[index]
                print(f"The total price of the items in the shopping cart is ${total:.2f}\n")
            case 5:
                quit = True
            case _:
                print("Please select an option from 1 to 5.")
print("Thank you.  Goodbye.")