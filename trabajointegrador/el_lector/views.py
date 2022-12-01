from django.shortcuts import render
from .models import Pais
from .models import Libro
from .models import Imprenta
from .models import Autor
# def index(request):
# return render(request,"index.html")


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def addbook(request):
    return render(request, 'addbook.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def books(request):
    return render(request, 'books.html')


def booklist(request):
    return render(request, 'booklist.html')


def addbook_view(request):
    autores = Autor.objects.all()
    imprentas = Imprenta.objects.all()

       
       

    return render(request, 'addbook.html', context={"autores": autores, "imprentas": imprentas})


def addbook(request):
    autores = Autor.objects.all()
    imprentas = Imprenta.objects.all()
    print(f"---{request.POST}---")


    autor = Autor.objects.filter( nro_documento=int(request.POST['id_autor']))
    imprenta = Imprenta.objects.filter(id=int(request.POST['id_imprenta']))

    titulo = request.POST['titulo']
    isbn = request.POST['isbn']
    cant_paginas = request.POST['cant_paginas']
    resena = request.POST['resena']
    id_imprenta = imprenta[0]
    id_autor = autor[0]

    new_libro = Libro(isbn=isbn, titulo=titulo, resena=resena, id_autor=id_autor, id_imprenta=id_imprenta, cant_paginas=cant_paginas
                      )
    new_libro.save()
    return render(request,'success.html',context={"autores": autores, "imprentas": imprentas})


#isbn = models.IntegerField(primary_key=True)
    # titulo = models.CharField("titulo",max_length=30)
    # cant_paginas = models.IntegerField("paginas")
    # resena = models.CharField("resena",max_length=100)
    # id_imprenta = models.ForeignKey(Imprenta, on_delete=models.CASCADE)
    # id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
