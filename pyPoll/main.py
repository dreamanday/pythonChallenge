
import os
outputPath = os.path.join('pythonChallenge','pyPoll', 'Resources', 'election_data.csv')

import sys
stdoutOrigin=sys.stdout 
sys.stdout = open("log2.txt", "w")

import csv
with open (outputPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    print('Election Results')
    print('----------------')

    next(csvreader)
    x=0
    khan=0
    correy=0
    li=0
    tooley=0

    for row in csvreader:
        x = x + 1
        if row[2] == 'Khan':
            khan = khan + 1
        if row[2] == 'Correy':
            correy = correy + 1
        if row[2] == 'Li':
            li = li + 1
        if row[2] == "O'Tooley":
            tooley = tooley +1
        
    y = max(khan,correy,li,tooley)

    if y == khan:
        a = 'Khan'
    if y == correy:
        a = 'Correy'
    if y == li:
        a = 'Li'
    if y == tooley:
        a = "O'Tooley"


    print(f'Total Votes: {x}')
    print('------------------')
    print(f'Khan: {round(((khan/x)*100),2)} % ({khan})')
    print(f'Correy: {round(((correy/x)*100),2)} % ({correy})')
    print(f'Li: {round(((li/x)*100),2)} % ({li})')
    print(f"O'Tooley: {round(((tooley/x)*100),2)} % ({tooley})")
    print('------------------')
    print(f'Winner: {a}')
    print('-------------------')

sys.stdout.close()
sys.stdout=stdoutOrigin

print(f'Total Votes: {x}')
print('------------------')
print(f'Khan: {round(((khan/x)*100),2)} % ({khan})')
print(f'Correy: {round(((correy/x)*100),2)} % ({correy})')
print(f'Li: {round(((li/x)*100),2)} % ({li})')
print(f"O'Tooley: {round(((tooley/x)*100),2)} % ({tooley})")
print('------------------')
print(f'Winner: {a}')
print('-------------------')