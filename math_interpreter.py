import time
print("This is a basic calculator...\n")
time.sleep(2)
print("You must input in the form of x y z...\n")
time.sleep(2)
print("For example, 1 + 2, where x is 1, y is +, and z is 2\n")
time.sleep(3)
print("You can only use these math operators:\nAddition: '+'\nSubtraction: '-'\nMultiplication: '*'\nDivision: '/'\n")
time.sleep(2)
print("You must have a space between each value: 'x y z'\n")
time.sleep(2)

while True:
    math = float(input("Math Expression: "))
    if len(math.split()) != 3:
        print("Invalid format!")
        print("\nTry again...")
#needs to have 2 splits or a length of 3: x y z
#x and z need to be integers
#y needs to be one of the math operators
#while True
    #prompt the user for and expression
    #use the split() method to get the parts of the expression
    #check the length of the list treturned from .split
    #if len(list) not = 3
        #output Incorrect format message and reprompt(continue)
    #try:
        #get X and Y and Z values from the list
        #and check if X and Z are intergers by converting to int()
    #except:
        #output Error message and reprompt
    #Check that operator is +, -, *, /
    #if y not in ["+", "-", "*", "/"]:
        #output Error message and reprompt(continue)
    