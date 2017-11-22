import csv
    
file1 = open('2016_Matric_Schools_Report.csv')
file2 = open('National Ordinary schools.csv')
csv1 = csv.reader(file1)
csv2 = csv.reader(file2, delimiter=',')
next(csv1, None)	
next(csv2, None)	
data1 = list(csv1)
data2 = list(csv2)
print(len(data1))
print(len(data2))

for i in range(0,len(data1)):
    for j in range(0,len(data2)):
        if(data1[i][0]==data2[j][0]):
            print(data1[i][0]+" "+data2[j][3])