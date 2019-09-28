from django.db import models

class Auto(models.Model):
    nombre = models.CharField(max_length= 100)
    precio = models.DecimalField(max_digits= 10, decimal_places= 2)
    color = models.CharField(max_length= 100)
    modelo = models.CharField(max_length= 100)
    img_url = models.TextField()

    def __str__(self):
          return self.nombre