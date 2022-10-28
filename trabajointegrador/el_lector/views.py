from django.shortcuts import render

#def index(request):
   # return render(request,"index.html")

def index(request):
    return render(request,'el_lector/index.html')