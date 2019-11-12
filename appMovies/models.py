from django.db import models

# Create your models here.

class Genero(models.Model):
     # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
     nombre = models.CharField(max_length=50)
     
     def __str__(self):
      return self.nombre

class Pelicula(models.Model):
     # Campo para la relación one-to-many
     genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
     titulo = models.CharField(max_length=40)
     fecha_lanzamiento = models.DateField()
     # Es posible indicar un valor por defecto mediante 'default'
     duracion = models.IntegerField(default=0)
     descripcion = models.TextField()
     portada = models.ImageField()

     def __str__(self):
      return self.nombre

class Director(models.Model):
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     nacionalidad = models.CharField(max_length=50)
     fecha_nacimiento = models.DateField()
     perfil = models.ImageField()
     
     def __str__(self):
      return self.nombre

class Peli_Dir(models.Model):
	 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
	 peliculas = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
	 director = models.ForeignKey(Director, on_delete=models.CASCADE)
	 
	 def __str__(self):
	 	return self.nombre



 
