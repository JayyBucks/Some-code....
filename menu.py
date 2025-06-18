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

menu_item = get_menu("file.txt")
total = 0
print("\n------- Menu -------") 
for item, price in menu_item.items():
    print(f"{item} | ${price:.2f}") 
while True:
    item = input("\nEnter Menu Item (or 'end' to finish): ")
    if item.lower() == "end":
            break
    try:
        total += menu_item[item.title()]
    except:
        continue
    print(f"{item} added to order.")
    print("\nOrder Summary:")
    print(f"Total: ${total:.2f}")