from django.shortcuts import render
from django.http import HttpResponse 

def index(request): 
#     return HttpResponse("hello python")
    msg = "Django"
    return render(request,'hellopython.html',{'msg': msg})











# Create your views here.
