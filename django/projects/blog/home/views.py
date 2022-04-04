
from django.shortcuts import render
from . import models

def index(request):

    post=models.Post.objects.all()
    category=models.Category.objects.all()
    

    context={
        'posts':post,
        'category':category
    }
    print(category)
    print(' ***************** here is it ****************** ')

    
    return render(request,'index.html',context)


def post(request,id):

    category=models.Category.objects.all()
    post =models.Post.objects.get(post_id=id)

    context={
        'posts':post,
        'category':category
    }

    return render(request,'post.html',context)

def category(request,title):



    cat=models.Category.objects.get(title=title)
    post=models.Post.objects.filter(category=cat)
    print("****************** here is it *******************")
    print(post)
    print("****************** here is it *******************")
    context={
        "posts":post
    }

    return render(request,'category.html',context)
