# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvfile:
        #Append the row to the menu 
        menu.append(row)
                           
# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader)
    for row in csvfile:
        #Append the row to the menu 
        sales.append(row)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0
total_months = 0
# @TODO: Loop over every row in the sales list object
for row in sales:

    

    #Calculation of the total number of months in the dataset 
    total_months += 1  


    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    Line_Item_ID = row[0]
    Date = row[1]
    Credit_Card_Number = row[2]
    Quantity = row[3]
    Menu_Item = row[4]
   
    

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sales not in report.keys():
        report[sales_item] = {"01-count": count, "02-revenue": revenue, "03-cost": cost, "04-profit": profit}
    else:
        report[sales_item]["01-count"] += count
        report[sales_item]["02-revenue"] += revenue
        report[sales_item]["03-cost"] += cost
        report[sales_item]["04-profit"] += profit
        

    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for row in menu:
        
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = row[0]
        category = row[1]
        description = row[2]
        price = row[3]
        cost = row[4]

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if report[sales_item] not in report.keys():
            #report[sales_item] = {"01-count": count, "02-revenue": revenue, "03-cost": cost, "04-profit": profit}
        
            
         
        
            # @TODO: Print out matching menu data
            print(sales_item)
            




            # @TODO: Cumulatively add up the metrics for each item key
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cost"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity  




        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print(f"{sales_tem} does not equal {item}! NO MATCH!")


    # @TODO: Increment the row counter by 1
    row_count += 1   

# @TODO: Print total number of records in sales data
print(len(report))



# @TODO: Write out report to a text file (won't appear on the command line output)
outputtxt = Path("output.txt")

with open(outputtxt, 'w') as outputfile:
    outputfile.write(f"hello")
    outputfile.wirte(report)
