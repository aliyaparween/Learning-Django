from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,"about.html")

def features(request):
    return render(request,"features.html")

def contact(request):
    return render(request,"contact.html")
