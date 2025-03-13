
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()  
    genres = models.ManyToManyField(Genre)  
    borrowed_by = models.CharField(max_length=100, blank=True, null=True) 
    borrow_date = models.DateTimeField(blank=True, null=True)  

    def __str__(self):
        return self.title
