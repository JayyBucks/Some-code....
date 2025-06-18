def get_menu(file_name:str) -> dict:
    data_file = open("file.txt")
    menu = {}
    for line_of_data in data_file: 
        name_price = line_of_data.split(",") 
        name = name_price[0] 
        price = name_price[1]
        menu[name] = price
    data_file.close()

def takeOrder(menu):
    """
    Takes a customer's order and calculates the total cost.

    Args:
        menu_dict: A dictionary containing menu items and their prices.
    """
    total_cost = 0.0 # Initialize total cost outside the loop
    print("\n------- Menu -------") # Display menu headers
    for item, price in menu.items(): # Iterate and print menu items and prices
        print(f"{item} | ${price:.2f}") # Format output for readability

    while True:
        order_item = input("\nEnter a menu item (or 'done' to finish): ").strip() # Prompt user for input and remove whitespace

        if order_item.lower() == 'done': # Check if user is finished
            break

        price = get_menu(menu) # Get item price

        if price is not None:
            total_cost += price # Add price to total
            print(f"{order_item} added to order.")
        else:
            print("Invalid menu item.")

    print("\nOrder Summary:")
    print(f"Total cost: ${total_cost:.2f}")

# Main program execution:
menu_file = "file.txt"
menu_data = {}

try:
    with open(menu_file, 'r') as file: # Open file for reading
        for line in file:
            item, price = line.strip().split(',') # Split each line into item and price
            menu_data[item.strip()] = float(price.strip()) # Convert price to float and store in dictionary
except FileNotFoundError: # Handle case if file is not found
    print(f"Error: Menu file '{menu_file}' not found.")
except ValueError: # Handle errors in file format
    print(f"Error: Invalid format in menu file '{menu_file}'. Ensure each line is 'item,price'.")

if menu_data: # Only proceed if menu data was loaded successfully
    takeOrder(menu_data) # Start the ordering process

