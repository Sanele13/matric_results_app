from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import matric_app_model
from .serializers import matric2016_serializer

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
    entries = matric_app_model.objects.all()
    content = "<h1>DB content</h1><br>"
    for entry in entries:
        content = content + entry.name + "<br>"