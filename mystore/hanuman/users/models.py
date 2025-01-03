from django.db import models

# Create your models here.
class users(models.Model):
    email=models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
class person(models.Model):
    first_name=models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
'''class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_palces=2)'''
                                   
