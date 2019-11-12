from django.contrib import admin
from .models import Genero, Pelicula, Director, Peli_Dir

# Register your models here.


admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Peli_Dir)