from django.db import models

class Pregunta(models.Model):
    pregunta_txt = models.CharField(max_length=200)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.pregunta_txt
class Opcion(models.Model):
    opcion_txt = models.CharField(max_length=200)
    punto = models.IntegerField(default=0)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    def __str__(self):
        return self.opcion_txt

class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    
    def __str__(self):
        return self.nombre

class Nota(models.Model):
    nota = models.IntegerField(default=0)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nota