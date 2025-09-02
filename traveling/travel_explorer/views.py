from django.shortcuts import render
from django.http import HttpResponse #including a protocol from the local server
from travel_explorer.models import nature    #view name
def travel(request): # Create your views here.
    return HttpResponse(" they are travelers") 
 
def index(request): #create you view
    return render(request,"travel_explorer/index.html") 
                                            
    #model name
def dataview(request):
  a=nature.objects.all()
  dictonary={'res':a} 
  return render(request,"travel_explorer/view.html",dictonary)
                                                             