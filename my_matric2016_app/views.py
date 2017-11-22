from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import matric_app_model
from .serializers import matric2016_serializer
import csv

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

def index(request):
    #read and display DB content
    
	#get every DB entry
    #entries = matric_app_model.objects.all()
    head = "<html><head><title>Matric Results</title><script src = 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js'></script><link href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u' crossorigin='anonymous'></head>"
    body = "<body><div style = 'width:40%;height:40%'><canvas id = 'chart'></canvas></div><script>var myChart = document.getElementById('chart').getContext('2d');var barChart = new Chart(myChart, {type: 'bar',data:{labels:['EC','WC','KZ','LP','NC','NW','FS','MP','GA'],"
    datasets="datasets:[{label:'Wrote',data:[70,80,74,95,82,49,78,92,68],backgroundColor:'black',},{label:'Passed',data:[60,70,52,81,69,49,43,58,49],backgroundColor:'green'},]},"
    rest ="options:{scales:{xAxes:[{scaleLabel:{display:true,labelString: 'Provinces'}}],yAxes:[{scaleLabel:{display:true,labelString: 'Number of Students'}}]}}})</script></body></html>"
	
    content = head+body+datasets+rest
    #for entry in entries:
    #    content = content + entry.name + "<br>"
    return HttpResponse(content)

def loadCSVdata(request):
    with open('2016_Matric_Schools_Report.csv') as csvfile:
        CSVfile = csv.reader(csvfile, delimiter = ',')
        #print(CSVfile)
    
        next(CSVfile, None) #ignore header
        #save rows to DB
        data = ""
        for row in CSVfile:
		#Save to database
            model = matric_app_model()
            model.emis = row[0]
            model.centre_no = row[1]
            model.name = row[2]
            model.wrote_2014 = row[3]
            model.passed_2014 = row[4]
            model.wrote_2015 = row[5]
            model.passed_2015 = row[6]
            model.wrote_2016 = row[7]
            model.passed_2016 = row[8]
            model.save()
            #cur.execute("INSERT INTO matric2016_app (emis,centre_no,name,wrote_2014,passed_2014,wrote_2015,passed_2015,wrote_2016,passed_2016) VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"','"+row[7]+"','"+row[8]+"')")
        return HttpResponse("Done!")