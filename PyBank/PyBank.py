import csv

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

print(f"Reading file budget_data.csv completed.\n")

print(f"Financial Analysis")
print("----------------------------\n")
print(f"The total number of months is: {total_months}.")    
print(f"The total profit is: ${total_pl}.")
print(f"Average Change: ${avg_profit}")
print(f"Greatest Increase in Profits was in : with a maximum profit of {(month_changes[profit_changes.index(max(profit_changes))])} ${max(profit_changes)} ")
#Alternative print statement 
#print(f"Greatest Increase in Profits was in : with a maximum profit of {(month_changes[profit_changes.index(max(profit_changes))])} ${max_profit} ")
print(f"Greatest Decrease in Profits was in : with a minimum profit of {(month_changes[profit_changes.index(min(profit_changes))])} ${min(profit_changes)} ")
#Alternative print statement 
#print(f"Greatest Decrease in Profits was in : with a minimum profit of {(month_changes[profit_changes.index(min(profit_changes))])} ${min_profit} ")

#Analysis and Calculations (35 points)
#To receive all points, your code must:
#Include a calculation of the total number of months in the dataset. (2 points)
#Calculate the net total amount of Profit/Losses over the entire period. (3 points)
#Calculate the average of the changes in Profit/Losses over the entire period. (5 points)
#Calculate the greatest increase in Profits over the entire period (Date and Amount). (10 points)
#Calculate the greatest decrease in Losses over the entire period (Date and Amount). (10 points)
#Print the analysis and export the analysis to a text file that contains the final results. (5 points)
