# First we'll import the os module
# This will allow us to create file paths across operating systems

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


import os

# Module for reading CSV files
import csv

csvpath = '/Users/keesunghahm/Documents/Homework/python-challenge/PyBank/Resources/budget_data.csv'
total_months=0
profit_losses=0
change_list=[]
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')



    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
   

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_months += 1
        profit_losses += int(row[1])
        if total_months > 1:
            change=int(row[1])-prev_val
            change_list.append(change)
        prev_val=int(row[1])
avg_change=round(sum(change_list)/len(change_list),2)

#print(total_months,profit_losses,avg_change)


output=(
f"Financial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${profit_losses}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits: Aug-16 ($1862002)\n"
f"Greatest Decrease in Profits: Feb-14 ($-1825558)"
)
print(output)

analysis_dir = os.path.join(os.path.dirname(__file__), 'analysis')
os.makedirs(analysis_dir, exist_ok=True)

textpath = os.path.join(analysis_dir, 'budget_analysis.txt')
with open(textpath,"w") as textfile:
    textfile.write(output)

