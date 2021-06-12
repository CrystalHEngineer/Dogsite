from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.IntegerField()
    ingredients = models.TextField()
    sale = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()


class Company(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.IntegerField()
    
