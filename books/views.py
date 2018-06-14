from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Book
from .forms import BookForm

# Create your views here.
def get_index(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
    else: 
        books = []
    return render(request, 'books/index.html', {'books': books})

def add_books(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            form.save()
            return redirect("/")

    else:
        form = BookForm()
    
    return render(request, 'books/books.html', {'form': form})