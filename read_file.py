#open file.txt: create a file handler in read mode
data_file = open("file.txt")
#create an empty dictionary to store item: price entries
menu = {
  
}

for line_of_data in data_file: #use a loop to read the contents of the file line by line
    name_price = line_of_data.split(",") #split the data at the comma
    #get the menu item and the price from the list
    name = name_price[0] 
    price = name_price[1]
    #create an entry in the dictionary for the item and price
    menu[name] = price

print(menu)