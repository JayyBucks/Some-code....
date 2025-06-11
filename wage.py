def wage_calculator(wage, hours):
    if 24 > hours > 0:
        if wage > 0:
            daily_wage = wage * hours
            salery = daily_wage * 350
            tax_amount = 0.12 * salery
    else:
        print("ERROR: Hours worked daily must be less than 24!")
    taxed_salery = salery - tax_amount
    print(f"Pay Advice\n----------\nYour Hours Worked: {hours}\nYour Hourly Wage: ${wage}\nYour Wages Before Taxes: ${salery:.2f}\nYour Tax Amount: ${tax_amount:.2f}\nYour Annual Salery: ${taxed_salery:.2f}")
def annual_salery ():      
    hours = float(input("Average daily work hours: "))
    wage = float(input("Hourly wage: "))
    wage_calculator(wage, hours)
annual_salery()
while True:
    redo_answer = input("Would you like to do another calculation? [y/n]: ")
    if redo_answer.lower() == "y" or redo_answer.lower() == "yes":
        annual_salery()
    else:
        break