#! python

items = ["abcde","fgh","ijklm","nopqrst","uvwxyzzzz"]
prices = [12.345, 20.0007, 5.01, 8, 2.5]
quantities = [1, 5, 8, 2, 1]

for item, price, quantity in zip(items, prices, quantities):
    #print(item, price)
    #print(f"{item:<27} {price:>7}")
    print(f"{quantity} {item:<27} {price:>7.2f}")
