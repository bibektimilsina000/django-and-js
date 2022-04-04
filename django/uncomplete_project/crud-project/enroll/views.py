from cmath import pi
from turtle import delay
from django.shortcuts import render,HttpResponseRedirect

from enroll.models import User
from . forms import StudentRegistration



def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration
        
        
    else:
        fm = StudentRegistration
    
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})

# Create your views here.

def deletedata(request,id):
    if request.method == 'POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    
# update or edit 

def update_data(request,id):
    return render( request,'enroll/updatestudent.html',{'id':id})
            
