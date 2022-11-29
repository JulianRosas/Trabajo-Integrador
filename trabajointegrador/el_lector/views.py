from django.shortcuts import render

#def index(request):
   # return render(request,"index.html")

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def addbook(request):
    return render(request,'addbook.html')

def login(request):
   return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def books(request):
    return render(request, 'books.html')

def booklist(request):
    return render(request, 'booklist.html')