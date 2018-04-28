from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.
def mainPage(request):
    list = Pages.objects.all()
    req = '<ul>'
    for item in list:
        req = req + '<li><a ref=' + item.name + '</a>'
    req = req + '</ul>'
    return HttpResponse("<h1>Hi!, these are our contents managed:</h1>" + req)

def contentPage(request, identifier):
    print ("entra")
    try:
        object = Pages.objects.get(name = identifier)
        return HttpResponse(object.page)
    except Pages.DoesNotExist:
        return HttpResponse("There are not pages for this object")
