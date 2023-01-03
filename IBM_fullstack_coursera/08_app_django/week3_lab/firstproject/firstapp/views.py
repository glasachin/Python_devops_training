from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

def index(request):
    template = "<html>" \
                "Hi, This is Sachin Sharma."\
                "</html>"
    
    return HttpResponse(content=template)

def current_date(request):
    today = date.today()
    template = "<html>" \
                "Todays Date is {}"\
                "</html>".format(today)
    
    return HttpResponse(content=template)