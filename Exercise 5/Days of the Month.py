#Create a dictionary for the number of days in each month
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}
#Ask the user to input the month number
month = int(input("Enter the month number (1-12): "))
#Check if the input is valid
if month in month_days:
    #Handle February for leap years
    if month == 2:
        year = int(input("Enter the year: "))
        #Check if it's a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"The number of days in February {year} is 29 (Leap Year).")
        else:
            print(f"The number of days in February {year} is 28.")
    else:
        print(f"The number of days in month {month} is {month_days[month]}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")