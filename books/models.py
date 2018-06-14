from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here - Books.

class Book(models.Model):
    title = models.CharField(max_length=254, default='')
    author = models.CharField(max_length=254, default='')
    ISBN = models.CharField(max_length=254, default='')
    date = models.DateTimeField(auto_now_add=False)
    notes = models.TextField()
    image = models.ImageField(upload_to='images')
    owner = models.ForeignKey(User, related_name='books', null=False)
    
    def __str__(self):
        return self.title