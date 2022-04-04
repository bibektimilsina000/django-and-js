from django.shortcuts import render,redirect
from . models import Employee


def emp_form(request):

    form=Employee()


    return render(request,'index.html',{'form':form})

def emp_list(request):

    return render(request,'emp_form.html')


def emp_delete(request):
    return redirect('home')