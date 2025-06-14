amount_due = 50
absolute_value = -1
while amount_due > 0: #display updated amount
    print(f"Vending Maching\n---------------\nAmount Due: {amount_due}\n") #display amount due
    try:
        user_input = int(input("Insert Coins: \n")) #prompt user to insert coins to reduce amount due then convert that input into an int
        #need a system to show the subtraction aspect of it when coins are added to the machine
        #accept inputs of 1, 5, 10, 25
        #ignore invalid inputs
        if user_input == 1:
            amount_due = amount_due - 1
        elif user_input == 5:
            amount_due = amount_due - 5
        elif user_input == 10:
            amount_due = amount_due - 10
        elif user_input == 25:
            amount_due = amount_due - 25
        if amount_due <= 0: #if the user inserts atleast 50 cents, then output how much the user is owed
            print("Vending Maching\n---------------\nAmount Owed:", amount_due * absolute_value) #then end the program
    except:
        continue