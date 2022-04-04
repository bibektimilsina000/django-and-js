from django.shortcuts import render

# Create your views here.
def homepaege(request):
    return render(request,'home.html')