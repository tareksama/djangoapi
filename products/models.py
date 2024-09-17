from django.db import models

class Product(models.Model):
    reference = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField(max_length=9)


    def __str__(self) -> str:
        return self.name+' ('+str(self.quantity)+')'

