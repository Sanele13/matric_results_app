from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#hello world!
def HelloWorld(request):
    text = "<h1>Hello World!</h1>"
    return HttpResponse(text)
