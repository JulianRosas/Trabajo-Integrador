from django.contrib import admin

from .models import Autor
from .models import Domicilio
from .models import Genero
from .models import Imprenta
from .models import Libro
from .models import Pais
from .models import Persona
from .models import Tipo_documento

# Register your models here.

admin.site.register(Pais)
admin.site.register(Tipo_documento)
admin.site.register(Domicilio)
admin.site.register(Genero)
admin.site.register(Imprenta)
admin.site.register(Persona)
admin.site.register(Autor)
admin.site.register(Libro)
