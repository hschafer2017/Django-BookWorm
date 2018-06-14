from django.conf.urls import url
from books.views import add_books

urlpatterns = [
    url(r'^add', add_books, name='books')
    ]
