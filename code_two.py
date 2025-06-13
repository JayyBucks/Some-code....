def lbs_to_kgs():
    while True:
        try:
            weight = float(input("How much do you weigh in pounds?\n"))
            if weight > 0:
                kilograms = weight/2.205
                print(f"You weigh {kilograms:.2f} kilograms!")
                break
            else:
                print("ERROR: Please enter a positive number!")
        except:
            print("ERROR: Please only enter a number!")
    return weight

def lbs_kgs(weight):
    weight_kgs = weight/2.205
    return weight_kgs

def positive_float_value():
    while True:
        try:
            num = float(input("Enter a number: \n"))
            if num > 0:
                break
            else:
                print("ERROR: Please enter a positive number!")
        except:
            print("ERROR: Please only enter a number!")
    return num
def main():
    lbs_to_kgs()
main()