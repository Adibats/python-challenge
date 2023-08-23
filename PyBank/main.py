import os
import csv

#creates path for reading raw data
py_bank_path = os.path.join('.','Resources','budget_data.csv')

#dimension variables to store KPIs of raw data
i = 0
sums = 0
change=[]
prev=0

#opens raw data
with open(py_bank_path,'r') as py_bank_csv:
    py_bank_reader = csv.reader(py_bank_csv, delimiter=",")

    #stores header
    py_bank_header = next(py_bank_reader)
    
    #iterates through raw data
    for rows in py_bank_reader:
        #count number of months
        i+=1
        #create running total
        sums+=int(rows[1])
        #creates list of M/M changes
        change.append(int(rows[1])-prev)
        #stores max change
        if int(change[i-1])>=int(max(change)):
            maximum = (f'Greatest Increase in Profits: {rows[0]} ({change[i-1]})')
        #stores min change
        if int(change[i-1])<=int(min(change)):
            minimum = (f'Greatest Decrease in Profits: {rows[0]} ({change[i-1]})')
        prev=int(rows[1])
    #removes first line in change data
    del change[0]       

#prints results to terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {i}')
print(f'Total: ${sums}')
print(f'Average Change: ${round(sum(change)/len(change),2)}')
print(maximum)
print(minimum)

#creates path for output csv
output_path = os.path.join(".",'analysis',"PyBank_Analysis.csv")

#writes all info to output csv
with open(output_path,"w") as analysis_writer:
    py_bank_writer=csv.writer(analysis_writer)
    print("Financial Analysis",file = analysis_writer)
    print("----------------------------",file = analysis_writer)
    print(f'Total Months: {i}',file = analysis_writer)
    print(f'Total: ${sums}',file = analysis_writer)
    print(f'Average Change: ${round(sum(change)/len(change),2)}',file = analysis_writer)
    print(maximum,file = analysis_writer)
    print(minimum,file = analysis_writer)