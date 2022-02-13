from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    category = Category.objects.all().order_by("-Cname")
    context = {
        'category': category,
    }
    return render(request,'pages/index.html',context)

def about(request):
    rusul = Rusul.objects.all()
    hussain = Hussain.objects.all()
    mohammed = Mohammed.objects.all()
    category = Category.objects.all().order_by("-Cname")
    members = Members.objects.all()
    context={
        'rusul':rusul,
        'hussain':hussain,
        'mohammed':mohammed,
        'category': category,
        'members':members,
    }
    
    
    return render(request,'pages/about.html',context)


def category(request):
    category = Category.objects.all().order_by("-Cname")
    project = Project.objects.all().order_by('-date_time')
    context = {
        'all' : project ,
        'category':category,
    }
    return render(request,'pages/category.html' ,context) 


def services(request):
    category = Category.objects.all().order_by("-Cname")
    posts = Posts.objects.all().order_by('-Pdata_time')
    context = {
        'posts':posts,
        'category': category,
    }
    return render(request,'pages/services.html',context)

def details(request,id):
    category = Category.objects.all().order_by("-Cname")
    project=Project.objects.filter(id=id)
    context = {
        'pro':project,
        'category': category,
    }
    return render(request,'pages/details.html' , context)