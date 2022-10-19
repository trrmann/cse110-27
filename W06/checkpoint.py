size = float(input("How large of a loan 1-10:  "))
credit = float(input("How good is your credit history 1-10:  "))
income = float(input("How high is your income 1-10:  "))
down = float(input("How large is your down payment 1-10:  "))
authorize = False
if size >= 5:
    if (credit >= 7) and (income >= 7):
        authorize=True
    elif ((credit >= 7) or (income >= 7)) and (down >= 5):
        authorize=True
else:
    if(credit >=4):
        if((income >= 7) or (down >= 7)):
            authorize=True
        elif ((income >= 4) and (down >= 4)):
            authorize=True
if authorize:
    print("Decision:  Yes.")
else:
    print("Decision:  No.")
