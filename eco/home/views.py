import email
from multiprocessing import context
from tempfile import template
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse

from .form import contactform,LoginForm,RegisterForm

from django.contrib.auth import authenticate,login, get_user_model

def home(request):
    
    context={
        'title':'homepage',
        
    }
    return render(request,'home/home.html',context)

def contact(request):
    form = contactform(request.POST or None)
    context={
        'title':'contactpage',
        'form':form,
    }
    if form.is_valid():
        print(form.cleaned_data)

    # if request.method == 'POST':
    #     print (request.POST)
    #     print(request.POST.get('fullname'))
    return render(request,'contact/contactpage.html',context)


def LOGINPAGE(request):
    form  = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            return redirect('/login') 
        else:
            print("Error")
    return render(request,'registration/loginpage.html',context)
User = get_user_model()
def RegistrationPage(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,'registration/registerpage.html',context)
