import csv
from pathlib import Path

#Initialize variables
total_months = 0
total_pl = 0
profit_changes = []
month_changes = []
previous_profit = None

total_profit = 0
count_profit = 0
min_profit = 0
max_profit = 0

#Analyze the records
with open("./resources/budget_data.csv", 'r') as file:
#returns the next line after the first line, "moves pointer" to second line in a sense
    csvreader = csv.reader(file)
    header = next(csvreader)
    
    for month, pl in csvreader:
    #Calculation of the total number of months in the dataset 
        total_months += 1
        
    #The net total amount of Profit/Losses over the entire period
    #Convert the number in the text file from string to int
        current_profit  = int(pl)
        total_pl += current_profit  
        
    #The average of the changes in Profit/Losses over the entire period    
         #if this is not the first month  
        if previous_profit is not None:
             #find difference between this month and the last one         
            profit_differences = current_profit - previous_profit
            #append to changes list
            profit_changes.append(profit_differences)
            month_changes.append(month)
        #take what was just used as current_profit and make it the new previous then repeat the loop 
        previous_profit = current_profit

#Iterate over a list to find the min and max salaries
for profit in profit_changes:

    # Sum the total and count variables
    total_profit += profit
    count_profit += 1

    # Logic to determine min and max salaries
    if min_profit == 0:
        min_profit = profit
    #The greatest increase in profits (date and amount) over the entire period
    elif profit > max_profit:
        max_profit = profit #25 Feb-2012  
    #The greatest decrease in losses (date and amount) over the entire period       
    elif profit < min_profit:
        min_profit = profit #44 Sept-2013 
        


# Calculate the average salary, round to the nearest 2 decimal places
avg_profit = round(total_profit / count_profit, 2)

avg_profit_total = round(sum(profit_changes) / len(profit_changes),2)

#Alternative print statement 
#print(f"Average Change: ${avg_profit}")

avg_profit_total = round(sum(profit_changes) / len(profit_changes),2)

#Alternative print statement 
#print(f"Greatest Increase in Profits was in : with a maximum profit of {(month_changes[profit_changes.index(max(profit_changes))])} ${max_profit} ")

#Alternative print statement 
#print(f"Greatest Decrease in Profits was in : with a minimum profit of {(month_changes[profit_changes.index(min(profit_changes))])} ${min_profit} ")

outputtxt = Path("output.txt")

with open(outputtxt, 'w') as outputfile:
    outputfile.write(f"Financial Analysis\n")
    outputfile.write(f"----------------------------\n")
    outputfile.write(f"The total number of months is: {total_months}.\n")  
    outputfile.write(f"The total profit is: ${total_pl}.\n")
    outputfile.write(f"Average Change: ${avg_profit_total}\n")
    outputfile.write(f"Greatest Increase in Profits was in : with a maximum profit of {(month_changes[profit_changes.index(max(profit_changes))])} ${max(profit_changes)}\n")
    outputfile.write(f"Greatest Decrease in Profits was in : with a minimum profit of {(month_changes[profit_changes.index(min(profit_changes))])} ${min(profit_changes)}\n")
    
