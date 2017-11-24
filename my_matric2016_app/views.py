from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import matric_app_model
from .serializers import matric2016_serializer
import csv
import psycopg2

# Create your views here.

#hello world!
def HelloWorld(request):
    text = "<h1>Hello World!</h1>"
    return HttpResponse(text)

class APIView(generics.ListCreateAPIView):
    queryset = matric_app_model.objects.all()
    serializer_class = matric2016_serializer
	
    def perform_create(self, serializer):
        serializer.save()
#connect to DB

def index(request):
    conn = psycopg2.connect("host='ec2-23-21-101-174.compute-1.amazonaws.com' user='rxtgqfxfcogpjk' password='d5644497df9db5ba0662be23d640c1dab93d7bfb4aad01cc23c3061bcb4ba2fa' dbname='d338a782pecr9b'")   
    cur=conn.cursor()
#get number of students who wrote and those who passed, given 'year' and 'province'
    def getData(year,province):
        cur.execute("select wrote_"+year+",passed_"+year+" from test_table where province='"+province+"'")
        rows=cur.fetchall()
        return rows

    def getNumber(year,province):
        cur.execute("select num_wrote,num_passed from "+ province +" where year='"+year+"'")
        rows= cur.fetchall()
        return rows
		
    def num_wrote(data):
        sum=0
        for n in data:
        #print(n[0])
            if(str(n[0])!=''):
                sum+=int(str(n[0]))
            else:
                sum+=0 
        return sum
	
    def num_passed(data):
        sum=0
        for n in data:
        #print(n[0])
            if(str(n[1])!=''):
                sum+=int(str(n[1]))
            else:
                sum+=0 
        return sum
	#Displaying graphs and things
    content = "<html><head><title>Matric Results</title><script src = 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js'></script><link href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u' crossorigin='anonymous'></head><body><h1 style = 'text-align:center'>Matric Results (2014,2015,2016)</h1><br><div class = 'container'><canvas id = 'chart2014'></canvas></div><br><div class = 'container'><canvas id = 'pass_rate2014'></canvas></div><br><div class = 'container'><canvas id = 'chart2015'></canvas></div><br><div class = 'container'><canvas id = 'pass_rate_2015'></canvas></div><br><div class = 'container'><canvas id = 'chart2016'></canvas></div><br><div class = 'container'><canvas id = 'pass_rate_2016'></canvas></div><br><script>var myChart2014 = document.getElementById('chart2014').getContext('2d');var barChart = new Chart(myChart2014, {type: 'bar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GP'],datasets:[{label:'Wrote',data:["+str(getNumber('2014','EC')[0][0])+","+str(getNumber('2014','WC')[0][0])+","+str(getNumber('2014','KZ')[0][0])+","+str(getNumber('2014','LP')[0][0])+","+str(getNumber('2014','NC')[0][0])+","+str(getNumber('2014','NW')[0][0])+","+str(getNumber('2014','FS')[0][0])+","+str(getNumber('2014','MP')[0][0])+","+str(getNumber('2014','GP')[0][0])+"],backgroundColor:'black',},{label:'Passed',data:["+str(getNumber('2014','EC')[0][1])+","+str(getNumber('2014','WC')[0][1])+","+str(getNumber('2014','KZ')[0][1])+","+str(getNumber('2014','LP')[0][1])+","+str(getNumber('2014','NC')[0][1])+","+str(getNumber('2014','NW')[0][1])+","+str(getNumber('2014','FS')[0][1])+","+str(getNumber('2014','MP')[0][1])+","+str(getNumber('2014','GP')[0][1])+"],backgroundColor:'green'},]},options:{title:{display:true, text:'2014 Results',fontSize:20},scales:{xAxes:[{scaleLabel:{display:true,labelString: 'Provinces',fontSize:20}}],yAxes:[{scaleLabel:{display:true,labelString: 'Number of Students',fontSize:20}}]}}})</script><script>var myChart2014h = document.getElementById('pass_rate2014').getContext('2d');var barChart = new Chart(myChart2014h, {type: 'horizontalBar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GP'],datasets:[{label:'Pass Rate (%)',data:["+str((int(getNumber('2014','EC')[0][1])/int(getNumber('2014','EC')[0][0]))*100)+","+str((int(getNumber('2014','WC')[0][1])/int(getNumber('2014','WC')[0][0]))*100)+","+str((int(getNumber('2014','KZ')[0][1])/int(getNumber('2014','KZ')[0][0]))*100)+","+str((int(getNumber('2014','LP')[0][1])/int(getNumber('2014','LP')[0][0]))*100)+","+str((int(getNumber('2014','NC')[0][1])/int(getNumber('2014','NC')[0][0]))*100)+","+str((int(getNumber('2014','NW')[0][1])/int(getNumber('2014','NW')[0][0]))*100)+","+str((int(getNumber('2014','FS')[0][1])/int(getNumber('2014','FS')[0][0]))*100)+","+str((int(getNumber('2014','MP')[0][1])/int(getNumber('2014','MP')[0][0]))*100)+","+str((int(getNumber('2014','GP')[0][1])/int(getNumber('2014','GP')[0][0]))*100)+"],backgroundColor:'green',}]},options:{title:{display:true, text:'2014 Pass Rate',fontSize:20},scales:{xAxes:[{ticks:{beginAtZero:true, min:0}}],yAxes:[{scaleLabel:{display:true,labelString: 'Provinces',fontSize:20}}]}}})</script><script>var myChart2015 = document.getElementById('chart2015').getContext('2d');var barChart = new Chart(myChart2015, {type: 'bar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GP'],datasets:[{label:'Wrote',data:["+str(getNumber('2015','EC')[0][0])+","+str(getNumber('2015','WC')[0][0])+","+str(getNumber('2015','KZ')[0][0])+","+str(getNumber('2015','LP')[0][0])+","+str(getNumber('2015','NC')[0][0])+","+str(getNumber('2015','NW')[0][0])+","+str(getNumber('2015','FS')[0][0])+","+str(getNumber('2015','MP')[0][0])+","+str(getNumber('2015','GP')[0][0])+"],backgroundColor:'black',},{label:'Passed',data:["+str(getNumber('2015','EC')[0][1])+","+str(getNumber('2015','WC')[0][1])+","+str(getNumber('2015','KZ')[0][1])+","+str(getNumber('2015','LP')[0][1])+","+str(getNumber('2015','NC')[0][1])+","+str(getNumber('2015','NW')[0][1])+","+str(getNumber('2015','FS')[0][1])+","+str(getNumber('2015','MP')[0][1])+","+str(getNumber('2015','GP')[0][1])+"],backgroundColor:'green'},]},options:{title:{display:true, text:'2015 Results',fontSize:20},scales:{xAxes:[{scaleLabel:{display:true,labelString: 'Provinces',fontSize:20}}],yAxes:[{scaleLabel:{display:true,labelString: 'Number of Students',fontSize:20}}]}}})</script><script>var myChart2015h = document.getElementById('pass_rate_2015').getContext('2d');var barChart = new Chart(myChart2015h, {type: 'horizontalBar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GP'],datasets:[{label:'Pass Rate (%)',data:["+str((int(getNumber('2015','EC')[0][0])/int(getNumber('2015','EC')[0][1]))*100)+","+str((int(getNumber('2015','WC')[0][0])/int(getNumber('2015','WC')[0][1]))*100)+","+str((int(getNumber('2015','KZ')[0][0])/int(getNumber('2015','KZ')[0][1]))*100)+","+str((int(getNumber('2015','LP')[0][0])/int(getNumber('2015','LP')[0][1]))*100)+","+str((int(getNumber('2015','NC')[0][0])/int(getNumber('2015','NC')[0][1]))*100)+","+str((int(getNumber('2015','NW')[0][0])/int(getNumber('2015','NW')[0][1]))*100)+","+str((int(getNumber('2015','FS')[0][0])/int(getNumber('2015','FS')[0][1]))*100)+","+str((int(getNumber('2015','MP')[0][0])/int(getNumber('2015','MP')[0][1]))*100)+","+str((int(getNumber('2015','GP')[0][0])/int(getNumber('2015','GP')[0][1]))*100)+"],backgroundColor:'green',}]},options:{title:{display:true, text:'2015 Pass Rate',fontSize:20},scales:{xAxes:[{ticks:{beginAtZero:true, min:0}}],yAxes:[{scaleLabel:{display:true,labelString: 'Provinces',fontSize:20}}]}}})</script><script>var myChart2016 = document.getElementById('chart2016').getContext('2d');var barChart = new Chart(myChart2016, {type: 'bar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GP'],datasets:[{label:'Wrote',data:["+str(getNumber('2016','EC')[0][0])+","+str(getNumber('2016','WC')[0][0])+","+str(getNumber('2016','KZ')[0][0])+","+str(getNumber('2016','LP')[0][0])+","+str(getNumber('2016','NC')[0][0])+","+str(getNumber('2016','NW')[0][0])+","+str(getNumber('2016','FS')[0][0])+","+str(getNumber('2016','MP')[0][0])+","+str(getNumber('2016','GP')[0][0])+"],backgroundColor:'black',},{label:'Passed',data:["+str(getNumber('2016','EC')[0][1])+","+str(getNumber('2016','WC')[0][1])+","+str(getNumber('2016','KZ')[0][1])+","+str(getNumber('2016','LP')[0][1])+","+str(getNumber('2016','NC')[0][1])+","+str(getNumber('2016','NW')[0][1])+","+str(getNumber('2016','FS')[0][1])+","+str(getNumber('2016','MP')[0][1])+","+str(getNumber('2016','GP')[0][1])+"],backgroundColor:'green'},]},options:{title:{display:true, text:'2016 Results',fontSize:20},scales:{xAxes:[{scaleLabel:{display:true,labelString: 'Provinces',fontSize:20}}],yAxes:[{scaleLabel:{display:true,labelString: 'Number of Students',fontSize:20}}]}}})</script><script>var myChart2016h = document.getElementById('pass_rate_2016').getContext('2d');var barChart = new Chart(myChart2016h, {type: 'horizontalBar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GP'],datasets:[{label:'Pass Rate (%)',data:["+str((int(getNumber('2016','EC')[0][0])/int(getNumber('2016','EC')[0][1]))*100)+","+str((int(getNumber('2016','WC')[0][0])/int(getNumber('2016','WC')[0][1]))*100)+","+str((int(getNumber('2016','KZ')[0][0])/int(getNumber('2016','KZ')[0][1]))*100)+","+str((int(getNumber('2016','LP')[0][0])/int(getNumber('2016','LP')[0][1]))*100)+","+str((int(getNumber('2016','NC')[0][0])/int(getNumber('2016','NC')[0][1]))*100)+","+str((int(getNumber('2016','NW')[0][0])/int(getNumber('2016','NW')[0][1]))*100)+","+str((int(getNumber('2016','FS')[0][0])/int(getNumber('2016','FS')[0][1]))*100)+","+str((int(getNumber('2016','MP')[0][0])/int(getNumber('2016','MP')[0][1]))*100)+","+str((int(getNumber('2016','GP')[0][0])/int(getNumber('2016','GP')[0][1]))*100)+"],backgroundColor:'green',}]},options:{title:{display:true, text:'2016 Pass Rate',fontSize:20},scales:{xAxes:[{ticks:{beginAtZero:true, min:0}}],yAxes:[{scaleLabel:{display:true,labelString: 'Provinces',fontSize:20}}]}}})</script><p>To View individual school's results: matric2016.heroku.com/schoolData/<school_name><br>NB: Replace spaces with underscores.</p></body></html>"
    end = "</script></body></html>"
	
    conn.close() #close connection
    return HttpResponse(content)
    	
