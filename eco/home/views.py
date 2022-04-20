from multiprocessing import context
from tempfile import template
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    context={
        'title':'homepage',
        'description':'this is a home page aaaanu'
    }
    return render(request,'home/home.html',context)

def contact(request):
    context={
        'title':'contactpage',
    }
    if request.method == 'POST':
        print (request.POST)
        print(request.POST.get('fullname'))
    return render(request,'contact/contactpage.html',context)