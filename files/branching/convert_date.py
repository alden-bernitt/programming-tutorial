print("Please only enter numeric values.")

month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

month_name = "Unknown"
if month == 1:
    month_name = "January"
elif month == 2:
    month_name = "February"
elif month == 3:
    month_name = "March"
elif month == 4:
    month_name = "April"
elif month == 5:
    month_name = "May"
elif month == 6:
    month_name = "June"
elif month == 7:
    month_name = "July"
elif month == 8:
    month_name = "August"
elif month == 9:
    month_name = "September"
elif month == 10:
    month_name = "October"
elif month == 11:
    month_name = "November"
elif month == 12:
    month_name = "December"

print(month_name, day, year)
