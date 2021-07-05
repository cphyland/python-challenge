import os
import csv

budget_data = os.path.join('.', 'Resources', 'budget_data.csv')


total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reding header row
    csv_header = next(csvreader)

    #reading the first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #looping through each row
    for row in csvreader:
        # dates
        dates.append(row[0])
        
        # change in values
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # total number of months
        total_months += 1

        # p&l over entire period
        total_pl = total_pl + int(row[1])

    # average change over period
    avg_change = sum(profits)/len(profits)

    # greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # greatest decrease in losses
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

# print summary
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# save to text (.txt) file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
