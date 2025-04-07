from django.shortcuts import render
from .models import Book





def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def home(request):
    return render(request, 'books/home.html')

def about(request):
    return render(request, 'about.html')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})
