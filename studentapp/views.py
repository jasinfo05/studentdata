from logging import warning
from tokenize import Name
from django.shortcuts import render
from django.http import HttpResponse

from studentapp.models import candidate

def home(request):
    if request.method=='POST':
        name=request.POST['studentname']
        dob=request.POST['dob']
        batch=request.POST['class']
        div=request.POST['division']
        gen=request.POST['gender']


    else:
        return render(request,'home.html')
