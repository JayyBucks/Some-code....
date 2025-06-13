a = 7
b = 4
if a > 4: 
    b = b + 2

print(a + b)
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{a} is less than {b}!")
else:
    print(f"{a} is equal to {b}")

test_score = int(input("Enter you test score: "))
if test_score > 100 or test_score < 0:
    print("Invalid test score!")
elif test_score >= 90:
    print("You got an A!")
elif test_score >= 80:
    print("You got a B!")
elif test_score >= 70:
    print("You got a C!")
elif test_score >= 60:
    print("You got a D!")
else:
    print("You FAILED!!!")

month = int(input("Enter the number of the month: "))
if month == 12 or month == 1 or month == 2:
    print("It is Winter!")
elif month == 3 or month == 4 or month == 5:
    print("It is Spring!")
elif month == 6 or month == 7 or month == 8:
    print("It is Summer!")
elif month == 9 or month == 10 or month == 11:
    print("It is Autumn/Fall!")
else:
    print("Invalid number!")