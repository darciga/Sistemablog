from django.db import models

# Create your models here.
class Blog(models.Model):
	nombre = models.CharField(max_length=100)
	etiqueta = models.TextField()

	def __unicode__(self):
		return self.nombre
class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	email = models.EmailField()

	def __unicode__(self):
		return self.nombre
class Entrada(models.Model):
	"""docstring for Entrada"""
	blog = models.ForeignKey(Blog)
	titulo = models.CharField(max_length=255)
	cuerpo_texto = models.TextField()
	fecha_publicacion = models.DateField()
	mod_date = models.DateField()
	autor = models.ManyToManyField(Autor)
	n_comentarios = models.IntegerField()

	def __unicode__(self):
		return self.titulo
		
		
