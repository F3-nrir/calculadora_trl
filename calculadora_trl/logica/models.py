from django.db import models

class Modelo(models.Model):
    TIPO_CHOICES = [
        ('trl', 'TRL'),
        ('crl', 'CRL'),
    ]
    nombre = models.TextField(null=False,unique=True,primary_key=True)
    descripcion = models.TextField(null=False)
    tipo = models.CharField(null=False,choices=TIPO_CHOICES,max_length=30,default='TRL')
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
    
    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    numero = models.IntegerField(null=False)
    nombre = models.TextField(null=False)
    descripcion = models.TextField(null=False)
    ptos_necesarios = models.IntegerField(null=False)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'
        
    def __str__(self):
        return str(self.numero)
    
class Pregunta(models.Model):
    numero = models.IntegerField(null=False)
    texto = models.TextField(null=False)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        
    def __str__(self):
        return self.texto
    
class Respuesta(models.Model):
    texto = models.TextField(null=False)
    puntos = models.IntegerField(null=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
    
    def __str__(self):
        return self.texto