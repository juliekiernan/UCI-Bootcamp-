import os
import csv
import datetime

PyBankPath = os.path.join('..', "PyBank", "PyBank_HW2.csv")
#define varables
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(PyBankPath, newline="") as PyBankData:
    bankreader = csv.bankreader(PyBankData, delimiter="")
    bankheader = next(bankreader)

    # Reading the first row (so that we track the changes properly)
    first_row = next(bankreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    # Going through each row of data after the header & first row
    for row in bankreader:
        # Keeping track of the dates
        dates.append(row[0])

        # Calculate the change, then add it to list of changes
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        # Total number of months in dataset
        total_months += 1

        # Net total of "P/L over entire period"
        total_pl = total_pl + int(row[1])

    # Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease (lowest increase) in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits) / len(profits)

# Displaying information
print("Financial Analysis")
print("----------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# Exporting to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change, 2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))








