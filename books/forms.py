from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BookForm(ModelForm):
   class Meta: 
       model = Book
       fields = ['title', 'author', 'ISBN', 'date', 'notes', 'image' ]