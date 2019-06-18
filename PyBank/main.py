import os
import csv

#Path to collect the data from
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

#Define variables
months = 0
profit = 0
differences = []
month_count = []
inc_profit = 0
dec_profit = 0
inc_month = 0
dec_month = 0


#Open csv file, skip header row and begin on next line
with open(pybank_csv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    next(csvreader)
    row = next(csvreader)

#Calculate count of months total profit
    old_profit = int(row[1])
    months = months + 1
    profit = profit + int(row[1])
    inc_profit = int(row[1])
    inc_month = row[0]

#Setting the loop for the rows
    for row in csvreader:
        months = months + 1
        profit = profit + int(row[1])
    
#Calculate the difference between month over month profit/losses
        difference = int(row[1]) - old_profit
        differences.append(difference)

 #Count month total from prior month's profit        
        old_profit = int(row[1])
        month_count.append(row[0])

#Calculate the max increase
        if int(row[1]) > inc_profit:
            inc_profit = int(row[1])
            inc_month = row[0]

#Calculate the min decrease
        if int(row[1]) < dec_profit:
            dec_profit = int(row[1])
            dec_month = row[0]

#Calculate the average change in profit/loss
    average_change = sum(differences)/len(differences)  

#Shows max increase and min decrease
    max_diff = max(differences)     
    min_diff = min(differences)   

 #Print values 
    print("Financial Analysis")
    print("Total Months:" + " " + str(months))
    print("Total:" + " " + "$" + str(profit))
    print("Average Change:" +"$" + " " + str(int(average_change)))
    print("Greatest Increase in Profits: " + " " + str(inc_month) + " " + "($" + str(max(differences)) + ")")
    print("Greatest Decrease in Profits: " + " " + str(dec_month) + " " + "($" + str(min(differences)) + ")")


#Create a .txt file for output of financial analysis 
with open('financial_analysis.txt', "w") as text:
    text.write("Financial Analysis" + "\n")    
    text.write("---------------------------\n\n")   
    text.write("Total Months: " + str(months) + "\n")    
    text.write("Total: " + "$" + str(profit) + "\n")
    text.write("Average Change:" + " " + "$" + " " + str(int(average_change))+ "\n") 
    text.write("Greatest Increase in Profits:" + " " + str(inc_month) + " "  + "($" + str(max(differences)) + ")\n")
    text.write("Greatest Decrease in Profits:" + " " + str(dec_month) + " "  + "($" + str(min(differences)) + ")\n")       





      







