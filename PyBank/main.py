import os
import csv

csvpath = os.path.join(".","Resources","budget_data.csv")
print(csvpath)
with open(csvpath,'r') as csvhandle:
    budgetcsv = csv.reader(csvhandle)
    header =next(budgetcsv)
    previous_month, month_PL_str = next (budgetcsv)
    previous_month_PL = int(month_PL_str)
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
        PL_change = current_month_PL - previous_month_PL
        if PL_change > Greatest_increase:
            Greatest_increase = PL_change
            Greatest_increase_month = current_month
        if PL_change < Greatest_decrease:
            Greatest_decrease = PL_change
            Greatest_decrease_month = current_month
        previous_month_PL = current_month_PL
        Total_PL_change+=PL_change
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
    # txtfile = csv.writer(txthandle,delimiter=' ')
    txthandle.write('------------------------------------------------------------------------------- \n')
    txthandle.write('Financial Analysis \n')
    txthandle.write('------------------------------------------------------------------------------- \n')
    # txtfile.writerow(f'Total Months: {Total_months}')
    txthandle.write(f'Total: {Total} \n')
    txthandle.write(f'Average Change: {round(Total_PL_change/(Total_months-1),2)} \n')
    txthandle.write(f'Greatest Increase in Profits: {Greatest_increase_month}  ($ {Greatest_increase}) \n')
    txthandle.write(f'Greatest Decrease in Profits: {Greatest_decrease_month}  ($ {Greatest_decrease}) \n')
    txthandle.write('------------------------------------------------------------------------------- \n')