#This file will demonstrate how for loops work


# for number in range(1,111,2):
#     print(number)

start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
# for number in range(start, stop + 1):
#     print(number)

for table in range(start, stop + 1):
    print(f"\nDisplaying the Multiplication table for {table}\n------------------------------------------")
    for multiple in range(1, 13):
        product = table * multiple
        print(f" {table} x {multiple} = {product}")