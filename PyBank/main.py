#import os and csv
import os
import csv

#assign csvfile to path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#make lists
profit = []
monthly_change = []
month = []

#initialize variables
count = 0
total_profits = 0
total_change_profits = 0
initial_profit = 0


#Read into csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:

        #use count func. to count rows minus header
        count = count + 1

        #append months to row[0] to collect differences in prof.
        month.append(row[0])

         #append profit col. then calc. total_profit
        profit.append(row[1])
        total_profits = total_profits + int(row[1])

        #calc avg change in prof. month/month
        final_profit = int(row[1])
        montly_change_profits = final_profit - initial_profit

        #store monthly changes in list
        monthly_change.append(montly_change_profits)

        total_change_profits = total_change_profits + montly_change_profits
        initial_profit = final_profit

        #calc avg change in profits
        average_change_profits = (total_change_profits/count)
        #Find the max and min change in profits and the corresponding dates these changes were obeserved
        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)

        increase_date = month[monthly_change.index(greatest_increase_profits)]
        decrease_date = month[monthly_change.index(greatest_decrease_profits)]
    
    #print results 
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profits))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open('analysis/finalcial_analysis.txt', 'w', newline='') as textfile:
    writer = csv.writer(textfile)
    writer.writerow(["----------------------------------------------------------"])
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------------------------------------"])
    writer.writerow(["Total Months: " + str(count)])
    writer.writerow(["Total Profits: " + "$" + str(total_profits)])
    writer.writerow(["Average Change: " + "$" + str(int(average_change_profits))])
    writer.writerow(["Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")"])
    writer.writerow(["----------------------------------------------------------"])

