import os
import csv

csvpath = os.path.join("..","Resources","budget_data.csv")
print(csvpath)
with open(csvpath,'r') as csvhandle: