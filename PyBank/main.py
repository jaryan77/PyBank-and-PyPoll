#import os and csv
import os
import csv

#assign csvfile to path
budget_csv = os.path.join('Resources', 'budget_data.csv')

#make lists
profit = []
monthly_change = []
month = []

# def print_table(budget_csv):
#      month = str(budget_csv[0])
#      profits = int(budget_csv[1])

#initialize variables
count = 0
total_profits = 0
total_change_profits = 0
initial_profit = 0




#Block of code for reading csv (warm-up)
with open(budget_csv) as csvfile:
     #csvreader = csv.DictReader(csvfile, delimiter=',')
     csvreader = csv.reader(csvfile, delimiter=',')
     header = next(csvreader)
     
     # def columns(csvreader):
     #      months = str(csvreader[0])
     #      profits = int(csvreader[1])


     # header = next(csvreader)
     # print(f"Financial Analysis:")
     # print("------------------------------")

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
      
     # print("----------------------------------------------------------")
     # print("Financial Analysis")
     # print("----------------------------------------------------------")
     # print("Total Months: " + str(count))
     # print("Total Profits: " + "$" + str(total_profits))
     # print("Average Change: " + "$" + str(int(average_change_profits)))
     # print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
     # print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
     # print("----------------------------------------------------------")

     greatest_increase = [increase_date, greatest_increase_profits]
     greatest_decrease = [decrease_date, greatest_decrease_profits]
     summary_table = {"Total Months":count,
          "Total Profits": total_profits,
          "Average Change": average_change_profits,
          "Greatest Increase in Profits": greatest_increase,
          "Greatest Decrease in Profits": greatest_decrease
          }
     print(summary_table)
     # month_count = 0

     # for row in csvreader:

     # total_months = sum(1 for row in csvreader)
     # print(f"Total Months: {total_months}")

     # total_profits = len(profits)
     # print(f"Total Profits: {total_profits}")

          
               
     # profits = {}
     # profits[sum(csvreader)[1]]
     # print(f"Total Profits: {profits}")

     #anything

     





     #create a dictionary for each column

     #conditional needed to calc avg change in profit/loss
     #for row in csvreader:

     #Add up values of Profit/Losses column, then average the sum
     # for row in csvreader:
     #      profits = float(sum(row[1]))
     #      print(f"Total Profits: {profits})

     # for row in csvreader:
     #      print(row)

         




    



