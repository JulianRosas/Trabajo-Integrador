from django.db import models


# Create your models here.
class Pais(models.Model):
    nombre = models.CharField("nombre", max_length=30)
    descripcion = models.CharField("descripcion", max_length=30)

    def __str__(self):
        return self.nombre


class Tipo_documento(models.Model):
    nombre = models.CharField("nombre", max_length=15)
    descripcion = models.CharField("descripcion", max_length=30)

    def __str__(self):
        return self.nombre


class Domicilio(models.Model):
    calle = models.CharField("calle", max_length=15)
    altura = models.IntegerField("altura")
    localidad = models.CharField("localidad", max_length=20)
    piso = models.IntegerField("piso")

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.calle, self.altura)


class Genero(models.Model):
    nombre = models.CharField("nombre", max_length=15)
    descripcion = models.CharField("descripcion", max_length=30)

    def __str__(self):
        return self.nombre


class Imprenta(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField("nombre", max_length=15)
    telefono = models.IntegerField
    sitio_web = models.URLField("web", max_length=40)
    email = models.EmailField("email", max_length=20)  # hay una clase email
    id_domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField("nombre", max_length=30)
    apellido = models.CharField("apellido", max_length=30)
    telefono = models.IntegerField
    id_domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    id_tipo_documento = models.ForeignKey(Tipo_documento, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.nombre, self.apellido)


class Autor(models.Model):
    nro_documento = models.IntegerField(primary_key=True)
    apellido = models.CharField("apellido", max_length=20)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.apellido


class Libro(models.Model):
    isbn = models.IntegerField(primary_key=True)
    titulo = models.CharField("titulo", max_length=30)
    cant_paginas = models.IntegerField("paginas")
    resena = models.CharField("resena", max_length=100)
    id_imprenta = models.ForeignKey(Imprenta, on_delete=models.CASCADE)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
