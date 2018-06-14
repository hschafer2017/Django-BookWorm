from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm

# Create your views here.
def get_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = BookForm()
    
    return render(request, 'books/books.html', {'form': form})