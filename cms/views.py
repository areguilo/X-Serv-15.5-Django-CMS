from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.
def mainPage(request):
    list = Pages.objects.all()
    response = '<ul><h2>'
    for item in list:
        print(item.name)
        response = response + '<li><a href=http://localhost:8000/' + str(item.name) + ">" + item.name + '</a></li>'
    response = response + '</ul></h2>'
    response = "<h1>Hi!, these are our contents managed:</h1>" + response
    return HttpResponse(response)

def contentPage(request, identifier):
    print ("entra")
    try:
        object = Pages.objects.get(name = identifier)
        response = object.page + '<br><br><a href=http://localhost:8000/> Return to Main menu </a>'
        return HttpResponse(response)
    except Pages.DoesNotExist:
        return HttpResponse("There are not pages for this object")
