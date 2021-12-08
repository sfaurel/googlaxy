from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
   
    def __str__(self):
        return self.items_text


class Numerals(models.Model):
    name = models.CharField(max_length=200)
    roman = models.CharField(max_length=1)
   
    def __str__(self):
        return self.numerals_text
    