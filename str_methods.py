my_name = "Gerard"
print(my_name.capitalize())
print(my_name.upper())
last_name = "WILLIAMS"
print(f"{my_name.lower()} {last_name.lower()}")
print("\nUsing startswift() method")
print(my_name.startswith("g") or my_name.startswith("G"))
if ((not my_name.startswith("gerard")) and (not my_name.startswith("Gerard"))):
    print(f"You spelled {my_name} incorrectly")
else:
    print(f"You spelled {my_name} correctly")
print(f"\nUsing endswith() method")
print(f"{my_name} ends with 'ard': {my_name.endswith("ard")}")
print("\nUsing the find() method")
search_letter = "ard"
if(my_name.find(search_letter) == -1):
    print(f"There is no {search_letter} in {my_name}")
else:
    print(f"The '{search_letter}' is at index {my_name.find(search_letter)}")
print("\nLoop thourgh a string")
for letter in my_name:
    print(letter)
    # print(my_name)
print(f"{my_name} has {len(my_name)} letters")
for letter_index in range(len(my_name)):
    print(f"Letter {letter_index + 1}: {my_name[letter_index]}")
print("\n\n")
sentence = "I have a dog. My dog is cute. Do you want a dog?"
search_word = "dog"
start_index = 0
number_of_dogs = 0
while True:
    dog_index = sentence.find(search_word, start_index)
    if dog_index == -1:
        break
    else:
        number_of_dogs += 1
        start_index = dog_index + 1
print(f"There are {number_of_dogs} {search_word}(s) in the sentence!")
print("\nUsing the split() method!")
car_info = "Lamborghini,Aventador,2017,500000,6.5\n"
car_data = car_info.split(",")
print(car_data)
make = car_data[0]
model = car_data[1]
year = int(car_data[2])
price = float(car_data[3])
engine = float(car_data[4])
print(f"{year} {make} {model}")
print(f"Price: ${price} - Engine: {engine}L")
print((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("yo")))))))))))))))))))))))))))))))))))))))))))))))))))))))))))