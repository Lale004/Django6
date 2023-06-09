from django.db import models

class Blog(models.Model):
    author=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    content=models.TextField()

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()

    def __str__(self):
         return self.name
# Create your models here.

