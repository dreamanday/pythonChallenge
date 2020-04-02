#this is my amazing code for my homework for pyBank section

# import os
# outputPath = os.path.join('budget_data.csv')

import sys
stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")

import csv
with open ('budget_data.csv') as csvfile:
     csvreader = csv.reader(csvfile, delimiter = ',')
     print('Financial Analysis')
     print('----------------------')
     change=[]
     change2=[]
     date=[]

     next(csvreader)
     x=0
     y=0
  
     for row in csvreader:
          x = x+1
          y = y + float(row[1])
          z = float(row[1])
          change.append(z)
          a = str(row[0])
          date.append(a)

     for i in range(x-1):
          q = change[i+1]-change[i]
          change2.append(q)
     avg = sum(change2)/len(change2)

     b = max(change2)

     for i in range(x-1):
          if change2[i] == b:
               c = date[i+1]
          
     d = min(change2)

     for i in range(x-1):
          if change2[i] == d:
               e = date[i+1]

print(f'Total Months: {x}')
print(f'Total: {y}')
print(f'Average Change: {avg}')
print(f'Greatest increase in profits: {c} {b}')
print(f'Greatest decrease in profits: {e} {d}')

print('it is done my friend!')


sys.stdout.close()
sys.stdout=stdoutOrigin

print(f'Total Months: {x}')
print(f'Total: {y}')
print(f'Average Change: {avg}')
print(f'Greatest increase in profits: {c} {b}')
print(f'Greatest decrease in profits: {e} {d}')

print('it is done my friend!')