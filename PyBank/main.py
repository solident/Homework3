#required stuffs
import os
import csv
#path to csv file

datapath=os.path.join('Resources', 'budget_data.csv')

totalmonths = 0
totalloss = 0
value = 0
change = 0
dates = []
profits = []

#Read csv
with open(datapath, newline="") as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    # Reading header
    csvheader = next(csvreader)
    # Go tofirst row


    firstrow = next(csvreader)

    #month counter

    totalmonths += 1

    # Add profit and loss counter

    totalloss += int(firstrow[1])
    value = int(firstrow[1])
  
    for row in csvreader:

        
        dates.append(row[0])

       
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

   
        totalmonths += 1

        # The total amount of profit/ losses

        totalloss = totalloss + int(row[1])

        # Average changes 

        avgchange = sum(profits)/len(profits)
  # The greatest increase 
    greatestincrease = max(profits)
    greatestincindex = profits.index(greatestincrease)
    greatestincdate = dates[greatestincindex]

    # The greatest decrease 
    greatestdecrease = min(profits)
    greatestdecindex = profits.index(greatestdecrease)
    greatestdecdate = dates[greatestdecindex]

#Printing the output
printoutput = (
    f"\nFinancial Analysis\n"
    f"\n-------------------------------------\n"
    f"Total Months: {str(totalmonths)}\n"
    f"Total: ${str(totalloss)}\n"
    f"Average Change: ${str(round(avgchange,2))}\n"
    f"Greatest Increase in Profits: {greatestincdate} (${str(greatestincrease)})\n"
    f"Greatest Decrease in Profits: {greatestdecdate} (${str(greatestdecrease)})\n")
print(printoutput)

# Exporting file

results = os.path.join('Analysis', 'pyBankresults.txt')


pyBankresults = open(results, "w")

line1 = "Financial Analysis"
line2 = "\n------------------------------------------\n"
line3 = str(f"Total Months: {str(totalmonths)}")
line4 = str(f"Total: ${str(totalloss)}")
line5 = str(f"Average Change: ${str(round(avgchange,2))}")
line6 = str(
    f"Greatest Increase in Profits: {greatestincdate} (${str(greatestincrease)})")
line7 = str(
    f"Greatest Decrease in Profits: {greatestdecdate} (${str(greatestdecrease)})")
pyBankresults.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))