def schoolData(request,schoolName):
    conn = psycopg2.connect("host='ec2-23-21-101-174.compute-1.amazonaws.com' user='rxtgqfxfcogpjk' password='d5644497df9db5ba0662be23d640c1dab93d7bfb4aad01cc23c3061bcb4ba2fa' dbname='d338a782pecr9b'")   
    cur=conn.cursor()
    
    cur.execute("select centre_no,name,wrote_2014,passed_2014,wrote_2015,passed_2015,wrote_2016,passed_2016,province from matric2016_app where upper(name) like upper('%"+schoolName+"%')")
    rows= cur.fetchall()
    htmlContent="<table><tr><th>centre_no</th><th>name</th><th>wrote_2014</th><th>passed_2014</th><th>wrote_2015</th><th>passed_2015</th><th>wrote_2016</th><th>passed_2016</th><th>province</th></tr>"
    data = list(rows)	
    for i in range(0,len(data)):
        htmlContent+="<tr><td>"+data[i][0]+"</td><td>"+data[i][1]+"</td><td>"+data[i][2]+"</td><td>"+data[i][3]+"</td><td>"+data[i][4]+"</td><td>"+data[i][5]+"</td><td>"+data[i][6]+"</td><td>"+data[i][7]+"</td><td>"+data[i][8]+"</td></tr>"
    htmlContent+="<table>"
    conn.close()
    return HttpResponse(htmlContent)
