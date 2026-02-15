from django.db import models

# Create your models here.



class Author(models.Model):
    name=models.CharField(max_length=200)
    biography=models.CharField(max_length=200)
    birth_date=models.DateField()
    nationality=models.CharField(max_length=200)