# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
import json
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #Append the row to the menu 
        menu.append(row)
                           
# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        #Append the row to the menu 
        sales.append(row)


# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for row in sales:

    #Calculation of the total number of months in the dataset -- this doesn't make sense this is wrongly put in from PyBank
      
    # Line_Item_ID,Date,Credit_Card_Number,quantity,menu_item
    # @TODO: Initialize sales data variables
    Line_Item_ID = row[0]
    Date = row[1]
    Credit_Card_Number = row[2]
    quantity = int(row[3])   
    menu_item = row[4]
   
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report.keys():
        report[menu_item] = {"01-count": 0,
                             "02-revenue": 0,
                             "03-cost": 0,
                             "04-profit": 0}
  
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for row in menu:
        # Item, Category, Description, Price, Cost
        # @TODO: Initialize menu data variables
        item = row[0]
        category = row[1]
        description = row[2]
        price = float(row[3])
        cost = int(row[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost
        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        # @TODO: Cumulatively add up the metrics for each item key
        if item == menu_item:
            # @TODO: Print out matching menu data   
            print(f"{menu_item} matches with {item}!") 
            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cost"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity 
        # @TODO: Else, the sales item does not equal any of the items in the menu data, therefore no match    
        else:
            print(f"{menu_item} does not equal {item}! NO MATCH!")
                
     
    # @TODO: Increment the row counter by 1
    row_count += 1   

# # @TODO: Print total number of records in sales data
print(f"The total number of records in sales dats i {row_count}!")

# @TODO: Write out report to a text file (won't appear on the command line output)
outputtxt = Path("output.txt")

with open(outputtxt, 'w') as outputfile:
    outputfile.write(f"{json.dumps(report)}")
