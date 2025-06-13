def season(month:int):
    if month == 12 or month == 1 or month == 2:
        return "Winter"
    elif month == 3 or month == 4 or month == 5:
        return "Spring"
    elif month == 6 or month == 7 or month == 8:
        return "Summer"
    elif month == 9 or month == 10 or month == 11:
        return "Fall"
    else:
        print("Invalid number!")

def season_2(month:int):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Fall"
    else:
        print("Invalid number!")

def month():
    while True:
        try:
            month = int(input("Enter the number of the month: "))
            if month <= 0 or month > 12:
                print("ERROR: Invalid Number!")
                continue
            else:
                break
        except:
            print("ERROR: Invalid Number!")
            continue
    return month
while True:
    month_number = month()
    season_name = season_2(month_number)
    print(f"It is {season_name}!")
    do_again = input("Would you like to run the program again? [y/n]: ")
    if do_again.lower() == "y" or do_again.lower() == "yes":
        continue
    else:
        break

