from logging import warning
from tokenize import Name
from django.shortcuts import render
from django.http import HttpResponse
from . models import candidate

def home(request):
    Admission_No = ""
    if request.method=='POST':
        name=request.POST['studentname']
        dob=request.POST['dob']
        batch=request.POST['class']
        div=request.POST['division']
        gen=request.POST['gender']

        if candidate.objects.filter(Name=name,DOB=dob,Class=batch,Division=div,Gender=gen).exists():
            warnmsg="This candidate already exists!"
            return render(request,'home.html',{'WMSG':warnmsg})
        else:
            adno=["R-{0:03}".format(num) for num in range(1,100)]
            for number in adno:
                if number!=Admission_No:
                    Admission_No=number
                    admn_no=Admission_No
                    student=candidate.objects.create(Name=name,DOB=dob,Class=batch,Division=div,Gender=gen,Admission_No=admn_no)
                    student.save();
                    jinjatext = {
                        'NAME':name,
                        'Dob':dob,
                        'Batch':batch,
                        'Div':div,
                        'Gen':gen,
                        'AdNo':admn_no,
                    }
                    return render(request,'responsepage.html')
    else:
        return render(request,'home.html')