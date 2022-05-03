#Practice Project: investment calculator
print("Welcome to the Return on Investment Calculator!")

def main():
    values()
    check()
    calc()
    redo()

#get inputs for later calculations.    
def values():
    try:
        values.amount = float(input("enter initial amount invested: "))
    except:
        values.amount = -1
    try:
        values.per = float(input("enter return percentage: "))
    except:
        values.per = -1
    try:
        values.time = float(input("enter years invested: "))
    except:
        values.time = -1
        
#check and make sure inputs are usable and if not usable, ask for usable data.
def check():
    if values.amount < 0:
        print("Not a valid input for Amount Invested!")
        print("Please enter number with no commas.")
        print("Example: 15000 not 15,000.")
        values()
    if values.per < 0:
        print("Not a valid input for return percentage!")
        print("Please enter percentage with no added characters.")
        print("Example: 15 or 0.15, not 15%")
        values()
    if values.time < 0:
        print("Not a valid input for years invested!")
        print("Please enter number value of years.")
        print("Example: 5 not five")
        values()
        
#once inputs are in usable form, investment return and profit can be calculated. 
def calc():
    if values.per < 1:
        deci_per = values.per
    elif values.per > 1:
        deci_per = values.per * 0.01

    rpy = deci_per + 1
    total_return = round((values.amount * (rpy ** values.time)), 2)
    profit = round((total_return - values.amount), 2)

    print("after", + values.time, "years your investment will be worth", + total_return,"dollars!")
    print("that is", + profit, "total dollars in profit!")

#alows the program to be reused.
def redo():
    print("Would you like to calculate another return?")
    again = input("Type yes or no: ")

    if again == "yes":
        main()
    elif again == "no":
        print("Thank you for using our calculator!")
    else:
        print("not a valid input")
        redo()
    
main()

