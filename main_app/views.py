from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book
from .forms import ReadingForm



@login_required
def book_index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html', {'books': books})

@login_required
def all_books(request):
    books = Book.objects.all()
    return render(request, 'books/all_books.html', {'books': books})

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reading_form = ReadingForm()
    return render(request, 'books/detail.html', {
        'book': book, 'reading_form': reading_form})


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['description']

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books/'

@login_required
def add_reading(request, book_id):
    form = ReadingForm(request.POST)
    if form.is_valid():
        new_reading = form.save(commit=False)
        new_reading.book_id = book_id
        new_reading.save()
    return redirect('book-detail', book_id=book_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book-index')
        else:
            error_message = 'Invalid sign up - try again'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)