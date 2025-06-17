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
    try:
        math = input("Math Expression: ").split() #needs to have 2 splits or a length of 3: x y z
        if len(math) != 3:
            print("\nInvalid format!")
            time.sleep(1)
            print("\nTry again...\n")
            time.sleep(1)
            continue
        x = int(math[0])
        y = math[1]
        z = int(math[2])
        if y not in ["+", "-", "/", "*"]: #y needs to be one of the math operators
            print("\nInvalid math operator!")
            time.sleep(1)
            print("\nTry again...\n")
            time.sleep(1)
            continue
        if y == "/" and (x == 0 or z == 0):
            print("\nInvalid input! You can't divide by zero!") 
            time.sleep(2)
            print("\nTry again...\n")
            time.sleep(1)
        else:
            break
    except:
        print("\nInvalid input! Please enter an integer for x and z!") 
        time.sleep(2)
        print("\nTry again...\n")
        time.sleep(1)
if y == "/":
    equation = x / z
elif y == "*":
    equation = x * z
elif y == "+":
    equation = x + z
elif y == "-":
    equation = x - z
print(f"{int(x)} {y} {int(z)} = {float(equation):.2f}")  