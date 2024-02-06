from django.db import models

class Material(models.Model):
    descripcion = models.CharField(max_length=200)
    serie_modelo = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio_individual = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion, self.serie_modelo, self.cantidad, self.precio_individual, self.precio_total
