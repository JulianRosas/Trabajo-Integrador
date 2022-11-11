from django.db import models

# Create your models here.
class Product(models.Model):
    bar_code=models.CharField("Codigo Barras",max_length=100)
    description=models.CharField("Descripcion",max_length=100)
    price=models.DecimalField("Precio",max_digits=5,decimal_places=2)
    