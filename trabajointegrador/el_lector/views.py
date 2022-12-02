from django.shortcuts import render
from django.db.models import Q
from .models import Autor, Libro, Imprenta


def index_view(request):
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
    libros=Libro.objects.all( )
    queryset = request.GET.get("buscar")
    if queryset:
        libros = Libro.objects.filter(
            Q(titulo = queryset) 
        )
        
        
    return render(request, 'booklist.html',context={"libros":libros}   )


def addbook_view(request):
    autores = Autor.objects.all()
    imprentas = Imprenta.objects.all()

    return render(request, 'addbook.html', context={"autores": autores, "imprentas": imprentas})


def addbook(request):       
    print(f"---{request.POST}---")

    autor = Autor.objects.filter(nro_documento=int(request.POST['id_autor']))
    imprenta = Imprenta.objects.filter(id=int(request.POST['id_imprenta']))

    titulo = request.POST['titulo']
    isbn = request.POST['isbn']
    cant_paginas = request.POST['cant_paginas']
    resena = request.POST['resena']
    id_imprenta = imprenta[0]
    id_autor = autor[0]

    new_libro = Libro(isbn=isbn, titulo=titulo, resena=resena, id_autor=id_autor, id_imprenta=id_imprenta,
                      cant_paginas=cant_paginas
                      )
    new_libro.save()
    return render(request, 'addbook.html')

# isbn = models.IntegerField(primary_key=True)
# titulo = models.CharField("titulo",max_length=30)
# cant_paginas = models.IntegerField("paginas")
# resena = models.CharField("resena",max_length=100)
# id_imprenta = models.ForeignKey(Imprenta, on_delete=models.CASCADE)
# id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
