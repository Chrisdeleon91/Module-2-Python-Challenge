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

# added variables
#total_months = 0
count = 0
revenue = 0
cogs = 0
profit = 0

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sales in sales:

    #Calculation of the total number of months in the dataset 
    #total_months += 1  

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,menu_item
    # @TODO: Initialize sales data variables
    Line_Item_ID = sales[0]
    Date = sales[1]
    Credit_Card_Number = sales[2]
    Quantity = int(sales[3])
    menu_item = sales[4]
   
    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report:
        report[menu_item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}
  
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for product in menu:
        
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = product[0]
        category = product[1]
        description = product[2]
        price = float(product[3])
        cost = float(product[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to any of the items in the menu, then begin tracking metrics for that item
        if menu_item == item:
            
            # @TODO: Print out matching menu data
            print(item)
            
            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any of the item in the menu data, therefore no match
        else:
            print(f"{Line_Item_ID} does not equal {item}! NO MATCH!")

    # @TODO: Increment the row counter by 1
    row_count += 1   

# @TODO: Print total number of records in sales data
print(len(report))

# @TODO: Write out report to a text file (won't appear on the command line output)
outputtxt = Path("output.txt")

with open(outputtxt, 'w') as outputfile:
    outputfile.wirte(f"{report}\n")
