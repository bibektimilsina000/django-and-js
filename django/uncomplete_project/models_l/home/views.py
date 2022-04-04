from django.shortcuts import render,redirect
from . models import Album,Song

def index (request):
    album=Album.objects.all()
    context={
        'albums':album


    }
    return render(request,'index.html',context)


# Create your views here.
