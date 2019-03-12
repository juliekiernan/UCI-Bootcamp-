import os
import csv
import datetime

PyBankPath = os.path.join('..', "PyBank", "PyBank_HW2.csv")
#define variables
total_months = 0
net_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(PyBankPath, newline="") as PyBankData:
    bankreader = csv.reader(PyBankData, delimiter=",")
    # Read each row of data after the header
    bankheader = next(bankreader)
    # print(f"CSV Header: {bankheader}")
    # for row in bankreader:
        #print(row)

    # Read first row (track changes)
    first_row = next(bankreader)
    total_months += 1
    net_pl += int(first_row[1])
    value = int(first_row[1])

    # Go through each row of data after the header & first row
    for row in bankreader:
        # Keep track of dates
        dates.append(row[0])

        # Calculate change, then add to list of changes
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        # Total number of months in dataset
        total_months += 1

        # Net total of "P/L over entire period"
        net_pl = net_pl + int(row[1])

    # Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Lowest increase in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits) / len(profits)

# Display info
print("Financial Analysis")
print("----------")
print(f"Total Months: {str(total_months)}")
print(f"Net Total: ${str(net_pl)}")
print(f"Average Change: ${str(round(avg_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Losses: {worst_date} (${str(greatest_decrease)})")

# Exporting to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Net Total: ${str(net_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change, 2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Losses: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))








