from django.db import models
from datetime import datetime
# Create your models here - Books.

class Book(models.Model):
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    ISBN = models.CharField(max_length=254, default='')
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField
    

    def __str__(self):
        return self.name