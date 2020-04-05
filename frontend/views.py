from django.shortcuts import render
from django.http import  Http404
from main.models import  Country
from django.views import generic
# Create your views here.
def display(request):
    return render(request,'frontend/home.html')
def details(request,name):
    try:
        qs=Country.objects.get(country_name=name)
        print(qs)
    except Country.DoesNotExist:
        raise  Http404("No MyModel matches the given query")
    return render(request,'frontend/details.html',{'qs':qs})

def About(request):
    template_name='frontend/about.html'
    return render(request,template_name)
