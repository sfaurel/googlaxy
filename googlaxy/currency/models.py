from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Numerals(models.Model):
    name = models.CharField(max_length=200, unique=True)
    roman = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.name
