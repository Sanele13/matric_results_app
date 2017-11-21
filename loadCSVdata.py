import csv

with open('file2.csv') as csvfile2:
    csv2 = csv.reader(csvfile2, delimiter=',')
    next(csv2, None)	
with open('file1.csv') as csvfile1:
    csv1 = csv.reader(csvfile1, delimiter=',')
    	
    next(csv1, None)
    
file1 = open('file1.csv')
file2 = open('file2.csv')
csv1 = csv.reader(file1)
csv2 = csv.reader(file2, delimiter=',')
next(csv1, None)	
next(csv2, None)	
data1 = list(csv1)
data2 = list(csv2)
print(len(data1))
for i in range(0,len(data1)):
    for j in range(0,len(data2)):
        print(data1[i][0]+" "+data2[j][1])