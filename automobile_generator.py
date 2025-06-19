from Automobile import Automobile

auto1 = Automobile("Honda", "Accord", "23456", 2.2, 2017, "Alice", "Blue")
auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, 2022, "Bob", "Black")

auto2.__year = 2024

auto1.owner = "John"

auto_list = []
auto_list.append(auto1)
auto_list.append(auto2)

for auto in auto_list:
    auto.printData()

print(f"Auto 1 is {auto1.get_age()} years old")