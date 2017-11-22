import csv
import psycopg2

#connect to DB
conn = psycopg2.connect("host='ec2-23-21-101-174.compute-1.amazonaws.com' user='rxtgqfxfcogpjk' password='d5644497df9db5ba0662be23d640c1dab93d7bfb4aad01cc23c3061bcb4ba2fa' dbname='d338a782pecr9b'")   
cur=conn.cursor()
 
file1 = open('2016_Matric_Schools_Report.csv')
file2 = open('National Ordinary schools.csv')
csv1 = csv.reader(file1,delimiter=',')
csv2 = csv.reader(file2, delimiter=',')
next(csv1, None)	
next(csv2, None)	
data1 = list(csv1)
data2 = list(csv2)
print(len(data1))
print(len(data2))
num=0

#cur.execute("INSERT INTO matric2016_app (emis,centre_no,name,wrote_2014,passed_2014,wrote_2015,passed_2015,wrote_2016,passed_2016,province) VALUES ('"+data1[0][0]+"','"+data1[0][1]+"','"+data1[0][2]+"','"+data1[0][3]+"','"+data1[0][4]+"','"+data1[0][5]+"','"+data1[0][6]+"','"+data1[0][7]+"','"+data1[0][8]+"','"+data2[0][3]+"')")
#cur.execute("delete from matric2016_app")
#cur.execute("commit")
#cur.execute("SELECT * FROM matric2016_app")

#rows = cur.fetchall()
#print(rows)

for i in range(0,len(data1)):
    for j in range(0,len(data2)):
        if(data1[i][0]==data2[j][0]):
		    #add to table in DB
            cur.execute("INSERT INTO matric2016_app (emis,centre_no,name,wrote_2014,passed_2014,wrote_2015,passed_2015,wrote_2016,passed_2016,province) VALUES ('"+data1[i][0]+"','"+data1[i][1]+"','"+data1[i][2]+"','"+data1[i][3]+"','"+data1[i][4]+"','"+data1[i][5]+"','"+data1[i][6]+"','"+data1[i][7]+"','"+data1[i][8]+"','"+data2[j][3]+"')")
            cur.execute("commit")
            #print((data1[i][0]+" "+data1[i][1]+" "+data1[i][2]+" "+data1[i][3]+" "+data1[i][4]+" "+data1[i][5]+" "+data1[i][6]+" "+data1[i][7]+" "+data1[i][8]+" "+data2[j][3]).encode('utf-8'))
print("All records added successfully!")
conn.close()