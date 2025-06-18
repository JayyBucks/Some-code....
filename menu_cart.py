def get_menu(file_name:str) -> dict:
    data_file = open("file.txt")
    menu = {}
    for line_of_data in data_file: 
        name_price = line_of_data.split(",") 
        name = name_price[0] 
        price = float(name_price[1])
        menu[name] = price
    data_file.close()
    return menu

def displayCart(cart:dict, menuItems:dict)->None:
    total = 0
    for item, quantity in cart.items():
        total += (menu_item[item] * quantity)
        print(f"{quantity} {item}(s): ${menu_item[item] * quantity:.2f}") 
    print(f"\nTotal: ${total:.2f}")

menu_item = get_menu("file.txt")

print("\n------- Menu -------") 

for item, price in menu_item.items():
    print(f"{item} | ${price:.2f}") 

item_cart = {}

while True:
    item = input("\nEnter Menu Item (or 'end' to finish): ").title()
    if item.lower() == "end":
            break
    if item not in menu_item:
        print(f"\nERROR: {item} not on the menu!")
        continue
    try:
         quantity = int(input("Quantity: "))
    except:
         print("\nERROR: Enter number for quantity!")
    if item not in item_cart:
        item_cart[item] = quantity
    else:
         item_cart[item] += quantity
    print(f"{item} added to order.")
    print("\nOrder Summary:")
    displayCart(item_cart, menu_item)