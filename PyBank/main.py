# PyBank: To analyze financial records

import os
import csv

# Relative file location
input_file = os.path.join("Resources", "budget_data.csv")

# Open and read budget_data
with open(input_file) as input_data:
    csv_reader = csv.reader(input_data, delimiter=",")

    # Store the header row
    csv_header = next(input_data)   

    # Determine first profit/loss value
    first_row = next(input_data) 
    first_profit = int(first_row.split(',')[1])

    # Start loop from first profit/loss value
    count_months = 1
    sum_profit = first_profit
    previous_profit = first_profit
    max_increase = 0
    max_decrease = 0
    sum_changes = 0

    for row in csv_reader:

        # Count no. of months
        count_months = count_months + 1

        # Running total profit/losses
        sum_profit = sum_profit + int(row[1])

        # Running total profit/loss changes
        change = int(row[1])-previous_profit
        sum_changes = sum_changes + change

        # Set current profit as previous profit for next change calculation
        previous_profit = int(row[1])

        # Determine and update only when increase/decrease is maximum
        if change > 0 and change >  max_increase:
            max_increase = change
            max_incdate = row[0]
        elif change < 0 and change < max_decrease:
            max_decrease = change
            max_decdate = row[0]

print("Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months: {count_months}") 
print(f"Total Profit/Losses: ${sum_profit}")
print("Average Change: $" + str(round(sum_changes/(count_months-1),2)))
print("Greatest Increase in Profits: " + max_incdate + " ($" + str(max_increase) + ")")
print("Greatest Decrease in Profits: " + max_decdate + " ($" + str(max_decrease) + ")")
            

# Specify the file to write to
output_file = os.path.join("analysis", "result.txt")

# Open the file using "write" mode.
with open(output_file, 'w') as txtfile:

    # Write text to file
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------------------------------\n")
    txtfile.write(f"Total Months: {count_months}\n")
    txtfile.write(f"Total Profit/Losses: ${sum_profit}\n")
    txtfile.write("Average Change: $" + str(round(sum_changes/(count_months-1),2)) + "\n") 
    txtfile.write("Greatest Increase in Profits: " + max_incdate + " ($" + str(max_increase) + ")\n")
    txtfile.write("Greatest Decrease in Profits: " + max_decdate + " ($" + str(max_decrease) + ")")

print("Result output to /PyBank/analysis/result.txt")
        