from django.db import models

# Create your models here.
class Coin(models.Model):
    charcode = models.CharField(max_length=10, unique=False)
    name = models.CharField(max_length=100, unique=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    
    def __str__(self) -> str:
        return f"{self.charcode} {self.name}"