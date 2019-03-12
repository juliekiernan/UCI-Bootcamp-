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

        # Net total of P/L over entire period
        net_pl = net_pl + int(row[1])

    # Greatest increase in profits
    biggest_increase = max(profits)
    pindex_values = profits.index(biggest_increase)
    entrydate = dates[pindex_values]

    # Lowest increase in profits
    smallest_increase = min(profits)
    lindex_values = profits.index(smallest_increase)
    worst_date = dates[lindex_values]

    # Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits) / len(profits)

# Display info
print("Financial Analysis")
print("----------")
print(f"Total Months: {str(total_months)}")
print(f"Net Total: ${str(net_pl)}")
print(f"Average Change: ${str(round(avg_change, 2))}")
print(f"Greatest Increase in Profits: {entrydate} (${str(biggest_increase)})")
print(f"Greatest Decrease in Losses: {worst_date} (${str(smallest_increase)})")

# Exporting to .txt file
output = open("output.txt", "w")

output.write("Financial Analysis" +'\n')
output.write("---------------------" +'\n')
output.write(f"Total Months: " + "{str(total_months)}" + '\n')
output.write(f"Net Total: " + "${str(net_pl)}" +  '\n' )
output.write(f"Average Change: " + "${str(round(avg_change, 2))}" + '\n')
output.write(f"Greatest Increase in Profits: " + "str{entrydate}" + "(${str(biggest_increase)})" +  '\n')
output.write(f"Greatest Decrease in Losses: " + "str{worst_date}" + "(${str(smallest_increase)})" +  '\n')

