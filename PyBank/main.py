import os
import csv

# path to data file
csvpath = os.path.join("Resources","budget_data.csv")
print(csvpath)
with open(csvpath,'r') as csvhandle:
    budgetcsv = csv.reader(csvhandle)
    header =next(budgetcsv)
    # capturing first month and P/L from csv file
    previous_month, month_PL_str = next (budgetcsv)
    previous_month_PL = int(month_PL_str)
    # initializing variables
    Total_months = 1
    Total = previous_month_PL
    Total_PL_change = 0
    Greatest_increase = 0
    Greatest_increase_month = ''
    Greatest_decrease = 0
    Greatest_decrease_month = ''
    
    for row in budgetcsv:
        
        current_month = row[0]
        current_month_PL = int(row[1])
        
        Total += current_month_PL
        Total_months += 1
       
        # calculating P/L change between months
        PL_change = current_month_PL - previous_month_PL
        # capturing Greatest increase and decrease in P/L, also capturing corresponding months
        if PL_change > Greatest_increase:
            Greatest_increase = PL_change
            Greatest_increase_month = current_month
        if PL_change < Greatest_decrease:
            Greatest_decrease = PL_change
            Greatest_decrease_month = current_month
        
        # reset current month to previous month
        previous_month_PL = current_month_PL
        Total_PL_change+=PL_change

# output to terminal and text file
print('-------------------------------------------------------------------------------')
print('Financial Analysis')
print('-------------------------------------------------------------------------------')
print(f'Total Months: {Total_months}')
print(f'Total: {Total}')
print(f'Average Change: {round(Total_PL_change/(Total_months-1),2)}')
print(f'Greatest Increase in Profits: {Greatest_increase_month}  ($ {Greatest_increase})')
print(f'Greatest Decrease in Profits: {Greatest_decrease_month}  ($ {Greatest_decrease})')
print('-------------------------------------------------------------------------------')

with open('./Analysis/Results.txt','w') as txthandle:
    txthandle.write('------------------------------------------------------------------------------- \n')
    txthandle.write('Financial Analysis \n')
    txthandle.write('------------------------------------------------------------------------------- \n')
    txthandle.write(f'Total Months: {Total_months} \n')
    txthandle.write(f'Total: {Total} \n')
    txthandle.write(f'Average Change: {round(Total_PL_change/(Total_months-1),2)} \n')
    txthandle.write(f'Greatest Increase in Profits: {Greatest_increase_month}  ($ {Greatest_increase}) \n')
    txthandle.write(f'Greatest Decrease in Profits: {Greatest_decrease_month}  ($ {Greatest_decrease}) \n')
    txthandle.write('------------------------------------------------------------------------------- \n')