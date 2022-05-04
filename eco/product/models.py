from operator import mod
from pydoc import describe
from string import digits
from turtle import title
from django.db import models

# Create your models here.

class Product(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=20)

    def __str__(self):
        return self.title