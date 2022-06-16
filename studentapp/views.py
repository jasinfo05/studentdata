from logging import warning
from msilib import sequence
from msilib.schema import Class
from multiprocessing import context
from tokenize import Name
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from . models import candidate

def home(request):
    
    Admission_No = ""

    #execute while method is POST
    if request.method=='POST':
        name=request.POST['sname']
        dob=request.POST['sdob']
        batch=request.POST['class']
        div=request.POST['division']
        gen=request.POST['gender']

        #if the student already exist it will return the form with an warning message.
        if candidate.objects.filter(Name=name).exists():
            warnmsg="This candidate already exist!"
            return render(request,'home.html',{'WMSG':warnmsg})

        #if it is a new student then an unique admission number will be created. 
        else:

            #generating unique admission numbers by string formatting.
            adno=["R-{0:03}".format(num) for num in range(1,100)]
            for number in adno:
                if candidate.objects.filter(Admission_No=number).exists():
                    continue
                Admission_No=number
                admn=Admission_No

                #new student object is created and saved to database.
                student=candidate.objects.create(Name=name,DOB=dob,Class=batch,Division=div,Gender=gen,Admission_No=admn)
                student.save();


                #fetching all objects and sending jinja texts to the html page.
                stud = candidate.objects.all()
                jinjatext = {
                    'NAME':name,
                    'Dob':dob,
                    'Batch':batch,
                    'Div':div,
                    'Gen':gen,
                    'AdNo':admn,
                    'std':stud,
                }
                return render(request,'home.html',jinjatext)
                
    #executes when method is default.           
    else:
        return render(request,'home.html')

