from django.shortcuts import render

#def index(request):
   # return render(request,"index.html")

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def single(request):
    return render(request,'single.html')

def register(request):
   return render(request, 'register.html')