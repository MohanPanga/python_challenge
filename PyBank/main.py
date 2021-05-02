import os
import csv

csvpath = os.path.join(".","Resources","budget_data.csv")
print(csvpath)
with open(csvpath,'r') as csvhandle:
    budgetcsv = csv.reader(csvhandle)
    header =next(budgetcsv)
    Total_months = 0
    Total = 0
    Greatest_increase = 0
    Greatest_increase_month = ''
    Greatest_decrease = 0
    Greatest_decrease_month = ''
    for row in budgetcsv:
        monthly_PL = int(row[1])
        Total += monthly_PL
        Total_months += 1
        if monthly_PL > Greatest_increase:
            Greatest_increase = monthly_PL
            Greatest_increase_month = row[0]
        if monthly_PL< Greatest_decrease:
            Greatest_decrease = monthly_PL
            Greatest_decrease_month = row[0]

print('-------------------------------------------------------------------------------')
print('Financial Analysis')
print('-------------------------------------------------------------------------------')
print(f'Total Months: {Total_months}')
print(f'Total: {Total}')
print(f'Average Change: {Total/Total_months}')
print(f'Greatest Increase in Profits: {Greatest_increase_month}  ($ {Greatest_increase})')
print(f'Greatest Decrease in Profits: {Greatest_decrease_month}  ($ {Greatest_decrease})')
print('-------------------------------------------------------------------------------')