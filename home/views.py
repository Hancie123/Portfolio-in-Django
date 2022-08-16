from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Contact

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method=='POST':

        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        message=request.POST['message']

        ins = Contact(name=name, email=email, mobile=mobile, message=message)
        ins.save()
        print("The data is save in db")
        
    return render(request, 'contact.html')
