from django.db import models

from authors.models import Author

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=200)
    desc=models.CharField(max_length=200,blank=True,null=True)
    price=models.IntegerField(default=0)
    public_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    isbn=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)