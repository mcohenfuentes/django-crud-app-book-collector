from django.shortcuts import render



class Book:
    def __init__(self, title, author, genre, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description

books = [
    Book('Pride and Prejudice', 'Jane Austen', 'Fiction', 'A classic. Timeless love story.'),
    Book('Bunny', 'Mona Awad', 'Fiction', 'Very unreliable narrator.'),
    Book('Braiding Sweetgrass', 'Robin', 'Nonfiction', 'Beautiful prose about humans relationship with nature.'),
]


def book_index(request):
    return render(request, 'books/index.html', {'books': books})

def home(request):
    return render(request, 'books/home.html')

def about(request):
    return render(request, 'about.html')

