# a = 7
# b = 4
# if a > 4:
#     b = b + 2

# print(a + b)
# if a > b:
#     print(f"{a} is greater than {b}")
# elif b > a:
#     print(f"{a} is less than {b}!")
# else:
#     print(f"{a} is equal to {b}")

test_score = int(input("Enter you test score: "))

if test_score >= 90:
    print("You got an A!")
elif 90 > test_score >= 80:
    print("You got a B!")
elif 80 > test_score >= 70:
    print("You got a C!")
elif 70 > test_score >= 60:
    print("You got a D!")
else:
    print("You FAILED!!!")